# Branching & Loops (SimTalk Control Flow)

## Precedence

Mathematical functions assume multiplication takes precedence over addition. SimTalk can combine
mathematical and relational operators. Operator precedence spares you having to insert too many
parentheses; set them only to deviate from the given order.

**Remarks**

Plant Simulation executes an expression within parentheses first. Within parentheses, precedence rules
apply. For nested parentheses, the innermost expression is analyzed first.

The table lists operator precedence from highest to lowest. Operators on the same line share the same
precedence.

| Precedence | Operator | Description |
|------------|----------|-------------|
| highest | `( )` | parenthesis |
| | `–`, `NOT` | leading sign, negation |
| | `*`, `/`, `//`, `\\` | multiplication, division, integer division, modulo |
| | `+`, `–` | addition, subtraction |
| | `<`, `<=`, `=`, `/=`, `>=`, `>` | less-than, less than or equal, equal, not equal, greater-than or equal, greater-than |
| | `AND` | logic AND |
| | `OR` | logic OR |
| lowest | `:=` | assignment |

## Control Flow Statements

A control is not always executed linearly. Different events influence the course of execution and require
an appropriate reaction. Plant Simulation provides various language constructs for programming control
flow statements:

- Branching with `if-else-end`
- Multiple branching with `if-elseif-end`
- Conditional expressions with `when-then-else`
- Check for a large amount of different values with `switch`
- Loops
- `waituntil` and `stopuntil` for suspending Methods

---

## Branching with `if-else-end`

The `if`-statement uses the given condition to decide where to continue: either with the following
statements or with the statements in the `else` branch. Branching is terminated with the keyword `end`.

**Remarks**

Plant Simulation executes `statement_list1` if the condition is true, otherwise it executes
`statement_list2` after `else`. If you omit the `else` branch, Plant Simulation continues with the first
statement after the branching.

A `statement_list` consists of assignments, method calls, loops, or additional branches. There is no
nesting limit.

**Syntax**

```simtalk
if condition
   statement_list1
[else
   statement_list2]
end
```

**Example with an `else` branch**

Within the condition Plant Simulation checks if the Transporter has reached its destination
(`@.destination = current`). If true, the control transfers a MU to the workstation. If false, the
Transporter moves on.

```simtalk
// Is this delivery destined for us?
if @.destination = current  // yes, then unload
   @.Cont.move(workstation)
else                        // if not, then move on
    @.move(current.succ(1))
end
```

```simtalk
var ages := [34,42,18,44,53,12,63]
var countBelow30: integer
var countAbove29: integer
for var i := 1 to ages.dim
   if ages[i] < 30
       countBelow30 := countBelow30 + 1
   else
       countAbove29 := countAbove29 + 1
   end
next

print "Below 30: ", countBelow30
print "Above 29: ", countAbove29
```

**Example without an `else` branch**

The condition returns true when MUs are located on the Transporter. In this case one MU is moved from
the Transporter to the workstation. If the Transporter is empty, nothing happens.

```simtalk
if @.NumMU > 0 // parts here?
   @.Cont.move(workstation)
end
```

**See also:** `else`, Method templates `if-else` and `if-else-end`.

---

## Multiple Branching with `if-elseif-end`

When a simple true/false distinction does not suffice, use `elseif` to select one of several possibilities.

**Remarks**

SimTalk analyzes the conditions one after the other until one is true, then executes the respective
statement. If no condition is true, it executes the optional `else` branch. If there is no `else` branch,
execution continues after the final `end`.

**Syntax**

```simtalk
if condition1
   statement_list1
elseif condition2
   statement_list2
[...]
[else
   statement_list3]
end
```

**Example**

```simtalk
// Is this part destined for us?
if transporter.destination = current
// yes, look for available workstation
   if Station_1.empty
       transporter.Cont.move(Station_1)
    elseif Station_2.empty
       transporter.Cont.move(Station_2)
    elseif Station_3.empty
       transporter.Cont.move(Station_3)
    else // no idle Station
       transporter.move(current.succ(1))
    end
else // the shipment is not for us
    transporter.move(current.succ(1))
end // end of multiple branching
```

**See also:** `else`, `elseif`, Method template `if-elseif-end`.

---

## Conditional Expressions with `when-then-else`

The `when-then-else` statement selects an expression based on the value of a boolean expression.

**Syntax**

```simtalk
when condition then expression1 else expression2
```

- `condition` is a boolean expression.
- `expression1` is selected if the condition is true.
- `expression2` is selected if the condition is false.

**Examples**

```simtalk
@.color := when ?.EntranceLocked then "red" else "green"
Method(x, y + (when dy > 0 then y+dy else 100))
```

**See also:** `when`, `then`, `else`.

---

## Check for a Large Amount of Different Values with `switch`

The `switch` control structure makes choices easier and clearer when confronted with several possible
choices, avoiding lengthy `if-elseif-end` chains.

**Syntax**

```simtalk
switch expression
   case constant_list statement_list
   [case constant_list statement_list ...]
   [else statement_list]
end
```

**Examples**

```simtalk
param number: integer
switch number
   case 1
      print "not a prime number"
   case 2,5,7,3
      print "prime number"
   case 9,4
      print "square number"
   else
      print "no special number"
      print "or number greater than 9"
end
```

```simtalk
var currentDay := 3
switch currentDay
case 1
   print "Monday"
case 2
   print "Tuesday"
case 3
   print "Wednesday"
case 4
   print "Thursday"
case 5
   print "Friday"
case 6
   print "Saturday"
case 7
   print "Sunday"
end
```

### Values of Data Type String

```simtalk
var ProductColor : string := "Green"
switch strToLower(ProductColor)
case "green"
    print "Product color is green."
case "blue"
    print "Product color is blue."
end
```

For values of data type `string`, the `switch` instruction distinguishes between upper and lower casing.

### Values of Data Type Real

For values of data type `real`, the `switch` instruction does not check for exact equivalence.

For `if` instructions you can decide whether to check exact equivalence or permit an epsilon tolerance by
using `=` (equal to) or `~=` (about equal). `switch` instructions do not support this. Because the epsilon
value permits comparatively great differences, it is not used for `switch`. Instead, the last significant
digit of the internal floating point display is ignored (it would be rounded when displayed and is thus
normally invisible).

```simtalk
var x := 1.0000000000000004
print x      // outputs 1
print x - 1  // outputs 4.44089209850063e-16
if x = 1.0
   print "x = 1.0"
elseif x ~= 1.0
   print "x ~= 1.0"  // will be reached
else
   print "x /= 1.0"
end
switch x
case 1.0
   print "case 1.0"  // will be reached
else
   print "x /= 1.0"
end
```

### Range of Definition

The `expression` can be as complex as needed. The data type of the result can be `integer`, `real`, or
`string`.

### Course of Execution

SimTalk analyzes the expression once and converts it into the data type of the constant. If this is not
possible, an error message is shown. It then executes the `case` branch whose list of constants contains
the result of the expression. If no constant fits and an `else` branch is present, the `else` branch is
executed.

The order of the `case` statements and of the constants within them does not affect execution speed.

**See also:** `switch`, `case`, "Tolerance For About Equal (~=) Comparison" model setting, `setEpsilon`,
Method templates `switch-case-end` and `switch-case-else-end`.

---

## Loops

Plant Simulation provides the `while`, the `repeat`, and the `for` loop. You can exit a loop with
`exitLoop`.

### `while` loop

Plant Simulation executes the instructions within the `while`-loop several times as long as the condition
is fulfilled. It checks the condition before each iteration; if the condition is not fulfilled on the first
iteration, the loop body is never executed.

**Remarks**

If the condition never becomes false, the loop runs infinitely. Press `Ctrl+Alt+Shift` to stop the infinite
loop and open the Method-Debugger.

**Examples**

```simtalk
param n: integer -> integer  // computes the factorial of n
result := 1
while n > 1
   result := n * result
   n -= 1
end
```

```simtalk
var n := 2
while n < 10
   n := n * 2
end
```

**See also:** Method template `while-end`, `exitLoop`, `while`, `repeat`.

### `repeat` loop

Plant Simulation executes the instructions within the `repeat`-loop one or more times. It checks the
condition after each iteration and only exits when the condition is fulfilled. Therefore the loop always
runs at least once.

**Remarks**

If the condition never returns true, the loop runs infinitely. Press `Ctrl+Alt+Shift` to stop the infinite
loop and open the Method-Debugger.

**Example**

```simtalk
var x: length
repeat
   x := methodEnterLength
until x >= 0
```

**See also:** Method template `repeat-until`, `exitLoop`, `repeat`, `while`.

### `for` loop

The `for`-loop iterates through a range between a start value and an end value.

**Remarks**

The `for` loop declares a loop variable of data type `integer`, initialized with a start value. At the end of
each iteration, Plant Simulation automatically increases the loop variable by 1. The loop runs as long as
the loop variable is less than or equal to the end value. If the end value is less than the start value, the
loop is not executed at all.

The loop variable is only visible within the loop; it cannot be accessed after the loop.

> **Note:** For performance reasons, Plant Simulation evaluates the start value and end value only once.

```simtalk
for var y := 1 to table.yDim -- assignment with the := operator
   print table[1,y]
next

for var y = 1 to table.yDim -- assignment with the = operator
   print table[1,y]
next
```

Use the keyword `downto` instead of `to` to iterate backward. Plant Simulation reduces the loop variable
by 1 each time and executes the loop as long as the loop variable is greater than or equal to the end
value. If the end value is greater than the start value, the loop is not executed at all.

```simtalk
for var y := table.yDim downto 1
   print table[1,y]
next
```

Outside the loop, the loop variable identifier points to an object with that name if it exists (e.g., a
global variable).

```simtalk
// the loop variable 'i' is only visible inside of the loop
for var i := 1 to ParallelStation.NumMU
   print ParallelStation.MU(i)
next
print i // the loop variable is not visible here, consequently 'i' must be
// the name of an object
```

```simtalk
// another loop with its own loop variable 'i'
for var i := ParallelStation.NumMU downto 1
   print ParallelStation.MU(i)
next
// the local variable 'i' is visible from here to the end of the source code
var i := 1.234
print i // prints 1.234
for var i := 1 to 10  // does not compile, because 'i' is already declared
next
```

You can also use a local variable of data type `integer` as the loop variable; then omit the keyword `var`
or `local`.

```simtalk
var y: integer
for y := Table.yDim downto 1
   if Table[1,y] > 100
      exitloop
   end
next
print y // outputs the index of the first table value greater than 100
```

**See also:** Method template `for-next`, `exitLoop`, `for`.
