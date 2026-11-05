"""
墨子统一连接器 — MoziConnector

合并自:
  - OCA制空扫荡 mozi_connector.py  (基础框架 + 战斗控制 + 武器查询)
  - 预警机前出巡逻 mozi_connector.py (create_patrol_zone, fly_full_route)
  - CAP战斗机巡逻 mozi_connector.py  (get_incoming_missiles, set_radar, get_blue_cap_fighters)

WS:  唯一状态源 (态势推送)
REST: 控制指令下发通道
"""

import json
import math
import re
import threading
import time
import zlib
from contextlib import contextmanager

import requests
import websocket
from .http_response import request_middleware

from .config import (
    MOZI_BASE, MOZI_HOST, MOZI_REST_PORT, MOZI_WS, MOZI_WS_PORT,
    BLUE_SIDE_NAME, BLUE_SIDE_COLOR, RED_SIDE_COLOR,
    WS_MAX_RETRIES, WS_BACKOFF_BASE, WS_WAIT_TIMEOUT, WS_FIRST_FRAME_TIMEOUT_SEC,
    AWACS_KEYWORDS, FIGHTER_KEYWORDS, OCA_AIRCRAFT_KEYWORDS,
    WEAPON_TYPE_KEYWORDS, DECOY_WEAPON_KEYWORDS,
    GEN5_KEYWORDS, MISSILE_KEYWORDS,
    CAP_FIGHTER_COUNT, ALLOW_FIRST_SIDE_FALLBACK, SCENARIO_READY_MODE,
)
from .helpers import match_keywords as _match_keywords
from .helpers import parse_cur_num, haversine_km


from src.basic_actions.flight import FlightCommands
from src.basic_actions.sensors import SensorCommands
from src.basic_actions.weapons import WeaponCommands


def _optional_fuel(unit):
    """缺失或无法解析的燃油是未知；真实的零油量仍保留为零。"""
    value = unit.get("FuelRec")
    if value is None or isinstance(value, bool):
        return None
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None
    return value if math.isfinite(value) and value >= 0 else None


class MoziConnector(FlightCommands, SensorCommands, WeaponCommands):
    """
    墨子平台统一连接器

    - WS:   一个连接, 一个 _last_full 缓存, 一个 _update_event
    - REST: 每个工作线程一个 requests.Session
    """

    def __init__(self, host=MOZI_HOST, rest_port=MOZI_REST_PORT, ws_port=MOZI_WS_PORT):
        self.host = host
        self.rest_port = rest_port
        self.ws_port = ws_port
        self.base = f"http://{host}:{rest_port}"
        self.ws_url = f"ws://{host}:{self.ws_port}/ws"

        # WS 状态
        self._last_full = None
        self._ws = None
        self._thread = None
        self._connected = False
        self._lock = threading.Lock()
        self._update_condition = threading.Condition(self._lock)
        self._update_event = threading.Event()
        self._update_sequence = 0
        self._last_received_monotonic = None
        self._read_local = threading.local()

        # 并发任务分支各用本线程的 requests.Session，避免跨线程共享。
        self._sessions = {}
        self._sessions_lock = threading.Lock()

    @property
    def _session(self):
        thread_id = threading.get_ident()
        with self._sessions_lock:
            session = self._sessions.get(thread_id)
            if session is None:
                session = requests.Session()
                session.headers["Content-Type"] = "application/json"
                self._sessions[thread_id] = session
            return session

    # ═══════════════════ WS 连接管理 ═══════════════════

    def connect(self):
        """连接 WS，带指数退避与首帧超时；想定就绪由 wait_for_scenario 判断。"""
        for attempt in range(WS_MAX_RETRIES):
            try:
                self.close()
                with self._lock:
                    self._last_full = None
                    self._last_received_monotonic = None
                self._ws = websocket.WebSocketApp(
                    self.ws_url,
                    on_open=self._on_open,
                    on_message=self._on_message,
                    on_error=self._on_error,
                    on_close=self._on_close,
                )
                self._thread = threading.Thread(
                    target=self._ws.run_forever, daemon=True
                )
                self._thread.start()

                # 等待 WS 连接建立
                for _ in range(50):
                    if self._connected:
                        break
                    time.sleep(0.1)

                if self._connected:
                    with self._update_condition:
                        if self._update_condition.wait_for(
                            lambda: self._last_full is not None,
                            timeout=WS_FIRST_FRAME_TIMEOUT_SEC,
                        ):
                            return True

            except Exception as e:
                pass
            if attempt < WS_MAX_RETRIES - 1:
                time.sleep(WS_BACKOFF_BASE ** attempt)

        return False

    def _on_open(self, ws):
        self._connected = True

    def _on_message(self, ws, message):
        try:
            if isinstance(message, bytes):
                try:
                    raw = zlib.decompress(message, -zlib.MAX_WBITS)
                except zlib.error:
                    raw = zlib.decompress(message)  # 兜底: zlib header
                data = json.loads(raw)
            else:
                data = json.loads(message)
            with self._update_condition:
                self._last_full = data
                self._connected = True
                self._update_sequence += 1
                self._last_received_monotonic = time.monotonic()
                self._update_condition.notify_all()
            self._update_event.set()
        except Exception as e:
            pass

    def _on_error(self, ws, error):
        self._connected = False

    def _on_close(self, ws, close_status_code=None, close_msg=None):
        self._connected = False

    def close(self):
        """关闭 WS 连接"""
        if self._ws:
            try:
                self._ws.close()
            except Exception:
                pass
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=2)
        self._ws = None
        self._thread = None
        self._connected = False
        with self._sessions_lock:
            sessions = list(self._sessions.values())
            self._sessions.clear()
        for session in sessions:
            try:
                session.close()
            except (AttributeError, OSError):
                pass

    def reconnect(self):
        """重新连接"""
        self.close()
        return self.connect()

    def is_connected(self):
        """检查 WS 是否存活"""
        sock = (
            getattr(getattr(self._ws, "sock", None), "connected", False)
            if self._ws else False
        )
        return sock and self._connected

    def is_situation_live(self, max_age_sec=10.0):
        """只有连接仍在且最近收到态势帧，才把缓存视为当前想定。"""
        if not self.is_connected():
            return False
        with self._lock:
            received_at = self._last_received_monotonic
        return received_at is not None and time.monotonic() - received_at <= max_age_sec

    def wait_for_update(self, timeout=WS_WAIT_TIMEOUT):
        """等待一次态势更新"""
        self._update_event.clear()
        return self._update_event.wait(timeout=timeout)

    def get_update_sequence(self):
        with self._lock:
            return self._update_sequence

    def get_scenario_name(self) -> str:
        """读取当前 WS 帧的想定名称，用于隔离在线config。"""
        data = self._get_data()
        return str(data.get("ScenarioName", "")).strip() if isinstance(data, dict) else ""

    def wait_for_new_update(self, last_sequence, timeout=WS_WAIT_TIMEOUT):
        """按帧序号等待，避免 Event.clear 与推送之间的丢帧竞态。"""
        with self._update_condition:
            arrived = self._update_condition.wait_for(
                lambda: self._update_sequence > last_sequence,
                timeout=timeout,
            )
            return self._update_sequence if arrived else None

    @contextmanager
    def consistent_read(self, snapshot=None):
        """让当前线程内的多个 get_* 调用读取同一份 WS 帧。

        并行子树可传入主线程已固定的 snapshot，保证同轮读同一帧。
        """
        previous = getattr(self._read_local, "snapshot", None)
        if snapshot is None and previous is None:
            with self._lock:
                snapshot = {
                    "sequence": self._update_sequence,
                    "received_at": self._last_received_monotonic,
                    "state": self._last_full,
                }
        elif snapshot is None:
            snapshot = previous
        self._read_local.snapshot = snapshot
        try:
            yield snapshot
        finally:
            if previous is None:
                del self._read_local.snapshot
            else:
                self._read_local.snapshot = previous

    def wait_for_scenario(self, timeout=120):
        """等待新想定加载 (检查战斗机)"""
        with self._lock:
            self._last_full = None

        if not self.is_connected():
            for i in range(60):
                if self.is_connected():
                    break
                time.sleep(0.5)
            else:
                self.reconnect()

        for i in range(int(timeout * 2)):
            if self._get_data() is not None:
                if SCENARIO_READY_MODE == "side" and self.get_blue_side():
                    return True
                if SCENARIO_READY_MODE == "aircraft" and self.get_blue_aircraft():
                    return True
                if SCENARIO_READY_MODE == "fighters" and self.get_blue_fighters():
                    return True
            if i % 20 == 19:
                pass
            time.sleep(0.5)

        return False

    # ═══════════════════ 想定控制 ═══════════════════

    def load_scenario(self, scenario_name):
        """加载想定，并检查中间件返回；调用方仍须等待新态势帧。"""
        if not isinstance(scenario_name, str) or not scenario_name.strip():
            raise ValueError("scenario_name 必须是非空字符串")
        payload = request_middleware(
            self._session, "GET", f"{self.base}/ApiCtrl/api/LoadScenario",
            params={"scenarioName": scenario_name.strip()}, timeout=30,
        )
        if payload.get("code") != 0:
            raise RuntimeError(f"墨子加载想定失败：{payload.get('message', '中间件未返回成功状态')}")
        return payload

    def start_simulation(self):
        """让墨子开始或继续推演；接口失败时交给画布显示，不能静默忽略。"""
        return self._simulation_control("StartSimulation", "开始")

    def pause_simulation(self):
        """暂停墨子推演；返回中间件应答供调用方确认。"""
        return self._simulation_control("PauseSimulation", "暂停")

    def _simulation_control(self, endpoint: str, label: str) -> dict:
        payload = request_middleware(self._session, 'GET', f"{self.base}/ApiCtrl/api/{endpoint}", timeout=10)
        if not payload.get('confirmation_required') and payload.get("code") != 0:
            message = payload.get("message", "中间件未返回成功状态") if isinstance(payload, dict) else "中间件应答格式无效"
            raise RuntimeError(f"墨子{label}推演失败：{message}")
        return payload

    def set_sim_speed(self, multiplier):
        """设置推演倍速"""
        try:
            r = self._session.get(
                f"{self.base}/ApiCtrl/api/SimCompression",
                params={"Compression": multiplier},
                timeout=10,
            )
        except Exception as e:
            pass

    # ═══════════════════ 内部辅助 ═══════════════════

    def _get_data(self):
        """线程安全地获取最新态势数据"""
        snapshot = getattr(self._read_local, "snapshot", None)
        if snapshot is not None:
            return snapshot["state"]
        with self._lock:
            return self._last_full

    def _find_blue_side(self):
        """找到蓝方 side 数据 (优先按名称, 兜底取第一个)"""
        data = self._get_data()
        if not data:
            return None
        for side in data.get("side", []):
            name = side.get("name", "")
            if BLUE_SIDE_NAME in name:
                return side
        # 可config的旧版兜底；默认关闭，避免未识别推演方时控制错误的一方。
        sides = data.get("side", [])
        return sides[0] if ALLOW_FIRST_SIDE_FALLBACK and sides else None

    def _get_blue_side_guid(self):
        """通过 REST API 获取蓝方 SideGuid (用于巡逻区创建等)"""
        try:
            r = self._session.get(
                f"{self.base}/ApiCtrl/api/sideOperation/getSideData",
                timeout=10,
            )
            for s in r.json().get("data", {}).get("sides", []):
                name = s.get("name", "")
                if BLUE_SIDE_NAME in name:
                    return s["guid"]
        except Exception as e:
            pass
        return None

    # ═══════════════════ 态势读取 (WS) ═══════════════════

    def get_full_state(self):
        """获取完整态势数据"""
        return self._get_data()

    def get_blue_side(self):
        """获取蓝方 side 字典 (同 _find_blue_side, 公开别名)"""
        return self._find_blue_side()

    def get_contacts(self):
        """获取蓝方探测到的所有 contacts"""
        side = self._find_blue_side()
        if not side:
            return []
        return [c for c in side.get("contacts", []) if isinstance(c, dict)]

    def get_awacs_info(self):
        """
        获取蓝方预警机信息

        Returns:
            {"lat", "lon", "guid", "name", "alt", "speed"} 或 None
        """
        side = self._find_blue_side()
        if not side:
            return None

        for u in side.get("activeUnits", []):
            if u.get("UnitType") != "Aircraft":
                continue
            name = u.get("name", "")
            if not _match_keywords(name, AWACS_KEYWORDS):
                continue
            lat = float(u.get("Latitude", 0) or 0)
            lon = float(u.get("Longitude", 0) or 0)
            if lat == 0 and lon == 0:
                continue
            return {
                "lat": lat,
                "lon": lon,
                "guid": u.get("id", ""),
                "name": name,
                "alt": float(u.get("CA", 0) or 0),
                "speed": float(u.get("CurrentSpeed", 0) or 0),
            }
        return None

    def get_blue_aircraft(self):
        """
        获取蓝方所有空中飞机 (含详细信息)

        Returns:
            [{"guid", "name", "sub_type", "lat", "lon", "alt", "speed",
              "heading", "fuel", "damage"}, ...]
        """
        side = self._find_blue_side()
        if not side:
            return []

        aircraft = []
        for u in side.get("activeUnits", []):
            if u.get("UnitType") != "Aircraft":
                continue
            # 排除在设施内的 (未起飞)
            if u.get("Component", "none") != "none":
                continue
            lat = float(u.get("Latitude", 0) or 0)
            lon = float(u.get("Longitude", 0) or 0)
            if lat == 0 and lon == 0:
                continue
            aircraft.append({
                "guid": u.get("id", ""),
                "id": u.get("id", ""),
                "name": u.get("name", "?"),
                "sub_type": u.get("subType", ""),
                "lat": lat,
                "lon": lon,
                "alt": float(u.get("CA", 0) or 0),
                "speed": float(u.get("CurrentSpeed", 0) or 0),
                "heading": float(u.get("heading", 0) or 0),
                "fuel": _optional_fuel(u),
                "damage": int(u.get("Damage", 0) or 0),
            })
        return aircraft

    def get_blue_parked_aircraft(self):
        """从同帧 FightTree 读取蓝方机场/舰船内的飞机，供开局绑定与起飞使用。"""
        side = self._find_blue_side()
        data = self._get_data()
        if not side or not isinstance(data, dict):
            return []
        side_id = side.get("id")
        parked = []
        for group in data.get("FightTree", []):
            if not isinstance(group, dict) or group.get("SideID") != side_id:
                continue
            for unit in group.get("FightTree", []):
                if (not isinstance(unit, dict) or unit.get("UnitType") != "Aircraft"
                        or unit.get("AirCraftInFacility") is not True):
                    continue
                guid = unit.get("id")
                lat = float(unit.get("Latitude", 0) or 0)
                lon = float(unit.get("Longitude", 0) or 0)
                if not guid or (lat == 0 and lon == 0):
                    continue
                parked.append({"guid": guid, "id": guid, "name": unit.get("name", "?"),
                               "sub_type": unit.get("subType", ""), "lat": lat, "lon": lon,
                               "airborne": False, "parked": True})
        return parked


    def get_blue_aircraft_positions(self):
        """
        获取蓝方所有飞机位置

        Returns:
            [(lat, lon), ...]
        """
        side = self._find_blue_side()
        if not side:
            return []

        positions = []
        for u in side.get("activeUnits", []):
            if u.get("UnitType") != "Aircraft":
                continue
            lat = float(u.get("Latitude", 0) or 0)
            lon = float(u.get("Longitude", 0) or 0)
            if lat == 0 and lon == 0:
                continue
            positions.append((lat, lon))
        return positions

    def get_blue_fighters(self, keywords=None):
        """
        获取蓝方战斗机 (按名称关键词筛选)

        Args:
            keywords: 筛选关键词元组, 默认使用 FIGHTER_KEYWORDS

        Returns:
            list[dict]: 战斗机列表
        """
        if keywords is None:
            keywords = FIGHTER_KEYWORDS
        side = self._find_blue_side()
        if not side:
            return []

        fighters = []
        for u in side.get("activeUnits", []):
            if u.get("UnitType") != "Aircraft":
                continue
            combined = (u.get("name", "") + " " + u.get("subType", "")).upper()
            if _match_keywords(combined, keywords):
                fighters.append({
                    "guid": u.get("id", ""),
                    "id": u.get("id", ""),
                    "name": u.get("name", "?"),
                    "sub_type": u.get("subType", ""),
                    "lat": float(u.get("Latitude", 0) or 0),
                    "lon": float(u.get("Longitude", 0) or 0),
                    "alt": float(u.get("CA", 0) or 0),
                    "speed": float(u.get("CurrentSpeed", 0) or 0),
                    "heading": float(u.get("heading", 0) or 0),
                    "fuel": _optional_fuel(u),
                    "damage": int(u.get("Damage", 0) or 0),
                })
        return fighters

    def get_blue_ground_positions(self):
        """
        获取蓝方地面/海面单元位置

        Returns:
            [(lat, lon), ...]
        """
        side = self._find_blue_side()
        if not side:
            return []

        positions = []
        for u in side.get("activeUnits", []):
            if u.get("UnitType") == "Aircraft":
                continue
            lat = float(u.get("Latitude", 0) or 0)
            lon = float(u.get("Longitude", 0) or 0)
            if lat == 0 and lon == 0:
                continue
            positions.append((lat, lon))
        return positions

    @staticmethod
    def _command_unit(u):
        """保留军种指挥所需的稳定字段，不把原始平台对象暴露给模型。"""
        return {
            "guid": u.get("id", ""),
            "id": u.get("id", ""),
            "name": u.get("name", "?"),
            "sub_type": u.get("subType", ""),
            "unit_type": u.get("UnitType", ""),
            "lat": float(u.get("Latitude", 0) or 0),
            "lon": float(u.get("Longitude", 0) or 0),
            "speed": float(u.get("CurrentSpeed", 0) or 0),
            "heading": float(u.get("heading", 0) or 0),
            "damage": int(u.get("Damage", 0) or 0),
        }

    def get_blue_naval_units(self):
        """读取蓝方舰艇/潜艇；只供上层海军指挥规划，不直接下达游戏命令。"""
        side = self._find_blue_side()
        if not side:
            return []
        naval_types = {"Ship", "舰艇", "Submarine", "潜艇"}
        return [self._command_unit(unit) for unit in side.get("activeUnits", [])
                if unit.get("UnitType") in naval_types and unit.get("id")]

    def get_blue_ground_units(self):
        """读取蓝方地面车辆与设施；机场等固定设施也属于陆军方向态势。"""
        side = self._find_blue_side()
        if not side:
            return []
        excluded = {"Aircraft", "飞机", "Ship", "舰艇", "Submarine", "潜艇",
                    "Weapon", "武器", "Satellite", "卫星"}
        return [self._command_unit(unit) for unit in side.get("activeUnits", [])
                if unit.get("UnitType") not in excluded and unit.get("id")]

    def get_oca_aircraft_positions(self):
        """
        获取 OCA 飞机位置 (用于计算 OCA 阵位重心)

        Returns:
            [(lat, lon), ...]
        """
        side = self._find_blue_side()
        if not side:
            return []

        positions = []
        for u in side.get("activeUnits", []):
            if u.get("UnitType") != "Aircraft":
                continue
            name = u.get("name", "")
            if not any(kw in name for kw in OCA_AIRCRAFT_KEYWORDS):
                continue
            lat = float(u.get("Latitude", 0) or 0)
            lon = float(u.get("Longitude", 0) or 0)
            if lat == 0 and lon == 0:
                continue
            positions.append((lat, lon))
        return positions

    def get_red_contacts(self):
        """获取探测到的红方 contacts (原始字典列表)"""
        return [
            c for c in self.get_contacts()
            if c.get("SideColor") == RED_SIDE_COLOR
        ]

    def get_enemy_ground_contacts(self):
        """仅从己方contacts按名称查地面装备；不读取敌方activeUnits。"""
        from src.equipment_data.catalog import default_catalog
        from src.task_planning.geometry.oca_safety import valid_point
        catalog = default_catalog()
        result = []
        for contact in self.get_red_contacts():
            kind = contact.get("UnitType", "")
            if kind in {"Aircraft", "飞机", "Weapon", "Missile", "导弹", "Ship", "舰艇", "Submarine", "潜艇"}:
                continue
            match = catalog.identify_ground_contact(contact) if catalog else {"status": "unknown", "candidates": []}
            if match["status"] == "unknown" and kind not in {"Facility", "设施", "地面设施"}:
                continue
            try:
                point = (float(contact.get("Latitude", contact.get("lat"))),
                         float(contact.get("Longitude", contact.get("lon"))))
            except (TypeError, ValueError):
                continue
            if not contact.get("id") or not valid_point(point):
                continue
            model = match["candidates"][0] if match["status"] == "matched" else None
            result.append({"id": contact["id"], "name": contact.get("name", ""),
                "sub_type": contact.get("subType", ""), "unit_type": kind,
                "lat": point[0], "lon": point[1], "model_status": match["status"],
                "catalog_name": model.get("name") if model else None,
                "model_guid": model.get("guid") if model else None,
                "model_candidates": [{"guid": r["guid"], "name": r.get("name"),
                                      "id": r.get("id")} for r in match["candidates"]],
                "source": "blue_contacts"})
        return result

    def get_enemy_aircraft(self):
        """
        获取红方飞机 (预警机/战斗机探测到的 contacts)

        Returns:
            list[dict]: 敌方飞机列表
        """
        red_contacts = self.get_red_contacts()
        enemies = []

        for c in red_contacts:
            unit_type = c.get("UnitType", "")
            name = c.get("name", "") + " " + c.get("subType", "")

            is_aircraft = (
                unit_type in ("Aircraft", "飞机") or
                _match_keywords(name, FIGHTER_KEYWORDS)
            )

            if is_aircraft:
                enemies.append({
                    "id": c.get("id", ""),
                    "name": c.get("name", "?"),
                    "sub_type": c.get("subType", ""),
                    "unit_type": unit_type,
                    "lat": float(c.get("Latitude", c.get("lat", 0)) or 0),
                    "lon": float(c.get("Longitude", c.get("lon", 0)) or 0),
                    "alt": float(c.get("CA", 0) or 0),
                    "speed": float(c.get("CurrentSpeed", 0) or 0),
                    "heading": float(c.get("heading", 0) or 0),
                    "heading_known": c.get("heading") is not None,
                    "alt_known": c.get("CA") is not None,
                })

        return enemies

    def get_enemy_ships(self):
        """
        获取红方舰艇 (探测到的 contacts 中的舰船)

        Returns:
            list[dict]: 敌方舰艇列表 [{"id", "name", "lat", "lon", "speed", "heading"}, ...]
        """
        red_contacts = self.get_red_contacts()
        ships = []
        ship_keywords = ("舰", "Ship", "CVN", "DDG", "FFG", "SSN", "SSBN",
                         "航母", "驱逐舰", "护卫舰", "潜艇", "巡洋舰",
                         "carrier", "destroyer", "frigate", "cruiser")

        for c in red_contacts:
            unit_type = c.get("UnitType", "")
            name = c.get("name", "") + " " + c.get("subType", "")

            is_ship = (
                unit_type in ("Ship", "舰艇", "Submarine", "潜艇") or
                _match_keywords(name, ship_keywords)
            )

            if is_ship:
                ships.append({
                    "id": c.get("id", ""),
                    "name": c.get("name", "?"),
                    "sub_type": c.get("subType", ""),
                    "unit_type": unit_type,
                    "lat": float(c.get("Latitude", c.get("lat", 0)) or 0),
                    "lon": float(c.get("Longitude", c.get("lon", 0)) or 0),
                    "speed": float(c.get("CurrentSpeed", 0) or 0),
                    "heading": float(c.get("heading", 0) or 0),
                    "speed_known": c.get("CurrentSpeed") is not None,
                    "heading_known": c.get("heading") is not None,
                })

        return ships

    def get_enemy_positions(self):
        """
        获取敌方接触位置 (排除蓝方 / 武器 / 导弹)

        Returns:
            [(lat, lon), ...]
        """
        side = self._find_blue_side()
        if not side:
            return []

        positions = []
        for contact in side.get("contacts", []):
            if not isinstance(contact, dict):
                continue
            color = contact.get("SideColor", "")
            if color == BLUE_SIDE_COLOR:
                continue
            # 跳过武器/导弹
            name = contact.get("name", "")
            unit_type = contact.get("UnitType", "")
            sub_type = contact.get("subType", "")
            combined = (name + " " + sub_type + " " + unit_type).upper()
            if "WEAPON" in combined or "MISSILE" in combined:
                continue
            lat = float(
                contact.get("Latitude", contact.get("lat", 0)) or 0
            )
            lon = float(
                contact.get("Longitude", contact.get("lon", 0)) or 0
            )
            if lat == 0 and lon == 0:
                continue
            positions.append((lat, lon))
        return positions

    def get_enemy_aircraft_center(self):
        """
        计算敌机群重心

        Returns:
            (lat, lon) 或 (None, None)
        """
        enemies = self.get_enemy_aircraft()
        if not enemies:
            return None, None

        lats = [e["lat"] for e in enemies if e["lat"] != 0]
        lons = [e["lon"] for e in enemies if e["lon"] != 0]

        if not lats:
            return None, None

        return sum(lats) / len(lats), sum(lons) / len(lons)

    def get_enemy_contacts_with_details(self):
        """
        获取敌方接触详情 (排除导弹/武器)

        Returns:
            [{"id", "name", "sub_type", "lat", "lon", "alt", "speed",
              "heading"}, ...]
        """
        side = self._find_blue_side()
        if not side:
            return []

        contacts = []
        for c in side.get("contacts", []):
            if not isinstance(c, dict):
                continue
            color = c.get("SideColor", "")
            if color == BLUE_SIDE_COLOR:
                continue
            # 排除导弹/武器
            name = c.get("name", "")
            unit_type = c.get("UnitType", "")
            sub_type = c.get("subType", "")
            combined = (name + " " + sub_type + " " + unit_type).upper()
            if "WEAPON" in combined or "MISSILE" in combined or "导弹" in combined:
                continue
            if _match_keywords(name + " " + sub_type, MISSILE_KEYWORDS):
                continue
            lat = float(c.get("Latitude", c.get("lat", 0)) or 0)
            lon = float(c.get("Longitude", c.get("lon", 0)) or 0)
            if lat == 0 and lon == 0:
                continue
            contacts.append({
                "id": c.get("id", ""),
                "name": name,
                "sub_type": sub_type,
                "lat": lat,
                "lon": lon,
                "alt": float(c.get("CA", 0) or 0),
                "speed": float(c.get("CurrentSpeed", 0) or 0),
                "heading": float(c.get("heading", 0) or 0),
            })
        return contacts

    def get_incoming_missiles(self):
        """
        获取来袭导弹 (目标是蓝方飞机的红方导弹)

        Returns:
            [{"id", "name", "lat", "lon", "alt", "speed", "heading",
              "target_id", "targeting_defender"}, ...]
        """
        side = self._find_blue_side()
        if not side:
            return []

        # 蓝方飞机 ID 集合
        blue_ids = set()
        for u in side.get("activeUnits", []):
            if u.get("UnitType") == "Aircraft":
                blue_ids.add(u.get("id", ""))

        missiles = []
        for c in side.get("contacts", []):
            if not isinstance(c, dict):
                continue
            color = c.get("SideColor", "")
            if color == BLUE_SIDE_COLOR:
                continue
            name = c.get("name", "") + " " + c.get("subType", "")
            unit_type = c.get("UnitType", "")
            is_missile = (
                _match_keywords(name, MISSILE_KEYWORDS) or
                unit_type in ("Missile", "Weapon", "导弹")
            )
            if is_missile:
                target_id = c.get("targetId", c.get("TargetID", None))
                is_targeting = target_id in blue_ids if target_id else False
                missiles.append({
                    "id": c.get("id", ""),
                    "name": c.get("name", "?"),
                    "lat": float(c.get("Latitude", c.get("lat", 0)) or 0),
                    "lon": float(c.get("Longitude", c.get("lon", 0)) or 0),
                    "alt": float(c.get("CA", 0) or 0),
                    "speed": float(c.get("CurrentSpeed", 0) or 0),
                    "heading": float(c.get("heading", 0) or 0),
                    "target_id": target_id,
                    "targeting_defender": is_targeting,
                })
        return missiles

    def get_known_sam_contacts(self):
        """仅筛选己方已探测的地面接触；名称识别不代表确认型号或射程。"""
        from src.task_planning.geometry.oca_safety import valid_point
        result = []
        for contact in self.get_red_contacts():
            text = str(contact.get("name", "")) + " " + str(contact.get("subType", ""))
            kind = contact.get("UnitType", "")
            if kind in {"Aircraft", "飞机", "Weapon", "Missile", "导弹", "Ship", "舰艇"}:
                continue
            if not any(word in text.lower() for word in ("sam", "地空", "地导", "防空导弹", "hq-", "红旗", "patriot", "s-300", "s-400", "buk", "tor-", "9m", "48n6", "40n6")):
                continue
            try:
                point = (float(contact.get("Latitude", contact.get("lat"))),
                         float(contact.get("Longitude", contact.get("lon"))))
            except (TypeError, ValueError):
                continue
            identity = contact.get("id")
            if identity and valid_point(point):
                result.append({"id": identity, "name": contact.get("name", ""),
                               "lat": point[0], "lon": point[1], "source": "blue_contacts"})
        from src.equipment_data.catalog import game_sam_radius
        existing = {row["id"] for row in result}
        for contact in self.get_enemy_ground_contacts():
            if contact["id"] not in existing and contact.get("catalog_name") and game_sam_radius(contact["catalog_name"]) is not None:
                result.append(contact)
        return result

    def get_scenario_elapsed_seconds(self):
        """按已文档化的 CurrentTime/StartTime 求游戏秒；不可用时返回 None。"""
        from datetime import datetime
        try:
            result = self._session.get(f"{self.base}/ApiCtrl/api/GetScenarioTime", timeout=3).json()
            if result.get("code") != 0:
                return None
            data = result["data"]
            current = datetime.fromisoformat(data["CurrentTime"])
            start = datetime.fromisoformat(data["StartTime"])
            elapsed = (current - start).total_seconds()
            return elapsed if elapsed >= 0 else None
        except Exception:
            return None

    def get_blue_missiles_in_flight(self):
        """
        获取蓝方在飞导弹 (蓝方 activeUnits 中的 Weapon/Missile)

        Returns:
            [{"id", "name", "lat", "lon", "alt", "speed"}, ...]
        """
        side = self._find_blue_side()
        if not side:
            return []

        missiles = []
        for u in side.get("activeUnits", []):
            unit_type = u.get("UnitType", "")
            name = u.get("name", "") + " " + u.get("subType", "")
            is_missile = (
                unit_type in ("Weapon", "Missile", "导弹") or
                _match_keywords(name, MISSILE_KEYWORDS)
            )
            if is_missile:
                missiles.append({
                    "id": u.get("id", ""),
                    "name": u.get("name", "?"),
                    "lat": float(u.get("Latitude", 0) or 0),
                    "lon": float(u.get("Longitude", 0) or 0),
                    "alt": float(u.get("CA", 0) or 0),
                    "speed": float(u.get("CurrentSpeed", 0) or 0),
                })
        return missiles

    def get_blue_cap_fighters(self):
        """
        筛选 CAP 战斗机: 非预警机 + 非五代机 + 仅空空弹

        Returns:
            list[dict]: 最多 CAP_FIGHTER_COUNT 架
        """
        all_aircraft = self.get_blue_aircraft()
        if not all_aircraft:
            return []

        # 排除预警机
        filtered = [
            ac for ac in all_aircraft
            if not any(kw in ac["name"] for kw in AWACS_KEYWORDS)
        ]

        # 排除五代机
        non_gen5 = []
        for ac in filtered:
            combined = ac["name"] + " " + ac["sub_type"]
            if _match_keywords(combined, GEN5_KEYWORDS):
                continue
            non_gen5.append(ac)

        # 按挂载分类
        air_to_air_fighters = []

        for ac in non_gen5:
            loadout_info = self.get_aircraft_loadout(ac["guid"])
            loadout_text = ""
            weapon_counts = {
                "air_to_air": 0,
                "ground_attack": 0,
                "anti_ship": 0,
                "anti_radiation": 0,
            }

            if loadout_info:
                info = loadout_info.get("Info", {})
                loadout_text = info.get("LoadoutRoleDescription", "")
                loadout_text += " " + json.dumps(loadout_info, ensure_ascii=False)
                for weapon_type, keywords in WEAPON_TYPE_KEYWORDS.items():
                    count = sum(
                        1 for kw in keywords
                        if kw.upper() in loadout_text.upper()
                    )
                    weapon_counts[weapon_type] = count

            has_aam = weapon_counts["air_to_air"] > 0
            has_other = (
                weapon_counts.get("ground_attack", 0) > 0 or
                weapon_counts.get("anti_ship", 0) > 0 or
                weapon_counts.get("anti_radiation", 0) > 0
            )

            if has_aam and not has_other:
                air_to_air_fighters.append(ac)
            elif has_aam and has_other:
                pass
            elif _match_keywords(
                ac["name"] + " " + ac["sub_type"], FIGHTER_KEYWORDS
            ):
                air_to_air_fighters.append(ac)


        selected = air_to_air_fighters[:CAP_FIGHTER_COUNT]
        for i, f in enumerate(selected):
            pass

        return selected

    # ═══════════════════ 飞行控制 (REST) ═══════════════════






    # ── 内部飞行指令 ──




    # ═══════════════════ 武器/传感器控制 (REST) ═══════════════════





    def create_patrol_zone(self, waypoints, name="巡逻区"):
        """
        创建巡逻区域: 批量创建参考点 + ScenArea

        Args:
            waypoints: [(lat, lon), ...] 航路点列表
            name: 区域名称

        Returns:
            bool: 创建成功
        """
        side = self._find_blue_side()
        if not side:
            return False

        side_name = side.get("name", BLUE_SIDE_NAME)
        side_guid = self._get_blue_side_guid()
        if not side_guid:
            return False

        # 步骤1: 批量创建参考点
        values = [
            {"Lon": wp[1], "Lat": wp[0], "Name": f"{name}-{i + 1:02d}"}
            for i, wp in enumerate(waypoints)
        ]
        try:
            r = self._session.post(
                f"{self.base}/ApiCtrl/api/ReferencePoint",
                json={
                    "Type": "AddReferencePoint",
                    "SideGuid": side_guid,
                    "Values": values,
                },
                timeout=10,
            )
            result = r.json()
            if result.get("code") != 0 or not result.get("data"):
                return False
            ref_guids = result["data"]
        except Exception as e:
            return False

        if len(ref_guids) < 3:
            return False

        # 步骤2: 创建区域
        area_points = []
        for i, wp in enumerate(waypoints):
            if i < len(ref_guids):
                area_points.append({
                    "id": ref_guids[i],
                    "x": wp[0],
                    "y": wp[1],
                })

        try:
            r = self._session.post(
                f"{self.base}/ApiCtrl/api/ScenArea",
                json={
                    "option": "addArea",
                    "side": side_name,
                    "areaType": "405",
                    "area_name": name,
                    "area_remark": name,
                    "area_points": area_points,
                },
                timeout=10,
            )
            result = r.json()
            if result.get("code") == 0:
                return True
            else:
                return False
        except Exception as e:
            return False

    # ═══════════════════ 挂载/武器查询 (REST) ═══════════════════

    def get_aircraft_loadout(self, guid):
        """获取飞机挂载信息"""
        try:
            r = self._session.get(
                f"{self.base}/ApiCtrl/api/air-operations/loadout",
                params={"Guid": guid},
                timeout=10,
            )
            data = r.json()
            if data.get("code") == 0:
                return data.get("data", {})
        except Exception as e:
            pass
        return None

    def get_weapon_status(self, unit_guid):
        """
        获取飞机武器状态 (合并: 空空/中距/近距 计数)

        Returns:
            dict: {
                "air_to_air_count":   int,  # 所有空空导弹
                "medium_range_count": int,  # 中距弹
                "short_range_count":  int,  # 近距弹
                "total_weapons":      int,
                "weapon_list":        list,
            }
            获取失败返回 None
        """
        try:
            r = self._session.get(
                f"{self.base}/ApiCtrl/api/unitWeaponInfo",
                params={"guid": unit_guid},
                timeout=10,
            )
            data = r.json()
            if data.get("code") != 0:
                return None

            payload = data.get("data", [])
            if not isinstance(payload, list):
                return None
            inventory_complete = all(isinstance(item, dict) and isinstance(item.get("weaponRecord"), list) for item in payload)

            air_to_air_kw = WEAPON_TYPE_KEYWORDS.get("air_to_air", ())
            medium_kw = WEAPON_TYPE_KEYWORDS.get("medium_range", ())
            short_kw = WEAPON_TYPE_KEYWORDS.get("short_range", ())

            air_to_air_count = 0
            medium_range_count = 0
            short_range_count = 0
            total = 0
            weapon_list = []

            for item in payload:
                records = item.get("weaponRecord", [])
                if not isinstance(records, list):
                    continue
                for rec in records:
                    name = rec.get("name", "")
                    cur_num = parse_cur_num(rec.get("curNum"))
                    count_known = cur_num is not None
                    if cur_num is None:
                        cur_num = 0
                    w_id = rec.get("id", "")

                    total += cur_num
                    weapon_list.append({
                        "guid": w_id,
                        "name": name,
                        "count": cur_num,
                        "count_known": count_known,
                    })

                    if _match_keywords(name, air_to_air_kw):
                        air_to_air_count += cur_num
                    if _match_keywords(name, medium_kw):
                        medium_range_count += cur_num
                    if _match_keywords(name, short_kw):
                        short_range_count += cur_num

            return {
                "air_to_air_count": air_to_air_count,
                "medium_range_count": medium_range_count,
                "short_range_count": short_range_count,
                "total_weapons": total,
                "weapon_list": weapon_list,
                "inventory_complete": inventory_complete,
            }

        except Exception as e:
            return None

    def get_ground_release_option(self, guid, target_guid, weapon_name, model_candidates):
        """使用游戏手动接战界面的明确可开火项复核制导/照射/射程条件。"""
        from src.equipment_data.catalog import normalize_name
        try:
            response = self._session.get(f"{self.base}/ApiCtrl/api/weapon-assignment",
                params={"unitGuid": guid, "targetGuid": target_guid}, timeout=10).json()
            payload = response.get("data")
            if response.get("code") != 0 or not isinstance(payload, dict) or not isinstance(payload.get("weaponList"), list):
                return {"status": "unknown", "reason": "游戏未返回可核实的投放清单"}
            for row in payload["weaponList"]:
                label = re.sub(r"^\s*\d+\s*[x×]\s*", "", str(row.get("name", "")), flags=re.I)
                label = re.sub(r"\s*[(（]\s*\d+\s*[x×]\s*已分配\s*[)）]\s*$", "", label, flags=re.I)
                if row.get("id") not in model_candidates and normalize_name(label) != normalize_name(weapon_name):
                    continue
                checks = row.get("children", [])
                if not isinstance(checks, list):
                    return {"status": "unknown", "reason": "武器投放条件结构未确认"}
                allowed = any(c.get("status") == 2 and "可以开火" in str(c.get("name", ""))
                    and not any(word in str(c.get("name", "")) for word in ("不能", "不可", "无法", "禁止"))
                    for c in checks if isinstance(c, dict))
                if allowed and row.get("id"):
                    return {"status": "ready", "weapon_dbid": row["id"],
                            "reason": "游戏手动分配条件允许", "source": "weapon-assignment GET"}
                return {"status": "blocked", "reason": "；".join(str(c.get("name", "")) for c in checks if isinstance(c, dict))[:1000]}
            return {"status": "unknown", "reason": "游戏清单中没有所选挂载的精确对应项"}
        except Exception:
            return {"status": "unknown", "reason": "游戏投放复核查询失败"}

    def get_maritime_release_option(self, guid, target_guid, weapon_name, model_candidates):
        """对海请求使用同一游戏手动接战清单，但保留独立接口供任务审计。"""
        return self.get_ground_release_option(guid, target_guid, weapon_name, model_candidates)

    def get_air_to_air_weapon_dbid(self, guid):
        """
        获取空空导弹的 DBID (用于 weapon_assignment)

        Returns:
            str: 武器 DBID, 或 None
        """
        loadout = self.get_aircraft_loadout(guid)
        if not loadout:
            return None

        weapons_data = loadout.get("Weapons", loadout.get("weapons", []))
        air_to_air_kw = WEAPON_TYPE_KEYWORDS.get("air_to_air", ())

        if isinstance(weapons_data, list):
            for w in weapons_data:
                w_name = w.get("name", w.get("Name", ""))
                w_dbid = w.get("dbid", w.get("Dbid", w.get("id", "")))
                if _match_keywords(w_name, air_to_air_kw):
                    return w_dbid

        # 兜底: AvailableWeapon 字典
        available = loadout.get("AvailableWeapon", {})
        if isinstance(available, dict):
            for dbid, info in available.items():
                name = info.get("name", "") if isinstance(info, dict) else ""
                if _match_keywords(name, air_to_air_kw):
                    return dbid

        return None

    def get_medium_range_weapon_dbid(self, guid, preferred_model=None, preferred_weapon_name=None):
        """从既有挂载契约选取中距弹，不用近距弹代替中距弹预算。"""
        loadout = self.get_aircraft_loadout(guid)
        if not isinstance(loadout, dict):
            return None
        keywords = WEAPON_TYPE_KEYWORDS.get("medium_range", ())
        from src.parameters.weapon_ranges import match_range_reference, lookup_range_reference

        def matches(name):
            if not _match_keywords(name, keywords):
                return False
            if preferred_weapon_name is not None and str(name).strip().casefold() != preferred_weapon_name.strip().casefold():
                return False
            reference = match_range_reference(name)
            if preferred_model is None or reference is not None and reference["model"] == preferred_model:
                return True
            # 兼容保存config中沿用的公开字典型号；新请求仍携带库内具体型号标识。
            legacy = lookup_range_reference(name, "air_to_air")
            return legacy is not None and legacy["id"] == preferred_model
        weapons = loadout.get("Weapons", loadout.get("weapons", []))
        if isinstance(weapons, list):
            for weapon in weapons:
                if matches(weapon.get("name", weapon.get("Name", ""))):
                    dbid = weapon.get("dbid", weapon.get("Dbid", weapon.get("id")))
                    if dbid:
                        return dbid
        for dbid, info in (loadout.get("AvailableWeapon", {}) or {}).items():
            if isinstance(info, dict) and matches(info.get("name", "")):
                return dbid
        return None

    def get_decoy_weapon_dbid(self, guid, target_lon=None, target_lat=None):
        """
        获取诱饵弹的 DBID (用于纯方位发射)

        优先使用 weapon-assignment GET (返回正确的 DBID 格式),
        回退使用 unitWeaponInfo API。

        Returns:
            str: 武器 DBID, 或 None
        """
        # 方法1: weapon-assignment GET
        if target_lon is not None and target_lat is not None:
            try:
                r = self._session.get(
                    f"{self.base}/ApiCtrl/api/weapon-assignment",
                    params={
                        "unitGuid": guid,
                        "targetLon": target_lon,
                        "targetLat": target_lat,
                    },
                    timeout=10,
                )
                data = r.json()
                if data.get("code") == 0:
                    weapon_list = data.get("data", {})
                    if isinstance(weapon_list, dict):
                        weapon_list = weapon_list.get("weaponList", [])
                    if not isinstance(weapon_list, list):
                        weapon_list = []
                    for w in weapon_list:
                        w_name = w.get("name", "")
                        w_id = w.get("id", "")
                        if _match_keywords(w_name, DECOY_WEAPON_KEYWORDS):
                            return w_id
            except Exception as e:
                pass

        # 方法2: unitWeaponInfo (回退)
        try:
            r = self._session.get(
                f"{self.base}/ApiCtrl/api/unitWeaponInfo",
                params={"guid": guid},
                timeout=10,
            )
            data = r.json()
            if data.get("code") != 0:
                return None
            items = data.get("data", [])
            if not isinstance(items, list):
                return None
            for item in items:
                records = item.get("weaponRecord", [])
                if not isinstance(records, list):
                    continue
                for rec in records:
                    rec_name = rec.get("name", "")
                    if _match_keywords(rec_name, DECOY_WEAPON_KEYWORDS):
                        rec_dbid = rec.get(
                            "dbid", rec.get("weaponGuid", rec.get("id", ""))
                        )
                        if rec_dbid:
                            return rec_dbid
        except Exception as e:
            pass
        return None

    def get_decoy_count(self, guid):
        """
        获取诱饵弹剩余数量

        Returns:
            (current, max) 元组, 获取失败返回 (None, None)
        """
        try:
            r = self._session.get(
                f"{self.base}/ApiCtrl/api/unitWeaponInfo",
                params={"guid": guid},
                timeout=10,
            )
            data = r.json()
            if data.get("code") != 0:
                return None, None
            items = data.get("data", [])
            if not isinstance(items, list):
                return None, None
            for item in items:
                records = item.get("weaponRecord", [])
                if not isinstance(records, list):
                    continue
                for rec in records:
                    name = rec.get("name", "")
                    if _match_keywords(name, DECOY_WEAPON_KEYWORDS):
                        cur_num = rec.get("curNum", 0)
                        parsed = parse_cur_num(cur_num)
                        if parsed is not None:
                            # 尝试解析 max
                            if isinstance(cur_num, str):
                                m = re.match(
                                    r"\((\d+)/(\d+)\)", cur_num
                                )
                                if m:
                                    return int(m.group(1)), int(m.group(2))
                            return parsed, parsed
            return None, None
        except Exception as e:
            return None, None
