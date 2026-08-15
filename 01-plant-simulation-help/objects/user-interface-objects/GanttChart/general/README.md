# README — GanttChart（通用说明）

本目录汇总了 **GanttChart（甘特图）** 用户界面对象的通用说明。内容来源为同目录下的 `general.md`（以及 `general.txtx` 原始文本）。

> 说明：`general` 目录下暂无子文件夹，因此不存在子文件夹内的 `README.md` 可供合并。本 README 仅基于 `general.md` 的内容总结。

## 概述

**GanttChart（甘特图）** 以时间轴上的条形图（bar）方式展示活动的时序（chronological sequence of activities）。

- GanttChart 可视化的是**物料流对象（material flow objects）**上的零件（parts），而不是资源对象（resource objects）。
- 除了单纯的占用（occupancy）数据外，GanttChart 还可以显示：
  - 机器的故障（failures）
  - 暂停时间（pausing times）
  - 阻塞时间（blocking times）

借此可以直观看出哪些机器或工位过载、哪些利用率低，以及哪些生产订单或产品在生产过程中等待时间较长。

基本操作提示：

- 将鼠标悬停在 GanttChart 上，可显示相关信息的工具提示（tooltip）。
- 在 **Edit** 功能区选项卡点击 **Show Manipulators** 或按键盘 **M** 键，可更改 GanttChart 图形的长度和锚点。

## 将对象添加到仿真模型

在 **Home** 功能区选项卡上依次点击：

> **Manage Class Library > Basic Objects > UserInterface > GanttChart**

> **注意：**
>
> - 对象 GanttChart 不属于 Plant Simulation 标准程序包。
> - 若正在使用 GanttChart，请用当前版本的 GanttChart 替换旧版本的 GanttChart，并将旧版本中用 SimTalk 编写的源代码调整到当前版本（对照 *Methods of the GanttChart* 与 *Attributes of the GanttChart*）。
> - 可参考示例模型：点击 Window 功能区选项卡，点击 **Start Page > Getting Started > Example Models > Small Examples**，然后在 *Examples Collection* 对话框中选择相应的 Category、Topic 和 Example，点击 **Open Model**。

## GanttChart 的对话框

双击 GanttChart 图标可打开其对话框。

### 编辑仿真属性

在对话框中可以修改对象的仿真属性，共享属性在 **Dialog Items of the Objects** 中描述。

### 编辑动画属性

要编辑对象的 3D 属性（在 *Edit 3D Properties* 对话框中）：

- 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮；
- 或选中模型中的对象并按空格键。

要操作对象的图形，点击 **Edit** 功能区选项卡上的 **Show Manipulators** 或按键盘 **M** 键。

## Collect Data [复选框]

勾选该复选框，使 GanttChart 在仿真运行期间收集数据；取消勾选则停用数据收集。

**备注：** 不能同时使用方法 `setData` 并自动收集数据。选中 **Collect Data** 时，请勿调用方法 `setData`。

## Show Chart [按钮]

点击该按钮，在显示窗口中显示 GanttChart 已收集的数据。

**备注：** 在 **Attributes** 选项卡上定义 GanttChart 如何显示收集的数据。

GanttChart 提供两种视图：

### 资源视图（Resource View）

资源视图显示被零件占用的资源：纵轴为资源，横轴为经过的时间。

> **注意：** GanttChart 按资源首次处理零件的顺序显示资源。最先处理零件的资源显示在第一条泳道（lane）中，之后处理零件的资源显示在下一条泳道中，依此类推。资源顺序无法更改。

默认设置下，GanttChart 在所有资源上以相同颜色显示同一零件。

### 零件视图（Part View）

零件视图显示占用资源的零件：纵轴为零件，横轴为经过的时间。

> **注意：** GanttChart 按零件首次被资源处理的顺序显示零件。最先被资源处理的零件显示在第一条泳道中，之后被处理的零件显示在下一条泳道中，依此类推。零件顺序无法更改。

默认设置下，GanttChart 对所有零件以相同颜色显示资源。所显示的资源状态指当前被该零件占用的资源。

### 显示更长或更短的时间区间

- 显示更长的时间区间：按住 `Ctrl` 并按 `-` 键，或向后滚动鼠标滚轮（放大视图）。
- 显示更短的时间区间：按住 `Ctrl` 并按 `+` 键，或向前滚动鼠标滚轮（缩小视图）。
- 以更大步长更改显示的时间区间：在按住 `Ctrl` 的同时再按住 `Shift`。
- 返回默认缩放比例：按住 `Ctrl` 并按 `0` 键。

## Tab Attributes [GanttChart]

在 **Attributes** 选项卡上设置 GanttChart 如何显示其收集的数据，可以：

- 选择 **View Mode**（资源视图或零件视图）；
- 选择显示或隐藏 **Show Resource Labels**（资源标签）；
- 选择显示或隐藏 **Show Bar Text**（条形文本）；
- 选择显示或隐藏 **Show Resource States**（资源状态）；
- 编辑显示 Gantt 数据所用的 **Lanes**（泳道）。

### View Mode（视图模式）

选择 GanttChart 显示 Gantt 数据的视图模式：

- **Resource View（资源视图）**：显示被零件占用的资源（纵轴为资源，横轴为时间）。资源按首次处理零件的顺序出现，顺序无法更改。对于由 Transporter 运输或 Worker 搬运的零件，资源视图将 Transporter 或 Worker 显示为资源，而不是 Track 或 Footpath。默认设置下，同一零件在所有资源上以相同颜色显示。
- **Part View（零件视图）**：显示占用资源的零件（纵轴为零件，横轴为时间）。零件按首次被资源处理的顺序出现，顺序无法更改。默认设置下，同一资源对所有零件以相同颜色显示。

可在下拉列表或上下文菜单中选择视图模式。所显示的资源状态指当前被该零件占用的资源。

可通过按住 `Ctrl` 并滚动鼠标滚轮调整 GanttChart 的时间尺度：

- 按住 `Ctrl` 向前滚动鼠标，显示更短的时间区间（更多细节）；
- 按住 `Ctrl` 向后滚动鼠标，显示更长的时间区间（粗略概览）。

将鼠标滚过某个条形时，**Resource View** 会在所有资源上高亮对应的零件；**Part View** 会对所有零件高亮对应的资源。借此可追踪零件在仿真过程中的路径。

- 在 **Resource View** 中，工具提示显示零件名称、其绝对路径、开始日期、结束日期和持续时间。若同一工位上有多个零件，工具提示会显示这些零件的信息；最后移动到工位上的零件位于列表顶部。
- 在 **Part View** 中，工具提示显示零件名称、被占用的资源、开始日期、结束日期和持续时间。

Resource View 在仿真期间持续刷新显示；Part View 必须按 `F5` 或选择上下文菜单命令 **Refresh** 手动刷新。

- 使用 **Show Resource Labels** 显示资源对象的标签而非名称。
- 使用 **Show Bar Text** 显示或隐藏资源的 Gantt 条形文本（条形文本可能重叠）。
- 使用 **Show Resource States** 显示或隐藏资源状态。
- 使用 **Edit Lanes** 设置 Gantt 条形距顶部的距离以及条形本身的高度。
- 使用属性 `ShowPartView` 设置 GanttChart 在零件视图中显示占用资源的零件，还是在资源视图中显示被占用的资源。

### Show Resource Labels [复选框]

勾选以显示资源的标签；取消勾选以隐藏标签并显示名称。

### Show Bar Text [复选框]

勾选以在 Gantt 条形上显示文本（条形文本可能重叠，显示零件名称）；取消勾选以隐藏资源的条形文本。

### Show Resource States [复选框]

勾选以在时间轴下方显示资源的彩色状态条。零件的颜色与对象的状态颜色相同（对照 *States of the Material Flow Objects*）；取消勾选以隐藏。

### Edit Lanes（编辑泳道）

点击 **Edit Lanes**，输入 Gantt 条形距顶部的距离以及条形本身的高度。要应用更改的值，在 *getLanes* 对话框中点击 **Apply**，然后在 GanttChart 对话框中点击 **Apply**。

GanttChart 始终在泳道 1 中收集数据。使用方法 `setData` 指定自己的数据，可将其分布到多个泳道上。

## Tab Parts [GanttChart]

在 **Parts** 选项卡上添加 GanttChart 要显示的零件。

**备注：**

- 首先取消勾选 **Inheritance** 复选框，使其显示为未选中状态；然后将要监视的零件类型从 Class Library 拖到选项卡的空行中。
- 也可以改为：在 Class Library 中选择零件，将其拖到 GanttChart 图标上并放下。这会自动停用继承，并将零件添加到 **Parts** 选项卡的空行中。

可以监视零件的类或零件的单个实例。可使用 *Context Menu of Embedded Lists* 上的命令编辑文本框内容。

## Tab Resources [GanttChart]

在 **Resources** 选项卡上添加 GanttChart 要显示的资源。

**备注：**

- GanttChart 将物料流对象视为资源，而不是资源对象。
- 若要监视仿真模型中的所有资源，请将 **Resources** 选项卡留空。GanttChart 随后显示仿真期间零件（在 **Parts** 选项卡上设置）所经过的所有资源。
- 首先取消勾选 **Inheritance** 复选框，使其显示为未选中状态；然后将要监视的资源类型从 Class Library 拖到选项卡的空行中。
- 也可以改为：在 Frame 中选择一个或多个资源，将其拖到 GanttChart 图标上并放下。这会自动停用继承，并将资源分别添加到 **Resources** 选项卡的空行中。

可以监视资源类或单个资源实例。可使用 *Context Menu of Embedded Lists* 上的命令编辑文本框内容。

## Tab User-defined（用户自定义选项卡）

按照 *Tab User-defined* 所述定义自己的属性。

## Navigate Menu（导航菜单）

命令在 *Navigate Menu* 中描述。

## View Menu（视图菜单）

命令在 *View Menu* 中描述。

## Tools Menu（工具菜单）

Tools Menu 提供以下访问其功能的命令：

- Edit Controls（编辑控件）
- Edit Observers（编辑观察者）

## Help Menu（帮助菜单）

命令在 *Help Menu* 中描述。

## GanttChart 的方法

GanttChart 提供：

- 左侧目录中列出的方法；
- 所有对象的方法（Methods of All Objects）。

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类（Class）的方法、只读属性和属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选实例（Instance）的方法、只读属性和属性。

## SimTalk 参考

### ZLabel [SimTalk]

设置由 `<Path>` 指定的 Chart 在 Chart 窗口中显示的 z 轴标签。

**备注：** 适用于 3D 图表类型 3D Columns、3D Wire Frame 和 3D Surface。

**类型：** 属性（Attribute）

**语法**

```
<Path>.ZLabel:string
```

**赋值：** 可赋值为 string 数据类型的值。

**示例**

```
MyChart.ZLabel := "Number of Stacked Rows"
```

**另请参见：** Z-Axis [text box] - Chart

### 引用的 SimTalk 方法与属性

- `CollectData [SimTalk]` - GanttChart
- `IsShown [SimTalk]` - GanttChart
- `setData [SimTalk]`
- `getData [SimTalk]`
- `setLanes [SimTalk]`
- `getLanes [SimTalk]`
- `ShowPartView [SimTalk]`
- `ShowResourceLabels [SimTalk]`
- `ShowBarText [SimTalk]`
- `ShowResourceStates [SimTalk]`
- `Parts [SimTalk]`
- `Resources [SimTalk]` - GanttChart
- `updateDialog [SimTalk]`

---

*来源：Plant Simulation Help 11-4838。Unpublished work. © 2026 Siemens。*
