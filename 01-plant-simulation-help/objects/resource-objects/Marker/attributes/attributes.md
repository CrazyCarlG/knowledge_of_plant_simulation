# Attributes of the Marker

## Overview

The **Marker** provides:

- The attributes listed in the table of contents.
- The [Attributes of All Objects](#).

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows or by assigning values to the respective attributes.

To query the value of a read-only attribute:

```simtalk
print MyMarker.UUID
```

To set the value of an attribute:

```simtalk
MyMarker.UseRotationOfMarker := true
```

To get the value of an attribute:

```simtalk
print MyMarker.UseRotationOfMarker
```

---

## ArrivalCtrl [SimTalk]

Designates a Method object of the object designated by `<Path>`.

**Remarks**

Plant Simulation runs the Arrival Control as soon as the Transporter driving freely within the area arrives at the Marker designated by `<Path>`.

For an omnidirectional Marker, Plant Simulation runs the control once the Transporter driving freely within the area arrives at the half-way point of the curvature/fillet at the Marker.

If you did not specify a Method, the value of the attribute is `VOID`.

**Type**: Attribute

**Syntax**

```simtalk
<Path>.ArrivalCtrl:method
```

**Assignment Value**

You can assign a value of data type `method`.

**Example**

```simtalk
MyMarker.ArrivalCtrl := &myMethod
```

**See also**: Arrival Control [Marker]

---

## UseRotationOfMarker [SimTalk]

Sets if the AGV uses the rotation of the Marker designated by `<Path>` when driving to its destination (`true`) or not (`false`).

**Type**: Attribute

**Syntax**

```simtalk
<Path>.UseRotationOfMarker:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

**Example**

```simtalk
MyMarker.UseRotationOfMarker := true
```

**See also**: Amount [text box] - AGVPool
