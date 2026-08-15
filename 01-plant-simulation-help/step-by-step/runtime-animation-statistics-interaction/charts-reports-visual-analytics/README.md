# Charts, Reports & Visual Analytics（图表、报告与可视化分析）总结

本目录对应 Plant Simulation 帮助文档（Step-by-Step Help）中 **查看与可视化统计数据（Viewing and Visualizing Statistics）** 章节，内容来源为 `charts-reports-visual-analytics.md`（以及其同名文本提取文件 `charts-reports-visual-analytics.txtx`）。本章介绍如何查看统计值，以及用 Chart、HtmlReport、Display、SankeyDiagram、GanttChart 等手段对统计数据进行可视化与报告输出。

## 目录结构

- `charts-reports-visual-analytics.md`：本章节的 Markdown 源文件。
- `charts-reports-visual-analytics.txtx`：相同内容的文本提取版本。
- `README.md`：本总结文件。
- 本目录无子文件夹，因此没有子文件夹 README.md 需要汇总。

---

## 1. 查看与可视化统计数据（Viewing and Visualizing Statistics）

- 默认情况下，所有物流对象（material flow objects）从仿真开始到结束都会收集统计值；清除选项卡 *Statistics* 上的 **Resource Statistics** 或选项卡 *Product Statistics* 上的 **Product Statistics** 复选框可禁用收集。物流对象还提供 **Energy Statistics** 值。
- **EventController** 控制统计收集的起始与重置：
  - 选项卡 *Settings* 的 **Statistics** 文本框设定重置时刻，届时删除此前收集的所有值（见 *Statistics Collection Period*），用于丢弃可能扭曲结果的预热阶段（warm-up phase）数据。
  - 点击 **Reset Simulation** 删除所有对象统计数据并把值归零；运行期间方法 `initStat` 可达到同样效果。

## 2. 在对象对话框中查看统计（View Statistics in the Dialogs of the Objects）

物流对象在选项卡 **Statistics** 上显示最重要的统计值。预选资源类型（resource type）：

| 资源类型 | 对象 |
|---|---|
| Production（生产） | Station、ParallelStation、AssemblyStation、DismantleStation |
| Transport（运输） | PlaceBuffer、Buffer、Sorter、Track、TwoLaneTrack、Conveyor、Transporter、Container |
| Storage（存储） | Store |

资源类型会影响移动对象（mobile objects）的统计。

> Working、Setting-Up、Waiting、Blocked、Powering up/down、Failed、Stopped、Paused、Unplanned 的百分比之和应为 100%。
> 对话框打开期间不会动态刷新运行中的数值，需在 View 菜单选择 **Refresh** 或按 **F5**。

### 统计表（Statistics Table）

| 项目 | 说明 |
|---|---|
| Working / Setting-up / Waiting / Blocked / Powering up/down / Failed / Stopped / Paused / Unplanned | 收集期内对象处于各状态的时间比例（Stopped 指被 LockoutZone 停止） |
| Relative Occupation | 基于容量的被占用时间（不含暂停/故障）相对可用时间的比例 |
| Relatively Empty | 对象相对可用时间处于空闲的比例 |
| Contents / Minimum Contents / Maximum Contents | 当前、最小、最大 MU 数量 |
| Entries / Exits | 进入 / 离开的 MU 数量（Container 按 1 计，不含内部） |
| Average Dwell Time | 零件在站点停留的平均时间（不含暂停/未计划时间） |

点击 Home 选项卡 **Show Statistics Report** 可查看收集值；大多数值可用其旁列出的方法查询。

### 能源统计（Energy Statistics）

点击能源图标打开独立对话框，含 Total Consumption、Working、Setting-up、Operational、Failed、Standby、Off 等能耗占比。能源状态相对总能耗而言，而同名资源状态相对统计收集期而言。选中对象并按 **F6** 可在 Statistics Report 中查看。

### 检查进出工厂的零件数量

- **Source**：选项卡 *Statistics* 选择 **Creation table** 并 **Open**，记录创建的 MU（列：Name、Path、Time of Generation）。
- **Drain**：选择 **Type Dependent Statistics**，记录同名 MU 的产品统计（各状态占比、Average Lifespan、Average Exit Interval、Total Throughput、Throughput per Hour/Day 等）。

### 检查站点统计与内容列表

- 所有物流对象显示标准统计；**AssemblyStation** / **DismantleStation** 额外显示 Waiting for parts、Waiting for resources，表 *Waiting Times* 按前驱对象显示等待时间总和。
- 通过 **View > Contents** 打开内容列表；点对象按容量显示，ParallelStation 按 x-y 坐标显示，长度导向对象（Conveyor、Track、TwoLaneTrack、Transporter）显示 Object/From/To 列。内容列表在模型重置时被删除，可用 `contentsList` 配合 `copyToTable` 保存到表，旧版写法为 `Buffer.contentsList(ContentsListBuffer)`。

### 零件产品统计 / Exporter 与 Worker 统计

- 所有 MU（Part、Container、Transporter）在选项卡 **Product Statistics** 显示在各资源上等待/工作的时间百分比；Container 与 Transporter 因能装载运输零件也提供资源统计。
- **Exporter** 与 **Worker** 的 *Statistics* 选项卡显示服务与出口值（各块合计 100%）；Exporter 选中 **Fail Services** 后也收集服务故障时间。关键值含 Services 各状态、Exporter 各状态、Free/Mediated Capacity 及最小最大值（有效值出现前显示 `-1`）。

### 查看统计报告（Statistics Report）

选中多个对象（Shift+点击或框选）后按 **F6** 打开，报告按状态拆分资源统计（合计 100%）。状态条颜色：绿=Working、棕=Setting-Up、灰=Waiting、黄=Blocked、紫=Powering up/down、红=Failed、粉=Stopped、蓝=Paused、浅蓝=Unplanned。悬停列标题可查看只读属性名；**Save** 导出 HTML/文本，**Refresh** 更新，**Print** 打印。

## 3. 用图表展示统计（Show Statistics in a Chart）

从 Class Library 的 *UserInterface* 文件夹或 *User Interface* 工具栏插入 **Chart**，显示来自表或输入通道（动态记录属性值）的数据。

- 拖放数据源：物流对象/Portioner/DePortioner → 统计值；PlaceBuffer/Buffer/Store → MU 数量频率分布；DataTable/TimeSequence/MaterialsTable → 表内容；Variable → 变量值。
- **Statistics Wizard**（右键 Chart）可批量选择对象类、资源类型、是否包含子 Frame、排序依据。
- **Data Source**：**Input Channels**（用 Data Table 定义通道）或 **Data Table**（用 `{*,*}..{*,*}` 等 Range 语法选取单元格）。
- **Update mode**：**Sample**（按 Interval 周期更新）、**Watch**（可监视值变化时更新）、**Plot**（每个仿真事件更新）。
- 类别：Chart、3D Chart、Histogram、3D Histogram、Plotter、XY Graph。

### 图表类型与显示选项

图表类型含 Columns、Stacked/100% Stacked Columns、Bars、Stacked/100% Stacked Bars、Area 系列、Line 系列、Spline、Markers、Points and Best Fit、Pie、XY 系列、3D Columns/Wire Frame/Surface 等。显示选项含 Graph/Table/Graph and Table、3D Effect、背景/桌面颜色、Display in Frame、Gap When Null、Print/Copy to Clipboard、网格线、y 轴 Range（默认 `0 … 0` 自动缩放）等。

### 标签、图例与标注（Annotations）

- 可输入 Title、Subtitle、x/y 轴文本并选择图例位置；图例文本写在输入通道表的行索引。
- 标注类型：`0` 竖线、`1` 横线、`2` X 轴标签、`3` Y 轴标签、`4` 文本；含 Value、From/To、Color、Style、Text 等列。文本可用 `|l`、`|L`、`|r`、`|R`、`|c` 前缀定位。

## 4. 在报告（HtmlReport）中展示统计及其他数值

**HtmlReport**（*UserInterface*）把所有仿真结果呈现为 HTML 页面。在选项卡 **Content** 用方括号语法配置。关键语法：

- `[ObjectName]` 引用对象；`[!self, iconName, *]` 显示图标；`[=function]` 公式；`[Object.Attribute]` 属性值；`[TableName]` 或 `[.Path.To.Object*]` 显示表/DataTable 内容。
- `#` / `##` 标题；`1.` 编号列表；`*` 项目符号；`**text**` 加粗；`><[current, "caption"]` 或 `><[Chart, w, h]` 居中截图；`---` 水平线；支持 HTML 标签。

## 5. 在层次化模型中展示报告（Show Reports in a Hierarchically Structured Model）

- 在每个子 Frame 中插入名为 `ReportObject` 的 HtmlReport，Plant Simulation 会在方括号引用 Frame 时自动使用它。
- 在总体 HtmlReport 中用 `[CarBody, #]`、`[PaintShop, #]` 等插入子报告，`#` 使子报告标题降一级（`##` 降两级）。
- 构建示例（汽车装配模型）：创建 CarBodyCell、PaintShop、AssemblyLine 等类，复制 Comment 为自定义类 `ToDo`；车身单元含 Buffer/AssemblyStation/Chart 直方图，喷漆线含 Conveyor，装配线含 Conveyor/Station/Workplace，安装部分用 Sequence Cyclical 的 PartsTable 供料；各层分别配置 ReportObject。
- 运行后在 HtmlReport 右键 **Show**；可在 HtmlReport 上定义 `endSim` 方法（`self.~.show`）在仿真结束后自动显示。
- 目录默认显示四级标题，属性 **TOCLevels** 可减少；点击 ToDo 链接打开 Comment 对象，用 **Navigate > Open Location** 跳转。

## 6. 仿真期间用 Display 展示数值

**Display**（*UserInterface*）在整个运行期间显示属性、方法或 Variable 值（如 `buffer.numMU`）。支持 boolean、integer、real、string、object、time、money、length、weight、speed、date、datetime 等类型；无效路径文本框背景变红。可选 Comment；Update mode 为 Sample 或 Watch。显示方式：Text、Bar、Pie（Bar/Pie 仅数值，相对 Min/Max 显示）；支持 Transparent 与颜色设置。

## 7. 用 SimTalk 访问统计（Accessing Statistics with SimTalk）

大多数统计值可通过方法、只读属性和属性访问，只读属性名列于 Statistics Report 说明中每个值旁。另见 *Read-Only Attributes for Accessing Statistics*、*Attributes for Statistics*、*Methods for Accessing Statistics of the MUs*、*_Attributes of All MUs*。

## 8. 用 SankeyDiagram 展示零件流 / AGV 流

- **零件/Worker 流**：建模 Source、Roughing、FineMachining、Drain，用 Broker、WorkerPool（Travel Mode）、Workplaces、FootPaths 配置搬运，配置 Parts 与 Worker 两个 SankeyDiagram，运行后右键 **Show** 查看。
- **AGV 流**：复制 AGVPool、Marker、Transporter（重命名 `AGV`），用 `init` 方法通过 `setRoute` 设置路线，拖 AGVPool 到 SankeyDiagram，运行后 **Show Diagram** 查看蓝色条状路线（较粗条表示共享路线）。

## 9. 用 GanttChart 展示资源上的零件

**GanttChart**（*UserInterface*）显示零件如何在资源（物流对象）之间移动。配置 Source（按 Delivery Table 供料）、ParallelStation（处理时间、故障，需清除 Start Processing When Full）、激活 Collect Data 并拖入零件与资源，运行后 **Show Chart**。提供 **Resource view**（纵轴资源）与 **Part view**（纵轴零件）两种视图；显示顺序按首次处理顺序且不可更改。

---

*来源：Plant Simulation Help — "Viewing and Visualizing Statistics"。Unpublished work. © 2026 Siemens.*
