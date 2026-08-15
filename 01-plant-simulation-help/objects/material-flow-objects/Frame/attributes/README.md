# Frame — 属性（Attributes）总结

> 本文件是对同目录下 `attributes.md`（以及同内容的文本提取文件 `attributes.txtx`）的总结，介绍对象 **Frame（框架）** 提供的**属性**。
> `attributes/` 目录下没有子文件夹，因此没有子文件夹 README.md。同级目录中的 README 为 `../general/README.md`、`../methods/README.md`、`../read-only-attributes/README.md` 与 `../window/README.md`，其内容摘要见文末“相关概述”。

## 属性来源

Frame 提供：

- 下表所列的 Frame 专属属性（本文件归纳的 13 个属性，其中 1 个为只读属性）。
- **所有对象的属性（Attributes of All Objects）**。

你可以设置属性的值，也可以获取属性的值，既可通过对话框中的复选框、文本框和下拉列表，也可通过给相应属性赋值。

查看对象的全部方法、只读属性和属性，可打开 **Show Attributes and Methods（显示属性和方法）** 窗口：

- 在 **Class Library（类库）** 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例的 Frame 的 **Home（开始）** 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。

设置示例：

```simtalk
Frame.StateBlocked := true
```

获取示例：

```simtalk
print .Models.Model.BackgroundColor
posit := MyStation.Cont.XPos
```

## 属性清单

| 属性 | 说明 | 类型 | 数据类型 / 语法 |
| --- | --- | --- | --- |
| [NumNodes](#numnodes) | 返回 Frame 中的对象数量 | 只读属性 | `<Path>.NumNodes → integer` |
| [Failed](#failed) | 使 Frame 失败（true）或不失败（false） | 属性（可监视） | `<Path>.Failed:boolean` |
| [LockStructure](#lockstructure) | 锁定（true）或解锁（false）Frame 结构 | 属性 | `<Path>.LockStructure:boolean` |
| [Pause](#pause) | 暂停（true）或不暂停（false）Frame | 属性 | `<Path>.Pause:boolean` |
| [ReplacementMode](#replacementmode) | 设置 Frame 的替换模式（`"exchange"` 或 `"merge"`） | 属性 | `<Path>.ReplacementMode:string` |
| [ShiftCalendarObject](#shiftcalendarobject) | 设置控制 Frame 工作班次的 ShiftCalendar | 属性 | `<Path>.ShiftCalendarObject:path` |
| [StateBlocked](#stateblocked) | 将 Frame 状态设为阻塞（true）或不阻塞（false） | 属性 | `<Path>.StateBlocked:boolean` |
| [StateEntryShut](#stateentryshut) | 将 Frame 状态设为入口关闭（true）或不关闭（false） | 属性 | `<Path>.StateEntryShut:boolean` |
| [StateResourceMissing](#stateresourcemissing) | 将 Frame 状态设为缺少资源/等待（true）或不缺少（false） | 属性 | `<Path>.StateResourceMissing:boolean` |
| [StateSetup](#statesetup) | 将 Frame 状态设为准备中（true）或不准备（false） | 属性 | `<Path>.StateSetup:boolean` |
| [StateWorking](#stateworking) | 将 Frame 状态设为工作中（true）或不工作（false） | 属性 | `<Path>.StateWorking:boolean` |
| [Stopped](#stopped) | 停止（true）或不停止（false）Frame | 属性（可监视） | `<Path>.Stopped:boolean` |
| [Unplanned](#unplanned) | 将 Frame 设为计划外（true）或计划内工作（false） | 属性 | `<Path>.Unplanned:boolean` |

此外，`attributes.md` 末尾还提及了 **Interface** 对象（用于在 Frame 之间建立转换、实现层次化建模），详见 [Interface](#interface)。

---

## NumNodes [SimTalk] — Frame

返回 `<Path>` 指定的 Frame 中的对象数量。

- **备注**：
  - 插入到所选 Frame 中的每个额外 Frame 都计为单个对象；Plant Simulation **不**统计这些 Frame 内部所包含的对象。
  - Connectors（连接器）也计为对象。
- **类型**：只读属性（Read-only attribute）
- **语法**：`<Path>.NumNodes → integer`
- **返回值**：数据类型为 `integer`。
- **示例**：

```simtalk
print .Models.MyPlant.NumNodes
```

- **参见**：`node` [SimTalk] - Frame、Attributes of the Frame

---

## Failed [SimTalk] — Frame

使 `<Path>` 指定的 Frame 失败（`true`）或不失败（`false`）。

- **类型**：属性（Attribute）
- **语法**：`<Path>.Failed:boolean`
- **可监视（Watchable）**：该属性可被监视，Plant Simulation 会调用一个 control。
- **赋值**：可赋 `boolean` 类型值。
- **注意**：在仿真的重置阶段，Plant Simulation 会重置所有故障。
- **示例**：

```simtalk
subFrame.failed := true
```

- **参见**：States of the Frame、Failed [check box] - material flow objects

---

## LockStructure [SimTalk]

锁定（`true`）或解锁（`false`）`<Path>` 指定的 Frame 的结构。

- **备注**：
  - `LockStructure` 默认关闭，即 Frame 处于解锁状态，可在其中创建模型。
  - 激活 **Lock Structure** 后，Plant Simulation 会阻止插入、删除和修改对象等意外更改；此时既不能更改对象的位置，也不能更改其名称。
  - 实例化的 Frame 默认激活 Lock Structure，以防止意外修改实例的结构——此类修改应作用于所有实例，因此应在类中进行。
- **类型**：属性（Attribute）
- **语法**：`<Path>.LockStructure:boolean`
- **赋值**：可赋 `boolean` 类型值。
- **示例**：

```simtalk
.frame2.LockStructure := true
print .frame2.LockStructure
```

- **参见**：Lock Structure [Frame ribbon]

---

## Pause [SimTalk] — Frame

暂停（`true`）或不暂停（`false`）`<Path>` 指定的 Frame。

- **备注**：重置 EventController 时，Plant Simulation 会重置暂停状态。
- **类型**：属性（Attribute）
- **语法**：`<Path>.Pause:boolean`
- **赋值**：可赋 `boolean` 类型值。
- **示例**：

```simtalk
EngineAssembly.Pause := true
```

- **参见**：Pause Material Flow Objects and Frames、Paused Frames、States of the Frame

---

## ReplacementMode [SimTalk]

设置 `<Path>` 指定的 Frame 的替换模式。

- **备注**：替换方（replacing）Frame 的替换模式决定 Frame 是被合并还是被替换；被替换方（replaced）Frame 的替换模式不产生任何影响。
- **类型**：属性（Attribute）
- **语法**：`<Path>.ReplacementMode:string`
- **赋值**：可赋 `string` 类型值，可指定 `"exchange"` 或 `"merge"`。
- **示例**：

```simtalk
Frame1.ReplacementMode := "merge"
```

- **SimTalk**：`loadObjectAs` [SimTalk]、`replace` [SimTalk]、`writeObject` [SimTalk]
- **参见**：Replacement Mode、Load Object

---

## ShiftCalendarObject [SimTalk] — Frame

设置控制 `<Path>` 指定的 Frame 中工作班次的 ShiftCalendar。

- **语法**：`<Path>.ShiftCalendarObject:path`
- **赋值**：可赋 `object` / `path` 类型值。
- **示例**：

```simtalk
EngineAssembly.ShiftCalendarObject := MyShiftCalendar
```

- **参见**：Select Shift Calendar

---

## StateBlocked [SimTalk]

将 `<Path>` 指定的 Frame 状态设为阻塞（`true`）或不阻塞（`false`）。

- **类型**：属性（Attribute）
- **语法**：`<Path>.StateBlocked:boolean`
- **赋值**：可赋 `boolean` 类型值。
- **示例**：

```simtalk
Frame.StateBlocked := true
```

- **参见**：States of the Frame、Blocked [state, material flow objects]

---

## StateEntryShut [SimTalk]

将 `<Path>` 指定的 Frame 状态设为入口关闭（`true`）或不关闭（`false`）。

- **备注**：Frame 仅在 **Recovery Time** 生效时才显示此状态。
- **类型**：属性（Attribute）
- **语法**：`<Path>.StateEntryShut:boolean`
- **赋值**：可赋 `boolean` 类型值。
- **示例**：

```simtalk
Frame.StateEntryShut := true
```

- **参见**：States of the Frame、Recovery Time [general description]

---

## StateResourceMissing [SimTalk]

将 `<Path>` 指定的 Frame 状态设为缺少资源/等待 Exporter（`true`）或不缺少（`false`）。

- **备注**：当 Frame 正在等待资源（即服务或 MU）时，适用“缺少资源/等待”状态。
- **类型**：属性（Attribute）
- **语法**：`<Path>.StateResourceMissing:boolean`
- **赋值**：可赋 `boolean` 类型值。
- **示例**：

```simtalk
Frame.StateResourceMissing := true
```

- **参见**：States of the Frame、Waiting [state, material flow objects]

---

## StateSetup [SimTalk]

将 `<Path>` 指定的 Frame 状态设为准备中（`true`）或不准备（`false`）。

- **类型**：属性（Attribute）
- **语法**：`<Path>.StateSetup:boolean`
- **赋值**：可赋 `boolean` 类型值。
- **示例**：

```simtalk
Frame.StateSetup := true
```

- **参见**：States of the Frame、Setting-Up [state, material flow objects]

---

## StateWorking [SimTalk]

将 `<Path>` 指定的 Frame 状态设为工作中（`true`）或不工作（`false`）。

- **语法**：`<Path>.StateWorking:boolean`
- **赋值**：可赋 `boolean` 类型值。
- **示例**：

```simtalk
Frame.StateWorking := true
```

- **参见**：States of the Frame、Working [state, material flow objects]

---

## Stopped [SimTalk] — Frame

停止（`true`）或不停止（`false`）`<Path>` 指定的 Frame。

- **类型**：属性（Attribute）
- **语法**：`<Path>.Stopped:boolean`
- **可监视（Watchable）**：该属性可被监视，可用 observer 检测状态是否发生变化。
- **赋值**：可赋 `boolean` 类型值。
- **示例**：

```simtalk
Frame.Stopped := true
```

- **参见**：States of the Frame、Stopped [state, material flow objects]

---

## Unplanned [SimTalk] — Frame

当当前时间超出分配给 Frame 的 ShiftCalendar 的任何班次时，将 `<Path>` 指定的 Frame 设为计划外（`true`）。

- **类型**：属性（Attribute）
- **语法**：`<Path>.Unplanned:boolean`
- **赋值**：可赋 `boolean` 类型值。指定 `false` 可将其设为计划内工作。
- **示例**：

```simtalk
EngineAssembly.Unplanned := false
```

- **参见**：States of the Frame、Unplanned [state, material flow objects]

---

## Interface

`attributes.md` 末尾提及 **Interface** 对象：用于在 Frame 之间建立转换（即从模型的一部分到另一部分），也有助于层次化建模。

---

## 相关概述（同级目录 README 摘要）

### ../general/README.md 摘要

`../general/README.md` 是对 `general.md` 的总结，介绍 Frame 的通用说明：

- **Frame 概述**：Frame 是创建仿真模型的容器对象，是层次化建模的主要对象。可用 **Interface** 实现 Frame 间转换，用 **Connector** 连接 Frame 内外对象。
- **添加到模型**：Home 功能区 → Manage Class Library > Basic Objects > MaterialFlow > Frame。
- **Frame 窗口**：包含 Frame 功能区选项卡与系统菜单；支持拖放建模操作。
- **功能区选项卡**：Find Object、Select Shift Calendar（`ShiftCalendarObject`）、Replacement Mode（`replace`/`ReplacementMode`）、Lock Structure（`LockStructure`）等。
- **替换模式**：Merge（合并，默认）与 Exchange（交换）；由替换方 Frame 决定。
- **Lock Structure**：锁定结构防止意外修改；新模型默认关闭，实例化 Frame 默认开启。
- **Frame 状态**：以彩色矩形显示，对应属性 `Failed`、`Stopped`、`Pause`、`Unplanned`、`StateWorking`、`StateBlocked`、`StateSetup`、`StateEntryShut`、`StateResourceMissing`。

### ../methods/README.md 摘要

`../methods/README.md` 是对 `methods.md` 的总结，介绍 Frame 提供的 4 个方法：

- **getHTMLCode** — 将 Frame 内容作为基于像素图形的 HTML 代码返回，语法 `<Path>.getHTMLCode(...) → string`。
- **node** — 返回 Frame 中指定编号或名称的对象，语法 `<Path>.node(ObjectNumberOrName:integer/string) → object`。
- **pasteClipboard** — 将剪贴板内容粘贴到 Frame，语法 `<Path>.pasteClipboard([TargetTable:table])`。
- **statistics** — 返回 Frame 中所有收集统计数据的物流对象的统计数据，语法 `<Path>.statistics` 等。

方法来源同样包括**所有对象的通用方法（Methods of All Objects）**。

### ../read-only-attributes/README.md 摘要

`../read-only-attributes/README.md` 是对 `read-only-attributes.md` 的总结，介绍 Frame 提供的 4 个只读属性：

- **Capacity** — 返回 Frame 中所有静态物流对象的容量，语法 `<Path>.Capacity → integer`（可监视）。
- **EventController** — 返回根 Frame 中的 EventController，语法 `EventController → object`。
- **NumberOfLimitedObjects** — 统计每个包含 EventController 的 Frame 中已插入对象的数量，语法 `NumberOfLimitedObjects → integer`。
- **NumNodes** — 返回 Frame 中的对象数量，语法 `<Path>.NumNodes → integer`（注意：本目录的 `attributes.md` 同样收录了 `NumNodes`）。

只读属性只能查询、不能设置；Plant Simulation 在查询时刻计算其值。只读属性来源同样包括**所有对象的只读属性（Read-Only Attributes of All Objects）**。

### ../window/README.md 摘要

`../window/README.md` 是对 `window.md` 的总结，介绍 Frame 窗口：包含 Frame 功能区选项卡与系统菜单、建模时的拖放操作、用户自定义功能区选项卡（`UserMenu`、`ShowUserMenu`、`UserMenuTitle`）、用户自定义右键菜单（`UserPopupMenu`、`ShowUserPopupMenu`）、替换模式、Lock Structure，以及 Frame 自身与选中对象的右键菜单命令。

## 目录说明

- `attributes.md`：Frame 属性说明的 Markdown 版本（本总结的源文件）。
- `attributes.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
