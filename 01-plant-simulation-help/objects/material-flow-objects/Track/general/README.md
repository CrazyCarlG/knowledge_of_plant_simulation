# Track（轨道）— 汇总说明

本目录 `general` 汇总了 Track（轨道）物料流对象的完整参考文档。Track 是 Plant Simulation 中的一种长度导向（length-oriented）物料流对象，与 Transporter（运输小车）配合使用，用于建模 AGV（自动导引车）系统。

本文件是 `general/general.md` 以及同级子目录 `attributes/attributes.md`、`methods/methods.md`、`read-only-attributes/read-only-attributes.md` 的内容总结。

---

## 1. 对象概述（general）

Track 与 Transporter 一起用于建模 AGV（automated guided vehicle，自动导引车）系统。

### 关键特性

- **Transporter 在 Track 上的停留时间**由以下因素决定：
  - Track 的 **Length**（长度）
  - Transporter 的 **MU Length**（MU 长度）
  - Transporter 的 **Speed**（速度）
- 与面向点（point-oriented）的物料流对象不同，Plant Simulation 在仿真运行中使用实际输入的 **Length**。
- Transporter **不能超越**其前方移动的另一辆 Transporter，因此 Transporters 保持驶入和驶离 Track 的顺序（**FIFO**）。
- 若较快的 Transporter 与较慢的 Transporter 发生碰撞，Plant Simulation 会激活较快 Transporter 的 **Collision Control**（碰撞控制），并自动将其速度降低到与较慢者一致。
- **最大容量**由 Track 的长度和其上各 Transporter 的长度决定（例如，3 码长的 Track 最多可容纳三辆 1 码长的 Transporter）。**Capacity** 属性可进一步限制该数量。
- Transporter 可以**前进和后退**（从其出口驶入、从其入口驶出）。前进/后退是 Transporter 的属性，而不是 Track 的属性。
- Track 可以插入 Frame 中：
  - 作为**弯曲对象**（curved object，默认设置）。
  - 通过插入任意**弯曲段和直线段**的序列，以真实地建模弯曲的输送系统。
- 可以在 **Appearance**（外观）选项卡上选择不同的配置。

### 显示操纵器（Show Manipulators）

- 要更改图形的长度和锚点，请点击 Edit 功能区选项卡上的 **Show Manipulators** 或按 `M` 键。
- 长度导向对象起点和终点的操纵器是被截断的。将同类型的对象附加到其上时，两个半截操纵器会重新组合成一个完整的操纵器。
- 将鼠标悬停在操纵器上会显示工具提示（Tooltip）。

### 添加对象到仿真模型

- 点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > MaterialFlow > Track**。
- 示例模型：**Window 功能区选项卡 > Start Page > Getting Started > Example Models > Small Examples**，然后在 *Examples Collection* 对话框中选择 Category、Topic 和 Example，点击 **Open Model**。

---

## 2. 属性（Attributes）

Track 提供的属性包括下表中的属性，以及 All Objects（所有对象）的属性和 Material Flow Objects（物料流对象）的属性。可通过窗口 **Show Attributes and Methods** 查看。

属性可以设置（set）和获取（get）其值。例如：

```simtalk
MyTrack.Length := 44m          -- 设置
print MyTrack.Length           -- 获取
```

### 属性列表

| 属性 | 数据类型 | 说明 |
| --- | --- | --- |
| **Length** | `length` | 设置轨道长度。Transporter 在位置 0 驶入 Track，覆盖此处输入的长度后驶出。Speed 与 Length 共同决定在 Track 上的停留时间。可监视（watchable）。 |
| **Width** | `length` | 设置轨道宽度。可监视。 |
| **Capacity** | `integer` | 设置同一时刻可整体或部分位于 Track 上的 Transporter 最大数量。输入 `-1` 表示无限容量。可监视。 |
| **BwDestList** | `object` | 设置 Transporter 在 Track 上后退行驶时的目的地列表（Backward Destination List）。 |
| **FwDestList** | `object` | 设置 Transporter 在 Track 上前进行驶时的目的地列表（Forward Destination List）。 |
| **OccupiedLength** | `length`（只读） | 返回 Track 的总 Length 中被其上所有 Transporter 占用的部分。 |

> 注：`OccupiedLength` 为只读属性，同时出现在只读属性文档 `read-only-attributes/read-only-attributes.md` 中。

### TwoLaneTrack（双车道轨道）

使用对象 `TwoLaneTrack` 可建模一条具有两个车道的运输线，无论是否使用自动路由，Transporter 都可以在相反方向上运输部件。

- 每个车道可以有自己的长度，以真实建模 `TwoLaneTrack` 转弯时外侧车道比内侧车道更长的情况。
- 其余行为（不能超车、碰撞控制、前进/后退、容量由长度决定等）与单车道 Track 相同。

---

## 3. 方法（Methods）

Track 提供的方法包括下表中的方法，以及 Curved Objects（弯曲对象）、Material Flow Objects（物料流对象）和 All Objects（所有对象）的方法。

### 方法列表

| 方法 | 语法 | 说明 |
| --- | --- | --- |
| **getRouteLength** | `<Path>.getRouteLength(Target:path[, Backwards:boolean, Position:length, ObjectsAlongRoute:table, RouteWeightingAttribute:string]) → length` | 返回从 Track 到目标的最短路径及其长度。 |

### getRouteLength 参数说明

- **Target**（数据类型 `object`）：指定目标。目标既可以是能通过 Connector 直接到达的物料流对象，也可以是键入到传感器（sensor）中的目的地。
- **Backwards**（可选，`boolean`）：指定搜索路径的方向。`true` 表示后退，`false` 表示前进（默认）。
- **Position**（可选，`length`）：指定开始搜索的 Track 位置。若未指定，前向搜索从 Track 末端开始，后向搜索从 Track 起点开始。当目标是位于 Track 自身上的传感器时尤其重要。
- **ObjectsAlongRoute**（可选，`table`）：将沿路径的对象写入指定表格。
- **RouteWeightingAttribute**（可选，`string`）：设置自动路由中用于路径加权的属性名称。若未传入该参数，Plant Simulation 不对路径长度进行加权。

> **注意**：由于该路径是为 Transporters 设计的，Plant Simulation 在计算路径时只考虑 Track 和 TwoLaneTrack 类型的对象。

**返回值**：数据类型为 `length`。若未找到路径，返回 `-1`。

**示例**：

```simtalk
print Track5.getRouteLength(Track26)
```

### 语法行约定

- `<Path>` 表示方法所应用对象的路径。
- 签名（参数标识符和数据类型）在括号中列出，例如 `(Parameter:string)`。
- 可选参数用方括号 `[...]` 表示。
- 带默认值的参数在参数后用 `:= default` 表示。
- 有返回值的方法在箭头 `->` 后显示数据类型。

---

## 4. 只读属性（Read-Only Attributes）

只读属性只能查询、不能设置，因为 Plant Simulation 在查询时计算其值。大多数情况下，只读属性对应对象某个选项卡（例如 Statistics）上不可用的对话框项。

### 只读属性列表

| 只读属性 | 语法 | 返回值 | 说明 |
| --- | --- | --- | --- |
| **OccupiedLength** | `<Path>.OccupiedLength → length` | `length` | 返回 Track 的总 Length 中被其上所有 Transporter 占用的部分。每个位于 Track 上的 Transporter 都会占用部分可用长度。 |

查询示例：

```simtalk
print MyTrack.OccupiedLength
```

---

## 5. 对话框选项卡（general.md 摘要）

Track 的对话框包含以下选项卡：

- **Attributes**：设置 Length、Width、Capacity、Backward Destination List、Forward Destination List 等。
- **Times**：定义时间分布（可用 `setTypeAndAttr` 方法设置）。
- **Failures**：定义故障。
- **Controls**：提供控件修改对象内置行为（如 Entrance / Exit / Backward Entrance / Backward Exit / Pull 控制、Shift Calendar 等）。
- **Exit**：选择对象将 MU 移动到的后继对象（退出策略、阻塞）。
- **Statistics**：统计信息（可查看 Stationary Resources 的 Resource Statistics）。
- **User-defined**：定义用户自定义属性。

### 菜单

- **Navigate 菜单**、**View 菜单**、**Tools 菜单**、**Tabs 菜单**、**Help 菜单**等。

---

## 6. 路由（Routing）详解

为便于分支 Track 的路径选择，Plant Simulation 按优先级顺序使用：

1. Track 的 **Exit Control**（最高优先级）。
2. Transporter 的 **Automatic Routing**（自动路由，使用后继对象的目的地列表）。
3. Transporter 的 **Driving Control**（行驶控制）。
4. Track 的**内置属性**（依次将 Transporters 移动到每个已连接的后继对象）。

补充说明：

- 若未定义 Exit Control，且为 Transporter 键入了目的地列表，则 Automatic Routing 会使用后继对象的目的地列表将 Transporter 移动到正确的后继对象。
- Track 具有 **Forward Destination List**（前进目的地列表）和 **Backward Destination List**（后退目的地列表），列出前进/后退时可达的所有目的地。
- 若 Track 未找到目的地，则依次将 Transporter 移动到下一个后继对象。
- 搜索在找到第一个目标实例后终止。
- 若未为 Transporter 键入目的地，或为 Track 键入了 Exit Control，则自动路由不生效。

---

## 7. 相关参考

- 示例模型：Window 功能区选项卡 > **Start Page > Getting Started > Example Models > Small Examples**。
- 相关对象：`Transporter`、`TwoLaneTrack`。
- 相关主题：Define Controls for Length-Oriented Objects、Entrance Control、Exit Control、Backward Entrance Control、Backward Exit Control、Pull Control、Shift Calendar、Resource Statistics、Resource Type。
- 方法参考：`getRouteLength [SimTalk]`。
- 只读属性参考：`OccupiedLength [SimTalk]`。
