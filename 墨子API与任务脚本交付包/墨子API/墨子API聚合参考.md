# 全部接口说明

整理日期：2026-10-04。共 239 个方法/路径组合。来源、字段、examples和未确认事项逐项列出。

> 先读mozi_api_user_manual.md。路由占位不代表可直接调用；examples单位 ID 不能硬编码。

## Admin

### AdminCtrl::configReload (auto-generated placeholder)

**操作标识：** `POST /api/admin/config/reload`

**分类：** Admin

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/admin/config/reload`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


## AirNaval

### 获取航母所处位置的环境数据

**操作标识：** `GET /api/GetEnvironmentData`

**分类：** AirNaval

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/GetEnvironmentData`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 设置飞机快速出动

**操作标识：** `POST /api/air-operations/quickTurnaround`

**分类：** AirNaval

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/air-operations/quickTurnaround`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


## Event

### 工具

**操作标识：** `GET /api/GenerateRandomTime`

**分类：** Event

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/GenerateRandomTime`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### EventCtrl::GetEventAllEvents (auto-generated placeholder)

**操作标识：** `GET /api/events`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `s2t`；调用位置数量 1。

```javascript
function s2t(e){return nt({url:"/ApiCtrl/api/events",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::CreateEventCondition (auto-generated placeholder)

**操作标识：** `POST /api/events/addCondition`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/addCondition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `r2t`；调用位置数量 0。

```javascript
function r2t(e){return nt({url:"/ApiCtrl/api/events/addCondition",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::CreateEventTrigger (auto-generated placeholder)

**操作标识：** `POST /api/events/addTrigger`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/addTrigger`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Z1t`；调用位置数量 0。

```javascript
function Z1t(e){return nt({url:"/ApiCtrl/api/events/addTrigger",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### 事件条件

**操作标识：** `GET /api/events/conditions`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/conditions`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `t2t`；调用位置数量 1。

```javascript
function t2t(e){return nt({url:"/ApiCtrl/api/events/conditions",method:"get",params:e})}
```

源文件 `index-DUzbMa7B.js`，函数 `u2t`；调用位置数量 1。

```javascript
function u2t(e){return nt({url:"/ApiCtrl/api/events/conditions",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::CopyEventAction (auto-generated placeholder)

**操作标识：** `POST /api/events/copyAction`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/copyAction`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `q1t`；调用位置数量 1。

```javascript
function q1t(e){return nt({url:"/ApiCtrl/api/events/copyAction",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::CopyEventCondition (auto-generated placeholder)

**操作标识：** `POST /api/events/copyCondition`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/copyCondition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `i2t`；调用位置数量 1。

```javascript
function i2t(e){return nt({url:"/ApiCtrl/api/events/copyCondition",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::CopyEventTrigger (auto-generated placeholder)

**操作标识：** `POST /api/events/copyTrigger`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/copyTrigger`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `e2t`；调用位置数量 1。

```javascript
function e2t(e){return nt({url:"/ApiCtrl/api/events/copyTrigger",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::DelEventAction (auto-generated placeholder)

**操作标识：** `POST /api/events/delAction`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/delAction`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Y1t`；调用位置数量 1。

```javascript
function Y1t(e){return nt({url:"/ApiCtrl/api/events/delAction",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::DelEventCondition (auto-generated placeholder)

**操作标识：** `POST /api/events/delCondition`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/delCondition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `o2t`；调用位置数量 1。

```javascript
function o2t(e){return nt({url:"/ApiCtrl/api/events/delCondition",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::DelEventTrigger (auto-generated placeholder)

**操作标识：** `POST /api/events/delTrigger`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/delTrigger`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Q1t`；调用位置数量 1。

```javascript
function Q1t(e){return nt({url:"/ApiCtrl/api/events/delTrigger",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::GetEventAction (auto-generated placeholder)

**操作标识：** `GET /api/events/getAction`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/getAction`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `G1t`；调用位置数量 1。

```javascript
function G1t(e){return nt({url:"/ApiCtrl/api/events/getAction",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::GetEventCondition (auto-generated placeholder)

**操作标识：** `GET /api/events/getCondition`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/getCondition`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `n2t`；调用位置数量 1。

```javascript
function n2t(e){return nt({url:"/ApiCtrl/api/events/getCondition",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### 事件整体操作

**操作标识：** `GET /api/events/getEvent`

**分类：** Event

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/events/getEvent`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### EventCtrl::GetEventTrigger (auto-generated placeholder)

**操作标识：** `GET /api/events/getTrigger`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/getTrigger`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `X1t`；调用位置数量 1。

```javascript
function X1t(e){return nt({url:"/ApiCtrl/api/events/getTrigger",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::EditEventCondition (auto-generated placeholder)

**操作标识：** `POST /api/events/setCondition`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/setCondition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `a2t`；调用位置数量 0。

```javascript
function a2t(e){return nt({url:"/ApiCtrl/api/events/setCondition",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::SetEvent (auto-generated placeholder)

**操作标识：** `POST /api/events/setEvent`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/setEvent`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `l2t`；调用位置数量 3。

```javascript
function l2t(e){return nt({url:"/ApiCtrl/api/events/setEvent",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### EventCtrl::SetEventAction (auto-generated placeholder)

**操作标识：** `POST /api/events/setEventAction`

**分类：** Event

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/events/setEventAction`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### EventCtrl::SetEventCondition (auto-generated placeholder)

**操作标识：** `POST /api/events/setEventCondition`

**分类：** Event

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/events/setEventCondition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 事件关联 (Trigger/Condition/Action → Event)

**操作标识：** `POST /api/events/setEventTrigger`

**分类：** Event

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/events/setEventTrigger`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### EventCtrl::EditEventTrigger (auto-generated placeholder)

**操作标识：** `POST /api/events/setTrigger`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/setTrigger`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `J1t`；调用位置数量 0。

```javascript
function J1t(e){return nt({url:"/ApiCtrl/api/events/setTrigger",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### 事件触发器

**操作标识：** `GET /api/events/triggers`

**分类：** Event

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/events/triggers`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `j1t`；调用位置数量 2。

```javascript
function j1t(e){return nt({url:"/ApiCtrl/api/events/triggers",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


## File

### FileCtrl::downloadUploaded (auto-generated placeholder)

**操作标识：** `GET /api/file/download/{filename}`

**分类：** File

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/file/download/{filename}`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### FileCtrl::listUploads (auto-generated placeholder)

**操作标识：** `GET /api/file/list`

**分类：** File

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/file/list`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### FileCtrl::upload (auto-generated placeholder)

**操作标识：** `POST /api/file/upload`

**分类：** File

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/file/upload`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### FileCtrl::getVersionLog (auto-generated placeholder)

**操作标识：** `GET /api/file/versionlog`

**分类：** File

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/file/versionlog`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### FileCtrl::importDeployment (auto-generated placeholder)

**操作标识：** `POST /api/situation/import/deployment`

**分类：** File

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/situation/import/deployment`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


## Health

### HealthCtrl::aggregates (auto-generated placeholder)

**操作标识：** `GET /api/health/aggregates`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/health/aggregates`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### HealthCtrl::crash (auto-generated placeholder)

**操作标识：** `GET /api/health/crash`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/health/crash`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### HealthCtrl::forward (auto-generated placeholder)

**操作标识：** `GET /api/health/forward`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/health/forward`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### HealthCtrl::inbound (auto-generated placeholder)

**操作标识：** `GET /api/health/inbound`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/health/inbound`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### HealthCtrl::resources (auto-generated placeholder)

**操作标识：** `GET /api/health/resources`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/health/resources`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### HealthCtrl::simulationOutbound (auto-generated placeholder)

**操作标识：** `GET /api/health/simulation-outbound`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/health/simulation-outbound`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### HealthCtrl::metrics (auto-generated placeholder)

**操作标识：** `GET /api/metrics`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/metrics`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### HealthCtrl::metricsPrometheus (auto-generated placeholder)

**操作标识：** `GET /api/metrics/prometheus`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/metrics/prometheus`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### HealthCtrl::resources (auto-generated placeholder)

**操作标识：** `GET /api/system/resources`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/system/resources`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### HealthCtrl::telemetrySpans (auto-generated placeholder)

**操作标识：** `GET /api/telemetry/spans`

**分类：** Health

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/telemetry/spans`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


## Permission

### PermissionCtrl::getBindings (auto-generated placeholder)

**操作标识：** `GET /api/permission/bindings`

**分类：** Permission

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/permission/bindings`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### PermissionCtrl::putBindings (auto-generated placeholder)

**操作标识：** `PUT /api/permission/bindings`

**分类：** Permission

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/permission/bindings`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### PermissionCtrl::getEffective (auto-generated placeholder)

**操作标识：** `GET /api/permission/effective`

**分类：** Permission

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/permission/effective`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### PermissionCtrl::getRolePermissions (auto-generated placehold

**操作标识：** `GET /api/permission/modes/{modeKey}/roles/{roleKey}`

**分类：** Permission

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/permission/modes/{modeKey}/roles/{roleKey}`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### PermissionCtrl::putRolePermissions (auto-generated placehold

**操作标识：** `PUT /api/permission/modes/{modeKey}/roles/{roleKey}`

**分类：** Permission

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/permission/modes/{modeKey}/roles/{roleKey}`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### PermissionCtrl::resetRolePermissions (auto-generated placeho

**操作标识：** `POST /api/permission/modes/{modeKey}/roles/{roleKey}/reset`

**分类：** Permission

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/permission/modes/{modeKey}/roles/{roleKey}/reset`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### PermissionCtrl::getSchema (auto-generated placeholder)

**操作标识：** `GET /api/permission/schema`

**分类：** Permission

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/permission/schema`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


## Replay

### ReplayCtrl::getCurrentPosition (auto-generated placeholder)

**操作标识：** `GET /api/replay/getCurrentPosition`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/getCurrentPosition`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `z1t`；调用位置数量 1。

```javascript
function z1t(e){return nt({url:"/ApiCtrl/api/replay/getCurrentPosition",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ReplayCtrl::getTotalTime (auto-generated placeholder)

**操作标识：** `GET /api/replay/getTotalTime`

**分类：** Replay

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/replay/getTotalTime`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### ReplayCtrl::isRecording (auto-generated placeholder)

**操作标识：** `GET /api/replay/isRecording`

**分类：** Replay

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/replay/isRecording`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### ReplayCtrl::listFiles (auto-generated placeholder)

**操作标识：** `GET /api/replay/listFiles`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/listFiles`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `O1t`；调用位置数量 1。

```javascript
function O1t(e){return nt({url:"/ApiCtrl/api/replay/listFiles",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ReplayCtrl::openFile (auto-generated placeholder)

**操作标识：** `POST /api/replay/openFile`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/openFile`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `N1t`；调用位置数量 0。

```javascript
function N1t(e){return nt({url:"/ApiCtrl/api/replay/openFile",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ReplayCtrl::pause (auto-generated placeholder)

**操作标识：** `GET /api/replay/pause`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/pause`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `V1t`；调用位置数量 0。

```javascript
function V1t(e){return nt({url:"/ApiCtrl/api/replay/pause",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ReplayCtrl::play (auto-generated placeholder)

**操作标识：** `GET /api/replay/play`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/play`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `B1t`；调用位置数量 0。

```javascript
function B1t(e){return nt({url:"/ApiCtrl/api/replay/play",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ReplayCtrl::resume (auto-generated placeholder)

**操作标识：** `GET /api/replay/resume`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/resume`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `F1t`；调用位置数量 0。

```javascript
function F1t(e){return nt({url:"/ApiCtrl/api/replay/resume",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ReplayCtrl::setPosition (auto-generated placeholder)

**操作标识：** `POST /api/replay/setPosition`

**分类：** Replay

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/replay/setPosition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### ReplayCtrl::setSpeed (auto-generated placeholder)

**操作标识：** `POST /api/replay/setSpeed`

**分类：** Replay

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/replay/setSpeed`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### ReplayCtrl::startRecording (auto-generated placeholder)

**操作标识：** `GET /api/replay/startRecording`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/startRecording`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `P1t`；调用位置数量 0。

```javascript
function P1t(e){return nt({url:"/ApiCtrl/api/replay/startRecording",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ReplayCtrl::getStatus (auto-generated placeholder)

**操作标识：** `GET /api/replay/status`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/status`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `H1t`；调用位置数量 1。

```javascript
function H1t(e){return nt({url:"/ApiCtrl/api/replay/status",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ReplayCtrl::stop (auto-generated placeholder)

**操作标识：** `GET /api/replay/stop`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/stop`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `$1t`；调用位置数量 0。

```javascript
function $1t(e){return nt({url:"/ApiCtrl/api/replay/stop",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ReplayCtrl::stopRecording (auto-generated placeholder)

**操作标识：** `GET /api/replay/stopRecording`

**分类：** Replay

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/replay/stopRecording`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `R1t`；调用位置数量 0。

```javascript
function R1t(e){return nt({url:"/ApiCtrl/api/replay/stopRecording",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


## Scenario

### ScenarioCtrl::PauseSimulation (auto-generated placeholder)

**操作标识：** `GET /api/PauseSimulation`

**分类：** Scenario

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/PauseSimulation`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `eU`；调用位置数量 1。

```javascript
function eU(n){return G5({url:"/ApiCtrl/api/PauseSimulation",method:"get",params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

- 现有项目已按此 GET 接口实现墨子暂停；本次只核对调用代码，未改变运行状态。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ScenarioCtrl::SimCompression (auto-generated placeholder)

**操作标识：** `GET /api/SimCompression`

**分类：** Scenario

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/SimCompression`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Li`；调用位置数量 2。

```javascript
function Li(n){return G5({url:"/ApiCtrl/api/SimCompression",method:"get",params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### 仿真控制

**操作标识：** `GET /api/StartSimulation`

**分类：** Scenario

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/StartSimulation`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `ZB`；调用位置数量 1。

```javascript
function ZB(n){return G5({url:"/ApiCtrl/api/StartSimulation",method:"get",params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

- 现有项目已按此 GET 接口实现墨子开始/继续；本次只核对调用代码，未改变运行状态。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### ScenarioCtrl::exportRemovedLogMessages (auto-generated place

**操作标识：** `GET /api/log/exportRemoved`

**分类：** Scenario

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/log/exportRemoved`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


## SideDoctrineGroup

### SideDoctrineGroupCtrl::PostResetDoctrine (auto-generated pla

**操作标识：** `POST /api/ResetDoctrine`

**分类：** SideDoctrineGroup

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/ResetDoctrine`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Qb`；调用位置数量 1。

```javascript
function Qb(n){return G5({url:"/ApiCtrl/api/ResetDoctrine",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


## Situation

### 数据库浏览器-分类树

**操作标识：** `GET /api/db/categories`

**分类：** Situation

**资料依据：** 本机 JSON 实测；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/db/categories`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 本机只读验证

- `http://127.0.0.1:8082/ApiCtrl/api/db/categories`：HTTP 200；2026-10-02 14:34:49 +0800；application/json; charset=utf-8

```json
{
  "Country": [
    "无",
    "未知 ",
    "通用",
    "民用",
    "商业",
    "海盗",
    "叛军",
    "恐怖分子",
    "阿布扎比",
    "阿尔巴尼亚",
    "阿尔及利亚",
    "安哥拉",
    "阿根廷",
    "澳大利亚 ",
    "奥地利",
    "巴林",
    "孟加拉国",
    "白俄罗斯[1992  - ] ",
    "比利时 ",
    "博茨瓦纳",
    "巴西",
    "文莱 ",
    "保加利亚",
    "加拿大",
    "智利",
    "中国",
    "哥伦比亚",
    "克罗地亚[1992  - ] ",
    "古巴",
    "塞浦路斯",
    "捷克共和国[1993  - ] ",
    "捷克斯洛伐克[-1992] ",
    "丹麦",
    "多明尼加共和国 ",
    "厄瓜多尔",
    "埃及",
    "萨尔瓦多",
    "爱沙尼亚[1992  - ] ",
    "芬兰",
    "法国",
    "加蓬",
    "德国[DDR（东德），-1990]",
    "德国[FRG /统一] ",
    "希腊",
    "危地马拉",
    "洪都拉斯",
    "中国香港",
    "匈牙利",
    "印度",
    "印尼",
    "伊朗",
    "伊拉克",
    "爱尔兰 ",
    "以色列",
    "意大利 ",
    "日本",
    "约旦",
    "科威特 ",
    "拉脱维亚[1992  - ] ",
    "黎巴嫩",
    "利比亚",
    "立陶宛[1992  - ] ",
    "马来西亚",
    "墨西哥",
    "黑山[1992  - ] ",
    "摩洛哥",
    "莫桑比克 ",
    "北约",
    "荷兰 ",
    "新西兰",
    "尼加拉瓜",
    "尼日利亚",
    "北朝鲜",
    "北越[-1975] ",
    "挪威",
    "阿曼",
    "巴基斯坦",
    "巴拿马",
    "巴拉圭",
    "秘鲁",
    "菲律宾",
    "波兰",
    "葡萄牙 ",
    "卡塔尔",
    "罗得西亚 ",
    "罗马尼亚",
    "俄罗斯[1992  - ] ",
    "沙特阿拉伯",
    "塞尔维亚[1992  - ] ",
    "新加坡",
    "斯洛伐克[1993  - ] ",
    "斯洛文尼亚",
    "南非",
    "韩国",
    "南越[-1975] ",
    "苏联[-1991] ",
    "西班牙",
    "斯里兰卡",
    "瑞典 ",
    "瑞士",
    "叙利亚",
    "中国台湾",
    "泰国",
    "突尼斯",
    "土耳其",
    "阿联酋",
    "乌克兰[1992  - ] ",
    "英国",
    "美国",
    "委内瑞拉",
    "越南[1975  - ] ",
    "也门",
    "南斯拉夫[-1992] ",
    "扎伊尔",
    "津巴布韦",
    "乌拉圭",
    "索马里",
    "埃塞俄比亚 ",
    "冰岛",
    "土库曼斯坦",
    "缅甸",
    "苏丹",
    "南苏丹",
    "坦桑尼亚",
    "乌干达",
    "巴布亚新几内亚 ",
    "密克罗尼西亚联邦 ",
    "索罗门群岛 ",
    "汤加",
    "斐济",
    "赤道几内亚",
    "肯尼亚",
    "柬埔寨",
    "阿富汗",
    "喀麦隆",
    "哈马斯伊斯兰抵抗运动",
    "哈萨克 [1992]",
    "纳米比亚",
    "Djibouti",
    "吉尔吉斯斯坦",
    "塔吉克斯坦",
    "乌兹别克斯坦",
    "阿塞拜疆",
    "巴哈马",
    "亚美尼亚",
    "赞比亚",
    "刚果（布）[1997-]",
    "加纳",
    "多哥",
    "塞内加尔",
    "安提瓜和巴布达[1981-]",
    "巴哈马[1973-]",
    "尼日尔",
    "牙买加[1962-]"
  ],
  "code": 0,
  "data": [
    {
      "key": "aircraft",
      "label": "飞机"
    },
    {
      "key": "ship",
      "label": "水面舰艇"
    },
    {
      "key": "submarine",
      "label": "潜艇"
    },
    {
      "key": "facility",
      "label": "地面兵力与设施"
    },
    {
      "key": "satellite",
      "label": "卫星"
    },
    {
      "key": "weapon",
      "label": "武器"
    }
  ],
  "message": ""
}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

- 本机响应是裸 JSON 对象，没有统一 code/data 信封。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 数据库浏览器-单元详情

**操作标识：** `GET /api/db/unit`

**分类：** Situation

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/db/unit`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 数据库浏览器-分页单元列表

**操作标识：** `GET /api/db/units`

**分类：** Situation

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/db/units`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 作战兵力分析-空中目标列表

**操作标识：** `GET /api/getCombatAnalysis/airContacts`

**分类：** Situation

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/getCombatAnalysis/airContacts`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 作战兵力分析-航空兵兵力统计列表

**操作标识：** `GET /api/getCombatAnalysis/airUnitStatistics`

**分类：** Situation

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/getCombatAnalysis/airUnitStatistics`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 作战兵力分析-在空兵力列表

**操作标识：** `GET /api/getCombatAnalysis/airUnits`

**分类：** Situation

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/getCombatAnalysis/airUnits`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 作战兵力分析-推演方评分记录

**操作标识：** `GET /api/getCombatAnalysis/sideScoringLogs`

**分类：** Situation

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/getCombatAnalysis/sideScoringLogs`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 作战兵力分析-推演方总得分

**操作标识：** `GET /api/getCombatAnalysis/sideTotalScore`

**分类：** Situation

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/getCombatAnalysis/sideTotalScore`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 作战兵力分析-目标毁伤统计

**操作标识：** `GET /api/getCombatAnalysis/targetDamageStatistics`

**分类：** Situation

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/getCombatAnalysis/targetDamageStatistics`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 融合显示威力范围

**操作标识：** `GET /api/powerRange/merged`

**分类：** Situation

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/powerRange/merged`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


## Station

### StationCtrl::postAddCommandPost (auto-generated placeholder)

**操作标识：** `POST /api/addCommandPost`

**分类：** Station

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/addCommandPost`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### 指挥关系

**操作标识：** `POST /api/addCommander`

**分类：** Station

**资料依据：** 安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/addCommander`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### StationCtrl::postCommandPost (auto-generated placeholder)

**操作标识：** `POST /api/appointCommandpost`

**分类：** Station

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/appointCommandpost`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `byt`；调用位置数量 3。

```javascript
function byt(e){return nt({url:"/ApiCtrl/api/appointCommandpost",headers:{"Content-Type":"application/json"},method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


### StationCtrl::exportDeploymentData (auto-generated placeholde

**操作标识：** `GET /api/situation/export/deployment`

**分类：** Station

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/situation/export/deployment`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `D1t`；调用位置数量 1。

```javascript
function D1t(e){return nt({url:"/ApiCtrl/api/situation/export/deployment",method:"get",params:e,responseType:"blob"})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


## Unit

### UnitCtrl::getPlatformTypeEnums (auto-generated placeholder)

**操作标识：** `GET /api/getPlatformTypeEnums`

**分类：** Unit

**资料依据：** 本机 JSON 实测；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/api/getPlatformTypeEnums`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 本机只读验证

- `http://127.0.0.1:8082/ApiCtrl/api/getPlatformTypeEnums`：HTTP 200；2026-10-02 14:34:49 +0800；application/json; charset=utf-8

```json
{
  "code": 0,
  "data": {
    "categories": [
      {
        "items": [
          {
            "id": 1001,
            "name": "其他",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:1001"
          },
          {
            "id": 2001,
            "name": "战斗机",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:2001"
          },
          {
            "id": 2002,
            "name": "多用途（战斗/攻击）",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:2002"
          },
          {
            "id": 2101,
            "name": "反卫星武器 （反卫星武器）",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:2101"
          },
          {
            "id": 2102,
            "name": "机载激光平台",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:2102"
          },
          {
            "id": 3001,
            "name": "攻击机",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:3001"
          },
          {
            "id": 3002,
            "name": "野鼬鼠 （防空压制）",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:3002"
          },
          {
            "id": 3101,
            "name": "轰炸机",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:3101"
          },
          {
            "id": 3401,
            "name": "战场空中拦截（BAI/ CAS）",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:3401"
          },
          {
            "id": 4001,
            "name": "电子战",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:4001"
          },
          {
            "id": 4002,
            "name": "早期空中预警 （AEW）",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:4002"
          },
          {
            "id": 4003,
            "name": "机载指挥站 （ACP）",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:4003"
          },
          {
            "id": 4101,
            "name": "搜索及救援 （SAR）",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:4101"
          },
          {
            "id": 4201,
            "name": "反水雷战 （MCM）",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:4201"
          },
          {
            "id": 6001,
            "name": "反潜作战 （ASW）",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:6001"
          },
          {
            "id": 6002,
            "name": "海上巡逻机 （MPA）",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:6002"
          },
          {
            "id": 7001,
            "name": "前进观察员",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7001"
          },
          {
            "id": 7002,
            "name": "区域监视",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7002"
          },
          {
            "id": 7003,
            "name": "侦察",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7003"
          },
          {
            "id": 7004,
            "name": "电子情报收集 （ELINT）",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7004"
          },
          {
            "id": 7005,
            "name": "信号情报收集 （SIGINT）",
            "rule": "传感器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7005"
          },
          {
            "id": 7101,
            "name": "运输机",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7101"
          },
          {
            "id": 7201,
            "name": "货机",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7201"
          },
          {
            "id": 7301,
            "name": "商业飞机",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7301"
          },
          {
            "id": 7302,
            "name": "民用飞机",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7302"
          },
          {
            "id": 7401,
            "name": " 通用直升机",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7401"
          },
          {
            "id": 7402,
            "name": " 海军通用直升机",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:7402"
          },
          {
            "id": 8001,
            "name": "加油机 （空中加油）",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:8001"
          },
          {
            "id": 8101,
            "name": "教练机",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:8101"
          },
          {
            "id": 8102,
            "name": "牵引机",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:8102"
          },
          {
            "id": 8103,
            "name": "靶机",
            "rule": "传感器,货物,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:8103"
          },
          {
            "id": 8201,
            "name": "无人机（UAV）",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:8201"
          },
          {
            "id": 8202,
            "name": "无人作战飞行器（UCAV）",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:8202"
          },
          {
            "id": 8901,
            "name": "飞艇",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:8901"
          },
          {
            "id": 8902,
            "name": "航空器",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:8902"
          },
          {
            "id": 9004,
            "name": "自杀式无人机",
            "rule": "传感器,武器,机载武器,机载燃油,电磁管控,作战事件,作战条令",
            "typeId": "Aircraft:9004"
          }
        ],
        "key": "aircraft",
        "name": "飞机",
        "rulePrefix": "Aircraft",
        "unitType": "Aircraft"
      },
      {
        "items": [
          {
            "id": 1001,
            "name": "其他",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:1001"
          },
          {
            "id": 2001,
            "name": "跑道",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:2001"
          },
          {
            "id": 2002,
            "name": "滑行道(可做临时跑道)",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:2002"
          },
          {
            "id": 2003,
            "name": "跑道人口",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:2003"
          },
          {
            "id": 2004,
            "name": "建筑物(地表)",
            "rule": "",
            "typeId": "Facility:2004"
          },
          {
            "id": 2005,
            "name": "建筑物(混凝土)",
            "rule": "",
            "typeId": "Facility:2005"
          },
          {
            "id": 2006,
            "name": "建筑物(地堡)",
            "rule": "",
            "typeId": "Facility:2006"
          },
          {
            "id": 2007,
            "name": "建筑物(地下)",
            "rule": "",
            "typeId": "Facility:2007"
          },
          {
            "id": 2008,
            "name": "建筑结构(开放)",
            "rule": "",
            "typeId": "Facility:2008"
          },
          {
            "id": 2009,
            "name": "建筑结构(混凝土)",
            "rule": "",
            "typeId": "Facility:2009"
          },
          {
            "id": 3001,
            "name": "建筑物 (地表)",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:3001"
          },
          {
            "id": 3002,
            "name": "建筑物 (砖石)",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:3002"
          },
          {
            "id": 3003,
            "name": "建筑物 (地堡)",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:3003"
          },
          {
            "id": 3004,
            "name": "建筑物 (地下)",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:3004"
          },
          {
            "id": 3005,
            "name": "建筑结构 (开放)",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:3005"
          },
          {
            "id": 3006,
            "name": "建筑结构 (砖石)",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:3006"
          },
          {
            "id": 4001,
            "name": "水下",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:4001"
          },
          {
            "id": 5001,
            "name": "陆军分队",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:5001"
          },
          {
            "id": 5002,
            "name": "火箭军导弹分队",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:5002"
          },
          {
            "id": 5003,
            "name": "地防导弹分队",
            "rule": "",
            "typeId": "Facility:5003"
          },
          {
            "id": 5004,
            "name": "雷达分队",
            "rule": "",
            "typeId": "Facility:5004"
          },
          {
            "id": 5100,
            "name": "移动人员",
            "rule": "",
            "typeId": "Facility:5100"
          },
          {
            "id": 6001,
            "name": "航空器系泊设备",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:6001"
          },
          {
            "id": 7001,
            "name": "通信中心",
            "rule": "",
            "typeId": "Facility:7001"
          },
          {
            "id": 9001,
            "name": "空军基地",
            "rule": "传感器,武器,弹药库,搭载武器,电磁管控,作战事件,作战条令",
            "typeId": "Facility:9001"
          }
        ],
        "key": "facility",
        "name": "地面",
        "rulePrefix": "Facility",
        "unitType": "Facility"
      },
      {
        "items": [
          {
            "id": 1001,
            "name": "其他",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:1001"
          },
          {
            "id": 2001,
            "name": "CV - 航空母舰",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2001"
          },
          {
            "id": 2002,
            "name": "CVA - 攻击型航空母舰",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2002"
          },
          {
            "id": 2003,
            "name": "CVB - 大型航空母舰",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2003"
          },
          {
            "id": 2004,
            "name": "CVE - 护航航空母舰",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2004"
          },
          {
            "id": 2005,
            "name": "CVGH - 导弹直升机航母",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2005"
          },
          {
            "id": 2006,
            "name": "CVH - 直升机航母",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2006"
          },
          {
            "id": 2007,
            "name": "CVL - 轻型航空母舰",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2007"
          },
          {
            "id": 2008,
            "name": "CVN -核动力航空母舰",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2008"
          },
          {
            "id": 2009,
            "name": "CVS - 水上飞机母舰",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2009"
          },
          {
            "id": 2010,
            "name": "CVS - 反潜航空母舰",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2010"
          },
          {
            "id": 2011,
            "name": "AVT - 训练舰",
            "rule": "传感器,武器,弹药库,货物,载机,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令,编辑停靠舰船",
            "typeId": "Ship:2011"
          },
          {
            "id": 3001,
            "name": "B-艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3001"
          },
          {
            "id": 3002,
            "name": "BB - 战列舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3002"
          },
          {
            "id": 3003,
            "name": "BBC - 指挥战列舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3003"
          },
          {
            "id": 3004,
            "name": "BBG - 导弹战列舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3004"
          },
          {
            "id": 3005,
            "name": "BBH - 直升机战列舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3005"
          },
          {
            "id": 3006,
            "name": "BCGN - 核动力导弹战列巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3006"
          },
          {
            "id": 3007,
            "name": "BM - 小型浅水重炮舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3007"
          },
          {
            "id": 3101,
            "name": "C - 巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3101"
          },
          {
            "id": 3102,
            "name": "CA - 重型巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3102"
          },
          {
            "id": 3103,
            "name": "CAG - 重型导弹巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3103"
          },
          {
            "id": 3104,
            "name": "CB - 大型巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3104"
          },
          {
            "id": 3105,
            "name": "CBG - 大型导弹巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3105"
          },
          {
            "id": 3106,
            "name": "CG - 导弹巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3106"
          },
          {
            "id": 3107,
            "name": "CGH - 导弹直升机巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3107"
          },
          {
            "id": 3108,
            "name": "CGN - 核动力导弹巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3108"
          },
          {
            "id": 3109,
            "name": "CL - 轻型巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3109"
          },
          {
            "id": 3110,
            "name": "CLAA - 轻型防空巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3110"
          },
          {
            "id": 3111,
            "name": "CLC - 轻型指挥巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3111"
          },
          {
            "id": 3112,
            "name": "CLG - 轻型导弹巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3112"
          },
          {
            "id": 3113,
            "name": "CLH - 轻型直升机巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3113"
          },
          {
            "id": 3114,
            "name": "CS - 侦查巡洋舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3114"
          },
          {
            "id": 3201,
            "name": "D - 驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3201"
          },
          {
            "id": 3202,
            "name": "DD - 驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3202"
          },
          {
            "id": 3203,
            "name": "DDG - 导弹驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3203"
          },
          {
            "id": 3204,
            "name": "DDH - 直升机驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3204"
          },
          {
            "id": 3205,
            "name": "DDK - 反潜艇驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3205"
          },
          {
            "id": 3206,
            "name": "DDR - 雷达警戒驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3206"
          },
          {
            "id": 3207,
            "name": "DE - 护航驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3207"
          },
          {
            "id": 3208,
            "name": "DEG - 导弹护航驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3208"
          },
          {
            "id": 3209,
            "name": "DER - 雷达警戒护航驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3209"
          },
          {
            "id": 3210,
            "name": "DL - 驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3210"
          },
          {
            "id": 3211,
            "name": "DLG - 导弹驱逐舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3211"
          },
          {
            "id": 3212,
            "name": "DM - 布雷驱逐舰（改装自驱逐舰）",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3212"
          },
          {
            "id": 3301,
            "name": "F - 护卫舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3301"
          },
          {
            "id": 3302,
            "name": "FF - 护卫舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3302"
          },
          {
            "id": 3303,
            "name": "FFG - 导弹护卫舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3303"
          },
          {
            "id": 3304,
            "name": "FFG - 轻型护卫舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3304"
          },
          {
            "id": 3305,
            "name": "PF - 巡逻护卫舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3305"
          },
          {
            "id": 3306,
            "name": "LCS - 濒海战斗舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3306"
          },
          {
            "id": 3307,
            "name": "OPV - 海洋巡逻艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3307"
          },
          {
            "id": 3308,
            "name": "USV - 无人艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3308"
          },
          {
            "id": 3401,
            "name": "PB - 巡逻艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3401"
          },
          {
            "id": 3402,
            "name": "PC1 - 海岸巡逻艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3402"
          },
          {
            "id": 3403,
            "name": "PC2 - 猎潜艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3403"
          },
          {
            "id": 3404,
            "name": "PCE - 猎潜护航艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3404"
          },
          {
            "id": 3405,
            "name": "PCF - 快速巡逻艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3405"
          },
          {
            "id": 3406,
            "name": "PCFG - 快速导弹巡逻艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3406"
          },
          {
            "id": 3407,
            "name": "PG1 - 巡逻舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3407"
          },
          {
            "id": 3408,
            "name": "PG2 - 轻型护卫舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3408"
          },
          {
            "id": 3409,
            "name": "PGM - 导弹炮舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3409"
          },
          {
            "id": 3410,
            "name": "PH - 水翼炮艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3410"
          },
          {
            "id": 3411,
            "name": "PHM - 导弹水翼船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3411"
          },
          {
            "id": 3412,
            "name": "PHT - 水翼鱼雷快艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3412"
          },
          {
            "id": 3413,
            "name": "PT - 巡逻鱼雷艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3413"
          },
          {
            "id": 3414,
            "name": "PTS - 小型鱼雷巡逻艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3414"
          },
          {
            "id": 3415,
            "name": "MTB - 鱼雷摩托艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3415"
          },
          {
            "id": 3416,
            "name": "WHEC - 海岸警卫队高续航快艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3416"
          },
          {
            "id": 3417,
            "name": "WMEC - 海岸警卫队中续航快艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3417"
          },
          {
            "id": 3418,
            "name": "WPB - 海岸警卫队巡逻船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3418"
          },
          {
            "id": 3419,
            "name": "WPG - 海岸警卫队巡逻炮艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3419"
          },
          {
            "id": 3420,
            "name": "MCDV - 海事海防船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3420"
          },
          {
            "id": 3421,
            "name": "WMEC - Medium Endurance Cutter",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3421"
          },
          {
            "id": 3422,
            "name": "WMSL - Maritime Security Cutter, Large",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3422"
          },
          {
            "id": 3423,
            "name": "WMSM - Maritime Security Cutter, Medium",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:3423"
          },
          {
            "id": 4000,
            "name": "AGF1 - 指挥舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4000"
          },
          {
            "id": 4001,
            "name": "AGC - 两栖舰队旗舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4001"
          },
          {
            "id": 4002,
            "name": "LCAC - 气垫登陆艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4002"
          },
          {
            "id": 4003,
            "name": "LCC - 两栖指挥舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4003"
          },
          {
            "id": 4004,
            "name": "LCM - 机械化登陆艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4004"
          },
          {
            "id": 4005,
            "name": "LCP- 人员登陆艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4005"
          },
          {
            "id": 4006,
            "name": "LCT - 坦克登陆艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4006"
          },
          {
            "id": 4007,
            "name": "LCU - 通用登陆艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4007"
          },
          {
            "id": 4008,
            "name": "LCVP - 车辆及人员登陆艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4008"
          },
          {
            "id": 4009,
            "name": "LFR - 近岸火力支援船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4009"
          },
          {
            "id": 4010,
            "name": "LHA - 通用两栖攻击舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4010"
          },
          {
            "id": 4011,
            "name": "LHD - 多用途两栖攻击舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4011"
          },
          {
            "id": 4012,
            "name": "LKA - 两栖货舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4012"
          },
          {
            "id": 4013,
            "name": "LPD - 两栖船坞运输舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4013"
          },
          {
            "id": 4014,
            "name": "LPH - 两栖攻击直升机航母",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4014"
          },
          {
            "id": 4015,
            "name": "LSD - 船坞登陆舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4015"
          },
          {
            "id": 4016,
            "name": "LSH - 未知！英国型号！",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4016"
          },
          {
            "id": 4017,
            "name": "LSL - 后勤登陆舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4017"
          },
          {
            "id": 4018,
            "name": "LSM - 中型登陆舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4018"
          },
          {
            "id": 4019,
            "name": "LSM(R) - 中型火箭登陆舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4019"
          },
          {
            "id": 4020,
            "name": "LST - 坦克登陆舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4020"
          },
          {
            "id": 4021,
            "name": "LSU - 通用登陆舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4021"
          },
          {
            "id": 4022,
            "name": "LSV - 车辆登陆舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4022"
          },
          {
            "id": 4023,
            "name": "LCI - 步兵登陆舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4023"
          },
          {
            "id": 4024,
            "name": "LSDV - 半潜水快艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4024"
          },
          {
            "id": 4025,
            "name": "LCPA - 气垫式人员登陆舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4025"
          },
          {
            "id": 4026,
            "name": "EPF - 远征快速运输舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4026"
          },
          {
            "id": 4027,
            "name": "ESD - 远征转运码头舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4027"
          },
          {
            "id": 4028,
            "name": "ESB - 远征移动基地舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:4028"
          },
          {
            "id": 5001,
            "name": "A - 辅助船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5001"
          },
          {
            "id": 5002,
            "name": "AD - 驱逐舰供应舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5002"
          },
          {
            "id": 5003,
            "name": "AE - 弹药船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5003"
          },
          {
            "id": 5004,
            "name": "AF - 冷藏储运船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5004"
          },
          {
            "id": 5005,
            "name": "AFS - 军需品储运船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5005"
          },
          {
            "id": 5006,
            "name": "AG - 通用辅助船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5006"
          },
          {
            "id": 5007,
            "name": "AGB - 重型破冰船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5007"
          },
          {
            "id": 5008,
            "name": "AGF2 - 指挥舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5008"
          },
          {
            "id": 5009,
            "name": "AGI - 情报收集舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5009"
          },
          {
            "id": 5010,
            "name": "AGMR - 通信中继船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5010"
          },
          {
            "id": 5011,
            "name": "AGOR - 海洋科学考察船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5011"
          },
          {
            "id": 5012,
            "name": "AGOS - 海洋监测船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5012"
          },
          {
            "id": 5013,
            "name": "AGR - 雷达警戒（改装自货船）",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5013"
          },
          {
            "id": 5014,
            "name": "AGS - 测量船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5014"
          },
          {
            "id": 5015,
            "name": "AGTR - 技术考察船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5015"
          },
          {
            "id": 5016,
            "name": "AH - 医疗船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5016"
          },
          {
            "id": 5017,
            "name": "AK - 货船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5017"
          },
          {
            "id": 5018,
            "name": "AKA - 武装货船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5018"
          },
          {
            "id": 5019,
            "name": "AKE - 干货船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5019"
          },
          {
            "id": 5020,
            "name": "AKR - 滚装船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5020"
          },
          {
            "id": 5021,
            "name": "AKS - 通用存运船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5021"
          },
          {
            "id": 5022,
            "name": "AO - 舰队油船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5022"
          },
          {
            "id": 5023,
            "name": "AOE - 快速战斗支援舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5023"
          },
          {
            "id": 5024,
            "name": "AOL - 小型油船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5024"
          },
          {
            "id": 5025,
            "name": "AOR - 补给油船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5025"
          },
          {
            "id": 5026,
            "name": "AOT - 运油船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5026"
          },
          {
            "id": 5027,
            "name": "APA - 攻击型人员运输舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5027"
          },
          {
            "id": 5028,
            "name": "APD - 运兵船（高速）",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5028"
          },
          {
            "id": 5029,
            "name": "AR - 修理船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5029"
          },
          {
            "id": 5030,
            "name": "AS - 潜艇供应舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5030"
          },
          {
            "id": 5031,
            "name": "ATC - 武装运兵船 (靶船)",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5031"
          },
          {
            "id": 5032,
            "name": "ATA - 辅助远洋拖船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5032"
          },
          {
            "id": 5033,
            "name": "ATS - 救助拖船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5033"
          },
          {
            "id": 5034,
            "name": "AV - 水上飞机供应舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5034"
          },
          {
            "id": 5035,
            "name": "AX - 训练舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5035"
          },
          {
            "id": 5036,
            "name": "ASR - 潜艇救援舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5036"
          },
          {
            "id": 5037,
            "name": "AP - 人员运输舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5037"
          },
          {
            "id": 5038,
            "name": "DSV - 潜水支援船/深潜车",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5038"
          },
          {
            "id": 5039,
            "name": "AGM - 导弹射程测量船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5039"
          },
          {
            "id": 5040,
            "name": "AD - 驱逐舰供应船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5040"
          },
          {
            "id": 5041,
            "name": "DTV - Diving Tender",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5041"
          },
          {
            "id": 5042,
            "name": "GPV - General Purpose Vessel",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5042"
          },
          {
            "id": 5101,
            "name": "T-AGOS - MSC (军事海运司令部) 海洋监测船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5101"
          },
          {
            "id": 5102,
            "name": "T-AH  - MSC (军事海运司令部) 医疗船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5102"
          },
          {
            "id": 5103,
            "name": "T-AK - MSC (军事海运司令部)货船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5103"
          },
          {
            "id": 5104,
            "name": "T-AKE - MSC (军事海运司令部) 干货船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5104"
          },
          {
            "id": 5105,
            "name": "T-AKR - MSC (军事海运司令部) 滚装船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5105"
          },
          {
            "id": 5106,
            "name": "T-AO - MSC (军事海运司令部) 舰队油船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5106"
          },
          {
            "id": 5107,
            "name": "T-AO - MSC (军事海运司令部) 运油船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5107"
          },
          {
            "id": 5108,
            "name": "T-MLP - MSC (军事海运司令部) 移动登陆平台",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:5108"
          },
          {
            "id": 6001,
            "name": "MCD - 反水雷无人艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6001"
          },
          {
            "id": 6002,
            "name": "MCM - 反水雷舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6002"
          },
          {
            "id": 6003,
            "name": "MCS - 反水雷支援舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6003"
          },
          {
            "id": 6004,
            "name": "MHC - 沿岸猎雷艇",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6004"
          },
          {
            "id": 6005,
            "name": "ML - 布雷艇 ",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6005"
          },
          {
            "id": 6006,
            "name": "MSC - 沿海扫雷舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6006"
          },
          {
            "id": 6007,
            "name": "MSF - 钢壳舰队扫雷舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6007"
          },
          {
            "id": 6008,
            "name": "MSI - 近岸扫雷舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6008"
          },
          {
            "id": 6010,
            "name": "MSO - 远洋扫雷舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6010"
          },
          {
            "id": 6011,
            "name": "MST - 扫雷舰支援舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6011"
          },
          {
            "id": 6012,
            "name": "MHI - 近岸猎雷舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6012"
          },
          {
            "id": 6013,
            "name": "MM - 雷区养护舰",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:6013"
          },
          {
            "id": 7001,
            "name": "YAG - 各类勤务船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:7001"
          },
          {
            "id": 7002,
            "name": "YRT - 鱼雷回收船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:7002"
          },
          {
            "id": 7003,
            "name": "YRM - 导弹回收船",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:7003"
          },
          {
            "id": 9001,
            "name": "民用船只",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:9001"
          },
          {
            "id": 9002,
            "name": "贸易船只",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:9002"
          },
          {
            "id": 9003,
            "name": "平底驳船/海上钻井平台",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:9003"
          },
          {
            "id": 9004,
            "name": "NGS - 国家大地测量局浮标",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:9004"
          },
          {
            "id": 9005,
            "name": "底部固定阵列声纳",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:9005"
          },
          {
            "id": 9006,
            "name": "系泊声纳浮标",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:9006"
          },
          {
            "id": 9007,
            "name": "特殊（地面单位/卫星）",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:9007"
          },
          {
            "id": 9008,
            "name": "小型水筏",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:9008"
          },
          {
            "id": 9011,
            "name": "MOB 移动式近海基地",
            "rule": "传感器,武器,弹药库,货物,舰载武器,舰艇燃油,电磁管控,作战事件,作战条令",
            "typeId": "Ship:9011"
          }
        ],
        "key": "ship",
        "name": "船",
        "rulePrefix": "Ship",
        "unitType": "Ship"
      },
      {
        "items": [
          {
            "id": 1001,
            "name": "其他",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:1001"
          },
          {
            "id": 2001,
            "name": "AGSS - 辅助/实验潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2001"
          },
          {
            "id": 2002,
            "name": "APSS - 辅助货运潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2002"
          },
          {
            "id": 2003,
            "name": "SS - 攻击/舰队型潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2003"
          },
          {
            "id": 2004,
            "name": "SSB - 弹道导弹潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2004"
          },
          {
            "id": 2005,
            "name": "SSBN - 核动力弹道导弹潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2005"
          },
          {
            "id": 2006,
            "name": "SSG - 导弹攻击型潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2006"
          },
          {
            "id": 2007,
            "name": "SSGN - 核动力导弹攻击型潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2007"
          },
          {
            "id": 2008,
            "name": "SSK - 猎杀潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2008"
          },
          {
            "id": 2009,
            "name": "SSM - 小型潜水艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2009"
          },
          {
            "id": 2010,
            "name": "SSN - 核动力攻击型潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2010"
          },
          {
            "id": 2011,
            "name": "SSP - 运输潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2011"
          },
          {
            "id": 2012,
            "name": "SSR - 雷达预警潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2012"
          },
          {
            "id": 2013,
            "name": "SSRN - 核动力雷达预警潜艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:2013"
          },
          {
            "id": 3001,
            "name": "SDV - 蛙人运送艇",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:3001"
          },
          {
            "id": 4001,
            "name": "ROV - 遥控载具",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:4001"
          },
          {
            "id": 4002,
            "name": "UUV - 无人水下航行器",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:4002"
          },
          {
            "id": 4003,
            "name": "Unmanned UNderwater Glider",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:4003"
          },
          {
            "id": 9001,
            "name": "生物",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:9001"
          },
          {
            "id": 9002,
            "name": "假目标",
            "rule": "传感器,武器,货物,弹药库,潜载武器,潜艇燃油,作战条令,作战事件,电磁管控",
            "typeId": "Submarine:9002"
          }
        ],
        "key": "submarine",
        "name": "潜艇",
        "rulePrefix": "Submarine",
        "unitType": "Submarine"
      },
      {
        "items": [
          {
            "id": 1001,
            "name": "其他",
            "rule": "传感器,电磁管控,作战事件,作战条令",
            "typeId": "Satellite:1001"
          },
          {
            "id": 2001,
            "name": "成像卫星 （IMGSAT）",
            "rule": "",
            "typeId": "Satellite:2001"
          },
          {
            "id": 2002,
            "name": "雷达型海洋监视卫星 （RORSAT）",
            "rule": "",
            "typeId": "Satellite:2002"
          },
          {
            "id": 2003,
            "name": "电子情报型海洋侦察卫星 （EORSAT）",
            "rule": "",
            "typeId": "Satellite:2003"
          },
          {
            "id": 2004,
            "name": "信号情报收集 （SIGINT）",
            "rule": "",
            "typeId": "Satellite:2004"
          },
          {
            "id": 2005,
            "name": "电子情报收集 （ELINT）",
            "rule": "",
            "typeId": "Satellite:2005"
          },
          {
            "id": 2006,
            "name": "海军海洋监测卫星 （NOSS）",
            "rule": "",
            "typeId": "Satellite:2006"
          },
          {
            "id": 2007,
            "name": "测量与特征信号情报 （MASINT）",
            "rule": "",
            "typeId": "Satellite:2007"
          },
          {
            "id": 2008,
            "name": "Reusable Test Vehicle",
            "rule": "",
            "typeId": "Satellite:2008"
          },
          {
            "id": 2009,
            "name": "Communications",
            "rule": "",
            "typeId": "Satellite:2009"
          }
        ],
        "key": "satellite",
        "name": "卫星",
        "rulePrefix": "Satellite",
        "unitType": "Satellite"
      }
    ]
  },
  "message": "succeed",
  "timestamp": "2026-10-02 14:34:49"
}
```

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`


### UnitCtrl::updateUnitWayPoint (auto-generated placeholder)

**操作标识：** `POST /api/unit/updateWayPoint`

**分类：** Unit

**资料依据：** 前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/unit/updateWayPoint`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `subscribe-CW8AO0i3.js`，函数 `n`；调用位置数量 0。

```javascript
function n(t){return i({url:"/ApiCtrl/api/unit/updateWayPoint",method:"post",data:t})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 安装包接口清单为自动生成占位条目；没有完整参数契约。

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- frontend：`source_materials/frontend_calls.json`


## agent获取数据

### Dify获取探测目标列表

**操作标识：** `GET /AgentApiCtrl/api/Dify_ContactInfoList`

**分类：** agent获取数据

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/AgentApiCtrl/api/Dify_ContactInfoList`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

- Agent 查询控制器与普通 /ApiCtrl 控制器不同，不能互相替换路径。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398745793e0)


### 获取飞机单元简要信息

**操作标识：** `GET /AgentApiCtrl/api/Dify_GetAircraftUnitBriefInfo`

**分类：** agent获取数据

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/AgentApiCtrl/api/Dify_GetAircraftUnitBriefInfo`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | SideName | string | 是 |  |
| query | UnitName | string | 是 |  |
| query | HostUnitName | string | 否 |  |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- Agent 查询控制器与普通 /ApiCtrl 控制器不同，不能互相替换路径。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398747115e0)


### 获取探测单元简要信息

**操作标识：** `GET /AgentApiCtrl/api/Dify_GetContactBriefInfo`

**分类：** agent获取数据

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/AgentApiCtrl/api/Dify_GetContactBriefInfo`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | SideName | string | 是 |  |
| query | ContactName | string | 是 |  |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- Agent 查询控制器与普通 /ApiCtrl 控制器不同，不能互相替换路径。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398746048e0)


### Dify获取当前想定时间

**操作标识：** `GET /AgentApiCtrl/api/Dify_GetScenarioTime`

**分类：** agent获取数据

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/AgentApiCtrl/api/Dify_GetScenarioTime`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

- Agent 查询控制器与普通 /ApiCtrl 控制器不同，不能互相替换路径。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398497823e0)


### 获取单元简要信息

**操作标识：** `GET /AgentApiCtrl/api/Dify_GetUnitBriefInfo`

**分类：** agent获取数据

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/AgentApiCtrl/api/Dify_GetUnitBriefInfo`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | SideName | string | 是 |  |
| query | UnitName | string | 是 |  |
| query | HostUnitName | string | 否 |  |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- Agent 查询控制器与普通 /ApiCtrl 控制器不同，不能互相替换路径。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398746356e0)


### Dify获取实体简要信息列表

**操作标识：** `GET /AgentApiCtrl/api/Dify_GetUnitBriefInfoList`

**分类：** agent获取数据

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/AgentApiCtrl/api/Dify_GetUnitBriefInfoList`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | SideName | string | 否 | 选填，推演方名称 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- Agent 查询控制器与普通 /ApiCtrl 控制器不同，不能互相替换路径。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398744801e0)


### Dify获取实体列表

**操作标识：** `GET /AgentApiCtrl/api/Dify_GetUnitInfoList`

**分类：** agent获取数据

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/AgentApiCtrl/api/Dify_GetUnitInfoList`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | SideName | string | 否 |  |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- Agent 查询控制器与普通 /ApiCtrl 控制器不同，不能互相替换路径。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398745631e0)


### 获取实体详细信息

**操作标识：** `GET /AgentApiCtrl/api/getUnitInfo`

**分类：** agent获取数据

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/AgentApiCtrl/api/getUnitInfo`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | sideName | string | 否 | ；文档examples：红方 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 本机只读验证

- `http://127.0.0.1:8050/AgentApiCtrl/api/getUnitInfo`：HTTP 200；2026-10-02 14:34:49 +0800；text/html; charset=utf-8

<!doctype html>

<html lang="">

  <head>

    <meta charset="utf-8">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link rel="icon" type="image/svg+xml" href="/vite.svg" />

    <title>子房·智能作战仿真系统</title>

    <script type="text/javascript" src="/config/index.js" ></script>

    <!--

      本地文件预览服务器config（如果需要与前端不同端口）：

      <script>

        window.__FILE_SERVER_URL__ = 'http://localhost:3001'

      </script>

      默认不设置（空字符串）表示使用同源部署，即由 server.cjs 统一托管前端和 API

    -->

    <script type="module" crossorigin src="/assets/index-BMQJCp2h.js"></script>
    <link rel="stylesheet

## 限制、差异及待确认事项

- 实测 HTTP 200 返回 HTML 页面，当前部署没有确认此 API 可调用；不能按 JSON API 使用。

- Agent 查询控制器与普通 /ApiCtrl 控制器不同，不能互相替换路径。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/433466043e0)


## 为制定区域布雷扫雷

### 扫雷

**操作标识：** `POST /api/ClearMine`

**分类：** 为制定区域布雷扫雷

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ClearMine`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | ReferencePoints | array[string] | 是 | 扫雷区域参考点GUID集合 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "ReferencePoints": [
        "string"
    ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `n1t`；调用位置数量 1。

```javascript
function n1t(e){return nt({url:"/ApiCtrl/api/ClearMine",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387861124e0)

- frontend：`source_materials/frontend_calls.json`


### 布雷

**操作标识：** `POST /api/DeployMine`

**分类：** 为制定区域布雷扫雷

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/DeployMine`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | SideGuid | string | 是 | 推演方GUID |
| body | MineDBGUID | string | 是 | 布雷型号DBGUID |
| body | Num | string | 是 | 布雷数量 |
| body | ReferencePoints | array[string] | 是 | 布雷区域参考点；值填参考点guid |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "SideGuid": "string",
    "MineDBGUID": "string",
    "Num": "string",
    "ReferencePoints": [
        "string"
    ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `t1t`；调用位置数量 1。

```javascript
function t1t(e){return nt({url:"/ApiCtrl/api/DeployMine",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387859870e0)

- frontend：`source_materials/frontend_calls.json`


### 查询雷

**操作标识：** `GET /api/QueryMine`

**分类：** 为制定区域布雷扫雷

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/QueryMine`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `e1t`；调用位置数量 1。

```javascript
function e1t(e){return nt({url:"/ApiCtrl/api/QueryMine",method:"get",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387860962e0)

- frontend：`source_materials/frontend_calls.json`


## 事件编辑

### 获取条件

**操作标识：** `GET /api/GetCondition`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetCondition`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 用途补充

获取条令规则模块-事件编辑模块下的动作

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394287048e0)


### 获取触发器

**操作标识：** `GET /api/GetTrigger`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetTrigger`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394483374e0)


### 添加条件

**操作标识：** `POST /api/PostAddCondition`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/PostAddCondition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | ConditionType | integer | 是 | 需要添加的条件类型 |
| query | ConditionData | array[string] | 是 | ；添加条件所需要的数据；文档examples：[""] |
| query | ConditionName | string | 是 | 需要添加的条件名称 |
| query | LuaScriptText | string | 否 | ；需要添加的Lua脚本的内容 |
| query | IsConditionChange | boolean | 否 | 是否需要条件取反 |
| query | ConditionObserverSideGuid | string | 否 | 推演方的guid |
| query | ConditionTargetSideGuid | string | 否 | ；考虑推演方的guid |
| query | ConditionTargetPosture | integer | 否 | 对考虑推演方的态度 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "ConditionType": 0,
    "ConditionData":[
        {
        "ConditionName": "推演",
        "IsConditionChange": false,
        "ObserverSide": "5a3acc31-5ac1-42dd-a2d7-6ce6ae9b68bc",
        "TargetPosture": 4,
        "TargetSide": "43dc235f-0b3f-4914-a79a-d5c3a37ea8af"
        }
    ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394448958e0)


### 通过guid克隆动作

**操作标识：** `POST /api/PostCloneAction`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/PostCloneAction`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；需要克隆动作的guid |
| query | ActionType | integer | 否 | 需要克隆动作的类型 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
            "Guid": "b663dcb3-0a20-42d3-aca0-dc530ae1db1f",
            "ActionName": "lua",
            "ActionType": 5
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394239540e0)


### 通过guid克隆条件

**操作标识：** `POST /api/PostCloneCondition`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/PostCloneCondition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；需要克隆条件的guid |
| query | ConditionType | integer | 否 | 需要克隆条件的类型 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
            "Guid": "1227990c-764c-4520-81fe-53a66a029252",
            "ConditionName": "lua",
            "ConditionType": 2
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394458508e0)


### 通过guid查看某一条件的详细信息

**操作标识：** `POST /api/PostConditionByGUID`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/PostConditionByGUID`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；需要查看条件的guid |
| query | CondionType | integer | 否 | 需要查看条件的类型 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
            "Guid": "1227990c-764c-4520-81fe-53a66a029252",
            "ConditionName": "333",
            "ConditionType": 2
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394341015e0)


### 通过guid删除动作

**操作标识：** `POST /api/PostDelAction`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/PostDelAction`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；需要删除动作的guid |
| query | ActionType | integer | 否 | 需要删除动作的类型 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
            "Guid": "5286cdb9-cf97-4090-aa63-d06d7f2e36de",
            "ActionName": "54y",
            "ActionType": 5
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394204181e0)


### 通过guid删除条件

**操作标识：** `POST /api/PostDelCondition`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/PostDelCondition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；需要删除动作的guid |
| query | ConditionType | integer | 否 | 需要删除动作的类型 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{

}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394480172e0)


### 通过guid修改条件

**操作标识：** `POST /api/PostSetCondition`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/PostSetCondition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；需要修改的条件guid |
| query | ConditionType | integer | 否 | 需要修改的条件类型 |
| query | ConditionData | array[string] | 否 | ；修改条件所需要的数据 |
| query | LuaScriptText | string | 否 | ；需要修改的Lua脚本的内容 |
| query | IsConditionChange | boolean | 否 | 是否需要条件取反 |
| query | ConditionObserverSideGuid | string | 否 | 推演方的guid |
| query | ConditionTargetSideGuid | string | 否 | ；考虑推演方的guid |
| query | ConditionTargetPosture | integer | 否 | 对考虑推演方的态度 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
        "Guid": "1227990c-764c-4520-81fe-53a66a029252",
    "ConditionType": 2,
    "ConditionData":[{

        "ConditionName": "lua",
        "LuaScriptText": "hello"
    }]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394453302e0)


### 获取动作

**操作标识：** `GET /api/events/actions`

**分类：** 事件编辑

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/events/actions`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 用途补充

获取条令规则模块-事件编辑模块下的动作

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `W1t`；调用位置数量 2。

```javascript
function W1t(e){return nt({url:"/ApiCtrl/api/events/actions",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392558719e0)

- frontend：`source_materials/frontend_calls.json`


### 添加动作

**操作标识：** `POST /api/events/addAction`

**分类：** 事件编辑

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/events/addAction`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | ActionType | integer | 是 | 需要添加的动作类型 |
| query | ActionData | array[string] | 是 | ；添加动作所需要的数据 |
| query | ActionName | string | 是 | 需要添加的动作名称 |
| query | Side | string | 否 | ；需要添加的推演方的guid |
| query | ReferencePointGuids | array[string] | 否 | ；需要添加的参考点的集合 |
| query | PointGuid | string | 否 | 参考点的guid |
| query | UnitGuids | array[string] | 否 | ；需要添加的单元的集合；文档examples：[""] |
| query | UnitGuid | string | 否 | 单元的guid |
| query | Status | integer | 否 | ；需要添加的任务状态是否激活 |
| query | MissionGuid | string | 否 | ；需要添加的任务的guid |
| query | LuaScriptText | string | 否 | ；需要添加的Lua脚本的内容 |
| query | MessageText | string | 否 | ；需要修改的消息文本内容 |
| query | Point | integer | 否 | 需要修改的分数变化 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
        // Points,						// 得分
		// EndScenario,				// 想定结束
		// TeleportInArea,				// 瞬时移动到区域
		// Message,					// 接收消息
		// ChangeMissionStatus,		// 改变任务状态
		// LuaScript					// LUA脚本
    // "ChangeMissionStatus":{

    //     "name":"g155551",//动作名称
    //     "mission_id":"2e448707-5d37-4ec4-ad1f-dcd73eb62bce",//任务id
    //     "status":"0",//0,0-激活，1-未激活
    //     "side_id":"211d36b8-901c-4d6e-bc5e-b99ca1fba7bd"//推演方id
    // }

    // "EndScenario": //终止想定
    // {
    //      "name":"dadad",//动作名
    // }

    // "TeleportInArea" //瞬时移动到区域
    // {
    //      "name":"g155551",//动作名，
    //      "unitIDs":[
    //        "",
    //         ""
    //      ],
    //      "areaid":"",//区域ID

    // }
     "Message"://消息
    {
         "name":"xitest",//动作名，
         "side_id":"211d36b8-901c-4d6e-bc5e-b99ca1fba7bd",//推演方id
         "text":"dadsadas"//消息内容

    }
    // //得分
    // "Points":
    // {
    //      "name":"tyu",//动作名，
    //      "side_id":"211d36b8-901c-4d6e-bc5e-b99ca1fba7bd",//推演方id
    //      "pointChange":-10//分数
    // }
    //lua脚本
    // "LuaScript":
    // {
    //      "name":"lua",//动作名，
    //      "scriptText":""
    // }
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `K1t`；调用位置数量 0。

```javascript
function K1t(e){return nt({url:"/ApiCtrl/api/events/addAction",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394001207e0)

- frontend：`source_materials/frontend_calls.json`


### 通过guid查看某一动作的详细信息

**操作标识：** `POST /api/events/getAction`

**分类：** 事件编辑

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/events/getAction`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；需要查看动作的guid |
| query | ActionType | integer | 否 | 需要查看动作的类型 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Guid": "e5bd70cd-3167-427c-a8a3-9b21fd8f3a91",
    "ActionType": 3
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393184745e0)


### 通过guid修改动作

**操作标识：** `POST /api/events/setAction`

**分类：** 事件编辑

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/events/setAction`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 是 | ；需要修改动作的guid |
| query | ActionType | integer | 是 | 需要修改动作的类型 |
| query | ActionData | array[string] | 是 | 需要修改的数据 |
| query | ActionName | string | 是 | 需要修改的动作名称 |
| query | Side | string | 否 | ；需要修改的推演方的guid |
| query | ReferencePointGuids | array[string] | 否 | ；需要修改的参考点的集合 |
| query | PointGuid | string | 否 | 参考点的guid |
| query | UnitGuids | array[string] | 否 | ；需要修改的单元的集合 |
| query | UnitGuid | string | 否 | 单元的guid |
| query | Status | integer | 否 | ；需要修改的任务状态是否激活 |
| query | MissionGuid | string | 否 | ；需要修改的任务的guid |
| query | LuaScriptText | string | 否 | ；需要修改的Lua脚本的内容 |
| query | MessageText | string | 否 | ；需要修改的消息文本内容 |
| query | Point | integer | 否 | 需要修改的分数变化 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Guid": "0e12d6a9-3dfc-4d74-9938-d25c944dc027",
    "ActionType": 1,
    "ActionData":[{



        "ActionName": "end"
    }]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `U1t`；调用位置数量 0。

```javascript
function U1t(e){return nt({url:"/ApiCtrl/api/events/setAction",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393274008e0)

- frontend：`source_materials/frontend_calls.json`


## 任务相关

### 给单元分配任务 取消任务 接口

**操作标识：** `POST /api/AssignUnitToMission`

**分类：** 任务相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/AssignUnitToMission`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

分配任务

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | UnitGuid | string | 是 | 单元guid |
| body | MissionGuid | string | 是 | 任务guid；当想取消分配任务   该参数为 “none” |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
  "UnitGuid": "550e8400-e29b-41d4-a716-446655440000",
  "MissionGuid": "a3b1c5d7-e8f9-0123-4567-89abcdef0123"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `ps`；调用位置数量 2。

```javascript
function ps(n){return G5({url:"/ApiCtrl/api/AssignUnitToMission",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- MissionGuid="none" 表示取消原生墨子任务。该接口操作墨子原生任务，不等于调度项目内部 Task/behavior_tree_id 绑定。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377634146e0)

- frontend：`source_materials/frontend_calls.json`


### 获取任务列表

**操作标识：** `GET /api/GetUnitToMissions`

**分类：** 任务相关

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetUnitToMissions`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；要查询单元的uuid；文档examples：F20185FD-3360-461F-AD40-22EC33C4AED2 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "Missions": [
            {
                "MissionGuid": "a7261f3e-0075-485a-876c-fd501b1571fb",
                "MissionName": "456"
            },
            {
                "MissionGuid": "bf7b4159-e3b8-44f7-808c-950b57387d9a",
                "MissionName": "123"
            },
            {
                "MissionGuid": "f20185fd-3360-461f-ad40-22ec33c4aed2",
                "MissionName": "任务:<名称>"
            }
        ],
        "UnitMission": "00000000-0000-0000-0000-000000000000"
    },
    "message": "succeed",
    "timestamp": "2025-11-21 11:55:31"
}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380047404e0)


### 获取任务界面数据

**操作标识：** `GET /api/Mission`

**分类：** 任务相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/Mission`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 是 | 任务的UUID；文档examples：89e9d80b-c73b-4f87-b663-3d2f05a34213 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.miningMissionData | object | 是 |  |
| response | data.missionBasicData | object | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "miningMissionData": {
            "AD": "0@2@0@0",
            "AirFuel": "1",
            "FlightSize": "4",
            "MinAircraftReq": "0",
            "MiningArea": [
                {
                    "id": "30e110d4-e9c3-440e-bd8a-b5f74699375c",
                    "latitude": "31.5629",
                    "longitude": "125.406",
                    "name": "RP1"
                },
                {
                    "id": "9c06e36c-8fc8-4f5d-b928-8ac815cd905b",
                    "latitude": "31.4454",
                    "longitude": "129.011",
                    "name": "RP2"
                },
                {
                    "id": "4ecea988-f8e9-47dd-851b-9de12a86c8e7",
                    "latitude": "28.9915",
                    "longitude": "128.83",
                    "name": "RP3"
                },
                {
                    "id": "927ff6c3-6802-44bb-bb1a-77148b696901",
                    "latitude": "29.218",
                    "longitude": "125.074",
                    "name": "RP4"
                },
                {
                    "id": "30e110d4-e9c3-440e-bd8a-b5f74699375c",
                    "latitude": "31.5629",
                    "longitude": "125.406",
                    "name": "RP1"
                },
                {
                    "id": "9c06e36c-8fc8-4f5d-b928-8ac815cd905b",
                    "latitude": "31.4454",
                    "longitude": "129.011",
                    "name": "RP2"
                },
                {
                    "id": "4ecea988-f8e9-47dd-851b-9de12a86c8e7",
                    "latitude": "28.9915",
                    "longitude": "128.83",
                    "name": "RP3"
                },
                {
                    "id": "927ff6c3-6802-44bb-bb1a-77148b696901",
                    "latitude": "29.218",
                    "longitude": "125.074",
                    "name": "RP4"
                }
            ],
            "OTR": true,
            "StationAltitude_Aircraft": "未定",
            "StationDepth_Submarine": "未定",
            "StationThrottle_Aircraft": "1",
            "StationThrottle_Ship": 1,
            "StationThrottle_Submarine": 1,
            "TransitAltitude_Aircraft": "未定",
            "TransitDepth_Submarine": "未定",
            "TransitThrottle_Aircraft": "2",
            "TransitThrottle_Ship": 2,
            "TransitThrottle_Submarine": 2,
            "UseFlightSizeHardLimit": true,
            "UseGroupSizeHardLimit": false
        },
        "missionBasicData": {
            "assignedCombatUnit": [
                {
                    "children": "",
                    "key": "04390eef-888d-4f12-a6e2-3552856f453f",
                    "label": "[单任务]DDG171 “邯郸”号052C型导弹驱逐舰 #2"
                }
            ],
            "classify": "布雷",
            "combatUnit": [
                {
                    "children": [
                        {
                            "key": "15fe4059-9676-44dd-a9a9-84097fb94829",
                            "label": "22(在空的)"
                        },
                        {
                            "key": "5811d5ff-056d-4153-bd5e-a9d72980e2fa",
                            "label": "C-5运输机（HJ2023）(货物，60吨)(在空的)"
                        }
                    ],
                    "key": "4cd37bc0-1d33-4a45-88dc-99fefc1ee961",
                    "label": "",
                    "number": 2
                },
                {
                    "children": [
                        {
                            "key": "137a8214-a978-4720-98be-1314463e65bd",
                            "label": "fi(GBU-54(V)1/B L联合直接攻击弹药 [Mk82], Litening II 型先进瞄准吊舱[前视红外], AN/ALQ-184型电子干扰吊舱, 轻型挂载)(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "25613009-04d4-4d9e-8c36-cf65485da06f",
                            "label": "fi#2(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "868cfcb6-e882-49d0-a4fa-9f78fae3caee",
                            "label": "过秀兰(在空的)"
                        }
                    ],
                    "key": "76428344-0177-4528-a84a-a438af38167d",
                    "label": "F-16C/D型“战隼”战斗机",
                    "number": 3
                },
                {
                    "children": [
                        {
                            "key": "8dd84062-27d9-4a9e-b8f7-6eb82b904406",
                            "label": "“攀登者“V形军用飞艇((预备飞行[可用]))(在空的)"
                        }
                    ],
                    "key": "d3db944a-8125-4097-80ca-7560071e18ec",
                    "label": "“攀登者“V形军用飞艇",
                    "number": 1
                },
                {
                    "children": "",
                    "key": "66f942ba-c4f3-4691-b57c-562c8765ea98",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #3"
                },
                {
                    "children": "",
                    "key": "b8fb803c-f3e7-4e85-8993-5eca86d86fc5",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #1"
                },
                {
                    "children": "",
                    "key": "cdbf1301-6682-42cd-b95c-e32fdb6aa544",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #49"
                },
                {
                    "children": "",
                    "key": "d5270e55-6c4d-452a-87b4-ea339ee86560",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #50"
                },
                {
                    "children": "",
                    "key": "dcd38659-a1b4-4c91-b666-8b88064031cb",
                    "label": "建筑结构(码头[特大型，200-500m])"
                },
                {
                    "children": "",
                    "key": "e549d0c8-fcc6-4061-8649-e3903e0c00b3",
                    "label": "单实体机场 (2x 3201-4000m 跑道)"
                }
            ],
            "endTime": "2025-08-16 20:49:21",
            "id": "a031e40e-9fed-477e-8397-a2306bd865ab",
            "name": "任务:<名称>",
            "startTime": "2025-08-15 20:49:21",
            "status": 0,
            "type": "Mining",
            "typeName": "布雷"
        }
    },
    "message": "succeed",
    "timestamp": "2025-11-19 11:25:44"
}
```

### 支援

```json
{
    "code": 0,
    "data": {
        "missionBasicData": {
            "assignedCombatUnit": [],
            "classify": "支援保障",
            "combatUnit": [
                {
                    "children": [
                        {
                            "key": "15fe4059-9676-44dd-a9a9-84097fb94829",
                            "label": "22(在空的)"
                        },
                        {
                            "key": "5811d5ff-056d-4153-bd5e-a9d72980e2fa",
                            "label": "C-5运输机（HJ2023）(货物，60吨)(在空的)"
                        }
                    ],
                    "key": "346a7794-c2c6-41ed-bee9-4215a40e2461",
                    "label": "",
                    "number": 2
                },
                {
                    "children": [
                        {
                            "key": "137a8214-a978-4720-98be-1314463e65bd",
                            "label": "fi(GBU-54(V)1/B L联合直接攻击弹药 [Mk82], Litening II 型先进瞄准吊舱[前视红外], AN/ALQ-184型电子干扰吊舱, 轻型挂载)(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "25613009-04d4-4d9e-8c36-cf65485da06f",
                            "label": "fi#2(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "868cfcb6-e882-49d0-a4fa-9f78fae3caee",
                            "label": "过秀兰(在空的)"
                        }
                    ],
                    "key": "554fdda2-17c8-43cd-8d8b-c82187d766f0",
                    "label": "F-16C/D型“战隼”战斗机",
                    "number": 3
                },
                {
                    "children": [
                        {
                            "key": "8dd84062-27d9-4a9e-b8f7-6eb82b904406",
                            "label": "“攀登者“V形军用飞艇((预备飞行[可用]))(在空的)"
                        }
                    ],
                    "key": "f2c657a9-71e5-46c4-aa0e-25f115c7e7bf",
                    "label": "“攀登者“V形军用飞艇",
                    "number": 1
                },
                {
                    "children": "",
                    "key": "04390eef-888d-4f12-a6e2-3552856f453f",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #2"
                },
                {
                    "children": "",
                    "key": "66f942ba-c4f3-4691-b57c-562c8765ea98",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #3"
                },
                {
                    "children": "",
                    "key": "b8fb803c-f3e7-4e85-8993-5eca86d86fc5",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #1"
                },
                {
                    "children": "",
                    "key": "cdbf1301-6682-42cd-b95c-e32fdb6aa544",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #49"
                },
                {
                    "children": "",
                    "key": "d5270e55-6c4d-452a-87b4-ea339ee86560",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #50"
                },
                {
                    "children": "",
                    "key": "dcd38659-a1b4-4c91-b666-8b88064031cb",
                    "label": "建筑结构(码头[特大型，200-500m])"
                },
                {
                    "children": "",
                    "key": "e549d0c8-fcc6-4061-8649-e3903e0c00b3",
                    "label": "单实体机场 (2x 3201-4000m 跑道)"
                }
            ],
            "endTime": "2025-08-16 20:49:21",
            "id": "6b91ec42-e832-4733-aa95-f4585b7522f2",
            "name": "support",
            "startTime": "2025-08-15 20:49:21",
            "status": 0,
            "type": "Support",
            "typeName": "支援保障"
        },
        "supportmissionData": {
            "AEOOS": false,
            "AirFuel": "1",
            "FlightSize": "1",
            "GroupSize": "1",
            "OTO": false,
            "OTR": true,
            "OneTankingCycleOnly": false,
            "SideWay": "默认",
            "StationAltitude_Aircraft": "未定",
            "StationDepth_Submarine": "未定",
            "StationThrottle_Aircraft": "1",
            "StationThrottle_Ship": 1,
            "StationThrottle_Submarine": 1,
            "TransitAltitude_Aircraft": "未定",
            "TransitDepth_Submarine": "未定",
            "TransitThrottle_Aircraft": "2",
            "TransitThrottle_Ship": 2,
            "TransitThrottle_Submarine": 2,
            "UnitBTRWay": "默认",
            "UseFlightSizeHardLimit": true,
            "UseGroupSizeHardLimit": false
        }
    },
    "message": "succeed",
    "timestamp": "2025-11-19 15:09:49"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `p7`；调用位置数量 21。

```javascript
function p7(n){return G5({url:"/ApiCtrl/api/Mission",method:"get",headers:{"Content-Type":"application/json"},params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370919380e0)

- frontend：`source_materials/frontend_calls.json`


### 任务界面操作

**操作标识：** `POST /api/Mission`

**分类：** 任务相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/Mission`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | type | enum<string> | 是 | 操作类型；枚举：createMission, AssignUnitToMission, UnAssignUnitToMission, AssignUnitToEscort, UnAssignUnitToEscort, AssignUnitAsTarget, RemoveUnitAsTarget, AddPatrolAreaPoint, AddProsecutionAreaPoint, UpPatrolAreaPoint, DownPatrolAreaPoint, UpProsecutionAreaPoint, DownProsecutionAreaPoint, RemovePatrolAreaPoint, RemoveProsecutionAreaPoint, StrikeMissionRules, PatrolMissionRules |
| body | createMission | object | 否 | 创建任务所需数据 |
| body | createMission.name | string | 是 | 任务名称 |
| body | createMission.sideGuid | string | 是 | 推演方GUID |
| body | createMission.type | enum<string> | 是 | 任务类型；枚举：Strike, Patrol, Ferry, Support, Mining, MineClearing, Cargo |
| body | createMission.classify | enum<string> | 否 | 任务分类；只有巡逻，打击任务需要；枚举：Air, land, SEA, Sub, AAW, SUR_SEA, SUR_LAND, SUR_Mixed, SUB, SEAD |
| body | createMission.status | boolean | 是 | 任务状态 |
| body | createMission.isOpenMissionWindows | boolean | 是 | 是否打开编辑任务界面 |
| body | createMission.groupGuid | string | 否 | 组ID；现阶段没有组，先空着就行 |
| body | MissionGuid | string | 否 | 任务GUID |
| body | Units | array[string] | 否 | 单元GUID列表 |
| body | Rules | object | 否 |  |
| body | Rules.TaskTriggerCondition | enum<integer> | 否 | 任务触发条件；枚举：1, 2, 3, 4 |
| body | Rules.FormationSize | enum<integer> | 否 | 编队规模；枚举：1, 2, 3, 4, 5 |
| body | Rules.RadarUse | enum<integer> | 否 | 雷达运用；枚举：1, 2, 3 |
| body | Rules.FuelAndMagazine | enum<integer> | 否 | 燃油弹药；枚举：0, 1, 2 |
| body | Rules.WeaponRouteLineGuid | string | 是 | 武器航线 |
| body | AreaPoints | array[string] | 否 | 区域列表guid数组 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "type": "createMission",
    "createMission": {
        "name": "添加打击任务",
        "sideGuid": "211d36b8-901c-4d6e-bc5e-b99ca1fba7bd",
        "type": "Strike",
        "classify": "Air",
        "status": true,
        "isOpenMissionWindows": true,
        //原有基础上加上  任务类型id
        "task_id": "2", //新任务类型需要
        "TreeParentID": "0" //task_trees上级节点id
    }
}
```

### 分配单元到任务

```json
{
    "type": "AssignUnitToMission",
    "MissionGuid": "ff843bd7-54f0-4947-adb7-5f3e5e7a4f7f",
    "Units": [
        "do magna irure",
        "ullamco",
        "amet consequat"
    ]
}
```

### 取消分配单元

```json
{
    "type": "UnAssignUnitToMission",
    "MissionGuid": "ff843bd7-54f0-4947-adb7-5f3e5e7a4f7f",
    "Units": [
        "2f1742f9-7e8a-423d-af8e-015a2ab75d4c",
        "4523b852-96fa-4e5c-b36c-1d7aa8ad0eb3",
        "5657dd09-b608-445e-9c21-b155dbe8d4ad"
    ]
}
```

### 添加打击任务

```json
{
    "type": "createMission",
    "createMission": {
        "name": "添加打击任务",
        "sideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
        "type": "Strike",
        "classify": "Air",
        "status": true,
        "isOpenMissionWindows": true,
        //原有基础上加上  任务类型id
        "task_id": "2", //新任务类型需要
        "TreeParentID": "0" //task_trees上级节点id
    }
}
```

### 转场任务

```json
{
    "type": "createMission",
    "createMission": {
        "name": "添加打击任务",
        "sideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
        "type": "Strike",
        "classify": "Air",
        "destination": "",
        "status": true,
        "isOpenMissionWindows": true,
        "task_id": "2", //新任务类型需要
        "TreeParentID": "0" //task_trees上级节点id
    }
}
```

### 布雷任务

```json
{
    "type": "createMission",
    "createMission": {
        "name": "添加布雷任务",
        "sideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
        "type": "Mining",
        "classify": "Air",
        "status": true,
        "isOpenMissionWindows": true,
        "task_id": "2", //新任务类型需要
        "TreeParentID": "0" //task_trees上级节点id
    }
}
```

### 布雷 扫雷 参数修改

```json
{
    "type": "MiningMissionRules",
    "MissionGuid": "5bbb0863-94a2-44bb-a621-c808c4d6ff82",
    "Rules": {
        "name": "布雷无敌任务",
        "startTime": "2025-11-21 10:30:24",
        "endTime": "2025-11-22 10:30:24",
        "area_ID": "",
        "OTR": true,
        "status": "1",
        "Day": "0", //扫雷没有延迟时间
        "Hour": "0",
        "Minute": "2",
        "Second": "2",
        "FlightSize": "1",
        "AirFuel": "2",
        "MinAircraftReq": "1",
        "UseFlightSizeHardLimit": true,
        "GroupSize": "1",
        "UseGroupSizeHardLimit": true,
        "TransitThrottle_Ship": "1",
        "StationThrottle_Ship": "1",
        "TransitThrottle_Submarine": "1",
        "StationThrottle_Submarine": "1",
        "TransitDepth_Submarine": "1",
        "StationDepth_Submarine": "1",
        "TransitThrottle_Aircraft": "0",
        "TransitAltitude_Aircraft": "2",
        "StationThrottle_Aircraft": "1",
        "StationAltitude_Aircraft": "1"
    }
}
```

### 支援任务参数

```json
{
    "type": "SupportMissionRules",
    "MissionGuid": "92d3e885-b173-4008-aa0b-853096b7d381",
    "Rules": {
        "name": "支援无敌任务",
        "startTime": "2025-11-21 10:30:24",
        "endTime": "2025-11-22 10:30:24",
        "area_ID": "",
        "MNOS": "", //阵位上保持单元数量
        "OTR": true,
        "OTO": true, //仅一次
        "AEOIPA": false,
        "OneTankingCycleOnly": true, //一个加油周期后，加油队列为空 返航
        "status": "1",
        "FlightSize": "1",
        "SideWay": "fd811a7d-1dcd-43e3-be71-f0404790cf99",
        "UnitBTRWay": "fd811a7d-1dcd-43e3-be71-f0404790cf99",
        "AirFuel": "2",
        "MinAircraftReq": "1",
        "UseFlightSizeHardLimit": true,
        "GroupSize": "1",
        "UseGroupSizeHardLimit": true,
        "TransitThrottle_Ship": "1",
        "StationThrottle_Ship": "1",
        "TransitThrottle_Submarine": "1",
        "StationThrottle_Submarine": "1",
        "TransitDepth_Submarine": "1",
        "StationDepth_Submarine": "1",
        "TransitThrottle_Aircraft": "0",
        "TransitAltitude_Aircraft": "2",
        "StationThrottle_Aircraft": "1",
        "StationAltitude_Aircraft": "1"
    }
}
```

### 添加转场任务

```json
{
    "type": "createMission",
    "createMission": {
        "name": "转场任务测试",
        "sideGuid": "4e53b6a7-8c4d-41a2-b745-9e0f8a7d6c3b",
        "status": true,
        "type": "Ferry",
        "classify": "",
        "destination": "", //目的地guid
        "isOpenMissionWindows": true,
        "task_id": "9",
        "TreeParentID": "0" //task_trees上级节点id
    }
}
```

### 修改转场任务参数

```json
{
    "type": "FerryMissionRules",
    "MissionGuid": "5bbb0863-94a2-44bb-a621-c808c4d6ff82",
    "Rules": {
        "name": "换场无敌任务",
        "startTime": "2025-11-21 10:30:24",
        "endTime": "2025-11-22 10:30:24",
        "status": "1",
        "FerryMissionBehavior": "0",
        "SideWay": "",
        "FlightSize": "1",
        "AirFuel": "2",
        "MinAircraftReq": "1",
        "UseFlightSizeHardLimit": true,
        "FerryThrottle_Aircraft": "0",
        "TransitAltitude_Aircraft": "100",
        "FerryTerrainFollowing_Aircraft": false
    }
}
```

### 添加投送任务

```json
{
    "type": "createMission",
    "createMission": {
        "name": "投送任务测试",
        "sideGuid": "4e53b6a7-8c4d-41a2-b745-9e0f8a7d6c3b",
        "status": true,
        "type": "Cargo",
        "classify": "",
        "isOpenMissionWindows": true,
        "task_id": "9",
        "TreeParentID": "0" //task_trees上级节点id
    }
}
```

### 修改投送任务参数

```json
{
    "type": "CargoMissionRules",
    "MissionGuid": "5bbb0863-94a2-44bb-a621-c808c4d6ff82",
    "Rules": {
        "name": "投送无敌任务",
        "startTime": "2025-11-21 10:30:24",
        "endTime": "2025-11-22 10:30:24",
        "status": "1",
        "area_ID": "",
        "TransitThrottle_Ship": "1",
        "StationThrottle_Ship": "1",
        "TransitThrottle_Aircraft": "0",
        "TransitAltitude_Aircraft": "2",
        "StationThrottle_Aircraft": "1",
        "StationAltitude_Aircraft": "1",
    }
}
```

### 投送任务货物数量增加到最大

```json
{
    "type": "AddAllMountToUnload",
    "MissionGuid": "19",
    "cargo_id": "" //选择的货物id
}
```

### 货物加一

```json
{
    "type": "AddMountToUnload",
    "MissionGuid": "19",
    "cargo_id": "" //选择的货物id
}
```

### 清除所有货物

```json
{
    "type": "RemoveAllMountToUnload",
    "MissionGuid": "19",
    "cargo_id": "" //选择的货物id
}
```

### 货物减一

```json
{
    "type": "RemoveMountToUnload",
    "MissionGuid": "19",
    "cargo_id": "" //选择的货物id
}
```

### 打击任务修改

```json
{
    "type": "StrikeMissionRules",
    "MissionGuid": "F20185FD-3360-461F-AD40-22EC33C4AED2",
    "Rules": {
        "name": "方案1-空中拦截1",
        "startTime": "2021-05-26 02:55:44",
        "endTime": "2021-05-26 06:15:45",
        "MCSTT": "3",
        "FlightSize": "3",
        "RadarBehaviour": "2",
        "Bingo": "1",
        "SideWeaponWay": "3cc455ef-c2c8-4515-b691-cab38c8b018e",
        "AirFuel": "2",
        "SideWay": "3cc455ef-c2c8-4515-b691-cab38c8b018e",
        "UnitBTRWay": "cfdc58b6-2b09-4fc6-8299-02f06d9a7065",
        "ShipAndSubWayEndStrike": "0",
        "plannedTarget": "0",
        "GroupSize": "2",
        "UseGroupSizeHardLimit": false,
        "Escort_FlightSize_Shooter": "0",
        "MinAircraftReq_Escorts_Shooter": "0",
        "MaxAircraftToFly_Escort_Shooter": "0",
        "Escort_ResponseRadius": "100",
        "Escort_FlightSize_NonShooter": "0",
        "UseFlightSizeHardLimit_Escort": "0",
        "GroupSize_Escort": "0",
        "UseGroupSizeHardLimit_Escort": "-94",
        "weaponPresetRoute": "3cc455ef-c2c8-4515-b691-cab38c8b018e",
    }
}
```

### 添加巡逻任务

```json
{
    "type": "createMission",
    "createMission": {
        "name": "东海巡逻任务",
        "sideGuid": "28bdfed6-b88a-401b-93b6-f37748b969ad",
        "status": true,
        "type": "Patrol",
        "classify": "AAW",
        "isOpenMissionWindows": true,
        "task_id": "9",
        "TreeParentID": "0" //task_trees上级节点id
    }
}
```

### 巡逻任务修改

```json
{
    "type": "PatrolMissionRules",
    "MissionGuid": "8579822a-1d09-4d45-b914-d29275489066",
    "Rules": {
        "name": "haha",
        // "startTime":"11/21/2025 16:29:32",
        //"endTime":"11/21/2025 16:29:33",
        //"OTR":"0",
        "PatrolArea_ID": "{4d941dde-6f12-4959-abf9-fb6f7851dc70}", //新区域接口
        "AlertArea_ID": "{4d941dde-6f12-4959-abf9-fb6f7851dc70}", //警戒区域ID
        // "PatrolArea": [   //老区域
        //     {"id": "708242c0-1cc0-46a9-ae0d-887748f063aa"},
        //     {"id": "3acfa468-e6ea-4995-8a5d-ffdcddc1e1ef"},
        //     {"id": "f5db0db4-ceed-4a56-a404-2808a2bfb9dc"}
        // ],
        //             "AlertArea": [
        //     {"id": "708242c0-1cc0-46a9-ae0d-887748f063aa"},
        //     {"id": "3acfa468-e6ea-4995-8a5d-ffdcddc1e1ef"},
        //     {"id": "f5db0db4-ceed-4a56-a404-2808a2bfb9dc"}
        // ],
        "OTR": false, //1/3规则
        "IOPA": false, //对巡逻区外的探测目标进行分析
        "IWWR": false, //对武器射程内探测目标进行分析
        "AEOIPA": false, //仅在patrol/警戒区内打开电磁辐射
        /**
      * 飞机设置参数
      */
        "FlightSize": '2', //编队规模
        "AirFuel": '3', //空中加油
        "SideWay": '0', //出航航线
        "UnitBTRWay": '0', //返航航线
        "PatrolAreaSideWay": '0', //patrol航线
        "MinAircraftReq": '0', //execution任务所需最低就绪飞机数
        "UseFlightSizeHardLimit": false, //飞机数低于编队规模要求不能起飞（根据基地、类型或挂载进行编组）
        /**
       * 水面舰艇/潜艇设置
       */
        "GroupSize": '1', //编队规模
        "ShipAndSubWay": '0', //出航航线
        "PatrolAreaShipAndSubWay": '0', //patrol航线
        "UseGroupSizeHardLimit": false, //水面舰艇或潜艇数低于编队规模要求，(不能出击根据基地编组)
        /**
       * 飞机航速与高度
       */
        "TransitThrottle_Aircraft":'0', //出航油门
        "StationThrottle_Aircraft":'0', //阵位油门
        "AttackThrottle_Aircraft":'0', //攻击油门
        "TransitSpeed_Aircraft":'0', //出航速度
        "StationSpeed_Aircraft":'0', //阵位速度
        "AttackSpeed_Aircraft":'0', //攻击速度
        "TransitAltitude_Aircraft":'0', //出航高度
        "StationAltitude_Aircraft":'0', //阵位高度
        "AttackAltitude_Aircraft":'0', //攻击高度
        "AttackDistance_Aircraft":'0', //攻击距离
        "TransitTerrainFollowing_Aircraft": false, //出航地形跟随
        "StationTerrainFollowing_Aircraft": false, //阵位地形跟随
        "AttackTerrainFollowing_Aircraft": false, //攻击地形跟随
    }
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "missionBasicData": {
            "assignedCombatUnit": [],
            "classify": "转场 - 目的地：单实体机场 (2x 3201-4000m 跑道) (0)",
            "combatUnit": [
                {
                    "children": [
                        {
                            "key": "5811d5ff-056d-4153-bd5e-a9d72980e2fa",
                            "label": "C-5运输机（HJ2023）(货物，60吨)(在空的)"
                        }
                    ],
                    "key": "a10f62ad-a619-4193-a170-4f518695810a",
                    "label": "",
                    "number": 1
                },
                {
                    "children": [
                        {
                            "key": "137a8214-a978-4720-98be-1314463e65bd",
                            "label": "fi(GBU-54(V)1/B L联合直接攻击弹药 [Mk82], Litening II 型先进瞄准吊舱[前视红外], AN/ALQ-184型电子干扰吊舱, 轻型挂载)(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "868cfcb6-e882-49d0-a4fa-9f78fae3caee",
                            "label": "过秀兰(在空的)"
                        }
                    ],
                    "key": "f29d3f08-c595-4cd3-b1f0-c5fe86a500c1",
                    "label": "F-16C/D型“战隼”战斗机",
                    "number": 2
                },
                {
                    "children": [
                        {
                            "key": "0384759a-30be-4d81-b4ef-c0f2d61d52dd",
                            "label": "Gladiator #9(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "12309eca-b498-4f04-a3bb-92667155319e",
                            "label": "Gladiator #7(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "2cab7094-5f50-4252-9348-556bca5690f5",
                            "label": "Gladiator #3(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "5f7b9cd4-cf32-4a60-9084-8bce1cc2e039",
                            "label": "Gladiator #6(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "65332e2f-5698-4677-9e27-842ec0259946",
                            "label": "Gladiator #8(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "8dc0839f-41cd-4456-97b9-8af042d8413d",
                            "label": "Gladiator #4(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "907e934e-1fad-465f-97ae-6b9a24986a53",
                            "label": "SH-3H型“海王”反潜作战机(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "ba929625-e0ca-4db7-9d18-c389c424114a",
                            "label": "Gladiator #5(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "f38f4e31-4716-4994-8edb-cc41531e186f",
                            "label": "Gladiator #2(单实体机场 (2x 3201-4000m 跑道))"
                        },
                        {
                            "key": "fbf07071-c3f8-49a0-a5d5-49773e486268",
                            "label": "Gladiator #10(单实体机场 (2x 3201-4000m 跑道))"
                        }
                    ],
                    "key": "f42bf398-6ef5-417e-a681-0d79ca62b120",
                    "label": "SH-3H型“海王”反潜作战机",
                    "number": 10
                },
                {
                    "children": [
                        {
                            "key": "8dd84062-27d9-4a9e-b8f7-6eb82b904406",
                            "label": "“攀登者“V形军用飞艇((预备飞行[可用]))()"
                        }
                    ],
                    "key": "22256438-eb43-4d5f-9314-85fb0293f7f9",
                    "label": "“攀登者“V形军用飞艇",
                    "number": 1
                },
                {
                    "children": "",
                    "key": "04390eef-888d-4f12-a6e2-3552856f453f",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #2"
                },
                {
                    "children": "",
                    "key": "04e2a3d4-e3b0-4fd3-ba02-2e0579ffdff7",
                    "label": "建筑物(塔台)"
                },
                {
                    "children": "",
                    "key": "66f942ba-c4f3-4691-b57c-562c8765ea98",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #3"
                },
                {
                    "children": "",
                    "key": "b8fb803c-f3e7-4e85-8993-5eca86d86fc5",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #1"
                },
                {
                    "children": "",
                    "key": "cdbf1301-6682-42cd-b95c-e32fdb6aa544",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #49"
                },
                {
                    "children": "",
                    "key": "d5270e55-6c4d-452a-87b4-ea339ee86560",
                    "label": "DDG171 “邯郸”号052C型导弹驱逐舰 #50"
                },
                {
                    "children": "",
                    "key": "dcd38659-a1b4-4c91-b666-8b88064031cb",
                    "label": "建筑结构(码头[特大型，200-500m])"
                },
                {
                    "children": "",
                    "key": "e549d0c8-fcc6-4061-8649-e3903e0c00b3",
                    "label": "单实体机场 (2x 3201-4000m 跑道)"
                }
            ],
            "endTime": "2025-08-16 20:49:21",
            "id": "dccba87b-5159-464d-8ec8-d507eb270804",
            "name": "添加转场任务",
            "startTime": "2025-08-15 20:49:21",
            "status": 4756,
            "type": "Ferry",
            "typeName": "转场 - 目的地：单实体机场 (2x 3201-4000m 跑道) (0)"
        }
    },
    "message": "succeed",
    "timestamp": "2025-11-20 10:40:21"
}
```

### 添加投送任务

```json
{
    "code": 0,
    "data": {
        "cargoMissionData": {
            "SideWay": "默认",
            "StationAltitude_Aircraft": "304.8",
            "StationThrottle_Aircraft": "4",
            "StationThrottle_Ship": "2",
            "TransitAltitude_Aircraft": "609.6",
            "TransitThrottle_Aircraft": "2",
            "TransitThrottle_Ship": "2",
            "area": [],
            "mounts": "",
            "platform": ""
        },
        "missionBasicData": {
            "assignedCombatUnit": [],
            "classify": "投送",
            "combatUnit": [
                {
                    "children": [
                        {
                            "key": "3a310dc5-7762-4d67-95e6-95df70ad75e7",
                            "label": "C-17A型“环球霸主III”运输机 #1(伞兵（或空降兵）, 102x, 20 吨)(单实体机场 (2x 3201-4000m 跑道))"
                        }
                    ],
                    "key": "fd519aa6-7acb-40fc-ba66-9eb9a53be9bf",
                    "label": "C-17A型“环球霸主III”运输机",
                    "number": 1
                },
                {
                    "children": [
                        {
                            "key": "747b9db3-0af1-44ef-915d-7c2aba0b7ca6",
                            "label": "C-5B型\\\"银河\\\"运输机 #1(货物，60吨)(单实体机场 (2x 3201-4000m 跑道))"
                        }
                    ],
                    "key": "e2ce1c26-8b5b-48b1-83b9-46a6d322cfa2",
                    "label": "C-5B型\"银河\"运输机",
                    "number": 1
                },
                {
                    "children": "",
                    "key": "5b55e7ce-ac00-4137-9f6d-cef02ec3ec0b",
                    "label": "单实体机场 (1x 3201-4000m 跑道)"
                },
                {
                    "children": "",
                    "key": "609a1564-ad78-46a6-91aa-4b76e6022dcc",
                    "label": "单实体机场 (2x 3201-4000m 跑道)"
                },
                {
                    "children": "",
                    "key": "6d4815a0-dab5-4c20-85d0-de03650cc8d1",
                    "label": "单实"
                },
                {
                    "children": "",
                    "key": "9375c1e8-e69b-401d-8c51-4ae2be241a13",
                    "label": "建筑结构(海军码头，船坞)"
                },
                {
                    "children": "",
                    "key": "b5aeae86-4920-4a51-b6e0-de712bc0c5bf",
                    "label": "单实体机场 (1x 1401-2000m 跑道)"
                },
                {
                    "children": "",
                    "key": "dbc2cc45-c409-4109-ac22-343b772af88e",
                    "label": "AAA高射炮兵分队(40mm/70 “博福斯”x 2, “捕蝇器”火控雷达）"
                }
            ],
            "endTime": "2025-08-16 20:49:21",
            "id": "dd9add92-091a-4a56-90ee-435745aee050",
            "name": "投送任务测试",
            "startTime": "2025-08-15 20:49:21",
            "status": 0,
            "type": "Cargo",
            "typeName": "投送"
        }
    },
    "message": "succeed",
    "timestamp": "2025-12-11 11:36:20"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `p5`；调用位置数量 84。

```javascript
function p5(n){return G5({url:"/ApiCtrl/api/Mission",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370919450e0)

- frontend：`source_materials/frontend_calls.json`


### 获取任务甘特图界面数据

**操作标识：** `GET /api/MissionGant`

**分类：** 任务相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/MissionGant`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | SideGuid | string | 是 | 推演方guid；文档examples：211d36b8-901c-4d6e-bc5e-b99ca1fba7bd |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Pt`；调用位置数量 3。

```javascript
function Pt(n){return G5({url:"/ApiCtrl/api/MissionGant",method:"get",headers:{"Content-Type":"application/json"},params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370919262e0)

- frontend：`source_materials/frontend_calls.json`


### 任务甘特图界面操作

**操作标识：** `POST /api/MissionGant`

**分类：** 任务相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/MissionGant`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | MissionGuid | string | 是 | 任务GUID；文档examples：11996f52-c718-4da2-93c0-a26e8c36fe92 |
| query | MissionName | string | 否 | 任务名称；文档examples：1111 |
| query | MissionStartTime | string | 否 | 任务开始时间；文档examples：2020-01-01 08:00:00 |
| query | MissionEndTime | string | 否 | 任务结束时间；文档examples：2020-01-02 08:00:00 |
| query | MissionCommandType | enum<string> | 是 | 任务操作类型；枚举：DeleteMission, ApplyMission；文档examples：ApplyMission |
| query | MissionStatus | enum<string> | 否 | 任务状态；枚举：Activation, DeActivation, Completed；文档examples：Activation |
| query | SideGuid | string | 是 | 任务所在推演方；文档examples：6F2DA012-0C8B-49F2-9D41-DC00EB48D27E |
| body | MissionGuid | string | 是 | 任务GUID；任务GUID |
| body | MissionName | string | 是 | 任务名称 |
| body | MissionStartTime | string | 是 | 任务开始时间 |
| body | MissionEndTime | string | 是 | 任务结束时间 |
| body | MissionCommandType | string | 是 | 任务操作类型 |
| body | MissionStatus | string | 是 | 任务状态 |
| body | SideGuid | string | 是 | 任务所在推演方 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Ok`；调用位置数量 1。

```javascript
function Ok(n){return G5({url:"/ApiCtrl/api/MissionGant",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370919291e0)

- frontend：`source_materials/frontend_calls.json`


### 参考点操作

**操作标识：** `POST /api/ReferencePoint`

**分类：** 任务相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ReferencePoint`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

参考点操作

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | Type | enum<string> | 是 | 操作类型；枚举：AddReferencePoint, RemoveReferencePoint, ChangeReferencePoint, AddArea |
| body | SideGuid | string | 是 | 推演方Guid |
| body | Values | array [object] | 否 | 经纬度集合，也可以是guid集合 |
| body | Values.Lon | string | 否 | 经度 |
| body | Values.Lat | string | 否 | 纬度 |
| body | Values.Guid | string | 否 | 参考点Guid |
| body | Values.Name | string | 是 | 修改参考点名字 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Type": "AddReferencePoint",
    "SideGuid": "28bdfed6-b88a-401b-93b6-f37748b969ad",
    "Values": [
        {
            "Lon": "100",
            "Lat": "20"
        },
        {
            "Lon": "100",
            "Lat": "20"
        }
    ]
}
```

### 修改参考点

```json
{
    "Type": "ChangeReferencePoint",
    "SideGuid": "50F6FE58-4B14-421C-B010-C26E3547C331",
    "Values": [
        {
            "Guid": "8c6307cb-1c1d-4250-8405-e8ff51399c4b",
            "Name": "RP98",
            "Lon": "124.4",
            "Lat": "28"
        }
    ]
}
```

### 删除参考点

```json
{
    "Type": "RemoveReferencePoint",
    "SideGuid": "50F6FE58-4B14-421C-B010-C26E3547C331",
    "Values": [
        {
            "Guid": "8c6307cb-1c1d-4250-8405-e8ff51399c4b"
        }
    ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Kje`；调用位置数量 10。

```javascript
function Kje(e){return nt({url:"/ApiCtrl/api/ReferencePoint",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376275614e0)

- frontend：`source_materials/frontend_calls.json`


## 任务编成树

### 任务编成

**操作标识：** `GET /api/TaskCompilation`

**分类：** 任务编成树

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/TaskCompilation`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | sideName | string | 否 | 推演方名称 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/399178102e0)


### 设置任务编成树

**操作标识：** `POST /api/TaskCompilation`

**分类：** 任务编成树

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/TaskCompilation`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
//新建组节点
// {
//     "option":"addMissionGroup",
//     "side":"中国",
//     "group_name":"组去",
//     "parentID":1 //父nodes/没有就默认0
// }
//移动节点 修改节点的parentID
// {
//     "option":"moveNode",
//     "unitID":5,
//     "parentID":3
// },
// // 修改组名称
// {

//         "option":"reName",
//         "nodeId":3,
//         "newName":"dsa"

// }
//删除组
{
    "option":"reName",
    "nodeId":3,
    "childAll":false
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `S1t`；调用位置数量 1。

```javascript
function S1t(e){return nt({url:"/ApiCtrl/api/TaskCompilation",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/399264652e0)

- frontend：`source_materials/frontend_calls.json`


## 任务config界面

### 任务大类型的操作

**操作标识：** `POST /api/ConfiguredTasks/MissionType`

**分类：** 任务config界面

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ConfiguredTasks/MissionType`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "option": "addTaskType", //操作选项 添加任务的大类型
    "typeName": "ggswdsdsg", //名称
    "entityUsed": "Ship" //名称
}
```

### 更新任务大类型

```json
{
    "option": "UpdateTaskType", //操作选项 添加任务的大类型
    "id": "1",
    "typeName": "ggg", //新名称
    "entityUsed": "Ship" //新的该任务使用的兵力 修改
}
```

### 删除大类型

```json
{
    "option": "delTaskType", //操作选项 添加任务的大类型
    "typeName": "ggg" //名称
}
```

### 给指定任务大类型添加任务

```json
{
    "option": "addTask", //操作选项 添加任务的大类型
    "typeName": "ggg", //大类型名称
    "task_name": "Strike", //任务名称
    "task_mztype": "", //对应的任务墨子类型
    "task_mzsubtype": "", //墨子任务子类型
    "dialog_type": "", //弹窗类型
    "remark": "" //描述
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `m1t`；调用位置数量 4。

```javascript
function m1t(e){return nt({url:"/ApiCtrl/api/ConfiguredTasks/MissionType",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/395114166e0)

- frontend：`source_materials/frontend_calls.json`


### 获取所有config的任务

**操作标识：** `GET /api/getAllConfiguredTasks`

**分类：** 任务config界面

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/getAllConfiguredTasks`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `g1t`；调用位置数量 3。

```javascript
function g1t(e){return nt({url:"/ApiCtrl/api/getAllConfiguredTasks",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/395063223e0)

- frontend：`source_materials/frontend_calls.json`


## 传感器相关

### 单元传感器界面数据

**操作标识：** `GET /api/unitSensors`

**分类：** 传感器相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitSensors`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | guid | string | 否 | 单元guid；文档examples：ee85da07-e79e-4e2b-ba15-6146b65f522f |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 否 |  |
| response | data.category | array[string] | 否 |  |
| response | data.complyElectromagnetic | string | 是 |  |
| response | data.sensorList | array [object] | 否 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "category": [
            "sonar",
            "ECM"
        ],
        "complyElectromagnetic": "true",
        "sensorList": [
            {
                "id": "08009a4e-6eca-4ddf-a2bc-dfed00fd179a",
                "name": "88型雷达",
                "open": 2,
                "status": "正常工作",
                "type": "雷达, 对空 & 海搜索, 3D 长距离"
            },
            {
                "id": "e11ccd1b-37b9-47d4-ba7c-f43c6ea47b5b",
                "name": "88型雷达",
                "open": 2,
                "status": "正常工作",
                "type": "雷达, 对空 & 海搜索, 3D 长距离"
            },
            {
                "id": "da72aa4c-1614-4604-8539-fcbfd28b7a9d",
                "name": "88型雷达",
                "open": 2,
                "status": "正常工作",
                "type": "雷达, 对空 & 海搜索, 3D 长距离"
            },
            {
                "id": "d50f4b0e-f582-4b98-acad-c3e86c8293df",
                "name": "电子support/测量系统[中级]",
                "open": 0,
                "status": "正常工作",
                "type": "电子情报收集"
            },
            {
                "id": "cbfc1204-08e5-42da-a8b4-2bbc3fc7f74f",
                "name": "目视观察",
                "open": 0,
                "status": "正常工作",
                "type": ""
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-10-28 17:07:26"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Dyt`；调用位置数量 1。

```javascript
function Dyt(e){return nt({url:"/ApiCtrl/api/unitSensors",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/367896942e0)

- frontend：`source_materials/frontend_calls.json`


### 单元传感器界面操作

**操作标识：** `POST /api/unitSensors`

**分类：** 传感器相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitSensors`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | guid | string | 是 | 单元id；文档examples：ef65f066-0fd3-4688-9710-5bbc89065a68 |
| body | complyElectromagnetic | enum<string> | 否 | 作战单元遵循电磁管控规则；不修改就不要传该参数；文档examples：true, flase |
| body | categorySwitch | enum<string> | 否 | 传感器类型开关字符串；不修改就不要传该参数；枚举：RADER=true, RADER=false, SONAR=true, SONAR=false, OECM=true, OECM=false |
| body | sensorList | array [object] | 否 | 传感器id 数组；不修改就不要传该参数 |
| body | sensorList.id | string | 是 | 传感器id |
| body | sensorList.open | string | 是 | 传感器是否开关机 |
| body | type | enum<string> | 是 | 操作指令；枚举：setEMCON, setCategorySwitch, setOnOff, addSensor, removeSensor |
| body | sensorGuid | string | 否 | 传感器GUID；删除传感器时传入该参数 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "guid": "ee85da07-e79e-4e2b-ba15-6146b65f522f",
    "type": "setEMCON",
    "complyElectromagnetic": "false",
    // "type": "setCategorySwitch",
    // "categorySwitch": "RADER=true",
    // "type": "setOnOff",
    // "sensorList": [
    //     {
    //         "id": "6add9f73-b008-4dc5-9cc9-35e0c323348f",
    //         "open": "true"
    //     }
    // ],
}
```

### 雷达类型开机

```json
{
    "guid": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    // "type": "setEMCON",
    // "complyElectromagnetic": "true",
    "type": "setCategorySwitch",
    "categorySwitch": "RADER=true",
    // "type": "setOnOff",
    // "sensorList": [
    //     {
    //         "id": "6add9f73-b008-4dc5-9cc9-35e0c323348f",
    //         "open": "true"
    //     }
    // ],
}
```

### 设置遵守电磁管控条例

```json
{
    "guid": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "type": "setEMCON",
    "complyElectromagnetic": "true",
    // "type": "setCategorySwitch",
    // "categorySwitch": "RADER=true",
    // "type": "setOnOff",
    // "sensorList": [
    //     {
    //         "id": "6add9f73-b008-4dc5-9cc9-35e0c323348f",
    //         "open": "true"
    //     }
    // ],
}
```

### 删除传感器

```json
{
    "guid": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "type": "removeSensor",
    "sensorGuid": "11"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.category | array[string] | 否 |  |
| response | data.complyElectromagnetic | string | 是 |  |
| response | data.sensorList | array [object] | 否 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "complyElectromagnetic": "false",
        "sensorList": [
            {
                "id": "6add9f73-b008-4dc5-9cc9-35e0c323348f",
                "name": "J-20 机载有源相控阵雷达",
                "open": 2,
                "status": "正常工作",
                "type": "雷达, 火控雷达, 空对空 & 对海, 长距离"
            },
            {
                "id": "1670f694-7bd8-4bea-9458-3065f602ec9f",
                "name": "EORD-31前视红外搜索跟踪系统",
                "open": 0,
                "status": "正常工作",
                "type": "成像红外搜索与追踪"
            },
            {
                "id": "98ee50c1-c2d6-4fc1-b74b-56dadf03cb1e",
                "name": "国产光电分布式孔径系统",
                "open": 0,
                "status": "正常工作",
                "type": "红外, 日/夜球型态势感知能力 & 火控能力"
            },
            {
                "id": "0e032214-0800-4ff7-8048-3473ad78b1de",
                "name": "国产导弹逼近告警系统(光电分布式孔径)",
                "open": 0,
                "status": "正常工作",
                "type": "导弹来袭警告系统"
            },
            {
                "id": "6ba00812-bdf6-425b-9545-09f1f474c845",
                "name": "国产BM/KJ-8602C电子support/测量系统[SPS-1000]",
                "open": 0,
                "status": "正常工作",
                "type": "雷达告警接收机"
            },
            {
                "id": "d3493c5b-5986-4e7b-a65f-2e759ff6ab27",
                "name": "通用综合防御电子对抗系统",
                "open": 0,
                "status": "正常工作",
                "type": "防御型 ECM"
            },
            {
                "id": "facd8f3d-c145-4b5b-bfdf-9434e3e5668f",
                "name": "通用激光测距仪",
                "open": 2,
                "status": "正常工作",
                "type": "激光测距仪"
            },
            {
                "id": "87045619-c7d7-4246-9f64-ecfbd8b00b1b",
                "name": "目视观察",
                "open": 0,
                "status": "正常工作",
                "type": ""
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-10-28 21:18:35"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Pyt`；调用位置数量 4。

```javascript
function Pyt(e){return nt({url:"/ApiCtrl/api/unitSensors",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 现有连接器使用 RADER=true/false，这个拼写按接口保留，不自动改为 RADAR。

- 文档按不同 type 使用不同字段，必须取对应examples。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/367949477e0)

- frontend：`source_materials/frontend_calls.json`


## 修改开关，并写回 config/config.ini

### 修改开关，并写回 config/config.ini

**操作标识：** `POST /api/unitDeployment/templateMaxLimit`

**分类：** 修改开关，并写回 config/config.ini

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitDeployment/templateMaxLimit`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{ "enforceTemplateMaxNum": false }
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/451783526e0)


## 兵力分析与统计

### 获取战损统计

**操作标识：** `GET /api/GetLossesAndExpenditures`

**分类：** 兵力分析与统计

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetLossesAndExpenditures`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Bo1`；调用位置数量 1。

```javascript
function Bo1(n){return G5({url:"/ApiCtrl/api/GetLossesAndExpenditures",method:"get",headers:{"Content-Type":"application/json"},params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380614132e0)

- frontend：`source_materials/frontend_calls.json`


## 兵力部署相关

### 界面config操作

**操作标识：** `POST /api/InterfaceRule`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/InterfaceRule`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "type_id":"",
    "rule":""
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `u1t`；调用位置数量 1。

```javascript
function u1t(e){return nt({url:"/ApiCtrl/api/InterfaceRule",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/391356542e0)

- frontend：`source_materials/frontend_calls.json`


### 获取添加单元界面数据

**操作标识：** `POST /api/addUnitOperation`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

目前只支持飞机，

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | model | string | 否 | 型号或名称 |
| body | category | string | 否 | ；类型id   界面数据结构获取 |
| body | country | string | 是 | 国家 |
| body | hypothesis | string | 是 | ；0列装  1,假设  2所有 |
| body | startNum | string | 是 | 1    第几页 |
| body | pageNum | string | 是 | ；20    一页几条数据 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "model": "",
    "category": "16",
    "country": "美国",
    "hypothesis": "2",
    "startNum": "1",
    "pageNum": "20"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.data | array [object] | 是 |  |
| response | data.total | integer | 是 | 总页数 |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "data": [
            {
                "Guid": "hsfw-dataaircraft-000000000006",
                "YearCommissioned": 1995,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "-",
                "id": 6,
                "name": "F-15E型“攻击鹰”战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000158",
                "YearCommissioned": 1981,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "-",
                "id": 158,
                "name": "F-16A型战隼战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000198",
                "YearCommissioned": 2003,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "保留， Blk 30",
                "id": 198,
                "name": "F-16C型\"战隼\"战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000223",
                "YearCommissioned": 1985,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "C Blk 25",
                "id": 223,
                "name": "F-16型“战隼”战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000278",
                "YearCommissioned": 2017,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "-",
                "id": 278,
                "name": "F-35A型\"闪电Ⅱ\"战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000314",
                "YearCommissioned": 1992,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "第40批次",
                "id": 314,
                "name": "F-16CG型“战隼”第40批次战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000315",
                "YearCommissioned": 1992,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "第42批次",
                "id": 315,
                "name": "F-16CG型“战隼”第42批次战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000316",
                "YearCommissioned": 1993,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "第50批次",
                "id": 316,
                "name": "F-16CJ型“战隼”第50批次战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000317",
                "YearCommissioned": 1993,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "第52批次",
                "id": 317,
                "name": "F-16CJ型“战隼”第52批次战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000322",
                "YearCommissioned": 2003,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "通用config实施方案（CCIP），Blk 52",
                "id": 322,
                "name": "F-16CM型“战隼”第52批次战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000323",
                "YearCommissioned": 2003,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "通用config实施方案（CCIP），Blk 50",
                "id": 323,
                "name": "F-16CM型“战隼”第50批次战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000332",
                "YearCommissioned": 1995,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "第52批次",
                "id": 332,
                "name": "F-16CJ型“战隼”第52批次战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000333",
                "YearCommissioned": 2006,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "第30批次",
                "id": 333,
                "name": "F-22A型“猛禽”战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000492",
                "YearCommissioned": 2003,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "保留， Blk 32",
                "id": 492,
                "name": "F-16C型“战隼”第32批次战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000494",
                "YearCommissioned": 2001,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "MMC任务计算机，Blk 40",
                "id": 494,
                "name": "F-16CG型“战隼”战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000495",
                "YearCommissioned": 2001,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "MMC任务计算机，Blk 42",
                "id": 495,
                "name": "F-16CG型“战隼”战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000521",
                "YearCommissioned": 1995,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "第50批次",
                "id": 521,
                "name": "F-16CJ型“战隼”第50批次战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000534",
                "YearCommissioned": 2016,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "-",
                "id": 534,
                "name": "F-35B型\"闪电Ⅱ\"战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000582",
                "YearCommissioned": 1999,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "第40批次",
                "id": 582,
                "name": "F-16CG型“战隼”战斗机"
            },
            {
                "Guid": "hsfw-dataaircraft-000000000586",
                "YearCommissioned": 1999,
                "YearDecommissioned": 0,
                "country": "美国",
                "description": "第42批次",
                "id": 586,
                "name": "F-16CG型“战隼”42批次战斗机"
            }
        ],
        "total": 174
    },
    "message": "succeed",
    "timestamp": "2025-10-29 19:13:55"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Syt`；调用位置数量 3。

```javascript
function Syt(e){return nt({url:"/ApiCtrl/api/addUnitOperation",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/367337685e0)

- frontend：`source_materials/frontend_calls.json`


### 添加卫星接口

**操作标识：** `POST /api/addUnitOperation/addSatellites`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/addSatellites`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | sideGuid | string | 是 | 推演方guid |
| body | Satellites | array [object] | 是 |  |
| body | Satellites.sID | string | 是 | ；level 3 ID |
| body | Satellites.oID | string | 是 | ；level 4 ID |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "sideGuid": "6f2da012-0c8b-49f2-9d41-dc00eb48d27e",
    "Satellites": [
        {
            "sID": "hsfw-datasatellite-00000000073",
            "oID": "1"
        }
    ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `qyt`；调用位置数量 2。

```javascript
function qyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/addSatellites",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377998597e0)

- frontend：`source_materials/frontend_calls.json`


### 复制兵力接口

**操作标识：** `POST /api/addUnitOperation/copy`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/copy`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unitGuid":"0f947c85-f484-4193-b310-425f19875941",
    "longitude": 115.317,
	"latitude": 24.64,
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Gyt`；调用位置数量 1。

```javascript
function Gyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/copy",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376925364e0)

- frontend：`source_materials/frontend_calls.json`


### 获取添加单元界面数据结构接口

**操作标识：** `GET /api/addUnitOperation/dataStructure`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/dataStructure`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 用途补充

获取单元分类数、国家数据、推演方

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `wyt`；调用位置数量 2。

```javascript
function wyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/dataStructure",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/369106899e0)

- frontend：`source_materials/frontend_calls.json`


### 删除单元接口

**操作标识：** `POST /api/addUnitOperation/del`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/del`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | delUnits | array[string] | 是 |  |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "delUnits":[
        "dd564499-aeec-476b-ab89-6dcc58ad0112"
    ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Hyt`；调用位置数量 3。

```javascript
function Hyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/del",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376582101e0)

- frontend：`source_materials/frontend_calls.json`


### 删除本方所有兵力

**操作标识：** `POST /api/addUnitOperation/delSideUnits`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/delSideUnits`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | side | string | 是 | 推演方名字 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "side":"1234"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Kyt`；调用位置数量 1。

```javascript
function Kyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/delSideUnits",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/378557044e0)

- frontend：`source_materials/frontend_calls.json`


### 编辑单元货物

**操作标识：** `POST /api/addUnitOperation/editGoods`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/editGoods`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

添加或删除货物

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | option | string | 是 | ；选项   add    del |
| body | unitID | string | 是 | 单元guid |
| body | id | string | 是 | 货物的id |
| body | number | integer | 是 | 数量 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "option":"del",
    "unitID":"76040d54-01da-4830-929d-17805b714ae5",
    "id":"hsfw-datamount-000000000002520",
    "number":2
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": [
        {
            "ID": "hsfw-datamount-000000000002402",
            "name": "120mm/24 2S9-1 Sviristelka 自行迫击炮(1984)",
            "number": 10
        },
        {
            "ID": "hsfw-datamount-000000000002520",
            "name": "10式 “人丸” 主战坦克(日本, 2013)",
            "number": 6
        }
    ],
    "message": "succeed",
    "timestamp": "2025-11-18 17:54:40"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Lyt`；调用位置数量 2。

```javascript
function Lyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/editGoods",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/378330543e0)

- frontend：`source_materials/frontend_calls.json`


### 获取编辑货物界面数据接口

**操作标识：** `GET /api/addUnitOperation/getAllGoods`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/getAllGoods`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | guid | string | 否 | ；文档examples：88c41b68-0c5f-4020-baa9-6522331a6c53 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `kyt`；调用位置数量 1。

```javascript
function kyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/getAllGoods",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/378100724e0)

- frontend：`source_materials/frontend_calls.json`


### 获取所有卫星数据

**操作标识：** `GET /api/addUnitOperation/getAllSatellite`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/getAllSatellite`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

四层结构 国家》类型》卫星》轨道

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | array [object] | 是 |  |
| response | data.ID | string | 是 |  |
| response | data.children | array [object] | 是 |  |
| response | data.level | integer | 是 |  |
| response | data.name | string | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Yyt`；调用位置数量 1。

```javascript
function Yyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/getAllSatellite",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377779455e0)

- frontend：`source_materials/frontend_calls.json`


### 获取当前实体内已有的货物

**操作标识：** `GET /api/addUnitOperation/getUnitGoodsAlready`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/getUnitGoodsAlready`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | guid | string | 否 | ；文档examples：76040d54-01da-4830-929d-17805b714ae5 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | ID | string | 否 |  |
| response | name | string | 否 |  |
| response | number | string | 否 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
[
    {
        "ID":"",
        "name":"",
        "number":""
    }


]



```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Iyt`；调用位置数量 1。

```javascript
function Iyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/getUnitGoodsAlready",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/378176561e0)

- frontend：`source_materials/frontend_calls.json`


### 添加单元操作

**操作标识：** `POST /api/addUnitOperation/handle`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/handle`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | guid | string | 是 | dbgud |
| body | longitude | number | 是 | 经度 |
| body | latitude | number | 是 | 纬度 |
| body | altitude | number | 是 | 高度 |
| body | loadoutID | string | 是 | 挂载方案guid |
| body | type | string | 是 | ；类型 Aircraft,Ship,Submarine,Facility |
| body | side | string | 是 | 推演方 |
| body | unitname | string | 是 | 单元名称 |
| body | parentID | string | 否 | ；army    部队GUID |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
			"guid": "hsfw-datasubmarine-00000000003",
			"longitude": 126.68,
			"latitude": 20.68,
			"altitude": 10000.2223,
			"loadoutID": "",
			"type": "Submarine",
			"side": "红方",
			"unitname": "过秀兰",
            "parentID": ""
}
```

### 添加部队

```json
{
    "type": "Army",
    "side": "红方",
    "unitname": "吴娟",
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "message": "succeed",
    "timestamp": "2025-10-31 10:51:48"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `xyt`；调用位置数量 3。

```javascript
function xyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/handle",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368754374e0)

- frontend：`source_materials/frontend_calls.json`


### 获取飞机挂载方案数据

**操作标识：** `GET /api/addUnitOperation/loadOut`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/loadOut`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | guid | string | 否 | ；飞机数据库id    测试数据  f-16cd的dbid；文档examples：0159c6be-8a5b-45b5-ac8b-18f2f00c76ea |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | array [object] | 是 |  |
| response | data.guid | string | 是 | 挂载guid |
| response | data.loadoutName | string | 是 | 挂载方案名称 |
| response | data.weapon | array [object] | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Cyt`；调用位置数量 1。

```javascript
function Cyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/loadOut",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368756369e0)

- frontend：`source_materials/frontend_calls.json`


### 移动兵力接口

**操作标识：** `POST /api/addUnitOperation/moveUnit`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/moveUnit`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | unitId | string | 是 | 单元ID |
| body | longitude | number | 是 | 经度 |
| body | latitude | number | 是 | 纬度 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unitId":"76040d54-01da-4830-929d-17805b714ae5",
    "longitude": 115.317,
	"latitude": 24.64,
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Uyt`；调用位置数量 1。

```javascript
function Uyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/moveUnit",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376926294e0)

- frontend：`source_materials/frontend_calls.json`


### 重命名兵力

**操作标识：** `POST /api/addUnitOperation/reNameUnit`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/reNameUnit`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | unitId | string | 是 | 单元Guid |
| body | name | string | 是 | 修改后的名字 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unitId":"76040d54-01da-4830-929d-17805b714ae5",
    "name":"11111",
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Wyt`；调用位置数量 3。

```javascript
function Wyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/reNameUnit",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376927342e0)

- frontend：`source_materials/frontend_calls.json`


### 获取单元信息框的货物数据

**操作标识：** `GET /api/getUnitCargoData`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/getUnitCargoData`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | guid | string | 否 | 单元id |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "maxCargo_Crew": 1.0,
    "maxCargo_Area": 1.0,
    "maxCargo_Mass": 1.0,
    "Cargos": [
        {
            "id": "",
            "name": "",
            "number:"",
            "Cargo_Mass": 1.0,
            "Cargo_Area": 1.0,
            "Cargo_Crew": 1.0
        }
    ]
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `r1t`；调用位置数量 1。

```javascript
function r1t(e){return nt({url:"/ApiCtrl/api/getUnitCargoData",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389940170e0)

- frontend：`source_materials/frontend_calls.json`


### 获取某个单元类型的rule

**操作标识：** `GET /api/getUnitTypeRule`

**分类：** 兵力部署相关

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/getUnitTypeRule`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | type_id | string | 否 | 类型id |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/391722739e0)


## 前端补充

### subscribe（前端补充）

**操作标识：** `POST /api/station/subscribe`

**分类：** 前端补充

**资料依据：** 前端src证据

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/station/subscribe`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `subscribe-CW8AO0i3.js`，函数 `s`；调用位置数量 0。

```javascript
function s(t){return i({url:"/ApiCtrl/api/station/subscribe",method:"post",data:t})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- frontend：`source_materials/frontend_calls.json`


### unsubscribe（前端补充）

**操作标识：** `POST /api/station/unsubscribe`

**分类：** 前端补充

**资料依据：** 前端src证据

**资料中的地址：** `http://127.0.0.1:8082/ApiCtrl/api/station/unsubscribe`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `subscribe-CW8AO0i3.js`，函数 `u`；调用位置数量 0。

```javascript
function u(t){return i({url:"/ApiCtrl/api/station/unsubscribe",method:"post",data:t})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- frontend：`source_materials/frontend_calls.json`


## 区域相关

### 获取区域

**操作标识：** `GET /api/GetZone`

**分类：** 区域相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetZone`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Type | string | 否 | ；NoNavZone 禁航区  ExclusionZone 封锁区；文档examples：NoNavZone |
| query | SideGuid | string | 否 | 推演方GUid；文档examples：05fc90c5-1a48-47dc-bd5c-7d66e1037306 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.NoNavZones | array [object] | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "NoNavZones": [
            {
                "Aircraft": false,
                "AreaRefPoints": [
                    {
                        "id": "4bf70994-b034-4d77-b0a2-65b529774bf0",
                        "latitude": "22.5233",
                        "longitude": "116.109",
                        "name": "RP1"
                    },
                    {
                        "id": "35d36f1e-a6bd-461e-9aec-63aac51b30c0",
                        "latitude": "22.4714",
                        "longitude": "117.886",
                        "name": "RP2"
                    },
                    {
                        "id": "3a8923a4-d28d-4337-9823-4ff84b3b012b",
                        "latitude": "21.2305",
                        "longitude": "117.82",
                        "name": "RP3"
                    },
                    {
                        "id": "b434388c-6a65-4cba-be09-783422dd07ed",
                        "latitude": "21.2789",
                        "longitude": "116.051",
                        "name": "RP4"
                    }
                ],
                "Description": "测试禁航区",
                "Facility": true,
                "Guid": "3daaee9a-52fb-4388-91d6-0e7a88dc5fa8",
                "IsActive": true,
                "Locked": false,
                "PointsVisible": false,
                "Ship": true,
                "Submarine": true
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-11-20 17:07:16"
}
```

### 封锁区

```json
{
    "code": 0,
    "data": {
        "ExclusionZones": [
            {
                "Aircraft": false,
                "AreaRefPoints": [
                    {
                        "id": "4bf70994-b034-4d77-b0a2-65b529774bf0",
                        "latitude": "22.5233",
                        "longitude": "116.109",
                        "name": "RP1"
                    },
                    {
                        "id": "35d36f1e-a6bd-461e-9aec-63aac51b30c0",
                        "latitude": "22.4714",
                        "longitude": "117.886",
                        "name": "RP2"
                    },
                    {
                        "id": "3a8923a4-d28d-4337-9823-4ff84b3b012b",
                        "latitude": "21.2305",
                        "longitude": "117.82",
                        "name": "RP3"
                    },
                    {
                        "id": "b434388c-6a65-4cba-be09-783422dd07ed",
                        "latitude": "21.2789",
                        "longitude": "116.051",
                        "name": "RP4"
                    }
                ],
                "Description": "测试封锁区改",
                "Facility": true,
                "Guid": "5e4177c3-a924-4c73-aea9-eb1d643e1667",
                "IsActive": true,
                "MarkViolatorAs": "Hostile",
                "PointsVisible": false,
                "Ship": true,
                "Submarine": true
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-11-20 17:06:43"
}
```

### 成功examples

```json
{
    "code": 0,
    "data": {
        "NoNavZones": [
            {
                "Aircraft": true,
                "AreaRefPoints": [
                    {
                        "id": "4bf70994-b034-4d77-b0a2-65b529774bf0",
                        "latitude": "22.5233",
                        "longitude": "116.109",
                        "name": "RP1"
                    },
                    {
                        "id": "35d36f1e-a6bd-461e-9aec-63aac51b30c0",
                        "latitude": "22.4714",
                        "longitude": "117.886",
                        "name": "RP2"
                    }
                ],
                "Description": "测试禁航区",
                "Facility": true,
                "Guid": "298d4adc-fec3-45b9-9b68-e5323b553b46",
                "IsActive": true,
                "Locked": true,
                "PointsVisible": false,
                "Ship": true,
                "Submarine": true
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-11-20 15:28:14"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `S2t`；调用位置数量 2。

```javascript
function S2t(e){return nt({url:"/ApiCtrl/api/GetZone",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/379046381e0)

- frontend：`source_materials/frontend_calls.json`


### 设置区域

**操作标识：** `POST /api/SetZone`

**分类：** 区域相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/SetZone`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | Type | enum<string> | 是 | 类型；枚举：AddZone, SetZone, RemoveZone |
| body | Guid | string | 否 | 区域GUID；修改删除时使用 |
| body | SideGuid | string | 是 | 推演方GUID |
| body | ZoneType | string | 是 | 区域类型 |
| body | Description | string | 否 | 区域描述；添加区域时可添可不添 |
| body | Areas | array[string] | 否 | 区域点集 |
| body | IsActive | boolean | 否 | 是否启用 |
| body | Locked | boolean | 否 | 区域锁定 |
| body | Aircraft | boolean | 否 | 是否作用于飞机 |
| body | Ship | boolean | 否 | 是否作用于船 |
| body | Submarine | boolean | 否 | 是否作用与潜艇 |
| body | Facility | boolean | 否 | 是否作用于地面设施 |
| body | PointsVisible | boolean | 否 | 参考点可见 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Type": "SetZone",
    "SideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "ZoneType": "ExclusionZone",
    "Areas": [
        "4bf70994-b034-4d77-b0a2-65b529774bf0",
        "35d36f1e-a6bd-461e-9aec-63aac51b30c0",
        "3a8923a4-d28d-4337-9823-4ff84b3b012b",
        "b434388c-6a65-4cba-be09-783422dd07ed"
    ],
    "Description": "测试封锁区改",
    "Facility": true,
    "Guid": "5e4177c3-a924-4c73-aea9-eb1d643e1667",
    "IsActive": true,
    "Aircraft": false,
    "Ship": true,
    "Submarine": true,
    "PointsVisible": true,
    "MarkAs": "Hostile"
}
```

### 添加禁航区

```json
{
    "Type": "AddZone",
    "SideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "ZoneType": "NoNavZone",
    "Description": "测试禁航区",
    "Guid": "3daaee9a-52fb-4388-91d6-0e7a88dc5fa8",
    "Areas": [
        "4bf70994-b034-4d77-b0a2-65b529774bf0",
        "35d36f1e-a6bd-461e-9aec-63aac51b30c0",
        "3a8923a4-d28d-4337-9823-4ff84b3b012b",
        "b434388c-6a65-4cba-be09-783422dd07ed"
    ]
}
```

### 设置禁航区

```json
{
    "Type": "SetZone",
    "SideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "ZoneType": "NoNavZone",
    "Areas": [
        "4bf70994-b034-4d77-b0a2-65b529774bf0",
        "35d36f1e-a6bd-461e-9aec-63aac51b30c0",
        "3a8923a4-d28d-4337-9823-4ff84b3b012b",
        "b434388c-6a65-4cba-be09-783422dd07ed"
    ],
    "Description": "测试禁航区改",
    "Facility": true,
    "Guid": "3daaee9a-52fb-4388-91d6-0e7a88dc5fa8",
    "IsActive": true,
    "Locked": false,
    "Aircraft": false,
    "Ship": true,
    "Submarine": true,
    "PointsVisible": true
}
```

### 添加封锁区

```json
{
    "Type": "AddZone",
    "SideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "ZoneType": "ExclusionZone",
    "Description": "测试封锁区",
    "Guid": "5e4177c3-a924-4c73-aea9-eb1d643e1667",
    "Areas": [
        "4bf70994-b034-4d77-b0a2-65b529774bf0",
        "35d36f1e-a6bd-461e-9aec-63aac51b30c0",
        "3a8923a4-d28d-4337-9823-4ff84b3b012b",
        "b434388c-6a65-4cba-be09-783422dd07ed"
    ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `C2t`；调用位置数量 10。

```javascript
function C2t(e){return nt({url:"/ApiCtrl/api/SetZone",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/379225921e0)

- frontend：`source_materials/frontend_calls.json`


## 区域config界面

### 获取当前想定的已有区域

**操作标识：** `GET /api/ScenArea`

**分类：** 区域config界面

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ScenArea`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | type | string | 否 | ；all    或者  推演方名称；文档examples：all |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `_1t`；调用位置数量 20。

```javascript
function _1t(e){return nt({url:"/ApiCtrl/api/ScenArea",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/396100861e0)

- frontend：`source_materials/frontend_calls.json`


### 添加想定区域类型

**操作标识：** `POST /api/ScenArea`

**分类：** 区域config界面

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ScenArea`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
//添加区域
{
    "option":"addArea",
    "side":"中国",//推演方名称
    "areaType":"201",//模板类型id
    "area_name":"区域q",//名字
    "area_remark":"",  //备注
    "area_points":[
        {
            "id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",//参考点的区域id
            "x":1.23,//经度
            "y":1.23//纬度
        },
        {
            "id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",//参考点的区域id
            "x":1.23,//经度
            "y":1.23//纬度
        }
    ]
//     "area_missions":[   任务关联写单独的接口
//         "",
//         "",
//         ""
//     ],
}

// //修改区域
// {
//     "option":"alterArea",
//     "side":"中国",//推演方名称
//     "area_id":"{d65b9020-1664-4bb0-b562-360588168e84}",//区域id
//     "area_name":"区域qqqqqqqqq",//名字
//     "area_remark":"",  //备注
//     "area_points":[
//         {
//             "id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",//参考点的区域id
//             "x":1.23,//经度
//             "y":1.23//纬度
//         },
//         {
//             "id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",//参考点的区域id
//             "x":1.23,//经度
//             "y":1.23//纬度
//         }
//     ]
// //     "area_missions":[   任务关联写单独的接口
// //         "",
// //         "",
// //         ""
// //     ],
// }

//删除区域
{

    "option":"delArea",
    "side":"中国",//推演方名称
    "area_id":"{d65b9020-1664-4bb0-b562-360588168e84}",//区域id




}

```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `w1t`；调用位置数量 4。

```javascript
function w1t(e){return nt({url:"/ApiCtrl/api/ScenArea",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/396267696e0)

- frontend：`source_materials/frontend_calls.json`


### 获取区域数据

**操作标识：** `GET /api/regionalManagement`

**分类：** 区域config界面

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/regionalManagement`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | type | string | 否 | ；all    或者 大分类名称  空中区域 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `y1t`；调用位置数量 2。

```javascript
function y1t(e){return nt({url:"/ApiCtrl/api/regionalManagement",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/395718697e0)

- frontend：`source_materials/frontend_calls.json`


### 区域config操作

**操作标识：** `POST /api/regionalManagement`

**分类：** 区域config界面

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/regionalManagement`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
//添加区域大型
// {
//     "option":"addZoneType",
//     "typeName":"作战区域"
// }

// //修改区域名称
//  {
//      "id":"5",
//      "option":"alterZoneType",
//      "newTypeName":"一个新区域类型"
//  }
//  //删除区域
//  {
//     "option":"delZoneType",
//      "id":"5"
//  }
//
// //给某个大类型添加小类型
// {
//     "option":"addZone",
//     "type_id":"1", //大类型的id
//     "zone_name":"jkjk",
//     "zone_type":"dsds",
//     "zone_icon":"dsdsd",
//     "zone_color":"ssss",
//     "zone_remark":"aaaa"
// }
//修改某个小类型
{
    "option":"alterZone",
    "type_id":"1", //大类型的id
    "zone_id":"101",
    // "zone_name":"ddddddd",
     "zone_type":"dsds",
    // "zone_icon":"dsdsd",
    // "zone_color":"ssss",
    // "zone_remark":"aaaa"
}
//删除某个小类型
// {
//     "option":"delZone",
//     "type_id":"2", //大类型的id
//     "zone_id":"201"
// }
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `b1t`；调用位置数量 4。

```javascript
function b1t(e){return nt({url:"/ApiCtrl/api/regionalManagement",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/395846753e0)

- frontend：`source_materials/frontend_calls.json`


## 单元操作相关

### 自动被探测到

**操作标识：** `POST /api/Detected`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/Detected`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{

    "guid":"5811d5ff-056d-4153-bd5e-a9d72980e2fa",
    "autodetectable":true

}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Qyt`；调用位置数量 1。

```javascript
function Qyt(e){return nt({url:"/ApiCtrl/api/Detected",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381296403e0)

- frontend：`source_materials/frontend_calls.json`


### 获取单元系统毁伤信息

**操作标识：** `GET /api/GetUnitDamage`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetUnitDamage`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | 单元GUID；文档examples：e9a0f38c-8329-40ca-955e-5745e73e7307 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `hyt`；调用位置数量 1。

```javascript
function hyt(e){return nt({url:"/ApiCtrl/api/GetUnitDamage",method:"get",headers:{"Content-Type":"application/json"},params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376327578e0)

- frontend：`source_materials/frontend_calls.json`


### 获取单元包络航线信息

**操作标识：** `GET /api/GetunitEnvelopeInfoJson`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetunitEnvelopeInfoJson`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Dje`；调用位置数量 1。

```javascript
function Dje(e){return nt({url:"/ApiCtrl/api/GetunitEnvelopeInfoJson",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376309915e0)

- frontend：`source_materials/frontend_calls.json`


### 单元信息获取

**操作标识：** `GET /api/GetunitInfoJson`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetunitInfoJson`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；文档examples：7d7bbd0b-6f59-4dc8-b2ca-dda0d43a9b4e |
| query | Type | string | 否 | ；文档examples：Unit |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

### 页面默认examples

```json
{
    "code": 0,
    "message": "string",
    "timestamp": "string"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `_yt`；调用位置数量 1。

```javascript
function _yt(e){return nt({url:"/ApiCtrl/api/GetunitInfoJson",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380919310e0)

- frontend：`source_materials/frontend_calls.json`


### 设置方位

**操作标识：** `POST /api/Orientation`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/Orientation`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "guid":"5811d5ff-056d-4153-bd5e-a9d72980e2fa",//单元guid
    "orientation":25.0
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Jyt`；调用位置数量 1。

```javascript
function Jyt(e){return nt({url:"/ApiCtrl/api/Orientation",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381286953e0)

- frontend：`source_materials/frontend_calls.json`


### 航线规划

**操作标识：** `POST /api/PlottedCourse`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/PlottedCourse`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | Guid | string | 是 | 单元GUID |
| body | Courses | array [object] \| null | 是 | 航路点集合；为空则取消航线 |
| body | Courses.lon | number | 否 | 经度 |
| body | Courses.lat | number | 否 | 纬度 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
  "Guids": ["单元GUID1", "单元GUID2"],
  "Courses": [
    {"lon": 120.123456, "lat": 30.123456},
    {"lon": 121.654321, "lat": 31.654321}
  ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Aje`；调用位置数量 3。

```javascript
function Aje(e){return nt({url:"/ApiCtrl/api/PlottedCourse",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- Apifox 新examples用 Guids 数组；现有前端和项目连接器用 Guid 单值。两种形态均作为版本证据保留，本次未下发航线验证兼容性。

- Courses 点对象用 lon、lat；不要把经纬度位置倒置。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376050791e0)

- frontend：`source_materials/frontend_calls.json`


### 修改上级

**操作标识：** `POST /api/PostSuperiorInfo`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/PostSuperiorInfo`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | UnitGuid | string | 否 | ；文档examples：00 |
| query | SuperiorID | string | 否 | ；文档examples：00 |


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `displaySetting-C7KFV-dj.js`，函数 `s`；调用位置数量 0。

```javascript
function s(e){return t({url:"/ApiCtrl/api/PostSuperiorInfo",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381941922e0)

- frontend：`source_materials/frontend_calls.json`


### 设置单元毁伤状态

**操作标识：** `POST /api/SetUnitDamage`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/SetUnitDamage`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | Guid | string | 是 | 单元GUID |
| body | Units | array [object] | 否 |  |
| body | Units.ComponentGuid | string | 是 | 组件GUID |
| body | Units.status | enum<integer> | 是 | 状态；枚举：0, 1, 2, 3, 4 |
| body | DamageValue | integer | 否 | 总体毁伤；0-100 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Guid": "e9a0f38c-8329-40ca-955e-5745e73e7307",
    "Units": [
        {
            "ComponentGuid": "308b1176-9530-45b0-a901-a641761cb05f",
            "status": 1
        },
        {
            "ComponentGuid": "fc253dfb-3cde-4e10-9cba-400791997de6",
            "status": 2
        },
        {
            "ComponentGuid": "b63bdb87-1f6a-4ed5-a0d5-3a1051d06c94",
            "status": 3
        }
    ],
    "DamageValue": 0
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `vyt`；调用位置数量 190。

```javascript
function vyt(e){return nt({url:"/ApiCtrl/api/SetUnitDamage",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376391528e0)

- frontend：`source_materials/frontend_calls.json`


### 获取速度高度属性

**操作标识：** `GET /api/SpeedAlt`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/SpeedAlt`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

获取单元最大速度，最小速度，最大高度（深度），最小高度（深度）

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | 查询的单元Guid；文档examples：2bd20f78-20af-4cb1-a246-998e691e1e50 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.Type | string | 是 | 类型；CFacility地面设施，CShip船 都不显示高度，CAircraft飞机显示高度，CSubmarine潜艇 显示深度 |
| response | data.AddForce | boolean | 是 | 加力是否显示 |
| response | data.AddForceSpeed | string | 是 | 加力速度 |
| response | data.CruiseSpeed | string | 是 | 巡航速度 |
| response | data.CurrentAlt | string | 是 | 当前高度 |
| response | data.CurrentSpeed | string | 是 | 当前速度 |
| response | data.DesiredAlt | string | 是 | 期望高度 |
| response | data.DesiredSpeed | string | 是 | 期望速度 |
| response | data.Hover | boolean | 否 | 悬停是否显示 |
| response | data.HoverSpeed | string | 是 | 悬停速度 |
| response | data.LowSpeed | string | 是 | 低速速度 |
| response | data.MaxAlt | string | 是 | 最大高度 |
| response | data.MaxHeight | string | 否 | 预设最大高度值；飞机 |
| response | data.MaxHightAltitude | string | 否 | 预设高空（高）；飞机 |
| response | data.MaxLowAltitude | string | 否 | 预设低空高度（高）；飞机 |
| response | data.MaxSpeed | string | 是 | 最大速度 |
| response | data.MidAltitude | string | 否 | 预设中空 |
| response | data.Military | boolean | 否 | 军用是否显示 |
| response | data.MilitarySpeed | string | 是 | 军用速度 |
| response | data.MinHeight | string | 否 | 预设最小高度；飞机/潜艇 |
| response | data.MinAlt | string | 是 | 最小高度 |
| response | data.MinHightAltitude | string | 否 | 预设高空高度（低）；飞机 |
| response | data.MinLowAltitude | string | 否 | 预设低空高度（低）；飞机 |
| response | data.MinSpeed | string | 是 | 最小速度 |
| response | data.PD | string | 否 | 潜望镜深度；潜艇 |
| response | data.Shallow | string | 否 | 浅；潜艇 |
| response | data.ThermoclineDownDepth | string | 否 | 温跃层下；潜艇 |
| response | data.ThermoclineUpDepth | string | 否 | 温跃层上；潜艇 |
| response | data.WaterSurface | string | 否 | 水面；潜艇 |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "AddForce": false,
        "AddForceSpeed": "259.28",
        "CruiseSpeed": "231.5",
        "CurrentAlt": "609.6",
        "CurrentSpeed": "0",
        "DesiredAlt": "609.6",
        "DesiredSpeed": "0",
        "Hover": true,
        "HoverSpeed": "0",
        "LowSpeed": "101.86",
        "MaxAlt": "4572",
        "MaxHeight": "4572",
        "MaxHightAltitude": "10973",
        "MaxLowAltitude": "610",
        "MaxSpeed": "259.28",
        "MidAltitude": "3658",
        "Military": true,
        "MilitarySpeed": "259.28",
        "MinAlt": "0",
        "MinHeight": "0",
        "MinHightAltitude": "7620",
        "MinLowAltitude": "305",
        "MinSpeed": "0"
    },
    "message": "succeed",
    "timestamp": "2025-11-19 16:30:22"
}
```

### 潜艇

```json
{
    "code": 0,
    "data": {
        "AddForceSpeed": "55.56",
        "CruiseSpeed": "55.56",
        "CurrentAlt": "0",
        "CurrentSpeed": "7.408",
        "DesiredAlt": "0",
        "DesiredSpeed": "0",
        "HoverSpeed": "0",
        "LowSpeed": "55.56",
        "MaxAlt": "0",
        "MaxSpeed": "55.56",
        "MilitarySpeed": "55.56",
        "MinAlt": "0",
        "MinHeight": "-450",
        "MinSpeed": "0",
        "PD": "-20",
        "Shallow": "-40",
        "ThermoclineDownDepth": "-47",
        "ThermoclineUpDepth": "-12",
        "WaterSurface": "0"
    },
    "message": "succeed",
    "timestamp": "2025-11-19 16:31:29"
}
```

### 地面设施

```json
{
    "code": 0,
    "data": {
        "AddForceSpeed": "0",
        "CruiseSpeed": "0",
        "CurrentAlt": "786",
        "CurrentSpeed": "0",
        "DesiredAlt": "0",
        "DesiredSpeed": "0",
        "HoverSpeed": "0",
        "LowSpeed": "0",
        "MaxAlt": "0",
        "MaxSpeed": "55.56",
        "MilitarySpeed": "0",
        "MinAlt": "1e+07",
        "MinSpeed": "0"
    },
    "message": "succeed",
    "timestamp": "2025-11-19 16:32:17"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `fyt`；调用位置数量 1。

```javascript
function fyt(e){return nt({url:"/ApiCtrl/api/SpeedAlt",method:"get",headers:{"Content-Type":"application/json"},params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376206074e0)

- frontend：`source_materials/frontend_calls.json`


### 油门高度深度设置

**操作标识：** `POST /api/SpeedAlt`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/SpeedAlt`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | Type | enum<string> \| enum<null> | 是 | 操作类型；枚举：SetDesiredSpeed, SetDesiredAlt, UnSetDesiredSpeed, UnSetDesiredAlt |
| body | Value | string | 否 | 修改的值，手动覆盖的√取消可不填 |
| body | UnitGuid | string | 是 | 被操作单元guid |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Type": "SetDesiredSpeed",
    "Value": "string",
    "UnitGuid": "string"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `dyt`；调用位置数量 24。

```javascript
function dyt(e){return nt({url:"/ApiCtrl/api/SpeedAlt",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- Type、Value、UnitGuid 大小写必须保留；Value 在文档为字符串。

- 高度米、速度 km/h 是当前连接器约定。Apifox 没有完整写出单位，新增单元类型仍需用 GET SpeedAlt/frontend核验。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/375953697e0)

- frontend：`source_materials/frontend_calls.json`


### 获取有加油机的支援任务

**操作标识：** `GET /api/getMissionTanker`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/getMissionTanker`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | side | string | 否 |  |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389168832e0)


### 保持阵位-所选单元

**操作标识：** `POST /api/holdPosition`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/holdPosition`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "option":"one",//one  或者  all
    "unitGuids":"868cfcb6-e882-49d0-a4fa-9f78fae3caee",//单元fuid  当option为one时需要
    "sideGuid":"",// 当前推演方id 当option为all时需要
    "TrueOrFalse":true//是否保持阵位
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380301687e0)


### 获取油量和留空时间数据接口

**操作标识：** `GET /api/oilLevelAndIdleTime`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/oilLevelAndIdleTime`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | guid | string | 否 | 飞机的guid；文档examples：5811d5ff-056d-4153-bd5e-a9d72980e2fa |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Xyt`；调用位置数量 1。

```javascript
function Xyt(e){return nt({url:"/ApiCtrl/api/oilLevelAndIdleTime",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381164442e0)

- frontend：`source_materials/frontend_calls.json`


### 设置油量和留空时间接口

**操作标识：** `POST /api/oilLevelAndIdleTime`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/oilLevelAndIdleTime`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "option":"cal", //勾选自动计算  cal   不勾选 set
    "unitGuid":"5811d5ff-056d-4153-bd5e-a9d72980e2fa",
    "AbnTime": 588.0,   //留空时间  单位 秒
    "CurrentFuelQuantity": 147697   //当前油量
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Zyt`；调用位置数量 2。

```javascript
function Zyt(e){return nt({url:"/ApiCtrl/api/oilLevelAndIdleTime",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381160914e0)

- frontend：`source_materials/frontend_calls.json`


### 返航

**操作标识：** `POST /api/returnToBase`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/returnToBase`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unit_id":""
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `I1t`；调用位置数量 2。

```javascript
function I1t(e){return nt({url:"/ApiCtrl/api/returnToBase",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389116571e0)

- frontend：`source_materials/frontend_calls.json`


### 选择新基地

**操作标识：** `POST /api/selectNewBase`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/selectNewBase`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unit_id":"5811d5ff-056d-4153-bd5e-a9d72980e2fa",   //单元id
    "base_id":"609a1564-ad78-46a6-91aa-4b76e6022dcc"    //基地id或名称
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `k1t`；调用位置数量 2。

```javascript
function k1t(e){return nt({url:"/ApiCtrl/api/selectNewBase",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389472532e0)

- frontend：`source_materials/frontend_calls.json`


### 补给

**操作标识：** `POST /api/supply`

**分类：** 单元操作相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/supply`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unit_id":"",
    "tanker_guid":"",
    "mission_guid":""
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `L1t`；调用位置数量 4。

```javascript
function L1t(e){return nt({url:"/ApiCtrl/api/supply",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389151328e0)

- frontend：`source_materials/frontend_calls.json`


### 武器预设航线设置

**操作标识：** `POST /api/weaponPresetRoute`

**分类：** 单元操作相关

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/weaponPresetRoute`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "routeGuid":"",//更新时需要，创建不用制定
    "platformGuid": "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}",//必须
    "weaponRecordDbId": "hsfw-dataweapon-00000000001234",//必须
    "routeName": "对舰导弹预设航线",
    "wayPoints": ["123.456,34.567", "124.000,35.000,8000"],//必须
    //"applyNow": true
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/426759700e0)


## 反潜搜索行动相关

### 投放主动声呐浮标

**操作标识：** `POST /api/Anti-SubOperation/deployActiveSonar`

**分类：** 反潜搜索行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/Anti-SubOperation/deployActiveSonar`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unitGuid":"5811d5ff-056d-4153-bd5e-a9d72980e2fa",//单元id
    "depth":"shallow",//'deep'：温跃层之下，'shallow'：温跃层之上
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Lb`；调用位置数量 1。

```javascript
function Lb(n){return G5({url:"/ApiCtrl/api/Anti-SubOperation/deployActiveSonar",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381560752e0)

- frontend：`source_materials/frontend_calls.json`


### 部署吊放声呐

**操作标识：** `POST /api/Anti-SubOperation/deployDippingSonar`

**分类：** 反潜搜索行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/Anti-SubOperation/deployDippingSonar`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{


  "unitGuid":"5811d5ff-056d-4153-bd5e-a9d72980e2fa",//单元id


}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `zb`；调用位置数量 1。

```javascript
function zb(n){return G5({url:"/ApiCtrl/api/Anti-SubOperation/deployDippingSonar",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381567643e0)

- frontend：`source_materials/frontend_calls.json`


### 投放被动声呐浮标

**操作标识：** `POST /api/Anti-SubOperation/deployPassiveSonar`

**分类：** 反潜搜索行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/Anti-SubOperation/deployPassiveSonar`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unitGuid":"cc06b058-8ff5-40dc-9e85-dd66236f232f",//单元id
    "depth":"shallow",//'deep'：温跃层之下，'shallow'：温跃层之上
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Nb`；调用位置数量 1。

```javascript
function Nb(n){return G5({url:"/ApiCtrl/api/Anti-SubOperation/deployPassiveSonar",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/381489735e0)

- frontend：`source_materials/frontend_calls.json`


## 存数据agent用

### 获取之前的记录

**操作标识：** `GET /api/ChatRecord`

**分类：** 存数据agent用

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ChatRecord`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/397351354e0)


### 存数据

**操作标识：** `POST /api/ChatRecord`

**分类：** 存数据agent用

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ChatRecord`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{"chat_id": "group_10086",
"chat_name": "项目技术讨论组",
"create_time": "2025-12-26 09:30:00",
"messages": [
    {
        "msg_id": "msg_001",
        "sender": {
            "user_id": "user_001",
            "username": "张三",
            "avatar": "https://example.com/avatars/zhangsan.png"
        },
        "content": "大家好，今天讨论一下接口联调的问题",
        "msg_type": "text",
        "send_time": "2025-12-26 09:30:15",
        "is_read": true,
        "reply_to": ""
    },
    {
        "msg_id": "msg_002",
        "sender": {
            "user_id": "user_002",
            "username": "李四",
            "avatar": "https://example.com/avatars/lisi.png"
        },
        "content": "我这边接口返回的JSON格式有点问题，稍后发截图",
        "msg_type": "text",
        "send_time": "2025-12-26 09:31:20",
        "is_read": true,
        "reply_to": "msg_001"
    },
    {
        "msg_id": "msg_003",
        "sender": {
            "user_id": "user_002",
            "username": "李四",
            "avatar": "https://example.com/avatars/lisi.png"
        },
        "content": "https://example.com/screenshots/interface_error.png",
        "msg_type": "image",
        "send_time": "2025-12-26 09:32:45",
        "is_read": false,
        "reply_to": "msg_002"
    },
    {
        "msg_id": "msg_004",
        "sender": {
            "user_id": "user_003",
            "username": "王五",
            "avatar": "https://example.com/avatars/wangwu.png"
        },
        "content": "我看了下，是字段名大小写的问题，改成小写就好了",
        "msg_type": "text",
        "send_time": "2025-12-26 09:35:10",
        "is_read": false,
        "reply_to": "msg_003"
    }
],
"participants": [
    {
        "user_id": "user_001",
        "username": "张三",
        "join_time": "2025-12-20 10:00:00"
    },
    {
        "user_id": "user_002",
        "username": "李四",
        "join_time": "2025-12-20 10:05:00"
    },
    {
        "user_id": "user_003",
        "username": "王五",
        "join_time": "2025-12-20 10:10:00"
    }
],
"unread_count": 2
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/397351707e0)


## 常用单元config

### 删除config

**操作标识：** `POST /api/delUnitOften`

**分类：** 常用单元config

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/delUnitOften`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "option":"id",
    "unit_id":"1ss"

}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `h1t`；调用位置数量 1。

```javascript
function h1t(e){return nt({url:"/ApiCtrl/api/delUnitOften",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392965369e0)

- frontend：`source_materials/frontend_calls.json`


### 获取常用单元

**操作标识：** `GET /api/oftenUnit`

**分类：** 常用单元config

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/oftenUnit`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | unit_type | string | 否 | 单元类型 四种  ；文档examples：1 |
| query | filter_name | string | 否 | 用名称过滤 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | array [object] | 是 |  |
| response | data.unitCurNum | integer | 是 |  |
| response | data.unitGuid | string | 是 |  |
| response | data.unitIcon | string | 是 |  |
| response | data.unitMaxNum | integer | 是 |  |
| response | data.unitName | string | 是 |  |
| response | data.unitType | string | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": [
        {
            "unitCurNum": 0,
            "unitGuid": "string",
            "unitIcon": "string",
            "unitMaxNum": 0,
            "unitName": "string",
            "unitType": "string"
        }
    ],
    "message": "string",
    "timestamp": "string"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `d1t`；调用位置数量 3。

```javascript
function d1t(e){return nt({url:"/ApiCtrl/api/oftenUnit",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392245725e0)

- frontend：`source_materials/frontend_calls.json`


### 设置常用单元

**操作标识：** `POST /api/oftenUnit`

**分类：** 常用单元config

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/oftenUnit`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unit_guid":"1",//单元id
    "unit_type":"2",//单元类型
    "unit_name":"222",//单元名称
    "unit_icon":"44",//单元图标
    "max_Num":65,//最大数量
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `f1t`；调用位置数量 56。

```javascript
function f1t(e){return nt({url:"/ApiCtrl/api/oftenUnit",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392245810e0)

- frontend：`source_materials/frontend_calls.json`


## 弹药库相关

### 获取所有弹药库数据

**操作标识：** `GET /api/unitMagazine`

**分类：** 弹药库相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitMagazine`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

飞机、卫星、武器不显示弹药库

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | guid | array[string] | 否 | 单元ID；文档examples：["71ded661-af71-46bb-9eb5-66079062e059"] |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `a1t`；调用位置数量 1。

```javascript
function a1t(e){return nt({url:"/ApiCtrl/api/unitMagazine",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387361528e0)

- frontend：`source_materials/frontend_calls.json`


### 获取添加弹药库界面数据

**操作标识：** `GET /api/unitMagazine/getMagazines`

**分类：** 弹药库相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitMagazine/getMagazines`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | filterName | string | 否 | 根据名称过滤 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `i1t`；调用位置数量 1。

```javascript
function i1t(e){return nt({url:"/ApiCtrl/api/unitMagazine/getMagazines",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387380781e0)

- frontend：`source_materials/frontend_calls.json`


### 弹药库数据操作接口

**操作标识：** `POST /api/unitMagazine/operation`

**分类：** 弹药库相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitMagazine/operation`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "option": "addMagazine", //删除弹药库
    "unit_id": "639038df-08ce-40fa-9a6d-c9f157ff575d", //单元id
    "magazine_dbid": "f1d851ef-c4b4-4f06-8138-0276ff876301" //弹药库dbid
}
```

### 删除弹药库

```json
{
    "option": "delMagazine", //删除弹药库
    "unit_id": "", //单元id
    "magazine_dbid": "" //弹药库dbid
}
```

### 添加武器

```json
{
    "option": "addWeapon", //添加武器
    "unit_id": "", //单元id
    "mag_id": "", //弹药库id
    "wea_dbid": "", //武器记录dbid
    "isTenThousand": false //是否添加10000所选武器
}
```

### 删除武器

```json
{
    "option": "delWeapon", //删除武器
    "unit_id": "", //单元id
    "mag_id": "", //弹药库id
    "wea_id": "" //武器记录id
}
```

### 修改武器当前数量

```json
{
    "option": "changeCurLoad", //修改武器当前数量
    "unit_id": "", //单元id
    "mag_id": "", //弹药库id
    "wea_id": "", //武器记录id
    "cur_load": 20 //修改后的武器数量
}
```

### 设置弹药库状态

```json
{
    "option": "setState", //设置当前状态
    "unit_id": "", //单元id
    "mag_id": "", //弹药库id
    "state": "" //完好性状态标识符（包括：'正常运转'，'轻度毁伤'，'中度毁伤'，'重度毁伤'，'摧毁'）
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `o1t`；调用位置数量 6。

```javascript
function o1t(e){return nt({url:"/ApiCtrl/api/unitMagazine/operation",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387385058e0)

- frontend：`source_materials/frontend_calls.json`


## 想定相关

### 获取想定描述

**操作标识：** `GET /api/GetScenarioDescription`

**分类：** 想定相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetScenarioDescription`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.Description | string | 是 |  |
| response | data.Title | string | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "Description": "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\"  font-size:12pt; font-weight:400; font-style:normal;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123</p></body></html>",
        "Title": "测试传感器"
    },
    "message": "succeed",
    "timestamp": "2025-11-14 15:02:51"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Vyt`；调用位置数量 1。

```javascript
function Vyt(e){return nt({url:"/ApiCtrl/api/GetScenarioDescription",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376646076e0)

- frontend：`source_materials/frontend_calls.json`


### 获取某个想定信息

**操作标识：** `GET /api/GetScenarioDescriptionFile`

**分类：** 想定相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetScenarioDescriptionFile`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Path | string | 否 | ；文档examples：大赛scenarios/-飞地风雷-晋级赛版.scen |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `jyt`；调用位置数量 1。

```javascript
function jyt(e){return nt({url:"/ApiCtrl/api/GetScenarioDescriptionFile",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/380375222e0)

- frontend：`source_materials/frontend_calls.json`


### 获取想定列表

**操作标识：** `GET /api/GetScenarioFile`

**分类：** 想定相关

**资料依据：** 本机 JSON 实测；Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetScenarioFile`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | array [object] | 是 |  |
| response | data.id | string | 是 |  |
| response | data.name | string | 是 |  |
| response | data.type | string | 是 |  |
| response | data.children | array [object] | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": [
        {
            "id": "string",
            "name": "string",
            "type": "string",
            "children": [
                {
                    "id": "string",
                    "name": "string",
                    "type": "string",
                    "children": [
                        {
                            "id": "string",
                            "name": "string",
                            "type": "string"
                        }
                    ]
                }
            ]
        }
    ],
    "message": "string",
    "timestamp": "string"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `pyt`；调用位置数量 1。

```javascript
function pyt(e){return nt({url:"/ApiCtrl/api/GetScenarioFile",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 本机只读验证

- `http://127.0.0.1:8082/ApiCtrl/api/GetScenarioFile`：HTTP 200；2026-10-02 14:34:49 +0800；application/json; charset=utf-8

```json
{
  "code": 0,
  "data": [
    {
      "id": "{a3fd6d80-ac35-44d2-9f5d-5f1651dfbee7}",
      "name": "对陆打击.xml",
      "type": "file"
    },
    {
      "id": "{74c79f9a-dc9f-414d-9335-ea96d52255d9}",
      "name": "404v404.xml",
      "type": "file"
    },
    {
      "id": "{5fad0c02-514c-4eff-af7a-9556f0b72cb7}",
      "name": "4141.xml",
      "type": "file"
    },
    {
      "children": [
        {
          "id": "{2ab37447-4d0d-43d9-bf98-4be29f0baea6}",
          "name": "太西海驱逐战－综合（人人对战版）.scen.xml",
          "type": "file"
        },
        {
          "id": "{035e6f20-4818-469d-8b4f-33212d77f382}",
          "name": "太西海驱逐战-潜（TXH4）.scen.xml",
          "type": "file"
        },
        {
          "id": "{2a3fa6ad-c732-4478-af7f-cadd77a5a36c}",
          "name": "太西海驱逐战-海（TXH3）.scen.xml",
          "type": "file"
        },
        {
          "id": "{a9639d87-f425-4d20-9b6f-17651a0016f8}",
          "name": "太西海驱逐战-综合（人机）CCQC.scen.xml",
          "type": "file"
        },
        {
          "id": "{818bc40b-951b-44dc-a6b1-ff69582a30d6}",
          "name": "太西海驱逐战-天（TXH1）.scen.xml",
          "type": "file"
        },
        {
          "id": "{5ca8456c-4850-4351-9fa6-98ab9ff92a15}",
          "name": "太西海驱逐战-综合（人机版）.scen.xml",
          "type": "file"
        },
        {
          "id": "{0eca4c40-8290-44d8-99c3-1f97874173d5}",
          "name": "太西海争夺战-综合（人人版）.scen.xml",
          "type": "file"
        },
        {
          "id": "{0fa2ca5e-112c-4af0-9d3e-3c0f02fab94b}",
          "name": "太西海驱逐战-综合（人机）中北.scen.xml",
          "type": "file"
        },
        {
          "id": "{771d56a4-9556-4c45-98dd-4a8fcc0638a2}",
          "name": "太西海驱逐战-空（TXH2）.scen.xml",
          "type": "file"
        }
      ],
      "id": "{f712e5b6-a78d-42cd-8fb9-b7536c91f067}",
      "name": "太西海想定",
      "type": "directory"
    },
    {
      "id": "{9ab161cc-3ce2-47ad-ac82-ec2d300d6a04}",
      "name": "测试另存.xml",
      "type": "file"
    },
    {
      "children": [
        {
          "id": "{6bd742e3-af82-4d3f-8b0d-974d5c7569df}",
          "name": "Scen1Sub.xml",
          "type": "file"
        },
        {
          "id": "{1af442a8-387c-4baa-afbd-03eb61894319}",
          "name": "Scen1Aircraft.xml",
          "type": "file"
        },
        {
          "id": "{bdf85d17-c1f3-4fbc-8f34-a5b380c171c1}",
          "name": "Scen1Ship.xml",
          "type": "file"
        },
        {
          "id": "{cd290bfc-282d-4d60-81a8-dc670b94cb92}",
          "name": "Scen1Sat.xml",
          "type": "file"
        },
        {
          "id": "{d81b7b97-6d4c-4766-b6c3-8a5130a5e64a}",
          "name": "Scen1Fac.xml",
          "type": "file"
        }
      ],
      "id": "{35d447e6-454a-43ce-b615-6f2045b12f1b}",
      "name": "单一想定",
      "type": "directory"
    },
    {
      "id": "{55e9f56c-324e-4352-99ae-c8d7e33c8d59}",
      "name": "另存测试.scen",
      "type": "file"
    },
    {
      "children": [
        {
          "id": "{f610483f-5c64-4aab-b3b8-0184ab15eed3}",
          "name": "210v210在空.scen",
          "type": "file"
        },
        {
          "id": "{4d0b3108-d54b-40a0-95da-338806f7c2ec}",
          "name": "300V300.scen",
          "type": "file"
        },
        {
          "id": "{87788e98-693b-4200-961c-ed5cbb47e324}",
          "name": "300v300在空.scen",
          "type": "file"
        },
        {
          "id": "{50e1685f-7e87-45c9-bca0-4c327945b2c6}",
          "name": "450v450在空.scen",
          "type": "file"
        },
        {
          "id": "{28e17e72-a2fe-457e-9d0a-76d8966d945f}",
          "name": "210v210.scen",
          "type": "file"
        },
        {
          "children": [
            {
              "id": "{8e3b53c9-353f-4c9b-83af-545a49516366}",
              "name": "455v458.xml",
              "type": "file"
            },
            {
              "id": "{df4abbd1-7532-4476-8b6c-60a124b9fe7b}",
              "name": "404v404.xml",
              "type": "file"
            },
            {
              "id": "{ad9fdbf6-a045-4c5e-90c0-b71a7bade85e}",
              "name": "354v354.xml",
              "type": "file"
            },
            {
              "id": "{d60a0d69-ba63-489b-ad05-23727a2129ef}",
              "name": "500v500.xml",
              "type": "file"
            }
          ],
          "id": "{9407fc4f-15d0-4e66-8789-4d21115053c6}",
          "name": "P920",
          "type": "directory"
        },
        {
          "id": "{0b02a82a-961c-4f4e-8079-28fd9cf37477}",
          "name": "400v400在空.scen",
          "type": "file"
        },
        {
          "id": "{7ae7ded2-a9e2-45a1-82be-013a442fa67f}",
          "name": "450v450.scen",
          "type": "file"
        },
        {
          "id": "{11d27dd1-5160-4ca4-9bbe-276253056d99}",
          "name": "在空150V150.scen",
          "type": "file"
        },
        {
          "id": "{512f321c-046c-4ffc-aeaa-aef4d293e099}",
          "name": "在空100V100.scen",
          "type": "file"
        },
        {
          "id": "{700189e9-d7ca-4281-97e4-0daca0d11687}",
          "name": "400v400初始.scen",
          "type": "file"
        },
        {
          "id": "{c0aeefd7-989a-43c3-991e-58b3a84fbd50}",
          "name": "在空200v200.scen",
          "type": "file"
        }
      ],
      "id": "{b1638a3b-0a85-4b73-89ac-e422a3f404c6}",
      "name": "测试想定",
      "type": "directory"
    },
    {
      "id": "{15cf9579-b565-476b-99e4-294d98286a71}",
      "name": "354v354.xml",
      "type": "file"
    },
    {
      "children": [
        {
          "id": "{70c21f85-a738-4317-a412-6371511358fd}",
          "name": "菲海战事-双方均有任务_修改lua脚本.scen",
          "type": "file"
        },
        {
          "id": "{61f01a57-18cd-4fb7-bc47-dafdaa7a9e1a}",
          "name": "菲海战事-仅蓝方有任务-v2.scen",
          "type": "file"
        },
        {
          "id": "{fc7fc8a1-7799-4841-84bf-22ca921b12b2}",
          "name": "菲海战事-双方均无任务-v2.scen",
          "type": "file"
        },
        {
          "id": "{4d10add4-0354-49ce-bdf6-2e64d8088e2a}",
          "name": "菲海战事-仅红方有任务-v2.scen",
          "type": "file"
        },
        {
          "id": "{7ab519be-1a04-4e18-9cf1-b79a81a0d70e}",
          "name": "海峡风暴-资格选拔赛.scen",
          "type": "file"
        },
        {
          "id": "{8fae4967-d4f2-4d0c-9e7a-f3de9f631dad}",
          "name": "菲海战事-双方均有任务-米格-29.scen",
          "type": "file"
        },
        {
          "id": "{e484db19-8b9c-4fc0-b59f-6a170aa9ebb7}",
          "name": "菲海战事-双方均有任务-v2.scen",
          "type": "file"
        }
      ],
      "id": "{c0ef7fff-8c10-4dea-9514-1a607cf6857f}",
      "name": "专项赛",
      "type": "directory"
    },
    {
      "id": "{f9c146fd-fd19-4613-a06b-87a18ae0740d}",
      "name": "电磁辐射.scen",
      "type": "file"
    },
    {
      "id": "{3517ff6f-e8c4-47aa-be19-df0a1d3ee67a}",
      "name": "效率测试想定.scen",
      "type": "file"
    },
    {
      "id": "{a37618d8-c0ef-4239-b717-62d54c8e62e7}",
      "name": "测试添加飞机默认加模拟器.scen",
      "type": "file"
    },
    {
      "id": "{59340428-cee6-4374-a4a5-f1a9041f1a3c}",
      "name": "标绘保存.scen",
      "type": "file"
    },
    {
      "children": [
        {
          "id": "{0ba45ad9-9bd5-455d-b010-0f98ee435046}",
          "name": "海峡风云-初赛想定.scen",
          "type": "file"
        },
        {
          "id": "{2a6d1c01-73c0-4c78-9cff-e3ab4bc0e62c}",
          "name": "-飞地风雷-晋级赛版.scen",
          "type": "file"
        },
        {
          "id": "{b225f196-9e9e-4dc0-ae5b-9922fb15b40a}",
          "name": "-飞地战云-复赛决赛版.scen",
          "type": "file"
        },
        {
          "id": "{bffe1fa4-1f66-4a14-9d31-9478726a614d}",
          "name": "海峡洪涛.scen",
          "type": "file"
        },
        {
          "id": "{15c96846-b05a-42f4-9109-a52bab6443a8}",
          "name": "飞地战云-初赛版-1.scen",
          "type": "file"
        },
        {
          "id": "{f5145e6c-c446-44d1-91f3-1682277b514c}",
          "name": "海峡风暴-红蓝无任务.scen",
          "type": "file"
        },
        {
          "id": "{83f02892-f1d3-4b95-90b4-926ce1ebed84}",
          "name": "拒止远征军-蓝海争锋（省赛推荐人机版）.scen",
          "type": "file"
        },
        {
          "id": "{fa451ee8-d517-471e-ad96-45b0f1054f56}",
          "name": "飞地战云-初赛版.scen",
          "type": "file"
        },
        {
          "id": "{1c0c14e1-77b5-4d05-91cd-b1ac68c97f10}",
          "name": "拒止远征军-蓝海争锋（省赛推荐人人版）.scen",
          "type": "file"
        },
        {
          "id": "{ea401072-5c88-4b42-918f-98912c078a11}",
          "name": "-海峡大潮.scen",
          "type": "file"
        },
        {
          "id": "{d3dc4bab-0b4e-4767-aa10-e60604a768f4}",
          "name": "拒止远征军-蓝海决胜（国赛人机版）.scen",
          "type": "file"
        },
        {
          "id": "{f94172ef-4f37-49f0-ae4d-ca46003e8320}",
          "name": "拒止远征军-太西海风云（省赛推荐人机版）.scen",
          "type": "file"
        },
        {
          "id": "{a01fb1ad-3c99-4522-a869-5a202622ff24}",
          "name": "怒海惊涛.scen",
          "type": "file"
        },
        {
          "id": "{54cf8952-8dea-4bba-a81a-a1cfcafd77b6}",
          "name": "拒止远征军2.xml",
          "type": "file"
        },
        {
          "id": "{712866f9-9d42-4835-bfcc-c910fe2a0dde}",
          "name": "海峡风云-初赛想定(人机想定).scen",
          "type": "file"
        },
        {
          "id": "{7d43da37-8a0b-43f3-b79e-12fc0a5acef7}",
          "name": "海峡风暴-资格选拔赛-蓝方任务随机方案.scen",
          "type": "file"
        },
        {
          "id": "{372773ae-027a-486c-bb0c-7c44f26ce8d0}",
          "name": "拒止远征军-太西海风云（省赛推荐人人版）.scen",
          "type": "file"
        },
        {
          "id": "{5af7aa17-52d1-49ec-b4cf-c71d8bdc9f0e}",
          "name": "拒止远征军.scen",
          "type": "file"
        },
        {
          "id": "{2424e89b-ea2c-4e69-9035-b7ac1b472f8c}",
          "name": "海峡风暴-红蓝无任务-想定无图片.scen",
          "type": "file"
        }
      ],
      "id": "{cf3eb499-d967-44ab-8e3b-b0c9b279f3eb}",
      "name": "大赛想定",
      "type": "directory"
    },
    {
      "children": [
        {
          "id": "{c0543fa7-3049-459a-9c09-84738ee93bd8}",
          "name": "20vs20.scen",
          "type": "file"
        },
        {
          "id": "{b068af3d-ad40-462a-9e68-89e2049a53bf}",
          "name": "台海演训-删减.xml",
          "type": "file"
        },
        {
          "id": "{dceb85a3-f942-4ed4-908c-11c67716eb2f}",
          "name": "20vs20.xml",
          "type": "file"
        },
        {
          "id": "{4bdc60d6-c1c9-4fb1-ad69-b5055f21dd26}",
          "name": "台海演训-删减.scen",
          "type": "file"
        }
      ],
      "id": "{622cec34-0e8c-45ca-9b6d-5707a00f0fb7}",
      "name": "HJ2022",
      "type": "directory"
    },
    {
      "children": [
        {
          "id": "{a79cb381-8100-4a83-9c9a-d6eb74ecdc74}",
          "name": "潜艇基础教程.scen",
          "type": "file"
        },
        {
          "id": "{d709745f-2654-4133-b008-d03cd803f927}",
          "name": "空战基础教程.scen",
          "type": "file"
        },
        {
          "id": "{51a76040-7af2-4f4f-baa9-7bdde16e963e}",
          "name": "水面舰艇基础教程.scen",
          "type": "file"
        }
      ],
      "id": "{89c9bef2-eb9f-4933-bbc5-23e470c9c2e3}",
      "name": "01 教程",
      "type": "directory"
    },
    {
      "id": "{5243bba4-ca4a-4ad3-aa44-a2de5de3e703}",
      "name": "7887878787.xml",
      "type": "file"
    },
    {
      "id": "{2223e61b-9199-4fcd-a917-114d131807d8}",
      "name": "展开撤收.xml",
      "type": "file"
    },
    {
      "id": "{8a2ea072-477c-47a4-8963-bdd4be59e7a6}",
      "name": "500v500.xml",
      "type": "file"
    },
    {
      "id": "{56a3034c-fcc4-40d0-b10e-f5d905d8bc8e}",
      "name": "HJ2024.scen",
      "type": "file"
    },
    {
      "id": "{bf2867e5-09f3-4002-b22e-fa3d9557733c}",
      "name": "200v200.scen",
      "type": "file"
    },
    {
      "id": "{89631144-9f5b-4f7f-a760-bbfd403d4036}",
      "name": "巡逻任务（未启用）.xml",
      "type": "file"
    },
    {
      "id": "{63e6ff9d-9e2d-4217-9db5-93ee13f74556}",
      "name": "HJ2025-任务99%.xml",
      "type": "file"
    },
    {
      "id": "{96d976c6-568f-43b3-961b-1460c2a4832d}",
      "name": "HJ2025-任务99%.scen",
      "type": "file"
    },
    {
      "id": "{1bd92b05-a670-4abb-9d17-d172095a7739}",
      "name": "4545646456.xml",
      "type": "file"
    },
    {
      "id": "{866728d7-570e-410a-8727-7ba7519935d6}",
      "name": "自动被探测到.scen",
      "type": "file"
    },
    {
      "id": "{6848ffd3-3e86-4371-a120-19c27829375b}",
      "name": "雷达告警.scen",
      "type": "file"
    },
    {
      "id": "{a85f5143-8203-4f2a-a910-e291b5816d88}",
      "name": "240v240SensorON.xml",
      "type": "file"
    },
    {
      "id": "{179da0ac-83ff-49fe-95c4-5722d48512d1}",
      "name": "1.xml",
      "type": "file"
    },
    {
      "id": "{09b3e23c-7b68-4dc2-9fc8-727ce847e36c}",
      "name": "240v240_10s.xml",
      "type": "file"
    },
    {
      "id": "{7ba1a29d-bd9f-458a-9081-155898c720d8}",
      "name": "测试由不明变已知图标颜色.scen",
      "type": "file"
    },
    {
      "id": "{ce61902b-a1c8-4f58-8d81-7b200c24c77b}",
      "name": "测试另存.scen",
      "type": "file"
    },
    {
      "id": "{e8dcf61b-0b1b-412e-8efa-d5b1ae9d44bb}",
      "name": "234.xml",
      "type": "file"
    },
    {
      "id": "{de66eec8-b970-477f-a764-5a588dda1e78}",
      "name": "123.xml",
      "type": "file"
    },
    {
      "id": "{d3cc33d7-8e8c-4f0c-b5e6-b43ea006c5a6}",
      "name": "天波雷达.xml",
      "type": "file"
    },
    {
      "id": "{d06efc2d-36d6-4b57-b0bc-6a4f5d91e612}",
      "name": "行为树test1.xml",
      "type": "file"
    },
    {
      "id": "{9071f827-88f4-48d2-8239-3afbac3bef97}",
      "name": "1203-2测试.scen",
      "type": "file"
    },
    {
      "id": "{27d07dbc-4a55-4cca-adc5-8cc585143649}",
      "name": "雷达告警另存测试.scen",
      "type": "file"
    },
    {
      "id": "{5da9b8c9-398b-4a48-9c80-741ff571a7d8}",
      "name": "测试xml文件.xml",
      "type": "file"
    },
    {
      "id": "{dea846c6-d1d1-4a7b-9cc2-3fbb1d9cd402}",
      "name": "反辐射.xml",
      "type": "file"
    },
    {
      "id": "{2ebae2dd-9233-498c-b7f8-427da2aeb5de}",
      "name": "飞机打91.xml",
      "type": "file"
    },
    {
      "id": "{11bc5904-5f24-499f-9f27-6945b50296cc}",
      "name": "发射测试.xml",
      "type": "file"
    },
    {
      "id": "{d3b5a411-8b9e-4e6e-a4ec-093b5309303f}",
      "name": "测试任务分配.xml",
      "type": "file"
    },
    {
      "id": "{278cc49f-2688-43d0-9880-bb36a3a88026}",
      "name": "HJ2025-任务80%.scen",
      "type": "file"
    },
    {
      "children": [
        {
          "id": "{af242539-72a6-40c8-b652-e2564d73b6db}",
          "name": "2025-8-15-1500初始态势_2025-08-15_17_45_13.xml",
          "type": "file"
        }
      ],
      "id": "{da46330c-608e-4d9a-b4b8-52b0b84beaaf}",
      "name": "标绘想定",
      "type": "directory"
    },
    {
      "id": "{8d118786-3893-428f-b4a5-a15beb054278}",
      "name": "455v458.xml",
      "type": "file"
    },
    {
      "id": "{4bfd7e0f-b5e3-4d4d-ad97-1523ede58dc5}",
      "name": "台海演训-删减.scen",
      "type": "file"
    },
    {
      "id": "{e22886d0-861d-4af5-824d-8b85c0309677}",
      "name": "测试分配任务给实体.xml",
      "type": "file"
    },
    {
      "id": "{21afd312-f41a-4321-9439-5b22921e5ebd}",
      "name": "123456.xml",
      "type": "file"
    },
    {
      "id": "{97c4b07b-c203-4bef-ba8d-9350bf391464}",
      "name": "354V354SensorON.xml",
      "type": "file"
    },
    {
      "id": "{5a63a26f-0204-4c58-ab13-2eb23d2f4321}",
      "name": "354V354SensorON.scen",
      "type": "file"
    },
    {
      "id": "{9fea1d54-cf29-4439-87c9-fedf41e7bcb7}",
      "name": "47.xml",
      "type": "file"
    },
    {
      "id": "{dfb2b0e2-36d9-4a52-8e9b-71c28df06e9d}",
      "name": "自动探测到的探测记录.scen",
      "type": "file"
    },
    {
      "id": "{03aa2bcc-fabd-4b65-b674-6722369fda7d}",
      "name": "12345.scen",
      "type": "file"
    },
    {
      "id": "{531916c0-580a-4ed5-b7a0-8ac68e2dee6d}",
      "name": "202408152053第三日最终.scen",
      "type": "file"
    }
  ],
  "message": "succeed",
  "timestamp": "2026-10-02 14:34:49"
}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370913470e0)

- frontend：`source_materials/frontend_calls.json`


### 获取想定时间

**操作标识：** `GET /api/GetScenarioTime`

**分类：** 想定相关

**资料依据：** 本机 JSON 实测；Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetScenarioTime`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.CurrentTime | string | 是 |  |
| response | data.DurationTime | string | 是 |  |
| response | data.StartTime | string | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "CurrentTime": "2025-09-30 15:18:41",
        "DurationTime": "1-0-0",
        "StartTime": "2025-09-30 15:18:41"
    },
    "message": "succeed",
    "timestamp": "2025-11-14 11:38:01"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Nyt`；调用位置数量 3。

```javascript
function Nyt(e){return nt({url:"/ApiCtrl/api/GetScenarioTime",method:"get",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 本机只读验证

- `http://127.0.0.1:8082/ApiCtrl/api/GetScenarioTime`：HTTP 200；2026-10-02 14:34:49 +0800；application/json; charset=utf-8

```json
{
  "code": 0,
  "data": {
    "CurrentTime": "2021-05-26 06:15:43",
    "DurationTime": "0-3-20",
    "StartTime": "2021-05-26 02:55:43"
  },
  "message": "succeed",
  "timestamp": "2026-10-02 14:34:49"
}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376492528e0)

- frontend：`source_materials/frontend_calls.json`


### 获取天气信息

**操作标识：** `GET /api/GetWeather`

**分类：** 想定相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetWeather`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | SideGuid | string | 否 |  |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `$yt`；调用位置数量 1。

```javascript
function $yt(e){return nt({url:"/ApiCtrl/api/GetWeather",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377301257e0)

- frontend：`source_materials/frontend_calls.json`


### 加载想定接口

**操作标识：** `GET /api/LoadScenario`

**分类：** 想定相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/LoadScenario`

**状态影响：** 会修改状态或执行控制；GET 也不可自动重试

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | scenarioName | string | 否 | ；想定列表中的name字段；文档examples：47.xml |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.endTime | string | 是 |  |
| response | data.scenarioName | string | 是 |  |
| response | data.sides | array [object] | 是 |  |
| response | data.startTime | string | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "endTime": "string",
        "scenarioName": "string",
        "sides": [
            {
                "color": "string",
                "commandpostModalList": [
                    "string"
                ],
                "friendlyColor": "string",
                "hostileColor": "string",
                "id": "string",
                "name": "string",
                "neutralColor": "string",
                "unFriendlyColor": "string"
            }
        ],
        "startTime": "string"
    },
    "message": "string",
    "timestamp": "string"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `myt`；调用位置数量 1。

```javascript
function myt(e){return nt({url:"/ApiCtrl/api/LoadScenario",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/430598374e0)

- frontend：`source_materials/frontend_calls.json`


### 获取想定基本信息

**操作标识：** `GET /api/Scen`

**分类：** 想定相关

**资料依据：** 本机 JSON 实测；Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/Scen`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 本机只读验证

- `http://127.0.0.1:8082/ApiCtrl/api/Scen`：HTTP 200；2026-10-02 14:34:49 +0800；application/json; charset=utf-8

```json
{
  "code": 0,
  "data": {
    "currentTime": "2021-05-26 06:15:43",
    "description": "<BODY scroll=auto></BODY>",
    "endTime": "2021-05-26 06:15:43",
    "scenarioFileName": "123",
    "scenarioGuid": "5f8bfea7-2d2b-44fb-aff1-e02e9ff73dc4",
    "startTime": "2021-05-26 02:55:43",
    "作战开始时间": "2021-05-26 02:55:43",
    "作战结束时间": "2021-05-26 06:15:43",
    "当前作战时间": "2021-05-26 06:15:43",
    "想定ID": "5f8bfea7-2d2b-44fb-aff1-e02e9ff73dc4",
    "想定名称": "123",
    "想定描述": "<BODY scroll=auto></BODY>"
  },
  "message": "succeed",
  "timestamp": "2026-10-02 14:34:49"
}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

- 用 scenarioGuid 辅助隔离想定；同名想定不能仅靠名称保证身份一致。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/432911259e0)


### 想定操作

**操作标识：** `POST /api/ScenarioOperation`

**分类：** 想定相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ScenarioOperation`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | type | enum<string> | 是 | 类型；枚举：CreateNewScenario, SaveAsScenario, SaveScenario |
| body | FileName | string | 是 | 文件名称 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "type": "SaveAsScenario",
    "FileName": "测试另存12.xml"
}
```

### 另存想定

```json
{
    "type": "SaveAsScenario",
    "FileName": "测试另存123"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `gyt`；调用位置数量 3。

```javascript
function gyt(e){return nt({url:"/ApiCtrl/api/ScenarioOperation",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/367979321e0)

- frontend：`source_materials/frontend_calls.json`


### 设置想定描述

**操作标识：** `POST /api/SetScenarioDescription`

**分类：** 想定相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/SetScenarioDescription`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | Title | string | 是 | 标题 |
| body | Description | string | 是 | 描述 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Title": "搜一起绿123",
    "Description": "月眼少。知命23123123123转作加。验变族。见儿决海很表何的书自。温内进支或五确打。见度且。"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Fyt`；调用位置数量 1。

```javascript
function Fyt(e){return nt({url:"/ApiCtrl/api/SetScenarioDescription",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376742420e0)

- frontend：`source_materials/frontend_calls.json`


### 设置想定时间

**操作标识：** `POST /api/SetScenarioTime`

**分类：** 想定相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/SetScenarioTime`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | StartTime | string | 是 | 开始时间；2025-9-30 15:18:41 |
| body | CurrentTime | string | 是 | 当前时间；2025-9-30 15:18:41 |
| body | DurationTime | string | 是 | 持续时间；1-1-1 天 时 分 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "StartTime": "2025-12-20 17:01:47",
    "CurrentTime": "2025-12-20 17:01:47",
    "DurationTime": "2-4-5"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Byt`；调用位置数量 1。

```javascript
function Byt(e){return nt({url:"/ApiCtrl/api/SetScenarioTime",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376607743e0)

- frontend：`source_materials/frontend_calls.json`


### 设置天气信息

**操作标识：** `POST /api/SetWeather`

**分类：** 想定相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/SetWeather`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | Temperature | integer | 是 | 平均气温；-49 - 50 |
| body | RainFallRate | number | 是 | 降雨量；0 - 50  0.00 1.00 2.00 |
| body | SkyCloud | number | 是 | 天空云量；0 - 1   0.1 0.2 0.3 |
| body | SeaState | integer | 是 | 海况/风力；0 - 9   0  1  2 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Temperature": 30,
    "RainFallRate": 10,
    "SkyCloud": 0.5,
    "SeaState": 10
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `zyt`；调用位置数量 1。

```javascript
function zyt(e){return nt({url:"/ApiCtrl/api/SetWeather",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377320506e0)

- frontend：`source_materials/frontend_calls.json`


### 编辑推演方接口

**操作标识：** `POST /api/sideOperation`

**分类：** 想定相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/sideOperation`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | option | string | 是 |  |
| body | sideGuid | string | 是 |  |
| body | sideName | string | 是 |  |
| body | sideColor | object | 是 |  |
| body | sideColor.color | string | 是 |  |
| body | sideColor.type | integer | 是 |  |
| body | sideRelation | object | 是 |  |
| body | sideRelation.sideGUid | string | 是 |  |
| body | sideRelation.relation | integer | 是 |  |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "option": "color",
    "sideGuid": "43dc235f-0b3f-4914-a79a-d5c3a37ea8af",
    "sideColor": [
        {
        "color": "绿色",
        "type": 5
    },
     {
        "color": "蓝色",
        "type": 1
    }
    ]
}
```

### 删除推演examples

```json
{
    "option": "del",
    "sideGuid": "02216f2a-244e-4a7f-84d8-f7830a5066df"
}
```

### 重命名

```json
{
    "option": "rename",
    "sideGuid": "6f2da012-0c8b-49f2-9d41-dc00eb48d27e",
    "sideName": "卢宇航"
}
```

### 设置颜色

```json
{
    "option": "color",
    "sideGuid": "6f2da012-0c8b-49f2-9d41-dc00eb48d27e",
    "sideColor": [
        {
        "color": "白色",
        "type": 1
    },
     {
        "color": "蓝色",
        "type": 2
    }
    ]
}
```

### 关系

```json
{
    "option": "relation",
    "sideGuid": "6f2da012-0c8b-49f2-9d41-dc00eb48d27e",
    "sideRelation": {
        "sideGUid": "6f2da012-0c8b-49f2-9d41-dc00eb48d27e",
        "relation": 1
    }
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Oyt`；调用位置数量 1。

```javascript
function Oyt(e){return nt({url:"/ApiCtrl/api/sideOperation",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/372636382e0)

- frontend：`source_materials/frontend_calls.json`


### 获取推演方界面数据接口

**操作标识：** `GET /api/sideOperation/getSideData`

**分类：** 想定相关

**资料依据：** 本机 JSON 实测；Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/sideOperation/getSideData`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 用途补充

返回服务端支持的颜色 ，返回 推演方关系
返回现有推演方，和 每个推演方的颜色设置 推演方关系设置

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Ryt`；调用位置数量 1。

```javascript
function Ryt(e){return nt({url:"/ApiCtrl/api/sideOperation/getSideData",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 本机只读验证

- `http://127.0.0.1:8082/ApiCtrl/api/sideOperation/getSideData`：HTTP 200；2026-10-02 14:34:49 +0800；application/json; charset=utf-8

```json
{
  "code": 0,
  "data": {
    "colors": [
      {
        "colorName": "橙色",
        "colorValue": "#ff7f27"
      },
      {
        "colorName": "白色",
        "colorValue": "#ffffff"
      },
      {
        "colorName": "紫色",
        "colorValue": "#ff00ff"
      },
      {
        "colorName": "红色",
        "colorValue": "#ff0000"
      },
      {
        "colorName": "绿色",
        "colorValue": "#00ff00"
      },
      {
        "colorName": "蓝色",
        "colorValue": "#0000ff"
      },
      {
        "colorName": "黄色",
        "colorValue": "#d2ab11"
      },
      {
        "colorName": "黑色",
        "colorValue": "#000000"
      }
    ],
    "postureStances": [
      {
        "id": "0",
        "name": "中立"
      },
      {
        "id": "1",
        "name": "友方"
      },
      {
        "id": "2",
        "name": "非友方"
      },
      {
        "id": "3",
        "name": "敌对方"
      }
    ],
    "sides": [
      {
        "color": {
          "friendly": "白色",
          "hostile": "红色",
          "neutral": "绿色",
          "self": "蓝色",
          "unfriendly": "橙色"
        },
        "guid": "f475d720-c142-4789-9737-71ad9ab56b5e",
        "name": "蓝方",
        "postureStance": [
          {
            "postureid": 3,
            "sideguid": "fc61476f-796e-429d-a93d-1446bfaba582",
            "sidename": "红方"
          }
        ]
      },
      {
        "color": {
          "friendly": "橙色",
          "hostile": "蓝色",
          "neutral": "绿色",
          "self": "红色",
          "unfriendly": "白色"
        },
        "guid": "fc61476f-796e-429d-a93d-1446bfaba582",
        "name": "红方",
        "postureStance": [
          {
            "postureid": 3,
            "sideguid": "f475d720-c142-4789-9737-71ad9ab56b5e",
            "sidename": "蓝方"
          }
        ]
      }
    ]
  },
  "message": "succeed",
  "timestamp": "2026-10-02 14:34:49"
}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/373037184e0)

- frontend：`source_materials/frontend_calls.json`


## 执行lua脚本

### 执行Lua脚本接口

**操作标识：** `POST /AgentApiCtrl/api/ExecuteLuaScript`

**分类：** 执行lua脚本

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/AgentApiCtrl/api/ExecuteLuaScript`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{

"LuaScripts":"local a=ScenEdit_GetUnit({name='“美国”级两栖攻击舰'})\n\rprint(a)"

}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- Agent 查询控制器与普通 /ApiCtrl 控制器不同，不能互相替换路径。

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/398775444e0)


## 指挥关系相关

### 指定实体为指挥所

**操作标识：** `POST /api/appointCommand`

**分类：** 指挥关系相关

**资料依据：** Apifox 文档

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/appointCommand`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "option":"Designated",  //指定实体为指挥所
    "unit_id":""
}

    // "commander_id":""
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/399761139e0)


### 获取指挥所信息

**操作标识：** `GET /api/getCommandPosts`

**分类：** 指挥关系相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/getCommandPosts`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | sideName | string | 否 | ；文档examples：红方 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `T1t`；调用位置数量 2。

```javascript
function T1t(e){return nt({url:"/ApiCtrl/api/getCommandPosts",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/432649881e0)

- frontend：`source_materials/frontend_calls.json`


### 获取指挥员

**操作标识：** `GET /api/getCommanders`

**分类：** 指挥关系相关

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/getCommanders`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | sideName | string | 否 | ；文档examples：红方 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{"code":0,"data":[{"age":47,"armType":"Mechanized Infantry","communication_style":"","core_ability":"","decision_rules":"","emergency_Handling":"","id":"A12345","militaryBranch":"United States Marine Corps","name":"Captain Jameson","output_format":"","personality":"Analytical, methodical, highly disciplined with strong leadership instincts","position":"","rank":"Captain (O-5)","role":"Operational level commander","unit":"1st Battalion, 7th Marines","workFlow":"","workFlowList":[]},{"age":47,"armType":"Mechanized Infantry","communication_style":"","core_ability":"","decision_rules":"","emergency_Handling":"","id":"A5","militaryBranch":"United States Marine Corps","name":"Captain Jameson","output_format":"","personality":"Analytical, methodical, highly disciplined with strong leadership instincts","position":"","rank":"Captain (O-5)","role":"Operational level commander","unit":"1st Battalion, 7th Marines","workFlow":"","workFlowList":[]}],"message":"succeed","timestamp":"2026-03-24 15:29:18"}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/432637800e0)


## 支撑认证接口

### 前端认证登录

**操作标识：** `POST /api/auth/login`

**分类：** 支撑认证接口

**资料依据：** 前端src证据

**资料中的地址：** `http://127.0.0.1:8082/api/auth/login`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 只有前端代码或本机调用证据

## 用途补充

前端 fetch 请求提交 username/password，HTTP 成功后读取响应 token；本次未登录测试。

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | username | string | 未说明 | 来自调用者config，不内置账户或密码 |
| body | password | string | 未说明 | 来自调用者config，不内置账户或密码 |


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `login`；调用位置数量 0。

```javascript
fetch("/api/auth/login", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({username, password})})
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 限制、差异及待确认事项

- 根级 /api/auth/login 不加 /ApiCtrl 前缀；该认证并非墨子单位控制接口。认证策略和部署可用性未实测。

## 来源

- frontend：`source_materials/frontend_calls.json`


## 攻击作战行动

### 针对所有目标类型的武器控制状态-针对所有单元

**操作标识：** `POST /api/allTargetTypeAll`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/allTargetTypeAll`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

控制所有单元对所有目标类型的攻击状态

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | sideGuid | string | 是 | 推演方ID；文档examples：f9fb65ad-b876-404b-acb5-f7a1c4a0b13d |
| body | type | enum<string> | 是 | 类型；枚举：Hold, Tight, Free, Inherited |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "sideGuid": "f9fb65ad-b876-404b-acb5-f7a1c4a0b13d",
    "unitGuid": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "type": "Hold"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | message | string | 是 | 提示信息 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "message": "succeed",
    "timestamp": "2025-10-29 10:40:40"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `zje`；调用位置数量 1。

```javascript
function zje(e){return nt({url:"/ApiCtrl/api/allTargetTypeAll",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368209458e0)

- frontend：`source_materials/frontend_calls.json`


### 针对所有目标类型的武器控制状态-针对所选单元

**操作标识：** `POST /api/allTargetTypeSelected`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/allTargetTypeSelected`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

控制指定单元对所有目标类型的攻击状态

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | sideGuid | string | 是 | 推演方ID；文档examples：f9fb65ad-b876-404b-acb5-f7a1c4a0b13d |
| body | unitGuid | string | 是 | 单元ID；文档examples：ef65f066-0fd3-4688-9710-5bbc89065a68 |
| body | type | enum<string> | 是 | 类型；枚举：Hold, Tight, Free, Inherited |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "sideGuid": "f9fb65ad-b876-404b-acb5-f7a1c4a0b13d",
    "unitGuid": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "type": "Hold"
}
```

### examples 2

```json
{
    "sideGuid": "f9fb65ad-b876-404b-acb5-f7a1c4a0b13d",
    "unitGuid": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "type": "Inherited"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | message | string | 是 | 提示信息 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "message": "succeed",
    "timestamp": "2025-10-29 10:40:13"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `$je`；调用位置数量 1。

```javascript
function $je(e){return nt({url:"/ApiCtrl/api/allTargetTypeSelected",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368201800e0)

- frontend：`source_materials/frontend_calls.json`


### 攻击时忽略计划航线-针对所有单元

**操作标识：** `POST /api/attackIgnorePlanLineAllUnit`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/attackIgnorePlanLineAllUnit`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | sideGuid | string | 是 | 推演方ID；文档examples：f9fb65ad-b876-404b-acb5-f7a1c4a0b13d |
| body | type | enum<string> | 是 | 操作类型；枚举：Yes, No, Inherited |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "sideGuid": "f9fb65ad-b876-404b-acb5-f7a1c4a0b13d",
    "type": "Yes"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | message | string | 是 | 提示信息 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "message": "succeed",
    "timestamp": "2025-10-29 10:42:03"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Fje`；调用位置数量 1。

```javascript
function Fje(e){return nt({url:"/ApiCtrl/api/attackIgnorePlanLineAllUnit",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368178503e0)

- frontend：`source_materials/frontend_calls.json`


### 攻击时忽略计划航线-针对所选单元

**操作标识：** `POST /api/attackIgnorePlanLineSelectedUnit`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/attackIgnorePlanLineSelectedUnit`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | sideGuid | string | 是 | 推演方ID；文档examples：f9fb65ad-b876-404b-acb5-f7a1c4a0b13d |
| body | unitGuid | string | 是 | 单元ID；文档examples：ef65f066-0fd3-4688-9710-5bbc89065a68 |
| body | type | enum<string> | 是 | 操作类型；枚举：Yes, No, Inherited |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "sideGuid": "f9fb65ad-b876-404b-acb5-f7a1c4a0b13d",
    "unitGuid": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "type": "Yes"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | message | string | 是 | 提示信息 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "message": "",
    "timestamp": "2025-10-29 10:13:14"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Vje`；调用位置数量 1。

```javascript
function Vje(e){return nt({url:"/ApiCtrl/api/attackIgnorePlanLineSelectedUnit",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368175947e0)

- frontend：`source_materials/frontend_calls.json`


### 自动接战目标

**操作标识：** `POST /api/autoFightToContact`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/autoFightToContact`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | unitGuid | string | 是 | 打击单元ID；文档examples：ef65f066-0fd3-4688-9710-5bbc89065a68 |
| body | targetGuid | string | 是 | 目标单元ID；文档examples：8b1bbe05-bab2-4afa-b088-3fd41703b544 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unitGuid": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "targetGuid": "8b1bbe05-bab2-4afa-b088-3fd41703b544"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | message | string | 是 | 提示信息 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "message": "succeed",
    "timestamp": "2025-10-28 22:00:41"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Oje`；调用位置数量 1。

```javascript
function Oje(e){return nt({url:"/ApiCtrl/api/autoFightToContact",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368078551e0)

- frontend：`source_materials/frontend_calls.json`


### 放弃指定目标

**操作标识：** `POST /api/giveUpFightAim`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/giveUpFightAim`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

放弃对指定目标进行攻击

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | sideGuid | string | 是 | 推演方ID；文档examples：f9fb65ad-b876-404b-acb5-f7a1c4a0b13d |
| body | unitGuid | string | 是 | 打击单元ID；文档examples：ef65f066-0fd3-4688-9710-5bbc89065a68 |
| body | targetGuid | string | 是 | 目标单元ID；文档examples：8b1bbe05-bab2-4afa-b088-3fd41703b544 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "sideGuid": "f9fb65ad-b876-404b-acb5-f7a1c4a0b13d",
    "unitGuid": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "targetGuid": "8b1bbe05-bab2-4afa-b088-3fd41703b544"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | message | string | 是 | 提示信息 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "message": "succeed",
    "timestamp": "2025-10-28 22:13:44"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Nje`；调用位置数量 1。

```javascript
function Nje(e){return nt({url:"/ApiCtrl/api/giveUpFightAim",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368083350e0)

- frontend：`source_materials/frontend_calls.json`


### 脱离接战（放弃所有目标）

**操作标识：** `POST /api/offFight`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/offFight`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | unitGuid | string | 是 | 打击单元ID；文档examples：ef65f066-0fd3-4688-9710-5bbc89065a68 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unitGuid": "ef65f066-0fd3-4688-9710-5bbc89065a68"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "message": "",
    "timestamp": "2025-10-29 10:15:42"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Bje`；调用位置数量 1。

```javascript
function Bje(e){return nt({url:"/ApiCtrl/api/offFight",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/368135752e0)

- frontend：`source_materials/frontend_calls.json`


### 武器分配界面（手动接战目标、纯方位攻击）

**操作标识：** `GET /api/weapon-assignment`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/weapon-assignment`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

targetGuid传参即为手动接战目标，targetLon、targetLat传参即为纯方位攻击

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | unitGuid | string | 是 | ；文档examples：ef65f066-0fd3-4688-9710-5bbc89065a68 |
| query | targetGuid | string \| null | 否 | ；手动接战目标时使用该参数；文档examples：8B1BBE05-BAB2-4AFA-B088-3FD41703B544 |
| query | targetLon | number | 否 | ；纯方位攻击时使用该参数；文档examples：122.56725 |
| query | targetLat | number | 否 | ；纯方位攻击时使用该参数；文档examples：21.8562 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | data.strikeAllTargetWeapon | object | 否 | 所选打击平台针对所有目标分配的武器 |
| response | data.strikeChooseTargetWeapon | object | 否 | 所选打击平台针对所选目标分配的武器 |
| response | data.targetChooseStrikeWeapon | object | 否 | 所选打击平台针对所选目标分配的武器 |
| response | data.targetAllStrikeWeapon | object | 否 | 所有打击平台针对所选目标分配的武器 |
| response | data.strikePlatform | object | 是 | 打击平台 |
| response | data.targetList | object | 是 | 目标清单 |
| response | data.weaponList | array [object] | 否 | 可用武器清单 |
| response | message | string | 是 | 提示信息 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "strikeAllTargetWeapon": {
            "children": [
                {
                    "id": "a356fcc5-84d9-482b-8886-66f81c6a3cc3",
                    "name": "分配到 F-16C/D型“战隼”战斗机 #2: 1x 霹雳-12C型空对空导弹"
                },
                {
                    "id": "b4f15211-815c-45a6-8e0b-0f16173f9de5",
                    "name": "分配到 F-16C/D型“战隼”战斗机 #2: 1x 霹雳-10型空对空导弹"
                },
                {
                    "id": "323495ca-47ea-478b-bd61-cb1bc9ff3325",
                    "name": "分配到 F-16C/D型“战隼”战斗机 #2: 3x 霹雳-12C型空对空导弹"
                },
                {
                    "id": "b7f71512-39be-4ae3-876a-1bbc6508e79b",
                    "name": "分配到 F-16C/D型“战隼”战斗机 #5: 2x 霹雳-12C型空对空导弹"
                }
            ],
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "打击平台: 歼-20型战斗机"
        },
        "strikeChooseTargetWeapon": {
            "children": [
                {
                    "id": "866ef2f7-b6be-49b5-abc3-b7b90b125522",
                    "name": "分配:  2x 霹雳-12C型空对空导弹"
                }
            ],
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "打击平台: 歼-20型战斗机"
        },
        "strikePlatform": {
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "歼-20型战斗机"
        },
        "targetChooseStrikeWeapon": {
            "children": [
                {
                    "id": "0d7b96ff-387b-4071-9f4c-164608aef186",
                    "name": "分配: 2x 霹雳-12C型空对空导弹",
                    "route": "false"
                }
            ],
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "打击平台: 歼-20型战斗机"
        },
        "targetList": {
            "id": "8b1bbe05-bab2-4afa-b088-3fd41703b544",
            "name": "F-16C/D型“战隼”战斗机 #5"
        },
        "weaponList": [
            {
                "children": [
                    {
                        "id": "ca0dc0f7-b38e-46c2-a107-8da13b0b67c2",
                        "name": "禁止自动开火, 目标超出武器射程",
                        "status": 0
                    },
                    {
                        "id": "94359872-3fea-4840-afbc-8f6604025604",
                        "name": "武器控制状态: 武器谨慎开火",
                        "status": 1
                    },
                    {
                        "id": "ef284151-96f7-4741-b0da-727647b825a2",
                        "name": "武器使用规则: 每次齐射所有武器开火. 最大射程发射武器. 目标类型:飞机 - 第4代战斗机/攻击机 [过载/g: 4.0-4.9] (F-14, F-15, F-16, MiG-29, Su-27)",
                        "status": 1
                    },
                    {
                        "id": "ce7b5f49-1f73-4d41-9699-226864c394ae",
                        "name": "5x 不能开火. 目标超出武器射程",
                        "status": 0
                    }
                ],
                "id": "hsfw-dataweapon-00000000001796",
                "name": "5x 30毫米 Gsh-30-1型航空机炮"
            },
            {
                "children": [
                    {
                        "id": "d15a297d-3f25-45a0-bee5-2fffae5ec945",
                        "name": "允许自动开火.",
                        "status": 0
                    },
                    {
                        "id": "69a4308c-071a-43e5-b3a3-ee8a14383c01",
                        "name": "武器控制状态: 武器谨慎开火",
                        "status": 1
                    },
                    {
                        "id": "a70f009a-9ba2-4791-8eb2-9163b11b8f42",
                        "name": "武器使用规则: 2x发齐射. 最大射程发射武器. 目标类型:飞机 - 第4代战斗机/攻击机 [过载/g: 4.0-4.9] (F-14, F-15, F-16, MiG-29, Su-27)",
                        "status": 1
                    },
                    {
                        "id": "2dbd9893-06c3-457d-a011-a45f841f2ea7",
                        "name": "1x 可以开火(人工分配武器)",
                        "status": 2
                    }
                ],
                "id": "hsfw-dataweapon-00000000002109",
                "name": "2x 霹雳-10型空对空导弹 (1x 已分配)"
            },
            {
                "children": [
                    {
                        "id": "b1658fdf-7d67-4f63-bc87-3b16188425a8",
                        "name": "允许自动开火.",
                        "status": 0
                    },
                    {
                        "id": "b2e80eeb-d4b9-4c6c-988a-29a0bda8aaa7",
                        "name": "武器控制状态: 武器谨慎开火",
                        "status": 1
                    },
                    {
                        "id": "40e437a9-8e9a-4eb0-b375-f5d32525e86b",
                        "name": "武器使用规则: 2x发齐射. 最大射程发射武器. 目标类型:飞机 - 第4代战斗机/攻击机 [过载/g: 4.0-4.9] (F-14, F-15, F-16, MiG-29, Su-27)",
                        "status": 1
                    },
                    {
                        "id": "e739087a-4583-43ba-a996-d1839ddb1351",
                        "name": "4x 可以开火(人工分配武器)",
                        "status": 2
                    }
                ],
                "id": "hsfw-dataweapon-00000000002108",
                "name": "10x 霹雳-12C型空对空导弹 (6x 已分配)"
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-10-27 19:24:23"
}
```

### 成功examples-纯方位打击

```json
{
    "code": 0,
    "data": {
        "strikeAllTargetWeapon": {
            "children": [
                {
                    "id": "851170b3-75ee-46dc-8ecf-1d50449ba13e",
                    "name": "分配到 F-16C/D型“战隼”战斗机 #2: 1x 霹雳-12C型空对空导弹"
                },
                {
                    "id": "cfa41963-3ebe-4732-ac98-a811e4321c1b",
                    "name": "分配到 F-16C/D型“战隼”战斗机 #2: 1x 霹雳-10型空对空导弹"
                },
                {
                    "id": "946ffee1-b527-4cf5-bfab-88981c62ee3c",
                    "name": "分配到 F-16C/D型“战隼”战斗机 #2: 3x 霹雳-12C型空对空导弹"
                },
                {
                    "id": "77a40574-46a5-4155-8a4d-12b2fa933c89",
                    "name": "分配到 F-16C/D型“战隼”战斗机 #5: 2x 霹雳-12C型空对空导弹"
                },
                {
                    "id": "4a10c5cf-2b10-4e49-86e6-cd62e84032d2",
                    "name": "分配到 BOL Activation Point: 北纬21°00'00\", 东经122°00'00\": 1x 霹雳-10型空对空导弹"
                }
            ],
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "打击平台: 歼-20型战斗机"
        },
        "strikeChooseTargetWeapon": {
            "children": [
                {
                    "id": "9df03553-98c5-435f-8eb0-33956328a5a1",
                    "name": "分配:  1x 霹雳-10型空对空导弹"
                }
            ],
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "打击平台: 歼-20型战斗机"
        },
        "strikePlatform": {
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "歼-20型战斗机"
        },
        "targetList": {
            "id": "BOL Activation Point:北纬21°51′22″，东经122°34′2″",
            "name": "BOL Activation Point:北纬21°51′22″，东经122°34′2″"
        },
        "weaponList": [
            {
                "children": [
                    {
                        "id": "28caac9d-e8e7-42ac-adde-14f11d05f760",
                        "name": "禁止自动开火, 作战条令规定'不准对地面或水面目标进行火炮攻击'",
                        "status": 0
                    },
                    {
                        "id": "8354fe4c-7cea-4aa1-8056-bfad2937d123",
                        "name": "武器控制状态: 武器谨慎开火",
                        "status": 1
                    },
                    {
                        "id": "34343bf9-696a-421f-987a-84a85d59e4ec",
                        "name": "武器使用规则: 不要对该目标类型使用武器. 目标类型:",
                        "status": 1
                    },
                    {
                        "id": "6577ca45-d7d8-4888-b145-56d361506b66",
                        "name": "5x 不能开火. 目标超出武器射程",
                        "status": 0
                    }
                ],
                "id": "hsfw-dataweapon-00000000001796",
                "name": "5x 30毫米 Gsh-30-1型航空机炮"
            },
            {
                "id": "hsfw-dataweapon-00000000002109",
                "name": "2x 霹雳-10型空对空导弹 (2x 已分配)"
            },
            {
                "children": [
                    {
                        "id": "7c46e16b-d0af-4adc-8b42-ac264ecc2b02",
                        "name": "禁止自动开火,武器控制状态为谨慎开火而目标经查证非敌方",
                        "status": 0
                    },
                    {
                        "id": "cdde6bd5-5d47-4406-9ed5-3c6a6090fc1c",
                        "name": "武器控制状态: 武器谨慎开火",
                        "status": 1
                    },
                    {
                        "id": "c3c25299-eaac-4989-af88-aad3e06fdadd",
                        "name": "武器使用规则: 不要对该目标类型使用武器. 目标类型:",
                        "status": 1
                    },
                    {
                        "id": "35884596-0d29-4b9f-bdbb-3590b6a90027",
                        "name": "4x 不能开火. 目标超出武器射程",
                        "status": 0
                    }
                ],
                "id": "hsfw-dataweapon-00000000002108",
                "name": "10x 霹雳-12C型空对空导弹 (6x 已分配)"
            },
            {
                "children": [
                    {
                        "id": "9cb35263-09d0-4d81-a4d3-449e2ea66a0d",
                        "name": "禁止自动开火,武器控制状态为谨慎开火而目标经查证非敌方",
                        "status": 0
                    },
                    {
                        "id": "4cb6fa8a-1240-46fd-aa9b-1a54ac0424ba",
                        "name": "武器控制状态: 武器谨慎开火",
                        "status": 1
                    },
                    {
                        "id": "b427a050-da04-4168-a747-5d4b68f7ccc5",
                        "name": "武器使用规则: 不要对该目标类型使用武器. 目标类型:",
                        "status": 1
                    },
                    {
                        "id": "ebbe9963-d7b7-439c-97d1-4ef1654c1081",
                        "name": "2x 不能开火. 目标超出武器射程",
                        "status": 0
                    }
                ],
                "id": "hsfw-dataweapon-00000000001533",
                "name": "2x 1700 升 副油箱"
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-10-27 22:08:26"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `c2t`；调用位置数量 1。

```javascript
function c2t(e){return nt({url:"/ApiCtrl/api/weapon-assignment",method:"get",headers:{"Content-Type":"application/json"},params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/366664598e0)

- frontend：`source_materials/frontend_calls.json`


### 武器分配（手动接战目标、纯方位攻击）

**操作标识：** `POST /api/weapon-assignment`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/weapon-assignment`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

targetGuid传参即为手动接战目标，targetLon、targetLat传参即为纯方位攻击

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | strikePlatformId | string | 是 | 打击平台id |
| body | targetPlatformId | string \| null | 否 | 目标平台id；手动接战目标时使用该参数 |
| body | targetLon | number \| null | 否 | 目标点的经度；纯方位攻击时使用该参数 |
| body | targetLat | number \| null | 否 | 目标点的纬度；纯方位攻击时使用该参数 |
| body | weaponId | string \| null | 否 | 武器DBID，是数据库ID不是UUID |
| body | type | enum<string> | 是 | ；枚举：add, addChoose, addAll, addSalvo, deleteSalvo, setSalvoTimeout |
| body | number | integer \| null | 否 | 武器一次分配数量 |
| body | weaponSalvoId | string \| null | 否 | 武器齐射GUID |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "strikePlatformId": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "targetLon": 122.56725,
    "targetLat": 21.8562,
    "weaponId": "hsfw-dataweapon-00000000002108",
    "type": "add",
    "number": 1,
    //"weaponSalvoId": "15"
}
```

### 删除分配

```json
{
    "strikePlatformId": "ef65f066-0fd3-4688-9710-5bbc89065a68",
    "targetPlatformId": "8B1BBE05-BAB2-4AFA-B088-3FD41703B544",
    "type": "deleteSalvo",
    "weaponSalvoId": "0d7b96ff-387b-4071-9f4c-164608aef186"
}
```

### 控制手动交战是否设置齐射间隔

```json
{
    "strikePlatformId": "123456",
    "type": "setSalvoTimeout",
    "number": 1
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | data.strikeAllTargetWeapon | object | 否 | 所选打击平台针对所有目标分配的武器 |
| response | data.strikeChooseTargetWeapon | object | 否 | 所选打击平台针对所选目标分配的武器 |
| response | data.targetChooseStrikeWeapon | object | 否 | 所选打击平台针对所选目标分配的武器 |
| response | data.targetAllStrikeWeapon | object | 否 | 所有打击平台针对所选目标分配的武器 |
| response | data.strikePlatform | object | 是 | 打击平台 |
| response | data.targetList | object | 是 | 目标清单 |
| response | data.weaponList | array [object] | 否 | 可用武器清单 |
| response | message | string | 是 | 提示信息 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "message": "succeed",
    "timestamp": "2025-10-28 15:36:48"
}
```

### 删除齐射分配

```json
{
    "code": 0,
    "data": {
        "strikeChooseTargetWeapon": {
            "children": [
                {
                    "id": "a17062dd-a994-4cbe-8f96-e746a38e1b83",
                    "name": "分配:  3x 霹雳-12C型空对空导弹"
                }
            ],
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "打击平台: 歼-20型战斗机"
        },
        "strikePlatform": {
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "歼-20型战斗机"
        },
        "targetChooseStrikeWeapon": {
            "children": [
                {
                    "id": "d16962a9-637d-4d01-b771-0d542e5baee9",
                    "name": "分配: 3x 霹雳-12C型空对空导弹",
                    "route": "false"
                }
            ],
            "id": "ef65f066-0fd3-4688-9710-5bbc89065a68",
            "name": "打击平台: 歼-20型战斗机"
        },
        "targetList": {
            "id": "8b1bbe05-bab2-4afa-b088-3fd41703b544",
            "name": "F-16C/D型“战隼”战斗机 #5"
        },
        "weaponList": [
            {
                "children": [
                    {
                        "autoFire": "true",
                        "id": "7765ce2f-6b8b-430b-98fd-442c8967a1a6",
                        "name": "禁止自动开火, 目标超出武器射程",
                        "status": 0
                    },
                    {
                        "autoFire": "true",
                        "id": "78b59ecf-66ed-400c-a975-0b1767200812",
                        "name": "武器控制状态: 武器谨慎开火",
                        "status": 1
                    },
                    {
                        "autoFire": "true",
                        "id": "d33983ff-d0f3-483f-820f-1ee41c0314a6",
                        "name": "武器使用规则: 每次齐射所有武器开火. 最大射程发射武器. 目标类型:飞机 - 第4代战斗机/攻击机 [过载/g: 4.0-4.9] (F-14, F-15, F-16, MiG-29, Su-27)",
                        "status": 1
                    },
                    {
                        "autoFire": "false",
                        "id": "c8434548-750a-439a-b24f-c804ba82b36a",
                        "name": "5x 不能开火. 目标超出武器射程",
                        "status": 0
                    }
                ],
                "id": "hsfw-dataweapon-00000000001796",
                "name": "5x 30毫米 Gsh-30-1型航空机炮"
            },
            {
                "children": [
                    {
                        "autoFire": "true",
                        "id": "64e109b7-3b35-47c4-84f8-23d03db6c248",
                        "name": "允许自动开火.",
                        "status": 0
                    },
                    {
                        "autoFire": "true",
                        "id": "98a9a77c-4401-48de-8d6d-f8d13c8b44d5",
                        "name": "武器控制状态: 武器谨慎开火",
                        "status": 1
                    },
                    {
                        "autoFire": "true",
                        "id": "21ad1192-d3a7-439e-a1ec-718952522d6b",
                        "name": "武器使用规则: 2x发齐射. 最大射程发射武器. 目标类型:飞机 - 第4代战斗机/攻击机 [过载/g: 4.0-4.9] (F-14, F-15, F-16, MiG-29, Su-27)",
                        "status": 1
                    },
                    {
                        "autoFire": "false",
                        "id": "71c2fef8-87dd-4dd9-a2a3-5ca823d4422d",
                        "name": "1x 可以开火(人工分配武器)",
                        "status": 2
                    }
                ],
                "id": "hsfw-dataweapon-00000000002109",
                "name": "2x 霹雳-10型空对空导弹 (1x 已分配)"
            },
            {
                "children": [
                    {
                        "autoFire": "true",
                        "id": "1c2f3a4d-c672-4ecf-9ed3-5c977abe8a7c",
                        "name": "允许自动开火.",
                        "status": 0
                    },
                    {
                        "autoFire": "true",
                        "id": "ff4e61ad-9fa2-4ba4-9029-01df7513ff03",
                        "name": "武器控制状态: 武器谨慎开火",
                        "status": 1
                    },
                    {
                        "autoFire": "true",
                        "id": "e5ac5edf-1a7a-4f03-bde9-74e91a97b46c",
                        "name": "武器使用规则: 2x发齐射. 最大射程发射武器. 目标类型:飞机 - 第4代战斗机/攻击机 [过载/g: 4.0-4.9] (F-14, F-15, F-16, MiG-29, Su-27)",
                        "status": 1
                    },
                    {
                        "autoFire": "false",
                        "id": "4c62bf21-cf50-4702-a691-33d4ba8095b3",
                        "name": "3x 可以开火(人工分配武器)",
                        "status": 2
                    }
                ],
                "id": "hsfw-dataweapon-00000000002108",
                "name": "10x 霹雳-12C型空对空导弹 (7x 已分配)"
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-10-28 15:45:04"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `f2t`；调用位置数量 2。

```javascript
function f2t(e){return nt({url:"/ApiCtrl/api/weapon-assignment",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/366662224e0)

- frontend：`source_materials/frontend_calls.json`


### 清空手动攻击的航路点

**操作标识：** `POST /api/weaponWay/clear`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/weaponWay/clear`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
  "activeUnitGUID": "单元GUID",
  "weaponSalvoGUID": "武器齐射GUID"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/427259006e0)


### 为分配的武器设置航线

**操作标识：** `POST /api/weaponWay/set`

**分类：** 攻击作战行动

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/weaponWay/set`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unitGuid": "单元GUID",
    "weaponSalvoGuid": "齐射GUID",
    "contactId": "目标GUID",
    "wayPoints": [
        { "longitude": 120.123456, "latitude": 30.123456 },
        { "longitude": 121.654321, "latitude": 31.654321 }
    ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/427097879e0)


## 条令

### 获取条令信息

**操作标识：** `GET /api/DoctrineInfo`

**分类：** 条令

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/DoctrineInfo`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 是 | ；被查询的推演方guid会单元guid；文档examples：28bdfed6-b88a-401b-93b6-f37748b969ad |
| query | Type | enum<string> | 是 | ；枚举：Unit, Mission, Side；文档examples：Side |
| query | IsEscort | boolean | 否 | ；文档examples：false |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Hb`；调用位置数量 1。

```javascript
function Hb(n){return G5({url:"/ApiCtrl/api/DoctrineInfo",method:"get",headers:{"Content-Type":"application/json"},params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/376692659e0)

- frontend：`source_materials/frontend_calls.json`


### 设置条令接口

**操作标识：** `POST /api/DoctrineInfo`

**分类：** 条令

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/DoctrineInfo`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | Guid | string | 是 | ；要设置的id 如单元id 任务id  推演方id |
| body | SubjectType | string | 是 | ；要设置的类型 如 Mission  Side Unit |
| body | IsEscort | boolean | 是 | 是否护航 |
| body | Value | object | 是 | 设置值 |
| body | Value.General | object | 是 | ；电磁管控设置节点名称 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Guid": "94",
    "SubjectType": "ea",
    "IsEscort": true,
    "Value": {
       "REARE":
       {
         "withdraw_on_damage":"",//字符串，毁伤程度大于，0--忽略毁伤，1--5%，2--25%，3--50%，4--75%
        "withdraw_on_fuel":"",//字符串，燃油少于，0--忽略燃油限制，1--Bingo燃油，2--25%，3--50%，4--75%
        "withdraw_on_attack":"",//字符串，主要攻击武器处于，0--忽略，1--耗光，2--25%，3--50%，4--75%
        "withdraw_on_defence":"",//字符串，主要防御武器至少处于0--忽略，1--耗光，2--25%，3--50%，4--75%
        //部署
        "deploy_on_damage":"",//字符串，毁伤程度小于0--忽略毁伤，1--5%，2--25%，3--50%，4--75%
        "deploy_on_fuel":"",//字符串，燃油至少处于0--忽略燃油限制，1--Bingo燃油，2--25%，3--50%，4--75%，5--100%
        "deploy_on_attack":"",//字符串，主要攻击武器处于0--忽略，1--耗光，2--25%，3--50%，4--75%，5--100%，6—所有攻击武器
        "deploy_on_defence":""//字符串，主要防御武器至少处于0--忽略，1--耗光，2--25%，3--50%，4--75%，5--100%，6—所有防御武器
       }
    },

    "WeaUse":[
      {
          "wea_id":"",//武器id
          "rules":[
            {
              "target_type":"",//目标类型
              "qty_salvo":" ",//齐射武器数量
              "shooter_salvo":"",//齐射发射架数
              "firing_range":"",//自动开火距离
              "self_defence":""//自动防御距离
            },
            {
              "target_type":"",//目标类型
              "qty_alvo":" ",//齐射武器数量
              "shooter_salvo":"",//齐射发射架数
              "firing_range":"",//自动开火距离
              "self_defence":""//自动防御距离
            }
          ]
      },
      {
          "wea_id":"",//武器id
          "rules":[
            {
              "target_type":"",//目标类型
              "qty_alvo":" ",//齐射武器数量
              "shooter_salvo":"",//齐射发射架数
              "firing_range":"",//自动开火距离
              "self_defence":""//自动防御距离
            },
            {
              "target_type":"",//目标类型
              "qty_alvo":" ",//齐射武器数量
              "shooter_salvo":"",//齐射发射架数
              "firing_range":"",//自动开火距离
              "self_defence":""//自动防御距离
            }
          ]
      }





    ]



}
```

### 设置通用条令 (General) 此场景用于设置更广泛的战术规则。 examples 2.1: 设置核武器使用规则

```json
{
    "Guid": "mission_67890",
    "SubjectType": "mission",
    "IsEscort": true,
    "Value": {
        "General": {
            "Nukes": "2"
        }
    }
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "Guid": "1111-1111-1111-1111",
    "SubjectType": "unit",
    "IsEscort": false,
    "Value": {
        "General": {
            "Other": {
                "AutomaticEvasion": "1"
            }
        }
    }
}
```

### examples 1.1: 设置雷达为被动模式

```json
{
    "Guid": "mission_12345",
    "SubjectType": "mission",
    "IsEscort": false,
    "Value": {
        "EMCSetting": {
            "Radar": "0"
        }
    }
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `ms`；调用位置数量 2。

```javascript
function ms(n){return G5({url:"/ApiCtrl/api/DoctrineInfo",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/377415052e0)

- frontend：`source_materials/frontend_calls.json`


### 获取某个武器的使用规则

**操作标识：** `POST /api/WeaponUsageRules`

**分类：** 条令

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/WeaponUsageRules`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "type":"",//side,mission,unit,group
    "id":"",  //sideid,missionid,unitid,groupid
    "escort":false,//是否护航
    "weapon_guid":""//武器guid
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Yb`；调用位置数量 1。

```javascript
function Yb(n){return G5({url:"/ApiCtrl/api/WeaponUsageRules",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/392962066e0)

- frontend：`source_materials/frontend_calls.json`


## 武器详细列表相关

### 获取单元武器信息

**操作标识：** `GET /api/unitWeaponInfo`

**分类：** 武器详细列表相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitWeaponInfo`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

获取武器的挂架 飞机会有挂载方案包含的数据

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | guid | string | 否 | 单元的guid；文档examples：6b55015f-f1ed-4823-bf7d-52f4a96bd4aa |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
[
    {
        "id": "", //挂架guid
        "name": "", //挂架名称
        "status": "", //挂架状态 0:正常工作,1:损伤,2:已被摧毁
        "fireState": "", //开火状态
        "numQuantity": "", //挂架中的数据比例  30/30   当前武器总数/容量
        "weaponRecord": [
            {
               "id": "", //武器记录id
                "name": "", //武器名称
                "curNum": 1, //当前数量
                "maxNum": 1 ,//最大数量
                "reloadPriority": false //重新装载优先级
            },
            {
                "id": "", //武器记录id
                "name": "", //武器名称
                "curNum": 1, //当前数量
                "maxNum": 1 ,//最大数量
                "reloadPriority": false //重新装载优先级
            }
        ]
    }
]
```

### 成功examples

```json
{
    "code": 101,
    "data": [
        {
            "fireState": "就绪",
            "id": "f3b93a28-4e14-4a3e-9631-12bd1151f5e9",
            "name": "20毫米/85 M61A1“火神”式航空机关炮 [675发备弹]",
            "numQuantity": "(7/7)",
            "status": "0",
            "type": "mount",
            "weaponRecord": [
                {
                    "curNum": 7,
                    "id": "d4c1d8b3-7943-4eb4-8a87-7b6a5b28d1ba",
                    "maxNum": 7,
                    "name": "20毫米/85 M61A1“火神”机载航炮 [100 发备弹]",
                    "reloadPriority": false
                }
            ]
        },
        {
            "fireState": "就绪",
            "id": "fd5c3857-ee70-4051-be8c-5ace029cbfbc",
            "name": "AN/ALE-39型干扰物投放器 x 2 [60发弹]",
            "numQuantity": "(16/16)",
            "status": "0",
            "type": "mount",
            "weaponRecord": [
                {
                    "curNum": 10,
                    "id": "30c20fe6-8e47-4ae4-bcfe-a9e231da3a34",
                    "maxNum": 10,
                    "name": "通用红外干扰弹 齐射 [3x 弹药桶, 单光谱]",
                    "reloadPriority": false
                },
                {
                    "curNum": 6,
                    "id": "8c051c07-c19c-465d-bbc2-2b7a12d23865",
                    "maxNum": 6,
                    "name": "通用箔条 齐射 [5x 弹药桶]",
                    "reloadPriority": false
                }
            ]
        },
        {
            "id": "fce2a702-3349-4b60-8d46-ec88d3888971",
            "name": "空对空: AIM-54A 型“不死鸟”远程空对空导弹, 轻型空中阻拦战斗巡逻任务",
            "numQuantity": "(8/8)",
            "type": "loadout",
            "weaponRecord": [
                {
                    "curNum": 2,
                    "id": "0ba6f65d-f71f-4c65-8884-2aff5e870576",
                    "maxNum": 2,
                    "name": "1010.595 升 副油箱"
                },
                {
                    "curNum": 2,
                    "id": "14de6d68-dc2c-4661-b9cd-b945b02e2aaa",
                    "maxNum": 2,
                    "name": "AIM-7M型“麻雀-3”空空导弹"
                },
                {
                    "curNum": 2,
                    "id": "1db89307-b2e6-4116-bc35-347149c11cc8",
                    "maxNum": 2,
                    "name": "AIM-54A型“不死鸟”空空导弹"
                },
                {
                    "curNum": 2,
                    "id": "48b911a5-cf25-4d78-8882-d73934e1ff2a",
                    "maxNum": 2,
                    "name": "AIM-9M型“响尾蛇”空空导弹"
                }
            ]
        }
    ],
    "message": "failed",
    "timestamp": "2025-12-05 15:17:21"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `v1t`；调用位置数量 1。

```javascript
function v1t(e){return nt({url:"/ApiCtrl/api/unitWeaponInfo",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/385732564e0)

- frontend：`source_materials/frontend_calls.json`


### 获取所有武器挂架

**操作标识：** `GET /api/unitWeaponInfo/getMountList`

**分类：** 武器详细列表相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitWeaponInfo/getMountList`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | filterName | string | 否 | 根据挂架名称 |
| query | startName | string | 否 | 选择的页数 |
| query | pageName | string | 否 | 一页多少条 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `p1t`；调用位置数量 1。

```javascript
function p1t(e){return nt({url:"/ApiCtrl/api/unitWeaponInfo/getMountList",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387333187e0)

- frontend：`source_materials/frontend_calls.json`


### 获取武器记录数据-添加武器系统窗口数据获取

**操作标识：** `GET /api/unitWeaponInfo/getWeaponRecordData`

**分类：** 武器详细列表相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitWeaponInfo/getWeaponRecordData`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | filterName | string | 否 | 通过名称过滤数据 |
| query | startNum | integer | 否 | 第几页；文档examples：1 |
| query | pageNum | string | 否 | 每页页数 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.Weacords | array [object] | 是 |  |
| response | data.total | integer | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `s1t`；调用位置数量 2。

```javascript
function s1t(e){return nt({url:"/ApiCtrl/api/unitWeaponInfo/getWeaponRecordData",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387082260e0)

- frontend：`source_materials/frontend_calls.json`


### 武器信息列表操作接口

**操作标识：** `POST /api/unitWeaponInfo/operation`

**分类：** 武器详细列表相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitWeaponInfo/operation`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

添加武器系统、删除武器系统、添加武器挂架、删除武器挂架，修改武器数量

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "option": "reloadMount", //操作类型  修改当前武器数量
    "uuitId": "027243ad-268f-47a9-b66c-de6f5bf35bd0", //单元id
    "mount_id": "07d4d9cf-9fca-4d0e-a873-588cbec8b4a4", //挂架id
    "wea_guid": "8bbf6279-d51d-4d91-884a-caaf3a984755" //武器记录id
}
```

### 删除武器系统

```json
{
    "option": "delWeapon", //操作类型   删除武器系统
    "uuitId": "", //单元id
    "wea_id": "", //武器id
    "mountId": "", //挂架id
}
```

### 添加挂架

```json
{
    "option": "addMount", //操作类型   添加挂架
    "uuitId": "", //单元id
    "mount_dbid": "", //挂架数据库id
    "arc_mount": "" //方位角 “'ps1','ps2'”
}
```

### 删除挂架

```json
{
    "option": "delMount", //操作类型   删除挂架
    "uuitId": "", //单元id
    "mount_id": "", //挂架id
}
```

### 修改武器当前数量

```json
{
    "option": "changeCurLoad", //操作类型  修改当前武器数量
    "uuitId": "", //单元id
    "mount_id": "", //挂架id
    "wea_guid": "", //武器记录id
    "cur_load": "", //修改的数量
}
```

### 立即装填

```json
{
    "option": "reloadMount", //操作类型  修改当前武器数量
    "uuitId": "", //单元id
    "mount_id": "", //挂架id
    "wea_guid": "", //武器记录id
}
```

### 设置重新装载的优先级

```json
{
    "option": "reloadPriority", //操作类型  设置武器重新装载的优先级
    "uuitId": "", //单元id
    "mount_id": "", //挂架id
    "wea_guid": "", //武器记录id
    "isReloadPriority": true //
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `l1t`；调用位置数量 6。

```javascript
function l1t(e){return nt({url:"/ApiCtrl/api/unitWeaponInfo/operation",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/387054479e0)

- frontend：`source_materials/frontend_calls.json`


## 目标标识

### 放弃目标

**操作标识：** `POST /api/contact-Operation/abandonContact`

**分类：** 目标标识

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/contact-Operation/abandonContact`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "side":"红方",//当前推演方的id
    "unit_id":"7d1d42c7-27a0-4b82-a19a-51beb63cfe5c",//目标id
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `bs`；调用位置数量 2。

```javascript
function bs(n){return G5({url:"/ApiCtrl/api/contact-Operation/abandonContact",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/389000404e0)

- frontend：`source_materials/frontend_calls.json`


### 标识目标立场

**操作标识：** `POST /api/contact-Operation/markContact`

**分类：** 目标标识

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/contact-Operation/markContact`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "side":"红方",//当前推演方的id
    "unit_id":"87ae1623-0a74-4ddf-9b3d-6e1f68ae2b4c",//目标id
    "contactType":"H"//目标立场类型 'F'：友方，'N'：中立，'U'：非友方，'H'：敌方
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Cs`；调用位置数量 2。

```javascript
function Cs(n){return G5({url:"/ApiCtrl/api/contact-Operation/markContact",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/388905536e0)

- frontend：`source_materials/frontend_calls.json`


### 重新命名目标

**操作标识：** `POST /api/contact-Operation/renameContact`

**分类：** 目标标识

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/contact-Operation/renameContact`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "side":"红方",//当前推演方的id
    "unit_id":"87ae1623-0a74-4ddf-9b3d-6e1f68ae2b4c",//目标id
    "newName":""//新名称
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `xs`；调用位置数量 2。

```javascript
function xs(n){return G5({url:"/ApiCtrl/api/contact-Operation/renameContact",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/388984687e0)

- frontend：`source_materials/frontend_calls.json`


## 空中行动、停靠行动相关

### 删除基地已有单元接口

**操作标识：** `POST /api/addUnitOperation/DelUnits`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/DelUnits`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | baseGuid | string | 是 | 基地Guid |
| body | selectDBGuid | string | 是 | ；选择删除的单元dbguid |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
  "baseGuid": "dcd38659-a1b4-4c91-b666-8b88064031cb",
  "selectDBGuid": "28cf5fe3-f025-4f77-8974-19f0a4cce6bf"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Eyt`；调用位置数量 1。

```javascript
function Eyt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/DelUnits",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/371048698e0)

- frontend：`source_materials/frontend_calls.json`


### 单元数量修改接口

**操作标识：** `POST /api/addUnitOperation/modifyNumber`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/modifyNumber`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

修改机场中某类型的单元数量

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | baseGuid | string | 是 | 基地GUID |
| body | selectDBGuid | string | 是 | ；当前需要修改数量的飞机的DBGUID |
| body | number | integer | 是 | 修改后的数量 |
| body | type | string | 是 | ；单元类型  Aircraft  Ship   Submarine |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "baseGuid": "e549d0c8-fcc6-4061-8649-e3903e0c00b3",
    "selectDBGuid": "0159c6be-8a5b-45b5-ac8b-18f2f00c76ea",
    "number": 1,
    "type": "Aircraft"
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Ayt`；调用位置数量 1。

```javascript
function Ayt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/modifyNumber",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/371049233e0)

- frontend：`source_materials/frontend_calls.json`


### 批量添加单元接口

**操作标识：** `POST /api/addUnitOperation/multiHandle`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/addUnitOperation/multiHandle`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

添加机场飞机，舰船停靠

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | guid | string | 是 | 数据库GUID |
| body | type | string | 是 | ；类型 Aircraft,Ship  ，飞机基地，舰艇停靠 |
| body | unitname | string | 是 | 呼号 |
| body | baseGuid | string | 是 | 基地guid |
| body | number | integer | 是 | 数量 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
	"guid": "0159c6be-8a5b-45b5-ac8b-18f2f00c76ea",
	"type": "Aircraft",
	"unitname": "fi",
	"baseGuid": "e549d0c8-fcc6-4061-8649-e3903e0c00b3",
	"number": 4
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Myt`；调用位置数量 1。

```javascript
function Myt(e){return nt({url:"/ApiCtrl/api/addUnitOperation/multiHandle",method:"post",data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370664859e0)

- frontend：`source_materials/frontend_calls.json`


### 获取空中行动界面数据

**操作标识：** `GET /api/air-operations`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/air-operations`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；文档examples：e9a0f38c-8329-40ca-955e-5745e73e7307 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | message | string | 是 | 提示信息 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | data.allMissions | object \| null | 否 | 全部任务 |
| response | data.airStatus | array [object] \| null | 否 | 飞机状态 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "airStatus": [
            {
                "children": [
                    {
                        "id": "3b997fbe-55b5-431f-bab6-70e96edad6f3",
                        "loadoutName": "进攻型电子干扰",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079@",
                        "missionName": "对海突击-A1（对海突击，护航）",
                        "name": "EC-130H #1",
                        "status": "停放状态",
                        "time": "就绪"
                    }
                ],
                "id": 1,
                "name": "EC-130H ",
                "number": 1
            },
            {
                "children": [
                    {
                        "id": "09e2a65a-ea2b-4cf4-be97-2243be07021b",
                        "loadoutName": "空中预警(AEW)",
                        "missionId": "98753c0c-541b-4d71-8956-4e66fb0f263a",
                        "missionName": "预警（支援保障）",
                        "name": "E-2K #1",
                        "status": "停放状态",
                        "time": "就绪"
                    }
                ],
                "id": 2,
                "name": "E-2K ",
                "number": 1
            },
            {
                "children": [
                    {
                        "id": "0664a6ec-6a2b-4978-889d-57b91d3620c6",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079",
                        "missionName": "对海突击-A1（对海突击）",
                        "name": "F-16A #1",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "78be73b4-9973-4114-8e23-479987bf29fc",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079",
                        "missionName": "对海突击-A1（对海突击）",
                        "name": "F-16A #2",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "b6f68fa2-81e8-46fd-b098-4d4040ea49c6",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079",
                        "missionName": "对海突击-A1（对海突击）",
                        "name": "F-16A #3",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "2e9be802-57a2-4ace-9af9-8f0cf0e9a5df",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079",
                        "missionName": "对海突击-A1（对海突击）",
                        "name": "F-16A #4",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "e376b578-f61a-4990-9291-e5a3d2820395",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079",
                        "missionName": "对海突击-A1（对海突击）",
                        "name": "F-16A #5",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "3b673120-ff89-4b11-bbb7-c19d472ec357",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079",
                        "missionName": "对海突击-A1（对海突击）",
                        "name": "F-16A #6",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "8257502e-add4-4871-8ff5-012548bc7b3b",
                        "loadoutName": "空对空: AIM-120C-7 高级中程空对空导弹, AN/ALQ-184型电子干扰吊舱, 重型挂载 402",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079@",
                        "missionName": "对海突击-A1（对海突击，护航）",
                        "name": "F-16A #7",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "1e354a53-fa06-4bf7-be61-9ea12c92e5df",
                        "loadoutName": "空对空: AIM-120C-7 高级中程空对空导弹, AN/ALQ-184型电子干扰吊舱, 重型挂载 402",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079@",
                        "missionName": "对海突击-A1（对海突击，护航）",
                        "name": "F-16A #8",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "887cbb68-5745-40fd-aecd-2172302712d8",
                        "loadoutName": "空对空: AIM-120C-7 高级中程空对空导弹, AN/ALQ-184型电子干扰吊舱, 重型挂载 402",
                        "missionId": "5ae20c52-6470-4920-b13b-9dd50d57f079@",
                        "missionName": "对海突击-A1（对海突击，护航）",
                        "name": "F-16A #9",
                        "status": "停放状态",
                        "time": "就绪"
                    }
                ],
                "id": 3,
                "name": "F-16A ",
                "number": 9
            }
        ],
        "allMissions": {
            "12f4fd92-d6db-45f1-908d-0d6257cbde71": "对海突击-C2",
            "12f4fd92-d6db-45f1-908d-0d6257cbde71@": "对海突击-C2 - 护航",
            "3222d96e-3c89-4da1-a4bb-577aff28b450": "对海突击-C1",
            "3222d96e-3c89-4da1-a4bb-577aff28b450@": "对海突击-C1 - 护航",
            "3496875a-8122-410e-8bc3-c020179a45f3": "对海突击-A3",
            "3496875a-8122-410e-8bc3-c020179a45f3@": "对海突击-A3 - 护航",
            "3512ea3f-1034-48e4-aa66-962947ed6f81": "对海突击-A2",
            "3512ea3f-1034-48e4-aa66-962947ed6f81@": "对海突击-A2 - 护航",
            "4b6022cc-38bb-4389-9e16-ced34ad48bc2": "对海突击-B2",
            "4b6022cc-38bb-4389-9e16-ced34ad48bc2@": "对海突击-B2 - 护航",
            "5ae20c52-6470-4920-b13b-9dd50d57f079": "对海突击-A1",
            "5ae20c52-6470-4920-b13b-9dd50d57f079@": "对海突击-A1 - 护航",
            "7e270a49-ad05-44ea-8b21-0d3f8fcd7661": "对海突击-B3",
            "7e270a49-ad05-44ea-8b21-0d3f8fcd7661@": "对海突击-B3 - 护航",
            "98753c0c-541b-4d71-8956-4e66fb0f263a": "early_warning",
            "c7e02b91-0a6a-473b-b6fd-d9bb9301caa4": "对海突击-B1",
            "c7e02b91-0a6a-473b-b6fd-d9bb9301caa4@": "对海突击-B1 - 护航",
            "f0a47fd6-19f2-476a-938c-ee012a202d32": "对海突击-C3",
            "f0a47fd6-19f2-476a-938c-ee012a202d32@": "对海突击-C3 - 护航"
        }
    },
    "message": "succeed",
    "timestamp": "2025-10-25 22:14:31"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Ib`；调用位置数量 1。

```javascript
function Ib(n){return G5({url:"/ApiCtrl/api/air-operations",method:"get",params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/365659907e0)

- frontend：`source_materials/frontend_calls.json`


### 确认出动准备接口

**操作标识：** `POST /api/air-operations/ConfirmDP`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/air-operations/ConfirmDP`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | Units | array[string] | 是 | 飞机的guid数组 |
| body | loadGuid | string | 是 | ；选择的挂载方案guid |
| body | option | string | 是 | ；normal (正常) 或者 automatic  (自动添加武器) |
| body | quickly | boolean | 是 |  |
| body | index | integer | 是 | ；没有勾选快速出动就-1，勾选了就是0 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Units":[
        "137a8214-a978-4720-98be-1314463e65bd",
        "25613009-04d4-4d9e-8c36-cf65485da06f"
    ],
    "loadGuid":"27f38ceb-719e-4bf8-9e4c-c117faabddf9",
    "option":"automatic",
    "quickly":false,
    "index":-1
}

```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `fs`；调用位置数量 2。

```javascript
function fs(n){return G5({url:"/ApiCtrl/api/air-operations/ConfirmDP",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/372233814e0)

- frontend：`source_materials/frontend_calls.json`


### 空中行动界面操作

**操作标识：** `POST /api/air-operations/aircraft-status`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/air-operations/aircraft-status`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 用途补充

暂时只开发了单机出动、编组出动，其他功能正在开发

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | id | array[string] | 是 | 单元GUID |
| body | type | enum<string> | 是 | 指令类型；枚举：singleOperation, groupOperation, operationReady, terminationOfOperation, moveHangar, operationalRules, assignMission, operationTime, rename, delete |
| body | params | enum<string> \| enum<null> | 否 | 额外参数；不同指令类型有不同的参数；枚举：00:00:00, 名称 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "id": [
        "2f1742f9-7e8a-423d-af8e-015a2ab75d4c",
        "8ffcf23e-407a-47bb-8e8d-937f2a7f39d2",
        "5657dd09-b608-445e-9c21-b155dbe8d4ad",
        "4523b852-96fa-4e5c-b36c-1d7aa8ad0eb3"
    ],
    "type": "singleOperation",
    "params": ""
}
```

### 设置出动准备时间

```json
{
    "id": [
        "2f1742f9-7e8a-423d-af8e-015a2ab75d4c",
        "8ffcf23e-407a-47bb-8e8d-937f2a7f39d2",
        "5657dd09-b608-445e-9c21-b155dbe8d4ad",
        "4523b852-96fa-4e5c-b36c-1d7aa8ad0eb3"
    ],
    "type": "operationTime",
    "params": "00:00:00"
}
```

### 终止出动

```json
{
    "id": [
        "2f1742f9-7e8a-423d-af8e-015a2ab75d4c",
        "8ffcf23e-407a-47bb-8e8d-937f2a7f39d2",
        "5657dd09-b608-445e-9c21-b155dbe8d4ad",
        "4523b852-96fa-4e5c-b36c-1d7aa8ad0eb3"
    ],
    "type": "terminationOfOperation",
    "params": ""
}
```

### 重命名

```json
{
    "id": [
        "2f1742f9-7e8a-423d-af8e-015a2ab75d4c"
    ],
    "type": "rename",
    "params": "新的名称"
}
```

### 删除

```json
{
    "id": [
        "2f1742f9-7e8a-423d-af8e-015a2ab75d4c",
        "8ffcf23e-407a-47bb-8e8d-937f2a7f39d2",
        "5657dd09-b608-445e-9c21-b155dbe8d4ad",
        "4523b852-96fa-4e5c-b36c-1d7aa8ad0eb3"
    ],
    "type": "delete",
    "params": ""
}
```

### 分配至任务

```json
{
    "id": [
        "2f1742f9-7e8a-423d-af8e-015a2ab75d4c",
        "8ffcf23e-407a-47bb-8e8d-937f2a7f39d2",
        "5657dd09-b608-445e-9c21-b155dbe8d4ad",
        "4523b852-96fa-4e5c-b36c-1d7aa8ad0eb3"
    ],
    "type": "assignMission",
    "params": "780fd45b-07c4-40a4-ad72-46e3f7285101"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | message | string | 是 | 提示信息 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | data.allMissions | object \| null | 否 | 全部任务 |
| response | data.airStatus | array [object] \| null | 否 | 飞机状态 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "airStatus": [
            {
                "children": [
                    {
                        "id": "3b997fbe-55b5-431f-bab6-70e96edad6f3",
                        "loadoutName": "进攻型电子干扰",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2@",
                        "missionName": "对海突击-B2（对海突击，护航）",
                        "name": "EC-130H #1",
                        "status": "停放状态",
                        "time": "就绪"
                    }
                ],
                "id": 1,
                "name": "EC-130H ",
                "number": 1
            },
            {
                "children": [
                    {
                        "id": "09e2a65a-ea2b-4cf4-be97-2243be07021b",
                        "loadoutName": "空中预警(AEW)",
                        "missionId": "98753c0c-541b-4d71-8956-4e66fb0f263a",
                        "missionName": "预警（支援保障）",
                        "name": "E-2K #1",
                        "status": "停放状态",
                        "time": "就绪"
                    }
                ],
                "id": 2,
                "name": "E-2K ",
                "number": 1
            },
            {
                "children": [
                    {
                        "id": "0664a6ec-6a2b-4978-889d-57b91d3620c6",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #1",
                        "status": "正在滑行准备起飞",
                        "time": "2分"
                    },
                    {
                        "id": "78be73b4-9973-4114-8e23-479987bf29fc",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #2",
                        "status": "正在滑行准备起飞",
                        "time": "2分"
                    },
                    {
                        "id": "b6f68fa2-81e8-46fd-b098-4d4040ea49c6",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #3",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "2e9be802-57a2-4ace-9af9-8f0cf0e9a5df",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #4",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "e376b578-f61a-4990-9291-e5a3d2820395",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #5",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "3b673120-ff89-4b11-bbb7-c19d472ec357",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #6",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "8257502e-add4-4871-8ff5-012548bc7b3b",
                        "loadoutName": "空对空: AIM-120C-7 高级中程空对空导弹, AN/ALQ-184型电子干扰吊舱, 重型挂载 402",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2@",
                        "missionName": "对海突击-B2（对海突击，护航）",
                        "name": "F-16A #7",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "1e354a53-fa06-4bf7-be61-9ea12c92e5df",
                        "loadoutName": "空对空: AIM-120C-7 高级中程空对空导弹, AN/ALQ-184型电子干扰吊舱, 重型挂载 402",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2@",
                        "missionName": "对海突击-B2（对海突击，护航）",
                        "name": "F-16A #8",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "887cbb68-5745-40fd-aecd-2172302712d8",
                        "loadoutName": "空对空: AIM-120C-7 高级中程空对空导弹, AN/ALQ-184型电子干扰吊舱, 重型挂载 402",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2@",
                        "missionName": "对海突击-B2（对海突击，护航）",
                        "name": "F-16A #9",
                        "status": "停放状态",
                        "time": "就绪"
                    }
                ],
                "id": 3,
                "name": "F-16A ",
                "number": 9
            }
        ],
        "allMissions": {
            "12f4fd92-d6db-45f1-908d-0d6257cbde71": "对海突击-C2",
            "12f4fd92-d6db-45f1-908d-0d6257cbde71@": "对海突击-C2 - 护航",
            "3222d96e-3c89-4da1-a4bb-577aff28b450": "对海突击-C1",
            "3222d96e-3c89-4da1-a4bb-577aff28b450@": "对海突击-C1 - 护航",
            "3496875a-8122-410e-8bc3-c020179a45f3": "对海突击-A3",
            "3496875a-8122-410e-8bc3-c020179a45f3@": "对海突击-A3 - 护航",
            "3512ea3f-1034-48e4-aa66-962947ed6f81": "对海突击-A2",
            "3512ea3f-1034-48e4-aa66-962947ed6f81@": "对海突击-A2 - 护航",
            "4b6022cc-38bb-4389-9e16-ced34ad48bc2": "对海突击-B2",
            "4b6022cc-38bb-4389-9e16-ced34ad48bc2@": "对海突击-B2 - 护航",
            "5ae20c52-6470-4920-b13b-9dd50d57f079": "对海突击-A1",
            "5ae20c52-6470-4920-b13b-9dd50d57f079@": "对海突击-A1 - 护航",
            "7e270a49-ad05-44ea-8b21-0d3f8fcd7661": "对海突击-B3",
            "7e270a49-ad05-44ea-8b21-0d3f8fcd7661@": "对海突击-B3 - 护航",
            "98753c0c-541b-4d71-8956-4e66fb0f263a": "early_warning",
            "c7e02b91-0a6a-473b-b6fd-d9bb9301caa4": "对海突击-B1",
            "c7e02b91-0a6a-473b-b6fd-d9bb9301caa4@": "对海突击-B1 - 护航",
            "f0a47fd6-19f2-476a-938c-ee012a202d32": "对海突击-C3",
            "f0a47fd6-19f2-476a-938c-ee012a202d32@": "对海突击-C3 - 护航"
        }
    },
    "message": "succeed",
    "timestamp": "2025-10-27 12:05:07"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Rb`；调用位置数量 1。

```javascript
function Rb(n){return G5({url:"/ApiCtrl/api/air-operations/aircraft-status",method:"post",data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/366580944e0)

- frontend：`source_materials/frontend_calls.json`


### 获取飞机出动准备界面数据

**操作标识：** `POST /api/air-operations/dispatchPreparation`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/air-operations/dispatchPreparation`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "Units":[
        "0f947c85-f484-4193-b310-425f19875941"
    ],

    "baseGuid":"76040d54-01da-4830-929d-17805b714ae5"
}

```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | array [object] | 是 |  |
| response | data.DefaultCombatRadius | number \| integer | 是 | 作战半径 |
| response | data.QuickTurnaround | integer | 是 | 是否支持快速出动 |
| response | data.QuickTurnaround_AirborneTime | integer | 是 | ；快速出动模式下，飞机滞空时间（分钟） |
| response | data.QuickTurnaround_MaxSorties | integer | 是 | ；快速出动中最大出动波次 |
| response | data.QuickTurnaround_ReadyTime | integer | 是 | ；快速出动模式下的准备时间 |
| response | data.Quick_loadouttime | string | 是 | ；挂载在快速出动模式下的使用时间要求，取值范围定义在enumloadouttimeofday，分为全天出动、仅白天出动、仅夜晚出动等。 |
| response | data.ReadyTime | integer | 是 | ；标准的出动准备时间(分钟) |
| response | data.ReadyTime_Sustained | integer | 是 | ；持续出动所需的准备时间(分钟) |
| response | data.guid | string | 是 | ；挂在方案dbguid |
| response | data.inum_Compulsory | integer | 是 | 可用挂载强制性 |
| response | data.inum_Magazine | integer | 是 | ；可用挂载弹药库+飞机 |
| response | data.inum_MagazineAndAircraft | integer | 是 | 可用挂载弹药库 |
| response | data.loadoutName | string | 是 | 挂载方案名称 |
| response | data.missionprofile | string | 是 | 任务剖面 |
| response | data.sTimeofDay | string | 是 | 昼夜条件 |
| response | data.sWeather | string | 是 | 气象条件 |
| response | data.weapon | array [object] | 是 | 所属武器 |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `cs`；调用位置数量 2。

```javascript
function cs(n){return G5({url:"/ApiCtrl/api/air-operations/dispatchPreparation",method:"post",data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/371520679e0)

- frontend：`source_materials/frontend_calls.json`


### 获取基地中已有单元数据的接口

**操作标识：** `GET /api/air-operations/getBaseUnitData`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/air-operations/getBaseUnitData`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | baseGuid | string | 否 | ；文档examples：76040d54-01da-4830-929d-17805b714ae5 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "units": [
            {
                "dbid": "0159c6be-8a5b-45b5-ac8b-18f2f00c76ea",
                "name": "fi",
                "num": 2
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-11-07 12:19:49"
}
```

## 前端请求证据

源文件 `index-DUzbMa7B.js`，函数 `Tyt`；调用位置数量 1。

```javascript
function Tyt(e){return nt({url:"/ApiCtrl/api/air-operations/getBaseUnitData",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/373156869e0)

- frontend：`source_materials/frontend_calls.json`


### 获取当前挂载信息

**操作标识：** `GET /api/air-operations/loadout`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/air-operations/loadout`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；文档examples：9b10821f-8312-4f36-8452-7dc5d05854bb |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.Info | object | 是 |  |
| response | data.LoadoutName | string | 是 |  |
| response | data.Weapon | object | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "Info": {
            "Capability": "全天, 全天候",
            "LoadoutRoleDescription": "打击，地/海",
            "NumberOfLoadouts": "0",
            "NumberOfLoadoutsIncludingMountedWeapon_MandatoryOnly": "1",
            "NumberOfLoadoutsIncludingMountedWeapons": "1",
            "RangeProfileDescription": "攻击任务活动半径,攻击目标任务剖面(接近-攻击-飞离)为: 高-低-高 . 飞行高度为10972.8米并保持中等油门(巡航) .185.2千米(92.6千米+92.6千米) 处从海平面高度冲向目标并保持最大油门(军用) . 在武器最大射程处开火. 10分钟内在609.6米高度重组队形. 燃料剩余10%时返航."
        },
        "LoadoutName": "500公斤引导式贯通炸弹, 外部挂载",
        "Weapon": {
            "AvailableWeapon": {
                "hsfw-dataweapon-00000000000221": "4x 500公斤引导式贯通炸弹",
                "hsfw-dataweapon-00000000001533": "2x 1700 升 副油箱",
                "hsfw-dataweapon-00000000002108": "2x 霹雳-12C型空对空导弹",
                "hsfw-dataweapon-00000000002109": "2x 霹雳-10型空对空导弹"
            },
            "AvailableWeaponMagazine": [],
            "AvailableWeaponMagazineAndAir": []
        }
    },
    "message": "succeed",
    "timestamp": "2025-11-13 11:22:09"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Ob`；调用位置数量 1。

```javascript
function Ob(n){return G5({url:"/ApiCtrl/api/air-operations/loadout",method:"get",params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/375693713e0)

- frontend：`source_materials/frontend_calls.json`


### 获取停靠行动界面数据

**操作标识：** `GET /api/ship-operations`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ship-operations`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；文档examples：7e77b819-a489-4419-8bd4-0527dfc58e42 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.shipStatus | array [object] | 是 |  |
| response | data.allMissions | object | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 54,
    "data": {
        "shipStatus": [
            {
                "children": [
                    {
                        "id": "78be73b4-9973-4114-8e23-479987bf29fc",
                        "name": "驱逐舰 #1",
                        "damageInfo": "没有结构性毁伤，所有系统离线",
                        "weaponInfo": "制导武器：78/78 非制导武器：1250/1250 其它武器：31/31",
                        "magazineInfo": "制导武器：78/78 非制导武器：1250/1250 其它武器：31/31",
                        "fuelState": "100%",
                        "missionName": "1",
                        "status": "完成停靠",
                        "time": "就绪"
                    },
                    {
                        "id": "78be73b5-9973-4114-8e23-479987bf29fc",
                        "name": "司马哲新",
                        "damageInfo": "in qui consectetur velit exercitation",
                        "weaponInfo": "do sed commodo Duis",
                        "magazineInfo": "aute dolor cillum qui ut",
                        "fuelState": "海南省",
                        "missionName": "伯霞",
                        "status": "ut et cillum officia consectetur",
                        "time": "2025-10-04 08:04:25"
                    }
                ],
                "id": 76,
                "name": "宿宇轩",
                "number": 88
            }
        ],
        "allMissions": {}
    },
    "message": "occaecat velit incididunt nisi ut",
    "timestamp": "1761881164"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Fb`；调用位置数量 1。

```javascript
function Fb(n){return G5({url:"/ApiCtrl/api/ship-operations",method:"get",params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/369586746e0)

- frontend：`source_materials/frontend_calls.json`


### 停靠行动界面操作

**操作标识：** `POST /api/ship-operations/ship-status`

**分类：** 空中行动、停靠行动相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/ship-operations/ship-status`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | id | array[string] | 是 | 单元GUID |
| body | type | enum<string> | 是 | 指令类型；枚举：singleOperation, groupOperation, terminationOfOperation, operationalRules, assignMission, operationTime, rename, delete |
| body | params | enum<string> \| enum<null> | 否 | 额外参数；不同指令类型有不同的参数；枚举：00:00:00, 名称 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "id": [
        "6c173bf9-c437-417e-8b3c-4b6a533c5b2b",
        "936e7003-49a6-47a2-911d-9bab625f7c1c"
    ],
    "type": "singleOperation",
    "params": ""
}
```

### 设置出动准备时间

```json
{
    "id": [
        "78327942-af5b-40f6-b47f-4962a961f89e"
    ],
    "type": "operationTime",
    "params": "00:00:00"
}
```

### 终止出动

```json
{
    "id": [
        "6c173bf9-c437-417e-8b3c-4b6a533c5b2b"
    ],
    "type": "terminationOfOperation",
    "params": ""
}
```

### 重命名

```json
{
    "id": [
        "6c173bf9-c437-417e-8b3c-4b6a533c5b2b"
    ],
    "type": "rename",
    "params": "新的名称"
}
```

### 删除

```json
{
    "id": [
        "6c173bf9-c437-417e-8b3c-4b6a533c5b2b"
    ],
    "type": "delete",
    "params": ""
}
```

### 分配至任务

```json
{
    "id": [
        "6c173bf9-c437-417e-8b3c-4b6a533c5b2b"
    ],
    "type": "assignMission",
    "params": "780fd45b-07c4-40a4-ad72-46e3f7285101"
}
```

### 编队出航

```json
{
    "id": [
        "78327942-af5b-40f6-b47f-4962a961f89e",
        "500b808a-612c-4aab-b69d-01544067217a",
        "85f55981-d392-4573-8a29-7b107b75bb73"
    ],
    "type": "groupOperation",
    "params": ""
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 | 状态码 |
| response | message | string | 是 | 提示信息 |
| response | data | object \| null | 否 | 返回的具体数据 |
| response | data.allMissions | object \| null | 否 | 全部任务 |
| response | data.airStatus | array [object] \| null | 否 | 飞机状态 |
| response | timestamp | string | 是 | 时间戳 |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "airStatus": [
            {
                "children": [
                    {
                        "id": "3b997fbe-55b5-431f-bab6-70e96edad6f3",
                        "loadoutName": "进攻型电子干扰",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2@",
                        "missionName": "对海突击-B2（对海突击，护航）",
                        "name": "EC-130H #1",
                        "status": "停放状态",
                        "time": "就绪"
                    }
                ],
                "id": 1,
                "name": "EC-130H ",
                "number": 1
            },
            {
                "children": [
                    {
                        "id": "09e2a65a-ea2b-4cf4-be97-2243be07021b",
                        "loadoutName": "空中预警(AEW)",
                        "missionId": "98753c0c-541b-4d71-8956-4e66fb0f263a",
                        "missionName": "预警（支援保障）",
                        "name": "E-2K #1",
                        "status": "停放状态",
                        "time": "就绪"
                    }
                ],
                "id": 2,
                "name": "E-2K ",
                "number": 1
            },
            {
                "children": [
                    {
                        "id": "0664a6ec-6a2b-4978-889d-57b91d3620c6",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #1",
                        "status": "正在滑行准备起飞",
                        "time": "2分"
                    },
                    {
                        "id": "78be73b4-9973-4114-8e23-479987bf29fc",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #2",
                        "status": "正在滑行准备起飞",
                        "time": "2分"
                    },
                    {
                        "id": "b6f68fa2-81e8-46fd-b098-4d4040ea49c6",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #3",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "2e9be802-57a2-4ace-9af9-8f0cf0e9a5df",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #4",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "e376b578-f61a-4990-9291-e5a3d2820395",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #5",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "3b673120-ff89-4b11-bbb7-c19d472ec357",
                        "loadoutName": "AGM-84L “鱼叉”II反舰导弹,“狙击手”XR瞄准吊舱[前视红外]，AN/ALQ-184型电子干扰吊舱",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2",
                        "missionName": "对海突击-B2（对海突击）",
                        "name": "F-16A #6",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "8257502e-add4-4871-8ff5-012548bc7b3b",
                        "loadoutName": "空对空: AIM-120C-7 高级中程空对空导弹, AN/ALQ-184型电子干扰吊舱, 重型挂载 402",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2@",
                        "missionName": "对海突击-B2（对海突击，护航）",
                        "name": "F-16A #7",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "1e354a53-fa06-4bf7-be61-9ea12c92e5df",
                        "loadoutName": "空对空: AIM-120C-7 高级中程空对空导弹, AN/ALQ-184型电子干扰吊舱, 重型挂载 402",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2@",
                        "missionName": "对海突击-B2（对海突击，护航）",
                        "name": "F-16A #8",
                        "status": "停放状态",
                        "time": "就绪"
                    },
                    {
                        "id": "887cbb68-5745-40fd-aecd-2172302712d8",
                        "loadoutName": "空对空: AIM-120C-7 高级中程空对空导弹, AN/ALQ-184型电子干扰吊舱, 重型挂载 402",
                        "missionId": "4b6022cc-38bb-4389-9e16-ced34ad48bc2@",
                        "missionName": "对海突击-B2（对海突击，护航）",
                        "name": "F-16A #9",
                        "status": "停放状态",
                        "time": "就绪"
                    }
                ],
                "id": 3,
                "name": "F-16A ",
                "number": 9
            }
        ],
        "allMissions": {
            "12f4fd92-d6db-45f1-908d-0d6257cbde71": "对海突击-C2",
            "12f4fd92-d6db-45f1-908d-0d6257cbde71@": "对海突击-C2 - 护航",
            "3222d96e-3c89-4da1-a4bb-577aff28b450": "对海突击-C1",
            "3222d96e-3c89-4da1-a4bb-577aff28b450@": "对海突击-C1 - 护航",
            "3496875a-8122-410e-8bc3-c020179a45f3": "对海突击-A3",
            "3496875a-8122-410e-8bc3-c020179a45f3@": "对海突击-A3 - 护航",
            "3512ea3f-1034-48e4-aa66-962947ed6f81": "对海突击-A2",
            "3512ea3f-1034-48e4-aa66-962947ed6f81@": "对海突击-A2 - 护航",
            "4b6022cc-38bb-4389-9e16-ced34ad48bc2": "对海突击-B2",
            "4b6022cc-38bb-4389-9e16-ced34ad48bc2@": "对海突击-B2 - 护航",
            "5ae20c52-6470-4920-b13b-9dd50d57f079": "对海突击-A1",
            "5ae20c52-6470-4920-b13b-9dd50d57f079@": "对海突击-A1 - 护航",
            "7e270a49-ad05-44ea-8b21-0d3f8fcd7661": "对海突击-B3",
            "7e270a49-ad05-44ea-8b21-0d3f8fcd7661@": "对海突击-B3 - 护航",
            "98753c0c-541b-4d71-8956-4e66fb0f263a": "early_warning",
            "c7e02b91-0a6a-473b-b6fd-d9bb9301caa4": "对海突击-B1",
            "c7e02b91-0a6a-473b-b6fd-d9bb9301caa4@": "对海突击-B1 - 护航",
            "f0a47fd6-19f2-476a-938c-ee012a202d32": "对海突击-C3",
            "f0a47fd6-19f2-476a-938c-ee012a202d32@": "对海突击-C3 - 护航"
        }
    },
    "message": "succeed",
    "timestamp": "2025-10-27 12:05:07"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Pb`；调用位置数量 1。

```javascript
function Pb(n){return G5({url:"/ApiCtrl/api/ship-operations/ship-status",method:"post",data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/369659282e0)

- frontend：`source_materials/frontend_calls.json`


## 编组操作

### 创建编组

**操作标识：** `POST /api/groupOperation/addGroup`

**分类：** 编组操作

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/groupOperation/addGroup`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "units":   //需要编组的单元id集合
    [
        "",
        "",
        ""
    ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `displaySetting-C7KFV-dj.js`，函数 `c`；调用位置数量 0。

```javascript
function c(e){return t({url:"/ApiCtrl/api/groupOperation/addGroup",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393284223e0)

- frontend：`source_materials/frontend_calls.json`


### 获取编组编辑器界面数据

**操作标识：** `GET /api/groupOperation/getGroupEditData`

**分类：** 编组操作

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/groupOperation/getGroupEditData`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | guid | string | 否 | 选中单元的guid；文档examples：f4107b18-09d0-4648-9c64-392fd876ec94 |


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "units": [
        {
            "id": "",
            "name": "",
            "leader":false;
        }
    ]
}
```

## 前端请求证据

源文件 `displaySetting-C7KFV-dj.js`，函数 `C`；调用位置数量 0。

```javascript
function C(e){return t({url:"/ApiCtrl/api/groupOperation/getGroupEditData",method:"get",params:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393384746e0)

- frontend：`source_materials/frontend_calls.json`


### 脱离编组

**操作标识：** `POST /api/groupOperation/removeUnitFromGroup`

**分类：** 编组操作

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/groupOperation/removeUnitFromGroup`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{

    "uuid":""//需要脱离编组的单元

}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `displaySetting-C7KFV-dj.js`，函数 `F`；调用位置数量 0。

```javascript
function F(e){return t({url:"/ApiCtrl/api/groupOperation/removeUnitFromGroup",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393356703e0)

- frontend：`source_materials/frontend_calls.json`


### 设置编组队形

**操作标识：** `POST /api/groupOperation/setGroupFormation`

**分类：** 编组操作

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/groupOperation/setGroupFormation`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
// {
//     "unit_id":"",//单元id
//     "type":"",//与领队的空间相对关系的维持模式（'FIXED'：维持平动，'Rotating'：同步转动）；
//     "bearing":0.0,//与领队的相对方位
//     "distance":0.0//与领队的距离
// }

{
  "units": [
    {
      "unit_id": "unit1_guid",
      "bearing": 45.0,
      "distance": 100.0,
      "idRotating": true
    },
    {
      "unit_id": "unit2_guid",
      "bearing": 90.0,
      "distance": 150.0,
      "idRotating": true
    }
  ]
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `displaySetting-C7KFV-dj.js`，函数 `U`；调用位置数量 0。

```javascript
function U(e){return t({url:"/ApiCtrl/api/groupOperation/setGroupFormation",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/394104804e0)

- frontend：`source_materials/frontend_calls.json`


### 设置编队领队

**操作标识：** `POST /api/groupOperation/setToGroupLead`

**分类：** 编组操作

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/groupOperation/setToGroupLead`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{

    "unit_id":""

}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `displaySetting-C7KFV-dj.js`，函数 `R`；调用位置数量 0。

```javascript
function R(e){return t({url:"/ApiCtrl/api/groupOperation/setToGroupLead",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/393870771e0)

- frontend：`source_materials/frontend_calls.json`


### 设置单元高低速交替航行

**操作标识：** `POST /api/groupOperation/setUnitSprintAndDrift`

**分类：** 编组操作

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/groupOperation/setUnitSprintAndDrift`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "unit_id":"",
    "sprint":true
}
```

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `Gb`；调用位置数量 1。

```javascript
function Gb(n){return G5({url:"/ApiCtrl/api/groupOperation/setUnitSprintAndDrift",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/429129472e0)

- frontend：`source_materials/frontend_calls.json`


## 航母仿真

### 获取某个航母的航空设施

**操作标识：** `GET /api/GetAviationFacilitiesData`

**分类：** 航母仿真

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/GetAviationFacilitiesData`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 用途补充

获取航母内的设施和某个设施内的飞机数量

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/425188558e0)


## 航线管理相关

### 获取航线点信息

**操作标识：** `GET /api/routeDetailList`

**分类：** 航线管理相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/routeDetailList`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Guid | string | 否 | ；文档examples：ccdf8847-9d8b-4d76-9c1c-0b0d1ce5d1a7 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.currentRouteDetailList | array [object] | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "currentRouteDetailList": [
            {
                "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                "name": "航线点1",
                "longitude": "116.404",
                "latitude": "39.915",
                "altitude": "1",
                "throttle": "1",
                "radar": "1",
                "sonar": "1",
                "EMI": "1"
            },
            {
                "id": "497f6eca-6276-4993-bfeb-53cbbbba6f09",
                "name": "航线点2",
                "longitude": "116.404",
                "latitude": "39.915",
                "altitude": "1",
                "throttle": "1",
                "radar": "1",
                "sonar": "1",
                "EMI": "1"
            }
        ]
    },
    "message": "string",
    "timestamp": "string"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `kD`；调用位置数量 1。

```javascript
function kD(n){return G5({url:"/ApiCtrl/api/routeDetailList",method:"get",headers:{"Content-Type":"application/json"},params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370407978e0)

- frontend：`source_materials/frontend_calls.json`


### 获取航线管理界面数据

**操作标识：** `GET /api/routeLineManage`

**分类：** 航线管理相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/routeLineManage`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | SideGuid | string | 否 | ；文档examples：05fc90c5-1a48-47dc-bd5c-7d66e1037306 |


## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.routeList | array [object] | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "routeList": [
            {
                "id": "1",
                "name": "测试航线1",
                "show": false,
                "type": "0"
            },
            {
                "id": "2",
                "name": "测试航线2",
                "show": false,
                "type": "1"
            }
        ]
    },
    "message": "string",
    "timestamp": "string"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `u7`；调用位置数量 22。

```javascript
function u7(n){return G5({url:"/ApiCtrl/api/routeLineManage",method:"get",headers:{"Content-Type":"application/json"},params:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/369939064e0)

- frontend：`source_materials/frontend_calls.json`


### 航线管理器界面操作

**操作标识：** `POST /api/routeLineManage/routeLine-status`

**分类：** 航线管理相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/routeLineManage/routeLine-status`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | sideGuid | string | 是 | 推演方GUID |
| body | name | string | 否 | 航线名称；添加重命名航线时需要 |
| body | routeType | enum<string> | 否 | 航线类型；添加航线时需要；枚举：0, 1 |
| body | type | enum<string> | 是 | 指令类型；枚举：createRouteLine, renameRouteLine, deleteRouteLine, routeLineIsShow |
| body | id | string | 否 | 航线GUID；重命名，删除，显示航线时需要 |
| body | isShow | boolean | 否 | 航线是否显示；显示航线时需要 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "sideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "type": "routeLineIsShow",
    "id": "ccdf8847-9d8b-4d76-9c1c-0b0d1ce5d1a7",
    "isShow": true
}
```

### 航线重命名

```json
{
    "sideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "id": "d9229a30-d2db-44cd-8221-700d8211de42",
    "name": "new1",
    "type": "renameRouteLine"
}
```

### 删除航线

```json
{
    "sideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "id": "d9229a30-d2db-44cd-8221-700d8211de42",
    "type": "deleteRouteLine"
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.routeList | array [object] | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "routeList": [
            {
                "id": "329d08a5-6dc7-4106-b55a-45cf1d243956",
                "name": "321",
                "show": false,
                "type": "1"
            },
            {
                "id": "ccdf8847-9d8b-4d76-9c1c-0b0d1ce5d1a7",
                "name": "123",
                "show": false,
                "type": "0"
            },
            {
                "id": "d9229a30-d2db-44cd-8221-700d8211de42",
                "name": "1",
                "show": false,
                "type": "0"
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-11-03 14:26:32"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `SD`；调用位置数量 1。

```javascript
function SD(n){return G5({url:"/ApiCtrl/api/routeLineManage/routeLine-status",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370490984e0)

- frontend：`source_materials/frontend_calls.json`


### 航线管理器航线信息操作

**操作标识：** `POST /api/routeLineManage/wayPoints-status`

**分类：** 航线管理相关

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/routeLineManage/wayPoints-status`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| body | sideGuid | string | 是 | 推演方GUID |
| body | type | enum<string> | 是 | 指令类型；枚举：addPlanWayPoint, removePlanWayPoint, updataPlanWayPoint |
| body | id | string | 是 | 航线GUID |
| body | planWayPoints | array [object] | 否 | 航线点；添加航线点时需要 |
| body | planWayPoints.longitude | string | 是 | 经度 |
| body | planWayPoints.latitude | string | 是 | 纬度 |
| body | wayPointGuid | string | 否 | 航线点GUID；删除时需要 |
| body | wayPointInformations | array [object] | 否 | 航线修改列表；更新航线时需要，修改那个值用哪个字段，不修改就不用不要为空 |
| body | wayPointInformations.id | string | 是 | 航线点GUID |
| body | wayPointInformations.name | string | 是 | 名称 |
| body | wayPointInformations.longitude | string | 是 | 经度 |
| body | wayPointInformations.latitude | string | 是 | 纬度 |
| body | wayPointInformations.altitude | string | 是 | 高度 |
| body | wayPointInformations.throttle | string | 是 | 油门 |
| body | wayPointInformations.radar | string | 是 | 雷达 |
| body | wayPointInformations.sonar | string | 是 | 声呐 |
| body | wayPointInformations.oecm | string | 是 | 干扰 |


## 请求体examples（examples ID 必须替换）

### 页面默认examples

```json
{
    "sideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "type": "updataPlanWayPoint",
    "id": "329d08a5-6dc7-4106-b55a-45cf1d243956",
    "wayPointInformations": [
        {
            "wayPointGuid": "c0ea2bbf-a988-4fa9-a937-43c97450740a",
            "name": "1",
            "longitude": "110",
            "latitude": "15",
            "altitude": "2",
            "throttle": "2",
            "radar": "1",
            "sonar": "1",
            "oecm": "1"
        },
        {
            "wayPointGuid": "aba499e8-763e-460e-904d-487fbd09b40a",
            "name": "2",
            "longitude": "111",
            "latitude": "16",
            "altitude": "2",
            "throttle": "2",
            "radar": "1",
            "sonar": "1",
            "oecm": "1"
        }
    ]
}
```

### 删除航线点

```json
{
    "sideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "type": "removePlanWayPoint",
    "id": "329d08a5-6dc7-4106-b55a-45cf1d243956",
    "wayPointGuid": "04ec9104-68b8-4b77-bf2e-fc8491607bfe"
}
```

### 更新航线点

```json
{
    "sideGuid": "05fc90c5-1a48-47dc-bd5c-7d66e1037306",
    "type": "updataPlanWayPoint",
    "id": "329d08a5-6dc7-4106-b55a-45cf1d243956",
    "wayPointInformation": [
        {
            "id": "48",
            "name": "1",
            "longitude": "110",
            "latitude": "15",
            "altitude": "2",
            "throttle": "2",
            "radar": "1",
            "sonar": "1",
            "oecm": "1"
        },
        {
            "id": "48",
            "name": "2",
            "longitude": "111",
            "latitude": "16",
            "altitude": "2",
            "throttle": "2",
            "radar": "1",
            "sonar": "1",
            "oecm": "1"
        }
    ]
}
```

## 返回字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| response | code | integer | 是 |  |
| response | data | object | 是 |  |
| response | data.routeList | array [object] | 是 |  |
| response | message | string | 是 |  |
| response | timestamp | string | 是 |  |


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{
    "code": 0,
    "data": {
        "currentRouteDetailList": [
            {
                "EMI": "2",
                "altitude": "0",
                "id": "a8bef2d4-1271-4033-84f4-5c275945b2ac",
                "latitude": "24.2522",
                "longitude": "120.705",
                "name": "",
                "radar": "2",
                "sonar": "2",
                "throttle": "0"
            },
            {
                "EMI": "2",
                "altitude": "0",
                "id": "c430dc0c-71c0-4240-8d35-239445a340ef",
                "latitude": "26.5422",
                "longitude": "116.889",
                "name": "",
                "radar": "2",
                "sonar": "2",
                "throttle": "0"
            },
            {
                "EMI": "2",
                "altitude": "0",
                "id": "84583c9c-2c92-432b-92f6-13e8a44f456e",
                "latitude": "24.2274",
                "longitude": "115.674",
                "name": "",
                "radar": "2",
                "sonar": "2",
                "throttle": "0"
            },
            {
                "EMI": "2",
                "altitude": "0",
                "id": "c6a4de4a-1f98-456d-a2dc-3255eec91a5b",
                "latitude": "25.1061",
                "longitude": "115.554",
                "name": "",
                "radar": "2",
                "sonar": "2",
                "throttle": "0"
            },
            {
                "EMI": "2",
                "altitude": "0",
                "id": "5077a910-6207-4bb0-abfd-3e93bb583301",
                "latitude": "25.7276",
                "longitude": "116.264",
                "name": "",
                "radar": "2",
                "sonar": "2",
                "throttle": "0"
            },
            {
                "EMI": "2",
                "altitude": "0",
                "id": "63f59fb8-3b2a-41d3-90ce-c7cababcd8af",
                "latitude": "31",
                "longitude": "121",
                "name": "",
                "radar": "2",
                "sonar": "2",
                "throttle": "0"
            }
        ]
    },
    "message": "succeed",
    "timestamp": "2025-11-03 15:37:01"
}
```

## 前端请求证据

源文件 `HomeNew-BR7XaDpD.js`，函数 `wD`；调用位置数量 1。

```javascript
function wD(n){return G5({url:"/ApiCtrl/api/routeLineManage/wayPoints-status",method:"post",headers:{"Content-Type":"application/json"},data:n})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/370681780e0)

- frontend：`source_materials/frontend_calls.json`


## 获取系统状态

### 获取系统状态

**操作标识：** `GET /api/status`

**分类：** 获取系统状态

**资料依据：** 本机 JSON 实测；Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/status`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 用途补充

是否加载想定 是：返回所有推演方，否：返回{}

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 本机只读验证

- `http://127.0.0.1:8082/ApiCtrl/api/status`：HTTP 200；2026-10-02 14:34:49 +0800；application/json; charset=utf-8

```json
{
  "code": 0,
  "data": {
    "sides": [
      "蓝方",
      "红方"
    ],
    "simStatus": 1,
    "simuTime": 12000000,
    "status": true
  },
  "message": "succeed",
  "timestamp": "2026-10-02 14:34:49"
}
```

- `http://127.0.0.1:8050/ApiCtrl/api/status`：HTTP 200；2026-10-02 14:34:49 +0800；application/json; charset=utf-8

```json
{
  "code": 0,
  "data": {
    "sides": [
      "蓝方",
      "红方"
    ],
    "simStatus": 1,
    "simuTime": 12000000,
    "status": true
  },
  "message": "succeed",
  "timestamp": "2026-10-02 14:34:49"
}
```

- `http://127.0.0.1:8050/api/status`：HTTP 200；2026-10-02 14:34:49 +0800；application/json; charset=utf-8

```json
{
  "code": 0,
  "data": {
    "sides": [
      "蓝方",
      "红方"
    ],
    "simStatus": 1,
    "simuTime": 12000000,
    "status": true
  },
  "message": "succeed",
  "timestamp": "2026-10-02 14:34:49"
}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

- simStatus 和 simuTime 的枚举/单位在提供的文档中不完整；本次值见验证报告，不据一次返回值推断所有状态。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/385591723e0)


## 设置是否获取消息output

### 设置是否获取消息output

**操作标识：** `POST /api/SetRecOutput`

**分类：** 设置是否获取消息output

**资料依据：** Apifox 文档；前端src证据；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/SetRecOutput`

**状态影响：** 可能修改状态（查询型 POST 需按用途确认）

**契约状态：** 参数来自 Apifox；运行语义需结合版本核验

## 请求字段

| 位置 | 字段路径 | 类型 | 必填 | 说明 / 枚举 |
| --- | --- | --- | --- | --- |
| query | Flag | boolean | 否 | 是否接收；文档examples：true |


资料没有完整请求体examples。仅有前端定义时，应结合对应调用位置继续核对。

## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 前端请求证据

源文件 `displaySetting-C7KFV-dj.js`，函数 `p`；调用位置数量 0。

```javascript
function p(e){return t({url:"/ApiCtrl/api/SetRecOutput",method:"post",headers:{"Content-Type":"application/json"},data:e})}
```

全部调用位置片段保存在api_catalog.json / source_materials/frontend_calls.json，不代表这些操作已在本次实测中执行。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/379929725e0)

- frontend：`source_materials/frontend_calls.json`


## 读取当前是否按模版上限限制兵力数量

### 读取当前是否按模版上限限制兵力数量

**操作标识：** `GET /api/unitDeployment/templateMaxLimit`

**分类：** 读取当前是否按模版上限限制兵力数量

**资料依据：** Apifox 文档；安装包路由

**资料中的地址：** `http://127.0.0.1:8050/ApiCtrl/api/unitDeployment/templateMaxLimit`

**状态影响：** 查询候选；本条未必已实测

**契约状态：** 缺少参数说明；无参数是否允许也需确认

## 请求字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回字段

资料没有给出可确认的字段表；不能把这一点自动解释为无参数。


## 返回examples（文档样例，不是当前想定保证值）

### 页面默认examples

```json
{}
```

## 限制、差异及待确认事项

- 资料未提供可确认的参数；不能由路由名猜测字段、枚举或成功响应。

## 来源

- local_openapi：`source_materials/openapi_original.json`

- [apifox](https://s.apifox.cn/273d98e7-69c6-4055-9fb7-ec7a22f90f74/451783206e0)
