# Lists, Tables, and Network Socket Exchange（列表、表格与网络套接字交换）总结

本目录包含 `lists-tables-network-socket-exchange.md`（以及同名文本提取文件 `lists-tables-network-socket-exchange.txtx`），内容为 Plant Simulation 帮助文档中 **数据集成与参数化** 章节下关于“列表、表格与网络套接字交换”的说明：介绍如何使用各类列表/表格对象存取数据，以及如何通过网络套接字（Socket）交换数据。以下是对其内容的总结。

## 1. 使用列表与表格（Working with Lists and Tables）

Plant Simulation 提供多种列表类型，区别在于访问数据的方式不同。可在仿真运行期间用列表为物料流对象提供数据，或把结果写入列表、导出并在其他应用中处理。

可用的列表对象（来自 Class Library 的 `InformationFlow` 文件夹，或 Toolbox 的 *Information Flow* 工具栏）：

| 对象 | 描述 |
| --- | --- |
| **DataList** | 单列；按位置随机访问单元格。可在任意位置新增单元格；删除单元格会使编号更大的单元格上移。 |
| **DataQueue** | 单列；FIFO 访问——最先添加的单元格最先处理。新单元格追加到最后一个单元格之后。 |
| **DataStack** | 单列；LIFO 访问——最后添加的单元格最先处理。在顶部添加单元格会把已有单元格下推。 |
| **DataTable** | 多列；按列号和行号访问单元格。新数据覆盖已有单元格内容。 |
| **TimeSequence** | 两列；按列/行号随机访问数据对，条目按时间升序排列。 |

下述操作对所有列表类型相同。更改设置前，取消 *List* 功能区选项卡上的继承按钮以停用继承。

## 2. 设置列的数据类型（Set the Data Type of a Column）

对 `DataList`、`DataStack`、`DataQueue`（单列列表），为整个列表设置数据类型。对 `DataTable`，可为单列或一列范围设置数据类型。

- 取消 *List* 功能区选项卡上的继承。
- 点击 *List* 功能区选项卡上的 *Edit Format* / *Format*，或右键列并选择 *Format*。
- 点击列标题显示 **Dimension** 和 **Data Type** 选项卡，然后选择数据类型。

### 数据类型

| 数据类型 | 描述 |
| --- | --- |
| Acceleration | m/s²（用于 Conveyor、Track、TwoLaneTrack、Transporter） |
| Boolean | `true` 或 `false` |
| Date | 日期（`dd.MM.yyyy`） |
| DateTime | 日期+时间（`dd.MM.yyyy HH:mm:ss`） |
| Integer | 整数值 |
| Length | 浮点数（长度单位） |
| List | 单列列表（DataList 属性） |
| Money | 浮点数 |
| Object | 对仿真模型或对象的引用 |
| Queue | 单列列表（DataQueue 属性） |
| Real | 浮点数（如 `3.1415`） |
| Speed | 浮点数（速度单位） |
| Stack | 单列列表（DataStack 属性） |
| String | 字符、数字、特殊字符 |
| Table | 一列或多列（DataTable 属性） |
| Time | 时间（`hh:mm:ss.ss`） |
| Weight | 浮点数（重量单位） |

注意：

- 双击值为 `true`/`false` 的 `string`/`boolean` 单元格会切换其值。
- 对 `Integer`、`Real`、`String` 还可输入 **Format String**。
- 隐藏单元格数据类型：取消 *List* 功能区选项卡上的 *Data Type*。

## 3. 设置列表的维度（Set the Dimension of a List）

- 取消继承，点击 *Format*（或右键列 → *Format*）。
- 为单列或选中列范围设置 **Column Width**（以字符宽度计）。
- 点击 *Select All*（左上角、工具栏或 `Ctrl+A`）限制整个表格尺寸。
- 输入 **Number of Rows**（所有列表）以及 `DataTable` 的 **Number of Columns**。留空使列表无界（消耗内存）。
- 右键列 → *Insert Column*（新列为 `string` 类型）；右键行 → *Insert Row*；右键 → *Cut* 删除列/行。

## 4. 设置单元格对齐与颜色（Set Alignment and Colors of Cells）

- 取消继承，点击 *Format*（或右键列 → *Format*）。
- 点击列/行标题选中要格式化的列/行（**Range** 框显示所选范围）。
- 选择 **Alignment**、**Font Size**、**Font Color** 和 **Background Color**。

## 5. 插入、剪切与删除行和列（Insert, Cut and Delete Rows and Columns）

- **插入行**：右键点击要插入位置上一行的单元格 → *Insert Row*。
- **插入列**：右键点击要插入位置左侧列的单元格 → *Insert Column*。若选中第一列，新列插入其右侧；其余列右移。
- **仅删除内容**（保留空行/列）：右键 → 迷你工具栏上的 *Delete*。
- **清除单个单元格**：双击，右键 → *Delete*。
- **删除整行/整列（含内容）**：右键行/列标题 → *Remove Column*。

## 6. 在列表或表格中处理数据（Work with Data in a List or Table）

- 点击单元格（或列/行上方的文本框）输入数据。向已有数据的单元格输入会替换其内容。
- 导航键：

| 键 | 动作 |
| --- | --- |
| `Enter` | 下移一个单元格 |
| `Shift+Enter` | 上移一个单元格 |
| `Tab` | 右移一个单元格 |
| `Shift+Tab` | 左移一个单元格 |
| `Ctrl+Enter` | 跳到下方单元格的起始 |
| `Shift+方向键（上/下/左/右）` | 选择范围 |
| `Esc` | 编辑时恢复原单元格内容 |
| 方向键 | 在单元格内移动光标 |
| `Shift+Left/Right` | 在单元格间移动 |

- 用 `Enter` 或移到另一单元格来应用输入的数据。
- 用拖放移动/复制单元格内容；拖动时按住 `Ctrl` 进行复制。
- 用 *Home > Paste* 粘贴；*Home > Copy* 复制。
- 通过标题选择整列/整行；拖动标题可选择连续的 `DataTable` 列。
- 用 *Select All* 或 `Ctrl+A` 全选。
- *Highlight Empty Cells* 用不同颜色显示空单元格。
- 在 `Table`/`List`/`Stack`/`Queue` 单元格中创建子列表：输入其名称/路径，或拖放进去。
- 打开单元格中的子列表/对象：`Shift` + 双击，或右键 → *Open Object*，或 `F2`。
- 设置标准列宽：*List > Format > Dimension > Column Width*，或拖动列边框（双箭头）。

## 7. 在 DataTable 中处理数据（Work with Data in the DataTable）

### 剪切或复制单元格范围
- 从一角拖到对角选择范围。
- *Home > Cut* 删除内容但保留空单元格；粘贴会覆盖目标范围。
- 点击灰色系统索引区选择整列/整行；剪切会删除并移动剩余列/行。

### DataTable 中的拖放

| 要执行 | 从 | 到 | 加速键 |
| --- | --- | --- | --- |
| 移动选中文本 | 表格窗口 | 表格窗口 | — |
| 复制选中文本 | 表格窗口 | 表格窗口 | `Ctrl` |
| 插入选中文本 | 任意 | 表格窗口 | 任意 |
| 复制选中文本 | 表格窗口 | 任意 | `Ctrl` |
| 剪切选中文本 | 表格窗口 | 任意 | — |

### 插入单元格范围
粘贴剪切/复制的范围仅当目标范围的列/行数与源相同或为其整数倍时才有效。不兼容的数据类型以红色标记。

### 隐藏与显示列
把列的左/右边框向左拖到列消失（隐藏列在前一列末尾用符号标记）。拖到该符号上并单击一次即可把列恢复为原宽度。

### 在单元格中插入下拉列表
选中 `String` 类型单元格，右键 → *Format* → *Data Type* 选项卡。在 **Format String** 中输入以分号分隔的项（末尾无空格）。示例：`Entry1;Entry2;Random` 创建含这些项的下拉列表。

> 注意：双击单元格才会在列表窗口中实际显示下拉列表。用 `openDialogBox` 打开列表窗口时，下拉列表立即显示。

## 8. 访问列表中的数据（Accessing Data in Lists）

用**系统索引**（分配的编号）或**用户自定义索引**（有意义的表达式）访问单元格。用户自定义索引可读性更好、对插入/删除更稳健，但稍慢：

```
Switch["Light","220 Volts"]
Vehicle["limo",#1]
Plant["Chicago",.building1.drill]
```

可用操作：

- 设置列索引 / 行索引。
- 创建用户自定义列索引和行索引。
- 设置和获取列表上界。
- 用方法寻址列和行。

## 9. 设置列索引（Set the Column Index）

- 点击 *List* 功能区选项卡上的 *Activate Column Index*（再次点击停用并删除已有内容）。
- 选中第一个数据行上方的索引行，点击 *Format*；在 *Data Type* 选项卡选择索引数据类型。
- 可选输入 **Format String**（对 `Integer`、`Real`、`String`）。
- 选择 **Fast Index Access** 以更快访问用户自定义索引。
- 选择 **Unique Index Key** 仅允许唯一条目。

## 10. 设置行索引（Set the Row Index）

- 点击 *List* 功能区选项卡上的 *Activate Row Index*。
- 选中索引列 → *Format* → 在 *Data Type* 选项卡选择数据类型。
- 可选设置 **Format String**、**Fast Index Access**、**Unique Index Key**。

## 11. 创建用户自定义列索引和行索引（Create a User-defined Column and Row Index）

- 取消继承。
- 点击 *Activate Column Index* 并在第一个索引行输入有意义的术语。通常选 `String`；对 `Integer`，在术语前加 `#` 以区别于系统索引。
- 点击 *Activate Row Index* 并在第一个索引列输入表达式（`Integer` 同样加 `#`）。

> 注意：当两个索引都激活时，单元格 `[0,0]`（交点）算作列索引的一部分，而非行索引。

## 12. 设置和获取列表上界（Set and Get the Upper Bound of a List）

- 取消继承，选中整个列表（*Select All* 或 `Ctrl+A`），点击 *Format*（或右键列 → *Format*）。
- 在 **Dimension** 选项卡输入 **Number of Columns** 和 **Number of Rows**。下界自动为 `1`（用户自定义索引为 `0`）。
- 属性：
  - 单列列表：`MaxDim`
  - 双列列表：`MaxXDim`、`MaxYDim`
  - 表格：只读 `XDim`/`YDim` 返回当前占用；`XDimIndex`/`YDimIndex` 返回最后占用的索引单元格。
- 用 *List* 功能区选项卡上的 *Go To* 移到指定单元格。

## 13. 用方法寻址列和行（Address Columns and Rows with Methods）

### 设置列和行的格式

```
setXX(Parameter:any, ..., Parameter:any, Parameter:integer)
```

- 参数个数始终 ≥ 2。
- 最后一个参数设置列或行（系统索引或用户自定义索引）。
- 对连续范围，用 `*` 定义所有行/列的范围：

```
MyDataTable.setDataType({3,*}..{4,*},6,"column1","real")
```

| 条目 | 表示 |
| --- | --- |
| `{3,*}..{4,*}` | 范围——第 3、4 列的所有单元格 |
| `6` | 某列的系统索引 |
| `"column1"` | 一个列索引 |
| `"real"` | 一个值 |

### 获取列或行的格式

```
getXX(ColumnOrRow:any)
```

- 参数个数始终为 1；`ColumnOrRow` 可为系统或用户自定义索引。

```
MyDataTable.getDataType(1)  -- returns the data type of column 1
```

## 14. 用方法搜索列表（Search Lists with Methods）

列表/表格有内部游标（`Cursor` 属性；表格为 `CursorX`/`CursorY`）。搜索（如 `find`）从当前游标位置开始。搜索成功后游标置于找到的单元格；再次 `find` 从此继续。若未找到，游标留在原处。

```
MyDataStack.find(12.34)
// finds the floating point value 12.34 starting from the current cursor position
MyDataQueue.find(42)
// finds the integer value 42 starting from the current cursor position
MyDataList.find({1},{4}..{8},"drill")
// finds the string "drill" in row 1 and rows 4 to 8
MyDataTable.find("a")
// finds the string "a" in the entire table
MyDataTable.setCursor(3,1)
// set cursor so that next find starts search from beginning
MyDataTable.find({3,*},"a")
// finds the string "a" in column 3
MyDataTable.find({1,1}..{4,*},"a")
// finds the string "a" in columns 1 to 4 in all rows
var MyDataTable.setCursor(1,1)
if MyDataTable.find("abc")
   print MyDataTable.CursorX, " ",MyDataTable.CursorY
else
   print "not found"
end
```

> 注意：插入或删除行后要重新设置游标。

检查 `DataTable` 中已存在哪些值的示例：

```
var lst : list; lst.create
for var i := 1 to DataTable5.YDim
   lst.setcursor(1)
   // Sets the cursor into the first cell. Searching starts there.
   if not lst.find(DataTable5[1, i])
      lst.append(DataTable5[1, i])
   end
next
promptListN(lst, "Found these values:")
```

## 15. 用查找对话框搜索列表（Search Lists with the Find Dialog）

右键列表 → *Find*，或按 `Ctrl+F`。

- **Find What**：搜索词。
- **Match Case**：区分大小写搜索。
- **Match Entire Cell Contents**：整单元格精确匹配。
- **Search in Rows** 或 **Columns**：搜索方向。
- **Search Criterion**：
  - *Find*：查找术语（比较方法 `find`）。
  - *Find ceil(ing)*：值 ≥ 搜索词（比较 `findCeil`）。
  - *Find floor*：值 ≤ 搜索词（比较 `findFloor`）。
- *Find Next* 查找下一处；*Replace* 显示 **Replace With** 并替换术语。

## 16. 在列表与表格中创建嵌套列表（Create Lists within Lists and Tables）

在 `DataList`、`DataStack`、`DataQueue` 或 `DataTable` 单元格中创建子列表/子表：

1. 打开列表对象；取消继承。
2. 右键列标题 → *Format*。
3. 选择子列表数据类型：`Table`、`List`、`Stack` 或 `Queue`。
4. 若该列所有子列表共享格式，选择 **Common Format**。
5. 在 **Contents** 选项卡应用格式，点击 OK（也可用 `setCommonFormat`）。
6. 在更改后的列单元格中输入名称以标识各子表。
7. 按住 `Shift` 双击子表以打开编辑。

把列表对象从 Frame/Class Library 插入单元格：

- 把列数据类型设为 `Object`，然后把表格拖入单元格（插入绝对路径）。当列表在同一 Frame 时，输入列表名使用相对路径。
- 打开子列表：`Shift`+双击、右键 → *Open Object* 或 `F2`。

## 17. 排序 DataList、DataTable 和 TimeSequence（Sort DataList, DataTable, and TimeSequence）

- 上下文菜单上的 **Sort Ascending** / **Sort Descending** 对选中列排序。
- 方法：`sort` 升/降序排序；`inOrder` 把值插入已有序列的正确位置。

## 18. 用公式计算值（Calculate Values with a Formula）

**Formula** 读取并关联其他单元格和对象属性的值，然后执行计算（使用与 Method 相同的运算符/函数）。

步骤：

1. 点击 *List* 功能区选项卡上的 *Create Formula* 激活公式模式。
2. 点击单元格（或列表上方的文本框）输入表达式。示例：`@[1,2]+@[2,3]` 把单元格 `[1,2]` 与 `[2,3]` 相加。
3. 按 `Enter` 显示结果。
4. 双击单元格显示/编辑公式本身。

含公式的单元格用颜色标识：青绿色=语法正确，红色=语法错误。

### 在公式中用 `@` 访问 DataTable 单元格

| 公式 | 执行 |
| --- | --- |
| `@[1,1]+@[1,2]` | 把 `[1,1]` 与 `[1,2]` 的内容相加 |
| `@[1,1]*track.length` | 把 `[1,1]` 乘以对象 `track` 的长度 |
| `@[1,@.ydim]+5` | 把 5 加到第一列最后一个单元格 |
| `@[xSelf+1,ySelf]-7` | 从右侧相邻单元格减去 7 |
| `@.sum({3,*})` | 计算第三列之和 |
| `@.min({1,2}..{1,*})` | 第一列从第 2 个单元格起的最小值 |

> 注意：公式结果必须与所在单元格/列的数据类型相同。

公式内也可用匿名标识符 `?` 访问 `table` 类型的局部变量。

### 用 `?` 访问子列表
在子列表中，`?` 访问子列表所插入的列表；对用户自定义属性，`?` 访问属性所属对象。`xSelf` 和 `ySelf` 包含公式单元格的列号/行号。

### 捕获公式中的运行时错误
为 `DataTable` 添加名为 `ErrorHandler`、数据类型为 `Method` 的用户自定义属性。把错误消息设为空字符串（`""`）可抑制它；处理器随后可为出错单元格返回新值。

## 19. 导入或导出列表内容（Import or Export the Contents of a List）

- **Export Object File**（`.psobj`）：保存列表及全部 Plant Simulation 格式；用 *List* 功能区选项卡上的 *Import* 导入。
- **Export Text File**：只保存内容，不含格式。通过 *Export > Text File Format* 配置分隔符。在 *Save As* 对话框选择编码。
- **Export Excel File**：把内容保存为 Excel 工作表；输入工作表名。

Excel 导出类型映射：

| Plant Simulation 数据类型 | Excel 数据类型 | Excel 格式 |
| --- | --- | --- |
| String | String | — |
| Boolean | Boolean | — |
| Integer | Number | — |
| Real | Number | — |
| Object / Table / List / Stack / Queue | String | — |
| Money / Length / Weight / Speed / Acceleration | Number | — |
| DateTime | Number | `dd/mm/yyyy hh:mm:ss.000` |
| Date | Number | `dd/mm/yyyy` |
| Time | Number | `dd:hh:mm:ss.000` |

> 注意：Integer 仅在 -536.870.912 到 536.870.911 范围内导出；超出范围的值保存为 `0`。读取 Excel 时，列应只含单一数据类型；第 0 行若存在则解释为列索引。

## 20. 取消共享列表或数据表（Unshare a List or Data Table）

把 `table`/`list`/`stack`/`queue` 类型的 `Variable` 赋给子表单元格（或把一个用户自定义属性赋给另一个）会创建**引用**而非副本——改一个会影响另一个。用 `unshare` 使用两个独立的值。

```
Variable := DataTable[1,1]
Variable[1,2] := "Value1" // Value1 appears in DataTable[1,1]
```

```
&Variable.unshare
Variable[1,2] := "Value2" // Value2 doesn't appear in DataTable[1,1]
```

## 21. 将列表作为前台对话框打开（Open a List as a Dialog in the Foreground）

默认列表窗口在对话框后面的后台打开。用 `openDialogBox` 将其作为前台对话框打开：

```
SteeringTypes.openDialogBox
```

对话框窗口在功能区选项卡和上下文菜单上提供精简的功能集，并且只有点击 *Apply* 或 *OK* 时才应用条目（而非输入时即应用）。

## 22. 通过网络套接字交换数据（Exchange Data via a Network Socket）

套接字通信是点对点的，在初始化时建立，直接基于 TCP/IP——速度快、数据开销小。`Socket` 对象提供 TCP/IP 接口。一个进程充当服务器，其他进程注册为客户端；Plant Simulation 可以是任一角色。

添加 `Socket` 对象：通过 *Home* 功能区选项卡上的 *Manage Class Library > Basic Objects > Socket*，或从 Class Library 的 `InformationFlow` / *Information Flow* 工具栏插入。

### 建立 Frame `ServerSocket`
插入：一个 `Socket` 对象、一个回调方法、两个 Variable（`MessageReceived`、`MessageSent`）和一个发送消息的 Method。

- 命名服务器 Socket 对象（如 `MyServerSocket`）；选择回调方法并只勾选 **On** 和 **Server Socket**。
- 协议：**TCP** 建立连接并保证投递；**UDP** 无连接交换数据（开销更小，不保证投递）。

发送方法（`sendMessages`）：

```
var str: string
// generates a random number between 0 and 100
str := to_str(round(z_uniform(1,0,100),1))
// writes the value of the random number to the variable 'MessageSent'
MessageSent := str
// sends the message using channel 0
MyServerSocket.write(0,str)
```

回调方法（`MyCallbackMethod`）：

```
param SocketChannelNo: integer, SocketMessage: string
// writes the value to the global variable 'MessageReceived'
if strLen(SocketMessage) = 1
   MessageReceived := to_str(strAscii(SocketMessage)) // byte received
else
   MessageReceived := to_str(SocketMessage)           // string received
end
// writes the message to the Plant Simulation Console
print "--------------------------------------------------------------------"
print self
print "Message: The number ", MessageReceived, " was received at ", sysdate
```

### 建立 Frame `ClientSocket`
插入与服务器相同的对象。命名客户端 Socket 对象（如 `MyClientSocket`），选择回调方法，勾选 **On** 并**取消** *Server Socket*。

发送方法（`sendMessages`）：

```
var str: string
str := to_str(round(z_uniform(1,0,100),1))
MessageSent := str
MyClientSocket.write(0,str)
```

回调方法（`MyCallbackMethod`）：

```
param SocketChannelNo: integer, SocketMessage: string
if strLen(SocketMessage) = 1
    MessageReceived := to_str(strAscii(SocketMessage)); // byte received
else
    MessageReceived := to_str(SocketMessage); // string received
end
print "--------------------------------------------------------------------"
print self
print "Message: The number ", MessageReceived, " was received at ", sysdate
```

### 运行
1. 在 `MyServerSocket` 和 `MyClientSocket` 中激活 **On**。
2. 右键 `ServerSocket` Frame 中的 `sendMessages` → *Run*。
3. 观察变量和 Console：计算出的值（如 `1.8`）写入服务器的 `MessageSent`，并出现在客户端的 `MessageReceived` 中。

## 目录说明

- `lists-tables-network-socket-exchange.md`：列表、表格与网络套接字交换章节的 Markdown 版本（本总结的源文件）。
- `lists-tables-network-socket-exchange.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Lists, Tables, and Network Socket Exchange"。Unpublished work. © 2026 Siemens.*
