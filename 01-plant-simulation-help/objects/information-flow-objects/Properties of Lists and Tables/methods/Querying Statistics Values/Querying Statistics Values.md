# Methods for Querying Statistics Values of Lists and Tables

Lists and tables provide the methods listed here for querying statistics values.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

You can:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the attributes and methods of the selected Instance.

---

## max [SimTalk] - lists

Returns the greatest value in the range of cells of the list or table designated by `<Path>`.

**Remarks**

- After it found the greatest value, the method sets the cursor into the cell in which it found the value.
- The method only applies to entries of data types `real` or `integer`. Plant Simulation ignores entries of other data types in the ranges to be searched or considers their value to be 0.
- The method applies to the objects `DataStack`, `DataQueue`, `DataList`, `DataTable`, and `TimeSequence`.

**Type**

Method

**Syntax**

```
<Path>.max([Range:listrange, ...]) -> real
```

**Parameter**

The parameters `Range` of data type `listrange` designate the range of cells.

`max` treats the boolean value `true` like `1.0` and the boolean value `false` like `0.0`.

**Return Value**

The return value has the data type of the designated list range if this list range has a uniform data type. If the data type is not uniform, the return values are converted to the data type `real` and the method returns the data type `real`.

**Example**

```SimTalk
print MyDataStack.max({*})
print MyDataQueue.max({1}..{*})
print MyDataList.max({*})
print MyDataTable.max({3,3}..{3,*}) // maximum number of entries
```

**See also**

- CursorX [SimTalk]
- CursorY [SimTalk]
- Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
- Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## meanValue [SimTalk]

Returns the arithmetic mean of all values in a range of cells of the list or table designated by `<Path>`.

**Remarks**

- The method only applies to entries of data types `real` or `integer`. Plant Simulation ignores entries of other data types in the ranges to be searched or considers their value to be 0.
- The method applies to the objects `DataStack`, `DataQueue`, `DataList`, `DataTable`, and `TimeSequence`.

**Type**

Method

**Syntax**

```
<Path>.meanValue([Range:listrange, ...]) -> real/integer
```

**Parameter**

The parameters `Range` of data type `listrange` designate the range of cells.

`meanValue` treats the boolean value `true` like `1.0` and the boolean value `false` like `0.0`.

**Return Value**

The return value has the data type `real` or `integer`.

**Example**

```SimTalk
print MyDataStack.meanValue({*})
print MyDataQueue.meanValue({1}..{*})
print MyDataList.meanValue({*})
print MyDataTable.meanValue({3,3}..{3,*})
```

**See also**

- Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
- Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## min [SimTalk] - lists

Returns the smallest value in a range of cells of the list or table designated by `<Path>`.

**Remarks**

- When the method finds the smallest value, it sets the cursor to the cell in which it found the value.
- The method only applies to entries of data types `real` or `integer`. Plant Simulation ignores entries of other data types in the ranges to be searched or considers their value to be 0.
- The method applies to the objects `DataStack`, `DataQueue`, `DataList`, `DataTable`, and `TimeSequence`.

**Type**

Method

**Syntax**

```
<Path>.min([Range:listrange, ...]) -> real
```

**Parameter**

The parameters `Range` of data type `listrange` designate the range of cells.

`min` treats the boolean value `true` like `1.0` and the boolean value `false` like `0.0`.

**Return Value**

The return value has the data type of the designated list range if this list range has a uniform data type. If the data type is not uniform, the return values are converted to the data type `real` and the method returns the data type `real`.

**Example**

```SimTalk
print MyDataStack.min({*})
print MyDataQueue.min({1}..{*})
print MyDataList.min({3}..{*})
print MyDataTable.min({3,3}..{3,*}) // minimum number of entries
```

**See also**

- CursorX [SimTalk]
- CursorY [SimTalk]
- Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
- Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## standardDeviation [SimTalk]

Returns the standard deviation from the mean of all values in a range of cells of the list or table designated by `<Path>`.

**Remarks**

- The method only applies to entries of data types `real` or `integer`. Plant Simulation ignores entries of other data types in the ranges to be searched or considers their value to be 0.
- The method applies to the objects `DataStack`, `DataQueue`, `DataList`, `DataTable`, and `TimeSequence`.

**Type**

Method

**Syntax**

```
<Path>.standardDeviation([Range:listrange, ...]) -> real/integer
```

**Parameter**

The parameters `Range` of data type `listrange` designate the range of cells.

`standardDeviation` treats the boolean value `true` like `1.0` and the boolean value `false` like `0.0`.

**Return Value**

The return value has the data type `real` or `integer`.

**Example**

```SimTalk
print MyDataStack.standardDeviation({*})
print MyDataQueue.standardDeviation({1}..{*})
print MyDataList.standardDeviation({*})
print MyDataTable.standardDeviation({3,3}..{3,*})
```

**See also**

- Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
- Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## sum [SimTalk] - lists

Returns the sum of all values in a range of cells of the list or table designated by `<Path>`.

**Remarks**

- The method only applies to entries of data types `real` or `integer`. Plant Simulation ignores entries of other data types in the ranges to be searched or considers their value to be 0.
- The method applies to the objects `DataStack`, `DataQueue`, `DataList`, `DataTable`, and `TimeSequence`.

**Type**

Method

**Syntax**

```
<Path>.sum([Range:listrange, ...]) -> real/integer
```

**Parameter**

The optional parameter `Range` of data type `listrange` designates the range of cells. If you do not specify the parameter, the sum is calculated over all cells.

`sum` treats the boolean value `true` like `1.0` and the boolean value `false` like `0.0`.

**Return Value**

The return value has the data type of the designated list range if this list range has a uniform data type. If the data type is not uniform, the return values are converted to the data type `real` and the method returns the data type `real`.

**Example**

```SimTalk
print MyDataStack.sum({*})
print MyDataQueue.sum({1}..{*})
print MyDataList.sum({*})
print MyDataTable.sum({3,3}..{3,*})
```

**See also**

- Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
- Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents
