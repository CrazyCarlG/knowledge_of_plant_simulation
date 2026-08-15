# 自由流动物料与流体仿真（Free-Flowing Materials and Fluids）

本目录介绍 Plant Simulation 中用于模拟**自由流动物料（Free-Flowing Materials）**的 **Fluid Objects（流体对象）**。这类物料可以是**液态、气态或可倾倒形态**，流体对象尤其适用于**食品饮料**和**制药**行业。

目录内包含两个内容一致的文档：

- `free-flowing-materials.md` —— 整理后的 Markdown 版本（建议阅读）
- `free-flowing-materials.txtx` —— Siemens Plant Simulation Help 的原始帮助文本

> 更完整的模型可参考示例模型库：`Window > Start Page > Getting Started > Example Models > Small Examples`，在 Examples Collection 中选择对应 Category / Topic / Example 并点击 **Open Model**。

---

## 概述

文档通过四个示例演示如何使用 Fluid Objects 建模：

1. **巧克力棒生产建模（Model the Production of Chocolate Bars）**
2. **连续混合果汁和水（Continuously Mix Juice and Water）**
3. **物料的份装与反份装（Portion and Deportion Materials）**
4. **按固定顺序生产流体（Produce Fluids in a Fixed Sequence）**

通用要点：

- 流体对象之间必须用 **Connector（连接器）** 连接，不能只靠 **Pipe（管道）**。
- 配方（材料、密度、颜色、产量、成分及用量）统一定义在 **MaterialsTable（物料表）** 中，供 FluidSource、Mixer 等对象引用。
- 若后续在 MaterialsTable 中修改物料/成分名称，需手动同步修改 FluidSource 的 `Material` 文本框、Mixer 的 `Product` 文本框、DePortioner 的 `Material` 文本框等，Plant Simulation 不会自动更新。

---

## 示例 1：巧克力棒生产建模

一条简单的巧克力棒生产线。三种基础物料（牛奶、糖、可可）由 **FluidSource** 提供，经 **Pipe** 流入各自的 **Tank** 暂存，再进入第一个 **Mixer** 混合成中间产品（基础巧克力），随后泵入下一个 **Mixer** 搅拌到所需稠度，最后进入第三个 **Mixer**，掺入由独立 FluidSource（`SourceChili`）供应的辣椒粉，得到辣椒巧克力。辣椒巧克力流入 **Portioner** 浇注成单个巧克力棒，再由 **Conveyor** 运送到 **Drain** 移出工厂。

**演示步骤：**

- **配置 MaterialsTable 中的配方**：录入基础产品、中间产品及最终产品的密度、颜色、产量和所需成分。
- **配置供料的 FluidSource**：为牛奶、糖、可可各插入一个 FluidSource，在 `Material` 文本框填入材料名称。
- **配置储料的 Tank**：为每种材料设置 `Outflow Rate`（流出速率）和 `Volume`（容积），并用 Pipe + Connector 连接。
- **配置转化的 Mixer**：插入三个 Mixer，分别设置流出速率、容积、`Product` 名称及 `Times` 选项卡上的处理时间。
- **配置供精炼料的 Source**：插入 `SourceChili`，`Material` 填 `ChiliPowder`，连接到 `MixerFinal`。
- **配置浇注的 Portioner**：选择 MU 产品 `ChiliChocolate`，设置 `Amount per MU`（每块 0.1 升）；在类库中新建 `ChiliChocolate` MU 类表示巧克力棒。
- **配置 Conveyor 并运行仿真**：Conveyor 速度设为 40 m/s，插入默认设置的 Drain；为使巧克力棒正确显示，在类库中右键 `ChiliChocolate` → Edit 3D Properties → Transformation → 勾选 Scale Automatically。
- **改变管道形状**：通过编辑 Pipe 的 **Segments** 表（追加行、插入行、F7 打开外观表等）弯曲管道，实现与真实管道一致的形状；其中 `Pipe8`（SourceChili 到 MixerFinal）用无缝连接。

---

## 示例 2：连续混合果汁和水

一条生产 **Apfelschorle**（苹果汁 + 气泡水混合饮料）的简单产线。两种 FluidSource 分别提供苹果汁和气泡水，经 Pipe 流入 **ContinuousMixer** 混合，成品流入 **Tank** 暂存待灌装。

**演示步骤：**

- **配置混合配方**：在 MaterialsTable 中录入材料、产品量、单位、成分 1/2 及其单位，并为各材料选择颜色；在对应 FluidSource 中填入 `AppleJuice` 和 `SparklingWater`。
- **配置 ContinuousMixer 并运行仿真**：在 `Materials Table` 文本框填入 `Apfelschorle`；Tank 使用默认设置（流出速率 1 L/s，容积 3000 L）；用 Pipe + Connector 连接并运行仿真，观察 Tank 侧面出料阀旁的液位指示器。

---

## 示例 3：物料的份装与反份装

用 **Mixer** 将两种原料混合成两种产品，产品经 **Portioner** 分装成 MU，由 Conveyor 运到 **DePortioner**，DePortioner 将产品拆解后分别流入各自的 Tank（可再由罐车取走）。该模型展示了如何用 Conveyor 将流体/散装货物的运输与常规连续物料流衔接起来。

**演示步骤：**

- **创建所需零件**：在类库 MUs 中复制 Parts，重命名为 `ForX` 和 `ForY`，设置 MU 尺寸、颜色，并启用 Scale Automatically。
- **配置 MaterialsTable 配方**：录入材料、密度、颜色、产量及两种成分的用量；当 Mixer 的产品量与 MaterialsTable 不同时，Plant Simulation 会按配方比例自动调整成分用量。
- **配置供料 FluidSource**：原料 1 流出速率 2 L/s，原料 2 为 1.5 L/s。
- **配置缓冲 Tank**：每个 Tank 流出速率 1 L/s、容积 5 L，并设置两个传感器及其控制、Reset 控制（用 `self.~.EntranceLocked` 控制入口锁定）。
- **配置混合 Mixer**：流出速率 1 L/s、容积 6 L、产品名、处理时间、Init Control（确保首个混合产品固定），并为只读属性 `ResWorking` 和 `Empty` 创建 observer 以切换配方。
- **配置分装 Portioner**：选择 MU `ForY`，每 MU 装 2 升。
- **配置 DePortioner**：在 Portioner 与 DePortioner 之间插入 Conveyor；流出速率默认 1 L/s；选择 `Fluid Depends On > MU Name` 并指定映射表 `MyTable`；设置 2 分钟 Set-up Time；用入口控制 `partArrives` 按材料名开关通往各 Tank 的 Pipe。
- **配置末端 Tank**：两个 Tank 流出速率 0.1 L/s、容积 2000 L，各建一个传感器，控制 `xyFull` 在装满时 `EventController.stop(true)` 停止仿真。

---

## 示例 4：按固定顺序生产流体

一个 **FluidSource** 按固定顺序生产三种材料的生产线。材料经 Pipe 流到 **PatchMatrix**，由 PatchMatrix 通过三条 Pipe 分发到存储对应材料的 Tank；分发逻辑在由 init 方法调用的 Method `fillTanks` 中定义。

**演示步骤：**

- **配置 FluidSource、MaterialsTable 和 SequenceTable**：FluidSource 选择 `Material Selection > Sequence`（序列仅处理一次）；MaterialsTable 录入 `MatA`、`MatB`、`MatC` 并分配不同颜色；SequenceTable 定义顺序——先 1000 L `MatB`，再 1500 L `MatC`，最后 800 L `MatA`。
- **配置接收材料的 Tank**：三个 Tank 设置相同（流出速率 1 L/s，容积 3000 L），可直接在 Tank 类中统一设置。
- **定义 PatchMatrix 的填罐逻辑**：方法 `fillTanks` 用 `waituntil FluidSource.CurrentMaterial /= currMaterial` 检测材料切换，再用 `PatchMatrix.setConnections(1, n, true/false)` 打开/关闭对应管道；init 方法调用 `PatchMatrix.resetConnections` + `fillTanks`，reset 方法也重置连接。
- **运行仿真查看结果**：设置 EventController 实时因子为 42 便于观察；最终各 Tank 装入指定材料与指定量。如需暂停后重复同一序列，可编写 `startSecondSequence` 方法，并在 init 中用 `&startSecondSequence.executeIn(1:00:00)` 定时执行，最终 Tank 材料量翻倍。

---

## 关键 SimTalk 代码片段

**Tank 传感器控制（示例 3）**

```simtalk
// Sensor Control 1
param SensorID: integer, Exceeded: boolean
self.~.EntranceLocked := false

// Sensor Control 2
param SensorID: integer, Exceeded: boolean
self.~.EntranceLocked := true

// Reset Control
self.~.EntranceLocked := false
```

**Mixer 的配方切换 observer（示例 3）**

```simtalk
// observer for ResWorking
param Attribute: string, previousValue: any
if NOT ?.ResWorking AND NOT ?.Failed AND NOT ?.Stopped
   if ?.Product = "Product X"
      ?.Product := "Product Y"
   else
      ?.Product := "Product X"
   end
end

// observer for Empty
param Attribute: string, previousValue: any
if ?.Leer
   if ?.Product = "Product Y"
      Portioner.MUPath := .UserObjects.ForY
      Portioner.AmountPerMU := 3
   else
      Portioner.MUPath := .UserObjects.ForX
      Portioner.AmountPerMU := 2
   end
end
```

**PatchMatrix 分发逻辑（示例 4）**

```simtalk
var currMaterial = ""
waituntil FluidSource.CurrentMaterial /= currMaterial
currMaterial = FluidSource.CurrentMaterial
PatchMatrix.setConnections(1, 1, true)    // 让第一种材料流入 Pipe1
waituntil FluidSource.CurrentMaterial /= currMaterial
currMaterial = FluidSource.CurrentMaterial
PatchMatrix.setConnections(1, 1, false)   // 关闭 Pipe1
PatchMatrix.setConnections(1, 2, true)    // 让第二种材料流入 Pipe2
waituntil FluidSource.CurrentMaterial /= currMaterial
currMaterial = FluidSource.CurrentMaterial
PatchMatrix.setConnections(1, 2, false)   // 关闭 Pipe2
PatchMatrix.setConnections(1, 3, true)    // 让第三种材料流入 Pipe3
```

---

## 涉及的核心对象一览

| 对象 | 用途 |
| --- | --- |
| FluidSource | 向系统引入基础/原料材料 |
| Tank | 暂存（缓冲）材料 |
| Pipe | 输送材料的管道 |
| Connector | 连接流体对象与管道（必须） |
| Mixer | 将基础材料/中间产品混合转化为新产品 |
| ContinuousMixer | 连续混合流体 |
| Portioner | 将流体分装成 MU（如巧克力棒、容器） |
| DePortioner | 将 MU 拆解还原为流体，分流至各 Tank |
| PatchMatrix | 将入料管道切换到指定出料管道 |
| MaterialsTable | 定义材料、密度、颜色、产量及配方成分 |
| SequenceTable | 定义按固定顺序生产材料的序列 |
| Conveyor | 运输 MU（如巧克力棒、容器） |
| Drain | 将 MU 移出工厂 |
