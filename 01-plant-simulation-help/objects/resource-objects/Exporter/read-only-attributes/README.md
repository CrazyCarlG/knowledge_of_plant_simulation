# Exporter 只读属性（Read-Only Attributes）总结

本目录汇总了 Exporter（导出器）对象的只读属性文档，来源于 `read-only-attributes.md`。内容说明 Exporter 提供的只读属性及其用途。

## 概述

Exporter 提供两类只读属性：

- 本目录左侧目录中列出的只读属性；
- 所有对象共有的只读属性（`_Read-Only Attributes of All Objects`）。

只读属性只能查询、不能设置，因为 Plant Simulation 在查询时刻才计算其值。大多数只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可编辑的对话框条目。

可通过打开 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选 Class 的方法、只读属性和属性；
- 在插入实例的 Frame 的 Home 功能区按 F8 键或点击 **Show Attributes and Methods**，查看所选实例的方法、只读属性和属性。

查询只读属性示例：

```simtalk
print .Resources.myExporter:2.AvailableForMediation
```

## 只读属性分类总览

Exporter 的只读属性可分为以下几类：

| 类别 | 说明 |
| --- | --- |
| 服务支持 | `hasService`（方法） |
| 可用性与容量（当前值） | `AvailableForMediation`、`FreeCapacity`、`MediatedCapacity` |
| Exporter 状态统计 | `StatExporter*` 系列（Failed / Operational / Paused / Unplanned） |
| 容量统计（最大/最小/累计） | `StatMax*`、`StatMin*`、`StatSum*` 系列 |
| 服务统计 | `StatServices*` 系列（Failed / Repairing / Setup / Waiting / Working） |

## 服务支持

### hasService（方法）

返回由 `<Path>` 指定的 Exporter/Worker 是否支持指定服务（`true`/`false`）。

- **类型：** Method
- **语法：** `<Path>.hasService(ServiceName:string) → boolean`
- **参数：** `ServiceName`（string）—— 服务名称
- **返回值：** boolean

```simtalk
MyExporter.hasService("drill")
```

## 可用性与容量（当前值）

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `AvailableForMediation` | boolean（可监视 watchable） | Exporter 是否可被中介（broker）。未失败、未暂停且仍有可用容量时为 `true`。 |
| `FreeCapacity` | integer | 当前可提供的容量。 |
| `MediatedCapacity` | integer | 当前被中介（brokered）的容量。 |

## Exporter 状态统计（StatExporter* 系列）

按状态维度统计 Exporter 的运行情况，各状态包含 Count（次数）、Delta（标准差）、Mu（均值）、Portion（占比）、Time（总时间）等子属性。

### 失败（Failed）状态

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatExporterFailedCount` | integer | 失败次数。 |
| `StatExporterFailedDelta` | time | 失败时间的标准差。 |
| `StatExporterFailedMu` | time | 平均失败持续时间。 |
| `StatExporterFailedPortion` | real | 失败时间占统计周期的比例。 |
| `StatExporterFailedTime` | time | 失败总时间。 |

### 工作（Operational）状态

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatExporterOperationalPortion` | real | 工作时间占统计周期的比例。 |
| `StatExporterOperationalTime` | time | 工作过程所占的总时间。 |

> **注意：** Exporter 仅计算 *working* 状态相关的值，因此只提供 `StatExporterOperationalPortion` 和 `StatExporterOperationalTime` 两个只读属性。

### 暂停（Paused）状态

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatExporterPausedCount` | integer | 暂停次数。 |
| `StatExporterPausedDelta` | time | 暂停时间的标准差。 |
| `StatExporterPausedMu` | time | 平均暂停持续时间。 |
| `StatExporterPausedPortion` | real | 暂停时间占统计周期的比例。 |
| `StatExporterPausedTime` | time | 暂停总时间。 |

### 未计划（Unplanned）状态

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatExporterUnplannedCount` | integer | 未计划工作的次数。 |
| `StatExporterUnplannedDelta` | time | 未计划时间的标准差。 |
| `StatExporterUnplannedMu` | time | 平均未计划持续时间。 |
| `StatExporterUnplannedPortion` | real | 未计划时间占统计周期的比例。 |
| `StatExporterUnplannedTime` | time | 未计划总时间。 |

## 容量统计（最大/最小/累计）

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatMaxFreeCapacity` | integer | 可提供的最大容量。 |
| `StatMaxMediatedCapacity` | integer | 最大被占用（brokered）容量。 |
| `StatMinFreeCapacity` | integer | 可提供的最小容量。 |
| `StatMinMediatedCapacity` | integer | 最小被占用容量。 |
| `StatSumFreeCapacity` | integer | 空闲容量之和。 |
| `StatSumMediatedCapacity` | integer | 被中介容量之和。 |

## 服务统计（StatServices* 系列）

按服务维度统计，各状态包含 Count（次数）、Portion（占比，按容量加权）、Time（总时间）等子属性。

> **通用备注：** 服务统计中的 "overall statistics time"（总体统计时间）指统计周期减去 Unplanned Time 和 Paused Time 之后的时间。
>
> **关于 `FailServices`：** 只有激活 `FailServices` 后，Exporter 才会收集服务的失败时间。

### 失败（Failed）服务

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatServicesFailedCount` | integer | 服务失败次数（需激活 `FailServices`）。 |
| `StatServicesFailedPortion` | real | 服务失败时间占总体统计时间的比例，按容量加权（需激活 `FailServices`）。 |
| `StatServicesFailedTime` | time | 服务失败总时间（需激活 `FailServices`）。 |

### 维修（Repairing）服务

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatServicesRepairingCount` | integer | 服务进行维修的次数。 |
| `StatServicesRepairingPortion` | real | 服务维修时间占总体统计时间的比例，按容量加权。 |
| `StatServicesRepairingTime` | time | 服务维修总时间。 |

### 设置（Setup）服务

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatServicesSetupCount` | integer | 服务进行站点设置（setting up）的次数。 |
| `StatServicesSetupPortion` | real | 服务设置时间占总体统计时间的比例，按容量加权。 |
| `StatServicesSetupTime` | time | 服务设置总时间。 |

> **注意：** 若站点变为 failed 和/或 unplanned 或 paused 状态，且随后有设置或处理服务被中介，这些服务仍保持被中介状态，设置时间与处理时间在站点失败期间仍继续累计。为避免此情况，可激活 `FailServices`。

### 等待（Waiting）服务

等待相关属性分为"等待 importer"与"等待 MU"两类，以及二者之和。

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatServicesWaitingImpCount` | integer | 服务等待 importer 的次数。 |
| `StatServicesWaitingImpPortion` | real | 服务等待 importer 的时间占总体统计时间的比例，按容量加权。 |
| `StatServicesWaitingImpTime` | time | 服务等待 importer 的总时间。 |
| `StatServicesWaitingMUCount` | integer | 服务在 importer 处等待 MU 的次数。 |
| `StatServicesWaitingMUPortion` | real | 服务在 importer 处等待 MU 的时间占总体统计时间的比例，按容量加权。 |
| `StatServicesWaitingMUTime` | time | 服务在 importer 处等待 MU 的总时间。 |
| `StatServicesWaitingPortion` | real | 服务等待总占比（= `StatServicesWaitingImpPortion` + `StatServicesWaitingMUPortion`）。 |
| `StatServicesWaitingTime` | time | 服务等待总时间（= `StatServicesWaitingImpTime` + `StatServicesWaitingMUTime`）。 |

### 工作（Working）服务

| 属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `StatServicesWorkingCount` | integer | 服务提供的工作过程次数。 |
| `StatServicesWorkingPortion` | real | 服务工作时间占总体统计时间的比例，按容量加权。 |
| `StatServicesWorkingTime` | time | 服务工作过程所占的总时间。 |

> **注意：** 若站点变为 failed 和/或 unplanned 或 paused 状态，且随后有设置或处理服务被中介，这些服务仍保持被中介状态，设置时间与处理时间在站点失败期间仍继续累计。为避免此情况，可激活 `FailServices`。

## 相关参考

- `Tab Statistics [Exporter]` — Exporter 的 Statistics 选项卡
- `Tab Statistics [Worker]` — Worker 的 Statistics 选项卡
- `Statistics report — Service Statistics — States — Capacities and States of the Exporters`
- `Statistics report — Service Statistics — States — Time Portions of the Exporters`
- `Services [Exporter]` / `Exported Services [Exporter]` / `Exported Services [Worker]`
- `FailServices [SimTalk]`
