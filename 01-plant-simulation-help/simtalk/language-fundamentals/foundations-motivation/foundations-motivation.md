# Foundations & Motivation

## Reference Parameters

Reference parameters (declared with the keyword `byref`) cannot have a default argument.

## General Access to SimTalk

SimTalk extends the ways you can model and control a simulation. Each object has built-in properties providing many useful features. If your model requires more detailed or completely different properties, you program these in SimTalk. You can also combine the Method object with built-in objects to create models of great complexity.

You type the statements into an instance of the object **Method**, which the built-in Interpreter executes. Press the **F7** and **F5** keys to execute your source code. The Copilot can assist you in writing source code in a Method. When you run the simulation, the Interpreter executes the source code line-by-line and takes the actions you programmed.

SimTalk normally does not distinguish between upper- and lower-casing for the names of methods, attributes, and read-only attributes typed into Method source code.

### SimTalk 2.0 vs SimTalk 1.0

SimTalk 2.0 makes programming methods in Plant Simulation faster, easier, and less error-prone than SimTalk 1.0. New simulation models use the SimTalk 2.0 notation by default.

- Switch between SimTalk 1.0 and 2.0 by clicking **New Syntax** on the Tools ribbon tab of the Method.
- To use SimTalk 2.0 syntax for all new Methods, activate **New Syntax** in the Method class in the Class Library.
- You can freely mix SimTalk 2.0 and 1.0 notation in simulation models — no need to reprogram existing source code.
- Clicking **New Syntax** in an existing SimTalk 1.0 Method automatically converts the source code to SimTalk 2.0.
- To convert all existing Methods in a model: hold Shift, right-click the object **Basis** in the Class Library, and click **Convert all Methods to New Syntax**.

## Why Use SimTalk 2.0?

SimTalk 2.0 provides significant improvements over SimTalk 1.0. Use SimTalk 2.0 whenever possible — support for SimTalk 1.0 might be terminated at a future date.

### Line-controlled syntax

No semicolon `;` is required at the end of each statement. You can type a single statement per line. The interpreter automatically determines if a statement is still incomplete and continues it on the next line. You can type a semicolon to add another statement to the same line.

| SimTalk 2.0 | SimTalk 1.0 |
|---|---|
| `MyStation.setName("MyStation")` | `MyStation.setName("MyStation");` |

### Simplified body syntax

SimTalk 1.0 requires the keywords `is do end`. SimTalk 2.0 does not need these keywords. In SimTalk 2.0 you declare:

- parameters with the keyword `param`
- local variables with the keyword `var`
- the return value of a method with `->` (hyphen plus right angle bracket)

| SimTalk 2.0 | SimTalk 1.0 |
|---|---|
| `MyStation.setName("MyStation")` | `MyStation.setName("MyStation") is`<br>`do`<br>&nbsp;&nbsp;&nbsp;&nbsp;`MyStation.setName("MyStation");`<br>`end` |

### Improved referencing of methods and global variables

SimTalk 1.0 references Methods and Variables with the reference operator `ref`. SimTalk 2.0 references them with a leading `&` operator:

```simtalk
var o:object := &Method
```

### New div/mod operators

SimTalk 1.0 uses `//` for integer division and `\\` for integer modulo. SimTalk 2.0 uses the keywords `div` and `mod`.

### Improved string literals

In SimTalk 2.0 a backslash `\` inside a string only protects double quotation marks and line breaks — it does not protect another backslash (as in SimTalk 1.0).

```simtalk
a := "It is \"very\" urgent."  -- the backslash protects the quotation marks
Path := "C:\Temp"             -- no need to protect the backslash here
Path := "C:\\" + FolderName    -- protected backslash at the end of the string
```

### Time literals

A time literal starts with a digit and must contain one or more colons. It can contain a decimal point and decimal places.

```simtalk
wait 1:30                    // wait for 1 minute and 30 seconds
&Methode.methCall(1:0:0:0.5)   // call the method in 1 day and half a second
```

### JSON literals

JSON literals are enclosed in curly braces `{}` and contain JSON elements separated by commas. Each element consists of a string literal, a colon, and a JSON value.

```simtalk
var j: json
var jobTitle: string := "Engineer"
var addressArray: string[] := ["Main street 42", "10001 New York"]
j := { "name": "Alice", "age": 42, "female": true,
     "job": jobTitle, "address": addressArray }
```

### Default arguments

Define default arguments for formal parameters by typing an assignment operator and the default value after the parameter declaration:

```simtalk
param x := 0
```

### Simplified control flow statements

| SimTalk 2.0 | SimTalk 1.0 |
|---|---|
| `if-end` | `if-then-end` |
| `for-next` | `for-loop-next` |
| `switch-case-end` | `inspect-when-then-end` |
| `while-end` | `while-loop-end` |

- The keyword `then` in if-statements is optionally allowed.
- The keyword `loop` in loops is optionally allowed.
- The keyword `continue` skips the rest of the loop iteration and continues with the next iteration (if it was the last iteration, `continue` exits the loop).

### Changed "about equal" operator

| SimTalk 2.0 | SimTalk 1.0 |
|---|---|
| `~=` | `==` |
| `<~=` | `<==` |
| `>~=` | `>==` |

### New compound assignment operators

```simtalk
x += y   -- short for x := x + y
x -= y   -- short for x := x - y
x *= y   -- short for x := x * y
```

### Improved list and table syntax

List ranges are typed using braces `{}` only. The optional 1.0 syntax using a grave accent `` `[] `` is no longer available.

Read an element of a one-dimensional list with the bracket operator `[]` (works for StackFile and QueueFile as well). Read and remove an element from a DataList with the built-in method `remove`.

In SimTalk 1.0, reading a DataList cell with `[]` reads **and removes** the contents (remaining cells move up); assigning a value inserts it (existing cells move down). In SimTalk 2.0, reading with `[]` leaves the contents in place, and assigning overwrites the existing cell — so a DataList behaves like a DataTable with one column.

## Introducing SimTalk

SimTalk consists of built-in methods, read-only attributes, attributes, and control structures:

- **Built-in methods, read-only attributes, and attributes** — provided by built-in Plant Simulation objects and defined by the software engineers.
- **Control structures and language constructs** — loops and conditional branching control the sequence of method execution.

### Syntax notation conventions

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier and parameter data type) is listed in parentheses. `(Parameter:string)` designates a string parameter. Instead of a constant, you can use a variable of the required type or a method returning the required type.
- Optional parameters are listed in brackets, e.g. `[,Parameter:boolean]`.
- If a parameter has a default value, the signature shows the default value after the parameter.
- If the method has a return value, the signature shows its data type after the arrow `->`.
- Make sure to enter parentheses for expressions within parentheses `(…)` — omitting them may lead to unexpected results and open the Debugger.

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected **Class**.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show them for the selected **Instance**.

### Spelling conventions in the Help

- Object names begin with an upper-case letter and are italicized (e.g. *ParallelStation*, *Station*).
- Method names begin with a lower-case letter; each new term after that begins with an upper-case letter (e.g. *derive*, *updateDialog*).
- Attribute and read-only attribute names begin with an upper-case letter (e.g. *CreationTableActive*, *ReferenceTime*).
- `MU` and `part` are used interchangeably. If `Part` starts with an upper-case P, it refers to the MU of type Part.
- SimTalk is case-insensitive for method, attribute, and read-only attribute names — e.g. `CreationTableActive`, `creationtableactive`, or `CREATIONTABLEACTIVE` are equivalent.
- SimTalk supports English and German. The German Help shows the English name next to the German name, separated by a forward slash (e.g. *EnergieAktiv [SimTalk] / EnergyActive*).

## SimTalk Attributes, Read-only Attributes, Methods, and Functions

### Attributes

An attribute sets or gets a property of an object. Attributes encompass built-in attributes, user-defined attributes, local variables, and objects of type Variable.

```simtalk
EventController.AbsTimeFormat := true
print EventController.AbsTimeFormat // returns true
```

### Methods

A method is a block of source code that executes a task when called. Methods as a rule have parameters, have side effects, and can return a value. A method:

- gets information from an object and returns a value
- computes a value
- starts one or several actions that control the behavior of the object

```simtalk
TableVariable := EventController.getEventList(-1)
MyStation.addObserver("occupied", &myMethod)
```

### Read-only Attributes

A read-only attribute returns a value of a property of an object. Read-only attributes do not expect parameters, do not have side effects, and return a value.

```simtalk
param sensorID: integer, Front: boolean
if @.ID = 1 
   @.Speed := 0
   print EventController.SimTime, " The first Transporter stopped."
end
```

### Functions

A function is a piece of source code that applies in general and is not object-specific.

```simtalk
if currentEventCtl /= VOID
   print "simulation running in frame", currentEventCtl.location
   print "simulation running in frame", root
end
```

## See Also

- Declare Parameters
- Colors for Syntax Highlighting
- SimTalk Access to 3D Functions
- String [SimTalk] - value
