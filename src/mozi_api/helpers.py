"""墨子连接器使用的小型解析工具，随项目一起提供。"""

import re
from math import asin, cos, radians, sin, sqrt


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """两经纬度之间的大圆距离，单位千米。"""
    lat1, lon1, lat2, lon2 = map(radians, (lat1, lon1, lat2, lon2))
    value = sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2
    return 12742.0 * asin(min(1.0, sqrt(value)))


def match_keywords(name: str, keywords: tuple[str, ...]) -> bool:
    """名称包含任一关键词时返回真，不区分大小写。"""
    return bool(name and keywords) and any(word.lower() in name.lower() for word in keywords)


def parse_cur_num(value: int | str) -> int | None:
    """读取墨子弹药数量字段，支持整数、'3' 和 '(3/4)'。"""
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        match = re.fullmatch(r"\((\d+)/(\d+)\)", value)
        if match:
            return int(match.group(1))
        try:
            return int(value)
        except ValueError:
            pass
    return None
