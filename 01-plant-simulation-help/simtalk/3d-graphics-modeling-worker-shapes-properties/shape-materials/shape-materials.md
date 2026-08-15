# Shape Materials — Graphic Shape Properties (SimTalk)

Source: `shape-materials.txtx` — Siemens Plant Simulation Help (pages 12-1010 to 12-1191).

This reference documents the SimTalk attributes for setting properties of **Graphic Shapes**. SimTalk provides these attributes to control the appearance and geometry of 3D graphics created via `Insert Shape` (e.g. Factory Walls, Fence, Mezzanine, Rack, Stairs, Dimensioning).

## Accessing Properties of Graphic Shapes

SimTalk provides the attributes listed in the table of contents for setting properties of Graphic Shapes.

See also: Insert Shape, `_Accessing Methods of Graphic Shapes`, `_Accessing Attributes of Graphic Shapes`.

---

## Common conventions

Most material attributes follow a shared pattern. Each material group exposes seven attributes:

| Attribute | Data type | Meaning |
|---|---|---|
| `...MaterialActive` | `boolean` | Activates/deactivates the material |
| `...MaterialAmbientColor` | `integer` | Ambient color (`makeRGBValue`) |
| `...MaterialDiffuseColor` | `integer` | Diffuse color (`makeRGBValue`) |
| `...MaterialEmissiveColor` | `integer` | Emissive color (`makeRGBValue`) |
| `...MaterialShininess` | `real` | Shininess, value between 0 and 1 |
| `...MaterialSpecularColor` | `integer` | Specular color (`makeRGBValue`) |
| `...MaterialTransparency` | `real` | Transparency, value between 0 and 1 |

**Common remarks** (apply to virtually all attributes):

- Assigning a value to a color attribute automatically sets the material to active (`MaterialActive := true`).
- Color/transparency/shininess attributes can only be accessed if the material is active.
- Assigning any attribute **deactivates graphic inheritance**.
- You cannot assign an attribute when the graphic is an **automatically generated graphic group** or when the graphic is located in an automatically generated graphic group.
- Colors are usually set with the method `makeRGBValue [SimTalk]`.

Graphics are referenced via `_3D.getGraphic("deco", [n])`.

---

## Board Material Attributes (Rack)

The Board Material of the Rack provides these attributes.

Attributes: `BoardMaterialActive`, `BoardMaterialAmbientColor`, `BoardMaterialDiffuseColor`, `BoardMaterialEmissiveColor`, `BoardMaterialShininess`, `BoardMaterialSpecularColor`, `BoardMaterialTransparency`.

### BoardMaterialActive
Activates (true) or deactivates (false) the material of the boards of the rack.

```simtalk
.Models.MyModel._3D.getGraphic("deco", [4]).BoardMaterialActive := true
```

### BoardMaterialAmbientColor
Sets the ambient color of the board material.

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BoardMaterialAmbientColor := makeRGBValue(255,0,0)
```

### BoardMaterialDiffuseColor
Sets the diffuse color of the board material.

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BoardMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### BoardMaterialEmissiveColor
Sets the emissive color of the board material.

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BoardMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### BoardMaterialShininess
Sets the shininess of the board material (`real` 0–1).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BoardMaterialShininess := 0.5
```

### BoardMaterialSpecularColor
Sets the specular color of the board material.

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BoardMaterialSpecularColor := makeRGBValue(255,0,0)
```

### BoardMaterialTransparency
Sets the transparency of the board material (`real` 0–1).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BoardMaterialTransparency := 0.6
```

---

## Border Line Material Attributes (Mezzanine)

Sets the Border Line Material around the platform of the Mezzanine.

Attributes: `BorderLineMaterialActive`, `BorderLineMaterialAmbientColor`, `BorderLineMaterialDiffuseColor`, `BorderLineMaterialEmissiveColor`, `BorderLineMaterialShininess`, `BorderLineMaterialSpecularColor`, `BorderLineMaterialTransparency`.

### BorderLineMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BorderLineMaterialActive := true
```

### BorderLineMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BorderLineMaterialAmbientColor := makeRGBValue(255,0,0)
```

### BorderLineMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BorderLineMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### BorderLineMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BorderLineMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### BorderLineMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BorderLineMaterialShininess := 0.7
```

### BorderLineMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BorderLineMaterialSpecularColor := makeRGBValue(255,0,0)
```

### BorderLineMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BorderLineMaterialTransparency := 0.4
```

---

## Dimensioning Attributes

Dimensionings provide these attributes: `DimensioningSpace`, `MeasuredLength`, `MeasuringPoint1`, `MeasuringPoint2`, `TextPosition`.

### DimensioningSpace
Sets the dimensioning space of the graphic. Valid values: `"X Axis"`, `"Y Axis"`, `"Z Axis"`, or `"XY plane"`.

```simtalk
.Models.Model2._3D.getGraphic("deco", [2]).DimensioningSpace := "XY plane"
.Models.Model2._3D.getGraphic("deco", [2]).MeasuringPoint1 := [2,2,2]
.Models.Model2._3D.getGraphic("deco", [2]).MeasuringPoint2 := [3,4,5]
.Models.Model2._3D.getGraphic("deco", [2]).TextPosition := [6,6,6]
print .Models.Model2._3D.getGraphic("deco", [2]).MeasuredLength 
// returns 2.23606797749979m
```

### MeasuredLength
**Read-only attribute** — returns the length of the graphic (data type `length`). The measuring text shows this length.

```simtalk
print .Models.Model2._3D.getGraphic("deco", [2]).MeasuredLength 
// returns 2.23606797749979m
```

### MeasuringPoint1
Sets the first measuring point. Assign an array of type `length[3]` (X-, Y-, Z-position).

```simtalk
.Models.Model2._3D.getGraphic("deco", [2]).MeasuringPoint1 := [2,2,2]
```

### MeasuringPoint2
Sets the second measuring point (array `length[3]`).

```simtalk
.Models.Model2._3D.getGraphic("deco", [2]).MeasuringPoint2 := [3,4,5]
```

### TextPosition
Sets the position of the caption of the dimensioning (array `length[3]`).

```simtalk
.Models.Model2._3D.getGraphic("deco", [2]).TextPosition := [6,6,6]
```

---

## Factory Walls Attributes

Sets the properties of the Factory Walls: `WallElementWidth`.

### WallElementWidth
Sets the width of an entire individual element of the factory walls (`length`).

```simtalk
MyStation.getGraphic("default").createFactoryWalls([11,40,3], 42cm).WallElementWidth := 150cm
print MyStation.getGraphic("default").createFactoryWalls([11,40,3], 42cm).WallElementWidth
```

---

## Fence Attributes

The Fence provides: `FenceElementWidth`, `MeshActive`, `PanesActive`.

### FenceElementWidth
Sets the width of an entire individual element of the fence (`length`).

```simtalk
MyStation.getGraphic("default").createFence([3,4,1], true, false).FenceElementWidth := 90cm
print MyStation.getGraphic("default").createFence([3,4,1], true, false).FenceElementWidth
```

### MeshActive
Activates (true) or deactivates (false) a wire mesh between the fence posts (`boolean`).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).MeshActive := true
```

### PanesActive
Activates (true) or deactivates (false) glass/acrylic glass panes between the fence posts (`boolean`).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PanesActive := true
```

---

## Floor Material Attributes (Mezzanine)

Sets the Floor Material of the platform of the Mezzanine.

Attributes: `FloorMaterialActive`, `FloorMaterialAmbientColor`, `FloorMaterialDiffuseColor`, `FloorMaterialEmissiveColor`, `FloorMaterialShininess`, `FloorMaterialSpecularColor`, `FloorMaterialTransparency`.

### FloorMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FloorMaterialActive := true
```

### FloorMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FloorMaterialAmbientColor := makeRGBValue(255,0,0)
```

### FloorMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FloorMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### FloorMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FloorMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### FloorMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FloorMaterialShininess := 0.2
```

### FloorMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FloorMaterialSpecularColor := makeRGBValue(255,0,0)
```

### FloorMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FloorMaterialTransparency := 0.5
```

---

## Frame Material Attributes (Factory Walls)

Sets the Frame Material of the Factory Walls.

Attributes: `FrameMaterialActive`, `FrameMaterialAmbientColor`, `FrameMaterialDiffuseColor`, `FrameMaterialEmissiveColor`, `FrameMaterialShininess`, `FrameMaterialSpecularColor`, `FrameMaterialTransparency`.

### FrameMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FrameMaterialActive := true
```

### FrameMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FrameMaterialAmbientColor := makeRGBValue(255,0,0)
```

### FrameMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FrameMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### FrameMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FrameMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### FrameMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FrameMaterialShininess := 0.9
```

### FrameMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FrameMaterialSpecularColor := makeRGBValue(255,0,0)
```

### FrameMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).FrameMaterialTransparency := 0.7
```

---

## Mesh Material Attributes (Fence)

Sets the Mesh Material of the Fence.

Attributes: `MeshMaterialActive`, `MeshMaterialAmbientColor`, `MeshMaterialDiffuseColor`, `MeshMaterialEmissiveColor`, `MeshMaterialShininess`, `MeshMaterialSpecularColor`, `MeshMaterialTransparency`.

### MeshMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).MeshMaterialActive := true
```

### MeshMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).MeshMaterialAmbientColor := makeRGBValue(255,0,0)
```

### MeshMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).MeshMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### MeshMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).MeshMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### MeshMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).MeshMaterialShininess := 0.9
```

### MeshMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).MeshMaterialSpecularColor := makeRGBValue(255,0,0)
```

### MeshMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).MeshMaterialTransparency := 0.9
```

---

## Mezzanine Attributes

Sets the properties of the Mezzanine: `BorderLineActive`, `FloorThickness`, `PostDiameter`, `RailingsActive`, `RailingSegmentWidth`.

### BorderLineActive
Activates/deactivates the border line around the platform of the mezzanine (`boolean`).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).BorderLineActive := true
```

### FloorThickness
Sets the floor thickness of the platform (`length`).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [7]).FloorThickness := 0.05
```

### PostDiameter (mezzanine)
Sets the diameter of the posts on which the platform rests (`length`).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [7]).PostDiameter := 0.25
```

### RailingsActive
Activates/deactivates railings around the platform (`boolean`).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).RailingsActive := true
```

### RailingSegmentWidth
Sets the width of the individual railing segments (distance between posts holding the railing). Accessible only if the railing is active (`length`).

```simtalk
MyFrame._3D.getGraphic("deco", [2]).RailingSegmentWidth := 1.2
```

---

## Pane Material Attributes (Factory Walls / Fence)

Sets the Pane Material of the Factory Walls and the Fence (glass/acrylic glass panes).

Attributes: `PaneMaterialActive`, `PaneMaterialAmbientColor`, `PaneMaterialDiffuseColor`, `PaneMaterialEmissiveColor`, `PaneMaterialShininess`, `PaneMaterialSpecularColor`, `PaneMaterialTransparency`.

### PaneMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [4]).PaneMaterialActive := true
```

### PaneMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PaneMaterialAmbientColor := makeRGBValue(255,0,0)
```

### PaneMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PaneMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### PaneMaterialEmissiveColor
```simtalk
.Models.Mode1._3D.getGraphic("deco", [5]).PaneMaterialEmissiveColor := makeRGBValue(0,255,0)
```

### PaneMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PaneMaterialShininess := 0.8
```

### PaneMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PaneMaterialSpecularColor := makeRGBValue(255,0,0)
```

### PaneMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PaneMaterialTransparency := 0.5
```

---

## Post Material Attributes (Fence / Mezzanine / Rack)

Sets the Post Material of the Fence, the Mezzanine, and the Rack.

> The attributes are available for graphics of type Fence, Mezzanine, and Rack (compare `InternalGraphicType`).

Attributes: `PostMaterialActive`, `PostMaterialAmbientColor`, `PostMaterialDiffuseColor`, `PostMaterialEmissiveColor`, `PostMaterialShininess`, `PostMaterialSpecularColor`, `PostMaterialTransparency`.

### PostMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [4]).PostMaterialActive := true
```

### PostMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PostMaterialAmbientColor := makeRGBValue(255,0,0)
```

### PostMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PostMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### PostMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PostMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### PostMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PostMaterialShininess := 0.6
```

### PostMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PostMaterialSpecularColor := makeRGBValue(255,0,0)
```

### PostMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).PostMaterialTransparency := 0.6
```

---

## Profile Material Attributes (Fence)

Sets the Profile Material of the Fence.

Attributes: `ProfileMaterialActive`, `ProfileMaterialAmbientColor`, `ProfileMaterialDiffuseColor`, `ProfileMaterialEmissiveColor`, `ProfileMaterialShininess`, `ProfileMaterialSpecularColor`, `ProfileMaterialTransparency`.

### ProfileMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).ProfileMaterialActive := true
```

### ProfileMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).ProfileMaterialAmbientColor := makeRGBValue(255,0,0)
```

### ProfileMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).ProfileMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### ProfileMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).ProfileMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### ProfileMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).ProfileMaterialShininess := 0.7
```

### ProfileMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).ProfileMaterialSpecularColor := makeRGBValue(255,0,0)
```

### ProfileMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [4]).ProfileMaterialTransparency := 0.9
```

---

## Rack Attributes

Sets the properties of the Rack: `BayDepth`, `BaySize`, `BoardDepth`, `BoardThickness`, `Capacity`, `GroundClearance`, `MinimalStructure`, `PostDiameter`, `SquarePosts`.

### BayDepth
Sets the depth of a single storage bay (`length`). Indirectly also sets the depth of the entire rack.

```simtalk
MyFrame._3D.getGraphic("deco", [8]).BayDepth := 1.5
```

### BaySize
Sets the size of a single storage bay in the XZ-dimension (array `length[2]`). `X`/`[0]` returns the first value, `Y`/`[1]` the second. Changing `BaySize` changes the overall `Dimensions` of the bay; existing capacity does not change.

```simtalk
MyFrame._3D.getGraphic("deco", [8]).BaySize := [2, 2.5]
```

### BoardDepth
Sets the depth of a board of the rack (`length`).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [8]).BoardDepth := 1.5
```

### BoardThickness
Sets the thickness of a board of the rack (`length`). The BoardThickness is not part of the height of the rack.

```simtalk
.Models.MyModel._3D.getGraphic("deco", [8]).BoardThickness := 0.025
```

### Capacity (rack)
Sets the number of storage bays per board and the number of boards in the XZ-dimension (array `integer[2]`). X-direction `.X`/`[0]` = storage bays per board; Y-direction `.Y`/`[1]` = number of boards. **Watchable** attribute.

```simtalk
.Models.MyModel._3D.getGraphic("deco", [8]).Capacity := [4, 4]
```

### GroundClearance
Sets the ground clearance of the rack (`length`) — the distance between the lower edge of the lowest shelf and the floor. Only applies for Store Type "Rack with round/square posts (dynamic)". Specify `void` for default; specify `0` so the lowest shelf rests flat on the floor.

```simtalk
Store3._3D.StoreType := "Rack with round posts (dynamic)"
Store3._3D.Gap := 0.1
Store3._3D.FloorThickness := 0.15
Store3._3D.GroundClearance := 0.3
```

### MinimalStructure
Sets whether the rack is optimized for performance (true) or for post-processing capability (false) (`boolean`).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [8]).MinimalStructure := true
```

### PostDiameter (rack)
Sets the diameter of the posts of the rack (`length`). Accessible only when the material is active.

```simtalk
MyFrame._3D.getGraphic("deco", [8]).PostDiameter := 0.25
```

### SquarePosts
Sets whether the posts are square (true) or round (false) (`boolean`).

```simtalk
MyFrame._3D.getGraphic("deco", [8]).SquarePosts := true
```

---

## Railing Material Attributes (Mezzanine)

Sets the material of the railing around the platform of the Mezzanine.

> The railing material does **not** affect the handrails of the mezzanine.

Attributes: `RailingMaterialActive`, `RailingMaterialAmbientColor`, `RailingMaterialDiffuseColor`, `RailingMaterialEmissiveColor`, `RailingMaterialShininess`, `RailingMaterialSpecularColor`, `RailingMaterialTransparency`.

### RailingMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).RailingMaterialActive := true
```

### RailingMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).RailingMaterialAmbientColor := makeRGBValue(255,0,0)
```

### RailingMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).RailingMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### RailingMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).RailingMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### RailingMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).RailingMaterialShininess := 0.9
```

### RailingMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).RailingMaterialSpecularColor := makeRGBValue(255,0,0)
```

### RailingMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).RailingMaterialTransparency := 0.9
```

---

## Stairs Attributes

Sets the properties of the Stairs: `Rise`, `Run`, `TreadWidth`.

### Rise
Sets the height of the staircase (`length`). Available for graphics of type Stairs (compare `InternalGraphicType`).

```simtalk
.Models.MyModel._3D.getGraphic("deco", [3]).Rise := 3.5
```

### Run
Returns the depth of the staircase. Return value has data type `length`.

```simtalk
print .Models.MyModel._3D.getGraphic("deco", [3]).Run
```

### TreadWidth
Sets the width of the treads of the staircase (`length`). Available for graphics of type Stairs.

```simtalk
.Models.MyModel._3D.getGraphic("deco", [3]).TreadWidth := 4
```

---

## Stringer Material Attributes (Stairs)

Sets the Stringer Material of the Stairs.

> Available for graphics of type Stairs (compare `InternalGraphicType`). The stringer material does **not** affect the handrails of the staircase.

Attributes: `StringerMaterialActive`, `StringerMaterialAmbientColor`, `StringerMaterialDiffuseColor`, `StringerMaterialEmissiveColor`, `StringerMaterialShininess`, `StringerMaterialSpecularColor`, `StringerMaterialTransparency`.

### StringerMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [4]).StringerMaterialActive := true
```

### StringerMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).StringerMaterialAmbientColor := makeRGBValue(255,0,0)
```

### StringerMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).StringerMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### StringerMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).StringerMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### StringerMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).StringerMaterialShininess := 0.5
```

### StringerMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).StringerMaterialSpecularColor := makeRGBValue(255,0,0)
```

### StringerMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).StringerMaterialTransparency := 0.5
```

---

## Tread Material Attributes (Stairs)

Sets the Tread Material of the Stairs.

> Available for graphics of type Stairs (compare `InternalGraphicType`).

Attributes: `TreadMaterialActive`, `TreadMaterialAmbientColor`, `TreadMaterialDiffuseColor`, `TreadMaterialEmissiveColor`, `TreadMaterialShininess`, `TreadMaterialSpecularColor`, `TreadMaterialTransparency`.

### TreadMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [4]).TreadMaterialActive := true
```

### TreadMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).TreadMaterialAmbientColor := makeRGBValue(255,0,0)
```

### TreadMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).TreadMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### TreadMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).TreadMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### TreadMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).TreadMaterialShininess := 0.5
```

### TreadMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).TreadMaterialSpecularColor := makeRGBValue(255,0,0)
```

### TreadMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).TreadMaterialTransparency := 0.5
```

---

## Wall Material Attributes (Factory Walls)

Sets the Wall Material of the Factory Walls.

Attributes: `WallMaterialActive`, `WallMaterialAmbientColor`, `WallMaterialDiffuseColor`, `WallMaterialEmissiveColor`, `WallMaterialShininess`, `WallMaterialSpecularColor`, `WallMaterialTransparency`.

### WallMaterialActive
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).WallMaterialActive := true
```

### WallMaterialAmbientColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).WallMaterialAmbientColor := makeRGBValue(255,0,0)
```

### WallMaterialDiffuseColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).WallMaterialDiffuseColor := makeRGBValue(255,0,0)
```

### WallMaterialEmissiveColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).WallMaterialEmissiveColor := makeRGBValue(255,0,0)
```

### WallMaterialShininess
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).WallMaterialShininess := 0.9
```

### WallMaterialSpecularColor
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).WallMaterialSpecularColor := makeRGBValue(255,0,0)
```

### WallMaterialTransparency
```simtalk
.Models.MyModel._3D.getGraphic("deco", [5]).WallMaterialTransparency := 0.9
```

---

## Attribute index (by graphic type)

| Graphic | Attribute groups |
|---|---|
| **Factory Walls** | Factory Walls Attributes, Frame Material, Pane Material, Wall Material |
| **Fence** | Fence Attributes, Mesh Material, Pane Material, Post Material, Profile Material |
| **Mezzanine** | Border Line Material, Floor Material, Mezzanine Attributes, Post Material, Railing Material |
| **Rack** | Board Material, Post Material, Rack Attributes |
| **Stairs** | Stairs Attributes, Stringer Material, Tread Material |
| **Dimensioning** | Dimensioning Attributes |

### Frequently referenced related items
`_3D.getGraphic [SimTalk]`, `createFactoryWalls [SimTalk]`, `createFence [SimTalk]`, `createMezzanine [SimTalk]`, `createRack [SimTalk]`, `createStairs [SimTalk]`, `createDimensioning [SimTalk]`, `InternalGraphicType [SimTalk]`, `makeRGBValue [SimTalk]`, `Dimensions [SimTalk] - graphic`.

---

*Source: Plant Simulation Help — Shape Materials (Siemens, © 2026).*
