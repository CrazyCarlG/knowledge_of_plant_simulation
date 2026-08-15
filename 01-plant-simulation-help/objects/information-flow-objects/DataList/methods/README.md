# DataList 对象 — Methods（方法）

本目录包含 **DataList 对象**（信息流对象）的方法（Methods）说明。文档描述的是 DataList 对象本身，即 Plant Simulation 中用于以单列列表存储数据、可通过行号随机访问单元格的对象，以及通过 SimTalk 方法对其单元格进行读取、写入、追加、移除等操作的方式。

> 源文件：`methods.md`（内容详见该文件）；原始导出文本：`methods.txtx`。

## 概述

DataList 提供以下方法分组：

- 目录表（左侧）中列出的本对象方法（见下方各方法说明）
- 列表和表格的共享方法（*The Methods of Lists and Tables*）
- 所有对象的共享方法（*The Methods of All Objects*）

要查看对象的所有方法、只读属性和属性，打开窗口 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法和属性。
- 按 `F8` 键，或点击包含该实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法和属性。

## 语法约定

一个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所作用对象的路径。
- 签名（参数的标识符和数据类型）写在括号中，如 `(Parameter:string)` 表示 `string` 类型的参数。除常量值外，也可使用所需类型的变量或返回所需数据类型的方法。
- 可选参数写在方括号内，如 `[,Parameter:boolean]`。
- 参数有默认值时，签名会在参数后面显示默认值。
- 方法有返回值时，签名在箭头 `->` 后面显示返回值的数据类型。
- 对括号内的表达式务必输入括号 `(…)`，否则可能出现意外结果并打开调试器（Debugger）。

签名中使用的缩写：

| 参数 | 数据类型 | 取值范围 |
|---|---|---|
| integer | integer | 大于零的整数 |
| any | 所有数据类型 | 取决于数据类型 |
| listrange | — | 一个范围 |
| any, ..., any | 任意数据类型 | 一个单元格范围 |

## 方法列表

| 方法 | 说明 |
|---|---|
| `[row]` | 返回 `<Path>` 指定 DataList 中指定行的值；也可为该行单元格赋新值。 |
| `append` | 将指定条目追加到 DataList 末尾。 |
| `appendList` | 将指定列表所有单元格的内容追加到 DataList 末尾，现有单元格内容保持不变。 |
| `createNestedList` | 在 DataList 中创建包含列表和表格的嵌套列表。 |
| `determineRange` | 解析 DataList 的实际列表范围，并把边界赋给指定的局部变量。 |
| `remove` | 移除指定单元格的内容并返回该值，其后单元格上移一位。 |

---

## [row] [SimTalk]

返回 `<Path>` 指定 DataList 中指定行的值。

- **备注：**
  - 也可以为该行的单元格赋一个新值。
  - 在 **SimTalk 2.0** 中用方括号运算符读取 DataList 单元格时，Plant Simulation 读取该单元格内容，但会将其保留在 DataStack、DataQueue 和 DataList 中；赋值时新值会直接覆盖现有单元格内容，此时 DataList 的行为与只有一列的 DataTable 相同。
  - 在 **SimTalk 1.0** 中用方括号运算符读取 DataList 单元格时，Plant Simulation 读取并移除该单元格内容，其余单元格上移一位；赋值时新值会插入该单元格，现有单元格下移一位。
- **类型：** 方法（Method）

**语法：**

```simtalk
<Path>[Row:integer]
```

**参数：** `Row`（数据类型 `integer`）指定单元格的位置。

**示例：**

```simtalk
print DataList[2]  // 打印第 2 行的内容
DataList[2] := 42  // 用值 42 覆盖第 2 行的单元格
```

---

## append [SimTalk] - DataList

将指定条目追加到 `<Path>` 指定 DataList 的末尾。

- **备注：** Plant Simulation 不允许超过所设置的行数。
- **类型：** 方法（Method）

**语法：**

```simtalk
<Path>.append(Entry:any)
```

**参数：** `Entry`（数据类型 `any`）指定要追加的条目。

**示例：**

```simtalk
MyDataList.append("crankshaft")
```

**参见：** Number of Rows [lists]

---

## appendList [SimTalk]

将指定列表所有单元格的内容添加到 `<Path>` 指定 DataList 的末尾。

- **备注：** 现有单元格的内容保持不变。
- **类型：** 方法（Method）

**语法：**

```simtalk
<Path>.appendList(List:any)
```

**参数：** `List`（数据类型 `any`）指定要追加的列表。

**示例：**

假设我们的 DataStack 如下：

```simtalk
var l: list[string]
l.create
l.insert(1,"one")
l.insert(2,"two")
MyDataList.appendList(l)
MyDataList.appendList(DataStack)
```

MyDataList 的内容随之变为相应追加后的结果。

---

## createNestedList [SimTalk] - DataList

在 `<Path>` 指定 DataList 中创建一个嵌套列表（包含列表和表格）。

- **备注：**
  - DataList 的数据类型须为 list、stack、queue 或 table。
  - Plant Simulation 会覆盖现有子列表，而不会将现有列表下移一行。
  - 数据类型为 `list` 的局部变量处理方式不同：它们本身不包含数据，只保存对相应数据结构的引用。进入 Method 对象时，此类变量尚未引用任何数据结构（`void`），只有创建嵌套列表后才能访问数据。
- **类型：** 方法（Method）

**语法：**

```simtalk
<Path>.createNestedList([Row:integer, Name:string]) → list
```

**参数：**

- 可选参数 `Row`（数据类型 `integer`）指定单元格的行。若未指定行，Plant Simulation 会把列表添加到 DataList 末尾。
- 可选参数 `Name`（数据类型 `string`）指定要创建的嵌套列表的名称。

**返回值：** 数据类型为 `list`，即所创建的嵌套列表（DataList、DataQueue、DataStack 或 DataTable）。

**示例：**

```simtalk
MyDataList.createNestedList(1,"MyNestedlist")
```

**参见：**

- setCommonFormat [SimTalk]
- getCommonFormat [SimTalk]
- setCommonFormatData [SimTalk] - lists
- getCommonFormatData [SimTalk] - lists
- Activating and Deactivating Common Format
- Creating Lists within Lists and Tables
- createNestedList [SimTalk] - DataQueue
- createNestedList [SimTalk] - DataTable
- createNestedList [SimTalk] - local variable

---

## determineRange [SimTalk] - DataList

解析 `<Path>` 指定 DataList 的实际列表范围。

- **类型：** 方法（Method）

**语法：**

```simtalk
<Path>.determineRange(Range:listrange, byRef StartColumn:integer, byRef StartRow:integer, byRef EndStartColumn:integer, byRef EndRow:integer)
```

**参数：** 该方法会把列表范围的边界赋给所指定的局部变量：

- `Range`（数据类型 `listrange`）指定列表的范围。
- 局部变量 `StartColumn`（数据类型 `integer`）指定范围的第一列编号。
- 局部变量 `StartRow`（数据类型 `integer`）指定范围的第一行编号。
- 局部变量 `EndStartColumn`（数据类型 `integer`）指定范围的最后一列编号。
- 局部变量 `EndRow`（数据类型 `integer`）指定范围的最后一行编号。

**示例：**

```simtalk
param a: any
var fromX, fromY, toX, toY: integer
if isListRange(a)
   myDataList.determineRange(a, fromX, fromY, toX, toY)
   print "{",fromY,"}..{",toY,"}"
end
// 可以这样调用该方法：
myMethod({*})
myMethod({1}..{*})
// 使用用户自定义行索引的范围
myMethod({#7}..{*})
```

**参见：**

- Specifying a Range of Cells [several columns] > Column index belongs to contents
- Specifying a Range of Cells [several columns] > Column index does not belong to contents

---

## remove [SimTalk] - DataList

移除 `<Path>` 指定 DataList 中某个单元格的内容并返回该值。

- **备注：** DataList 会把所有索引大于指定索引的单元格上移一位。
- **类型：** 方法（Method）

**语法：**

```simtalk
<Path>.remove(Row:integer) → any
```

**参数：** `Row`（数据类型 `integer`）指定单元格的位置。

**返回值：** 数据类型为 `any`，与 DataList 的数据类型一致。

**示例：**

```simtalk
value := MyDataList.remove(2)
```

**参见：**

- cutRow [SimTalk] - DataTable
- Remove Row [context menu, lists]

---

## Read-Only Attributes of the DataList（只读属性）

DataList 提供：

- 列表和表格的只读属性（*The Read-Only Attributes of Lists and Tables*）
- 所有对象的只读属性（*The Read-Only Attributes of All Objects*）

可以查询只读属性的值，但不能设置，因为 Plant Simulation 会在查询的时间点计算该值。在大多数情况下，只读属性对应于对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。

要查询某个只读属性的值，例如可输入：

```simtalk
print MyDataList.Full
```

## Attributes of the DataList（属性）

DataList 提供：

- 列表和表格的属性（*The Attributes of Lists and Tables*）
- 所有对象的属性（*The Attributes of All Objects*）

要查看对象的所有方法、只读属性和属性，打开窗口 **Show Attributes and Methods**。
