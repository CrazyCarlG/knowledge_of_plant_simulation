# Pull Systems, Carriers, and Line Balancing

本目录涵盖 Plant Simulation 帮助文档中关于**拉动式物料流**（Pull Material Flow）、**堆叠零件**、**工件载具**（Workpiece Carriers）以及**生产线平衡**（Line Balancing）的主题。

> 内容来源：`pull-systems-carriers-line-balancing.md`

---

## 目录

1. [将 Store 用作超市（Supermarket）](#1-将-store-用作超市supermarket)
2. [在 Store 中堆叠零件](#2-在-store-中堆叠零件)
3. [使用工件载具（Workpiece Carriers）](#3-使用工件载具workpiece-carriers)
4. [平衡生产线](#4-平衡生产线)

---

## 1. 将 Store 用作超市（Supermarket）

Store 可以作为**超市**（Supermarket）来表示*拉动式*物料流。在此场景中，Store 从 Source 订购两种不同的零件类型，仅当这些零件的库存低于某个阈值时，Source 才开始生产。

**启用方式：**

- 在 Store 中激活 **Supermarket** 选项。
- 在 Source 中选择 **MU Selection > Order Controlled**。

Store 随后将这些零件送往 AssemblyStation，由后者将它们装载到相应的托盘上并继续流转。

**建模步骤：**

- 按图示插入物料流对象（Store、SourceParts、AssemblyStation、托盘等）。
- 将 **Part** 和 **Container** 各复制两份，重命名为 `PartRed`、`PartBlue` 和 `PalletRed`、`PalletBlue`，并设置相应颜色。
- 将 Station 的**加工时间**从 10 秒缩短为 2 秒（`0:02`）。
- 配置 AssemblyStation：仅输入零件名称（而非路径）。
- 将 AssemblyStation 的**加工时间**从 10 秒缩短为 5 秒（`0:05`）。
- 在 Source1 和 Source2 中输入相应托盘。

**配置 Store 与 Source：**

- Store 对话框：勾选 **Supermarket**，点击 **Configuration** 填写配置表：
  - `PartRed` 和 `PartBlue` 的**最小库存**为 2、**最大库存**为 6、**初始库存**为 3。
  - 供应商为名为 `SourceParts` 的 Source。
  - 仿真期间 `Current` 列显示 Store 中零件的实际数量。
- Source 对话框：选择 **MU selection > Order Controlled**。

> **注意：** 若仿真无法启动，请检查 AssemblyStation 的 **Main part from predecessor no** 设置。

**查看等待零件与订单数量：**

- Store 初始各含 3 个零件，被装载到托盘上。当达到最小库存时，Store 向 Source 重新订购，Source 此时才开始生产。
- Source 的 **View > Show Orders** 显示待处理订单（含零件类型、数量、目标）。
- Store 的 **View > Show Orders** 显示该 Store 的待处理订单。
- 将配置为 Supermarket 的 Store 拖到 Chart 上，默认显示配置表中所有零件的占用情况。

---

## 2. 在 Store 中堆叠零件

可以在 Store 中堆叠零件，只需设置 Store 的 **Z-Dimension**。

示例中 Source 生产零件并送往 Conveyor，Robot 将零件从 Conveyor 卸下并放入 Store。

- Source 与 Conveyor 使用默认设置。
- Robot：**加载时间**和**卸载时间**各为 1 秒（`0:01`），**Default Angle** 为 180 度。
- Store 每个维度可存储 4 个零件。

**逐层装载 Container：**

默认情况下，Plant Simulation 会将零件在 Container 的每个装载位上堆叠到最大 Z 尺寸，然后再在新的装载位开始新的一层。

通过激活 **Fill Whole Layer** 可实现**逐层装载**：

- **未激活**（默认）：先在一个 Container 上堆满零件，再开始新的一层。
- **激活**：一层装满后，Plant Simulation 即开始新的一层。

---

## 3. 使用工件载具（Workpiece Carriers）

可将 Container 用作**工件载具**，勾选对话框中的相应选项后，Plant Simulation 会考虑装载在其上的工件（MU），而非载具本身。这会影响零件的**加工时间**和**设置时间**等。

示例展示了工件载具与 AssemblyStation 的结合使用（主零件附着在工件载具上）：

- 两个 Source 各生产一个 Container，用作工件载具。
- 在 Source 的 **Entrance Control** 中，额外生产一个 Container（主零件），附着到第一个 Container（工件载具）上。
- 两个 Conveyor 将主零件（附着在工件载具上）运送到 Station，该 Station 按 `SetUpTable` 设置、按 `ProcessingTable` 加工零件。
- 随后 Container 经另一条 Conveyor 运往 AssemblyStation。
- AssemblyStation 由两个附加 Source 供给两种不同的附加零件，并将附加零件装配到工件载具上的主零件上。
- AssemblyStation 最后将装配完成的零件送往 Drain。

**配置工件载具、主零件与附加零件：**

- 在 Class Library 的 **MUs** 文件夹中复制 Container 并重命名为 `WorkpieceCarrier`。
- 再复制 Container 两次，重命名为 `MainPartA`、`MainPartB`。
- 复制 Part 两次，重命名为 `AddOnPartA`、`AddOnPartB`。
- WorkpieceCarrier：在 3D 中交换为堆叠箱图形。
- MainParts：略小于蓝色堆叠箱，以便附着到工件载具；设置 Transformation/Appearance 与 MU Animation。
- AddOnParts：删除默认图形，创建简单圆柱体，分别设置颜色。

**配置 Source：**

- `SourceCarrierA` 生产 `MainPartA` 的工件载具，其 Entrance Control 使用指令：

```simtalk
.UserObject.MainPartA.create(@)
```

- `SourceCarrierB` 类似，使用 `MainPartB`。

**配置加工 Station 与表：**

- 使用 `List(Type)` 类型的 DataTable `SetUpTable` 设置**设置时间**。
- 使用 `List(Type)` 类型的 DataTable `ProcessingTable` 设置**加工时间**。
- Plant Simulation 会自动将 DataTable 格式化为两列：MU 类型与相应时间。

**配置附加零件 Source 与 AssemblyStation：**

- 附加零件 Source 选择 `AddOnPartA`、`AddOnPartB` 作为生产的 MU。
- AssemblyStation 的 **AssemblyTable** 中设置相应 AddOnPart 装配到对应的 MainPart。

最后插入 Drain 并用 Conveyor/Connector 连接各对象，Drain 设置恒定加工时间 1 分钟。

**运行与查看结果：** Source 先创建工件载具（蓝色堆叠箱），再创建主零件（紫色/橙色板）；加工后 AssemblyStation 将附加零件装配到主零件上。工件载具的 Product Statistics 显示离开 AssemblyStation 后的结果。

---

## 4. 平衡生产线

**Cycle** 对象同步生产线中零件在各工位之间的传送。仅当满足以下条件时，才将零件送往平衡线中的下一工位：

- 所有工位均已完成零件加工。
- 没有工位发生故障、暂停或处于非计划状态。
- 平衡线的后继对象已准备好接收零件。

从 Class Library 的 **MaterialFlow** 文件夹或 Toolbox 的 **MaterialFlow** 工具栏插入 **Cycle** 对象。

**打开 2D 创建的生产线模型：**

- 输入第一个和最后一个工位的名称来定义平衡线。
- 两者之间所有通过 Connector 连接的工位构成平衡线。
- 每个工位必须只有一个前驱和一个后继。

> **注意：** 只能平衡由 **Station** 和 **AssemblyStation** 类型对象构成的生产线。当平衡线中包含 AssemblyStation 时，Cycle 仅在装配过程完成后才继续平衡。

- 将 Station/AssemblyStation 拖放到 Cycle 图标上即可设为第一个工位；再拖放另一个设为最后一个工位。
- 通过对比平衡线与不平衡线的 Drain 的 **Type Statistics** 选项卡来观察差异。

**将生产线模型转换为 3D 模型：**

1. 将 MU `TableLeg`、`TableTop` 保存为对象文件 `TableLeg.psobj`、`TableTop.psobj`。
2. 将 DataTable `TableLegs`、`TableTops` 导出为 `TableLegTable.psobj`、`TableTopTable.psobj`（含设置颜色的属性）。

然后打开 2D 模型 `MyBalancedLine.spp`：

- 另存为 `My3DBalancedLine.spp`。
- 在 Model Settings 中选择 **Visualization > 3D only**。
- 若某些对象（如 DataTable）未显示，可在 Class Library 中选中该对象，按 F8，双击 `CreateIn3D` 使其为 `true`。
- 恢复标准图形：按住 Shift 右键 Class Library 中的 **Basis**，选择 **Revert all Objects to Standard Graphics**，随后需重新导入仿真设置与图形。

**导入仿真设置与图形：** 通过 Class Library 中 Models 文件夹的 **Save/Load > Load Object** 导入 `TableLeg.psobj`、`TableTop.psobj`，并重命名原类与新导入类。

**导入生产表内容：** 在 Frame `TableAssembly` 中打开生产表，点击 **Import File** 选择 `TableLegTable.psobj` 或 `TableTopTable.psobj`，使颜色正确。最后调整对象位置并插入注释 "Balanced Line" 与 "Non-Balanced Line"。
