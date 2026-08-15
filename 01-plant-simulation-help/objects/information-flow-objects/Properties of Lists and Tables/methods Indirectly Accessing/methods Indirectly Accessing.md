# Methods for Indirectly Accessing Lists and Tables

Lists and tables provide the methods listed in the table of contents to the left for indirectly accessing them.

These methods only apply to ranges of data type **object**. The contents of the cells are references to objects whose attributes are to be processed.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object **Station**.

You can:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the attributes and methods of the selected Instance [general description].

---

## asObject [SimTalk]

Returns the contents of a cell of data type string or object of the list/table designated by `<Path>` if the cell contains a valid path to an object.

### Remarks

The method applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

### Type

Method

### Syntax

```
<Path>.asObject(Column:any, Row:any) → any
```

### Parameters

You can specify the following parameters:

- The parameter **Column** of data type `any` designates the column of the table.
- The parameter **Row** of data type `any` designates the row.

### Return Value

The return value has the data type `any`.

### Note

The return value is the lane of the **TwoLaneTrack** if the table cell, which `asString` returned, contains a valid path to a lane of a TwoLaneTrack. This returned value does not have the data type object and thus cannot be assigned to a variable of data type object. You can, however, assign it to a local variable of data type `any`.

If a table cell of data type object contains a path to a lane, reading the contents of the cell with brackets (`table[x,y]`) returns **VOID** as a lane does not have the data type object.

### Example

```
var a : any
if .MUs.Transporter:1.getRoute(DataTable) 
a := MyDataTable.asObject(1,1)
if isObject(a) 
print "first object: ", a.name
else
print "first object is a two-lane track: ", a.~.name
end
print "the length is: ", a.length
```

---

## asString [SimTalk] - DataTable

Returns the designated cell of the DataTable designated by `<Path>` as a string.

### Remarks

This is especially handy if the cell of data type object contains a path for which Plant Simulation would return the contents either as an object or as **VOID**.

The method applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

### Type

Method

### Syntax

```
<Path>.asString(Column:any, Row:any) → string
```

### Parameters

You can specify the following parameters:

- The parameter **Column** of data type `any` designates the column of the table.
- The parameter **Row** of data type `any` designates its row.

### Return Value

The return value has the data type `string`.

### Example

```
MyDataTable[1,2] := "Station" // writes an absolute path
MyDataTable.asString(1,2)     // reads a relative path
```

### See also

asObject [SimTalk]

---

## findAttr [SimTalk]

Searches for an object which contains the attribute with the passed name and passed attribute value in the List/Table designated by `<Path>`.

### Remarks

The method `findAttr` only searches in columns of data type object, i.e. it ignores columns with other data types. The method finds built-in attributes as well as user-defined attributes. If you just want to search for an object, which has this attribute, independent of the attribute value, then enter **VOID** as the value to be searched for.

`findAttr` starts its search at the position of the internal pointer of the List/Table. If `findAttr` finds such an object, then the method sets the internal pointer to the respective cell and returns `true`. If `findAttr` does not find such an object starting at the position of the internal pointer, it returns `false`.

The method applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

### Type

Method

### Syntax

```
<Path>.findAttr([Range:listrange, ]AttributeName:string, Value:any) → 
boolean
```

### Parameters

You can specify the following parameters:

- The optional parameter **Range** of data type `listrange` designates the range which you would like to search. If you do not specify this parameter, Plant Simulation searches the entire Table. You can also specify several list ranges, all of which the method then searches.
- The parameter **AttributeName** of data type `string` designates the name of the attribute to be searched for.
- The parameter **Value** of data type `any` designates the value of the attribute for which you are searching. If Plant Simulation finds this value, it terminates the search. If you enter **VOID** as value, the search ends if an attribute with the name of the parameter **AttributeName** is found. `findAttr` sets the internal pointer to the entry of the object and returns `true`. If the value does not match, `findAttr` continues searching. If it does not find a matching entry, it returns `false`.

### Note

The search for attribute names and attribute values is not case-sensitive.

Depending on whether **Column Index Belongs to Contents** is active or not, the range has different effects on the method `findAttr` of the DataTable.

- If the DataTable has a column index and the column index belongs to the contents, the method relates to the entire contents of the DataTable, including the column index. See Column Index Belongs to Contents.
- If the DataTable has a column index and the column index does not belong to the contents, the method only relates to the contents of the DataTable, excluding the column index. See Column Index Does Not Belong to Contents.

### Return Value

The return value has the data type `boolean`.

### Example

```
var wanted: object,
var row,column: integer 
MyDataList.Cursor := 1
if MyDataList.findAttr("color", "red") 
   wanted := MyDataList.read(MyDataList.Cursor)
end
MyDataTable.CursorX := 1 MyDataTable.CursorY := 1
if MyDataTable.findAttr({1,1}..{4,4},"order",VOID) 
   column := MyDataTable.CursorX 
   row := MyDataTable.CursorY print table[column,row].order
end
```

### See also

- CursorX [SimTalk]
- CursorY [SimTalk]
- Cursor [SimTalk]
- Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
- Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## maxAttr [SimTalk]

Returns the maximum of the designated attribute of all objects in the list/table designated by `<Path>` to the designated value.

### Remarks

In addition, Plant Simulation sets the file cursor into the cell in which the object with the maximum attribute value is located.

The method applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

### Type

Method

### Syntax

```
<Path>.maxAttr(Range:listrange, ..., AttributeName:string) → real
```

### Parameters

You can specify the following parameters:

- The parameters **Range** of data type `listrange` designate the range of the list.
- The parameter **AttributeName** of data type `string` designates the name of the attribute.

### Return Value

The return value has the data type of the designated list range if this list range has a uniform data type. If the data type is not uniform, the return values are converted to the data type `real` and the method returns the data type `real`.

### Example

```
// search all entries within the specified range on the table and determine
// the maximum of the user-defined attribute Time
MyDataTable.setCursor(1,1)
print MyDataTable.maxAttr({1,2}..{3,5},"time")
```

### See also

- minAttr [SimTalk]
- Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
- Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## meanValueAttr [SimTalk]

Returns the mean value of the designated attribute of all objects within the designated range of the list/table designated by `<Path>`.

### Remarks

The method applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

### Type

Method

### Syntax

```
<Path>.meanValueAttr(Range:listrange, ... AttributeName:string) → real
```

### Parameters

You can specify the following parameters:

- The parameters **Range** of data type `listrange` designate the range of the list.
- The parameter **AttributeName** of data type `string` designates the name of the attribute.

### Return Value

The return value has the data type `real`.

### Example

```
MyDataStack.Cursor := 1
print MyDataStack.meanValueAttr({3}..{*},"SetupTime")
```

### See also

Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## minAttr [SimTalk]

Returns the minimum of the designated attribute of all objects in the list/table designated by `<Path>` to the designated value.

### Remarks

Plant Simulation sets the file cursor into the cell in which the object with the minimum attribute value is located.

The method applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

### Type

Method

### Syntax

```
<Path>.minAttr(Range:listrange, ... AttributeName:string) → real
```

### Parameters

You can specify the following parameters:

- The parameters **Range** of data type `listrange` designate the range of the list.
- The parameter **AttributeName** of data type `string` designates the name of the attribute.

### Return Value

The return value has the data type of the designated list range if this list range has a uniform data type. If the data type is not uniform, the return values are converted to the data type `real` and the method returns the data type `real`.

### Example

```
// cycle through all cells in the lixg, query their processing time 
// and return the minimum of the processing times as result 
MyDataList.Cursor := 1
print MyDataList.minAttr({*},"ProcTime")
table.setCursor(1,1)
print MyDataTable.minAttr({1,2}..{3,5},"time")
```

### See also

- maxAttr [SimTalk]
- Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
- Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## standardDeviationAttr [SimTalk]

Returns the standard deviation of the designated attribute of all objects in the designated range of the list/table designated by `<Path>`.

### Remarks

The method applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

### Type

Method

### Syntax

```
<Path>.standardDeviationAttr(Range:listrange, ... AttributeName:string) → 
real
```

### Parameters

You can specify the following parameters:

- The parameters **Range** of data type `listrange` designate the range of the list.
- The parameter **AttributeName** of data type `string` designates the name of the attribute.

### Return Value

The return value has the data type `real`.

### Example

```
MyDataList.Cursor := 1
print MyDataList.standardDeviationAttr({*},"ProcTime")
```

### See also

Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## sumAttr [SimTalk]

Returns the sum of the designated attributes of all objects in the designated range of the list/table designated by `<Path>`.

### Remarks

The method applies to the objects **DataStack**, **DataQueue**, **DataList**, **DataTable**, and **TimeSequence**.

### Type

Method

### Syntax

```
<Path>.sumAttr(Range:listrange, ... AttributeName:string) → real
```

### Parameters

You can specify the following parameters:

- The parameters **Range** of data type `listrange` designate the range of the list.
- The parameter **AttributeName** of data type `string` designates the name of the attribute.

### Return Value

The return value has the data type of the designated list range if this list range has a uniform data type. If the data type is not uniform, the return values are converted to the data type `real` and the method returns the data type `real`.

### Example

```
// cycle through all cells in the DataQueue, sum up the processing times 
// and return the sum as the result
MyDataQueue.Cursor := 1
print MyDataQueue.sumAttr({1}..{5},"ProcTime")
```

### See also

Specifying a Range of Cells [several columns] > Column Index Belongs to Contents
Specifying a Range of Cells [several columns] > Column Index Does Not Belong to Contents

---

## Read-only Attributes and Attributes of Cells

Cells in lists and tables provide the read-only attribute **Void [SimTalk] - cells of lists/tables** and the attribute **Name [SimTalk] - cells**.

Read and write access depend on the object class and are described in the sub-chapters.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object **Station**.

You can:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the attributes and methods of the selected Instance [general description].
