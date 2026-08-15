# Frame Methods（Frame 方法总结）

本目录包含 Frame（框架）对象的方法文档。文档来源为 `methods.md`（以及同内容的文本提取版 `methods.txtx`），内容均一致。

## 概述

Frame 对象提供以下两类方法：

- 下表列出的 Frame 专属方法。
- **所有对象的通用方法**（Methods of All Objects）。

要查看对象的全部方法、只读属性和属性，可打开 **Show Attributes and Methods（显示属性和方法）** 窗口：

- 在 Class Library（类库）的右键菜单中选择 **Show Attributes and Methods**，可查看所选 Class（类）的方法；
- 按下 **F8** 键，或点击 Frame 的 Home 功能区选项卡中的 **Show Attributes and Methods**，可查看所选 Instance（实例）的方法。

## 语法行阅读说明（Reading a Syntax Line）

语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所作用对象的路径。
- 括号内为方法的签名（参数标识符及数据类型），如 `(Parameter:string)` 表示 string 类型的参数。参数处既可使用常量，也可使用所需类型的变量或返回该类型的方法。
- **注意**：表达式内的括号必须输入，否则可能导致意外结果并打开 Debugger（调试器）。
- 可选参数用方括号 `[…]` 表示，如 `[,Parameter:boolean]` 表示可输入也可不输入该 boolean 参数。
- 若参数有默认值，签名会在参数后标注，如 `:= false`。
- 若方法有返回值，签名会在箭头 `→` 后标注其数据类型，如 `→ boolean`。

## 方法清单

| 方法 | 说明 | 返回值类型 |
| --- | --- | --- |
| `getHTMLCode` | 返回 Frame 内容作为基于像素图形的 HTML 代码 | string |
| `node` | 返回 Frame 中指定编号或名称的对象 | object |
| `pasteClipboard` | 将剪贴板内容粘贴到 Frame 中 | 无 |
| `statistics` | 返回 Frame 中所有收集统计数据的物流对象的统计数据 | 无（输出到屏幕/表/文件） |

---

## getHTMLCode [SimTalk]

将 `<Path>` 指定的 Frame 内容作为基于像素图形的 HTML 代码返回，并赋给传入的参数。

**类型：** Method（方法）

**语法：**

```
<Path>.getHTMLCode([Caption:string, Width:integer, Height:integer,
SizeInPercent:string, CameraPositionX:real, CameraPositionY:real,
CameraPositionZ:real, CameraRotationX:real, CameraRotationZ:real]) → string
```

**参数（均为可选）：**

- `Caption` (string)：图形的期望标题。若指定，Plant Simulation 会以该标题显示图形。
- `Width` (integer)：图形的期望宽度。若未指定 Width 与 Height，则使用能显示 Frame 内所有对象的 2D 或 3D 视图的宽高。
- `Height` (integer)：图形的期望高度。
- `SizeInPercent` (string)：图形的期望尺寸百分比，例如 `"75%"`。可用百分比代替 Width 和 Height。
- `CameraPositionX` / `CameraPositionY` / `CameraPositionZ` (real)：相机位置的 x / y / z 轴坐标。
  - 仅当同时指定 CameraRotation 参数时才需指定 CameraPosition 参数。
- `CameraRotationX` / `CameraRotationZ` (real)：相机绕 x 轴 / z 轴的旋转角度。
  - 也可在不指定 CameraPosition 的情况下单独使用 CameraRotation 参数。

> 若指定了 CameraPosition 和/或 CameraRotation 参数，则必须同时指定 Width、Height 或 SizeInPercent。

**返回值：** 数据类型为 string。

**示例：**

```simtalk
print MyFrame.getHTMLCode
MyFrame.getHTMLCode("Caption")
MyFrame.getHTMLCode(100, 100)                        // 尺寸（毫米）
MyFrame.getHTMLCode("Caption", 100, 100)             // 标题 + 尺寸（毫米）
MyFrame.getHTMLCode("75%")                           // 占显示所有对象图形的百分比
MyFrame.getHTMLCode(*)                               // 足以显示所有对象，并尽可能大地显示在 HtmlReport 中
MyFrame.getHTMLCode(100,*)                           // 宽度（毫米），高度按显示所有对象所需比例计算
MyFrame.getHTMLCode(*, 100)                          // 高度（毫米），宽度按显示所有对象所需比例计算
MyFrame.getHTMLCode(100%, -1.123, 2.345, -3.456, -45.0, 15.0)
// 100% 尺寸显示所有对象，同时指定 CameraPosition 和 CameraRotation
```

**另请参见：** Display a Frame、Display a HtmlReport

---

## node [SimTalk]

返回 `<Path>` 指定的 Frame 中指定的对象。

**备注：** Plant Simulation 按插入顺序对模型内的对象编号。此方法也可用于 Class Library。

**类型：** Method（方法）

**语法：**

```
<Path>.node(ObjectNumberOrName:integer/string) → object
```

**参数：**

- `ObjectNumberOrName` (integer)：指定对象的编号。
- `ObjectNumberOrName` (string)：指定对象的名称。若传入字符串，则返回该名称的对象；若不存在该对象，则返回 void。

**返回值：** 数据类型为 object。

**示例：**

```simtalk
print .model.node(3)
// 例如可能返回 .Models.MyPlant.MyStation
```

```simtalk
// 将 Frame 及子 Frame 中的所有对象写入 DataTable。
// 第一列赋为 object 数据类型。
param Frame: object := void
if Frame = VOID
   Frame := current
end
for var i := 1 to Frame.numNodes
   DataTable[1, DataTable.yDim + 1] := Frame.Node(i)     // object
   DataTable [2, DataTable.yDim] := Frame.Node(i).Name   // string
   if Frame.Node(i).InternalClassType = "Frame"          // 子结构
        self.execute(Frame.Node(i))                      // 递归调用
   end
next
```

**另请参见：** node [SimTalk] - folder、NumNodes [SimTalk] - Frame

---

## pasteClipboard [SimTalk]

将剪贴板的内容粘贴到 `<Path>` 指定的 Frame 中。

**类型：** Method（方法）

**语法：**

```
<Path>.pasteClipboard([TargetTable:table])
```

**参数：**

- `TargetTable` (table，可选)：方法执行后，将所有粘贴的对象写入指定表。该表含一列 object 数据类型。

**示例：**

```simtalk
var tbl: table
var   i: integer
pasteClipboard(tbl)
for var i := 1 to tbl.yDim
   print tbl[1,i]  // 输出所有粘贴的对象
next
```

**SimTalk：** copyObjectsToClipboard [SimTalk]

**另请参见：** Paste Contents of the Clipboard [Home ribbon]、Copy [Home ribbon]

---

## statistics [SimTalk]

返回 `<Path>` 指定的 Frame 中所有收集统计数据的物流对象的统计数据。

**备注：** 同样适用于模型较低层级的对象，即模型内嵌套的模型。

**类型：** Method（方法）

**语法：**

```
<Path>.statistics
<Path>.statistics(NameOfTable:table_path)
<Path>.statistics(FileName:string[, CodePage:string:="UTF-8"])
```

**参数：**

- `NameOfTable` (table_path)：将数据写入该表。
- `FileName` (string)：将表写入该文件。Plant Simulation 会覆盖已有条目。
- `CodePage` (string，可选)：设置所需编码：ANSI、UTF-8 或 Unicode。

**参数默认值：** 若未指定 CodePage 参数，默认使用 UTF-8 编码。

**示例：**

```simtalk
building12.statistics                             // 输出到屏幕
.plant.statistics(stat_tab)                       // 输出到表
MySubFrame.statistics("C:\temp\statistics1.txt")  // 输出到文件
```

---

## Frame 的只读属性（Read-Only Attributes of the Frame）

Frame 对象还提供以下只读属性（详见对应文档章节）：

- 目录中列出的 Frame 专属只读属性；
- 所有对象的通用只读属性（_Read-Only Attributes of All Objects）；
- 物流对象的只读属性（Read-Only Attributes of the Material Flow Objects）。

只读属性的值只能查询、不能设置——Plant Simulation 会在查询的时刻计算其值。多数情况下，只读属性对应对象某个选项卡（如 Statistics 选项卡）上不可用的对话框项。

查询只读属性示例：

```simtalk
print .Models.Model.Capacity
```
