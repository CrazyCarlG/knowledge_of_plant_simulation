# Creating Lists within Lists and Tables

This README summarizes the topic **"Creating Lists within Lists and Tables"**, which describes how to create nested lists (sublists) and tables (subtables) inside other list objects in Plant Simulation.

## Overview

Nested lists and tables can be created inside the list objects **DataList**, **DataStack**, **DataQueue**, and **DataTable**. There are three general approaches:

- Add a sublist to a cell within the object.
- Insert a list object from a Frame or the Class Library into a cell (drag-and-drop).
- Assign a list to a cell programmatically in a Method.

## Drag-and-Drop in Lists and Tables

Drag-and-drop in lists and tables performs a number of actions. The expression **Accelerator** designates the key on the keyboard.

| To do this | Drag from | To | Accelerator |
|---|---|---|---|
| Move the selected text | table window | table window | — |
| Copy the selected text | table window | table window | Ctrl |
| Insert the selected text | any | table window | any |
| Copy the selected text | table window | any | Ctrl |
| Cut the selected text | table window | any | — |

## Creating a List within a DataQueue or DataStack

To create a sublist or subtable in a **DataQueue** or **DataStack**:

- Add the sublist to a cell within the object.
- Drag a list object from the Class Library into the active cell (inserts the path and name of the list/table).
- Assign a DataList to the object in a Method.

### Assign a DataList to a DataQueue or DataStack in a Method

Declare a local variable of type `Stack`, `Queue`, `List`, or `Table`; create the list with `create`, then assign it to cells. Initially all cells of the local variable are void until the list is actually created.

**Syntax:** `<Local-variable>.create`

**Example:**
```simtalk
var l: list[string]
l.create
l.insert(1,"Hello")
```

## Creating a List within a DataList

To create a list or table in a **DataList**:

- Add the sublist to a cell within the object.
- Drag a list object from a Frame into the active cell.
- Assign a list in a Method.

### Insert a List into a DataList from a Frame

The inserted list is initially empty; only running `create` actually creates it and enters a pointer into the DataList.

**Syntax:** `<DataList-Path>.createNestedList(integer)`

The integer parameter is the index. If the index is greater than the largest permitted index, Plant Simulation inserts the entry into the first blank cell (a list never has blank cells). If a list already exists in that cell, all entries move up one position.

**Example** — a DataList of type `stack[string]`:
```simtalk
MyDataList.createNestedList(5) // create first entry
MyDataList.read(1).insert(1,"hello")
```

### Assign a List to a DataList in a Method

Same pattern: declare a local variable, call `create`, then assign.

**Example:**
```simtalk
var s: stack[string]
s.create
s.insert("Hello")
```

## Creating a List within a DataTable

To create a list or table in a **DataTable**:

- Add the sublist to a cell within the object.
- Drag a list object from a Frame into the active cell.
- Assign a list in a Method.

### Insert a List into a DataTable from a Frame

The inserted DataTable is empty until `createNestedList` runs and creates a pointer to the new subtable.

**Syntax:** `<Path>.createNestedList(index1,index2)`

If you create a list in an entry that already contains an entry, Plant Simulation overwrites the existing entry.

**Example** — a DataTable whose cells contain other DataTables:
```simtalk
MyDataTable.createNestedList(2,1) // creates the first entry
MyDataTable[2,1][1,1] := "Hello"  // DataTable in DataTable
```

### Assign a List to a DataTable in a Method

Declare a local variable, call `create`, then assign it to a cell.

**Example:**
```simtalk
var t: table[string,string]
t.create
t[1,1] := "Hello"
```

## Accessing the Name of a Sublist with a Method

To open a sublist contained in a cell of type `Stack`, `Queue`, `List`, or `Table`:

- Hold **Shift** and double-click the cell.
- Right-click the cell and select **Open Object**.
- Click in the text box and press **F2**.

Use the attribute `Name` to access the sublist name via information flow.

**Example:**
```simtalk
var str: string
str := .Models.MyPlantAnytown.SteeringTypes["Jacks","9149"].Name
// returns the value of the cell that contains the subtable, 4 in the example
```

## Methods of Lists and Tables

Lists and tables share a number of methods. The kinds **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence** additionally provide object-specific methods.

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library (for the selected Class).
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame (for the selected Instance).

An example syntax line of a method:

```
<Path>.readFile(FileName:string[, NoDebugger:boolean:=false,
CodePage:string:="ANSI"]) → boolean
```

The expression `<Path>` designates the path of the object to which the method applies.

## See Also

- `createNestedList` [SimTalk] - DataQueue
- `createNestedList` [SimTalk] - DataList
- `createNestedList` [SimTalk] - DataTable
- `create` [SimTalk] - local list
- `setCommonFormat` [SimTalk]
- `getCommonFormat` [SimTalk]
- `Name` [SimTalk] - DataTable
