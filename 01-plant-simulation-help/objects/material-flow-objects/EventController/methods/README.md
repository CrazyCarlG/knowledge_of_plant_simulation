# EventController — 方法

> 本文件是对同目录下 `methods.md`（以及 `methods.txtx`）的总结，介绍对象 **EventController**（事件控制器）提供的**方法**。
> `methods/` 目录下没有子文件夹；EventController 下唯一的 README 是 `../general/README.md`，其内容摘要见文末“相关概述”。

## 方法来源

EventController 提供：

- 左侧目录中所列的方法（即本文件归纳的 `getEventList`、`reset`、`start`、`stop`）。
- **所有对象的通用方法（Methods of All Objects）**。

查看对象的全部方法、只读属性和属性：

- 在 Class Library 中选中类，右键选择 **Show Attributes and Methods**。
- 在插入实例的 Frame 中按 **F8**，或点击 Home 选项卡上的 **Show Attributes and Methods**。

## 语法行读法（Reading the Syntax Line）

方法语法行示例：

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所作用对象的路径。
- 方法签名（标识符 + 参数数据类型）写在括号内。如 `(Parameter:string)` 表示 string 类型参数；除了常量，也可使用所需类型的变量或返回所需类型的方法。
  > **注意：** 括号内的表达式务必带上括号 `(…)`，否则可能产生意外结果并打开 Debugger。
- 可选参数放在方括号内，如 `[,Parameter:boolean]` 表示该布尔参数可省略。
- 若参数有默认值，签名会在参数后写出，如 `:= false`。
- 若方法有返回值，签名在箭头后写出其数据类型，如 `→ boolean`。

---

## getEventList [SimTalk]

返回 `<Path>` 所指定的 EventController 的**已调度事件列表**。

- **类型：** 方法
- **语法：** `<Path>.getEventList(MaximumNumberOfEvents:integer) → table`
- **参数：** `MaximumNumberOfEvents`（integer）指定 EventController 写入数据表的最大事件数。传 `getEventList(-1)` 可写入全部事件。事件列表包含列 **Type**、**Time**、**Receiver**、**Sender**、**Insertion Time**、**Parameters**。
- **返回值：** 数据类型 `table`。
- **示例：** `TableVariable := EventController.getEventList(-1)`
- **参见：** List of Events、Event List

---

## reset [SimTalk] — EventController

使 `<Path>` 所指定的 EventController 运行仿真模型中所有名为 `reset` 的方法。

所有 `reset` 方法执行完毕后，Plant Simulation 会：

- 删除所有未处理的事件
- 将仿真时间重置为 0
- 重置统计
- 清除模型中所有对象的所有故障
- 将所有对象设置为 `planned` 状态
- （若启用）删除所有零件
- 若保持 **Tools > Inherit 'Entrance/Exit Locked' On Reset** 开启，则为新模型重新激活 **Entrance Locked** 与 **Exit Locked** 设置的继承

> **注意：** 重置仿真时，Importer 的 Request Control、Receive Control、Release Control **不会**被调用。

Plant Simulation **不会立即**执行重置命令，而是等到当前正在执行的所有方法（包括触发重置的那个方法）完全执行完后才执行；`start` 方法同样如此。

- **类型：** 方法
- **语法：** `<Path>.reset`
- **示例：**

```simtalk
EventController.reset
EventController.start
EventController.RandomNumbersVariant :=
EventController.RandomNumbersVariant + 1
-- 当此方法完全执行完后，EventController 才会被重置。
-- 当重置阶段完全结束后，仿真才会再次启动。
end
```

- **参见：** ResetCtrl [SimTalk]、reset [SimTalk]（预定义名称）、start [SimTalk] — EventController、Reset Simulation [EventController]、Reset Simulation [EventDebugger]、Entrance Locked / Exit Locked [material flow objects]、Inherit 'Entrance/Exit Locked' On Reset

---

## start [SimTalk] — EventController

激活 `<Path>` 所指定的 EventController 并启动仿真运行。

- 若在仿真运行期间对另一个 Frame 中的另一个 EventController 调用该方法，Plant Simulation 会停止当前的 EventController，并在那个 Frame 中启动仿真运行。
- Plant Simulation **不会立即**启动 EventController，而是等到当前正在执行的所有方法完全执行完后才启动；`reset` 方法同样如此。

- **类型：** 方法
- **语法：** `<Path>.start([WithAnimation:boolean:=animation, RealTime:boolean:=EventController.Realtime])`
- **参数：**
  - `WithAnimation`（boolean）：设置是否带动画启动（`true`）或关闭动画（`false`）。默认值为 `animation`；若不指定，则采用全局动画设置（参见 MUs and States 与函数 `animation`）。
  - `RealTime`（boolean）：设置 EventController 启动实时仿真（`true`）还是全速仿真（`false`）。默认值为 `EventController.Realtime`；若不指定，则使用属性 `RealTime` 的值。
    > **注意：** 实时仿真会考虑实时缩放因子，因此当因子大于 1 时可比实时更快，因子小于 1 时更慢。
- **示例：** `.delivery.EventController.start(false,false)` — 以最大速度、无动画方式启动仿真。
- **参见：** reset [SimTalk] — EventController、Realtime [SimTalk]、animation [SimTalk]、Start/Stop Simulation [EventController]、MUs and States [Home ribbon]、Real-time x [EventController]

---

## stop [SimTalk] — EventController

停止 `<Path>` 所指定的 EventController，从而终止仿真运行。

- 仿真不会停止，直到当前方法执行（包括整个调用栈）完成或被挂起；例如 `wait` 语句会挂起方法执行。

- **类型：** 方法
- **语法：** `<Path>.stop([EndSim:boolean:=false])`
- **参数：** 可选参数 `EndSim`（boolean）设置：停止仿真并执行 `endSim` 方法（`true`），或仅停止仿真（`false`）。默认值为 `false`。
- **示例：** `root.EventController.stop`
- **参见：** endSim [SimTalk]、Start/Stop Simulation [EventController]、wait [SimTalk]、Suspending Methods

---

## 只读属性（Read-Only Attributes）

`methods.md` 末尾附带只读属性的总述：

- EventController 提供目录中所列的只读属性，以及 **所有对象的只读属性（Read-Only Attributes of All Objects）**。
- 只读属性只能查询、不能设置；Plant Simulation 在你查询的时刻计算其值。多数只读属性对应对象某个选项卡（如 Statistics 选项卡）上的不可用对话框项。
- 查询示例：`print EventController.AbsSimTime`

---

## 相关概述（../general/README.md 摘要）

`../general/README.md` 是对 `general.md` 的总结，可作为本文件方法的背景参考：

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
