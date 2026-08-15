# Turntable（转台）— 通用说明总结

本目录包含 Turntable（转台）对象的通用文档（`general.md`）。本文档为该内容的总结。

## 概述

**Turntable**（转台）是一种旋转平台，用于将零件（MU）传送到若干相连的物料流对象之一，和/或将其掉头转向。

- **容量为 1**：同一时刻转台上只能有一个零件。
- MU 的长度不能超过转台本身的 **Length**（长度）。

## 转台如何将零件移交给后继对象

1. MU 到达前驱对象的出口，并通知转台希望被旋转。
2. 转台判断是否接受该 MU：
   - **无 Pull Control**：转台收到请求后直接接受。
   - **有 Pull Control**：转台执行该控制，选中 MU 后才进行旋转。
3. 转台旋转到对应前驱，MU 移动到转台上。
4. 满足以下任一条件后，转台开始寻找目标工位并朝其旋转：
   - MU 已完全进入转台；
   - MU 已到达转台上的旋转点（支点）；
   - 零件位于转台中心（两端到转台两端的距离相等）；
   - 手动控制时选择 **User-defined with Sensor**，并在 **Sensor Control** 中调用方法 `setDestination`。
5. 转台通过默认出口策略或 **Target Control** 确定目标工位，在方法内用 `setDestination` 设置目标。

> 注意：不要用 **Exit Control** 来确定 MU 的目标——Exit Control 只在 MU 即将离开转台时才被调用，为时已晚。

6. 转台旋转到目标，MU 在最终旋转位置到达后继续移动。之后新 MU 才能上转台（容量为 1）。

> 查询当前旋转角度用只读属性 `CurrentAngle [SimTalk]`。

> 若某角度表中不存在要移入/移出的对象，转台会检查 **Exit Angle Table**（对进入的 MU）或 **Entry Angle Table**（对离开的 MU），否则使用 Frame 中布局的角度。

- 可在 Length-oriented Objects 的 **Appearance** 选项卡选择不同配置。
- 速度为 0 的可动画对象，若插入点位于动画旋转轴上（插入点恰好在动画旋转中心，或沿轴线无横向偏移可到达），则转台旋转时它不随之转动，类似“固定底座 + 旋转台面”的真实转台。

## 添加到仿真模型

点击 Home 功能区选项卡的 **Manage Class Library > Basic Objects > MaterialFlow > Turntable**。

示例模型：**Window 功能区选项卡 > Start Page > Getting Started > Example Models > Small Examples**，在 **Examples Collection** 对话框中选择 Category、Topic 和 Example，点击 **Open Model**。

## 对话框

双击 Turntable 图标打开其对话框：

- **Edit Simulation Properties** — 修改仿真属性（公共属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties** — 在 **Edit 3D Properties** 中编辑 3D 属性（点击仿真属性对话框左下角的 **Edit 3D Properties**，或选中对象后按空格键）。
- 点击 Edit 功能区选项卡的 **Show Manipulators** 或按 `M` 操作图形。

## 选项卡 Attributes（属性）

| 属性 | 说明 | SimTalk |
|------|------|---------|
| Length | 转台长度，只旋转短于或等于该值的零件 | `Length`（另见 `OccupiedLength`） |
| Width | 转台宽度 | `Width` |
| Rotation Point | 旋转支点位置，取值 0 到 Length 之间，0 表示插入起点 | `RotationPoint` |
| Conveyor Speed | 转台输送 MU 的速度 | `Speed`（另见 `Velocity [joint]`） |
| Rotation Time per 90° | 转台旋转 90° 所需时间，输入 0 立即旋转 | `RotationTimePer90Degrees` |
| Rotate When | 转台何时朝目标旋转：完全进入 / 到达支点 / 位于中心 / **User-defined with Sensor**（在 Sensor Control 中调用 `setDestination`） | `RotateWhen` |
| Go to Default Position | MU 离开且无新 MU 时转回默认位置，复位时使用 Default Angle | `GoToDefaultPosition`（另见 `DefaultAngle`） |
| Default Angle | 转到默认位置时的角度，转到起点一侧需加 180° | `DefaultAngle` |
| MU Leaves Backwards Depends On | MU 的用户自定义属性名，触发向后驶出；仅当 Exit Angle Table 中侧边选 **Any** 时评估 | `MURotationAttribute` |
| Entry Angle Table | 入口角度表：前驱编号/名称、连接角度、转向侧边（Start Point / End Point / Any） | `setEntryAngles`、`getEntryAngles`、`calculateAngles` |
| Exit Angle Table | 出口角度表：后继编号/名称、连接角度、转向侧边（Start Point / End Point / Any / MU keeps Direction / MU leaves backward） | `setExitAngles`、`getExitAngles`、`calculateAngles` |
| Automatic Stop | 不输送零件时把当前速度设为 0（空载或阻塞），速度为 0 时 Energy State 变为 Operational | `AutomaticStop` |

> 角度表按钮只有在连接前驱/后继后才激活；计算角度：右键选择 **Calculate Angles**。

## 其他选项卡

- **Times**：按 Tab Times 定义，选分布并输入数值（也支持常量 **Const**）。转台不提供 **Cycle Time**；用 `setTypeAndAttr` 设置分布类型和参数。
- **Failures**：按 Tab Failures 定义。
- **Controls**：修改内置行为；可指定已有 Method 的路径，或创建对象自身的控制 Method（输入名称后选 **Create Control**，或空文本框选 **Create Control** 生成 `self.OnBuilt_in_name`）。含 Entrance Control、Exit Control、Pull Control、Target Control 等。
  - **Target Control**：MU 完全移上转台或到达旋转中心时调用（此时 MU 尚未准备离开）。标准 Target Control 见 `TargetCtrl [SimTalk]`，相关方法 `setDestination`、`getDestination`。
- **Exit**：选择 MU 移交给哪个后继。见 *Blocking [exit strategy]* 和 *Strategy [material flow objects]*。
- **Statistics**：除公共统计外，额外收集：
  - Rotation Empty — 空转（未移动零件）时间占比，`StatRotationEmptyPortion`。
  - Rotation Loaded — 载货旋转时间占比，`StatRotationLoadedPortion`。
  - 查看方式：**View > Show Statistics Report**，或在 Frame 中右键选择 **Show Statistics Report**，或按 `F6`。
- **Energy**：在 Tab Energy 中选择能耗设置。
- **Costs**：在 Tab Costs 中选择成本设置；成本在转台输送 MU 期间产生，来自总投资成本与总运行成本。总投资成本仅在折旧期内产生；转台空载时成本作为一般成本留在转台。
- **User-defined**：按 Tab User-defined 定义自己的属性。

## 菜单

- **Navigate Menu** / **Tools Menu** / **Help Menu** — 见对应章节。
- **View Menu** — 提供 Refresh、Show Statistics Report、Show Attributes and Methods、Contents、Forward/Backward/Exit Blocking List、Associated Lockout Zones、Associated Shift Calendar。
- **Tabs Menu** — 显示/隐藏各选项卡，隐藏未用选项卡可加快打开速度；**Inherit** 切换显示/隐藏选项卡的继承。

## 方法

Turntable 提供：

- 目录中列出的方法；
- Curved Objects 的方法；
- Material Flow Objects 的方法；
- All Objects 的方法。

查看全部方法/只读属性/属性：在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**。

## 另见

- Move Parts On with the Turntable
- YouTube 视频：https://youtu.be/hOvdrDnvXXo?si=Cs5gOF4JB5PBlVma&t=532
