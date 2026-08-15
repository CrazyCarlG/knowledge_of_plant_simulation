# Window of Lists and Tables

This document summarizes the Plant Simulation Help topic *Window of Lists and Tables*, which describes the window of list/table objects, the List ribbon tab, and the related context menus and dialogs.

---

## Window of Lists and Tables

Double-click the icon of a list object (inserted into a simulation model) to open its window.

### Remarks

- To change the properties of the object's **Class**, double-click it in the Class Library or on the tab **Information Flow** in the Toolbox. There you can view/change saved data, enter new data, and adapt the format and data types.
- Access list-object functions on the **List Ribbon Tab**.
- To edit the 3D properties of the object in the 3D model, select it and press the spacebar, then change settings in **Edit 3D Properties**.
- To manipulate the object's graphic, click **Show Manipulators** on the Edit ribbon tab or press `M`.

### See also

- Work with Data in a List or Table
- List Ribbon Tab
- Context Menu of the Contents of List Objects
- Context Menu of Embedded Lists

---

## List Ribbon Tab

The List ribbon tab provides commands to access the functions of list objects. Not all list objects provide all commands.

### Command Reference

| Command | Method or Attribute |
|---|---|
| Import File | `readFile` (SimTalk) - lists |
| Export to File (Text / Object / Excel / XML) | `writeFile`, `writeObjectFile`, `writeExcelFile`, `writeXMLFile` |
| Text File Format | `ColumnSeparator`, `DecimalSeparator`, `TimeFormat` |
| Print List / Print Setup | `printList`, `showPrintDialog`, `PrintRowNumber`, `PrintColumnNumber`, `PrintDataType`, `RepeatRowIndex`, `RepeatColumnIndex`, `PrintInternalLists`, `GenerateColumnWidth` |
| Find / Replace | `find`, `findCeil`, `findFloor` |
| Go To Cell | `Cursor`, `CursorX`, `CursorY` |
| Insert Row | `insertRow` |
| Insert Column | `insertColumn` |
| Sort Ascending / Descending | `sort` |
| Create Formula | `setFormula` |
| Activate Column Index | `ColumnIndex` |
| Activate Row Index | `RowIndex` |
| Edit Format | various |
| Inherit Format | `InheritFormat` |
| Inherit Contents | `InheritContents` |
| Inherit Comment | `InheritComment` |
| Recompute Formulas | `calculateList` |
| Show Comment | `ShowComment` |
| Show Data Type | `ShowDataType` |
| Highlight Empty Cells | `ShowVoid` |
| Open Object | `openDialog`, `openDialogBox` |

The other tabs on the Ribbon Bar provide additional commands pertaining to list objects.

---

## Import File

Imports a previously saved list and opens the **Open** dialog.

You can open these file types:

- **Object Files (*.pslist)** — Contains the contents *and* the Plant Simulation format (data format, dimension, index/column widths, etc.). Lets you exchange lists between models; proprietary format (`.psobj`). Other programs do not recognize it.
- **Text Files (*.txt)** — Contains only the list contents, no Plant Simulation-specific settings. Can be created in a text editor or spreadsheet application. See *Text File Format*.
- **Excel Workbooks (*.xls, .xlsx, .xlsm, .xlsb)** — Plant Simulation uses Excel as a COM-server; MS Excel must be installed. Use the start option `-NativeExcel` to keep the previous (unsupported) Excel interface.

### Excel import notes

- Raw values are imported from Excel and converted inside Plant Simulation.
- When importing into string columns, numerical values are converted in Plant Simulation; the Plant Simulation format may differ from the Excel format.
- Each Excel column should contain only a single data type.
- **Row 0 (zero)** is treated as the column index if present, and is not part of the data-type designation.
- Plant Simulation respects the dimension of the DataTable — e.g., 3 rows × 10 columns imports only the first 3 rows and 10 columns (useful for performance).

### See also

- `readFile`, `readExcelFile`, `readXMLFile`
- Specifying Start Options, `-NativeExcel`

---

## Export to File

Provides commands to export the list in different formats: **Export Text File**, **Export Object File**, **Export Excel File**, **Export XML File**, and **Text File Format**.

### Export Text File

Saves the list contents as a text file (`.txt`) without formatting information. Selectable encodings:

- **ANSI** — 8-bit character set (0–255), superset of ASCII.
- **UTF-8** — Unicode encoding, one to three bytes per character.
- **Unicode** — 16-bit character set, saved as UTF-16 (two bytes per character).

Text-file save/load is governed by the **Text File Format** settings.

### Export Object File

Saves the list as `*.pslist` with contents *and* formatting (data types, column/row formatting, dimension, column/row index). Opens with identical properties in another model; proprietary format.

### Export Excel File

Saves as a Microsoft Excel worksheet (`.xls`), opening the **Save As** dialog.

- Uses Excel as COM-server; MS Excel must be installed. `-NativeExcel` keeps the previous interface.
- Only exports integers in the range **-536,870,912 to 536,870,911** in the required format; values outside are saved as `0`.
- Exports data using the selected unit settings (e.g., meter for `Length`).
- Each Excel column should contain only a single data type; **Row 0** is treated as the column index.
- Import respects the DataTable dimension.

**Data-type conversion table (Plant Simulation → Excel):**

| Plant Simulation | Excel data type | Excel format |
|---|---|---|
| string | String | — |
| Boolean | Boolean | — |
| Integer / Real | Number | — |
| Object / Table / List / Stack / Queue | String | — |
| Money / Length / Weight / Speed / Acceleration | Number | — |
| DateTime | Number | `dd/mm/yyyy hh:mm:ss.000` |
| Date | Number | `dd/mm/yyyy` |
| Time | Number | `dd:hh:mm:ss.000` |

### Export XML File

Saves the list as an XML file (`.xml`) with UTF-8 encoding and the tag `PlantSimulationTable`.

---

## Text File Format

Opens the **Text File Format** dialog to select settings for exporting/importing text files. Plant Simulation exports and imports data row by row.

- **Column Separator**: Tab, Space, Semicolon, or Comma.
  - *Note:* Avoid using the comma as *both* the column separator and decimal separator.
- **Decimal Separator**: Period (`.`) or Comma (`,`).
- **Time format**: `S`, `M:S`, `H:M:S`, or `D:H:M:S` — lets spreadsheet applications read time values they could not otherwise recognize.

SimTalk: `ColumnSeparator`, `DecimalSeparator`, `TimeFormat`.

---

## Print List / Print Setup

- **Print List** opens the **Print** dialog (printer, paper format, orientation, copies).
- **Print Setup** opens the **Print Setup** dialog to choose which items are printed.

| Check Box | Description | Attribute |
|---|---|---|
| Row Number | Prints the row number before each cell | `PrintRowNumber` |
| Column Number | Prints the column number above each column | `PrintColumnNumber` |
| Data Type | Prints the data type of each column | `PrintDataType` |
| Repeat Row Index | Repeats the user-defined row index on each page | `RepeatRowIndex` |
| Repeat Column Index | Repeats the user-defined column index on each page | `RepeatColumnIndex` |
| Internal Lists | Prints nested tables the list contains | `PrintInternalLists` |
| Column Width | Prints columns using the widest column's width | `GenerateColumnWidth` |

---

## Find / Replace

- **Find** finds and selects the cell containing an expression. Searches the entire list if no cell is selected; otherwise starts at the selected cell toward the end.
- **Replace** finds an expression and replaces it.

Both dialogs support:

- **Match Case** — case-sensitive matching.
- **Match Entire Cell Contents** — exact full-cell match.
- **Search in Rows / Columns**.
- **Search criterion**: `Find` (exact), `Find ceil(ing)` (`findCeil`, value ≥ expression), `Find floor` (`findFloor`, value ≤ expression).
- **Find Next**, **Replace**, **Replace All**, **Cancel**.

SimTalk: `find`, `findCeil`, `findFloor`.

---

## Go To Cell

Moves to a specific cell in the list/table by entering its **Column** and **Row** numbers (the cell becomes the starting point for scrolling). Shows the number of **Occupied Columns** and **Occupied Rows**.

SimTalk: `Cursor`, `CursorX`, `CursorY`.

---

## Insert Row / Insert Column

- **Insert Row** — adds an empty row above the active cell/row.
- **Insert Column** — inserts a new empty column to the left of the selected column; existing columns move right.

SimTalk: `insertRow`, `getRowNo`, `cutRow`; `insertColumn`, `getColumnNo`, `cutColumn`.

---

## Sort Ascending / Sort Descending

- **Ascending**: lowest number, earliest date, or start of alphabet first.
- **Descending**: highest number, latest date, or end of alphabet first.

Sorting is case-sensitive and only sorts the selected column of the DataTable. Empty cells are sorted at the end (ascending) or start (descending) of the column.

SimTalk: `sort`, `inOrder`.

---

## Create Formula

Activates/deactivates formula mode for the DataTable. A formula can access/link other cells or object attributes.

Steps:

1. Click the button to activate formula mode.
2. Click a cell (or the text box above the list) and type the expression.
   - *Note:* If a distribution function is called with `z_`, you must type the random number stream — formulas never use the random stream of the surrounding object.
3. Press Enter to show the calculated value in the cell.
4. Click a formula cell to show the formula itself in the text box.

*Note:* The result's data type must match the data type of the cell/column.

See also: `getFormula`, `setFormula`.

---

## Activate Column Index / Activate Row Index

Activates the column/row index (header). Click again to deactivate and delete existing contents.

- If both indexes are active, cell `[0,0]` counts as part of the **column** index, not the row index.
- You can use the **system index** (assigned numbers) or a **user-defined index** (any meaningful expression).
- In the expression `[3,1]`, the first value is the **column**, the second is the **row**.

**Example (user-defined indexes):**

```
orders["urgent","preferred customer"]
vehicles["truck",#1]
switch["light",true]
plant["Chicago",.building1.drill]
```

- User-defined indexes are more meaningful and less error-prone than system indexes; they remain valid when columns/rows are added (unlike the system index, which shifts). Accessing a user-defined index is slightly slower.
- User-defined indexes may only be defined for the data types **string, integer, object, and boolean**.
- For an **integer** index, prefix the expression with a number sign/hash `#` to distinguish it from the system index.

To set the data type of an index: click the Activate Column/Row Index button, select the index column/row (number 0), click **Format**, choose the data type, and optionally set a **Format String**, **Fast Index Access**, and **Unique Index Key**.

- **Fast Index Access** — creates an internal structure for fast user-defined index lookups (slightly increases memory and index-change time). Recommended for large tables.
- **Unique Index Key** — only allows unique entries (Plant Simulation highlights duplicates in red; no warning is shown when assigning duplicates in a Method).

SimTalk (column): `ColumnIndex`, `ShowColumnIndex`, `DataTypeColumnIndex`, `FormatStringColumnIndex`, `XDimIndex`, `FastAccessColumnIndex`, `UniqueKeyColumnIndex`.
SimTalk (row): `RowIndex`, `ShowRowIndex`, `FormatStringRowIndex`, `YDimIndex`, `FastAccessRowIndex`, `UniqueKeyRowIndex`.

---

## Edit Format

Opens the **Edit Format** dialog to edit Settings, Permissions, Dimension, and Data Type. The visible tabs depend on the selection:

- Selecting cell(s)/range → **Settings** and **Permissions** tabs.
- Selecting column(s) → additionally **Data Type** and **Dimension** tabs.
- Selecting the entire list → settings apply to the whole list.

The **Range** box shows the selected range. **Apply** applies settings without closing; **OK** applies and closes; **Cancel** discards changes.

### Tab Settings

Settings for Alignment, Font Size, Font Color, Background Color, and **Column Index Belongs to Contents**.

- **Alignment** — Left, Right, or Center (`Alignment`, `setAlignmentCells`, `setAlignmentColumn`, `setAlignmentRow`, etc.).
- **Font Size** — the list auto-adjusts cell width/height (`FontSize`, `setFontsizeColumn`, `setFontSizeCells`, etc.).
- **Font Color** / **Background Color** — choose a predefined color or **More Colors**; **Default** uses the theme color (`FontColor`, `BackgroundColor`, and their `set*`/`get*` methods).
- **Column Index Belongs to Contents** — when checked, the column index is inherited together with the contents (via Inherit Contents); when cleared, it is inherited with the format (via Inherit Format). Default is deactivated for new models (index belongs to format). Only the DataTable provides this setting. SimTalk: `ColumnIndexContents`, `DataTable.delete`.

### Tab Permissions

Select read/write privileges via the **Editor** and **Information Flow** check boxes.

- **Editor** — checked = read-only in the list window; cleared = read/write in the List Editor (`EditorReadOnly`).
- **Information Flow** — checked = read-only access via Methods/Attributes; cleared = read/write via Methods/Attributes (`InfoflowReadOnly`). Only active when all cells containing an entry are selected.

### Tab Dimension

Set **Number of Rows** (and, for DataTable, **Number of Columns**) and **Column Width**. Leaving rows/columns empty means the dimension is unlimited.

- **Number of Rows** (`MaxDim`, `MaxYDim`)
- **Number of Columns** (`MaxDim`, `MaxXDim`)
- **Column Width** — in character widths of a non-proportional font; default 20, max 180 (`ColumnWidth`, `getColumnWidth`, `setColumnWidth`).

The Data Type and Dimension tabs are only shown after selecting one or more columns via the column header.

### Tab Data Type

Select the **Data Type** and optionally a **Format String**.

**Available data types:**

| Data type | Description |
|---|---|
| Acceleration | m/s² (Conveyor, Track, TwoLaneTrack, Transporter) |
| Boolean | `true` or `false` |
| Date | `dd.MM.yyyy` |
| DateTime | `dd.MM.yyyy HH:mm:ss` |
| Integer | integer value |
| Length | floating point (unit-dependent) |
| List | one-column list (DataList properties) |
| Money | floating point |
| Object | reference to a model/object |
| Queue | one-column list (DataQueue properties) |
| Real | floating point (e.g., `3.1415`) |
| Speed | floating point (unit-dependent) |
| Stack | one-column list (DataStack properties) |
| String | characters, numbers, special characters |
| Table | one or more columns (DataTable properties) |
| Time | `hh:mm:ss.ss` |
| Weight | floating point (unit-dependent) |

*Notes:*
- You can only change the data type for entire column(s), not for cells/rows.
- Double-clicking a `true`/`false` cell toggles the value.
- Dates can be entered day-month-year or `year/month/day` (e.g., `2026/11/11` in English models).

SimTalk: `DataType`, `setDataType`, `getDataType`, `setDataTypeDefault`.

#### Format String

Restricts the data users can enter in the list window (does not restrict Method assignments). Applies to Integer, Real, Length, Weight, Speed, Acceleration, Money, and String.

- **String** format characters (per digit):

| Letter | Output |
|---|---|
| A | Letters only |
| U | Upper case letters only |
| X | All characters |
| C | Upper case letters and numbers |
| N | Numbers only |
| L | Letters and numbers |
| I | All characters permitted for object names (letters, umlaut, numbers, underscore) |

  Example `AANXU`: first two digits must be letters, third a number, fourth any character, fifth an upper-case letter. Separating several terms with semicolons (no trailing blank) creates a drop-down list (e.g., `Entry1;Entry2;Random`).

- **Integer** — a number limits digits shown (e.g., `3` shows first three digits); a minus prefix (e.g., `-3`) allows negative values. Using `color` as the format string opens the Windows Color dialog (stores RGB via `makeRGBValue`).
- **Real** — two numbers separated by a point restrict digits before/after the decimal (e.g., `5.3` = 5 digits total, 3 after decimal; `-6.3` allows negatives).

SimTalk: `FormatString`, `getFormatString`, `setFormatString`, `makeRGBValue`.

#### Common Format

For data types Table, List, Stack, Queue, the **Common Format** check box replaces the Format String text box and adds the **Tab Contents**.

- Force all lists in the displayed range into the same format, then create a template list on Tab Contents. Newly created lists inherit these format properties.
- If Common Format is active, assigning a subtable to a table cell creates a **copy** of the assigned table; otherwise Plant Simulation enters a **reference**.

SimTalk: `CommonFormatColumnIndex`, `setCommonFormat`, `setCommonFormatData`, `getCommonFormatData`.

##### Activating and Deactivating Common Format

**First example (Common Format selected)** — the Method uses a local variable to access a list in a table; Plant Simulation accesses a reference:

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

**Second example (Common Format cleared)** — the same result is reached by assigning a local list with the same format; the format is determined by the local variable, not the table:

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

*Note:* Assigning a list/table to a cell with list/table format while Common Format is active may create a copy instead of a reference, depending on the assigned list/table format.

---

## Tab Contents

Select the common format of the list (shown for data types Table, List, Stack, Queue). Create a template list here to force all lists in the displayed range into the same format.

See also: `createNestedList` (DataQueue, DataList, DataTable), `setCommonFormat`.

---

## Inherit Format / Inherit Contents / Inherit Comment

- **Inherit Format** — toggles format inheritance. An inserted list inherits its format from its class; you can change the format only after turning it off. Turning it off also turns off Inherit Contents (`InheritFormat`).
- **Inherit Contents** — toggles contents inheritance. An inserted list inherits contents from its class; you can change contents only after turning it off. Turning it off also turns off Inherit Format; typing data into a list automatically turns it off. *Note:* Plant Simulation does **not** turn it off when instantiating a class containing a sublist and then writing via a Method — you must turn it off yourself (`InheritContents`).
- **Inherit Comment** — toggles inheritance of comments added to the list (`InheritComment`).

---

## Recompute Formulas

Recomputes typed formulas and shows their current values in the respective cells (`calculateList`).

---

## Show Comment / Show Data Type / Highlight Empty Cells

- **Show Comment** — shows/hides the descriptive-text box above the table contents. The comment also appears as a tooltip when dragging over the object in the Frame, and as a heading in `HtmlReport` (`Comment`, `ShowComment`).
- **Show Data Type** — shows/hides data types of columns and rows (abbreviated if too long; includes user-defined indexes) (`ShowDataType`).
- **Highlight Empty Cells** — toggles light-gray display of empty cells. Cells containing an empty string `""` are *not* empty (`ShowVoid`).

---

## Open Object

Opens the dialog of the object whose name is typed into a cell of data types object, table, stack, or queue (or press `F2`). SimTalk: `openDialog`, `openDialogBox`.

---

## Context Menu of Embedded Lists

Embedded lists provide context-menu commands for often-used settings. Examples include the Services list of the Failure Importer, the Creation Table of the WorkerPool, the Parts Table of the GanttChart, the FlowControl strategy lists, and the Trigger/ShiftCalendar/AttributeExplorer lists. Not all embedded lists provide all commands.

Commands:

| Command | Description | SimTalk |
|---|---|---|
| Open Object | Open the dialog of the object in the cell (or `F2`) | `openDialog`, `openDialogBox` |
| Select Object | Pick an object via the **Select Object** dialog | — |
| Cut | Cut cell/column/row contents to clipboard | `cutColumn`, `cutRow` |
| Copy | Copy cell/column/row contents to clipboard | `copy`, `copyRangeTo` |
| Paste | Paste clipboard contents into the selected cell | — |
| Delete | Delete cell/column/row contents | `delete` |
| Select All | Select the entire list contents | — |
| Delete Row | Delete the selected row | — |
| Insert Row | Insert an empty row above the selected row | `insertRow` |
| Append Row | Insert an empty row below the last row | — |
| Sort Ascending / Descending | Sort (case-sensitive; only selected rows/columns) | `sort`, `inOrder` |
| Show Comment | Show/hide the descriptive-text box | `ShowComment` |
| Import | Import a file (`.pslist`, `.txt`, `.xls/.xlsc/.xlsm/.xlsb`, `.xml`) | — |
| Export | Export to tab-delimited text/Excel | — |

**Import/Export notes:**

- Importing a file only works correctly if the file contains the **Name** of the attribute (not the Alias).
- Export formats: ANSI, UTF-8, Unicode text files, and Excel workbooks (`.xls`).

---

## Context Menu of the Contents of List Objects

The context menu of list-object contents provides the most important commands (some on the mini toolbar).

Toolbar commands include: **Open Location**, **Open Origin**, **Open Class**, **Copy Objects**, **Cut Objects**, **Paste Objects**, **Delete Objects**, **Select All**, **Open Object**, **Insert Row**, **Remove Row**, **Insert Column**, **Remove Column**, **Insert**, **Format**, **Find**, **Sort Ascending**, **Sort Descending**.

| Command | Description | SimTalk |
|---|---|---|
| Open Location | Open the object containing the list/table | `Location` |
| Open Origin | Open the object from which the selected object was derived | `Origin` |
| Open Class | Open the dialog of the class in the Class Library | `derive` |
| Cut / Copy / Paste / Delete | Clipboard operations on cell/column/row | `cutColumn`, `cutRow`, `copy`, `delete` |
| Select All | Select the entire list contents | — |
| Open Object | Open the dialog of the object in the cell (or `F2`) | `openDialog`, `openDialogBox` |
| Show Object | Show/select the object in the Frame (object-type column) | — |
| Insert Row / Remove Row | Insert an empty row above / remove the selected row (rows shift) | `insertRow`, `cutRow` |
| Insert Column / Remove Column | Insert a new empty column left / remove selected column | `insertColumn` |
| Insert | Insert empty rows until the list is full (limited by Dimension) | `insert` |
| Format | Open the **Edit Format** dialog | — |
| Find | Open the **Find** dialog | — |
| Sort Ascending / Descending | Sort selected rows/columns (case-sensitive) | `sort`, `inOrder` |

Notes:
- **Remove Row** is not available for the row containing the row index; **Remove Column** is not available for the column containing the column index.
- **Insert** fills the list until the specified Dimension (DataList/DataStack/DataQueue) is reached.

---

## Accessing a Range of Cells with a Method

You can also process a contiguous range of cells (not just individual entries). Some methods (e.g., `min`, `max`) only apply to a range, which requires special syntax.

Two cases:

- **Cell Ranges in Lists with One Column**
- **Cell Ranges in Tables with Several Columns**

### Cell Ranges in Lists with One Column

Access a cell range in a one-column list using left curly brace `{`, the first cell number, right curly brace `}`, two periods `..`, left curly brace `{`, the last cell number, and the closing curly brace `}`.

---

*Source: Plant Simulation Help — Window of Lists and Tables (pp. 11-3823 ff.). Unpublished work. © 2026 Siemens.*
