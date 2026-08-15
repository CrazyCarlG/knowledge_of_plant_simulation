# Lists, Tables, and Network Socket Exchange

## Working with Lists and Tables

Plant Simulation provides several types of lists that differ in how they access the data they contain. Use lists to supply material-flow objects with data during a simulation run, or to write results into lists, export them, and process them in other applications.

Available list objects (from the `InformationFlow` folder in the Class Library, or the *Information Flow* toolbar in the Toolbox):

| Object | Description |
| --- | --- |
| **DataList** | One column; accesses cells randomly by position. New cells can be added at any position; removing a cell shifts higher-numbered cells up. |
| **DataQueue** | One column; FIFO access — the first cell added is processed first. New cells are appended after the last cell. |
| **DataStack** | One column; LIFO access — the last cell added is processed first. Adding a cell to the top pushes existing cells down. |
| **DataTable** | Several columns; accesses cells by column and row number. New data overwrites existing cell contents. |
| **TimeSequence** | Two columns; accesses pairs randomly by column/row number, keeps entries in ascending time order. |

The procedures described are the same for all list types. Before changing settings, deactivate inheritance by deselecting the inheritance button on the *List* ribbon tab.

## Set the Data Type of a Column

For `DataList`, `DataStack`, and `DataQueue` (single-column lists) you set the data type for the entire list. For `DataTable` you can set the data type per column or for a range of columns.

- Deactivate inheritance on the *List* ribbon tab.
- Click *Edit Format* / *Format* on the *List* ribbon tab, or right-click the column and select *Format*.
- Click a column header to show the **Dimension** and **Data Type** tabs, then select a data type.

### Data Types

| Data type | Description |
| --- | --- |
| Acceleration | m/s² (for Conveyor, Track, TwoLaneTrack, Transporter) |
| Boolean | `true` or `false` |
| Date | date statement (`dd.MM.yyyy`) |
| DateTime | date + time (`dd.MM.yyyy HH:mm:ss`) |
| Integer | integer value |
| Length | floating point number (length unit) |
| List | one-column list (DataList properties) |
| Money | floating point number |
| Object | reference to a simulation model or object |
| Queue | one-column list (DataQueue properties) |
| Real | floating point number (e.g. `3.1415`) |
| Speed | floating point number (speed unit) |
| Stack | one-column list (DataStack properties) |
| String | characters, numbers, special characters |
| Table | one or more columns (DataTable properties) |
| Time | time statement (`hh:mm:ss.ss`) |
| Weight | floating point number (weight unit) |

Notes:
- Double-clicking a cell of type `string`/`boolean` with value `true`/`false` toggles the value.
- For `Integer`, `Real`, and `String` you can also enter a **Format String**.
- To hide the data type of cells, deselect *Data Type* on the *List* ribbon tab.

## Set the Dimension of a List

- Deactivate inheritance, then click *Format* (or right-click the column → *Format*).
- Set the **Column Width** (in character widths) for a single column or a selected range of columns.
- Click *Select All* (top-left corner, toolbar, or `Ctrl+A`) to limit the whole table size.
- Enter **Number of Rows** (all lists) and, for `DataTable`, **Number of Columns**. Leaving them empty makes the list unbounded (memory-consuming).
- Right-click a column → *Insert Column* (new column is data type `string`); right-click a row → *Insert Row*; right-click → *Cut* to delete a column/row.

## Set Alignment and Colors of Cells

- Deactivate inheritance, then click *Format* (or right-click the column → *Format*).
- Click the column/row header to select columns/rows to format (the **Range** box shows the selection).
- Select **Alignment**, **Font Size**, **Font Color**, and **Background Color**.

## Insert, Cut and Delete Rows and Columns

- **Insert Row**: right-click a cell in the row above which to insert → *Insert Row*.
- **Insert Column**: right-click a cell in the column to the left of which to insert → *Insert Column*. If you select the first column, the new column is inserted to its right; all other columns shift right.
- **Delete contents only** (keep empty row/column): right-click → *Delete* on the mini toolbar.
- **Clear a single cell**: double-click, right-click → *Delete*.
- **Remove entire row/column** (with contents): right-click the row/column header → *Remove Column*.

## Work with Data in a List or Table

- Click a cell (or the text box above the columns/rows) and type data. Typing into a cell that already contains data replaces its contents.
- Navigation keys:

| Key | Action |
| --- | --- |
| `Enter` | one cell down |
| `Shift+Enter` | one cell up |
| `Tab` | one cell right |
| `Shift+Tab` | one cell left |
| `Ctrl+Enter` | jump to start of the cell below |
| `Shift+Cursor Up/Down/Left/Right` | select a range |
| `Esc` | restore previous cell contents while editing |
| Arrow keys | move cursor within a cell |
| `Shift+Left/Right` | move between cells |

- Apply entered data with `Enter` or by moving to another cell.
- Move/copy cell contents with drag-and-drop; hold `Ctrl` while dragging to copy.
- Paste with *Home > Paste*; copy with *Home > Copy*.
- Select entire columns/rows via headers; select contiguous `DataTable` columns by dragging across headers.
- Select all with *Select All* or `Ctrl+A`.
- *Highlight Empty Cells* shows blank cells in a different color.
- To create a sublist in a `Table`/`List`/`Stack`/`Queue` cell, type its name/path or drag-and-drop it in.
- Open a sublist/object in a cell: `Shift` + double-click, or right-click → *Open Object*, or `F2`.
- Set standard column width via *List > Format > Dimension > Column Width*, or drag the column border (double-headed arrow).

## Work with Data in the DataTable

### Cut or Copy a Range of Cells
- Select a range by dragging from one corner to the opposite corner.
- *Home > Cut* removes the contents but leaves empty cells; pasting overwrites the target range.
- Clicking in the gray system-index area selects entire columns/rows; cutting removes and shifts remaining columns/rows.

### Drag-and-Drop in DataTables

| To do this | Drag from | To | Accelerator |
| --- | --- | --- | --- |
| Move the selected text | table window | table window | — |
| Copy the selected text | table window | table window | `Ctrl` |
| Insert selected text | any | table window | any |
| Copy the selected text | table window | any | `Ctrl` |
| Cut the selected text | table window | any | — |

### Insert a Range of Cells
Pasting a cut/copied range works only if the target range has the same number of columns/rows, or an integer multiple of them. Incompatible data types are marked in red.

### Hide and Show Columns
Drag the column's left/right border to the left until the columns disappear (hidden columns are marked with a symbol at the end of the preceding column). Drag over that symbol and click once to restore the columns to their original width.

### Insert a Drop-down List into a Cell
Select a cell of data type `String`, right-click → *Format* → *Data Type* tab. Enter terms separated by a semicolon (no trailing blank) into **Format String**. Example: `Entry1;Entry2;Random` creates a drop-down list with those entries.

> Note: Double-click the cell to actually show the drop-down list in the list window. When the list window is opened with `openDialogBox`, the drop-down list is shown immediately.

## Accessing Data in Lists

Access a cell with a **system index** (assigned number) or a **user-defined index** (a meaningful expression). User-defined indexes are more readable and more robust against insertions/deletions, but slightly slower:

```
Switch["Light","220 Volts"]
Vehicle["limo",#1]
Plant["Chicago",.building1.drill]
```

Available operations:
- Set the Column Index / Row Index.
- Create a User-defined Column and Row Index.
- Set and Get the Upper Bound of a List.
- Address Columns and Rows with Methods.

## Set the Column Index

- Click *Activate Column Index* on the *List* ribbon tab (clicking again deactivates it and deletes existing contents).
- Select the index row above the first data row and click *Format*; choose the index data type on the *Data Type* tab.
- Optionally enter a **Format String** (for `Integer`, `Real`, `String`).
- Select **Fast Index Access** for quicker access to the user-defined index.
- Select **Unique Index Key** to allow only unique entries.

## Set the Row Index

- Click *Activate Row Index* on the *List* ribbon tab.
- Select the index column → *Format* → choose data type on the *Data Type* tab.
- Optionally set **Format String**, **Fast Index Access**, and **Unique Index Key**.

## Create a User-defined Column and Row Index

- Deactivate inheritance.
- Click *Activate Column Index* and enter a meaningful term in the first index row. Usually choose `String`; for `Integer`, prefix the term with `#` to distinguish it from the system index.
- Click *Activate Row Index* and enter an expression in the first index column (same `#` rule for `Integer`).

> Note: When both indexes are active, cell `[0,0]` (the intersection) counts as part of the column index, not the row index.

## Set and Get the Upper Bound of a List

- Deactivate inheritance, select the entire list (*Select All* or `Ctrl+A`), and click *Format* (or right-click a column → *Format*).
- On the **Dimension** tab, enter **Number of Columns** and **Number of Rows**. The lower bound is automatically `1` (`0` for a user-defined index).
- Attributes:
  - One-column lists: `MaxDim`
  - Two-column lists: `MaxXDim`, `MaxYDim`
  - Tables: read-only `XDim`/`YDim` return current occupancy; `XDimIndex`/`YDimIndex` return the last occupied index cell.
- Use *Go To* on the *List* ribbon tab to move to a specific cell.

## Address Columns and Rows with Methods

### Set the Format of Columns and Rows
```
setXX(Parameter:any, ..., Parameter:any, Parameter:integer)
```
- The parameter count is always ≥ 2.
- The last parameter sets the column or row (system index or user-defined index).
- For a contiguous range, define a range with `*` for all rows/columns:

```
MyDataTable.setDataType({3,*}..{4,*},6,"column1","real")
```

| Entry | Designates |
| --- | --- |
| `{3,*}..{4,*}` | the range — all cells in columns 3 and 4 |
| `6` | the system index of a column |
| `"column1"` | a column index |
| `"real"` | a value |

### Get the Format of Columns or Rows
```
getXX(ColumnOrRow:any)
```
- The parameter count is always 1; `ColumnOrRow` may be a system or user-defined index.

```
MyDataTable.getDataType(1)  -- returns the data type of column 1
```

## Search Lists with Methods

Lists/tables have an internal cursor (`Cursor` attribute; `CursorX`/`CursorY` for tables). A search (e.g. `find`) starts at the current cursor position. After a successful search the cursor is placed in the found cell; a repeated `find` continues from there. If not found, the cursor stays where it was.

```
MyDataStack.find(12.34)
// finds the floating point value 12.34 starting from the current cursor
// position
MyDataQueue.find(42)
// finds the integer value 42 starting from the current cursor position
MyDataList.find({1},{4}..{8},"drill")
//finds the string "drill" in row 1 and in rows 4 to 8 starting from the
//current cursor position
MyDataTable.find("a")
// finds the string "a" in the entire table starting from the current
//cursor position
MyDataTable.setCursor(3,1)
// set cursor so that next find starts search from beginning
MyDataTable.find({3,*},"a")
// finds the string "a" in column 3 starting from the current cursor
//position
MyDataTable.find({1,1}..{4,*},"a")
// finds the string "a" in columns 1 to 4 in all rows starting from the
//current cursor position
var MyDataTable.setCursor(1,1)
// starts searching for "abc" from the beginning to the end
if MyDataTable.find("abc")
   print MyDataTable.CursorX, " ",MyDataTable.CursorY
else
   print "not found"
end
```

> Note: Set the cursor anew after inserting or deleting rows.

Example — checking which values already exist in a `DataTable`:

```
var lst : list; lst.create
for var i := 1 to DataTable5.YDim
   lst.setcursor(1)
   // Sets the cursor into the first cell. Searching starts there.
   if not lst.find(DataTable5[1, i])
   // Checks if a value already exists in the list variable.
      lst.append(DataTable5[1, i])
   end
next
promptListN(lst, "Found these values:")
// Presents all values in the list.
```

## Search Lists with the Find Dialog

Right-click in the list → *Find*, or press `Ctrl+F`.

- **Find What**: the search term.
- **Match Case**: case-sensitive search.
- **Match Entire Cell Contents**: exact full-cell match.
- **Search in Rows** or **Columns**: direction of the search.
- **Search Criterion**:
  - *Find* — finds the term (compare method `find`).
  - *Find ceil(ing)* — value ≥ search term (compare `findCeil`).
  - *Find floor* — value ≤ search term (compare `findFloor`).
- *Find Next* finds the next instance; *Replace* shows **Replace With** and replaces the term.

## Create Lists within Lists and Tables

To create a sublist/subtable in a `DataList`, `DataStack`, `DataQueue`, or `DataTable` cell:
1. Open the list object; deactivate inheritance.
2. Right-click the column header → *Format*.
3. Select the sublist data type: `Table`, `List`, `Stack`, or `Queue`.
4. Select **Common Format** if all sublists in that column should share formatting.
5. Apply formatting on the **Contents** tab, click OK (also possible via `setCommonFormat`).
6. Enter a name into the cells of the changed column to identify each subtable.
7. Hold `Shift` and double-click the subtable to open and edit it.

To insert a list object from a Frame/Class Library into a cell:
- Set the column data type to `Object`, then drag the table into a cell (inserts the absolute path). Type the list name to use a relative path when it is in the same Frame.
- Open sublists via `Shift`+double-click, right-click → *Open Object*, or `F2`.

## Sort DataList, DataTable, and TimeSequence

- **Sort Ascending** / **Sort Descending** on the context menu sorts the selected column.
- Methods: `sort` sorts ascending/descending; `inOrder` inserts a value into an existing sequence at the correct position.

## Calculate Values with a Formula

A **Formula** reads and links values of other cells and object attributes, then performs calculations (using the same operators/functions as Methods).

Procedure:
1. Click *Create Formula* on the *List* ribbon tab to activate formula mode.
2. Click a cell (or the text box above the list) and type the expression. Example: `@[1,2]+@[2,3]` adds cell `[1,2]` to cell `[2,3]`.
3. Press `Enter` to show the result.
4. Double-click the cell to show/edit the formula itself.

Cells with formulas are color-coded: turquoise = correct syntax, red = syntax errors.

### Access a Cell in a DataTable with `@` in a Formula

| Formula | Executes |
| --- | --- |
| `@[1,1]+@[1,2]` | adds contents of `[1,1]` to contents of `[1,2]` |
| `@[1,1]*track.length` | multiplies `[1,1]` by the length of object `track` |
| `@[1,@.ydim]+5` | adds 5 to the last cell in the first column |
| `@[xSelf+1,ySelf]-7` | subtracts 7 from the neighboring cell to the right |
| `@.sum({3,*})` | computes the sum of the third column |
| `@.min({1,2}..{1,*})` | smallest value of the first column, starting from cell 2 |

> Note: The formula result must have the same data type as the cell/column containing it.

Within a formula you can also access a local variable of data type `table` with the anonymous identifier `?`.

### Access a Sublist with `?`
In sublists, `?` accesses the list into which the sublist was inserted; for user-defined attributes, `?` accesses the object the attribute belongs to. `xSelf` and `ySelf` contain the column/row number of the formula cell.

### Catch Runtime Errors in Formulas
Add a user-defined attribute of data type `Method` named `ErrorHandler` to the `DataTable`. Assign an empty string (`""`) to the error message to suppress it; the handler can then return a new value for the faulty cell.

## Import or Export the Contents of a List

- **Export Object File** (`.psobj`): saves the list with all Plant Simulation formatting; import via *Import* on the *List* ribbon tab.
- **Export Text File**: saves only the contents, without formatting. Configure the separator via *Export > Text File Format*. Select encoding in the *Save As* dialog.
- **Export Excel File**: saves the contents as an Excel worksheet; enter the worksheet name.

Excel export type mapping:

| Plant Simulation data type | Excel data type | Excel format |
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

> Note: Integers are only exported in the range -536.870.912 to 536.870.911; values outside this range are saved as `0`. When reading Excel, columns should contain a single data type; row 0 is interpreted as a column index if present.

## Unshare a List or Data Table

Assigning a `Variable` of data type `table`/`list`/`stack`/`queue` to a subtable cell (or assigning one user-defined attribute to another) creates a **reference**, not a copy — changing one changes the other. Use `unshare` to use two independent values.

```
Variable := DataTable[1,1]
Variable[1,2] := "Value1" // Value1 appears in DataTable[1,1]
```

```
&Variable.unshare
Variable[1,2] := "Value2" // Value2 doesn't appear in DataTable[1,1]
```

## Open a List as a Dialog in the Foreground

By default list windows open in the background behind dialogs. Open them as foreground dialogs with `openDialogBox`:

```
SteeringTypes.openDialogBox
```

The dialog window provides a reduced set of functions on the ribbon tab and context menu, and applies entries only when you click *Apply* or *OK* (rather than as you type).

## Exchange Data via a Network Socket

Socket communication is point-to-point, established during initialization, and directly based on TCP/IP — fast with little data overhead. The `Socket` object provides the TCP/IP interface. One process acts as a server, others register as clients; Plant Simulation can be either.

Add the `Socket` object via *Manage Class Library > Basic Objects > Socket* on the *Home* ribbon tab, or insert it from `InformationFlow` in the Class Library / *Information Flow* toolbar.

### Model the Frame `ServerSocket`
Insert: a `Socket` object, a Callback Method, two Variables (`MessageReceived`, `MessageSent`), and a Method to send messages.

- Name the server Socket object (e.g. `MyServerSocket`); select the callback method and check only **On** and **Server Socket**.
- Protocol: **TCP** establishes a connection and guarantees delivery; **UDP** exchanges data without a connection (less overhead, no delivery guarantee).

Sending method (`sendMessages`):

```
var str: string
// generates a random number between 0 and 100
str := to_str(round(z_uniform(1,0,100),1))
// writes the value of the random number to the variable 'MessageSent'
MessageSent := str
// sends the message using channel 0
MyServerSocket.write(0,str)
```

Callback method (`MyCallbackMethod`):

```
param SocketChannelNo: integer, SocketMessage: string
// writes the value to the global variable 'MessageReceived'
if strLen(SocketMessage) = 1
   MessageReceived := to_str(strAscii(SocketMessage)) // byte received
else
   MessageReceived := to_str(SocketMessage)           // string received
end
 // writes the message to the Plant Simulation Console
print
"--------------------------------------------------------------------"
print self
print "Message: The number ", MessageReceived, " was received at ",
sysdate
```

### Model the Frame `ClientSocket`
Insert the same objects as the server. Name the client Socket object (e.g. `MyClientSocket`), select the callback method, and check **On** while **clearing** *Server Socket*.

Sending method (`sendMessages`):

```
var str: string
// generates a random number between 0 and 100
str := to_str(round(z_uniform(1,0,100),1))
// writes the value of the random number to the variable 'MessageSent'
MessageSent := str
// sends the message using channel 0
MyClientSocket.write(0,str)
```

Callback method (`MyCallbackMethod`):

```
param SocketChannelNo: integer, SocketMessage: string
// writes the value to the global variable 'MessageReceived'
if strLen(SocketMessage) = 1
    MessageReceived := to_str(strAscii(SocketMessage)); // byte received
else
    MessageReceived := to_str(SocketMessage); // string received
end
// writes the message to the Plant Simulation Console
print
"--------------------------------------------------------------------"
print self
print "Message: The number ", MessageReceived, " was received at ",
sysdate; )
```

### Run
1. Activate **On** in `MyServerSocket` and `MyClientSocket`.
2. Right-click `sendMessages` in the `ServerSocket` Frame → *Run*.
3. Watch the variables and the Console: the value computed (e.g. `1.8`) is written to `MessageSent` in the server and appears in `MessageReceived` in the client.
