"""武器控制与攻击分配；成功表示请求被接受，命中结果须读后续态势。"""


class WeaponCommands:
    """基础控制方法组，由 MoziConnector 组合使用；不单独实例化。"""

    def set_weapon_control(self, unit_guid, mode="Hold", air_mode="Hold"):
        """
        设置武器控制模式 (DoctrineInfo API)

        Args:
            unit_guid: 单元 GUID
            mode:     对海/对地 "Hold" / "Tight" / "Free"
            air_mode: 对空 (默认=mode)

        Hold→2 (限制开火), Tight→1 (谨慎开火), Free→0 (自由开火)
        """
        wcs_map = {"Hold": "2", "Tight": "1", "Free": "0"}
        wcs_surface = wcs_map.get(mode, "1")
        wcs_air = wcs_map.get(air_mode, "1")
        try:
            r = self._session.post(
                f"{self.base}/ApiCtrl/api/DoctrineInfo",
                json={
                    "Guid": unit_guid,
                    "SubjectType": "Unit",
                    "IsEscort": False,
                    "Value": {
                        "General": {
                            "ROE": {
                                "WCS_Surface": wcs_surface,
                                "WCS_Air": wcs_air,
                                "WCS_Land": wcs_surface,
                                "WCS_Submarine": "1",
                            }
                        }
                    },
                },
                timeout=10,
            )
            result = r.json()
            if result.get("code") == 0:
                pass
            else:
                pass
            return result
        except Exception as e:
            return {"code": -1, "message": str(e)}


    def weapon_assignment(self, strike_guid, weapon_dbid,
                          target_guid=None, target_lon=None,
                          target_lat=None,
                          assign_type="add", count=1):
        """
        手动接战 — 分配武器到目标

        Args:
            strike_guid:  打击平台 GUID
            weapon_dbid:  武器 DBID
            target_guid:  目标平台 GUID (与 lon/lat 二选一)
            target_lon:   目标经度 (纯方位攻击)
            target_lat:   目标纬度 (纯方位攻击)
            assign_type:  "add" / "addAll" / "addChoose" / "addSalvo"
            count:        分配数量 (仅 add/addChoose 时有效)

        Returns:
            dict: API 响应
        """
        payload = {
            "strikePlatformId": strike_guid,
            "weaponId": weapon_dbid,
            "type": assign_type,
        }
        if target_guid:
            payload["targetPlatformId"] = target_guid
        elif target_lon is not None and target_lat is not None:
            payload["targetLon"] = target_lon
            payload["targetLat"] = target_lat
        if assign_type in ("add", "addChoose"):
            payload["number"] = count

        try:
            r = self._session.post(
                f"{self.base}/ApiCtrl/api/weapon-assignment",
                json=payload,
                timeout=10,
            )
            result = r.json()
            if result.get("code") == 0:
                pass
            else:
                pass
            return result
        except Exception as e:
            return {"code": -1, "execution_unknown": True, "message": str(e)}
