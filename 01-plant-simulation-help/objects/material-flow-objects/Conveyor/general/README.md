# Conveyor（输送机）— 概述

本目录的 `general.md` 是 Conveyor（输送机）对象的总体帮助文档，介绍其概念、工作原理、对话框及各选项卡设置。本文档为 `general.md` 的摘要，并附带指向同层级 SimTalk 参考文档（`attributes`、`methods`、`read-only-attributes`）的链接。

## 对象简介

Conveyor 是**长度导向（length-oriented）**的物料流对象，与点导向对象（如 Source、Station）不同，它在仿真中实际使用你输入的 **Length（长度）** 参与计算。

核心行为：

- 以**恒定速度**沿整个长度输送 MU。
- MU 不能超越其前方移动中的 MU。
- 未设置 Exit Control 时，Conveyor 将 MU 均等分配到所有连接的后继对象。
- **Accumulating（累积）** 复选框决定：当前方 MU 无法离开时，后续 MU 是前移并首尾相接，还是保持相互间距。

## MU 的移动方式

| 转换类型 | 行为 |
|----------|------|
| 点导向对象 → 长度导向对象 | MU 的前端移动到 Conveyor 起点；若两对象未紧邻放置，MU 会看似悬空。 |
| 长度导向对象 → 长度导向对象 | MU 持续前进，只有前端进入后继，其余部分按 Speed 跟随；速度不同时采用 MU 定位点所在 Conveyor 的速度。 |
| 长度导向对象 → 点导向对象 | MU 整体瞬间移入目标对象，而非仅前端。 |

**MU Distance（MU 间距）** 定义 Conveyor 上 MU 之间的距离（前一 MU 末端到下一 MU 前端）。无后续 MU 到达时 Conveyor 停止，新 MU 到达后再启动。默认值 `-1` 表示不使用 MU 间距。

**插入方式：** Conveyor 默认作为**曲线对象（curved object）**插入，可通过曲线段与直线段组合逼真建模曲线输送系统。在 **Appearance** 选项卡可选择不同外观配置。按 `M` 键或点击 Edit 功能区的 **Show Manipulators** 可调整图形长度与锚点。

**添加到模型：** Home 功能区 → **Manage Class Library > Basic Objects > MaterialFlow > Conveyor**。

## 对话框与选项卡

双击 Conveyor 图标打开对话框，可编辑仿真属性与动画属性（3D）。

### Tab Attributes（属性选项卡）

主要设置项：

- **Length** — 输送机长度。长度与 MU 长度共同决定可容纳的 MU 数量；改变长度会自动重算 Time。`SimTalk: Length`
- **Width** — 宽度。`SimTalk: Width`
- **Speed** — 最终速度；可输入 `-1` 表示无限速度；与 Time 联动。`SimTalk: Speed`
- **Time** — MU 通过空输送机全程所需时间；仅在取消 Acceleration 时可输入。`SimTalk: Time`
- **Accumulating** — 出口阻塞时 MU 是否首尾相接累积；取消则 MU 保持间距且阻塞时整体停止。`SimTalk: Accumulating`
- **Backwards** — 反向运行，MU 从出口进入、入口离开。`SimTalk: Backwards`
- **Acceleration（复选框）** — 启用加速/减速；启用后需输入 Acceleration 与 Deceleration，并显示 Current Speed。`SimTalk: AccelerationEnabled`
- **Current Speed** — 当前速度（启用 Acceleration 时显示，可监视）。`SimTalk: CurrentSpeed`
- **Acceleration（文本框）** — 加速值（m/s²，≥ 0）。`SimTalk: Acceleration`
- **Deceleration（文本框）** — 减速值（≥ 0）。`SimTalk: Deceleration`
- **Capacity** — 同一时刻可容纳的 MU 数量上限；`-1` 为无限容量。`SimTalk: Capacity`
- **MU Distance Type** — 间距类型：`Gap`、`Pitch`、`Minimum Gap`、`Minimum Pitch`、`Multiple Gap`、`Multiple Pitch`。`SimTalk: MUDistanceType`
- **MU Distance** — 间距数值；默认 `-1` 表示不使用间距。`SimTalk: MUDistance`
- **Enforce MU Distance** — 累积时仍强制保持间距（仅累积且正向时生效）。`SimTalk: EnforceMUDistance`
- **Automatic Stop** — 不输送 MU 时自动将当前速度置 0。`SimTalk: AutomaticStop`

### 其他选项卡

- **Tab Times** — 定义时间分布（可用 `setTypeAndAttr` 设置分布类型与参数）。
- **Tab Failures** — 定义故障。
- **Tab Controls** — 修改内置行为；可创建 Entrance / Exit / Backward Entrance / Backward Exit / Speed / Pull 等控制、Shift Calendar 及 Sensors。
- **Speed Control** — 仅在启用 Acceleration 后可设置；在加速/减速达到最终速度或减速停止时被调用。
- **Tab Exit** — 选择 MU 移向的后继对象。
- **Tab Statistics** — 累积型输送机额外显示 **Exit blocked**；Conveyor 当前速度非 0 时处于 Working 状态。
- **Tab Importer** — 配置 Worker 如何取走/送入已输送的零件。
- **Tab Energy** — 能量设置。
- **Tab Costs** — 成本设置；输送成本按零件长度比例分摊（投资成本仅在折旧期内累计）。
- **Tab User-defined** — 用户自定义属性。

### 菜单

- **Navigate / View / Tools / Help Menu** — 通用命令。
- **Tabs Menu** — 显示或隐藏选项卡以加快对话框打开速度。

## 方法、属性与只读属性

Conveyor 提供：
- 曲线对象（Curved Objects）的方法；
- 物料流对象（Material Flow Objects）的方法/属性/只读属性；
- 所有对象（All Objects）的方法/属性/只读属性。

按 `F8` 或点击 **Show Attributes and Methods** 可查看对象的全部方法、只读属性与属性。

## 相关文档（同层级 SimTalk 参考）

- [Attributes（属性参考）](../attributes/attributes.md) — SimTalk 属性详解，含 `OccupiedLength`、`Acceleration`、`Accumulating`、`Capacity`、`CurrentSpeed`、`Deceleration`、`Length`、`MUDistance`、`MUDistanceType`、`Speed`、`SpeedCtrl`、`Time` 等，附快速对照表。
- [Methods（方法）](../methods/methods.md) — 方法概述及语法行约定。
- [Read-Only Attributes（只读属性）](../read-only-attributes/read-only-attributes.md) — `CurrentAcceleration`、`OccupiedLength` 等只读属性。
