# Marker — General（概述）

本文件是对 `general.md` 内容的总结，介绍 Plant Simulation 中 **Marker**（标记点）对象的基本用途、属性与配置方式。

> 目录中仅存在 `general.md` 一个 Markdown 源文件（另有 `general.txtx` 为同一内容的原始导出文本），且 `general` 目录下没有子文件夹及 README.md，因此本总结完全基于 `general.md`。

## 概述

**Marker** 对象用于在仿真模型中设置路径点（waypoints）。自动导引车（AGV, Automated Guided Vehicle）从 **AGVPool** 出发，沿这些 Marker 行驶到目的地。

## 说明（Description）

- **Default Curve Radius / `DefaultCurveRadius`**：设置 Marker 处圆角（rounding）的大小。设为 `0` 时，AGV 在 Marker 处原地旋转（rotate on the spot），而不是沿弧线行驶。
- **对齐要求**：插入 Marker 时应确保它们对齐，避免 Plant Simulation 在 Marker 之间计算不必要的圆角。若在 *Show Grid* 关闭时插入 Marker，可能导致 Marker 未对齐。
- **初始行驶**：若静止的 Transporter 无法以指定的 Default Curve Radius 到达第一个 Marker，则会尽可能原地旋转，然后直线驶向 Marker。
- **方向类型**：Marker 可以是**方向性（directional）**或**全向性（omnidirectional）**，通过 **Use Rotation of Marker** 复选框切换。
- **显示/隐藏**：点击 **Show Connections** 可显示或隐藏 Marker。

### 添加到仿真模型

在 Home 功能区的 **Manage Class Library > Basic Objects > Resources > Marker** 中添加 Marker 对象。

## 方向性与全向性 Marker

- **全向（omnidirectional）Marker**：AGV **不会**穿过该 Marker，而是在该 Marker 前方转向下一个 Marker。
- **方向性（directional）Marker**：AGV 可沿两个方向穿过。Plant Simulation 根据 Marker 序列中**前一个 Marker 的位置**来选择行驶方向。

以 90° 角的 Marker 为例，Plant Simulation 的路由计算规则：

- 若前一个 Marker 位于该 90° Marker 的**上方**，AGV 从上到下穿过。
- 若前一个 Marker 位于**下方**，AGV 从下到上穿过。
- 若前一个 Marker 恰好与该 Marker **同高**，则根据 AGV 当前朝向判断：
  - 车头朝上 → 从上到下穿过；
  - 车头朝下 → 从下到上穿过；
  - 车头正对 Marker 中心 → 从上到下穿过。

对于其他角度，规则类推。

- **默认角度 0°** 的方向性 Marker：AGV 穿过 Marker，然后在 Marker 上按设定的角度转向下一个 Marker 的方向。
- **非默认角度** 的方向性 Marker：AGV 按输入的角度驶向 Marker，穿过它，并以指定角度离开。

## Marker 对话框（Dialog Box）

双击 Marker 图标打开对话框。

- **Edit Simulation Properties**：修改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit 3D Properties**：编辑 3D 属性，方式：
  - 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮；
  - 或在模型中选中对象后按空格键。
- 操纵图形：点击 Edit 功能区的 **Show Manipulators** 或按 `M` 键。

## Tab Attributes（属性选项卡）

- **Use Rotation of Marker [复选框]**：选中后 AGV 会使用 Marker 的旋转方向——穿过 Marker 并在其上按定义的角度转向下一个 Marker。旋转角度可在 Marker 的 *Edit 3D Properties* 对话框的 **Transformation** 选项卡下 *Settings for the Rotation* 中设置。清除复选框则 AGV 不穿过 Marker，而是在 Marker 前转向下一个 Marker（即全向）。**SimTalk：** `UseRotationOfMarker`
- **Arrival Control [Marker]**：修改对象内置行为。当在区域内自由行驶的 Transporter 到达 Marker 时，对象调用 Arrival Control，可在此编程处理 AGV 到达或最接近 Marker 时的动作（例如向车队管理软件反馈 AGV 位置）。对于全向 Marker，当 Transporter 到达曲率/圆角的中点时执行该控制。若未输入 Method，控制值为 `VOID`。**SimTalk：** `ArrivalCtrl`

## Tab User-defined

按 *Tab User-defined* 的描述自定义属性。

## 菜单（Menus）

- **Navigate Menu**：见 *Navigate Menu*。
- **View Menu**：`Refresh`、`Show Attributes and Methods`。**SimTalk：** `updateDialog`
- **Tools Menu**：`Edit Controls`、`Edit Observers`。
- **Help Menu**：见 *Help Menu*。

## Marker 的方法（Methods）

Marker 提供 **Methods of All Objects**（所有对象的通用方法）。可通过 *Show Attributes and Methods* 窗口查看所有方法、只读属性和属性：

- 在 Class Library 上下文菜单选择 **Show Attributes and Methods** 查看所选类；
- 按 `F8` 或在 Frame 的 Home 功能选项卡点击 **Show Attributes and Methods** 查看所选实例。

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## Amount [SimTalk] — AGVPool

设置由 `<Path>` 指定的 AGVPool 所创建的 AGV 数量，在仿真运行的 init 阶段创建。

- **类型：** Attribute
- **语法：**

```
<Path>.Amount:integer
```

- **赋值：** 可赋 `integer` 类型值。
- **示例：**

```simtalk
MyAGVPool.Amount := 2
```

## 相关链接（See also）

- Amount [text box] - AGVPool
- AGV [SimTalk]
- Directional and Omnidirectional Markers
- Dialog Box of the Marker
- Model an Automated Guided Vehicle System (AGVS)
- Select Object [for controls]
- Model an Automated Guided Vehicle System (AGVS) > Cover a Route Along Omnidirectional Markers
- Model an Automated Guided Vehicle System (AGVS) > Cover a Route Along Directional Markers
