# Primitive & Structured Data Types

## Overview

This reference covers the primitive and structured data types in SimTalk, including their value ranges, units, and available methods/attributes.

Example of a SimTalk function using parameters, local variables, and a result list:

```
// returns a list that contains the value added tax amount
// added to the prices of the price list that was passed
param pricelist: queue, VAT: real -> list[real]
var i: integer                 // loop index
result.create                  // instantiates the results list
i := 1
while not pricelist.empty loop // stop condition
   result[i] := pricelist.pop * (1 + VAT)
   i := i + 1                  // increases the index
end                            // end of function
```

---

## Data Types [SimTalk]

Each local variable in SimTalk has a data type that defines its range of values and the permitted operations.

SimTalk provides these data types:

- Acceleration, Any, Array, Boolean, Date, DateTime, Integer, JSON, Length, List, Method, Object, Queue, Real, Speed, Stack, String, Table, Time, Weight

All of the above data types are also keywords in SimTalk. You cannot use them to name an object, a local variable, or a function.

---

## Money [SimTalk]

Plant Simulation only supports the data type `money` for global variables, user-defined attributes, and for lists and tables. **Money is not a SimTalk data type.** For local variables use the data type `real` instead.

## RandTime [SimTalk]

The global Variable and user-defined attributes provide the data type `randtime`. Use it to generate random numbers of data type `time` using a random number stream of its own.

> Example: To make random numbers for Set-up Time independent of those for Processing Time, create a user-defined attribute of data type `randtime`, set the distribution type of Set-up time to Formula, and type `self.<UserDefinedAttribute>.rollDice`.

RandTime is **not** a SimTalk data type. When getting a `randtime` value, Plant Simulation returns a value of data type `time`.

## Path [signature]

The window Show Attributes and Methods shows the signature `path` for some objects in the column Signature. Path is **not** a data type that you can assign. If a built-in attribute is listed with data type `path`, you can assign a value of data type `object` or `string` to it.

---

## Acceleration [SimTalk] — data type

A local variable of data type `acceleration` has a maximum range of values between `-8.9e307 ≤ acceleration ≤ 8.9e307`.

**Remarks**
- Applies to the objects Conveyor and Transporter.
- When assigning, Plant Simulation interprets the value as meters per second squared (m/s²).
- When outputting, Plant Simulation converts the value to the unit selected under *File > Model Settings/Preferences > Units > Acceleration*.

**Note** (SimTalk 2.0): you can specify the acceleration units `mps²`, `cm²`, `fps²`, and `LU/s²`. Type the unit directly after the value, without a separating blank space.

```
var a : acceleration := 10mps²  // 10 meters per second squared
var b : acceleration := 2.5fps² // 2.5 feet per second squared
```

> The data types `time`, `length`, `weight`, `speed`, and `acceleration` are not compatible! You can, for example, only assign a value of data type `length`, `real`, or `integer` to a variable of data type `length`.

---

## Any [SimTalk] — data type

A local variable of data type `any` can take any value.

**Remarks**
- The data type of the variable assumes the data type of the first assigned value. If you then assign an incompatible value, Plant Simulation shows an error.
- Use the `forget` statement to reset the assumed data type.

**Referencing a Python object**: now Plant Simulation returns the Python object as a value of data type `any` (previously converted to SimTalk types/string). Python lists are returned as `any` (previously converted to arrays), preventing unnecessary memory allocation for large lists.

**Return Value** — `boolean`

Query the data type of a variable of data type `any` with functions such as:
`getSimTalkTypename`, `isLength`, `isAcceleration`, `isBoolean`, `isDate`, `isDatetime`, `isInteger`, `isJson`, `isList`, `isListRange`, `isObject`, `isQueue`, `isReal`, `isSpeed`, `isString`, `isTable`, `isTime`, `isWeight`, `typeStatisticsCumulated`.

```
a := 3.14   -- data type real is assumed
forget a    -- now we can assign a new data type
a := "Test" -- data type string is assumed
```

```
param arg: any // declaring the method named myPrint
if isLength(arg)
   print "length = ", arg
end

// calling the method myPrint
myPrint(1)
myPrint("any text")
myPrint(MyConveyor.length)
```

```
var a : any
a := MyConveyor.acceleration
print a," ",getUnit(a)
print isAcceleration(a)
```

**Note** — The value `VOID` does not have a data type (object, table, and list can all take `void`). A local variable of data type `any` does not take a data type when you assign `void`. `isObject` returns `false` in this case.

```
var a: any := void
print isObject(a)   // prints false
print a = void      // prints true
var b : any := 123
print b = void      // prints false
```

You can also use `getSimTalkTypename` (returns `string`) to get the data type of an `any` variable.

```
param a : any
switch getSimTalkTypename(a)
case "integer"
   print "integer argument"
case "string"
   print "string argument"
end
```

---

## Array [SimTalk] — data type

A local variable of data type `array` designates a one-dimensional or two-dimensional value field of one of the base data types.

**Base data types** can be all data types **except** `table`, `list`, `stack`, and `queue`. If you use `any` as the base data type, each item can have a different data type, and even lists and tables can be placed in the array.

- Array indexes are one-based (start with 1, not 0).
- Declaration forms:
  - `a : integer[10]` — one-dimensional array of fixed size 10.
  - `b : boolean[10,20]` — two-dimensional array of fixed size.
  - `a : string[]` — one-dimensional array, size not fixed, initially empty.

```
var vector3  : real[3]               // one-dimensional array with 3 real values
var matrix3x3 : real[3,3]            // two-dimensional array with 9 real values
var objList : object[]               // one-dimensional array with n objects (size can change)
var a        : any[]                 // one dimensional array with n values of any data type
print vector3[2]                     // prints 0 to the console
vector3 := [1.0, 2.0, 3.0]           // fills a one-dimensional array
print vector3[2]                     // prints 2 to the console
// For filling a two-dimensional array you might type:
for var x := 1 to matrix3x3.xDim
   for var y := 1 to matrix3x3.yDim
      matrix3x3[x,y] := x + y
next
next
print matrix3x3         // prints [2, 3, 4][3, 4, 5][4, 5, 6]
print objList.dim       // prints 0 to the console
objList.append(Station) // adds Station to the array
print objList.dim       // prints 1 to the console
print objList[1]        // prints the path to the Station on the console
a := vector3
a.append("Hello World")
print a.dim             // prints 4 in the console
print a                 // prints [1, 2, 3, Hello World] to the console
```

Empty arrays display with a space between brackets `"[ ]"`:

```
var a : real[]
var s : string := to_str(a)  // s := "[ ]"
```

Nested array example:

```
-- array of two arrays
-- detect the datatype by the method isArray
var a:any[] := [[current, pi, exp(1)], [Eventcontroller, 42]]
print "a = ",a
print  "a[1] = ",a[1]
print  "a[2] = ",a[2]
-- datatype array
print isArray(a[1])
print isArray(a)
```

### Add and Subtract Arrays of Numerical Data Types

You can add and subtract arrays of numerical data types (`integer`, `real`, `length`, `weight`, `speed`, `acceleration`, `time`) whose dimensions match.

In addition, you can multiply arrays of a floating point data type (`real`, `length`, `weight`, `speed`, `acceleration`, `time`) with a numerical value (`integer`, `real`) or divide them by a numerical value. Matrix multiplication is also supported for floating point arrays.

### Compare Arrays of Different Data Types

Plant Simulation throws a runtime error and opens the Method Debugger in these cases:
- Arrays of data type `real`, `length`, `time`, `speed`, `weight` based on their content.
- Arrays of data type `any` compared to other arrays based on their content.

> Arrays of data type `integer` cannot be compared with arrays of data type `real`, `length`, `time`, `speed`, or `weight`.

```
-- array with different data types
var a:any[4]
a := [current, pi, -42, [1, 2, 3]]
print "a = ",a
print "a[1]: ", getSimTalkTypename(a[1])
a[1] := "Hello" -- change the data type
print "a[1]: ", getSimTalkTypename(a[1])
```

```
-- create, assign, compare arrays
var a:integer[3]
a[1] := 5
a[2] := 2
a[3] := 7
print "a = ",a
var b:integer[3]
print "b = ",b
b := a
print "b = ",b
print"a = b ", a=b
b.sort
print "b = ",b
print "a = b ", a=b
```

### Methods and Attributes of Arrays

Array data types provide these methods and attributes:

`append`, `appendArray`, `appendValueOfType`, `asAny`, `contains`, `copyFromTable`, `copyFromTableColumn`, `copyToTable`, `copyToTableColumn`, `delete`, `deleteValue`, `Dim`, `Empty`, `find`, `getValueOfType`, `insert`, `join`, `Magnitude`, `makeRGBValue`, `max`, `min`, `normalize`, `pop`, `sort`, `sum`, `X`, `xDim`, `Y`, `yDim`.

#### append — array

Appends a value to the end of a one-dimensional array that does not have a fixed size.

Syntax: `<array>.append(Value:any)`

```
var a: string[]
a.append("string")
a.append("string")
print a[2]
```

#### appendArray

Appends all elements of the passed array to the array. Data types must match; only applies to one-dimensional arrays without a fixed size.

Syntax: `<array>.appendArray(ArrayToBeAppended:array)`

```
var a : integer[]  := [1, 2, 3]
var b : integer[2] := [4, 5]
a.appendArray(b)
print a  // outputs [1, 2, 3, 4, 5]
```

#### appendValueOfType

Converts the passed value to a byte sequence and appends these bytes at the end of an `integer` array. Useful for sending binary data with the `Socket` object.

Syntax: `<array>.appendValueOfType(Value:any, Type:string)`

- Allowed `Type` values: `"int8"`, `"int16"`, `"int32"`, `"int64"`, `"uint8"`, `"uint16"`, `"uint32"`, `"uint64"`, `"real32"`, `"real64"` (and capitalized variants).
- Lower-case first letter → little-endian; upper-case first letter → big-endian.

```
var a : integer[]
a.appendValueOfType(123456, "int32")  // append 4 bytes
a.appendValueOfType(-3000, "int16")   // append 2 bytes
var x := a.getValueOfType(1, "int32") // read 4 bytes
var y := a.getValueOfType(5, "int16") // read 2 bytes
```

#### asAny

Returns a reference to the addressed array element (for `string`/`object` arrays) if its value is a relative/absolute path to an existing object, lane, storage place, or user-defined attribute of type `table`, `list`, `stack`, or `queue`.

Syntax: `<array>.asAny(Index:integer[, YIndex:integer]) → any`

Return value types:
- `object` — if element contains a reference/path to an existing Frame object.
- `any` — if element contains path to a lane or storage place.
- `table`/`list`/`stack`/`queue` — for paths to user-defined attributes of those types.
- `VOID` — if value does not contain a path to a valid object.

```
var a : object[2];
a[1] := "TwoLaneTrack.A"
a[2] := "Station.MyTableAttr"
var obj0 := a[1]        // obj0 is VOID, as not of type 'object'
var obj1 := a.asAny(1)  // obj1 is .Models.Model.TwoLaneTrack.A of type 'any'
var obj2 := a.asAny(2)  // obj2 is .Models.Model.Station.MeinTabellenAttr of type 'table'
```

#### contains — array

Returns whether the specified value is contained in a one-dimensional array.

Syntax: `<array>.contains(Value:any) → boolean`

```
var a : string[] := ["hello", "world"]
if a.contains("world")
   print "this code is always reached"
end
if a.contains("hell")
   print "this code is never reached"
end
param color : string := "yellow"
if ["red","green","blue"].contains(color)
  print "color is red or green or blue"
end
```

#### copyFromList

Copies a `list` into the array.

Syntax: `<array>.copyFromList(Source:list) -> void`

```
targetArray.copyFromList(MyList)
```

#### copyFromTable

Copies a `table` (or range) into the array. If the array has a fixed size, dimensions must match.

Syntax: `<array>.copyFromTable([SourceRange:listrange,] SourceTable:table)`

```
targetArray.copyFromTable(MyDataTable)
```

#### copyFromTableColumn

Copies a table column into a one-dimensional array.

Syntax: `<array>.copyFromTableColumn(SourceTable:table, Column:integer)`

```
var array: string[]
array.copyFromTableColumn(DataTable, 3)
```

#### copyToList

Copies the array into a list.

Syntax: `<array>.copyToList(Target:list) -> void`

```
arrayVar.copyToList(MyList)
```

#### copyToTable

Copies the array into a table.

Syntax: `<array>.copyToTable(TargetTable:table[, Column:integer, Row:integer])`

```
arrayVar.copyToTable(MyDataTable,2,9)
```

#### copyToTableColumn — array

Copies a one-dimensional array into a specified table column.

Syntax: `<array>.copyToTableColumn(TargetTable:table, Column:integer)`

```
var array: string[2] := ["hello", "world"]
array.copyToTableColumn(DataTable, 3)
```

#### delete — array

Deletes the contents of the array, or (with `Index`) the item at that position (size shrinks by 1).

Syntax: `<array>.delete([Index:integer])`

```
a := [current,pi,e]
a.delete(2)
print a.dim
```

#### deleteValue

Deletes the first occurrence of the specified value from a one-dimensional array. Returns `true` if found, `false` otherwise.

Syntax: `<array>.deleteValue(Value:any) → boolean`

```
a: string[] := ["Alice", "Bob", "Charlie"]
a.deleteValue("Bob")
print a
// prints ["Alice", "Charlie"]
```

#### Dim — array

Returns the dimension of a one-dimensional array (read-only attribute, `integer`).

Syntax: `<array>.Dim`

```
var a:real[3]
print a.Dim // prints 3
```

#### Empty — array

Returns if the array is empty (`true`) or contains items (`false`). Only applies to one-dimensional arrays.

Syntax: `<array>.Empty → boolean`

```
var a : integer[]
if a.empty
a.append(42)
end
if not a.empty
print a[1]
end
```

#### find — array

Searches for a value in a one-dimensional array; returns the position, or `0` if not found.

Syntax: `<array>.find(Value:any[, StartIndex:integer])`

```
var a:real[5] := [1.1, 2.2, 3.3, 4.4, 5.5]
print a.find(3.3)     // prints 3
print a.find(3.3, 4)  // prints 0, that is, not found
```

#### getValueOfType

Reads a byte sequence from an `integer` array and converts it to a value. Useful for receiving binary data with the `Socket` object.

Syntax: `<array>.getValueOfType(Index:integer, Type:string) -> any`

- Allowed `Type` values include `"int8"` … `"real64"`, plus `"bool"` (and capitalized variants).

```
var a : integer[]
a.appendValueOfType(123456, "int32")  // append 4 bytes
a.appendValueOfType(-3000, "int16")   // append 2 bytes
var x := a.getValueOfType(1, "int32") // read 4 bytes
var y := a.getValueOfType(5, "int16") // read 2 bytes
```

#### insert — array

Inserts a value into a one-dimensional array that does not have a fixed size.

Syntax: `<array>.insert(Index:integer, Value:any)`

```
var a: real[] := [1.1, 2.2, 3.3, 4.4, 5.5]
a.insert(3,-11)
print a // returns [1.1, 2.2, -11, 3.3, 4.4, 5.5]
```

#### join

Converts the array elements into a single string separated by the separator string.

Syntax: `<array>.join(separator:string) → string`

```
var a:integer[]
a.append(1)
a.append(2)
a.append(3)
print a.join(" * ") // 1 * 2 * 3
```

#### Magnitude

Returns the magnitude/length of a numerical one-dimensional array (vector). Read-only attribute, `real`.

Syntax: `<array>.Magnitude → real`

```
var direction: real[3] := [2.0, 3.5, 2.8]
print direction.Magnitude
```

#### max — array

Returns the greatest value in a one-dimensional array of numerical or string type. Empty number array → `0`; empty string array → `""`.

Syntax: `<array>.max`

Unit rules: `max(time, time) -> time`, `max(length, length) -> length`, `max(length, speed) -> real`, etc.

```
var a:real[5] := [1.1, 2.2, 3.3, 4.4, 5.5]
print a.max // prints 5.5
var arrPartPos: length[]
arrPartPos := [6300mm, 5600mm]
var maxPartPos: length := arrPartPos.max
print arrPartPos.max
```

#### min — array

Returns the smallest value in a one-dimensional numerical/string array.

Syntax: `<array>.min`

```
var a:real[5] := [1.1, 2.2, 3.3, 4.4, 5.5]
print a.min // prints 1.1
var arrPartPos:length[]
arrPartPos := [6300mm, 5600mm]
print arrPartPos.min
```

#### normalize

Normalizes a numerical one-dimensional array (its Magnitude becomes 1). Returns the old magnitude (`real`).

Syntax: `<array>.normalize → real`

```
var v:real[3]
v := [2,3,4]
print v.normalize
print v
// prints 5.3851648071345
[0.371390676354104, 0.557086014531156, 0.742781352708207]
```

#### pop — array

Removes the last element from the array and returns it.

Syntax: `<array>.pop → any`

```
var a:integer[]
a.append(1)
a.append(2)
a.append(3)
print a.pop // 3
```

#### sort — array

Sorts the array. For two-dimensional arrays, rows are sorted by the first column. Sorting is case-sensitive.

Syntax: `<array>.sort(Descending:boolean:=false)`

```
var a:integer[] := [4, 2, 1, 3]
a.sort(false) // ascending
print a       // returns [1, 2, 3, 4]
var a:integer[] := [4, 2, 1, 3]
a.sort(true) // descending
print a      // returns [4, 3, 2, 1]
```

#### sum — array

Returns the sum of all values in a one-dimensional array.

Syntax: `<array>.sum`

```
var a:real[5] := [1.1, 2.2, 3.3, 4.4, 5.5]
print a.sum // returns 16.5
```

#### X / Y / Z — array

Returns the element at index 1 / 2 / 3 respectively. Applies to one-dimensional arrays of type `integer`, `real`, or `length` with fixed dimension of three (X/Y) or two (X/Y) elements.

Syntax: `<array>.X → integer`

```
var c: real[3] := Station.Coordinate3D
print c.X  // prints c[1]
c.X := 42  // c[1] := 42
```

#### xDim / yDim — array

`xDim` returns the x-dimension of a two-dimensional array; `yDim` returns the y-dimension (returns `0` for a one-dimensional array).

Syntax: `<array>.xDim → integer`, `<array>.yDim → integer`

```
var matrix:real[2,3]
print matrix.xDim // prints 2
print matrix.yDim // prints 3
```

---

## Boolean [SimTalk] — data type

A local variable of data type `boolean` can be `true` or `false`.

## Date [SimTalk] — data type

A local variable of data type `date` designates a date between 01.01.1900 and 31.12.9999.

**Remarks**
- When assigning, convert the date with `str_to_date`.
- Initial value is `0` for numerical types, `false` for boolean, `""` for string, `void` for object/list/table.
- For `date`/`DateTime`, the start value depends on the Plant Simulation version; for models created in 14.0+, it is `01.01.1900`.

## DateTime [SimTalk] — data type

A local variable of data type `dateTime` designates a date and time between `01.01.1900 00:00:00` and `31.12.9999 23:59:59`. Convert with `str_to_dateTime` when assigning.

## Integer [SimTalk] — data type

A local variable of data type `integer` can only contain integer numbers.

Range: `-9.223.372.036.854.775.808 ≤ integer ≤ 9.223.372.036.854.775.807`. Plant Simulation does not check for values outside this range.

---

## JSON [SimTalk] — data type

A local variable of data type `JSON` can hold values in the JSON data format (JavaScript Object Notation).

**Remarks**
- JSON data is structured, nestable data of name-value pairs. Names can contain spaces and special characters and are case-sensitive.
- Values can be: Integer, Real, Boolean, String, Array (in `[]`), JSON (in `{}`), or Void (`null`).

```
var person: json
person["Name"] := "Robert"
person["Age"] := 42
person["Personnel No"] := "007-1234-55"
var person
person["age"] := 30
person["age"] += 1  // Congratulations :-)
```

Address a name-value pair via integer index, selecting `.Name` or `.Value`:

```
var j: json
    j["color"] := "red"
    j["shape"] := "triangle"
    for var i := 1 to j.dim
      print j[i].Name, " ", j[i].Value
    next
```

### JSON Literals

JSON literals are enclosed in curly braces `{ }`, with elements separated by commas. Elements consist of a string literal, a colon, and a JSON value.

JSON values can be: a number, a string literal, `true`/`false`, `void`, or a local variable of type `integer`, `real`, `boolean`, `string`, `object`, `array`, or `json`.

```
var j: json
var jobTitle: string := "Engineer"
var addressArray: string[] := ["Main street 42", "10001 New York"]
j := { "name": "Alice", "age": 42, "female": true,
     "job": jobTitle, "address": addressArray }
```

### Elements of Data Type Object in JSON Variables

JSON variables can accept elements of data type `object` (a Plant Simulation extension not in the JSON standard). When converted to a string, object elements are written as their absolute path.

```
var j: json
j["o"] := MyStation    -- element "o" is of data type object
j["o"].Label := "ABC"  -- assigns a label to the object MyStation
```

```
var json1, json2: json
json1["o"] := MyStation          -- element "o" is of data type object
var s : string := to_str(json1)  -- convert data into a string
json2.parse(s)                   -- element "o" is of data type string
```

### Methods and Attributes of JSON

`asString`, `contains`, `copy`, `copyToTableColumn`, `copyToTableRow`, `delete`, `Dim`, `getOrCreateJSON`, `parse`, `readFile`, `unshareAndDelete`, `writeFile`.

#### asString — JSON

Returns the string representation of the JSON object. `MultiLine` (default `true`) sets line breaks/indentation.

Syntax: `<json>.asString([MultiLine:boolean:=true]) -> string`

```
var j: json
j["Name"] := "Tom"
j["Age"] := 32
var s: string := j.asString(false)
```

#### contains — JSON

Returns if the JSON object contains a name-value-pair with the passed name.

Syntax: `<json>.contains(Name:string) -> boolean`

```
var j: json
j["Body color"] := "blue"
if a.contains("Body color")
   print "This code will always be reached."
end
```

#### copy — JSON

Returns a copy of the JSON object (deep copy; assignment alone shares the reference).

Syntax: `<json>.copy -> json`

```
var Person1, Person2: json
Person2 := Person1          -- Person1 and Person2 reference the same JSON object
Person2["Name"] := "Alice"  -- also changes Person1["Name"]
print Person1["Name"]       -- returns Alice
Person2 := Person1.copy     -- Person1 and Person2 now are different JSON objects
Person2["Name"] := "Bob"    -- does not change Person1["Name"]
print Person1["Name"]       -- returns Alice
var Person, Job: json
Job["Description"] := "engineer"
Person["Job"] := Job.copy    -- inserts a copy of Job in Person
Job["Company"] := "Siemens"  -- does not change Person["Job"]
```

#### copyToTableColumn — JSON

Copies the contents of a json array into a specified table column.

Syntax: `<json array>.copyToTableColumn(TargetTable:table, Column:integer)`

```
var j:json
j["a"] := ["hello", "world", 42]
j["a"].copyToTableColumn(DataTable, 2)
-- copies the three array elements into the first
-- three cells of the second column of the table
```

#### copyToTableRow — JSON

Copies the contents of a json array into a specified table row.

Syntax: `<json array>.copyToTableRow(TargetTable:table, Row:integer)`

```
var j:json
j["a"] := ["hello", "world", 42]
j["a"].copyToTableRow(DataTable, 2)
-- copies the three array elements into the first
-- three cells of the second row of the table
```

#### delete — JSON

Without parameter: deletes the entire JSON contents. With parameter: deletes the specified name-value pair. Returns `true` if the name existed.

Syntax: `<json>.delete([Name:string]) -> boolean`

```
var person: json
person["Name"] := "Jason"
if person.delete("name")
   print "This code will never be reached."
elseif person.delete("Name")
   print "This code will always be reached."
end
```

#### Dim — JSON

Returns the number of name-value-pairs. Read-only attribute, `integer`.

Syntax: `<json>.Dim -> integer`

```
param s: string
var j: json
j.parse(s)
if j.Dim = 0
   print "No data available."
end
```

#### getOrCreateJSON

Returns a reference to an empty JSON object; creates the name-value-pair (with empty JSON object) if it does not exist. Returns a reference to the contained value if it is already `json` (otherwise error).

Syntax: `<json_Variable>.getOrCreateJSON(Name:string) -> json`

```
-- source code of Method1:
var JsonObj: json
var ColorInfo := JsonObj.getOrCreateJSON("ColorInfo")
-- JSON-subobject named "ColorInfo" will be created and returned
ColorInfo["color"] := "red"
ColorInfo["NumberChangesColor"] += 1
Method2(JsonObj)
-- source code of Method2:
param JsonObj: json
var ColorInfo := JsonObj.getOrCreateJSON("ColorInfo")
-- existing JSON-subobject will be returned
ColorInfo["color"] := "green"
ColorInfo["NumberChangesColor"] += 1
-- the value will be increased to 2
```

#### parse

Parses the passed text and returns the parsed value. If the value is a JSON object, it is also assigned to `<json>`; otherwise `<json>` is set to an empty JSON object.

Syntax: `<json>.parse(Data:string) -> any`

```
var j: json
var value1 := j.parse("{ \"count\": 123 }")
// value1: json = { "count": 123 }
// j     : json = { "count": 123 }
var value2 := j.parse("123")
// value2: integer = 123
// j     : json = {}
var arr := j.parse("[3.141, 100, true]")
// arr   : any[] = [3.141, 100, true]
// j     : json = {}
```

#### readFile — JSON

Imports JSON source code from a text file into the JSON variable.

Syntax: `<json_Variable>.readFile(FileName:string) → void`

```
var js:json

js.readFile("D:\json.txt")
print js
```

#### unshareAndDelete

Unshares the reference to the JSON object and assigns an empty JSON object.

Syntax: `<json>.unshareAndDelete`

```
var person1, person2 : json
person2 := person1          -- person1 and person2 reference the same JSON object
person2["Name"] := "Alice"  -- also changes person1["Name"]
person2.unshareAndDelete    -- person2 is an empty JSON object
person2["Name"] := "Bob"    -- only changes person2["Bob"]
```

#### writeFile — JSON

Writes the JSON source code to a text file.

Syntax: `<json_Variable>.writeFile(FileName:string) → void`

```
-- our text file JSON.txt contains this JSON source code:
{
  "first_name": "John",
  "last_name": "Doe",
  "age": 46,
  "address": {
    "street_address": "42 42nd Street",
    "city": "New York",
    "state": "NY",
    "postal_code": "10021-3100"
  }
}
```

---

## Length [SimTalk] — data type

A local variable of data type `length` has a maximum range of `-8.9e307 ≤ length ≤ 8.9e307`.

**Remarks**
- When assigning, Plant Simulation interprets the value as meters (m).
- When outputting, it converts to the unit selected under *File > Model Settings/Preferences > Units > Length*.

**Note** (SimTalk 2.0): length units are `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in` (typed directly after the value, no blank space).

```
var len := 1.0ft
var s : speed := 10.5m / 1:30
var x : length := 3m
```

> The data types `time`, `length`, `weight`, `speed`, and `acceleration` are not compatible.

---

## List [SimTalk] — data type

A local variable of data type `list` shares its built-in properties with the object `DataList`.

**Remarks**
- The data type `list` (variables/attributes) is not an object of its own and does not have its own icon; it does not recognize all attributes/methods of `DataList` (e.g., `Location`, `existsIcon`). All read/write methods otherwise apply to both.
- Before first access, create the local variable with `create` or assign a value.

```
var l: list[string]
l.create
l.insert(1,"Hello")
```

## Method [SimTalk] — data type

A local variable of data type `method` is a user-defined attribute of data type `method` (an "attribute method"). It is part of the object and moves with it.

**Remarks**
- Attribute methods have their own random number stream (`RandomSeed`), automatically assigned on insertion.
- If a suspended attribute method's object is deleted, method execution is terminated immediately; the instructions after the `waituntil` will not execute. The return value is the value of `result` at that point (or `VOID`).
- For `Station.MyMethAttr.executeIn(60)`, Plant Simulation calls the user-defined attribute `MyMethAttr`. To execute the method itself, use the reference operator: `Station.&MyMethAttr.executeIn(60)`.

## Object [SimTalk] — data type

A local variable of data type `object` points to an object in the simulation model or is `void`.

**Remarks**
- Can store any graphically represented object (local variable, formal parameter, global variable, table values).
- You can assign both objects and strings.
  - Assigning an object creates an Object Reference; relative paths are resolved immediately.
  - Assigning a string assigns it as a path (not resolved until read, each time).

```
var o1: object := "Station"
var o2: object := ".Models.Model.Station"
var o3: object := .Models.Model.Station
var s1: string := o1  -- "Station"
var s2: string := o2  -- ".Models.Model.Station"
var s3: string := o3  -- "*.Models.Model.Station"
```

> When assigning an object value to a string, an object reference is assigned as its absolute path with a leading asterisk (`*`).

---

## Queue [SimTalk] — data type

A local variable of data type `queue` shares some built-in properties of the object `DataQueue`. Variables/attributes of this type are not objects of their own (no icon, no `Location`/`existsIcon`), but all read/write methods apply.

> Before first access, create with `create` or assign a value.

```
var q: queue[string]
q.create
q.push("Hello")
q.delete
-- deletes the contents from the cell of the queue
```

## Real [SimTalk] — data type

A local variable of data type `real` contains floating point numbers, range `-1.7976931348623158e+308` to `1.7976931348623158e+308`.

**Remarks**
- Precision of 16 places (digits); displayed rounded to 15 places.
- Floating point rounding errors can occur; avoid `=` for comparing floats — use the about-equal operator `~=` instead.
- Numbers can be typed with mantissa/exponent, e.g., `1.0e-3` (0.001).
- Internal representation follows IEEE 754 (53 binary digits of mantissa). Some decimal numbers (e.g., 1.1) cannot be represented exactly.

```
var x: real := 1.1 - 1
-- x has the value 0.1000000000000001
```

## Speed [SimTalk] — data type

A local variable of data type `speed` has a maximum range of `-8.9e307 ≤ speed ≤ 8.9e307`.

**Remarks**
- Interpreted as meters per second (m/s) on assignment; converted to the selected unit on output.
- SimTalk 2.0 units: `mps`, `fps`, `kmh`, `mph` (typed directly after the number).

```
var len := 1.0ft
var s : speed := 10.5m / 1:30
var x : length := 3m
```

## Stack [SimTalk] — data type

A local variable of data type `stack` shares some built-in properties of the object `DataStack`. Variables/attributes are not objects of their own (no icon, no `Location`/`existsIcon`), but read/write methods apply.

> Before first access, create with `create` or assign a value.

```
var s: stack[string]
s.create
s.push("bottles")
-- adds the cell containing the string bottles as the
-- first cell of the variable of data type stack
s.delete
-- deletes the contents from the cell in the stack
```

## String [SimTalk] — data type

A local variable of data type `string` consists of any number of characters enclosed in quotation marks `""`.

```
var st: string := "Hello World! Good day to everybody."
```

## Table [SimTalk] — data type

A local variable of data type `table` shares some built-in properties of the object `DataTable`. Variables/attributes are not objects of their own (no icon, no `Location`/`existsIcon`), but read/write methods apply.

> Before first access, create with `create` or assign a value.

```
var OrderList: table[string,real]
OrderList.create
OrderList[1,1] := "Cans"
OrderList[2,1] := 3000.0
OrderList.delete
var myWaitingTimesTable: table
MyAssembly.statWaitingTimeTable(myWaitingTimesTable)
```

## Time [SimTalk] — data type

A local variable of data type `time` has a maximum range of `-8.9e307 ≤ time ≤ 8.9e307`.

**Remarks**
- Values are interpreted in seconds (sec); output is converted to compound format `hh:mm:ss.ss`.

> The data types `time`, `length`, `weight`, `speed`, and `acceleration` are not compatible.
