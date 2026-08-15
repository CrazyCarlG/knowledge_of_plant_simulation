# Values, Variables & Parameters

## Namespace

All objects inserted into a Frame, plus the names of its built-in attributes and methods and the names of the user-defined attributes, form a **namespace**. The same applies to folders and to any objects that provide built-in attributes/methods with user-defined attributes.

- Within a namespace, each name must be unique (no duplicate names allowed).
- Identical names may be used in *different* namespaces; Plant Simulation differentiates them by their paths.

**See also:** Name, `isNameUnique`.

---

## Constant Values

Constants contain values that do not change. You can assign constant values of the following data types:

- Boolean
- Integer
- Real
- String
- pi

### Boolean

Assign `true` or `false` to a boolean constant.

```simtalk
order_done := true
```

### Integer

Assign numbers 0–9 with an optional leading sign (`+` or `-`); this is called an *integer constant*. The range is **−9223372036854775807** to **9223372036854775807**.

```simtalk
order_number := -112304
```

### pi

The constant `pi` is the ratio of a circle's circumference to its diameter; it has data type `real`.

```simtalk
print pi // 3.141592653589793
```

### Real

Assign one or several digits after the decimal point (a *real constant*). In exponential notation, the value consists of a mantissa followed by `E` and an exponent (e.g. `100` as `1.0e2`).

- The exponent range is limited to `[307, -307]`.
- A real constant is recognized by its decimal point; without it, the value is an `integer` with a limited range.
- The types `time`, `date`, and `dateTime` do not support constant values; use real/integer constants or conversion functions `str_to_time`, `str_to_date`, `str_to_dateTime`.

```simtalk
Conveyor.Speed := 2.5
Avogadro := 6.5e23
epsilon := 1.0e-6 // 0.000001
```

### String

Assign a string of letters, numbers, and special characters within quotation marks `""` (a *string constant*).

```simtalk
priority := "Urgent"
```

Rules for string constants:

- To use quotation marks inside a string, protect them with a backslash `\`.

```simtalk
print "It is \"very\" urgent."
-- outputs It is "very" urgent.
```

- To specify a line break, terminate the line with a backslash `\` and continue on the next line.

```simtalk
var address : string
address := "Frank Jones\
Halford Lane 9\
Cedar Rapids, IA 52409"
print address
-- outputs
Frank Jones
Halford Lane 9
Cedar Rapids, IA 52409
```

- Protect a backslash by typing a second backslash `\\` (necessary if the literal ends with a backslash).

```simtalk
a := "It is \"very\" urgent." -- the backslash protects the quotation marks
Path := "C:\Temp"             -- no need to protect the backslash here
Path := "C:\\" + FolderName   -- protected backslash at the end of the string
```

- A string constant can contain **1024 characters** at most. Link individual strings with `+` to build arbitrary-length strings.

```simtalk
var s : string
s := "This is a long string," +
" formed by linking together several" +
" sub-strings."
print s
-- outputs This is a long string, formed by linking together several sub-strings.
```

---

## Variables

Local variables, global variables, and parameters store values over time and allow access at a later point. Their values can be changed at any time.

### Local Variables

Use a local variable to save a calculation result for reuse within the same Method call (when you do not need it after the call ends).

- A local variable's name is only known within the Method where it is declared; other Methods cannot access it.
- Each Method call creates a **new set** of local variables. If a Method calls itself, a new set is created and only that new set is accessible until the call finishes.
- Declare the local variable before using it.

**Initial values** before assignment:

| Data type | Initial value |
|-----------|---------------|
| numerical types | `0` |
| boolean | `false` |
| string | `""` |
| object, list/table | `void` |
| date | `1900/01/01` |
| dateTime | `1900/01/01 00:00:00.0000` |

(For models originally created in Plant Simulation 13 or older, the initial value differs depending on the version.)

If you need to access the saved value later, use the object `Variable` (see global variables).

### Data Types in Local Variables

Usable data types: `Integer`, `Real`, `Length`, `Speed`, `Acceleration`, `Weight`, `Time`, `Date`, `DateTime`, `Json`, `Boolean`, `String`, `Object`, `Table`, `List`, `Stack`, `Queue`, and `Any`.

For `stack`, `queue`, `list`, and `table`, type the data type(s) of the columns in brackets `[data type]`. These local variables differ from Frame-inserted objects — they only provide built-in methods for Instantiation, State, Access, and Order.

| Data type | Shares built-in properties of |
|-----------|-------------------------------|
| List | DataList |
| Queue | DataQueue |
| Stack | DataStack |
| Table | DataTable |

Before first accessing these data types, create the local variable with `create` or assign a value.

```simtalk
var l: list[string]
l.create
l.insert(1,"Hello")
```

**Initial values:**

| Data type | Initial value |
|-----------|---------------|
| integer, real, length, … | `0` |
| boolean | `false` |
| string | `""` |
| object | `void` |
| time | `0:00:00` |

### Declare Local Variables in the Source Code

Start with the keyword `var`, followed by one or several identifiers, then optionally a colon and the data type.

```simtalk
var x, y: integer
```

You can also assign a value at declaration; then declaring the data type is optional (it is determined by the assigned value).

```simtalk
var a: length := Track1.Length
var b: Length := Track2.Length
var c: Length := sqrt(a*a + b*b)
print c
```

```simtalk
var a := Track1.length
var b := Track2.length
var c := sqrt(a*a + b*b)
print c
```

A variable declared like this is visible from its declaration line to the end of the source code.

**Loop behavior:** If you declare a local variable inside a loop, the initial value is *not* reset each pass — the variable keeps its previous value. However, an assignment within the declaration is re-executed each pass.

```simtalk
// the loop outputs: 0 0 --> 1 0 --> 2 0
for var i := 1 to 3
    var x: integer
    var y: integer := 0
    print x, " ", y
    x += 1
    y += 1
next
```

**Visibility:** A local variable declared inside an `if`-statement is visible after it, even if the instructions were not executed — in that case it holds the initial value (even if the declaration contains an assignment).

```simtalk
if 1 = 2
   var x: integer := 1
end
print x  // outputs 0
```

The same applies to loops: if a loop never executed (condition false from the start), the variable declared inside is still accessible after the loop and holds the initial value.

```simtalk
for var y := 1 to DataTable.yDim
    var i : integer
    i := DataTable[1,y]
next
print i    // outputs 0 if the DataTable is empty
```

### Global Variables

A global variable holds a non-fixed value accessible by any Method; data stored persists after the Method finishes.

- Use global variables (or list entries) to keep data for extended periods during a simulation run.
- Plant Simulation provides the object `Variable` as a global variable. Any Method can access it by name and an absolute or relative path.
- If you do not need the value later, use a local variable instead.

```simtalk
MyVariable := Transporter:1.CurrentSpeed  -- assign a new value to the global variable 'MyVariable'
print MyVariable                          -- read out the value and print it into the Console window
print &MyVariable.DataType       -- print the data type of 'MyVariable'
var obj : object := &MyVariable  -- store a reference to 'MyVariable' in a local variable of data type object
```

---

## Parameters

You can pass values (called **arguments**) to a Method when it is called. Declare the same number of parameters in the Method, with the same data types as the arguments. Exception: integer and real values are converted automatically.

In the example below, `x` is the parameter name and `123` is the argument value.

```simtalk
param x: integer := 123
```

> **Note:** When converting real → integer, Plant Simulation deletes numbers after the decimal point, which may cause unexpected behavior. Generally avoid automatic type conversion.

### Declare Parameters

Declare parameters at the start of the source code, starting with the keyword `param`, then the identifier, a colon, and the data type.

- Several parameters with the same data type can be listed comma-separated before a single colon and data type.
- Parameters with different data types are separated by commas (each with its own colon and data type).

```simtalk
param repeats: integer                           // single parameter of data type integer
param minimum, maximum: real                     // two parameters of data type real
param rpm: real, tool: string                    // two parameters with different data types
param workpiece: string, Islength, shorten: real // three parameters with different data types
```

Parameters are used like local variables; the initial value is set by the caller.

Type `byref` in front of a parameter to pass a **reference** instead of a value — changes then affect the caller.

For `stack`, `queue`, `list`, and `table`, only the data type is required (no additional type parameters).

```simtalk
param order: list                                 // DataList of any type
param orders, deliveries: queue                   // two DataQueues of any type
param cost: table, VAT: real, complaints: stack   // mixed declaration DataTable and DataStack
```

**Optional parameters:**

```simtalk
param maxValue:real := 1.0 -> real                // optional parameter
return z_uniform(0,maxValue)
```

**Function result** (no parameters — just declare the result type; or with parameters):

```simtalk
-> boolean // no parameters
// or with parameters
param v1,v2: integer, name: string -> boolean
```

### Declare Default Arguments

Default arguments (optional arguments/parameters) are supported in SimTalk 2.0. If a Method is called without the argument, the parameter takes its default value.

```simtalk
param x: integer := 123
```

The Method can be called with or without an argument; without one, `x` has the value `123`.

If a parameter has a default argument, **all following parameters must also have a default argument**.

```simtalk
param a: string,
      b, c: string := "",
      d: boolean := true
```

This Method can be called with one to four arguments (but not zero, since `a` has no default):

```simtalk
Method("A")
Method("A", "B")
Method("A", "B", "C")
Method("A", "B", "C", false)
```

**Allowed values for default arguments:**

- Only constant values: numbers, string constants, `true`, `false`, `void`, and `pi`.
- Parameters of type `object`, `table`, `list`, `stack`, `queue`, and `any` can only have `void` as default.
- Parameters of type `date` and `dateTime` cannot have a default argument.
- Parameters of type `array` can have an empty array `[]` or an empty JSON object `{}` as default.
- Reference parameters (`byref`) cannot have a default argument.

### Declare the Function Result of a Method

A Method can return a result like a function. Specify `->` (minus sign and greater-than sign) followed by the data type. If the function requires parameters, specify them before the `->` return-value declaration.

- A function returns only **one** result.
- Within the function, assign the result to the return value `result`; Plant Simulation returns its contents to the caller.

Examples:

```simtalk
-> real                                     // function without parameter, calculates a real value

param CustomerNo:integer
-> string                                   // function with a parameter, returns a string

param orders,deliveries: list, delivery_date: time
-> table                                    // function with several parameters, returns a table
```

> **Note:** Instead of `result`, you can also terminate the Method using `return`.

For `stack`, `queue`, `list`, and `table`, the local variable `result` starts empty — assign a value to it or call `create` before accessing it.
