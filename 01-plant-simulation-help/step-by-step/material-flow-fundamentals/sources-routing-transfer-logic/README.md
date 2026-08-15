# Sources, Routing, and Transfer Logic

本目录汇总了 Plant Simulation 帮助文档中关于**物料流建模基础（Modeling the Flow of Materials — Basics）**的内容，主题聚焦于：如何使用 `Source` 创建零件、如何用加工站（Station）处理零件、如何在站与站之间路由/转移零件，以及如何用 `Drain` 移除零件。

> 目录内文件：
> - `sources-routing-transfer-logic.md` —— 本主题的结构化总结（主要来源）
> - `sources-routing-transfer-logic.txtx` —— Plant Simulation Help 原始文本（含分页标记与导航）

---

## 1. 内容概览

物料流建模基础涵盖以下要点：

- 用 `Source` 创建/引入零件。
- 设定 `Station` 处理零件的时长。
- 将 `Station` 设置为可处理另一种零件类型。
- 在加工站之间转移零件。
- 建模加工站的故障与故障时间。
- 用 `Drain` 移除已加工零件。

---

## 2. 主动对象与被动对象（Active and Passive Objects）

移动与固定物料流对象是仿真模型的基本构件。

- **移动对象（MUs）**：`Part`、`Container`、`Transporter`，代表在工厂中流动的实体或逻辑零件，需要主动/被动对象来加工和运输。
- **源与汇**：`Source` 在物料流起点创建 MU；`Drain` 在加工完成后移除 MU；`FluidSource` / `FluidDrain` 分别对应流体的创建与移除。
- **主动物料流对象**：`Drain, Station, ParallelStation, AssemblyStation, DismantleStation, Conveyor, Sorter, PlaceBuffer, Buffer`。它们接收 MU、加工一段时间，再沿 `Connector` 连接、按 **push-block 原则**主动转移 MU。它们代表工厂中的工位（车床、钻床等），区别在于同时可加工 MU 的数量（单个/多个）和加工方式（串行/并行）。`Conveyor` 以设定速度、在设定距离上输送 MU。
- **主动流体对象**：`FluidDrain, Tank, Mixer, Portioner, DePortioner`，同样按 push-block 原则转移流体。
- **被动物料流对象**：`Store, Track, TwoLaneTrack` 不自动转移 MU。MU 保留在 `Store` 中直到被（如 Method）移除；`Track`/`TwoLaneTrack` 与 `Transporter` 配合使用；用 `FlowControl` 建模分流与合流策略。
- **被动流体对象**：`Pipe`、`PatchMatrix`。
- **主动 MU**（可自行移动）：`Transporter`（自驱动）、`Worker`（人）。
- **被动 MU**（被运输/加工）：`Part`（工件）、`Container`（容器/托盘）。
- **面向点对象**：MU 位于固定加工位，其长度/尺寸与 MU 长度/尺寸对仿真无关（`Source, Drain, Station, ... PatchMatrix`）。
- **面向长度对象**：其长度/尺寸参与仿真（`Conveyor, Track, TwoLaneTrack, FootPath, Pipe, Container, Transporter`）；3D 中称为 extrusion objects。特殊对象：`Turntable`（单段直线）、`Turnplate`（设定直径的直线段）、`AngularConverter`（两段直线）、`Converter`（单段直线）。

---

## 3. 用 Source 生产零件

- `Source` 创建 MU，`Drain` 移除零件（如发货部门）。
- 可从类库 `MaterialFlow` 文件夹或 Toolbox 的 `Material Flow` 工具栏插入。

### 3.1 无法生产时的行为（Blocking）
通过 `Operating Mode > Blocking` 控制：
- **勾选 Blocking**：Source 记住本应生产但未生产的时间点，在下一个可行时刻补产。
- **取消 Blocking**：仅在设定的创建时间生产，不补产。

### 3.2 按 Delivery Table 生产
- 用 `Time of Creation > Delivery Table`，选择/拖入投递表。
- Delivery Table 五列：`Delivery Time`（生产时刻）、`MU`（MU 类）、`Number`（数量）、`Name`（名称）、`Attributes`（属性子表名）。
- 规则：`Delivery Time` 与 `MU` 必填；缺省 Number 产 1 个；缺省 Name 用类名；Number 为 0 时该周期不产件但不跳过；`Delivery Time` 可用 `time/date/dateTime/real` 类型。

### 3.3 按自定义区间生产
- `Time of Creation > Interval Adjustable`：`Start` 产第一件，每隔 `Interval` 产下一件，到 `Stop` 停止（0 = 无限制）。
- `MU Selection` 选项：
  - `Constant`：只产一种类型。
  - `Sequence Cyclical`：按表循环生产固定序列；可勾选 `Generate as Batch` 整批生产。
  - `Sequence`：按表一次性生产（`Number Adjustable` 时不可用）。
  - `Random`：按数据表频率随机生产。
  - `Percentage`：按数据表百分比生产。

### 3.4 按数量生产
- `Time of Creation > Number Adjustable`：设定 `Amount`，选择 `Creation Times` 分布。
- 不能配合 `MU Selection > Sequence`；SimTalk 用属性 `Interval` 设置创建时间。

### 3.5 用 Trigger 对象生产
- `Time of Creation > Trigger`，勾选 `Inheritance`，拖入 Trigger。
- 在 Trigger 中设 `Active Interval`、`Period Length`，`Values` 标签选 `Trigger Type > Input`，在 `TimeSequence` 中输入时刻与值序列。
- 值格式：`amount,mu_Type,distributionType[,distribution parameters]`（不能含空格；`Const` 表示在左侧时刻生产，`Const` 后数字为秒级偏移）。

---

## 4. 用工作计划生产与加工零件（Work Plan）

工作计划（operations plan）按执行顺序列出生产步骤；成本中心与每步允许时间在 Process Designer 中处理。示例中每道工序由单一工位完成：

| 位置 | 工位 |
| --- | --- |
| 0 | Receiving（Source） |
| 1 | Milling |
| 2 | Drilling_A 或 Drilling_B |
| 3 | Packing |

建模步骤：
1. **创建加工站**：从 `Station` 派生类（Derive），移动到模型文件夹并重命名（如 `MyStation`），插入三次并重命名实例。
2. **在类中定义时间**：`Processing Time` 通过 Method `ProcessingTimeInFormula` 从 `root.myWorkPlan` 查询；`Set-up Time` 用公式 `root.MyWorkPlan["Operations",@.EntityType]["Setup time",Self]`。
3. **定义换型行为**：勾选 `Automatic`，`Set-up depends on` 选 `User-defined Attribute`，输入如 `EntityType`。
4. **指定 Exit Control** 名称。
5. **创建工作计划**：插入 `DataTable`，`Operations` 列数据类型设为 `Table`，列索引为 `Object`、后两列为 `Time`；输入标识符生成子表，填写工序/工位、换型时间与加工时间。
6. **用 Source + 序列表生产零件**：`MU Selection > Sequence Cyclical`，为零件定义用户属性 `PartType` 与 `PositionInWorkPlan`（0=Source，1=Milling，2=Drilling，3=Packing）。
7. **编写 Exit Control**：查找下一工位并移动零件，到终点时移向 `root.Shipping`。

---

## 5. 用 Drain 移除零件

`Drain` 用于在加工完成后将零件移出工厂（如发货部门）。它只有一个加工位，内置属性与 `Station` 相同；换型与加工后移除 MU（而非移到后继对象），并统计 MU。可从 `MaterialFlow` 文件夹或 `Material Flow` 工具栏插入。

---

## 6. 工位间转移零件

转移方式包括：标准转移行为（push-block）、Exit Strategy（退出策略）、`FlowControl` 分流、观察者（observer）、跨 Frame 的 Interface 退出策略、`TransferStation` 装卸。

### 6.1 零件移动方式（按对象类型）
- 点 → 点：MU 从 booking point 到 booking point 瞬时整体移动。
- 点 → 长：MU 前端移动到 Conveyor 起点。
- 长 → 长：MU 连续移动，仅前端前进、其余按 `Speed` 跟随；速度不同时取 MU `Booking Point Length` 所在 Conveyor 的速度。
- 长 → 点：MU 总是整体瞬时移动到对象上。

### 6.2 标准转移行为（push-block 原则）
- 对象加工完后主动把零件推给后继（push）；后继无法接收时触发 block，保证后继就绪时对象被重新激活。
- 默认策略为**循环、非阻塞**：MU 移到第一个非阻塞后继，循环查找直到回到上次搜索的后继。
- 阻塞机制：Part:2 意图移动到 Drilling_A，若 Drilling_A 无法接收，Part:2 进入 Drilling_A 等的 forward blocking list；Part:1 离开 Drilling_A 时，Drilling_A 为所有阻塞 MU 安排 Out 事件并清空列表。
- 处理时间类型：`Processing Time`、`Set-up Time`、`Recovery Time`、`Cycle Time`（不必全部定义），以及故障。

### 6.3 选择退出策略（Exit Strategy）
在 `Exit` 标签选择策略。主要策略：

| 策略 | 行为 |
| --- | --- |
| Cyclic | 循环移向下一个后继 |
| Cyclic Sequence | 按列表顺序循环移向后继（`ExitStrategySequence`） |
| Least Recent Demand | 移到等待最久的后继 |
| Linear Sequence | 按列表顺序线性（一次性）移向后继 |
| Maximum Contents | 移到 MU 数量最多的后继 |
| Maximum Number In | 移到接收 MU 最多的后继 |
| Maximum Processing Time | 移到加工时间最长的后继 |
| Maximum Relative Occupation | 移到相对占用率最高的后继 |
| Maximum Set-up Time | 移到换型时间最长的后继 |
| Minimum Contents | 移到 MU 数量最少的后继 |
| Minimum Number In | 移到接收 MU 最少的后继 |
| Minimum Processing Time | 移到加工时间最短的后继 |
| Minimum Relative Occupation | 移到相对占用率最低的后继 |
| Minimum Set-up Time | 移到换型时间最短的后继 |
| Most Recent Demand | 移到最近接收过 MU 的后继 |
| MU Attribute | 按 MU 属性移向后继（`ExitStrategyMUAttributeList`） |
| Percentage | 按百分比分布移向后继（`ExitStrategyPercentageValues`） |
| Random | 随机移向后继 |
| Start at Successor 1 | 总是移到 1 号后继 |

> 注：`Maximum/Minimum Contents, Number In, Processing Time, Relative Occupation, Set-up Time` 仅在后继/前驱的资源统计启用时才能正确工作。

---

## 7. 用 FlowControl 分流

`FlowControl` 建模分流/合流策略，不存储、不加工 MU，只在其后继之间分配。前驱与后继数量通常不限。示例按零件属性分配；若零件有多个属性，只要有一个属性满足列表条件即可。

默认后继（default successor）取值含义：

| 值 | 行为 |
| --- | --- |
| 1 或其他后继号 | 移到该后继 |
| 0 | 不移动，零件停留在 FlowControl 前，阻塞后续零件 |
| -1（或任何负数） | 显示错误消息 |

- 配置 Source：用 Delivery Table（如 `MyDeliveryTable`），在 `Attributes` 列创建子表定义属性（如 `Color`、`Shape`），Source 将其创建为 `string` 类型用户属性。
- 配置 FlowControl：`Strategy > MU Attribute`，`Open List` 输入属性名、值、后继号，自上而下匹配。

---

## 8. 用 TransferStation 装卸零件

`TransferStation` 自定义零件转移行为，从 `Tools` 文件夹或工具栏插入。默认不在新模型中显示；`PickAndPlace` 机器人可模拟其大部分功能。

示例场景：4 个零件装到托盘 → 传送带输送 → 从托盘按 2 个一组卸下并装到运输车 → 按 1 个一组卸到加工站 → 移出工厂。

- **Load（装载）**：从零件站取零件，装到位于目标站上的运输工具（`Container`/`Transporter`）。设 `Station type = Load`，指定零件来源站、运输工具所在 Conveyor，以及传感器位置（如 0 米）；`Advanced Attributes` 设置装载块大小（如 4）。
- **Reload（转载）**：从位于零件站的运输工具取零件，放到位于目标站的运输工具。设 `Station type = Reload`，拖入 Line/Conveyor（来源）与 Track（运输工具位置），分别设传感器位置（如 22 米、15 米）；块大小如 2。
- **Unload（卸载）**：从位于零件站的运输工具取零件，放到目标站。设 `Station type = Unload`，拖入 Track（来源）与 Station（目标），设传感器位置（如 43 米）；块大小如 1。最后插入 Method（源码 `deleteMovables`，命名 `reset`）与 `EventController` 并运行仿真。

> 注意：确保目标工位有足够空间容纳待进入的 MU。
