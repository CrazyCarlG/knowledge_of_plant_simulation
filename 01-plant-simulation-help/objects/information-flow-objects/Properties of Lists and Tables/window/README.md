# Window — 列表与表格的窗口（Window of Lists and Tables）

本目录汇总了 Plant Simulation 列表与表格对象（Lists and Tables）的窗口（Window）说明。内容来源于本目录下的 `window.md`（其原始文本见 `window.txtx`）。本目录没有子文件夹，因此没有其他子目录 `README.md` 需要汇总。

## 概述

`window.md` 对应 Plant Simulation 帮助主题 *Window of Lists and Tables*，涵盖以下内容：

- 列表/表格对象的窗口（Window of Lists and Tables）
- **List 功能区选项卡**（List Ribbon Tab）及其命令
- 各命令对应的对话框：**导入/导出文件**、**文本文件格式**、**打印**、**查找/替换**、**转到单元格**、**插入行/列**、**排序**、**创建公式**、**激活行/列索引**、**编辑格式**等
- 相关的两个上下文菜单（嵌入式列表、列表对象内容）
- 用方法访问单元格范围

---

## 窗口（Window of Lists and Tables）

双击插入到仿真模型中的列表对象图标，即可打开其窗口。

### 备注（Remarks）

- 要修改对象 **Class** 的属性，可在 Class Library 中双击该对象，或在 Toolbox 的 **Information Flow** 选项卡上双击它。在这里可以查看/更改已保存的数据、输入新数据，并调整格式和数据类型。
- 可在 **List Ribbon Tab** 上访问列表对象的函数。
- 要在 3D 模型中编辑对象的 3D 属性，选中对象并按**空格键**，然后在 **Edit 3D Properties** 对话框中修改。
- 要操作对象的图形，点击 Edit 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

---

## List 功能区选项卡（List Ribbon Tab）

List 选项卡提供访问列表对象函数的命令。并非所有列表对象都提供所有命令。

| 命令 | 对应的方法或属性（SimTalk） |
| --- | --- |
| Import File（导入文件） | `readFile`（列表） |
| Export to File（导出到文件：文本/对象/Excel/XML） | `writeFile`、`writeObjectFile`、`writeExcelFile`、`writeXMLFile` |
| Text File Format（文本文件格式） | `ColumnSeparator`、`DecimalSeparator`、`TimeFormat` |
| Print List / Print Setup（打印列表/打印设置） | `printList`、`showPrintDialog`、`PrintRowNumber`、`PrintColumnNumber`、`PrintDataType`、`RepeatRowIndex`、`RepeatColumnIndex`、`PrintInternalLists`、`GenerateColumnWidth` |
| Find / Replace（查找/替换） | `find`、`findCeil`、`findFloor` |
| Go To Cell（转到单元格） | `Cursor`、`CursorX`、`CursorY` |
| Insert Row（插入行） | `insertRow` |
| Insert Column（插入列） | `insertColumn` |
| Sort Ascending / Descending（升序/降序排序） | `sort` |
| Create Formula（创建公式） | `setFormula` |
| Activate Column Index（激活列索引） | `ColumnIndex` |
| Activate Row Index（激活行索引） | `RowIndex` |
| Edit Format（编辑格式） | 多种 |
| Inherit Format（继承格式） | `InheritFormat` |
| Inherit Contents（继承内容） | `InheritContents` |
| Inherit Comment（继承注释） | `InheritComment` |
| Recompute Formulas（重新计算公式） | `calculateList` |
| Show Comment（显示注释） | `ShowComment` |
| Show Data Type（显示数据类型） | `ShowDataType` |
| Highlight Empty Cells（高亮空单元格） | `ShowVoid` |
| Open Object（打开对象） | `openDialog`、`openDialogBox` |

功能区栏上的其他选项卡也提供与列表对象相关的命令。

---

## 导入文件（Import File）

导入先前保存的列表，并打开 **Open** 对话框。支持的文件类型：

- **对象文件（*.pslist）** — 包含内容 *和* Plant Simulation 格式（数据格式、维度、索引/列宽等）。可在模型间交换列表；专有格式（`.psobj`），其他程序无法识别。
- **文本文件（*.txt）** — 仅包含列表内容，不含 Plant Simulation 专属设置。可在文本编辑器或电子表格程序中创建。参见 *文本文件格式*。
- **Excel 工作簿（*.xls, .xlsx, .xlsm, .xlsb）** — Plant Simulation 将 Excel 作为 COM 服务器使用，须安装 MS Excel。使用启动选项 `-NativeExcel` 可保留旧版（不受支持的）Excel 接口。

### Excel 导入注意事项

- 从 Excel 导入的是原始值，并在 Plant Simulation 内部转换。
- 导入到字符串列时，数值在 Plant Simulation 内转换；Plant Simulation 的格式可能与 Excel 格式不同。
- 每个 Excel 列应只包含一种数据类型。
- 如果存在**第 0 行（zero）**，它会被当作列索引处理，不参与数据类型指定。
- Plant Simulation 尊重 DataTable 的维度——例如 3 行 × 10 列只导入前 3 行和 10 列（有利于性能）。

参见：`readFile`、`readExcelFile`、`readXMLFile`；启动选项说明、`-NativeExcel`。

---

## 导出到文件（Export to File）

提供不同格式的导出命令：**Export Text File**、**Export Object File**、**Export Excel File**、**Export XML File** 和 **Text File Format**。

### 导出文本文件（Export Text File）

将列表内容保存为文本文件（`.txt`），不含格式信息。可选编码：

- **ANSI** — 8 位字符集（0–255），是 ASCII 的超集。
- **UTF-8** — Unicode 编码，每个字符一到三个字节。
- **Unicode** — 16 位字符集，以 UTF-16 保存（每字符两字节）。

文本文件的保存/读取由 **Text File Format** 设置决定。

### 导出对象文件（Export Object File）

将列表保存为 `*.pslist`，包含内容 *和* 格式（数据类型、列/行格式、维度、列/行索引）。在另一模型中打开时属性相同；专有格式。

### 导出 Excel 文件（Export Excel File）

保存为 Microsoft Excel 工作表（`.xls`），打开 **Save As** 对话框。

- 使用 Excel 作为 COM 服务器，须安装 MS Excel；`-NativeExcel` 保留旧接口。
- 仅能以所需格式导出范围在 **-536,870,912 到 536,870,911** 的整数；超出范围的值保存为 `0`。
- 使用所选单位设置导出数据（例如 `Length` 使用米）。
- 每个 Excel 列应只包含一种数据类型；**第 0 行** 被当作列索引。
- 导入尊重 DataTable 维度。

**数据类型转换表（Plant Simulation → Excel）：**

| Plant Simulation | Excel 数据类型 | Excel 格式 |
| --- | --- | --- |
| string | String | — |
| Boolean | Boolean | — |
| Integer / Real | Number | — |
| Object / Table / List / Stack / Queue | String | — |
| Money / Length / Weight / Speed / Acceleration | Number | — |
| DateTime | Number | `dd/mm/yyyy hh:mm:ss.000` |
| Date | Number | `dd/mm/yyyy` |
| Time | Number | `dd:hh:mm:ss.000` |

### 导出 XML 文件（Export XML File）

将列表保存为 XML 文件（`.xml`），使用 UTF-8 编码，标签为 `PlantSimulationTable`。

---

## 文本文件格式（Text File Format）

打开 **Text File Format** 对话框，选择导出/导入文本文件的设置。Plant Simulation 按行导入和导出数据。

- **Column Separator（列分隔符）**：Tab、Space、Semicolon 或 Comma。
  - *注意：* 避免将逗号同时用作列分隔符和小数分隔符。
- **Decimal Separator（小数分隔符）**：句点（`.`）或逗号（`,`）。
- **Time format（时间格式）**：`S`、`M:S`、`H:M:S` 或 `D:H:M:S` —— 让电子表格程序读取其原本无法识别的时间值。

SimTalk：`ColumnSeparator`、`DecimalSeparator`、`TimeFormat`。

---

## 打印列表 / 打印设置（Print List / Print Setup）

- **Print List** 打开 **Print** 对话框（打印机、纸张格式、方向、份数）。
- **Print Setup** 打开 **Print Setup** 对话框，选择要打印的项目。

| 复选框 | 说明 | 属性 |
| --- | --- | --- |
| Row Number | 在每个单元格前打印行号 | `PrintRowNumber` |
| Column Number | 在每列上方打印列号 | `PrintColumnNumber` |
| Data Type | 打印每列的数据类型 | `PrintDataType` |
| Repeat Row Index | 在每页重复用户定义的行索引 | `RepeatRowIndex` |
| Repeat Column Index | 在每页重复用户定义的列索引 | `RepeatColumnIndex` |
| Internal Lists | 打印列表所包含的嵌套表格 | `PrintInternalLists` |
| Column Width | 使用最宽列的宽度打印列 | `GenerateColumnWidth` |

---

## 查找 / 替换（Find / Replace）

- **Find** 查找并选中包含某表达式的单元格。若未选中单元格，则搜索整个列表；否则从选中单元格向末尾搜索。
- **Replace** 查找表达式并替换。

两个对话框都支持：

- **Match Case** — 区分大小写匹配。
- **Match Entire Cell Contents** — 整单元格精确匹配。
- **Search in Rows / Columns** — 按行/列搜索。
- **搜索准则**：`Find`（精确）、`Find ceil(ing)`（`findCeil`，值 ≥ 表达式）、`Find floor`（`findFloor`，值 ≤ 表达式）。
- **Find Next**、**Replace**、**Replace All**、**Cancel**。

SimTalk：`find`、`findCeil`、`findFloor`。

---

## 转到单元格（Go To Cell）

通过输入 **Column（列）** 和 **Row（行）** 编号移动到列表/表格中的特定单元格（该单元格成为滚动的起点）。显示 **Occupied Columns（已占用列）** 和 **Occupied Rows（已占用行）** 数量。

SimTalk：`Cursor`、`CursorX`、`CursorY`。

---

## 插入行 / 插入列（Insert Row / Insert Column）

- **Insert Row** — 在活动单元格/行上方添加一个空行。
- **Insert Column** — 在选中列左侧插入一个新的空列；现有列右移。

SimTalk：`insertRow`、`getRowNo`、`cutRow`；`insertColumn`、`getColumnNo`、`cutColumn`。

---

## 升序 / 降序排序（Sort Ascending / Sort Descending）

- **升序**：最小数字、最早日期或字母表开头在前。
- **降序**：最大数字、最晚日期或字母表末尾在前。

排序区分大小写，且只对 DataTable 的选中列排序。空单元格排在列的末尾（升序）或开头（降序）。

SimTalk：`sort`、`inOrder`。

---

## 创建公式（Create Formula）

激活/停用 DataTable 的公式模式。公式可访问/链接其他单元格或对象属性。

步骤：

1. 点击按钮激活公式模式。
2. 点击单元格（或列表上方的文本框）并输入表达式。
   - *注意：* 如果用 `z_` 调用分布函数，必须输入随机数流——公式从不使用周围对象的随机数流。
3. 按 Enter 在单元格中显示计算值。
4. 点击公式单元格可在文本框中显示公式本身。

*注意：* 结果的数据类型必须与单元格/列的数据类型匹配。

参见：`getFormula`、`setFormula`。

---

## 激活列索引 / 激活行索引（Activate Column Index / Activate Row Index）

激活列/行索引（表头）。再次点击可停用并删除现有内容。

- 若两个索引都激活，单元格 `[0,0]` 计入**列**索引，而非行索引。
- 可使用**系统索引**（自动编号）或**用户自定义索引**（任意有意义的表达式）。
- 在表达式 `[3,1]` 中，第一个值是**列**，第二个是**行**。

**示例（用户自定义索引）：**

```
orders["urgent","preferred customer"]
vehicles["truck",#1]
switch["light",true]
plant["Chicago",.building1.drill]
```

- 用户自定义索引比系统索引更有意义、更不易出错；在添加列/行时仍然有效（系统索引会移位）。访问用户自定义索引略慢。
- 用户自定义索引只能为数据类型 **string、integer、object 和 boolean** 定义。
- 对于 **integer** 索引，在表达式前加井号 `#` 以区别于系统索引。

设置索引的数据类型：点击 Activate Column/Row Index 按钮，选中索引列/行（编号 0），点击 **Format**，选择数据类型，并可设置 **Format String**、**Fast Index Access** 和 **Unique Index Key**。

- **Fast Index Access（快速索引访问）** — 为快速用户自定义索引查找创建内部结构（略微增加内存和索引更改时间）。推荐用于大表。
- **Unique Index Key（唯一索引键）** — 仅允许唯一条目（Plant Simulation 用红色高亮重复项；在 Method 中赋值重复项时不会给出警告）。

SimTalk（列）：`ColumnIndex`、`ShowColumnIndex`、`DataTypeColumnIndex`、`FormatStringColumnIndex`、`XDimIndex`、`FastAccessColumnIndex`、`UniqueKeyColumnIndex`。
SimTalk（行）：`RowIndex`、`ShowRowIndex`、`FormatStringRowIndex`、`YDimIndex`、`FastAccessRowIndex`、`UniqueKeyRowIndex`。

---

## 编辑格式（Edit Format）

打开 **Edit Format** 对话框，编辑 Settings、Permissions、Dimension 和 Data Type。可见的选项卡取决于选择：

- 选中单元格/范围 → **Settings** 和 **Permissions** 选项卡。
- 选中列 → 额外显示 **Data Type** 和 **Dimension** 选项卡。
- 选中整个列表 → 设置应用于整个列表。

**Range** 框显示选中范围。**Apply** 应用设置而不关闭；**OK** 应用并关闭；**Cancel** 放弃更改。

### Settings 选项卡

设置 Alignment（对齐）、Font Size（字号）、Font Color（字体颜色）、Background Color（背景颜色）以及 **Column Index Belongs to Contents（列索引属于内容）**。

- **Alignment** — 左、右或居中（`Alignment`、`setAlignmentCells`、`setAlignmentColumn`、`setAlignmentRow` 等）。
- **Font Size** — 列表自动调整单元格宽/高（`FontSize`、`setFontsizeColumn`、`setFontSizeCells` 等）。
- **Font Color / Background Color** — 选择预定义颜色或 **More Colors**；**Default** 使用主题颜色（`FontColor`、`BackgroundColor` 及其 `set*`/`get*` 方法）。
- **Column Index Belongs to Contents** — 勾选时，列索引随内容一起继承（通过 Inherit Contents）；清除时，随格式一起继承（通过 Inherit Format）。新模型默认停用（索引属于格式）。仅 DataTable 提供此设置。SimTalk：`ColumnIndexContents`、`DataTable.delete`。

### Permissions 选项卡

通过 **Editor** 和 **Information Flow** 复选框选择读写权限。

- **Editor** — 勾选 = 在列表窗口中只读；清除 = 在 List Editor 中可读写（`EditorReadOnly`）。
- **Information Flow** — 勾选 = 通过 Methods/Attributes 只读；清除 = 通过 Methods/Attributes 可读写（`InfoflowReadOnly`）。仅当选中所有含条目的单元格时激活。

### Dimension 选项卡

设置 **Number of Rows（行数）**（DataTable 还有 **Number of Columns 列数**）和 **Column Width（列宽）**。将行/列留空表示维度不受限制。

- **Number of Rows**（`MaxDim`、`MaxYDim`）
- **Number of Columns**（`MaxDim`、`MaxXDim`）
- **Column Width** — 以非比例字体的字符宽度计；默认 20，最大 180（`ColumnWidth`、`getColumnWidth`、`setColumnWidth`）。

Data Type 和 Dimension 选项卡仅在通过列标题选中一列或多列后显示。

### Data Type 选项卡

选择 **Data Type（数据类型）** 和可选的 **Format String（格式字符串）**。

**可用数据类型：**

| 数据类型 | 说明 |
| --- | --- |
| Acceleration | m/s²（Conveyor、Track、TwoLaneTrack、Transporter） |
| Boolean | `true` 或 `false` |
| Date | `dd.MM.yyyy` |
| DateTime | `dd.MM.yyyy HH:mm:ss` |
| Integer | 整数值 |
| Length | 浮点数（随单位） |
| List | 单列列表（DataList 属性） |
| Money | 浮点数 |
| Object | 对模型/对象的引用 |
| Queue | 单列列表（DataQueue 属性） |
| Real | 浮点数（如 `3.1415`） |
| Speed | 浮点数（随单位） |
| Stack | 单列列表（DataStack 属性） |
| String | 字符、数字、特殊字符 |
| Table | 一列或多列（DataTable 属性） |
| Time | `hh:mm:ss.ss` |
| Weight | 浮点数（随单位） |

*注意：*
- 只能更改整列的数据类型，不能更改单元格/行。
- 双击 `true`/`false` 单元格可切换其值。
- 日期可按日-月-年或 `年/月/日`（如英文模型中 `2026/11/11`）输入。

SimTalk：`DataType`、`setDataType`、`getDataType`、`setDataTypeDefault`。

#### 格式字符串（Format String）

限制用户在列表窗口中可输入的数据（不限制 Method 赋值）。适用于 Integer、Real、Length、Weight、Speed、Acceleration、Money 和 String。

- **String** 格式字符（按位）：

| 字母 | 输出 |
| --- | --- |
| A | 仅字母 |
| U | 仅大写字母 |
| X | 所有字符 |
| C | 大写字母和数字 |
| N | 仅数字 |
| L | 字母和数字 |
| I | 对象名允许的所有字符（字母、变音符、数字、下划线） |

  示例 `AANXU`：前两位必须是字母，第三位是数字，第四位任意字符，第五位是大写字母。用分号分隔多个词条（末尾不留空格）可创建下拉列表（如 `Entry1;Entry2;Random`）。

- **Integer** — 一个数字限制显示的位数（如 `3` 显示前三位）；前缀减号（如 `-3`）允许负值。用 `color` 作为格式字符串可打开 Windows 颜色对话框（通过 `makeRGBValue` 存储 RGB）。
- **Real** — 用点分隔的两个数字限制小数点前后的位数（如 `5.3` = 共 5 位，小数点后 3 位；`-6.3` 允许负数）。

SimTalk：`FormatString`、`getFormatString`、`setFormatString`、`makeRGBValue`。

#### 通用格式（Common Format）

对于 Table、List、Stack、Queue 数据类型，**Common Format** 复选框取代 Format String 文本框，并添加 **Tab Contents**。

- 强制显示范围内的所有列表采用同一格式，然后在 Tab Contents 上创建模板列表。新建列表继承这些格式属性。
- 若 Common Format 激活，将子表赋值给表格单元格会创建该表的**副本**；否则 Plant Simulation 输入**引用**。

SimTalk：`CommonFormatColumnIndex`、`setCommonFormat`、`setCommonFormatData`、`getCommonFormatData`。

##### 激活与停用 Common Format

**第一个示例（选中 Common Format）** — Method 使用局部变量访问表中的列表；Plant Simulation 访问引用：

```
var l: list[string]
MyDataTable.delete
MyDataTable.createNestedList
l := MyDataTable[2,1]            // reference
l.insert(1,"abc")
l.insert(1,"Hello")
print MyDataTable[2,1].read(1)  //abc
print MyDataTable[2,1].read(2 ) // Hello
```

**第二个示例（清除 Common Format）** — 通过赋值相同格式的局部列表达到同样结果；格式由局部变量决定，而非表格：

```
var l:list[string]
MyDataTable.delete
l.createNestedList
l.insert(1,"abc")
MyDataTable[2,1] := l
l.insert(1,"Hello")
print MyDataTable[2,1].read(1) // abc
print MyDataTable[2,1].read(2) // Hello
```

*注意：* 当 Common Format 激活时，将列表/表格赋值给具有列表/表格格式的单元格可能创建副本而非引用，具体取决于所赋列表/表格的格式。

---

## 内容选项卡（Tab Contents）

选择列表的通用格式（对 Table、List、Stack、Queue 数据类型显示）。在此创建模板列表，强制显示范围内的所有列表采用同一格式。

参见：`createNestedList`（DataQueue、DataList、DataTable）、`setCommonFormat`。

---

## 继承格式 / 继承内容 / 继承注释（Inherit Format / Inherit Contents / Inherit Comment）

- **Inherit Format** — 切换格式继承。插入的列表从其类继承格式；只有关闭后才能更改格式。关闭它同时会关闭 Inherit Contents（`InheritFormat`）。
- **Inherit Contents** — 切换内容继承。插入的列表从其类继承内容；只有关闭后才能更改内容。关闭它同时会关闭 Inherit Format；向列表输入数据会自动关闭它。*注意：* 当实例化包含子列表的类并通过 Method 写入时，Plant Simulation **不会** 自动关闭它——你必须自行关闭（`InheritContents`）。
- **Inherit Comment** — 切换列表注释的继承（`InheritComment`）。

---

## 重新计算公式（Recompute Formulas）

重新计算已输入的公式，并在相应单元格中显示其当前值（`calculateList`）。

---

## 显示注释 / 显示数据类型 / 高亮空单元格（Show Comment / Show Data Type / Highlight Empty Cells）

- **Show Comment** — 显示/隐藏表格内容上方的描述性文本框。该注释还会在 Frame 中拖动对象时作为工具提示出现，并作为 `HtmlReport` 中的标题（`Comment`、`ShowComment`）。
- **Show Data Type** — 显示/隐藏列和行的数据类型（过长时缩写；包含用户自定义索引）（`ShowDataType`）。
- **Highlight Empty Cells** — 切换空单元格的浅灰色显示。包含空字符串 `""` 的单元格 *不* 是空的（`ShowVoid`）。

---

## 打开对象（Open Object）

打开数据类型为 object、table、stack 或 queue 的单元格中所输入名称对应的对象对话框（或按 `F2`）。SimTalk：`openDialog`、`openDialogBox`。

---

## 嵌入式列表的上下文菜单（Context Menu of Embedded Lists）

嵌入式列表提供常用设置的上下文菜单命令。示例包括 Failure Importer 的 Services 列表、WorkerPool 的 Creation Table、GanttChart 的 Parts Table、FlowControl 的策略列表，以及 Trigger/ShiftCalendar/AttributeExplorer 列表。并非所有嵌入式列表都提供所有命令。

| 命令 | 说明 | SimTalk |
| --- | --- | --- |
| Open Object | 打开单元格中对象的对话框（或 `F2`） | `openDialog`、`openDialogBox` |
| Select Object | 通过 **Select Object** 对话框选择对象 | — |
| Cut | 剪切单元格/列/行内容到剪贴板 | `cutColumn`、`cutRow` |
| Copy | 复制单元格/列/行内容到剪贴板 | `copy`、`copyRangeTo` |
| Paste | 将剪贴板内容粘贴到选中单元格 | — |
| Delete | 删除单元格/列/行内容 | `delete` |
| Select All | 选中整个列表内容 | — |
| Delete Row | 删除选中行 | — |
| Insert Row | 在选中行上方插入空行 | `insertRow` |
| Append Row | 在最后一行下方插入空行 | — |
| Sort Ascending / Descending | 排序（区分大小写；仅选中行/列） | `sort`、`inOrder` |
| Show Comment | 显示/隐藏描述性文本框 | `ShowComment` |
| Import | 导入文件（`.pslist`、`.txt`、`.xls/.xlsc/.xlsm/.xlsb`、`.xml`） | — |
| Export | 导出为制表符分隔文本/Excel | — |

**导入/导出注意事项：**

- 仅当文件包含属性的 **Name**（而非 Alias）时，导入文件才能正确工作。
- 导出格式：ANSI、UTF-8、Unicode 文本文件，以及 Excel 工作簿（`.xls`）。

---

## 列表对象内容的上下文菜单（Context Menu of the Contents of List Objects）

列表对象内容的上下文菜单提供最重要的命令（部分在迷你工具栏上）。

工具栏命令包括：**Open Location**、**Open Origin**、**Open Class**、**Copy Objects**、**Cut Objects**、**Paste Objects**、**Delete Objects**、**Select All**、**Open Object**、**Insert Row**、**Remove Row**、**Insert Column**、**Remove Column**、**Insert**、**Format**、**Find**、**Sort Ascending**、**Sort Descending**。

| 命令 | 说明 | SimTalk |
| --- | --- | --- |
| Open Location | 打开包含列表/表格的对象 | `Location` |
| Open Origin | 打开所选对象派生来源的对象 | `Origin` |
| Open Class | 打开 Class Library 中类的对话框 | `derive` |
| Cut / Copy / Paste / Delete | 对单元格/列/行进行剪贴板操作 | `cutColumn`、`cutRow`、`copy`、`delete` |
| Select All | 选中整个列表内容 | — |
| Open Object | 打开单元格中对象的对话框（或 `F2`） | `openDialog`、`openDialogBox` |
| Show Object | 在 Frame 中显示/选中对象（对象类型列） | — |
| Insert Row / Remove Row | 在上方插入空行 / 删除选中行（行移位） | `insertRow`、`cutRow` |
| Insert Column / Remove Column | 在左侧插入新空列 / 删除选中列 | `insertColumn` |
| Insert | 插入空行直到列表填满（受 Dimension 限制） | `insert` |
| Format | 打开 **Edit Format** 对话框 | — |
| Find | 打开 **Find** 对话框 | — |
| Sort Ascending / Descending | 排序选中行/列（区分大小写） | `sort`、`inOrder` |

注意：
- **Remove Row** 不适用于包含行索引的行；**Remove Column** 不适用于包含列索引的列。
- **Insert** 填充列表直到达到指定 Dimension（DataList/DataStack/DataQueue）。

---

## 用方法访问单元格范围（Accessing a Range of Cells with a Method）

除单个条目外，还可以处理连续的单元格范围。某些方法（如 `min`、`max`）只适用于范围，需要特殊语法。

两种情况：

- **单列列表中的单元格范围（Cell Ranges in Lists with One Column）**
- **多列表格中的单元格范围（Cell Ranges in Tables with Several Columns）**

### 单列列表中的单元格范围

使用左花括号 `{`、第一个单元格编号、右花括号 `}`、两个点 `..`、左花括号 `{`、最后一个单元格编号和右花括号 `}` 访问单列列表中的单元格范围。

---

*来源：Plant Simulation Help — Window of Lists and Tables（pp. 11-3823 ff.）。未发表作品。© 2026 Siemens。*
