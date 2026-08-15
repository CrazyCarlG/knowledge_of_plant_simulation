# PickAndPlace Robot — 属性（Attributes）

本目录汇总了 **PickAndPlace Robot**（拾放机器人）的**属性**说明。内容来源为 `attributes.md`（`attributes.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 内容来源

- `attributes.md`：拾放机器人属性主文档。
- `attributes.txtx`：同一内容的原始提取文本（含页面编号与若干交叉引用）。

> 说明：本目录下无子文件夹，故无子文件夹 README.md 需要汇总。

## 概述

PickAndPlace Robot 提供：

- 本目录列出（左侧目录中）的属性；
- 所有对象的属性（Attributes of All Objects）；
- 物料流对象的属性（Attributes of the Material Flow Objects）。

要查看对象的全部方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，查看所选**类**的方法、只读属性和属性；
- 在插入实例的 Frame 中按 **F8** 键，或点击 Home 功能区标签页的 **Show Attributes and Methods**，查看所选**实例**的方法、只读属性和属性。

可以通过对话框（复选框、文本框、下拉列表）设置和读取属性值，也可以在 SimTalk 中为属性赋值或取值：

- 设置：`MyPickAndPlace.Capacity := 12`
- 读取：`print MyPickAndPlace.TimeFactor`、`posit := MyStation.Cont.XPos`

## 属性列表

拾放机器人自身定义的属性共 17 个，另含 1 个只读属性（`StatRotationLoadedTime`，详见只读属性目录）。按用途可分为以下几类：

| 类别 | 属性 | 类型 | 语法 |
| --- | --- | --- | --- |
| 角度/位置 | `BlockingAngle` | real | `<Path>.BlockingAngle:real` |
| 角度/位置 | `DefaultAngle` | real | `<Path>.DefaultAngle:real` |
| 角度/位置 | `GoToDefaultPosition` | boolean | `<Path>.GoToDefaultPosition:boolean` |
| 角度/位置 | `OnlyForEmptyBlockingList` | boolean | `<Path>.OnlyForEmptyBlockingList:boolean` |
| 角度/位置 | `MUConveyingDirection` | string | `<Path>.MUConveyingDirection:string` |
| 容量/时间 | `Capacity` | integer | `<Path>.Capacity:integer` |
| 容量/时间 | `LoadingTime` | time | `<Path>.LoadingTime:time` |
| 容量/时间 | `UnloadingTime` | time | `<Path>.UnloadingTime:time` |
| 容量/时间 | `TimeFactor` | real | `<Path>.TimeFactor:real` |
| 容量/时间 | `UseKinematicsForTimes` | boolean | `<Path>.UseKinematicsForTimes:boolean` |
| 控制 | `PullCtrl` | method | `<Path>.PullCtrl:method` |
| 控制 | `TargetCtrl` | method | `<Path>.TargetCtrl:method` |
| 目标 | `TargetObject` | path | `<Path>.TargetObject:path` |
| 目标 | `TargetSelection` | string | `<Path>.TargetSelection:string` |
| 目标 | `TargetSensorID` | integer | `<Path>.TargetSensorID:integer` |
| 目标 | `WaitForFreeTarget` | boolean | `<Path>.WaitForFreeTarget:boolean` |
| 只读（统计） | `StatRotationLoadedTime` | time | `<Path>.StatRotationLoadedTime → time` |

## 属性详解

### StatRotationLoadedTime [SimTalk] — PickAndPlace（只读属性）

返回 `<Path>` 所指拾放机器人在运送工件期间**带载旋转**的总时长。

```simtalk
<Path>.StatRotationLoadedTime → time
```

返回类型：`time`。

```simtalk
print MyPickAndPlace.StatRotationLoadedTime
```

相关：Statistics report、Rotation Time。

---

### BlockingAngle [SimTalk]

设置拾放机器人的**阻塞角（Blocking Angle）**。阻塞角是机器人无法越过的角度（单位：度），用于阻止机器人走最短路径。

- 阻塞角仅影响动画，仿真仍由 **Times Table** 中定义的旋转时间控制。

```simtalk
<Path>.BlockingAngle:real
```

赋值：数据类型 `real`，可指定 0–360 度之间的角度。默认值 `-1` 表示不设阻塞角（机器人走最短路径）。

```simtalk
MyPickAndPlace.BlockingAngle := 5
```

相关：Blocking Angle [文本框]、Times Table [PickAndPlace]。

---

### Capacity [SimTalk] — PickAndPlace

设置拾放机器人的**容量（Capacity）**，即机器人一次可运输的 MU 数量。

- 使机器人能同时运输多个工件（例如一次拾取多个瓶子，再逐一放入瓶箱的槽位——FIFO）。
- 如需按其他规则（如 LIFO）卸载，可在 Exit Control 中编程实现。

```simtalk
<Path>.Capacity:integer
```

可监控（watchable）。赋值：数据类型 `integer`，值大于 1。

```simtalk
MyPickAndPlace.Capacity := 12
```

相关：Capacity [文本框] — PickAndPlace。

---

### DefaultAngle [SimTalk] — PickAndPlace

设置拾放机器人的**默认角度（Default Angle）**。当 `GoToDefaultPosition` 为 `true` 时，机器人末端旋转到该角度（单位：度）；若要旋转到起点所在的一侧，需在此角度上加 180°。

- 复位（Reset）后也用作起始位置，与是否勾选 Go to Default Position 无关。

```simtalk
<Path>.DefaultAngle:real
```

赋值：数据类型 `real`，0°–360° 之间。

```simtalk
MyPickAndPlace.DefaultAngle := 5
```

相关：GoToDefaultPosition [SimTalk]。

---

### GoToDefaultPosition [SimTalk] — PickAndPlace

设置机器人在放置工件后是否旋转回默认位置（`true`）或否（`false`）。

- 设为 `true` 时，复位模型后机器人使用 `DefaultAngle` 指定的角度。

```simtalk
<Path>.GoToDefaultPosition:boolean
```

赋值：数据类型 `boolean`。

```simtalk
MyPickAndPlace.GoToDefaultPosition := true
```

相关：Go to Default Position [复选框]、Default Angle [PickAndPlace]。

---

### LoadingTime [SimTalk] — PickAndPlace

设置拾放机器人在工位**拾取工件所用的装载时间（Loading Time）**。若机器人已满，则旋转到目标工位并放置工件。

- **点方向（point-oriented）交付工位**：拾取时工件登记到机器人，交付工位锁定至装载时间结束。
- **长度方向（length-oriented）交付工位**：装载期间工件留在交付工位上，之后才移动到机器人。

中断行为说明：

- 机器人中断会延长装载时间，交付工位在中断期间保持锁定。
- 交付工位中断不影响机器人装载，装载继续进行。
- 装载时间运行期间机器人入口打开；工件实际移动后入口关闭；卸载时间结束后入口重新打开。

```simtalk
<Path>.LoadingTime:time
```

赋值：数据类型 `time`。

```simtalk
MyPickAndPlaceRobot.LoadingTime := 1:00
MyPickAndPlaceRobot.LoadingTime.setTypeAndAttr("Normal",30,10)
```

相关：Loading Time [PickAndPlace]、LoadingTime.Type [SimTalk]、IsLoading [SimTalk]。

---

### MUConveyingDirection [SimTalk]

设置工件在拾放机器人上的**输送方向（MU Conveying Direction）**。

- `Retain`、`Rotate 90° to the right`、`Rotate 90° to the left`、`Rotate 180°` 为**相对旋转**，取决于工件到达方向。
- `Forwards`、`Lateral right`、`Backwards`、`Lateral left` 为**绝对旋转**，与到达方向无关。

| 输送方向 | 描述 |
| --- | --- |
| Retain | 沿工件到达方向继续输送。 |
| Rotate 90° to the right | 相对右转 90° 后放置到后继。 |
| Rotate 90° to the left | 相对左转 90° 后放置到后继。 |
| Rotate 180° | 相对旋转 180° 后放置到后继。 |
| Forwards | 旋转使工件朝前放置到后继。 |
| Lateral right | 旋转使工件侧向右放置到后继。 |
| Backwards | 旋转使工件朝后放置到后继。 |
| Lateral left | 旋转使工件侧向左放置到后继。 |

```simtalk
<Path>.MUConveyingDirection:string
```

赋值：数据类型 `string`，取值 `"Retain"`、`"Rotate 90° to the right"`、`"Rotate 90° to the left"`、`"Rotate 180°"`、`"Forwards"`、`"Lateral right"`、`"Backwards"`、`"Lateral left"`。

```simtalk
MyPickAndPlace.MUConveyingDirection := "Forwards"
```

相关：MU Conveying Direction [下拉列表]。

---

### OnlyForEmptyBlockingList [SimTalk]

设置机器人是否仅在**阻塞列表为空**（即没有其他已登记的请求）时才旋转回默认位置（`true`）或否（`false`）。

```simtalk
<Path>.OnlyForEmptyBlockingList:boolean
```

赋值：数据类型 `boolean`。

```simtalk
MyPickAndPlace.OnlyForEmptyBlockingList := true
```

相关：Go to Default Position [复选框]。

---

### PullCtrl [SimTalk] — PickAndPlace

指定一个 Method 对象作为**拉取控制（Pull Control）**。

- 每当机器人准备好拾取新工件、或有新 MU 在其入口等待时调用。
- 若 `TargetSelection` 为 `"Load part onto MU at sensor"`，仅当 Container/Transporter 在传感器处等待时机器人才算就绪（编程了 Pull Control 时同样如此）。
- 在 Pull Control 中可用 `fwBlockList` 获取前向阻塞列表，并用 `unblock` 解除阻塞，以决定接受哪个工件。
- 注意：Pull Control 不决定工件去向哪个后继，只从已确定要移向此后继的工件中选择。

```simtalk
<Path>.PullCtrl:method
```

赋值：数据类型 `method`。

```simtalk
MyPickAndPlace.PullCtrl := &myPullControl
```

相关：Pull Control [PickAndPlace]。

---

### TargetCtrl [SimTalk] — PickAndPlace

指定一个 Method 对象作为**目标控制（Target Control）**。

- 机器人完全拾取工件后立即运行，用于确定放置工件的后继，须用 `setDestination` 设置目标。
- 与 Exit Control 不同，此时工件尚未准备好退出对象。
- 机器人放置工件后也会调用此控制，此时活动元素 `@` 为空，需用 `setDestination` 设置下一个拾取对象。
- 仅当**未勾选 Go to Default Position** 时，才在卸载期间调用。

```simtalk
<Path>.TargetCtrl:method
```

赋值：数据类型 `method`。

```simtalk
if ?.empty
   return
end
if @.LastStation = Source
   ?.setDestination(Drain)
elseif @.LastStation = Source1
   ?.setDestination(Station, true)
else
   ?.setDestination(Drain1)
end
```

```simtalk
MyPickAndPlace.TargetCtrl := &myTargetControl
```

相关：setDestination [SimTalk]、Target Control [PickAndPlace]。

---

### TargetObject [SimTalk]

指定机器人放置或装载工件的**长度方向目标对象（Target Object）**。

```simtalk
<Path>.TargetObject:path
```

赋值：数据类型 `path`。

```simtalk
MyPickAndPlace.TargetObject := .Models.MyModel.Conveyor
```

相关：Target Object。

---

### TargetSelection [SimTalk]

设置机器人如何为待移动的工件**选择目标**。

```simtalk
<Path>.TargetSelection:string
```

赋值：数据类型 `string`，可选值：

- `"Exit strategy or target control"` — 以往版本的默认行为；目标由 Exit Strategy 或 Target Control 设置。
- `"Load part onto MU at sensor"` — 需在长度方向目标对象上手动创建**前触发光栅模式**传感器，并输入 Target Object 与 Target Sensor ID。仅当未输入控制时，停止/装载/发送 Container/Transporter 才会自动进行；否则需在控制中编程。仅当 Container/Transporter 在传感器处等待时机器人才拾取工件。
- `"Place part at sensor"` — 需在长度方向目标对象上手动创建**后触发光栅模式**传感器，并输入 Target Object 与 Target Sensor ID。

```simtalk
MyPickAndPlace.TargetSelection := "Load part onto MU at sensor"
```

相关：Target Control [PickAndPlace]、Target Object、Target Sensor ID [文本框]。

---

### TargetSensorID [SimTalk]

设置目标对象的**传感器 ID（Target Sensor ID）**，机器人将在该传感器处放置或装载工件。

- Plant Simulation 不会自动创建传感器，需手动创建或用 `createSensor` 创建。

```simtalk
<Path>.TargetSensorID:integer
```

赋值：数据类型 `integer`。

```simtalk
MyPickAndPlace.TargetSensorID := 2
```

相关：createSensor [SimTalk]、Target Sensor ID [文本框]。

---

### TimeFactor [SimTalk]

设置**时间因子（Time Factor）**，Times Table 中的所有时间都乘以此因子。

- 可在不手动修改表格时间的情况下，以不同速度仿真机器人。

```simtalk
<Path>.TimeFactor:real
```

赋值：数据类型 `real`。

```simtalk
MyPickAndPlace.TimeFactor := 5
```

相关：Time Factor [PickAndPlace]、Times Table [PickAndPlace]。

---

### UnloadingTime [SimTalk] — PickAndPlace

设置拾放机器人将拾取的工件**放置到目标工位的卸载时间（Unloading Time）**。

- **点方向目标工位**：放置时工件登记到机器人，目标工位锁定至卸载时间结束。
- **长度方向目标工位**：工件在卸载时间开始前移动到长度方向对象上。

中断行为说明：

- 机器人中断会延长卸载时间，目标加工工位保持锁定。
- 目标工位中断不影响机器人卸载，卸载继续进行。
- 装载时间运行期间机器人入口打开；工件实际移动后入口关闭；卸载时间结束后入口重新打开。

```simtalk
<Path>.UnloadingTime:time
```

赋值：数据类型 `time`。

```simtalk
MyPickAndPlaceRobot.UnloadingTime := 1:00
MyPickAndPlaceRobot.UnloadingTime.setTypeAndAttr("Normal",30,10)
```

相关：Unloading Time [PickAndPlace]、UnloadingTime.Type [SimTalk]、IsLoading [SimTalk]。

---

### UseKinematicsForTimes [SimTalk]

设置机器人是否使用 **3D 运动学**来确定其时间（`true`），而非使用 Angles Table 和 Times Table 中定义的时间（`false`）。

- 仅当 Plant Simulation 找到受支持的机器人运动学（见 Configuring the Robot）时才能使用。
- 3D 运动学可来自导入的机器人图形，或在 Plant Simulation 中定义。
- 支持除线性机器人外 `_3D.Poses.moveToCoordinate`、`_3D.Poses.moveToMU`、`_3D.Poses.moveToMUAnimationPosition` 使用的所有运动学。
- 在可动画对象的 **Joint** 选项卡上定义 Joint Settings。

```simtalk
<Path>.UseKinematicsForTimes:boolean
```

赋值：数据类型 `boolean`。

```simtalk
MyPickAndPlace.UseKinematicsForTimes := true
```

相关：Use Kinematics for Times、Configuring the Robot、Joint、JointVelocity [SimTalk]、Times Table [PickAndPlace]。

---

### WaitForFreeTarget [SimTalk] — PickAndPlace

设置机器人是否仅在**目标对象准备好接收工件**时才旋转到待退出前驱的工件并拾取（`true`），或否（`false`）。

- 设为 `false` 可使机器人立即旋转到工件。
- 仅对 **Target Selection > Exit strategy or target control** 求值。
- 无法运输的工件会进入目标对象的 Exit Blocking List。
- 设为 `true` 时，机器人旋转拾取前就求值 Exit Strategy 或 Target Control，并把确定的目标写入 `TargetObject`。

```simtalk
<Path>.WaitForFreeTarget:boolean
```

赋值：数据类型 `boolean`。

```simtalk
MyPickAndPlace.WaitForFreeTarget := true
```

相关：ReservedFor [SimTalk]、ReservedPlace [SimTalk]、contentsAndReservedList [SimTalk]、TargetSelection [SimTalk]、Wait for Free Target [PickAndPlace]。

---

## 注意事项

`attributes.txtx` 原始提取文本末尾含有一段与 **Store** 对象（仓库对象）无关的说明：Store 用于存放工件，MUs 直到被移除前一直留在其中，按 X/Y/Z 坐标网格设置存储位，无 Set-up Time 与 Processing Time，其 Entrance Control 决定存储位置。该段不属于 PickAndPlace Robot 的属性，此处不予汇总。

## 目录说明

- `attributes.md`：PickAndPlace Robot 属性说明的 Markdown 版本（本总结的源文件）。
- `attributes.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
