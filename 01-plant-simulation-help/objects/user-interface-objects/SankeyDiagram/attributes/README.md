# README — SankeyDiagram（属性）

本目录汇总了 **SankeyDiagram（桑基图）** 用户界面对象的属性（Attributes）说明。内容来源为同目录下的 `attributes.md`（以及 `attributes.txtx` 原始文本）。

> 说明：`attributes` 目录下暂无子文件夹，因此不存在子文件夹内的 `README.md` 可供合并。本 README 仅基于 `attributes.md` 的内容总结。

## 概述

SankeyDiagram 提供：

- 左侧目录（table of contents）中列出的属性；
- **所有对象的属性（Attributes of All Objects）**。

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选**类（Class）** 的方法、只读属性与属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选**实例（Instance）** 的方法、只读属性与属性。

属性既可以**设置**其值，也可以**获取**其值，方式有两种：

- 通过对话框中的复选框、文本框和下拉列表；
- 通过为相应属性赋值。

查询某个只读属性的值，例如：

```simtalk
print MySankeyDiagram.UUID
```

设置某个属性的值，例如：

```simtalk
MySankeyDiagram.IsShown := true
```

获取某个属性的值，例如：

```simtalk
print MySankeyDiagram.IsShown
posit := Station.Cont.XPos
```

## 属性列表

| 属性 | 语法 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| `CollectData [SimTalk]` | `<Path>.CollectData:boolean` | boolean | 设置 SankeyDiagram 是否收集数据 |
| `Color [SimTalk]` | `<Path>.Color:integer` | integer | 设置 Plant Simulation 在 Frame 中显示零件和 Worker 的 Sankey 流时所用的颜色 |
| `IsShown [SimTalk]` | `<Path>.IsShown:boolean` | boolean | 激活/停用 SankeyDiagram 的显示 |
| `MaximumWidth [SimTalk]` | `<Path>.MaximumWidth:length` | length | 设置 Plant Simulation 在 Frame 中可视化 Sankey 流时的最大宽度 |
| `Objects [SimTalk]` | `<Path>.Objects:array` | array | 设置 SankeyDiagram 在 Frame 中可视化的对象（零件或 Worker） |

## 属性详解

### CollectData [SimTalk] - SankeyDiagram

设置由 `<Path>` 指定的 SankeyDiagram 是否收集数据：`true` 收集数据，`false` 不收集数据。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 boolean 数据类型的值。

**示例**

```simtalk
MySankeyDiagram.CollectData := true
```

**另请参见：** Collect Data [check box] - SankeyDiagram、CollectData [SimTalk] - SankeyDiagram

### Color [SimTalk] - SankeyDiagram

设置 Plant Simulation 在 Frame 中显示由 `<Path>` 指定的 SankeyDiagram 的零件和 Worker 的 Sankey 流时所用的颜色。

> **备注：** 使用 `makeRGBValue` 方法设置颜色的 RGB 值。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 integer 数据类型的值。

**示例**

```simtalk
MySankeyDiagram.Color := makeRGBValue(255,0,0)
```

**SimTalk：** makeRGBValue [SimTalk]

**另请参见：** Color [SankeyDiagram]、Color [SimTalk] - SankeyDiagram

### IsShown [SimTalk] - SankeyDiagram

激活（`true`）或停用（`false`）由 `<Path>` 指定的 SankeyDiagram 的显示。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 boolean 数据类型的值。

**示例**

```simtalk
MySankeyDiagram.IsShown := false
```

**另请参见：** Show Diagram、IsShown [SimTalk] - SankeyDiagram

### MaximumWidth [SimTalk]

设置 Plant Simulation 在 Frame 中可视化由 `<Path>` 指定的 SankeyDiagram 的零件和 Worker 的 Sankey 流时的最大宽度。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 length 数据类型的值。

**示例**

```simtalk
MySankeyDiagram.MaximumWidth := 1.0 -- meters
```

**另请参见：** Maximum Width [SankeyDiagram]、MaximumWidth [SimTalk]

### Objects [SimTalk] - SankeyDiagram

设置由 `<Path>` 指定的 SankeyDiagram 在 Frame 中可视化的对象，即其 Sankey 流被可视化的零件（Parts）或 Worker。

- **类型：** 属性（Attribute）
- **赋值：** 可赋值为 array 数据类型的值。

**示例**

```simtalk
MySankeyDiagram.Objects := [.Resources.Worker]         // 该类的所有 Worker
MySankeyDiagram.Objects := [.Resources.WorkerPool]     // 所有 WorkerPool 类
MySankeyDiagram.Objects := [.Models.Model.WorkerPool]  // 名为 Frame 的 Frame 中 WorkerPool 的所有 Worker
MySankeyDiagram.Objects := [.Resources.Worker:1]       // 编号为 1 的 Worker
```

**另请参见：** Objects, tab、CostAnalyzer、CostAnalyzer

> 可使用 **CostAnalyzer** 对象分析各个机器和 Worker 所产生的成本。CostAnalyzer 会计算物料流对象在处理设备中零件时所产生的成本。

---

*来源：Plant Simulation Help 11-4877。Unpublished work. © 2026 Siemens。*
