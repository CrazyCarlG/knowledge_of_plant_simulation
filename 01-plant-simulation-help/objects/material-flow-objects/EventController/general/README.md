# EventController — 概述

> 本文件是对同目录下 `general.md` 的总结，介绍对象 **EventController**（事件控制器）。

## 用途

**EventController** 用于协调、同步和控制仿真运行期间发生的事件。Plant Simulation 是一个**离散事件仿真系统**：它只在特定时间点显示模型组件的状态变化，而不是随时间连续变化。

- 无法更改 EventController 的名称。
- 若手动删除 EventController，Plant Simulation 会先重置模型。

## 工作原理

当 MU 进入某个加工站（如 Station）时，Plant Simulation 计算其加工时间，并把该事件写入 EventController 的**已调度事件列表（List of scheduled events）**——相当于在时间轴上插入标记。EventController 像播放器一样沿时间轴移动，在时间到达时通知相应对象处理事件（如 `Out` 事件），将 MU 传送到后续对象。此过程对所有 MU 循环进行。

## 启动与停止仿真

**启动仿真：**
- 点击 EventController 对话框中的 **Start/Stop Simulation**
- 点击 Frame 的 Home 选项卡上的 **Start/Stop Simulation**（若尚未插入 EventController 会提示插入）
- 点击迷你工具栏上的 **Start/Stop Simulation**

**停止仿真：**
- 点击 **Single Step Simulation**
- 再次点击 Home 选项卡上的 **Start/Stop Simulation**
- 再次点击迷你工具栏上的 **Start/Stop Simulation**

仿真在当前事件完全处理完后停止。仿真运行结束时，Plant Simulation 执行所有名为 `endSim` 的方法（当事件列表为空或达到 **End time** 时触发）。也可用 **EventDebugger** 单步执行。

**添加到模型：** Home 选项卡 → *Manage Class Library > Basic Objects > MaterialFlow > EventController*。

## 对话框与时间显示

双击 EventController 图标打开对话框，可编辑仿真属性与动画属性。

**Time** 可切换时间显示方式：
- **Relative time**（相对时间，默认，从 0 开始）
- **Current time plus simulation time**（当前日期时间 + 仿真时间）

相关 SimTalk：`AbsSimTime`、`SimTime`。

## 选项卡 Controls（控制）

- **Reset Simulation** — 重置模型：调用所有 `reset` 方法，删除未处理事件、仿真时间归零、重置统计、清除故障、对象置为 `planned` 状态等。SimTalk：`reset`、`deleteSuspendedMethods`、`initStat`、`IsInitialized`、`ResetCtrl`。
- **Start/Stop Simulation** — 启动/停止仿真；必要时先调用 `init` 方法。SimTalk：`start`、`stop`、`StartStopCtrl`、`init`、`InitCtrl`。
- **Start Full Speed Simulation** — 全速 + 动画，忽略实时缩放因子。SimTalk：`Realtime`、`RealtimeScale`。
- **Start Fast Forward Simulation** — 最快速度、无动画、不更新部分数值（如 Variable/Display）。
- **Single Step Simulation** — 处理下一个事件后停止；按住 Shift 会打开 Method Debugger。

## 已调度事件列表（List of Scheduled Events）

点击 **List** 打开 Event Debugger，显示事件列表（按时间升序）。列包括：**Breakpoint**、**Type**、**Time**、**Receiver**、**Sender**、**Insertion Time**、**Parameters**。SimTalk：`getEventList`。

事件类型众多（约 50 种），例如：
- `Animation` — MU 位于 Track/Conveyor/Buffer 上
- `Battery` — Transporter 电池状态变化
- `CreateMU` — Source 尝试创建 MU
- `DisruptionBegin` / `DisruptionEnd` — 故障开始/结束
- `Init` / `InitStat` — 初始化模型 / 重置统计
- `MethCall` / `MethWakeup` — 调度方法调用 / `wait` 后继续
- `Out` / `OutEnd` — MU 离开对象
- `Pause` / `PauseEnd` — 暂停开始/结束
- `SensorStart` / `SensorEnd` / `SensorBookPos` — 传感器触发
- `SetupEnd` — 设置时间结束
- `Shift` / `ShiftCalendarStart` — 班次调度
- `StartActions`、`StartTransporter`、`TankEmpty`、`TankFull`、`TriggerAction`、`UpdateDisplay` 等

完整列表（含德文对照）见 `general.md`。

**事件列表上下文菜单**：Show Receiver/Open Receiver/Show Sender/Open Sender、Stop at Event、Create Breakpoint from Event、Run to Time、Time。

## 速度滑块与实时缩放

- **Slower/Faster Slider** — 左右拖动（或方向键）调整仿真速度，效果同 Home 选项卡的速度滑块。
- **Real-time x** — 设置实时缩放因子（实时持续时间 = 仿真时间 / 缩放因子）。Start/Stop Simulation 默认缩放因子为 3；Full Speed 与 Fast Forward 忽略该因子。SimTalk：`Realtime`、`RealtimeScale`。

## 选项卡 Settings（设置）

- **Start Date** — 绝对时间基准（SimTalk：`StartDate`）。
- **End Time** — 仿真结束的相对时间（SimTalk：`EndTime`）。
- **Statistics** — 开始收集统计数据的时刻，用于丢弃预热阶段数据（SimTalk：`StartStat`）。
- **Skip Long Event Intervals** — 实时仿真中跳过无相关事件的长时间段（SimTalk：`SkipLongEventIntervals`）。
- **Show Summary Report** — 运行结束显示 Drain 删除零件的汇总报告（平均寿命、总吞吐量、每小时吞吐量、生产/运输/存储时间占比、增值占比等；默认关闭）。SimTalk：`SummaryReport`。

## Event Debugger 对话框

用于精确控制事件执行，可设置条件、单步跟踪。打开方式：Controls 选项卡点击 **List**，或按住 Shift 双击 EventController 图标。

- **Breakpoints Active** — 激活断点（SimTalk：`BreakpointsActive`）。
- **Breakpoints** — 打开断点对话框，创建/编辑/删除断点。
- **Breakpoint 对话框** — 可设置 Receiver、Sender、Start Time、Stop Time、Type（`*` 表示任意类型）、Condition（匿名标识符 `@` 访问接收方、`?` 访问发送方）、Trace File。
- **Run to Time** — 运行到指定时间后停止（不执行 `endSim` 方法）。
- **Trace File** — 将记录的事件写入文件（SimTalk：`TraceActive`、`TraceFile`）。
- **仿真控制按钮** — Reset、Start/Stop、Full Speed、Fast Forward、Single Step、Debug Next Simulation Step、Step Halts Additionally Before Event、Close。

**Condition 代码示例：**

```simtalk
@.Name = "Wheel" AND @.getNo = 4
```

```simtalk
@.length < 100
```

## 菜单

- **Navigate Menu** — 导航菜单。
- **View Menu** — `Refresh`、`Show Summary Report`、`Show Attributes and Methods`（SimTalk：`updateDialog`）。
- **Tools Menu** — `Edit Controls > Init Control`、`Random Numbers Variant`、`Increment Variant on Reset`、`Antithetic Random Numbers`、`User-defined Attributes`、`Edit Observers`、`Show Summary Report`。
- **Help Menu** — 帮助菜单。

### Init Control

在初始化阶段、对象初始化之前调用一次，用于初始化影响事件生成的属性（如可用性）。SimTalk：`InitCtrl`。

### 随机数相关

- **Random Numbers Variant** — 显示/设置随机数变体（SimTalk：`RandomNumbersVariant`、`RandomSeed`）。
- **Increment Variant on Reset** — 重置后是否生成不同随机数（SimTalk：`IncrementRandomNumbersVariantOnReset`）。
- **Antithetic Random Numbers** — 使用普通/对偶随机数（均匀分布 `U` 的对偶值为 `1-U`）。SimTalk：`setAntitheticRandomNumbers`。

## 方法

EventController 提供目录中所列方法以及 **所有对象的通用方法（Methods of All Objects）**。可打开 **Show Attributes and Methods**（Frame 上按 F8，或 Class Library 上下文菜单）查看全部方法、只读属性和属性。
