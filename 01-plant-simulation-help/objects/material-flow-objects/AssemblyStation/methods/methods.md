# Methods of the AssemblyStation

The AssemblyStation provides:

- The methods listed below.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods** (shown using the example of the object Station):

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Syntax line conventions

An example of the Syntax line of the individual methods:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method (identifier and data type of each parameter) is listed in parentheses. `(Parameter:string)` designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows it after the parameter, e.g. `:= false`.
- If the method has a return value, the signature shows its data type after the arrow `->`, e.g. `→ boolean`.

---

## Methods

### musToBeDeleted

Returns the contents of the table **MUs to Be Deleted** of the AssemblyStation designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.musToBeDeleted([Table:table]) → any`

**Parameter:** The optional parameter `Table` of data type `table` designates the name of the table.

**Return Value:** The return value has the data type `any`. If you specify the optional parameter, the return value has the data type `boolean`. Do not specify the optional parameter to return an array containing the MUs that are to be deleted.

**Example:**

```
MyAssembly.musToBeDeleted
MyAssembly.musToBeDeleted(myEvalTable)
```

**See also:** `MUs To Be Deleted`, `muToBeDeleted`, `NumMUsToBeDeleted`

---

### muToBeDeleted

Returns the specified MU from the table **MUs to Be Deleted** of the AssemblyStation designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.muToBeDeleted(NumberOfTheMU:integer) → object`

**Parameter:** The parameter `NumberOfTheMU` of data type `integer` designates the number of the MU in the table.

**Return Value:** The return value has the data type `object`.

**Example:**

```
for var i := 1 to MyAssembly.NumMUsToBeDeleted
   print MyAssembly.muToBeDeleted(i)
next
```

**See also:** `MUs To Be Deleted`, `musToBeDeleted`, `NumMUsToBeDeleted`

---

### statWaitingTimePerPredecessor

Returns the summed-up waiting times for the mounting parts of the designated predecessor of the AssemblyStation designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.statWaitingTimePerPredecessor(Predecessor:integer) → time`

**Parameter:** The parameter `Predecessor` of data type `integer` designates the number of the predecessor.

> **Note:** The return value for the predecessor number along which the main part arrives at the AssemblyStation is always 0.

**Return Value:** The return value has the data type `time`.

**Example:**

```
var i : integer
for var i := 1 to MyAssembly.NumPred
    print MyAssembly.statWaitingTimePerPredecessor(i)
next
```

**See also:** `Waiting [state, material flow objects]`, `Tab Statistics [AssemblyStation] > Waiting Times`

---

### statWaitingTimeTable

Returns the table that contains the summed-up waiting times for the mounting parts of all predecessors of the AssemblyStation designated by `<Path>`.

**Remarks:**

- Plant Simulation only shows Waiting Times for mounting parts. The Waiting Time for the main part is always 0.
- Plant Simulation only shows Waiting Times when you selected **None** or **Predecessors** as the Assembly Table.
- In the example below, the main part arrives along the connector from `SourceMainParts`. As only waiting times for mounting parts are shown, the first row shows 0.

- **Type:** Method
- **Syntax:** `<Path>.statWaitingTimeTable(WaitingTimes:table) → boolean`

**Parameter:** The parameter `WaitingTimes` of data type `table` designates the name of the table.

**Return Value:** The return value has the data type `boolean`. Returns `false` for the settings `MU Types` and `Depends on Main MU`.

**Examples:**

```
var myWaitingTimesTable: table
MyAssembly.statWaitingTimeTable(myWaitingTimesTable)
print MyAssembly.statWaitingTimeTable(myWaitingTimesTable)
```

**See also:** `Waiting [state, material flow objects]`, `Tab Statistics [AssemblyStation] > Waiting Times`

---

## Read-Only Attributes of the AssemblyStation

The AssemblyStation provides:

- The read-only attributes listed in the table of contents (to the left in the Help).
- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.
