# LockoutZone（锁定区域）— 属性汇总

> 本 README 汇总了 `attributes` 目录下的 `attributes.md`，以及相邻子目录（`general`、`methods`、`read-only-attributes`）中 README.md 的内容，便于快速了解 **LockoutZone** 资源对象的属性、只读属性和方法。

## 概述

**LockoutZone（锁定区域）** 用于将一组物料流对象组合在一起。当其中某个工位（station）发生故障时，锁定区域内的所有其他工位也会停止加工其零件。LockoutZone 负责控制所有工位的故障，并返回所分配工位的总体可用性。

主要行为：

- 一个仿真模型中可插入多个 LockoutZone，且它们可以重叠——即一个工位可被分配给多个 LockoutZone。
- 必须至少为其中一个被分配的工位定义故障配置文件（failure profile）。一旦某个工位发生故障，LockoutZone 会停止所有被分配工位的加工操作，即将它们的属性 `Stopped` 设为 `true`。
- 只有当所有故障都被排除后，工位才会重新开始加工零件，并且只消耗剩余的加工时间。
- 可将任何内置的物料流对象（Material Flow Objects）或流体对象（Fluid Objects）分配给 LockoutZone；对于用户在 Frame 中自行建模的工位，LockoutZone 会将该 Frame 的属性 `Stopped` 设为 `true`，用户需自行建模对该属性的反应；此外还可添加 Worker 或 WorkerPool。
- LockoutZone 不影响其控制工位的恢复时间（Recovery Time）和循环时间（Cycle Time）。

## 属性（Attributes）

LockoutZone 提供以下属性。可通过复选框、文本框和下拉列表，或通过给相应属性赋值来设置属性的值；也可读取属性的值。

设置属性值示例：

```simtalk
MyLockoutZone.StopMode := "stop when service arrives"
```

读取属性值示例：

```simtalk
print MyLockoutZone.StopMode
```

### Active [SimTalk] — LockoutZone

激活（`true`）或停用（`false`）由 `<Path>` 指定的对象。

- **类型：** 属性
- **语法：** `<Path>.Active:boolean`
- **可赋值：** 数据类型 `boolean`
- **说明：** 激活后，会为被分配的对象创建并转发故障（failures）。

```simtalk
MyLockoutZone.Active := true
```

### Objects [SimTalk] — LockoutZone

设置要分配给由 `<Path>` 指定的 LockoutZone 的资源对象。

- **类型：** 属性
- **语法：** `<Path>.Objects:array`
- **可赋值：** 数据类型 `array`（包含资源对象）
- **说明：** LockoutZone 也会返回这些资源。

```simtalk
var a : object[] := [MyStation1, MyStation2]
LockoutZone.Objects := a
```

```simtalk
print MyLockoutZone.Objects
// 可能返回
[*.Models.MyEnginePlant.Station1, *.Models.MyEnginePlant.Frame,
*.Models.MyEnginePlant.Station2, *.Models.MyEnginePlant.Station3,
*.Models.MyEnginePlant.ParallelStation]
```

### ResumeCtrl [SimTalk]

指定由 `<Path>` 指定的对象的 Method 对象。

- **类型：** 属性
- **语法：** `<Path>.ResumeCtrl:method`
- **可赋值：** 数据类型 `method`
- **说明：** 当分配给 LockoutZone 的所有对象的故障都被排除、对象可以继续加工零件时，Plant Simulation 会调用该 Method。

```simtalk
MyLockoutZone.ResumeCtrl := &myResumeCtrl
```

### StopCtrl [SimTalk]

指定由 `<Path>` 指定的对象的 Method 对象。

- **类型：** 属性
- **语法：** `<Path>.StopCtrl:method`
- **可赋值：** 数据类型 `method`
- **说明：** 当分配给 LockoutZone 的某个对象发生故障时，Plant Simulation 会调用该 Method。匿名标识符 `@` 表示触发故障的工位，`?` 表示 LockoutZone。

```simtalk
MyLockoutZone.StopCtrl := &myStopCtrl
```

### StopMode [SimTalk]

设置由 `<Path>` 指定的 LockoutZone 的停止模式。

- **类型：** 属性
- **语法：** `<Path>.StopMode`
- **可监视（Watchable）：** 是
- **可赋值：** 数据类型 `string`
- **可选值：**
  - **"Stop immediately"（立即停止）** — 一旦某个被分配工位故障，立即停止 LockoutZone 内所有其他对象的加工操作（这些对象本身不发生故障）。期间可能发生多次故障并相互重叠；所有故障排除后才恢复加工，且只消耗剩余加工时间。
  - **"Stop when Service arrives"（服务到达时停止）** — 仅在故障工位请求的维修服务被指派后才停止。对通过 Footpath 步行的 Worker，视为其到达工位后；对可传送的 Exporter/Worker，视为 Broker 指派服务后（与 Receive Control 行为一致）。

```simtalk
MyLockoutZone.StopMode := "Stop when Service arrives"
```

### Stopped [SimTalk] — LockoutZone

设置由 `<Path>` 指定的 LockoutZone 是否停止（`true`）或未停止（`false`）。

- **语法：** `<Path>.Stopped`
- **可监视（Watchable）：** 是
- **可赋值：** 数据类型 `boolean`
- **说明：** Stopped 表示 LockoutZone 所控制的所有对象的加工操作全部停止。

```simtalk
MyLockoutZone.Stopped := true
```

## 只读属性（Read-Only Attributes）

LockoutZone 的只读属性值只能查询、不能设置；Plant Simulation 在查询的那一刻计算各值。所有 `Stat*` 属性均显示在 **Statistics** 选项卡上，并从由 `<Path>` 引用的 LockoutZone 读取。

| 属性 | 返回类型 | 说明 | 可监视 |
| --- | --- | --- | --- |
| `StatStoppedCount` | integer | LockoutZone 停止所分配工位的次数 | 是 |
| `StatStoppedDelta` | time | LockoutZone 停止工位加工操作时间的标准差 | 是 |
| `StatStoppedIntervalDelta` | time | LockoutZone 停止工位区间时间的标准差 | 是 |
| `StatStoppedIntervalMu` | time | LockoutZone 停止工位区间时间的平均值 | 是 |
| `StatStoppedIntervalTime` | time | LockoutZone 停止工位区间时间的总时间 | 否 |
| `StatStoppedMu` | time | LockoutZone 停止工位加工操作时间的平均值 | 是 |
| `StatStoppedPortion` | real | 统计周期内工位被停止的时间占比 | 是 |
| `StatStoppedTime` | time | LockoutZone 停止工位加工操作的总时间 | 是 |

语法：

```simtalk
<Path>.StatStoppedCount         → integer
<Path>.StatStoppedDelta         → time
<Path>.StatStoppedIntervalDelta → time
<Path>.StatStoppedIntervalMu    → time
<Path>.StatStoppedIntervalTime  → time
<Path>.StatStoppedMu            → time
<Path>.StatStoppedPortion       → real
<Path>.StatStoppedTime          → time
```

示例：

```simtalk
print MyLockoutZone.StatStoppedCount
print MyLockoutZone.StatStoppedTime
```

## 方法（Methods）

LockoutZone 提供方法 `addObject [SimTalk] — LockoutZone`，以及所有对象的通用方法（*Methods of All Objects*）。

### `addObject` [SimTalk] — LockoutZone

向由 `<Path>` 指定的 LockoutZone 添加单个对象。

- **类型：** 方法
- **语法：**

  ```simtalk
  <Path>.addObject(NameOfObject:path) → boolean
  ```

- **参数：** `NameOfObject`（数据类型 `path`）— 要添加的对象的名称。
- **返回值：** 数据类型 `boolean`。

```simtalk
MyLockoutZone.addObject(MyParallelStation)
```

## 查看所有属性、只读属性和方法

打开 **Show Attributes and Methods** 窗口可查看对象的所有方法、只读属性和属性：

- 在 **Class Library** 中，从对象的上下文菜单中选择 **Show Attributes and Methods**。
- 对于实例，按 `F8` 键，或点击 Frame 中「主页」选项卡上的 **Show Attributes and Methods**。
