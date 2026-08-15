# TimeSequence — Methods

This document summarizes the methods of the **TimeSequence** information-flow object from the Plant Simulation help.

## Active [check box]

To record the progression of the values of the TimeSequence, select the **Active** check box. To not record any values, clear the check box.

**Remarks:** You can also right-click the TimeSequence object in the Frame and select **Activate** on the context menu. To deactivate it, select **Deactivate**.

---

## Overview

The TimeSequence provides:

- Methods for Columns
- Methods for Rows
- Methods for Accessing the TimeSequence
- The shared Methods of Lists and Tables
- The shared Methods of All Objects

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

---

## Reading Method Syntax

An example of the syntax line:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier + parameter data types) is listed in parentheses. `(Parameter:string)` designates a parameter of data type `string`. Instead of a constant, you can also use a variable of the required type or a method returning that type.
- Optional parameters are listed within brackets, e.g. `[,Parameter:boolean]`.
- Default values are shown after the parameter.
- If the method has a return value, its data type is shown after the arrow `->`.

**Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

### Abbreviations used in signatures

| Argument of data type | Data type | Range of values |
|---|---|---|
| integer | integer | integer greater than zero |
| any | all data types | depending on the data type |
| listrange | — | a range |
| direction | string | `"up"`, `"down"`, `" "` |
| attributes | string | name of an attribute |

---

## Methods for Columns

The TimeSequence provides the methods below for the column format. You can also select these settings under **Format > Column**. In methods, the first parameter always designates the column — either the column index, the column range, or the column number.

### getAlignmentColumn

Returns the alignment of the specified column.

- **Syntax:** `<Path>.getAlignmentColumn(Column:any) → string`
- **Example:**
  ```
  str := timeSequence1.getAlignmentColumn(1)
  ```

### getBackgroundColorColumn

Returns the background color of the specified column.

- **Syntax:** `<Path>.getBackgroundColorColumn(Column:any) → integer`
- **Example:**
  ```
  print timeSequence1.getBackgroundColorColumn(4)
  ```

### getColumnWidth

Returns the width of the specified column.

- **Syntax:** `<Path>.getColumnWidth(Column:any) → integer`
- **Example:**
  ```
  print timeSequence1.getColumnWidth(1)
  ```

### getEditorRightsColumn

Returns the editor rights of the specified column.

- **Syntax:** `<Path>.getEditorRightsColumn(Column:any) → boolean`
- **Return value:** `true` for read-only access, `false` for read and write access.
- **Example:**
  ```
  print timeSequence1.getEditorRightsColumn(1)
  ```

### getFontColorColumn

Returns the font color of the specified column.

- **Syntax:** `<Path>.getFontColorColumn(Column:any) → integer`
- **Example:**
  ```
  print timeSequence1.getFontColorColumn(3)
  ```

### getFontSizeColumn

Returns the font size of the specified column.

- **Syntax:** `<Path>.getFontSizeColumn(Column:any) → integer`
- **Return value:** `1` = Small, `2` = Medium, `3` = Large, `4` = Extra Large.
- **Example:**
  ```
  print timeSequence1.getFontSizeColumn(2)
  ```

### getFormatString

Returns the format string of the column.

- **Syntax:** `<Path>.getFormatString(Column:any) → string`
- **Example:**
  ```
  timeSequence1.getFormatString("paint")
  print timeSequence1.getFormatString(1)
  ```

### getVisibility

Returns whether a column is visible (`true`) or hidden (`false`).

- **Syntax:** `<Path>.getVisibility(Column:any) → boolean`
- **Example:**
  ```
  print timeSequence1.getVisibility(4)
  ```

### isAlignmentColumn

Returns whether the alignment of the specified column matches the designated value (`true`) or not (`false`).

- **Syntax:** `<Path>.isAlignmentColumn(Column:any, Alignment:string) → boolean`
- **Parameters:**
  - `Column` (any): the column.
  - `Alignment` (string): the value to check — `"Right"`, `"Left"`, or `"Center"`.
- **Example:**
  ```
  print timeSequence1.isAlignmentColumn("column4","right")
  ```

### setAlignmentColumn

Sets the alignment of the specified column(s).

- **Syntax:** `<Path>.setAlignmentColumn(Column:any[, Column:any,...,], Aligmnent:string)`
- **Parameters:**
  - `Column` (any): the column whose alignment to set.
  - Optional additional `Column` parameters designate more columns.
  - `Alignment` (string): `"Left"`, `"Right"`, or `"Centered"`.
- **Example:**
  ```
  timeSequence1.setAlignmentColumn(5,"center")
  timeSequence1.setAlignmentColumn("Value","right")
  ```

### setBackgroundColorColumn

Sets the background color of the specified column(s).

- **Syntax:** `<Path>.setBackgroundColorColumn(Column:any [,Column:any,...], BackgroundColor:integer)`
- **Parameters:**
  - `Column` (any): the column whose background color to set; optional additional columns.
  - `BackgroundColor` (integer): the color — `1` = Black, `2` = Red, `3` = Green, `4` = Blue, `5` = Magenta, `6` = Yellow, `7` = Cyan. Set RGB values with `makeRGBValue`.
- **Example:**
  ```
  timeSequence1.setBackgroundColorColumn(1,1)
  // sets the background color of column 1 to black
  timeSequence1.setBackgroundColorColumn(1,2,2)
  // sets the background color of columns 1 and 2 to red
  ```

### setColumnWidth

Sets the width of the specified column(s).

- **Syntax:** `<Path>.setColumnWidth(Column:any, ..., ColumnWidth:integer)`
- **Parameters:**
  - `Column` (any): the columns whose width to set.
  - `ColumnWidth` (integer): the width in character widths of a non-proportional font.
- **Example:**
  ```
  timeSequence1.setColumnWidth("column2",10)
  ```

### setEditorRightsColumn

Sets the editing permissions of the specified column(s).

- **Syntax:** `<Path>.setEditorRightsColumn(Column:any, ..., ReadOnly:boolean)`
- **Parameters:**
  - `Column` (any): the columns whose editor permissions to set.
  - `ReadOnly` (boolean): `true` for read-only, `false` for read and write access.
- **Example:**
  ```
  timeSequence1.setEditorRightsColumn(1,true)
  ```

### setFontColorColumn

Sets the font color of the specified column(s).

- **Syntax:** `<Path>.setFontColorColumn(Column:any, ..., FontColor:integer)`
- **Parameters:**
  - `Column` (any): the column(s) whose font color to set.
  - `FontColor` (integer): `1` = Black, `2` = Red, `3` = Green, `4` = Blue, `5` = Magenta, `6` = Yellow, `7` = Cyan. Set RGB values with `makeRGBValue`.
- **Example:**
  ```
  timeSequence1.setFontColorColumn(3,7)
  ```

### setFontsizeColumn

Sets the font size of the specified column(s).

- **Syntax:** `<Path>.setFontsizeColumn(Column:any, ..., FontSize:integer)`
- **Parameters:**
  - `Column` (any): the columns.
  - `FontSize` (integer): `1` = Small, `2` = Medium, `3` = Large, `4` = Extra Large.
- **Example:**
  ```
  timeSequence1.setFontsizeColumn("Value",2)
  ```

### setFormatString

Sets the format string of the specified column, depending on the data type.

- **Syntax:** `<Path>.setFormatString(Column:any, ..., FormatString:string)`
- **Example:**
  ```
  timeSequence1.setFormatString(1,"8")
  ```

### setVisibility

Shows or hides the specified column(s).

- **Syntax:** `<Path>.setVisibility(Column:any, ..., Visible:boolean)`
- **Parameters:**
  - `Column` (any): the columns.
  - `Visibility` (boolean): `true` to show, `false` to hide.
- **Example:**
  ```
  timeSequence1.setVisibility(2,true)
  ```

---

## Methods for Rows

The TimeSequence provides the methods below for the row format. You can also select these settings under **Format > Row** of the TimeSequence.

### getAlignmentRow

Returns the alignment of the specified row.

- **Syntax:** `<Path>.getAlignmentRow(Row:any) → string`
- **Example:**
  ```
  print timeSequence1.getAlignmentRow("BurnIn")
  ```

### getBackgroundColorRow

Returns the background color of the specified row.

- **Syntax:** `<Path>.getBackgroundColorRow(Row:any) → integer`
- **Example:**
  ```
  print timeSequence1.getBackgroundColorRow(14)
  ```

### getEditorRightsRow

Returns the editor rights of the specified row.

- **Syntax:** `<Path>.getEditorRightsRow(Row:any) → boolean`
- **Return value:** `true` for read-only, `false` for read and write access.
- **Example:**
  ```
  print timeSequence1.getEditorRightsRow(1)
  ```

### getFontColorRow

Returns the font color of the specified row.

- **Syntax:** `<Path>.getFontColorRow(Row:any) → integer`
- **Example:**
  ```
  timeSequence1.getFontColorRow(34)
  ```

### getFontSizeRow

Returns the font size of the specified row.

- **Syntax:** `<Path>.getFontSizeRow(Row:any) → integer`
- **Return value:** `1` = Small, `2` = Medium, `3` = Large, `4` = Extra Large.
- **Example:**
  ```
  print timeSequence1.getFontSizeRow(34)
  ```

### isAlignmentRow

Returns whether the alignment of the specified row matches the designated value (`true`) or not (`false`).

- **Syntax:** `<Path>.isAlignmentRow(Row:any, Alignment:string) → boolean`
- **Parameters:**
  - `Row` (any): the row.
  - `Alignment` (string): `"Right"`, `"Left"`, or `"Center"`.
- **Example:**
  ```
  print timeSequence1.isAlignmentRow(7,"center")
  ```

### setAlignmentRow

Sets the alignment of the specified row(s).

- **Syntax:** `<Path>.setAlignmentRow(Row:any[, Row:any,...], Aligmnent:string)`
- **Parameters:**
  - `Row` (any): the row whose alignment to set; optional additional rows.
  - `Alignment` (string): `"Left"`, `"Right"`, or `"Centered"`.
- **Example:**
  ```
  timeSequence1.setAlignmentRow(2,"right")
  ```

### setBackgroundColorRow

Sets the background color of the specified row(s).

- **Syntax:** `<Path>.setBackgroundColorRow(Row:any[, Row:any,...], BackgroundColor:integer)`
- **Parameters:**
  - `Row` (any): the row whose background color to set; optional additional rows.
  - `BackgroundColor` (integer): `1` = Black, `2` = Red, `3` = Green, `4` = Blue, `5` = Magenta, `6` = Yellow, `7` = Cyan. Set RGB values with `makeRGBValue`.
- **Examples:**
  ```
  var rgb: integer
  // sets the background color of row 3
  MyTimeSequence.setBackgroundColorRow(3,makeRGBValue(0,200,0))
  // sets the background color of rows 4 and 8
  MyTimeSequence.setBackgroundColorRow(4,8,makeRGBValue(60,100,0))
  print MyTimeSequence.getBackgroundColorRow(3)
  // sets the background color of row 1 to black
  MyTimeSequence.setBackgroundColorRow(1,1)
  // sets the background color of rows 1 and 2 to red
  MyTimeSequence.setBackgroundColorRow(1,2,2)
  ```

### setEditorRightsRow

Sets the editing permissions of the designated row(s).

- **Syntax:** `<Path>.setEditorRightsRow(Row:any[, Row:any, ...], ReadOnly:boolean)`
- **Parameters:**
  - `Row` (any): the row(s).
  - `ReadOnly` (boolean): `true` for read-only, `false` for read and write access.
- **Example:**
  ```
  timeSequence1.setEditorRightsRow(1,true)
  ```

### setFontColorRow

Sets the font color of the designated row(s).

- **Syntax:** `<Path>.setFontColorRow(Row:any[, Row:any, ...], FontColor:integer)`
- **Parameters:**
  - `Row` (any): the cells whose font color to set.
  - `FontColor` (integer): `1` = Black, `2` = Red, `3` = Green, `4` = Blue, `5` = Magenta, `6` = Yellow, `7` = Cyan. Set RGB values with `makeRGBValue`.
- **Example:**
  ```
  timeSequence1.setFontColorRow(34,5)
  ```

### setFontSizeRow

Sets the font size of the designated row(s).

- **Syntax:** `<Path>.setFontSizeRow(Row:any[, Row:any, ...], FontSize:integer)`
- **Parameters:**
  - `Row` (any): the rows.
  - `FontSize` (integer): `1` = Small, `2` = Medium, `3` = Large, `4` = Extra Large.
- **Example:**
  ```
  timeSequence1.setFontSizeRow(2,2)
  ```

---

## Methods for Accessing the TimeSequence

The TimeSequence provides the methods below for accessing it.

### `[ , ]` — read cell contents

Randomly access cell contents by column and row indexes.

- **Syntax:** `<Path>[Column:integer, Row:integer] → contents of the cell`
- **Remarks:** The index statement begins and ends with a bracket. Inside, first enter the column, then the row. The return value's data type is the same as the table cell. Plant Simulation only reads the cell contents — it does not remove them.
- **Return value:** The cell contents; `VOID` if the cell is empty.
- **Example:**
  ```
  print timeSequence[1,2]
  print timeSequence["Value",2]
  ```

### `[ , ]` — write cell contents

Writes data to the specified cell.

- **Syntax:** `<Path>[Column:integer, Row:integer]`
- **Remarks:** First access the cell by its index, then assign a value. The new value's data type must match the table cell.
- **Example:**
  ```
  timeSequence[2,3] := 12.34
  ```

### add

Adds a numerical value to all entries of the value column, or combines the time and value columns of two TimeSequence objects.

- **Syntax:** `<Path>.add(ValueToBeAdded:any)`
- **Parameter:** If `ValueToBeAdded` is a numerical value, it is added to each value-column entry (time column unchanged). If it is another TimeSequence, time/value pairs are added in sections; time columns determine section extents. Multiple entries at a time value are combined in pairs, and if counts differ, the last entry is duplicated before addition.
- **Example:**
  ```
  MyTimeSequence.add(5)
  shiftA.add(shiftB)
  ```

### and — operator

Boolean operation `and` usable in a TimeSequence of data type `boolean`.

- **Syntax:** `<Path>.and(Operand:any)`
- **Remarks:** The operation may be executed with a single boolean parameter or another TimeSequence. With another TimeSequence, the resulting time column is the union of both time columns.
- **Example:**
  ```
  failureA.and(failureB)
  workerA.or(workerB)
  MyTimeSequence.or(true)
  MyTimeSequence.and(false)
  ```

### deleteInterval

Deletes all values located within the designated time interval.

- **Syntax:** `<Path>.deleteInterval([BeginningOfInterval:time, EndOfInterval:time])`
- **Parameters:**
  - `BeginningOfInterval` (time, optional): beginning of the interval.
  - `EndOfInterval` (time, optional): end of the interval.
- **Remarks:** Entries matching one of the boundaries are also deleted.
- **Example:**
  ```
  resultList.deleteInterval(0,3600)
  ```

### divide

Divides all items of the value column by a numerical value, or divides by another TimeSequence.

- **Syntax:** `<Path>.divide(Divisor:any)`
- **Remarks:** With another TimeSequence, the resulting time column is the combination of both time columns; the value column contains the quotient at the respective times.
- **Note:** All divisors must be non-zero.
- **Example:**
  ```
  MyTimeSequence.divide(5)
  numEntities.divide(current.NumMU)
  ```

### include

Takes all entries of the designated TimeSequence and inserts them into `<Path>`.

- **Syntax:** `<Path>.include(TimeSequence:object)`
- **Remarks:** May result in multiple entries with the same time value; the order of such entries relative to each other is undefined. Data types must be identical or compatible.
- **Example:**
  ```
  timeSequence1.include(timeSequence2)
  ```

### insert

Inserts a time/value pair into the TimeSequence.

- **Syntax:** `<Path>.insert(GivenTime:any, Value:any)`
- **Parameters:**
  - `GivenTime` (any): the time. For the time reference **Absolute**, this is of data type `dateTime`; otherwise `time`.
  - `Value` (any): the value, matching or compatible with the TimeSequence's data type.
- **Example:**
  ```
  MyTimeSequence.insert(eventcontroller.simtime,3)
  MyTimeSequence.insert(sysdate,3)
  ```

### multiply

Multiplies all items of the value column by a numerical value, or multiplies with another TimeSequence.

- **Syntax:** `<Path>.multiply(Factor:any)`
- **Remarks:** With another TimeSequence, the time column is the union of both time columns; the value column contains the product at the respective times.
- **Example:**
  ```
  MyTimeSequence.multiply(5)
  dimx.multiply(dimy)
  ```

### not

Applies a boolean NOT operation to all values in the value column.

- **Syntax:** `<Path>.not`
- **Example:**
  ```
  MyTimeSequence.not // reverses all inputs
  ```

### or — operator

Boolean operation `or` usable in a TimeSequence of data type `boolean`.

- **Syntax:** `<Path>.or(Operand:any)`
- **Remarks:** The operation may be executed with a single boolean parameter or another TimeSequence. With another TimeSequence, the resulting time column is the union of both time columns.
- **Example:**
  ```
  failureA.and(failureB)
  workerA.or(workerB)
  MyTimeSequence.or(true)
  MyTimeSequence.and(false)
  ```

### repeat

Deletes all entries and replaces them with copies of a sub-range of the data of another TimeSequence.

- **Syntax:** `<Path>.repeat(TimeSequence:object, Subrange:time, NumberOfCopies:real)`
- **Parameters:**
  - `TimeSequence` (object): the TimeSequence whose sub-range is pasted.
  - `Subrange` (time): starts at time zero and ends at this time.
  - `NumberOfCopies` (real): number of copies to insert (e.g., create a week's schedule from a day's by repeating five times).
- **Example:**
  ```
  LengthOfDay := str_to_time("1:00:00:00.00")
  weekPlan.repeat(dayPlan,lengthOfDay,5)
  ```

### repeatTo

Removes all entries and replaces them with copies of a sub-range of the designated TimeSequence, filling a target range.

- **Syntax:** `<Path>.repeatTo(TimeSequence:object, Subrange:time, RangeToBeFilled:time)`
- **Parameters:**
  - `TimeSequence` (object): the TimeSequence whose data replaces the existing data.
  - `Subrange` (time): starts at time zero and ends at this time.
  - `RangeToBeFilled` (time): the range of `<Path>` to fill with copies of the sub-range. Must be greater than the sub-range, otherwise it remains empty.
- **Examples:**
  ```
  weekPeriod := str_to_time("5:00:00:00.00")
  dayPeriod := str_to_time("1:00:00:00.00")
  weekPlan.repeatTo(dayPlan,weekPeriod,dayPeriod)
  MyTimeSequence.or(true) // all values := true
  MyTimeSequence.and(false) // all values := false
  ```

### subtract

Subtracts a numerical value from all entries of the value column, or subtracts time/value pairs of another TimeSequence.

- **Syntax:**
  ```
  <Path>.subtract(ValueToBeSubtracted:integer)
  <Path>.subtract(ValueToBeSubtracted:real)
  <Path>.subtract(ValueToBeSubtracted:object)
  ```
- **Parameters:**
  - Numerical value (`integer`/`real`): subtracted from each value-column entry (time column unchanged).
  - Another TimeSequence (`object`): time/value pairs subtracted in sections; multiple entries combined in pairs, and if counts differ, the last entry is duplicated before subtraction.
- **Example:**
  ```
  MyTimeSequence.subtract(5)
  stock.subtract(missingEntities)
  ```

### value

Returns the value the TimeSequence takes at a given time.

- **Syntax:** `<Path>.value(GivenTime:time) -> any`
- **Remarks:** If multiple entries share the same time, the entry with the highest number is returned.
- **Parameter:** `GivenTime` (time): the time.
- **Example:**
  ```
  print ts1.value(1.5)+ts2.value(1.5)
  ```

---

## Read-Only Attributes

The TimeSequence provides the Read-Only Attributes of Lists and Tables, and of All Objects. You can query read-only attribute values but cannot set them — Plant Simulation computes the value at the point in time you query it.

Example query:

```
print MyTimeSequence.Full
```

---

## Attributes

The TimeSequence provides the attributes listed in the table of contents, plus the Attributes of Lists and Tables and the Attributes of All Objects.

---

*Source: Plant Simulation Help (TimeSequence methods). Unpublished work. © 2026 Siemens.*
