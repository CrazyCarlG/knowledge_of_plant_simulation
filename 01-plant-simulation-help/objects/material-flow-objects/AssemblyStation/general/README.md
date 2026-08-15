# AssemblyStation — General（概述）

本目录存放 **AssemblyStation**（装配站）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. AssemblyStation 对象概述

**AssemblyStation** 用于将**安装部件（mounting parts）**添加到**主要工件（main MU）**上，例如将车门装配到车身。

- AssemblyStation 根据你在 **Assembly Table（装配表）**中输入的值，将安装部件移动到主要 MU 上，或将其删除。安装部件也可称为装配部件、附加部件、附件等。
- 用 AssemblyStation 建模装配流程。若装配流程需要服务，可指定 AssemblyStation 请求安装部件与服务的顺序。
- 若要**拆卸**部件，可使用 **DismantleStation**。

**顺序装配模式：** 若 AssemblyStation 使用装配表，并为每个安装部件指定了 **Assembly Time（装配时间）** 与 **Sequence Number（序号）**，则它按顺序装配安装部件：

- 每个安装部件消耗其指定的装配时间；全部装配完成后，主要工件的加工时间（Processing Time）结束，随后离开工位。
- 从**最低序号**开始装配，依次递增；当前装配序列中仅需要的安装部件才可进入 AssemblyStation；同一序列内按进入顺序装配。

> **注：** 不能通过信息流（即使用 Method）将部件移动到 AssemblyStation！

- 将鼠标悬停在 AssemblyStation 上可显示工具提示；点击编辑功能区标签页的 **Show Manipulators**（或按 `M`）可更改图形长度和锚点。

**添加到模型：** Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > AssemblyStation`。

**示例模型：** Window 功能区标签页 → `Start Page > Getting Started > Example Models > Small Examples`。

## 2. AssemblyStation 对话框

双击 AssemblyStation 图标打开对话框。

- **编辑仿真属性：** 共享属性见 *Dialog Items of the Objects*。
- **编辑动画属性：** 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮，或选中模型中的对象并按空格键；点击 **Show Manipulators**（或按 `M`）操纵图形。

## 3. 选项卡 Attributes（属性）

在该选项卡上设置 AssemblyStation 如何将安装部件装配到主要工件上。

### Assembly Table（装配表）

选择 AssemblyStation 是否使用装配表以及使用哪种类型。

> **注：** 主要 MU 已位于 AssemblyStation 上时，无法更改装配表；如需更改，须在工位 Entrance Control 中勾选 **Before Actions**。

选择装配表类型后点击 **Open** 输入所需信息：

- **None** — 不使用装配表，而是期望每个前驱对象各提供一个部件。
- **Predecessors（前驱）** — 在第 1 列输入移动该部件的前驱编号，第 2 列输入 Amount（数量；缺省为 1）。
  - Amount 输入 `-1`：接受该前驱的部件，直到主要 MU 容量被占满。
  - 若使用主要部件编号的部件作为安装部件，将主要 MU 编号加入装配表。
- **MU Types** — 在第 1 列输入部件 MU 名称（如 Part、Container、Transporter、Shaft），第 2 列输入 Amount。
  - 输入的是部件**名称**而非路径，例如 `MyMountingPart`，而非 `*.UserObjects.MyMountingPart`。
  - Amount 输入 `-1`：接受该 MU 名称的部件直到主要 MU 容量被占满。
- **Depends on Main MU（取决于主要 MU）** — 输入主要 MU 名称。
  - 输入星号 `*` 处理所有未单独列出的主要部件；输入 MU 名称与部件 Amount。
- **Fill up Main MU（填满主要 MU）** — 不使用装配表，而是接受任意前驱的部件，直到主要 MU 容量被占满。

各表类型的**共同列**（Predecessors、MU Types、Depends on Main MU）：

- **Assembly Time（装配时间）：** 每个部件装配所消耗的时间（秒），须为正数或 0，缺省为 0。
- **Sequence Number（序号）：** 装配顺序编号，须为正整数，缺省为 1。
- 若**非顺序装配**，将 Assembly Time 与 Sequence Number 两列留空。

> **注（MU Types 与 Depends on Main MU）：** 若前驱为 Store 类型对象，AssemblyStation 会从 Store 请求所需安装部件；若部件暂缺，Store 会记录请求并在可用后送达。部件也可由 Worker 从 Store 搬运到 AssemblyStation。Store 只能提供安装部件（不能提供主要部件），且必须用 Connector 连接（即使由 Worker 搬运）。

**SimTalk：** `AssemblyTable [SimTalk]`、`AssemblyTableMode [SimTalk]`

### Workers Sequentially Deliver MUs to Assemble（Worker 顺序递送待装配 MU）

勾选后，Worker 将 AssemblyStation 请求的安装部件**逐个顺序**递送。该设置可防止多个 Worker 走到 AssemblyStation 后因工位无法接收而无法递送、存放部件——Plant Simulation 会在 AssemblyStation 上为安装部件预留加工位置。

> **注：** 勾选后属性 `ReservedFor` 返回当前预留位置对应的部件；取消勾选后 `ReservedFor` 返回预留位置对应部件的数组。

- 取消勾选：单个 Worker 可一次递送尽可能多的部件；或多个 Worker 并行递送。

**SimTalk：** `SequentialDelivery [SimTalk]`、`ReservedFor [SimTalk]`

### Main MU from Predecessor（来自前驱的主要 MU）

输入将主要 MU 移动到 AssemblyStation 的**前驱对象编号**。

- 输入 `0`：主要部件不由任何前驱递送（例如由 Worker 运输，或用 SimTalk 命令移动）。
- 前驱是通过 Connector 连接、在模型工位序列中位于所选对象之前的对象。AssemblyStation 至少连接两个工位，**连接顺序**很重要；若装配流程异常，请检查前驱编号。
- 拖动鼠标悬停在 Connector 上可查看对象的前驱/后继工具提示。

**SimTalk：** `MainMU [SimTalk] - AssemblyStation`

### Assembly Mode（装配模式，下拉列表）

选择 AssemblyStation 如何处理 MU：

- **Attach MUs** — 将安装部件装配到主要 MU 上。
- **Delete MUs** — 装配操作完成后删除安装部件。

**SimTalk：** `AssemblyMode [SimTalk]`

### Exiting MU（离开 MU，下拉列表）

选择 AssemblyStation 如何处理离开工位的 MU：

- **Main MU** — 将主要 MU 移动到后继对象。
- **New MU** — 将装配后的新 MU 移动到后继对象。选择后显示按钮与文本框 **MU**，点击打开 *Select Object* 选择新 MU；当工件载体（Workpiece Carrier）进入时，用新 MU 替换各个工件。

**SimTalk：** `ExitingMU [SimTalk]`、`NewMU [SimTalk] - AssemblyStation`

### Sequence（请求顺序，下拉列表）

选择 AssemblyStation 请求部件和/或服务的顺序：

- **MUs then Services** — 先请求 MU，后请求服务。当所有安装部件可用后才请求服务；服务请求完成后，设置与加工操作开始。
- **Services then MUs** — 先请求服务，后请求 MU。服务在主要部件到达前（准备离开前驱工位时）即被请求；安装部件到达时 Exporter 已就位。若服务不可用，安装部件不会被移动或删除，工位记录特殊的阻塞时间。
- **MUs and Services** — 同时请求 MU 与服务。

> **注：** AssemblyStation 在主要 MU 进入或尝试进入时请求设置服务。若服务立即可用，Services then MUs 与 MUs and Services 行为一致；若服务不可用，安装部件仍会被移动然后删除。

**SimTalk：** `OrderSequence [SimTalk]`

## 4. 选项卡 Times（时间）

按 *Tab Times* 说明定义时间。从下拉列表选择分布类型并输入所需值（参数显示在选项卡上边界）；也可选择恒定时间（**Const**）。分布类型与参数可用方法 `setTypeAndAttr [SimTalk]` 设置。

## 5. 选项卡 Set-Up（设置）

按 *Tab Set-Up* 说明定义对象设置（set-up）的相关属性。

## 6. 选项卡 Failures（故障）

按 *Tab Failures* 说明定义故障。

## 7. 选项卡 Controls（控制）

提供修改对象内置行为的控制项。

- **选择已有 Method 的路径：** 点击省略号按钮，在 *Select Object [for controls]* 中导航选择；在文本框中按 `F2` 打开 Method，或将 Method 从 Frame 拖入文本框。
- **创建对象方法作为控制：**
  - 在文本框中输入有意义名称并选择 **Create Control** —— 插入 `self.你输入的控制名`（如 `self.A1Ctrl`）。
  - 在空文本框上选择 **Create Control** —— 插入 `self.On内置控制名`（如 `self.OnEntrance`）。
- **编辑源代码：** 按 `F2`、按住 `Shift` 双击文本框、在上下文菜单选择 **Open Object**，或使用 **User-defined** 选项卡。删除控制需删除相应用户自定义属性（仅从文本框删除名称不会删除该属性）。

## 8. 选项卡 Exit（出口）

选择对象将 MU 移动到哪个后继。

## 9. 选项卡 Statistics（统计）

统计按 *Tab Statistics* 说明描述。此外，AssemblyStation 还收集以下统计值：

| 项（英文） | 说明 | 只读属性 | 项（德文） |
| --- | --- | --- | --- |
| Waiting Parts | 统计收集周期内 AssemblyStation 等待安装部件（Waiting 状态）的时间占比。 | `StatWaitingPartsPortion [SimTalk]` | Warten auf Teile |
| Waiting Resources | 统计收集周期内 AssemblyStation 等待 Exporter 和/或安装部件的时间占比。 | `StatWaitingResPortion [SimTalk] - AssemblyStation` | Warten auf Ressourcen |

查看统计报告：`View > Show Statistics Report`，右键 Frame 选择 **Show Statistics Report**，或按 `F6`。

**相关 SimTalk 属性：** `StatWaitingResPortion`、`StatWaitingResCount`、`StatWaitingPartsPortion`、`StatWaitingResDelta`、`StatWaitingPartsCount`、`StatWaitingResMu`、`StatWaitingPartsDelta`、`StatWaitingResTime`、`StatWaitingPartsMu`、`statWaitingTimePerPredecessor`、`StatWaitingPartsTime`、`statWaitingTimeTable`（均为 `[SimTalk]`，部分标注 `- AssemblyStation`）。

### Waiting Times（等待时间）

点击该按钮打开 Waiting Times 表，显示**每个前驱**安装部件的等待时间总和。

> **注：** 仅显示安装部件的等待时间，主要部件的等待时间恒为 0。

> **注：** 仅当装配表设为 **None** 或 **Predecessors** 时显示；设为 MU Types 或 Depends on Main MU 时按钮不可用（不收集这些等待时间）。

**SimTalk：** `statWaitingTimeTable [SimTalk]`

## 10. 选项卡 Importer（导入）

定义加工工件、为某种工件类型设置工位以及维修工位的服务。查看 Importer Statistics：`View > Show Statistics Report`，右键 Frame 选择 **Show Statistics Report**，按 `F6`，或点击 Home 功能区标签页的 **Show Statistics Report**。

## 11. 选项卡 Energy（能源）

选择能源设置。

## 12. 选项卡 Costs（成本）

选择成本设置。AssemblyStation 将安装部件添加到主要部件期间，成本由投资成本与运营成本之和累积：

- 投资成本仅在**折旧期（Depreciation Period）**内累积。
- 成本作为**应计成本（accrued costs）**分配到主要部件上；此前已累积到安装部件上的成本会转移到主要部件。
- 若 AssemblyStation 空闲，成本作为**一般成本（general costs）**保留在 AssemblyStation 上。

## 13. 选项卡 User-defined（用户自定义）

按 *Tab User-defined* 说明定义自定义属性。

## 14. 菜单

- **Navigate 菜单：** 命令见 Navigate Menu 说明。
- **View 菜单：** 命令见 View Menu 说明；另提供 **MUs To Be Deleted**（SimTalk：`updateDialog`）。
- **Tools 菜单：** 命令见 Tools Menu 说明。
- **Tabs 菜单：** 显示/隐藏所选物料流对象的各个选项卡；隐藏不用的选项卡可加快对话框打开与切换速度；点击 **OK** 关闭并重新打开对话框以应用更改；**Inherit** 命令切换显示/隐藏选项卡的继承。
- **Help 菜单：** 提供 `Contents`、`Help on Object`。

### MUs To Be Deleted（待删除 MU）

打开位于 AssemblyStation 上、当主要部件离开时将被删除的 MU 列表。

**SimTalk：** `muToBeDeleted [SimTalk]`、`musToBeDeleted [SimTalk]`、`NumMUsToBeDeleted [SimTalk]`

## 15. AssemblyStation 的方法

AssemblyStation 提供：

- 左侧目录中列出的方法；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

查看方式：打开 **Show Attributes and Methods**（在类库上下文菜单中选择）查看全部方法、只读属性和属性。

## 目录说明

- `general.md`：AssemblyStation 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
