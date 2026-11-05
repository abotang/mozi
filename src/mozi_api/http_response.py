"""中间件HTTP应答适配；传输受理和游戏动作生效分别确认。"""
import json
import re
from urllib.parse import urlsplit, urlunsplit

import requests


SIMULATION_CONTROLS = frozenset(('StartSimulation', 'PauseSimulation'))


class MiddlewareProtocolError(RuntimeError):
    """接口返回了错误状态、网页或无法用于当前操作的应答。"""


class MiddlewareTransportError(RuntimeError):
    """请求传输失败；控制指令可能已到达，调用方不能自动重发。"""


def safe_url(url):
    """日志不包含URL中的口令、查询参数和片段。"""
    parsed = urlsplit(url)
    authority = (parsed.hostname or '')
    if ':' in authority:
        authority = '[' + authority + ']'
    if parsed.port is not None:
        authority += ':' + str(parsed.port)
    return urlunsplit((parsed.scheme, authority, parsed.path, '', ''))


def response_summary(response, method, url):
    text = response.content[:512].decode('utf-8-sig', errors='replace')
    text = re.sub(r'(?i)((?:password|token|secret|api[_-]?key)\s*["\']?\s*[:=]\s*["\']?)[^\s,"\'<>]+',
                  r'\1[已隐藏]', text)
    preview = ' '.join(text.split())[:200] or '（空响应）'
    content_type = response.headers.get('Content-Type', '未提供')
    return (f'{method} {safe_url(url)}；HTTP {response.status_code}；'
            f'Content-Type={content_type}；响应{len(response.content)}字节；摘要：{preview}')


def decode_middleware_response(response, method, url):
    endpoint = urlsplit(url).path.rstrip('/').rsplit('/', 1)[-1]
    is_simulation_control = method.upper() == 'GET' and endpoint in SIMULATION_CONTROLS
    summary = response_summary(response, method, url)
    if not 200 <= response.status_code < 300:
        raise MiddlewareProtocolError('中间件接口未成功返回：' + summary)
    text = response.content.decode('utf-8-sig', errors='replace').strip()
    content_type = response.headers.get('Content-Type', '').casefold()
    if 'text/html' in content_type or text.startswith('<'):
        raise MiddlewareProtocolError('中间件返回网页，请检查端口、登录或代理：' + summary)
    try:
        payload = json.loads(text)
    except (ValueError, TypeError) as exc:
        if not is_simulation_control:
            raise MiddlewareProtocolError('接口需要JSON对象，实际应答不符：' + summary) from exc
        payload = text or None
    if isinstance(payload, dict) and 'code' in payload:
        # 部分版本把控制接口的0写为字符串；数据接口仍保留原始结构。
        if is_simulation_control and payload['code'] == '0':
            payload = {**payload, 'code': 0}
        return payload
    if not is_simulation_control:
        raise MiddlewareProtocolError('接口需要带code的JSON对象，实际应答不符：' + summary)
    if payload is False or isinstance(payload, dict) and payload.get('success') is False:
        raise MiddlewareProtocolError('推演控制接口明确返回失败：' + summary)
    # 空应答、文字、true和无code对象只说明HTTP返回；绝不伪造code=0。
    # 开始推演必须由新的同想定WS态势确认，不能仅凭这份应答起飞。
    return {'http_accepted': True, 'confirmation_required': True, 'confirmed': False,
            'response_summary': summary}


def request_middleware(session, method, url, timeout=3, **kwargs):
    # 控制接口即使使用GET也不重试、不跟随重定向，避免重复或向登录页发送控制。
    kwargs.setdefault('allow_redirects', False)
    try:
        response = session.request(method, url, timeout=timeout, **kwargs)
    except requests.RequestException as exc:
        raise MiddlewareTransportError(
            f'{method} {safe_url(url)} 请求传输失败（{type(exc).__name__}）；'
            '控制结果未知，未自动重发，请以当前态势确认。') from exc
    return decode_middleware_response(response, method, url)
