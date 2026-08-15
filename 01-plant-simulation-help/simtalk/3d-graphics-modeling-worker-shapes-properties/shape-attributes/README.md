# Shape Attributes

SimTalk provides attributes, read-only attributes, and methods for setting properties of shapes (graphics) in 3D modeling.

> **Source:** `shape-attributes.md`

## Overview

The following table lists all shape attributes and methods documented in this directory, along with their type and the graphic types they apply to.

| Name | Type | Applies to graphic types |
| --- | --- | --- |
| `importGraphics` | Method | Any graphic (via `_3D.getGraphic`) |
| `Dimensions` (barred area) | Attribute | `BarredArea` |
| `Dimensions` (graphic) | Attribute | `Box`, `FactoryWalls`, `Fence`, `Mezzanine`, `Rack` |
| `Form` | Attribute | `BarredArea` |
| `HasCutouts` | Read-only attribute | `FactoryWalls`, `Fence`, `Mezzanine` |
| `PlaceRemainder` | Attribute | `FactoryWalls`, `Fence` |
| `restoreCutouts` | Method | `FactoryWalls`, `Fence`, `Mezzanine` |
| `WallThickness` | Attribute | `Box`, `FactoryWalls` |

## Attributes and Methods

### `importGraphics` (method)

Imports an external graphic (e.g. JT, DWG) into the designated graphic.

- **Default parameter value:** `false`
- **Return value:** data type `any` — the created graphic (compare `_3D.getGraphic`)

```simtalk
var g := Station._3D.getGraphic("default").importGraphics("C:\Program Files\Siemens\Plant Simulation 2606\3D\jt-graphics\Robot Kuka.jt", true, true)
g.Position.Z := 3
g.Name := "RobotKuka"
myFrame._3D.getGraphic("deco").importGraphics("D:\\MyDWGFolder\\myLayout.dwg")
```

### `Dimensions` — barred area

Sets the dimensions of the barred area graphic.

- **Applies to:** `BarredArea`
- **Syntax:** `<Path>.Dimensions:length[2]`
- **Assignment value:** array of `length` with two values — Dimension X and Dimension Y

```simtalk
MyFrame._3D.getGraphic("deco", [2]).Dimensions := [4, 5]
```

### `Dimensions` — graphic

Sets the dimensions of the graphic.

- **Applies to:** `Box`, `FactoryWalls`, `Fence`, `Mezzanine`, `Rack`
- **Syntax:** `<Path>.Dimensions:length[3]`
- **Assignment value:** array of `length` with three values — Dimension X, Y, Z
- **Note:** for type `Rack`, this sets the entire size of the rack

```simtalk
MyFrame._3D.getGraphic("deco", [2]).Dimensions := [4, 5, 2]
```

### `Form`

Sets the shape of the barred area.

- **Applies to:** `BarredArea`
- **Syntax:** `<Path>.Form:string`
- **Assignment value:** `"Rectangular"`, `"Rectangular with hatching"`, `"Round"`, or `"One-sided delimitation"`

```simtalk
var ba := Station._3D.getGraphic("default").createBarredArea([4, 4])
barredArea.Form := "One-sided delimitation"
```

### `HasCutouts` (read-only attribute)

Returns whether parts of the factory walls, fence, or mezzanine graphic are cut out.

- **Applies to:** `FactoryWalls`, `Fence`, `Mezzanine`
- **Syntax:** `<Path>.HasCutouts → boolean`
- **Return value:** `boolean`

```simtalk
print .Models.MyModel._3D.getGraphic("deco", [4]).HasCutouts
```

### `PlaceRemainder`

Sets where the remainder of the elements of the factory walls or fence is added. The remainder is the difference between the wall/fence length and the next lower multiple of the element width.

- **Applies to:** `FactoryWalls`, `Fence`
- **Syntax:** `<Path>.PlaceRemainder:string`

| Setting | Remainder is located |
| --- | --- |
| `"Clockwise"` | clockwise at the end of the wall |
| `"Counter-clockwise"` | counter-clockwise at the end of the wall |
| `"Top and left"` | at the top and the left end of the wall |
| `"Top and right"` | at the top and the right end of the wall |
| `"Bottom and left"` | at the bottom and the left end of the wall |
| `"Bottom and right"` | at the bottom and the right end of the wall |

- **Note:** changing this setting resets the cutouts.

```simtalk
MyStation._3D.getGraphic("default").createFactoryWalls([11,40,3], 42cm).PlaceRemainder := "Counter-clockwise"
MyStation1._3D.getGraphic("default").createFence([3,4,1], true, false).PlaceRemainder := "Top and left"
```

### `restoreCutouts` (method)

Restores the parts of the graphic that were cut out, returning them to the state before the cutouts.

- **Applies to:** `FactoryWalls`, `Fence`, `Mezzanine`
- **Remarks:** deactivates graphic inheritance; cannot be assigned if the graphic is an automatically generated graphic group or is located in one.
- **Syntax:** `<Path>.restoreCutouts -> boolean`
- **Return value:** `boolean`

```simtalk
print .Models.MyModel._3D.getGraphic("deco", [4]).restoreCutouts
```

### `WallThickness`

Sets the thickness of the walls of the graphic.

- **Applies to:** `Box`, `FactoryWalls`
- **Remarks:** cannot be assigned when the graphic is an automatically generated graphic group or is located in one; assigning deactivates graphic inheritance.
- **Syntax:** `<Path>.WallThickness:length`
- **Assignment value:** data type `length`

```simtalk
.Models.MyModel._3D.getGraphic("deco", [3]).WallThickness := 0.02
```

## Related Topics

- **Creation methods:** `createBarredArea`, `createBox`, `createFactoryWalls`, `createFence`, `createMezzanine`, `createRack`
- **Graphic access:** `_3D.getGraphic`
- **Graphic type:** `InternalGraphicType`
- **Optimization:** `optimizeByPruningTinyGraphics`, `optimizeByStructureFlattening`, `optimizeByVisibilityFilter`
- **Settings dialogs:** Barred Area Settings, Box Settings, Factory Walls Settings, Fence Settings, Mezzanine Settings, Rack Settings
- **Command:** Import Graphics
