# Length-oriented Objects & Profiles

SimTalk provides attributes, methods, and functions for defining **length-oriented objects** in 3D and for accessing **extrusion profiles**.

You can view and access these attributes and methods by clicking **Auto Complete** on the **Edit** ribbon tab of the **Method Editor**.

---

## `_3D.StoreType`

Sets the type of the Store designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>._3D.StoreType:string`
- **Assignment value:** string

You can specify: `"Floorspace"`, `"Rack with round posts"`, `"Rack with square posts"`, `"Floorspace (dynamic)"`, `"Rack with round posts (dynamic)"`, or `"Rack with square posts (dynamic)"`.

```simtalk
Store3._3D.StoreType := "Rack with round posts (dynamic)"
Store3._3D.Gap := 0.1
Store3._3D.FloorThickness := 0.15
Store3._3D.GroundClearance := 0.3
```

**See also:** Edit 3D Properties [dialog] > Appearance of the Store > Type [drop-down list] - Store; createRack [SimTalk]

---

## `_3D.AniGravityMode`

Activates **Gravity Mode** of the length-oriented object designated by `<Path>` (`true`) or deactivates it (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>._3D.AniGravityMode:boolean`
- **Assignment value:** boolean

**Remarks**

- Only applies to length-oriented objects; especially helpful for suspension tracks, etc.
- Gravity Mode only affects **automatic animations** (animations for which you did not specify an animation path).
- On a suspension track the part is always placed perpendicular to the floor in Gravity Mode, either hanging from a rail on the ceiling or standing up on a rail on the floor.

```simtalk
MyConveyor._3D.AniGravityMode := true
```

**See also:** Gravity Mode

---

## `_3D.AnimationOffset`

Sets the **Animation Offset** of the length-oriented object designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>._3D.AnimationOffset:length[3]`
- **Assignment value:** array of `length` with three values

The values set the offset of the animation path to the surface of the object along the X-, Y-, and Z-directions.

```simtalk
MyConveyor._3D.AnimationOffset := [0m, 0m, 1m]
```

**See also:** Animation Offset

---

## `_3D.AniSmoothRotation`

Activates **Smooth Rotation** of the length-oriented object designated by `<Path>` (`true`) or deactivates it (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>._3D.AniSmoothRotation:boolean`
- **Assignment value:** boolean

**Remarks**

- Only applies to length-oriented objects; especially helpful for suspension tracks, etc.
- Smooth Rotation only affects **automatic animations** (animations without a specified animation path).
- If the object animates its MUs using a user-defined Animation Path Type > Lines, Smooth Rotation specifies whether the part slowly changes its rotation around the anchor points (as on a Station, `true`) or abruptly changes its orientation (as at a corner on a Conveyor with the standard MU animation, `false`).

```simtalk
MyConveyor._3D.AniSmoothRotation := true
```

**See also:** Smooth Rotation

---

## `_3D.BaseHeight` - 3D

Sets the **Base Height** of the length-oriented object designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>._3D.BaseHeight:length`
- **Assignment value:** length

**Remarks**

- The Base Height sets the distance between the insertion height (z-coordinate) of the length-oriented object and the height of a segment whose ΔZ equals 0.
- The Base Height can be **inherited** (defined once in the class instead of per instance).
- The z-coordinate defines the floor of the installation; the base height defines the distance of the legs from the floor. Changing ΔZ in the Segments Table adds an additional offset.

```simtalk
MyConveyor._3D.BaseHeight := 3
print MyConveyor._3D.BaseHeight
```

**See also:** Base Height [tab Appearance]; `_3D.getExtSegments`; `_3D.setExtSegments`; Insert Curved and Straight Segments > Anchor Point Height

---

## `_3D.ExtConfiguration`

Sets the **extrusion configuration** of the length-oriented object designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>._3D.ExtConfiguration:table`
- **Assignment value:** table containing the extrusion configuration

### Parameters of the Extrusion Configuration

- **Index Name:** Name of the extrusion group, entered only once per group in the first column (column 0).
- **Extrusion Profile:** The subtable `[2 x number of points]` (opened by double-clicking the cell) specifies the profile to be extruded. Define the values so they match a width of 1 meter.
- **Configuration Type:** See the table below.
- **Start Offset:** Offset of the start reference in the extrusion direction.
- **End Offset:** Offset of the end reference in the extrusion direction.
- **Repetition Interval:** For configuration types 14–19, 22, and 23, `0` means the extrusion is generated once at the object's start point; a value greater than 0 generates the extrusion every that many meters along `<Path>` (e.g., `0.5` = every 50 cm). For other values this is meaningless and only `0` is accepted.
- **Graphic Group ID:** Default `0`; a value between 0 and 10 generates additional graphic groups into which the marked extrusions are placed (e.g., used by the Fluid object Pipe).
- **Material:** Subtable (opened by double-clicking the cell) where you can set:
  - Diffuse Color [MUs] — see `makeRGBValue`
  - Ambient Color [MUs]
  - Specular Color [MUs]
  - Emissive Color [MUs]
  - Transparency [MUs]
  - Shininess [MUs]

### Configuration Type values

| Name / Value for Assignment | Description |
|---|---|
| Path, z max, Move abs / `0` | Extrude once along the path with z as defined in the anchors; the distance from the edge remains fixed when changing the width. |
| Path, z max, Move rel / `1` | Extrude once along the path with z as defined in the anchors; pin the profile base point to its relative position when changing the width. |
| Path, z max, Scale x / `2` | Extrude once along the path with z as defined in the anchors; scale in the x-direction when changing the width. |
| Path, z max, Scale xy / `3` | Extrude once along the path with z as defined in the anchors; scale in the x- and y-directions when changing the width. |
| Path, Floor, Move abs / `4` | Extrude once along the path with z = 0.0; the distance from the edge remains fixed when changing the width. |
| Path, Floor, Move rel / `5` | Extrude once along the path with z = 0.0; pin the profile base point to its relative position when changing the width. |
| Path, Floor, Scale x / `6` | Extrude once along the path with z = 0.0; scale in the x-direction when changing the width. |
| Path, Floor, Scale xy / `7` | Extrude once along the path with z = 0.0; scale in the x- and y-directions when changing the width. |
| Horizontal, Anchors, z max, Move / `8` | Extrude horizontally for every anchor point with z as defined in the anchors; pin to the borders when changing the width. The graphic tilts according to the incline. |
| Horizontal, Anchors, z max, Scale / `9` | Extrude horizontally for every anchor point with z as defined in the anchors; pin to the center when changing the width. The graphic tilts according to the incline. |
| Horizontal, Anchors, z 1/5, Move / `10` | Extrude horizontally for every anchor point with z = 1/5 of the anchor point height; pin to the borders when changing the width. |
| Horizontal, Anchors, z 1/5, Scale / `11` | Extrude horizontally for every anchor point with z = 1/5 of the anchor point height; pin to the center when changing the width. |
| Horizontal, Anchors, Floor, Move / `12` | Extrude horizontally for every anchor point with z = 0.0; pin to the borders when changing the width. |
| Horizontal, Anchors, Floor, Scale / `13` | Extrude horizontally for every anchor point with z = 0.0; pin to the center when changing the width. |
| Horizontal, Interval, z max, Move / `14` | Extrude horizontally with a fixed interval with z as defined in the anchors; pin to the borders when changing the width. The graphic tilts according to the incline. |
| Horizontal, Interval, z max, Scale / `15` | Extrude horizontally with a fixed interval with z as defined in the anchors; pin to the center when changing the width. The graphic tilts according to the incline. |
| Horizontal, Interval, z 1/5, Move / `16` | Extrude horizontally with a fixed interval with z = 1/5 of the anchor point height; pin to the borders when changing the width. |
| Horizontal, Interval, z 1/5, Scale / `17` | Extrude horizontally with a fixed interval with z = 1/5 of the anchor point height; pin to the center when changing the width. |
| Horizontal, Interval, Floor, Move / `18` | Extrude horizontally with a fixed interval with z = 0.0; pin to the borders when changing the width. |
| Horizontal, Interval, Floor, Scale / `19` | Extrude horizontally with a fixed interval with z = 0.0; pin to the center when changing the width. |
| Vertical, Floor, Anchors, Move / `20` | Extrude vertically for every anchor point from the path anchor to the floor; pin to the borders when changing the width. |
| Vertical, Floor, Anchors, Fix / `21` | Extrude vertically for every anchor point from the path anchor to the floor; pin to the center when changing the width. |
| Vertical, Interval, Move / `22` | Extrude vertically with a fixed interval from the path anchor to the floor; pin to the borders when changing the width. |
| Vertical, Interval, Fix / `23` | Extrude vertically with a fixed interval from the path anchor to the floor; pin to the center when changing the width. |
| Forward, z max, Anchors, Move abs / `24` | Repeatedly extrude a small segment in the path direction for each anchor point; the distance from the borders remains fixed when changing the width. |
| Forward, z max, Anchors, Move rel / `25` | Repeatedly extrude a small segment in the path direction for each anchor point; pin the base point of the profile to its relative position when changing the width. |
| Forward, z max, Anchors, Fix / `26` | Repeatedly extrude a small segment in the path direction for each anchor point; the distance from the center remains fixed when changing the width. |
| Forward, z max, Interval, Move abs / `27` | Repeatedly extrude a small segment in the path direction with a fixed interval; the distance from the borders remains fixed when changing the width. |
| Forward, z max, Interval, Move rel / `28` | Repeatedly extrude a small segment in the path direction with a fixed interval; pin the base point of the profile to its relative position when changing the width. |
| Forward, z max, Interval, Fix / `29` | Repeatedly extrude a small segment in the path direction with a fixed interval; the distance from the center remains fixed when changing the width. |
| Vertical, z max, Anchors, Move / `30` | Extrude vertically for each anchor point at the height of the path anchor point; pin to the borders when changing the width. |
| Vertical, z max, Anchors, Fix / `31` | Extrude vertically for each anchor point at the height of the path anchor point; pin to the center when changing the width. |
| Vertical, z max, Interval, Move / `32` | Extrude vertically with a fixed interval at the height of the path anchor point; pin to the borders when changing the width. |
| Vertical, z max, Interval, Fix / `33` | Extrude vertically with a fixed interval at the height of the path anchor point; pin to the center when changing the width. |
| Forward, Floor, Anchors, Move abs / `34` | Repeatedly extrude a small segment in the path direction for each anchor point with z = 0.0; the distance from the borders remains fixed when changing the width. |
| Forward, Floor, Anchors, Move rel / `35` | Repeatedly extrude a small segment in the path direction for each anchor point with z = 0.0; pin the base point of the profile to its relative position when changing the width. |
| Forward, Floor, Anchors, Fix / `36` | Repeatedly extrude a small segment in the path direction for each anchor point with z = 0.0; the distance from the center remains fixed when changing the width. |
| Forward, Floor, Interval, Move abs / `37` | Repeatedly extrude a small segment in the path direction with a fixed interval with z = 0.0; the distance from the borders remains fixed when changing the width. |
| Forward, Floor, Interval, Move rel / `38` | Repeatedly extrude a small segment in the path direction with a fixed interval with z = 0.0; pin the base point of the profile to its relative position when changing the width. |
| Forward, Floor, Interval, Fix / `39` | Repeatedly extrude a small segment in the path direction with a fixed interval with z = 0.0; the distance from the center remains fixed when changing the width. |
| Vertical, Ceiling, Anchors, Move / `40` | Extrude vertically for each anchor point from the path anchor point to the ceiling; pin to the borders when changing the width. The end offset denotes the ceiling height. |
| Vertical, Ceiling, Anchors, Fix / `41` | Extrude vertically for each anchor point from the path anchor point to the ceiling; pin to the center when changing the width. The end offset denotes the ceiling height. |
| Vertical, Ceiling, Interval, Move / `42` | Extrude vertically with a fixed interval from the path anchor point to the ceiling; pin to the borders when changing the width. The end offset denotes the ceiling height. |
| Vertical, Ceiling, Interval, Fix / `43` | Extrude vertically with a fixed interval from the path anchor point to the ceiling; pin to the center when changing the width. The end offset denotes the ceiling height. |
| Horizontal, Anchors, z max Gr, Move / `44` | Extrude horizontally for each anchor point with z as defined in the anchor points; pin to the borders when changing the width. |
| Horizontal, Anchors, z max Gr, Scale / `45` | Extrude horizontally for each anchor point with z as defined in the anchor points; pin to the center when changing the width. |
| Horizontal, Interval, z max Gr, Move / `46` | Extrude horizontally with a fixed interval with z as defined in the anchor points; pin to the borders when changing the width. |
| Horizontal, Interval, z max Gr, Scale / `47` | Extrude horizontally with a fixed interval with z as defined in the anchor points; pin to the center when changing the width. |

### Notes

This attribute returns a **copy** of the values. Compare these examples:

```simtalk
Conveyor._3D.ExtConfiguration := MyExtrusionConfigurationTable      // assigns a new value
MyExtrusionConfigurationTable := Conveyor._3D.ExtConfiguration      // reads a value
```

This example has correct-looking syntax but has **no effect**:

```simtalk
Conveyor._3D.ExtConfiguration[2,1] := 2
// does not assign the subtable to the first cell of the attribute
```

To get the desired result, enter:

```simtalk
var extConfTable := Conveyor._3D.ExtConfiguration
extConfTable[2,1] := 2
Conveyor._3D.ExtConfiguration := extConfTable
```

To copy `_3D.ExtConfiguration` to a DataTable in a Frame, use format + content copying (not a simple `:=` assignment):

```simtalk
var MyExtrusionConfigurationTable : table := Conveyor._3D.ExtConfiguration
MyDataTable.delete
MyExtrusionConfigurationTable.copyFormatTo(MyDataTable)
MyExtrusionConfigurationTable.copyRangeTo({0,0}..{*,*}, MyDataTable, 0, 0)
```

**See also:** Appearance of the Length-oriented Objects in the dialog Edit 3D Properties; User-defined [Conveyor type]; `makeRGBValue`

---

## `_3D.getExtSegments`

Gets the segments table of the length-oriented object designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>._3D.getExtSegments(Table:table)`
- **Parameter:** `Table` (data type `table`) — the table into which Plant Simulation writes the settings of the segments table.

```simtalk
MyConveyor._3D.getExtSegments(extSegmentsTable)
```

**See also:** `_3D.setExtSegments`; Length [SimTalk] - animatable object; Segments [tab Appearance]; Reuse the Segments of a Length-oriented Object

---

## `_3D.setExtSegments`

Sets the segments table of the length-oriented object designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.3D.setExtSegments(Table:table)`
- **Parameter:** `Table` (data type `table`) — the table from which Plant Simulation imports the settings of the segments table.

```simtalk
MyConveyor._3D.setExtSegments(extSegmentsTable)
```

**See also:** `_3D.getExtSegments`; Length [SimTalk] - animatable object; Segments [tab Appearance]; Reuse the Segments of a Length-oriented Object

---

## `_3D.ShowMaterialFlowDirection`

Shows the material flow direction arrow of the length-oriented object designated by `<Path>` (`true`) along the insertion direction or hides it (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>._3D.ShowMaterialFlowDirection:boolean`
- **Assignment value:** boolean

**Remarks:** Only applies to simulation objects and animatable objects that are length-oriented and have a meaningful material flow direction. The FootPath does not show the direction arrow despite being length-oriented, because it has no meaningful material flow direction.

```simtalk
MyConveyor._3D.ShowMaterialFlowDirection := false
```

**See also:** Show Material Flow Direction [check box]

---

## `_3D.ShowSensors`

Shows (`true`) or hides (`false`) the sensors of the length-oriented object designated by `<Path>` in 3D.

- **Type:** Attribute
- **Syntax:** `<Path>._3D.ShowSensors:boolean`
- **Assignment value:** boolean

```simtalk
MyConveyor._3D.ShowSensors := false
```

**See also:** Sensors [general description]; Show Sensors [check box]

---

## `_3D.Width`

Sets the width of the length-oriented object designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>._3D.Width:real`
- **Assignment value:** real

```simtalk
Conveyor._3D.Width := 2
```

**See also:** Width [tab Appearance] in the dialog Edit 3D Properties

---

# Accessing Functions of the Extrusion Profile

SimTalk provides the following functions for accessing an **extrusion profile**.

---

## `F3DgenerateEllipse`

Creates a two-dimensional **ellipse** profile usable in a user-defined extrusion configuration.

- **Type:** Method
- **Syntax:** `F3DgenerateEllipse(BasePoint:length[2], Width:length, Height:length, CurvePrecision:length)`

**Parameters**

- `BasePoint` — array of `length` with two values setting the base point of the ellipse profile.
- `Width` — `length`; sets its width.
- `Height` — `length`; sets its height.
- `CurvePrecision` — `length`; sets the sampling accuracy for the generated ellipse.

```simtalk
var profile : any := F3DgenerateEllipse([2.6,4.5], 4, 4, 0.1)
// returns a two-dimensional array containing the values defining a profile
// to be used for an extrusion profile
```

**See also:** `_3D.ExtConfiguration`; `_3D.InheritGraphics`; `createExtrusionGraphic`; `F3DgenerateHollowEllipse`; `F3DgenerateHollowRectangle`; `F3DgenerateRectangle`

---

## `F3DgenerateHollowEllipse`

Creates a two-dimensional **hollow ellipse** profile usable in a user-defined extrusion configuration.

- **Type:** Method
- **Syntax:** `F3DgenerateHollowEllipse(BasePoint:length[2], Width:length, Height:length, BarThickness:length, CurvePrecision:length)`

**Parameters**

- `BasePoint` — array of `length` with two values setting the base point of the hollow ellipse profile.
- `Width` — `length`; sets its width.
- `Height` — `length`; sets its height.
- `BarThickness` — `length`; sets the thickness of the bar.
- `CurvePrecision` — `length`; sets the sampling accuracy for the generated ellipse.

```simtalk
// The following code visualizes the generated profile using cubes
var points := F3DgenerateHollowEllipse([0,0], 4, 2, 0.1, 0.1)
for var i := 1 to points.ydim
    var Cube := _3D.getGraphic("deco").createCuboid([0.03, 0.03, 0.01])
    Cube.Position := [points[1,i], points[2,i], 0.0]
    Cube.MaterialActive := true
    Cube.MaterialDiffuseColor :=  makeRGBValue(0,255,0)
next
```

**See also:** `_3D.InheritGraphics`; `_3D.ExtConfiguration`; `createExtrusionGraphic`; `F3DgenerateEllipse`; `F3DgenerateHollowRectangle`; `F3DgenerateRectangle`

---

## `F3DgenerateHollowRectangle`

Creates a two-dimensional **hollow rectangular** profile usable in a user-defined extrusion configuration.

- **Type:** Method
- **Syntax:** `F3DgenerateHollowRectangle(BasePoint:length[2], Width:length, Height:length, BarThickness:length)`

**Parameters**

- `BasePoint` — array of `length` with two values setting the base point of the hollow rectangular profile.
- `Width` — `length`; sets its width.
- `Height` — `length`; sets its height.
- `BarThickness` — `length`; sets the thickness of the bar.

```simtalk
var profile : any := F3DgenerateHollowRectangle([2.6,4.5], 4, 2, 3, 0.1)
// returns a two-dimensional array containing the values defining a profile
// to be used for an extrusion profile
```

**See also:** `_3D.ExtConfiguration`; `_3D.InheritGraphics`; `createExtrusionGraphic`; `F3DgenerateEllipse`; `F3DgenerateHollowEllipse`; `F3DgenerateRectangle`

---

## `F3DgenerateRectangle`

Creates a two-dimensional **rectangular** profile usable in a user-defined extrusion configuration.

- **Type:** Method
- **Syntax:** `F3DgenerateRectangle(BasePoint:length[2], Width:length, Height:length)`

**Parameters**

- `BasePoint` — array of `length` with two values setting the base point of the rectangular profile.
- `Width` — `length`; sets its width.
- `Height` — `length`; sets its height.

```simtalk
var profile : any := F3DgenerateRectangle([2.6,4.5],4, 2)
// returns a two-dimensional array containing the values defining a profile
// to be used for an extrusion profile
```

**See also:** `_3D.InheritGraphics`; `createExtrusionGraphic`; `F3DgenerateEllipse`; `F3DgenerateHollowEllipse`; `F3DgenerateHollowRectangle`; `_3D.ExtConfiguration`
