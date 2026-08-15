# Methods of the AGVPool

The AGVPool provides:

- The methods listed below.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Understanding the Syntax line

An example of the Syntax line of an individual method might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

---

## getAssignedAGV [SimTalk]

Returns the AGV designated by the number in the AGVPool designated by `<Path>`.

**Type:** Method

**Syntax:**

```
<Path>.getAssignedAGV(No:integer) -> object
```

**Parameter**

The parameter `No` of data type integer designates the number of the AGV that is assigned.

**Return Value**

The return value has the data type object.

**Example**

```
print MyAGVPool.getAssignedAGV(2)
-- might, for example, return .UserObjects.MyAGV:2
```

**See also:** Assigned AGVs [AGVPool]

---

## getAssignedAGVsTable [SimTalk]

Returns the table containing the assigned AGVs of the AGVPool designated by `<Path>`.

**Type:** Method

**Syntax:**

```
<Path>.getAssignedAGVsTable([AssignedAGVs:table]) -> any
```

**Parameter**

The optional parameter `AssignedAGVs` of data type table designates the name of the table into which the AGVs will be written.

If you do not specify the optional parameter, Plant Simulation returns an array with the assigned automated guided vehicles (AGVs).

**Return Value**

The return value has the data type any.

**Examples**

```
MyAGVPool.getAssignedAGVsTable(myAssignedAGVsTable) // writes the AGVs into the specified table
MyAGVPool.getAssignedAGVsTable // writes the AGVs to an array
```

**See also:** Assigned AGVs [AGVPool]

---

## getIdleAGV [SimTalk]

Returns an AGV of the AGVPool designated by `<Path>` for which the attribute `IsIdle` has the value `true`.

**Remarks**

`getIdleAGV` also sets the attribute `IsIdle` of the returned AGV to `false`. You yourself are responsible to set `IsIdle` to `true` again if the AGV is to be available again, normally when the AGV has reached the end of the route.

**Type:** Method

**Syntax:**

```
<Path>.getIdleAGV → object
```

**Return Value**

The return value has the data type object.

`VOID` if no idle AGV is available.

**Example**

```
waituntil AGVPool.NumIdleAGVs > 0
var AGV := AGVPool.getIdleAGV
```

**See also:**

- IsIdle [SimTalk] - Transporter
- NumIdleAGVs [SimTalk]
- Fine-position an AGV
- Read-Only Attributes of the AGVPool
