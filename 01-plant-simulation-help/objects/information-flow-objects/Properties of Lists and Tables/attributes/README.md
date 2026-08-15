# Attributes of Lists and Tables（列表与表格的属性）

本目录汇总了 Plant Simulation 中列表与表格对象（**DataStack、DataQueue、DataList、DataTable、TimeSequence**）的属性说明。内容来源于 `attributes.md`。

列表和表格对象提供了以下用途的属性：设置格式、以文本格式处理、打印、显示/隐藏设置以及其他杂项用途。

## 查看属性与方法

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的属性、只读属性和方法。
- 选中插入到 Frame 的实例后，按 **F8** 或点击 Home 选项卡上的 **Show Attributes and Methods**，可查看实例的属性与方法。

可通过对话框中的复选框、文本框、下拉列表，或直接对属性赋值来读取和设置属性值。例如：

```
MyDataTable.MaxXDim := -1      // 设置属性
print MyDataTable.MaxXDim      // 获取属性
```

---

## 一、格式相关属性（Format）

在对话框中通过 **List 选项卡 > Edit Format** 设置。下表为概览：

| 属性 | 语法 | 说明 |
|---|---|---|
| `Alignment` | `<Path>.Alignment:string` | 设置所有单元格对齐方式：`"left"`、`"right"`、`"center"` |
| `BackgroundColor` | `<Path>.BackgroundColor:integer` | 设置背景色（1–7 或 `makeRGBValue` 的 RGB 值） |
| `ColumnWidth` | `<Path>.ColumnWidth:integer` | 设置列宽（字符宽度，默认 20，最大 180） |
| `DataType` | `<Path>.DataType:string` | 设置数据类型（Boolean、Integer、Real、String、Table、Stack、Queue、List 等） |
| `EditorReadOnly` | `<Path>.EditorReadOnly:boolean` | 设置列表/表格是否只读（true） |
| `FontColor` | `<Path>.FontColor:integer` | 设置字体颜色（1–7 或 RGB 值） |
| `FontSize` | `<Path>.FontSize:integer` | 设置字体大小（1=小、2=中、3=大、4=特大），仅 DataTable |
| `FormatString` | `<Path>.FormatString:string` | 根据数据类型设置格式字符串 |
| `InfoflowReadOnly` | `<Path>.InfoflowReadOnly:boolean` | 设置是否只能通过方法读取（true） |

`DataType` 支持的数据类型包括：Acceleration、Boolean、Date、DateTime、Integer、Length、List、Money、Object、Queue、Real、Speed、Stack、String、Table、Time、Weight。

---

## 二、文本格式相关属性（Text Format）

在对话框中通过 **List 选项卡 > Export > Text File Format** 设置。

| 属性 | 语法 | 说明 |
|---|---|---|
| `ColumnSeparator` | `<Path>.ColumnSeparator:string` | 设置文本格式保存时的列分隔符（Tab、空格、`,`、`;`） |
| `DecimalSeparator` | `<Path>.DecimalSeparator:string` | 设置小数分隔符（`.` 或 `,`） |
| `TimeFormat` | `<Path>.TimeFormat:string` | 设置时间格式（`"D:H:M:S"`、`"H:M:S"`、`"M:S"`、`"S"`） |

> 注意：强烈建议不要同时使用逗号 `,` 作为小数分隔符和列分隔符，只能二选一。

---

## 三、打印相关属性（Printing）

在对话框中通过 **List 选项卡 > Print > Print Setup** 设置。

| 属性 | 语法 | 说明 |
|---|---|---|
| `GenerateColumnWidth` | `<Path>.GenerateColumnWidth:boolean` | 打印时是否使用最宽列宽 |
| `PrintColumnNumber` | `<Path>.PrintColumnNumber:boolean` | 是否打印列号 |
| `PrintDataType` | `<Path>.PrintDataType:boolean` | 是否打印数据类型 |
| `PrintInternalLists` | `<Path>.PrintInternalLists:boolean` | 是否打印嵌套列表 |
| `PrintRowNumber` | `<Path>.PrintRowNumber:boolean` | 是否打印行号 |
| `RepeatColumnIndex` | `<Path>.RepeatColumnIndex:boolean` | 是否在每页打印用户定义的列索引 |
| `RepeatRowIndex` | `<Path>.RepeatRowIndex:boolean` | 是否在每页打印用户定义的行索引 |

---

## 四、显示设置相关属性（Showing Settings）

| 属性 | 语法 | 说明 |
|---|---|---|
| `ShowComment` | `<Path>.ShowComment:boolean` | 是否显示注释 |
| `ShowDataType` | `<Path>.ShowDataType:boolean` | 是否显示数据类型 |
| `ShowVoid` | `<Path>.ShowVoid:boolean` | 是否以灰色显示空单元格 |

---

## 五、其他杂项属性（Miscellaneous）

| 属性 | 语法 | 说明 |
|---|---|---|
| `Comment` | `<Path>.Comment:string` | 设置列表/表格的注释（DataTable、DataList、DataStack、DataQueue） |
| `Cursor` | `<Path>.Cursor:integer` | 设置单列列表中光标所在的单元格（DataList、DataStack、DataQueue） |
| `InheritComment` | `<Path>.InheritComment:boolean` | 是否继承类的注释 |
| `InheritContents` | `<Path>.InheritContents:boolean` | 是否继承类的内容 |
| `InheritFormat` | `<Path>.InheritFormat:boolean` | 是否继承类的格式 |
| `MaxDim` | `<Path>.MaxDim:integer` | 设置单列列表的最大单元格数（`-1` 表示无限），适用于 DataStack、DataQueue、DataList |

关于 `Cursor` 的注意事项：

- 所有使用范围的方法（如 `find`、`max`）都从当前光标位置开始，光标位置之前的部分会被忽略；若方法未返回预期值，请检查光标位置。
- 也可用 `setCursor` 方法配合用户自定义索引设置光标。
- 相关属性/方法：`CursorX`、`CursorY`、`setCursor`、`find`、`max`。

---

## 六、DataTable 对象

`DataTable` 用于在多个列中存储数据，且各列可以有不同的数据类型。

- 可通过行号和列号索引访问单个单元格；类比为一个可填入、取出值的"货架"。
- 与 DataList 不同，DataTable 的内容会保留在表中，且允许范围内存在空单元格；仿真运行期间可随时增删行列。
- DataTable 默认在后台打开，可用 `openDialogBox` 方法将其置于前台。
- DataTable 与数据类型 `table` 共享内置属性，但两者有区别：对象 DataTable 可插入模型，而用户定义属性/局部、全局变量的 `table` 类型属于其他对象的一部分（无独立图标）。
- 因此，`table` 类型的变量和属性不识别 DataTable 的 SimTalk 函数（如 `Location`、`existsIcon`），但其他方法（尤其是读写访问）对二者均适用。
- 可在 HtmlReport 中显示 DataTable 内容；悬停可显示工具提示；点击 Edit 选项卡的 Show Manipulators 或按 **M** 可更改图形长度和锚点。
- 添加方式：Home 选项卡 > **Manage Class Library > Basic Objects > InformationFlow > DataTable**。
- 流体对象的 MaterialsTable 与 DataTable 共享属性。

---

## 备注

- 本目录仅包含 `attributes.md`（英文原文）与 `attributes.txtx`（辅助文件），无子目录。
- 本文档为上述内容的归纳总结，详细语法与示例请参阅 `attributes.md`。
