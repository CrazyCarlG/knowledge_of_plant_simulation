# DePortioner — 概述

本文件汇总了 `general` 目录下 Markdown 文档（`general.md`）的内容。该目录无子文件夹，因此不包含子目录中的 README.md。

> 对象 **DePortioner** 用于将到达的散装物料或流体零件（MU）倒空，从中生成流体，并将生成的流体送入 **Pipe**。

## 说明（Description）

提供三种定义待生成流体的方式：

- **按固定物料与固定数量（每个 MU）**：在此设置下可输入 *Material* 与 *Amount per MU*。
- **按 MU 名称（MU Name）**：取决于 *Mapping Table* 中定义的 MU 名称。
- **按 MU 属性（MU Attribute）**：在此设置下可输入 MU 的 *Material Attribute* 与 *Amount Attribute*。

其他要点：

- 生成的流体流出 DePortioner 进入 Pipe 后，提供它的 MU 将被删除。
- 若因故障、暂停或后继对象暂时无法接收而导致流体流出中断，Exporter 不会被释放。
- 典型用途：将盛装流体或散装物料的桶（barrels）倒空，作为后续生产线上混合产品的原料，并将物料送入 Pipe。
- 可将 DePortioner 视为 **Portioner** 的对应物（counterpart）。
- 将鼠标悬停在 DePortioner 上可显示工具提示；在 Edit 功能区点击 **Show Manipulators** 或按 `M` 键可调整图形长度与锚点。

### 添加到仿真模型

点击 Home 功能区的 **Manage Class Library > Basic Objects > Fluids > DePortioner**。

对比示例模型：点击 Window 功能区，**Start Page > Getting Started > Example Models > Small Examples**，然后在 *Examples Collection* 对话框中选择相应 Category、Topic 与 Example，点击 **Open Model**。

## 对话框（Dialog Box）

双击 DePortioner 图标打开其对话框。

- **Edit Simulation Properties**：修改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties**：在 **Edit 3D Properties** 对话框中编辑对象的 3D 属性（通过仿真属性对话框左下角的 **Edit 3D Properties** 按钮，或选中对象后按空格键）。
- 要操纵对象图形，点击 Edit 功能区的 **Show Manipulators** 或按 `M` 键。

## 属性选项卡（Tab Attributes）

- **Outflow Rate（出流速率）**：物料在倒空到达零件后流出 DePortioner，并经 Pipe 流向下一对象的速度，单位为升/秒。
  - 当前出流速率取决于所连接的 Pipe 数量：连接两条 Pipe 时，每条 Pipe 都会按该速率流出（前提是连接 Pipe 的出流速率允许）。若只想让指定量流出对象，则连接一条 Pipe，之后再拆分。
  - SimTalk：`OutflowRate`
- **Fluid Depends On（流体取决于）**：选择 DePortioner 如何定义待生成流体的物料与数量，可选：
  - **Fixed**：在 *Material* 与 *Amount per MU* 中设置物料与每 MU 数量。
  - **MU Name**：在 *Mapping Table* 中设置物料与每 MU 数量。
  - **MU Attribute**：在 *Material Attribute* 与 *Amount Attribute* 中设置物料与每 MU 数量（需自行创建的 MU 用户自定义属性）。
  - 各物料名称需在 *MaterialsTable* 中定义。
  - SimTalk：`FluidDependsOn`
- **Material（物料）**：输入 DePortioner 生成的物料名称；仅当 *Fluid Depends On* 选择 *Fixed* 时适用。SimTalk：`Material`
- **Amount per MU（每 MU 数量）**：输入 DePortioner 生成的流体总量（升）；仅当 *Fluid Depends On* 选择 *Fixed* 时适用。SimTalk：`AmountPerMU`
- **Mapping Table（映射表）**：输入映射表名称，其中包含到达 MU 的 MU Name 及 DePortioner 生成的流体的 Material 与 Amount；仅当 *Fluid Depends On* 选择 *MU Name* 时适用。可点击选择。SimTalk：`MappingTable`
- **Material Attribute（物料属性）**：输入用户自定义物料属性名称，用于定义 DePortioner 生成的流体；仅当 *Fluid Depends On* 选择 *MU Attribute* 时适用。SimTalk：`AttrNameMaterial`
- **Amount Attribute（数量属性）**：输入用户自定义数量属性名称，用于设置 DePortioner 生成的流体数量；仅当 *Fluid Depends On* 选择 *MU Attribute* 时适用。SimTalk：`AttrNameAmount`
- **Materials Table（物料表）**：包含 DePortioner 可生成的各种物料数据。点击省略号按钮在 *Select Object* 对话框中选择，或从 Frame 拖动到文本框。SimTalk：`MaterialsTable`
- **Current Amount（当前数量）**：显示当前位于 DePortioner 中的流体数量。SimTalk：`CurrentAmount`
- **Current Outflow Rate（当前出流速率）**：显示每秒流出 DePortioner 的流体升数。SimTalk：`CurrentOutFlowrate`

## 时间选项卡（Tab Times）

按 “Tab Times” 所述定义时间。从下拉列表选择分布并输入所需数值；也可选择常量时间（`Const`）。可用方法 `setTypeAndAttr`（SimTalk）设置分布类型及完整参数集。

## 设置选项卡（Tab Setup）

按 “Tab Set-Up” 所述定义设置对象的属性。

## 故障选项卡（Tab Failures）

按 “Tab Failures” 所述定义故障。

## 控制选项卡（Tab Controls）

提供用于修改对象内置行为的控件。

- **选择现有 Method 的路径**：点击省略号按钮，在 *Select Object [for controls]* 对话框中导航选择 Method，或从 Frame 拖动 Method 到文本框；在文本框中按 `F2` 打开 Method 并输入控件源代码。
- **创建作为对象方法的控件（Control）**：输入有意义名称后选择 **Create Control**（上下文菜单），Plant Simulation 会插入 `self.<输入的名称>`（如 `self.A1Ctrl`）；或对空文本框选择 **Create Control**，插入 `self.On<内置控件名>`（如 `self.OnEntrance`）。
- 后续编辑：按 `F2`，或按住 `Shift` 双击文本框，或选择上下文菜单 *Open Object*，或点击 *User-defined* 选项卡双击列表中的 Method 名称。
- 删除控件需删除用户自定义属性；仅删除文本框中的名称不会删除该属性。

## 统计选项卡（Tab Statistics）

DePortioner 按 “Tab Statistics” 所述显示资源统计（resource statistics）。

## Importer 选项卡（Tab Importer）

在 *Importer* 选项卡上定义用于处理零件、为特定类型零件设置工位以及维修工位的服务。

查看 Importer 统计报告的方式：

- 在对象对话框中选择 **View > Show Statistics Report**。
- 在 Frame 中右键点击对象，选择 *Show Statistics Report* 或按 `F6`。
- 点击 Home 功能区的 **Show Statistics Report** 按钮。

## 用户自定义选项卡（Tab User-defined）

按 “Tab User-defined” 所述定义自有属性。

## 菜单（Menus）

- **Navigate Menu**：见 Navigate Menu 说明。
- **View Menu**：提供访问其功能的命令，包括与 Transport Importer 相关的命令（Exporters、Unavailable Services、Services、Associated Workplaces）。
- **Tools Menu**：见 Tools Menu 说明。
- **Help Menu**：见 Help Menu 说明。

## DePortioner 的方法（Methods）

DePortioner 提供：

- 流体对象（Fluid Objects）的方法。
- 所有对象（All Objects）的方法。

可通过 **Show Attributes and Methods** 窗口查看全部方法、只读属性和属性：

- 在 Class Library 上下文菜单中选择 *Show Attributes and Methods*，查看所选类（Class）的方法、只读属性和属性。
- 按 `F8` 或点击 Frame 的 Home 功能区 *Show Attributes and Methods*，查看所选实例（Instance）的方法、只读属性和属性。

## SimTalk 参考

### PredecessorNumber [SimTalk]

设置向 `<Path>` 指定的 Portioner 提供物料的前置对象编号。

- **类型**：属性（Attribute）
- **语法**：`<Path>.PredecessorNumber:integer`
- **赋值**：可赋整数值。

```simtalk
MyPortioner.PredecessorNumber := 2
```

另见：Fluid from Predecessor [文本框]、DePortioner。

## 另见（See Also）

- Portion and Deportion Materials
- Configure the DePortioner
- Dialog Box of the DePortioner
- MaterialsTable
- Select Object [for controls]
- Tab Importer [general description]
