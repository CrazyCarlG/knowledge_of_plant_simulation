# CostAnalyzer 对象 — General（总览）

> 本目录 `general/` 下只有一个 Markdown 文件 `general.md`（以及同名源文本 `general.txtx`），没有子文件夹，也没有其他 README.md。本文件是对 `general.md` 内容的总结。

## 概述

**CostAnalyzer**（成本分析器）对象用于分析各个机器（machines）和工人（Workers）所产生的成本。CostAnalyzer 计算设备中物流对象（material flow objects）在加工零件（Parts）过程中累计的成本。

### 说明（Description）

- CostAnalyzer 同时计算对象的**投资成本总和（summed-up investment costs）**。
- 你**无法对 CostAnalyzer 本身进行配置**——目前只能设置它是否收集数据（即 Collect Data 复选框），没有其他配置项。
- 将鼠标悬停在 CostAnalyzer 上可显示包含相关信息的工具提示（tooltip）。

### 显示分析结果

要显示成本分析结果，可将 CostAnalyzer 从 Frame 拖到 **HtmlReport** 的图标上并放下：

- 若 HtmlReport 的 **Content 为 inherited（继承）**，CostAnalyzer 的数据会**替换** HtmlReport 的预定义内容，Plant Simulation 会自动打开 HtmlReport 的显示窗口。
- 若 HtmlReport 的 **Content 不是 inherited**，CostAnalyzer 的数据会**追加**到 HtmlReport 的预定义内容之后，Plant Simulation 会自动打开 HtmlReport 的显示窗口。

也可以将 CostAnalyzer 对象拖入 HtmlReport 打开的窗口中并放下（例如放在 *Statistics* 标题下方），然后点击 **Show Report**。

> 分别在活动物流对象的 **Costs** 选项卡、**Part** 的 **Costs** 选项卡以及 **Container** 的 **Costs** 选项卡中键入相应成本。

### 添加对象到仿真模型

在 **Home** 功能区选项卡上依次点击：

> **Manage Class Library > Basic Objects > UserInterface > CostAnalyzer**

### 更改图形

要更改 CostAnalyzer 图形的长度和锚点，点击 **Edit** 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

## How the CostAnalyzer Assigns Costs to Part Types（CostAnalyzer 如何将成本分配到零件类型）

物流对象在仿真过程中会产生成本，这些成本来自**总投资成本**与**单位时间的总运营成本**。这些成本作为**累计成本（accrued costs）**分配到物流对象所加工的零件上。

### 备注（Remarks）

- 若物流对象上**没有零件**，成本会作为**一般成本（general costs）**分配到相应的物流对象上。
- 当 CostAnalyzer 计算其结果时，这些一般成本会分配到该物流对象在仿真过程中加工过的**零件类型（part types）**上。名称相同的零件归入同一个零件类型（MU Type）。Plant Simulation 使用零件到达 **Drain** 时所用的名称。

### 注意（Note）

- 对于**在制品（Work in process）**，最终生产成本未知，因此它们只以 **50 %** 计入生产成本。其假设是：在制品零件平均已完成其生产过程的一半左右。
- 正在通过生产过程的零件的成本并不精确。只有当 **Throughput（吞吐量）远高于 Work in process（在制品）** 时，单件成本才有意义。

### 各物流对象的成本分配方式

并非所有物流对象都按相同方式处理：

- **AssemblyStation（装配站）**：将成本分配给**主零件（main part）**；此前为安装零件累计的成本会转移到主零件上。
- **Conveyor（传送带）**：按零件的**长度比例**分配成本。
- **DismantleStation（拆解站）**：将成本分配给**主零件**。
- **ParallelStation（并行站）**：在其加工位之间**平均分配**成本。
- **Container（容器）**：若启用了 **Distribute costs**，则在各存储位之间**平均分配**累计成本。

此外，在仿真过程中，当新零件进入生产过程时，会产生**材料成本（material costs）**。

## Costs Shown in the Costs Report（成本报告中显示的成本）

HtmlReport 默认显示成本分析中的 **Investment Costs（投资成本）** 和 **Piece Costs（单件成本）** 两张表。

> 你无法对 CostAnalyzer 对象本身进行配置。要显示分析结果，可将 CostAnalyzer 对象拖入 HtmlReport 打开的窗口中并放下（例如放在 *Statistics* 标题下方），然后点击 **Show Report**。

### Investment Costs（投资成本）

**Investment Costs** 表按**层级结构（hierarchically structured）**显示插入模型中的物流对象的投资成本、折旧期（depreciation period）和运营成本。

- **注意：** HtmlReport **静态地**显示投资成本，即这些值在仿真运行期间不会变化。
- 对于层级中的 **Frames**，该表显示**累计（summed-up）投资成本**，以浅灰色高亮；第一行显示整个模型的累计投资成本。
- 对于层级中的 **sub-Frames（子 Frame）**，该表同样显示累计投资成本，以浅灰色高亮；第一行显示该子 Frame 的累计投资成本。

**SimTalk：** `putInvestmentCostsIntoTable`、`getInvestmentCostsTable`

### Piece Costs（单件成本）

**Piece Costs** 表显示仿真过程中各零件类型在单独各行累计的成本：

- **MU Type（零件类型）**：零件到达 Drain 时的名称。若零件在仿真运行期间更改名称（例如不同生产阶段），成本会分配给最终产品。
- **Material costs（材料成本）**：仿真过程中新零件进入生产时产生的成本。
- **Accrued costs（累计成本）**：零件在物流对象上加工时分配到的成本。
- **General costs（一般成本）**：物流对象在仿真期间空闲时产生的成本，会分配到该物流对象加工过的零件类型上。
- **Piece costs（单件成本）**：材料成本、累计成本与一般成本之和。
- **Throughput（吞吐量）**：已加工并流经生产线的零件数量。
- **Work in process（在制品）**：当前正在通过生产过程的零件数量，这些零件在计算单件成本时只计入一半。

所有成本均按**每件平均（averaged per piece）**计算。

**SimTalk：** `getPieceCostsTable`、`putPieceCostsIntoTable`

## CostAnalyzer 的对话框

双击 CostAnalyzer 图标即可打开其对话框。

### 编辑仿真属性（Edit Simulation Properties）

在对话框中可更改对象的仿真属性。共有属性见 *Dialog Items of the Objects*（对象的对话框项）。

### 编辑动画属性（Edit Animation Properties）

在 **Edit 3D Properties** 对话框中编辑对象的 3D 属性：

- 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮。
- 在模型中选择该对象并按空格键。

要操作对象的图形，点击 **Edit** 功能区选项卡中的 **Show Manipulators** 或按 `M` 键。

## Collect Data [复选框] — CostAnalyzer

勾选此复选框使 CostAnalyzer 在仿真运行期间收集数据；清除复选框可停用数据收集。

**SimTalk：** `CollectData`

## Investment Costs [按钮]

点击此按钮打开一个列表，其中包含 CostAnalyzer 计算出的投资成本。

**SimTalk：** `getInvestmentCostsTable`

## Piece Costs [按钮]

点击此按钮打开一个列表，其中包含 CostAnalyzer 计算出的单件成本。

**SimTalk：** `getPieceCostsTable`

## Tab User-defined

如 *Tab User-defined* 所述定义自己的属性。

## 菜单

- **Navigate Menu** —— 命令在 Navigate Menu 中说明。
- **View Menu** —— 命令在 View Menu 中说明。SimTalk：`updateDialog`。
- **Tools Menu** —— 提供访问其功能（Edit Controls、Edit Observers）的命令。
- **Help Menu** —— 命令在 Help Menu 中说明。

## CostAnalyzer 的方法

CostAnalyzer 提供：

- 左侧目录中所列的方法。
- **Methods of All Objects**（所有对象的通用方法）。

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 可显示所选类（Class）的方法、只读属性和属性。
- 按 `F8` 或点击插入实例的 Frame 的 **Home** 功能区选项卡中的 **Show Attributes and Methods** 可显示所选实例（Instance）的方法、只读属性和属性。

## 另请参阅

- Simulate the Accrued Costs of the Machines（模拟机器的累计成本）
- How the CostAnalyzer Assigns Costs to Part Types（CostAnalyzer 如何将成本分配到零件类型）
- Costs Shown in the Costs Report（成本报告中显示的成本）
- View the Costs Report（查看成本报告）
- Depreciation Period [文本框]
- Investment Costs [文本框]
- Investment Costs per Length [文本框]
- Operating Costs [文本框]
- Operating Costs per Length [文本框]
- Material Costs per Piece [文本框]
- Distribute Costs [复选框]
- Tools Menu [一般说明]

> 附注：源文件 `general.md` 开头包含一节 `Objects [SimTalk] - SankeyDiagram`，其内容描述的是 **SankeyDiagram** 对象的 `Objects` 属性（设置 SankeyDiagram 要可视化的零件或工人的桑基流），并非 CostAnalyzer 自身的属性，属于交叉引用残留。

---

*来源：Plant Simulation Help 11-4883–11-4901。未发表作品。© 2026 Siemens。*
