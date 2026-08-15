# Names & Object Access

Summary of the Plant Simulation SimTalk help section on naming conventions, predefined names, keywords, anonymous identifiers, and object paths.

## Names

All objects and local variables in Plant Simulation are identified by their names or their paths. Certain limitations apply when choosing a new name:

- You cannot use the names of keywords as the name of an object or a local variable.
- Self-explanatory names (e.g., `.building1` for a Frame, `forklift` for a Transporter) make working with and maintaining a model easier.

SimTalk normally does not distinguish between upper- and lower-casing for the names of methods, attributes, and read-only attributes typed into the source code of Method objects.

## User-defined Names in Methods

Plant Simulation automatically assigns valid names to new objects. Within control methods you must select names for variables yourself.

Restrictions:

- The name cannot start with a digit. It can start with a letter or an underscore (`_`), followed by letters, digits, or underscores. Examples: `MyStation`, `_MyStation`, `MyStation1`, `My_Station_1`.
  - An object name cannot start with a digit (e.g., `1Station` is invalid).
  - Special characters with meaning in SimTalk (`+`, `-`, `*`, `/`, `=`, `<`, `>`, etc.) cannot be part of a name.
- Names of keywords and names of built-in functions/methods are not allowed.
- Names are not case-sensitive (`upper`, `UpPER`, `UPPER` are treated the same).

> Data you enter is case-sensitive. When comparing string values, Plant Simulation takes upper- and lower-casing into account.

Use names that identify the role of an object or variable whenever possible:

```simtalk
forklift.destination := .building1.station_1  -- more meaningful than:
MU1.attrib := .Frame1.Station21
```

## Predefined Names

The predefined names `reset`, `init`, `autoexec`, and `endSim` perform their tasks during the respective phase of the simulation.

Plant Simulation defines specific method names for the four consecutive phases of a simulation:

- `reset` — reset the simulation model to its initial state
- `init` — initialize the simulation model
- `autoexec` — automatically start the simulation run
- `endSim` — terminate the simulation run

These methods correspond to the buttons **Reset Simulation** and **Start/Stop Simulation** on the tab **Controls** of the EventController.

### autoexec

Plant Simulation calls the method named `autoexec` immediately after opening the simulation model, provided the `autoexec` method is located in the Class Library.

You can create and use any number of `autoexec` methods. To make the ExperimentManager run models in a batch run, start the experiment in the `autoexec` method using `startExperiment`:

```simtalk
// the name of the method is autoexec
.Models.MySimulation.ExperimentManager.startExperiment
```

### autoexecLoadObj

Plant Simulation runs all loaded method classes named `autoexecLoadObj` when it loads an object file (`*.psobj`) or library file (`*.pslib`) into the simulation model.

It also executes all user-defined attributes of data type method named `autoexecLoadObj` located in any of the loaded classes. It executes `autoexecLoadObj` methods when:

- loading an object file with `loadObjectAs`,
- selecting **Load Object**, **Load Object into Folder**, or **Update**,
- adding a library in the dialog **Manage Class Library**.

It does **not** execute `autoexecLoadObj` methods when opening a model file.

Optional parameters (data type `boolean`):

- First parameter is `true` when the Class Library is updated, `false` when loading an object.
- If located within a library, the second parameter is `true` if the library was updated, or `false` if the library was added.
- The second parameter can also be `string`: when a library is updated, the old version number is passed; when added, an empty string `""` is passed.

### endSim

Plant Simulation calls all methods named `endSim` at the end of a simulation run. Use it to, for example, evaluate the data of the run and save it to a file.

The simulation ends when the EventController has processed all events in the List of scheduled events, or when Plant Simulation reaches the **End Time** set on the tab **Settings** of the EventController.

Examples:

```simtalk
-- Show simulated Availability in the Console
print EventController.simTime," Simulated availability in the afternoon: ",
round(100 * (1 - MyStation.statFailPortion),2)," %"

-- Close a database
closeMyDatabase  -- is the name of the method that closes the database
```

Writing the contents list into a table:

```simtalk
// Copies the contents lists into the table MyContentsList
// as an array with the method copyToTable
var x,y: real, row : integer
var a: any := Buffer.ContentsList
MyContentsList[1,1] := "Buffer"
a.copyToTable(MyContentsList,2,1)
row := MyContentsList.yDim + 2 // inserts an empty line
MyContentsList[1,row] := "Conveyor"
print a // prints the contents list as an array to the console
print "Number of items: ",a.yDim
var b := Conveyor.ContentsList // local variable is of data type any
print b
print "Number of items: ",b.yDim
b.copyToTable(MyContentsList,2,row)
MyContentsList.opendialog
// Writes the ContentsList into a table
// as previous versions of Plant Simulation did
Buffer.ContentsList(ContentsListBuffer)
Conveyor.ContentsList(ContentsListConveyor)
```

Call sequence: `endSim` methods are executed in the **reverse order** in which objects were inserted. Within a Frame, the Frame's own `init`/`reset` methods are executed after the `endSim` methods of all objects inserted into it.

> Cutting/Pasting an object, or using **Bring to Front** / **Send to Back**, changes insertion order and therefore call order. `endSim` methods in a Method object and as user-defined attributes of data type method are treated the same.

### init

The Init event is the first event executed when you start a simulation. Plant Simulation executes all methods named `init` within the current model.

- **Init controls** are executed before the events are computed.
- Normal **init methods** are executed after the initial events have been computed.

Examples:

```simtalk
-- Reduce Availability after 12 simulated hours
&setFailure.methCall(str_to_time("12:0:0"))

-- Create and insert a Transporter on a Track
.MUs.Transporter.create(Track)       // inserts a Transporter anywhere on the Track
.MUs.Transporter.create(Track, 5.5)  // inserts a Transporter 5.5 meters along the Track

-- Reopen Entrance and Exit of a station (user-defined attribute named init)
self.~.EntranceLocked := false
self.~.ExitLocked := false
```

Parameters in init methods (data type `integer`): the init controls are called first; then init methods with parameter value `1`; then objects are initialized; then init methods (with or without parameter) are called, with parameter value `2`.

```simtalk
param phase: integer
if phase = 1
-- Objects are not yet initialized
-- The station has not yet computed the event for the first failure
-- so we can set the failure profile
  Station.Availability = 95;
  Station.MTTR = 10:00
else
-- Objects are already initialized
-- Now the first failure event is created based on
-- the parameters set in phase 1
   print Station.GetDisruptionBeginTime
end
```

### Init Methods and Init Controls

You can execute procedures before the simulation starts using:

- An **init control**: built-in attribute `InitCtrl` of material flow objects pointing to a Method object or a user-defined method attribute.
- An **init method**: an object of type Method named `init` (or a user-defined method attribute named `init`). It can be configured with an `integer` parameter.

The key difference is the point in time they are called:

- Init controls are executed **before** objects are initialized.
- Init methods are executed **after** all objects have been initialized.

For example, you can change the **Workers to Create** table of a WorkerPool with an init control, but not with an init method (which would be called too late).

Call sequence of init controls and init methods:

1. Init Control of the EventController
2. Init controls of all other objects (Transporter, WorkerPool, model frame, etc.)
3. Init methods with parameter (value `1`)
4. Initialization of the objects
5. Init methods with or without parameter (parameter value `2`)
6. Init methods of the inserted objects
7. Init method of the model frame

### Call Sequence of the Init Controls

1. Init control of the EventController
2. Init control of all other objects (recursively for objects inserted into a Frame)
3. Init control of the model frame

The init control of an object inserted into a Frame is always executed before the init control of the Frame itself. The last init control called is always the init control of the model frame. After this, all objects are initialized (Workers created, machines set up, etc.).

### Call Sequence of the Init Methods

The sequence is the same as the call sequence of the init controls. Within a Frame, the init methods of inserted objects are executed before the init methods of the Frame itself.

### Example of the Call Sequence

Objects inserted in this sequence: EventController; Method object named `Init` in Frame `Model`; WorkerPool; Frame1; Frame2; Station2 (in Frame2); Station (in Model); Station1 (in Frame1); Init method in Frame1; Init method in Frame2.

Init controls execute: EventController first, then Station (last inserted in Model), then Frame2's child Station2 (before Frame2 itself), then Station1, then Frame1, then WorkerPool, then the Frame `Model` last. Init methods then execute in the same recursive order.

### Call Sequence of Reset and Init Methods

Init and reset methods are always executed in the **reverse order** of insertion. Within a Frame, the Frame's own init/reset methods execute after those of all inserted objects. Cut/Paste and Bring to Front/Send to Back change insertion order. Init/reset methods in Method objects and as user-defined attributes are treated the same.

### reset

Plant Simulation calls all methods named `reset` when you click **Reset Simulation** in the EventController. It also deletes all events from the List of scheduled events, sets simulation time to 0, deletes statistics data, and clears all failures.

> The Request Control, Receive Control, and Release Control of the Importer are **not** called when resetting.
>
> `executeIn` calls do not work in reset methods, because the EventController deletes every scheduled event during the reset phase. Use an init method instead to schedule events.

Examples:

```simtalk
-- Delete all parts in the model on reset
deleteMovables

-- Reduce simulation speed on reset
EventController.Speed := 60

-- Reset Availability to 100 percent for the next run
MyStation.Availability := 100

-- Delete table contents (user-defined attribute named reset)
self.~.delete

-- Delete DataTable contents and reset a Variable counter
InventoryTable.delete({0,1}..{*,*})
NextNumber := 1

-- Reset result numbers in a Comment object
Comment.Text := "MU Type, Lifetime"+strChr(13)+strChr(10)+"----------------------"
```

## Keywords

A keyword is a reserved word in SimTalk that cannot be used as an identifier (for an object, a local variable, or a function).

SimTalk keywords:

- `and`, `basis`, `byref`, `case`, `continue`, `create`, `current`, `div`, `downto`, `else`, `elseif`, `end`, `exitloop`, `false`, `for`, `forget`, `if`, `loop`, `mod`, `next`, `not`, `or`, `param`, `pi`, `prio`, `print`, `repeat`, `result`, `return`, `root`, `rootfolder`, `self`, `stopuntil`, `switch`, `then`, `to`, `true`, `until`, `var`, `void`, `wait`, `waitExpired`, `waituntil`, `when`, `while`

Keywords are not case-sensitive (`IntEgeR` and `inTEGer` are the same). Adding letters or numbers to the beginning or end means it is no longer a keyword — `list` is not allowed, but `alist` or `list0` are allowed.

The function `checkID` checks if an expression can be used as an object name (considering all keywords and function calls).

All data types are also keywords: `Acceleration`, `Any`, `Array`, `Boolean`, `Date`, `DateTime`, `Integer`, `JSON`, `Length`, `List`, `Method`, `Object`, `Queue`, `Real`, `Speed`, `Stack`, `String`, `Table`, `Time`, `Weight`.

### Keyword descriptions

- **and** — logical operator AND.
- **case** — part of the `switch` control structure.
- **continue** — skips the rest of the loop iteration and continues with the next iteration. To continue an outer loop, specify an integer (`continue 2`).
- **div** — integer division.
- **downto** — part of the `for` loop (with `for`, `next`, `to`).
- **else** — part of the if-else-end-elseif statement.
- **elseif** — part of the if-else-end-elseif statement.
- **end** — part of if-else branching and the while loop. Indent instructions within branches/loops by at least one space.
- **exitloop** — exits any loop. Optionally set the number of loops to exit (`exitloop 2`).
- **false** — boolean value false.
- **for** — part of the for loop.
- **forget** — applies to local variables of data types `table`, `list`, `queue`, `stack`, and `any`:

```simtalk
var t: table
t.create
t.forget
t.create

var a: any
a := "Test"
forget a
a := 123
```

- **if** — part of the if-else-end-elseif statement.
- **loop** — part of loops; allows writing a loop on a single line:

```simtalk
while x < 5 x += 1 end   ->   while x < 5 loop x += 1 end
for var i := 1 to 5 print i next   ->   for var i := 1 to 5 loop print i next
```

- **mod** — integer modulo operation:

```simtalk
Variable := Variable mod 360
```

- **next** — part of the for loop.
- **not** — logical operator NOT.
- **or** — logical operator OR (also grouped with AND).
- **param** — declares parameters in a Method:

```simtalk
param v1,v2: integer, name: string
param maxValue:real := 1.0 -> real // optional parameter
return z_uniform(0,maxValue)

-> boolean // the data type of the return value is boolean
param v1,v2: integer, name: string -> boolean
```

The expression `->` (hyphen plus right angle bracket) declares the data type of the return value.

- **prio** — sets execution priority for `waituntil`/`stopuntil` statements.
- **repeat** — part of the repeat loop.
- **result** — designates the function result of a Method.
- **return** — exits a method.
- **stopuntil** — suspends Method execution until the condition evaluates to true.
- **switch** — part of the switch control structure (with `case`).
- **then** — part of the if-else-end-elseif statement; writes an if statement on a single line:

```simtalk
if x = 0 y := 1 end   ->   if x = 0 then y := 1 end
```

- **to** — part of the for loop.
- **true** — boolean value true.
- **until** — part of the repeat loop and the from-until loop.
- **var** — declares a local variable:

```simtalk
var myVariable := 42
var myDouble: real := 3.1415
var myIntegerArray: integer[]
myIntegerArray.append(3)
print myIntegerArray[1]
```

- **wait** — interrupts execution for the specified simulation time:

```simtalk
@.move  -- the part exits
?.ExitLocked := true
wait 5  -- the exit is blocked for 5 seconds
?.ExitLocked := false
```

- **waitExpired** — part of `waituntil`/`stopuntil`; sets a time limit. Set to `true` if woken up due to the time limit, `false` if woken up due to the condition:

```simtalk
waituntil Station.Empty wait 60
   if waitExpired
       Station.deleteMovables
   else
       .MUs.Part.create(Station)
   end

var t:time := z_uniform(1, 50:0, 70:0)
stopuntil GateOpen prio @.ID wait t
if waitExpired
    @.name := "Expired"
else
    @.name := "Unexpired"
end
@.move(PP)
GateOpen := false

waituntil Station.empty prio @.ID wait 5:0
if waitExpired
    @.name := "Expired"
else
    @.name := "Unexpired"
end
if NOT @.umlagern(Station)
    print Eventcontroller.simTime," The waiuntil expired and the MU ",
@.ID," was added into the forward blocking list."
end
```

- **waituntil** — suspends Method execution until the condition evaluates to true.
- **when** — part of the when-then-else statement and the switch control structure.
- **while** — part of the while loop.

## Anonymous Identifiers

Anonymous identifiers make a Method more flexible and independent of its context. Examples: `@`, `basis`, `current`, `?`, `root`, `RootFolder`, `self`.

You can insert an anonymous identifier into different models without modifying the source code. Use them when a control requires the current path.

### @

Designates the MU that triggered the respective control (e.g., the MU that entered or is ready to exit a material flow object via Entrance/Exit Control).

```simtalk
@.move(ParallelStation.succ(3))
```

### ?

Designates the material flow object or the control (Method) that called the Method. Enables a control to be used by several objects without modification.

```simtalk
?.Cont.move(E2) // moves the contents of the object that called the method to E2
```

### basis

Designates the Class Library. Usable only in comparisons (`=` or `/=`).

```simtalk
if location = basis
// in the class library
else
// inserted into a Frame
end
```

### current

Returns the Frame within which the Method object is located. Can also distinguish a local variable from a global variable with the same name (`name` is the local variable, `current.name` is the global).

```simtalk
print "Current pause ", current.pause
MyStation.pause := current.pause
var shift := root.ShiftCalendar.GetCurrShift
print "Current shift: ", shift

if not current.unplanned

if current.pause
   current.currIcon := "pause"
else
   current.currIcon := "working"
end
current.extendPath("Station")
-- checks if the object 'Station' exists in the current Frame
```

### root

Designates the topmost Frame in the hierarchy of Frames. Helpful when you do not know the name of the root Frame.

```simtalk
Method1                  // same namespace
root.Frame2.Method1      // path and name
&Method1.executeIn(8.5)  // pass to EventController
Variable.execute         // call the referenced Method (Variable has data type object)
```

### rootfolder

Designates the folder in the Class Library in which you store Methods used by a number of objects (set the attribute `RootFolder`). Prevents wasting main memory and prevents long paths, as Plant Simulation calls the method once from the Class Library instead of many instances.

```simtalk
.UserObjects.rootfolder := true
```

### self

Designates the currently executed Method. Use it if methods are likely to be renamed.

```simtalk
self.executeIn(60)
self      // returns the path to and the name of the Method
self.Name // returns the name of the Method only

self.~.pause := true  // pauses the object for which you defined the user-defined attribute
```

In a user-defined attribute of data type method, `self` is the user-defined method attribute itself; use `self.~` to access the object it is attached to. The return value has data type `object`.

## Object Paths in SimTalk

If objects are not located within the same Frame (namespace), you must add their path to uniquely identify them.

An object path consists of a sequence of names separated by a period:

```
[.]name[.name.name[...]]
```

Brackets designate optional components. The syntax of individual methods looks like:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier + data type of parameters) is in parentheses.
- Optional parameters are in brackets; default values are shown after the parameter.
- The return value data type is shown after the arrow `→`.

Plant Simulation distinguishes two kinds of paths:

- **Absolute path** — starts with a period (standing for the Class Library), followed by the folder and top-level Frame, then alternating periods and names. Example: `.Models.MyPlant.Engine_Assembly_Anytown.MyStation`
- **Relative path** — starts in the current namespace and identifies an object by a combination of built-in methods and names; usually starts with a Frame. Example: `MyPlant.Engine_Assembly_Anytown.MyStation`
- In addition, you can access a variable of data type `object` using an **object reference**.

### The Absolute Path

```simtalk
.Models.MyPlant.EngineAssemblyMyTown.MyStation
```

Use the absolute path for methods that never change (e.g., a control method in the Class Library). You must use the absolute path for MUs when modeling a complex station. Use the relative path when you want the same method, but with different source code, in instantiated Frames.

To insert the absolute path into a text box with drag-and-drop, hold down Shift and Ctrl.

### The Relative Path

The relative path starts in the current namespace, or the Frame in which the Method object is located. It starts with an anonymous identifier, a name, or a built-in method, then alternates periods with Frame names, built-in methods, attributes, or the object name.

```simtalk
MyPlant.EngineAssemblyMyTown.MyStation
```

Where the relative path starts for different objects:

| Object | Relative path starts in |
| --- | --- |
| Built-in/user-defined attribute of data type object in a material flow object | the Frame containing the material flow object |
| Built-in/user-defined attribute of data type object in a MU | the parent Frame of the material flow object containing the MU |
| Built-in/user-defined attribute of data type object in a Frame | the Frame itself |
| Source code of a Method / user-defined method attribute | the Frame containing the Method or the object with the attribute |
| DataTable / user-defined table attribute (object columns) | the Frame containing the DataTable, or the parent object with the attribute |
| User-defined table attribute of a MU (object columns) | the Frame in which the MU is located |
| WorkerPool | the Frame in which the Worker is located |

Examples:

```simtalk
Frame1.Station1      -- accessing Station1 in sub-Frame Frame1
Location.Station2    -- from a sub-Frame of Frame2, accessing Station2 in Frame2
~.Station2           -- tilde ~ abbreviates the built-in attribute Location
```

You can change the starting position of the relative path with the keywords `root`, `self`, and `RootFolder`. When dragging and dropping an object onto a text box, Plant Simulation inserts the relative path by default.

### Object Reference

A variable of data type `object` can accept a relative or absolute path as well as an object reference. This applies to global/local variables, formal parameters, and table values of data type object. An object reference always references a single object.

Plant Simulation still points to the object when you rename it. If you delete the object, the reference cannot be resolved — even if you insert a new object with the same name.

```simtalk
*.Models.Model.Station
```

The asterisk `*` in front of the path denotes the object reference.

> Use caution with object references. As a rule you can always use an object reference instead of an absolute path; use a relative path when relative addressing is needed. Main advantages over a path: higher access speed and tolerance toward renaming.
