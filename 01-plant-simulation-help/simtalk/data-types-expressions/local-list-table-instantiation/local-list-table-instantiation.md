# Instantiating Local Lists and Tables

## Overview

A local variable of data type `list`, `queue`, `stack`, or `table` — as well as lists within lists and tables within tables — does not contain the data itself, but a **reference** to the respective data structure.

When the variables are entered into a Method, they are **void**, meaning they do not yet contain a reference to a data structure. You must create (instantiate) the variable before you can access the data.

Lists and tables provide two methods for instantiation:

- `create` — creates an empty data structure.
- `createNestedList` — creates a nested sublist or subtable.

---

## `create` [SimTalk] - local list

Creates an empty data structure without contents in the local variable designated by `<Local-variable>`.

### Remarks

`create` applies to local variables of data type `list`, `queue`, `stack`, and `table`.

### Type

Method

### Syntax

```
<Local-variable>.create([NumberOfRows:integer])
```

### Parameter

The optional parameter `NumberOfRows` of data type `integer` designates the number of rows in the list or table.

### Example

```simtalk
var orderlist: table[string,real]
orderlist.create
orderlist[1,1] := "cans"
orderlist[2,1] := 3000.0
orderlist.forget    // destroys the table
orderlist.create(4) // recreates the table with 4 rows
```

### See also

- Data Types in Local Variables

---

## `createNestedList` [SimTalk] - local variable

Creates a new sublist or subtable in the local variable designated by `<local-list>` or by `<local-table>`.

### Remarks

The local variable has to be of data type `list`, `queue`, `stack`, or `table`. The data type of the column of this list or table has to be of data type `list`, `stack`, `queue`, or `table` as well.

### Type

Method

### Syntax

```
<Local-list>.createNestedList(Column:integer, Row:integer[, Name:string]) → list
<Local-table>.createNestedList(Column:integer, Row:integer[, Name:string]) → list
```

### Parameters

- `Column` (integer) — designates the column of the cell.
- `Row` (integer) — designates the row of the cell.
- `Name` (string, optional) — designates the name of the sublist or subtable to be created.

### Note

This method also applies to sublists and subtables.

### Return Value

The return value has the data type `list` — the nested list (`DataList`, `DataQueue`, `DataStack`, or `DataTable`) that was created.

### Examples

```simtalk
var t: table[table]
t.create                 // creates a table
t.createNestedList(1,1)  // creates a subtable
t[1,1][2,3] := "Hello world" // writes Hello world into the nested table
```

The code inserts a subtable into cell 1 of the table. It then inserts `Hello world` into the cell at position `2,3`.

```simtalk
var subtable: table
MyDataTable.createNestedList(2,3) // creates a subtable
subtable := MyDataTable[2,3]
subtable.createNestedList(1,1)    // creates a subtable within a subtable
subtable[1,1][4,4] := "Hello world"
```

### See also

- `setCommonFormat` [SimTalk]
- Activating and Deactivating Common Format
- `createNestedList` [SimTalk] - DataQueue
- `createNestedList` [SimTalk] - DataList
- `createNestedList` [SimTalk] - DataTable
- `createNestedList` [SimTalk] - local variable

---

## Related: `Weight` [SimTalk] - data type

A local variable of data type `weight` has a maximum range of values between `-8.9*10^307 ≤ weight ≤ 8.9*10^307`, displayed as `-8.9e307 ≤ real ≤ 8.9e307`.

### Remarks

- When assigning it to a variable or an attribute, Plant Simulation interprets the value as kilograms (kg).
- When outputting it, Plant Simulation converts the value to the unit selected under **File > Model Settings/Preferences > Units > Mass**.
- The data types `time`, `length`, `weight`, `speed`, and `acceleration` are **not compatible**! You can, for example, only assign a value of data type `length`, `real`, or `integer` to a variable of data type `length`.

### See also

- `isWeight` [SimTalk]
