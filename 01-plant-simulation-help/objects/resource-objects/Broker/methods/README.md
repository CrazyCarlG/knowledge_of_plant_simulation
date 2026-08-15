# Broker Methods — 摘要

本目录记录了 Plant Simulation 中 **Broker（中介/代理）** 对象的全部方法（Methods）与只读属性（Read-Only Attributes）。内容来源于 `methods.md`（`methods.txtx` 为同内容的原始导出文本）。

## 概述

Broker 是资源对象，用于在 Importers（请求方）与 Exporters/Workers（提供方）之间中介服务（Service）。它提供了：

- 下列方法（见本文档表格）。
- 所有对象共有的方法（Methods of All Objects）。

查看方式：在 Class Library 上下文菜单选择 **Show Attributes and Methods**，或在 Frame 中选中实例后按 **F8**。

## 语法约定

方法语法行形如 `<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`：

- `<Path>` 表示方法所应用对象的路径。
- 括号内为参数签名（标识符 + 数据类型）。
- 可选参数写在方括号 `[…]` 中，默认值以 `:=` 标注。
- 返回值类型以箭头 `→` 标注。
- 注意：嵌套括号必须输入完整，否则可能触发 Debugger。

## 方法一览

| 方法 | 说明 | 语法 |
| --- | --- | --- |
| `brokerStat` | 返回 Broker 的统计表并写入表格 | `<Path>.brokerStat([BrokerStatisticsTable:table]) → boolean` |
| `doStandardExport` | 让 Broker 对指定 Worker/Exporter 执行标准导出 | `<Path>.doStandardExport(Exporter:object)` |
| `doStandardImport` | 让 Broker 对指定 Importer 执行标准导入 | `<Path>.doStandardImport(Importer:object, Type:integer)` |
| `engage` | 让 Broker 将若干 Exporter/Worker 分配给一个 Importer | `<Path>.engage(Importer:object, Type:integer, Data:table) → boolean` |
| `forgetOpenRequest` | 取消 Broker 的一个未满足请求 | `<Path>.forgetOpenRequest(Importer:object, Type:integer)` |
| `getExportersForService` | 返回能提供指定服务的 Exporter/Worker 数组 | `<Path>.getExportersForService(Service:string) → object[]` |
| `getOfferedServices` | 返回 Broker 管理的所有已提供服务，写入表格 | `<Path>.getOfferedServices([Services:table]) → table` |
| `getOpenImporters` | 返回所有未满足（open）的 Importers，写入表格 | `<Path>.getOpenImporters([Importers:table]) → table` |
| `getSatisfiedImporters` | 返回所有已满足的 Importers，写入表格 | `<Path>.getSatisfiedImporters([Importers:table]) → table` |
| `globalOpenRequestsFor` | 在整个 Broker 层级中查找某 Exporter/Worker 服务的 Importers | `<Path>.globalOpenRequestsFor(Exporter:object, Importers:table)` |
| `globalTestImportFor` | 在整个 Broker 层级中为 Importer 检查可用的 Exporter/Worker | `<Path>.globalTestImportFor(Importer:object, Type:integer, Exporters:table[, OnlyAvailable:boolean]) → boolean` |
| `localOpenRequestsFor` | 在本地 Broker 中查找某 Exporter/Worker 服务的 Importers | `<Path>.localOpenRequestsFor(Exporter:object, Importers:table)` |
| `localTestImportFor` | 在本地 Broker 中为 Importer 检查可用的 Exporter/Worker | `<Path>.localTestImportFor(Importer:object, Type:integer, Exporters:table[, OnlyAvailable:boolean]) → boolean` |
| `serviceStat` | 返回 Broker 的服务统计并写入表格 | `<Path>.serviceStat([ServiceStatistics:table]) → boolean` |
| `testImportFor` | 对 Importer 执行测试请求，判断 Broker 能否满足 | `<Path>.testImportFor(Importer:object, Type:integer, Exporter:table) → boolean` |

## 关键概念：Importer 类型（Type 参数）

多个方法使用 `Type` 整数参数标识 Importer 类型：

- `0` — failure / remove failure importer（故障/移除故障）
- `1` — set-up importer（设置/准备）
- `2` — processing importer（加工）
- `3` — transport importer（运输）

## 本地 vs. 全局

- **local\*** 方法仅检查 Broker 直接管理的 Exporters/Workers。
- **global\*** 方法检查整个 Broker 层级（即通过 Connector 连接的所有 Broker）。
- 对单个 Broker 而言，`localTestImportFor` 与 `globalTestImportFor` 返回相同结果。

## 方法要点

### 统计类

- **`brokerStat`**：返回 Broker 统计表。统计收集激活时返回 `true`，否则返回 `false`（表格不变）；不传可选参数时，激活返回统计表，停用返回 `void`。
- **`serviceStat`**：返回服务统计表，返回逻辑同 `brokerStat`。统计表包含 **Dwelling Time（驻留时间）** 与 **Mediation Time（中介时间）** 两组的 Count / Sum / Mean / StdDev / Min / Max 列，对应只读属性如 `StatStayTime`、`StatStayTimeMu`、`StatStayTimeDelta`、`StatMediationTime`、`StatMediationTimeMu`、`StatMediationTimeDelta` 等。

### 请求与中介

- **`engage`**：将服务分配给 Importer。`Data` 为包含 Exporter、Services、Amount 三列的表格。全部满足返回 `true`；未满足返回 `false`，且 Broker 不会记住无法满足的请求。
- **`testImportFor`**：测试 Broker 是否会满足请求，返回 `true`/`false`。
- **`doStandardImport`** / **`doStandardExport`**：分别在 Importer/Exporter 请求控制中执行标准导入/导出，避免手动调用 `testImportFor` 与 `engage`。若不想让 Broker 自动分配，可设置 `AutomaticMediation = false` 或不调用这两个方法。
- **`forgetOpenRequest`**：取消某个未满足的请求。

### 查询类

- **`getExportersForService`**：返回提供指定服务的 Exporter/Worker 对象数组。
- **`getOfferedServices`**：返回 Broker 管理的全部服务（子表列出提供服务的 Exporter/Worker）。
- **`getOpenImporters`** / **`getSatisfiedImporters`**：返回未满足/已满足的 Importers 表格（第 1 列为对象，第 2 列为类型整数）。

## 只读属性（Read-Only Attributes）

Broker 的只读属性只能查询、不能设置（由 Plant Simulation 在查询时点即时计算）。常见示例：`MyBroker.OpenCapacity`。

## 交叉引用

各方法文档中的 **See also** 指向以下相关主题：

- Tab Statistics [Broker]、Service Statistics [Broker]、Offered Services [Broker]、Open Importers [Broker]
- Exporter Request Control [Broker]、Importer Request Control [Broker]
- `AutomaticMediation`（Worker / Exporter）、`SetUpOnlyWhenEmpty`、`doStandardImport`、`doStandardExport`
- `testImportFor`、`engage`、`localTestImportFor`、`globalTestImportFor`、`localOpenRequestsFor`、`globalOpenRequestsFor`
- Statistics report（Dwelling Time / Mediation Time）

## 相关文件

- `methods.md` — 完整方法文档（Markdown）
- `methods.txtx` — 同内容的原始导出文本
