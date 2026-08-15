# Operators

## Manually Converting Data Types

The remaining data types must be converted explicitly by calling the conversion functions listed below:

| Conversion method | Data type of the return value |
| --- | --- |
| `bool_to_num` (boolean) | real |
| `num_to_bool` (integer) | boolean |
| `str_to_bool` (string) | boolean |
| `str_to_date` (string) | time |
| `str_to_dateTime` (string) | dateTime |
| `str_to_length` (string) | length |
| `str_to_num` (string) | real |
| `str_to_obj` (string) | object |
| `str_to_speed` (string) | speed |
| `str_to_time` (string) | time |
| `str_to_weight` (string) | weight |
| `to_str` (any, … ) | string |

## Operators and Expressions

The most basic and simplest form of an expression is a constant value or a variable value. By combining constants or variables and operators, you can create increasingly complex expressions.

The order in which Plant Simulation analyzes complex expressions depends on the priority of the operators involved.

Plant Simulation provides arithmetic operators, the logical operators AND and OR, the logical operator NOT, and relational operators. Some operators are restricted to certain data types. Logical operators combine boolean expressions, for example.

## Arithmetic Operators

SimTalk supports the basic arithmetic operators.

- **Addition (`+`), subtraction (`-`), multiplication (`*`), and floating-point division (`/`)** compute a new number from two given numbers.

```simtalk
x += y      // adds a value (short for x := x + y)
x -= y      // subtracts a value (short for x := x - y)
x *= y      // multiplies a value (short for x := x * y)
1 + 2  * 3  // returns 7
(1 + 2) * 3 // returns 9
```

For objects of type `Variable` and for user-defined attributes of data types `time`, `length`, `weight`, `speed`, and `acceleration`, the operators `+=` and `-=` check the type more accurately than in previous versions. The following source code will throw an error:

```simtalk
var len : length
VariableObjectOfTypeSpeed += len   // not allowed any longer
len += VariableObjectOfTypeSpeed   // was never allowed
```

- **Integer division (`//`)** is defined for the data type integer, returns another integer as the result, and ignores the remainders.

```simtalk
15 div 5 // returns 3
17 div 5 // also returns 3
```

- **Modulo operation (`mod`)** returns the remainder of an integer division that the division of integer values suppresses.

```simtalk
15 mod 5 // returns 0
17 mod 5 // returns 2
Variable := Variable mod 360
```

Use the modulo operation to find out if an integer is an odd or an even number:

```simtalk
14 mod 2 = 0
15 mod 2 = 1
```

The modulo operation (`mod`) also works for floating point values:

```simtalk
print 6.123 mod 2.5 // outputs 1.123
```

## Relational Operators

The relational operators compare two values. The result has the data type boolean.

| Operator | Operator Name | Result of the Comparison |
| --- | --- | --- |
| `=` | equal to | true if left and right side are equal, otherwise false (strings are case-sensitive) |
| `/=` or `!=` | not equal to | true if left and right side are not equal, otherwise false |
| `<` | less than | true if left side is less than right side, otherwise false |
| `<=` | less than or equal to | true if left side is less than or equal to right side, otherwise false |
| `>` | greater than | true if left side is greater than right side, otherwise false |
| `>=` | greater than or equal to | true if left side is greater than or equal to right side, otherwise false |
| `~=` | about equal to | true if left and right side are about equal, otherwise false * |
| `<~=` | less than or about equal to | true if left side is less than or about equal to right side, otherwise false * |
| `>~=` | greater than or about equal to | true if left side is greater than or about equal to right side, otherwise false * |

### About Equal Operators

\* The about equal operators `~=`, `<~=`, and `>~=` ignore the case when comparing strings and ignore value differences less than epsilon when comparing numbers. For numerical values you can set the *Tolerance for About Equal Comparison*.

```simtalk
print "a" = "A"              -- false
print "a" ~= "A"             -- true
print 1 = 1.00000000000001   -- false
print 1 ~= 1.00000000000001  -- true
```

You can search for a fuzzy match with the about equal operator `~=`:

```simtalk
-- fuzzy match 1: ignores upper and lower case
"hello" ~= "HELLO"
-- fuzzy match 2: ignores leading & trailing spaces
strTrim("  hello  ") ~= strTrim("hello    ")
-- fuzzy match 3: ignores both of the above
strTrim(s1) ~= strTrim(s2)
```

> Searching for a fuzzy match might fail because the string contains invisible characters, for example control characters.

### Compare Storage Places on Objects and Objects with the about equal operator

All material flow objects that can receive MUs have one or more storage places. The about equal operator `~=` returns true under these conditions:

- If both values have the data type `object` and if the objects are identical.
- If both values are of data type `storage place`, and if both storage places are located on the same object.
- If one value has the data type `storage place` and the other has the data type `object` and if the storage place is located on the object.

```simtalk
var L : object := "Store"
var L11 : any := Store[1,1]
var L23 : any := Store[2,3]
var W : object := TwoLaneTrack
var WA : any := TwoLaneTrack.A
var WB : any := TwoLaneTrack.B
print L ~= L11    -- true
print L11 ~= L23  -- true
print W ~= WA     -- true
print WA ~= WB    -- true
print L ~= W      -- false
print L11 ~= WA   -- false
```

### Supported Data Types

The relational operators `=` and `/=` support comparing the following data types:

| Left Side | Right Side |
| --- | --- |
| integer, real, length, weight, speed, time, acceleration | integer, real, length, weight, speed, time, acceleration |
| date, dateTime | date, dateTime |
| string | string |
| boolean | boolean |
| object | object |
| table, list, stack, queue | table, list, stack, queue |

> When comparing values of data type `object`, Plant Simulation always compares the absolute object paths. It resolves relative paths before comparing them.
>
> When comparing values of data type `table`, `list`, `stack`, and `queue`, Plant Simulation checks if it is the same list/table. The relational operator `=` returns `false` if a list/table is compared with a copy.

The relational operators `<`, `<=`, `>=`, `>`, `~=`, `<~=`, and `>~=` support comparing the following data types:

| Left Side | Right Side |
| --- | --- |
| integer, real, length, weight, speed, time, acceleration | integer, real, length, weight, speed, time, acceleration |
| date, dateTime | date, dateTime |
| string | string |

You can use the result of a comparison in nested expressions. For example, concatenate several comparisons with the logical operators AND, OR, and NOT:

```simtalk
if index > 0 and index <= DataList.Dim
   print "index in valid range"
end
```

## The Logical Operators AND and OR

The logical operators connect two boolean expressions. They return true under the following conditions:

- **AND** only returns true if both operands have the value true.

| AND | false | true |
| --- | --- | --- |
| false | false | false |
| true | false | true |

- **OR** returns true if at least one of the two operands has the value true.

| OR | false | true |
| --- | --- | --- |
| false | false | true |
| true | true | true |

Plant Simulation analyzes a logical combination from left to right. The evaluation ends as soon as the value of the expression is known.

```simtalk
expression1 AND expression2
```

`expression2` is not going to be evaluated if `expression1` returns false — independent of `expression2`, the combined result is already false. You can use this for programming branching operations and loop termination conditions:

```simtalk
if i <= DataList.dim AND DataList[i] > 0
   // process entry
end
```

The first expression (`i <= DataList.Dim`) ensures that the list is only accessed if the index is small enough. The same is true for the operator OR: as soon as the expression on the left returns true, Plant Simulation stops evaluating.

Example — search a list for a value greater than 0:

```simtalk
var i := 0
repeat
    i := i + 1
until i > DataList.Dim OR DataList[i] > 0
```

If the list does not contain a value greater than 0, Plant Simulation exits the loop when the index is greater by one than the largest index permitted. It then does not access the second part of the expression.

## The Logical Operator NOT

The logical operator NOT negates a value of data type boolean, i.e., it changes true to false and vice versa.

```simtalk
failure := false
print failure         // outputs false
print NOT failure     // outputs true
print NOT NOT failure // outputs false

var i,j :real

i:=4.00000001
j:=3.999999

if NOT {i~=j}
```

## Assignment Operators

SimTalk provides several assignment operators:

- The assignment operator `:=` or `=` respectively
- The reference operator `&`
- `byRef`
- `void`

### `:=` — assignment operator

The assignment operator `:=` assigns a new value to a variable. Plant Simulation first evaluates the expression to the right of the operator. If value and variable have the same data type, the value is assigned to the variable.

> Instead of `:=` you can also use `=` as the assignment operator.

If the data types are different, the value has to be converted first. Plant Simulation automatically converts real into integer and integer into real values. During the conversion of real values into integer values, Plant Simulation deletes the numbers after the decimal point. The same is true for assignments of date to dateTime and dateTime to date — the time part will be discarded.

```simtalk
integerVar := 2.999 // value is 2, no digits after decimal point
```

Instead, you can also type:

```simtalk
integerVar = 2.999 // value is 2, no digits after decimal point
```

All other data types must be converted explicitly using the respective conversion functions (see Manually Converting Data Types).

```simtalk
var r: real; var b: boolean; var s: string; var d: date; var dt: dateTime
r := 1.0 + 4 * (3 - 0.18)                      // 12.28
b := true and (b or true)                      // true
s := "new" + " value"                          // "new value"
dt := str_to_dateTime("2018/1/31 13:45:44")    // date and time
d := dt                                        // date without time, i.e. midnight
```

Plant Simulation first completely evaluates the right side of an assignment before assigning the value to the variable on the left side. This permits directly increasing the value of a variable:

```simtalk
a := a + 3 // integer
```

Suppose that the variable `a` has the value 5; then the right side is formed by adding the previous value of `a` and the integer value 3, equaling 8. This sum is then assigned to the variable `a`. The previous value will be overwritten.

### `&` — reference operator

The reference operator `&` accesses attributes or methods of objects.

Be aware of the following before accessing attributes or methods of objects of type `Variable` or `Method`, or user-defined attributes of data type `object` or `json`:

- When accessing a global `Variable`, Plant Simulation returns its contents, so you would send the attribute/method name to the contents and not to the Variable object itself.
- When accessing a `Method`, Plant Simulation starts executing the Method, so you would send the attribute/method name to the result and not to the Method object itself.
- When accessing a user-defined attribute of data type `object` or `json`, Plant Simulation accesses the value of the user-defined attribute and not the user-defined attribute itself.

The reference operator prevents accessing the contents of the Variable or calling the Method, and returns the reference to the object itself. You can then specify this reference or the path in lists or tables, and specify them as parameters into other methods.

For object paths, insert the reference operator `&` directly in front of the name of the Method or the Variable:

```simtalk
print &MyVariable.DataType
print .UserObjects.&MyVariable.DataType
var obj: object
obj := &MyMethod
obj := &MyVariable
MyStation.&ObjAttr.InitValue := Buffer     // assigns the initial value of the user-defined attribute of data type object
MyStation.&JsonAttr.InheritValue := false  // turns off inheritance of the user-defined attribute of data type JSON
```

If you have a reference to a global Variable and want to read its value, apply the attribute `Value` to the reference. If you have a reference to a Method and want to call it, call the method `execute` for the reference.

```simtalk
MyVariable := .MaterialFlow.Station  // variable of data type object
var obj := &MyVariable
print obj.Name                       // returns MyVariable
print obj.Value.Name                 // returns Station

obj := &MyMethod                     // reference
obj.execute                          // call
obj := &methodWithArgument
obj.execute(1.0, true,"parameter")   // call with parameter
```

> If you are using a user-defined attribute of data type `method`, and want to access the attributes and methods of that user-defined attribute, you may not use the reference operator.

```simtalk
Station.method                // executes the user-defined method
Station.method.executeIn(60)  // schedules the user-defined method to be called in 60 seconds
```

### `byref` — reference operator

The `byref` operator passes parameters as a reference.

Passing parameters as a reference means that Plant Simulation does not copy the value into the parameter; instead, the called Method directly accesses the calling local variable. The keyword `byref` can return more than one result to the calling Method. You can only specify local variables. The data type of the passed local variable has to be the exact same data type as the formal parameter — Plant Simulation does not convert the data types of referenced parameters.

```simtalk
param byref a,b : real             // declares method1
a := a + 1
b := b + 1
                                   // declares method2
var x, y : real
print x, " ", y                    // 0 0
method1(x, y)
print x, " ", y                    // 1 1
method1(x, x)
print x, " ", y                    // 3 1
```

### `void` — variable

Plant Simulation assigns the value `void` to a local variable if a local variable of data type `object` points to a Plant Simulation object that does not exist.

## Compatibility of Data Types

You can only use mathematical and relational operators with certain data types. The result of the operation may even have a totally different data type.

The following tables list the combinations allowed and the data type of the result. If you are looking for the operation `a op b`, search the data type `a` in the row and the data type `b` in the column. The entry in the table contains the data type of the result.

The data types `time`, `length`, `weight`, `speed`, and `acceleration` are not compatible. For example, you can only assign a value of data type `length`, `real`, or `integer` to a variable of data type `length`.

### Compatibility When Assigning a Data Type

When assigning a value to a variable or an attribute, Plant Simulation retains the data type of the variable or attribute. An assignment is only allowed if the data types match, or if the value to be assigned and the variable/attribute are both numerical — except if they have two differing physical units. You can assign a value of data type `length` to an integer or real variable, but not to a speed variable.

Values are only changed for the data type `integer`, as the digits after the decimal point are cut off. Allocating 2.5, for example, returns an integer variable with the value 2.

Read the table as follows: the columns contain the data type of the value to be assigned; the rows contain the data type of the Variable or attribute to which the value is going to be assigned.

| `:=` | integer | real | length | weight | speed | time | date | datetime | string | object |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| integer | integer | integer | integer | integer | integer | integer | — | — | — | — |
| real | real | real | real | real | real | real | — | — | — | — |
| length | length | length | length | — | — | — | — | — | — | — |
| weight | weight | weight | — | weight | — | — | — | — | — | — |
| speed | speed | speed | — | — | speed | — | — | — | — | — |
| time | time | time | — | — | — | time | — | — | — | — |
| date | — | — | — | — | — | — | date | date | — | — |
| datetime | — | — | — | — | — | — | datetime | datetime | — | — |
| string | — | — | — | — | — | — | — | — | string | string |
| object | — | — | — | — | — | — | — | — | object | object |

### Compatibility When Adding Values

When adding values to each other, Plant Simulation considers the data types `integer` and `real` to be without unit. If the data types of the operands are incompatible, the result has the data type `real`.

Read the table as follows: the rows contain the data type of the left operand; the columns contain the data types of the right operand.

| `+` | integer | real | length | weight | speed | time | date | datetime | string |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| integer | integer | real | length | weight | speed | time | date | datetime | — |
| real | real | real | length | weight | speed | time | datetime | datetime | — |
| length | length | length | length | — | — | — | — | — | — |
| weight | weight | weight | real | weight | — | — | — | — | — |
| speed | speed | speed | — | — | speed | — | — | — | — |
| time | time | time | — | — | — | time | datetime | datetime | — |
| date | date | datetime | — | — | — | datetime | — | — | — |
| datetime | datetime | datetime | — | — | — | datetime | — | — | — |
| string | string | — | — | — | — | — | — | — | string |

### Compatibility When Subtracting Values

When subtracting values from each other, Plant Simulation considers the data types `integer` and `real` to be without unit. If the data types of the operands are incompatible, the result has the data type `real`.

Read the table as follows: the rows contain the data type of the left operand; the columns contain the data types of the right operand.

| `-` | integer | real | length | weight | speed | time | date | datetime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| integer | integer | real | length | weight | speed | time | — | — |
| real | real | real | length | weight | speed | time | — | — |
| length | length | length | length | — | — | — | — | — |
| weight | weight | weight | — | weight | — | — | — | — |
| speed | speed | speed | — | — | speed | — | — | — |
| time | time | time | — | — | — | time | — | — |
| date | date | datetime | — | — | — | datetime | integer (days) | time |
| datetime | datetime | datetime | — | — | — | datetime | time | time |

### Compatibility When Multiplying Values

When multiplying values with each other, Plant Simulation considers the data types `integer` and `real` to be without unit. If the data types of the operands are incompatible, the result has the data type `real`.

Read the table as follows: the rows contain the data type of the left operand; the columns contain the data types of the right operand.

| `*` | integer | real | length | weight | speed | time |
| --- | --- | --- | --- | --- | --- | --- |
| integer | integer | real | length | weight | speed | time |
| real | real | real | length | weight | speed | time |
| length | length | length | real* | real* | real* | real* |
| weight | weight | weight | real* | real* | real* | real* |
| speed | speed | speed | real* | real* | real* | length |
| time | time | time | real* | real* | length | real* |

\* The result of the multiplication preserves the correct physical unit.

### Compatibility When Dividing Values

When dividing values by each other, Plant Simulation considers the data types `integer` and `real` to be without unit. If the data types of the operands are incompatible, the result has the data type `real`.

Read the table as follows: the rows contain the data type of the left operand; the columns contain the data types of the right operand.

| `/` | integer | real | length | weight | speed | time |
| --- | --- | --- | --- | --- | --- | --- |
| integer | integer | real | real* | real* | real* | real* |
| real | real | real | real* | real* | real* | real* |
| length | length | length | real | real* | time | speed |
| weight | weight | weight | real* | real | real* | real* |
| speed | speed | speed | real* | real* | real | acceleration |
| time | time | time | real* | real* | real* | real |

\* The result of the division preserves the correct physical unit.

### Compatibility of the Data Type string

The data type `string` only recognizes the addition operator (`+`). Plant Simulation combines the two strings to a new string, meaning that it appends the second string to the first string.

```simtalk
print "My short string " + "plus my long string with many words."
```

As an exception, you can also add an integer value to a string. Plant Simulation converts the integer value to a string and appends it.

```simtalk
param obj : object -> string
return obj.Name + obj.Label + obj.XPos
```
