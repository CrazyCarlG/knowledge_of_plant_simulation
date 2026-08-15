# Attributes of the AngularConverter

This document summarizes the attributes (and read-only attributes) of the AngularConverter material flow object in Plant Simulation.

## Overview

The AngularConverter provides:

- The attributes listed in the table of contents.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods** (e.g. select it on the Class Library context menu, or press F8 / click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing the instance).

You can set an attribute's value and get its value, either with the dialog window controls (check boxes, text boxes, drop-down lists) or by assigning values to the respective attributes.

- To set an attribute value:
  ```simtalk
  MyAngularConverter.AutomaticStop := false
  ```
- To get an attribute value:
  ```simtalk
  print MyAngularConverter.Pause
  posit := MyStation.Cont.XPos
  ```

---

## IsUp [SimTalk] — read-only attribute

Returns whether a MU is located on the exit leg of the AngularConverter designated by `<Path>` after the Moving Time has elapsed and after the MU has exited while the Moving Time is still running (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.IsUp → boolean`
- **Watchable:** The read-only attribute is watchable.
- **Return Value:** boolean

**Example**
```simtalk
print MyAngularConverter.IsUp
```

---

## AutomaticStop [SimTalk]

Automatically stops the AngularConverter designated by `<Path>`. This sets its current speed to 0 if it does not transport a part.

**Remarks**

This might be the case if it is empty or if it is blocked because a MU cannot leave it. If the speed of the AngularConverter is 0, the Energy State changes to operational.

- **Type:** Attribute
- **Syntax:** `<Path>.AutomaticStop:boolean`
- **Assignment Value:** boolean

**Example**
```simtalk
MyAngularConverter.AutomaticStop := true
```

**See also:** Automatic Stop [check box], Operational [energy]

---

## EntryLength [SimTalk]

Sets the length of the first leg of the AngularConverter designated by `<Path>`.

**Remarks**

The EntryLength covers the distance from the entry point to the point at which the AngularConverter switches the conveying direction.

- **Type:** Attribute
- **Syntax:** `<Path>.EntryLength:length`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** length

**Example**
```simtalk
MyAngularConverter.EntryLength := 2
```

**See also:** Entry Length [text box], ExitLength [SimTalk]

---

## EntrySpeed [SimTalk]

Sets the speed with which the MU moves on the AngularConverter designated by `<Path>` from the entry point to the point at which the AngularConverter switches the conveying direction.

- **Type:** Attribute
- **Syntax:** `<Path>.EntrySpeed:speed`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** speed

**Example**
```simtalk
MyAngularConverter.EntrySpeed := 2
```

**See also:** Entry Speed [text box], ExitSpeed [SimTalk]

---

## ExitLength [SimTalk]

Sets the length of the second leg of the AngularConverter designated by `<Path>`.

**Remarks**

The ExitLength covers the distance from the point at which the AngularConverter switches the conveying direction to the point at which the MU exits the object.

- **Type:** Attribute
- **Syntax:** `<Path>.ExitLength:length`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** length

**Example**
```simtalk
MyAngularConverter.ExitLength := 2
```

**See also:** Exit Length [text box], EntryLength [SimTalk]

---

## ExitSpeed [SimTalk]

Sets the speed with which the MU moves on the AngularConverter designated by `<Path>` from the point at which the AngularConverter switches the conveying direction to the point at which it exits the object.

- **Type:** Attribute
- **Syntax:** `<Path>.ExitSpeed:speed`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** speed

**Example**
```simtalk
MyAngularConverter.ExitSpeed := 2
```

**See also:** Exit Speed [text box], EntrySpeed [SimTalk]

---

## MovingTime [SimTalk]

Sets the time it takes the AngularConverter designated by `<Path>` to switch from lengthwise to crosswise conveyance and vice versa.

**Remarks**

The Moving Time is triggered when the MU arrives at the corner at which the AngularConverter switches conveyance. It is triggered again when it has exited the AngularConverter altogether, to set it back to its original position.

If you use the formula distribution, you can enter a numeric expression or the name of a Method. You can use the anonymous identifier `@` to access the MU for which the moving time applies.

- **Type:** Attribute
- **Syntax:** `<Path>.MovingTime:time`
- **Assignment Value:** time

**Example**
```simtalk
MyAngularConverter.MovingTime := 20
```

**See also:** Moving Time [drop-down list], Formula [distribution]

---

## Width [SimTalk]

Sets the Width of the AngularConverter designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Width:length`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** length

**Note**

In SimTalk 2.0 you can specify the length units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in`. Type the unit directly after the value, without a separating blank space, for example `10m` or `10.2m`. You can specify the unit for floating point values and for integer values.

**Example**
```simtalk
MyAngularConverter.Width := 4
```

**See also:** Width [text box], Converter [object]

---

## Converter [object] — Image / Description

Use the object Converter for conveying a part either straight through, or for lifting it onto a laterally moving transport level and then conveying it to the left- or right-hand side.

Use the Converter to model materials handling equipment. If the MU moves onto the Converter it either:

- passes straight through in the conveying direction, or
- is lifted onto a laterally moving transport level by a lifting mechanism and then conveyed laterally to the left or laterally to the right.

If the part enters on side 1 or 3, straight means that the part keeps its conveying direction and exits on the opposite side. The insertion direction for this lateral movement is from side 3 to side 1 when the insertion direction of the Converter is from left to right (i.e. up to down).

You can query the side on which the part enters the Converter with the method `getObjectOfSide` [SimTalk].

The Converter can only be connected to a single object per side. The numbers designate the side of the Converter at which the MU exits. The figures in the original documentation illustrate the sides depending on the direction in which you inserted the Converter into your simulation model.
