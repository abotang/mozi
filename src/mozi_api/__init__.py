from .adapter import ExistingConnectorAdapter, MoziAdapter


def create_mozi_connector(*args, **kwargs):
    """按需加载实时网络依赖；离线规划不需要安装 requests/websocket-client。"""
    try:
        from .connector import MoziConnector
    except ModuleNotFoundError as exc:
        if exc.name in {"requests", "websocket"}:
            raise RuntimeError("实时模式需要先运行：python -m pip install -r requirements.txt") from exc
        raise
    return MoziConnector(*args, **kwargs)


__all__ = ["ExistingConnectorAdapter", "MoziAdapter", "create_mozi_connector"]
