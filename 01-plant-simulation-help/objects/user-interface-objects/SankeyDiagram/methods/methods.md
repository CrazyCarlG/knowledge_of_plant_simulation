# Methods of the SankeyDiagram

The SankeyDiagram provides the methods listed in the table of contents for accessing it, along with the **Methods of All Objects**.

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the members of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the members of the selected Instance.

## Reading the Syntax line

An example syntax line looks like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier + data type of each parameter) is listed in parentheses. `(Parameter:string)` designates a parameter of data type `string`. Instead of a constant, you can use a variable of the required type or a method that returns the required type.
- Optional parameters are listed within brackets, e.g. `[,Parameter:boolean]`.
- If a parameter has a default value, the signature shows it after the parameter, e.g. `:= false`.
- If the method has a return value, its data type appears after the arrow `->`, e.g. `→ boolean`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

---

## getPartFlowData [SimTalk]

Writes the flows that the SankeyDiagram designated by `<Path>` collected during the simulation to the designated DataTable.

### Remarks

The SankeyDiagram collects the number of parts which move between point-oriented objects or along length-oriented objects. It does not consider the direction nor the sequence of the movements of the parts, and they cannot be traced back from the returned data.

### Type

Method

### Syntax

```
<Path>.getPartFlowData(DataTable:table)
```

### Parameter

The parameter `DataTable` of data type `table` designates the table into which Plant Simulation writes the data of the flows.

### Example

```
MySankeyDiagram.getPartFlowData(MyDataTable)
```

---

## update [SimTalk] - SankeyDiagram

Refreshes the displayed SankeyDiagram designated by `<Path>` with the current values.

### Type

Method

### Syntax

```
<Path>.update
```

### Example

```
MySankeyDiagram.update
```

### See also

- Update [in Frame]

---

## Read-Only Attributes of the SankeyDiagram

The SankeyDiagram provides the **Read-Only Attributes of All Objects**.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, the **Statistics** tab).
