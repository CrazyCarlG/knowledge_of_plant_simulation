# Attributes of Lists and Tables

Lists and tables (DataStack, DataQueue, DataList, DataTable, TimeSequence) provide attributes for setting the format, working in text format, printing, showing/hiding settings, and miscellaneous purposes.

## Viewing Attributes and Methods

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute, for example:
  ```
  MyDataTable.MaxXDim := -1
  ```
- To get the value of an attribute, for example:
  ```
  print MyDataTable.MaxXDim
  posit := Station.Cont.XPos
  ```

---

## Attributes for the Format of Lists and Tables

Lists and tables provide the following attributes for setting the format of the entire list or table. In the dialog, select these settings on the **List ribbon tab > Edit Format**.

### Alignment [SimTalk] - lists

Sets the alignment of all cells of the list/table designated by `<Path>`.

- **Syntax:** `<Path>.Alignment:string`
- **Assignment value:** `"left"`, `"right"`, or `"center"`.
- **Applies to:** DataStack, DataQueue, DataList, DataTable, TimeSequence.

```
MyDataQueue.Alignment := "left"
print MyDataQueue.Alignment
```

### BackgroundColor [SimTalk] - lists

Sets the background color for all cells of the list/table designated by `<Path>`.

- **Syntax:** `<Path>.BackgroundColor:integer`
- **Assignment value:** 1 = Black, 2 = Red, 3 = Green, 4 = Blue, 5 = Magenta, 6 = Yellow, 7 = Cyan. Or set the RGB values with `makeRGBValue`.

```
var rgb: integer
MyDataTable.BackgroundColor := makeRGBValue(120,120,120)
rgb := MyDataTable.BackgroundColor
print rgb
```

### ColumnWidth [SimTalk]

Sets the column width (in character widths of a non-proportional font) of all cells of the list/table designated by `<Path>`.

- **Syntax:** `<Path>.ColumnWidth:integer`
- **Assignment value:** between 20 (default) and 180 (maximum).

```
MyDataQueue.ColumnWidth := 10
```

### DataType [SimTalk] - lists

Sets the data type of the list/table designated by `<Path>`.

- **Syntax:** `<Path>.DataType:string`

Data types:

| Data type | Description |
|---|---|
| Acceleration | applies to Conveyor, Track, TwoLaneTrack, Transporter (m/s²) |
| Boolean | true or false |
| Date | date statement (dd.MM.yyyy) |
| DateTime | date statement including time (dd.MM.yyyy HH:mm:ss) |
| Integer | integer value |
| Length | floating point number, depends on the unit of length |
| List | list with one column, shares properties of the DataList |
| Money | floating point number |
| Object | reference to a simulation model or an object |
| Queue | list with one column, shares properties of the DataQueue |
| Real | floating point number, e.g. 3.1415 |
| Speed | floating point number, depends on the unit for speed |
| Stack | list with one column, shares properties of the DataStack |
| String | characters, numbers and special characters |
| Table | table with one or more columns, shares properties of the DataTable |
| Time | time statement (hh:mm:ss.ss) |
| Weight | floating point number, depends on the unit of weight |

```
MyDataList.DataType := "integer"
```

### EditorReadOnly [SimTalk]

Sets read-only permission for the list/table designated by `<Path>` (true), or allows editing (false).

- **Syntax:** `<Path>.EditorReadOnly:boolean`

```
MyDataStack.EditorReadOnly := false
```

### FontColor [SimTalk]

Sets the font color used for displaying data in the cells of the list/table designated by `<Path>`.

- **Syntax:** `<Path>.FontColor:integer`
- **Assignment value:** 1 = Black, 2 = Red, 3 = Green, 4 = Blue, 5 = Magenta, 6 = Yellow, 7 = Cyan. Or set RGB values with `makeRGBValue`.

```
MyDataTable.FontColor := 2
```

Related methods: `makeRGBValue`, `setFontColorCells`, `setFontColorColumn`, `getFontColorColumn`, `setFontColorRow`, `getFontColorRow`.

### FontSize [SimTalk] - DataTable

Sets the font size used for displaying data in the cells of the list/table designated by `<Path>`.

- **Syntax:** `<Path>.FontSize:integer`
- **Assignment value:** 1 = Small, 2 = Medium, 3 = Large, 4 = Extra Large.

```
MyDataTable.FontSize := 2
```

### FormatString [SimTalk] - lists

Sets, depending on the data type, the format string of the list/table designated by `<Path>`.

- **Syntax:** `<Path>.FormatString:string`

```
MyDataQueue.FormatString := "5.3"
```

### InfoflowReadOnly [SimTalk]

Sets whether the list/table can only be read via methods (true), or whether methods may also write (false).

- **Syntax:** `<Path>.InfoflowReadOnly:boolean`

```
MyDataStack.InfoflowReadOnly := true
```

---

## Attributes for the Text Format of Lists and Tables

Lists and tables provide the following attributes for working with them in text format. In the dialog, select these settings under **Export > Text File Format** on the List ribbon tab.

### ColumnSeparator [SimTalk]

Sets the column separator when saving the list/table designated by `<Path>` in text format.

- **Syntax:** `<Path>.ColumnSeparator:string`
- **Assignment value:** Tab, blank Space, `,` (comma), or `;` (semicolon).

> **Note:** Strongly avoid using the comma (`,`) as both decimal separator and column separator. Use it only as one or the other.

```
MyDataQueue.ColumnSeparator := " "
```

### DecimalSeparator [SimTalk]

Sets the decimal separator when saving the list/table designated by `<Path>` in text format.

- **Syntax:** `<Path>.DecimalSeparator:string`
- **Assignment value:** `"."` (period) or `","` (comma).

> **Note:** Strongly avoid using the comma (`,`) as both decimal separator and column separator.

```
MyDataStack.DecimalSeparator := "," // comma
```

### TimeFormat [SimTalk]

Sets the time format when saving the list/table designated by `<Path>` in text format.

- **Syntax:** `<Path>.TimeFormat:string`
- **Assignment value:** `"D:H:M:S"`, `"H:M:S"`, `"M:S"`, or `"S"`.

```
MyDataList.TimeFormat := "M:S"
```

---

## Attributes for Printing Lists and Tables

Lists and tables provide the following attributes for printing their contents. In the dialog, select these settings by clicking **Print > Print Setup** on the List ribbon tab.

### GenerateColumnWidth [SimTalk]

Uses the widest column of the list when printing the list/table designated by `<Path>` (true) or not (false).

- **Syntax:** `<Path>.GenerateColumnWidth:boolean`

```
MyDataQueue.GenerateColumnWidth := true
```

### PrintColumnNumber [SimTalk]

Prints the column number of the list/table designated by `<Path>` (true) or not (false).

- **Syntax:** `<Path>.PrintColumnNumber:boolean`

```
MyDataStack.PrintColumnNumber := false
```

### PrintDataType [SimTalk]

Prints the data type of the list/table designated by `<Path>` (true) or not (false).

- **Syntax:** `<Path>.PrintDataType:boolean`

```
MyDataStack.PrintDataType := false
```

### PrintInternalLists [SimTalk]

Prints nested lists located in the list/table designated by `<Path>` (true) or not (false).

- **Syntax:** `<Path>.PrintInternalLists:boolean`

```
MyDataStack.PrintInternalLists := false
```

### PrintRowNumber [SimTalk]

Prints the row number of the list/table designated by `<Path>` (true) or not (false).

- **Syntax:** `<Path>.PrintRowNumber:boolean`

```
MyDataStack.PrintRowNumber := false
```

### RepeatColumnIndex [SimTalk]

Prints the user-defined column index on each page of the printed list/table designated by `<Path>` (true) or not (false).

- **Syntax:** `<Path>.RepeatColumnIndex:boolean`

```
MyDataQueue.RepeatColumnIndex := false
```

### RepeatRowIndex [SimTalk]

Prints the user-defined row index on each page of the printed list/table designated by `<Path>` (true) or not (false).

- **Syntax:** `<Path>.RepeatRowIndex:boolean`

```
MyDataQueue.RepeatRowIndex := true
```

---

## Attributes for Showing Settings of Lists and Tables

Lists and tables provide the following attributes for showing and hiding their settings.

### ShowComment [SimTalk] - lists

Shows the comment of the list/table designated by `<Path>` (true) or not (false).

- **Syntax:** `<Path>.ShowComment:boolean`

```
MyDataQueue.ShowComment := true
```

### ShowDataType [SimTalk] - lists

Shows the data type of the list/table designated by `<Path>` (true) or hides it (false).

- **Syntax:** `<Path>.ShowDataType:boolean`

```
MyDataQueue.ShowDataType := false
```

### ShowVoid [SimTalk]

Shows empty cells in the list/table designated by `<Path>` in gray (true) or not (false).

- **Syntax:** `<Path>.ShowVoid:boolean`

```
MyDataQueue.ShowVoid := false
```

---

## Miscellaneous Attributes of Lists and Tables

Lists and tables provide the following attributes for miscellaneous purposes.

### Comment [SimTalk] - lists

Sets the comment of the list/table designated by `<Path>`.

- **Syntax:** `<Path>.Comment:string`
- **Applies to:** DataTable, DataList, DataStack, DataQueue.

```
MyDataQueue.Comment := "parts produced"
print MyDataQueue.Comment
```

### Cursor [SimTalk]

Sets the cell (in a list with one column) designated by `<Path>` in which the cursor is placed.

- **Syntax:** `<Path>.Cursor:integer`
- **Applies to:** DataList, DataStack, DataQueue.

> All methods that use ranges (such as `find` or `max`) use the current cursor position. Plant Simulation ignores ranges located before the current cursor position; the method starts at the cursor position. If a method does not return the expected values, check the cursor position.

> You can also set the cursor using a user-defined index with the method `setCursor` (data type integer).

```
MyDataStack.Cursor := 1
MyDataQueue.Cursor := 2
MyDataList.Cursor := MyDataList.Cursor + 1
```

Related: `CursorX`, `CursorY`, `setCursor`, `find`, `max`.

### InheritComment [SimTalk]

Makes the list/table designated by `<Path>` inherit its comment (true) or not (false).

- **Syntax:** `<Path>.InheritComment:boolean`

```
MyDataTable.InheritComment := true
```

### InheritContents [SimTalk]

Makes the list/table designated by `<Path>` inherit its contents from the class (true) or not (false).

- **Syntax:** `<Path>.InheritContents:boolean`

> **Note:** Plant Simulation does not deactivate Inherit Contents when you instantiate the class of a list containing a sublist and then write to the instance (or the sublist) with a method. If you model like that, deactivate Inherit Contents yourself in the window of the list object.

> **Note:** User-defined attributes and local variables do not provide this attribute.

```
MyDataList.InheritContents := false
```

### InheritFormat [SimTalk]

Makes the list/table designated by `<Path>` inherit its format from the class (true) or not (false).

- **Syntax:** `<Path>.InheritFormat:boolean`

> **Note:** User-defined attributes and local variables do not provide this attribute.

```
MyDataStack.InheritFormat := true
```

### MaxDim [SimTalk]

Sets the maximum number of cells for a list with one column designated by `<Path>`.

- **Syntax:** `<Path>.MaxDim:integer`
- **Applies to:** DataStack, DataQueue, DataList.
- **Assignment value:** `-1` for infinite size.

```
MyDataStack.MaxDim := -1                  // unlimited dimension
MyDataQueue.MaxDim := 20                  // 20 entries
MyDataList.MaxDim := 2*MyDataList.MaxDim  // double the number of entries
```

---

## DataTable [object]

Use the object DataTable for storing data in several columns, which can have different data types.

### Description

You can access individual cells in the DataTable via their index (row number and column number). A DataTable can be compared to a shelf in which you enter values and references to the cells and remove them again. Unlike the DataList, the contents of the cells remain in the DataTable, and the DataTable can have blank cells in a range. You can add and remove rows and columns during a simulation run at will.

- The DataTable always opens in the background behind any open dialog boxes. Open it in the foreground with the method `openDialogBox`.
- The DataTable shares its built-in properties with the data type `table`. Note the difference between the object DataTable (which can be inserted into models) and the data type `table`. User-defined attributes and local/global variables of data type `table` are part of another object and are not objects of their own (no own icon).
- For this reason, variables and attributes of data type `table` do not recognize the SimTalk functions of the DataTable (such as `Location` or `existsIcon`). All other methods, especially for read/write access, apply to both the DataTable and to variables/attributes.
- Show the contents of a DataTable in an HtmlReport.
- Hover over the DataTable to show a tooltip with information.
- To change the graphic length and anchor points, click Show Manipulators on the Edit ribbon tab or press **M**.

### Adding the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > InformationFlow > DataTable** on the Home ribbon tab.

> The MaterialsTable of the fluid objects shares the properties of the DataTable.
