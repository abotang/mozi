"""为项目内 MoziConnector 提供规划器和动作层使用的稳定接口。"""

from typing import Any


class MoziAdapter:
    def __init__(self, connector: Any):
        self.connector = connector

    def get_snapshot(self) -> Any:
        return self.connector.get_full_state()

    def consistent_read(self):
        """在一次规划读取中固定同一份墨子态势帧。"""
        return self.connector.consistent_read()

    def get_awacs_info(self) -> dict | None:
        return self.connector.get_awacs_info()

    def get_blue_aircraft_positions(self) -> list[tuple[float, float]]:
        return self.connector.get_blue_aircraft_positions()

    def get_blue_ground_positions(self) -> list[tuple[float, float]]:
        return self.connector.get_blue_ground_positions()

    def get_enemy_positions(self) -> list[tuple[float, float]]:
        return self.connector.get_enemy_positions()

    def get_aircraft(self) -> list[dict]:
        return self.connector.get_blue_aircraft()

    def get_contacts(self) -> list[dict]:
        return self.connector.get_contacts()

    def get_weapon_status(self, unit_guid: str) -> dict | None:
        return self.connector.get_weapon_status(unit_guid)

    def fly_to(self, unit_guid: str, lat: float, lon: float, altitude_m: float, speed_kmh: float) -> bool:
        return self.connector.fly_to_waypoint(unit_guid, lat, lon, altitude_m, speed_kmh)

    def fly_full_route(self, unit_guid: str, waypoints: list[tuple[float, float]], altitude_m: float, speed_kmh: float) -> bool:
        return self.connector.fly_full_route(unit_guid, waypoints, altitude_m, speed_kmh)

    def assign_weapon(self, unit_guid: str, weapon_dbid: str, target_guid: str) -> dict:
        return self.connector.weapon_assignment(unit_guid, weapon_dbid, target_guid=target_guid)


# 保留旧examples的导入名；两者现在都包装本项目内的连接器。
ExistingConnectorAdapter = MoziAdapter
