# Source Methods（Source 对象方法）

本目录汇总了 Plant Simulation 中 **Source（源）** 对象提供的方法与只读属性，内容来源于 `methods.md`。

## 概述

Source 对象提供以下方法：

- 本目录（`methods.md`）中所列的方法。
- Material Flow Objects（物流对象）的方法。
- All Objects（所有对象）的方法。

要查看对象的全部方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口（在 Class Library 中右键选择，或选中实例后按 **F8** / 在 Home 功能区点击 **Show Attributes and Methods**）。

## 语法行说明（Syntax line）

方法的语法行格式示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所作用对象的路径。
- `(Parameter:string)`：参数签名，包含参数标识符与数据类型；可用同类型变量或返回该类型的方法替代常量。
- `[,Parameter:boolean]`：方括号内为可选参数。
- `:= false`：参数的默认值。
- `→ boolean`：箭头后为返回值的数据类型。

## 方法一览

| 方法 | 语法 | 返回类型 | 说明 |
| --- | --- | --- | --- |
| `creationTable` | `<Path>.creationTable(CreationTable:table)` | — | 将 Source 的 Creation Table（创建表）写入一个表。 |
| `getCurrentOrderTableRow` | `<Path>.getCurrentOrderTableRow -> integer` | `integer` | 返回 Source 当前按哪个表行生产零件。 |
| `orderParts` | `<Path>.orderParts(PartType:object, Amount:integer, Destination:object[, Name:string])` | — | 从 Source 订购零件。 |

### creationTable

将 `<Path>` 指定的 Source 的创建表写入一个 `table`。

- **参数** `CreationTable`（类型 `table`）：本地变量、`table` 类型的表格单元格，或 DataTable 的路径。
- **示例**

```
MySource.creationTable(myEvaluationTable)
MySource.creationTable(MyDataTable[2,8])
```

### getCurrentOrderTableRow

返回 Source 当前用于生产零件的表行号。

- **备注**：仅在 MU Selection 为 `Sequence Cyclical`、`Sequence`、`Random`、`Percentage`（即按 DataTable 生产）时返回有效表行；其他情况始终返回 `0`。
- **示例**

```
print MySource.getCurrentOrderTableRow
```

### orderParts

从 `<Path>` 指定的 Source 订购零件。

- **参数**
  - `PartType`（类型 `object`）：要订购的零件类型路径。
  - `Amount`（类型 `integer`）：订购数量。
  - `Destination`（类型 `object`）：发起订购的对象，可为任意物流对象。若为 Supermarket，Plant Simulation 会增加剩余订购数量计数器（参见 Store 配置表中的 Waiting 列）。
  - `Name`（类型 `string`，可选）：订购零件类型名称；未填写时使用 `PartType` 对象的名称。
- **示例**

```
MySource.orderParts(.UserObjects.MyPart, 12, MyStation, "MyPart")
```

```
param partName:string, minStock:integer, maxStock:integer, currentStock:integer, orderedParts:integer
var amount:integer := maxStock-currentStock-orderedParts
if amount > 0 then
   Source.orderParts(@, amount, ?, partName)
end
```

## 只读属性（Read-Only Attributes）

Source 提供：

- All Objects 的只读属性。
- Material Flow Objects 的只读属性。

只读属性的值由 Plant Simulation 在查询时刻计算，只能读取、不能设置；多数只读属性对应对象某个标签页（如 Statistics）上不可用的对话框项。查询示例：

```
print MySource.UUID
```
