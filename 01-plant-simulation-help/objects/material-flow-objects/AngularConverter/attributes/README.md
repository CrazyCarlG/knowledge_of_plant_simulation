# AngularConverter Attributes

This README summarizes the attributes (and read-only attributes) of the **AngularConverter** material flow object in Plant Simulation.

## Overview

The AngularConverter provides:

- The attributes listed below.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all methods, read-only attributes, and attributes of the object, open **Show Attributes and Methods** (e.g. select it on the Class Library context menu, or press F8 / click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing the instance).

You can set and get an attribute's value either with dialog window controls (check boxes, text boxes, drop-down lists) or by assigning values in SimTalk:

```simtalk
MyAngularConverter.AutomaticStop := false   -- set
print MyAngularConverter.Pause              -- get
posit := MyStation.Cont.XPos
```

## Attributes

| Attribute | Type | Syntax | Watchable | Description |
|-----------|------|--------|-----------|-------------|
| **IsUp** | Read-only attribute | `<Path>.IsUp → boolean` | Yes | Returns `true` if a MU is located on the exit leg after the Moving Time has elapsed and the MU has exited while the Moving Time is still running, otherwise `false`. |
| **AutomaticStop** | Attribute | `<Path>.AutomaticStop:boolean` | — | Automatically stops the AngularConverter (sets current speed to 0) if it does not transport a part, e.g. when empty or blocked. If the speed is 0, the Energy State changes to operational. |
| **EntryLength** | Attribute | `<Path>.EntryLength:length` | Yes | Sets the length of the first leg, from the entry point to the point where the conveying direction switches. |
| **EntrySpeed** | Attribute | `<Path>.EntrySpeed:speed` | Yes | Sets the speed of the MU on the first leg, from the entry point to the point where the conveying direction switches. |
| **ExitLength** | Attribute | `<Path>.ExitLength:length` | Yes | Sets the length of the second leg, from the point where the conveying direction switches to the point where the MU exits. |
| **ExitSpeed** | Attribute | `<Path>.ExitSpeed:speed` | Yes | Sets the speed of the MU on the second leg, from the point where the conveying direction switches to the point where it exits. |
| **MovingTime** | Attribute | `<Path>.MovingTime:time` | — | Sets the time to switch from lengthwise to crosswise conveyance (and back). Triggered when the MU arrives at the corner, and again after it exits to return to the original position. |
| **Width** | Attribute | `<Path>.Width:length` | Yes | Sets the width of the AngularConverter. |

### Additional notes

- **MovingTime**: with the formula distribution you can enter a numeric expression or a Method name; the anonymous identifier `@` accesses the MU for which the moving time applies.
- **Width**: in SimTalk 2.0 you can specify length units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in` directly after the value (e.g. `10m`, `10.2m`).

## Converter Object Description

The **Converter** conveys a part either straight through, or lifts it onto a laterally moving transport level and conveys it left or right. It models materials handling equipment:

- A MU either passes straight through in the conveying direction, or is lifted by a lifting mechanism onto a laterally moving transport level and conveyed left or right.
- If the part enters on side 1 or 3, "straight" means it keeps its conveying direction and exits on the opposite side. The insertion direction for lateral movement is from side 3 to side 1 when the insertion direction is left-to-right (up-to-down).
- Query the entry side with the method `getObjectOfSide` [SimTalk].
- The Converter can only be connected to a single object per side; the numbers designate the exit side.
