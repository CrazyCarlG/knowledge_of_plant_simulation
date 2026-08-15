# Chart 对象（General）

本目录汇总 **Chart** 对象的一般说明（`general.md` / `general.txtx`）。本目录无子文件夹。

## 概述

**Chart** 用于在 Frame 中可视化当前数据与仿真运行结果。可在 Frame 中插入一个 Chart，将数据以图表形式呈现。

要绘制的数据可通过两种方式定义：

- 使用包含数据的 **Table**（例如仿真结果）。
- 定义 **Input Channels**（输入通道），记录对象中感兴趣的属性值。

添加到模型：Home 功能区 → *Manage Class Library > Basic Objects > UserInterface > Chart*。

常用操作：

- 鼠标悬停 Chart 显示提示信息。
- 将 **WorkerPool** 拖到 Chart 上，显示其管理的 Worker 的统计信息。
- 点击 Edit 功能区 *Show Manipulators*（或按 `M`）修改图形长度与锚点。

---

## Statistics Wizard（统计向导）

插入 Frame 的 Chart 提供统计向导。通过 Frame 上下文菜单 *Statistics Wizard* 打开。

- 选择要显示统计的对象类；Chart 仅添加在 **Statistics** 选项卡上勾选了 **Resource Statistics** 的物流对象。
- **Inherit Settings**：继承设置。
- **Class** 组：选择要显示的对象类，可多选。
- **Resource Type**（对象 Statistics 选项卡）限制显示的对象：
  - **Production**：Source、Drain、Station、ParallelStation、AssemblyStation、DismantleStation 的默认值。
  - **Transport**：PlaceBuffer、Buffer、Sorter、Track、TwoLaneTrack、Conveyor、AngularConverter、Turntable、Transporter、Container 的默认值。
  - **Storage**：Store 的默认值。
- **Sort Criterion**：
  - *Name*：按名称字母顺序排序。
  - 手动拖动对象到 Chart 以自定义顺序。
  - 之后可通过剪切/粘贴 Input Channels 表中的列重新排序。
- **Statistics type**：Resource Statistics、Energy Statistics 或 Occupancy。
- **Include Subframes**：同时显示子 Frame 中的对象。
- **Reapply at Init**：模型初始化时重新应用设置。

将物流对象拖到未配置的 Chart 上时，需选择统计类型（默认 Resource 或 Occupancy；激活能量功能后可选择 Energy）：

- **Resource**：显示对象名称及状态 Working、Setting-Up、Waiting、Blocked、Powering up/down、Failed、Stopped、Paused、Unplanned。
- **Energy**：显示 Working、Setting-up、Operational、Failed、Standby、Off（能量状态值指总能耗，资源状态值指统计采集期）。
- **Occupancy**：显示对象名称及位于其上的零件数量，用彩色条区分对象。

图表画面也可显示在 **HtmlReport** 中。

---

## Drag-and-Drop（拖放）

| 要完成的操作 | 拖放源 | 拖放目标 | 加速键 |
|---|---|---|---|
| 显示单个物流对象统计 | 物流对象 | Chart | `*` |
| 显示多个物流对象统计 | 物流对象 | Chart | `*` |
| 显示 Transporter 的 Driving 统计 | Transporter | Chart | `*` |
| 显示 Worker/Exporter 的 Services 统计 | Worker/Exporter | Chart | `*` |
| 显示 Worker/Exporter 的 Exporter 统计 | Worker/Exporter | Chart | `Shift` |
| 显示 WorkerPool 管理的 Worker 统计 | WorkerPool | Chart | — |
| 显示 MU 数量的频率分布 | PlaceBuffer、Buffer 或 Store | Chart | `*` |
| 显示 Supermarket 各零件类型频率分布 | 配置为 Supermarket 的 Store | Chart | — |
| 显示分配给 LockoutZone 的所有资源统计 | LockoutZone | Chart | `*` |
| 显示表格内容 | DataTable、TimeSequence | Chart | — |
| 显示 Frame 中 Variable 的值 | Variable | Chart | `*` |
| 显示带 `StatisticsObject` 属性的 Frame 统计 | 用户自定义对象（Frame） | Chart | `*` |
| 显示带 `AOLType` 属性的 Frame 中 Workplace 统计 | 用户自定义对象（Frame） | Chart | `*` |

`*` 表示拖放时按住 **Shift** 会删除输入通道中已有条目，而不是添加新对象。

- 方法 **`addObject`** 与上述拖放操作等效。
- 删除单个显示对象：点击 Data Source 旁的 **Data Table** 并删除。
- 删除整个输入通道表：拖放新对象时按住 **Shift**。
- 让自定义 Frame 拖放时像内置对象：创建数据类型为 **object** 的用户属性并命名为 `StatisticsObject`；若需显示多个对象统计，则将该属性设为 **table** 类型，且第一列必须为 **string** 类型。

---

## 对话框

双击 Chart 图标打开对话框：

- **Edit Simulation Properties**：共享属性见 *Dialog Items of the Objects*。
- **Edit 3D Properties**：点击仿真属性对话框左下角按钮，或选中对象后按空格键。

---

## Show Chart 按钮

点击显示 Chart 采集的数据：

- 双击显示窗口任意处打开 Chart 对话框。
- 右键 Frame 中的 Chart 并选择 **Show**。
- 拖出选择矩形可缩放感兴趣区域。

**Chart 窗口键盘加速键：**

| 操作 | 按键 |
|---|---|
| 单色/彩色视图切换 | `S` |
| 显示导出对话框 | `X` |
| 最大化窗口 | `M` |
| 缩放全部（无滚动条显示全部数据） | `Z` |
| 显示文本/数据导出对话框 | `D` |
| 显示打印对话框 | `P` |
| 滚动垂直/水平滚动条一行 | 方向键 |
| 垂直滚动条翻页 | `PgUp`/`PgDown` |
| 水平滚动条向右翻页 | `Shift+PgUp` |
| 水平滚动条向左翻页 | `Shift+PgDown` |
| 垂直滚动条移到起始 | `Home` |
| 垂直滚动条移到末尾 | `End` |
| 水平滚动条移到最左 | `Shift+Home` |
| 水平滚动条移到最右 | `Shift+End` |

**SimTalk:** `IsShown`

---

## Collect Data 复选框

勾选使 Category 为 **Histogram** 或 **Plotter** 的 Chart 在仿真运行期间采集数据；取消勾选停用采集。

**SimTalk:** `CollectData`

---

## Tab Data

在 Data 选项卡选择 **Data Source** 与 **Mode**。

### Data Source

- **Data Table**：将 DataTable 内容显示为图表。
  - 输入表名称/路径，或点击按钮在 *Select Object* 中选择。
  - **Range**：单元格范围，如 `{*,*}..{*,*}`、`{1,1}..{1,4}`、`{1,1}..{1,*}`、`{-2,*}..{-2,*}`、`{-2,*}..{*,*}`。
- **Input Channels**：显示输入通道表中的通道（属性/方法的路径，或方法调用、公式、求和等复杂表达式）。
  - 指定公式时直接输入单元格（不要点击 List 功能区的公式按钮）。
- **Worker Pools**：显示 WorkerPool 管理的 Worker。
  - 按 **Pool**（整个 WorkerPool）或 **Creation Table**（*Workers to Create* 表中的 Worker）分组。
  - Occupancy 统计：**Operational + failed** 或 **Overall Time**。

**SimTalk:** `DataRange`, `DataTable`, `InputChannels`, `UseInputChannels`

### Data

选择数据展示方式：**In Rows** 或 **In Columns**。

**SimTalk:** `DataInColumn`

### Mode

- **Sample Mode**：按输入的时间间隔周期性更新。
- **Watch Mode**：可监视的输入数据变化时更新（见 *Show Attributes and Methods* 的 *Watchable* 列）。
- **Plot Mode**：发生仿真事件时更新。

**SimTalk:** `update`, `NumIntervals`, `Mode`, `SampleInterval`

---

## Tab Display

- Category **Histogram**：可显示 **Accumulated** 数据。
- Category **Plotter**：可显示为 **Step Curve**。

### Category 下拉列表

- **Chart**：一个或几组数值。
- **Histogram**：一个或多个输入通道的频率分布（可用 *Accumulated*）。输入通道应为可监视类型以获得精确值。
- **Plotter**：一个或多个值随时间的变化（可用 *Step Curve*）。
- **3D Chart**：嵌入 3D 显示窗口的 3D 图（不能单独开窗）。
- **3D Histogram**：嵌入 3D 显示窗口的 3D 直方图。
- **XY Graph**：x-y 数值对（仅当 Data Source 为 **Table File** 时有效）。x 值在第一行/列；范围决定 y 值。

**SimTalk:** `Category`, `putValuesIntoTable`, `resetValues`

### 3D Chart / 3D Histogram 特性

- 固定 **Font Size**（仅 *Bold* 生效）；宽/高 > 5 m 时字号绝对固定，更小时按比例缩小。
- 对 Chart Type **Line** 使用 Color 选项卡的 **Color** 与 **Line Weight**；无 Marker Type 或 Line Style。
- 将 Background 与 Desk 的 **Opacity** 设为 0 可隐藏底板/背景（透明图表/直方图）。
- 底板厚度默认 20 cm（Background 透明度为 0 时为 10 cm）；尺寸 < 5 m 时按比例缩小。

### Chart Type 下拉列表

| 类型 | 说明 |
|---|---|
| Columns | 每条记录为一列，多记录并排 |
| Stacked Columns | 列上下堆叠 |
| 100% Stacked Columns | 堆叠列显示 100% 百分比 |
| Bars | 水平条，多记录并排 |
| Stacked Bars | 水平堆叠条 |
| 100% Stacked Bars | 水平条显示 100% 百分比 |
| Area | 区域前后堆叠 |
| Stacked Area | 区域上下堆叠 |
| 100% Stacked Area | 区域显示 100% 百分比 |
| Line | 每条记录为一条线 |
| Line with Markers | 带标记的线 |
| Spline | 每条记录为一条曲线 |
| Spline with Markers | 带标记的曲线 |
| Markers | 每条记录为一组不同标记 |
| Points and Best Fit Conveyor | 数据点 + 最佳拟合直线（最小二乘） |
| Points and Best Fit Curve | 数据点 + 最佳拟合曲线（最小二乘） |
| Pie | 饼图，切片显示占整体百分比 |
| XY Points | x-y 对作为数据点 |
| Line | x-y 对连线 |
| Sticks | 每个 x-y 对从零线起的垂直条 |
| Area | 连接 x-y 点并填充区域 |
| 3D Columns | 3D 空间堆叠柱（可用 Rotation/Height 转动） |
| 3D Wire Frame | 3D 空间堆叠线框 |
| 3D Surface | 3D 空间堆叠实体面 |

**SimTalk:** `ChartType`, `Rotation`, `Height`

### 3D Effect

**None**、**Shadow**（黑色阴影）、**3D**（3D 深度）、**Gradient Bars**（用于 Columns 和 Bars）、**Contoured**（用于 3D Columns 和 3D Surface）。

**SimTalk:** `Effect`

### Graph/table 下拉列表

- **Graph**：仅以图形显示记录。
- **Table**：仅以表格显示记录。
- **Graph and Table**：同时显示图形与表格。

**SimTalk:** `GraphTable`

### Display in Frame 复选框

在 Frame 中直接显示 Chart（而非图标）。输入 **Width** 与 **Height**，设置 **3D Image Quality**。

**SimTalk:** `DisplayInFrame`

### Width / Height 文本框

激活 *Display in Frame* 后输入宽/高（单位：米）。

**SimTalk:** `SizeInFrame`

### 3D Image Quality 下拉列表

仅 *Display in Frame* 时可用：**High quality**、**Balanced**、**High performance**。

**SimTalk:** `ImageQuality3D`, `DisplayInFrame`

### Gap When Null 复选框

未定义值时中断折线（取消则继续连线）。**Undefined Value**：视为未定义的值（默认 `-999999`）。

**SimTalk:** `GapWhenNull`, `NullValue`

### Accumulated 复选框

创建累积直方图（累加之前所有值；最后一个值为 100%）。仅 Category **Histogram**。

**SimTalk:** `Accumulated`

### Step Curve 复选框

用阶梯曲线代替直线。仅 Category **Plotter**。

**SimTalk:** `StepCurve`

---

## Tab Axes

根据 Category 不同，设置不同。

### Grid Lines Y-Axis

显示/隐藏 Y 轴网格线。**Interval** 设置水平网格线与标签间距（留空 = 自动）。

**SimTalk:** `XGrid`, `YGrid`, `YGridLineInterval`

### Grid Lines X-Axis

显示/隐藏 X 轴网格线。**Number** 设置最多显示的网格线数。Category **XY-Graph** 时，仅当 Range X 固定（无星号）才评估 Number。

**SimTalk:** `XGrid`, `YGrid`, `XGridlines`

### Logarithmic Y-Axis

激活 Y 轴对数刻度（适合跨多个数量级的数据；不能显示负值）。要求 Range Y > 0（如 `0.1`）。

**SimTalk:** `YLog`

### Logarithmic X-Axis

X 轴对数刻度（仅 Chart Type **XY-Graph**；并非所有图表类型都显示）。

**SimTalk:** `XLog`

### Number of Values 文本框

每通道随时间采集的值的数量（Category **Plotter**）。达到数量后丢弃最早的值。

**SimTalk:** `NumValues`

### Scrollbar 复选框

为 Category **Plotter** 的 Chart 窗口添加滚动条。激活后可输入 **Feed Rate**。

**SimTalk:** `ScrollBar`

### Feed Rate 文本框

Chart 到达右边界时滚动的网格单位数（Plotter）。取值 `0.1`（平滑）到 `12`（整页）。

**SimTalk:** `FeedRate`

### Step Size 文本框

频率分布区间的宽度（Category **Histogram**）。

**SimTalk:** `StepSize`

### Range Y

Y 轴范围首末值。默认 `0 … *`（0 到最大值）。用 `*` 表示开区间/半开区间：

| 输入 | 含义 |
|---|---|
| `* … *` | 最小到最大显示值 |
| `0 … *` | 0 到最大显示值 |
| `* … 7.5` | 最小显示值到 7.5 |
| `-20 … 20` | -20 到 +20 |

**SimTalk:** `YScaleMin`, `YScaleMax`, `XScaleMin`, `XScaleMax`

### Range X

X 轴范围首末值。默认 `0 … 0` 显示整个定义域。用 `*` 表示开区间/半开区间（示例见 Range Y）。**Histogram** 的 Range X 定义定义域（右侧输入 `0` 自动调整，配合 Step Size）；**Plotter** 的 Range X 定义显示的时间跨度。

**SimTalk:** `XScaleMin`, `XScaleMax`, `XRange`, `FirstInterval`, `NumIntervals`, `StepSize`

---

## Tab Labels

输入 **Title**、**Subtitle** 及 **X-Axis**、**Y-Axis**、**Z-Axis** 标签，选择 Legend 位置与 Annotations。

- **Title**：图表标题。**SimTalk:** `Title`
- **Subtitle**：图表副标题。**SimTalk:** `SubTitle`
- **X-Axis**：X 轴文本。**SimTalk:** `XLabel`
- **Y-Axis**：Y 轴文本。**SimTalk:** `YLabel`
- **Z-Axis**：Z 轴文本（仅 3D 图表类型）。**SimTalk:** `ZLabel`

> 注意：若未指定 Title 或 Subtitle，Y 范围上部可能被截断；在 Subtitle 输入一个空格可避免。

### Legend

图例位置：**Off**、**On the Right**（一行/两行/堆叠）、**On the Left**（一行/两行）、**At the Top**（一行/两行）、**At the Bottom**（一行/两行）。

**SimTalk:** `LegendLocation`

### Annotations 按钮

打开 Annotations 表添加线条与文本。设置项：

- **Type**：`0` 垂直线，`1` 水平线，`2` X 轴标签，`3` Y 轴标签，`4` 文本。
- **Value**：线条显示的位置（水平线/Y 轴为 Y 值；垂直线/X 轴为 X 值）。
- **From** / **To**：线条起止点（可创建对角线）。
- **Color**：颜色编号（在 Tab Color 定义）。
- **Style**：线型（类型 0/1）或标记样式（类型 4）。

| 值 | 线型 | 标记样式 |
|---|---|---|
| 0 | 细实线 | 仅文本，无标记 |
| 1 | 虚线 | 加号 |
| 2 | 点线 | 叉号 |
| 3 | 点划线 | 圆 |
| 4 | 双点划线 | 实心圆 |
| 5 | 中等细实线 | 方形 |
| 6 | 粗实线 | 实心方形 |
| 7 | 网格刻度 | 菱形 |
| 8 | 网格线 | 实心菱形 |
| 9 | 无 | 上三角 |
| 10 | 中等粗实线 | 实心上三角 |
| 11 | 特粗实线 | 下三角 |
| 12–24 | 无 | 各种小三角/圆/方/菱形标记 |
| 25–36 | 无 | 大标记 |
| 92–99 | 无 | 北/东北/东/东南/南/西南/西/西北箭头 |

- **Text**：描述文本，可选两位前缀码（`|` + 字母）：

| 前缀 | 位置 |
|---|---|
| `|l` | 图内左边缘 |
| `|L` | 图外左边缘 |
| `|r` | 图内右边缘 |
| `|R` | 图外右边缘 |
| `|c` | 图内居中 |

用户自定义注解始终显示在前景。

**SimTalk:** `getAnnotations`, `setAnnotations`

---

## Tab Color

为 **Grid**、**Background**、**Desk**、**Text**、绘图数据（编号 1–14）及附加颜色选择颜色。可添加/删除颜色，设置 **Opacity**、**Line Style**、**Line Weight**、**Marker Size**。

**SimTalk:** `setColor`, `setLineStyle`, `getColor`, `getLineStyle`

### Color

| 项目 | 编号 |
|---|---|
| Grid | -3 |
| Background | -2 |
| Desk | -1 |
| Text | 0 |
| 颜色（预定义输入通道） | 1–14 |

双击 Color 框打开 MS Windows *Colors* 对话框。

### Opacity

`0` = 完全透明，`255` = 完全不透明。

### Line Style / Line Weight / Marker Type

配置线条属性（用于 Chart Type **Line** 和 **Spline**；**Marker Type** 用于 **Line with Markers** 和 **Spline with Markers**）。

**SimTalk:** `setLineStyle`, `getLineStyle`

### Add / Delete

向颜色表添加额外颜色；删除所选颜色。

### Marker Size

选择标记大小（用于 **Line with Markers** 和 **Spline with Markers**）。

---

## Tab Font

为 **Labels**、**Title**、**Subtitle**、**Table** 数据选择字体、文本效果与缩放因子。

- **Labels**：标签字体。**SimTalk:** `LabelFont`
- **Title**：标题字体。**SimTalk:** `TitleFont`
- **Subtitle**：副标题字体。**SimTalk:** `SubtitleFont`
- **Table**：表格数据字体。**SimTalk:** `TableFont`

字号数字是缩放因子，而非实际磅值。

---

## Tools Menu

### Use Metric Prefix

在 Y 轴显示单位前缀（如 `100K` 代替 `100000`）。前缀：p（pico）、n（nano）、u（micro）、m（milli）、K（kilo）、M（million）、B（billion）、T（trillion）。

**SimTalk:** `UseMetricPrefix`

### Reset Values

删除 Chart 采集的所有值。**SimTalk:** `resetValues`

### Print

打开打印对话框。**SimTalk:** `showPrintDialog`

### Copy to Clipboard

将 Chart 窗口内容复制为位图。**SimTalk:** `copyBitmapToClipboard`

---

## 方法（Methods）

Chart 提供上述方法及 **所有对象的通用方法**。可通过 **Show Attributes and Methods**（类库上下文菜单，或 Frame 中按 `F8`）查看全部方法、只读属性与属性。

文中引用的关键 SimTalk 方法/属性：

`addObject`, `IsShown`, `CollectData`, `DataRange`, `DataTable`, `InputChannels`, `UseInputChannels`, `DataInColumn`, `update`, `NumIntervals`, `Mode`, `SampleInterval`, `Category`, `putValuesIntoTable`, `resetValues`, `ChartType`, `Rotation`, `Height`, `Effect`, `GraphTable`, `DisplayInFrame`, `SizeInFrame`, `ImageQuality3D`, `GapWhenNull`, `NullValue`, `Accumulated`, `StepCurve`, `XGrid`, `YGrid`, `YGridLineInterval`, `XGridlines`, `YLog`, `XLog`, `NumValues`, `ScrollBar`, `FeedRate`, `StepSize`, `YScaleMin`, `YScaleMax`, `XScaleMin`, `XScaleMax`, `XRange`, `FirstInterval`, `Title`, `SubTitle`, `XLabel`, `YLabel`, `ZLabel`, `LegendLocation`, `getAnnotations`, `setAnnotations`, `setColor`, `setLineStyle`, `getColor`, `getLineStyle`, `LabelFont`, `TitleFont`, `SubtitleFont`, `TableFont`, `UseMetricPrefix`, `showPrintDialog`, `copyBitmapToClipboard`, `updateDialog`
