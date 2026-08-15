# Methods of the Source

The Source provides:

- The methods listed in the table of contents to the left.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class (general description).
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance (general description).

## Syntax line

An example of the Syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

## creationTable [SimTalk]

Returns the Creation Table of the Source designated by `<Path>` and writes it into a table.

**Type:** Method

**Syntax:**

```
<Path>.creationTable(CreationTable:table)
```

**Parameter:** The parameter `CreationTable` of data type `table` either designates a local variable, a table cell of data type `table`, or the path to a DataTable.

**Example:**

```
MySource.creationTable(myEvaluationTable)
MySource.creationTable(MyDataTable[2,8])
```

**See also:**

- Creation Table [Source]

## getCurrentOrderTableRow [SimTalk]

Returns the row number of the table according to which the Source designated by `<Path>` currently produces parts.

**Remarks:** `getCurrentOrderTableRow` only returns the table row for MU Selection > Sequence Cyclical, Sequence, Random, and Percentage, which produce parts according to a DataTable. In all other cases the return value always is 0.

**Syntax:**

```
<Path>.getCurrentOrderTableRow -> integer
```

**Return Value:** The return value has the data type `integer`.

**Example:**

```
print MySource.getCurrentOrderTableRow
```

**See also:**

- MU selection [drop-down list] > Sequence Cyclical [MU selection]
- Sequence [MU selection]
- Random [MU selection]
- Percentage [MU selection]

## orderParts [SimTalk]

Orders parts from the Source designated by `<Path>`.

**Type:** Method

**Syntax:**

```
<Path>.orderParts(PartType:object, Amount:integer, Destination:object[, Name:string])
```

**Parameters:** You can specify the following parameters:

- The parameter `PartType` of data type `object` designates the path to the part type that is going to be ordered.
- The parameter `Amount` of data type `integer` designates the amount of parts that is going to be ordered.
- The parameter `Destination` of data type `object` designates the object that orders the parts. The destination can be any material flow object.
  - If the Destination is a Supermarket, Plant Simulation increases the counter of the amount of the remaining ordered parts, compare the column Waiting in the Configuration Table of the Store.
- The optional parameter `Name` of data type `string` designates the name of the part type that is going to be ordered. If you do not enter anything, Plant Simulation uses the name of the object which you entered as the `PartType`.

**Examples:**

```
MySource.orderParts(.UserObjects.MyPart, 12, MyStation, "MyPart")
```

```
param partName:string, minStock:integer, maxStock:integer, currentStock:integer, orderedParts:integer
var amount:integer := maxStock-currentStock-orderedParts
if amount > 0 then
   Source.orderParts(@, amount, ?, partName)
end
```

**See also:**

- MU selection [drop-down list] > Order Controlled [MU selection]
- Configuration [button]

## Read-Only Attributes of the Source

The Source provides:

- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class (general description).
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance (general description).

To query the value of a read-only attribute, you might, for example, type:

```
print MySource.UUID
```
