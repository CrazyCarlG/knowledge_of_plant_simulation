# EventController — 只读属性

> 本文件是对同目录下 `read-only-attributes.md`（以及 `read-only-attributes.txtx`）的总结，介绍对象 **EventController**（事件控制器）提供的**只读属性**。
> `read-only-attributes/` 目录下没有子文件夹；同级目录中的 README 为 `../general/README.md` 与 `../methods/README.md`，其内容摘要见文末“相关概述”。

## 只读属性来源

EventController 提供：

- 目录中所列的只读属性（即本文件归纳的 7 个属性）。
- **所有对象的只读属性（Read-Only Attributes of All Objects）**。

只读属性只能查询、不能设置；Plant Simulation 在你查询的时刻计算其值。多数只读属性对应对象某个选项卡（如 **Statistics** 选项卡）上的不可用对话框项。

查看对象的全部方法、只读属性和属性：

- 在 Class Library 中选中类，右键选择 **Show Attributes and Methods**。
- 在插入实例的 Frame 中按 **F8**，或点击 Home 选项卡上的 **Show Attributes and Methods**。

查询示例：

```simtalk
print EventController.AbsSimTime
```

---

## AbsSimTime [SimTalk]

返回 `<Path>` 所指定的 EventController 的当前仿真时间，以绝对时间语句表示。

- **类型：** 只读属性
- **语法：** `<Path>.AbsSimTime → dateTime`
- **返回值：** `dateTime`
- **示例：** `print EventController.AbsSimTime // 可能返回 22026-01-01 06:00:00.0000`
- **参见：** Time [EventController]

---

## GetNextEventTime [SimTalk]

返回 `<Path>` 所指定的 EventController 的事件列表中，下一个事件计划执行的时间。

- **类型：** 只读属性
- **语法：** `<Path>.GetNextEventTime → time`
- **返回值：** `time`
- **示例：** `print EventController.GetNextEventTime // 可能返回 10.0000`
- **参见：** List of Events

---

## IsFinished [SimTalk]

返回 `<Path>` 所指定的 EventController 是否已停止仿真并执行了所有 `endSim` 方法（`true`）或尚未（`false`）。

**备注：** 与只读属性 `IsRunning` 不同，`IsFinished` 只有在所有 `endSim` 方法都执行完之后才会变为 `true`。

- **类型：** 只读属性
- **语法：** `<Path>.IsFinished → boolean`
- **可监视（Watchable）：** 是
- **返回值：** `boolean`
- **示例：** `print root.EventController.IsFinished`
- **参见：** `endSim` [SimTalk]、`IsRunning` [SimTalk]

---

## IsInitialized [SimTalk]

返回 `<Path>` 所指定的 EventController 是否已初始化（`true`）或尚未（`false`）。

**备注：** 当所有以整数为参数的 `init` 方法在初始化阶段 1 中以值 `1` 被调用，且所有对象都已初始化时，Plant Simulation 会初始化 EventController。例如：故障配置文件处于活动状态且所有对象已计算出其第一个故障事件；某个 Variable 的属性 `HasInitValue` 被设为 `true` 且初始值已重置等。

- **类型：** 只读属性
- **语法：** `<Path>.IsInitialized → boolean`
- **可监视（Watchable）：** 是
- **返回值：** `boolean`
- **示例：** `print root.EventController.IsInitialized`
- **参见：** `HasInitValue` [SimTalk] - Variable、`InitValue` [SimTalk] - Variable、Initial Value [Variable]

---

## IsResetting [SimTalk]

返回 `<Path>` 所指定的 EventController 此刻是否正在被重置（`true`）或否（`false`）。

**备注：** 当你用 `<Path>` 所指定的 EventController 重置仿真模型时，Plant Simulation 将 `IsResetting` 设为 `true`；当所有 `reset` 方法处理完毕后，再将其设回 `false`。

- **类型：** 只读属性
- **语法：** `<Path>.IsResetting → boolean`
- **可监视（Watchable）：** 是
- **返回值：** `boolean`
- **示例：** `print EventController.IsResetting`
- **参见：** `reset` [SimTalk] - EventController

---

## IsRunning [SimTalk]

返回 `<Path>` 所指定的 EventController 此刻是否正在运行（`true`）或否（`false`）。

- **类型：** 只读属性
- **语法：** `<Path>.IsRunning → boolean`
- **可监视（Watchable）：** 是
- **返回值：** `boolean`
- **示例：** `print root.EventController.IsRunning`
- **参见：** `IsFinished` [SimTalk]

---

## SimTime [SimTalk]

返回 `<Path>` 所指定的 EventController 的当前仿真时间。

- **类型：** 只读属性
- **语法：** `<Path>.SimTime → time`
- **可监视（Watchable）：** 是
- **返回值：** `time`

**注意：** 你可以用 Display 或 Chart 类型的对象监视 `SimTime` 值。切勿在影响仿真的方法中将 `SimTime` 与 `waituntil` 或 `stopuntil` 指令一起使用。时间并非连续推进，而是从一个事件跳到下一个事件；若启用动画，Plant Simulation 会生成额外事件，`waituntil` 或 `stopuntil` 指令可能在比预期更早的时间点被唤醒。

**示例：**

```simtalk
param sensorID: integer, Front: boolean
if @.ID = 1 
   @.Speed := 0
   print EventController.SimTime, " The first Transporter stopped."
end
```

```simtalk
print "Machine was deactivated at:",
root.EventController.SimTime."
```

- **参见：** Time [EventController]、`waituntil` [SimTalk]、`stopuntil` [SimTalk]

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
