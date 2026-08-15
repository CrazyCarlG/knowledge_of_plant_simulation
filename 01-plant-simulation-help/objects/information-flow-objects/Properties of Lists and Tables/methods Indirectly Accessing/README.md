# 间接访问列表与表格的方法（Methods for Indirectly Accessing Lists and Tables）

本目录汇总了列表（List）和表格（Table）用于**间接访问**的 SimTalk 方法。内容来源于本目录下的 `methods Indirectly Accessing.md`（其原始文本见 `methods Indirectly Accessing.txtx`）。本目录没有子文件夹，因此没有其他子目录 `README.md` 需要汇总。

## 概述

列表和表格提供以下方法，用于间接访问它们的内容。

这些方法**仅适用于数据类型为 `object`（对象）的范围**。单元格的内容是指向待处理对象的引用，这些对象的属性即为被访问的目标。

> 适用于以下对象（除非另有说明）：`DataStack`、`DataQueue`、`DataList`、`DataTable`、`TimeSequence`。

可通过 **Show Attributes and Methods** 窗口查看对象的全部方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **Class（类）** 的属性和方法。
- 按 **F8** 键，或点击插入了实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选 **Instance（实例）** 的属性和方法。

## 方法总览

| 方法 | 功能 | 语法 | 返回值类型 |
| --- | --- | --- | --- |
| `asObject` | 若单元格包含有效对象路径，返回该单元格的内容（字符串或对象） | `<Path>.asObject(Column:any, Row:any)` | `any` |
| `asString` | 将指定单元格作为字符串返回 | `<Path>.asString(Column:any, Row:any)` | `string` |
| `findAttr` | 查找包含指定名称和指定值的属性的对象 | `<Path>.findAttr([Range:listrange, ]AttributeName:string, Value:any)` | `boolean` |
| `maxAttr` | 返回指定属性的最大值 | `<Path>.maxAttr(Range:listrange, ..., AttributeName:string)` | 范围统一类型 / `real` |
| `meanValueAttr` | 返回指定属性的平均值 | `<Path>.meanValueAttr(Range:listrange, ... AttributeName:string)` | `real` |
| `minAttr` | 返回指定属性的最小值 | `<Path>.minAttr(Range:listrange, ... AttributeName:string)` | 范围统一类型 / `real` |
| `standardDeviationAttr` | 返回指定属性的标准差 | `<Path>.standardDeviationAttr(Range:listrange, ... AttributeName:string)` | `real` |
| `sumAttr` | 返回指定属性值的总和 | `<Path>.sumAttr(Range:listrange, ... AttributeName:string)` | 范围统一类型 / `real` |

## 各方法详解

### asObject — 将单元格内容作为对象返回

返回 `<Path>` 指定的列表/表格中某个单元格的内容（数据类型为 `string` 或 `object`），前提是该单元格包含指向对象的有效路径。

- **参数**：`Column`（数据类型 `any`）指定表格的列；`Row`（数据类型 `any`）指定行。
- **返回值**：数据类型为 `any`。
- **注意**：如果 `asString` 返回的单元格包含指向 **TwoLaneTrack（双车道轨道）** 车道的有效路径，则返回值为该车道。由于车道不具有 `object` 数据类型，因此不能赋给 `object` 类型的变量，但可赋给 `any` 类型的局部变量。若 `object` 类型的单元格包含指向车道的路径，使用方括号（`table[x,y]`）读取其内容会返回 **VOID**。

```simtalk
var a : any
if .MUs.Transporter:1.getRoute(DataTable) 
a := MyDataTable.asObject(1,1)
if isObject(a) 
print "first object: ", a.name
else
print "first object is a two-lane track: ", a.~.name
end
print "the length is: ", a.length
```

### asString — 将单元格内容作为字符串返回

返回 `<Path>` 指定的 DataTable 中指定单元格的内容，数据类型为 `string`。

- **备注**：当 `object` 类型的单元格包含一个 Plant Simulation 会将其作为对象或 **VOID** 返回的路径时，此方法尤为实用。
- **返回值**：数据类型为 `string`。

```simtalk
MyDataTable[1,2] := "Station" // 写入绝对路径
MyDataTable.asString(1,2)     // 读取相对路径
```

**参见**：`asObject [SimTalk]`

### findAttr — 查找包含指定属性的对象

在 `<Path>` 指定的列表/表格中查找包含指定名称和指定属性值的属性的对象。

- **备注**：
  - 仅在数据类型为 `object` 的列中搜索，忽略其他数据类型的列。
  - 可查找内置属性和用户自定义属性。
  - 若只想查找具有该属性的对象而不关心属性值，可将 **VOID** 作为要搜索的值传入。
  - 从列表/表格内部指针的当前位置开始搜索。若找到，则将内部指针设置到相应单元格并返回 `true`；否则返回 `false`。
- **参数**：
  - `Range`（可选，数据类型 `listrange`）：指定要搜索的范围。若未指定，则搜索整个表格；也可指定多个列表范围。
  - `AttributeName`（数据类型 `string`）：要搜索的属性名。
  - `Value`（数据类型 `any`）：要搜索的属性值。找到即终止搜索。若为 **VOID**，则找到名为 `AttributeName` 的属性即结束，并将指针设置到该对象条目并返回 `true`；值不匹配则继续搜索，未找到则返回 `false`。
- **注意**：
  - 属性名和属性值的搜索**不区分大小写**。
  - 对 DataTable，范围的效果取决于「列索引是否属于内容（Column Index Belongs to Contents）」：属于内容时，范围包含列索引；不属于内容时，范围仅针对内容本身，不含列索引。
- **返回值**：数据类型为 `boolean`。

```simtalk
var wanted: object,
var row,column: integer 
MyDataList.Cursor := 1
if MyDataList.findAttr("color", "red") 
   wanted := MyDataList.read(MyDataList.Cursor)
end
MyDataTable.CursorX := 1 MyDataTable.CursorY := 1
if MyDataTable.findAttr({1,1}..{4,4},"order",VOID) 
   column := MyDataTable.CursorX 
   row := MyDataTable.CursorY print table[column,row].order
end
```

**参见**：`CursorX [SimTalk]`、`CursorY [SimTalk]`、`Cursor [SimTalk]`、指定单元格范围（多列）> 列索引属于内容、指定单元格范围（多列）> 列索引不属于内容。

### maxAttr — 返回属性最大值

返回 `<Path>` 指定的列表/表格中所有对象的指定属性的最大值。

- **备注**：此外，Plant Simulation 会将文件光标设置到包含最大属性值的对象所在的单元格。
- **参数**：`Range`（数据类型 `listrange`，可多个）指定列表范围；`AttributeName`（数据类型 `string`）指定属性名。
- **返回值**：若指定列表范围具有统一数据类型，则为该数据类型；否则返回值转换为 `real` 类型。

```simtalk
// 搜索表格指定范围内的所有条目，并确定用户自定义属性 Time 的最大值
MyDataTable.setCursor(1,1)
print MyDataTable.maxAttr({1,2}..{3,5},"time")
```

**参见**：`minAttr [SimTalk]`

### meanValueAttr — 返回属性平均值

返回 `<Path>` 指定的列表/表格指定范围内所有对象的指定属性的平均值。

- **参数**：`Range`（数据类型 `listrange`，可多个）指定列表范围；`AttributeName`（数据类型 `string`）指定属性名。
- **返回值**：数据类型为 `real`。

```simtalk
MyDataStack.Cursor := 1
print MyDataStack.meanValueAttr({3}..{*},"SetupTime")
```

### minAttr — 返回属性最小值

返回 `<Path>` 指定的列表/表格中所有对象的指定属性的最小值。

- **备注**：Plant Simulation 会将文件光标设置到包含最小属性值的对象所在的单元格。
- **参数**：`Range`（数据类型 `listrange`，可多个）指定列表范围；`AttributeName`（数据类型 `string`）指定属性名。
- **返回值**：若指定列表范围具有统一数据类型，则为该数据类型；否则返回值转换为 `real` 类型。

```simtalk
// 循环遍历列表中的所有单元格，查询其加工时间，并返回加工时间的最小值
MyDataList.Cursor := 1
print MyDataList.minAttr({*},"ProcTime")
table.setCursor(1,1)
print MyDataTable.minAttr({1,2}..{3,5},"time")
```

**参见**：`maxAttr [SimTalk]`

### standardDeviationAttr — 返回属性标准差

返回 `<Path>` 指定的列表/表格指定范围内所有对象的指定属性的标准差。

- **参数**：`Range`（数据类型 `listrange`，可多个）指定列表范围；`AttributeName`（数据类型 `string`）指定属性名。
- **返回值**：数据类型为 `real`。

```simtalk
MyDataList.Cursor := 1
print MyDataList.standardDeviationAttr({*},"ProcTime")
```

### sumAttr — 返回属性值之和

返回 `<Path>` 指定的列表/表格指定范围内所有对象的指定属性值之和。

- **参数**：`Range`（数据类型 `listrange`，可多个）指定列表范围；`AttributeName`（数据类型 `string`）指定属性名。
- **返回值**：若指定列表范围具有统一数据类型，则为该数据类型；否则返回值转换为 `real` 类型。

```simtalk
// 循环遍历 DataQueue 中的所有单元格，累加加工时间，并返回总和
MyDataQueue.Cursor := 1
print MyDataQueue.sumAttr({1}..{5},"ProcTime")
```

## 只读属性与单元格属性

列表和表格中的单元格提供以下只读属性和属性：

- **Void [SimTalk] - 列表/表格的单元格**（只读属性）
- **Name [SimTalk] - 单元格**（属性）

读取和写入权限取决于对象类，详见各子章节。

> 说明：与「查询统计值」系列方法（`max`、`min`、`sum` 等直接作用于数值单元格）不同，本目录的 `*Attr` 系列方法（`maxAttr`、`minAttr`、`sumAttr`、`meanValueAttr`、`standardDeviationAttr`）通过单元格中**对象引用的属性**进行统计，且 `findAttr` 也仅搜索 `object` 类型的列。

## 相关参考

- 指定单元格范围（多列）> 列索引属于内容（Column Index Belongs to Contents）
- 指定单元格范围（多列）> 列索引不属于内容（Column Index Does Not Belong to Contents）
- `Cursor [SimTalk]`、`CursorX [SimTalk]`、`CursorY [SimTalk]`
- `asObject [SimTalk]` / `asString [SimTalk]`
