# Methods of the DataTable

The DataTable provides the following method groups:

- Methods of Columns of the DataTable
- Methods of Rows of the DataTable
- Miscellaneous Methods of the DataTable
- Methods for Accessing the DataTable
- Methods for Instantiating the DataTable
- The shared Methods of Lists and Tables
- The shared Methods of All Objects

To view all methods, read-only attributes, and attributes of an object, open the window **Show Attributes and Methods** (select it on the Class Library context menu, or press `F8` / click it on the Home ribbon tab of the Frame containing the instance).

## Syntax conventions

An example syntax line:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier and data type of parameters) is listed in parentheses. `(Parameter:string)` designates a parameter of data type `string`.
- Optional parameters are listed in brackets, e.g. `[,Parameter:boolean]`.
- If a parameter has a default value, the signature shows it after the parameter.
- If the method has a return value, the signature shows its data type after the arrow `->`.
- Always enter parentheses for expressions within parentheses, otherwise unexpected results may occur and the Debugger may open.

**Abbreviations used in signatures:**

| Argument | Data type | Range of values |
|---|---|---|
| integer | integer | integer greater than zero |
| any | all data types | depending on the data type |
| listrange | — | a range |
| direction | string | `"up"`, `"down"`, `" "` |
| attributes | string | name of an attribute |

---

## Methods of Columns of the DataTable

The first parameter designates the column (column index, column range, or column number).

### cutColumn

Cuts the designated column, including all of its data. Plant Simulation shifts all columns with an equal or greater index to the left. The column index cannot be cut with `cutColumn(0)`.

```
<Path>.cutColumn(Column:any) → boolean
```

```simtalk
MyDataTable.cutColumn(8)
```

### getAlignmentColumn

Returns the alignment of the specified column (`"Left"`, `"Right"`, or `"Centered"`).

```
<Path>.getAlignmentColumn(Column:any) → string
```

```simtalk
print MyDataTable.getAlignmentColumn(4)
```

### getBackgroundColorColumn

Returns the background color of the specified column.

```
<Path>.getBackgroundColorColumn(Column:any) → integer
```

```simtalk
print MyDataTable.getBackgroundColorColumn(4)
```

### getColumnNo

Searches for the column containing a user-defined column index. Works only for simple data types (string, integer, etc.). Returns the column number, or `-1` if the column index does not exist.

```
<Path>.getColumnNo(ColumnIndex:any) → integer
```

```simtalk
var column : integer
column := MyDataTable.getColumnNo("Urgent")
```

### getColumnUniqueValues

Returns an array with the values contained exactly once in the specified column. The column must be of data type String, Integer, Real, Time, Money, Length, Weight, Speed, Acceleration, Date, or DateTime.

```
<Path>.getColumnUniqueValues(Column:any) → any[]
```

```simtalk
print MyDataTable.getColumnUniqueValues(1)
```

### getColumnWidth

Returns the width of the specified column.

```
<Path>.getColumnWidth(Column:any) → integer
```

```simtalk
MyDataTable.getColumnWidth(1)
print MyDataTable.getColumnWidth(1)
```

### getColumnYDim

Returns the number of the last cell of the specified column that contains an entry. Returns `0` if the column is empty.

```
<Path>.getColumnYDim(ColumnNumber:integer) → integer
```

```simtalk
MyDataTable.getColumnYDim(1)
print MyDataTable.getColumnYDim(1)
```

### getCommonFormat

Returns whether Common Format of the specified column is turned on (`true`) or off (`false`).

```
<Path>.getCommonFormat(Column:any) -> boolean
```

```simtalk
print MyDataTable.getCommonFormat(3)
```

### getDataType

Returns the data type of the specified column.

```
<Path>.getDataType(Column:any) → string
```

```simtalk
print MyDataTable.getDataType(1)
```

### getEditorRightsColumn

Returns the editor rights of the specified column (`true` for read-only access, `false` for read and write access).

```
<Path>.getEditorRightsColumn(Column:any) → boolean
```

```simtalk
MyDataTable.getEditorRightsColumn(1)
print MyDataTable.getEditorRightsColumn(1)
```

### getFontColorColumn

Returns the font color of the specified column.

```
<Path>.getFontColorColumn(Column:any) → integer
```

```simtalk
MyDataTable.getFontColorColumn(2)
print MyDataTable.getFontColorColumn(3)
```

### getFontSizeColumn

Returns the font size of the specified column. `1` = Small, `2` = Medium, `3` = Large, `4` = Extra Large.

```
<Path>.getFontSizeColumn(Column:any) → integer
```

```simtalk
print MyDataTable.getFontSizeColumn(2)
```

### getFormatString

Returns the format string of the specified column.

```
<Path>.getFormatString(Column:any) → string
```

```simtalk
tab1.getFormatString("paint")
print tab1.getFormatString(1)
```

### getVisibility

Returns whether a column is visible (`true`) or hidden (`false`).

```
<Path>.getVisibility(Column:any) → boolean
```

```simtalk
print MyDataTable.getVisibility(4)
```

### insertColumn

Adds an empty column to the left of the specified column. Plant Simulation shifts columns with an equal or greater index one position to the right.

```
<Path>.insertColumn(Column:any) → boolean
```

```simtalk
MyDataTable.insertColumn(8)
```

### isAlignmentColumn

Returns whether the alignment of the specified column matches the designated value (`true`) or not (`false`).

```
<Path>.isAlignmentColumn(Column:any, Alignment:string) → boolean
```

Alignment can be `"Right"`, `"Left"`, or `"Center"`.

```simtalk
print MyDataTable.isAlignmentColumn("column4","right")
```

### setAlignmentColumn

Sets the alignment of column(s). Alignment can be `"Left"`, `"Right"`, or `"Centered"`.

```
<Path>.setAlignmentColumn(Column:any [,Column:any,...], Aligmnent:string)
```

```simtalk
MyDataTable.setAlignmentColumn(1,"right")
MyDataTable.setAlignmentColumn(1,2,"right")
```

### setBackgroundColorColumn

Sets the background color of column(s). Color: `1` = Black, `2` = Red, `3` = Green, `4` = Blue, `5` = Magenta, `6` = Yellow, `7` = Cyan. Set RGB values with `makeRGBValue`.

```
<Path>.setBackgroundColorColumn(Column:any[, Column:any,...], BackgroundColor:integer)
```

```simtalk
var rgb: integer
// sets the background color of column 2
MyDataTable.setBackgroundColorColumn(2,makeRGBValue(120,0,0))
// sets the background color of columns 3 and 5
MyDataTable.setBackgroundColorColumn(3,5,makeRGBValue(120,10,0))
print MyDataTable.getBackgroundColorColumn(2)
MyDataTable.setBackgroundColorColumn(1,1)
// sets the background color of column 1 to black
MyDataTable.setBackgroundColorColumn(1,2,2)
// sets the background color of columns 1 and 2 to red
```

### setColumnWidth

Sets the width of one or several columns (in character widths of a non-proportional font).

```
<Path>.setColumnWidth(Column:any[, Column:any, ...], ColumnWidth:integer)
```

```simtalk
MyDataTable.setColumnWidth("column12",10)
```

### setCommonFormat

Assigns the same format to all columns within the designated range. If Common Format is activated for a column, assigning a subtable to a table cell creates a copy of the assigned table; otherwise a reference is entered.

```
<Path>.setCommonFormat(Column:any[, Column:any, ..., ]CommonFormat:boolean)
```

```simtalk
// activate common format for the columns 3 to 5, for column 7 and for the
// column with the user-defined column index "mycolumn".
MyDataTable.setCommonFormat({3,*}..{5,*},7,"mycolumn", true)
MyDataTable.setDataType(3,"Table")
MyDataTable.setCommonFormat(3,true) -- formats the subtable within the table
MyDataTable.createNestedList(3,1)
MyDataTable[3,1].setDataType(2,"Boolean")
MyDataTable.createNestedList(3,7)
MyDataTable[3,7][2,77] := true
```

### setDataType

Sets the data type of the specified column(s).

```
<Path>.setDataType(Column:any, [Column:any, ..., ]DataType:string)
```

| Data type | Description |
|---|---|
| Acceleration | applies for Conveyor, Track, TwoLaneTrack, Transporter; meter per second squared |
| Boolean | true or false |
| Date | date statement (dd.MM.yyyy) |
| DateTime | date statement including time (dd.MM.yyyy HH:mm:ss) |
| Integer | integer value |
| Length | floating point number, depends on the length unit |
| List | list with one column, shares DataList properties |
| Money | floating point numbers |
| Object | reference to a simulation model or an object |
| Queue | list with one column, shares DataQueue properties |
| Real | floating point number, e.g. 3.1415 |
| Speed | floating point number, depends on the speed unit |
| Stack | list with one column, shares DataStack properties |
| String | characters, numbers and special characters |
| Table | table with one or more columns, shares DataTable properties |
| Time | time statement (hh:mm:ss.ss) |
| Weight | floating point number, depends on the weight unit |

```simtalk
-- set data type of column 2 and column 5
MyDataTable.setDataType(2, 5, "real")

-- set the data type of the row index
MyDataTable.setDataType(0, "integer")
-- set the data type of columns 3 to 5, of column 7 and of the column
-- with the user-defined column index "mycolumn" to the data type real
MyDataTable.setDataType({3,*}..{5,*},7,"mycolumn","real")
```

### setDataTypeDefault

Resets the data type of the specified column(s) to the default data type of the table.

```
<Path>.setDataTypeDefault(Column:any, ...)
```

```simtalk
// resets the data type of the columns 3 to 4, and of column 10 to
// the standard data type of the table
MyDataTable.setDataTypeDefault({3,*}..{4,*},10)
```

### setEditorRightsColumn

Sets the editing permissions of the specified column(s). `ReadOnly = true` for read-only, `false` for read and write access.

```
<Path>.setEditorRightsColumn(Column:any[, Column:any, ...], ReadOnly:boolean)
```

```simtalk
// sets the editor rights of column 1
Tab1.setEditorRightsColumn(1,true)
// sets the editor rights of columns 2 and 4
Tab1.setEditorRightsColumn(2,4,true)
```

### setFontColorColumn

Sets the font color of the specified column(s). Color codes are the same as background color (`1`..`7`), or use `makeRGBValue`.

```
<Path>.setFontColorColumn(Column:any[, Column:any, ...], FontColor:integer)
```

```simtalk
// sets the font color of column 3 to cyan
Tab2.setFontColorColumn(3,7)
// sets the font color of column 1 and 5 to green
Tab2.setFontColorColumn(1,5,3)
```

### setFontsizeColumn

Sets the font size of the specified column(s). `1` = Small, `2` = Medium, `3` = Large, `4` = Extra Large.

```
<Path>.setFontsizeColumn(Column:any[, Column:any, ...], FontSize:integer)
```

```simtalk
// sets the font size of column 2 to medium
Tab2.setFontsizeColumn(2,2)
// sets the font size of columns 3 and 5 to small
Tab2.setFontsizeColumn(3,5,1)
```

### setFormatString

Sets, depending on the data type, the format string of the specified column(s).

```
<Path>.setFormatString(Column:any[, Column:any, ...], FormatString:string)
```

```simtalk
MyDataTable.setFormatString(1,"-15.3") // three digits after the comma
```

### setVisibility

Shows (`true`) or hides (`false`) the designated column(s).

```
<Path>.setVisibility(Column:any[, Column:any, ...], Visibility:boolean)
```

```simtalk
MyDataTable.setVisibility(2,true)
```

---

## Methods of Rows of the DataTable

### appendRow

Adds a new row and writes the passed values to the individual columns. If the row has a row index, the first value is written into the row index. Returns the index of the appended row.

```
<Path>.appendRow(Value:any[, Value:any, ..., Value:any]) -> integer
```

```simtalk
MyDataTable.appendRow("My value", "My value in row 2")
```

### cutEmptyRows

Cuts all empty rows from the DataTable.

```
<Path>.cutEmptyRows → void
```

```simtalk
MyNewDataTable.cutEmptyRows
```

### cutRow

Cuts a row, including all of its data. The row index cannot be cut with `cutRow(0)`.

```
<Path>.cutRow(Row:any)
```

```simtalk
MyDataTable.cutRow(8)
```

### getAlignmentRow

Returns the alignment of the specified row.

```
<Path>.getAlignmentRow(Row:any) → string
```

```simtalk
print MyDataTable.getAlignmentRow(14)
```

### getBackgroundColorRow

Returns the background color of a row.

```
<Path>.getBackgroundColorRow(Row:any) → integer
```

```simtalk
print MyDataTable.getBackgroundColorRow(14)
```

### getEditorRightsRow

Returns the editor rights of a row (`true` read-only, `false` read and write).

```
<Path>.getEditorRightsRow(Row:any) → boolean
```

```simtalk
print MyDataTable.getEditorRightsRow(1)
```

### getFontColorRow

Returns the font color of a row.

```
<Path>.getFontColorRow(Row:any) → integer
```

```simtalk
DataTable3.getFontColorRow(34)
```

### getFontSizeRow

Returns the font size of a row. `1` = Small, `2` = Medium, `3` = Large, `4` = Extra Large.

```
<Path>.getFontSizeRow(Row:any) → integer
```

```simtalk
print DataTable3.getFontSizeRow(34)
```

### getRowNo

Searches for the row containing a user-defined row index. Works only for simple data types. Returns the row number, or `-1` if the row index does not exist.

```
<Path>.getRowNo(RowIndex:any) → integer
```

```simtalk
MyDataTable.getRowNo("article1234")
```

### insertRow

Adds an empty row above the specified row, moving existing cells down one position.

```
<Path>.insertRow(Above:any) → boolean
```

```simtalk
MyDataTable.insertRow(8)
```

### isAlignmentRow

Returns whether the alignment of a row matches the designated value (`true`) or not (`false`).

```
<Path>.isAlignmentRow(Row:any, Alignment:string) → boolean
```

```simtalk
print MyDataTable.isAlignmentRow(7,"center")
```

### setAlignmentRow

Sets the alignment of row(s). Alignment can be `"Left"`, `"Right"`, or `"Centered"`.

```
<Path>.setAlignmentRow(Row:any[, Row:any,...], Alignment:string)
```

```simtalk
MyDataTable.setAlignmentRow(9,10,"center")
MyDataTable.setAlignmentRow(10,"center")
```

### setBackgroundColorRow

Sets the background color of row(s). Color codes `1`..`7`, or use `makeRGBValue`.

```
<Path>.setBackgroundColorRow(Row:any[, Row:any,... , ]BackgroundColor:integer)
```

```simtalk
MyDataTable.setBackgroundColorRow(1,1)   // sets the background color of row 1 to black
MyDataTable.setBackgroundColorRow(1,2,2) // sets the background color of rows 1 and 2 to red
var rgb: integer
// sets the background color of row 3
MyDataTable.setBackgroundColorRow(3,makeRGBValue(0,200,0))
// sets the background color of rows 4 and 8
MyDataTable.setBackgroundColorRow(4,8,makeRGBValue(60,100,0))
print MyDataTable.getBackgroundColorRow(3)
```

### setEditorRightsRow

Sets the editing permissions of row(s). `ReadOnly = true` read-only, `false` read and write.

```
<Path>.setEditorRightsRow(Row:any[, Row:any, ...], ReadOnly:boolean)
```

```simtalk
// sets the editor rights of row 1
Tab1.setEditorRightsRow(1,true)
// sets the editor rights of row 3 and 5
Tab1.setEditorRightsRow(3,5,false)
```

### setFontColorRow

Sets the font color of row(s).

```
<Path>.setFontColorRow(Row:any[, Row:any, ...], FontColor:integer)
```

```simtalk
// sets the font color of row 34 to magenta
DataTable3.setFontColorRow(34,5)
// sets the font color of row 3 and 5 to yellow
DataTable3.setFontColorRow(3,5,6)
```

### setFontSizeRow

Sets the font size of row(s). `1` = Small, `2` = Medium, `3` = Large, `4` = Extra Large.

```
<Path>.setFontSizeRow(Row:any[, Row:any, ...], FontSize:integer)
```

```simtalk
// sets the font size of row 2 to medium
DataTable3.setFontSizeRow(2,2)
// sets the font size of rows 3 and 5 to small
DataTable3.setFontSizeRow(3,5,1)
```

---

## Miscellaneous Methods of the DataTable

### calculateList

Recomputes formulas and shows their current values in the respective cells.

```
<Path>.calculateList([Range:listrange])
```

```simtalk
MyDataTable.calculateList({2,*},{3,3}) // computes column 2, cell 3,3
```

### copyFilteredTableTo

Copies all rows of the source table into the target table for which the Condition returns `true`. The anonymous identifier `@` references the DataTable, and `ySelf` contains the row number of the row to be copied. Also copies the column index if defined.

```
<Path>.copyFilteredTableTo(TargetTable:table, Condition:string)
```

```simtalk
DataTable.copyFilteredTableTo(DataTable1, "@[2, ySelf] = 3")
```

### copyRangeTo

Copies the designated range of the source table into the target table.

```
<Path>.copyRangeTo(SourceRange:listrange, TargetTable:any, TargetColumn:any, TargetRow:any)
```

```simtalk
tableA.copyRangeTo({2,2}..{*,*}, tableB, 1,1)
```

The behavior depends on whether *Column Index Belongs to Contents* is active:

```simtalk
tableA.copyRangeTo({2,*}, tableB, 1,1)
```

- If `tableA` has a column index that belongs to contents, the entire contents of column 2 are copied, including the column index.
- If `tableB` has a column index that does not belong to contents, only the column contents are copied, excluding the column index.

### determineRange

Resolves the actual list range and assigns its boundaries to local variables.

```
<Path>.determineRange(Range:listrange, byRef StartColumn:integer, byRef StartRow:integer, byRef EndColumn:integer, byRef EndRow:integer)
```

```simtalk
param a: any
var fromX, fromY, toX, toY: integer
if isListRange(a)
   MyDataTable.determineRange(a, fromX, fromY, toX, toY)
   print "{",fromX,",",fromY,"}..{",toX,",",toY,"}"
end
// You can call this method like this:
myMethod({2,3})
myMethod({1,1}..{2,*})
// range with a user-defined column/row index
myMethod({#7,"abc"}..{#8,*})
```

### getCommonFormatData

Gets format data of the column of data type list/table for which Common Format is activated and writes it to the target table/list. If no column is specified, the first column is used.

```
<Path>.getCommonFormatData(TargetTable:table[, Column:any])
<Path>.getCommonFormatData(TargetList:list[, Column:any])
```

```simtalk
SourceTable.getCommonFormatData(DataTable,4)
```

### getFormula

Returns the formula located in the specified cell.

```
<Path>.getFormula(Column:any, Row:any) → string
```

```simtalk
MyDataTable.getFormula(16,8)
```

### initialize

Initializes the cells within the designated range with the designated value, overwriting any existing data. If the range contains the index and the content, only the content is initialized.

```
<Path>.initialize([Range:listrange, ..., ]Value:any)
```

```simtalk
MyDataTable.initialize({1,0}..{5,*},{7,*},5)
MyDataTable.initialize({*,*},"Empty")
```

### mergeTable

Copies the columns of the source table to the target table. Uses the row index to correctly assign rows, so both tables must have a row index.

```
<Path>.mergeTable(SourceTable:table)
```

```simtalk
TargetTable.mergeTable(SourceTable)
```

### setCommonFormatData

Sets the common format data for the subtables contained in columns of data type list/table for which Common Format is activated. Applies to the DataTable and the TimeSequence.

```
<Path>.setCommonFormatData(FormatData:table[, Column:any])
<Path>.setCommonFormatData(FormatData:list[, Column:any])
```

```simtalk
MyTargetTable.setCommonFormatData(DataTable,2)
```

### setCursor

Sets the internal cursors (`CursorX`/`CursorY`) to the designated cell. Returns `true` if the cursors were set to the desired position.

```
<Path>.setCursor(Column:any, Row:any) → boolean
```

```simtalk
MyDataTable.setCursor(1,1)
MyDataTable.setCursor(1, "Test") // returns false if the index named Test does not exist
```

### setFormula

Enters the formula into the table cell(s) of the designated range.

```
<Path>.setFormula([Range:listrange, ..., ]Formula:string)
```

```simtalk
// 'myFormula' is a method whose return value is the result of the formula
MyDataTable.setFormula({1,2}..{2,3},"myFormula")
// column 3 results from the difference of column 1 and column 2
MyDataTable.setFormula({3,1}..{3,*}, "@[1,yself] - @[2,yself]")
```

---

## Methods for Accessing the DataTable

### `[ , ]` — read cell contents

Returns the data of the designated cell. Returns a zero value if the cell is empty: `0` for numerical data types, `false` for Boolean, `""` for strings, `void` for object/table/list/stack/queue. Reading does not remove the content.

```
<Path>[Column:integer or string, Row:integer or string] → contents of the cell
```

```simtalk
print MyDataTable[1,2]
print MyDataTable["Value",2]
```

### `[ , ]` — write cell contents

Accesses a cell by its index (system index or user-defined index) and assigns a value. The data type of the new value must match the data type of the cell.

```
<Path>[Column:integer or string, Row:integer or string]
```

```simtalk
MyDataTable[2,3] := 12.34                // system index
orderList["OrderNo","Miller"] := 12.34   // user-defined index
```

### deleteContents

Deletes the contents of the DataTable (including the row index; the column index too if *Column Index Belongs to Contents* is activated).

```
<Path>.deleteContents
```

```simtalk
MyDataTable.deleteContents
```

### writeRow

Writes data to the DataTable at the designated position, replacing any data in those cells.

```
<Path>.writeRow(Column:any, Row:any, Value:any[, Value:any, ..., Value:any])
```

```simtalk
var servicesTable : table[string,integer,string]
Station.imp.getServices(servicesTable)
servicesTable.delete
switch @.Name
case "PartA"
   servicesTable.writeRow(1,1, "ServiceA",2)
case "PartB"
   servicesTable.writeRow(1,1, "ServiceB",1)
case "PartC"
   servicesTable.writeRow(1,1, "ServiceA",1)
   servicesTable.writeRow(1,2, "ServiceB",1)
end
Station.imp.setServices(servicesTable)
end
MyDataTable.writeRow(1,2,"Smith")
```

---

## Methods for Instantiating the DataTable

A local variable of data type `table` does not contain the data itself, only a reference to the data structure. It is `void` when entered into a Method object; you must create it before accessing the data.

### create

Creates a data structure without contents in the local variable. Only applies to a local variable of data type `table`.

```
<var>.create
```

```simtalk
var OrderList : table[string,real]
OrderList.create
OrderList[1,1] := "Cans"
OrderList[2,1] := 3000.0
```

### createNestedList

Creates a nested list in the designated cell. The column data type must be list, stack, queue, or table. Returns the created nested list (DataList, DataQueue, DataStack, or DataTable).

```
<Path>.createNestedList(Column:any, Row:any[, Name:string]) → list
```

```simtalk
MyDataTable.createNestedList(1,2,"My subtable")
```

---

## Read-Only Attributes of the DataTable

The DataTable provides read-only attributes (including the Read-Only Attributes of Lists and Tables, and of All Objects). You can query their values but cannot set them; Plant Simulation computes the value at query time.

Example:

```simtalk
print MyDataTable.Full
```
