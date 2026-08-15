# PickAndPlace Robot（拾放机器人）— General 总结

本目录存放 **PickAndPlace Robot**（拾放机器人）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致），并汇总了兄弟子文件夹 `methods/`、`attributes/`、`read-only-attributes/` 中对应文档（`methods.md`、`attributes.md`、`read-only-attributes.md`）的要点。以下是对这些内容的总结。

## 1. 对象用途

**PickAndPlace robot** 用于在一个工位拾取工件（part），旋转，并将其放置到另一个工位。它可一次拾取和运送一个或多个工件（数量由 **Capacity** 设置）。该机器人可模拟 TransferStation 的大部分功能。

## 2. 物料流（Flow of materials）

1. 工件到达前驱对象出口，并通知拾放机器人它希望被拾取。
2. 机器人决定是否拾取该工件：
   - 无 **Pull Control** 时，机器人被通知后即接受工件。
   - 有 **Pull Control** 时，机器人执行该控制，当工件被选中时才拾取。
3. 机器人旋转到相应的前驱对象并拾取工件。
4. 对于目标工位，机器人使用其默认 **Exit Strategies** 或 **Target Control**（在其中设置目标工位）。Target Control 在机器人拾取或放置工件时被调用；在方法 `setDestination` 中，布尔参数控制机器人是否在目标工位等待。
5. 机器人旋转到目标工位并放置工件。
6. 然后旋转回到标准位置（默认位置）。

## 3. 配置机器人

### 显示操纵器（Show Manipulators）

点击编辑功能区标签页的 **Show Manipulators** 或按 `M` 键，可更改图形与锚点的长度。旋转操纵器用鼠标和键盘设置对象的旋转：

- 向右拖动 → 绕 z 轴顺时针旋转；向左拖动 → 逆时针旋转。
- 点击操纵器后按左/右方向键 → 旋转 1°。
- 按住 `Shift` + 左/右方向键 → 旋转 45°。

> 注意：旋转操纵器不能与 3D 窗口中的任何其他对象同时被选中。

### 添加到模型

点击 Home 功能区标签页 **Manage Class Library > Basic Objects > MaterialFlow > PickAndPlace**。示例模型：Window 功能区标签页 > Start Page > Getting Started > Example Models > Small Examples。

### 通过拖放配置机器人

将拾放机器人拖到 Conveyor、Track 或 TwoLaneTrack 上并选择操作。拖放仅适用于可定义传感器的长度方向对象。一次完整配置需要两次拖放操作（一次 pick/unload + 一次 place/load）。

| 操作 | 行为 |
| --- | --- |
| **Pick part** | 在传感器处从长度方向对象拾取工件。创建前触发光栅模式传感器，以及将工件移动到机器人的传感器控制。 |
| **Unload part** | 在传感器处从 Container 或 Transporter 卸载工件。创建前触发光栅模式传感器，以及向机器人卸载的传感器控制。 |
| **Place part** | 在传感器处将工件放置到长度方向对象上。创建后触发光栅模式传感器（无传感器控制）；同时设置 Target Selection、Target Object 和 Target Sensor ID。 |
| **Load part** | 在传感器处将工件装载到 Container 或 Transporter 上。创建由登记点触发的传感器（无传感器控制）；设置 Target Selection、Target Object 和 Target Sensor ID。 |

所有情况 Plant Simulation 都会在 **Angles Table** 和 **Times Table** 中创建条目。

### 配置机器人（Robot Arm Animation）

**Robot Arm Animation** 选项卡决定机器人在拾取或放置工件前所经过的路径。机器人手臂动画路径仅用于至少具有三个轴的机器人。

动画对象在 **MU Animation** 选项卡的 **Animation Object** 文本框中定义。机器人从上到下检查机器人类型，并在第一个匹配处停止：

1. Six Axis Robot（六轴机器人）
2. Five Axis Robot（五轴机器人）
3. Four Axis Robot with Ball Joint Gripper（带球关节夹持器的四轴机器人）
4. SCARA Robot with Concluding Revolute Joint（末轴为旋转关节的 SCARA 机器人）
5. SCARA Robot with Concluding Prismatic Joint（末轴为移动关节的 SCARA 机器人）
6. Three Axis Robot（三轴机器人）
7. One Axis Robot（单轴机器人）
8. Linear Robot（线性机器人）

若均未识别，机器人将绕旋转轴 `[0,0,-1]` 通过旋转中心 `[0,0,0]` 完全旋转。

> 注意：Plant Simulation 13.0 之前的默认机器人是单轴机器人；从旧模型加载时此类机器人不会被更改。

CranesAndMore 库提供了一个在轨道上移动的七轴机器人作为演示器。你可以通过将任何物料流或流体对象的图形替换为 `3D\s3d-graphics` 中的机器人图形，将其转换为机器人。

#### 各类机器人的识别标准

- **六轴机器人**：需满足一系列旋转关节条件（绕 `[0,0,1]`/`[0,0,-1]`、`[0,1,0]`/`[0,-1,0]` 等），且 `_3D.AnimationObject` 引用最底层可动画对象、存在合适的动画路径。可到达夹持范围内所有点，并将 MU 定位到所有可达位置。`PickAndPlaceComau.s3d` 与 `PickAndPlaceKuka.s3d` 为六轴机器人。
- **五轴机器人**：一个绕 z 轴的旋转关节 + 三层绕 y 轴的旋转关节 + 一个绕 z 轴的旋转关节，可定位 MU 到大部分（但非全部）位置。
- **带球关节夹持器的四轴机器人**：Plant Simulation 的默认机器人，无法用鼠标或键盘移动其姿态和关节。
- **末轴为旋转关节的 SCARA 机器人**：仅能将 MU 放置到完全由绕 z 轴旋转所描述的位置。
- **末轴为移动关节的 SCARA 机器人**：`PickAndPlaceComauSCARA.s3d` 是 SCARA 机器人。
- **三轴机器人**：MU 刚性固定在夹持器上，仅随机器人运动而旋转。
- **单轴机器人**：无法到达夹持范围内所有点，且不使用用户定义的机器人手臂动画。
- **线性机器人**：由正交的移动关节（prismatic joint）定义，即使最末可动画对象不存在仍可被识别。

## 4. 对话框

双击图标打开对话框。共享仿真属性见 *Dialog Items of the Objects*。编辑 3D 属性：点击 **Edit 3D Properties** 或按空格键。

### 选项卡 Attributes（属性）

#### Angles Table [PickAndPlace]（角度表）

打开机器人拾取或放置工件角度的表。可查看/微调：

- **Name** — 前驱（拾取）或后继（放置）。也可输入传感器，如 `Conveyor.Sensors.ID1`。
- **Angle** — 工位与机器人之间的角度。

Connector/拖放会自动添加值；删除 Connector 不会删除条目，需手动删除。右键机器人选择 **Calculate Angles** 可重新计算角度。

SimTalk：`setAnglesTable`、`getAnglesTable`、`calculateAngles`。

#### Times Table [PickAndPlace]（时间表）

打开工位之间（及返回）旋转时间的表，还包含乘所有时间的 **Time Factor**。

- 所有被服务对象的 **Names** 与 **Default Angle**。
- **对角线上方**的时间 = 空载旋转；**对角线下方** = 满载旋转（带工件）。

自动填充时假设四分之一圈旋转需一秒。删除 Connector 不删除条目；在 Angles Table 中删除后点击 Apply 会同时从 Times Table 移除。

SimTalk：`setTimesTable`、`getTimesTable`。

#### Go to Default Position（复选框）

放置工件后旋转回默认位置。激活时可再激活 **Only for Empty Blocking List**。

SimTalk：`GoToDefaultPosition`、`OnlyForEmptyBlockingList`、`DefaultAngle`。

#### Only for Empty Blocking List（仅空阻塞列表）

仅当阻塞列表为空（无其他请求）时才旋转回默认位置。仅在 **Go to Default Position** 激活时可更改。

#### Use Kinematics for Times（使用运动学计算时间）

使用机器人 3D 运动学而非 Angles/Times 表来计算时间。仅支持受支持的机器人运动学（线性机器人除外），支持 `_3D.Poses.moveToCoordinate`、`moveToMU`、`moveToMUAnimationPosition` 使用的所有运动学。增大 **Joint Velocity** 可加快手臂移动。

SimTalk：`UseKinematicsForTimes`。

#### Time Factor（时间因子）

乘 Times Table 中所有时间，用于模拟不同速度而无需编辑表。

SimTalk：`TimeFactor`。

#### Default Angle（默认角度）

当选择 **Go to Default Position** 时机器人旋转到的角度（度）。加 180° 可面向起始位置。范围 0°–360°。复位后也作为起始位置（与复选框无关）。

SimTalk：`DefaultAngle`。

#### Blocking Angle（阻塞角，文本框）

机器人旋转时不能越过的角度（阻止最短路径）。默认 `-1` = 无阻塞角。范围 0–360。仅影响动画，仿真由 Times Table 控制。

SimTalk：`BlockingAngle`。

#### Capacity（容量，文本框）

机器人一次可运输的 MU 数量（大于 1）。可拾取多个工件并逐一放置（FIFO）。其他规则（如 LIFO）需编程 Exit Control。

SimTalk：`Capacity`。

#### MU Conveying Direction（MU 输送方向，下拉列表）

| 设置 | 描述 |
| --- | --- |
| **Retain** | 沿到达方向继续输送。 |
| **Rotate 90° to the right** | 相对旋转 90° 向右。 |
| **Rotate 90° to the left** | 相对旋转 90° 向左。 |
| **Rotate 180°** | 相对旋转 180°。 |
| **Forwards** | 绝对旋转使其向前。 |
| **Lateral right** | 绝对旋转使其侧向右。 |
| **Backwards** | 绝对旋转使其向后。 |
| **Lateral left** | 绝对旋转使其侧向左。 |

> 注意：`Retain`、`Rotate by 90°`、`Rotate by 180°` 为相对旋转；`Forwards`、`Lateral right`、`Backwards`、`Lateral left` 为绝对旋转。

SimTalk：`MUConveyingDirection`。

#### Loading Time（装载时间）

在工位拾取工件的时间：

- 点方向工位：拾取时工件登记到机器人，工位锁定至装载时间结束。
- 长度方向工位：装载期间工件留在工位上，之后移动到机器人。

可选择分布（或常量 `Const`）。`Formula` 可输入数值表达式或 Method 名；用 `@` 表示工件、`?` 表示机器人。装载期间不能向交付工位放置工件。机器人中断会延长装载时间；交付工位中断不影响装载。

SimTalk：`LoadingTime`、`LoadingTime.Type`、`IsLoading`、`putAttributeNamesIntoTable`。

#### Unloading Time（卸载时间）

将拾取的工件放置到目标工位的时间：

- 点方向工位：放置时工件登记到机器人，目标工位锁定至卸载时间结束。
- 长度方向工位：工件在卸载时间开始前移动到其上。

同样的分布/Formula 选项（`@` = 工件，`?` = 机器人）。机器人中断会延长卸载；目标工位中断不影响卸载。

SimTalk：`UnloadingTime`、`UnloadingTime.Type`、`IsLoading`、`putAttributeNamesIntoTable`。

### 选项卡 Failures（故障）

按通用 **Tab Failures** 说明定义。

### 选项卡 Controls（控制）

控制修改内置行为。点击省略号选择已有 Method，按 `F2` 编辑源代码，或将 Method 拖入文本框。

创建 Method 类型的用户自定义属性控制：

- 输入名称并选择 **Create Control** → 插入 `self.Name`，如 `self.A1Ctrl`。
- 或在空文本框选择 **Create Control** → 插入 `self.On内置控制名`，如 `self.OnEntrance`。

删除控制即删除用户自定义属性（仅删除名称则保留属性）。

#### Target Control（目标控制）

机器人拾取工件后（准备退出前）立即调用，设置机器人放置工件的目标。放置工件后也调用，此时通过 `setDestination` 设置下一个拾取对象（此时 `@` 为空）。仅在卸载且 **Go to Default Position** 未勾选时调用。必须使用 `setDestination` 确定目标对象。

> 注意：不要用 Exit Control 确定目标——它调用得太晚（仅在 MU 准备退出时）。

SimTalk：`TargetCtrl`、`setDestination`、`getDestination`。

#### Pull Control（拉取控制）

机器人准备好拾取新工件时调用，决定接受哪个等待的工件：用 `fwBlockList` 获取 Forward Blocking List，用 `unblock` 解阻塞 MU；用只读属性 `FwBlockListEntry1` 可更快访问首项。它在已确定移动到此后继的工件中选择（不选择后继）。

示例用途：优先拉取红色工件（优先级），然后是其他颜色。

SimTalk：`PullCtrl`。

### 选项卡 Exit（出口）

- **Target Selection > Exit strategy or target control**：选择出口策略；机器人需通过 Connector 连接。选择 **Wait for Free Target** 仅在目标就绪时才旋转/拾取。
- **Target Selection > Place part at sensor** / **Load part onto MU at sensor**：显示 **Target Object** 与 **Target Sensor ID**；机器人使用你创建的传感器（无需 Connector）。

#### Wait for Free Target（等待空闲目标）

仅当目标准备接收时机器人才旋转拾取工件，防止将工件运送到占用/保留的 Station 或 Conveyor，保持机器人可用。仅对 **Exit strategy or target control** 求值。工件进入目标的 Forward Blocking List。出口策略/Target Control 在机器人旋转拾取前求值。

SimTalk：`WaitForFreeTarget`、`TargetSelection`、`ReservedFor`、`ReservedPlace`、`contentsAndReservedList`。

#### Target Selection（目标选择，下拉列表）

- **Exit strategy or target control** — 默认；通过 Exit Strategy 或 Target Control 设置目标。
- **Load part onto MU at sensor** — 需在长度方向目标上手动创建前触发光栅传感器，并设置 Target Object 与 Target Sensor ID。无控制时停止/装载/发送自动工作。
- **Place part at sensor** — 需手动创建后触发光栅传感器，并设置 Target Object 与 Target Sensor ID。

SimTalk：`TargetSelection`。

#### Target Object（目标对象）

工件放置/装载到的长度方向对象路径（或通过 **Select Object** 选择）。

SimTalk：`TargetObject`。

#### Target Sensor ID（目标传感器 ID，文本框）

目标传感器的传感器 ID。传感器不会自动创建——手动创建或使用拖放。

SimTalk：`TargetSensorID`。

### 选项卡 Statistics（统计）

除标准统计外，机器人还收集：

| 项目 | 描述 | 只读属性 |
| --- | --- | --- |
| **Rotation Empty** | 空载旋转的时间占比。 | `StatRotationEmptyPortion` |
| **Rotation Loaded** | 运载工件旋转的时间占比。 | `StatRotationLoadedPortion` |

在 Statistics Report（`F6` 或 View > Show Statistics Report）中查看。

### 选项卡 Importer / Energy / Costs / User-defined

- **Importer**：拾放机器人仅提供 **Failure Importer**。
- **Energy**：按通用 **Tab Energy** 说明选择能源设置。
- **Costs**：机器人在拾取、旋转、放置工件期间累积成本（投资 + 运营成本）。投资成本仅在折旧期内累积。成本作为应计成本分配到工件；若机器人空载，成本作为一般成本留在机器人上。
- **User-defined**：按通用 **Tab User-defined** 说明定义自定义属性。

## 5. 菜单

- **Navigate 菜单**：见通用 Navigate Menu 说明。
- **View 菜单**：提供 *Refresh*、*Show Statistics Report*、*Show Attributes and Methods*、*Contents*（Forward/Exit Blocking List、Associated Lockout Zones、Associated Shift Calendar）。
- **Tools 菜单**：见通用 Tools Menu 说明。
- **Tabs 菜单**：显示/隐藏各个选项卡；用 **Inherit** 切换选项卡可见性的继承。
- **Help 菜单**：见通用 Help Menu 说明。

## 6. 方法（来自 `methods/methods.md`）

拾放机器人提供左侧目录中列出的方法、物料流对象的方法（Methods of the Material Flow Objects）、以及所有对象的通用方法（Methods of All Objects）。查看方式：打开 **Show Attributes and Methods**（类库上下文菜单，或按 `F8` / 点击 Frame 的 Home 功能区标签页）。

主要方法（SimTalk）如下：

- `calculateAngles` — 计算机器人与前驱/后继连接的角度，写入 Angles Table。
- `getAnglesTable(AnglesTable:table) → table` — 返回 Angles Table 并写入表格。
- `getDestination → any` — 返回机器人拾取或放置工件的目标对象。
- `getTimesTable(TimesTable:table) → table` — 返回 Times Table 并写入表格。
- `setAnglesTable(AnglesTable:table)` — 为机器人分配 Angles Table。
- `setDestination(DestinationObject:any[, WaitAtTarget:boolean])` — 设置机器人放置工件或拾取新工件的目标对象；空载时 `setDestination(void)` 将其送到默认位置。
- `setTimesTable(TimesTable:table)` — 为机器人分配 Times Table。

## 7. 属性（来自 `attributes/attributes.md`）

拾放机器人提供左侧目录列出的属性、所有对象的属性（Attributes of All Objects）、以及物料流对象的属性（Attributes of the Material Flow Objects）。可通过对话框或 SimTalk 赋值/取值（如 `MyPickAndPlace.Capacity := 12`、`print MyPickAndPlace.TimeFactor`）。

主要属性（SimTalk）如下：

- `BlockingAngle:real` — 阻塞角，0–360 度，默认 `-1`（无阻塞角）。
- `Capacity:integer` — 一次可运输的 MU 数量（大于 1）。
- `DefaultAngle:real` — 默认角度（0°–360°）。
- `GoToDefaultPosition:boolean` — 放置工件后是否旋转回默认位置。
- `LoadingTime:time` — 拾取工件的装载时间。
- `MUConveyingDirection:string` — 输送方向，取值 `"Retain"`、`"Rotate 90° to the right"`、`"Rotate 90° to the left"`、`"Rotate 180°"`、`"Forwards"`、`"Lateral right"`、`"Backwards"`、`"Lateral left"`。
- `OnlyForEmptyBlockingList:boolean` — 仅当阻塞列表为空时旋转回默认位置。
- `PullCtrl:method` — 指定 Pull Control 方法。
- `TargetCtrl:method` — 指定 Target Control 方法。
- `TargetObject:path` — 放置/装载工件的长度方向目标对象。
- `TargetSelection:string` — 目标选择方式，取值 `"Exit strategy or target control"`、`"Load part onto MU at sensor"`、`"Place part at sensor"`。
- `TargetSensorID:integer` — 目标传感器 ID。
- `TimeFactor:real` — 乘 Times Table 所有时间的时间因子。
- `UnloadingTime:time` — 放置工件的卸载时间。
- `UseKinematicsForTimes:boolean` — 是否用 3D 运动学计算时间。
- `WaitForFreeTarget:boolean` — 是否仅在目标空闲时旋转拾取。
- `StatRotationLoadedTime → time` — 运载工件旋转的总时间（只读属性）。

## 8. 只读属性（来自 `read-only-attributes/read-only-attributes.md`）

拾放机器人提供左侧目录列出的只读属性、所有对象的只读属性、以及物料流对象的只读属性。只读属性的值只能查询、不能设置（Plant Simulation 在查询时点计算其值），多数对应对象某选项卡（如 Statistics）上不可用的对话框项。

主要只读属性（SimTalk）如下：

- `GetCurrentAngle → object` — 机器人当前所在的角度。
- `GetLastDestination → object` — 机器人最后放置或拾取工件的目标对象。
- `IsLoading → boolean` — 机器人是否正在装载。
- `IsRotating → boolean` — 机器人是否正在旋转。
- `StatRotationEmptyPortion → real` — 空载旋转时间占比。
- `StatRotationEmptyTime → time` — 空载旋转总时间。
- `StatRotationLoadedPortion → real` — 运载工件旋转时间占比。
- `StatRotationLoadedTime → time` — 运载工件旋转总时间。

## 9. 引用的关键 SimTalk 属性与方法

- 角度/时间表：`setAnglesTable`、`getAnglesTable`、`calculateAngles`、`setTimesTable`、`getTimesTable`
- 目标：`setDestination`、`getDestination`、`GetLastDestination`、`TargetObject`、`TargetSensorID`、`TargetSelection`、`WaitForFreeTarget`
- 控制：`TargetCtrl`、`PullCtrl`
- 运动/角度：`UseKinematicsForTimes`、`DefaultAngle`、`GoToDefaultPosition`、`OnlyForEmptyBlockingList`、`BlockingAngle`、`GetCurrentAngle`
- 时间/容量：`LoadingTime`、`UnloadingTime`、`TimeFactor`、`Capacity`、`MUConveyingDirection`、`IsLoading`、`IsRotating`
- 统计：`StatRotationEmptyPortion`、`StatRotationEmptyTime`、`StatRotationLoadedPortion`、`StatRotationLoadedTime`

## 目录说明

- `general.md`：PickAndPlace Robot 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- 兄弟子文件夹（内容已在本总结中汇总）：
  - `methods/methods.md`：拾放机器人的方法文档。
  - `attributes/attributes.md`：拾放机器人的属性文档。
  - `read-only-attributes/read-only-attributes.md`：拾放机器人的只读属性文档。
