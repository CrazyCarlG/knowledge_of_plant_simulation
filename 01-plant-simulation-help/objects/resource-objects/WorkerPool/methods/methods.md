# Methods of the WorkerPool

The WorkerPool provides:

- The methods listed in the table of contents.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

## Syntax Line Conventions

An example of the Syntax line of an individual method might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method (identifier and data type of the parameter) is listed in parentheses. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter (`:= false`).
- If the method has a return value, the signature shows its data type after the arrow (`→ boolean`).

---

## getAssignedWorker [SimTalk]

Returns the assigned Worker designated by the number in the WorkerPool designated by `<Path>`.

**Type:** Method

**Syntax:**

```
<Path>.getAssignedWorker(No:integer) -> object
```

**Parameter:** `No` (integer) designates the number of the Worker that is assigned.

**Return Value:** `object`

**Example:**

```simtalk
print MyWorkerPool.getAssignedWorker(2)
-- might, for example, return .Resources.John:2
```

---

## getAssignedWorkersTable [SimTalk]

Returns the table that contains the assigned Workers of the WorkerPool designated by `<Path>`.

**Type:** Method

**Syntax:**

```
<Path>.getAssignedWorkersTable([AssignedWorkers:table]) -> any
```

**Parameter:** The optional parameter `AssignedWorkers` (table) designates the name of the table into which the Workers will be written. If you do not specify the optional parameter, Plant Simulation returns an array with the assigned Workers.

**Return Value:** `any`

**Example:**

```simtalk
MyWorkerPool.getAssignedWorkersTable(MyAssignedWorkersTable)
MyWorkerPool.getAssignedWorkersTable
```

---

## getIdleWorker [SimTalk]

Returns the first idle Worker in the WorkerPool designated by `<Path>`.

**Remarks:** `getIdleWorker` returns the first idle Worker for whom the attribute `IsIdle` is set to `true` and sets it to `false`. When you no longer need the Worker, you can send the Worker to the WorkerPool and set `IsIdle` to `true`.

**Type:** Method

**Syntax:**

```
<Path>.getIdleWorker -> object
```

**Return Value:** `object` — the first idle Worker in the WorkerPool, or `VOID` if no Worker is idle.

**Example:**

```simtalk
.Resources.WorkerPool.getIdleWorker
```

---

## getWorkersToCreateTable [SimTalk]

Returns the Workers to Create table of the WorkerPool designated by `<Path>` and writes it into a table.

**Remarks:** Plant Simulation always resolves relative paths in relation to the Frame in which the WorkerPool is inserted. If Plant Simulation cannot resolve a path in the Scope array during the simulation, it shows an error message and asks if you would like to stop the simulation. This also applies to the Home Location.

**Type:** Method

**Syntax:**

```
<Path>.getWorkersToCreateTable(WorkersToCreateTable:table/void[, byref Inherited:boolean])
```

**Parameters:**

- `WorkersToCreateTable` (table) designates the name of the table that contains the Workers to be created. The column of the table has to have the data type table. If the optional parameter `Inherited` is passed, you can specify `VOID` for this parameter — in this case `WorkersToCreateTable` is ignored.
- `Inherited` (boolean, optional) designates a local variable which is set to `true` if the WorkersToCreateTable of the WorkerPool is inherited, and `false` if it is not inherited.

**Example:**

```simtalk
var rt: table                             // read the Workers to Create table
MyWorkerPool.getWorkersToCreateTable(rt)  // set the new amount
rt [2,1]:= AmountOfWorkers                // name of a Variable
// assign the Workers to Create table to the WorkerPool
MyWorkerPool.setWorkersToCreateTable(rt)
```

---

## getWorkersToCreateTableRow [SimTalk] - WorkerPool

The sub-attributes of the method `getWorkersToCreateTableRow` set and get the individual settings of the Workers to Create table of the WorkerPool designated by `<Path>`.

**Remarks:** Plant Simulation always resolves relative paths in relation to the Frame in which the WorkerPool is inserted. If Plant Simulation cannot resolve a path in the Scope array during the simulation, it shows an error message and asks if you would like to stop the simulation. This also applies to the Home Location.

**Type:** Method

**Syntax:**

```
<Path>.getWorkersToCreateTableRow(row:integer).AdditionalServices:string[]
<Path>.getWorkersToCreateTableRow(row:integer).Amount:integer
<Path>.getWorkersToCreateTableRow(row:integer).Efficiency:real
<Path>.getWorkersToCreateTableRow(row:integer).HomeLocation:path
<Path>.getWorkersToCreateTableRow(row:integer).Scope:array
<Path>.getWorkersToCreateTableRow(row:integer).Shift:string
<Path>.getWorkersToCreateTableRow(row:integer).Speed:speed
<Path>.getWorkersToCreateTableRow(row:integer).Worker:object
```

**Parameters:**

- `row` (integer) designates the row in the Workers to Create table in which you would like to set the attribute.
- `AdditionalServices` is an array of data type string containing the additional services that the Worker can provide.
- `Amount` (integer) designates the number of Workers that are going to be created.
- `Efficiency` (real) designates the efficiency of the Worker.
- `HomeLocation` (path) designates the path to the Workplace to which the Worker walks once he has finished his current job.
- `Scope` (array) designates the path to the material flow objects to which the Worker can be brokered. The scope also encompasses sub-Frames.
- `Shift` (string) designates the shift during which the Worker works. You define the shift itself in the assigned ShiftCalendar.
- `Speed` (speed) designates the speed with which the Worker walks.
- `Worker` (object) sets the class of the Worker which the WorkerPool uses as the template for the Workers to be created.

**Example:**

```simtalk
MyWorkerPool.getWorkersToCreateTableRow(1).AdditionalServices := ["drill1", "drill2", "drill3"]
```

---

## getWorkingWorkersTable [SimTalk]

Returns the table that contains the working Workers of the WorkerPool designated by `<Path>`.

**Type:** Method

**Syntax:**

```
<Path>.getWorkingWorkersTable(WorkingWorkers:table)
```

**Parameter:** `WorkingWorkers` (table) designates the name of the table into which the working Workers will be written.

**Example:**

```simtalk
MyWorkerPool.getWorkingWorkersTable(MyWorkingWorkers)
```

---

## setWorkersToCreateTable [SimTalk]

Sets the name of the Workers to Create table for the Workers of the WorkerPool designated by `<Path>`.

**Remarks:** Plant Simulation always resolves relative paths in relation to the Frame in which the WorkerPool is inserted. If Plant Simulation cannot resolve a path in the Scope array during the simulation, it shows an error message and asks if you would like to stop the simulation. This also applies to the Home Location.

**Type:** Method

**Syntax:**

```
<Path>.setWorkersToCreateTable(WorkersToCreateTable:table/void)
```

**Parameter:** `WorkersToCreateTable` (table) designates the Workers to Create table. Enter the Names of the Workers to be created, the name of the Shift, their Amount, their Speed, their Efficiency, their Home Location, their Scope, and Additional Services into the table.

Specify `void` for the parameter to activate inheritance of the Workers to Create table in the WorkerPool instead of filling the table with the Workers that you entered into the table.

> **Note:** To apply the changes to the Workers to Create table to the simulation run, the change has to occur before the model is initialized.
>
> The name is not case-sensitive, just like the names of attributes and methods of the objects are not case-sensitive. To save memory and improve access speed, all places which are using such a case-insensitive string are pointing to the same string in main memory. The visible and unexpected result is that the first occurrence of the string defines how the string is written in terms of upper- and lower-casing. In SimTalk you can compare strings in a case-insensitive manner with the `~=` operator.

**Examples:**

```simtalk
MyWorkerPool.setWorkersToCreateTable(MyWorkersToCreateTable)
```

```simtalk
var rt: table                                // read the Workers to Create table
MyWorkerPool.getWorkersToCreateTableRow(rt)  // set the new amount
rt [2,1]:= AmountOfWorkers                   // name of a Variable
                                             // assign the Workers to Create table
                                             // to the WorkerPool
MyWorkerPool.setWorkersToCreateTable(rt)
```

---

## Read-Only Attributes of the WorkerPool

The WorkerPool provides read-only attributes. You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.
