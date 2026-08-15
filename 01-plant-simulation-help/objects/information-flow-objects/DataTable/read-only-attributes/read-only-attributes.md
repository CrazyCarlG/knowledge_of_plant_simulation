# Read-Only Attributes of the DataTable

The DataTable provides:

- The read-only attributes listed below.
- The _Read-Only Attributes of Lists and Tables.
- The _Read-Only Attributes of All Objects.

You can query the values of read-only attributes, but you cannot set them, because Plant Simulation computes the value at the point in time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which an instance was inserted to show them for the selected Instance.

To query the value of a read-only attribute, for example:

```simtalk
print MyDataTable.Full
```

---

## XDim [SimTalk] - DataTable

Returns the number of the last column of the DataTable designated by `<Path>` that contains an entry.

**Remarks:** Plant Simulation does not count the user-defined index.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.XDim -> integer`
- **Watchable:** Yes
- **Return Value:** data type `integer`

**Example:**

```simtalk
print MyDataTable.XDim
print timeSequence.XDim
```

---

## XDimIndex [SimTalk]

Returns the last cell of the column index of the DataTable designated by `<Path>` that contains an entry.

**Remarks:** Plant Simulation does not count column 0.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.XDimIndex -> integer`
- **Return Value:** data type `integer`

**Example:**

```simtalk
print MyDataTable.XDimIndex
```

---

## YDim [SimTalk] - DataTable

Returns the number of the last row of the DataTable designated by `<Path>` that contains an entry.

**Remarks:** Plant Simulation does not count the user-defined index.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.YDim -> integer`
- **Watchable:** Yes
- **Return Value:** data type `integer`

**Example:**

```simtalk
print MyDataTable.YDim
print timeSequence.YDim
```

---

## YDimIndex [SimTalk]

Returns the last cell of the row index of the DataTable designated by `<Path>` that contains an entry.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.YDimIndex -> integer`
- **Return Value:** data type `integer`

**Example:**

```simtalk
print MyDataTable.YDimIndex
```

---

## See also

- `XDim [SimTalk] - DataTable`
- `YDim [SimTalk] - DataTable`
- `XDimIndex [SimTalk]`
- `YDimIndex [SimTalk]`
- `ColumnIndex [SimTalk]`
- `RowIndex [SimTalk]`
- Number of Columns [lists]
- Number of Rows [lists]
