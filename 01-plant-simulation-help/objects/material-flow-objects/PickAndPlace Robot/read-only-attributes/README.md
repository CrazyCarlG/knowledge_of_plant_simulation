# PickAndPlace Robot — 只读属性（Read-Only Attributes）

本目录汇总了 PickAndPlace Robot（拾放机器人）的**只读属性**说明。只读属性只能查询、不能赋值；查询时 Plant Simulation 会返回查询那一刻计算出的值。多数只读属性对应对象某个选项卡（例如 Statistics 选项卡）上不可编辑的对话框条目。

> 说明：目录下无子文件夹，内容来源于 `read-only-attributes.md`（及 `read-only-attributes.txtx` 中的同源内容）。

## 内容来源

- `read-only-attributes.md`：只读属性主文档。
- `read-only-attributes.txtx`：同一内容的原始提取文本（含页面编号与若干交叉引用）。

## 概览

PickAndPlace Robot 提供以下只读属性，按用途可分为三类：

| 类别 | 属性 | 返回类型 |
| --- | --- | --- |
| 当前状态 | `GetCurrentAngle` | object |
| 当前状态 | `GetLastDestination` | object |
| 当前状态 | `IsLoading` | boolean |
| 当前状态 | `IsRotating` | boolean |
| 旋转统计（空载） | `StatRotationEmptyPortion` | real |
| 旋转统计（空载） | `StatRotationEmptyTime` | time |
| 旋转统计（带载） | `StatRotationLoadedPortion` | real |
| 旋转统计（带载） | `StatRotationLoadedTime` | time |

## 查看方式

- 在 Class Library 的上下文菜单选择 **Show Attributes and Methods**，查看所选类的全部方法、只读属性与属性。
- 在 Frame 中选中插入的实例后，按 **F8** 或点击 Home 选项卡上的 **Show Attributes and Methods**，查看实例的全部方法、只读属性与属性。

查询示例：

```simtalk
print PickAndPlaceRobot.GetCurrentAngle
```

## Times Table 说明

- 插入 Connector 或将对象拖放到 PickAndPlace Robot 上时，Plant Simulation 会把对应数值写入 Times Table；计算时假设四分之一圈旋转耗时 1 秒，该时间可修改。
- 删除 Connector 时，已断开对象的条目**不会**自动从 Times Table 中删除，需在 Angles Table 中手动删除（例如右键对应行选择 **Delete Row**），或在 PickAndPlace Robot 对话框中点击 **Apply** 后由系统一并删除。

```simtalk
MyPickAndPlace.setTimesTable(myTimesTable)
```

## 属性详解

### GetCurrentAngle [SimTalk]

返回 `<Path>` 所指 PickAndPlace Robot 当前所处的角度。

```simtalk
<Path>.GetCurrentAngle → object
```

返回类型：`object`。

```simtalk
print PickAndPlace.GetCurrentAngle
```

### GetLastDestination [SimTalk]

返回 PickAndPlace Robot 最近一次放置或拾取零件的目标对象。

```simtalk
<Path>.GetLastDestination → object
```

返回类型：`object`。

```simtalk
print MyRobot.GetLastDestination
// might return .Models.MyRobot.Source
```

相关：`setDestination [SimTalk] - PickAndPlace`、`getDestination [SimTalk] - PickAndPlace`。

### IsLoading [SimTalk]

返回 PickAndPlace Robot 当前是否处于 loading（装载）状态：`true` / `false`。

```simtalk
<Path>.IsLoading → boolean
```

返回类型：`boolean`，可被监控（watchable）。

**备注**：`IsLoading` 用于观察 Loading Time 的开始与结束；在设置了 Loading Time 的情况下，它是确保 Container/Transporter 正确卸载所必需的。

```simtalk
print PickAndPlace.IsLoading
```

```simtalk
param SensorID: integer, Front: boolean, BookPos: boolean
var MU : object
@.Stopped  := true // stop
var Destination:object := Robot
MU := @.Cont
MU.Destination := Drain
if not MU.move(Destination)
   stopuntil MU.Location /= @ and not Destination.IsLoading
end
@.Stopped := false
```

相关：`LoadingTime [SimTalk] - PickAndPlace`、Loading Time [PickAndPlace]。

### IsRotating [SimTalk]

返回 PickAndPlace Robot 当前是否正在旋转：`true` / `false`。

```simtalk
<Path>.IsRotating → boolean
```

返回类型：`boolean`。

```simtalk
print PickAndPlace.IsRotating
```

### StatRotationEmptyPortion [SimTalk] - PickAndPlace

返回统计收集期内 PickAndPlace Robot 处于**空载旋转**（未运送零件）状态所占的比例。

```simtalk
<Path>.StatRotationEmptyPortion → real
```

返回类型：`real`。

```simtalk
print MyPickAndPlace.StatRotationEmptyPortion
```

相关：Tab Statistics [PickAndPlace]、Statistics report、Rotation Time、Empty [state, material flow objects]。

### StatRotationEmptyTime [SimTalk] - PickAndPlace

返回统计收集期内 PickAndPlace Robot 处于**空载旋转**状态的总时长。

```simtalk
<Path>.StatRotationEmptyTime → time
```

返回类型：`time`。

```simtalk
print MyPickAndPlace.StatRotationEmptyTime
```

相关：Statistics report、Rotation Time、Empty [state, material flow objects]。

### StatRotationLoadedPortion [SimTalk] - PickAndPlace

返回统计收集期内 PickAndPlace Robot 处于**带载旋转**（正在运送零件）状态所占的比例。

```simtalk
<Path>.StatRotationLoadedPortion → real
```

返回类型：`real`。

```simtalk
print MyPickAndPlace.StatRotationLoadedPortion
```

相关：Tab Statistics [PickAndPlace]、Statistics report、Rotation Time。

### StatRotationLoadedTime [SimTalk] - PickAndPlace

返回统计收集期内 PickAndPlace Robot 处于**带载旋转**状态的总时长。

```simtalk
<Path>.StatRotationLoadedTime → time
```

返回类型：`time`。

```simtalk
print MyPickAndPlace.StatRotationLoadedTime
```

相关：Statistics report、Rotation Time。
