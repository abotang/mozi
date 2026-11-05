"""Gymnasium-style episode contract, independent of Agent and behavior trees."""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Any, Callable, Protocol


class EnvironmentBackend(Protocol):
    def reset(self, scenario_name: str) -> dict: ...
    def apply_actions(self, actions: list[dict]) -> list[dict]: ...
    def advance(self, frames: int) -> dict: ...
    def close(self) -> None: ...


RewardFunction = Callable[[dict, list[dict], dict, dict], tuple[float, dict]]
TerminalFunction = Callable[[dict, dict], bool]


@dataclass(frozen=True)
class EnvironmentConfig:
    scenario_name: str
    frames_per_step: int = 1
    episode_duration_sec: float = 3600.0
    max_steps: int | None = None

    def __post_init__(self):
        if not isinstance(self.scenario_name, str) or not self.scenario_name.strip():
            raise ValueError("scenario_name 必须是非空字符串")
        if isinstance(self.frames_per_step, bool) or not isinstance(self.frames_per_step, int) or self.frames_per_step <= 0:
            raise ValueError("frames_per_step 必须是正整数")
        for name in ("episode_duration_sec",):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
                raise ValueError(f"{name} 必须是有限正数")
        if self.max_steps is not None and (isinstance(self.max_steps, bool)
                                           or not isinstance(self.max_steps, int) or self.max_steps <= 0):
            raise ValueError("max_steps 必须是正整数")


def _finite_number(value: Any, name: str, low: float, high: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} 必须是数字")
    number = float(value)
    if not math.isfinite(number) or not low <= number <= high:
        raise ValueError(f"{name} 必须在 {low}～{high} 之间")
    return number


def validate_actions(action: dict | list[dict] | None, observation: dict) -> list[dict]:
    """Validate the complete batch before sending any command to the simulator."""
    if action is None:
        return []
    batch = [action] if isinstance(action, dict) else action
    if not isinstance(batch, list):
        raise ValueError("action 必须是动作对象、动作列表或 None")
    own_units = {unit["id"]: unit for unit in observation.get("units", [])}
    own_ids = set(own_units)
    contact_ids = {contact["id"] for contact in observation.get("contacts", [])}
    valid_types = {"takeoff", "course", "heading", "speed", "altitude", "radar",
                   "weapon_control", "weapon_assignment"}
    validated = []
    for index, item in enumerate(batch):
        if not isinstance(item, dict):
            raise ValueError(f"动作 {index} 必须是对象")
        kind, unit_id = item.get("type"), item.get("unit_id")
        if kind not in valid_types:
            raise ValueError(f"动作 {index} 类型无效：{kind}")
        if not isinstance(unit_id, str) or unit_id not in own_ids:
            raise ValueError(f"动作 {index} 的 unit_id 不属于当前己方单位")
        allowed = {"type", "unit_id"}
        if kind == "course":
            points = item.get("waypoints")
            if not isinstance(points, list) or not 1 <= len(points) <= 32:
                raise ValueError("course.waypoints 必须包含 1～32 个航路点")
            clean_points = []
            for point in points:
                if not isinstance(point, dict) or set(point) != {"lat", "lon"}:
                    raise ValueError("航路点只能包含 lat、lon")
                clean_points.append({"lat": _finite_number(point["lat"], "lat", -90, 90),
                                     "lon": _finite_number(point["lon"], "lon", -180, 180)})
            allowed.add("waypoints")
        elif kind == "heading":
            heading = _finite_number(item.get("heading_deg"), "heading_deg", 0, 360)
            distance = _finite_number(item.get("distance_km"), "distance_km", 0.1, 1000)
            if own_units[unit_id].get("lat") is None or own_units[unit_id].get("lon") is None:
                raise ValueError("heading 动作需要当前单位的有效位置")
            allowed.update({"heading_deg", "distance_km"})
        elif kind == "speed":
            speed = _finite_number(item.get("speed_kmh"), "speed_kmh", 0, 4000)
            allowed.add("speed_kmh")
        elif kind == "altitude":
            altitude = _finite_number(item.get("altitude_m"), "altitude_m", 0, 30000)
            allowed.add("altitude_m")
        elif kind == "radar":
            if not isinstance(item.get("enabled"), bool):
                raise ValueError("radar.enabled 必须是布尔值")
            allowed.add("enabled")
        elif kind == "weapon_control":
            if item.get("air_mode") not in {"Hold", "Tight", "Free"}:
                raise ValueError("air_mode 必须是 Hold、Tight 或 Free")
            if item.get("surface_mode", "Hold") not in {"Hold", "Tight", "Free"}:
                raise ValueError("surface_mode 必须是 Hold、Tight 或 Free")
            allowed.update({"air_mode", "surface_mode"})
        elif kind == "weapon_assignment":
            if not isinstance(item.get("target_id"), str) or item["target_id"] not in contact_ids:
                raise ValueError("target_id 必须是当前己方已探测接触目标")
            if not isinstance(item.get("weapon_dbid"), (str, int)) or not str(item["weapon_dbid"]).isdigit():
                raise ValueError("weapon_dbid 必须是数字编号")
            count = item.get("count", 1)
            if isinstance(count, bool) or not isinstance(count, int) or not 1 <= count <= 100:
                raise ValueError("count 必须是 1～100 的整数")
            allowed.update({"target_id", "weapon_dbid", "count"})
        if set(item) - allowed:
            raise ValueError(f"动作 {index} 包含未知字段：{sorted(set(item) - allowed)}")
        clean = {"type": kind, "unit_id": unit_id}
        if kind == "course": clean["waypoints"] = clean_points
        elif kind == "heading": clean.update(heading_deg=heading, distance_km=distance)
        elif kind == "speed": clean["speed_kmh"] = speed
        elif kind == "altitude": clean["altitude_m"] = altitude
        elif kind == "radar": clean["enabled"] = item["enabled"]
        elif kind == "weapon_control":
            clean.update(air_mode=item["air_mode"], surface_mode=item.get("surface_mode", "Hold"))
        elif kind == "weapon_assignment":
            clean.update(target_id=item["target_id"], weapon_dbid=str(item["weapon_dbid"]), count=count)
        validated.append(clean)
    return validated


class MoziRLEnv:
    """One exclusive simulator session; reset/step return Gymnasium's five values."""

    def __init__(self, backend: EnvironmentBackend, config: EnvironmentConfig,
                 reward_fn: RewardFunction | None = None,
                 terminal_fn: TerminalFunction | None = None):
        from .rewards import ZeroReward
        self.backend = backend
        self.config = config
        self.reward_fn = reward_fn or ZeroReward()
        self.terminal_fn = terminal_fn
        self._observation: dict | None = None
        self._start_time = 0.0
        self._steps = 0
        self._finished = False

    def reset(self, *, seed: int | None = None, options: dict | None = None) -> tuple[dict, dict]:
        if options:
            raise ValueError("此环境暂不支持 reset options；想定由 EnvironmentConfig 指定")
        if seed is not None and (isinstance(seed, bool) or not isinstance(seed, int)):
            raise ValueError("seed 必须是整数")
        observation = self.backend.reset(self.config.scenario_name)
        self._start_time = float(observation["sim_time_sec"])
        self._steps = 0
        self._finished = False
        self._observation = observation
        return observation, {"scenario_name": self.config.scenario_name,
                             "seed_applied": False, "reset_confirmed": True}

    def step(self, action: dict | list[dict] | None) -> tuple[dict, float, bool, bool, dict]:
        if self._observation is None or self._finished:
            raise RuntimeError("请先 reset；终止或异常后也必须重新 reset")
        actions = validate_actions(action, self._observation)
        previous = self._observation
        try:
            commands = self.backend.apply_actions(actions)
            current = self.backend.advance(self.config.frames_per_step)
        except Exception:
            self._finished = True
            raise
        delta = float(current["sim_time_sec"]) - float(previous["sim_time_sec"])
        if delta < 0:
            self._finished = True
            raise RuntimeError("推演时间倒退；当前 episode 已失效")
        info = {"commands": commands, "sim_delta_sec": delta,
                "frames_advanced": current["frame_seq"] - previous["frame_seq"],
                "action_count": len(actions)}
        try:
            reward, components = self.reward_fn(previous, actions, current, info)
            reward = _finite_number(reward, "reward", -1e12, 1e12)
            if not isinstance(components, dict):
                raise ValueError("reward_fn 必须返回 (数值, 分量字典)")
            terminated = bool(self.terminal_fn(current, info)) if self.terminal_fn else False
        except Exception:
            self._finished = True
            raise
        self._steps += 1
        elapsed = float(current["sim_time_sec"]) - self._start_time
        truncated = elapsed >= self.config.episode_duration_sec or (
            self.config.max_steps is not None and self._steps >= self.config.max_steps)
        info.update(reward_components=components, episode_elapsed_sec=elapsed,
                    step=self._steps)
        self._observation = current
        self._finished = terminated or truncated
        return current, reward, terminated, truncated, info

    def close(self) -> None:
        self._finished = True
        self.backend.close()
