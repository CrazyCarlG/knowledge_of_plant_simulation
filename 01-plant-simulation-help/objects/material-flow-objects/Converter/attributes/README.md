# Converter — Attributes (Summary)

This document summarizes the attributes of the **Converter** material flow object from Plant Simulation.

The Converter provides:

- The attributes listed below.
- The *Attributes of All Objects*.
- The *Attributes of the Material Flow Objects*.

You can set and get an attribute value using dialog windows or by assigning values in SimTalk:

```simtalk
Converter.Length := 11
print Converter.Length
posit := MyStation.Cont.XPos
```

## Attribute Overview

| Attribute | Type | Syntax | Description |
|-----------|------|--------|-------------|
| `StatMovingLoadedTime` | Read-only | `<Path>.StatMovingLoadedTime → time` | Total time the Converter was raising/lowering itself while conveying a MU. |
| `AttributeType` | Attribute | `<Path>.AttributeType:string` | Data type of the *Strategy > MU Attribute* used to route parts. |
| `AutomaticStop` | Attribute | `<Path>.AutomaticStop:boolean` | Sets speed to 0 when not transporting a MU. |
| `Capacity` | Attribute (watchable) | `<Path>.Capacity:integer` | Number of MUs the Converter can hold; `-1` = infinite. |
| `DefaultExit` | Attribute | `<Path>.DefaultExit:integer` | Default exit side (0–3). |
| `ExitForMU` | Attribute | `<Path>.ExitForMU:integer` | Exit side for the next MU (set in Strategy Method). |
| `GoToDefaultPosition` | Attribute | `<Path>.GoToDefaultPosition:boolean` | Rotate back to default position after the MU leaves. |
| `Length` | Attribute (watchable) | `<Path>.Length:length` | Length of the Converter. |
| `MovingTime` | Attribute | `<Path>.MovingTime:time` | Time to lift the MU and return to default position. |
| `RelConvertingPointL` | Attribute (watchable) | `<Path>.RelConvertingPointL:real` | Relative converting point along length (0.0–1.0). |
| `RelConvertingPointW` | Attribute (watchable) | `<Path>.RelConvertingPointW:real` | Relative converting point along width (0.0–1.0). |
| `Speed` | Attribute (watchable) | `<Path>.Speed:speed` | Conveying speed; `-1` = infinite. |
| `Strategy` | Attribute | `<Path>.Strategy:string` | Routing strategy of the Converter. |
| `StrategyCtrl` | Attribute | `<Path>.StrategyCtrl:method` | Method that determines the exit side. |
| `Width` | Attribute (watchable) | `<Path>.Width:length` | Width of the Converter. |

## Attribute Details

### `StatMovingLoadedTime` (read-only)
Returns the total time the Converter was raising/lowering itself while conveying a MU. Data type `time`.

```simtalk
print Converter.StatMovingLoadedTime
```

### `AttributeType`
Sets the data type of the attribute that defines the material flow object to which the Converter moves the part.

```simtalk
Converter.AttributeType := "String"
```

### `AutomaticStop`
Automatically stops the Converter (sets speed to 0) when it is empty or blocked. When speed is 0, the Energy State changes to *operational*.

```simtalk
Converter.AutomaticStop := true
```

### `Capacity`
Sets how many MUs the Converter can hold. Default `-1` means infinite capacity. Limits the number of MUs but the Converter still conveys one MU at a time.

```simtalk
Converter.Capacity := 8
```

### `DefaultExit`
Sets the default exit side. Applies to the strategies *Default Exit*, *MU Attribute*, and *MU Name*. Values:
- `1` — laterally to the right in the insertion direction
- `2` — against the insertion direction
- `3` — laterally to the left in the insertion direction
- `0` — along the insertion direction

```simtalk
MyConverter.DefaultExit := 2
```

### `ExitForMU`
Sets the side at which the next MU wants to exit. Only settable in the Strategy Method / `StrategyCtrl`. The MU cannot exit on the side it entered.

```simtalk
param entranceNo: integer
if @.name = "C"
   ?.ExitForMU := 0
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
```

### `GoToDefaultPosition`
Rotates the Converter back to its default position after the MU leaves (`true`) or not (`false`). Does not return if a MU is waiting to enter laterally.

```simtalk
MyConverter.GoToDefaultPosition := true
```

### `Length`
Sets the length of the Converter. When conveying perpendicular, it must fit the MU's length and width if the booking point is at the converting point in the center. Units (`m`, `mm`, `km`, `cm`, `yd`, `ft`, `in`) are typed directly after the value.

```simtalk
MyConverter.Length := 2m
```

### `MovingTime`
Sets the time to lift the MU onto a different conveying level, lower itself, and return to default position. With a formula distribution, `@` accesses the MU.

```simtalk
MyConverter.MovingTime := 2
```

### `RelConvertingPointL` / `RelConvertingPointW`
Set the relative position of the converting point along the length/width (value between `0.0` and `1.0`, i.e. 0 % to 100 %). The converting point is where the Converter changes the conveying direction.

```simtalk
MyConverter.RelConvertingPointL := 0.2
MyConverter.RelConvertingPointW := 0.8
```

### `Speed`
Sets the conveying speed. Use `-1` for infinite speed. Units: `mps`, `fps`, `kmh`, `mph`.

```simtalk
MyConverter.Speed := 2
```

### `Strategy`
Sets the routing strategy. Possible values:
- `"Default Exit"` — all MUs exit through the selected Default Exit.
- `"Straight"` — convey the MU straight through to the next station.
- `"Feed in"` — branch-line MUs enter the main line only when no part is within the Free Space.
- `"MU Attribute"` — route by a built-in or user-defined MU attribute (use `setAttributeList`, `DefaultExit`).
- `"MU Name"` — route by the MU's name (use `DefaultExit`, `setAttributeList`).
- `"Method"` — route by `ExitForMU` in the Strategy Method (set control with `StrategyCtrl`).
- `"Method at Converting Point"` — determine the target only at the converting point (Capacity must be 1).

The Strategy Method is not called when the MU has a route and Automatic Routing is active.

```simtalk
MyConverter.Strategy := "Straight"
```

### `StrategyCtrl`
Designates the Method object that determines the exit side. Plant Simulation calls it when the MU wants to enter (*Method*) or reaches the converting point (*Method at Converting Point*). The side is set via `ExitForMU`. Default method:

```simtalk
param entranceNo: integer
?.ExitForMU := 0 /* number of exit */
```

```simtalk
MyConverter.StrategyCtrl := &myStrategyCtrl
```

### `Width`
Sets the width of the Converter. Same perpendicular-fit consideration as `Length`.

```simtalk
MyConverter.Width := 2
```

## Related Object: Turntable

The **Turntable** object models a rotating platform that moves a part onto one of several connected material flow objects and/or turns it around.

- Capacity of one — only one part at a time.
- The MU length must not exceed the Turntable length.

Conveying process:
1. The MU arrives at the predecessor's exit and notifies the turntable.
2. The turntable decides whether to accept it (with or without a Pull Control).
3. The turntable rotates to the predecessor and the MU drives onto it.
4. The turntable looks for the target and rotates toward it when: the MU fully entered, reached the rotation point, is centered, or (with *User-defined with Sensor*) `setDestination` is called in the Sensor Control.
5. The target station is determined by default exit strategies or the Target Control (`setDestination`).
