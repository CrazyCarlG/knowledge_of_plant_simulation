# Cost and Power Analysis（成本与能耗分析）

本目录对应 Plant Simulation Help 中「Cost and Power Analysis」一节，涵盖两大主题：

1. **Simulating the Accrued Costs of the Machines** —— 模拟机器的累计成本
2. **Simulating the Power Consumption in Your Facility** —— 模拟工厂的能耗

> 目录内容说明：本目录当前包含 `cost-power-analysis.md`（结构化正文）与 `cost-power-analysis.txtx`（原始文本导出，含原帮助页码及导航信息），二者内容一致，无子文件夹。

---

## 一、模拟机器的累计成本（Accrued Costs）

使用 **CostAnalyzer** 对象模拟机器的累计成本。可在材料流对象、**Part** 和 **Container** 的 **Costs** 选项卡中输入相应成本，并用 CostAnalyzer 对工厂中活跃材料流对象、Part 及 Container 产生的成本进行分析。

演示流程分为四步：

### 1. 指定传送带成本（Specify the Costs of the Conveyors）

- 为展示子 Frame（sub-Frame）的成本如何被汇总，模型的一部分建在名为 `SubFrame` 的子 Frame 中。
- 分别录入 **Conveyor1**、子 Frame 中的 **Conveyor**、以及连接 **AssemblyStation** 与 **Drain** 的 **Conveyor** 的成本。

### 2. 指定站点与零件成本（Specify the Costs of the Stations and the Parts）

- 为展示子 Frame 内容而非图标，在子 Frame 的 **Graphics** 选项卡上激活 **Show Content**（3D 下）。
- 录入 **Station1** 成本（附 10 分钟固定加工时间）、子 Frame 中 **Station** 成本（附 15 分钟固定加工时间）、**AssemblyStation** 成本。
- 为零件类型 **Part** 与 **MyMountingPart** 录入成本。
- 为 **SourceMainParts** 与 **SourceMountingParts** 配置创建间隔。

> **注意：** 在装配表（Assembly Table）中只输入装配零件的名称，而非完整路径。

### 3. 配置成本报告（Configure the Costs Report）

- CostAnalyzer 本身不可配置。将 **CostAnalyzer** 拖放到 **HtmlReport** 图标上以显示分析结果。
  - 若 HtmlReport 的 Content 为继承（inherited），CostAnalyzer 的数据会**替换**预定义内容并自动打开显示窗口。
  - 若 Content 非继承，CostAnalyzer 的数据会**追加**到预定义内容之后并自动打开显示窗口。
- 也可将 CostAnalyzer 拖入 HtmlReport 的打开窗口（例如标题 *Statistics* 之下），点击 **Show Report** 时还会显示预定义的 *General Information*。
- 该操作会向 HtmlReport 添加如下指令：

```html
# Statistics
## CostAnalyzer
[CostAnalyzer]
```

### 4. 查看成本报告（View the Costs Report）

HtmlReport 按所设配置展示成本报告：

- **Investment Costs（投资成本）表：** 不可用单元格中显示该 Frame 的汇总投资成本；下方逐行列出各对象的投资成本、折旧期与运营成本。可用方法 `putInvestmentCostsIntoTable` 查询。
- **Piece Costs（单件成本）表：** 显示所用 MU 类型（本例为 Part）的汇总单件成本，含以下字段：
  - **MU Type（零件类型）**：零件到达 Drain 时的名称（仿真中改名时，成本计入最终产品）。
  - **Piece costs（单件成本）** = 材料成本 + 累计成本 + 一般成本，共 **8.32 €**。
  - **Material costs（材料成本）**：新零件进入生产时产生，**8.00 €**。
  - **Accrued costs（累计成本）**：零件在材料流对象上加工时计入，**0.17 €**。
  - **General costs（一般成本）**：材料对象空闲时产生，**0.15 €**，按加工过的零件类型分摊。
  - **Throughput（吞吐量）**：10,650 件。
  - **Work in process（在制品）**：6 件。

在 CostAnalyzer 对话框中点击 **Investment Costs** 或 **Piece Costs** 可查看对应成本，也可分别用 `putInvestmentCostsIntoTable` / `putPieceCostsIntoTable` 查询。

---

## 二、模拟工厂能耗（Power Consumption）

针对能源成本上升与资源枯竭问题，Plant Simulation 提供能耗追踪功能。**Energy** 选项卡提供两类能耗评估：

- 单台机器的功耗
- Frame 内所有对象的总功耗

演示流程分为五步（多数材料流对象使用默认设置，仅录入能耗相关设置，并为部分对象定义故障）：

### 1. 配置加工站点与传送带（Configure the Processing Stations and the Conveyor）

- **Source**：供料，默认设置不变。
- **Station**（第一台机器）：每件加工 1 分钟，录入各状态功耗及状态切换时间。
- **Station1**（第二台机器）：每件加工 2 分钟，录入各状态功耗及切换时间，并定义故障配置。
- **Conveyor**：将零件从 Station1 运往 ParallelStation，录入各状态功耗及切换时间，并定义故障配置。长度型对象 Conveyor 的能耗设置少于点型对象 Station / ParallelStation。
- **ParallelStation**（第三台机器）：每件加工 1 分钟，录入各状态功耗及切换时间。
- **Drain**：出料，默认设置不变。
- **Charts**：显示所选对象的资源统计图与能耗统计图。

### 2. 配置班次日历（Configure the ShiftCalendar）

- 插入 **ShiftCalendar** 控制人与机器的工作时段，默认班次时间不变，仅录入材料流对象。
- 操作：按住 **Shift** 框选对象，再将其拖放到 ShiftCalendar 上。

### 3. 在对象对话框中查看功耗（Check the Power Consumption in the Dialogs）

1. 双击对象图标，点击 **Statistics** 选项卡。
2. 点击 **Energy Statistics** 查看各能耗构成的详细数值。

### 4. 在统计报告中查看功耗（Check the Power Consumption in the Statistics Report）

- 在 **StatisticsReport** 的下拉列表中选择 **Energy Statistics**，查看总能耗及各能耗状态占比。

> **注意：** 材料流对象的能耗状态（energy states）与同名的资源状态（resource states）含义不同——资源状态值对应统计采集周期，能耗状态值对应总能耗。

### 5. 在图表中查看功耗（Check the Power Consumption in the Chart）

1. 选择要在 Chart 中显示的对象。
2. 将其拖放到 Chart 上。
3. 在弹出对话框中选择 **Statistics Type > Energy Statistics** 并点击 **OK**。
