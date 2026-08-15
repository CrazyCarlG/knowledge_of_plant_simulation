# ShiftCalendar Methods（方法）说明总结

本目录汇总了 Plant Simulation 中 **ShiftCalendar（班次日历）** 对象的方法与只读属性相关文档，来源文件为 `methods.md`（及等价的 `methods.txtx` 纯文本导出）。本目录下暂无子文件夹及其中的 README.md。

## 一、概述

ShiftCalendar 对象提供：

- 左侧目录中所列的方法；
- 所有对象通用方法（Methods of All Objects）。

可通过 **Show Attributes and Methods** 窗口查看对象全部的方法、只读属性和属性：

- 在 Class Library 的类上右键选择 **Show Attributes and Methods**，查看所选类的方法、只读属性和属性；
- 在 Frame 中选中实例后，按 **F8** 或点击 Home 功能区中的 **Show Attributes and Methods**，查看所选实例的方法、只读属性和属性。

## 二、语法行约定（Syntax Line Conventions）

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所应用对象的路径。
- 括号内为方法签名，由参数标识符和数据类型组成，如 `(Parameter:string)` 表示 string 类型参数；除常量外，也可使用相应类型的变量或返回该类型的方法。
- 方括号内为可选参数，如 `[,Parameter:boolean]` 表示布尔参数可省略。
- 参数带默认值时，在参数后显示 `:= 默认值`，如上例的 `:= false`。
- 方法有返回值时，箭头 `→` 后为返回值数据类型，如上例的 `→ boolean`。

> **注意**：括号内的表达式必须正确输入括号 `(…)`，否则可能产生意外结果并打开调试器（Debugger）。

## 三、方法 / 只读属性

### 1. calculateWorkingDuration [SimTalk]

- **功能**：计算 `<Path>` 所指定 ShiftCalendar 在两点时间之间的**工作时间（Working Duration）**。
- **类型**：只读属性（Read-only attribute）。
- **说明**：计算时会考虑暂停（pauses）和班次（shifts）。
- **语法**：

```
<Path>.calculateWorkingDuration(StartTime:dateTime, EndTime:dateTime) → time
```

- **参数**：
  - `StartTime`（dateTime）：开始时间，ShiftCalendar 从该时刻起计算工作时间。
  - `EndTime`（dateTime）：结束时间，ShiftCalendar 计算到该时刻为止。
- **返回值**：`time` 类型。

### 2. schedule [SimTalk] - ShiftCalendar

- **功能**：为 `<Path>` 所指定的 ShiftCalendar 排定生产过程的开始或结束日期时间。
- **类型**：方法（Method）。
- **说明**：`schedule` 最多可排到未来 100 年。
- **语法**：

```
<Path>.schedule(StartTime:dateTime, Duration:time, Direction:string) → dateTime
```

- **参数**：
  - `StartTime`（dateTime）：ShiftCalendar 排定生产日期所依据的开始或结束日期时间。
  - `Duration`（time）：生产过程的持续时间。
  - `Direction`（string）：排定方向，即 ShiftCalendar 是向前还是向后计算时间。
    - **向前排程（forward scheduling）**：已知生产工单所需生产时间，从开始日期（通常为当前日期）起，计算产品必须完成的日期；计算时考虑生产时间、班次时间、周末和节假日。
    - **向后排程（backward scheduling）**：已知产品必须就绪的日期及生产时间，计算生产必须开始的日期；同样考虑生产时间、班次时间、周末和节假日。
- **返回值**：`dateTime` 类型。

## 四、只读属性（Read-Only Attributes）

ShiftCalendar 的只读属性：

- 左侧目录中所列的只读属性；
- 所有对象通用只读属性（Read-Only Attributes of All Objects）。

只读属性的值只能查询、不能设置，因为 Plant Simulation 会在查询时刻即时计算其值。多数情况下，只读属性对应对象某个选项卡上不可编辑的对话框项（例如 Statistics 选项卡）。

查看方式与第一节相同：通过 **Show Attributes and Methods** 窗口（类上右键，或实例按 F8 / 点击 Home 功能区按钮）。
