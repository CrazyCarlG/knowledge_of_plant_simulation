# Read-Only Attributes of the Drain — Summary

本目录汇总了 **Drain**（排空/移除站）对象的只读属性（read-only attributes）。这些属性用于查询被 Drain 从工厂中移除的 MU（物流单元）在其生命周期中经历的各种统计信息，只能读取、不能赋值——Plant Simulation 会在查询时刻实时计算其值。

> 说明：本目录下目前仅有一个内容文件 `read-only-attributes.md`，无子文件夹。以下为对其内容的总结。

## 概述

- 只读属性只能查询，不能设置；其值在查询时刻由 Plant Simulation 计算得出。
- 多数只读属性对应对象某个选项卡（例如 **Statistics**）上不可编辑的对话框项。
- 可通过 **Show Attributes and Methods** 窗口查看对象全部的方法、只读属性与属性（Class Library 右键菜单，或按 **F8** / Home 选项卡按钮）。
- 查询示例：`print Drain.StatAvgExitInterval`

## 属性总览

| 属性 | 返回类型 | 说明 |
|-----------|-------------|-------------|
| `StatAvgExitInterval` | time | 被移除 MU 之间的平均离开时间间隔 |
| `StatAvgLifeSpan` | time | 被移除 MU 的平均生命周期 |
| `StatDeleted` | integer | 从工厂中移除的 MU 数量 |
| `StatProdFailPortion` | real | 在故障的 Production 资源上停留的生命时间占比 |
| `StatProdPausingPortion` | real | 在暂停/非计划的 Production 资源上停留的生命时间占比 |
| `StatProdSetupPortion` | real | 在换装的 Production 资源上停留的生命时间占比 |
| `StatProdStoppedPortion` | real | 在被 LockoutZone 停止的 Production 资源上的时间占比 |
| `StatProdWaitingPortion` | real | 在等待的 Production 资源上停留的生命时间占比 |
| `StatProdWorkingPortion` | real | 在工作中的 Production 资源上停留的生命时间占比 |
| `StatStoreFailPortion` | real | 在故障的 Storage 资源上停留的生命时间占比 |
| `StatStorePausingPortion` | real | 在暂停/非计划的 Storage 资源上停留的生命时间占比 |
| `StatStoreSetUpPortion` | real | 在换装的 Storage 资源上停留的生命时间占比 |
| `StatStoreStoppedPortion` | real | 在被 LockoutZone 停止的 Store 资源上的时间占比 |
| `StatStoreWaitingPortion` | real | 在等待的 Storage 资源上停留的生命时间占比 |
| `StatStoreWorkingPortion` | real | 在工作中的 Storage 资源上停留的生命时间占比 |
| `StatThroughputPerDay` | real | 每天移除的 MU 数（每小时吞吐量 × 24） |
| `StatThroughputPerHour` | real | 每小时移除的 MU 数 |
| `StatThroughputPerMinute` | real | 每分钟移除的 MU 数 |
| `StatTranspFailPortion` | real | 在故障的 Transport 资源上停留的生命时间占比 |
| `StatTranspPausingPortion` | real | 在暂停/非计划的 Transport 资源上停留的生命时间占比 |
| `StatTranspSetupPortion` | real | 在换装的 Transport 资源上停留的生命时间占比 |
| `StatTranspStoppedPortion` | real | 在被 LockoutZone 停止的 Transport 资源上的时间占比 |
| `StatTranspWaitingPortion` | real | 在等待的 Transport 资源上停留的生命时间占比 |
| `StatTranspWorkingPortion` | real | 在工作中的 Transport 资源上停留的生命时间占比 |

## 属性分类说明

这些属性按所统计的资源类型可分为四组：

1. **核心统计**（`StatAvgExitInterval`、`StatAvgLifeSpan`、`StatDeleted`）：描述被移除 MU 的整体数量、平均生命周期与平均离开间隔。
2. **吞吐量**（`StatThroughputPerMinute/Hour/Day`）：描述 Drain 在可用观察时间内的移除速率，吞吐量以升（liters）为单位。
3. **Production 资源占比**（`StatProd*`）：MU 生命周期中停留在各种状态的 Production（生产类）资源上的时间占比。
4. **Storage 资源占比**（`StatStore*`）：MU 生命周期中停留在各种状态的 Storage（存储类）资源上的时间占比。
5. **Transport 资源占比**（`StatTransp*`）：MU 生命周期中停留在各种状态的 Transport（运输类）资源上的时间占比。

每组内的状态类别一致，包括：`Fail`（故障）、`Pausing`（暂停/非计划）、`Setup`（换装）、`Stopped`（被 LockoutZone 停止）、`Waiting`（等待）、`Working`（工作）。

## 语法与类型

- 所有属性均通过 `<Path>.<AttributeName>` 语法访问，例如 `MyDrain.StatDeleted`。
- 返回类型分别为 `time`、`integer` 或 `real`（见上表）。
- 注意：部分属性的文档语法名与属性名存在拼写差异，例如 `StatProdSetupPortion` 的语法写作 `StatProdSetUpPortion`、`StatTranspSetupPortion` 的语法写作 `StatTranspSetUpPortion`（`Up` 大小写不同）。

## 相关引用

`read-only-attributes.md` 末尾还指出，Drain 还额外提供：

- 属性 `TypeStatOn` [SimTalk]。
- **Station** 的属性（Attributes of the Station）。
- **All Objects** 的属性（Attributes of All Objects）。
- **Material Flow Objects** 的属性（Attributes of the Material Flow Objects）。

## 文件说明

- `read-only-attributes.md`：Drain 只读属性的完整说明（本目录核心内容）。
- `read-only-attributes.txtx`：上述内容的原始导出/源文本（Siemens Plant Simulation Help 导出，含分页与 "See also" 交叉引用）。
