# ShiftCalendar Read-Only Attributes（只读属性）说明总结

本目录汇总了 Plant Simulation 中 **ShiftCalendar（班次日历）** 对象的只读属性（Read-Only Attributes）相关文档，来源文件为 `read-only-attributes.md`（及等价的 `read-only-attributes.txtx` 纯文本导出）。本目录下暂无子文件夹及其中的 README.md。

## 一、概述

ShiftCalendar 对象提供：

- 左侧目录中所列的只读属性；
- 所有对象通用只读属性（Read-Only Attributes of All Objects）。

只读属性的值只能查询、不能设置，因为 Plant Simulation 会在查询时刻即时计算其值。多数情况下，只读属性对应对象某个选项卡上不可编辑的对话框项（例如 **Statistics** 选项卡）。

可通过 **Show Attributes and Methods** 窗口查看对象全部的方法、只读属性和属性：

- 在 Class Library 的类上右键选择 **Show Attributes and Methods**，查看所选类的方法、只读属性和属性；
- 在 Frame 中选中实例后，按 **F8** 或点击 Home 功能区中的 **Show Attributes and Methods**，查看所选实例的方法、只读属性和属性。

查询某个只读属性值的示例：

```
print MyShiftCalendar.Unplanned
```

## 二、只读属性

### 1. GetCurrShift [SimTalk]

- **功能**：返回 `<Path>` 所指定的 ShiftCalendar 当前处于活动状态的班次（shift）名称。
- **类型**：只读属性（Read-only attribute）。
- **备注**：该名称为你在 **Tab Shift Times** 的 **Shift** 列中输入的班次名称。
- **语法**：

```
<Path>.GetCurrShift → string
```

- **可监视（Watchable）**：该只读属性可监视。
- **返回值**：`string` 类型。
- **示例**：

```
shift := root.MyShiftCalendar.GetCurrShift
```

- **参见**：Tab Shift Times、Shift [ShiftCalendar]、GetCurrShift [SimTalk]。

### 2. Pause [SimTalk] - ShiftCalendar

- **功能**：返回 `<Path>` 所指定的 ShiftCalendar 是否处于暂停状态（`true`）或未暂停（`false`）。
- **类型**：只读属性（Read-only attribute）。
- **语法**：

```
<Path>.Pause → boolean
```

- **可监视（Watchable）**：该只读属性可监视。
- **返回值**：`boolean` 类型。
- **示例**：

```
print MyShiftCalendar.Pause
```

- **参见**：Paused [state, material flow objects]、Pause [SimTalk] - ShiftCalendar。

### 3. Unplanned [SimTalk] - ShiftCalendar

- **功能**：返回 `<Path>` 所指定的 ShiftCalendar 是否处于非计划（unplanned）状态（`true`）或否（`false`）。
- **类型**：只读属性（Read-only attribute）。
- **语法**：

```
<Path>.Unplanned → boolean
```

- **可监视（Watchable）**：该只读属性可监视。
- **返回值**：`boolean` 类型。
- **示例**：

```
print MyShiftCalendar.Unplanned
```

- **参见**：Unplanned [state, material flow objects]、Attributes of the ShiftCalendar。

## 三、小结

ShiftCalendar 的只读属性共 3 项：

| 只读属性 | 返回值类型 | 说明 |
| --- | --- | --- |
| `GetCurrShift` | `string` | 返回当前活动班次的名称 |
| `Pause` | `boolean` | 返回班次日历是否暂停 |
| `Unplanned` | `boolean` | 返回班次日历是否处于非计划状态 |

三者均为可监视（watchable）的只读属性，只能查询、不能赋值。
