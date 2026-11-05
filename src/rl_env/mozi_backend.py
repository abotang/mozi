"""Live Mozi backend. Only the selected side's units and contacts are observable."""

from __future__ import annotations

import math
import time

from src.mozi_api.config import BLUE_SIDE_NAME
from src.mozi_api.connector import MoziConnector


class CommandRejected(RuntimeError):
    def __init__(self, message: str, completed: list[dict]):
        super().__init__(message)
        self.completed = completed


def _number(value):
    if value is None or isinstance(value, bool):
        return None
    try:
        number = float(value)
        return number if math.isfinite(number) else None
    except (TypeError, ValueError):
        return None


def _unit(raw: dict, *, parked: bool = False) -> dict:
    return {"id": str(raw.get("id", "")), "name": raw.get("name", ""),
            "type": raw.get("UnitType", ""), "sub_type": raw.get("subType", ""),
            "lat": _number(raw.get("Latitude")), "lon": _number(raw.get("Longitude")),
            "altitude_m": _number(raw.get("CA")), "speed_kmh": _number(raw.get("CurrentSpeed")),
            "heading_deg": _number(raw.get("heading")), "damage": _number(raw.get("Damage")),
            "fuel": _number(raw.get("FuelRec")), "parked": parked}


def _contact(raw: dict) -> dict:
    return {"id": str(raw.get("id", "")), "name": raw.get("name", ""),
            "type": raw.get("UnitType", ""), "sub_type": raw.get("subType", ""),
            "side_color": raw.get("SideColor"),
            "lat": _number(raw.get("Latitude", raw.get("lat"))),
            "lon": _number(raw.get("Longitude", raw.get("lon"))),
            "altitude_m": _number(raw.get("CA")),
            "speed_kmh": _number(raw.get("CurrentSpeed")),
            "heading_deg": _number(raw.get("heading"))}


def _heading_waypoint(lat: float, lon: float, heading_deg: float, distance_km: float) -> dict:
    radius_km = 6371.0
    angular = distance_km / radius_km
    lat_r, lon_r, bearing = map(math.radians, (lat, lon, heading_deg))
    dest_lat = math.asin(math.sin(lat_r) * math.cos(angular)
                         + math.cos(lat_r) * math.sin(angular) * math.cos(bearing))
    dest_lon = lon_r + math.atan2(math.sin(bearing) * math.sin(angular) * math.cos(lat_r),
                                  math.cos(angular) - math.sin(lat_r) * math.sin(dest_lat))
    return {"lat": math.degrees(dest_lat), "lon": (math.degrees(dest_lon) + 540) % 360 - 180}


class MoziBackend:
    def __init__(self, connector: MoziConnector | None = None, *, side_name: str = BLUE_SIDE_NAME,
                 wall_timeout_sec: float = 120.0, reset_timeout_sec: float = 90.0,
                 reset_max_elapsed_sec: float = 30.0, include_weapon_status: bool = False):
        if not isinstance(side_name, str) or not side_name.strip():
            raise ValueError("side_name 必须明确指定")
        if any(not math.isfinite(x) or x <= 0 for x in
               (wall_timeout_sec, reset_timeout_sec, reset_max_elapsed_sec)):
            raise ValueError("超时和重置时间阈值必须为有限正数")
        self.connector = connector or MoziConnector()
        self.side_name = side_name.strip()
        self.wall_timeout_sec = wall_timeout_sec
        self.reset_timeout_sec = reset_timeout_sec
        self.reset_max_elapsed_sec = reset_max_elapsed_sec
        if not isinstance(include_weapon_status, bool):
            raise ValueError("include_weapon_status 必须是布尔值")
        self.include_weapon_status = include_weapon_status
        self._unit_positions: dict[str, tuple[float, float]] = {}

    def _side(self, data: dict) -> dict:
        sides = data.get("side", [])
        matches = [side for side in sides if isinstance(side, dict)
                   and side.get("name") == self.side_name]
        if not matches:
            matches = [side for side in sides if isinstance(side, dict)
                       and self.side_name in str(side.get("name", ""))]
        if len(matches) != 1:
            raise RuntimeError(f"想定中无法唯一确定阵营 {self.side_name!r}")
        return matches[0]

    def observe(self) -> dict:
        with self.connector.consistent_read() as frame:
            data = self.connector.get_full_state()
            if not isinstance(data, dict):
                raise RuntimeError("墨子尚无可用态势帧")
            side = self._side(data)
            own = [_unit(raw) for raw in side.get("activeUnits", [])
                   if isinstance(raw, dict) and raw.get("id")
                   and raw.get("UnitType") not in {"Weapon", "武器", "Missile", "导弹"}]
            known = {unit["id"] for unit in own}
            for group in data.get("FightTree", []):
                if not isinstance(group, dict) or group.get("SideID") != side.get("id"):
                    continue
                for raw in group.get("FightTree", []):
                    if (isinstance(raw, dict) and raw.get("AirCraftInFacility") is True
                            and raw.get("id") and raw["id"] not in known):
                        own.append(_unit(raw, parked=True))
                        known.add(raw["id"])
            contacts = [_contact(raw) for raw in side.get("contacts", [])
                        if isinstance(raw, dict) and raw.get("id")]
            observation = {"schema_version": 1, "scenario_name": data.get("ScenarioName", ""),
                           "side_name": self.side_name, "frame_seq": frame["sequence"],
                           "units": sorted(own, key=lambda x: x["id"]),
                           "contacts": sorted(contacts, key=lambda x: x["id"])}
        self._unit_positions = {unit["id"]: (unit["lat"], unit["lon"])
                                for unit in observation["units"]
                                if unit["lat"] is not None and unit["lon"] is not None}
        if self.include_weapon_status:
            observation["weapon_status_by_unit"] = {
                unit["id"]: self.connector.get_weapon_status(unit["id"])
                for unit in observation["units"] if unit["type"] in {"Aircraft", "飞机"}
            }
        sim_time = self.connector.get_scenario_elapsed_seconds()
        if sim_time is None or not math.isfinite(sim_time):
            raise RuntimeError("无法读取墨子游戏时钟 GetScenarioTime")
        observation["sim_time_sec"] = float(sim_time)
        return observation

    def reset(self, scenario_name: str) -> dict:
        if not self.connector.is_connected() and not self.connector.connect():
            raise RuntimeError("墨子 WS 连接失败")
        sequence = self.connector.get_update_sequence()
        response = self.connector.load_scenario(scenario_name)
        returned_name = response.get("data", {}).get("scenarioName") if isinstance(response.get("data"), dict) else None
        accepted_names = {scenario_name, returned_name}
        deadline = time.monotonic() + self.reset_timeout_sec
        while time.monotonic() < deadline:
            next_seq = self.connector.wait_for_new_update(sequence, timeout=min(1.0, max(0.0, deadline-time.monotonic())))
            if next_seq is None:
                continue
            sequence = next_seq
            if self.connector.get_scenario_name() not in accepted_names:
                continue
            observation = self.observe()
            if observation["sim_time_sec"] <= self.reset_max_elapsed_sec:
                self.connector.start_simulation()
                return observation
        raise TimeoutError("加载想定后未观察到同名想定的初始态势与游戏时间；重置未确认")

    def apply_actions(self, actions: list[dict]) -> list[dict]:
        completed = []
        for action in actions:
            kind, unit_id = action["type"], action["unit_id"]
            if kind == "takeoff":
                result = self.connector.takeoff(unit_id)
            elif kind == "course":
                result = self.connector.set_course(unit_id, [
                    {"lat": p["lat"], "lon": p["lon"]} for p in action["waypoints"]])
            elif kind == "heading":
                if unit_id not in self._unit_positions:
                    raise CommandRejected(f"{unit_id} 无可用位置，不能换算航向动作", completed)
                lat, lon = self._unit_positions[unit_id]
                result = self.connector.set_course(unit_id, [
                    _heading_waypoint(lat, lon, action["heading_deg"], action["distance_km"])])
            elif kind == "speed":
                result = self.connector.set_speed(unit_id, action["speed_kmh"])
            elif kind == "altitude":
                result = self.connector.set_altitude(unit_id, action["altitude_m"])
            elif kind == "radar":
                result = self.connector.set_radar(unit_id, action["enabled"])
            elif kind == "weapon_control":
                result = self.connector.set_weapon_control(unit_id, mode=action["surface_mode"],
                                                           air_mode=action["air_mode"])
            elif kind == "weapon_assignment":
                result = self.connector.weapon_assignment(unit_id, action["weapon_dbid"],
                                                          target_guid=action["target_id"], count=action["count"])
            else:
                raise ValueError(f"不支持的动作：{kind}")
            accepted = (result is True or isinstance(result, dict) and result.get("code") in (0, "0"))
            completed.append({"action": action, "accepted": accepted})
            if not accepted:
                raise CommandRejected(f"墨子未接受 {kind} 动作；之前已接受 {len(completed)-1} 条，不能自动回滚或重试",
                                      completed)
        return completed

    def advance(self, frames: int) -> dict:
        if isinstance(frames, bool) or not isinstance(frames, int) or frames <= 0:
            raise ValueError("frames 必须是正整数")
        sequence = self.connector.get_update_sequence()
        target = sequence + frames
        deadline = time.monotonic() + self.wall_timeout_sec
        while time.monotonic() < deadline:
            received = self.connector.wait_for_new_update(
                sequence, timeout=min(1.0, max(0.0, deadline-time.monotonic())))
            if received is None:
                continue
            sequence = received
            if sequence >= target:
                return self.observe()
        raise TimeoutError("等待墨子实时态势帧超时；本轮不可作为训练样本")

    def close(self) -> None:
        self.connector.close()
