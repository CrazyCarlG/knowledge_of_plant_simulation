# Working with Animation Paths（使用动画路径）总结

本目录包含 `paths-mu-joints-poses.md`（以及同名文本提取文件 `paths-mu-joints-poses.txtx`），内容为 Plant Simulation 帮助文档中 **Working with Animation Paths（使用动画路径）**、**Controlling the MU Animation（控制 MU 动画）** 与 **Modeling Joints and Poses（建模关节与姿态）** 三个相关章节的总结。以下是对其内容的总结。

## 1. 路径类型（Path Types）

动画路径由空间中的一组点组成，描述被动画的移动对象在物料流对象上或场景中的运动轨迹；飞越场景时观看场景的相机也使用动画路径。共有三种可动画对象路径，其创建与编辑流程仅略有差异，公共属性统一说明。

### 1.1 MU 动画路径（MU animation paths）

在 Home 功能区选项卡的 **Edit 3D Properties > Tab MU Animation** 下创建和编辑动画路径及动画区域（零件在其上被动画）。

### 1.2 自动画路径（Self animation paths）

点击 Home 功能区选项卡的 **Edit 3D Properties > Tab Self Animation** 创建和编辑对象自身移动的路径。

- 自动画路径的锚点是所选对象自身移动的线、多曲线或样条曲线的顶点。例如，自动画路径可模拟机器人运动。
- 多曲线（Polycurve）动画锚点是一条弯曲路径（一系列曲线段与直线段）的顶点。
- 样条（Spline）动画锚点是一条样条曲线的顶点。

### 1.3 相机动画路径（Camera animation paths）

点击 Home 功能区选项卡的 **Edit 3D Properties > Tab Camera Animation** 创建和编辑相机在 Frame 中穿过 3D 场景的路径。

- 相机动画路径的锚点是相机在 Frame 场景中移动的线、多曲线或样条曲线的顶点。
- 多曲线动画锚点是相机移动的弯曲路径（曲线段 + 直线段）的顶点。
- 样条动画锚点是一条样条曲线的顶点。

## 2. 创建动画路径（Create an Animation Path）

可创建三种动画路径：MU 在工厂中移动时被动画的路径、物料流对象自身被动画的路径、相机穿过 Frame 的路径。

1. 打开 **Edit 3D Properties**，根据需要点击 **Tab MU Animation**、**Tab Self Animation** 或 **Tab Camera Animation**。
2. 点击 **Add**。
3. 输入唯一的路径名称；通常使用 `Default` 路径做动画。
4. 选择要创建的 **Path type**。
   - 若对象（如 Store 或 ParallelStation）有多个放置来件移动对象的位置，可在 MU Animation 选项卡上把它们分布到动画区域。
5. 点击 **OK** 创建路径。初始路径由位于所选对象原点的一个锚点组成。
6. 通过 **Edit 3D Properties > MU Animation/Self Animation/Camera Animation > Edit > Path Anchor Points** 扩展/编辑初始路径。

## 3. 创建旋转对象的动画路径（Create an Animation Path that Rotates Objects）

通过设置旋转参数（而非编辑锚点）可创建使对象做圆周旋转的动画路径（例如起重机臂的运动）。

1. 选中物料流对象或场景对象，点击 Home 选项卡的 **Edit 3D Properties**。
2. 旋转所选对象处理的 MU 点击 **Tab MU Animation**；旋转对象自身点击 **Tab Self Animation**。
3. 点击 **Add**，在 **Create Rotation Path** 对话框中输入旋转路径名称，选择 **Path Type > Rotation Path [MU animation] - Lines**。
4. 编辑 **Create Rotation Path** 对话框设置：

| 参数 | 说明 |
|---|---|
| **Start Angle** | 旋转起始位置 |
| **End Angle** | 旋转结束位置；仅当与 Start Angle 不同 3D 才旋转 MU，值可大于 360° 或小于 -360° 以执行超过一整圈的旋转 |
| **Axis** | 旋转轴；通常 Z 轴 `(0,0,1)`（XY 平面）、Y 轴 `(0,1,0)`（XZ 平面）、X 轴 `(1,0,0)`（YZ 平面）；其他轴使对象在 3D 空间中对角旋转，倾斜旋转轴需在至少两个文本框输入值 |
| **Center point** | 旋转中心（所选对象坐标系）；若与起点不同，旋转对象沿圆弧移动并在不同于起点的位置停下（360° 旋转除外） |

- 旋转方向由角度大小决定：**End Angle 大于 Start Angle → 顺时针**；**End Angle 小于 Start Angle → 逆时针**。

5. 点击 **Apply** 计算动画路径。该路径即被动画对象移动的轨迹，在此路径上的运动就是旋转。

> **注意：** 可用方法 `_3D.SelfAnimations.scheduleRotation` 执行自旋转或相机旋转，无需创建路径。

6. 选中对象并启动测试动画以测试旋转路径。
7. 若旋转不满足预期，重新打开 **Create Rotation Path**，编辑参数、点击 **Apply** 再测试，直到满足需求。
8. 更改单个旋转步骤的时长：在列表选中路径点击 **Edit**；在 **Path Anchor Points** 中选中锚点点击 **Edit Values** 打开 **Edit Anchor Point**，在 **Time** 下编辑每个锚点（对应旋转步骤）的时间。

## 4. 编辑动画路径（Edit an Animation Path）

在 **Edit 3D Properties** 对话框中编辑各类动画路径：

- 编辑对象上零件（MU）的动画路径：选中对象 → **Edit 3D Properties** → **Tab MU Animation**。
- 编辑对象自身动画路径：选中对象 → **Edit 3D Properties** → **Tab Self Animation**。
- 编辑 Frame 的相机动画路径：选中 Frame → **Edit 3D Properties** → **Tab Camera Animation**。

> **注意：** 只有 Frame 提供 Tab Camera Animation。

在该对话框中可执行：创建动画路径、测试动画路径、用鼠标编辑、通过锚点编辑、创建旋转路径、重命名动画路径、删除动画路径。

## 5. 用鼠标编辑动画路径（Edit an Animation Path with the Mouse）

1. 打开 **Edit 3D Properties**，点击 **Tab MU Animation**、**Tab Self Animation**、**Tab Camera Animation** [Frame] 或 **Tab Robot Arm Animation** [PickAndPlace]。
2. 点击动画路径下 **Show** 单元格中的按钮，在场景窗口显示所选路径及其锚点。
3. 添加新锚点：点击 **Extend**，在期望位置点击鼠标左键插入锚点，重复直到路径成形。
4. 改变路径形状：选中锚点用鼠标拖拽，和/或用 **Edit 3D Properties > Tab Transformation** 设置。沿 X/Y 方向拖拽锚点时，Plant Simulation 也会双向拖动相连的曲线段（直到下一个直线段）。
5. 旋转锚点：点击它、按住左键拖动，和/或点击 **Edit 3D Properties > Transformation**。

> **注意：** 旋转描述动画路径的锚点时，也会旋转沿该路径移动的 MU。

6. 删除部分路径：选中锚点按 **Delete**，从路径中移除该锚点并修改形状。

## 6. 用鼠标编辑曲线路径（Edit a Curved Path with the Mouse）

除可编辑任意路径类型外，多曲线（polycurve）路径还可：

- 点击 **Extend** 添加锚点：
  - 添加直线段：在期望位置点击左键。
  - 添加曲线段：按住 **Ctrl** 并在期望位置点击左键。
  - 重复直到路径成形。
- 选中锚点拖动改变直线段形状；沿 X/Y 方向拖拽时，3D 也会双向拖动相连曲线段（直到下一个直线段）。

## 7. 通过锚点编辑动画路径（Edit an Animation Path via Anchor Points）

当鼠标编辑不够精确时，可在 **Path Anchor Points** 对话框中输入精确值：

1. 打开 **Edit 3D Properties**，在 **Tab MU Animation**、**Tab Self Animation** 或 **Tab Camera Animation** 选中路径。
2. 点击 **Edit**。
3. 在 **Path Anchor Points** 中选中锚点点击 **Edit Values**，或双击表格行。
4. 在 **Edit Anchor Point** 中为锚点输入/选择新的 **Position** 与 **Rotation** 设置。
5. 在路径末尾添加锚点：点击 **Add**（添加到列表底部），再编辑其设置。
6. 在选中锚点之前插入锚点：点击 **Insert Before**。
7. 删除锚点：选中后点击 **Delete**。
   - 删除连续锚点：按住 **Shift** 依次点击范围首尾锚点。
   - 删除非连续锚点：按住 **Ctrl** 逐个点击锚点。
8. 上移一个位置：**Move Up**。
9. 下移一个位置：**Move Down**。
10. 复制选中锚点设置并插入到其下方：**Duplicate**。

> **注意：** 可在 Edit 对话框中编辑 Polycurve 类型路径。

## 8. 测试动画路径（Test an Animation Path）

定义动画路径后，无需运行仿真即可在动画选项卡的 **Test Path** 组框测试设置：

1. 选择 **Test Object**——一个 MU，3D 复制其图形作为测试对象。
2. 输入测试对象在路径上移动的 **Velocity**。
3. 选择正向或 **Backwards** 移动（选择 Backwards 时 3D 自动输入负速度）。
4. 点击播放按所选设置运行动画。
5. 点击暂停暂停测试动画。
6. 点击停止停止测试动画。

## 9. 控制 MU 动画（Controlling the MU Animation）

在 **MU Animation** 选项卡定义移动对象（MU）如何在物料流对象上被动画；Frame 也算物料流对象。选项卡对无装载空间和有装载空间的对象外观不同。

- **Sub-tab Animation Paths** 可定义：长度导向对象、点导向对象、承载多个零件的点导向对象、Workplace 动画路径上的 MU 动画。
- **Sub-tab Animation Area** 可激活动画区域定义带装载空间对象上的 MU 动画。

带装载空间的对象——AGVPool、Container、ParallelStation、PlaceBuffer、Store、Transporter、Worker、Workplace、WorkerPool——若激活动画区域则使用它；否则使用动画路径。除 AGVPool 外都需自行创建动画路径。

### 9.1 长度导向对象上的 MU 动画（MU Animation on Length-Oriented Objects）

长度导向对象自动动画零件；若存在名为 `Default` 的路径则使用它。

- **AngularConverter、FootPath、Turnplate、Turntable**：各承载并运输单个零件。
- **Conveyor、Track、TwoLaneTrack**：承载并运输多个零件。
- 所有长度导向对象都可添加 **Animation Offset** 并选择/清除 **Gravity Mode**；按 **M** 键在场景中显示操纵器。
- **Conveyor** 在传送带中央的蓝色线上动画零件；**FootPath** 在中央蓝线上动画 Worker；**Converter** 自动动画零件（长度方向 `Default`、横向 `Cross`）；**Track** 在行驶轨道中央动画 Transporter；**TwoLaneTrack** 自动动画 Transporter（视车道与左右行设置使用 `A` 或 `B` 路径）。

### 9.2 点导向对象上的 MU 动画（MU Animation on Point-Oriented Objects）

对于承载单个零件的点导向对象（如 Station），可指定 **Animation Object** 与 **MU Side to Attach**，并添加、扩展、编辑、删除动画路径。

- **Station** 使用 `Default` 路径动画零件。点击 **Show** 显示路径；因只能处理单个零件，路径由单个点组成。路径工具（红色金字塔）显示零件动画位置，可点击并用箭头键移动。
- **DePortioner**、**Portioner** 均使用 `Default` 路径。

### 9.3 承载多个零件的点导向对象（MU Animation on Point-Oriented Objects Holding Several Parts）

可指定 **Animation Object** 与 **MU Side to Attach**，并添加、扩展、编辑、删除动画路径。

- **Buffer**：沿标准动画路径向上逐个堆叠零件；在 Attributes 选项卡仿真属性中设置容量。
- **PickAndPlace** 机器人：自动动画零件。若存在路径，第一个 MU 用第一条、第二个用第二条，依此类推；若无合适路径但有 `Default`，则用该路径。
- **WorkerPool**：可选择在动画路径上动画 Worker 或在沿 Y 方向分布的动画区域上动画。Class Library 中的 WorkerPool 仅当在 Graphics 选项卡激活 **Show Content** 时才显示已创建 Worker。
  - 设 **Animation Path** 时：第一个 Worker 用第一条路径、第二个用第二条，依此类推；若无合适路径但有 `Default`，则用该路径。
- **Workplace**：可选择在动画路径上动画 Worker 或在沿 X 方向分布的动画区域上动画。

若不用动画区域：Plant Simulation 依次用第一条/第二条/第三条动画路径动画第一/第二/第三个 Worker（需自行定义）。若无第三条路径则用默认路径；若无默认路径则完全不动画该 Worker。

### 9.4 带装载空间对象上的 MU 动画（MU Animation on Objects with Loading Space）

Plant Simulation 在动画区域上动画带装载空间对象上的 MU。通常可使用出厂设置，除非不满足需求；Plant Simulation 将零件均匀分布到由长度和宽度定义的动画区域。

> **注意：** 路径索引从 0 开始，而非 1。签名 `#0#0` 表示第一个动画点；`#1#2` 表示 X 索引 2、Y 索引 3 的位置。

> **注意：** Plant Simulation 推荐使用动画区域而非动画路径，因为建模工作量大幅减少（无需创建动画路径）。

各对象动画零件的方式：

- **AGVPool**：仅在 Graphics 选项卡激活 **Show Content** 时显示已创建 Transporter。若动画区域激活则使用它（MU 索引为 Y 方向区域索引，X 方向容量恒为 1）；否则依次用路径，无合适路径但有 `Default` 则用默认路径。
- **Container**（标准设置，两排各两件）显示四个装载零件。
- **ParallelStation** 默认容量 4 个零件，标准设置将其分布到动画区域；增大 X 方向容量（如 3）或动画区域长度以重新均匀分布。
- **PlaceBuffer** 默认容量 4：若动画区域激活则使用它；若存在多于一个锚点的 `Default` 路径，则 MU 索引转换为相对位置并沿线均匀分布；否则依次用路径，若只有单点 `Default` 路径则用该路径。
- **Store**（标准设置，三排各三件）显示九个适合单个存储格子的零件；可更改单个存储格子尺寸并在 Z 方向设置容量以堆叠零件；存储区位于 XZ 平面。
- **Transporter** 标准设置（Store + 动画区域，两排各三件）显示六个装载零件：主动装载空间类型 Line 用 `Line` 路径；被动装载空间类型 Track 用 `Track` 路径。
- **Worker** 默认 X、Z 方向容量各 1；Z 方向输入 `2` 可背两件堆叠零件；X 方向输入 `2` 并清除 **Animation Area** 可两手各拿一件（改用定义的动画路径）。

### 9.5 Workplace 动画路径上的 MU 动画（MU Animation on Animation Paths on the Workplace）

Workplace 默认提供一条名为 `Queue` 的 MU 动画路径，用于动画无法进入的 Workplace 前排队的 Worker，可视化队列。

> **注意：** 若 Workplace 未提供 `Queue` 路径，所有 Worker 在进入前都在同一位置等待。

- 在 Workplace 对话框中设置 **Distance in Queue**。
- 点击 **Show** 显示路径；路径工具（金字塔）显示 Worker 动画位置，可点击并用箭头键移动。
- 也可定义 Polycurve、Spline 或 Rotation 类型路径：先将预定义的 `Queue` 重命名（如 `MyQueue`），再创建所需类型的名为 `Queue` 的新路径；要恢复默认路径，重命名新路径并把原路径名改回 `Queue`。
- 在动画区域动画 Worker：勾选 **Animation Area** 并定义设置。

若不用动画区域：依次用第一/第二/第三条动画路径动画 Worker（需自行定义），否则回退到默认路径，无默认路径则不动画。多数情况下动画路径是 Workplace 上动画 Worker 的合适方式，但建模需要时也可用动画区域。

## 10. 建模关节与姿态（Modeling Joints and Poses）

示例模型用关节（joints）与姿态（poses）建模真实运动学，设置位于 **Edit 3D Properties** 的 **Joint** 与 **Poses** 选项卡。

姿态用于动画对象自身：与普通自动画不同，只需设置动画要移动到的位置；Plant Simulation 知道先前位置并内部创建自动画，确保从旧状态到新状态的平滑过渡。

示例模型中：Source 生产零件，Conveyor 将零件送到加工工站处理。旋转关节（revolute joint）使 ToolHead 左右旋转，移动关节（prismatic joint）使 ToolHolder 上下移动；Station 再把零件交给 Drain 移出设备。Start Page 的 Factory 51 示例模型展示了旋转与移动关节的更多用法。

### 10.1 配置仿真对象（Configure the Simulation Objects）

- **Source**：恒定创建间隔 10 秒，其余默认。
- **Conveyor**：容量 1（只运输单个零件），其余默认。
- **Station**：处理时间 20 秒、恢复时间 5 秒，其余默认。
- **Drain**：默认设置。

### 10.2 创建动画对象（Create the Animation Objects）

零件位于机器上时，ToolHead 向右旋转、ToolHolder 上移；处理时间期间二者保持新位置，随后都返回原始姿态。

1. 右键 Station 在新窗口打开。
2. 右键名为 `default.tool` 的图形部分。
3. 选择 **Make Animatable Object**，命名 `ToolHead`，点击 **OK**。

> **注意：** **Object Position** 设置旋转原点（ToolHead 绕其旋转）。若对象旋转异常，检查旋转原点各轴数值。

4. 在 Tab Joint 设置关节（见下一节）。
5. 右键 ToolHead 在新窗口打开。
6. 左键点击 ToolHead，按 **+** 键（方形伸缩支座部分）选中 ToolHolder，右键选择 **Make Animatable Object** 并输入名称。仿真期间 ToolHolder 上下移动。

### 10.3 配置关节（Configure the Joints）

为 ToolHead 配置旋转关节（Revolute Joint），为 ToolHolder 配置移动关节（Prismatic Joint）。

- 右键 ToolHead → **Edit 3D Properties**，转到 **Tab Joint** 选择旋转关节设置。
- 左键点击 ToolHolder 按 **空格键**，转到 Joint 选项卡。因 ToolHolder 需沿 z 方向移动，点击 **Z** 旁按钮设为平移方向，再选择关节设置。

### 10.4 配置姿态（Configure the Poses）

在 **Tab Poses** 上：

1. 右键 Station 窗口背景，添加 `Pose1` 与 `Pose2`。
2. 左键点击 `Pose1` 点击 **Edit**，对话框显示 Joint 选项卡所选设置。
3. 左键点击 `Pose2` 点击 **Edit**，对话框显示 Joint 选项卡所选设置。
4. 关节与姿态配置完成后，在相应控制中编程运动。返回仿真对象，转到 **Controls** 选项卡创建 **Entrance Control** 与 **Exit Control**。

在控制中定义 ToolHead 与 ToolHolder 移动到的姿态。

Entrance Control：

```simtalk
?._3D.Poses.moveTo("Pose2") // moves to Pose2
```

Exit Control：

```simtalk
wait ?._3D.Poses.moveTo("Pose1") // returns to Pose1
@.move                           // and moves the part
```

仿真启动后可看到 ToolHead 旋转、ToolHolder 上移再下移。为更好观察，选择 Real time factor x 3。

### 10.5 显示与隐藏姿态（Showing and hiding poses）

用切换按钮显示/隐藏姿态。Plant Simulation 一次只显示一个姿态；显示另一姿态时会先隐藏已显示姿态，再把对象移动到该姿态对应状态。

姿态显示且对话框打开时，可用左右箭头键逐步改变姿态状态：

- 若两个限值都已定义：按关节设置范围的 1° 旋转姿态。
- 选移动关节（Prismatic Joint）且至少缺一个限值：移动 0.1 m。
- 选旋转关节（Revolute Joint）且至少缺一个限值：旋转 1°。

左箭头键使姿态朝下限移动，右箭头键朝上限移动，与旋转轴或平移方向无关。

## 目录说明

- `paths-mu-joints-poses.md`：本目录源文件（Markdown 版本），涵盖“使用动画路径”“控制 MU 动画”“建模关节与姿态”三个章节。
- `paths-mu-joints-poses.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Working with Animation Paths", "Controlling the MU Animation" and "Modeling Joints and Poses"。Unpublished work. © 2026 Siemens.*
