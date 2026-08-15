# Read-Only Attributes of the Turnplate

## Parameter / Attributes (table)

The parameter `Attributes` of data type `table` designates the path to a list or a variable of the same data type. Plant Simulation then copies the contents of the passed list to the attribute list of the Turnplate.

**Example**

```simtalk
MyTurnplate.setAttributeList(MyAttributes)
```

**SimTalk**

```simtalk
getAttributeList [SimTalk] - Turnplate
```

**See also**

- Strategy [drop-down list] - Turnplate
- Open List [Turnplate]
- Data Held in Tabular Form in Attributes [material flow objects]

---

## Overview

The Turnplate provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

To view read-only attributes and methods:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Turnplate.StatRotationLoadedPortion
```

---

## StatRotationLoadedPortion [SimTalk] - Turnplate

Returns the portion of the statistics collection period during which the Turnplate designated by `<Path>` was rotating while a MU was located on the plate.

**Syntax**

```simtalk
<Path>.StatRotationLoadedPortion → real
```

**Return Value**

The return value has the data type `real`.

**Example**

```simtalk
print MyTurnplate.StatRotationLoadedPortion
```

**See also**

- Tab Statistics [Turnplate]
- Statistics report, Rotation Time

---

## StatRotationLoadedTime [SimTalk] - Turnplate

Returns the total time during which the Turnplate designated by `<Path>` was rotating while a MU was located on the plate.

**Syntax**

```simtalk
<Path>.StatRotationLoadedTime → time
```

**Return Value**

The return value has the data type `time`.

**Example**

```simtalk
print MyTurnplate.StatRotationLoadedTime
```

**See also**

- Statistics report, Rotation Time

---

## Attributes of the Turnplate

The Turnplate provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.
