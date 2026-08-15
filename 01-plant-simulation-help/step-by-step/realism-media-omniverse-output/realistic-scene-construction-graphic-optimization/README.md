# Realistic Scene Construction & Graphic Optimization（真实场景构建与图形优化）总结

本目录包含 `realistic-scene-construction-graphic-optimization.md`（以及同名文本提取文件 `realistic-scene-construction-graphic-optimization.txtx`），内容为 Plant Simulation 帮助文档中 **真实场景构建与图形优化** 相关章节的说明。以下是对其内容的总结。

本指南介绍如何在 Plant Simulation 中创建视觉上美观、逼真的仿真模型，涵盖工厂墙与通道、门、文本与显示板、JT 布局文件、点云、导入的 JT 图形以及图形优化。

示例模型 **Factory 51**（可从 Start Page 的 *Example Models* 打开）演示了这些技巧。

## 1. 创建真实感模型（Creating a Realistic Looking Model）

可通过以下方式创建真实感模型：

- 插入工厂墙并创建通道
- 添加文本和显示板
- 向仿真模型添加 JT 布局文件
- 添加点云
- 导入表示对象的 JT 图形

视频：https://youtu.be/wfVN-mcWNsc?si=LepG6cgh0MDLKilQ&t=22

### 在 Omniverse 中增强可视化

使用 **Omniverse Connector** 在 Omniverse 中为仿真模型创建美观的可视化：

- https://support.sw.siemens.com/en-US/okba/KB000179528_EN_US
- https://support.sw.siemens.com/en-US/knowledge-base/KB000179496_EN_US

## 2. 插入工厂墙并创建通道（Insert Factory Walls and Create Passageways）

在示例模型中，围绕一条传送带创建了四面工厂墙。

**步骤：**

1. 在 3D 中点击 **Edit** 功能区选项卡，然后 **Edit > Insert Shape > Factory Walls**。
2. 选择墙的设置。
3. 模型会显示传送带周围的墙。

接下来，在 Station 与 Conveyor 之间的墙上切开一个通道，使传送带能穿过它。这涵盖：

- 在墙上切开开放通道
- 创建通道和门

### 在墙上切开开放通道

**步骤：**

1. 在工厂墙上要切开通道的位置点击鼠标。
2. 按 **+** 键，直到只有要切除的墙段被选中。
3. 按 **Del** 删除该墙段（图形），在消息框中点击 **Yes** 确认。
4. 添加 **过梁**（一个 Cube 或 Textured Plate），使通道顶部不敞开。

由于 Cube 的 Thickness 插入后无法更改，请先记下工厂墙的 **Thickness** 值（示例中为 0.3 米），并将立方体的 Width 与之匹配。

**过梁步骤：**

- 点击 Cube，将其 Width 设为 0.3 米（与墙 Thickness 匹配）。点击 **Create**，拖到通道位置并点击插入。
- 切换到 **Planning View**（平面视图），用方向键粗略放置过梁。
- 右键过梁，选择 **Show 3D Properties**，点击 **X-Position** 文本框并滚动鼠标滚轮，直到位置看起来正确。
- 取消 Planning View，以同样方式调整 **Z-Position**。
- 使过梁材质与墙一致：打开 **Factory Wall Settings > Wall Material**，复制材质，然后粘贴到过梁 3D 属性的 **Material** 选项卡。
- 延长传送带，使其穿过通道。
- 可选：通过更改 Z 方向的 **Scaling** 抬高过梁。

### 创建通道和门

通道可由 PVC 条帘覆盖以便通行。这里创建一扇门，当零件接近时自动打开，零件通过后关闭。这用一块上下移动的板来建模。

**步骤：**

1. 按上述方法从工厂墙上切出选中的墙段。
2. 在通道左右各插入一根立柱（长方体），并在立柱上放置过梁。
3. 在 **Transformation** 选项卡上微调位置——点击文本框，按住 **Ctrl** 并滚动鼠标滚轮。

门可通过以下几种方式控制：

- 使用姿势开关门
- 不使用姿势开关门
- 将门移到零件高度

#### 使用姿势开关门

使用关节和两个姿势以及三个控制来建模门的开关。

**步骤：**

1. 创建门图形（一个压扁的长方体）并将其定位在两根立柱之间。
2. 为门着色，使其与墙区分开。
3. 在 Station（内侧）与 Drain（外侧）之间插入一条 Conveyor。一条螺旋传送带可克服 1 米的高度差。
4. 将门设为可动画对象：右键门，选择 **Make Animatable Object**，点击 **OK**。
5. 在 **Tab Joint** 上设置一个 **Prismatic Joint**（棱柱关节），从 0 米开始，向上移动到 2 米。
6. 在名为 `FactoryWalls` 的后台 Frame 中，选择 **Edit 3D Properties**，转到 **Tab Poses**，添加两个姿势：
   - `GateUp` — 将门移到 2 米。
   - `GateDown` — 将门移回 0 米。
7. 在传送带的 Entrance Control 和 Exit Control 中控制时序。

**Entrance Control：**

```simtalk
self.~.EntranceLocked := true
_3D.Poses.moveTo("GateUp")
self.~.ExitLocked := false
```

**Exit Control：**

```simtalk
self.~.ExitLocked := true
wait _3D.Poses.moveTo("GateDown")
@.move
self.~.EntranceLocked := false
```

**Init（用户自定义属性）** — 确保模型重置时出口关闭、入口打开：

```simtalk
self.~.ExitLocked := true
self.~.EntranceLocked := false
```

仿真运行时，门在零件接近时升起，保持升起直到零件通过，然后落下。

#### 不使用姿势开关门

使用 `moveTo` 方法代替姿势。门仍然上移 2 米、停止，并在零件通过后回到 0 米。

**Entrance Control：**

```simtalk
self.~.EntranceLocked := true
wait _3D.getObject("Gate").moveTo(2) // gate moves 2 meters up
// wait _3D.Poses.moveTo("GateUp")
self.~.ExitLocked := false
```

**Exit Control：**

```simtalk
self.~.ExitLocked := true
wait _3D.getObject("Gate").moveTo(0) // moves the gate back to initial position
// wait _3D.Poses.moveTo("GateDown")
@.move
self.~.EntranceLocked := false
```

Init Control 源代码不变。

#### 将门移到零件高度

将门只升到零件本身的高度（加上间隙）。

**Entrance Control：**

```simtalk
self.~.EntranceLocked := true
wait _3D.getObject("Gate").moveTo(@.MUHeight+0.1m)
// moves the gate up to the height of the part
// plus 10 cm for the height of the conveyor
wait _3D.Poses.moveTo("GateUp")
self.~.ExitLocked := false
```

**Exit Control：**

```simtalk
self.~.ExitLocked := true
wait _3D.getObject("Gate").moveTo(0.1m)
// moves the gate back to the initial position
wait _3D.Poses.moveTo("GateDown")
@.move
self.~.EntranceLocked := false
```

**Init Control：**

```simtalk
self.~.ExitLocked := true
self.~.EntranceLocked := false
_3D.getObject("Gate").moveTo(0.1m, 0) 
// 0 means that the target position becomes 
// active immediately without moving there
```

## 3. 添加文本和显示板（Adding Text and Display Boards）

- 对于**永不改变的静态文本**：插入 **3D Text**（`Edit > Insert Shape`），或导入一个在 NX 等软件中创建的 JT 文件（Factory 51 中的 "Plant Simulation" 字样就是这样做的）。
- 对于**可编辑的显示板**：使用 *User Interface* 工具栏中的 **Comment** 对象。

### 显示文本

**步骤：**

1. 在 **Edit > Insert Shape** 下点击 **Text**。
2. 在对话框中输入文本并选择设置，点击 **Create**。
3. 拖到某个位置并点击左键——文本平铺插入到地面上（最初会小得多）。

修正比例：

- 右键文本，选择 **Edit 3D Properties**。
- 使用 **Uniform Scaling**，系数为 3（示例）。
- 绕 X 轴旋转 45 度。
- 沿 Z 轴向上移动，直到下边缘平放在地面上。

### 显示显示板

**步骤：**

1. 点击 *User Interface* 工具栏上的 **Comment** 对象，并将其插入模型。
2. 双击 Comment 并输入文本（例如 "My factory in Crailsheim, Baden-Württemberg, Germany"），选择 **Font Size > Extra Large**，点击 **OK**。
3. 使其朝向大厅上边界上方的工厂地面：右键，**Edit 3D Properties**，绕 X 轴旋转 45 度，并沿 Z 轴向上移动。

## 4. 向仿真模型添加 JT 布局文件（Add a JT Layout File to Your Simulation Model）

布局图形可增加真实感。

**步骤：**

1. 将布局图形（如 `Layout_Factory_Training.jt`）从 Windows 资源管理器拖入打开的 Frame 窗口。Plant Simulation 会把图形附加到鼠标指针并打开 **Insert Graphic** 对话框——接受默认值并点击 **OK**。
2. 拖到 Frame 左上角（坐标 0, 0）并点击放置。

之后可以继续插入对象并操作它们。除了 JT 布局文件，也可以用点云作为背景。

## 5. 添加点云（Add a Point Cloud）

点云是由 X、Y、Z 坐标定义的一组 3D 数据点。用它可视化真实的工厂布局，并在其上真实地布置机器。

**步骤：**

1. 点击模型背景，选择 **Edit 3D Properties**，然后进入 **Tab Point Cloud**。
2. 点击按钮并选择点数据库文件（`*.pod`）。相对路径相对于仿真模型所在的文件夹。
3. 要移除点云，删除文本框中的名称。
4. 点击 **OK** 或 **Apply** 显示点云。

**注意：**

- 最初可能只显示点云的一小部分；旋转视图可显示更多部分。
- 如果点云文件位于 **SSD** 上，加载会显著加快。
- 用 *View* 功能区选项卡上的 **Show Point Clouds** 切换可见性。
- 通过 **Edit 3D Properties > Tab Point Cloud**（Position 和 Rotation Angle）调整位置/方向。
- 出于性能考虑，**Show Point Clouds 默认停用**；重新打开模型后需重新启用。

## 6. 导入表示对象的 JT 图形（Import JT Graphics Representing an Object）

除了在 3D 中创建形状，也可导入图形来表示对象。示例：用同事提供的 JT 图形构建一辆沙丘越野车（dune buggy）。

**步骤：**

1. 在 Class Library 中复制零件 `.MUs.Part` 并重命名（如 `DuneBuggy`）。在 **Tab Graphics** 上为组件添加图形组。
2. 将 JT 图形导入匹配的图形组。将 `Body.jt` 和 `Seats.jt` 导入所有名称以 `Body` 或 `Seats` 开头的图形组。
   - 转到 3D 功能区选项卡 **Edit**，点击 **Import Graphics**，导航到文件夹并点击 **Open**。
   - 将 JT 图形大致拖到 Frame（`.MUs.DuneBuggy`）中所需位置并点击。选择目标图形组。
   - 对所有 JT 文件重复上述操作。
3. 用方向键和 **Edit 3D Properties** 对话框排列组件。
   - 将三个车身面板放在完全相同的位置；三个座椅组件也同样处理。这样可通过显示/隐藏面板和座椅来测试颜色组合。
4. 要更改图形颜色：右键 `.MUs.DuneBuggy` 的背景，选择 **Show Graphic Structure**。
   - 展开图形组（如 `BodyRed`）。
   - 找到以 `-M` 结尾的节点（表示材质）。
   - 右键该节点（如 `1-JtGroup-M`）并选择 **Edit 3D Properties**。尝试材质颜色以微调光泽效果。

## 7. 优化图形（Optimizing a Graphic）

优化图形——即展平对象的层级结构——会删除不必要的信息，从而加快渲染和显示速度。

导入的图形通常是为其他目的设计的（例如制造一个包含所有细节的引擎）。对于仿真用户来说，速度和流畅的动画比这些细节更重要。

> **建议：** 优化每一个导入的图形。尽快进行，但**不要早于**提取所有需要的结构信息（例如在创建带动画的仿真对象时）。

**前提：** 首先将图形设为可动画对象（**Make Animatable Object**）。

**步骤：**

1. 在场景窗口中点击要优化其图形的可动画对象。
2. 点击 3D 窗口 *Edit* 功能区选项卡上的 **Optimize Selected Graphic**。
3. 尝试设置：
   - **Step 1: Prune Tiny Graphics**（修剪细小图形）
   - **Step 2: Flatten Structure**（展平结构）
   - **Step 3: Visibility Filter**（可见性过滤）

**注意：**

- 点击 *View* 功能区选项卡上的 **Show External Graphic Group** 显示打开 3D 对象的外部图形。
- 在 **Graphic Complexity** 下，Plant Simulation 显示两个特征：**节点（nodes）** 数量和**多边形（polygons）** 数量。优化策略主要影响这两个值。

## 目录说明

- `realistic-scene-construction-graphic-optimization.md`：真实场景构建与图形优化章节的 Markdown 版本（本总结的源文件）。
- `realistic-scene-construction-graphic-optimization.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Realistic Scene Construction & Graphic Optimization"（10-1119 – 10-1149）。Unpublished work. © 2026 Siemens.*
