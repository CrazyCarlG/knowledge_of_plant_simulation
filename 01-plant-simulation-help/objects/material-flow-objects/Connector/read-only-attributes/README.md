# Read-Only Attributes of the Connector — Summary

This directory documents the read-only attributes of the Plant Simulation **Connector** material flow object. The Connector provides the read-only attributes listed below, plus the `_Read-Only Attributes of All Objects` and the `Read-Only Attributes of the Material Flow Objects`.

Read-only attributes can be **queried** but not **set**: Plant Simulation computes the value at the point in time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window:

- In the Class Library context menu: **Show Attributes and Methods** shows them for the selected Class.
- Press **F8**, or click **Show Attributes and Methods** on the Home ribbon tab of the Frame, to show them for the selected Instance.

## Read-Only Attributes

### PredInterface
Returns the direct predecessor object of the Connector.

- **Remarks:** If the preceding object is a Frame, `PredInterface` returns the Interface object (the method `pred` returns the Frame instead).
- **Syntax:** `<Connector-Path>.PredInterface → object`
- **Return value:** data type `object`
- **Example:** `print Connector2.predinterface`

### PredLane
Returns the lane of a TwoLaneTrack whose end point is connected with the Connector.

- **Remarks:** The predecessor lane leads to the Connector in the forward direction. If the predecessor is not a TwoLaneTrack, `PredLane` returns the predecessor object.
- **Syntax:** `<Connector-Path>.PredLane → any`
- **Return value:** data type `any`
- **Example:** `print Connector2.PredLane`

### SuccInterface
Returns the direct successor object of the Connector.

- **Remarks:** If the succeeding object is a Frame, `SuccInterface` returns the Interface object (the method `succ` returns the Frame instead).
- **Syntax:** `<Connector-Path>.SuccInterface → object`
- **Return value:** data type `object`
- **Example:** `print connector2.SuccInterface`

### SuccLane
Returns the lane of a TwoLaneTrack whose starting point is connected with the Connector.

- **Remarks:** The successor lane is the lane to which the Connector leads in the forward direction. If the successor is not a TwoLaneTrack, `SuccLane` returns the successor object.
- **Syntax:** `<Connector-Path>.SuccLane → any`
- **Return value:** data type `any`
- **Example:** `print Connector2.SuccLane`

## Related Method Reference

The Connector's `connect` method creates a Connector between two objects (returns the created Connector, data type `object`).

- The optional parameter `SideOfConverterEnd` (integer) is required only when inserting a Connector between two Converters.
- `SideOfConverterStart` designates the side of the source Converter; `SideOfConverterEnd` designates the side of the target Converter at which the Connector ends.

**Examples:**

```simtalk
.Materialflow.Connector.connect(Station, Store)
.Materialflow.Connector.connect(Station, Interface3)
.Materialflow.Connector.connect(T1, T2)
// connects the exit of T1 with the entrance of T2
.Materialflow.Connector.connect(T1.A, T2.A)
// connects the exit of T1 with the entrance of T2
.Materialflow.Connector.connect(T1.A, T2.B)
// connects the exit of T1 with the exit of T2
.Materialflow.Connector.connect(T1.B, T2.A)
// connects the entrance of T1 with the entrance of T2
.MaterialFlow.Connector.connect("TwoLaneTrack1.B", "TwoLaneTrack2.A")
// connects lanes of two-laned tracks
```

## Files in This Directory

- `read-only-attributes.md` — formatted reference of the Connector's read-only attributes.
- `read-only-attributes.txtx` — plain-text source export of the same reference content.
