# Track（轨道）— 属性（Attributes）汇总说明

本目录 `attributes` 汇总了 Track（轨道）物料流对象的属性参考文档。Track 是 Plant Simulation 中的一种长度导向（length-oriented）物料流对象，与 Transporter（运输小车）配合使用，用于建模 AGV（自动导引车）系统。

本文件是 `attributes/attributes.md` 的内容总结，并参考了同级目录 `general/README.md`、`methods/README.md` 与 `read-only-attributes/README.md` 的汇总内容。当前目录下没有子文件夹，因此没有可引用的子目录 README.md。

---

## 1. 概述

Track 提供的属性包括：

- 本目录文档中列出的属性（见下表）。
- All Objects（所有对象）的属性。
- Material Flow Objects（物料流对象）的属性。

要查看对象的所有方法、只读属性和属性，请打开窗口 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，以显示所选 Class 的方法、只读属性和属性。
- 在插入实例的 Frame 的 Home 功能区选项卡上按 **F8** 键或点击 **Show Attributes and Methods**，以显示所选 Instance 的方法、只读属性和属性。

属性可以设置（set）和获取（get）其值，既可以通过对话框中的复选框、文本框和下拉列表，也可以通过给相应属性赋值来实现。

设置属性值的示例：

```simtalk
MyTrack.Length := 44
```

获取属性值的示例：

```simtalk
print MyTrack.Length
posit := MyStation.Cont.XPos
```

---

## 2. 属性列表

| 属性 | 数据类型 | 语法 | 说明 |
| --- | --- | --- | --- |
| **OccupiedLength** | `length`（只读） | `<Path>.OccupiedLength → length` | 返回 Track 的总 Length 中被其上所有 Transporter 占用的部分。 |
| **BwDestList** | `object` | `<Path>.BwDestList:object` | 设置 Transporter 在 Track 上后退行驶时的目的地列表（Backward Destination List）。 |
| **Capacity** | `integer` | `<Path>.Capacity:integer` | 设置同一时刻可整体或部分位于 Track 上的 Transporter 最大数量。输入 `-1` 表示无限容量。可监视（watchable）。 |
| **FwDestList** | `object` | `<Path>.FwDestList:object` | 设置 Transporter 在 Track 上前进行驶时的目的地列表（Forward Destination List）。 |
| **Length** | `length` | `<Path>.Length:length` | 设置轨道长度。Transporter 在位置 0 驶入 Track，覆盖此处输入的长度后驶出。可监视。 |
| **Width** | `length` | `<Path>.Width:length` | 设置轨道宽度。可监视。 |

> 注：`OccupiedLength` 为只读属性，同时出现在只读属性文档 `read-only-attributes/read-only-attributes.md` 中。

---

## 3. 属性详解

### OccupiedLength [SimTalk] — Track

返回由 `<Path>` 指定的 Track 的整个 `Length` 中，被其上所有 Transporter 占用的部分。

**备注（Remarks）**

每个位于 Track 上的 Transporter 都会占用部分可用总长度。

**类型（Type）**：只读属性（Read-only attribute）。

**语法**

```simtalk
<Path>.OccupiedLength → length
```

**返回值**

返回值的数据类型为 `length`。

**示例**

```simtalk
print MyTrack.OccupiedLength
```

**参见：** Length [text box] - Track。

---

### BwDestList [SimTalk]

设置由 `<Path>` 指定的 Track 上后退行驶的 Transporter 的目的地列表（Backward Destination List）名称。

**类型（Type）**：属性（Attribute）。

**语法**

```simtalk
<Path>.BwDestList:object
```

**赋值（Assignment Value）**

可赋数据类型为 `object` 的值。

该目的地列表包含 Transporter 在此 Track 上后退行驶时可到达的所有目的地。

**示例**

```simtalk
MyTrack.BwDestList := myDataList
```

**参见：** Backward Destination List [text box]。

---

### Capacity [SimTalk] — Track

设置由 `<Path>` 指定的 Track 上，同一时刻可整体或部分位于其上的 Transporter 最大数量。

**类型（Type）**：属性（Attribute）。

**语法**

```simtalk
<Path>.Capacity:integer
```

**可监视（Watchable）**：该属性可监视。

**赋值（Assignment Value）**

可赋数据类型为 `integer` 的值。输入 `-1` 表示无限容量。

**示例**

```simtalk
if MyTrack.Capacity = -1
   @.move(AEConveyor)
end
```

**参见：** Capacity [text box] - Track。

---

### FwDestList [SimTalk]

设置由 `<Path>` 指定的 Track 上前进行驶的 Transporter 的目的地列表（Forward Destination List）名称。

**备注（Remarks）**

该目的地列表包含 Transporter 在此 Track 上前进方向移动时可到达的所有目的地。

**类型（Type）**：属性（Attribute）。

**语法**

```simtalk
<Path>.FwDestList:object
```

**赋值（Assignment Value）**

可赋数据类型为 `object` 的值。

**示例**

```simtalk
MyTrack.FwDestList := myDataList1
```

**参见：** Forward Destination List [text box]。

---

### Length [SimTalk] — Track

设置由 `<Path>` 指定的 Track 的长度。

**备注（Remarks）**

- Transporter 在位置 0 驶入 Track，覆盖此处输入的长度后驶出。
- `Speed` 与 `Length` 共同决定 Transporter 在 Track 上的停留时间。

**类型（Type）**：属性（Attribute）。

**语法**

```simtalk
<Path>.Length:length
```

**可监视（Watchable）**：该属性可监视。

**赋值（Assignment Value）**

可赋数据类型为 `length` 的值。

**注意（Note）**

在 SimTalk 2.0 中可指定长度单位 `m`、`mm`、`km`、`cm`、`yd`、`ft`、`in`。单位直接写在数值之后，不加空格，例如 `10m` 或 `10.2m`。浮点值和整数值均可指定单位。

**示例**

```simtalk
MyTrack.Length := 44m
```

**参见：** Length [text box] - Track。

---

### Width [SimTalk] — Track

设置由 `<Path>` 指定的 Track 的宽度。

**类型（Type）**：属性（Attribute）。

**语法**

```simtalk
<Path>.Width:length
```

**可监视（Watchable）**：该属性可监视。

**赋值（Assignment Value）**

可赋数据类型为 `length` 的值。

**注意（Note）**

在 SimTalk 2.0 中可指定长度单位 `m`、`mm`、`km`、`cm`、`yd`、`ft`、`in`。单位直接写在数值之后，不加空格，例如 `10m` 或 `10.2m`。浮点值和整数值均可指定单位。

**示例**

```simtalk
MyTrack.Width := 2 // meters
```

**参见：** Width [text box] - AngularConverter。

---

### TwoLaneTrack（双车道轨道）

使用对象 `TwoLaneTrack` 可建模一条具有两个车道的运输线，无论是否使用自动路由，Transporter 都可以在相反方向上运输部件。

**描述（Description）**

- 例如，可使用 `TwoLaneTrack` 和 `Transporter` 建模 AGV（自动导引车）系统。Transporter 在 `TwoLaneTrack` 上需行驶的距离由车道 A 的 `Length`、车道 B 的 `Length`、Transporter 的 MU Length 及其 `Speed` 决定，它们共同决定 Transporter 在 `TwoLaneTrack` 上的停留时间。与面向点的物料流对象不同，Plant Simulation 在仿真运行中使用实际输入的长度。
- Transporter **不能超越**其前方移动的另一辆 Transporter，因此 Transporters 保持驶入和驶离 `TwoLaneTrack` 的顺序。
- `TwoLaneTrack` 的每个车道可以有自己的长度，以真实建模 `TwoLaneTrack` 转弯时的情况——此时外侧车道比内侧车道更长。
- 若多辆 Transporter 以不同速度沿同一车道行驶，较快的会与较慢的发生碰撞。Plant Simulation 会激活较快 Transporter 的 **Collision Control**，并自动将其速度降低到与较慢者一致。
- Transporter 可以在 `TwoLaneTrack` 上**前进和后退**，即从其出口驶入、从其入口驶出。前进/后退不是 `TwoLaneTrack` 的属性，而是在其上行驶的 Transporter 的属性。
- `TwoLaneTrack` 的最大容量由其长度和其上各 Transporter 的长度决定（例如，3 码长的 `TwoLaneTrack` 最多可容纳三辆 1 码长的 Transporter）。`Capacity` 属性可进一步限制位于其上的 Transporter 数量。

可插入 `TwoLaneTrack` 的方式：

- 作为**弯曲对象**（curved object，默认设置）。
- 通过插入任意**弯曲段和直线段**的序列，以真实地建模 Transporter 在其上移动的弯曲输送系统。

可以在 **Appearance** 选项卡上为 `TwoLaneTrack` 选择不同的配置。

---

### General Notes on Track Attributes（Track 属性通用说明）

Track 提供：

- 目录中列出的属性。
- All Objects（所有对象）的属性。
- Material Flow Objects（物料流对象）的属性。

要查看对象的所有方法、只读属性和属性，请打开窗口 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，以显示所选 Class 的方法、只读属性和属性（一般说明）。
- 按 **F8** 键，或在插入实例的 Frame 的 Home 功能区选项卡上点击 **Show Attributes and Methods**，以显示所选 Instance 的方法、只读属性和属性（一般说明）。

属性可以设置（set）和获取（get）其值，既可以通过对话框中的复选框、文本框和下拉列表，也可以通过给相应属性赋值来实现。

- 设置属性值的示例：

```simtalk
MyTrack.Length := 44
```

- 获取属性值的示例：

```simtalk
print MyTrack.Length
posit := MyStation.Cont.XPos
```

---

## 4. 同级目录 README 摘要

### 4.1 general（对象概述）

`general/README.md` 汇总了 Track 的完整参考文档，要点如下：

- **用途**：Track 与 Transporter 一起用于建模 AGV（automated guided vehicle，自动导引车）系统。
- **关键特性**：
  - Transporter 在 Track 上的停留时间由 Track 的 **Length**、Transporter 的 **MU Length** 和 **Speed** 决定。
  - 与面向点（point-oriented）的物料流对象不同，Plant Simulation 在仿真运行中使用实际输入的 **Length**。
  - Transporter 不能超越前方移动的 Transporter，保持 FIFO 顺序。
  - 较快 Transporter 碰撞较慢者时，Plant Simulation 激活较快者的 **Collision Control** 并自动降速。
  - 最大容量由 Track 长度和其上 Transporter 长度决定；**Capacity** 可进一步限制。
  - Transporter 可前进和后退；前进/后退是 Transporter 的属性，而非 Track 的属性。
  - Track 可作为弯曲对象（默认）或弯曲段 + 直线段的序列插入。
- **对话框选项卡**：Attributes、Times、Failures、Controls、Exit、Statistics、User-defined。
- **路由（Routing）优先级**：Exit Control > Automatic Routing > Driving Control > Track 内置属性。
- **相关对象**：`Transporter`、`TwoLaneTrack`。

### 4.2 methods（方法）

`methods/README.md` 汇总了 Track 的方法参考文档，要点如下：

- **语法行约定**：`<Path>` 表示方法所应用对象的路径；签名（参数标识符与数据类型）在括号中列出；可选参数用方括号 `[...]` 表示；带默认值的参数用 `:= default` 表示；有返回值的方法在箭头 `->` 后显示数据类型。
- **方法列表**：

| 方法 | 语法 | 说明 |
| --- | --- | --- |
| **getRouteLength** | `<Path>.getRouteLength(Target:path[, Backwards:boolean, Position:length, ObjectsAlongRoute:table, RouteWeightingAttribute:string]) → length` | 返回从 Track 到目标的最短路径及其长度。若未找到路径返回 `-1`。 |

- **参数说明**：`Target`（目标，`object`）；`Backwards`（可选，`boolean`，`true` 后退 / `false` 前进）；`Position`（可选，`length`，开始搜索的 Track 位置）；`ObjectsAlongRoute`（可选，`table`，写入沿路径对象）；`RouteWeightingAttribute`（可选，`string`，自动路由路径加权属性名称）。
- **注意**：由于路径是为 Transporters 设计的，Plant Simulation 在计算路径时只考虑 Track 和 TwoLaneTrack 类型的对象。

### 4.3 read-only-attributes（只读属性）

`read-only-attributes/README.md` 汇总了 Track 的只读属性参考文档，要点如下：

- 只读属性只能查询、不能设置，因为 Plant Simulation 在查询时计算其值。
- 大多数情况下，只读属性对应对象某个选项卡（例如 Statistics）上不可用的对话框项。

| 只读属性 | 语法 | 返回值 | 说明 |
| --- | --- | --- | --- |
| **OccupiedLength** | `<Path>.OccupiedLength → length` | `length` | 返回 Track 的总 Length 中被其上所有 Transporter 占用的部分。每个位于 Track 上的 Transporter 都会占用部分可用长度。 |

查询示例：

```simtalk
print MyTrack.OccupiedLength
```

---

## 5. 相关参考

- 属性对应的对话框项：**Length [text box]**、**Width [text box]**、**Capacity [text box]**、**Backward Destination List [text box]**、**Forward Destination List [text box]**。
- 相关对象：`Transporter`、`TwoLaneTrack`。
- 方法参考：`getRouteLength [SimTalk]`。
- 只读属性参考：`OccupiedLength [SimTalk]`。
- 对象概述：`general/general.md`。

---

*Source: Plant Simulation Help 11-2465 — 11-2472. Unpublished work. © 2026 Siemens.*
