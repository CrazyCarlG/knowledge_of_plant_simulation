# DataTable Attributes

This document summarizes the SimTalk attributes of the DataTable object in Plant Simulation.

## General Notes

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set and get the value of an attribute either with the check boxes, text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To **set** the value of an attribute, for example:

```simtalk
MyDataTable.ColumnIndex := false
MyDataTable.calculateList({1,3}..{2,4})
```

- To **get** the value of an attribute, for example:

```simtalk
print MyDataTable.MaxXDim
posit := Station.Cont.XPos
```

---

## Alignment [SimTalk] - DataTable

Sets the alignment of all cells of the DataTable designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Alignment:string`
- **Assignment Value:** A value of data type string. You can specify `"left"`, `"right"`, or `"center"`.

**Example**

```simtalk
MyDataTable.Alignment := "left"
```

---

## Changed [SimTalk]

Is set to `true` if the contents of the DataTable designated by `<Path>` changed.

- **Remarks:** You can reset the attribute to `false` at any time to detect a change at a later point in time.
- **Type:** Attribute
- **Syntax:** `<Path>.Changed:boolean`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
while true 
   MyDataTable.Changed := false
   stopuntil MyDataTable.Changed
   print "Contents of the table has changed."
   print "New sum of all values: ", MyDataTable.sum"
end
```

---

## ColumnIndex [SimTalk]

Activates (`true`) or deactivates (`false`) the user-defined column index of the DataTable designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.ColumnIndex:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
MyDataTable.ColumnIndex := true
```

**See also:** Activate Column Index, ShowColumnIndex [SimTalk] - DataTable

---

## ColumnIndexContents [SimTalk]

Makes the column index belong to the contents of the DataTable designated by `<Path>` (`true`) or not (`false`).

- **Remarks:**
  - Then the column index is inherited together with the contents of the DataTable if *Inherit Contents* is active.
  - If you enter `false`, the column index belongs to the format of the DataTable. Then the column index is inherited together with the format of the DataTable when *Inherit Format* is active.
- **Type:** Attribute
- **Syntax:** `<Path>.ColumnIndexContents:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
MyDataTable.ColumnIndexContents := true
```

**See also:** Column Index Belongs to Contents, Inherit Contents [lists], Inherit Format [button]

---

## CommonFormatColumnIndex [SimTalk]

Activates the Common Format for the column index of the DataTable designated by `<Path>` (`true`) or deactivates it (`false`).

- **Remarks:** CommonFormatColumnIndex applies if the column index is of data type table, list, stack or queue. If you activated Common Format for a column, assigning a subtable to a table cell creates a copy of the assigned table. Otherwise Plant Simulation enters a reference to the assigned table.
- **Type:** Attribute
- **Syntax:** `<Path>.CommonFormatColumnIndex:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
MyDataTable.CommonFormatColumnIndex := true
```

**See also:** Common Format [check box], Tab Contents

---

## CursorX [SimTalk]

Sets the column in which the internal cursor of the DataTable designated by `<Path>` is located.

- **Remarks:**
  - The method `find` starts searching from the current cursor position and sets the cursor to the next found item.
  - The methods `max` and `min` set the cursor to the maximum or minimum value of the given range.
  - Plant Simulation ignores ranges located before the current cursor position. The Method starts its task beginning at the cursor position. If a Method does not return the expected values, check the cursor position. The first row has the number 1. If you also want to include the user-defined index, set the attribute `CursorX` to 0.
- **Note:** This attribute applies to the DataTable and the TimeSequence.
- **Note:** You can also set the pointer by using a user-defined index. For a user-defined index of data type integer, use the method `setCursor!`.
- **Type:** Attribute
- **Syntax:** `<Path>.CursorX:integer`
- **Assignment Value:** A value of data type integer.

**Example**

```simtalk
MyDataTable.CursorX := 1 // starting position
MyDataTable.CursorY := 1 // set
if MyDataTable.find({1,*},4712)
 print "found in row:", MyDataTable.CursorY
end 
```

**See also:** setCursor [SimTalk] - DataTable, CursorY [SimTalk], find [SimTalk] - lists, findCeil, findFloor, findAttr, min [SimTalk] - lists, max [SimTalk] - lists

---

## CursorY [SimTalk]

Sets the row in which the internal cursor of the DataTable designated by `<Path>` is located.

- **Remarks:**
  - The method `find` starts searching from the current cursor position and sets the cursor to the next found item.
  - The methods `max` and `min` set the cursor to the maximum or minimum value of the given range.
  - Plant Simulation ignores ranges located before the current cursor position. The Method starts its task beginning at the cursor position. If a Method does not return the expected values, check the cursor position. The first column has the number 1. If you also want to include the user-defined index, set the attribute `CursorY` to 0.
- **Note:** This attribute applies to the DataTable and the TimeSequence.
- **Note:** You can also set the pointer by employing a user-defined index. For a user-defined index of data type integer, use the method `setCursor!`.
- **Type:** Attribute
- **Syntax:** `<Path>.CursorY:integer`
- **Assignment Value:** A value of data type integer.

**Example**

```simtalk
MyDataTable.CursorX := 1 // starting position
MyDataTable.CursorY := 1 // set
if MyDataTable.find({1,*},4712)
 print "found in row:", MyDataTable.CursorY
end 
```

```simtalk
MyDataTable.CursorY := "urgent" // user-defined index
MyDataTable.CursorX := 3.1415 
```

**See also:** setCursor [SimTalk] - DataTable, CursorX [SimTalk], find [SimTalk] - lists, findCeil, findFloor, findAttr, min [SimTalk] - lists, max [SimTalk] - lists

---

## DataType [SimTalk] - DataTable

Sets the default data type of the DataTable designated by `<Path>` to the value designated by the value you enter as a string.

- **Type:** Attribute
- **Syntax:** `<Path>.DataType:string`
- **Assignment Value:** A value of data type string.

**Data types:**

| Data type | Description |
|-----------|-------------|
| Acceleration | applies for the objects Conveyor, Track, TwoLaneTrack, and Transporter, meter per second squared |
| Boolean | true or false |
| Date | date statement (dd.MM.yyyy) |
| DateTime | date statement, including the time (dd.MM.yyyy HH:mm:ss) |
| Integer | integer value |
| Length | floating point number, value depends on the unit of the length |
| List | list with one column, shares properties of the DataList |
| Money | floating point numbers |
| Object | reference to a simulation model or an object |
| Queue | list with one column, shares properties of the DataQueue |
| Real | floating point number, such as 3.1415 |
| Speed | floating point number, value depends on the unit for speed |
| Stack | list with one column, shares properties of the DataStack |
| String | characters, numbers and special characters |
| Table | table with one or more columns, shares properties of the DataTable |
| Time | time statement (hh:mm:ss.ss) |
| Weight | floating point number, value depends on the unit of the weight |

**Example**

```simtalk
MyDataTable.DataType := "real"
```

**See also:** Data Type [lists]

---

## DataTypeColumnIndex [SimTalk]

Sets the Data Type of the user-defined column index of the DataTable designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.DataTypeColumnIndex:string`
- **Assignment Value:** A value of data type string.

**Data types:** Same list as `DataType` above (Acceleration, Boolean, Date, DateTime, Integer, Length, List, Money, Object, Queue, Real, Speed, Stack, String, Table, Time, Weight).

**Example**

```simtalk
MyDataTable.DataTypeColumnIndex := "queue"
```

**See also:** Data Type [lists]

---

## FastAccessColumnIndex [SimTalk]

Uses the faster access to the user-defined column index (`true`) or not (`false`) for the DataTable designated by `<Path>`.

- **Remarks:** The more columns and rows your table has, the more you benefit from the improved access speed.
- **Type:** Attribute
- **Syntax:** `<Path>.FastAccessColumnIndex:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
MyDataTable.FastAccessColumnIndex := true
```

**See also:** Fast Index Access [columns], getColumnNo [SimTalk], UniqueKeyColumnIndex [SimTalk]

---

## FastAccessRowIndex [SimTalk]

Uses the faster access to the user-defined row index (`true`) or not (`false`) for the DataTable designated by `<Path>`.

- **Remarks:** The more columns and rows your table has, the more you benefit from the improved access speed.
- **Type:** Attribute
- **Syntax:** `<Path>.FastAccessRowIndex:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
MyDataTable.FastRowColumnIndex := true
```

**See also:** Fast Index Access [rows], getRowNo [SimTalk], UniqueKeyRowIndex [SimTalk]

---

## FormatString [SimTalk] - DataTable

Sets the Format String of the DataTable designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.FormatString:string`
- **Assignment Value:** A value of data type string.

**Example**

```simtalk
MyDataTable.FormatString := "-9"
```

**See also:** Format String [text box]

---

## FormatStringColumnIndex [SimTalk]

Sets, depending on the data type, the Format String of the column index of the DataTable designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.FormatStringColumnIndex:string`
- **Assignment Value:** A value of data type string.

**Example**

```simtalk
MyDataTable.FormatString := "3.3"
```

**See also:** Format String [text box]

---

## FormatStringRowIndex [SimTalk]

Sets, depending on the data type, the Format String of the row index of the DataTable designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.FormatStringRowIndex:string`
- **Assignment Value:** A value of data type string.

**Example**

```simtalk
MyDataTable.FormatStringRowIndex := "-2.3"
```

**See also:** Format String [text box]

---

## MaxXDim [SimTalk]

Sets the maximum number of columns of the DataTable designated by `<Path>`.

- **Remarks:** MaxXDim applies to the DataTable and to the TimeSequence.
- **Type:** Attribute
- **Syntax:** `<Path>.MaxXDim:integer`
- **Assignment Value:** A value of data type integer. Specify `-1` for an infinite size.

**Example**

```simtalk
MyDataTable.MaxXDim := 10   // 10 columns
DataTable1.MaxXDim := -1    // unlimited
```

**See also:** Number of Columns [lists]

---

## MaxYDim [SimTalk]

Sets the maximum number of rows of the DataTable designated by `<Path>`.

- **Remarks:** MaxYDim applies to the DataTable and the TimeSequence.
- **Type:** Attribute
- **Syntax:** `<Path>.MaxYDim:integer`
- **Assignment Value:** A value of data type integer. Specify `-1` for an infinite size.

**Example**

```simtalk
MyDataTable.MaxYDim := 50 // 50 rows
DataTable1.MaxYDim := -1  // unlimited
```

**See also:** Number of Rows [lists]

---

## Name [SimTalk] - DataTable

Sets the name of the DataTable designated by `<Path>` to the designated expression.

- **Remarks:** You can use the attribute Name to access the name of the sublist via information flow.
- **Type:** Attribute
- **Syntax:** `<Path>.Name:string`
- **Assignment Value:** A value of data type string.

**Examples**

```simtalk
DataTable.createNestedList(1, 1)
DataTable[1,1].Name := "MyName"
var str : string
str := .Models.MyPlantAnytown.SteeringTypes["Jacks","9149"].Name 
// returns the value of the cell that contains the subtable, 4 in the 
example
```

**See also:** Cut [Home ribbon], Accessing the Name of a Sublist with a Method

---

## RowIndex [SimTalk]

Activates (`true`) or deactivates (`false`) the user-defined row index of the DataTable designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.RowIndex:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
MyDataTable.RowIndex := false
```

**See also:** Activate Row Index

---

## ShowColumnIndex [SimTalk] - DataTable

Shows the column index of the DataTable designated by `<Path>` (`true`) or hides it (`false`).

- **Remarks:** You can activate or deactivate the column index with the attribute ColumnIndex.
- **Type:** Attribute
- **Syntax:** `<Path>.ShowColumnIndex:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
MyDataTable.ShowColumnIndex := false
```

**See also:** Activate Column Index, ColumnIndex [SimTalk]

---

## ShowRowIndex [SimTalk] - DataTable

Shows the row index (`true`) of the DataTable designated by `<Path>` or hides it (`false`).

- **Remarks:** You can activate or deactivate the row index with the attribute RowIndex.
- **Type:** Attribute
- **Syntax:** `<Path>.ShowRowIndex:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
MyDataTable.ShowRowIndex := true
```

**See also:** Activate Row Index, RowIndex [SimTalk]

---

## UniqueKeyColumnIndex [SimTalk]

Applies a unique key to the user-defined column index (`true`) to the DataTable designated by `<Path>` or not (`false`).

- **Remarks:** UniqueKeyColumnIndex only works while you manually edit a DataTable. It does not work when writing to an index using a Method. Plant Simulation does not detect multiple entries via information flow.
- **Type:** Attribute
- **Syntax:** `<Path>.UniqueKeyColumnIndex:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
Tab.UniqueKeyColumnIndex := true
```

**See also:** Unique Index Key [columns]

---

## UniqueKeyRowIndex [SimTalk]

Applies a unique key to the user-defined row index (`true`) to the DataTable designated by `<Path>` or not (`false`).

- **Remarks:** UniqueKeyRowIndex only works while you manually edit a DataTable. It does not work when writing to an index using a Method. Plant Simulation does not detect multiple entries via information flow.
- **Type:** Attribute
- **Syntax:** `<Path>.UniqueKeyRowIndex:boolean`
- **Assignment Value:** A value of data type boolean.

**Example**

```simtalk
tab2.UniqueKeyRowIndex := false
```

**See also:** Unique Index Key [rows]

---

## DataList (Related Object)

Use the object DataList for randomly accessing the contents of the individual cells using their position, i.e., their row number.

### Description

The DataList is a list with one column providing random access to the contents of the individual cells using their position, i.e., their row number. Imagine the DataList as a file-card box. When you add an entry, Plant Simulation moves all entries after this one position down. You can delete an entry, and you can read an entry and add that entry back to the DataList.

You can access the functions of the list objects on the List Ribbon Tab.

**Note:** The DataList always opens in the background behind any open dialog boxes. You can also open it in the foreground as a dialog box with the method `openDialogBox`.

The DataList shares its built-in properties with the data type List.

Note the difference between the object DataList, which you can insert into a model, and the data type list. You can create user-defined attributes and local and global variables of data type list that are part of another object and thus are not an object of their own and do not have their own icon. For this reason these variables and attributes do not recognize the SimTalk functions of the DataList, such as `Location` or `existsIcon`. All other methods, especially for read and write access, apply to both the DataList and to variables and attributes.

To show a tooltip with information about the DataList, hover with the mouse over it. To change the length of the graphic and the anchor points of the DataList, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

### Add the Object to the Simulation Model

To add the object DataList to your simulation model, click **Manage Class Library > Basic Objects > InformationFlow > DataList** on the Home ribbon tab.

**See also:** Properties of Lists and Tables, Work with Data in a List or Table in the Step-by-Step Help, Access Data in Lists in the Step-by-Step Help, Accessing a Range of Cells with a Method
