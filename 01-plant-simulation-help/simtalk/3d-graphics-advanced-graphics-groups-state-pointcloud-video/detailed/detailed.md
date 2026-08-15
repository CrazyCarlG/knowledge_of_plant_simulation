# Accessing Graphics (SimTalk)

SimTalk provides attributes and methods for accessing graphics of simulation objects. You can view them via **Auto Complete** on the Edit ribbon tab of the Method Editor.

---

## Object-Level Graphics Access (`_3D`)

### `_3D.calculateMUDimensions` — Method

Calculates the dimensions of the MU designated by `<Path>` from its graphic.

```simtalk
<Path>._3D.calculateMUDimensions([OnlyVisibleGroups:boolean:=false])
```

- `OnlyVisibleGroups` (optional, boolean): if `false` (default) all graphic groups are computed; if `true` only visible graphic groups.
- After execution, the MU's Length, Width, and Height match the graphic dimensions. The zero point of the graphic is used for the booking point.

```simtalk
.MUs.Part._3D.calculateMUDimensions(true)
```

### `_3D.exchangeGraphic` — Method

Exchanges the entire graphic of the selected object with a graphic imported from a file.

```simtalk
<Path>._3D.exchangeGraphic(FilePath:string[, UseNewGraphicMeasurement:boolean:=false]) → boolean
```

- `FilePath` (string): path and name of the file to import.
- `UseNewGraphicMeasurement` (optional, boolean, default `false`): if `true` and the object is an MU and `_3D.ScaleAutomatically` of the loaded `.s3d` file is `false`, it is set to `true` and the graphic measurements are applied.
- Returns boolean.

```simtalk
MyFrame._3D.exchangeGraphic("C:\Program Files\Siemens\Plant Simulation 2606\3D\s3D-graphics\Lathe.s3d")
```

### `_3D.ExcludeFromShowContentOfLocation` — Attribute

Hides (`true`) or shows (`false`) the object's outside representation, and also hides Connectors connected with hidden objects.

```simtalk
<Path>._3D.ExcludeFromShowContentOfLocation:boolean
```

After assigning `true`, the outside representation is only visible within its location, not in the location of its location (useful for EventController, Methods, DataTables, etc.).

```simtalk
Station._3D.ExcludeFromShowContentOfLocation := true
```

### `_3D.exportAsJt` — Method

Exports the designated graphic or 3D object as a `.JT` file. Only exports graphics that are part of the object.

```simtalk
<Path>._3D.exportAsJt(FilePath:string[, OptimizeForCAD:boolean := false, ExcludeInvisibleParts:boolean := false]) → boolean
```

- `FilePath` (string): path to the target file.
- `OptimizeForCAD` (optional, boolean, default `false`): optimize structure for CAD (NX) if `true`, or for Plant Simulation / Teamcenter Visualization if `false`.
- `ExcludeInvisibleParts` (optional, boolean, default `false`): export all graphics (`false`) or only visible ones (`true`).
- When `OptimizeForCAD` is active, captions and logical objects are excluded. Logical objects include: EventController, FlowControl, Cycle, Exporter, Broker, ShiftCalendar, LockoutZone, all InformationFlow objects, all UserInterface objects, all GA objects.
- Returns `true` if the file could be exported with graphics, `false` if nothing was left to export.

```simtalk
.MaterialFlow.Frame.exportAsJt("D:\MyS3D\MyFrame.jt")
```

### `_3D.exportAsS3D` — Method

Exports the graphic data and designated animation object as an `.s3D` file. Exports graphics that are part of the object, appearance/animation-relevant attributes, and the 3D part of embedded objects.

```simtalk
<Path>._3D.exportAsS3D(FilePath:string) → boolean
```

```simtalk
.MaterialFlow.Frame._3D.exportAsS3D("D:\MyS3D\MyFrame.s3d")
```

### `_3D.exportModelingViewBitmap` — Method

Exports the 3D modeling view scene as a `.PNG` file. Camera parameters correspond to `F3DconfigureView`.

```simtalk
<Path>._3D.exportModelingViewBitmap(FilePath:string, Width:integer, Height:integer[, CameraPosition:length[3], CameraRotationX:real, CameraRotationZ:real]) → boolean
```

- `FilePath` (string): path to the target file.
- `Width`, `Height` (integer): bitmap dimensions in pixels.
- `CameraPosition` (optional, `length[3]`): camera position.
- `CameraRotationX`, `CameraRotationZ` (optional, real): rotation angles around x- and z-axis.
- Specify either all three camera parameters or none; without them, Plant Simulation creates a bitmap of the entire scene.
- Returns `true` if the bitmap was created.

```simtalk
.Models.Model._3D.exportModelingViewBitmap("D:\FactoryLibraries\MyFrame", 100, 100, [2,3,2], 2,2)
```

### `_3D.exportPlanningViewBitmap` — Method

Exports the 3D planning view scene as a `.PNG` file. View parameters correspond to `F3DconfigurePlanningView`.

```simtalk
<Path>._3D.exportPlanningViewBitmap(FilePath:string, Width:integer, Height:integer[, ViewPosition:length[2], Zoom:real]) → boolean
```

- `FilePath` (string): path to the target file.
- `Width`, `Height` (integer): bitmap dimensions in pixels.
- `ViewPosition` (optional, `length[2]`): view position.
- `Zoom` (optional, real): zoom factor.
- Specify both view position and zoom together, or neither.
- Returns `true` if the bitmap was created.

```simtalk
.Models.Model._3D.exportPlanningViewBitmap("D:\FactoryLibraries\MyFrame", 100, 100, [2,3], 3)
```

### `_3D.getGraphic` — Method

Returns the designated graphic of the object designated by `<Path>`.

```simtalk
<Path>._3D.getGraphic(GraphicGroupName:string[, Path:any[]]) → void
```

- `GraphicGroupName` (string): name of the graphic group.
- `Path` (optional, `any[]`): lists either one-based numerical indexes or names; the two types cannot be mixed.
  - `[]` designates the entire graphic group (same as omitting the parameter).
  - `[1]` designates the first direct child graphic.
  - `["abc"]` designates the direct child graphic named `abc`.
  - `[1,4]` designates the fourth child of the first direct child.
  - `["abc","def"]` designates the child `def` of direct child `abc`.
- Returns `void` if the specified graphic does not exist, so you can query existence.

```simtalk
var g := Machine._3D.getGraphic("default", [1])
// returns the first graphic in the graphic group named default
g.Position := [1,2,3]
var g := Machine._3D.getGraphic("default", ["head"])
// returns the graphic named head in the graphic group named default
g.Position := [1,2,3]
```

Abbreviated notation when `GraphicGroupName` is a valid identifier:

```simtalk
var g := Machine._3D.default([1])
// returns the first graphic in the graphic group named default
g.Position := [1,2,3]
var g := Machine._3D.default(["head"])
// returns the graphic named head in the graphic group named default
g.Position := [1,2,3]
```

### `_3D.InheritGraphics` — Attribute

Activates (`true`) or deactivates (`false`) graphic inheritance of the object.

```simtalk
<Path>._3D.InheritGraphics:boolean
```

```simtalk
.Models.Model.Station1._3D.InheritGraphics := false
var a: boolean := .Models.Model.Station1._3D.InheritGraphics
// returns whether the graphic is inherited or not
```

### `_3D.optimizeObject` — Method

Optimizes the 3D object designated by `<Path>`. The object can be a simulation object or an animatable object. Optimizing improves performance; discarded data cannot be restored, so optimize after modeling is complete and consider saving the model under a different name first.

```simtalk
<Path>_3D.optimizeObject(WithContainedObjects:boolean, OptimizeInheritance:boolean, OptimizeGraphicStructure:boolean)
```

- `WithContainedObjects` (boolean): optimize the entire partial structure from `<Path>` (`true`) or only the object itself (`false`).
- `OptimizeInheritance` (boolean): activate "Optimize 3D Attribute Inheritance"; if `true`, Plant Simulation activates inheritance of 3D attributes matching their origin, and replaces MU Animation Paths (e.g. `#0#0`) with an Animation Area when possible. Graphics inheritance is never activated.
- `OptimizeGraphicStructure` (boolean): activate "Optimize 3D Graphic Structure" and apply "Flatten structure" without "Keep Grouping" to all editable graphics. When `true`, the model is optimized with "Preserve References" to prevent model size increase.

```simtalk
.Models.Model._3D.optimizeObject(true, true, false)
```

### `_3D.ShowContent` — Attribute

Shows (`true`) or hides (`false`) the outside representation of objects contained within the object. Applies only to objects that can contain MUs (most material flow objects, plus Container and Transporter and their animatable objects) and to Frame.

```simtalk
<Path>._3D.ShowContent:boolean
```

```simtalk
Station._3D.ShowContent := true
```

---

## Detailed Access To Graphics

SimTalk provides these attributes and methods for accessing object graphics in detail.

### `addGraphicTransformation` — Method

Adds an additional transformation to an existing transformation of the designated graphic. Assigning it deactivates graphic inheritance. Cannot be used on automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.addGraphicTransformation(Position:length[3], RotationAngle:real, RotationAxis:real[3], Scale:real/real[3])
```

- `Position` (`length[3]`): position of the graphic.
- `RotationAngle` (real): rotation angle.
- `RotationAxis` (`real[3]`): rotation axis.
- `Scale`: a single `real` for uniform scaling, or `real[3]` for per-axis scaling factors (X, Y, Z).

Transformations are applied sequentially (order matters). Example: a graphic translated by (3,0,0) and rotated 30° around the y-axis, then `addGraphicTransformation` with translation (2,0,0) and scale 2 results in: translate (3,0,0) → rotate 30° around y → translate (2,0,0) → scale by 2. Translations cannot simply be combined into one.

```simtalk
MyStation.getGraphic("default", [1,4]).addGraphicTransformation([3,2,1], 30, [0,0,-1], 2)
MyStation.getGraphic("deco", [1,4]).addGraphicTransformation([3,2,1], 30, [0,0,-1], 2)
```

### `deleteGraphic` — Method

Deletes the specified graphic of the object. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.deleteGraphic
```

```simtalk
MyStation._3D.getGraphic("default", [2,2]).deleteGraphic
```

### `graphic` — Method

Returns the designated inner graphic or graphic group of the graphic/group designated by `<Path>`. Available for composite graphics (see `InternalGraphicType > Composite Graphics`).

```simtalk
<Path>.graphic(Name:string)
<Path>.graphic(Index:string)
```

```simtalk
var outerGraphic := machine._3D.getGraphic("default", [1])
// returns the first graphic in the graphic group named 'default'
var innerGraphic := outerGraphic.Graphic(2)
// returns the second graphic in the first graphic in the graphic group named 'default'
innerGraphic.Position := [1,2,3]
```

### `groupGraphics` — Method

Transforms the designated graphics into a group. Available for composite graphics. Graphics can be specified by numeric indexes or names. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.groupGraphics(Children:any[]) → any
```

- `Children` (`any[]`): numeric indexes or names of graphics to group.
- Returns the created graphic (compare `_3D.getGraphic`).

```simtalk
MyFrame._3D.getGraphic("default", [1,2]).groupGraphics([2,3])
// groups the graphics at the indexes [1,2,2] and [1,2,3]
MyFrame._3D.getGraphic("deco").groupGraphics(["Plate","Tool"])
// groups the graphics named "Plate" and "Tool"
```

### `Index` — Read-only attribute (graphic in 3D)

Returns the numeric index of the specified graphic.

```simtalk
<Path>.Index → integer
```

```simtalk
var index : integer := MyStation._3D.getGraphic("default", ["Wheels"].Index
// the Variable contains the numeric index of the graphic
var index : integer := Graphicgroup.Graphic("Wheels").Index
// the Variable contains the numeric index of the graphic
var Graphicgroup := MyStation._3D.getGraphic("default")
```

### `InternalGraphicType` — Read-only attribute

Returns the type of the graphic or graphic group designated by `<Path>`.

```simtalk
<Path>.InternalGraphicType → string
```

Composite graphics:
- `FactoryWalls` — Factory Walls (after optimizing a parent, may be recognized as `Shape` or `GroupNode`).
- `Fence` — a Fence (may become `GroupNode` after optimization).
- `GraphicGroup` — a graphic group (access with empty array or single parameter in `_3D.getGraphic`).
- `GroupNode` — a normal group node (e.g. formed by `groupGraphics`).
- `Instance` — a special group node that can only contain a single child graphic.
- `Rack` — a Rack (may become `Shape` or `GroupNode`).
- `Stairs` — a Staircase (may become `Shape` or `GroupNode`).
- `Switch` — a special group node that always shows only one of its children.

Simple graphics:
- `BarredArea` — a Barred Area (may become `Shape`).
- `Box` — a Box (may become `Shape`).
- `Dimensionings` — Measurements within the model (may become `Shape`).
- `Shape` — a graphic that is not subdivided further and contains its own graphics data.

```simtalk
var graphic := MyStation._3D.getGraphic("default", [1])
if graphic.InternalGraphicType = "Fence"
   graphic.restoreCutouts
end
```

### `makeAnimatableObject` — Method

Creates an animatable object for the object designated by `<Path>`. It takes the designated graphic, extracts it from the original object, and uses it for the new animatable object. If the graphic is not part of the default graphics group, a graphics group with the name of the source group is created. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.makeAnimatableObject(ObjectName:string, ExtractAtBoundingBoxBase:boolean[, ExtractionOffset:length[3], SwapXAndZAxis:boolean]) → any
```

- `ObjectName` (string): name of the animatable object.
- `ExtractAtBoundingBoxBase` (real): determine insertion position based on the bounding box (`true`) or not (`false`).
- `ExtractionOffset` (optional, `length[3]`, default `[0,0,0]`): offset of the insertion position.
- `SwapXAndZAxis` (optional, boolean, default `false`): rotate graphics by 90° around the y-axis to swap x/z axes while looking the same from outside.
- Returns the newly created animatable object.

```simtalk
var tool := MyStation._3D.getGraphic("default", ["tool"]).makeAnimatableObject("toolHead",true, [0,0,0])
tool.JointType := "Revolute Joint"
MyStation._3D.getGraphic("default", ["tool"]).makeAnimatableObject("toolHead",true, [0,0,0])
MyStation._3D.getObject("toolHead").JointType := "Revolute Joint"
// This line of code accomplishes the same as the second line of code in the first example.
```

### `MaterialActive` — Attribute

Activates (`true`) or deactivates (`false`) the material of the graphic. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.MaterialActive:boolean
```

```simtalk
MyStation._3D.getGraphic("default", [3,3]).MaterialActive := true
```

### `MaterialAmbientColor` — Attribute

Sets the ambient color of the material. Assigning it automatically sets `MaterialActive := true`. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.MaterialAmbientColor:integer
```

```simtalk
MyStation._3D.getGraphic("default", [3,3]).MaterialAmbientColor := makeRGBValue(0,0,255)
```

### `MaterialDiffuseColor` — Attribute

Sets the diffuse color of the graphic. Assigning it automatically sets `MaterialActive := true`. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.MaterialDiffuseColor:integer
```

```simtalk
MyStation._3D.getGraphic("default", [3,3]).MaterialDiffuseColor := makeRGBValue(255,0,0)
```

### `MaterialEmissiveColor` — Attribute

Sets the emissive color of the graphic. Assigning it automatically sets `MaterialActive := true`. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.MaterialEmissiveColor:integer
```

```simtalk
MyStation._3D.getGraphic("default", [3,3]).MaterialEmissiveColor := makeRGBValue(0,255,0)
```

### `MaterialShininess` — Attribute

Sets the material shininess of the graphic. Assigning it automatically sets `MaterialActive := true`. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.MaterialShininess:real
```

Value between 0 and 1.

```simtalk
MyStation._3D.getGraphic("default", [3,3]).MaterialShininess := 0.9
```

### `MaterialSpecularColor` — Attribute

Sets the specular color of the graphic. Assigning it automatically sets `MaterialActive := true`; the attribute can only be accessed if the material is active. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.MaterialSpecularColor:integer
```

```simtalk
MyStation._3D.getGraphic("default", [3,3]).MaterialSpecularColor := makeRGBValue(0,255,0)
```

### `MaterialTransparency` — Attribute

Sets the transparency of the material of the graphic. Assigning it automatically sets `MaterialActive := true`; the attribute can only be accessed if the material is active. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.MaterialTransparency:real
```

Value between 0 and 1. Note: several partially/fully transparent graphics behind each other may render incorrectly or appear missing due to rendering heuristics.

```simtalk
MyStation._3D.getGraphic("default", [3,3]).MaterialTransparency := 0.9
```

### `Name` — Attribute (graphic)

Sets the name of the graphic or graphic group. Deactivates graphic inheritance. The graphic group named `default` cannot be renamed. Not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.Name:string
```

```simtalk
Station._3D.getGraphic("default", [1]).Name := "MyGraphic"
var n:string := Station._3D.getGraphic("default", [1]).Name
```

### `NumGraphics` — Read-only attribute

Returns the number of direct child graphics of the graphic or graphic group.

```simtalk
<Path>.NumGraphics → integer
```

```simtalk
var count : integer := MyStation._3D.getGraphic("default", [1,2,4]).NumGraphics
var count : integer := MyStation._3D.getGraphic("deco", [1,2,4]).NumGraphics
```

### `ObstacleForWorker` — Attribute

Sets the obstacle settings for the Worker of the graphic. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them). Not available for objects that cannot be inserted directly into a Frame (e.g. MUs or folders), nor for graphics of type `BarredArea`.

```simtalk
<Path>.ObstacleForWorker:string
```

For graphics of type `Stairs`:
- `"(None)"` — no obstacle; the Worker can walk through it.
- `"Bounding box"` — the bounding box is an obstacle.
- `"Sides"` — computes the obstacle so an accessible entrance/exit is not obscured and the obstacle is limited to the simulation-relevant height.

For graphics types `FactoryWalls`, `Fence`, `GroupNode`, `Instance`, `Mezzanine`, `Rack`, and `Switch`:
- `"(None)"` — no obstacle.
- `"Bounding box"` — the bounding box is an obstacle.
- `"Graphics"` — the graphics themselves are obstacles.

For graphics of type `Box` and `Shape`:
- `"(None)"` — no obstacle.
- `"Bounding box"` — the bounding box is an obstacle.

```simtalk
Station._3D.ObstacleForWorker := "Graphics"
Station._3D.getGraphic("default", [2]).ObstacleForWorker := "(None)"
```

### `optimizeByPruningTinyGraphics` — Method

Optimizes the graphic by pruning tiny graphics — removes all component graphics that individually fit within the cube designated by `BoundingCubeSideLength`. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.optimizeByPruningTinyGraphics(BoundingCubeSideLength:length)
```

```simtalk
.Models.Model._3D.getGraphic("deco",[1]).optimizeByPruningTinyGraphics([1], 0.001)
```

### `optimizeByStructureFlattening` — Method

Optimizes the graphic designated by `<Path>`. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.optimizeByStructureFlattening(KeepGrouping:boolean, PreserveObstacles:boolean, RemovePolylinesAndPointSets:boolean[, PreserveReferences:boolean:=false])
```

- `KeepGrouping` (boolean): flatten structure while preserving contents (`true`) or not (`false`).
- `PreserveObstacles` (boolean): preserve obstacles (`true`) or not (`false`).
- `RemovePolylinesAndPointSets` (boolean): delete polylines and point sets (`true`) or not (`false`).
- `PreserveReferences` (optional, boolean, default `false`): preserve multiple references to sub-graphics to keep model size small (`true`); if `KeepGrouping` is also `true`, this has no effect.

```simtalk
.Models.Model._3D.getGraphic("deco", [1]).optimizeByStructureFlattening(true, true, false)
```

### `optimizeByVisibilityFilter` — Method

Optimizes the graphic by removing graphic components that are not visible from the outside. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.optimizeByVisibilityFilter(CullGranularity:integer, ReductionLevel:integer)
```

- `CullGranularity` (integer): granularity for deleting graphics — `0` very fine, `3` very coarse.
- `ReductionLevel` (integer): how closely the procedure looks at the graphic — `0` coarse (fast, deletes a lot), `3` very close (slower).

```simtalk
.Models.Model._3D.getGraphic("default", [1]).optimizeByVisibilityFilter(0, 1)
.Models.Model._3D.getGraphic("deco", [2]).optimizeByVisibilityFilter(2, 1)
```

### `Position` — Attribute (graphic)

Sets the position of the graphic. Deactivates graphic inheritance; not applicable to graphics located in automatically generated graphic groups.

```simtalk
<Path>.Position:length[3]
```

The three values designate position on the X-, Y-, and Z-axis.

```simtalk
obj._3D.getGraphic("default", [1,7]).Position := [5,-5,0]
var p : length[3] := obj._3D.getGraphic("deco", [1,7]).Position
```

### `removeTexture` — Method

Deletes an existing texture from the graphic. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.removeTexture
```

```simtalk
MyFrame._3D.getGraphic("deco", [1,2]).removeTexture
```

### `Rotation` — Attribute (graphic)

Sets the rotation of the graphic. Deactivates graphic inheritance; not applicable to automatically generated graphic groups (or graphics within them).

```simtalk
<Path>.Rotation:real/real[4]
```

- A single `real` sets rotation around the negative Z-axis at the insertion position.
- A `real[4]` array: first value is the angle, remaining three are the components of the rotation axis.
- Returns an array of four real values.

```simtalk
var a : any := MyStation._3D.getGraphic("default", [1]).Rotation
// returns an array of size 4
MyStation._3D.getGraphic("default", [1]).Rotation := 30
// rotates the graphic by 30 degrees
MyStation._3D.getGraphic("default", [1]).Rotation := [45, 0, 1, 0]
// rotates the graphic by 45 degrees around the Y-axis
```

### `Scale` — Attribute (graphic)

Sets the scaling of the graphic. Deactivates graphic inheritance; not applicable to graphics located in automatically generated graphic groups.

```simtalk
<Path>.Scale:real/real[3]
```

- A single `real` sets uniform scaling.
- A `real[3]` array sets scaling factors along X-, Y-, and Z-axis.

```simtalk
obj._3D.getGraphic("default", [1,7]).Scale := 1
var w : real[3] := obj._3D.getGraphic("deco", [1,7]).Scale
```

### `TransformationMatrix` — Attribute

Sets the transformation matrix of the designated graphic group. Deactivates graphic inheritance; not applicable to graphics located in automatically generated graphic groups.

```simtalk
<Path>.TransformationMatrix:real[4,4]/real:[16]
```

To set the matrix:
- A two-dimensional `real[4,4]` array:
  ```
  m11 m12 m13 0
  m21 m22 m23 0
  m31 m32 m33 0
  x   y   z   1
  ```
  The sub-matrix `m` contains rotation and scaling; `x`, `y`, `z` designate the position.
- A one-dimensional `real[16]` array in the sequence: `m11 m12 m13 0 m21 m22 m23 0 m31 m32 m33 0 x y z 1`.

Returns an array of `4 × 4` real values.

```simtalk
MyStation._3D.getGraphic("default", [1]).TransformationMatrix := [1,0,0,0, 0,1,0,0, 0,0,1,0, 3,4,0,1]
var m := MyStation._3D.getGraphic("default", [1]).TransformationMatrix
m[2,4] += 3
MyStation._3D.getGraphic("default", [2]).TransformationMatrix  := m
```

---

## Summary Table

| Name | Kind | Purpose |
|------|------|---------|
| `_3D.calculateMUDimensions` | Method | Compute MU dimensions from graphic |
| `_3D.exchangeGraphic` | Method | Replace graphic from file |
| `_3D.ExcludeFromShowContentOfLocation` | Attribute | Hide outside representation |
| `_3D.exportAsJt` | Method | Export as `.JT` file |
| `_3D.exportAsS3D` | Method | Export as `.s3D` file |
| `_3D.exportModelingViewBitmap` | Method | Export modeling view as `.PNG` |
| `_3D.exportPlanningViewBitmap` | Method | Export planning view as `.PNG` |
| `_3D.getGraphic` | Method | Access a graphic/graphic group |
| `_3D.InheritGraphics` | Attribute | Toggle graphic inheritance |
| `_3D.optimizeObject` | Method | Optimize 3D object structure |
| `_3D.ShowContent` | Attribute | Show/hide contained objects |
| `addGraphicTransformation` | Method | Add transformation to graphic |
| `deleteGraphic` | Method | Delete graphic |
| `graphic` | Method | Access inner graphic (composite) |
| `groupGraphics` | Method | Group graphics |
| `Index` | Read-only attribute | Numeric index of graphic |
| `InternalGraphicType` | Read-only attribute | Type of graphic/group |
| `makeAnimatableObject` | Method | Create animatable object |
| `MaterialActive` | Attribute | Activate/deactivate material |
| `MaterialAmbientColor` | Attribute | Ambient color |
| `MaterialDiffuseColor` | Attribute | Diffuse color |
| `MaterialEmissiveColor` | Attribute | Emissive color |
| `MaterialShininess` | Attribute | Shininess (0–1) |
| `MaterialSpecularColor` | Attribute | Specular color |
| `MaterialTransparency` | Attribute | Transparency (0–1) |
| `Name` | Attribute | Name of graphic/group |
| `NumGraphics` | Read-only attribute | Number of direct child graphics |
| `ObstacleForWorker` | Attribute | Worker obstacle settings |
| `optimizeByPruningTinyGraphics` | Method | Prune tiny graphics |
| `optimizeByStructureFlattening` | Method | Flatten graphic structure |
| `optimizeByVisibilityFilter` | Method | Remove invisible components |
| `Position` | Attribute | Position of graphic |
| `removeTexture` | Method | Delete texture |
| `Rotation` | Attribute | Rotation of graphic |
| `Scale` | Attribute | Scaling of graphic |
| `TransformationMatrix` | Attribute | Full transformation matrix |
