# TimeSequence（时间序列）— 方法

本目录（`methods`）包含 TimeSequence 对象的方法说明文档，主要内容来源于 `methods.md`（`methods.txtx` 为同一内容的原始提取文本，二者内容一致）。本 README 对这些内容进行总结。

## 概述

**TimeSequence** 提供以下方法：

- 列方法（Methods for Columns）
- 行方法（Methods for Rows）
- 访问 TimeSequence 的方法（Methods for Accessing the TimeSequence）
- 列表与表格的共享方法
- 所有对象的共享方法

打开 **Show Attributes and Methods** 窗口可查看对象的全部方法、只读属性与属性。

## Active 复选框

勾选 **Active** 复选框可记录 TimeSequence 的数值演变过程；取消勾选则不记录任何数值。

> **备注**：也可在 Frame 中右键 TimeSequence 对象，在上下文菜单中选择 **Activate** 进行激活，选择 **Deactivate** 取消激活。

## 方法语法说明

语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所作用对象的路径。
- 签名（标识符 + 参数数据类型）列在圆括号中。`(Parameter:string)` 表示数据类型为 `string` 的参数。除常量外，也可使用所需类型的变量或返回该类型的方法。
- 可选参数列在方括号内，例如 `[,Parameter:boolean]`。
- 默认值在参数之后显示。
- 若方法有返回值，其数据类型显示在箭头 `->` 之后。

> **注意**：务必为括号内的表达式输入圆括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。

### 签名中使用的缩写

| 参数数据类型 | 数据类型 | 取值范围 |
|---|---|---|
| integer | integer | 大于零的整数 |
| any | 所有数据类型 | 取决于数据类型 |
| listrange | — | 一个范围 |
| direction | string | `"up"`、`"down"`、`" "` |
| attributes | string | 属性名称 |

## 列方法（Methods for Columns）

TimeSequence 提供以下用于列格式的方法。这些设置也可在 **Format > Column** 中选择。在方法中，第一个参数始终指定列——列索引、列范围或列号。

| 方法 | 说明 | 语法 |
|---|---|---|
| `getAlignmentColumn` | 返回指定列的对齐方式 | `<Path>.getAlignmentColumn(Column:any) → string` |
| `getBackgroundColorColumn` | 返回指定列的背景颜色 | `<Path>.getBackgroundColorColumn(Column:any) → integer` |
| `getColumnWidth` | 返回指定列的宽度 | `<Path>.getColumnWidth(Column:any) → integer` |
| `getEditorRightsColumn` | 返回指定列的编辑权限（`true` 只读，`false` 可读写） | `<Path>.getEditorRightsColumn(Column:any) → boolean` |
| `getFontColorColumn` | 返回指定列的字体颜色 | `<Path>.getFontColorColumn(Column:any) → integer` |
| `getFontSizeColumn` | 返回指定列的字体大小（1=小、2=中、3=大、4=特大） | `<Path>.getFontSizeColumn(Column:any) → integer` |
| `getFormatString` | 返回列的格式字符串 | `<Path>.getFormatString(Column:any) → string` |
| `getVisibility` | 返回某列是否可见（`true`）或隐藏（`false`） | `<Path>.getVisibility(Column:any) → boolean` |
| `isAlignmentColumn` | 判断指定列的对齐方式是否与给定值一致 | `<Path>.isAlignmentColumn(Column:any, Alignment:string) → boolean` |
| `setAlignmentColumn` | 设置指定列的对齐方式（`"Left"`、`"Right"`、`"Centered"`） | `<Path>.setAlignmentColumn(Column:any[, Column:any,...], Alignment:string)` |
| `setBackgroundColorColumn` | 设置指定列的背景颜色 | `<Path>.setBackgroundColorColumn(Column:any[, Column:any,...], BackgroundColor:integer)` |
| `setColumnWidth` | 设置指定列的宽度（以非比例字体字符宽度计） | `<Path>.setColumnWidth(Column:any, ..., ColumnWidth:integer)` |
| `setEditorRightsColumn` | 设置指定列的编辑权限（`true` 只读，`false` 可读写） | `<Path>.setEditorRightsColumn(Column:any, ..., ReadOnly:boolean)` |
| `setFontColorColumn` | 设置指定列的字体颜色 | `<Path>.setFontColorColumn(Column:any, ..., FontColor:integer)` |
| `setFontsizeColumn` | 设置指定列的字体大小（1=小、2=中、3=大、4=特大） | `<Path>.setFontsizeColumn(Column:any, ..., FontSize:integer)` |
| `setFormatString` | 设置指定列的格式字符串（取决于数据类型） | `<Path>.setFormatString(Column:any, ..., FormatString:string)` |
| `setVisibility` | 显示或隐藏指定列（`true` 显示，`false` 隐藏） | `<Path>.setVisibility(Column:any, ..., Visible:boolean)` |

颜色常量：`1` = 黑，`2` = 红，`3` = 绿，`4` = 蓝，`5` = 品红，`6` = 黄，`7` = 青。可用 `makeRGBValue` 设置 RGB 颜色值。

## 行方法（Methods for Rows）

TimeSequence 提供以下用于行格式的方法。这些设置也可在 TimeSequence 的 **Format > Row** 中选择。

| 方法 | 说明 | 语法 |
|---|---|---|
| `getAlignmentRow` | 返回指定行的对齐方式 | `<Path>.getAlignmentRow(Row:any) → string` |
| `getBackgroundColorRow` | 返回指定行的背景颜色 | `<Path>.getBackgroundColorRow(Row:any) → integer` |
| `getEditorRightsRow` | 返回指定行的编辑权限（`true` 只读，`false` 可读写） | `<Path>.getEditorRightsRow(Row:any) → boolean` |
| `getFontColorRow` | 返回指定行的字体颜色 | `<Path>.getFontColorRow(Row:any) → integer` |
| `getFontSizeRow` | 返回指定行的字体大小（1=小、2=中、3=大、4=特大） | `<Path>.getFontSizeRow(Row:any) → integer` |
| `isAlignmentRow` | 判断指定行的对齐方式是否与给定值一致 | `<Path>.isAlignmentRow(Row:any, Alignment:string) → boolean` |
| `setAlignmentRow` | 设置指定行的对齐方式（`"Left"`、`"Right"`、`"Centered"`） | `<Path>.setAlignmentRow(Row:any[, Row:any,...], Alignment:string)` |
| `setBackgroundColorRow` | 设置指定行的背景颜色 | `<Path>.setBackgroundColorRow(Row:any[, Row:any,...], BackgroundColor:integer)` |
| `setEditorRightsRow` | 设置指定行的编辑权限（`true` 只读，`false` 可读写） | `<Path>.setEditorRightsRow(Row:any[, Row:any,...], ReadOnly:boolean)` |
| `setFontColorRow` | 设置指定行的字体颜色 | `<Path>.setFontColorRow(Row:any[, Row:any,...], FontColor:integer)` |
| `setFontSizeRow` | 设置指定行的字体大小（1=小、2=中、3=大、4=特大） | `<Path>.setFontSizeRow(Row:any[, Row:any,...], FontSize:integer)` |

颜色常量与列方法一致：`1` = 黑，`2` = 红，`3` = 绿，`4` = 蓝，`5` = 品红，`6` = 黄，`7` = 青。可用 `makeRGBValue` 设置 RGB 颜色值。

## 访问 TimeSequence 的方法（Methods for Accessing the TimeSequence）

TimeSequence 提供以下用于访问其数据的方法。

### `[ , ]` — 读取单元格内容

按列和行索引随机访问单元格内容。

- **语法**：`<Path>[Column:integer, Row:integer] → 单元格内容`
- **备注**：索引语句以方括号开始和结束，内部先输入列，再输入行。返回值的类型与表格单元格相同。Plant Simulation 只读取单元格内容，不删除内容。
- **返回值**：单元格内容；若单元格为空则返回 `VOID`。
- **示例**：
  ```
  print timeSequence[1,2]
  print timeSequence["Value",2]
  ```

### `[ , ]` — 写入单元格内容

将数据写入指定单元格。

- **语法**：`<Path>[Column:integer, Row:integer]`
- **备注**：先通过索引访问单元格，再为其赋值。新值的数据类型必须与表格单元格匹配。
- **示例**：
  ```
  timeSequence[2,3] := 12.34
  ```

### add

将一个数值加到值列的所有条目上，或合并两个 TimeSequence 对象的时间列与值列。

- **语法**：`<Path>.add(ValueToBeAdded:any)`
- **参数**：若 `ValueToBeAdded` 为数值，则将其加到值列的每个条目上（时间列不变）。若为另一个 TimeSequence，则按区间将时间/值对相加；时间列决定区间范围。同一时间值的多个条目成对合并，若数量不同，则相加前复制最后一个条目。
- **示例**：
  ```
  MyTimeSequence.add(5)
  shiftA.add(shiftB)
  ```

### and — 运算符

对数据类型为 `boolean` 的 TimeSequence 执行布尔 `and` 运算。

- **语法**：`<Path>.and(Operand:any)`
- **备注**：可用单个布尔参数或另一个 TimeSequence 执行运算。使用另一个 TimeSequence 时，结果时间列为两个时间列的并集。
- **示例**：
  ```
  failureA.and(failureB)
  MyTimeSequence.and(false)
  ```

### deleteInterval

删除指定时间区间内的所有值。

- **语法**：`<Path>.deleteInterval([BeginningOfInterval:time, EndOfInterval:time])`
- **参数**：`BeginningOfInterval`（time，可选）：区间起点；`EndOfInterval`（time，可选）：区间终点。
- **备注**：与边界之一匹配的条目也会被删除。
- **示例**：
  ```
  resultList.deleteInterval(0,3600)
  ```

### divide

将值列的所有条目除以一个数值，或除以另一个 TimeSequence。

- **语法**：`<Path>.divide(Divisor:any)`
- **备注**：使用另一个 TimeSequence 时，结果时间列为两个时间列的组合，值列包含各时间点处的商。
- **注意**：所有除数必须非零。
- **示例**：
  ```
  MyTimeSequence.divide(5)
  numEntities.divide(current.NumMU)
  ```

### include

将指定 TimeSequence 的所有条目插入到 `<Path>` 中。

- **语法**：`<Path>.include(TimeSequence:object)`
- **备注**：可能产生具有相同时间值的多个条目，这些条目之间的相对顺序不确定。数据类型必须相同或兼容。
- **示例**：
  ```
  timeSequence1.include(timeSequence2)
  ```

### insert

向 TimeSequence 中插入一个时间/值对。

- **语法**：`<Path>.insert(GivenTime:any, Value:any)`
- **参数**：
  - `GivenTime`（any）：时间。若时间参考为 **Absolute（绝对）**，则数据类型为 `dateTime`；否则为 `time`。
  - `Value`（any）：数值，须与 TimeSequence 的数据类型相同或兼容。
- **示例**：
  ```
  MyTimeSequence.insert(eventcontroller.simtime,3)
  MyTimeSequence.insert(sysdate,3)
  ```

### multiply

将值列的所有条目乘以一个数值，或与另一个 TimeSequence 相乘。

- **语法**：`<Path>.multiply(Factor:any)`
- **备注**：使用另一个 TimeSequence 时，时间列为两个时间列的并集，值列包含各时间点处的乘积。
- **示例**：
  ```
  MyTimeSequence.multiply(5)
  dimx.multiply(dimy)
  ```

### not

对值列中的所有值执行布尔 NOT 运算。

- **语法**：`<Path>.not`
- **示例**：
  ```
  MyTimeSequence.not // 反转所有输入
  ```

### or — 运算符

对数据类型为 `boolean` 的 TimeSequence 执行布尔 `or` 运算。

- **语法**：`<Path>.or(Operand:any)`
- **备注**：可用单个布尔参数或另一个 TimeSequence 执行运算。使用另一个 TimeSequence 时，结果时间列为两个时间列的并集。
- **示例**：
  ```
  workerA.or(workerB)
  MyTimeSequence.or(true)
  ```

### repeat

删除所有条目，并用另一个 TimeSequence 数据子范围的副本替换。

- **语法**：`<Path>.repeat(TimeSequence:object, Subrange:time, NumberOfCopies:real)`
- **参数**：
  - `TimeSequence`（object）：要粘贴其子范围的 TimeSequence。
  - `Subrange`（time）：从时间零点开始，到该时间结束。
  - `NumberOfCopies`（real）：要插入的副本数量（例如，将一天的排班重复五次以创建一周的排班）。
- **示例**：
  ```
  LengthOfDay := str_to_time("1:00:00:00.00")
  weekPlan.repeat(dayPlan,lengthOfDay,5)
  ```

### repeatTo

删除所有条目，并用指定 TimeSequence 的子范围副本替换，填充目标范围。

- **语法**：`<Path>.repeatTo(TimeSequence:object, Subrange:time, RangeToBeFilled:time)`
- **参数**：
  - `TimeSequence`（object）：其数据替换现有数据的 TimeSequence。
  - `Subrange`（time）：从时间零点开始，到该时间结束。
  - `RangeToBeFilled`（time）：`<Path>` 中要用子范围副本填充的范围。必须大于子范围，否则保持为空。
- **示例**：
  ```
  weekPeriod := str_to_time("5:00:00:00.00")
  dayPeriod := str_to_time("1:00:00:00.00")
  weekPlan.repeatTo(dayPlan,weekPeriod,dayPeriod)
  ```

### subtract

从值列的所有条目中减去一个数值，或减去另一个 TimeSequence 的时间/值对。

- **语法**：
  ```
  <Path>.subtract(ValueToBeSubtracted:integer)
  <Path>.subtract(ValueToBeSubtracted:real)
  <Path>.subtract(ValueToBeSubtracted:object)
  ```
- **参数**：
  - 数值（`integer`/`real`）：从值列的每个条目中减去（时间列不变）。
  - 另一个 TimeSequence（`object`）：按区间减去时间/值对；多个条目成对合并，若数量不同，则相减前复制最后一个条目。
- **示例**：
  ```
  MyTimeSequence.subtract(5)
  stock.subtract(missingEntities)
  ```

### value

返回 TimeSequence 在给定时间点处的值。

- **语法**：`<Path>.value(GivenTime:time) -> any`
- **备注**：若多个条目具有相同的时间，则返回序号最大的条目。
- **参数**：`GivenTime`（time）：时间。
- **示例**：
  ```
  print ts1.value(1.5)+ts2.value(1.5)
  ```

## 只读属性（Read-Only Attributes）

TimeSequence 提供列表与表格以及所有对象的只读属性。可以查询只读属性值但不能设置它们——Plant Simulation 在查询时计算该值。

查询示例：

```
print MyTimeSequence.Full
```

## 属性（Attributes）

TimeSequence 提供目录中列出的属性，以及列表与表格的属性和所有对象的属性。

---

*来源：Plant Simulation Help（TimeSequence 方法）。未发表作品。© 2026 Siemens。*
