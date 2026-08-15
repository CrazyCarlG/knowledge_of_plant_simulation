# Broker 属性（Attributes）— 摘要

本目录记录了 Plant Simulation 中 **Broker（中介/代理）** 对象的属性（Attributes）文档。内容来源于 `attributes.md`（`attributes.txtx` 为同内容的原始导出文本）。

## 概述

Broker 是资源对象，用于在 Importers（请求方）与 Exporters/Workers（提供方）之间中介服务（Service）。它提供了：

- 下列属性（见本文档表格）。
- 所有对象共有的属性（_Attributes of All Objects_）。
- 所有物流对象共有的属性（_Attributes of the Material Flow Objects_）。

属性既可以**设置**（通过对话框中的复选框、文本框、下拉列表，或直接赋值），也可以**读取**其值。

查看方式：在 Class Library 上下文菜单选择 **Show Attributes and Methods**，或在 Frame 中选中实例后按 **F8**（或 Home 选项卡上的 **Show Attributes and Methods**）。

## 语法约定

- 可设置属性：语法行形如 `<Path>.BrokerStatOn:boolean`，冒号后为可赋值的数据类型，用 `:=` 赋值，例如 `MyBroker.BrokerStatOn := true`。
- 只读属性：语法行形如 `<Path>.StatStayTimeMu → time`，箭头 `→` 后为返回值的数据类型，只能查询，例如 `print MyBroker.StatStayTimeMu`。

## 属性一览

| 属性 | 说明 | 数据类型 | 语法 |
| --- | --- | --- | --- |
| `StatStayTimeMu` | 返回 Exporter/Worker 在该 Broker 管理的单个 importer 处停留的平均时间（**只读属性**） | `time` | `<Path>.StatStayTimeMu → time` |
| `BrokerStatOn` | 激活（`true`）/ 停用（`false`）Broker 的统计收集 | `boolean` | `<Path>.BrokerStatOn:boolean` |
| `ChooseNearestWorker` | 让 Broker 优先选择步行距离最短的 Worker（`true`）或任意能胜任的 Worker（`false`） | `boolean` | `<Path>.ChooseNearestWorker:boolean` |
| `ExpRequestCtrl` | 指定 Exporter 请求控制 Method 对象 | `method` | `<Path>.ExpRequestCtrl:method` |
| `ImpRequestCtrl` | 指定 Importer 请求控制 Method 对象 | `method` | `<Path>.ImpRequestCtrl:method` |

## 属性详解

### 只读属性

- **`StatStayTimeMu`**：返回 Exporter/Worker 在单个 importer 处停留时间的**平均值**（medium duration）。该值属于停留时间（Stay Time / Dwelling Time）统计，需启用统计收集后才有意义。参见 `read-only-attributes` 目录中完整的只读属性清单（如 `StatStayTime`、`StatStayTimeDelta` 等）。

### 统计开关

- **`BrokerStatOn`**：激活或停用 Broker 的统计收集。激活后对应 Statistics 选项卡中的 **Broker Statistics** 复选框。停用时相关统计只读属性（`Stat*`）不更新。

### 派工偏好

- **`ChooseNearestWorker`**：设为 `true` 时，Broker 额外按"步行距离最短"准则挑选 Worker。Broker 接收导入请求时，按以下准则依次挑选 Worker：

  1. 最高优先级（Priority）
  2. 已位于请求工位的 Workplace 上
  3. 匹配 Scope
  4. （勾选后）步行距离最短的 Worker

  设为 `false` 时，Broker 选择任意能胜任该工作的 Worker，不论其当前位置。

  > 注意：勾选后 Plant Simulation 需为所有符合条件的 Worker 计算到工位的路径，可能拖慢仿真。

### 请求控制（Request Control）

- **`ExpRequestCtrl`**：指定一个 Method 对象。每当 Exporter/Worker 向其 Broker 注册为可用、可能被分配新 importer 时，Plant Simulation 调用该 Method。源码中需自行确保请求被处理（例如调用 `engage`），可用于将特定 importer 分配给 Exporter/Worker。
- **`ImpRequestCtrl`**：指定一个 Method 对象。每当 Broker 收到请求、或需再次处理请求（例如 Exporter/Worker 注册为可用）时，Plant Simulation 调用该 Method。源码中需自行确保请求被处理（例如调用 `engage`），可用于自定义分配策略。

  > 注意：对于 Broker 层级（多个 Broker 用 Connector 相连），Plant Simulation **不调用子 Broker 的控制**，只调用键入 importer 对象中的那个 Broker 的控制。

## 交叉引用

各属性文档中的 **See also** 指向以下相关主题：

- `engage`、`Exporter Request Control`、`Importer Request Control`
- `Broker Statistics`、`Statistics report`、`Tab Statistics [Broker]`
- `Choose the Nearest Worker`、`Priority`、`Objects`、`Workers to Create`、`How the Worker Decides Where to Work`
- `AGVPool`

相关 SimTalk 属性/方法：`BrokerStatOn`、`ChooseNearestWorker`、`ImpRequestCtrl`、`ExpRequestCtrl`、`StatStayTimeMu`、`brokerStat`、`serviceStat`。

## 相关文件

- `attributes.md` — 完整属性文档（Markdown）
- `attributes.txtx` — 同内容的原始导出文本
- `../read-only-attributes/README.md` — Broker 只读属性摘要（含 `StatStayTimeMu` 等）
- `../methods/README.md` — Broker 方法摘要（含 `engage`、`brokerStat`、`serviceStat` 等）
- `../general/README.md` — Broker 对象总览（含 Statistics 选项卡、派工机制等）
