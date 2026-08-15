# Creating Lists within Lists and Tables

This topic describes how to create lists (sublists) and tables (subtables) inside other lists and tables in Plant Simulation.

## Overview

You can create nested lists and tables inside the list objects **DataList**, **DataStack**, **DataQueue**, and **DataTable**. There are three general approaches:

- Add a sublist to a cell within the object.
- Insert a list object from a Frame or the Class Library into a cell of the list object (drag-and-drop).
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

To create a sublist or a subtable in objects of type **DataQueue** or **DataStack**:

- Add the sublist to a cell within the object.
- Insert a list object from the Class Library into your simulation model: drag that object to the active cell of the DataQueue/DataStack and drop it there. This inserts the path to and the name of the list or table into the active cell.
- Assign a DataList to a DataQueue or a DataStack in a Method.

### Assign a DataList to a DataQueue or a DataStack in a Method

Within a Method you can declare a local variable of data type `Stack`, `Queue`, `List`, and `Table`. After you create a list of these types, you can assign it to cells in a queue or stack. Initially, all of the cells of the local variable are void. Only when Plant Simulation creates the list, by executing the method `create`, will it actually create it and enter a pointer to this new list into the DataList.

**Syntax**

```
<Local-variable>.create
```

**Example**

```simtalk
var l: list[string]
l.create
l.insert(1,"Hello")
```

You can then insert this list into another list (see also Common Format).

## Creating a List within a DataList

To create a list or table in an object of type **DataList**:

- Add the sublist to a cell within the object.
- Insert a list into a DataList from a Frame: drag that object to the active cell of the DataList and drop it there. This inserts the path to and the name of the list or table into the active cell.
- Assign a list to a DataList in a Method.

### Insert a List into a DataList from a Frame

When you insert a list object from the Class Library into your simulation model, it will be empty, as it is unknown at this time how many rows it will contain. Only when Plant Simulation creates the list, by executing the method `create`, will it actually create it and enter a pointer to this new list into the DataList.

**Syntax**

```
<DataList-Path>.createNestedList(integer)
```

The expression `<DataList-path>` is the name of the DataList in which Plant Simulation creates the entry designated by the parameter of data type `integer`. This list has the data type you specified. The method `create` can access every cell. If you type in an index that is greater than the largest index permitted, Plant Simulation inserts the entry into the first blank cell of the list, regardless of the actual index. That is to say, a list never has blank cells. If you create a list in a cell that already contains another list, Plant Simulation moves all entries up one position in the index.

**Example** — a DataList of data type `stack[string]` without entries:

```simtalk
MyDataList.createNestedList(5) // create first entry
MyDataList.read(1).insert(1,"hello")
```

The method `DataList.read(1)` returns the contents of cell 1 of the DataList, a stack of data type `string`. Using the method `insertList` and the parameter, you can now insert text into the stack.

### Assign a List to a DataList in a Method

Within a Method you can declare a local variable of data type `Stack`, `Queue`, `List`, and `Table`. After you create a list of these types, you can assign it to cells in a list. Initially, all of the cells of the local variable are void. Only when Plant Simulation creates the list, by executing the method `create`, will it actually create it and enter a pointer to this new list into the DataList.

**Syntax**

```
<Local-variable>.create
```

**Example**

```simtalk
var s: stack[string]
s.create
s.insert("Hello")
```

You can then insert this list into another list (see also Common Format).

## Creating a List within a DataTable

To create a list or table in an object of type **DataTable**:

- Add the sublist to a cell within the object.
- Insert a list into a DataTable from a Frame: drag that object to the active cell of the DataTable and drop it there. This inserts the path to and the name of the list or table into the active cell.
- Assign a list to a DataTable in a Method.

### Insert a List into a DataTable from a Frame

When you insert a DataTable from the Class Library into your simulation model, it will be empty as it is unknown at this time how many columns and rows it will contain. Only when Plant Simulation creates the DataTable, by running the method `createNestedList`, will it actually create it and enter a pointer to this new list into the DataTable.

**Syntax**

```
<Path>.createNestedList(index1,index2)
```

The expression `Path` designates the name of the DataTable in which Plant Simulation creates the subtable designated by the parameter `[index1,index2]`. The method `create` can access every position. If you create a list in an entry that already contains an entry, Plant Simulation overwrites the existing entry.

**Example** — a DataTable some of whose cells contain other DataTables:

```simtalk
MyDataTable.createNestedList(2,1) // creates the first entry
MyDataTable[2,1][1,1] := "Hello"  // DataTable in DataTable
```

The method `DataTable[2,1]` returns the table occupying the first cell of the table. Accessing the index at the coordinates `[1,1]` and using an assignment, you may now enter a string into the table.

### Assign a List to a DataTable in a Method

Within a Method you can declare a local variable of data type `Stack`, `Queue`, `List`, and `Table`. After you create a list of these types, you can assign it to cells in a table. Initially, all of the cells of the local variable are void. Only when Plant Simulation creates the list as a local variable, by executing the method `create`, and when assigning it, will it actually create it and enter a pointer to this new list into the DataTable.

**Syntax**

```
<Local-variable>.create
```

**Example**

```simtalk
var t: table[string,string]
t.create
t[1,1] := "Hello"
```

You can then insert this list into another list (see also Common Format).

## Accessing the Name of a Sublist with a Method

To open the sublist contained in a cell of type `Stack`, `Queue`, `List`, and `Table`:

- Hold down **Shift** and double-click into the cell.
- Or right-click the cell and select **Open Object**.
- Or click in the text box and press **F2**.

Use the attribute `Name` to access the name of the sublist via information flow.

**Example**

```simtalk
var str: string
str := .Models.MyPlantAnytown.SteeringTypes["Jacks","9149"].Name
// returns the value of the cell that contains the subtable, 4 in the example
```

## Methods of Lists and Tables

The lists and tables share a number of methods. The different kinds — **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence** — in addition provide object-specific methods.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the attributes and methods of the selected Instance.

An example of the Syntax line of the individual methods might look like this:

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
