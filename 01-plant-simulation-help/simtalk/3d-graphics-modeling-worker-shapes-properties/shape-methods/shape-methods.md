# Shape Methods

SimTalk reference for 3D graphics, modeling, worker shapes, and shape properties — attributes and methods for creating and accessing graphic shapes.

## Worker 3D Attributes

### `_3D.SynchronizedJoints`

Sets if moving toward a pose will synchronize the joints, so that all joints that are part of the movement reach the target state at the same time (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>._3D.SynchronizedJoints:boolean`
- **Assignment Value:** boolean

```simtalk
.MaterialFlow.Station._3D.SynchronizedJoints := true
```

**See also:** Poses, Synchronized Joints, Accessing the Worker

### `_3D.GraphicsWhenCarrying`

Sets a sequence of graphic groups of the Worker designated by `<Path>`, while he carries a part.

- **Remarks:** The Worker cycles through the graphic groups in the sequence while he walks on a FootPath or walks freely within the model while carrying a part. If the sequence is empty, 3D uses the visible graphic groups defined in `_3D.VisibleGraphics` (default behavior).
- **Type:** Attribute
- **Syntax:** `<Path>._3D.GraphicsWhenCarrying:string[]`
- **Assignment Value:** array of string

```simtalk
.Resources.MyWorker._3D.GraphicsWhenCarrying := ["Pose1", "Pose2"]
```

**See also:** `_3D.VisibleGraphicGroups`, `_3D.VisibleWalkingGraphicGroup`

### `_3D.GraphicsWhenEmpty`

Sets a sequence of graphic groups of the Worker designated by `<Path>`, while he does not carry a part.

- **Remarks:** The Worker cycles through the graphic groups in the sequence while walking on a FootPath or freely within the model without carrying a part. If empty, uses `_3D.VisibleGraphics` (default behavior).
- **Type:** Attribute
- **Syntax:** `<Path>._3D.GraphicsWhenEmpty:string[]`
- **Assignment Value:** array of string

```simtalk
.Resources.MyWorker._3D.GraphicsWhenEmpty := ["Pose1", "Pose2"]
```

**See also:** `_3D.VisibleGraphicGroups`, `_3D.VisibleWalkingGraphicGroup`

### `_3D.ObstacleForWorker`

Sets which part of the object designated by `<Path>` is an obstacle for the Worker when walking freely within the model.

- **Type:** Attribute
- **Syntax:** `<Path>._3D.ObstacleForWorker:string`
- **Assignment Value:** string

| Setting | Description |
| --- | --- |
| `"Bounding box"` | The bounding box of the entire object is an obstacle around which the Worker has to walk. For the Workplace, Plant Simulation shows two bounding boxes with a gap in between (the Worker stays in the middle). Most performant setting. |
| `"Bounding box of visible graphics"` | Bounding box of the entire object is an obstacle; hidden graphic groups are not considered. Length-oriented objects and Frames do not provide this setting. |
| `"Graphics"` | Individual graphics of the object are obstacles. The Worker can walk through pillars/station without walking around the overall obstacle. Conveyor curves are only roughly approximated. Can have negative performance effects. |
| `"Visible graphics"` | Graphics are obstacles; hidden graphic groups not considered. Can have negative performance effects. |
| `"(None)"` | The object is no obstacle; the Worker can walk through/across it (e.g., information flow objects like Method). |

```simtalk
Station._3D.ObstacleForWorker := "Graphics"
PickAndPlace._3D.ObstacleForWorker := "(None)"
```

**See also:** `_3D.getGraphic.ObstacleForWorker`, Show Obstacles, Worker Width, Barred Area, Worker object

### `_3D.VisibleWalkingGraphicGroup`

Returns the name of the graphic group that the Worker instance designated by `<Path>` is currently using to visualize a walking Worker.

- **Remarks:** If the Worker is not currently walking, returns an empty string `""`.
- **Type:** Read-only Attribute
- **Syntax:** `<Path>._3D.VisibleWalkingGraphicGroup:string`

```simtalk
print .Resources.Worker:1._3D.VisibleWalkingGraphicGroup 
-- might, for example, return carrying0
```

**See also:** `_3D.GraphicsWhenCarrying`, `_3D.GraphicsWhenEmpty`

---

## Methods for Creating Shapes

Methods for creating shapes in a graphic or graphic group. Access them via Auto Complete on the Edit ribbon tab of the Method Editor, or insert shapes via Insert Shape.

### `createBarredArea`

Creates a barred area in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Initially the created graphic has no materials; set these later.
- **Type:** Method
- **Syntax:** `<Path>.createBarredArea(Dimensions:length[2]) → any`
- **Parameter:** `Dimensions` is an array of `length` setting Width/dimension X and Depth/dimension Y.
- **Return Value:** `any` — designates the created graphic (compare `_3D.getGraphic`).

```simtalk
var BarredArea := _3D.getGraphic("deco").createBarredArea([8, 6])
BarredArea.MaterialActive := true
BarredArea.MaterialDiffuseColor := makeRGBValue(255,0,0)

var BarredArea := _3D.getGraphic("deco").createBarredArea([8, 6])
// the x dimension does not matter as long as it is not 0 because 
// it will be thrown away when the Form becomes "One-sided delimitation"
BarredArea.Form := "One-sided delimitation"
```

**See also:** Barred Area, Form

### `createBox`

Creates a box in the graphic or graphic group designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createBox(Dimensions:length[3][, WallThickness:length]) → any`
- **Parameters:**
  - `Dimensions` — array of `length` with three values: Width/X, Depth/Y, Height/Z.
  - `WallThickness` (optional) — thickness of the walls; default 0.
- **Return Value:** `any` — the created graphic.

```simtalk
var box := _3D.getGraphic("deco").createBox([2.0,2.5,1], 0.15)
box.MaterialActive := true
box.MaterialDiffuseColor := makeRGBValue(255,0,0)
```

**See also:** Box, `createRectangle`

### `createConeFrustum`

Creates a cone frustum in the graphic or graphic group designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createConeFrustum(TopRadius:length, BottomRadius:length, Height:length[, WallThickness:length]) → any`
- **Parameters:**
  - `TopRadius` — top radius. 0 creates a cone with a tip; > 0 cuts off the tip (e.g., a bottle).
  - `BottomRadius` — bottom radius. Greater bottom radius creates a funnel-type truncated cone.
  - `Height` — height.
  - `WallThickness` (optional) — wall thickness. Omit to create a closed cone; negative value is interpreted as unspecified; 0 creates a mantle without thickness.
- **Return Value:** `any` — the created graphic.

```simtalk
var Cone := _3D.getGraphic("deco").createConeFrustum(2, 3, 4)
Cone.MaterialActive := true
Cone.MaterialDiffuseColor := makeRGBValue(255,0,0)

var Cone := _3D.getGraphic("deco").createConeFrustum(2, 3, 4, 0.1)
Cone.MaterialActive := true
Cone.MaterialDiffuseColor := makeRGBValue(255,0,0)

-- createConeFrustum, createText
if not is3DOpen 
    open3D
end
var obj : object := ~.Canvas
if not obj.CreateIn3D 
       obj.CreateIn3D := true
end
obj._3D.deleteGraphicGroupContent
var pos3D : length[3] := [1, 0, -0.5]
var defaultGraphicGroup : any     := obj._3D.getGraphic("default")
-- bottom radius, top radius, height
-- defaultGraphicGroup.createConeFrustum(1, 0, 1.2).Position := pos3D -- German erzeugeKegel
pos3D[2] := 1.5
-- Text width 3m
defaultGraphicGroup.createText(" My text! ", 3m).Position := pos3D -- German erzeugeTextplatte 
pos3D[2] := 2.5
-- defaultGraphicGroup.erzeugeText(" My large text ! ", 3m).Position := pos3D
```

**See also:** Cone Frustum

### `createCuboid`

Creates a cuboid in the graphic or graphic group designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createCuboid(Dimensions:length[3][, LineWidth:real, LineColor:integer]) → any`
- **Parameters:**
  - `Dimensions` — array of `length` with three values: Width/X, Depth/Y, Height/Z. Set one dimension to 0 to create a flat wall (e.g., `[0,2,3]` creates a wall on the YZ plane).
  - `LineWidth` (optional) — width of the line around the cuboid (> 0).
  - `LineColor` (optional) — color of the line around the cuboid.
  - Without optional parameters, the cuboid has no border.
- **Return Value:** `any` — the created graphic.

```simtalk
var Cube := _3D.getGraphic("deco").createCuboid([3.0, 2.5, 1])
Cube.MaterialActive := true
Cube.Position := [1.0, 2.0, 0.0]
Cube.MaterialDiffuseColor :=  makeRGBValue(255,0,0)

// creates a flat wall on the YZ plane
var Cube := _3D.getGraphic("deco").createCuboid([0, 2, 3]) // flat wall
Cube.MaterialActive := true
Cube.Position := [1.0, 2.0, 0.0]
Cube.MaterialDiffuseColor :=  makeRGBValue(255,0,0)

-- create cuboid
if not is3DOpen 
    open3D
end
var obj:object := ~.Canvas
if not obj.CreateIn3D 
       obj.CreateIn3D := true
end
obj._3D.deleteGraphicGroupContent
obj._3D.getGraphic("default").createCuboid([1.0m, 1.0m, 1.0m])
```

**See also:** Cuboid

### `createDimensioning`

Creates dimensionings in the graphic or graphic group designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createDimensioning(MeasuringPoint1:length[3], MeasuringPoint2:length[3], TextPosition:length[3]) → any`
- **Parameters:**
  - `MeasuringPoint1` — `length[3]`: X, Y, Z of the first measuring point.
  - `MeasuringPoint2` — `length[3]`: X, Y, Z of the second measuring point.
  - `TextPosition` — `length[3]`: X, Y, Z of the text that shows the measured value. If omitted, the center between the two measuring points is used.
- **Return Value:** `any` — the created graphic.

```simtalk
var Dimensioning := _3D.getGraphic("deco").createDimensioning([10,10,5], [5,5,5], [5,5,5])
Dimensioning.MaterialActive := true
Dimensioning.MaterialDiffuseColor :=  makeRGBValue(255,0,0)
```

**See also:** Dimensioning, DimensioningSpace, MeasuredLength, MeasuringPoint1, MeasuringPoint2, TextPosition

### `createExtrusionGraphic`

Creates a graphic that extrudes a two-dimensional profile along a three-dimensional vector in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Profiles can be created using the `F3DGenerate...` functions or fully user-defined profiles. A profile needs to surround an area and is not allowed to intersect itself.
- **Type:** Method
- **Syntax:** `<Path>.createExtrusionGraphic(Profile:length[2,*], ExtrusionVector:length[3], ClosedShape:boolean) → any`
- **Parameters:**
  - `Profile` — two-dimensional array of `length` with two values (the profile to extrude).
  - `ExtrusionVector` — array of `length` with three values (the vector to extrude along).
  - `ClosedShape` — `boolean`: closed shape (with cover faces at start/end) or hollow shape (you can look through along the extrusion vector). Closed shapes with holes are possible.
- **Return Value:** `any` — the created graphic.

```simtalk
-- This creates a closed but hollow extruded ellipse: You can see through the hole but not through the graphic.
MyObject._3D.getGraphic("default").createExtrusionGraphic(F3DgenerateHollowEllipse([0m, 0m], 2m, 3m, 0.1m, 0.1m), [2m, 0m, 0m], true)
-- This creates a closed cylinder: You cannot see through anything.
MyObject._3D.getGraphic("default").createExtrusionGraphic(F3DgenerateEllipse([5m, 0m], 2m, 2m, 0.1m, 0.1m), [0m, 2m, 0m], true)
-- This creates the shell of a cylinder: You cannot see through anything.
MyObject._3D.getGraphic("default").createExtrusionGraphic(F3DgenerateEllipse([-5m, 0m], 2m, 2m, 0.1m, 0.1m), [0m, 0m, 2m], false)
```

**See also:** `createIndexedFaceSet`, `F3DgenerateEllipse`, `F3DgenerateHollowEllipse`, `F3DgenerateHollowRectangle`, `F3DgenerateRectangle`, `_3D.ExtConfiguration`

### `createFactoryWalls`

Creates factory walls in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Initially the created graphic has no materials; set these later.
- **Type:** Method
- **Syntax:** `<Path>.createFactoryWalls(Dimensions:length[3], WallThickness:length[, WallElementWidth:length]) → any`
- **Parameters:**
  - `Dimensions` — `length[3]`: Width/X, Depth/Y, Height/Z.
  - `WallThickness` (optional) — thickness of the factory walls.
  - `WallElementWidth` (optional) — width of the individual elements of the factory walls.
- **Note:** Changing the setting for Placing The Remainder resets the Cutouts.
- **Return Value:** `any` — the created graphic.

```simtalk
var FactoryWalls := _3D.getGraphic("deco").createFactoryWalls([10, 10, 5], 0.3)
FactoryWalls.MaterialActive := true
FactoryWalls.MaterialDiffuseColor := makeRGBValue(255,0,0)

MyStation.getGraphic("default").createFactoryWalls([11,40,3], 1m)
MyStation._3D.getGraphic("default").createFactoryWalls([11,40,3], 42cm).PlaceRemainder := "Counter-clockwise"
```

**See also:** Factory Walls, PlaceRemainder

### `createFence`

Creates a fence in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Initially the created graphic has no materials; set these later.
- **Type:** Method
- **Syntax:** `<Path>.createFence(Dimensions:length[3], Mesh:boolean, Panes:boolean[, FenceElementWidth:length]) → any`
- **Parameters:**
  - `Dimensions` — `length[3]`: Dimension X, Y, Z of the fence.
  - `Mesh` — `boolean`: whether a wire mesh is inserted between posts (`true`) or not (`false`).
  - `Panes` — `boolean`: whether transparent/non-transparent panes are inserted between posts (`true`) or not (`false`).
  - `FenceElementWidth` (optional) — width of the individual elements of the fence.
- **Note:** Changing Placing The Remainder resets the Cutouts.
- **Return Value:** `any` — the created graphic.

```simtalk
var Fence := _3D.getGraphic("deco").createFence([3.0, 2.5, 2], true, true)
Fence.MaterialActive := true
Fence.MaterialDiffuseColor := makeRGBValue(255,0,0)

MyStation.getGraphic("default").createFence([3.0, 2.5, 2], true, true, 0.5m)
MyStation1._3D.getGraphic("default").createFence([3,4,1], true, false).PlaceRemainder := "Top and left"
```

**See also:** Fence, PlaceRemainder

### `createIndexedFaceSet`

Creates an indexed face set in the graphic or graphic group designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createIndexedFaceSet(Nodes:length[3,*], Faces:length[][][, Colors:integer[]]) → any`
- **Parameters:**
  - `Nodes` — two-dimensional array of `length` with three values (positions of nodes in space).
  - `Faces` — array of arrays of `length`: each inner array contains a sequence of node indexes defining the contour of a face. Only works correctly with convex faces.
  - `Colors` (optional) — `integer`: a single color applies to the entire graphic; an array of colors applies each color to one face.
- **Return Value:** `any` — the created graphic.

```simtalk
var obj := .Models.Model._3D
var Group := obj.getGraphic("deco")
for var i := Group.NumGraphics downto 1
    Group.graphic(1).deleteGraphic
next
// ######### Begin code example ###########
var GraphicGroup := .Models.Model._3D.getGraphic("deco")
var Points: real[3, 8]
var b:real := 0 // bottom
var t:real := 1 // top
Points[1, 1] := b;  Points[2, 1] := b;  Points[3, 1] := b
Points[1, 2] := t;  Points[2, 2] := b;  Points[3, 2] := b
Points[1, 3] := t;  Points[2, 3] := t;  Points[3, 3] := b
Points[1, 4] := b;  Points[2, 4] := t;  Points[3, 4] := b
Points[1, 5] := b;  Points[2, 5] := b;  Points[3, 5] := t
Points[1, 6] := t;  Points[2, 6] := b;  Points[3, 6] := t
Points[1, 7] := t;  Points[2, 7] := t;  Points[3, 7] := t
Points[1, 8] := b;  Points[2, 8] := t;  Points[3, 8] := t
var Faces : any[6] := [[1,2,3,4], [5,6,7,8], [1,2,6,5], [4,3,7,8], [2,3,7,6], [1,4,8,5]]
// colors: yellow pink blue green red black
var FaceColors: integer[6] := [makeRGBValue(255,255,0), makeRGBValue(255,0,255), makeRGBValue(0,0,255), makeRGBValue(0,255,0), makeRGBValue(255,0,0), makeRGBValue(0,0,0)]
GraphicGroup.createIndexedFaceSet(Points, Faces, FaceColors).Position := [-5,0,0.5]
var FaceColor: integer := makeRGBValue(190,190,190) // grey
GraphicGroup.createIndexedFaceSet(Points, Faces, FaceColor).Position := [-3,0,0.5]

var PolyLine: any[2] := [[1,2,3,4,1],[5,6,7,8,5]]
GraphicGroup.createIndexedLineSet(Points, PolyLine, makeRGBValue(0,0,0)).Position := [0,0,0.5]
var Poly3Line1: any[2] := [[1,2,6,7], [3,4,8,5]]
var Poly3Line2: any[2] := [[2,3,7,8], [4,1,5,6]]
GraphicGroup.createIndexedLineSet(Points, Poly3Line1, makeRGBValue(255,0,0)).Position := [2,0,0.5]
GraphicGroup.createIndexedLineSet(Points, Poly3Line2, makeRGBValue(0,0,255)).Position := [2,0,0.5]
// ######### End code example ###########
```

**See also:** `createIndexedLineSet`

### `createIndexedLineSet`

Creates an indexed line set in the graphic or graphic group designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createIndexedLineSet(Nodes:length[3], LineSequences:integer[][][, Color:integer]) → any`
- **Parameters:**
  - `Nodes` — two-dimensional array of `length` with three values (positions of nodes).
  - `LineSequences` — array of arrays of `integer`: each inner array contains a sequence of node indexes defining the line.
  - `Color` (optional) — the color.
- **Return Value:** `any` — the created graphic.

```simtalk
var obj := .Models.Model._3D
var Group := obj.getGraphic("deco")
for var i := Group.NumGraphics downto 1
    Group.graphic(1).deleteGraphic
next
// ######### Begin code example ###########
var GraphicGroup := .Models.Model._3D.getGraphic("deco")
var Points: real[3, 8]
var b:real := 0 // bottom
var t:real := 1 // top
Points[1, 1] := b;  Points[2, 1] := b;  Points[3, 1] := b
Points[1, 2] := t;  Points[2, 2] := b;  Points[3, 2] := b
Points[1, 3] := t;  Points[2, 3] := t;  Points[3, 3] := b
Points[1, 4] := b;  Points[2, 4] := t;  Points[3, 4] := b
Points[1, 5] := b;  Points[2, 5] := b;  Points[3, 5] := t
Points[1, 6] := t;  Points[2, 6] := b;  Points[3, 6] := t
Points[1, 7] := t;  Points[2, 7] := t;  Points[3, 7] := t
Points[1, 8] := b;  Points[2, 8] := t;  Points[3, 8] := t
var Faces : any[6] := [[1,2,3,4], [5,6,7,8], [1,2,6,5], [4,3,7,8], [2,3,7,6], [1,4,8,5]]
// colors: yellow pink blue green red black
var FaceColors: integer[6] := [makeRGBValue(255,255,0), makeRGBValue(255,0,255), makeRGBValue(0,0,255), makeRGBValue(0,255,0), makeRGBValue(255,0,0), makeRGBValue(0,0,0)]
GraphicGroup.createIndexedFaceSet(Points, Faces, FaceColors).Position := [-5,0,0.5]
var FaceColor: integer := makeRGBValue(190,190,190) // grey
GraphicGroup.createIndexedFaceSet(Points, Faces, FaceColor).Position := [-3,0,0.5]

var PolyLine: any[2] := [[1,2,3,4,1],[5,6,7,8,5]]
GraphicGroup.createIndexedLineSet(Points, PolyLine, makeRGBValue(0,0,0)).Position := [0,0,0.5]
var Poly3Line1: any[2] := [[1,2,6,7], [3,4,8,5]]
var Poly3Line2: any[2] := [[2,3,7,8], [4,1,5,6]]
GraphicGroup.createIndexedLineSet(Points, Poly3Line1, makeRGBValue(255,0,0)).Position := [2,0,0.5]
GraphicGroup.createIndexedLineSet(Points, Poly3Line2, makeRGBValue(0,0,255)).Position := [2,0,0.5]
// ######### End code example ###########
```

**See also:** `createIndexedFaceSet`

### `createMezzanine`

Creates a mezzanine in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Initially the created graphic has no materials; set these later.
- **Type:** Method
- **Syntax:** `<Path>.createMezzanine(Dimensions:length[3], FloorThickness:length, PostDiameter:length, BorderLine:boolean, RailingSegmentWidth:length) → any`
- **Parameters:**
  - `Dimensions` — `length[3]`: Width/X, Depth/Y, Height/Z.
  - `FloorThickness` — floor thickness on which the platform rests.
  - `PostDiameter` — diameter of the posts.
  - `BorderLine` — `boolean`: whether a borderline is inserted around the platform (`true`) or not (`false`).
  - `RailingSegmentWidth` — width of individual railing segments (distance between posts holding the railing). 0 deactivates the railing; > 0 activates it and sets the segment width.
- **Return Value:** `any` — the created graphic.

```simtalk
var mezzanine := _3D.getGraphic("deco").createMezzanine([1.5, 3.0, 2.8], 0.08, 0.15, true, 1.0)
mezzanine.MaterialActive := true
mezzanine.MaterialDiffuseColor := makeRGBValue(255,0,0)
```

**See also:** Mezzanine

### `createPicture`

Creates a textured plate showing the full-sized picture loaded from the designated file in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Several transparent graphics behind each other may look wrong/missing due to rendering heuristics.
- **Type:** Method
- **Syntax:** `<Path>.createPicture(FilePath:string, Orientation:integer, Size:length[2], Bifacial:boolean[, Thickness:length:=1mm, UseTransparency:boolean:=true]) → any`
- **Parameters:**
  - `FilePath` — path and name of the file to import.
  - `Orientation` — `1` = Floor, `2` = Front Wall, `3` = Side Wall.
  - `Size` — `length[2]`: Width and Height. A value ≤ 0 computes the other value from the width-to-height ratio.
  - `Bifacial` — `boolean`: show texture on both sides (`true`) or only top side (`false`).
  - `Thickness` (optional) — thickness of the plate. Default `1 mm`.
  - `UseTransparency` (optional) — `boolean`: transparent pixels shown transparent (`true`) or opacity enforced (`false`). Default `true`. No effect if the image has no transparent pixels.
- **Return Value:** `any` — the created graphic.

```simtalk
var picture := _3D.getGraphic("deco").createPicture("D:\Picture.png", 1, [5.0,3.0], false, 1)
picture.MaterialActive := true
picture.MaterialDiffuseColor := makeRGBValue(255,0,0)
```

**See also:** Textured Plate, `createTiledPlate`

### `createPolyLine`

Creates a polyline with the specified parameters in the 3D simulation model specified by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createPolyLine(Nodes:length[3,*], Diameter:length[, Directed:boolean:=false]) → any`
- **Parameters:**
  - `Nodes` — array of `length`: the anchor points of the polyline.
  - `Diameter` — diameter of the polyline.
  - `Directed` (optional) — `boolean`: whether the direction is shown (`true`) or not (`false`). Default `false`.
- **Return Value:** `any` — the created polyline.

```simtalk
// The following code creates a directed polyline with 4 points, a diameter of 0.1 and a color of orange.
var Points = make2DimArray(3, [ 6.0, -2.0, 1.0,
                               9.0, -2.0, 1.0,
                              12.0, -4.0, 2.0,
                              15.0, -4.0, 2.0])
var PolyLine := _3D.getGraphic("deco").createPolyLine(Points, 0.1, true)
PolyLine.MaterialDiffuseColor :=  makeRGBValue(255, 128, 0)
```

### `createRack`

Creates a rack in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Initially the created graphic has no materials; set these later.
- **Type:** Method
- **Syntax:** `<Path>.createRack(BaySize:length[2], BoardDepth:length, Capacity:integer[2], MinimalStructure:boolean[, SquarePosts:boolean:=false, PostDiameter:length:=40mm, BoardThickness:length:=30mm, GroundClearance:length]) → any`
- **Parameters:**
  - `BaySize` — `length[2]`: Width/X and Height/Z of individual bays.
  - `BoardDepth` — depth/Y of the boards.
  - `Capacity` — `integer[2]`: Number of Bays per Board and Number of Boards.
  - `MinimalStructure` — `boolean`: optimization aims for Performance (`true`) or Post-processing Capability (`false`).
  - `SquarePosts` (optional) — square posts (`true`) or round posts (`false`). Default round.
  - `PostDiameter` (optional) — diameter of the posts. Default `4 cm`.
  - `BoardThickness` (optional) — thickness of a board. Default `3 cm`.
  - `GroundClearance` (optional) — distance between the lower edge of the lowest board and the floor. `0` = flat on the floor.
- **Return Value:** `any` — the created graphic.

```simtalk
var Rack := _3D.getGraphic("deco").createRack([1.5, 1.5], 1, [3, 4], true, true, 0.1, 0.05, 0.5)
Rack.MaterialActive := true
Rack.MaterialDiffuseColor := makeRGBValue(255,0,0)
```

**See also:** Rack

### `createRectangle`

Creates a rectangle in the graphic or graphic group designated by `<Path>` at position (X,Y) with the specified Width and Height.

- **Remarks:** A negative Width makes X the X-position of the right-hand side. A positive Height makes Y the Y-position of the bottom side.
- **Type:** Method
- **Syntax:** `<Path>.createRectangle(X:real, Y:real, Width:real, Height:real[, Color:integer=-1, Thickness:real=0.08]) -> any`
- **Parameters:**
  - `X` — X-position.
  - `Y` — Y-position.
  - `Width` — width.
  - `Height` — height.
  - `Color` (optional) — color. Default `-1`.
  - `Thickness` (optional) — thickness of the line. Default `0.08`.
- **Return Value:** `any` — the created graphic.

```simtalk
-- Creates a rectangle in the graphic group named deco with the top left corner located at the position (2,-2), a width of 8, and a height of 6.
root._3D.deco.createRectangle(2, -2, 8, -6, getStandardColor(1), 0.1)
-- Creates a rectangle with the bottom left corner located at the position (2,-2).
root._3D.deco.createRectangle(2, -2, 8, 6, getStandardColor(1), 0.1)
-- Creates a rectangle with the lower left corner at (2,-2), color RGB(200, 0, 0), default line width 0.08.
root._3D.getGraphic("deco").createRectangle(2, -2, -8, 6, makeRGBValue(200, 0, 0))
```

**See also:** Box, `createBox`

### `createSphere`

Creates a sphere in the graphic or graphic group designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createSphere(Radius:length) → any`
- **Parameter:** `Radius` — radius of the sphere.
- **Return Value:** `any` — the created graphic.

```simtalk
var Sphere := _3D.getGraphic("deco").createSphere(2)
Sphere.MaterialActive := true
Sphere.MaterialDiffuseColor := makeRGBValue(255,0,0)
```

**See also:** Sphere

### `createStairs`

Creates a staircase in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Initially the created graphic has no materials; set these later.
- **Type:** Method
- **Syntax:** `<Path>.createStairs(TreadWidth:length, Rise:length, StartAtFirstTread:boolean) → any`
- **Parameters:**
  - `TreadWidth` — tread width (width of the steps and thus the entire stairway).
  - `Rise` — rise (height of the entire stairway from one floor to the next).
  - `StartAtFirstTread` — `boolean`: whether the staircase starts at the first tread without the stringer jutting out onto the floor (`true`) or not (`false`).
- **Return Value:** `any` — the created graphic.

```simtalk
var Stairs := _3D.getGraphic("deco").createStairs(1.5, 3, true)
Stairs.MaterialActive := true
Stairs.MaterialDiffuseColor := makeRGBValue(255,0,0)
```

**See also:** Stairs

### `createText`

Creates text in the graphic or graphic group designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createText(Text:string[, Width:length, TextColor:integer, BackgroundColor:integer, Alignment:integer]) → any`
- **Parameters:**
  - `Text` — the actual text to show.
  - `Width` (optional) — width of the text. Enter `-1` to automatically compute the width from the text length.
  - `TextColor` (optional) — color of the text.
  - `BackgroundColor` (optional) — background color of the text.
  - `Alignment` (optional) — `-1` left, `0` center, `1` right.
- **Return Value:** `any` — the created graphic.

```simtalk
var Text := _3D.getGraphic("deco").createText("My text.", 6) // width 6m
Text.MaterialActive := true
Text.MaterialDiffuseColor := makeRGBValue(255,0,0)
```

**See also:** Text (graphic shape)

### `createTiledPlate`

Creates a plate which shows the picture or texture loaded from a picture, tiled, in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Several transparent graphics behind each other may look wrong/missing due to rendering heuristics.
- **Type:** Method
- **Syntax:** `<Path>.createTiledPlate(FilePath:string, Orientation:integer, Size:length[2], Bifacial:boolean, TileSize:length[2][, Thickness:length:=1mm, UseTransparency:boolean:=true]) → any`
- **Parameters:**
  - `FilePath` — path and name of the file to import.
  - `Orientation` — `1` = Floor, `2` = Front Wall, `3` = Side Wall.
  - `Size` — `length[2]`: Width and Height. A value ≤ 0 computes the other value. Max Width/Height 32767 pixels.
  - `Bifacial` — `boolean`: show texture on both sides (`true`) or only top side (`false`).
  - `TileSize` — `length[2]`: Width/Tile Size X and Depth/Tile Size Y of a tile. A value ≤ 0 computes the other value from the ratio.
  - `Thickness` (optional) — thickness of the plate. Default `1 mm`.
  - `UseTransparency` (optional) — `boolean`: transparent pixels shown transparent (`true`) or opacity enforced (`false`). Default `true`. No effect without transparent pixels.
- **Return Value:** `any` — the created graphic.

```simtalk
var TiledPlate := _3D.getGraphic("deco").createTiledPlate("D:\Picture.png", 1, [4.0,2.0], true, [2.0, 2.0], 0.1)
TiledPlate.MaterialActive := true
TiledPlate.MaterialDiffuseColor := makeRGBValue(255,0,0)
```

**See also:** Textured Plate, `createPicture`

### `importGraphics`

Imports the specified graphic from the file and adds it to the existing graphic in the graphic or graphic group designated by `<Path>`.

- **Remarks:** Plant Simulation uses the file name of the graphic as the name of the graphic node.
- **Type:** Method
- **Syntax:** `<Path>.importGraphics(FilePath:string[, YUpToZUp:boolean:=false, MoveContentToZero:boolean:=false]) → any`
- **Parameters:**
  - `FilePath` — path to the graphic to be imported.
  - `YUpToZUp` (optional) — `boolean`: convert the up-direction (y) of the imported graphic to z-direction (`true`) or not (`false`). Default `false`.
  - `MoveContentToZero` (optional) — `boolean`: move the visible center of the imported graphic to coordinates 0,0,0 (`true`) or not (`false`). Default `false`.
- **Return Value:** `any`

## Related Topics

- `_Accessing Poses`
- `_Accessing the Worker`
- `_Accessing Methods of Graphic Shapes`
- `_Accessing Attributes of Graphic Shapes`
- `_Detailed Access To Graphics`
- `_3D.getGraphic`
- Auto Complete
- Insert Shape

> Source: Plant Simulation Help (Unpublished work. © 2026 Siemens)
