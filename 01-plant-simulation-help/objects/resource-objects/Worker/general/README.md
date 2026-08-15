# Worker（工人）对象 — 内容摘要

> 本文件为 `general.md` 的摘要，概述 Plant Simulation 中 **Worker** 对象的功能、属性与用法。

## 概述

**Worker** 用于在工作站（Station）的 **Workplace（工位）** 上执行作业。它实现了 Worker–WorkerPool–Workplace–FootPath 的概念，是对 Broker–Importer–Exporter 概念的细化。

与 Exporter 的区别：Worker 在走向工位执行作业时会**消耗时间**。Worker 拥有与 Exporter 相同的统计值，并额外提供"前往作业途中（En-route to the Job）"的统计值。

## 核心机制

- Worker 在 **WorkerPool** 中创建，空闲时留在 WorkerPool 等待工作订单。
- 通常在 **Workers to Create** 表中输入 Worker 名称，或从 Class Library 拖入 WorkerPool。
- 也可用 `create` 方法创建单个 Worker（仅限 WorkerPool，且只对单次仿真运行有效，Reset 后删除）。
- **Broker** 负责将 Worker 派发到请求服务的工作站。

## 三种行进模式（Travel Mode）

| 模式 | 说明 |
|---|---|
| **Move freely within area** | 工人在模型区域内自由行走，自动绕开障碍物（墙壁、支柱、机器等）。Plant Simulation 自动计算最短路线，障碍物会被识别为 Barred Areas。 |
| **Walk along footpaths** | 工人在插入的 FootPath 上行走。可用 Connector 连接多条 FootPath 组成网络。 |
| **Beam to workplace** | 工人被"传送"到被派发的工作位，瞬时完成、不消耗时间（此时相当于容量为 1 的 Exporter）。 |

SimTalk 属性：`WorkersTravelMode`、`teleportTo`、`teleportToHome`、`teleportToPool`。

## 派工决策（Broker 与 Worker 的协商顺序）

1. Broker 先检查请求的 **Priority（优先级）**；
2. Worker 检查目标对象是否属于其 **Scope**；
3. Broker 检查是否选中 **Choose the Nearest Worker**；
4. 若 Worker 优先级最高、Scope 匹配、路线最短，则被派往该 Workplace。

## 搬运零件（Carrying Parts）

Worker 可在工位之间搬运零件，需要：取件站与目标站各有一个 Workplace、一个 Broker 和一个 WorkerPool。搬运容量由 X/Y/Z 维度决定（容量 = X × Y × Z，最大一百万）。

## 主要属性（Tab Attributes）

- **Stopped**：勾选后停止行进中的 Worker。
- **Priority**：工作订单紧急程度（整数，越大越紧急）。
- **Efficiency**：工作效率百分比（100% = 标准时间，200% = 一半时间，50% = 两倍时间）。
- **Speed**：在 FootPath 或区域内的行走速度。
- **X-/Y-/Z-Dimension**：各方向可携带零件数。
- **Shift**：Worker 所属班次。
- **Services**：Worker 提供的服务列表（按顺序尝试提供）。
- **Broker**：指派服务的 Broker 对象。
- **Home Location**：Worker 完成作业后返回的工位。

## 其他选项卡

- **Tab Failures**：定义故障。
- **Tab Scope**：指定 Worker 可被派往的对象范围。
- **Tab Controls**：提供 **Order Control**（`OrderCtrl`）与 **Release Control**（`ReleaseCtrl`）两个控制方法，用于定制派单与释放行为。
- **Tab Statistics**：展示服务（设置/加工/维修/运输/途中/等待/故障）及 Exporter/Worker 各状态占比、行进距离等统计（需勾选 **Exporter Statistics**）。
- **Tab User-defined**：自定义属性。

## 菜单与视图

- **Navigate Menu**：导航命令。
- **View Menu**：Contents（携带的 MU 列表）、Position、Importers、Exported Services、Route to Destination 等。
- **Tools Menu**：Edit Controls、Edit Observers，并提供 **Available** 与 **Not-available** 控制。

## 状态显示

- **Horizontal**：沿图片底部水平排列显示状态。
- **Color**：用颜色填充整个 Worker 图片。

## 方法

Worker 提供目录中列出的方法、Exporter 的方法（Worker 本质是容量为 1 的 Exporter）以及所有对象的通用方法。若未使用 FootPath，Plant Simulation 会将 Worker 传送到工位。

## 相关主题

- Broker 如何向 Worker 派发作业
- 建模工人及其作业
- 建模在工位间搬运零件的 Worker
- Worker 的最短路线、派工决策与搬运机制
- 工人在工位前排队
- 在图表中显示 Worker 统计信息
- Worker 如何在工厂内行进
- 视频：https://youtu.be/HiPziA8kxc0?si=QnyvMaEQeVyaDoHo
