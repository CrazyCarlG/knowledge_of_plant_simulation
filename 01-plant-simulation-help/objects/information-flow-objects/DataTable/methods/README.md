# DataTable 对象 — Methods（方法）

本目录包含 **DataTable 对象**（信息流对象）的方法说明。文档描述的是 DataTable 对象本身，即 Plant Simulation 中用于以行列结构（表格）存储数据、可通过索引访问单元格的对象，以及通过 SimTalk 方法对其列、行、单元格进行操作和读写访问的方式。

> 源文件：`methods.md`（内容详见该文件）；原始导出文本：`methods.txtx`。

## 概述

DataTable 提供以下方法分组：

- Methods of Columns of the DataTable（DataTable 列的方法）
- Methods of Rows of the DataTable（DataTable 行的方法）
- Miscellaneous Methods of the DataTable（DataTable 的杂项方法）
- Methods for Accessing the DataTable（访问 DataTable 的方法）
- Methods for Instantiating the DataTable（实例化 DataTable 的方法）
- 列表和表格的共享方法（*The shared Methods of Lists and Tables*）
- 所有对象的共享方法（*The shared Methods of All Objects*）

要查看对象的所有方法、只读属性和属性，打开窗口 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法和属性。
- 按 `F8` 键，或点击包含该实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法和属性。

## 语法约定

一个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所作用对象的路径。
- 签名（参数的标识符和数据类型）写在括号中，如 `(Parameter:string)` 表示 `string` 类型的参数。
- 可选参数写在方括号内，如 `[,Parameter:boolean]`。
- 参数有默认值时，签名会在参数后面显示默认值。
- 方法有返回值时，签名在箭头 `->` 后面显示返回值的数据类型。
- 对于括号内的表达式务必输入括号，否则可能出现意外结果并打开调试器（Debugger）。

签名中使用的缩写：

| 参数 | 数据类型 | 取值范围 |
|---|---|---|
| integer | integer | 大于零的整数 |
| any | 所有数据类型 | 取决于数据类型 |
| listrange | — | 一个范围 |
| direction | string | `"up"`、`"down"`、`" "` |
| attributes | string | 属性名 |

## Methods of Columns of the DataTable（列的方法）

这些方法的第一个参数用于指定列（列索引、列范围或列号）。

| 方法 | 说明 |
|---|---|
| `cutColumn` | 剪切指定列及其全部数据；索引相等或更大的列向左移动。不能用 `cutColumn(0)` 剪切列索引。 |
| `getAlignmentColumn` | 返回指定列的对齐方式（`"Left"`、`"Right"` 或 `"Centered"`）。 |
| `getBackgroundColorColumn` | 返回指定列的背景色。 |
| `getColumnNo` | 查找包含用户自定义列索引的列；仅适用于简单数据类型（如 string、integer 等）。返回列号，不存在则返回 `-1`。 |
| `getColumnUniqueValues` | 返回指定列中只出现一次的值组成的数组；列需为 String、Integer、Real、Time、Money、Length、Weight、Speed、Acceleration、Date 或 DateTime 类型。 |
| `getColumnWidth` | 返回指定列的宽度。 |
| `getColumnYDim` | 返回指定列最后一个有内容的单元格的编号；列为空时返回 `0`。 |
| `getCommonFormat` | 返回指定列的 Common Format（通用格式）是否开启（`true`/`false`）。 |
| `getDataType` | 返回指定列的数据类型。 |
| `getEditorRightsColumn` | 返回指定列的编辑权限（`true` 为只读，`false` 为可读写）。 |
| `getFontColorColumn` | 返回指定列的字体颜色。 |
| `getFontSizeColumn` | 返回指定列的字体大小（`1`=Small，`2`=Medium，`3`=Large，`4`=Extra Large）。 |
| `getFormatString` | 返回指定列的格式字符串。 |
| `getVisibility` | 返回指定列是否可见（`true`）或隐藏（`false`）。 |
| `insertColumn` | 在指定列左侧插入一个空列；索引相等或更大的列向右移动一位。 |
| `isAlignmentColumn` | 判断指定列的对齐方式是否与给定值一致。对齐值可为 `"Right"`、`"Left"` 或 `"Center"`。 |
| `setAlignmentColumn` | 设置一列或多列的对齐方式；对齐值可为 `"Left"`、`"Right"` 或 `"Centered"`。 |
| `setBackgroundColorColumn` | 设置一列或多列的背景色；颜色码 `1`..`7`（Black/Red/Green/Blue/Magenta/Yellow/Cyan），或使用 `makeRGBValue` 设置 RGB 值。 |
| `setColumnWidth` | 设置一列或多列的宽度（以非比例字体的字符宽度为单位）。 |
| `setCommonFormat` | 为指定范围内的所有列分配相同格式。列开启 Common Format 后，给表格单元格赋子表会创建副本，否则会写入引用。 |
| `setDataType` | 设置指定一列或多列的数据类型。 |
| `setDataTypeDefault` | 将指定一列或多列的数据类型重置为表格的默认数据类型。 |
| `setEditorRightsColumn` | 设置指定一列或多列的编辑权限（`ReadOnly=true` 只读，`false` 可读写）。 |
| `setFontColorColumn` | 设置指定一列或多列的字体颜色；颜色码同背景色，或使用 `makeRGBValue`。 |
| `setFontsizeColumn` | 设置指定一列或多列的字体大小（`1`..`4`）。 |
| `setFormatString` | 根据数据类型设置指定一列或多列的格式字符串。 |
| `setVisibility` | 显示（`true`）或隐藏（`false`）指定的一列或多列。 |

## Methods of Rows of the DataTable（行的方法）

| 方法 | 说明 |
|---|---|
| `appendRow` | 添加新行并把传入的值写入各列；有行索引时第一个值写入行索引。返回追加行的索引。 |
| `cutEmptyRows` | 剪切 DataTable 中的所有空行。 |
| `cutRow` | 剪切指定行及其全部数据；不能用 `cutRow(0)` 剪切行索引。 |
| `getAlignmentRow` | 返回指定行的对齐方式。 |
| `getBackgroundColorRow` | 返回指定行的背景色。 |
| `getEditorRightsRow` | 返回指定行的编辑权限（`true` 只读，`false` 可读写）。 |
| `getFontColorRow` | 返回指定行的字体颜色。 |
| `getFontSizeRow` | 返回指定行的字体大小（`1`..`4`）。 |
| `getRowNo` | 查找包含用户自定义行索引的行；仅适用于简单数据类型。返回行号，不存在则返回 `-1`。 |
| `insertRow` | 在指定行上方插入空行，原单元格下移一位。 |
| `isAlignmentRow` | 判断指定行的对齐方式是否与给定值一致。 |
| `setAlignmentRow` | 设置一行或多行的对齐方式（`"Left"`、`"Right"` 或 `"Centered"`）。 |
| `setBackgroundColorRow` | 设置一行或多行的背景色；颜色码 `1`..`7`，或使用 `makeRGBValue`。 |
| `setEditorRightsRow` | 设置一行或多行的编辑权限（`ReadOnly=true` 只读，`false` 可读写）。 |
| `setFontColorRow` | 设置一行或多行的字体颜色。 |
| `setFontSizeRow` | 设置一行或多行的字体大小（`1`..`4`）。 |

## Miscellaneous Methods of the DataTable（杂项方法）

| 方法 | 说明 |
|---|---|
| `calculateList` | 重新计算公式并在相应单元格中显示当前值。 |
| `copyFilteredTableTo` | 将源表中满足条件（Condition 返回 `true`）的所有行复制到目标表。匿名标识符 `@` 引用 DataTable，`ySelf` 为待复制行的行号；也会复制列索引（若已定义）。 |
| `copyRangeTo` | 将源表的指定范围复制到目标表。行为取决于是否激活 *Column Index Belongs to Contents*（列索引是否属于内容）。 |
| `determineRange` | 解析实际列表范围，并把其边界赋给局部变量（StartColumn/StartRow/EndColumn/EndRow）。 |
| `getCommonFormatData` | 获取已激活 Common Format 的 list/table 类型列的格式数据并写入目标表/列表；未指定列时使用第一列。 |
| `getFormula` | 返回指定单元格中的公式。 |
| `initialize` | 用指定值初始化指定范围内的单元格，覆盖已有数据；若范围包含索引和内容，则只初始化内容。 |
| `mergeTable` | 将源表的列复制到目标表，依据行索引正确匹配行（两张表都必须有行索引）。 |
| `setCommonFormatData` | 为已激活 Common Format 的 list/table 类型列中的子表设置通用格式数据；适用于 DataTable 和 TimeSequence。 |
| `setCursor` | 将内部游标（`CursorX`/`CursorY`）设置到指定单元格；设置成功返回 `true`。 |
| `setFormula` | 在指定范围的单元格中输入公式。 |

## Methods for Accessing the DataTable（访问 DataTable 的方法）

| 方法 | 说明 |
|---|---|
| `[ , ]` — 读单元格 | 返回指定单元格的数据。空单元格返回零值：数值类型为 `0`，Boolean 为 `false`，字符串为 `""`，object/table/list/stack/queue 为 `void`。读取不会移除内容。 |
| `[ , ]` — 写单元格 | 通过索引（系统索引或用户自定义索引）访问单元格并赋值；新值的数据类型必须与单元格一致。 |
| `deleteContents` | 删除 DataTable 的内容（包括行索引；若激活 *Column Index Belongs to Contents* 也删除列索引）。 |
| `writeRow` | 在指定位置写入数据，替换这些单元格中的任何数据。 |

## Methods for Instantiating the DataTable（实例化 DataTable 的方法）

`table` 类型的局部变量本身不包含数据，只是对数据结构的引用；在 Method 对象中初始为 `void`，访问数据前必须先创建。

| 方法 | 说明 |
|---|---|
| `create` | 在局部变量中创建不含内容的数据结构；仅适用于 `table` 类型的局部变量。 |
| `createNestedList` | 在指定单元格中创建嵌套列表；列数据类型须为 list、stack、queue 或 table。返回创建的嵌套列表（DataList、DataQueue、DataStack 或 DataTable）。 |

## Read-Only Attributes of the DataTable（只读属性）

DataTable 提供只读属性（包括列表和表格的只读属性、所有对象的只读属性）。只能查询其值，不能设置；Plant Simulation 在查询时计算该值。示例：

```simtalk
print MyDataTable.Full
```
