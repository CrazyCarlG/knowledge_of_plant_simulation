# EventController — 属性

> 本文件是对同目录下 `attributes.md`（以及 `attributes.txtx`）的总结，介绍对象 **EventController**（事件控制器）提供的**属性**。
> `attributes/` 目录下没有子文件夹；同级目录中的 README 为 `../general/README.md`、`../methods/README.md` 与 `../read-only-attributes/README.md`，其内容摘要见文末“相关概述”。

## 属性来源

EventController 提供：

- 目录中所列的属性（即本文件归纳的 17 个属性）。
- **所有对象的属性（Attributes of All Objects）**。

你可以设置属性的值，也可以获取属性的值，既可通过对话框中的复选框、文本框和下拉列表，也可通过给相应属性赋值。

查看对象的全部方法、只读属性和属性：

- 在 Class Library 中选中类，右键选择 **Show Attributes and Methods**。
- 在插入实例的 Frame 中按 **F8**，或点击 Home 选项卡上的 **Show Attributes and Methods**。

设置示例：

```simtalk
EventController.AbsTimeFormat := true
```

获取示例：

```simtalk
print EventController.AbsTimeFormat
posit := MyStation.Cont.XPos
```

---

## AbsTimeFormat [SimTalk]

显示 `<Path>` 所指定的 EventController 的时间为绝对时间（`true`）或相对时间（`false`）。

- **类型：** 属性
- **语法：** `<Path>.AbsTimeFormat:boolean`
- **赋值：** 可赋 `boolean` 类型值。
- **示例：** `EventController.AbsTimeFormat := false`
- **参见：** Time [EventController]

---

## BreakpointsActive [SimTalk]

激活（`true`）或停用（`false`）`<Path>` 所指定的 EventController 的 Event Debugger 断点。

- **类型：** 属性
- **语法：** `<Path>.BreakpointsActive:boolean`
- **赋值：** 可赋 `boolean` 类型值。
- **示例：** `EventController.BreakpointsActive := true`
- **参见：** Breakpoints Active

---

## EndTime [SimTalk] — EventController

设置 `<Path>` 所指定的 EventController 控制的仿真运行结束的时间。

**备注：** 给该属性赋值后，Plant Simulation 不会立即更新对话框中的显示，需点击 **OK** 或 **Apply** 才会更新。

- **类型：** 属性
- **语法：** `<Path>.EndTime:time`
- **赋值：** 可赋 `time` 类型值。
- **示例：**

```simtalk
if root.EventController.EndTime - root.EventController.SimTime < 600
   print "Less than 10 minutes until the end of the simulation."
end
```

- **参见：** End Time [EventController]

---

## ExperimentManager [SimTalk]

由 ExperimentManager 在控制 `<Path>` 所指定的 EventController 的实验时设置。

**备注：** 若 EventController 控制仿真，则该属性为 void。

- **类型：** 属性
- **语法：** `<Path>.ExperimentManager:path`
- **赋值：** 可赋 `path` 类型值。
- **示例：** `print EventController.ExperimentManager`
- **参见：** List of Events、ExperimentManager [object]

---

## IncrementRandomNumbersVariantOnReset [SimTalk]

使 `<Path>` 所指定的 EventController 在重置模型后生成不同的随机数（`true`）或不（`false`）。

- **类型：** 属性
- **语法：** `<Path>.IncrementRandomNumbersVariantOnReset:boolean`
- **赋值：** 可赋 `boolean` 类型值。
- **示例：** `EventController.IncrementRandomNumbersVariantOnReset := false`
- **参见：** Increment Variant on Reset、Simulating Random Processes

---

## InitCtrl [SimTalk] — EventController

指定 `<Path>` 所指定对象的一个 Method 对象作为 **Init Control**。该对象在仿真运行开始时的初始化阶段、对象初始化之前、init 方法执行之前调用一次。

**备注：** 当你点击 **Start/Stop Simulation** 初始化由该 EventController 控制的仿真模型，或调用 `start` 方法时，Plant Simulation 会运行该 init control。

- **类型：** 属性
- **语法：** `<Path>.InitCtrl:method`
- **赋值：** 可赋 `method` 类型值。
- **示例：**

```simtalk
EventController.InitCtrl := &myInitControl
// The source code of an init control might look like this:
MyWorkersTable[2,1] := 2 // enters the desired amount of the worker John
MyWorkersTable[2,2] := 1 // enters the desired amount of the worker Nellie
WorkerPool.setCreationTable(MyWorkersTable)
```

- **SimTalk：** `init` [SimTalk]（预定义名称）、`start` [SimTalk] — EventController
- **参见：** Start/Stop Simulation [EventController]、Init Control [EventController]、Set How Many Workers Are Created During Initialization

---

## RandomNumbersVariant [SimTalk]

设置 `<Path>` 所指定的 EventController 使用的随机数变体。

**备注：** 不同的变体会生成不同的随机数。

- **类型：** 属性
- **语法：** `<Path>.RandomNumbersVariant:integer`
- **赋值：** 可赋 `integer` 类型值。
- **示例：** `EventController.RandomNumbersVariant := 2`
- **SimTalk：** `RandomSeed` [SimTalk] — material flow objects
- **参见：** Random Numbers Variant、Simulating Random Processes

---

## Realtime [SimTalk]

设置 `<Path>` 所指定的 EventController 的 `start` 方法启动实时仿真（`true`）还是全速仿真（`false`）。

**备注：** 仅当调用 `start` 方法且未指定第二个参数 `Realtime` 时，该属性才适用。

- **类型：** 属性
- **语法：** `<Path>.Realtime:boolean`
- **赋值：** 可赋 `boolean` 类型值。
- **示例：**

```simtalk
EventController.Realtime := false
EventController.start
```

- **SimTalk：** `start` [SimTalk] — EventController
- **参见：** Real-time x [EventController]、Start Full Speed Simulation [Home ribbon]

---

## RealtimeScale [SimTalk]

设置 `<Path>` 所指定的 EventController 在实时仿真中两个事件之间经过的时间因子。

**备注：** 该值确保仿真推进时 EventController 以此因子显示时间跨度。实时仿真中事件的持续时间等于仿真时间除以你输入的缩放因子，结果为整数。

- **类型：** 属性
- **语法：** `<Path>.RealtimeScale:real`
- **赋值：** 可赋 `real` 类型值。
- **示例：** `EventController.RealtimeScale := 10`
- **参见：** Real-time x [EventController]

---

## ResetCtrl [SimTalk]

指定 `<Path>` 所指定对象的一个 Method 对象作为 **reset control**。每当点击 `<Path>` 所指定的 EventController 中的 **Reset Simulation** 或调用 `reset` 方法时，Plant Simulation 会调用该 reset control。

**备注：** Plant Simulation 会先执行该 reset control，再调用你插入到 Frame 及其任意子 Frame 中的任何 `reset` 方法。

- **类型：** 属性
- **语法：** `<Path>.ResetCtrl:method`
- **赋值：** 可赋 `method` 类型值。
- **示例：** `EventController.ResetCtrl := &myResetMethod`
- **SimTalk：** `reset` [SimTalk] — EventController
- **参见：** Reset Simulation [EventController]、Reset Simulation [EventDebugger]

---

## SkipLongEventIntervals [SimTalk]

使 `<Path>` 所指定的 EventController 在实时仿真期间跳过没有相关事件发生的长时间段（`true`）或不（`false`）。

**备注：** 类型为 `Animation` 和 `UpdateDisplay` 的事件被认为不相关。

- **类型：** 属性
- **语法：** `<Path>.SkipLongEventIntervals:boolean`
- **赋值：** 可赋 `boolean` 类型值。
- **示例：** `EventController.SkipLongEventIntervals := true`
- **参见：** Skip Long Event Intervals

---

## StartDate [SimTalk] — EventController

设置仿真期间 `<Path>` 所指定的 EventController 的绝对时间所基于的日期和时间。

- **类型：** 属性
- **语法：** `<Path>.StartDate:dateTime`
- **赋值：** 可赋 `dateTime` 类型值。
- **示例：** `EventController.StartDate := str_to_dateTime("2025/01/02 14:00:00")`
- **参见：** Start Date [EventController]

---

## StartStat [SimTalk]

设置 `<Path>` 所指定的 EventController 重置统计收集并重新开始统计收集的时间点。

- **类型：** 属性
- **语法：** `<Path>.StartStat:time`
- **赋值：** 可赋 `time` 类型值。
- **示例：** `root.EventController.StartStat := str_to_time("40:00.00") // 40 minutes after simulation start`
- **参见：** Statistics [EventController]

---

## StartStopCtrl [SimTalk]

指定 `<Path>` 所指定对象的一个 Method 对象。

**备注：** 每当点击 `<Path>` 所指定的 EventController 中的 **Start/Stop Simulation** 或调用 `start` 方法时，Plant Simulation 会调用该 Method。点击 EventController 中的 **Single Step Simulation**、处理下一个事件、再次执行 start stop control 时也会运行该 Method；仿真结束时同样会调用。你可以在 control 代码中使用表达式 `?.IsRunning` 判断 EventController 是已启动（`false`）还是已停止（`true`）。

- **类型：** 属性
- **语法：** `<Path>.StartStopCtrl:method`
- **赋值：** 可赋 `method` 类型值。
- **示例：** `EventController.StartStopCtrl := &myStartStopControl`
- **SimTalk：** `IsRunning` [SimTalk]、`start` [SimTalk] — EventController
- **参见：** Start/Stop Simulation [EventDebugger]、Single Step Simulation [EventDebugger]

---

## SummaryReport [SimTalk]

使 `<Path>` 所指定的 EventController 在仿真运行结束时显示 Drain 删除零件的汇总报告（`true`）或不（`false`）。

- **类型：** 属性
- **语法：** `<Path>.SummaryReport:boolean`
- **赋值：** 可赋 `boolean` 类型值。
- **示例：** `EventController.SummaryReport := true`
- **参见：** Show Summary Report [EventController]

---

## TraceActive [SimTalk]

设置 `<Path>` 所指定的 EventController 记录事件（`true`）或不记录（`false`）。

- **类型：** 属性
- **语法：** `<Path>.TraceActive:boolean`
- **赋值：** 可赋 `boolean` 类型值。
- **示例：** `EventController.TraceActive := true`
- **参见：** Trace File [check box]

---

## TraceFile [SimTalk]

设置 `<Path>` 所指定的 EventController 的 Event Debugger 写入事件日志的 trace 文件名。

- **类型：** 属性
- **语法：** `<Path>.TraceFile:string`
- **赋值：** 可赋 `string` 类型值。
- **示例：** `EventController.TraceFile := "C:\temp\run1"`
- **参见：** Trace File [text box]

---

## 相关概述（同级目录 README 摘要）

### ../general/README.md 摘要

`../general/README.md` 是对 `general.md` 的总结，介绍 EventController 的总体用途与对话框：

- **用途：** EventController 用于协调、同步和控制仿真运行期间发生的事件。Plant Simulation 是**离散事件仿真系统**，只在特定时间点显示状态变化。EventController 名称不可更改；手动删除会先重置模型。
- **工作原理：** MU 进入加工站时计算加工时间，把事件写入**已调度事件列表**（相当于时间轴上的标记）；EventController 沿时间轴推进，到点时通知对象处理事件（如 `Out`）并传递 MU。
- **启动/停止仿真：** 通过 EventController 对话框、Frame Home 选项卡或迷你工具栏的 **Start/Stop Simulation** 启动；停止则用 **Single Step Simulation** 或再次点击 Start/Stop。仿真在当前事件完全处理完后停止；运行结束时执行所有 `endSim` 方法（事件列表为空或到达 **End time** 时触发）。
- **Time 显示：** 可在 **Relative time**（默认，从 0 开始）与 **Current time plus simulation time** 间切换。相关 SimTalk：`AbsSimTime`、`SimTime`。
- **Controls 选项卡：** `Reset Simulation`（`reset`、`deleteSuspendedMethods`、`initStat`、`IsInitialized`、`ResetCtrl`）、`Start/Stop Simulation`（`start`、`stop`、`StartStopCtrl`、`init`、`InitCtrl`）、`Start Full Speed Simulation`、`Start Fast Forward Simulation`、`Single Step Simulation`。
- **已调度事件列表：** 点击 **List** 打开 Event Debugger；列包括 **Breakpoint**、**Type**、**Time**、**Receiver**、**Sender**、**Insertion Time**、**Parameters**（SimTalk：`getEventList`）。事件类型约 50 种，如 `Animation`、`Battery`、`CreateMU`、`DisruptionBegin/End`、`Init/InitStat`、`MethCall/MethWakeup`、`Out/OutEnd`、`Pause/PauseEnd`、`SensorStart/End/BookPos`、`SetupEnd`、`Shift/ShiftCalendarStart`、`StartActions`、`StartTransporter`、`TankEmpty/TankFull`、`TriggerAction`、`UpdateDisplay` 等。
- **速度滑块与实时缩放：** `Slower/Faster Slider` 调整速度；`Real-time x` 设置实时缩放因子（实时持续时间 = 仿真时间 / 缩放因子）。相关 SimTalk：`Realtime`、`RealtimeScale`。
- **Settings 选项卡：** `Start Date`（`StartDate`）、`End Time`（`EndTime`）、`Statistics`（`StartStat`，用于丢弃预热阶段数据）、`Skip Long Event Intervals`、`Show Summary Report`（`SummaryReport`）。
- **Event Debugger：** 断点（`BreakpointsActive`、`Breakpoints`）、`Run to Time`、Trace File（`TraceActive`、`TraceFile`）及仿真控制按钮；Condition 代码用 `@` 访问接收方、`?` 访问发送方。
- **随机数：** `Random Numbers Variant`（`RandomNumbersVariant`、`RandomSeed`）、`Increment Variant on Reset`（`IncrementRandomNumbersVariantOnReset`）、`Antithetic Random Numbers`（`setAntitheticRandomNumbers`）。

### ../methods/README.md 摘要

`../methods/README.md` 是对 `methods.md` 的总结，介绍 EventController 提供的 4 个方法：

- **getEventList** — 返回 `<Path>` 所指定的 EventController 的已调度事件列表。语法 `<Path>.getEventList(MaximumNumberOfEvents:integer) → table`；传 `-1` 写入全部事件；列包括 Type、Time、Receiver、Sender、Insertion Time、Parameters。
- **reset** — 运行仿真模型中所有名为 `reset` 的方法；完成后删除未处理事件、仿真时间归零、重置统计、清除故障、对象置为 `planned` 状态等。重置命令**不会立即执行**，而是等到当前所有方法（含触发重置的方法）执行完后才执行。语法 `<Path>.reset`。
- **start** — 激活 EventController 并启动仿真运行；若在仿真期间对另一 Frame 的 EventController 调用，会停止当前 EventController 并在该 Frame 启动。语法 `<Path>.start([WithAnimation:boolean:=animation, RealTime:boolean:=EventController.Realtime])`。
- **stop** — 停止 EventController 以终止仿真；仿真不会停止，直到当前方法执行（含调用栈）完成或被挂起。语法 `<Path>.stop([EndSim:boolean:=false])`。

方法来源同样包括**所有对象的通用方法（Methods of All Objects）**。

### ../read-only-attributes/README.md 摘要

`../read-only-attributes/README.md` 是对 `read-only-attributes.md` 的总结，介绍 EventController 提供的 7 个只读属性：

- **AbsSimTime** — 返回当前仿真时间的绝对时间表示，语法 `<Path>.AbsSimTime → dateTime`。
- **GetNextEventTime** — 返回事件列表中下一个事件计划执行的时间，语法 `<Path>.GetNextEventTime → time`。
- **IsFinished** — 返回是否已停止仿真并执行完所有 `endSim` 方法，语法 `<Path>.IsFinished → boolean`。
- **IsInitialized** — 返回是否已初始化，语法 `<Path>.IsInitialized → boolean`。
- **IsResetting** — 返回此刻是否正在被重置，语法 `<Path>.IsResetting → boolean`。
- **IsRunning** — 返回此刻是否正在运行，语法 `<Path>.IsRunning → boolean`。
- **SimTime** — 返回当前仿真时间，语法 `<Path>.SimTime → time`（可监视）。

只读属性只能查询、不能设置；Plant Simulation 在查询时刻计算其值。只读属性来源同样包括**所有对象的只读属性（Read-Only Attributes of All Objects）**。
