# SankeyDiagram 对象（桑基图对象）

> 本目录 `general/` 下只有一个 Markdown 文件 `general.md`（以及同名源文本 `general.txtx`），没有子文件夹，也没有其他 README.md。本文件是对 `general.md` 内容的总结。

## 概述

**SankeyDiagram**（桑基图）对象用于可视化以下对象的桑基流（Sankey flows）：

- **零件（Parts）**
- **工人（Workers）** —— 在区域内自由走动或在 FootPaths（人行道）上走动
- **AGV** —— 在模型区域内自由行驶

### 说明（Description）

- 要显示**类对象**的桑基流，可将 `Part`、`Container`、`Worker`、`WorkerPool`、`Transporter` 或 `AGVPool` 类从 Class Library 拖到 SankeyDiagram 的图片上并放下。
- 要显示**单个实例**的桑基流，可在 **Objects** 选项卡列表的单元格中键入实例名称，例如 `.MUs.Part:3`。
- 将鼠标悬停在 SankeyDiagram 上可显示相关提示信息（tooltip）。
- 在 **Edit** 功能区选项卡中点击 **Show Manipulators** 或按 `M` 键，可更改图形长度和锚点。

### 添加对象到仿真模型

点击 **Home** 功能区选项卡中的 **Manage Class Library > Basic Objects > UserInterface > SankeyDiagram**。

## TimeScale [SimTalk]

设置由 `<Path>` 指定的 `GanttChart` 的时间刻度。Plant Simulation 在打开 `GanttChart` 时应用该值。

**备注：** 时间刻度的单位是逻辑像素/秒。对于时间刻度 `0.5`，Plant Simulation 会将持续 60 秒的甘特事件显示为 30 逻辑像素长的条形。

- **类型：** 属性（Attribute）
- **语法：** `<Path>.TimeScale:integer`
- **赋值：** 可赋 `real` 数据类型的值。指定 `0` 使用默认时间刻度。

```simtalk
MyGanttChart.TimeScale := 2.5
```

## SankeyDiagram 的对话框

双击 SankeyDiagram 图标即可打开其对话框。

### 编辑仿真属性（Edit Simulation Properties）

在对话框中可更改对象的仿真属性。共有属性见 *Dialog Items of the Objects*（对象的对话框项）。

### 编辑动画属性（Edit Animation Properties）

在 **Edit 3D Properties** 对话框中编辑对象的 3D 属性：

- 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮。
- 在模型中选择该对象并按空格键。

要操作对象的图形，点击 **Edit** 功能区选项卡中的 **Show Manipulators** 或按 `M` 键。

## Show Diagram（显示图）

要在 Frame 中显示桑基流，点击 **Show Diagram**。要隐藏桑基流，点击 **Hide Diagram**。

**备注：**
- 也可改用上下文菜单命令 **Show/Hide**。
- 点击 **Update** 可用当前值更新所显示的桑基流。

## Collect Data [复选框] — SankeyDiagram

勾选此复选框使 SankeyDiagram 收集数据。清除复选框可停用数据收集。

## Maximum Width [SankeyDiagram]

在文本框中键入桑基流的最大宽度，这些桑基流用于可视化 Frame 中零件和工人的路径。

## Color [SankeyDiagram]

选择可视化 Frame 中零件和工人路径的桑基流的颜色。

## Attributes 选项卡

**Attributes** 选项卡提供对象所提供设置。共有属性见 *Tab Attributes*。

## Objects 选项卡

在 **Objects** 选项卡上，可将要为其显示桑基流的对象分配给 SankeyDiagram。

### Objects [SankeyDiagram]

要显示类对象的桑基流，可将零件类（`Part`、`Container`、`Transporter`）、Worker 类或 WorkerPool 类从 Class Library 拖到列表相应单元格上并放下。

**备注：** 要显示单个零件（`Part`、`Container`、`Transporter`）、Worker 实例或 WorkerPool 实例的桑基流，可将其名称键入列表相应单元格，例如 `.MUs.Part:3`。

**注意：** 如果选项卡上对象启用了继承，SankeyDiagram 会用拖放所设置的类替换默认对象类。例如，这样可轻松地将 SankeyDiagram 从零件切换到工人。

## User-defined 选项卡

如 *Tab User-defined* 所述定义自己的属性。

## 菜单

- **Navigate Menu** —— 命令在 Navigate Menu 中说明。
- **View Menu** —— 命令在 View Menu 中说明。
- **Tools Menu** —— 提供访问其功能（Edit Controls、Edit Observers）的命令。
- **Help Menu** —— 命令在 Help Menu 中说明。

## SankeyDiagram 的方法

SankeyDiagram 提供：

- 左侧目录中所列的方法。
- **Methods of All Objects**（所有对象的通用方法）。

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 可显示所选类（Class）的方法、只读属性和属性。
- 按 `F8` 或点击插入实例的 Frame 的 **Home** 功能区选项卡中的 **Show Attributes and Methods** 可显示所选实例（Instance）的方法、只读属性和属性。

## 另请参阅

- Show Chart [按钮] — GanttChart
- Show Part Flows in a SankeyDiagram（在桑基图中显示零件流）
- Show AGV Flows in a SankeyDiagram（在桑基图中显示 AGV 流）
- Display a SankeyDiagram in the HtmlReport（在 HtmlReport 中显示桑基图）
- Update [in Frame]
- IsShown [SimTalk] — SankeyDiagram
- CollectData [SimTalk] — SankeyDiagram
- MaximumWidth [SimTalk]
- Color [SimTalk] — SankeyDiagram
- Objects [SimTalk] — SankeyDiagram
- updateDialog [SimTalk]
- Tools Menu [一般说明]
