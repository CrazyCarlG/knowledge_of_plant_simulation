# Methods for Accessing Lists and Tables

Lists and tables provide the methods below for accessing them. Read and write access depend on the object class and are described in the sub-chapters.

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window. You can:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the attributes and methods of the selected Instance.

The methods apply to the objects `DataStack`, `DataQueue`, `DataList`, `DataTable`, and `TimeSequence` (unless noted otherwise).

---

## closeDialog [SimTalk] — lists

Closes the dialog box of the list object designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.closeDialog → boolean`
- **Return Value:** `boolean`

```simtalk
MyDataTable.closeDialog
MyDataList.closeDialog
MyDataStack.closeDialog
MyDataQueue.closeDialog
MyTimeSequence.closeDialog
```

---

## copy [SimTalk] — lists

Copies the entire list/table designated by `<Path>` and returns it as a value of data type list/table.

- `copy(Range)` copies the specified range.
- If no range is specified, Plant Simulation copies the entire list. A range may only encompass a single range.
- To also copy the column index and/or row index during the copy, enter column 0 and/or row 0 into the range.

- **Type:** Method
- **Syntax:**
  - `<Path>.copy → list or table`
  - `<Path>.copy(Range:listrange) → list or table`
- **Parameter:** `Range` (data type `listrange`) designates the range.
- **Return Value:** `list`/`table`

You can process the copied region in a number of ways:

**Assign the copied range to a local variable of the corresponding type:**

```simtalk
var MyDataList : list[integer]
MyDataList := MyDataList1.copy({1}..{5})
```

**Insert the copied range into the column of a table.** The column where you paste the range must have the same data type as the DataList:

```simtalk
MyDataTable.insertList(3,1,MyDataList.copy({1}..{5}))
```

**Make the copied range a DataList of its own.** Its data type is `list`, so you can assign it to a cell in a DataList of data type `list`:

```simtalk
MyDataList.insertList(2,tab.copy({1,1}..{1,5}))
```

---

## countMatches [SimTalk]

Counts how often the designated value occurs in the designated range of the list/table designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.countMatches(Value:any[, Range:any, CaseSensitive:boolean:=false]) → integer`
- **Parameters:**
  - `Value` (data type `any`): the value for which matching values are counted.
  - `Range` (optional, data type `any`): the range within which to look. If omitted, Plant Simulation searches the entire range `{1,1}..{*,*}`.
  - `CaseSensitive` (optional, data type `boolean`): sets whether the search is case-sensitive. Default is `false`.
- **Return Value:** `integer`

```simtalk
print MyDataTable.countMatches("a1", {1,1}..{3,12})
```

---

## delete [SimTalk] — lists

Deletes the contents of the list object designated by `<Path>`. `delete(Range)` deletes the specified range.

- **Type:** Method
- **Syntax:**
  - `<Path>.delete`
  - `<Path>.delete([Range:listrange, ...])`
- **Parameter:** `Range` (optional, data type `listrange`) designates the range to delete. Several ranges can be entered.
  - If no range is entered, Plant Simulation deletes the contents of all cells without the cells of the column or row index (equivalent to `{1,1}..{*,*}`).
  - To delete the user-defined row index or column index of DataTables, explicitly enter row 0 or column 0 in the range.

> **Note:** You can also delete sub-tables that inherit their contents with `delete`. The inheritance relation causes the reference to be passed to the origin, thus deleting the contents in the origin.

```simtalk
MyDataStack.delete                                -- deletes the data range
MyDataQueue.delete({2}..{4})
MyDataList.delete({1}..{5}, {8})
MyDataTable.delete({2,2}..{*,*})
MyDataTable.delete({0,1}..{0,*})                  -- deletes the row index
MyDataTable.delete({"ColumnB",0}..{"ColumnB",*})  -- deletes the column index
```

---

## insert [SimTalk] — lists

Adds additional entries to the list objects with one column designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.insert(Row:integer, Entry:any)`
- **Parameters:**
  - `Row` (data type `integer`): the number of the cell into which the value is inserted. All cells with the same or greater index are moved down one position. If the number is greater than the highest position, Plant Simulation adds it after the last current entry (gaps between entries are not allowed).
  - `Entry` (data type `any`): the value to insert. Its data type must match the list object's data type.

```simtalk
MyDataList.insert(2,12.24)
MyDataStack.insert(3,32.34)
MyDataQueue.insert(4,42.44)
```

---

## insertList [SimTalk]

Inserts the contents of a list into the DataTable or DataList designated by `<Path>`.

- Plant Simulation deletes existing data in a DataTable; in a DataList it moves the data to another position.

> **Note:** Copying a large amount of data from one list to another with `insertList` might be slow. For objects of type `DataTable`, use `copyRangeTo` instead, whose code executes much faster.

- **Type:** Method
- **Syntax:**
  - `<Path>.insertList(Cell:integer, SourceList:any)`
  - `<Path>.insertList(Column:integer, Row:integer, SourceList:any)`
- **Parameters:**
  - `Cell` (for DataList, data type `integer`): the cell from which on the contents are inserted.
  - `Column` (for DataTable, data type `integer`): the column of the cell from which on the contents are inserted.
  - `Row` (for DataTable, data type `integer`): the row of the cell from which on the contents are inserted.
  - `SourceList` (data type `any`): the contents of the list to insert.

```simtalk
var lst: list [string]
lst.create           -- create
lst.insert(1,"one")  -- enters value
lst.insert(2,"two")

MyDataList.insertList(3,lst)
DataTable.insertList(2,2,lst)
```

---

## intersection [SimTalk]

Returns those values that the ranges of the list/table designated by `<Path1>` share, i.e., where they intersect.

- Both ranges or lists/tables must have the same data type. The return value is a list with one column containing the shared items. Values may be listed more than once.

- **Type:** Method
- **Syntax:**
  - `<Path>1.intersection(Path2:any) → list`
  - `<Path>1.intersection(Range:any, Path2:any) → list`
  - `<Path>1.intersection(Range:any, Range:any) → list`
- **Parameters:**
  - `Range` (data type `any`): a range of the table.
  - `Path1` and `Path2` (data type `any`): two lists or tables.
- **Return Value:** `list`

```simtalk
-- the second column of the DataTable contains the numbers 2,4, ... 40
-- the third column contains the numbers 3,6, ... 60. The DataList
-- contains the square numbers from -10 to 10.
destination.delete
destination.insertList(2,1,MyDataTable.intersection(DataList))
-- the second column of the DataTable destination
-- contains the numbers 4,9,16,36,36
destination.insertList(3,1,MyDataTable.intersection({2,1}..{3,2},DataList))
-- the third column of the DataTable destination contains 4
dest.insertList(4,1,MyDataTable.intersection({2,1}..{2,*},{3,1}..{3,*}))
-- the fourth column of the DataTable
-- destination contains the numbers 6,12,18,24,30,36
```

---

## openDialog [SimTalk] — lists

Opens the window of the list/table designated by `<Path>`.

- Applies also to sub-tables and to user-defined attributes of data type `table`.

- **Type:** Method
- **Syntax:** `<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`
- **Parameter:** `CallOpenControl` (optional, data type `boolean`): sets whether the Open Control is executed (`true`) or not (`false`). Default is `false`.
- **Return Value:** `boolean`

```simtalk
MyDataTable.openDialog
MyDataStack.openDialog(true)
```

---

## openDialogBox [SimTalk]

Opens the window of the list object designated by `<Path>` as a dialog in front of all other windows and dialog boxes.

- The dialog box shows the contents in a uniform standard font, not with the Font Size and Font Color selected in the Format dialog.
- Deactivate the command `Inherit Contents`/`InheritContents` before attempting to type in data.
- Applies to `DataStack`, `DataQueue`, `DataList`, and `DataTable`.

> **Note:** The Close button in the title bar is deactivated to prevent accidentally canceling changes. You must decide what happens when closing the dialog by clicking **OK** or **Cancel**.

- **Type:** Method
- **Syntax:** `<Path>.openDialogBox([AutoSizeColumns:boolean:=false]) → boolean`
- **Parameter:** `AutoSizeColumns` (optional, data type `boolean`): sets whether column widths are calculated automatically according to the widest occupied cell for each column (`true`) or not (`false`). Default is `false`. Applies to objects of type `DataTable`, subtables, and user-defined attributes of data type `table`.
- **Return Value:** `boolean`

```simtalk
MyDataTable.openDialogBox
MyDataList.openDialogBox
```

---

## printList [SimTalk]

Prints the contents of the list designated by `<Path>`, without the icon and information about origin and class.

- The printout is identical to clicking **Print** on the List ribbon tab.

- **Type:** Method
- **Syntax:** `<Path>.printList([string]) → boolean`
- **Return Value:** `boolean`

```simtalk
MyDataQueue.printList
MyTimeSequence.printList
```

---

## refillDialog [SimTalk]

Fills the open dialog box of a list or table designated by `<Path>` with the current values.

- Especially helpful if you changed values via information flow and want to show them in a list/table opened as a dialog box. If the table was opened as a regular list window (not a dialog box), Plant Simulation always shows current values anyway; in this case the method recomputes any formulas in the list window.

> **Note:** Values changed in the dialog box but not applied will be discarded.

- **Type:** Method
- **Syntax:** `<Path>.refillDialog`

```simtalk
MyDataStack.refillDialog
MyDataQueue.refillDialog
MyDataList.refillDialog
MyDataTable.refillDialog
```

---

## showPrintDialog [SimTalk] — lists

Opens the **Print** dialog of the default printer set under MS Windows.

- **Type:** Method
- **Syntax:** `<Path>.showPrintDialog → boolean`
- **Return Value:** `boolean`

```simtalk
MyTimeSequence.showPrintDialog
```

---

## Methods for the Order of Cells within Lists and Tables

Lists and tables also provide methods (listed in the table of contents) for manipulating the order of cells. To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window.
