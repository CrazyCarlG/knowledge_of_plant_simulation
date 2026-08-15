# Import and Export Data, Databases, and External Media

> Source: Plant Simulation Help — Import/Export, Databases, and External Media (© 2026 Siemens)

## Overview

This section covers how to import and export data for simulation, work with databases, and display data stored in external programs.

As a rule, data is imported from a spreadsheet program (such as Microsoft Excel) or from a database into a Plant Simulation list or table. You filter out the data you actually need, and the material flow objects can then access these lists and use the data for simulation. You may also export data produced by simulation runs for use in other programs.

Plant Simulation provides several ways to import data:

- Import a Text File or an Object File into a List
- Import Data from a Microsoft Excel Worksheet
- Import a List of Services, Shifts, etc. into an Object
- Import Data in XML Format
- Import Data from a Database
- Import or Export Data in ANSI Format
- Import or Export the Contents of a List

---

## Import a Text File or an Object File into a List

The Plant Simulation lists `DataTable`, `DataList`, `DataQueue`, `DataStack`, and `TimeSequence` can open text files, Plant Simulation object files, XML files, and Microsoft Excel files.

- Before opening a text file, select the correct data type for each column of the DataTable. If the text file has a column header you want to reuse, activate and show the column index.
- To open a text file or object file in a list, click **Import File** on the List ribbon tab, navigate to the folder, select the file type, and click **Open**.
- Plant Simulation opens an object file with its original formatting. For text files, you must manually select the correct data types.
- To export the contents of a list or table, click **Export to File** or **Export Object File** on the List ribbon tab.

---

## Import Data from a Microsoft Excel Worksheet

When Plant Simulation reads an MS Excel table, it attempts to convert the values in each column to the data types of the columns in your Plant Simulation table. This only works when each Excel column contains a single data type (e.g., an entire column of type `String`).

After importing, check the data types, correct any as needed, and filter out unneeded data. You can do this manually or by programming a Method to manipulate the data while importing.

- Example file: `MyTestData.xlsx`.
- To open the Excel file in a Plant Simulation table, click **Import File** on the List ribbon tab, select the file, click **Open**, choose the worksheet, and click **OK**.
- To export a list or table as an Excel file, click **Export Excel File** on the List ribbon tab.

---

## Import a List of Services, Shifts, etc. into an Object

In most cases, importing such lists involves two lists:

1. A **main list** containing placeholder expressions (for example, operation names such as `Operations for MyPart A`).
2. A **sublist** containing the actual station names and information pertaining to them.

To import a services list, shift list, or worker creation table into an embedded list of an object:

- Open the received file in a text editor. Ensure the text shown in the column header is the first line. Separate columns with tabs. Save as a text file (`.txt`).
- Open the Plant Simulation object and change to the **Importer** tab. Click the inheritance check box to the right of **Services** on the sub-tab **Processing**, then click **Services**.
- Right-click in the list and click **Import**. Navigate to the saved text file and click **OK**.
- To export the contents of an embedded list as a tab-delimited text file, right-click in the list and select **Export**.

---

## Import Data in XML Format

You can import data stored in XML format and extract data from the XML file. For example, use the `XMLInterface` to read data exported from **Process Designer** (Siemens' program for planning, analyzing, and managing manufacturing processes) or from an XML database.

After importing and manipulating data with a Method, use the methods `write` and `writeElement` to write simulation results back to an XML file.

To get the most out of `XMLInterface`, you should be familiar with **XPath** (see http://www.w3.org/TR/xpath) and with **SimTalk** programming.

You can insert the `XMLInterface` from the folder **InformationFlow** in the Class Library or from the toolbar **Information Flow** in the Toolbox.

You can:

- Select File Name, Context, and Import Method
- Read and Write Data Sequentially
- Read and Access Data Randomly
- Access and Traverse Data Randomly

### Select File Name, Context, and Import Method

In the dialog of the `XMLInterface`:

- **File Name**: the XML file the `XMLInterface` opens (import) or the file it saves (export).
- **Context**: the node of the XML document structure at which reading starts (for example `Data/Objects`). This restricts the data read. Without a context, the entire file is imported, which may consume significant time and RAM.
- **Import Method**: click to enter the path and name of the Method that extracts and sequentially processes the imported data.

### Read and Write Data Sequentially

You can sequentially read data line-by-line, write it to an Import Method, and immediately process it line-by-line. Enter a **Context** to restrict the amount of data imported.

Example — sequentially writing an XML file:

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
       // adds an attribute to the item 'author'
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

### Read and Access Data Randomly

Plant Simulation can read the data in its entirety and then randomly process it as a whole. It imports the entire document first, then processes and analyzes all data in your Method. Random access requires all data to be in RAM — the larger the amount of data, the more RAM the `XMLInterface` uses.

**Select data from the XML document:**

```simtalk
// randomly accesses data via XPath instructions
var tbl:table
XMLInterface.FileName := "D:\MSXML 4.0\books.xml"
// load the XML document for random access into RAM
XMLInterface.openDocument
// select nodes via XPath instruction
// selection starts at the Context node which you entered in the
XMLInterface
// the second parameter is the selection depth for each node
// 0 means that no children will be selected
// the result is passed to a table
tbl := XMLInterface.getNodes("book[title='Midnight Rain']", 1)
XMLInterface.close
```

**Delete existing data from the XML document:**

```simtalk
// deletes all nodes specified by XPath instructions
XMLInterface.FileName := "D:\MSXML 4.0\books.xml"
// load the XML document for random access into RAM
XMLInterface.openDocument
// delete all book nodes of genre 'Fantasy'
XMLInterface.deleteNodes("book[genre = 'Fantasy']")
XMLInterface.FileName := "D:\MSXML 4.0\tmp.xml"
// write the document to a file
XMLInterface.write
// remove the document from RAM
XMLInterface.close
```

**Insert new data into the XML document:**

```simtalk
// inserts new data into the XML document
var tbl:table
XMLInterface.FileName := "D:\MSXML 4.0\books.xml"
// load the XML document
XMLInterface.openDocument
// get an empty table for writing the data to
// depth=1 means that we want to write nodes with children
tbl := XMLInterface.getContainer(1)
// set the parent node for the new data
XMLInterface.setContext("/catalog")
// designate the node to append to the 'catalog' nodes
tbl[1,1] := "book"
// are the attributes of the 'book' node
tbl.createNestedList(4,1)
// explicit namespace
tbl[4,1][1,1] := "xmlns:aa"
tbl[4,1][2,1] := "specAth"
// additional attributes
tbl[4,1][1,2] := "id"
tbl[4,1][2,2] := "bk113"
// child nodes
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
// save the changed document
XMLInterface.FileName := "D:\MSXML 4.0\tmp.xml"
XMLInterface.write
// close the document
XMLInterface.close
```

**Update the XML document:**

```simtalk
// updates the selected nodes of the document
var tbl:table;
XMLInterface.FileName := "D:\MSXML 4.0\books.xml"
XMLInterface.openDocument;
// select the nodes to be changed
tbl := XMLInterface.getNodes("/catalog/book[title='Midnight Rain']", 1)
// update the values
tbl[5,1][3,3] := "TEST"
// write the changed values
XMLInterface.updateNodes(tbl)
XMLInterface.FileName := "D:\MSXML 4.0\tmp.xml"
XMLInterface.write
XMLInterface.close
```

**Create a new XML document:**

```simtalk
// creates a new document by calling the method newDocument
var tbl:table;
XMLInterface.newDocument("catalog")
tbl := XMLInterface.getContainer(1)
XMLInterface.setContext("/catalog")
// parent node
tbl[1,1] := "book"
// default namespace
tbl[2,1] := "MyBooks"
// attributes
tbl.createNestedList(4,1)
// explicit namespace
tbl[4,1][1,1] := "xmlns:aa"
tbl[4,1][2,1] := "specAth"
// additional attributes
tbl[4,1][1,2] := "id"
tbl[4,1][2,2] := "bk113"
// child nodes
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

### Access and Traverse Data Randomly

You can extract data in its entirety and then randomly traverse it. For example, define the starting point with `selectNodes`, get the next node with `getNodeName`, check for attributes with `getNumberAttributes`, output attribute names, and recursively check children.

```simtalk
// selects the starting nodes and calls the method visitChildren
// recusively for each node
var numberAttributes
XMLInterface.FileName := "D:\Public\XML\books.xml"
// load the XML document to be randomly accessed into RAM
XMLInterface.openDocument
// select some nodes using XPath instructions
XMLInterface.selectNodes("book[genre = 'Computer']")
// define the loop for the selected nodes
while XMLInterface.getNextNode = true
   print XMLInterface.getNodeName
   // check for attributes of the nodes
   numberAttributes := XMLInterface.getNumberAttributes
   for var i := 0 to numberAttributes-1
       // print the data of the attributes
       print XMLInterface.getAttributeName(i)+":"
+XMLInterface.getAttributeValue(i)
   next
   // check the children of the current node
   VisitChildren
end
// remove the XML document from RAM
XMLInterface.close
```

---

## Import Data from a Database

You can import data from a database into Plant Simulation, run simulations with it, and write results back. To get the most out of this, you should be familiar with **SQL** (see http://sqlzoo.net) and with **SimTalk** programming.

You can:

- Import Data from an ODBC Database
- Import Data from an Oracle Database
- Exchange Data with an SQL Database

---

## Import Data from an ODBC Database

To import data from an ODBC database, use the Plant Simulation object `ODBC`. To access several databases at the same time, insert several `ODBC` objects, each communicating with a different database.

> **Note:** The example below only runs if 64-bit ODBC drivers are installed on your 64-bit Windows operating system. You cannot install 64-bit ODBC drivers in parallel with a 32-bit version of Microsoft Office.

You can access the same database with several ODBC objects, but this is discouraged as it may result in inconsistent data caused by conflicting commands (e.g., one Method deletes a data set while another attempts to access it). Using a single ODBC object ensures the sequence of instructions conforms to your intentions. This is especially true for real databases where data manipulations (read, write, delete, etc.) must be applied with the SQL instruction `commit`.

To import data from an ODBC database:

1. Set the Data Source Up
2. Import Data into Your Simulation Model

After simulation runs finish, you can export results back to the database.

### Set the Data Source Up

- Type **ODBC Data Sources (64-bit)** into the Search text box.
- In the **ODBC Data Source Administrator** dialog, add a new data source on the **User DSN** or **System DSN** tab (usually **System DSN**).
  - Click **Add** on the **System DSN** tab.
  - In **Create New Data Source**, select the ODBC driver (e.g., **Microsoft Access Driver**) and click **Finish**.
  - Click **Select** in **ODBC Microsoft Access Setup**, select the database, and type the **Data Source Name**. Optionally add a **Description**. Plant Simulation addresses the database with this name, so mind the Plant Simulation naming conventions.
  - Click **Select** and select the database to which you want to connect.

### Import Data into Your Simulation Model

After setting up the ODBC data source, insert the `ODBC` object into your model. It establishes the connection and enables importing data into Plant Simulation tables.

- To add `ODBC` to the toolbar **Information Flow**, click **Manage Class Library > Basic Objects > InformationFlow** on the Home ribbon tab, then insert the object.

Typical setup includes:

- An `ODBC` object (controls communication with the database).
- A Method for reading data from the database.
- A Method for writing data to the database.
- A Plant Simulation `DataTable` for importing/exporting data.

- Double-click the `ODBC` object and type the database name in **Database** (e.g., `TestDB`). For databases with user management (SQL Server, Oracle, etc.), also enter **User name** and **Password**. Click **Apply**, then **Login**.

When settings work, Plant Simulation dims the database name box and shows **Ok** in **Message**. Otherwise, an error message appears.

Reading and writing only works while connected; the methods `login` and `logout` frame the database operation:

```simtalk
ODBC.login("TestDB","","")
// database operation
ODBC.logout
```

To read data and write query results into a Plant Simulation table (or a local variable), start with the `sql` command, then define the target table, then enter SQL queries within quotation marks:

```simtalk
ODBC.login("TestDB","","")
ODBC.sql(Orders, "select * from Orders2")
ODBC.logout
```

To format the target table columns according to database formatting while reading, check **Format table** in the `ODBC` object dialog. This only applies when Plant Simulation provides formats corresponding to the database formats (Plant Simulation does not provide a counterpart for the typical Oracle date format).

For large amounts of data, prefer SQL queries with filters, as they are often considerably faster than searching large Plant Simulation tables:

```simtalk
ODBC.login("TestDB","","")
ODBC.sql(Orders, "select DeliveryTime, Amount from Orders2 where MU =
'.MUs.panel'")
ODBC.logout
```

### Export Data to the Database

You can export selected simulation results back to the ODBC database using the `sql` method and SQL instructions.

Add a new row with `insert into`:

```simtalk
ODBC.login("TestDB","","")
ODBC.sql("insert into Orders2 values ('15:00:00.0000', '.MUs.NewPart',
'150', 'NewPart', 'abc')")
ODBC.logout
```

> **Note:** SQL does not provide a single statement for adding the contents of a row or entire table, so you must type the contents of each cell into the Method.

Update existing data with the `update` instruction:

```simtalk
ODBC.login("TestDB","","")
ODBC.sql("update Orders2 set Attribute = 'xyz' where Name = 'rod'")
ODBC.logout
```

---

## Import Data from an Oracle Database

Use the object `Oracle11g`/`Oracle19c` much like the `ODBC` object. First establish a connection with a database instance on the Oracle Server; that instance determines the database name you type into the object.

Microsoft Windows does not provide Oracle settings. If the Oracle Server is not installed on the same computer as Plant Simulation, install an Oracle Client to establish the connection (contact your Oracle provider if it is not included).

For large amounts of data, `Oracle11g` performs better and provides more commands than `ODBC`.

- To add `Oracle11g` to the toolbar **Information Flow**, click **Manage Class Library > Basic Objects > InformationFlow > Oracle11g** on the Home ribbon tab, then insert the object.

> **Note:** You can also use ODBC together with Oracle — then you do not need an Oracle Client. Be aware that the SQL instructions you use are not necessarily compatible with the ODBC version. For switching between Oracle and Access databases for testing, use ODBC for all databases.

---

## Exchange Data with an SQL Database

Plant Simulation can exchange data with an SQL database using the object `SQLite`.

- To add `SQLite` to the toolbar **Information Flow**, click **Manage Class Library > Basic Objects > InformationFlow > SQLite** on the Home ribbon tab, then insert the object.

This sample model demonstrates using `SQLite` to connect Plant Simulation with an SQL database:

- `MySQLite` uses a database stored in main memory instead of a file on the hard disk.
- `openDatabase` opens the database and creates a table using SQL statements.
- `SourcePart` and `SourcePallet` produce parts; when parts leave the Sources, `enterCreationTime` records part type and creation time.
- When parts reach the Drain, `enterDeletionTime` records the time parts leave the plant.
- The simulation runs for six days; `endSim` computes average lifetime of parts, and `fillTable` writes results into a Plant Simulation table.
- `closeDatabase` (called by `endSim`) closes the database.

To create the model:

1. Configure the Connection with the SQL Database
2. Configure the Material Flow Through the Facility
3. Import the Simulation Results From the Database and Show Them

Compare sample models: **Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples > Category > Information Flow > Topic > SQLite Introduction**.

### Configure the Connection with the SQL Database

- Insert the `SQLite` object (named `MySQLite`), using the default `:memory:` setting — the database is stored in main memory for better performance. Note that all data is lost when Plant Simulation closes or crashes. To keep data, enter a database file name.

**Method `openDatabase`:**

```simtalk
// called by the init method
MySQLite.open          // opens the database
MySQLite.exec("CREATE TABLE MUTrace (MUName TEXT PRIMARY KEY, MUType
TEXT, StartTime REAL, EndTime REAL)")
// creates the table MUTrace in the database with four columns containing
the
// name of the part, the type of the part, the start time, and the end
time
```

**Method `closeDatabase`:**

```simtalk
// called by the endsim method
MySQLite.close // closes the database
```

**Method `reset`** (called when clicking Reset Simulation in the EventController) deletes DataTable contents and result numbers from the Comment:

```simtalk
DataTable.delete
DataTable.closeDialog
Comment.Text :=  "MU Type,
Lifetime"+strChr(13)+strChr(10)+"------------------------"
```

**Method `init`** shows `Processing...` and opens the database:

```simtalk
Comment.Text := "Processing..."
openDatabase
```

### Configure the Material Flow Through the Facility

- Insert two `Source` objects producing different part types (`SourcePart` produces type `Part`, `SourcePallet` produces type `Container`). Select the same rear-triggered Exit Control for both Sources.

**Method `enterCreationTime`** inserts creation times, type, and start time into `MUTrace`, then binds and executes the SQL statement:

```simtalk
MySQLite.prepare("INSERT INTO MUTrace (MUName, MUType, StartTime) VALUES
(?1, ?2, ?3)")
MySQLite.bindString(1, obj_to_str(@))
MySQLite.bindString(2, @.name)
MySQLite.bindReal(3, EventController.simTime)
MySQLite.step
```

- Insert four `Station` objects to process the parts.
- Insert the `Drain`, which removes parts from the plant, using `enterDeletionTime` as the Entrance Control.

**Method `enterDeletionTime`** updates `MUTrace` with deletion time:

```simtalk
MySQLite.prepare("UPDATE MUTrace set EndTime = ?1  WHERE MUName = ?2")
MySQLite.bindReal(1, EventController.simTime)
MySQLite.bindString(2, obj_to_str(@))
MySQLite.step
```

### Import the Simulation Results From the Database and Show Them

Insert a `DataTable` (column 1 and 2 data type `string`, column 3 and 4 data type `time`) and a `Comment` object. The `endSim` method computes the average lifetime of part types and writes the result into the Comment, then calls `fillTable`:

```simtalk
var str := "MU Type,
Lifetime"+strChr(13)+strChr(10)+"------------------------"
MySQLite.prepare("SELECT MUType, avg(EndTime-StartTime) FROM MUTrace GROUP
BY MUType")
while MySQLite.step
   str := str+strChr(13)+strChr(10)+MySQLite.getColumnString(0)+",
"+to_str(MySQLite.getColumnReal(1))
Comment.Text := str
fillTable     // name of the method that writes data to the DataTable
closeDatabase
```

**Method `fillTable`** writes the lifetime of individual parts into the DataTable:

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

---

## Import or Export Data in ANSI Format

You can import data for a simulation run from, or export data to, a text file using the `FileInterface`. The `FileInterface` only processes ASCII characters (letters, numbers, special characters) and provides methods to move within the file.

Insert the `FileInterface` from **InformationFlow** in the Class Library or the **Information Flow** toolbar.

- Enter the **Filename [FileInterface]** of the text file to open (import) or save (export).
- The method `readLn` opens the file, reads a single line, increases the internal line counter by one, and closes the file again.
- `readLn` transforms the read line into a string. Manipulate these strings with string functions (`strCopy`, `strOmit`, `strLen`) and conversion functions (`str_to_num`, `str_to_time`, etc.).
- Calling `readLn` repeatedly moves to the next line. `goToLine` moves to the line specified as an integer, then `readLn` imports that line.
- To access the same file several times in a row, open it beforehand to increase access speed. Close it when no longer needed.

> **Note:** The `FileInterface` can keep ten text files open at any one time.

When writing (e.g., with `write`), the `FileInterface` opens the file, sets its internal line counter to the end via `goBottom`, saves the data, and closes the file. It always appends new data to the end — it does not overwrite existing data. To access the same file repeatedly, open it beforehand to buffer data before saving; the `FileInterface` saves data before the next reading access or when closing.

---

## Display Data Stored in an External Program

The `FileLink` lets you place a link (shortcut) to a file into a Frame within Plant Simulation, enabling you to display and edit data stored in external programs directly within your simulation model.

Insert the `FileLink` from **InformationFlow** in the Class Library or the **Information Flow** toolbar.

- Drag a file from the Desktop or Windows Explorer into a Plant Simulation Frame. The `FileLink` creates a link and places the icon of the associated application in the Frame. By default, Plant Simulation enters the full path into **Label** and **File name**.
- When prompted, choose whether to embed the file:
  - **Yes:** copies the file into the model file when you save.
  - **No:** creates a link to the file in the file system.
- Double-click the icon to open the application and file for editing.
- If the link is invalid, Plant Simulation opens the `FileLink` dialog showing the invalid path in **File Name**. Right-click the icon and select **Open** to open the dialog.

You can:

- Open Formatted Text from within the Model
- Open a Picture From Within the Model
- Open Documents From Office Applications and PDF Files
- Play a Video in Your Simulation Model

### Open Formatted Text from within the Model

To show formatted text, save it as an RTF file (openable in WordPad).

- Create the document in a program that can save RTF (e.g., WordPad), apply formatting, and save as `MyRTFDocument.rtf`.
- Drag the RTF file into the Frame. Click **Yes** to embed. Optionally change the **Label** (e.g., to `RTF Text`).
- When passed to another person, double-clicking the icon opens it in WordPad.

### Open a Picture From Within the Model

Save the picture as BMP or PNG (openable in Paint).

- Save the picture in a program that can save BMP/PNG (e.g., Paint) as `MyPicture`.
- Drag the file into the Frame. Plant Simulation asks whether to use it as a background image; click **No**, then click **Yes** to embed. Optionally change the **Label** (e.g., `png graphic`).
- Double-clicking the icon opens the picture in Paint.

### Open Documents From Office Applications and PDF Files

Save Office documents in native format or as PDF (requires Microsoft Office and a PDF Viewer on the target computer).

- Save the document in the native format (e.g., `MyPresentation` as PowerPoint `.pptx`), and also save as PDF.
- Drag the `.pptx` file into the Frame and click **Yes** to embed. Optionally change the **Label** (e.g., `PowerPoint presentation`). Double-clicking opens it in PowerPoint.
- Drag the PDF file into the Frame and click **Yes** to embed. Optionally change the **Label** (e.g., `Presentation pdf`). Double-clicking opens it in the installed PDF Viewer.

### Play a Video in Your Simulation Model

To embed and play a video with the default media player:

- Record the video in a video recording tool and save it as an `.avi` file (e.g., `MyVideo`).
- Drag the AVI file into the Frame and click **Yes** to embed.
- Double-click the `FileLink` to play the video with the default player.
