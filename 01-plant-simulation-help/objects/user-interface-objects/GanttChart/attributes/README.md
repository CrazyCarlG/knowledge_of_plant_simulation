# README — GanttChart（属性）

本目录汇总了 **GanttChart（甘特图）** 用户界面对象的属性（Attributes）说明。内容来源为同目录下的 `attributes.md`（以及 `attributes.txtx` 原始文本）。

> 说明：`attributes` 目录下暂无子文件夹，因此不存在子文件夹内的 `README.md` 可供合并。本 README 仅基于 `attributes.md` 的内容总结。

## 概述

GanttChart 提供：

- 左侧目录（table of contents）中列出的属性；
- **所有对象的属性（Attributes of All Objects）**。

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选**类（Class）** 的方法、只读属性与属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选**实例（Instance）** 的方法、只读属性与属性。

属性既可以**设置**其值，也可以**获取**其值，方式有两种：

- 通过对话框中的复选框、文本框和下拉列表；
- 通过为相应属性赋值。

查询某个只读属性的值，例如：

```
print MyGanttChart.UUID
```

设置某个属性的值，例如：

```
MyGanttChart.IsShown := true
```

获取某个属性的值，例如：

```
print MyGanttChart.IsShown
posit := Station.Cont.XPos
```

## 属性列表

| 属性 | 语法 | 说明 |
| --- | --- | --- |
| `CollectData [SimTalk]` | `<Path>.CollectData:boolean` | 设置 GanttChart 是否收集数据 |
| `EnableVisualTracking [SimTalk]` | `<Path>.EnableVisualTracking:boolean` | 激活/停用零件或资源的可视跟踪 |
| `IsShown [SimTalk]` | `<Path>.IsShown:boolean` | 激活/停用 GanttChart 的显示 |
| `NumVisibleBars [SimTalk]` | `<Path>.NumVisibleBars:integer` | 设置最大可见条形数 |
| `Parts [SimTalk]` | `<Path>.Parts:array` | 设置 GanttChart 可视化的零件（MU） |
| `Resources [SimTalk]` | `<Path>.Resources:array` | 设置 GanttChart 可视化的资源（物料流对象） |
| `ShowBarText [SimTalk]` | `<Path>.ShowBarText:boolean` | 设置是否在 Gantt 条形上显示零件名称文本 |
| `ShowPartView [SimTalk]` | `<Path>.ShowPartView:boolean` | 设置显示零件视图还是资源视图 |
| `ShowResourceLabels [SimTalk]` | `<Path>.ShowResourceLabels:boolean` | 设置显示资源标签还是资源名称 |
| `ShowResourceStates [SimTalk]` | `<Path>.ShowResourceStates:boolean` | 设置是否以条形颜色显示资源状态 |
| `TimeScale [SimTalk]` | `<Path>.TimeScale:integer` | 设置 GanttChart 的时间尺度 |

## 属性详解

### CollectData [SimTalk] - GanttChart

设置由 `<Path>` 指定的 GanttChart 是否收集数据：`true` 收集数据，`false` 不收集数据。

> **备注：** 不能同时使用方法 `setData` 并自动收集数据。当给 `CollectData` 赋值 `true` 时，请勿调用方法 `setData`。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 boolean 数据类型的值。

**示例**

```
MyGanttChart.CollectData := true
```

**另请参见：** Collect Data [check box] - GanttChart、CollectData [SimTalk] - GanttChart

### EnableVisualTracking [SimTalk]

激活（`true`）或停用（`false`）由 `<Path>` 指定的 GanttChart 对零件或资源的可视跟踪。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 boolean 数据类型的值。

**示例**

```
MyGanttChart.EnableVisualTracking := true
```

**另请参见：** Show Chart [button] - GanttChart、EnableVisualTracking [SimTalk]

### IsShown [SimTalk] - GanttChart

激活（`true`）或停用（`false`）由 `<Path>` 指定的 GanttChart 的显示。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 boolean 数据类型的值。

**示例**

```
MyGanttChart.IsShown := false
```

**另请参见：** Show Chart [button] - GanttChart、IsShown [SimTalk] - GanttChart

### NumVisibleBars [SimTalk]

设置由 `<Path>` 指定的 GanttChart 中最大可见条形数。

> **备注：** 默认设置为 `100000`。若超过该数值，较旧的条形将不再显示。若性能受损，可减小该数值。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 integer 数据类型的值。

**示例**

```
MyGanttChart.NumVisibleBars := 8000
```

**另请参见：** Show Chart [button] - GanttChart、NumVisibleBars [SimTalk]

### Parts [SimTalk]

设置由 `<Path>` 指定的 GanttChart 所可视化的零件，即 MU。

> **备注：** 可以监视零件的类，也可以监视零件的单个实例。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 array 数据类型的值。

**示例**

```
MyGanttChart.Parts := [*.MUs.Entity]   // 该类的所有零件
MyGanttChart.Parts := [*.MUs.Entity:1] // 编号为 1 的零件
```

**另请参见：** Tab Parts [GanttChart]、Parts [SimTalk]

### Resources [SimTalk] - GanttChart

设置由 `<Path>` 指定的 GanttChart 所可视化的资源，即物料流对象。

> **备注：** 可以监视资源的类，也可以监视资源的单个实例。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 array 数据类型的值。

**示例**

```
MyGanttChart.Resources := [Source, Station, Station1, Drain]
```

**另请参见：** Tab Resources [GanttChart]、Resources [SimTalk] - GanttChart

### ShowBarText [SimTalk]

设置由 `<Path>` 指定的 GanttChart 是否在 Gantt 条形上以文本显示零件名称：`true` 显示，`false` 不显示。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 boolean 数据类型的值。

**示例**

```
MyGanttChart.ShowBarText := true
```

**另请参见：** Show Bar Text [check box]、ShowBarText [SimTalk]

### ShowPartView [SimTalk]

设置由 `<Path>` 指定的 GanttChart 在**资源视图**中显示资源（`false`），还是在**零件视图**中显示零件（`true`）。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 boolean 数据类型的值。

**示例**

```
MyGanttChart.ShowPartView := true
```

**另请参见：** Show Chart [button] - GanttChart、ShowPartView [SimTalk]

### ShowResourceLabels [SimTalk]

设置由 `<Path>` 指定的 GanttChart 显示资源的**标签**（`true`），还是显示其**名称**（`false`）。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 boolean 数据类型的值。

**示例**

```
MyGanttChart.ShowResourceLabels := true
```

**另请参见：** Show Resource Labels [check box]、ShowResourceLabels [SimTalk]

### ShowResourceStates [SimTalk]

设置由 `<Path>` 指定的 GanttChart 是否以条形颜色显示资源的状态：`true` 显示，`false` 不显示。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 boolean 数据类型的值。

**示例**

```
MyGanttChart.setLanes(MyLanesTable)
MyGanttChart.ShowResourceStates := true
```

**另请参见：** Show Resource States [check box]、States of the Material Flow Objects、ShowResourceStates [SimTalk]

### TimeScale [SimTalk]

设置由 `<Path>` 指定的 GanttChart 的时间尺度。Plant Simulation 在打开 GanttChart 时应用该值。

> **备注：** 时间尺度的单位为“逻辑像素/秒”。当时间尺度为 `0.5` 时，Plant Simulation 将持续 60 秒的 Gantt 事件显示为 30 逻辑像素长的条形。

- **类型：** 属性（Attribute）
- **语法：** `<Path>.TimeScale:integer`
- **赋值：** 可赋值为 real 数据类型的值。指定 `0` 以使用默认时间缩放。

**示例**

```
MyGanttChart.TimeScale := 2.5
```

**另请参见：** Show Chart [button] - GanttChart、SankeyDiagram

---

*来源：Plant Simulation Help 11-4848。Unpublished work. © 2026 Siemens。*
