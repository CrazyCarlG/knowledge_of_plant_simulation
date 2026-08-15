# Methods of the DismantleStation

The DismantleStation provides:

- The methods listed in the table of contents.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which an instance was inserted to show them for the selected Instance.

## Syntax line example

An example of the Syntax line of an individual method might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. `[,Parameter:boolean]`, for example, means that you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

---

## leavingMU [SimTalk]

Returns the specified MU from the table **Exiting MUs** of the DismantleStation designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.leavingMU(MU:integer) → object`
- **Parameter:** The parameter `MU` of data type `integer` designates the MU.
- **Return Value:** The return value has the data type `object`.

**Example:**

```simtalk
for var i := 1 to MyDismantleStation.NumLeavingMU 
   print MyDismantleStation.leavingMU(i)
next
```

**See also:** Exiting MUs, leavingMUs [SimTalk]

---

## leavingMUs [SimTalk]

Returns the contents of the table of the **Exiting MUs** of the DismantleStation designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.leavingMUs([MUsTable:table]) → any`
- **Parameter:** The optional parameter `MUsTable` of data type `table` designates the name of the table.
- **Return Value:** The return value has the data type `any`. It is an array containing the MUs that wanted to leave the DismantleStation if you do not specify the optional parameter.

**Example:**

```simtalk
MyDismantleStation.leavingMUs(myEvalTable)
MyDismantleStation.leavingMUs
```

**See also:** Exiting MUs, leavingMU [SimTalk]

---

## statBlockingTimePerSuccessor [SimTalk]

Returns the blocking time in relation to the specified successor from the table **Blocking Times** of the DismantleStation designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.statBlockingTimePerSuccessor(Successor:integer) → time`
- **Parameter:** The parameter `Successor` of data type `integer` designates the successor.
- **Return Value:** The return value has the data type `time`.

**Example:**

```simtalk
for var i := 1 to MyDismantleStation.NumSucc 
    print MyDismantleStation.statBlockingTimePerSuccessor(i)
next
```

**See also:** Tab Statistics [DismantleStation], statBlockingTimePerSuccessor [SimTalk]

---

## statBlockingTimeTable [SimTalk]

Returns the contents of the table **Blocking Times** of the DismantleStation designated by `<Path>` and writes it into the table.

- **Type:** Method
- **Syntax:** `<Path>.statBlockingTimeTable(BlockingTimes:table) → boolean`
- **Parameter:** The parameter `BlockingTimes` of data type `table` designates the name of the table.
- **Return Value:** The return value has the data type `boolean`.

**Example:**

```simtalk
var myBlockingTimesTable: table
MyDismantleStation.statBlockingTimeTable(myBlockingTimesTable)
```

**See also:** Tab Statistics [DismantleStation]

---

## Read-Only Attributes of the DismantleStation

The DismantleStation provides:

- The read-only attributes listed in the table of contents.
- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.
