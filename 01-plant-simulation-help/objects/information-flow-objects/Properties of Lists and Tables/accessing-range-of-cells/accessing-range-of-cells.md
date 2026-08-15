# Accessing a Range of Cells with a Method

You can access not only individual entries in a single cell of the lists, but also process a contiguous range of cells.

## Remarks

A number of methods, such as `min` and `max`, only apply to a range. If you access a range of cells, you have to use a special syntax.

We differentiate between:

- Cell Ranges in Lists with One Column
- Cell Ranges in Tables with Several Columns

---

## Ranges in Lists with One Column

Access a cell range in a list with one column by typing:

- the left curly brace `{`
- the number of the first cell in the range
- the right curly brace `}`
- two periods `..`
- the left curly brace `{`
- the number of the last cell in the range
- the closing curly brace `}`

The syntax diagram describes the structure of a range for lists with one column, for example for the objects `DataStack`, `DataQueue`, and `DataList`.

### Specify the Identifier of a Cell [one column]

The left curly brace `{` designates the start of the range, followed by the number of the index of the cell, followed by a right curly brace `}`.

The direct statement consists of the identifier of a cell. This identifier may be a number greater than 0, a user-defined index, or an asterisk `*`, which stands for all cells.

**Example**

```simtalk
{1} // first cell
{*} // all cells
```

### Specifying a Range of Cells [one column]

The from-to statement consists of the identifiers of two cells within braces, separated by two periods.

If you do not know the identifier of the last cell, type in `{*}`, which designates the last cell if preceded by two periods.

| Type in | To access |
| --- | --- |
| `{1,3}` | the cell in column 1, row 3 |
| `{1,*}` | all rows in column 1 |
| `{*,3}` | all columns in row 3 |
| `{*,*}` | the entire list |

**Example**

```simtalk
{2}..{4} // cells 2 to 4
{3}..{*} // from cell 3 to the last cell in the range
```

### Address a User-defined Index [one column]

For a user-defined index of data type `integer`, add the number sign/hash `#` in front of the identifier, because the system index (the numbers of rows and columns Plant Simulation assigns) also has the data type `integer`.

Without the number sign, Plant Simulation would not be able to distinguish whether to use the system index or the user-defined index.

**Example**

```simtalk
[2]  // system index
[#2] // user-defined index
```

---

## Cell Ranges in Tables with Several Columns

Plant Simulation can process contiguous ranges of cells of tables spanning several columns. A number of methods do not work without specifying a range.

### Specify the Identifier of a Cell [several columns]

To access a cell, type in the identifier of the column and the identifier of the row, separated by a comma.

The identifier for the column and row may be a number greater than 0, a user-defined index, or an asterisk `*`, which stands for the entire table.

The left curly bracket `{` designates the start of the range, followed by the identifier of the column, a comma, the identifier of the row, and a right curly bracket `}`.

| Type in | To access |
| --- | --- |
| `{1,3}` | the cell in column 1, row 3 |
| `{1,*}` | all rows in column 1 |
| `{*,3}` | all columns in row 3 |
| `{*,*}` | the entire table |

**Example**

```simtalk
{1,3}                  // the cell in column 1, row 3
{"vehicle","door"}     // the cell with the column index vehicle and the
                       // row index door
{2,*}                  // all cells in column 2
```

### Specifying a Range of Cells [several columns]

To access a range of cells, use the from-to statement. It consists of two cells located in two columns, separated by two periods.

The first identifier designates the top-left cell (column number and row number); the second designates the bottom-right cell (column number and row number). If the second identifier is `{*,*}`, Plant Simulation processes the table up to the highest valid column index and row index.

| Type in | To access |
| --- | --- |
| `{1,2}..{3,5}` | the cells starting with column 1, row 2 to column 3, row 5 |
| `{1,*}..{4,*}` | all rows in columns 1 to 4 |
| `{2,3}..{*,3}` | all columns in row 3 starting with column 2 |
| `{2,3}..{*,*}` | all columns starting with column 2, row 3 to the highest valid cell |
| `{*,*}..{3,5}` | all columns up to column 3 and all rows until row 5 |
| `{4,*}` | all rows in column 4 including the column index if *Column Index Belongs to Contents* is active |
| `{"ColumnB", 0}..{"ColumnB",*}` | the column index of columnB and all rows in columnB |

**Example**

```simtalk
{1,2}..{3,5}                        // cells starting with column 1, row 2
                                    // to column 3, row 5
{"front","door"}..{"rear","door"}   // all cells from column index front to
                                    // rear and row index door
{2,3}..{*,*}                        // all columns starting with column 2,
                                    // row 3 to the highest valid cell
```

**Note**

Specifying the range of cells has different effects on SimTalk instructions, depending on whether *Column Index Belongs to Contents* is activated or not.

#### Column Index Belongs to Contents

When *Column Index Belongs to Contents* is active, this instruction deletes the entire contents of `ColumnB`, including the column index:

```simtalk
DataTableColumnIndexContents.delete({"ColumnB", *})
```

#### Column Index Does Not Belong to Contents

When *Column Index Belongs to Contents* is NOT active, this instruction deletes the contents of `ColumnB`, excluding the column index:

```simtalk
DataTableColumnIndexNotContents.delete({"ColumnB", *})
```

To delete the entire contents of `ColumnB`, including the column index, enter this instruction:

```simtalk
DataTableColumnIndexNotContents.delete({"ColumnB", 0}..{"ColumnB", *})
```

### Address a User-defined Index [several columns]

To address a user-defined index of data type `integer`, add the number sign/hash `#` in front of the identifier.

The system index (the numbers of rows and columns Plant Simulation assigns) also has the data type `integer`. Without the number sign, Plant Simulation would not be able to distinguish whether to use the system index or the user-defined index.

**Note**: To denote range statements, type the curly braces `{ }`.

**Example**

```simtalk
{2,5}   // system index
{#2,#7} // user-defined index
```

If the range consists of two index specifications, Plant Simulation interprets the specified cells as opposing corner points of a rectangular range (as when selecting the range with the mouse).

---

## Related SimTalk Methods

`calculateList`, `copyRangeTo`, `delete` (lists), `determineRange` (DataTable), `find` (lists), `findAttr`, `findCeil`, `findFloor`, `initialize`, `max` (lists), `maxAttr`, `meanValue`, `meanValueAttr`, `min` (lists), `minAttr`, `setAlignmentCells`, `setEditorRightsCells`, `setFormula`, `standardDeviation`, `standardDeviationAttr`, `sum` (lists), `sumAttr`.

## See Also

- Activate Column Index
- Activate Row Index
- Create a User-defined Column and Row Index
- Specify the Identifier of a Cell
- Specifying a Range of Cells
- Address a User-defined Index
