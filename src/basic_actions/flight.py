"""起飞、航路、高度与速度；复用连接器的 base 地址和线程独立 REST 会话。"""


class FlightCommands:
    """基础控制方法组，由 MoziConnector 组合使用；不单独实例化。"""

    def takeoff(self, guid: str) -> dict:
        """请求指定机场内飞机起飞；响应成功仅代表中间件接受，仍须等待态势确认。"""
        response = self._session.post(
            f"{self.base}/ApiCtrl/api/air-operations/aircraft-status",
            json={"id": [guid], "type": "singleOperation", "params": ""},
            timeout=10,
        )
        response.raise_for_status()
        return response.json()


    def fly_to_waypoint(self, guid, lat, lon, alt_m, speed_kmh):
        """
        控制飞机飞往单个航路点

        Args:
            guid: 飞机 GUID
            lat, lon: 目标坐标
            alt_m: 目标高度 (m)
            speed_kmh: 目标速度 (km/h)

        Returns:
            bool: 指令发送成功
        """
        return self.fly_full_route(guid, [(lat, lon)], alt_m, speed_kmh)


    def fly_full_route(self, guid, waypoints_latlon, alt_m, speed_kmh):
        """
        一次性下发完整航路

        Args:
            guid: 飞机 GUID
            waypoints_latlon: [(lat, lon), ...]
            alt_m: 巡航高度 (m)
            speed_kmh: 巡航速度 (km/h)

        Returns:
            bool: 指令发送成功
        """
        courses = [{"lon": wp[1], "lat": wp[0]} for wp in waypoints_latlon]
        ok = self._send_course(guid, courses)
        if not ok:
            return False
        altitude_ok = self._send_altitude(guid, alt_m)
        speed_ok = self._send_speed(guid, speed_kmh)
        return altitude_ok and speed_ok


    def set_course(self, guid, waypoints):
        """
        设置航线 (PlottedCourse API)

        Args:
            guid: 飞机 GUID
            waypoints: [{"lon": float, "lat": float}, ...]
        """
        return self._send_course(guid, waypoints)


    def set_speed(self, guid, speed_kmh):
        """设置速度 (km/h)"""
        return self._send_speed(guid, speed_kmh)


    def set_altitude(self, guid, alt_m):
        """设置高度 (m)"""
        return self._send_altitude(guid, alt_m)


    def _send_course(self, guid, waypoints):
        """设置航线 (内部)"""
        try:
            r = self._session.post(
                f"{self.base}/ApiCtrl/api/PlottedCourse",
                json={"Guid": guid, "Courses": waypoints},
                timeout=10,
            )
            result = r.json()
            if result.get("code") != 0:
                return False
            return True
        except Exception as e:
            return False


    def _send_altitude(self, guid, alt_m):
        """设置高度 (内部)"""
        try:
            response = self._session.post(
                f"{self.base}/ApiCtrl/api/SpeedAlt",
                json={
                    "Type": "SetDesiredAlt",
                    "Value": str(int(alt_m)),
                    "UnitGuid": guid,
                },
                timeout=10,
            )
            return response.json().get("code") == 0
        except Exception as e:
            return False


    def _send_speed(self, guid, speed_kmh):
        """设置速度 (内部)"""
        try:
            response = self._session.post(
                f"{self.base}/ApiCtrl/api/SpeedAlt",
                json={
                    "Type": "SetDesiredSpeed",
                    "Value": str(int(speed_kmh)),
                    "UnitGuid": guid,
                },
                timeout=10,
            )
            return response.json().get("code") == 0
        except Exception as e:
            return False
