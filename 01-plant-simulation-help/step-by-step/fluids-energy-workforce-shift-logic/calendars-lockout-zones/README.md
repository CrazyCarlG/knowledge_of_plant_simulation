# Calendars, Lockout Zones & Shift Logic（日历、封锁区与班次逻辑）

本目录汇总了 Plant Simulation 帮助文档中关于班次系统、`ShiftCalendar`（班次日历）与 `LockoutZone`（封锁区）对象的内容。目录内的源文件为：

- `calendars-lockout-zones.md` —— 已整理为 Markdown 的总结文档
- `calendars-lockout-zones.txtx` —— 原始帮助文本（含页码与排版）

以下为全部内容的要点总结。

---

## 1. 用 Importer、Broker 与 Exporter 建模工人（结论）

打开 `EventController` 并点击 **Start/Stop Simulation**。由于 `Exporter` 一次只能在一个工位工作，而 `Station1` 与 `Station3` 共享 `Exporter1`，因此会出现短暂的停顿：

- `Station1` 必须等待 `Station3` 释放 `ExporterJob1`，因此处于 **Blocked（阻塞）** 状态。
- `Station3` 必须等待 `Station1` 释放 `Exporter1`，因此处于 **Waiting（等待）** 状态。
- 所有工位都从 `Exporter3` 获取 `Setup` 服务，该服务每个工位仅需一次，所以不造成问题。

还可以打开 **Statistics（统计）** 选项卡查看对象收集的数据。

---

## 2. 建模班次系统（Modeling a Shift System）

使用 `ShiftCalendar` 对象可以快速定义班次。

`ShiftCalendar` 可以控制以下物流对象的**工作时间、暂停时间、计划时间与非计划时间**：

`Frame`、`Station`、`ParallelStation`、`AssemblyStation`、`DismantleStation`、`Buffer`、`PlaceBuffer`、`Store`、`Sorter`、`Conveyor`、`AngularConverter`、`Turntable`、`Turnplate`、`Track`、`TwoLaneTrack`、`Source`、`Drain`、`WorkerPool`、`Exporter`。

它还可以控制用于建模整个工厂组件的 `Frame`。此时使用 **Method（方法）** 作为 Frame 的"非计划时间"与"暂停时间"控制，把班次设置传播到 Frame 内部的对象。

对于流体对象，`ShiftCalendar` 可控制以下对象的工作时间、暂停时间、计划时间与非计划时间：

`FluidSource`、`Mixer`、`Portioner`、`DePortioner`。

可使用 `schedule` 方法让 `ShiftCalendar` 设定生产过程的开始或结束日期与时间。

### 开始与结束一个班次

- 当 `ShiftCalendar` **开始班次**时，会将其控制的物流对象与 Frame 的属性 `Unplanned` 设为 `false`（停用非计划时间）。必要时可编写 **Unplanned Control** 执行其他动作。
- 物流对象的统计随即开始记录**非计划时间**——即资源未被安排工作的时间。
- 例如：班次从 06:00 到 22:00 有效 → 计划时间为 06:00–22:00；非计划时间为次日凌晨 22:00–06:00。
- 当 `ShiftCalendar` **结束班次**时，会把 `Unplanned` 设为 `true`（启用非计划时间）。对象停止处理当前零件并释放所有服务。

### 开始与结束休息

- 当 `ShiftCalendar` **开始休息**时，会将其控制对象与 Frame 的属性 `Pause` 设为 `true`。对物流对象，启用暂停还会影响统计；对 Frame，Plant Simulation 只改变属性状态（可编写 **Pause Control**）。
- 当 `ShiftCalendar` **结束休息**时，将 `Pause` 设为 `false`。

示例模型位于：**Window 功能区选项卡 > Start Page > Getting Started > Example Models > Small Examples**。

---

## 3. 用 ShiftCalendar 定义班次

从类库的 **Resources** 文件夹，或工具箱的 **Resources** 工具栏插入 `ShiftCalendar`。

可以：

- 指定班次名称、相应时间与星期
- 指定工厂部分时间工作的时间段
- 指定 `ShiftCalendar` 控制的工位
- 安排生产过程开始/结束的日期与时间

输入完设置后，勾选 **Active** 复选框，Plant Simulation 才会在模型中使用这些班次。

### 指定班次名称、时间与星期

输入数据前先点击 **Inheritance** 复选框。每一行输入一个班次的数据：

- **Shift** —— 班次名称（如 Morning shift、Day shift、Evening shift、Graveyard shift）。
- **From** —— 班次开始时间（0:00–24:00，仅小时和分钟）。
  - 单日内的班次：结束时间大于开始时间（如早班 6:00 → 14:00）。
  - 跨两天的班次：结束时间小于开始时间（如夜班 22:00 → 次日 6:00）。
- **To** —— 班次结束时间（0:00–24:00，仅小时和分钟）。
- **Days of the week** —— 点击星期下方的单元格选择生效日期（如早班周一至周六；晚班周一至周五）。
- **Pauses** —— 各班次的休息时间，如 `9:00-9:15;12:00-12:45`（咖啡休息 + 午休）。多个休息用分号分隔。

点击 **Apply** 让 `ShiftCalendar` 检查休息时间是否合理、格式是否正确。

还可以将班次以制表符分隔的文本文件**导入/导出**（右键列表字段 → **Export** 或 **Import**）。

### 指定工厂部分工作的时间段

先点击 **Inheritance** 复选框。

- **Date From** —— 工厂开始停工（不工作）的日期。双击单元格，点击下拉箭头，在日历中选择日期。
- 将整天设为休息日：只输入开始日期（不填 **Date To** 和 **Reduce Time To**）。
- **Date To** —— 工厂停止不工作的日期（从日历选择）。
- **Reduce Time To** —— 单个工作日部分时间工作时，输入缩减工作时间的起止小时（如平安夜半天工作输入 `0:00 - 12:00`）。
- **Comment** —— 说明工厂为何不工作的描述。

> **注意：** `ShiftCalendar` 会把某天的缩减时间与班次定义结合起来。如果缩减工作日的开始时间恰好落在休息时段，该工作日会以休息开始。

也可将日历以制表符分隔文本文件导入/导出。

### 指定 ShiftCalendar 控制的工位

在列表单元格中输入任意内置物流对象的名称，或用于建模机器的 `Frame` 的名称。这会自动把 `ShiftCalendar` 填入：

- Frame 功能区选项卡上 **Select Shift Calendar** 命令打开的对话框。
- 物流对象 **Controls** 选项卡上的 **Shift calendar** 文本框。

### 安排生产过程开始/结束的日期与时间

使用 `schedule` 方法设置生产过程的开始/结束日期与时间。有两种模式：

- **Forward scheduling（正向排程）** —— 从开始日期向未来推进。
- **Backward scheduling（逆向排程）** —— 从需求日期向过去倒推开始日期。

通常从需求日期出发，通过逆向排程计算开始日期；若开始日期已过去，则从当前时间重新计算并正向排程结束日期。

示例——计算两个作业的结束日期（考虑 `ShiftCalendar` 中定义的班次）：

```simtalk
var startTime := str_to_dateTime( "4.1.2013 0:00" )
var durationTime := str_to_time( "10:00:00.0" )
var EndTime := ShiftCalendar.schedule( startTime, durationTime, "forward" )
print "StartDate: ", startTime, "   Duration: ", durationTime, "   EndDate: ", EndTime
startTime := str_to_dateTime( "20.12.2013 0:00" )
durationTime := str_to_time( "19:00:00.0" )
EndTime := ShiftCalendar.schedule( startTime, durationTime, "forward" )
print "StartDate: ", startTime, "   Duration: ", durationTime, "   EndDate: ", EndTime
```

第一个作业从 2013 年 1 月 4 日午夜开始，耗时 10 小时；第二个从 2013 年 12 月 12 日开始，耗时 19 小时。方法把结果打印到 Console。

---

## 4. 暂停物流对象与 Frame（Pausing Material Flow Objects and Frames）

`ShiftCalendar` 通过改变所控制对象与 Frame 的 `Paused`/`Planned`/`Unplanned` 状态来与之交互。

对象状态：

- **Paused（暂停）** —— 因休息而不再处理零件。休息结束后恢复（从下拉列表选择 **Planned**，或将 `Pause` 设为 `false`）。

  > **注意：** 当工位发生故障且故障期间出现休息时，即使工位处于暂停，故障时间仍会被消耗。统计会把这两个状态重叠的时间计为暂停时间。重置模型会同时移除故障与暂停。

- **Unplanned（非计划）** —— 在 `ShiftCalendar` 定义的班次之外，未被安排工作。
- **Planned（计划）** —— 在班次内被安排工作。计划/排程时间 = 处理时间 − 休息时间。

### 暂停的物流对象

`ShiftCalendar` 按定义的班次改变物流对象的暂停状态。仿真运行期间，这些对象的对话框会在下拉列表中反映当前状态。

暂停时，物流对象不接收任何移动零件（MU）。只有通过 Method 编程才能让 MU 离开对象。Plant Simulation 会停止装配与处理，直到暂停或非计划时间结束。

非计划状态与暂停状态相同，唯一区别在于 Plant Simulation 如何统计内部数据。当被安排工作时，对象接收并处理 MU，并移交给后续对象。

### 暂停的 Frame

用属性 `Pause` 与 `Unplanned` 暂停 Frame。与物流对象（可手动暂停）不同，Frame 的暂停/非计划状态只能通过属性修改。

还可以编写暂停控制与/或非计划时间控制，二者都在属性值改变时激活一个 Method。

#### 暂停控制（Pause Control）示例

给属性 `Pause` 赋值 `true` 或 `false`。在控制内部用匿名标识符 `?` 访问该对象。每当暂停状态改变时，Plant Simulation 执行 Pause Control；在 Method 中读取暂停状态会得到改变后的状态。

```simtalk
print "Current pause ", current.pause
MyStation.pause := current.pause
var shift := root.ShiftCalendar.getCurrShift
print "Current shift: ", shift
if not current.unplanned
   if current.pause
      current.currIcon := "pause"
   else
       current.currIcon := "working"
   end
end
```

#### 非计划控制（Unplanned Control）示例

每当 Frame 的非计划状态改变时，Plant Simulation 执行 Unplanned Control。给属性 `Unplanned` 赋值 `true` 或 `false`。用 `?` 访问对象。

```simtalk
print "Frame unplanned: ", current.unplanned
MyStation.unplanned := current.unplanned
if current.unplanned
   current.currIcon := "unplanned"
else
   if current.pause
      current.currIcon := "pause"
   else
      current.currIcon := "working"
   end
end
```

---

## 5. 建模封锁区（Modeling a Lockout Zone）

`LockoutZone` 将一组物流对象组合在一起。当其中某个工位发生故障时，封锁区内的其他所有工位都停止处理零件。

必须为至少一个被指派的工位定义故障配置（failure profile）。一旦某个工位故障，`LockoutZone` 会停止所有已指派工位的全部处理操作。可以选择立即停止，或在所需服务到达时停止。

只有**所有**故障都被排除后，工位才会重新开始处理零件，且只消耗剩余的加工时间。可以指派任意内置物流对象，或在 Frame 中建模的工位。

从类库 **Resources** 文件夹或工具箱 **Resources** 工具栏插入 `LockoutZone`。

可以：

- 指定 `LockoutZone` 停止的工位
- 为其中一个工位创建故障配置
- 故障后立即停止关联工位
- 维修人员到达时停止关联工位
- 使用停止处理控制（Stop Processing Control）
- 使用恢复处理控制（Resume Processing Control）

### 指定 LockoutZone 停止的工位

示例模型中，`Station2`、`Station3`、`Station4` 属于封锁区。若 `Station3` 故障，封锁区会停止 `Station2` 与 `Station4`。

`Station2` 与 `Station4` 的停止时间百分比须与 `Station3` 的故障时间百分比一致；封锁区内工位的总可用性与 `Station3` 的可用性一致。

将工位添加为资源：

- 把对象图标（如 `Station2`）拖到 `LockoutZone` 图标上并放下。
- 对 `Station3` 和 `Station4` 重复此操作。

为直观显示哪些对象属于封锁区，可在 Frame 中插入一个 `Cuboid` 并赋予材质：

- 点击 **Edit** 功能区选项卡上的 **Cuboid**，为 **Dimension Z**（高度）输入较小值。
- 将 Cuboid 插到 `Station2` 上方，按 **M** 显示操纵器。
- 点击 Cuboid 右下角并拖动，使其覆盖 `LockoutZone` 与各工位。
- 调整标题位置（如选中 `Station1`，按空格键，在 **Edit 3D Properties** 中切换到 **Captions** 选项卡；受影响工位使用 Y 位置 -1.35）。
- 最后调整 `LockoutZone` 的标题位置，并为 Cuboid 赋予材质/颜色。

### 为其中一个工位创建故障配置

让某个工位（如 `Station3`）故障：

- 点击 **Failures** 选项卡，点击 **New**。
- 输入**可用性（availability）** 与**平均修复时间（mean time to repair）**（如可用性 85%，MTTR 15 分钟）。
- 点击 **OK**。

### 故障后立即停止关联工位

选择 **Stop mode > Stop immediately**。这样 `Station3` 一故障，`LockoutZone` 就立即停止 `Station2` 与 `Station4` —— 只停止封锁区内的工位。

检查统计：

- 打开 `Station2`、`Station3`、`Station4` 的对话框，切换到 **Statistics** 选项卡。
- `Station2` 与 `Station4` 的停止百分比与 `Station3` 的故障百分比一致；总体可用性与故障工位一致。
- 要打开统计报告，选中 Frame 中的工位并按 **F6**。

### 维修人员到达时停止关联工位

选择 **Stop mode > Stop when Service arrives**。`LockoutZone` 会在故障工位请求的维修服务被指派时停止关联工位。

创建示例模型：

- 插入工位并拖到 `LockoutZone` 图标上指派（本例为 `Station2`、`Station3`、`Station4`）。
- 为工位添加 `Workplace`，并用 footpath（步行路径）将其与 `WorkerPool` 连接。
- 为 `Station3` 定义故障配置。
- 插入 `Broker`，在 **Failure** 子选项卡上指派它，并激活故障 importer。无需改动其他设置。
- 运行仿真。`Station3` 故障后，Worker 沿 footpath 从 `WorkerPool` 走向故障工位。服务技术员到达故障工位附着的 `Workplace` 后，`LockoutZone` 停止关联工位。

### 使用停止处理控制（Stop Processing Control）

要使用自己的逻辑处理"某个指派工位故障"的情况，可编写 **Stop Control**。在 Stop Control 内，匿名标识符 `@` 表示触发故障的工位，`?` 表示 `LockoutZone`。

示例（把信息写入表 `ReportStopping`）：

```simtalk
var row:integer := ReportStopping.ydim + 1
ReportStopping["First Failed Station",row] := @.name
ReportStopping["Start Stopping",row] := eventcontroller.simTime
```

### 使用恢复处理控制（Resume Processing Control）

要使用自己的逻辑处理"所有指派工位的故障都已修复、工位可继续处理"的情况，可编写 **Resume Control**。其中 `@` 表示触发工位，`?` 表示 `LockoutZone`。

示例：

```simtalk
var row: integer := ReportStopping.ydim
ReportStopping["Last Failed Station",row] := @.name
ReportStopping["End Stopping",row] := eventcontroller.simTime
ReportStopping["Duration",row] := ReportStopping["End Stopping",row] - ReportStopping["Start Stopping",row]
```

### 被停止的物流对象与 Frame

`LockoutZone` 通过将其指派物流对象的属性 `Stopped` 设为 `true` 来停止它们；对于被指派的 Frame，同样将其属性 `Stopped` 设为 `true`。
