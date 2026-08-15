# Methods of the Turnplate

The Turnplate provides:

- The methods listed in the table of contents to the left.
- The Methods of Curved Objects.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

## Syntax line conventions

An example of the syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature, consisting of the identifier and the data type of the parameter, is listed in parentheses. `(Parameter:string)` designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

---

## getAttributeList [SimTalk] - Turnplate

Returns the attribute list of the Turnplate designated by `<Path>`.

**Remarks**

- Contains the name of the Attribute of the MU, the Value of the attribute, and the rotation Angle for the Strategy > MU Attribute.
- Contains the Name of the attribute of the part and the rotation Angle for the Strategy > MU Name.

**Type:** Method

**Syntax**

```
<Path>.getAttributeList(Attributes:table)
```

**Parameter**

The parameter `Attributes` of data type `table` designates the name of the list.

**Example**

```
MyTurnplate.getAttributeList(MyAttributesList)
```

**See also:** Strategy [drop-down list] - Turnplate; Open List [Turnplate]; Data Held in Tabular Form in Attributes [material flow objects]

---

## rotatePart [SimTalk]

Rotates the MU on the Turnplate designated by `<Path>` by the specified angle.

**Type:** Method

**Syntax**

```
<Path>.rotatePart(Angle:integer)
```

**Parameter**

The parameter `Angle` of data type `integer` designates the angle. This angle has to be a positive or a negative multiple of 90.

**Example**

```
?.rotatePart(180)
```

**See also:** Strategy Method [Turnplate]

---

## setAttributeList [SimTalk] - Turnplate

Sets the attribute list of the Turnplate designated by `<Path>`. The attribute list sets the MU that leaves the Turnplate.

**Remarks**

- For the Strategy > MU Attribute you can specify the name of the Attribute of the MU, its Value and the rotation Angle.
- For the Strategy > MU Name you can specify the Name of the MU and the rotation Angle.

**Type:** Method

**Syntax**

```
<Path>.setAttributeList(Attributes:table)
```

**Parameter**

The parameter `Attributes` of data type `table` designates the path to a list or a variable of the same data type. Plant Simulation then copies the contents of the passed list to the attribute list of the Turnplate.

**Example**

```
MyTurnplate.setAttributeList(MyAttributes)
```

**See also:** Strategy [drop-down list] - Turnplate; Open List [Turnplate]; Data Held in Tabular Form in Attributes [material flow objects]

---

## Read-Only Attributes of the Turnplate

The Turnplate provides:

- The read-only attributes listed in the table of contents to the left.
- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.
