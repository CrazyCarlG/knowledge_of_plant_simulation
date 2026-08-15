# Import and Export Data, Databases, and External Media（数据的导入导出、数据库与外部媒体）总结

本目录包含 `import-export-databases-external-media.md`（以及同名文本提取文件 `import-export-databases-external-media.txtx`），内容为 Plant Simulation 帮助文档中 **数据集成与参数化** 章节下关于“导入导出数据、数据库与外部媒体”的说明：介绍如何为仿真导入/导出数据、与数据库交互，以及显示外部程序中存储的数据。以下是对其内容的总结。

## 1. 概述（Overview）

本节介绍如何导入导出仿真数据、使用数据库，以及显示存储在外部程序中的数据。

通常数据从电子表格程序（如 Microsoft Excel）或数据库导入到 Plant Simulation 的列表或表格中。筛选出实际需要的数据，物料流对象即可访问这些列表并用数据进行仿真。也可导出仿真运行产生的数据供其他程序使用。

Plant Simulation 提供多种数据导入方式：

- 将文本文件或对象文件导入列表
- 从 Microsoft Excel 工作表导入数据
- 将服务、班次等列表导入对象
- 以 XML 格式导入数据
- 从数据库导入数据
- 以 ANSI 格式导入/导出数据
- 导入/导出列表内容

## 2. 将文本文件或对象文件导入列表（Import a Text File or an Object File into a List）

Plant Simulation 的 `DataTable`、`DataList`、`DataQueue`、`DataStack` 和 `TimeSequence` 列表可打开文本文件、Plant Simulation 对象文件、XML 文件和 Microsoft Excel 文件。

- 打开文本文件前，为 DataTable 每列选择正确数据类型。若文本文件有想复用的列标题，激活并显示列索引。
- 在列表中打开文本文件或对象文件：点击 List 功能区选项卡上的 **Import File**，导航到文件夹，选择文件类型，点击 **Open**。
- Plant Simulation 按原始格式打开对象文件。对于文本文件，必须手动选择正确数据类型。
- 导出列表或表格内容：点击 List 功能区选项卡上的 **Export to File** 或 **Export Object File**。

## 3. 从 Microsoft Excel 工作表导入数据（Import Data from a Microsoft Excel Worksheet）

Plant Simulation 读取 MS Excel 表格时，尝试把每列的值转换为 Plant Simulation 表格对应列的数据类型。这仅当每个 Excel 列只含单一数据类型（如整列均为 `String`）时才有效。

导入后检查数据类型，纠正错误并筛选掉不需要的数据。可手动完成，也可编写 Method 在导入时处理数据。

- 示例文件：`MyTestData.xlsx`。
- 在 Plant Simulation 表格中打开 Excel 文件：点击 List 功能区选项卡的 **Import File**，选择文件，点击 **Open**，选择工作表，点击 **OK**。
- 将列表或表格导出为 Excel 文件：点击 List 功能区选项卡的 **Export Excel File**。

## 4. 将服务、班次等列表导入对象（Import a List of Services, Shifts, etc. into an Object）

多数情况下此类列表导入涉及两个列表：

1. 含占位表达式的**主列表**（例如操作名 `Operations for MyPart A`）。
2. 含实际工位名及相关信息的**子列表**。

将服务列表、班次列表或工人创建表导入对象的嵌入列表：

- 在文本编辑器中打开收到的文件。确保列标题中的文本在第一行，列用制表符分隔，另存为文本文件（`.txt`）。
- 打开 Plant Simulation 对象，切换到 **Importer** 选项卡。点击子选项卡 **Processing** 上 **Services** 右侧的继承复选框，再点击 **Services**。
- 在列表中右键点击 **Import**。导航到保存的文本文件并点击 **OK**。
- 将嵌入列表导出为制表符分隔的文本文件：在列表中右键选择 **Export**。

## 5. 以 XML 格式导入数据（Import Data in XML Format）

可导入 XML 格式存储的数据并从中提取数据。例如用 `XMLInterface` 读取从 **Process Designer**（Siemens 用于规划、分析和管理制造流程的程序）或 XML 数据库导出的数据。

导入并用 Method 处理数据后，用 `write` 和 `writeElement` 方法把仿真结果写回 XML 文件。

要充分利用 `XMLInterface`，应熟悉 **XPath**（见 http://www.w3.org/TR/xpath）和 **SimTalk** 编程。

可从 Class Library 的 **InformationFlow** 文件夹，或 Toolbox 的 **Information Flow** 工具栏插入 `XMLInterface`。

可进行：选择文件名、上下文与导入方法；顺序读写数据；随机读取与访问数据；随机访问与遍历数据。

### 选择文件名、上下文与导入方法（Select File Name, Context, and Import Method）

在 `XMLInterface` 的对话框中：

- **File Name**：`XMLInterface` 打开（导入）或保存（导出）的 XML 文件。
- **Context**：XML 文档结构中开始读取的节点（如 `Data/Objects`）。它限制读取的数据量。不设上下文则导入整个文件，可能耗时耗内存。
- **Import Method**：点击输入提取并顺序处理导入数据的 Method 的路径和名称。

### 顺序读写数据（Read and Write Data Sequentially）

可逐行顺序读取数据，写入 Import Method，并立即逐行处理。输入 **Context** 以限制导入的数据量。

顺序写 XML 文件示例：

```simtalk
XMLInterface.FileName := "D:\MSXML 4.0\writeSequentially.xml"
// opens the XML document for sequential writing
XMLInterface.openWrite
XMLInterface.startElement("catalog")
   XMLInterface.startElement("book")
   // adds attributes to the item 'book'
   XMLInterface.addAttribute("id", "bk01")
   XMLInterface.addAttribute("xmlns","myBooks")
   XMLInterface.addAttribute("xmlns:aa","specAth")
   // these are the children of the item 'book'
   XMLInterface.writeElement("aa:author","Gambardella, Matthew")
       XMLInterface.addAttribute("age","16")
       XMLInterface.writeElement("title","XML Developer's Guide")
       XMLInterface.writeElement("genre","Computer")
       XMLInterface.writeElement("price","44.95")
       XMLInterface.writeElement("publish_date","2000-10-01")
       XMLInterface.writeElement("description","An in-depth ...")
   // terminates the item 'book'
   XMLInterface.endElement
// terminates the element 'catalog'
XMLInterface.endElement
XMLInterface.close
```

### 随机读取与访问数据（Read and Access Data Randomly）

Plant Simulation 可完整读取数据，然后整体随机处理。它先导入整个文档，再在 Method 中处理分析全部数据。随机访问要求所有数据都在 RAM 中——数据量越大，`XMLInterface` 占用的 RAM 越多。

**从 XML 文档中选择数据：**

```simtalk
// randomly accesses data via XPath instructions
var tbl:table
XMLInterface.FileName := "D:\MSXML 4.0\books.xml"
// load the XML document for random access into RAM
XMLInterface.openDocument
// select nodes via XPath instruction
tbl := XMLInterface.getNodes("book[title='Midnight Rain']", 1)
XMLInterface.close
```

**删除 XML 文档中已有数据：**

```simtalk
XMLInterface.FileName := "D:\MSXML 4.0\books.xml"
XMLInterface.openDocument
// delete all book nodes of genre 'Fantasy'
XMLInterface.deleteNodes("book[genre = 'Fantasy']")
XMLInterface.FileName := "D:\MSXML 4.0\tmp.xml"
XMLInterface.write
XMLInterface.close
```

**向 XML 文档插入新数据：**

```simtalk
var tbl:table
XMLInterface.FileName := "D:\MSXML 4.0\books.xml"
XMLInterface.openDocument
tbl := XMLInterface.getContainer(1)
XMLInterface.setContext("/catalog")
tbl[1,1] := "book"
tbl.createNestedList(4,1)
tbl[4,1][1,1] := "xmlns:aa"
tbl[4,1][2,1] := "specAth"
tbl[4,1][1,2] := "id"
tbl[4,1][2,2] := "bk113"
tbl.createNestedList(5,1)
tbl[5,1][1,1] := "aa:author"
tbl[5,1][2,1] := "specAth"
tbl[5,1][3,1] := "XYZ"
tbl[5,1][1,2] := "title"
tbl[5,1][3,2] := "UNKNOWN"
tbl[5,1][1,3] := "genre"
tbl[5,1][3,3] := "also"
tbl[5,1][1,4] := "price"
tbl[5,1][3,4] := "12,45"
tbl[5,1][1,5] := "publish_date"
tbl[5,1][3,5] := "12.1.02"
tbl[5,1][1,6] := "description"
tbl[5,1][3,6] := "xx0011"
XMLInterface.insertNodes(tbl)
XMLInterface.FileName := "D:\MSXML 4.0\tmp.xml"
XMLInterface.write
XMLInterface.close
```

**更新 XML 文档：**

```simtalk
var tbl:table;
XMLInterface.FileName := "D:\MSXML 4.0\books.xml"
XMLInterface.openDocument;
tbl := XMLInterface.getNodes("/catalog/book[title='Midnight Rain']", 1)
tbl[5,1][3,3] := "TEST"
XMLInterface.updateNodes(tbl)
XMLInterface.FileName := "D:\MSXML 4.0\tmp.xml"
XMLInterface.write
XMLInterface.close
```

**新建 XML 文档：**

```simtalk
var tbl:table;
XMLInterface.newDocument("catalog")
tbl := XMLInterface.getContainer(1)
XMLInterface.setContext("/catalog")
tbl[1,1] := "book"
tbl[2,1] := "MyBooks"
tbl.createNestedList(4,1)
tbl[4,1][1,1] := "xmlns:aa"
tbl[4,1][2,1] := "specAth"
tbl[4,1][1,2] := "id"
tbl[4,1][2,2] := "bk113"
tbl.createNestedList(5,1)
tbl[5,1][1,1] := "aa:author"
tbl[5,1][2,1] := "specAth"
tbl[5,1][3,1] := "XYZ"
tbl[5,1][1,2] := "title"
tbl[5,1][3,2] := "UNKNOWN"
tbl[5,1][1,3] := "genre"
tbl[5,1][3,3] := "also"
tbl[5,1][1,4] := "price"
tbl[5,1][3,4] := "12,45"
tbl[5,1][1,5] := "publish_date"
tbl[5,1][3,5] := "12.1.02"
tbl[5,1][1,6] := "description"
tbl[5,1][3,6] := "xx0011"
XMLInterface.insertNodes(tbl)
XMLInterface.FileName := "D:\MSXML 4.0\tmp.xml"
XMLInterface.write
```

### 随机访问与遍历数据（Access and Traverse Data Randomly）

可完整提取数据后随机遍历。例如用 `selectNodes` 定义起点，用 `getNodeName` 获取下一节点，用 `getNumberAttributes` 检查属性，输出属性名，并递归检查子节点。

```simtalk
var numberAttributes
XMLInterface.FileName := "D:\Public\XML\books.xml"
XMLInterface.openDocument
XMLInterface.selectNodes("book[genre = 'Computer']")
while XMLInterface.getNextNode = true
   print XMLInterface.getNodeName
   numberAttributes := XMLInterface.getNumberAttributes
   for var i := 0 to numberAttributes-1
       print XMLInterface.getAttributeName(i)+":"+XMLInterface.getAttributeValue(i)
   next
   VisitChildren
end
XMLInterface.close
```

## 6. 从数据库导入数据（Import Data from a Database）

可从数据库导入数据到 Plant Simulation，用它运行仿真，并把结果写回。要充分利用此功能，应熟悉 **SQL**（见 http://sqlzoo.net）和 **SimTalk** 编程。

可进行：从 ODBC 数据库导入数据、从 Oracle 数据库导入数据、与 SQL 数据库交换数据。

## 7. 从 ODBC 数据库导入数据（Import Data from an ODBC Database）

用 Plant Simulation 的 `ODBC` 对象从 ODBC 数据库导入数据。要同时访问多个数据库，可插入多个 `ODBC` 对象，各自与不同数据库通信。

> **注意：** 以下示例仅在 64 位 Windows 操作系统上安装了 64 位 ODBC 驱动时才能运行。64 位 ODBC 驱动不能与 32 位 Microsoft Office 并行安装。

可用多个 ODBC 对象访问同一数据库，但不推荐，因为冲突命令（如一个 Method 删除数据集而另一个尝试访问）可能导致数据不一致。使用单个 ODBC 对象可确保指令顺序符合意图。这对真实数据库尤其重要，数据操作（读、写、删等）必须用 SQL 指令 `commit` 提交。

从 ODBC 数据库导入数据分两步：

1. 设置数据源
2. 将数据导入仿真模型

仿真运行结束后，可把结果导回数据库。

### 设置数据源（Set the Data Source Up）

- 在搜索框中输入 **ODBC Data Sources (64-bit)**。
- 在 **ODBC Data Source Administrator** 对话框中，在 **User DSN** 或 **System DSN** 选项卡（通常为 **System DSN**）添加新数据源。
  - 在 **System DSN** 选项卡点击 **Add**。
  - 在 **Create New Data Source** 中选择 ODBC 驱动（如 **Microsoft Access Driver**）并点击 **Finish**。
  - 在 **ODBC Microsoft Access Setup** 中点击 **Select**，选择数据库，输入 **Data Source Name**，可选加 **Description**。Plant Simulation 用此名称寻址数据库，注意遵循 Plant Simulation 命名约定。
  - 点击 **Select** 选择要连接的数据库。

### 将数据导入仿真模型（Import Data into Your Simulation Model）

设置好 ODBC 数据源后，把 `ODBC` 对象插入模型。它建立连接并把数据导入 Plant Simulation 表格。

- 将 `ODBC` 加入 **Information Flow** 工具栏：点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > InformationFlow**，然后插入对象。

典型设置包括：

- 一个 `ODBC` 对象（控制与数据库通信）。
- 一个从数据库读数据的 Method。
- 一个向数据库写数据的 Method。
- 一个用于导入/导出的 Plant Simulation `DataTable`。

- 双击 `ODBC` 对象，在 **Database** 输入数据库名（如 `TestDB`）。对有用户管理的数据库（SQL Server、Oracle 等），还要输入 **User name** 和 **Password**。点击 **Apply**，再 **Login**。

设置正确时，Plant Simulation 使数据库名框变灰并在 **Message** 显示 **Ok**；否则显示错误信息。

读写仅在连接时有效；`login` 和 `logout` 方法框定数据库操作：

```simtalk
ODBC.login("TestDB","","")
// database operation
ODBC.logout
```

读取数据并把查询结果写入 Plant Simulation 表格（或局部变量）：先 `sql` 命令，再定义目标表格，再在引号内输入 SQL 查询：

```simtalk
ODBC.login("TestDB","","")
ODBC.sql(Orders, "select * from Orders2")
ODBC.logout
```

读取时按数据库格式格式化目标表格列：勾选 `ODBC` 对象对话框中的 **Format table**。仅当 Plant Simulation 提供与数据库格式对应的格式时生效（Plant Simulation 不提供典型 Oracle 日期格式的对应项）。

数据量大时，优先用带过滤条件的 SQL 查询，通常比搜索大型 Plant Simulation 表格快得多：

```simtalk
ODBC.login("TestDB","","")
ODBC.sql(Orders, "select DeliveryTime, Amount from Orders2 where MU = '.MUs.panel'")
ODBC.logout
```

### 将数据导出到数据库（Export Data to the Database）

可用 `sql` 方法和 SQL 指令把选定的仿真结果导回 ODBC 数据库。

用 `insert into` 添加新行：

```simtalk
ODBC.login("TestDB","","")
ODBC.sql("insert into Orders2 values ('15:00:00.0000', '.MUs.NewPart', '150', 'NewPart', 'abc')")
ODBC.logout
```

> **注意：** SQL 没有添加整行或整表内容的单条语句，因此必须在 Method 中逐个输入每个单元格的内容。

用 `update` 指令更新已有数据：

```simtalk
ODBC.login("TestDB","","")
ODBC.sql("update Orders2 set Attribute = 'xyz' where Name = 'rod'")
ODBC.logout
```

## 8. 从 Oracle 数据库导入数据（Import Data from an Oracle Database）

使用 `Oracle11g`/`Oracle19c` 对象，方式与 `ODBC` 对象类似。先与 Oracle Server 上的数据库实例建立连接；该实例决定输入到对象中的数据库名。

Microsoft Windows 不提供 Oracle 设置。若 Oracle Server 未与 Plant Simulation 安装在同一台计算机，需安装 Oracle Client 建立连接（若未随附，联系 Oracle 供应商）。

数据量大时，`Oracle11g` 比 `ODBC` 性能更好、命令更多。

- 将 `Oracle11g` 加入 **Information Flow** 工具栏：点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > InformationFlow > Oracle11g**，然后插入对象。

> **注意：** 也可将 ODBC 与 Oracle 一起使用——此时不需要 Oracle Client。注意所用 SQL 指令不一定与 ODBC 版本兼容。若要在 Oracle 与 Access 数据库间切换测试，请对所有数据库使用 ODBC。

## 9. 与 SQL 数据库交换数据（Exchange Data with an SQL Database）

Plant Simulation 可用 `SQLite` 对象与 SQL 数据库交换数据。

- 将 `SQLite` 加入 **Information Flow** 工具栏：点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > InformationFlow > SQLite**，然后插入对象。

本示例模型演示用 `SQLite` 连接 Plant Simulation 与 SQL 数据库：

- `MySQLite` 使用存储在内存而非硬盘文件的数据库。
- `openDatabase` 打开数据库并用 SQL 语句建表。
- `SourcePart` 和 `SourcePallet` 生产零件；零件离开 Source 时 `enterCreationTime` 记录零件类型和创建时间。
- 零件到达 Drain 时，`enterDeletionTime` 记录零件离开工厂的时间。
- 仿真运行六天；`endSim` 计算零件平均寿命，`fillTable` 把结果写入 Plant Simulation 表格。
- `closeDatabase`（由 `endSim` 调用）关闭数据库。

创建模型三步：

1. 配置与 SQL 数据库的连接
2. 配置工厂物料流
3. 从数据库导入仿真结果并显示

对比示例模型：**Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples > Category > Information Flow > Topic > SQLite Introduction**。

### 配置与 SQL 数据库的连接（Configure the Connection with the SQL Database）

- 插入 `SQLite` 对象（命名 `MySQLite`），使用默认 `:memory:` 设置——数据库存于内存以提升性能。注意 Plant Simulation 关闭或崩溃时所有数据丢失。要保留数据，输入数据库文件名。

**Method `openDatabase`：**

```simtalk
// called by the init method
MySQLite.open          // opens the database
MySQLite.exec("CREATE TABLE MUTrace (MUName TEXT PRIMARY KEY, MUType TEXT, StartTime REAL, EndTime REAL)")
```

**Method `closeDatabase`：**

```simtalk
// called by the endsim method
MySQLite.close // closes the database
```

**Method `reset`**（在 EventController 中点击 Reset Simulation 时调用）删除 DataTable 内容及 Comment 中的结果数字：

```simtalk
DataTable.delete
DataTable.closeDialog
Comment.Text :=  "MU Type, Lifetime"+strChr(13)+strChr(10)+"------------------------"
```

**Method `init`** 显示 `Processing...` 并打开数据库：

```simtalk
Comment.Text := "Processing..."
openDatabase
```

### 配置工厂物料流（Configure the Material Flow Through the Facility）

- 插入两个 `Source` 对象，生产不同零件类型（`SourcePart` 生产 `Part` 型，`SourcePallet` 生产 `Container` 型）。为两个 Source 选择相同的后置触发 Exit Control。

**Method `enterCreationTime`** 把创建时间、类型和开始时间插入 `MUTrace`，再绑定并执行 SQL 语句：

```simtalk
MySQLite.prepare("INSERT INTO MUTrace (MUName, MUType, StartTime) VALUES (?1, ?2, ?3)")
MySQLite.bindString(1, obj_to_str(@))
MySQLite.bindString(2, @.name)
MySQLite.bindReal(3, EventController.simTime)
MySQLite.step
```

- 插入四个 `Station` 对象处理零件。
- 插入 `Drain`，用 `enterDeletionTime` 作为 Entrance Control，把零件移出工厂。

**Method `enterDeletionTime`** 用删除时间更新 `MUTrace`：

```simtalk
MySQLite.prepare("UPDATE MUTrace set EndTime = ?1  WHERE MUName = ?2")
MySQLite.bindReal(1, EventController.simTime)
MySQLite.bindString(2, obj_to_str(@))
MySQLite.step
```

### 从数据库导入仿真结果并显示（Import the Simulation Results From the Database and Show Them）

插入一个 `DataTable`（第 1、2 列数据类型 `string`，第 3、4 列 `time`）和一个 `Comment` 对象。`endSim` 方法计算各零件类型的平均寿命并写入 Comment，再调用 `fillTable`：

```simtalk
var str := "MU Type, Lifetime"+strChr(13)+strChr(10)+"------------------------"
MySQLite.prepare("SELECT MUType, avg(EndTime-StartTime) FROM MUTrace GROUP BY MUType")
while MySQLite.step
   str := str+strChr(13)+strChr(10)+MySQLite.getColumnString(0)+", "+to_str(MySQLite.getColumnReal(1))
Comment.Text := str
fillTable     // name of the method that writes data to the DataTable
closeDatabase
```

**Method `fillTable`** 把各零件的寿命写入 DataTable：

```simtalk
// called by the endSim method
MySQLite.prepare("SELECT * FROM MUTrace")
for var column := 1 to MySQLite.getcolumnCount
    var row := 1
    while MySQLite.step
        switch column
        case 1,2 // column 1 and 2 of data type string
            DataTable[column,row] :=  MySQLite.getColumnString(column - 1)
        else // column 3 and 4 of data type time
            DataTable[column,row] :=  MySQLite.getColumnReal(column - 1)
        end
        row += 1
    end
next
DataTable.opendialog
```

## 10. 以 ANSI 格式导入/导出数据（Import or Export Data in ANSI Format）

可用 `FileInterface` 从文本文件导入仿真运行数据或导出数据到文本文件。`FileInterface` 只处理 ASCII 字符（字母、数字、特殊字符），并提供在文件内移动的方法。

从 Class Library 的 **InformationFlow**，或 **Information Flow** 工具栏插入 `FileInterface`。

- 输入要打开（导入）或保存（导出）的文本文件的 **Filename [FileInterface]**。
- `readLn` 方法打开文件、读取单行、内部行计数器加一并再次关闭文件。
- `readLn` 把读到的行转换为字符串。用字符串函数（`strCopy`、`strOmit`、`strLen`）和转换函数（`str_to_num`、`str_to_time` 等）处理这些字符串。
- 反复调用 `readLn` 移到下一行。`goToLine` 移到指定整数行，再由 `readLn` 导入该行。
- 连续多次访问同一文件时，预先打开它可提高访问速度；不再需要时关闭它。

> **注意：** `FileInterface` 任意时刻最多可保持打开十个文本文件。

写入时（如用 `write`），`FileInterface` 打开文件，用 `goBottom` 把内部行计数器设为末尾，保存数据并关闭文件。它总是在末尾追加新数据——不覆盖已有数据。反复访问同一文件时，预先打开它可在保存前缓冲数据；`FileInterface` 在下一次读取访问前或关闭时保存数据。

## 11. 显示外部程序中存储的数据（Display Data Stored in an External Program）

`FileLink` 可在 Plant Simulation 的 Frame 中放置指向文件的链接（快捷方式），从而直接在仿真模型内显示和编辑存储在外部程序中的数据。

从 Class Library 的 **InformationFlow**，或 **Information Flow** 工具栏插入 `FileLink`。

- 从桌面或 Windows 资源管理器把文件拖入 Plant Simulation Frame。`FileLink` 创建链接并把关联应用的图标放到 Frame 中。默认 Plant Simulation 把完整路径填入 **Label** 和 **File name**。
- 提示时选择是否嵌入文件：
  - **Yes：** 保存时把文件复制进模型文件。
  - **No：** 创建指向文件系统中文件的链接。
- 双击图标打开应用和文件进行编辑。
- 若链接无效，Plant Simulation 打开 `FileLink` 对话框，在 **File Name** 显示无效路径。右键图标选 **Open** 打开对话框。

可进行：在模型内打开格式化文本、在模型内打开图片、打开 Office 文档与 PDF 文件、在仿真模型中播放视频。

### 在模型内打开格式化文本（Open Formatted Text from within the Model）

要显示格式化文本，将其保存为 RTF 文件（可在 WordPad 中打开）。

- 在可保存 RTF 的程序（如 WordPad）中创建文档，应用格式，保存为 `MyRTFDocument.rtf`。
- 把 RTF 文件拖入 Frame。点击 **Yes** 嵌入。可选改 **Label**（如 `RTF Text`）。
- 转交给他人时，双击图标即在 WordPad 中打开。

### 在模型内打开图片（Open a Picture From Within the Model）

把图片保存为 BMP 或 PNG（可在 Paint 中打开）。

- 在可保存 BMP/PNG 的程序（如 Paint）中把图片保存为 `MyPicture`。
- 把文件拖入 Frame。Plant Simulation 询问是否用作背景图；点击 **No**，再点击 **Yes** 嵌入。可选改 **Label**（如 `png graphic`）。
- 双击图标即在 Paint 中打开图片。

### 打开 Office 文档与 PDF 文件（Open Documents From Office Applications and PDF Files）

以原生格式或 PDF 保存 Office 文档（目标计算机需安装 Microsoft Office 和 PDF 查看器）。

- 以原生格式保存文档（如 `MyPresentation` 为 PowerPoint `.pptx`），并另存为 PDF。
- 把 `.pptx` 文件拖入 Frame，点击 **Yes** 嵌入。可选改 **Label**（如 `PowerPoint presentation`）。双击即在 PowerPoint 中打开。
- 把 PDF 文件拖入 Frame，点击 **Yes** 嵌入。可选改 **Label**（如 `Presentation pdf`）。双击即在已安装的 PDF 查看器中打开。

### 在仿真模型中播放视频（Play a Video in Your Simulation Model）

用默认媒体播放器嵌入并播放视频：

- 用视频录制工具录制视频，保存为 `.avi` 文件（如 `MyVideo`）。
- 把 AVI 文件拖入 Frame，点击 **Yes** 嵌入。
- 双击 `FileLink` 用默认播放器播放视频。

## 目录说明

- `import-export-databases-external-media.md`：数据导入导出、数据库与外部媒体章节的 Markdown 版本（本总结的源文件）。
- `import-export-databases-external-media.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Import/Export, Databases, and External Media"。Unpublished work. © 2026 Siemens.*
