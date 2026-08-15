# Turntable — Attributes

This document summarizes the attributes of the **Turntable** material flow object in Plant Simulation.

## Overview

The Turntable provides:
- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:
- Select *Show Attributes and Methods* on the context menu of the Class Library to show them for the selected **Class** (general description).
- Press **F8** or click *Show Attributes and Methods* on the Home ribbon tab of the Frame into which you inserted an instance to show them for the selected **Instance** (general description).

You can set an attribute's value and get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

```simtalk
-- To set the value of an attribute
MyTurntable.GoToDefaultPosition := false

-- To get the value of an attribute
print MyTurntable.GoToDefaultPosition
posit := MyStation.Cont.XPos
```

---

## StatRotationLoadedTime [SimTalk]

Returns the total time during which the Turntable designated by `<Path>` was rotating with a MU being located on the table.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatRotationLoadedTime → time`
- **Return Value:** The return value has the data type `time`.

**Example**

```simtalk
print MyTurntable.StatRotationLoadedTime
```

**See also:** Statistics report, Rotation Time

---

## AutomaticStop [SimTalk]

Automatically stops the Turntable designated by `<Path>`. This means that it sets the current speed to 0 if it does not transport a MU. This might, for example, be the case if it is empty or if it is blocked because a MU cannot leave it.

- **Remarks:** If the speed of the Turntable is 0, the Energy State changes to *operational*.
- **Type:** Attribute
- **Syntax:** `<Path>.AutomaticStop:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example**

```simtalk
MyTurntable.AutomaticStop := true
```

**See also:** Automatic Stop [check box], Operational [energy]

---

## DefaultAngle [SimTalk]

Sets the rotation angle in degrees to which the side of the end point of the Turntable designated by `<Path>` rotates.

- **Remarks:** `DefaultAngle` applies when you set *Go to Default Position* / `GoToDefaultPosition` to `true`. To rotate the Turntable to the side on which the start point is located, add 180° to this angle.
- **Type:** Attribute
- **Syntax:** `<Path>.DefaultAngle:real`
- **Assignment Value:** You can assign a value of data type `real`.

**Example**

```simtalk
MyTurntable.DefaultAngle := 5
```

**See also:** Default Angle [text box], Go to Default Position [check box]

---

## GoToDefaultPosition [SimTalk]

Returns the Turntable designated by `<Path>` to its default position (`true`) or not (`false`).

- **Remarks:** `GoToDefaultPosition` applies when the part has left the Turntable and if no new part is ready to be rotated.
- **Note:** If you set the attribute to `true`, the Turntable uses the attribute `DefaultAngle` when you reset the model. The attribute `DefaultAngle` sets the actual angle.
- **Type:** Attribute
- **Syntax:** `<Path>.GoToDefaultPosition:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example**

```simtalk
MyTurntable.GoToDefaultPosition := true
```

**See also:** Go to Default Position [check box], Default Angle [text box]

---

## Length [SimTalk]

Sets the Length of the Turntable designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Length:length`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type `length`.
- **Note:** In SimTalk 2.0 you can specify the length units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in`. Type in the unit directly after the values, without a separating blank space, for example `10m` or `10.2m`. You can specify the unit for floating point values and for integer values.

**Example**

```simtalk
MyTurntable.Length := 10.0m
```

**See also:** Length [text box]

---

## MURotationAttribute [SimTalk]

Sets the name of the user-defined attribute of the MU which triggers its rotation on the Turntable designated by `<Path>`.

- **Remarks:** `MURotationAttribute` can be an attribute of data type `boolean` or a Method, which returns a value of data type `boolean`. `MURotationAttribute` will only be evaluated when you select *Any* as the Side in the Exit Angle Table.
- **Type:** Attribute
- **Syntax:** `<Path>.MURotationAttribute:string`
- **Assignment Value:** You can assign a value of data type `string`.

**Example**

```simtalk
MyTurntable.MURotationAttribute := "MyRotationAttribute"
```

**See also:** Exit Angle Table, MU Leaves Backwards Depends On

---

## RotateWhen [SimTalk]

Sets when the Turntable designated by `<Path>` rotates toward its target station.

- **Type:** Attribute
- **Syntax:** `<Path>.RotateWhen:string`
- **Assignment Value:** You can assign a value of data type `string`. You can specify:
  - `"Completely entered"` — if the MU has completely entered the Turntable.
  - `"Rotation point reached"` — if the MU has reached the center of rotation on the table.
  - `"Centered"` — if both ends of the MU have the same distance from the ends of the turntable.
  - `"User-defined with Sensor"` — the Turntable does not rotate automatically, but only when the MU has reached a user-defined sensor. In the Sensor Control, you have to tell the Turntable to call the method `setDestination`.

**Example**

```simtalk
MyTurntable.RotateWhen := "completely entered"
```

**See also:** Strategy [drop-down list] - Turnplate, Rotation Point [text box]

---

## RotationPoint [SimTalk]

Sets the position of the point around which the Turntable designated by `<Path>` rotates.

- **Type:** Attribute
- **Syntax:** `<Path>.RotationPoint:length`
- **Assignment Value:** You can assign a value of data type `length`. Specify a value between `0` and the length of the Turntable. `0` designates the point at which you start inserting the Turntable.

**Example**

```simtalk
MyTurntable.RotationPoint := 4
```

**See also:** Rotation Point [text box]

---

## RotationTimePer90Degrees [SimTalk]

Sets the time it takes the Turntable designated by `<Path>` to rotate by 90 degrees.

- **Type:** Attribute
- **Syntax:** `<Path>.RotationTimePer90Degrees:time`
- **Assignment Value:** You can assign a value of data type `time`.

**Example**

```simtalk
MyTurntable.RotationTimePer90Degrees := 2
```

**See also:** Rotation Time per 90° [text box]

---

## Speed [SimTalk]

Sets the speed with which the Turntable designated by `<Path>` rotates.

- **Type:** Attribute
- **Syntax:** `<Path>.Speed:speed`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type `speed`. Specify `-1` for an infinite speed.
- **Note:** In SimTalk 2.0 you can specify the speed units `mps`, `fps`, `kmh`, and `mph`. Type in the unit directly after the number, without a separating blank space, for example `100kmh` or `100.5kmh`.

```simtalk
var len := 1.0ft
var s : speed := 10.5m / 1:30
var x : length := 3m
```

**Example**

```simtalk
MyTurntable.Speed := 1.5
```

**See also:** Conveyor Speed [text box]

---

## TargetCtrl [SimTalk]

Designates a Method object of the object designated by `<Path>`.

- **Remarks:** Plant Simulation calls the Method as soon as the MU has completely moved onto the Turntable or has reached the center of rotation. In the Target Control you determine the successor to which the Turntable designated by `<Path>` moves the MU. As opposed to the Exit Control, the MU is not ready to exit the object yet. You have to set the target object in the method `setDestination`.
- **Type:** Attribute
- **Syntax:** `<Path>.TargetCtrl:method`
- **Assignment Value:** You can assign a value of data type `method`.

**Examples**

```simtalk
if @.Name = "PartA" 
-- the identifier "@" points to the MU, the part in our case, 
-- which triggers the call of the current method in a control 
    ?.setDestination(ConveyorPartA)
    -- the identifier "?" points to the object which
    -- calls the method, the turntable in our case
else
    ?.setDestination(ConveyorPartB)
end
```

```simtalk
MyTurntable.TargetCtrl := &myTargetControl
```

**See also:** Target Control [Turntable]

---

## Width [SimTalk]

Sets the width of the Turntable designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Width:length`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type `length`.
- **Note:** In SimTalk 2.0 you can specify the length units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in`. Type in the unit directly after the values, without a separating blank space, for example `10m` or `10.2m`. You can specify the unit for floating point values and for integer values.

**Example**

```simtalk
MyTurntable.Width := 2 -- meters
```

**See also:** Width [text box]

---

# Turnplate [object]

Use the object **Turnplate** for modeling a rotating platform, which rotates the loaded parts and ensures the uniform orientation of the leaving parts.

## Description

A typical example is in the package shipping industry where all packages have to be rotated to a uniform direction so that a scanner can automatically read the bar code holding the address information.

- The Turnplate has a capacity of one, i.e., only one MU can be located on it at any one time.
- The MU moves onto the Turnplate and the Turnplate starts rotating when the booking point of the MU has reached the center of rotation of the Turnplate.
- When the rotation is finished, the MU exits the Turnplate.
- The conveying direction on the Turnplate is unidirectional, i.e., the MU cannot be conveyed forward and then backward.
- The length of the MU must not be longer than the Length of the Turnplate itself.
- The center of rotation is by default located in the center of the Turnplate.
- The rotation takes up a certain amount of time. You can type in the rotation time per rotation steps of 90 degrees. If you type in a rotation time of 0, the MU is rotated instantaneously without using up any time at all.
- The rotation angle that you type in should be a multiple of 90 degrees. If you type in an angle other than that, Plant Simulation rounds this angle to the next angle that is divisible by 90. You can also type in a value greater than 360 degrees as long as it is divisible by 90. This way the Turnplate can rotate the MU several times to simulate packing machines, such as shrink wrappers, etc.
- By default, the Turnplate rotates 90 degrees clockwise.
- After the turnplate has rotated the MU and it has left it, the Turnplate returns to its starting position.
- You can select different configurations for the Turnplate on the tab *Appearance* of the Length-oriented Objects.
