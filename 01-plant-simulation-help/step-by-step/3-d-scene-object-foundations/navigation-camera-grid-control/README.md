# Navigation, Camera & Grid Control（导航、相机与网格控制）总结

本目录包含 `navigation-camera-grid-control.md`（以及同名文本提取文件 `navigation-camera-grid-control.txtx`），内容为 Plant Simulation 帮助文档中 **导航、相机与网格控制** 相关章节的说明。以下是对其内容的总结。

## 1. 可视化物料流（Visualizing the Material Flow）

介绍创建与可视化仿真模型时最重要的任务。Plant Simulation 区分以下对象类型：

- Simulation Object（仿真对象）
- Animatable Object（可动画对象）
- Graphic Group（图形组，已定义）
- State Graphic（状态图形，已定义）
- Graphic（图形，已定义）

**Show Graphic Structure** 上下文菜单对话框以树结构显示这些对象类型。3D 窗口用颜色区分选中对象：

| 对象类型 | 选中后颜色 |
|---|---|
| 仿真对象（Simulation Object） | 绿色（打开后内部显示绿色边框） |
| 可动画对象（Animatable Object） | 紫色（打开后内部显示紫色边框） |
| 图形（Graphic） | 黄绿色 |

## 2. 创建仿真模型（Creating a Simulation Model）

分几个步骤创建仿真模型：

- **新建模型**：点击 Start Page 上的 **Create New Model**，或选择 **File > New**。
- **显示内置对象**：在 Class Library 中右键 **MaterialFlow** 文件夹并选择 **Open in 3D**（其他文件夹同理）。
- **显示对象名称**：将鼠标拖过对象即可显示其名称。

### 基本鼠标导航

| 操作 | 鼠标方式 |
|---|---|
| 旋转场景 | 按住左键 + 右键拖动，或 **Ctrl** + 右键拖动 |
| 平移场景 | 按住右键拖动 |
| 前后移动相机 | 滚动鼠标滚轮 |
| 缩放 | 滚动鼠标滚轮，或 **Shift** + 右键拖动 |

> 三键鼠标：描述中说“点击鼠标滚轮”的地方，点击中键即可。
>
> 若鼠标操作无效，检查 **Start > Control Panel** 中 Mouse Properties 的 Wheel 设置。

### 插入对象

- 在 Class Library 中右键文件夹选择 **Open in 3D** 打开新窗口。
- 插入前建议开启 View 选项卡上的 **Show Grid**，以便精确定位；不显示网格时默认使用源对象的原始坐标。
- 在 Toolbox 中选择对象，拖到目标位置后左键点击插入；选中对象期间会显示预览。
- 右键点击可取消插入。
- 示例：插入 **Source**、**Conveyor**、**Station**、**Drain**。

### 连接对象

- 确保 View 选项卡上的 **Show Connections** 已激活（3D 默认不显示 Connector）。
- 点击 Toolbox 的 **MaterialFlow** 选项卡上的 **Connector**。
- 左键点击源对象，然后拖到目标对象并再次左键建立连接。
- 3D 将 Connector 显示为两个内部接口之间的连线，尖锥表示方向。
- 在点击目标前右键或按 **Esc** 可终止连接模式。
- 连续连接多个对象：按住 **Ctrl**，先挂到第一个对象，再依次拖动点击。

### 启动仿真

- 使用 **Home** 选项卡上的按钮，或双击 **EventController** 图标并使用其按钮。
- 观察产出的零件如何在仿真对象上移动。

## 3. 3D 中的层次化建模（Modeling Hierarchically [in 3D]）

层次化建模可给区域和机器添加任意细节：在 **Frame** 中用内置类或自定义类创建机器、生产区域等，再将该 Frame 插入另一个 Frame（例如把生产区域插入整厂的 Frame）。

## 4. 操作场景（Working with the Scene）

对活动场景本身（而非场景中插入的对象）的操作包括：

- 用鼠标操作场景
- 将视图对齐到主方向
- 随模型保存视图并可返回
- 沿定义路径飞行

按 **F** 键可显示/隐藏场景信息：帧率（FPS）、节点总数、多边形总数、内存占用、OpenGL 版本、显示驱动信息。

### 用鼠标操作场景

也可使用 **Space Navigator** 鼠标代替普通鼠标。

- **旋转**：左键 + 右键拖动，或 **Ctrl** + 右键拖动。
  - 若开始旋转后在指针停留位置保持至少 400ms，且指针下方有对象/图形，则绕该位置旋转。
  - 否则绕窗口中心在插入平面上的投影旋转（视图旋转 90° 时为对应的正交方向），此时指针位置无关。
- **平移**：右键拖动（三键鼠标可用中键拖动）。
- **前后移动相机**：滚动滚轮，或 **Shift** + 右键拖动。
  - **1/10 速度**：**Ctrl** + 滚动滚轮。
  - **10 倍速度**：**Shift** + 滚动滚轮。

**Planning View（平面视图）** 中：

- 在平面上移动场景：右键拖动。
- 缩放：滚动滚轮，或 **Shift** + 右键拖动。
  - **1/10 速度**：**Ctrl** + 滚动滚轮。
  - **10 倍速度**：**Shift** + 滚动滚轮。

### 将视图对齐到主方向

使用 **View** 选项卡上的命令从预定义方向查看场景：**Top**、**Front**、**Left**、**Right**、**Back**、**Bottom**。

- 顶部俯视、正面、左侧、底部（沿负 z 轴向上看）。
- 若 **Show Grid** 激活，网格显示在对象下方。
- 若 **Show Base Plate** 激活，底板显示在对象下方并遮挡对象本身。
- 若选中了对象，命令会适配该选择而非整个场景。
- **View All** 使整个场景适配窗口并显示所有对象。

### 随模型保存视图并可返回

将当前相机位置/方向随模型保存，以便稍后返回。

- 在 3D 中点击 View 选项卡的 **Camera Marks**。
- 在 **Mark Current Camera Settings** 对话框中输入 **Name**。
- 3D 在 **Scene Path** 字段显示场景路径。
- 点击 **OK**，该设置随活动的根对象保存到模型文件。

返回已保存视图：点击 **Camera Marks** 的下拉箭头选择相机标记，或选择 **Camera Marks** 命令并点击 **Activate**。

- 可对相机标记进行 **Rename** 或 **Delete**。
- 用上下箭头按钮调整相机标记在列表中的顺序。

### 设置场景背景色

为选中的 Frame 或 Class Library 文件夹设置 3D 窗口背景色：

- 点击 Home 选项卡的 **Edit 3D Properties**（或右键 Frame 窗口选择 **Edit 3D Properties**），打开 **Background** 选项卡；也可按**空格键**打开。
- 选择 **Assign a Background Color of Its Own**。
- 选择 **Base Color**（预定义色，或 **More Colors → Select** 在矩阵中选色）。
- 用四个滑条设置 **Corner Brightness** 以定义颜色渐变。

> 若未定义背景色，Plant Simulation 使用父对象的背景色。

## 5. 沿定义路径飞行（Flying on a Defined Path Through the Scene）

将相机附着到对象上，通过该对象的“镜头”查看场景，相机随对象在仿真运行中移动。共有三种相机：

- **Main camera（主相机）**：正常视图。
- **Object camera（对象相机）**：附着到对象（如零件或 Worker）并随之移动。
- **Animation camera（动画相机）**：沿定义的动画路径移动。

定义跟踪镜头：

- 左键选中对象。
- 点击 View 选项卡的 **Animate Camera** 打开 **Fly on Path**（未选中对象时对话框指当前根对象）。
- 选择相机路径；在 **Edit 3D Properties > Tab Camera Animation** 中定义/编辑路径。

### 将相机附着到对象

- 选中单个对象。
- 点击 3D 窗口 View 选项卡的 **Attach Camera**。
- 相机附着在对象包围盒顶部中心，偏移量为 `(0, 0, 0.1)`，使视点位于顶面上方。
- 默认对象相机沿正 x 轴观察，以正 z 轴为 Up 方向。

对象移动时相机会自动随之移动。

### 从对象上分离相机

点击 View 选项卡的 **Detach Camera** 返回正常视图。

对象相机也会在以下情况被分离：

- 删除相机所附着的对象时。
- 改变场景时。

### 动画化对象相机

在所选 Frame 的相机动画路径上动画化相机，营造飞越场景的效果。

> 需先在 Frame 的 **Tab Camera Animation** 上定义相机动画路径。

- 转到 View 选项卡点击 **Animate**。
- 在 **Fly on Path** 的 **Path Name [MU animation]** 中选择动画路径。
- 选择 **Backwards** 可朝起点方向移动（Plant Simulation 自动输入负速度）。
- 点击 **Play** 开始、**Pause** 暂停、**Stop** 停止（均独立于仿真）。

动画结束时，3D 将主相机设为动画相机的最后位置并删除动画相机。动画相机使用 `(0, 0, 0.1)` 的镜头偏移。

可用 **Edit Path** 的 **Test** 选项卡选择动画图形测试路径。

## 6. 控制场景中的视图（Controlling Your View in the Scene）

3D 窗口控制代表观察者眼睛的相机，可执行：

- 设置主方向
- 设置视点
- 将相机附着到对象/Frame 并分离
- 动画化相机

### 设置主方向

独立于活动相机，随时可将视图调整到视图或对象的任意主方向。选中对象时，3D 窗口会缩放该对象并将相机方向适配到所选对象坐标系的主方向。

### 设置视点

随时保存任意视图（主相机位置/方向）并稍后返回。也可将活动相机设置连同活动根对象以有意义的名字保存为 **Camera Mark**。

与自动保存的视点不同，可保存任意数量的 Camera Mark（保存在模型文件中），并可随时重命名/删除。

### 将相机附着到对象/Frame 并分离

将相机附着到任意对象以通过其镜头观察，不需要时再分离。对象移动时（例如仿真运行期间）相机随之移动。

Plant Simulation 还会：

- 将附着的相机可视化为可动画对象。
- 允许在对象视图与正常视图间切换。
- 允许手动变换相机（在对象视图中改变视图，或在正常视图中操作对象）。
- 允许设置动画的速度和方向。
- 允许独立于其他动画/仿真暂停、继续和停止相机动画。

### 动画化相机

让相机在所选对象或根对象的任意动画路径上移动，在路径上飞行并观察场景。

Plant Simulation 还会：

- 将动画相机可视化为可动画对象。
- 允许在动画期间在动画视图与正常视图间切换。
- 允许手动变换动画相机。
- 允许定义动画速度和方向。
- 允许独立于其他动画/仿真暂停、继续和停止相机动画。

## 7. 使用网格（Working with the Grid）

Plant Simulation 将网格作为插入对象的表面。

> 显示或隐藏网格会影响对象行为：
> - **显示**网格时，操作对象参照**网格平面**。
> - **隐藏**网格时，操作对象参照**视图平面**（垂直于观察方向）。

- 修改当前模型网格设置：点击 View 选项卡的 **Settings** 打开 **Edit Grid and Base Plate Settings**。
- 修改新模型网格设置：选择 **File > Preferences > 3D**。

网格行为：

- 网格原点位于窗口左上角，分别向右和向下偏移一个网格单位。
- 每次模型更改后重绘场景时，Plant Simulation 会重新创建网格；网格会扩展/收缩以显示所有对象。
- 网格是建模辅助工具，展示模型时通常按 **Ins** 键隐藏。
- 原点线（默认为红色）始终是网格的一部分。
- 网格尺寸始终是最小可见网格距离的倍数。

可执行：显示/隐藏网格、设置网格属性、编辑网格线、将网格定位到不同平面、在窗口中移动网格。

插入对象后，可将其对齐到网格、吸附到网格、吸附到其他对象，或在网格上排列（需确保 **Show Grid** 开启）。

### 显示和隐藏网格

- 点击 View 选项卡的 **Show Grid**，或按 **Ins** 键。

### 设置网格属性

点击 View 选项卡的 **Edit Grid and Base Plate Settings**。

- 给网格线下方底板分配材质：点击颜色框并在 **Material** 对话框（Tab Material）中选择材质组件；用 **Show Base Plate** 显示/隐藏底板。
- 给坐标轴（x 轴和 y 轴）分配颜色：使用 **Axes Color** 下拉列表。
- 定义网格线设置：编辑选项卡上的表格。

### 编辑网格线

在 **Grid Lines** 组框中编辑或新增网格线。

- **添加**网格线：点击 **Add**，输入两线间距（如 2 米）、选择颜色（如亮蓝）、选择 **Visible** 显示，并设置插入对象是否吸附到该网格线（吸附可实现鼠标精确定位）。
- **编辑**现有网格线：选中后编辑其间距、颜色、吸附行为及可见性。

### 将网格定位到不同平面

Plant Simulation 使用**左手坐标系**：

- **x 轴**：从左到右
- **z 轴**：从下到上
- **y 轴**：从前到后

点击 View 选项卡的 **Transform**，在 **Grid Position and Orientation** 中选择单选按钮：

- **XY Plane**：x 轴与 y 轴定义的平面。
- **XZ Plane**：x 轴与 z 轴定义的平面。
- **YZ Plane**：y 轴与 z 轴定义的平面。

> 这些对话框设置不会被保存，仅在对话框打开期间有效。

### 在窗口中移动网格

点击 View 选项卡的 **Transform**，在 **Grid Position and Orientation** 的 **Position** 下使用文本框/按钮移动网格原点。

> 设置不会被保存，仅在对话框打开期间有效。
>
> 移动原点使用 **Model Settings > Units > Length** 中的长度单位。

滚轮调整（在文本框中滚动滚轮）：

| 轴 / 方向 | 0.01 单位 | 0.1 单位 | 1 单位 |
|---|---|---|---|
| x 向右 | Ctrl + 向前 | 向前 | Shift + 向前 |
| x 向左 | Ctrl + 向后 | 向后 | Shift + 向后 |
| y 向后 | Ctrl + 向前 | 向前 | Shift + 向前 |
| y 向前 | Ctrl + 向后 | 向后 | Shift + 向后 |
| z 向上 | Ctrl + 向前 | 向前 | Shift + 向前 |
| z 向下 | Ctrl + 向后 | 向后 | Shift + 向后 |

- **Scene Origin**：将 x/y/z 重置为默认值 `0, 0, 0`。
- **Object Origin**：将 x/y/z 设为单个选中对象的位置。

## 目录说明

- `navigation-camera-grid-control.md`：导航、相机与网格控制章节的 Markdown 版本（本总结的源文件）。
- `navigation-camera-grid-control.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
