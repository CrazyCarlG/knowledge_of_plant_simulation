# Broker 只读属性（Read-Only Attributes）— 摘要

本目录记录了 Plant Simulation 中 **Broker（中介/代理）** 对象的全部只读属性（Read-Only Attributes）。内容来源于 `read-only-attributes.md`（`read-only-attributes.txtx` 为同内容的原始导出文本）。

## 概述

Broker 是资源对象，用于在 Importers（请求方）与 Exporters/Workers（提供方）之间中介服务（Service）。它提供了：

- 下列只读属性（见本文档表格）。
- 所有对象共有的只读属性（_Read-Only Attributes of All Objects）。

只读属性只能查询、不能设置，其值由 Plant Simulation 在查询的时间点即时计算。多数只读属性对应对象某选项卡（如 Statistics 选项卡）上一个不可编辑的对话框项。

查看方式：在 Class Library 上下文菜单选择 **Show Attributes and Methods**，或在 Frame 中选中实例后按 **F8**。

## 语法约定

只读属性语法行形如 `<Path>.OpenCapacity → integer`：

- `<Path>` 表示属性所应用对象的路径。
- 箭头 `→` 后为返回值的数据类型。
- 示例统一使用 `print MyBroker.<属性名>` 查询并打印值。

## 只读属性一览

| 只读属性 | 说明 | 返回类型 |
| --- | --- | --- |
| `AdministeredExporters` | 返回直接注册到该 Broker 的 Exporter/Worker 数组（不含经 Broker 层级可达的） | `array` |
| `MediatedCapacity` | 返回该 Broker 已中介（brokered）的容量 | `integer` |
| `OpenCapacity` | 返回该 Broker 未能满足的开放容量总量 | `integer` |
| `OpenRequests` | 返回该 Broker 当前管理的开放请求实际数量 | `integer` |
| `SatisfiedRequests` | 返回该 Broker 已满足的请求数量 | `integer` |
| `StatMediatedCapacity` | 返回该 Broker 管理的中介容量累计总量 | `integer` |
| `StatMediationTime` | 返回该 Broker 满足所有已满足请求所需的时间总和 | `time` |
| `StatMediationTimeDelta` | 返回该 Broker 满足所有请求所需中介时间的标准差 | `time` |
| `StatMediationTimeMu` | 返回该 Broker 满足单个请求所需的平均时间 | `time` |
| `StatOpenCapacity` | 返回该 Broker 管理的开放容量累计总量 | `integer` |
| `StatOpenRequests` | 返回该 Broker 管理的开放请求累计总数 | `integer` |
| `StatSatisfiedRequests` | 返回该 Broker 已满足的请求累计总数 | `integer` |
| `StatStayTime` | 返回 Exporter/Worker 在 importer 处停留的时间总和 | `time` |
| `StatStayTimeDelta` | 返回 Exporter/Worker 在该 Broker 管理的 importer 处停留时间的标准差 | `time` |
| `StatStayTimeMu` | 返回 Exporter/Worker 在该 Broker 管理的单个 importer 处停留的平均时间 | `time` |

## 属性分类

### 当前值 vs. 累计值（Stat\*）

- 不带 `Stat` 前缀的属性返回**当前/即时**状态：
  - `MediatedCapacity`、`OpenCapacity`、`OpenRequests`、`SatisfiedRequests`
- 带 `Stat` 前缀的属性返回**累计统计**值（需启用统计收集，对应 Statistics 选项卡）：
  - `StatMediatedCapacity`、`StatOpenCapacity`、`StatOpenRequests`、`StatSatisfiedRequests`

### 中介时间（Mediation Time）

- `StatMediationTime`：满足所有已满足请求所需时间的总和（即 importer 等待服务的时间）。
- `StatMediationTimeMu`：满足单个请求的平均时间。
- `StatMediationTimeDelta`：中介时间的标准差。

### 停留时间（Stay Time / Dwelling Time）

- `StatStayTime`：Exporter/Worker 在 importer 处停留的时间总和（即被中介服务持续的时间）。
- `StatStayTimeMu`：单次停留的平均时间。
- `StatStayTimeDelta`：停留时间的标准差。

## 典型查询

```simtalk
print MyBroker.OpenCapacity
print MyBroker.AdministeredExporters
var t : object[] := MyBroker.AdministeredExporters
```

## 交叉引用

各只读属性文档中的 **See also** 指向以下相关主题：

- `Tab Statistics [Broker]`、`Statistics report, Broker Statistics [described]`
- 对应方法/概念：`brokerStat`、`serviceStat`、`getOpenImporters`、`getSatisfiedImporters`、`getOfferedServices`
- 各属性自身的 SimTalk 主题（如 `OpenCapacity [SimTalk]`、`StatStayTimeMu [SimTalk]` 等）

## 相关文件

- `read-only-attributes.md` — 完整只读属性文档（Markdown）
- `read-only-attributes.txtx` — 同内容的原始导出文本
