# Shape Attributes

SimTalk provides attributes, read-only attributes, and methods for setting properties of shapes.

## importGraphics (method)

- **Default value of the parameter:** `false`
- **Return value:** data type `any` — designates the created graphic (compare `_3D.getGraphic`)

```simtalk
var g := Station._3D.getGraphic("default").importGraphics("C:\Program Files\Siemens\Plant Simulation 2606\3D\jt-graphics\Robot Kuka.jt", true, true)
g.Position.Z := 3
g.Name := "RobotKuka"
myFrame._3D.getGraphic("deco").importGraphics("D:\\MyDWGFolder\\myLayout.dwg")
```

**See also:** Import Graphics [command], `_3D.getGraphic`, `optimizeByPruningTinyGraphics`, `optimizeByStructureFlattening`, `optimizeByVisibilityFilter`

---

## Dimensions — barred area

Sets the dimensions of the graphic of the barred area designated by `<Path>`.

- **Remarks:** available for graphics of type `BarredArea` (compare `InternalGraphicType`)
- **Type:** Attribute
- **Syntax:** `<Path>.Dimensions:length[2]`
- **Assignment value:** array of data type `length` with two values — Dimension X and Dimension Y

```simtalk
MyFrame._3D.getGraphic("deco", [2]).Dimensions := [4, 5]
```

**See also:** Barred Area, Barred Area Settings, `InternalGraphicType`, `createBarredArea`, `X` (array), `Y` (array), `_3D.getGraphic`

---

## Dimensions — graphic

Sets the dimensions of the graphic designated by `<Path>`.

- **Remarks:** available for graphics of types `Box`, `FactoryWalls`, `Fence`, `Mezzanine`, and `Rack`
- **Type:** Attribute
- **Syntax:** `<Path>.Dimensions:length[3]`
- **Assignment value:** array of data type `length` with three values — Dimension X, Dimension Y, Dimension Z
- **Note:** for type `Rack` the attribute sets the entire size of the rack

```simtalk
MyFrame._3D.getGraphic("deco", [2]).Dimensions := [4, 5, 2]
```

**See also:** Box Settings, `createBox`, Factory Walls, Factory Walls Settings, `createFactoryWalls`, Fence Settings, `createFence`, Mezzanine Settings, `createMezzanine`, Rack Settings, `createRack`, `InternalGraphicType`, `X`/`Y`/`Z` (array), `_3D.getGraphic`

---

## Form

Sets the shape of the barred area designated by `<Path>`.

- **Remarks:** available for graphics of type `BarredArea`
- **Type:** Attribute
- **Syntax:** `<Path>.Form:string`
- **Assignment value:** string — `"Rectangular"`, `"Rectangular with hatching"`, `"Round"`, or `"One-sided delimitation"`

```simtalk
var ba := Station._3D.getGraphic("default").createBarredArea([4, 4])
// creates a rectangular barred area around the Station
var BarredArea := _3D.getGraphic("deco").createBarredArea([8, 6])
// the x dimension does not matter as long as it is not 0 as it
// will be discarded when the Form changes to "One-sided delimitation"
barredArea.Form := "One-sided delimitation"
```

**See also:** Barred Area, Barred Area Settings, `InternalGraphicType`, `createBarredArea`, `_3D.getGraphic`

---

## HasCutouts (read-only attribute)

Returns whether parts of the graphic of the factory walls, fence, or mezzanine designated by `<Path>` are cut out.

- **Remarks:** available for graphics of types `FactoryWalls`, `Fence`, and `Mezzanine`
- **Type:** Read-only attribute
- **Syntax:** `<Path>.HasCutouts → boolean`
- **Return value:** `boolean`

```simtalk
print .Models.MyModel._3D.getGraphic("deco", [4]).HasCutouts
```

**See also:** Factory Walls Settings, `createFactoryWalls`, Fence Settings, `createFence`, Mezzanine Settings, `createMezzanine`, `restoreCutouts`, `InternalGraphicType`, `_3D.getGraphic`

---

## PlaceRemainder

Sets where the remainder of the elements of the factory walls or fence designated by `<Path>` is added. The remainder is the difference between the length of the wall/fence and the next lower multiple of the element width.

- **Remarks:** available for graphics of types `FactoryWalls` and `Fence`
- **Type:** Attribute
- **Syntax:** `<Path>.PlaceRemainder:string`

| Setting | Remainder is located |
| --- | --- |
| `"Clockwise"` | clockwise at the end of the wall |
| `"Counter-clockwise"` | counter-clockwise at the end of the wall |
| `"Top and left"` | at the top and the left end of the wall (depends on the orientation of the wall) |
| `"Top and right"` | at the top and the right end of the wall (depends on the orientation of the wall) |
| `"Bottom and left"` | at the bottom and the left end of the wall (depends on the orientation of the wall) |
| `"Bottom and right"` | at the bottom and the right end of the wall (depends on the orientation of the wall) |

- **Note:** when you change the setting for placing the remainder, Plant Simulation resets the cutouts.

```simtalk
MyStation._3D.getGraphic("default").createFactoryWalls([11,40,3], 42cm).PlaceRemainder := "Counter-clockwise"
MyStation1._3D.getGraphic("default").createFence([3,4,1], true, false).PlaceRemainder := "Top and left"
```

**See also:** Factory Walls Settings, `createFactoryWalls`, Fence Settings, `createFence`, `restoreCutouts`, `InternalGraphicType`, `_3D.getGraphic`

---

## restoreCutouts (method)

Restores the parts of the graphic designated by `<Path>` that were cut out, returning them to the state before the cutouts.

- **Remarks:** available for graphics of types `FactoryWalls`, `Fence`, and `Mezzanine`. Assigning the method deactivates graphic inheritance. Cannot be assigned if the graphic is an automatically generated graphic group or is located in one.
- **Type:** Method
- **Syntax:** `<Path>.restoreCutouts -> boolean`
- **Return value:** `boolean`

```simtalk
print .Models.MyModel._3D.getGraphic("deco", [4]).restoreCutouts
```

**See also:** Factory Walls Settings, `createFactoryWalls`, Fence Settings, `createFence`, Mezzanine Settings, `createMezzanine`, `HasCutouts`, `InternalGraphicType`, `_3D.getGraphic`

---

## WallThickness

Sets the thickness of the walls of the graphic designated by `<Path>`.

- **Remarks:** available for graphics of types `Box` and `FactoryWalls`. Cannot be assigned when the graphic is an automatically generated graphic group or is located in one. Assigning the attribute deactivates graphic inheritance.
- **Type:** Attribute
- **Syntax:** `<Path>.WallThickness:length`
- **Assignment value:** data type `length`

```simtalk
.Models.MyModel._3D.getGraphic("deco", [3]).WallThickness := 0.02
```

**See also:** Factory Walls, `InternalGraphicType`, `createFactoryWalls`, `createBox`, `_3D.getGraphic`
