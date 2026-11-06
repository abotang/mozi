# 墨子 API 与蓝方海空任务实测手册

> 文档来源：用户提供的 Apifox 项目“游杰-子房 API 接口（zifangweb）”及本机墨子服务实测。  
> 最后实测：2026-11-06，蓝方，想定 `11111111111111111111111111111`。  
> Apifox 入口：<https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376206074e0>

## 1. 结论

已读取并下载该 Apifox 项目的 **154 个接口文档**，并在重启后的想定中重新完成蓝方四类任务：

| 任务 | 任务 GUID | 单元 | 必需对象 | 实测结果 |
| --- | --- | --- | --- | --- |
| 飞机战斗巡逻 | `a04b5f0b-c5b0-4023-9fe9-09d58d9627cd` | F/A-18E `415888b4-4203-4d1b-b80a-1c8956b0f307` | 空中巡逻区 `{e41bb385-1e56-455d-9f60-23875b4668f2}` | 区域、规则、单元均回读成功 |
| 飞机对空打击 | `7c14e834-a475-4237-96b2-0cc2f4e11db8` | 主攻机 `40398342-c0f4-4b8c-9741-e11d3b53f763`；护航机 `47641b17-e450-4f55-ab59-431daa791c45` | 蓝方接触 `6700aeaa-35dd-4006-8ab5-f821991f4bd2`（空警-600 #11） | `targetList` 有目标，分配列表有 `[护航]` 标记 |
| 舰艇海上巡逻 | `0c744d3d-3b2a-4fc0-8ffd-a044cc8abf8a` | 伯克级驱逐舰-126 `70114345-48cf-4835-b19d-682d12353c15` | 海上巡逻区 `{adf30375-f151-4905-af1d-88850f6889a1}` | 当前主任务正确；舰艇已在区内实际航行 |
| 舰艇对海打击 | `25dfa3c9-ae72-484b-a1ad-53334505dd05` | 伯克级驱逐舰-125 `563a778d-9fe7-49e3-9a61-db4a371df4d5` | 蓝方接触 `85b6a4f4-25c8-44a2-84ce-a7b20ef52140`（003 航空母舰 #9） | `targetList` 回读成功 |

三架 F/A-18E 都已换成：`空对空：AIM-120D先进中程空对空导弹，标准战斗空中巡逻`。

舰艇巡逻还绑定了任务级航线：

- 出航航线：`31d3bdff-f05b-446a-96e5-acf354d321f3`
- 区内巡逻航线：`17094256-5c69-4f10-a2da-7947961f852e`
- 实测 10 秒内纬度 `17.0392697 → 17.0422721`，航速 `21.40 → 35.39`，经纬度位于区域 `[136.90,137.75] × [16.70,17.55]` 内。

## 2. 任务究竟需要区域、目标还是其它对象

这一步是创建任务最容易出错的地方。只创建任务名和分配单元，不等于任务完整。

| 任务类型 | 必需对象 | 典型 API 操作 | 验收字段 |
| --- | --- | --- | --- |
| `Patrol` 巡逻 | **巡逻区**；需要时再配警戒区、出航航线、区内巡逻航线 | `PatrolMissionRules` | `patrolmissionData.PatrolArea`、`PatrolArea_ID` |
| `Strike` 打击 | **蓝方已探测接触目标** | `AssignUnitAsTarget` | `strikeMissionData.targetList` |
| 护航 | 不是独立任务；把护航单元挂到具体打击任务 | `AssignUnitToEscort` | `assignedCombatUnit` 中的 `[护航]` |
| `Support` 支援 | 支援区域/航线；不同模板还需预警机、加油机、侦察机等匹配平台 | `SupportMissionRules` | `supportmissionData.area`、分配单元 |
| `Ferry` 转场 | **目的地基地 GUID** | `createMission.destination`、`FerryMissionRules` | 任务目的地、分配飞机 |
| `Mining` 布雷 | **布雷区**，以及具备布雷能力的单元 | `MiningMissionRules` | 区域、分配单元 |
| `MineClearing` 扫雷 | **扫雷区**，以及具备扫雷能力的单元 | `MineClearingMissionRules` | 区域、分配单元 |
| `Cargo` 投送 | **投送区/目的地 + 货物清单** | `CargoMissionRules`、`AddMountToUnload` 等 | 区域、货物、分配单元 |

### 区域类型 ID

| 大类 | 巡逻区 | 警戒区 | 其它常用区域 |
| --- | ---: | ---: | --- |
| 空中区域 | `405` | `106` | 侦查 `108`、加油 `109`、布雷 `111`、扫雷 `112`、预警 `407`、投送 `410` |
| 海上区域 | `413` | `414` | 布雷 `415`、扫雷 `416`、投送 `417` |
| 水下区域 | `418` | `419` | 布雷 `420` |
| 地面区域 | `421` | `422` | 预警 `423` |

## 3. 50 个任务模板与正确对象

以下映射来自实时接口 `GET /ApiCtrl/api/getAllConfiguredTasks`，不要凭中文名称猜 `mzType/mzSubType`，尤其注意 `Sub` 与 `SUB` 大小写不同。

### 3.1 航空兵任务（18）

| 模板 | `mzType` | `mzSubType` | 必需对象与适用单元 |
| --- | --- | --- | --- |
| 空中拦截 | Strike | Air | 空中接触目标；空优/截击机，空空挂载 |
| 空中突击 | Strike | land | 地面接触目标；攻击机/多用途战斗机，对地挂载 |
| 对海打击 | Strike | SEA | 水面接触目标；反舰平台、反舰挂载 |
| 航空反潜 | Strike | Sub | 潜艇接触目标；反潜机/直升机、反潜武器 |
| 战斗巡逻 | Patrol | AAW | 空中巡逻区；战斗机、空战挂载 |
| 对海巡逻 | Patrol | SUR_SEA | 海上/空中巡逻区；海上巡逻机或具备海搜能力的平台 |
| 对陆巡逻 | Patrol | SUR_LAND | 地面巡逻区；侦察/攻击平台 |
| 两栖巡逻 | Patrol | SUR_Mixed | 陆海混合巡逻区；多用途平台 |
| 反潜巡逻 | Patrol | SUB | 海上/水下反潜巡逻区；反潜平台 |
| 压制防空 | Patrol | SEAD | 巡逻/警戒区；SEAD/DEAD 挂载平台 |
| 控制巡逻 | Patrol | Sub | 海上控制巡逻区；按实时模板保留 `Sub` |
| 空中侦查 | Support | 空 | 侦查区/航线；侦察机、无人机、预警平台 |
| 空中预警 | Support | 空 | 预警区/航线；预警机 |
| 空中加油 | Support | 空 | 加油区/航线；加油机 |
| 转场飞行 | Ferry | 空 | 目的地基地；可转场飞机 |
| 航空布雷 | Mining | 空 | 布雷区；可携雷飞机 |
| 航空扫雷 | MineClearing | 空 | 扫雷区；具备扫雷能力的平台 |
| 空中投送 | Cargo | 空 | 投送区/目的地与货物；运输机/直升机 |

### 3.2 水面舰艇任务（13）

| 模板 | `mzType` | `mzSubType` | 必需对象与适用单元 |
| --- | --- | --- | --- |
| 舰艇防空 | Strike | Air | 空中接触目标；具备防空武器/传感器的舰艇 |
| 对岸攻击 | Strike | land | 地面接触目标；具备对陆导弹/舰炮的舰艇 |
| 对海攻击 | Strike | SEA | 水面接触目标；具备反舰武器的舰艇 |
| 舰艇反潜 | Strike | Sub | 潜艇接触目标；反潜舰艇 |
| 防空警戒 | Patrol | AAW | 海上警戒/巡逻区；防空舰艇 |
| 海上巡逻 | Patrol | SUR_SEA | **海上巡逻区**；水面舰艇 |
| 对陆警戒 | Patrol | SUR_LAND | 近岸/地面警戒区；具备对陆侦察能力的舰艇 |
| 陆海巡逻 | Patrol | SUR_Mixed | 陆海混合区；多用途舰艇 |
| 反潜巡逻 | Patrol | SUB | 反潜巡逻区；反潜舰艇 |
| 海潜巡防 | Patrol | Sub | 海潜控制区；按实时模板保留 `Sub` |
| 舰艇布雷 | Mining | 空 | 海上布雷区；布雷舰艇 |
| 舰艇扫雷 | MineClearing | 空 | 海上扫雷区；扫雷舰艇 |
| 海上投送 | Cargo | 空 | 海上投送区与货物；运输舰/两栖舰 |

### 3.3 潜艇任务（11）

| 模板 | `mzType` | `mzSubType` | 必需对象与适用单元 |
| --- | --- | --- | --- |
| 潜空作战 | Strike | Sub | 实时模板返回 `Sub`；必须以实际任务配置为准 |
| 对陆攻击 | Strike | land | 地面接触目标；具备对陆巡航导弹的潜艇 |
| 对海攻击 | Strike | SEA | 水面接触目标；攻击潜艇 |
| 潜艇反潜 | Strike | Sub | 潜艇接触目标；攻击潜艇 |
| 防空警戒 | Patrol | AAW | 水下/警戒区；仅适用于具备相应能力的平台 |
| 对海警戒 | Patrol | SUR_SEA | 水下/海上警戒区；潜艇 |
| 陆海巡逻 | Patrol | SUR_Mixed | 陆海混合警戒区；潜艇 |
| 反潜巡逻 | Patrol | SUB | 水下反潜巡逻区；潜艇 |
| 潜海巡逻 | Patrol | Sub | 水下控制区；按实时模板保留 `Sub` |
| 潜艇布雷 | Mining | 空 | 水下布雷区；具备布雷能力的潜艇 |
| 水下投送 | Cargo | 空 | 投送区与货物；特战/运输型潜艇 |

### 3.4 地面装备任务（8）

| 模板 | `mzType` | `mzSubType` | 必需对象与适用单元 |
| --- | --- | --- | --- |
| 地面防空 | Strike | Air | 空中接触目标；地空导弹/高炮单元 |
| 对陆攻击 | Strike | land | 地面接触目标；炮兵、导弹、装甲等 |
| 对海攻击 | Strike | SEA | 水面接触目标；岸舰导弹等 |
| 对空警戒 | Patrol | AAW | 地面警戒区；防空/雷达单元 |
| 对海警戒 | Patrol | SUR_SEA | 地面/海岸警戒区；岸基雷达等 |
| 对陆警戒 | Patrol | SUR_LAND | 地面巡逻/警戒区；地面侦察单元 |
| 陆海巡逻 | Patrol | SUR_Mixed | 陆海混合警戒区；岸防/侦察单元 |
| 地面预警 | Support | 空 | 地面预警区；雷达/预警单元 |

## 4. 正确调用顺序

### 4.1 基础地址与返回判定

- 主要 REST 前缀：`http://127.0.0.1:8050/ApiCtrl/api`
- 部分控制端文档写 `8082`；本机实测 `8050` 可用。
- Agent 接口前缀在部分资料中为 `/AgentApiCtrl/api`。
- 常见成功返回：HTTP 200 且 JSON `code == 0`。不能只看 HTTP 状态。

### 4.2 换挂载

1. `GET /air-operations/loadout?Guid=<飞机GUID>` 回读当前挂载。
2. 确认候选 `loadGuid` 与任务匹配。
3. `POST /air-operations/ConfirmDP`。
4. 再次 GET 回读 `LoadoutName`，不能只相信 POST 成功。

```json
{
  "Units": ["飞机GUID"],
  "loadGuid": "hsfw-dataloadout-0000000028899",
  "option": "automatic",
  "quickly": false,
  "index": -1
}
```

### 4.3 建巡逻区

1. `POST /ReferencePoint` 创建至少 3 个参考点，推荐 4 点矩形。
2. `POST /ScenArea`，`option=addArea`，选择正确 `areaType`。
3. `GET /ScenArea?type=all` 回读区域和 `missionList`。

```json
{
  "option": "addArea",
  "side": "蓝方",
  "areaType": "413",
  "area_name": "蓝方-舰艇海上巡逻区",
  "area_remark": "海上巡逻任务区域",
  "area_points": [
    {"id": "参考点GUID", "x": 137.0, "y": 17.0}
  ]
}
```

### 4.4 建巡逻任务

必须按这个顺序：

1. `createMission`
2. `PatrolMissionRules` 写入 `PatrolArea_ID/AlertArea_ID`，必要时写任务航线
3. `AssignUnitToMission`
4. GET `/Mission?Guid=...` 回读

原因：本机版本实测中，更新 `PatrolMissionRules` 会清空已有分配，因此不能先分配单元再写规则。

```json
{
  "type": "createMission",
  "createMission": {
    "name": "蓝方-舰艇海上巡逻",
    "sideGuid": "bc47d6c9-2492-46a8-abe4-bbe39dc65aa8",
    "type": "Patrol",
    "classify": "SUR_SEA",
    "status": true,
    "isOpenMissionWindows": false,
    "task_id": "blue-sea-patrol",
    "TreeParentID": "0"
  }
}
```

```json
{
  "type": "PatrolMissionRules",
  "MissionGuid": "任务GUID",
  "Rules": {
    "PatrolArea_ID": "{区域GUID}",
    "AlertArea_ID": "{区域GUID}",
    "SideWay": "出航航线GUID",
    "PatrolAreaSideWay": "区内巡逻航线GUID",
    "GroupSize": "1",
    "UseGroupSizeHardLimit": false,
    "TransitThrottle_Ship": "2",
    "StationThrottle_Ship": "2"
  }
}
```

### 4.5 建打击任务与选择目标

打击目标必须是**蓝方 `contacts` 里的接触 GUID**，不能直接使用红方 `activeUnits` GUID。

1. 从蓝方态势帧或接触接口读取 contacts。
2. 按 `UnitType` 匹配任务：`Air`→Aircraft，`SEA`→Ship，`Sub`→Submarine，`land`→Facility/地面接触。
3. 创建 `Strike` 任务。
4. `AssignUnitToMission` 分配主攻单元。
5. 有护航时调用 `AssignUnitToEscort`。
6. `AssignUnitAsTarget` 绑定目标接触。
7. GET Mission，确认 `strikeMissionData.targetList` 非空。

```json
{
  "type": "AssignUnitAsTarget",
  "MissionGuid": "打击任务GUID",
  "Units": ["蓝方接触GUID"]
}
```

```json
{
  "type": "AssignUnitToEscort",
  "MissionGuid": "打击任务GUID",
  "Units": ["护航机GUID"]
}
```

目标接触可能因丢失、被摧毁或想定重启而消失。`code=101, message=目标不存在` 时，必须重新读取蓝方 contacts，不能继续使用旧 GUID。

### 4.6 舰艇航线注意事项

本机版本的巡逻任务即使已绑定区域，若任务级航线保持“默认”，水面舰艇可能沿原航向航行。稳定做法：

1. `POST /routeLineManage/routeLine-status` 创建 `routeType=0` 的出航航线与区内巡逻航线。
2. `POST /routeLineManage/wayPoints-status` 添加航线点。
3. 再调用 `updataPlanWayPoint`，把航线点 `throttle` 从默认 `0` 改为巡航档 `2`。
4. 在 `PatrolMissionRules` 中写实时回读字段 `SideWay` 和 `PatrolAreaSideWay`。

文档样例还出现 `ShipAndSubWay/PatrolAreaShipAndSubWay`，但本机版本写入后没有回读；实际有效字段是 `SideWay/PatrolAreaSideWay`。

## 5. 验收清单

### 巡逻任务

- `missionBasicData.assignedCombatUnit` 包含预期单元。
- `patrolmissionData.PatrolArea` 至少 3 点。
- `PatrolArea_ID` 是预期区域 GUID。
- 舰艇任务应回读 `SideWay/PatrolAreaSideWay`。
- `GET /GetUnitToMissions?Guid=<单元>` 的 `UnitMission` 等于任务 GUID。
- 推演时钟确实前进；必要时调用 `GET /StartSimulation`。
- 态势帧中速度或经纬度实际变化。

### 打击任务

- 主攻单元存在。
- `strikeMissionData.targetList` 非空且类型与任务一致。
- 护航任务在分配标签中出现 `[护航]`。
- 飞机挂载与任务一致。

## 6. 重要陷阱

1. **想定重启后，任务、区域、接触 GUID 全部重新获取。** 旧 GUID 不可复用。
2. `simStatus=1` 不足以证明时钟正在走；同时比较两次 `GetScenarioTime.CurrentTime`。
3. `StartSimulation` 是 GET，但会改变状态，不能当普通查询重试。
4. `PatrolMissionRules` 可能清空已分配单元；规则在前，分配在后。
5. 新建航线点默认油门可能是 `0`；必须回读 `routeDetailList`。
6. 区域坐标中 `x=经度`、`y=纬度`；航线点是 `longitude/latitude`。
7. 打击目标用己方接触 GUID，不是敌真实单元 GUID。
8. 成功返回只代表中间件接受，最终要靠任务详情与态势位移验收。
9. `Sub` 与 `SUB` 是不同模板值，必须按实时 `getAllConfiguredTasks` 原样使用。

## 7. 本地资料

- 全量 154 个 Apifox 原始 Markdown：`C:\Users\hs123\Desktop\墨子任务调度架构\api_docs`
- Apifox 全量索引：`C:\Users\hs123\Desktop\墨子任务调度架构\apifox_llms.txt`
- 扩展聚合参考：`C:\Users\hs123\Desktop\墨子任务调度架构\docs\mozi_api_reference\all_api_reference.md`
- 本轮最终实测结果：`C:\Users\hs123\Desktop\墨子任务调度架构\tmp\mozi_recreate_blue_air_ship_tasks_result.json`
- 舰艇位移样本：`C:\Users\hs123\Desktop\墨子任务调度架构\tmp\mozi_ship_movement_result.json`

## 8. 用户提供 Apifox 的全量 API 索引

共 **150** 个接口。每个接口的完整 OpenAPI 原文已保存在 `api_docs` 目录。

| # | 分类 | 名称 | 方法 | 路径 | 文档 | 备注 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | 航线管理相关 | 航线管理器航线信息操作 | `POST` | `/routeLineManage/wayPoints-status` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370681780e0.md) |  |
| 2 | 航线管理相关 | 航线管理器界面操作 | `POST` | `/routeLineManage/routeLine-status` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370490984e0.md) |  |
| 3 | 航线管理相关 | 获取航线管理界面数据 | `GET` | `/routeLineManage` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/369939064e0.md) |  |
| 4 | 航线管理相关 | 获取航线点信息 | `GET` | `/routeDetailList` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370407978e0.md) |  |
| 5 | 空中行动、停靠行动相关 | 停靠行动界面操作 | `POST` | `/ship-operations/ship-status` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/369659282e0.md) |  |
| 6 | 空中行动、停靠行动相关 | 获取停靠行动界面数据 | `GET` | `/ship-operations` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/369586746e0.md) |  |
| 7 | 空中行动、停靠行动相关 | 空中行动界面操作 | `POST` | `/air-operations/aircraft-status` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/366580944e0.md) | 暂时只开发了单机出动、编组出动，其他功能正在开发 |
| 8 | 空中行动、停靠行动相关 | 获取空中行动界面数据 | `GET` | `/air-operations` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/365659907e0.md) |  |
| 9 | 空中行动、停靠行动相关 | 批量添加单元接口 | `POST` | `/addUnitOperation/multiHandle` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370664859e0.md) | 添加机场飞机，舰船停靠 |
| 10 | 空中行动、停靠行动相关 | 删除基地已有单元接口 | `POST` | `/addUnitOperation/DelUnits` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/371048698e0.md) |  |
| 11 | 空中行动、停靠行动相关 | 单元数量修改接口 | `POST` | `/addUnitOperation/modifyNumber` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/371049233e0.md) | 修改机场中某类型的单元数量 |
| 12 | 空中行动、停靠行动相关 | 获取飞机出动准备界面数据 | `POST` | `/air-operations/dispatchPreparation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/371520679e0.md) |  |
| 13 | 空中行动、停靠行动相关 | 确认出动准备接口 | `POST` | `/air-operations/ConfirmDP` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/372233814e0.md) |  |
| 14 | 空中行动、停靠行动相关 | 获取基地中已有单元数据的接口 | `GET` | `/air-operations/getBaseUnitData` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/373156869e0.md) |  |
| 15 | 空中行动、停靠行动相关 | 获取当前挂载信息 | `GET` | `/air-operations/loadout` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/375693713e0.md) |  |
| 16 | 想定相关 | 想定操作 | `POST` | `/ScenarioOperation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/367979321e0.md) |  |
| 17 | 想定相关 | 获取想定列表 | `GET` | `/GetScenarioFile` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370913470e0.md) |  |
| 18 | 想定相关 | 编辑推演方接口 | `POST` | `/sideOperation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/372636382e0.md) |  |
| 19 | 想定相关 | 获取推演方界面数据接口 | `GET` | `/sideOperation/getSideData` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/373037184e0.md) | 返回服务端支持的颜色     ，返回  推演方关系 |
| 20 | 想定相关 | 获取想定时间 | `GET` | `/GetScenarioTime` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376492528e0.md) |  |
| 21 | 想定相关 | 设置想定时间 | `POST` | `/SetScenarioTime` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376607743e0.md) |  |
| 22 | 想定相关 | 获取想定描述 | `GET` | `/GetScenarioDescription` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376646076e0.md) |  |
| 23 | 想定相关 | 设置想定描述 | `POST` | `/SetScenarioDescription` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376742420e0.md) |  |
| 24 | 想定相关 | 获取天气信息 | `GET` | `/GetWeather` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377301257e0.md) |  |
| 25 | 想定相关 | 设置天气信息 | `POST` | `/SetWeather` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377320506e0.md) |  |
| 26 | 想定相关 | 获取某个想定信息 | `GET` | `/GetScenarioDescriptionFile` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380375222e0.md) |  |
| 27 | 想定相关 | 加载想定接口 | `GET` | `/LoadScenario` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/430598374e0.md) |  |
| 28 | 想定相关 | 获取想定基本信息 | `GET` | `/Scen` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/432911259e0.md) |  |
| 29 | 任务相关 | 获取任务甘特图界面数据 | `GET` | `/MissionGant` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370919262e0.md) |  |
| 30 | 任务相关 | 任务甘特图界面操作 | `POST` | `/MissionGant` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370919291e0.md) |  |
| 31 | 任务相关 | 获取任务界面数据 | `GET` | `/Mission` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370919380e0.md) |  |
| 32 | 任务相关 | 任务界面操作 | `POST` | `/Mission` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370919450e0.md) |  |
| 33 | 任务相关 | 参考点操作 | `POST` | `/ReferencePoint` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376275614e0.md) | 参考点操作 |
| 34 | 任务相关 | 给单元分配任务   取消任务 接口 | `POST` | `/AssignUnitToMission` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377634146e0.md) | 分配任务 |
| 35 | 任务相关 | 获取任务列表 | `GET` | `/GetUnitToMissions` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380047404e0.md) |  |
| 36 | 兵力部署相关 | 获取添加单元界面数据结构接口 | `GET` | `/addUnitOperation/dataStructure` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/369106899e0.md) | 获取单元分类数、国家数据、推演方 |
| 37 | 兵力部署相关 | 获取添加单元界面数据 | `POST` | `/addUnitOperation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/367337685e0.md) | 目前只支持飞机，   请求参数category，分类后面需要改一下规则 |
| 38 | 兵力部署相关 | 获取飞机挂载方案数据 | `GET` | `/addUnitOperation/loadOut` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368756369e0.md) |  |
| 39 | 兵力部署相关 | 添加单元操作 | `POST` | `/addUnitOperation/handle` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368754374e0.md) |  |
| 40 | 兵力部署相关 | 删除单元接口 | `POST` | `/addUnitOperation/del` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376582101e0.md) |  |
| 41 | 兵力部署相关 | 复制兵力接口 | `POST` | `/addUnitOperation/copy` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376925364e0.md) |  |
| 42 | 兵力部署相关 | 移动兵力接口 | `POST` | `/addUnitOperation/moveUnit` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376926294e0.md) |  |
| 43 | 兵力部署相关 | 重命名兵力 | `POST` | `/addUnitOperation/reNameUnit` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376927342e0.md) |  |
| 44 | 兵力部署相关 | 获取所有卫星数据 | `GET` | `/addUnitOperation/getAllSatellite` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377779455e0.md) | 四层结构      国家》类型》卫星》轨道 |
| 45 | 兵力部署相关 | 添加卫星接口 | `POST` | `/addUnitOperation/addSatellites` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377998597e0.md) |  |
| 46 | 兵力部署相关 | 获取编辑货物界面数据接口 | `GET` | `/addUnitOperation/getAllGoods` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/378100724e0.md) |  |
| 47 | 兵力部署相关 | 获取当前实体内已有的货物 | `GET` | `/addUnitOperation/getUnitGoodsAlready` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/378176561e0.md) |  |
| 48 | 兵力部署相关 | 编辑单元货物 | `POST` | `/addUnitOperation/editGoods` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/378330543e0.md) | 添加或删除货物 |
| 49 | 兵力部署相关 | 删除本方所有兵力 | `POST` | `/addUnitOperation/delSideUnits` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/378557044e0.md) |  |
| 50 | 兵力部署相关 | 获取单元信息框的货物数据 | `GET` | `/getUnitCargoData` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389940170e0.md) |  |
| 51 | 兵力部署相关 | 界面配置操作 | `POST` | `/InterfaceRule` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/391356542e0.md) |  |
| 52 | 兵力部署相关 | 获取某个单元类型的rule | `GET` | `/getUnitTypeRule` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/391722739e0.md) |  |
| 53 | 条令 | 获取条令信息 | `GET` | `/DoctrineInfo` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376692659e0.md) |  |
| 54 | 条令 | 设置条令接口 | `POST` | `/DoctrineInfo` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377415052e0.md) |  |
| 55 | 条令 | 获取某个武器的使用规则 | `POST` | `/WeaponUsageRules` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392962066e0.md) |  |
| 56 | 区域相关 > 单元操作相关 | 油门高度深度设置 | `POST` | `/SpeedAlt` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/375953697e0.md) |  |
| 57 | 区域相关 > 单元操作相关 | 航线规划 | `POST` | `/PlottedCourse` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376050791e0.md) |  |
| 58 | 区域相关 > 单元操作相关 | 获取速度高度属性 | `GET` | `/SpeedAlt` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376206074e0.md) | 获取单元最大速度，最小速度，最大高度（深度），最小高度（深度） |
| 59 | 区域相关 > 单元操作相关 | 获取单元包络航线信息 | `GET` | `/GetunitEnvelopeInfoJson` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376309915e0.md) |  |
| 60 | 区域相关 > 单元操作相关 | 获取单元系统毁伤信息 | `GET` | `/GetUnitDamage` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376327578e0.md) |  |
| 61 | 区域相关 > 单元操作相关 | 设置单元毁伤状态 | `POST` | `/SetUnitDamage` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376391528e0.md) |  |
| 62 | 区域相关 > 单元操作相关 | 保持阵位-所选单元 | `POST` | `/holdPosition` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380301687e0.md) |  |
| 63 | 区域相关 > 单元操作相关 | 单元信息获取 | `GET` | `/GetunitInfoJson` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380919310e0.md) |  |
| 64 | 区域相关 > 单元操作相关 | 设置油量和留空时间接口 | `POST` | `/oilLevelAndIdleTime` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381160914e0.md) |  |
| 65 | 区域相关 > 单元操作相关 | 获取油量和留空时间数据接口 | `GET` | `/oilLevelAndIdleTime` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381164442e0.md) |  |
| 66 | 区域相关 > 单元操作相关 | 设置方位 | `POST` | `/Orientation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381286953e0.md) |  |
| 67 | 区域相关 > 单元操作相关 | 自动被探测到 | `POST` | `/Detected` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381296403e0.md) |  |
| 68 | 区域相关 > 单元操作相关 | 修改上级 | `POST` | `/PostSuperiorInfo` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381941922e0.md) |  |
| 69 | 区域相关 > 单元操作相关 | 返航 | `POST` | `/returnToBase` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389116571e0.md) |  |
| 70 | 区域相关 > 单元操作相关 | 补给 | `POST` | `/supply` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389151328e0.md) |  |
| 71 | 区域相关 > 单元操作相关 | 获取有加油机的支援任务 | `GET` | `/getMissionTanker` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389168832e0.md) |  |
| 72 | 区域相关 > 单元操作相关 | 选择新基地 | `POST` | `/selectNewBase` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389472532e0.md) |  |
| 73 | 区域相关 > 单元操作相关 | 武器预设航线设置 | `POST` | `/weaponPresetRoute` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/426759700e0.md) |  |
| 74 | 区域相关 | 获取区域 | `GET` | `/GetZone` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/379046381e0.md) |  |
| 75 | 区域相关 | 设置区域 | `POST` | `/SetZone` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/379225921e0.md) |  |
| 76 | 兵力分析与统计 | 获取战损统计 | `GET` | `/GetLossesAndExpenditures` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380614132e0.md) |  |
| 77 | 反潜搜索行动相关 | 投放被动声呐浮标 | `POST` | `/Anti-SubOperation/deployPassiveSonar` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381489735e0.md) |  |
| 78 | 反潜搜索行动相关 | 投放主动声呐浮标 | `POST` | `/Anti-SubOperation/deployActiveSonar` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381560752e0.md) |  |
| 79 | 反潜搜索行动相关 | 部署吊放声呐 | `POST` | `/Anti-SubOperation/deployDippingSonar` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381567643e0.md) |  |
| 80 | 传感器相关 | 单元传感器界面数据 | `GET` | `/unitSensors` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/367896942e0.md) |  |
| 81 | 传感器相关 | 单元传感器界面操作 | `POST` | `/unitSensors` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/367949477e0.md) |  |
| 82 | 攻击作战行动 | 自动接战目标 | `POST` | `/autoFightToContact` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368078551e0.md) |  |
| 83 | 攻击作战行动 | 放弃指定目标 | `POST` | `/giveUpFightAim` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368083350e0.md) | 放弃对指定目标进行攻击 |
| 84 | 攻击作战行动 | 脱离接战（放弃所有目标） | `POST` | `/offFight` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368135752e0.md) |  |
| 85 | 攻击作战行动 | 攻击时忽略计划航线-针对所选单元 | `POST` | `/attackIgnorePlanLineSelectedUnit` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368175947e0.md) |  |
| 86 | 攻击作战行动 | 攻击时忽略计划航线-针对所有单元 | `POST` | `/attackIgnorePlanLineAllUnit` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368178503e0.md) |  |
| 87 | 攻击作战行动 | 针对所有目标类型的武器控制状态-针对所选单元 | `POST` | `/allTargetTypeSelected` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368201800e0.md) | 控制指定单元对所有目标类型的攻击状态 |
| 88 | 攻击作战行动 | 针对所有目标类型的武器控制状态-针对所有单元 | `POST` | `/allTargetTypeAll` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368209458e0.md) | 控制所有单元对所有目标类型的攻击状态 |
| 89 | 攻击作战行动 | 武器分配（手动接战目标、纯方位攻击） | `POST` | `/weapon-assignment` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/366662224e0.md) | targetGuid传参即为手动接战目标，targetLon、targetLat传参即为纯方位攻击 |
| 90 | 攻击作战行动 | 武器分配界面（手动接战目标、纯方位攻击） | `GET` | `/weapon-assignment` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/366664598e0.md) | targetGuid传参即为手动接战目标，targetLon、targetLat传参即为纯方位攻击 |
| 91 | 攻击作战行动 | 为分配的武器设置航线 | `POST` | `/weaponWay/set` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/427097879e0.md) |  |
| 92 | 攻击作战行动 | 清空手动攻击的航路点 | `POST` | `/weaponWay/clear` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/427259006e0.md) |  |
| 93 | 武器详细列表相关 | 获取单元武器信息 | `GET` | `/unitWeaponInfo` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/385732564e0.md) | 获取武器的挂架    飞机会有挂载方案包含的数据 |
| 94 | 武器详细列表相关 | 获取武器记录数据-添加武器系统窗口数据获取 | `GET` | `/unitWeaponInfo/getWeaponRecordData` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387082260e0.md) |  |
| 95 | 武器详细列表相关 | 武器信息列表操作接口 | `POST` | `/unitWeaponInfo/operation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387054479e0.md) | 添加武器系统、删除武器系统、添加武器挂架、删除武器挂架，修改武器数量 |
| 96 | 武器详细列表相关 | 获取所有武器挂架 | `GET` | `/unitWeaponInfo/getMountList` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387333187e0.md) |  |
| 97 | 弹药库相关 | 获取所有弹药库数据 | `GET` | `/unitMagazine` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387361528e0.md) | 飞机、卫星、武器不显示弹药库 |
| 98 | 弹药库相关 | 获取添加弹药库界面数据 | `GET` | `/unitMagazine/getMagazines` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387380781e0.md) |  |
| 99 | 弹药库相关 | 弹药库数据操作接口 | `POST` | `/unitMagazine/operation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387385058e0.md) |  |
| 100 | 为制定区域布雷扫雷 | 布雷 | `POST` | `/DeployMine` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387859870e0.md) |  |
| 101 | 为制定区域布雷扫雷 | 查询雷 | `GET` | `/QueryMine` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387860962e0.md) |  |
| 102 | 为制定区域布雷扫雷 | 扫雷 | `POST` | `/ClearMine` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387861124e0.md) |  |
| 103 | 目标标识 | 标识目标立场 | `POST` | `/contact-Operation/markContact` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/388905536e0.md) |  |
| 104 | 目标标识 | 重新命名目标 | `POST` | `/contact-Operation/renameContact` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/388984687e0.md) |  |
| 105 | 目标标识 | 放弃目标 | `POST` | `/contact-Operation/abandonContact` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389000404e0.md) |  |
| 106 | 事件编辑 | 获取动作 | `GET` | `/events/actions` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392558719e0.md) | 获取条令规则模块-事件编辑模块下的动作 |
| 107 | 事件编辑 | 通过guid查看某一动作的详细信息 | `POST` | `/events/getAction` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393184745e0.md) |  |
| 108 | 事件编辑 | 通过guid修改动作 | `POST` | `/events/setAction` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393274008e0.md) |  |
| 109 | 事件编辑 | 添加动作 | `POST` | `/events/addAction` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394001207e0.md) |  |
| 110 | 事件编辑 | 通过guid删除动作 | `POST` | `/PostDelAction` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394204181e0.md) |  |
| 111 | 事件编辑 | 通过guid克隆动作 | `POST` | `/PostCloneAction` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394239540e0.md) |  |
| 112 | 事件编辑 | 获取条件 | `GET` | `/GetCondition` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394287048e0.md) | 获取条令规则模块-事件编辑模块下的动作 |
| 113 | 事件编辑 | 通过guid查看某一条件的详细信息  | `POST` | `/PostConditionByGUID` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394341015e0.md) |  |
| 114 | 事件编辑 | 添加条件 | `POST` | `/PostAddCondition` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394448958e0.md) |  |
| 115 | 事件编辑 | 通过guid修改条件 | `POST` | `/PostSetCondition` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394453302e0.md) |  |
| 116 | 事件编辑 | 通过guid克隆条件 | `POST` | `/PostCloneCondition` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394458508e0.md) |  |
| 117 | 事件编辑 | 通过guid删除条件 | `POST` | `/PostDelCondition` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394480172e0.md) |  |
| 118 | 事件编辑 | 获取触发器 | `GET` | `/GetTrigger` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394483374e0.md) |  |
| 119 | 常用单元配置 | 获取常用单元 | `GET` | `/oftenUnit` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392245725e0.md) |  |
| 120 | 常用单元配置 | 设置常用单元 | `POST` | `/oftenUnit` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392245810e0.md) |  |
| 121 | 常用单元配置 | 删除配置 | `POST` | `/delUnitOften` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392965369e0.md) |  |
| 122 | 编组操作 | 创建编组 | `POST` | `/groupOperation/addGroup` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393284223e0.md) |  |
| 123 | 编组操作 | 脱离编组 | `POST` | `/groupOperation/removeUnitFromGroup` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393356703e0.md) |  |
| 124 | 编组操作 | 获取编组编辑器界面数据 | `GET` | `/groupOperation/getGroupEditData` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393384746e0.md) |  |
| 125 | 编组操作 | 设置编队领队 | `POST` | `/groupOperation/setToGroupLead` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393870771e0.md) |  |
| 126 | 编组操作 | 设置编组队形 | `POST` | `/groupOperation/setGroupFormation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394104804e0.md) |  |
| 127 | 编组操作 | 设置单元高低速交替航行 | `POST` | `/groupOperation/setUnitSprintAndDrift` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/429129472e0.md) |  |
| 128 | 任务配置界面 | 获取所有配置的任务 | `GET` | `/getAllConfiguredTasks` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/395063223e0.md) |  |
| 129 | 任务配置界面 | 任务大类型的操作 | `POST` | `/ConfiguredTasks/MissionType` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/395114166e0.md) |  |
| 130 | 区域配置界面 | 获取区域数据 | `GET` | `/regionalManagement` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/395718697e0.md) |  |
| 131 | 区域配置界面 | 区域配置操作 | `POST` | `/regionalManagement` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/395846753e0.md) |  |
| 132 | 区域配置界面 | 获取当前想定的已有区域 | `GET` | `/ScenArea` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/396100861e0.md) |  |
| 133 | 区域配置界面 | 添加想定区域类型 | `POST` | `/ScenArea` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/396267696e0.md) |  |
| 134 | 存数据agent用 | 获取之前的记录 | `GET` | `/ChatRecord` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/397351354e0.md) |  |
| 135 | 存数据agent用 | 存数据 | `POST` | `/ChatRecord` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/397351707e0.md) |  |
| 136 | agent获取数据 | Dify获取当前想定时间 | `GET` | `/Dify_GetScenarioTime` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398497823e0.md) |  |
| 137 | agent获取数据 | Dify获取实体简要信息列表 | `GET` | `/Dify_GetUnitBriefInfoList` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398744801e0.md) |  |
| 138 | agent获取数据 | Dify获取实体列表 | `GET` | `/Dify_GetUnitInfoList` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398745631e0.md) |  |
| 139 | agent获取数据 | Dify获取探测目标列表 | `GET` | `/Dify_ContactInfoList` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398745793e0.md) |  |
| 140 | agent获取数据 | 获取探测单元简要信息 | `GET` | `/Dify_GetContactBriefInfo` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398746048e0.md) |  |
| 141 | agent获取数据 | 获取单元简要信息 | `GET` | `/Dify_GetUnitBriefInfo` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398746356e0.md) |  |
| 142 | agent获取数据 | 获取飞机单元简要信息 | `GET` | `/Dify_GetAircraftUnitBriefInfo` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398747115e0.md) |  |
| 143 | agent获取数据 | 获取实体详细信息 | `GET` | `/getUnitInfo` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/433466043e0.md) |  |
| 144 | 执行lua脚本 | 执行Lua脚本接口 | `POST` | `/ExecuteLuaScript` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398775444e0.md) |  |
| 145 | 任务编成树 | 任务编成 | `GET` | `/TaskCompilation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/399178102e0.md) |  |
| 146 | 任务编成树 | 设置任务编成树 | `POST` | `/TaskCompilation` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/399264652e0.md) |  |
| 147 | 指挥关系相关 | 指定实体为指挥所 | `POST` | `/appointCommand` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/399761139e0.md) |  |
| 148 | 指挥关系相关 | 获取指挥员 | `GET` | `/getCommanders` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/432637800e0.md) |  |
| 149 | 指挥关系相关 | 获取指挥所信息 | `GET` | `/getCommandPosts` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/432649881e0.md) |  |
| 150 | 航母仿真 | 获取某个航母的航空设施 | `GET` | `/GetAviationFacilitiesData` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/425188558e0.md) | 获取航母内的设施和某个设施内的飞机数量 |
| 151 | 未分类 | 设置是否获取消息输出 | `POST` | `/SetRecOutput` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/379929725e0.md) |  |
| 152 | 未分类 | 获取系统状态 | `GET` | `/status` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/385591723e0.md) | 是否加载想定；加载时返回推演方 |
| 153 | 未分类 | 读取当前是否按模板上限限制兵力数量 | `GET` | `/unitDeployment/templateMaxLimit` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/451783206e0.md) |  |
| 154 | 未分类 | 修改模板上限开关并写回配置 | `POST` | `/unitDeployment/templateMaxLimit` | [Apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/451783526e0.md) | 修改开关并写回 `config/config.ini` |
