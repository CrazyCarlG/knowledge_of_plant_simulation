# Exporter（通用说明）

本目录汇总了 `Exporter`（导出器/服务提供者）对象的通用文档，来源为 `general.md`。

## 概述

**Exporter** 对象用于提供和导出服务。它代表一群人，其中单个成员无法区分，也无法作为个体来寻址。它通常与 **Broker**（经纪人）和各类工位（Station、ParallelStation、AssemblyStation、DismantleStation）的 **Importer** 协同工作。

- 单个 Broker 管理 Exporter，并将其分配给某个 Importer。
- Exporter 完成服务后，会向 Broker 登记为可用，Broker 在需要时再将其分配给其他 Importer。
- 若 Importer 同时请求多个服务，则这些服务必须同时可用，Broker 才会分配给工位。
- 容量（Capacity）大于 1 的 Exporter 可同时为多个 Importer 提供服务。
- 若行驶/移动时间不重要，可使用 Exporter；如需区分单个成员，则应使用单独的 Exporter 或 Worker。

## 添加到仿真模型

点击 Home 功能区的 **Manage Class Library > Basic Objects > Resources > Exporter**。

## 属性选项卡（Tab Attributes）

| 属性 | 说明 | SimTalk |
|------|------|---------|
| Services | 导出器提供的服务名称列表 | `Services`、`hasService` |
| Fail Services | 失败时是否中断对应进程 | `FailServices` |
| Priority | 工作订单优先级，值越大越紧急，仅对同一 Broker 有效 | `Priority` |
| Capacity | 最大可导出服务数量，≥ 0 | `Capacity` |
| Broker | 分配服务的 Broker | `BrokerPath` |

## 失败选项卡（Tab Failures）

与通用失败配置一致（见 Tab Failures 文档）。

## 控件选项卡（Tab Controls）

- **Order Control**：Exporter 被分配给 Importer 时调用。参数 `Importer`（object）与 `Type`（integer，0=失败/移除失败、1=换型、2=加工、3=运输）。SimTalk：`OrderCtrl`
- **Release Control**：Importer 释放 Exporter/Worker 时调用，需自行通过 `findNewImporter` 重新分配。SimTalk：`ReleaseCtrl`
- **Shift Calendar**：指定排班日历，控制 Exporter 在哪些班次工作。SimTalk：`ShiftCalendarObject`

## 统计选项卡（Tab Statistics）

统计值按“服务”与“Exporter”两块展示，每块各项相加为 100%。主要统计项包括：

- 服务类：加工（Processing）、换型（Setting-up）、维修（Repairing）、等待（Waiting）、失败（Failed）
- Exporter 类：运行（Operational）、暂停（Paused）、未计划（Unplanned）、失败（Failed）
- 容量类：可用容量（Free Capacity）、已分配容量（Mediated Capacity）及其总和/最小值/最大值

勾选 **Exporter Statistics**（SimTalk：`ExpStatOn`）以收集 Exporter 统计数据。

## 用户定义选项卡 / 导航 / 视图 / 工具 / 帮助菜单

- **User-defined**：自定义属性。
- **View Menu**：Importers（显示所有 Importer 及其类型）、Exported Services（显示当前导出服务）、Associated Shift Calendar、Show Statistics Report（F6）等。
- **Tools Menu**：Available Control（`AvailableCtrl`）、Not Available Control（`NotAvailableCtrl`）、Edit Observers。

## Exporter 状态

| 状态 | 图形颜色 |
|------|----------|
| 失败 | 红色 |
| 正在导出服务 | 绿色 |
| 暂停 | 蓝色 |

## 方法

Exporter 提供目录中列出的方法以及所有对象的通用方法。

## SimTalk 属性速查

| 属性 | SimTalk 属性 |
|------|--------------|
| Services | `Services`、`hasService` |
| Fail Services | `FailServices` |
| Priority | `Priority` |
| Capacity | `Capacity` |
| Broker | `BrokerPath` |
| Order Control | `OrderCtrl` |
| Release Control | `ReleaseCtrl` |
| Shift Calendar | `ShiftCalendarObject` |
| Exporter Statistics | `ExpStatOn` |
| Available Control | `AvailableCtrl` |
| Not Available Control | `NotAvailableCtrl` |

*来源：Plant Simulation Help — Unpublished work. © 2026 Siemens*
