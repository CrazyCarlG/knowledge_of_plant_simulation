# Robot Arms, Joints & Poses（SimTalk）— 目录摘要

本目录汇总了 Plant Simulation 3D 动画/运动控制中关于**机器人手臂（Robot Arms）**、**关节（Joints）**与**姿态（Poses）**的 SimTalk 参考文档。内容来源于目录内的 `robot-arms-joints-poses.md`（本目录无子文件夹，因此无额外子级 `README.md`）。

全部分为三大主题：

1. 访问机器人手臂动画（Robot Arm Animations）
2. 访问关节（Joints）
3. 访问姿态（Poses）

---

## 1. 访问机器人手臂动画（Robot Arm Animations）

SimTalk 提供 3D 机器人手臂动画的方法。可把某一类型的所有动画缓存到一个 `any` 类型变量中：

```simtalk
var a : any := .PickAndPlace._3D.RobotArmAnimations
```

| 成员 | 类型 | 说明 |
| --- | --- | --- |
| `_3D.RobotArmAnimations.getTable(Animations:table)` | 方法 | 将 `<Path>` 对象的机器人手臂动画数据读入指定表。Plant Simulation 会自动格式化该表。 |
| `_3D.RobotArmAnimations.setTable(Animations:table)` | 方法 | 用指定表设置 `<Path>` 对象的机器人手臂动画。 |

**表结构（三列）：**

- `From`（`string`）— 手臂动画从哪个对象开始；单元格为空表示以默认方向为起点。
- `To`（`string`）— 手臂动画移动到哪个对象；单元格为空表示以默认方向为终点。
- `Table`（`table`）— 手臂动画路径子表，含三列 `length`（X、Y、Z），表示机器人在自身坐标系中从 `From` 到 `To` 途经的所有坐标。

**示例：**

```simtalk
var t : table
PickAndPlace1._3D.RobotArmAnimations.getTable(t)
PickAndPlace2._3D.RobotArmAnimations.setTable(t)
```

---

## 2. 访问关节（Joints）

SimTalk 提供访问关节的属性和方法（另见 Joint、Poses）。多数关节属性可通过 `_3D.getObject` 访问可动画对象。

### 关节属性

| 成员 | 类型 | 说明 |
| --- | --- | --- |
| `_3D.JointUseShortestRotationDirection` | 属性 | 设置旋转关节是否朝目标方向走空间最短路径（`true`/`false`）。若启用则不能指定关节限位。 |
| `JointAcceleration` | 属性 | 设置关节加速度。棱柱关节为 `acceleration`（m/s²），旋转关节为 `real`（°/s²）。 |
| `JointCurrentValue` | 只读属性 | 返回当前关节值。棱柱关节返回 `length`（米），旋转关节返回 `real`（度）。 |
| `JointDeceleration` | 属性 | 设置关节减速度。棱柱关节为 `acceleration`（m/s²），旋转关节为 `real`（°/s²）。 |
| `JointLowerLimit` | 属性 | 设置关节下限。平移为 `length`（米），旋转为 `real`（度）。限位仅在定义姿态时使用，不影响 `_3D.Poses.moveToCoordinate`、`_3D.Poses.moveToMU` 等行为。 |
| `JointLowerLimitActive` | 属性 | 设置下限是否激活（`true`/`false`）。 |
| `JointType` | 属性 | 设置关节类型，可取 `"Prismatic joint"` 或 `"Revolute joint"`。 |
| `JointUpperLimit` | 属性 | 设置关节上限。平移为 `length`（米），旋转为 `real`（度）。限位仅在定义姿态时使用。 |
| `JointUpperLimitActive` | 属性 | 设置上限是否激活（`true`/`false`）。 |
| `JointVelocity` | 属性 | 设置关节速度。棱柱关节为 `speed`（m/s），旋转关节为 `real`（°/s，角速度）。速度为 0 的可动画对象在转台旋转时（插入点位于转台动画旋转轴上时）不随转台旋转。 |

### 关节方法

| 成员 | 类型 | 说明 |
| --- | --- | --- |
| `moveTo(...)` | 方法 | 移动到一个或多个位置/旋转角度。支持单值或数组，可选 `TimeSpan`（单个时间）或 `TimeSpans`（时间数组）。返回预计耗时 `time`。 |
| `moveToCoordinate(Coordinate, [TimeSpan])` | 方法 | 把关节移动到指定坐标（关节坐标系）。基于放松状态（原点在 `[0,0,0]`，方向由 `_3D.AniTranslationDirection` 指定）计算目标关节状态。返回 `time`。 |
| `moveToMU(MU, [TimeSpan])` | 方法 | 把关节移动到指定 MU 实例。返回 `time`。 |
| `moveToMUAnimationPosition(MU, TargetPE, [RelPos/AbsPos], [TimeSpan])` | 方法 | 把关节移动到指定 MU 被移动到目标工位（PE）时的位置与旋转。对长度导向目的地会以 MU 前端而非定位点落位。返回 `time`。 |

**关节运动共同要点：**

- `moveTo` 调用会中止同一可动画对象上一次的 `moveTo` 运行；若该对象参与另一活动运动（姿态或 `_3D.Poses.moveToCoordinate`），会产生冲突。
- 修改限位、速度、加速度或关节类型后，下一次影响该对象的姿态运行初始位置归 `0`。
- `moveTo` / `moveToCoordinate` / `moveToMU` / `moveToMUAnimationPosition` 均**不使用关节限位**，可移动到超过限位的位置。
- 未指定 `TimeSpan` 时，运动时长由关节定义的速度决定；指定单个时间表示全程在该时间内完成，指定时间数组则要求时间数等于位置/旋转数（且必须配合数组形式的位置/旋转）。

---

## 3. 访问姿态（Poses）

SimTalk 为可插入 Frame 的对象及 MU 提供姿态相关的属性与方法。

**关键概念：**

- **姿态（pose）**：一般指对象的位置与朝向组合。此处指属于某仿真对象的可动画对象的一组平移或旋转位置，并考虑这些对象关节定义中设置的自由度。
- **姿态运行（pose run）**：由任意形式的 `_3D.Poses.moveTo` 与 `_3D.Poses.moveToCoordinate` 启动的所有运动（含对象本身及其可动画对象）。

### 姿态属性

| 成员 | 类型 | 说明 |
| --- | --- | --- |
| `_3D.MovementInterruptible` | 属性 | 设置失败/暂停是否中断对象的姿态运行（`true`/`false`）。若在失败/暂停已激活时启动姿态运行，则无论该设置如何都会启动。适用于 `FluidSource`、`FluidDrain`、`Tank`、`Mixer`、`Transporter`、`Frame`、`Exporter`、`Worker` 等可运输 MU/Worker 的对象（`Workplace` 除外）。 |
| `_3D.Poses.EndPoseWasReached` | 只读属性（可监视） | 返回对象的所有姿态运行是否已结束。被 `cancelMovement`/`stopMovement` 取消也算结束；仅被 `pauseMovement` 或失败/暂停暂停的运行不会置为 `true`。 |

### 姿态方法

| 成员 | 类型 | 说明 |
| --- | --- | --- |
| `_3D.Poses.cancelMovement([Pose])` | 方法 | 取消朝指定姿态的运动；不指定参数则取消所有运动。会连同同一次 `moveTo` 中的其他姿态一起取消。 |
| `_3D.Poses.continueMovement([Pose])` | 方法 | 继续朝指定姿态的运动；不指定参数则继续所有已暂停运动。 |
| `_3D.Poses.getAnimationTime([Pose])` | 方法 | 返回朝指定姿态运动所需时长（不指定参数返回剩余总仿真时间）。 |
| `_3D.Poses.getMUAnimationPosition(MU, TargetPE, [RelPos/AbsPos])` | 方法 | 返回 MU 在指定 PE 上将占据的位置（X、Y、Z 的 `real[3]`），与 `moveToMUAnimationPosition` 接近的位置相同。 |
| `_3D.Poses.getTable(Poses:table)` | 方法 | 将对象姿态数据写入指定表。 |
| `_3D.Poses.isMovingTo(Pose)` | 方法 | 返回对象是否正在朝指定姿态移动。空或不存在姿态名会报错。 |
| `_3D.Poses.moveTo(...)` | 方法 | 移动到一个或多个姿态。支持单个/数组姿态名，可选 `TimeSpan` 或 `TimeSpans`。返回预计耗时 `time`。移动到名为 `"init"` 的不存在姿态时，会将所有可动画对象置 `0`。 |
| `_3D.Poses.moveToCoordinate(Coordinate, Rotation, [TimeSpan])` | 方法 | 把对象以其第一个动画点移动到指定坐标与旋转（无需预先定义姿态）。依赖机器人配置识别。返回 `time`。 |
| `_3D.Poses.moveToMU(MU, [TimeSpan])` | 方法 | 把对象以其第一个动画点移动到指定 MU 实例（无需预先定义姿态）。返回 `time`。 |
| `_3D.Poses.moveToMUAnimationPosition(MU, TargetPE, [RelPos/AbsPos], [TimeSpan])` | 方法 | 把对象移动到指定 MU 被移动到目标工位时的位置与旋转（无需预先定义姿态）。返回 `time`。 |
| `_3D.Poses.pauseMovement([Pose])` | 方法 | 暂停朝指定姿态的运动；不指定参数则暂停所有运动。 |
| `_3D.Poses.setTable(Poses:table)` | 方法 | 从指定表设置对象姿态。 |
| `_3D.Poses.stopMovement([Pose])` | 方法 | 停止朝指定姿态的运动；若为关节设置了减速度则减速至停止。返回 `time`。 |

**姿态运行共同要点：**

- `cancelMovement` / `continueMovement` / `pauseMovement` / `stopMovement` / `isMovingTo` 作用于指定姿态时，总是连同同一次 `_3D.Poses.moveTo` 调用中的其他姿态一起生效。
- `moveTo` 支持三种时间指定方式：不指定（按关节定义速度）、单个时间（保持各关节与各姿态间的时间比例）、时间数组（数量须等于姿态数，且须配合姿态数组）。修改限位/速度/加速度/关节类型后，下一次姿态运行初始位置归 `0`。
- 所有姿态运行到达终点后，Plant Simulation 会向事件列表写入 `EndOfTime` 事件。

### 机器人配置识别（`moveToCoordinate` / `moveToMU` / `moveToMUAnimationPosition`）

- 这些方法无需预定义姿态，通过检查 `_3D.AnimationObject` 识别机器人配置；检查范围从仿真对象（不含）到 `_3D.AnimationObject`（含）。
- 轴数更多的机器人类型优先于轴数更少的类型；不支持“四轴带球关节夹爪”机器人。
- 无法识别机器人配置属于错误（打开 Method Debugger）；未能到达目标坐标/旋转/MU 不属于错误。
- 这些方法同样**不使用关节限位**。

---

## 交叉引用（See Also）

- **相关主题**：Joint、Poses、Model Joints and Poses、Configuring the Robot、Joint Settings of an Animatable Object、Type of Joint > Revolute Joint。
- **示例/对话框**：Open and Close the Gate with/without Poses、Move the Gate Up to the Height of the Part、Edit 3D Properties > Robot Arm Animation [PickAndPlace]。
- **关联成员**：`_3D.getObject`、`_3D.Rotation`、`_3D.AnimationObject`、`_3D.AniRotationAxis`、`_3D.AniRotationCenter`、`_3D.AniTranslationDirection`、`_3D.getMUAnimationPosition`、`_3D.getMUAnimationRotation`。
- **关节级与姿态级同名方法**：`moveTo`、`moveToCoordinate`、`moveToMU`、`moveToMUAnimationPosition`（关节级作用于单个关节，姿态级作用于整个对象及其可动画对象）。
- **视频**：[Robots (YouTube)](https://youtu.be/wfVN-mcWNsc?si=Un-c8tYPrM135pgG&t=479)、[Poses (YouTube)](https://youtu.be/rQi5oRyZckQ?si=pGkDwvoDw3LOD4Wo&t=1130)。

---

> 资料来源：Siemens Plant Simulation Help（12-894 至 12-947），Unpublished work. © 2026 Siemens。
