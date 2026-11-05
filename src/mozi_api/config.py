"""本项目的墨子连接config；不读取旧项目config，也不保存 API 密钥。"""

MOZI_HOST = "127.0.0.1"
MOZI_WS_PORT = 8050
MOZI_REST_PORT = 8082
MOZI_WS = f"ws://{MOZI_HOST}:{MOZI_WS_PORT}/ws"
MOZI_BASE = f"http://{MOZI_HOST}:{MOZI_REST_PORT}"

BLUE_SIDE_NAME = "蓝"
BLUE_SIDE_COLOR = "#0000ff"
RED_SIDE_COLOR = "#ff0000"
WS_MAX_RETRIES = 5
WS_BACKOFF_BASE = 2
WS_WAIT_TIMEOUT = 30
WS_FIRST_FRAME_TIMEOUT_SEC = 15.0
ALLOW_FIRST_SIDE_FALLBACK = False
SCENARIO_READY_MODE = "fighters"

AWACS_KEYWORDS = ("E-2", "E-3", "early_warning", "AWACS", "鹰眼", "Hawkeye", "KJ-", "空警", "预警机")
FIGHTER_KEYWORDS = ("战斗机", "F-16", "F-15", "F/A-18", "F-14", "Su-27", "Su-30", "J-10", "歼", "Fighter")
OCA_AIRCRAFT_KEYWORDS = ("OCA诱饵", "OCA扫荡", "OCA电子干扰")
DECOY_WEAPON_KEYWORDS = ("ADC", "诱饵", "decoy", "ADM-", "MALD")
GEN5_KEYWORDS = ("F-22", "F-35", "J-20", "歼-20", "Su-57", "FC-31", "歼-35")
MISSILE_KEYWORDS = ("导弹", "missile", "AAM", "SAM", "AIM", "PL-", "R-7")
WEAPON_TYPE_KEYWORDS = {
    "air_to_air": ("PL-", "霹雳", "AIM-", "R-73", "R-77", "R-27", "RVV-", "Р-73", "Р-77", "Р-27", "РВВ-", "SD-10", "METEOR", "IRIS-T", "AA-", "空空", "AAM"),
    "medium_range": ("AIM-120", "AMRAAM", "PL-12", "PL-15", "R-77", "R-27", "RVV-AE", "RVV-SD", "Р-77", "Р-27", "РВВ-АЕ", "РВВ-СД", "SD-10", "METEOR", "AA-10", "AA-12"),
    "short_range": ("AIM-9", "Sidewinder", "PL-8", "PL-10", "R-73", "R-60", "AA-8", "AA-11"),
}
CAP_FIGHTER_COUNT = 4
