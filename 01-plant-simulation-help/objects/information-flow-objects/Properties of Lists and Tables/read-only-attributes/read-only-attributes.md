# Read-Only Attributes of Lists and Tables

Lists and tables provide the read-only attributes listed below for returning their state.

You can query the values of the read-only attributes, but you cannot set them — Plant Simulation computes the value for the point in time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, on the tab *Statistics*).

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class**.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected **Instance**.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyDataTable.Full
```

---

## Void [SimTalk] - cells of lists/tables

Returns whether the specified cell of the list/table designated by `<Path>` is empty (`true`) or not (`false`).

**Type:** Read-only attribute

**Syntax**

```simtalk
<Path-of-the-list[row]>.void -> boolean
<Path-of-the-table[column,row]>.void -> boolean
```

**Return Value**

The return value has the data type `boolean`.

**Example**

```simtalk
if not DataTable[1,1].void
   DataTable[1,1] += 1
end
```

---

## Dim [SimTalk] - lists

Returns the **Dimension**, i.e., the number of entries, of the list/table designated by `<Path>`.

**Remarks**

For a DataTable the dimension is the product of x-dimension/column times the y-dimension/cell.

The read-only attribute applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

**Type:** Read-only attribute

**Syntax**

```simtalk
<Path>.Dim → integer
```

**Watchable:** The read-only attribute is watchable.

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print MyDataStack.Dim
number := MyDataQueue.Dim
print MyDataList.Dim
number := table.Dim
```

---

## Empty [SimTalk] - lists

Returns whether the list/table designated by `<Path>` contains blank cells (`true`) or no blank cells (`false`).

**Remarks**

The read-only attribute applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

**Type:** Read-only attribute

**Syntax**

```simtalk
<Path>.Empty → boolean
```

**Return Value**

The return value has the data type `boolean`.

**Example**

```simtalk
print MyDataQueue.Empty
print MyDataList.Empty
print MyDataTable.Empty
```

---

## Full [SimTalk] - lists

Returns whether the list/table designated by `<Path>` is full (`true`) or not (`false`).

**Remarks**

Normally the number of entries/cells in a list/table is unlimited, meaning it will never be full. You can limit the number of cells in the dialog or with the attributes `MaxDim` or `MaxXDim` and `MaxYDim`.

The read-only attribute applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

**Type:** Read-only attribute

**Syntax**

```simtalk
<Path>.Full → boolean
```

**Watchable:** The read-only attribute is watchable.

**Return Value**

The return value has the data type `boolean`.

**Example**

```simtalk
print MyDataStack.Full
print MyDataList.Full
print MyDataTable.Full
```

**See also:** `MaxDim`, `MaxXDim`, `MaxYDim`

---

## Occupied [SimTalk] - lists

Returns whether at least one cell of the list/table designated by `<Path>` contains an entry (`true`) or not (`false`).

**Remarks**

The read-only attribute applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

**Type:** Read-only attribute

**Syntax**

```simtalk
<Path>.Occupied → boolean
```

**Return Value**

The return value has the data type `boolean`.

**Example**

```simtalk
print MyDataStack.Occupied
print MyDataList.Occupied
print MyDataTable.Occupied
```

---

## Related: Attributes of Lists and Tables

All manifestations of lists and tables — **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence** — share a number of predefined attributes controlling their behavior or representing their state.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class**.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected **Instance**.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
MyDataTable.MaxXDim := -1
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print MyDataTable.MaxXDim
posit := Station.Cont.XPos
```

### See also

- Attributes for the Format of Lists and Tables
- Attributes for the Text Format of Lists and Tables
- Attributes for Printing Lists and Tables
- Attributes for Showing Settings of Lists and Tables
- Miscellaneous Attributes of Lists and Tables

---

*Source: Plant Simulation Help — Read-Only Attributes of Lists and Tables*
