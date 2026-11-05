# 墨子强化学习环境接口

`mozi_rl` 是独立于当前 Agent 和行为树的研究 SDK。研究者可以把自己的策略接到同一个墨子想定，通过 `reset → step → reward → episode` 收集轨迹。已有 Agent/行为树可以另行作为基线策略，但环境本身不执行它们。核心实现位于 `src/rl_env`，公开导入路径为 `mozi_rl`。

## 接口

```python
from mozi_rl import make_env

env = make_env(
    "你的想定文件名.xml",
    side_name="蓝",
    frames_per_step=1,
    episode_duration_sec=3600,
    include_weapon_status=True,
    trajectory_path="run_data/episode.jsonl",
)
try:
    obs, info = env.reset()
    done = False
    while not done:
        action = None  # 换成研究者的策略输出；None 表示本步不下新命令
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
finally:
    env.close()
```

在项目根目录运行 `python -m pip install -e .` 即可安装 SDK。环境需要独占一个墨子实例；不要同时启动 `run_mozi.py` 或另一个训练进程控制相同实例。`reset` 会重新加载想定，`close` 关闭本环境的连接。

在线连通性验证可运行 `python -m examples.mozi_rl_quickstart 你的想定文件名.xml --steps 3`。这个示例会真正重载想定并启动/暂停推演，请只在专用实例上运行。

返回值与 Gymnasium 的 `reset`/`step` 约定相同，但观测和动作是**可变长度的 JSON 字典**，并没有声明固定形状的 `observation_space`/`action_space`。接入需要固定张量形状的 PPO/DQN 实现时，应由研究者明确设置单位/接触目标容量、排序、填充、掩码和溢出处理，避免把未探测敌人写进观测。

## 观测

`obs` 包含：

| 字段 | 内容 |
| --- | --- |
| `scenario_name`, `side_name`, `frame_seq`, `sim_time_sec` | 想定、阵营、WS 帧序号、游戏秒数 |
| `units` | 所选阵营的活动单位及机场内飞机，含 ID、类型、位置、高度、速度、航向、损伤、燃油、停放状态；缺失字段为 `null` |
| `contacts` | **该阵营自己探测到**的接触目标及已知字段；不读取敌方 `activeUnits` |
| `weapon_status_by_unit` | 可选；`include_weapon_status=True` 时逐架查询当前飞机挂载，查询失败为 `null`，会增加每步 REST 耗时 |

观测使用同一份 WS 态势帧读取单位和接触目标。游戏时钟来自 REST `GetScenarioTime`，可能比 WS 帧稍新；每一步返回实际 `sim_delta_sec`。

## 动作

`step` 接受一个动作、动作列表或 `None`。动作列表先整体校验，再顺序下发。可用类型：

```json
{"type":"takeoff","unit_id":"己方飞机ID"}
{"type":"course","unit_id":"己方单位ID","waypoints":[{"lat":30.0,"lon":80.0}]}
{"type":"heading","unit_id":"己方单位ID","heading_deg":90,"distance_km":50}
{"type":"speed","unit_id":"己方单位ID","speed_kmh":600}
{"type":"altitude","unit_id":"己方飞机ID","altitude_m":9000}
{"type":"radar","unit_id":"己方单位ID","enabled":true}
{"type":"weapon_control","unit_id":"己方单位ID","air_mode":"Tight","surface_mode":"Hold"}
{"type":"weapon_assignment","unit_id":"己方单位ID","target_id":"已探测接触ID","weapon_dbid":"1234","count":1}
```

`unit_id` 必须来自本轮 `units`，攻击 `target_id` 必须来自本轮 `contacts`。这只是格式与观测可见性校验；武器库存、射程、单位能力等仍由游戏接口决定。命令返回成功表示中间件接受，不代表飞机已经起飞、武器已发射或目标已命中；实际结果取决于后续观测。若列表中某条命令失败，先前成功的命令不能回滚，环境抛出 `CommandRejected` 并要求重新 `reset`。

动作由 SDK 解码后直接调用墨子接口：`heading` 以当前坐标计算航点，再走 `PlottedCourse`；`speed`/`altitude` 走 `SpeedAlt`；`radar` 走 `unitSensors`；`weapon_control` 走 `DoctrineInfo`；`weapon_assignment` 走手动武器分配接口。参考项目 `飞机空战1V1` 的离散 5 维动作可以在策略侧映射为以上动作列表；SDK 不把 1V1 的速度档位、高度档位或奖励系数强加给其他想定。

## 时间、奖励与终止

`reset` 加载想定并启动一次推演。此后每次 `step` 先下动作，再等待至少 `frames_per_step` 个新的 WS 态势帧；**运行期间不暂停推演**。这是逐帧状态转移接口，不承诺每帧有固定游戏秒数。超时会抛异常且本轮样本无效。`info` 同时返回实际跨过的帧数与游戏秒数。

对环境全局状态建模时，可按 MDP 使用逐帧转移。默认 `units` 和 `contacts` 仅来自己方视角；由于敌情可能未探测，策略面对的是部分可观测问题。现有 WS 字段也未必包含墨子内部全部隐状态，因此 SDK 不宣称数学上已验证严格马尔可夫性。

默认奖励为 0。可传入 `reward_fn(previous_obs, actions, current_obs, info) -> (reward, components)`；`AttritionDiscoveryReward` 是简单示例，不是通用胜负评分。可传入 `terminal_fn(current_obs, info) -> bool` 定义想定目标达成。达到 `episode_duration_sec` 或 `max_steps` 返回 `truncated=True`。目前没有一个经过核实、跨想定通用的“想定胜利”信号，所以默认不会凭空宣布胜利。

`reset(seed=...)` 接受统一 API 参数，但墨子加载接口尚未提供经过验证的随机种子设置；返回的 `info.seed_applied=False`。要比较算法，请固定想定、墨子版本、倍速和外部随机源，并保存 JSONL 轨迹。记录器写出每一步的原观测、动作、下一观测、奖励和实际游戏秒数。

## 目前边界

本模块已提供在线适配、重置/步进、己方视角观测、基础动作、奖励/终止扩展、轨迹记录及离线契约测试。尚未实测当前在线想定的完整 episode；也尚未实现并行墨子实例调度、跨想定统一胜负评分、固定张量编码和多智能体 PettingZoo 接口。这些需要对具体想定与部署方式确认后逐项加入。
