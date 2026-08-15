# Converter — Attributes

This document summarizes the attributes of the **Converter** material flow object, based on the SimTalk reference. Each attribute describes its purpose, type, syntax, and assignment value, and keeps the original code examples.

The Converter provides:

- The attributes listed below.
- The *Attributes of All Objects*.
- The *Attributes of the Material Flow Objects*.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods** (context menu of the Class Library, or press F8 in the Frame).

You can set and get an attribute value using dialog windows or by assigning values:

```simtalk
Converter.Length := 11
print Converter.Length
posit := MyStation.Cont.XPos
```

---

## StatMovingLoadedTime [SimTalk]

Returns the total time during which the Converter designated by `<Path>` was raising or lowering itself and was conveying a MU.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatMovingLoadedTime → time`
- **Return Value:** data type `time`

```simtalk
print Converter.StatMovingLoadedTime
```

**See also:** Moving Time [statistics report], Attributes of the Converter

---

## AttributeType [SimTalk] - Converter

Sets the Attribute Type of the *Strategy > MU Attribute* of the Converter designated by `<Path>`.

**Remarks:** `AttributeType` sets the data type of the attribute that defines the material flow object to which the Converter moves the part.

- **Type:** Attribute
- **Syntax:** `<Path>.AttributeType:string`
- **Assignment Value:** string

```simtalk
Converter.AttributeType := "String"
```

**See also:** Attribute Type [drop-down list] - Converter

---

## AutomaticStop [SimTalk] - Converter

Automatically stops the Converter designated by `<Path>`. This means it sets its current speed to 0 if it does not transport a MU.

**Remarks:**

- This might be the case if it is empty or if it is blocked because a MU cannot leave it.
- If the speed of the Converter is 0, the Energy State changes to *operational*.

- **Type:** Attribute
- **Syntax:** `<Path>.AutomaticStop:boolean`
- **Assignment Value:** boolean

```simtalk
Converter.AutomaticStop := true
```

**See also:** Automatic Stop [check box] - Converter, Operational [energy]

---

## Capacity [SimTalk] - Converter

Sets the Capacity, i.e., the number of MUs which the Converter designated by `<Path>` can hold.

**Remarks:**

- The default value of `-1` stands for an infinite capacity.
- If the Converter conveys parts along the insertion direction, use the Capacity to allow the Converter to only convey this number of MUs at the same time.
- This only limits the possible number of MUs. If the Converter conveys parts, it still conveys a single MU at a time.

- **Type:** Attribute
- **Syntax:** `<Path>.Capacity:integer`
- **Watchable:** yes
- **Assignment Value:** integer

```simtalk
Converter.Capacity := 8
```

**See also:** Capacity [text box] - Converter

---

## DefaultExit [SimTalk]

Sets the Default Exit of the Converter designated by `<Path>`.

**Remarks:** The Default Exit applies to the Strategies *Default Exit*, *MU Attribute*, and *MU Name*. The figures illustrate the sides depending on the direction in which you inserted the Converter.

- **Type:** Attribute
- **Syntax:** `<Path>.DefaultExit:integer`
- **Assignment Value:** integer
  - `1` — laterally to the right in the insertion direction
  - `2` — against the insertion direction
  - `3` — laterally to the left in the insertion direction
  - `0` — along the insertion direction

```simtalk
MyConverter.DefaultExit := 2
```

**See also:** Default Exit [drop-down list], Strategy [drop-down list] - Converter

---

## ExitForMU [SimTalk]

Sets the side at which the next entering MU or the MU positioned at the converting point wants to exit the Converter designated by `<Path>`.

**Remarks:**

- You can only set `ExitForMU` in the Strategy method / `StrategyCtrl`.
- The MU cannot exit the Converter at the side at which it entered.

- **Type:** Attribute
- **Syntax:** `<Path>.ExitForMU:integer`
- **Assignment Value:** integer

```simtalk
param entranceNo: integer
if @.name = "C"
   ?.ExitForMU := 0 /* number of the exit of the converter*/
elseif @.name = "A"
   if entranceNo = 2
       ?.ExitForMU := 3
   else
       ?.ExitForMU := 0
   end
else
   if entranceNo = 2
       ?.ExitForMU := 1
   else
       ?.ExitForMU := 0
   end
end
?.ExitForMU := 1
```

**See also:** Strategy Method [Converter], StrategyCtrl [SimTalk] - Converter

---

## GoToDefaultPosition [SimTalk] - Converter

Rotates the Converter designated by `<Path>` back to its default position after the MU has left the Converter (`true`) or not (`false`).

**Remarks:** The Converter does not return to its default position if a MU is waiting that wants to enter laterally.

- **Type:** Attribute
- **Syntax:** `<Path>.GoToDefaultPosition:boolean`
- **Assignment Value:** boolean

```simtalk
MyConverter.GoToDefaultPosition := true
```

**See also:** Go to Default Position [check box] - Converter

---

## Length [SimTalk] - Converter

Sets the length of the Converter designated by `<Path>`.

**Remarks:** If the Converter is to convey parts perpendicular, it has to provide enough room for the length and the width of the MU to completely fit on the Converter, if the booking point is located on the converting point in the center of the Converter.

- **Type:** Attribute
- **Syntax:** `<Path>.Length:length`
- **Watchable:** yes
- **Assignment Value:** length
- **Note:** In SimTalk 2.0 you can specify the length units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in`. Type the unit directly after the value, without a separating blank space.

```simtalk
MyConverter.Length := 2m
```

**See also:** Length [text box] - Converter

---

## MovingTime [SimTalk] - Converter

Sets the Moving Time which the Converter designated by `<Path>` needs to lift the MU onto a different conveying level and to then lower itself and move back to the default position.

**Remarks:** If you use the formula distribution, you can enter a numeric expression or the name of a Method. Use the anonymous identifier `@` to access the MU for which the moving time applies.

- **Type:** Attribute
- **Syntax:** `<Path>.MovingTime:time`
- **Assignment Value:** time

```simtalk
MyConverter.MovingTime := 2
```

**See also:** Moving Time [drop-down list] - Converter, Formula [distribution]

---

## RelConvertingPointL [SimTalk]

Sets the relative position of the converting point along the length of the Converter designated by `<Path>`.

**Remarks:** The converting point is the point at which the Converter changes the conveying direction of the MUs it conveys.

- **Type:** Attribute
- **Syntax:** `<Path>.RelConvertingPointL:real`
- **Watchable:** yes
- **Assignment Value:** real (between `0.0` and `1.0`, denoting a position between 0 % and 100 %)

```simtalk
MyConverter.RelConvertingPointL := 0.2
```

**See also:** Relative Converting Point For Length

---

## RelConvertingPointW [SimTalk]

Sets the relative position of the converting point along the width of the Converter designated by `<Path>`.

**Remarks:** The converting point is the point at which the Converter changes the conveying direction of the MUs it conveys.

- **Type:** Attribute
- **Syntax:** `<Path>.RelConvertingPointW:real`
- **Watchable:** yes
- **Assignment Value:** real (between `0.0` and `1.0`, denoting a position between 0 % and 100 %)

```simtalk
MyConverter.RelConvertingPointW := 0.8
```

**See also:** Relative Converting Point For Width

---

## Speed [SimTalk] - Converter

Sets the Speed with which the Converter designated by `<Path>` conveys the MUs.

- **Type:** Attribute
- **Syntax:** `<Path>.Speed:speed`
- **Watchable:** yes
- **Assignment Value:** speed. Specify `-1` for an infinite speed.
- **Note:** In SimTalk 2.0 you can specify the speed units `mps`, `fps`, `kmh`, and `mph`. Type the unit directly after the number, without a separating blank space.

```simtalk
var len := 1.0ft
var s : speed := 10.5m / 1:30
var x : length := 3m

MyConverter.Speed := 2
```

**See also:** Speed [text box] - Converter

---

## Strategy [SimTalk] - Converter

Sets the Strategy of the Converter designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Strategy:string`
- **Assignment Value:** string. You can specify:
  - `"Default Exit"` — make all MUs exit through the Default Exit selected, to the successor attached to that exit.
  - `"Straight"` — convey the MU straight through to the next station.
  - `"Feed in"` — allow MUs from a branch line to enter the main line only when no part is located on the main line within the Free Space you enter.
  - `"MU Attribute"` — move the MU on according to a built-in or user-defined attribute of the MU. Set attributes with `setAttributeList`; set the default exit with `DefaultExit`.
  - `"MU Name"` — move the MU on according to its name. Set the default exit with `DefaultExit`; set attributes with `setAttributeList`.
  - `"Method"` — convey the MU according to the attribute `ExitForMU` entered into the Strategy Method. Set the control with `StrategyCtrl`.
  - `"Method at Converting Point"` — only determine the target at the converting point with `ExitForMU`, not already before the MU enters. Only available for a Capacity of 1. The MU always stops at the converting point, then Plant Simulation calls the method.

**Note:** As the Strategy Method is used for determining the side of the exit, it will not be called when the MU has a route and Automatic Routing is activated.

```simtalk
MyConverter.Strategy := "Straight"
```

**See also:** Strategy [drop-down list] - Converter, Strategy Method [Converter], Default Exit [drop-down list], Capacity [text box] - Converter, Automatic Routing [Part, Container], StrategyCtrl, ExitForMU, setAttributeList, DefaultExit

---

## StrategyCtrl [SimTalk] - Converter

Designates a Method object of the object designated by `<Path>`.

**Remarks:**

- Type in the source code that determines the side of the Converter at which the MU will exit.
- Plant Simulation calls the Strategy Method as soon as the MU wants to enter the Converter for the setting *Strategy > Method*.
- Plant Simulation calls the Strategy Method when the MU has reached the converting point for the setting *Strategy > Method at Converting Point*.
- You have to set the side with the attribute `ExitForMU`.
- The Strategy Method will not be called when the MU has a route and Automatic Routing is activated.

The default strategy method looks like this:

```simtalk
param entranceNo: integer
?.ExitForMU := 0 /* number of exit */
```

- **Type:** Attribute
- **Syntax:** `<Path>.StrategyCtrl:method`
- **Assignment Value:** method

```simtalk
param entranceNo: integer
if @.name = "C"
    ?.ExitForMU := 0 /* number of the exit of the converter*/
elseif @.name = "A"
    if entranceNo = 2
        ?.ExitForMU := 3
    else
        ?.ExitForMU := 0
    end
else
    if entranceNo = 2
        ?.ExitForMU := 1
    else
        ?.ExitForMU := 0
    end
end

MyConverter.StrategyCtrl := &myStrategyCtrl
```

**See also:** Strategy Method [Converter], Automatic Routing [Part, Container], ExitForMU [SimTalk]

---

## Width [SimTalk] - Converter

Sets the Width of the Converter designated by `<Path>`.

**Remarks:** If the Converter is to convey MUs perpendicular, it has to provide enough room for the Length and the Width of the MU to completely fit on the Converter, if the booking point is located on the converting point in the center of the Converter.

- **Type:** Attribute
- **Syntax:** `<Path>.Width:length`
- **Watchable:** yes
- **Assignment Value:** length
- **Note:** In SimTalk 2.0 you can specify the length units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in`.

```simtalk
MyConverter.Width := 2
```

**See also:** Width [text box] - Converter

---

## Turntable [object]

Use the object **Turntable** for modeling a rotating platform, which moves the part onto one of several connected material flow objects and/or turns it around.

**Description:**

- The Turntable has a capacity of one — only one part can be located on it at any one time.
- The length of the MU must not be longer than the Length of the Turntable itself.

The Turntable moves the part to its successors within the flow of materials like this:

1. The MU arrives at the exit of the predecessor and notifies the turntable that it wants to be rotated.
2. The turntable determines if it accepts the MU for rotating:
   - Without a Pull Control, the turntable is notified and accepts the MU.
   - With a Pull Control, the turntable executes it; when the MU is selected, it is rotated.
3. The turntable rotates to the respective predecessor, and the MU moves and drives onto it.
4. Once one of the following conditions is met, the turntable looks for the target station and starts rotating toward it:
   - The MU has completely entered the turntable.
   - The MU has reached the rotation point on the table.
   - The part is located in the center of the turntable (both ends of the part have the same distance from the ends of the turntable).
   - To rotate only when the MU reaches a user-defined sensor, select *User-defined with Sensor* and call the method `setDestination` in the Sensor Control.
5. For determining the target station, the turntable uses its default exit strategies or the Target Control. Within this Method you set the target station with `setDestination`.
