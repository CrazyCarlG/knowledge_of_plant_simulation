# Connector — Attributes

## SuccLane [SimTalk] — Connector

Returns the lane of a `TwoLaneTrack` whose starting point is connected with the `Connector` designated by `<Connector-Path>`.

**Remarks**

- The successor lane is the lane to which the Connector leads in the forward direction.
- If the successor is not a `TwoLaneTrack`, `SuccLane` returns the successor object.

**Type**

- Read-only attribute

**Syntax**

```
<Connector-Path>.SuccLane → any
```

**Return Value**

- Data type `any`.

**Example**

```simtalk
print Connector2.SuccLane
```

---

## Attributes of the Connector

The Connector provides:

- The attributes listed in the table of contents.
- The attributes of all objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

You can:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set and get an attribute value either with the check boxes, text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute:

```simtalk
MyStation.succConnector(3).Color := makeRGBValue(0,10,100)
```

- To get the value of an attribute:

```simtalk
print MyStation.succConnector(3).Width
posit := MyStation.Cont.XPos
```

`<Connector-Path>` designates a valid path to a Connector for which the method applies, either an absolute path to the Connector in the Class Library (`.Materialflow.Connector`) or an access via the methods `predConnector` or `succConnector`.

---

## Color [SimTalk] — Connector

Sets the color of the Connector designated by `<Connector-Path>`.

**Remarks**

- Set the RGB values of the color with the method `makeRGBValue`. If you assign an invalid value to the attribute `Color`, Plant Simulation retains the current color.
- Connectors in 3D use the color you define here as well. The default RGB color `7, 0, 0` of the Connector in Plant Simulation is interpreted as white in 3D. All other colors are applied as you define them in Plant Simulation.

**Type**

- Attribute

**Syntax**

```
<Connector-Path>.Color:integer
```

**Assignment Value**

- You can assign a value of data type `integer`.

**Example**

```simtalk
MyStation.succConnector(3).Color := makeRGBValue(100,100,100)
MyStation.succConnector(3).Color := 6579300 // is the same as the color above
```

**See also**

- `makeRGBValue [SimTalk]`
- `Color [Connector]`

---

## Width [SimTalk] — Connector

Sets the width of the Connector designated by `<Connector-Path>`.

**Remarks**

- The `Width` is a value of data type `real`.
- You can reduce the default width, which corresponds to `0` or `1`, with values between `0` and `1`, to a fraction of that.

**Type**

- Attribute

**Syntax**

```
<Connector-Path>.Width:real
```

**Assignment Value**

- You can assign a value of data type `real`.
- You can specify a number between `1` and `100` pixels:
  - `1` stands for a line weight of 1 pixel in a Frame window with a zoom factor of 100 percent.
  - `0` stands for a Connector width of 1 pixel no matter if the Frame window is zoomed or not.
  - `-1` makes the Connector invisible.

| Width | Meaning |
|-------|---------|
| -1    | Invisible |
| 0     | 1 pixel regardless of zoom |
| 1     | 1 pixel at 100% zoom |
| 5     | 5 pixels at 100% zoom |

**Examples**

```simtalk
MyStation.succConnector(3).Width := 2
.Materialflow.Connector.Width := 0.5
```

**See also**

- `Width [text box] - Connector`

---

## Related: EventController [object]

Use the object `EventController` for coordinating, synchronizing, and controlling the events taking place during a simulation run.

**Note:** You cannot change the name of the EventController.

You can start, stop, and reset the simulation with the EventController. Plant Simulation is a discrete event-oriented simulation system that shows the state changes of the model components at certain points in time, not continually over time. When a part enters a processing station, for example a Station, Plant Simulation computes the time it takes to cover it and enters that time and that event into the List of scheduled events of the EventController.

The EventController moves along the timeline like the play-back head of a video player, and interprets messages relating to the events the objects execute. After a certain simulation time, for example the Processing Time, has elapsed, the EventController arrives at the marker which has been set when the part entered the station. This marker denotes that the processing time has elapsed and that an `Out` event is pending. The EventController notifies the Station that has to process the `Out` event and moves the part on to the succeeding object in the flow of materials. Plant Simulation repeats this process cyclically for all MUs located in the simulation model.
