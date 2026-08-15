# Methods of the Converter

The Converter provides:

- The methods listed below.
- The _Methods of Curved Objects.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class, or press the **F8** key / click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which an instance was inserted.

## Syntax line example

An example of the Syntax line of an individual method might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. `(Parameter:string)`, for example, designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

---

## getAttributeList [SimTalk] - Converter

Returns the target list for the **Strategy > MU Attribute** of the Converter designated by `<Path>`.

**Remarks**

The Attribute List contains the names of the Attributes of the MU, their Values, and on Which Side they exit. The numbers designate the side of the Converter at which the MU exits. For the **Strategy > MU Name** it contains the names of the MUs and on which side they exit.

**Type:** Method

**Syntax**

```
<Path>.getAttributeList(AttributeList:table)
```

**Parameter**

The parameter `AttributeList` of data type table designates the name of the list.

**Example**

```
Converter.getAttributeList(MyAttributesList)
```

**See also:** Open List [button] - Converter, Strategy [drop-down list] - Converter

---

## getEntranceSide [SimTalk]

Returns the side of the Converter from which the last part moved onto the Converter designated by `<Path>`.

**Remarks**

The numbers designate the side of the Converter at which the MU enters.

**Type:** Method

**Syntax**

```
<Path>.getEntranceSide -> integer
```

**Return Value**

The return value has the data type integer. It is `-1` if no part moved onto the Converter.

**Example**

```
print MyConverter.getEntranceSide
```

---

## getObjectOfSide [SimTalk]

Returns the object on the specified side of the Converter designated by `<Path>`.

**Remarks**

The numbers designate the side of the Converter at which the MU enters.

**Type:** Method

**Syntax**

```
<Path>.getObjectOfSide(side:integer) -> object
```

**Return Value**

The return value has the data type object. It is `VOID` if the specified side is not occupied.

**Example**

```
print Converter.getobjectOfSide(0) -- returns .Models.Model2.Connector3
print Converter.getobjectOfSide(1) -- returns VOID
print Converter.getobjectOfSide(2) -- returns .Models.Model2.Connector2
print Converter.getobjectOfSide(3) -- returns VOID
```

---

## getSideOfConnector [SimTalk]

Returns the side at which the designated Connector is attached to the Converter designated by `<Path>`.

**Remarks**

The numbers designate the side of the Converter at which the MU exits.

**Type:** Method

**Syntax**

```
<Path>.getSideOfConnector(Connector:object) → integer
```

**Parameter**

The parameter `Connector` of data type object designates the Connector.

**Return Value**

The return value has the data type integer.

**Example**

```
var side: integer
side := Converter.getSideOfConnector(Connector)
side := Converter.getSideOfConnector(Connector1)
```

---

## getSuccessorAtExit [SimTalk]

Returns the successor object, which is connected to the Converter designated by `<Path>` at the side designated by the parameter.

**Type:** Method

**Syntax**

```
<Path>.getSuccessorAtExit(Side:integer) → object
```

**Parameter**

The parameter `Side` of data type integer designates the side. The numbers designate the side of the Converter at which the MU exits.

**Return Value**

The return value has the data type object.

**Example**

```
MyObject := ?.getSuccessorAtExit(1)
```

---

## setAttributeList [SimTalk] - Converter

Sets the target list for the **Strategy > MU Attribute** of the Converter designated by `<Path>`.

**Remarks**

The Attribute List contains the names of the Attributes of the MU, the Values of the attributes, and on Which Side it exits. The numbers designate the side of the Converter at which the part exits. For the **Strategy > MU Name** you can enter the Names of the parts and on Which Side they exit.

**Type:** Method

**Syntax**

```
<Path>.setAttributeList(AttributeList:table)
```

**Parameter**

The parameter `AttributeList` of data type table designates the path to a list or a variable of the same data type. Plant Simulation then copies the contents of the passed list to the target list of the Converter.

**Example**

```
Converter.setAttributeList(MyAttributes)
```

**See also:** Open List [button] - Converter, Data Held in Tabular Form in Attributes [material flow objects], Strategy [drop-down list] - Converter

---

# Read-Only Attributes of the Converter

The Converter provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.
