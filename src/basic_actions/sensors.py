"""传感器基础控制；负责雷达、电子干扰与电磁管控请求，不选择执行时机。"""


class SensorCommands:
    """基础控制方法组，由 MoziConnector 组合使用；不单独实例化。"""

    def set_radar(self, guid, radar_on):
        """
        设置雷达开关

        Args:
            guid: 单元 GUID
            radar_on: True=开机, False=关机
        """
        radar_str = "RADER=true" if radar_on else "RADER=false"
        try:
            r = self._session.post(
                f"{self.base}/ApiCtrl/api/unitSensors",
                json={
                    "guid": guid,
                    "type": "setCategorySwitch",
                    "categorySwitch": radar_str,
                },
                timeout=10,
            )
            return r.json()
        except Exception as e:
            return {"code": -1}


    def set_oecm(self, guid: str, enabled: bool) -> dict:
        """设置单元进攻性电子干扰（OECM）设备开关。

        Args:
            guid: 装有相应干扰设备的单元 GUID。
            enabled: True=开启，False=关闭；必须传布尔值。

        Returns:
            墨子原始业务响应；HTTP、通信或解析失败返回 code=-1。
            code=0 仅表示请求被接受，设备状态仍需从后续态势确认。

        本方法只设置设备类别开关，不自动修改电磁管控遵从或飞行状态。
        """
        if not isinstance(enabled, bool):
            raise ValueError("enabled 必须为布尔值（True 或 False）")
        try:
            response = self._session.post(
                f"{self.base}/ApiCtrl/api/unitSensors",
                json={
                    "guid": guid,
                    "type": "setCategorySwitch",
                    "categorySwitch": "OECM=true" if enabled else "OECM=false",
                },
                timeout=10,
            )
            response.raise_for_status()
            result = response.json()
            if not isinstance(result, dict):
                return {"code": -1, "message": "电子干扰接口返回的不是 JSON 对象"}
            return result
        except Exception as exc:
            return {"code": -1, "message": str(exc)}


    def disable_emcon(self, guid):
        """关闭电磁管控遵从"""
        try:
            r = self._session.post(
                f"{self.base}/ApiCtrl/api/unitSensors",
                json={
                    "guid": guid,
                    "type": "setEMCON",
                    "complyElectromagnetic": "false",
                },
                timeout=10,
            )
            return r.json()
        except Exception as e:
            return {"code": -1}
