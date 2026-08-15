# 状态可视化（State Visualization）总结

本目录为 Plant Simulation 帮助文档 **Working with Graphics（使用图形）** 相关章节的内容总结，源文件为 `state-visualization.md`（另附同名文本提取文件 `state-visualization.txtx`）。本章涵盖图形与图形组、图形继承与复制、材质设置、导入与建模图形、替代图形组以及对象状态可视化。

## 1. 图形与图形组（Graphics and Graphic Groups）

Plant Simulation 用图形显示对象，图形组织在一个或多个**图形组（graphic group）**中。对象和 Frame 的图形组由一个或多个图形组成，名称在对象内唯一（类似仿真对象的 2D 图标）。

图形组分为：

- **外部图形组（external）**：向外表示对象。
- **内部图形组（internal）**：装饰对象内部。

关键要点：

- 哪些图形组是 `internal` 或 `locked`，连同图形结构，都是**可继承**的对象属性。
- 图形组可永久显示或隐藏，用于在多个视觉表示间切换。
- 每个仿真对象或可动画对象至少含一个名为 `default` 的外部图形组，还可有任意数量的替代/附加图形组，可独立显示或隐藏。
- Frame 初始含一个名为 `deco` 的内部图形组。
- 图形组的可见性是对象属性，可独立于图形结构及 `internal`/`locked` 属性继承。

图形组在 **Edit 3D Properties** 的 **Graphics** 选项卡和 **Show Graphic Structure** 对话框中创建、删除或配置：

- 眼睛图标 = 图形组**可见**。
- 带叉的眼睛图标 = 图形组**不可见（按所选）**。

图形组中的每个图形都可单独删除和编辑——用鼠标在 3D 窗口操作，或在 **Edit 3D Properties** 中指定位置、旋转、缩放或材质。

> **注意：** 更改类对象的任何图形或图形结构会同时更改所有继承对象；更改派生对象的图形只影响该对象，因为 3D 会停用图形继承（若尚未停用）。停用图形继承会导致图形被复制，因此应尽量在类对象中修改。

状态图形可在 **Edit 3D Properties** 的 **States** 选项卡创建、替换或删除，并选择状态方向 **Horizontal**、**Vertical** 或 **Off**；更改该设置会删除所有状态图形并按选择重新排列创建新状态图形。

## 2. 继承图形（Inherit Graphics）

对象图形是可继承的对象数据。继承图形的对象与父对象共享图形，从而节省内存；类对象中的图形更改自动反映到图形继承已激活的派生对象中。

对派生对象的下列图形更改会**停用图形继承**，之后派生对象含自身修改过的父图形副本，占用额外内存：

- 添加/删除图形组或图形。
- 变换图形（移动、旋转、缩放）。
- 更改图形材质。
- 组合/取消组合图形组。
- 重命名图形组。
- 更改图形组设置 `internal` 或 `locked`。

激活/停用图形继承：

- 点击 **Home > Edit 3D Properties > Graphics > Graphic Groups** 下的继承复选框。
- 在 **Show Graphic Structure** 对话框点击 **Inherit Graphic Groups**。

开启继承使对象重新使用父对象图形并取消更改；关闭则保留实例已改图形、占用更多内存。

**参见：** `_3D.InheritGraphics` [SimTalk]

## 3. 复制图形（Duplicate Graphics）

复制 3D 窗口中选中的图形：按住 **Ctrl+Shift** 并在 3D 窗口另一位置点击鼠标左键。

Plant Simulation 不创建副本；新图形**引用**被复制的图形，大幅降低内存消耗。引用图形在 **Show Graphic Structure** 中以菱形标记显示。

## 4. 编辑成组图形（Edit Grouped Graphics）

可整体编辑成组图形。要同时移动、旋转或缩放多个图形并保持相对位置，先组合再整体操作。

组合多个图形：

- 按住 **Shift** 点击对象，或拖出选取框选中它们。
- 点击 Edit 功能区选项卡的 **Group Graphics** 或按 **Ctrl+G**，Plant Simulation 创建单个新组。
- 像单个图形一样移动、旋转、缩放组；也可在 **Edit 3D Properties** 的 **Transformation** 选项卡变换组。

恢复原结构：选中新组，点击 Edit 选项卡的 **Ungroup Group of Graphics** 或按 **Ctrl+U**。

## 5. 设置图形材质（Set the Material of a Graphic）

可定义图形的表面质量与外观（材质）：反射光线的程度、反射的颜色、发出的颜色。操作：选中图形，点击 Home 选项卡的 **3D Properties**，点击 **Material** 选项卡。

选项：

- **Material Active** — 为图形分配材质。
- **Diffuse Color** — 粗糙表面的光线反射，与镜面反射互补。
- **Ambient Color** — 被环境物体照亮时反射的光线颜色。
- **Specular Color** — 对象高光的反射颜色。
- **Emissive Color** — 对象发出的颜色（如灯罩基色黄色、点亮时发出白光）。
- **Transparency** — `0.0`（不透明）到 `1.0`（完全透明）之间的值。
- **Shininess** — `0.0`（很暗淡）到 `1.0`（高度抛光）之间的值，决定光线反射的锐度。

点击 **Apply** 应用材质。还可：复制当前材质设置、粘贴先前复制的材质、移除嵌套图形中的材质。

> **注意：** 若多个部分/完全透明的图形在当前视角下前后重叠，因渲染启发式，部分可能看起来错误或像缺失。

> **注意：** 材质定义在图形结构不同层级时，Plant Simulation 渲染时总是使用结构最底层的材质。

## 6. 为对象使用不同图形（Use a Different Graphic for an Object）

可用接近实际机器的图片替换默认图形，或使用机器制造商提供的图形文件。程序自带的图形以 `s3d` 格式保存，多数已预定义动画路径且对象缩放正确。

选项：

1. **用另一个预定义对象图形替换**：选中对象，点击 Edit 选项卡的 **Exchange Graphics**（或上下文菜单），导航到 `C:\Program Files\Siemens\Tecnomatix Plant Simulation XX\3D\s3D-graphics` 选择 `.s3d` 文件，点击 **Open** 替换所选对象的所有图形与动画数据（图形组、状态图形和动画属性被移除替换）。也可从文件管理器拖 `.s3d` 文件到 3D 窗口。
2. **插入现有图形文件的图形**：选中图形，点击 3D 的 Edit 选项卡 **Graphics**，选择 `.jt` 图形（默认文件夹 `...\3D\jt-graphics`）。导入图形添加到所选图形组并保留现有图形，删除不需要的图形。
3. **创建自己的对象图形**：打开对象，点击 Edit 选项卡 **Insert Shape** 选择要创建的形状，形状添加到所选图形组。也可通过 **Show Graphic Structure** 从其他图形组复制图形并用 **Ctrl+V** 粘贴。
4. **创建复杂图形**：插入多个形状或导入图形，并定位、旋转、缩放或着色。

> **注意：** 导入、创建或变换对象图形后，可能需要调整动画路径或点——使用 **Exchange Graphics** 时除外。

## 7. 创建自己的对象（Creating Your Own Objects）

- **复制或派生** Class Library 中属性相似的类对象，再编辑其 3D 属性。
- **导入 3D 图形**：从 Plant Simulation 图形库（`安装文件夹 > 3D > jt graphics`）、自己的库或其他程序导入。导入后可能需要缩放、旋转并移到场景原点，右键图形选择 **Make Simulation Object**。
- **建模自己的 3D 图形**：插入形状并定位/旋转/缩放/着色，组合多个图形后再通过 **Make Simulation Object** 转成仿真对象。
- **创建带动画的仿真对象**，使模型尽可能接近真实。

## 8. 导入 3D 图形（Import a 3D Graphic）

3D 可导入的文件格式：

| 格式 | 扩展名 |
|---|---|
| 所有 3D 图形文件 | — |
| JT 文件（推荐优先使用） | `*.jt` |
| Parasolid 文件 | `*.x_b`, `*.x_t`, `*.xmt_bin`, `*.xmt_txt` |
| IGES 文件 | `*.igs`, `*.iges` |
| STEP 文件 | `*.stp`, `*.step` |
| VRML 文件 | `*.wrl` |
| STL 文件 | `*.stl` |
| Catia V4 文件 | `*.exp`, `*.model` |
| CAD Layout 文件 | `*.dgn`, `*.dwg`, `*.dxf` |

导入含动画结构的图形（如 JT 文件）：点击 Edit 选项卡 **Import Graphics**，选文件类型、导航到文件并点击 **Open**。要用含动画结构的另一图形替换对象图形，右键对象选 **Exchange Graphic**，再选 3D Files。

## 9. 建模自己的 3D 图形（Model Your Own 3D Graphic）

可插入一种或多种形状建模自己的 3D 图形：**Barred Area、Box、Cone、Cuboid、Cylinder、Dimensioning、Factory Walls、Fence、Mezzanine、Rack、Sphere、Stairs、Text 或 Textured Plate**。

- 点击要创建的形状（如 Cuboid）。
- 选择要加入的 **Graphic Group**。
- 输入 **Dimension X/Width**、**Y/Depth**、**Z/Height**。
- 点击 **Create**；3D 把形状挂到鼠标指针，拖动定位并左键插入，右键或按 **Esc** 取消。
- 改变位置/旋转/缩放：选中形状，用 **3D Properties > Transformation** 选项卡。
- 设置形状是否为 Worker 的障碍物：**Edit 3D Properties > Graphic Settings** 选项卡。
- 分配颜色/材质：**3D Properties > Material** 选项卡。
- 删除形状：右键用迷你工具栏，或用 **Show Graphic Structure** 选择 **Delete**。

> **注意：** 向外部图形组插入新形状时，Plant Simulation 自动激活 **Show External Graphic Groups**，便于将新图形与目标组其他图形对齐。

## 10. 创建带纹理的板（Create a Textured Plate）

- 点击 3D 窗口 Edit 选项卡的 **Textured Plate**。
- 选择图像与设置（如方向、适配）。
- 点击 **Create**，拖动并点击放置（右键或 **Esc** 取消）。

方向：

| 方向 | 外观 |
|---|---|
| Floor | 平铺在地面 |
| Front wall | 贴在前墙 |
| Side wall | 贴在侧墙 |

- **Show on Both Sides** — 在板的顶/前与底/背显示图像。
- **Fit Image Size** 每个维度 2 块瓷砖时，每维度插入两块图像瓷砖。
- 用鼠标拖动移动板；**Ctrl + 上箭头** 上移。
- 通过 **Edit 3D Properties > Transformation** 更改尺寸。
- 通过 **Graphic Settings** 设为 Worker 障碍物；通过 **Material** 选项卡分配材质。

## 11. 创建无纹理的板（Create a Non-textured Plate [example]）

- 点击 Edit 选项卡的 **Cuboid**。
- 在相应文本框输入 `0` 在该平面创建板。
- 点击 **Create**，按带纹理板的方式放置或移动。

## 12. 建模一个瓶子（Model a Bottle）

用 3D 形状 **Cylinder** 和 **Cone Frustum** 组合成瓶子或类似物品，用易区分的颜色区分组件：

1. **瓶底** — 扁平的 Cylinder。
2. **瓶身** — 上下开口的 Cylinder。
3. **瓶颈** — 一个 **Cone Frustum**。
4. **瓶盖** — 与瓶颈同半径的 Cylinder。

装配：

- 将瓶身放到瓶底上，点击 Edit 选项卡 **Align to Grid**；组合这些零件。
- 放置瓶颈，再 **Align to Grid**。
- 在 Z 方向向下移动瓶颈（通过 **Edit 3D Properties**）直到齐平，组合零件。
- 放置瓶盖：按住 **Ctrl** 按 **上箭头** 移到瓶颈上方，再按 **左箭头** 定位；点击 **Align to Grid**，调整 Z 方向直到贴合。

## 13. 设置 Plant Simulation 如何显示对象（Set How Plant Simulation Shows an Object）

对象外观取决于打开窗口的对象层级，Plant Simulation 区分**外部表示**与**内部表示**：

**Frame 的外部表示**（在其所在位置的窗口中点击该 Frame 时选中）：

- 标记 **Visible** 和 **External** 的图形组。
- 未显式排除的所含对象（仅当 Frame 选择了 **Show Content**）。

**其他对象的外部表示**：

- 标记 **Visible** 的图形组。
- 按 **Orientation** 设置的状态图形。
- 物料流方向（若为长度导向对象）。

**Frame 的内部表示**（打开 Frame 时显示）：

- 标记 **Visible** 和 **Internal** 的图形组。
- 所含对象与 Frame 的外部表示。

**其他对象的内部表示**：

- 标记 **Visible** 的图形组。
- 按 **Orientation** 的状态图形。
- 所含对象的外部表示。

要同时显示外部与内部表示，在含正编辑对象的窗口中激活 **Show External Graphic Groups**。活动窗口中还可额外显示/隐藏：所有 Connector、Interface 与 Marker（**Show Connections**），物料流方向箭头（**Show Material Flow Directions**）。

## 14. Plant Simulation 在窗口中显示什么（What Plant Simulation Shows in a Window）

显示内容取决于对象/Frame 的内容、内容设置与窗口设置：

- **对象**（不含 Frame/连接/传感器）：若其位置在窗口中打开且至少一个图形组为 Visible、External 且含图形，则显示。
- **Frame**：若其位置打开且（至少一个图形组 Visible/External/含图形，或 Frame 显示 Content 且含至少一个未被 Excluded From Show Content 的对象/Frame），则显示。
- **Frame 的外部图形组**：若 Visible 且（Frame 在窗口显示，或 Frame 已打开且窗口显示 External Graphics）。
- **Frame 的内部图形组**：若 Visible 且 Frame 在窗口中打开。
- **对象的图形组**：若 Visible 且（对象已打开或在窗口显示）。
- **Frame/对象的名称**：若对象显示 Captions 且 Frame/对象已显示且窗口显示 Names。
- **Frame/对象的标签（Label）**：若对象显示 Captions 且已显示且窗口显示 Labels。
- **对象的状态图形**：若对象显示 States 且（已打开或在窗口显示）。
- **Frame 的 Connector**：若窗口显示 Connections 且（Frame 打开或以 Content 显示，且两连接对象未 Excluded From Show Content）。
- **Frame 的 Interface/Marker**：若窗口显示 Connections 且（Frame 打开或以 Content 显示，且 Interface/Marker 未 Excluded From Show Content）。
- **长度导向对象的 Sensor**：若对象显示 Sensors 且（已打开或已显示）。
- **长度导向对象的物料流方向**：若窗口显示 Flow Directions 且对象已显示。

## 15. 使用替代图形组（Using Alternative Graphic Groups）

该示例建模一架简化飞机，通过显示展示已完成组件的选定图形组来展示飞机装配进度。

建模任务：

- 为对象创建新 MU 类。
- 为组件创建替代图形组。
- 显示飞机装配进度。

### 15.1 为对象创建新的 MU 类

- 在 Class Library 打开 **MUs** 文件夹。
- 右键 **Container** 选 **Duplicate**。
- 按 **F2** 将新 Container 重命名为 `Airplane`。

### 15.2 为组件创建替代图形组

- 打开含仿真模型的 Frame。
- 编辑 MU 类 `Airplane`（右键 Class Library 中该类选 **Open in 3D**；右键 `.UserObjects.Airplane` 背景选 **Edit 3D Properties**）。
- 删除默认图形（名为 `default` 的托盘）。
- 点击 **Add** 添加新图形组：`Fuselage`、`Cockpit`、`RightWing`、`LeftWing`、`TailAssembly`。
- 在 Edit 选项卡为每组创建实际图形：
  - **Fuselage** — 一个 Cylinder，旋转 90° 至水平。
  - **Cockpit** — 一个 Cone Frustum，旋转 90° 并放在机身右侧。
  - **RightWing** 与 **LeftWing** — 放在机身合适位置。
  - **TailAssembly** — 一个 Cone（垂直尾翼）和一个 Sphere（水平尾翼，缩放并压扁）。

> **注意：** 清除 Transformation 选项卡的 **Scale automatically**，否则图形不会显示所输入的设置。

## 16. 显示飞机装配进度（Show the Progress of the Airplane Assembly）

飞机从一个工站移动到下一个工站时，依次隐藏和显示图形组以展示装配进度。

### 16.1 插入并配置 Source 与加工工站

- 插入一个 **Source**，生产类型 `Airplane` 的 MU；在 Controls 选项卡选 `hidePlane` 作为 **Exit Control**。
- 插入 **Station**（处理时间 10 秒 `0:10`），选 `showFuselage` 作为 **Entrance Control**。
- 插入 **Station1**（10 秒），选 `showTailAssembly` 作为 **Entrance Control**。
- 插入 **Station2**（10 秒），选 `showWings` 作为 **Entrance Control**。
- 用 Connectors 连接各工站。

### 16.2 编写可见性控制代码

用属性 `Visible` 隐藏/显示图形组。

`hidePlane`（Source 的 Exit Control）隐藏所有组件，再把飞机移到下一工站：

```simtalk
@._3D.getGraphic("Fuselage").Visible := false
@._3D.getGraphic("Cockpit").Visible := false
@._3D.getGraphic("LeftWing").Visible := false
@._3D.getGraphic("RightWing").Visible := false
@._3D.getGraphic("TailAssembly").Visible := false
@.move -- move the airplane on to the next station
```

`showFuselage`（`Station` 的 Entrance Control）显示机身与驾驶舱：

```simtalk
@._3D.getGraphic("Fuselage").Visible := true
@._3D.getGraphic("Cockpit").Visible := true
```

`showTailAssembly`（`Station1` 的 Entrance Control）显示尾翼组件：

```simtalk
@._3D.getGraphic("TailAssembly").Visible := true
```

`showWings`（`Station2` 的 Entrance Control）显示机翼：

```simtalk
@._3D.getGraphic("LeftWing").Visible := true
@._3D.getGraphic("RightWing").Visible := true
```

在 EventController 对话框设置 Real-time factor 16 以获得平滑动画。

### 16.3 更改对象在工站上的方向与位置

- 将飞机右旋 90°：右键飞机类，选 **Open in 3D**，右键背景选 **Edit 3D Properties**，在 **Transformation > Rotation** 选项卡的 **Angle** 输入 `90`。
- 更改位置：在新窗口打开类，按 **Ctrl+A** 选中所有图形组，用左箭头键左移直到机翼中心位于 y 轴，再用 **Ctrl+Shift+上箭头** 沿 z 轴上移。

## 17. 显示对象状态（Show Object States）

可用**状态图形（state graphics）**显示对象状态。状态图形显示物料流对象的 **States**，一个状态图形可同时显示多个状态。设置在 **Edit 3D Properties** 的 **States** 选项卡。

### 17.1 在机器上方的信号柱显示状态

垂直排列的状态图形默认以灰色信号柱上的信号灯显示在标准图形的左后上方角落。要激活垂直状态图形：在 3D 打开对象，右键 3D 窗口背景，选 **Edit 3D Properties**。

### 17.2 在机器前方显示状态

Plant Simulation 默认将状态显示为机器图形后方的水平排列立方体；视机器图形而定，可能遮挡状态图形。要在机器前方显示：

- 在 3D 打开对象，右键背景选 **Edit 3D Properties**。
- 点击 **Show All Possible States** 并旋转机器查看状态图形。
- 将水平状态移到前方：

| 方式 | Y 方向 | X 方向 | Z 方向 |
|---|---|---|---|
| 箭头键 | 上/下 | 左/右 | Ctrl+上/下 |
| 鼠标拖动 | 左/右拖 | 前/后拖 | Ctrl+上/下拖 |
| 精确值 | `Y = -0.2` | `X = -1.07` | `Z = 0.25` |

- 精确值法：右键机器选 **Show Graphic Structure**，再 **Edit 3D Properties**，在 **Transformation** 选项卡设置 `X = -1.07`、`Y = -0.2`、`Z = 0.25`，点击 **Apply**。
- 若过高，在 Z 方向缩放：清除 **Uniform** 复选框并在 **Z** 输入 `0.9`。

## 目录说明

- `state-visualization.md`：本目录源文件（Markdown 版本），为“使用图形”（含图形组、材质、导入/建模、替代图形组与对象状态可视化）章节的说明。
- `state-visualization.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Working with Graphics"。Unpublished work. © 2026 Siemens.*
