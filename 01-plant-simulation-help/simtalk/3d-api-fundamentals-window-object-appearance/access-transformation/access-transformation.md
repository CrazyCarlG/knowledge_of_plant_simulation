# Access Transformation (3D API Fundamentals — Window, Object & Appearance)

Summary of the Plant Simulation SimTalk 3D API documentation for accessing objects and
transformation settings in 3D. All topics come from the file
`access-transformation.txtx` (Plant Simulation Help, pages 12-666 to 12-729).

---

## 1. Accessing Objects in 3D

SimTalk provides the following attributes and methods for accessing objects in 3D.

### `_3D.ShowUserDefinedAttributes`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.ShowUserDefinedAttributes:boolean`
- Shows (`true`) or hides (`false`) the user-defined attributes of the objects in the Frame designated by `<Path>`.

```simtalk
MyFrame._3D.ShowUserDefinedAttributes := false
```

### `_3D.addLengthOrientation`
- **Type:** Method
- **Syntax:** `<Path>._3D.addLengthOrientation`
- Makes a length-oriented object out of the object designated by `<Path>`.
- **Remarks:** Does not apply to existing length-oriented objects, MUs, Connectors, and Interfaces.

```simtalk
MyStation._3D.addLengthOrientation
```

### `_3D.addObject`
- **Type:** Method
- **Syntax:** `<Path>._3D.addObject(Name:string[, LengthOriented:boolean]) → any`
- Creates an animatable object for the object designated by `<Path>`.
- **Parameters:**
  - `Name` (string): name of the animatable object. Specify a name matching an animatable object in the object's origin to create an inheriting object (restores a deleted animatable object so it inherits again).
  - `LengthOriented` (boolean, optional): whether the animatable object is length-oriented.
- **Return Value:** the newly created object (data type `any`).

```simtalk
// adds an animatable object to the Station
var MyAnimatableObject := Station._3D.addObject("MyAnimatableObject")
// deletes the animatable object from the Station
MyAnimatableObject.delete
Station._3D.getObject("MyAnimatableObject").delete
// adds an animatable object to the Conveyor and makes it length-oriented
var MyAnimatableObject := Conveyor._3D.addObject("MyAnimatableObject", true)
```

### `_3D.Exists`
- **Type:** Read-only attribute
- **Syntax:** `<Path>._3D.Exists → boolean`
- Checks if the object designated by `<Path>` exists in 3D (`true`) or not (`false`).
- **Remarks:** A Connector in 3D only exists if its predecessor and successor exist in 3D.

```simtalk
if obj._3D.Exists
...
end
```

### `_3D.existsObject`
- **Type:** Method
- **Syntax:**
  - `<Path>._3D.existsObject(Name:string) → boolean`
  - `<Path>._3D.existsObject(Index:integer) → boolean`
- Checks if the animatable object designated by `<Path>` exists in 3D.

```simtalk
print basis._3D.existsObject("MyObject")
```

### `_3D.ExistsWithAnimation`
- **Type:** Read-only attribute
- **Syntax:** `<Path>._3D.ExistsWithAnimation → boolean`
- Returns whether the object exists in 3D and whether the respective animation function is activated.
- **Remarks:** For MUs the animation function is the MU Animation, for all other objects the States Animation. Does not apply to folders, Connectors, and Interfaces.

```simtalk
print MyStation._3D.ExistsWithAnimation
```

### `_3D.getAttribute`
- **Type:** Method
- **Syntax:** `<Path>._3D.getAttribute(AttributeName:string[, byRef Inherited:boolean, byRef CanInherit:boolean]) → any`
- Returns the value of the specified attribute. Also applies to animatable objects.
- **Parameters:**
  - `AttributeName` (string): the attribute name.
  - `Inherited` (boolean, optional, by reference): `true` if the attribute inherits its value.
  - `CanInherit` (boolean, optional, by reference): `true` if the attribute value can be inherited.

```simtalk
var inherited, canInherit : boolean
var pos := MyRobot._3D.getAttribute("Position", inherited, canInherit)
// inherited returns if the position can be inherited and canInherit if the attribute supports inheritance

var inherited : boolean
var pos := MyRobot._3D.getObject("Z").getAttribute("Position", inherited)
// inherited returns if the position is inherited

var AttrName : string := "ShowContent"
var zi := MyFrame._3D.getAttribute(AttrName)
```

### `_3D.getMUAnimationPosition`
- **Type:** Method
- Returns the position at which a MU would be animated under certain marginal conditions.
- Applies to length-oriented and point-oriented objects. If called on a simulation object, it evaluates `_3D.AnimationObject`; if called on the animatable object itself, only that object is considered.

**For length-oriented objects:**
- **Syntax:** `<Path>._3D.getMUAnimationPosition(RelPos/AbsPos:real/length[, Lane/Direction:integer:=1]) -> length[3]`
- `RelPos/AbsPos`: relative position (`real`, 0–1) or absolute position (`length`, distance from object start).
- `Lane/Direction` (integer, optional, default 1): for a TwoLaneTrack, 1 = lane A, 2 = lane B; for a Converter, 1 = default direction, 2 = cross-wise conveying.
- **Return Value:** array of `length` with three values.

```simtalk
var p := Converter._3D.getMUAnimationPosition(0.5, 2)
var p := Conveyor._3D.getMUAnimationPosition(1m)
```

**For point-oriented objects:**
- **Syntax:** `<Path>._3D.getMUAnimationPosition([X:integer:=1, Y:integer:=1]) -> length[3]`
- `X` / `Y` (integer, optional, default 1): processing place in X-/Y-direction (required for matrix loading space).

```simtalk
var p := Station._3D.getMUAnimationPosition()
var p := PlaceBuffer._3D.getMUAnimationPosition(4)
var p := ParallelStation._3D.getMUAnimationPosition(3,4)
// Compute the position of the MU on place (1,1) in the current frame:
var container := Station.Cont
var animPos   := Station.Cont._3D.getMUAnimationPosition(1,1)
print current._3D.getPositionOfObject(container, animPos)
```

### `_3D.getMUAnimationRotation`
- **Type:** Method
- Returns the rotation with which a MU would be animated under certain marginal conditions. Applies to length-oriented and point-oriented objects.

**For length-oriented objects:**
- **Syntax:** `<Path>._3D.getMUAnimationRotation(RelPos/AbsPos:real/length[, Lane/Direction:integer:=1]) -> real[4]`
- **Return Value:** array of `real` with four values.

```simtalk
var p := Converter._3D.getMUAnimationRotation(0.5, 2)
var p := Conveyor._3D.getMUAnimationRotation(1m)
```

**For point-oriented objects:**
- **Syntax:** `<Path>._3D.getMUAnimationRotation([X:integer:=1, Y:integer:=1]) -> real[4]`

```simtalk
var p := Station._3D.getMUAnimationRotation()
var p := PlaceBuffer._3D.getMUAnimationRotation(4)
var p := ParallelStation._3D.getMUAnimationRotation(3,4)
// Compute the rotation of the MU on place (1,1) in the current frame:
var container := Station.Cont
var animRot   := Station.Cont._3D.getMUAnimationRotation(1,1)
print current._3D.getrotationOfObject(container, animPos)
```

### `_3D.getObject`
- **Type:** Method
- **Syntax:**
  - `<Path>._3D.getObject(ObjectName:string)`
  - `<Path>._3D.getObject(ObjectIndex:integer)`
- Returns the designated inner object of the object designated by `<Path>`.

```simtalk
var o := Machine._3D.getObject("Arm")
// if ObjectName is a valid identifier, you can also type:
var o := Machine._3D.Arm
```

### `_3D.getPositionOfObject`
- **Type:** Method
- **Syntax:** `<Path>._3D.getPositionOfObject(Object:any[, Offset:length[3]]) → length[3]`
- Returns the position of the designated object in the coordinate system of the object designated by `<Path>`.
- **Parameters:**
  - `Object` (any): the object whose position you want to know.
  - `Offset` (length[3], optional): converts a coordinate within the passed object's coordinate system into the calling object's coordinate system.

```simtalk
// the part Part:1 is located on Transporter:2. The Transporter drives on .Models.Model.Track ...
Track._3D.getPositionOfObject(.MUs.Part:1) // returns the position of the Part relative to the object position of the Track
_3D.getPositionOfObject(.MUs.Part:1)       // returns the position of the Part relative to the Frame
.MUs.Transporter:2._3D.getPositionOfObject(Station) // returns the position .Models.Model.Station relative to .Transporter
// You can also specify simulation and 3D simulation objects and animatable objects.
.MUs.Transporter:2._3D.getPositionOfObject(Station._3D) // same as above
.MUs.Transporter:2._3D.getPositionOfObject(PickAndPlace._3D.getObject(1).getObject(1).getObject(1))
// returns the position of the ball joint of a four-axis robot relative to the Transporter
```

### `_3D.getRotationOfObject`
- **Type:** Method
- **Syntax:** `<Path>._3D.getRotationOfObject(Object:any) → real[4]`
- Returns the rotation of the designated object in the coordinate system of the object designated by `<Path>`.
- **Return Value:** array of `real` with four values — first value is the angle, remaining three are the rotation axis components.

```simtalk
print _3D.getRotationOfObject(Store)
```

### `_3D.hasAttribute`
- **Type:** Method
- **Syntax:** `<Path>._3D.hasAttribute(AttributeName:string) → boolean`
- Returns whether the simulation object has the named attribute.

```simtalk
print Store._3D.hasAttribute("StorageAreaMaterialShininess")
print Station._3D.getObject(1).hasAttribute("AnimationOffset")
print Conveyor._3D.hasAttribute("Imp")        -- returns false
print Conveyor._3D.hasAttribute("SetupImp")   -- returns false
print Conveyor._3D.hasAttribute("FailImp")    -- returns false
```

### `_3D.inheritAttribute`
- **Type:** Method
- **Syntax:** `<Path>._3D.inheritAttribute(AttributeName:string)`
- Turns inheritance of the designated attribute on if it was turned off. If several attributes are inherited together, all will be inherited.

```simtalk
Conveyor._3D.inheritAttribute("VisibleGraphicGroups")
Frame._3D.inheritAttribute("PlanningView")
// You can call the method for any of the view options.
// This turns inheritance of all view options on or off.
```

### `_3D.InternalClassType`
- **Type:** Read-only attribute
- **Syntax:** `<Path>._3D.InternalClassType -> string`
- Returns the built-in English name of the length-oriented object.
- **Return Values:**
  - `AnimatableExtrusionObject` / `SimulationExtrusionObject` — length-oriented object in 3D.
  - `AnimatableObject` / `SimulationObject` — point-oriented object in 3D.

```simtalk
var animObject : any := obj._3D.getObject(1)
if animObject.InternalClassType = "AnimatableExtrusionObject" then
   animObject.BaseHeight := 2
end
```

### `_3D.memUsage`
- **Type:** Method
- **Syntax:** `<Path>._3D.memUsage → integer`
- Computes how much memory the 3D part of the object uses.

```simtalk
print MyStation._3D.memUsage  -- might return 2665, i.e. 2.6 KB
print MyStation.memUsage      -- might return 4975, i.e. 4.9 KB
```

### `_3D.NumObjects`
- **Type:** Read-only attribute
- **Syntax:** `<Path>._3D.NumObjects → integer`
- Returns the number of animatable objects that are part of the object. Access them with `_3D.getObject`.

```simtalk
var obj := .Models.Model.MyStation._3D
for var i := 1 to obj.NumObjects
   print obj.getObject(i).Name
next
```

### `_3D.openDialog`
- **Type:** Method
- **Syntax:** `<Path>._3D.openDialog`
- Opens the dialog *Edit 3D Properties* of the object.

```simtalk
Buffer._3D.openDialog
```

### `_3D.openWindow`
- **Type:** Method
- **Syntax:** `<Path>._3D.openWindow`
- Opens the object in a new window in 3D.

```simtalk
MyFrame._3D.openWindow
```

### `_3D.removeLengthOrientation`
- **Type:** Method
- **Syntax:** `<Path>._3D.removeLengthOrientation`
- Makes the length-oriented object non-length-oriented.
- **Remarks:** Only applies to classes that do not inherit settings from another class.

```simtalk
MyStationLengthOriented._3D.removeLengthOrientation
```

### `_3D.Selected`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.Selected:boolean`
- Selects (`true`) or deselects (`false`) the object in 3D. Selects all simulation and animatable objects in all windows.

```simtalk
MyStation._3D.Selected := true
MyPickAndPlace._3D.getObject(1).Selected := true
```

### `delete` — animatable object
- **Type:** Method
- **Syntax:** `<PathToObjectToBeDeleted>.delete`
- Deletes the animatable object.
- **Remarks:** Can invalidate variables referencing neighboring or contained animatable objects.

```simtalk
var MyAnimatableObject := Station._3D.addObject("MyAnimatableObject")
MyAnimatableObject.delete
Station._3D.getObject("MyAnimatableObject").delete
```

### `Length` — animatable object
- **Type:** Attribute
- **Syntax:** `<Path>.Length:length`
- Sets the length of the animatable object. Can be set/get only if the object has a single straight-lined segment.
- **Note:** SimTalk 2.0 units: `m`, `mm`, `km`, `cm`, `yd`, `ft`, `in` (no separating blank, e.g. `10m`).

```simtalk
MyStation._3D.getObject(1).Length := 2m
```

### `Name` — animatable object
- **Type:** Attribute
- **Syntax:** `<Path>.Name:string`
- Sets the name of the animatable object.

```simtalk
PickAndPlace._3D.getObject(1).Name := "MyObject"
var n:string := PickAndPlace._3D.getObject(1).Name
```

---

## 2. Accessing Transformation Settings

SimTalk provides these attributes/methods for accessing the transformation of objects in 3D.
Access via `<Path>._3D.NameOfTheAttribute`, set via `<Path>._3D.NameOfTheAttribute := "MyString"`.

### `_3D.CornerPoints`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.CornerPoints:length[3,*]`
- Sets the intermediate anchor points of the Connector. Accepts a two-dimensional array of `length` with sequences of three values.

```simtalk
var cornerPoints := .Models.Model.Connector1._3D.CornerPoints
cornerPoints[3,1] := 4
.Models.Model.Connector1._3D.CornerPoints := cornerPoints
.Models.Model.Connector1._3D.CornerPoints[3,1] := 4
```

### `_3D.Dimensions` — simulation object
- **Type:** Attribute
- **Syntax:** `<Path>._3D.Dimensions:length[3]`
- Sets the dimensions of the scaled graphic of the simulation object and the non-length-oriented animatable object.
- **Remarks:** Cannot set dimensions for an object without graphics. Not provided by Part/Container/Transporter/Worker, Connector/Interface/Marker, length-oriented objects, Store, or Variable/Comment/Button/DropDownList/Checkbox/Display.

```simtalk
MyStation._3D.Dimensions := [3m, 2m, 2m]
```

### `_3D.getWorldCoordinate`
- **Type:** Method
- **Syntax:** `<Path>._3D.getWorldCoordinate([Offset:length[3]]) → length[3]`
- Returns the position of the object in the topmost Frame.
- **Parameter:** `Offset` (length[3], optional) — query the world coordinate of a coordinate within the object coordinate system.

```simtalk
print Store._3D.getWorldCoordinate(Store.getAnimationPoint(1, 1))
```

### `_3D.getWorldRotation`
- **Type:** Method
- **Syntax:** `<Path>._3D.getWorldRotation → real[4]`
- Returns the rotation of the object in the topmost Frame.
- **Return Value:** array of `real` with four values (angle + rotation axis components).

```simtalk
print Store._3D.getWorldRotation // might return [0, 0, 0, -1]
```

### `_3D.Mirror`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.Mirror:boolean/boolean[3]`
- Sets mirroring of the object on one or three planes.
- **Remarks:** Does not apply to existing length-oriented objects, MUs, or Connectors.
- **Assignment Value:**
  - Single `boolean`: mirror on the YZ-plane only.
  - `boolean[3]`: mirroring around the YZ-, XZ-, and XY-planes (in that order).

```simtalk
MyFrame._3D.Mirror := true
MyFrame._3D.Mirror := [true,false,true]
```

### `_3D.Position`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.Position:length[3]`
- Sets the current position of the object.
- **Remarks:** Does not apply to MU instances or Connector instances. For MU instances the position is computed by the animation.

```simtalk
MyFrame._3D.Position := [5,3,0]
```

### `_3D.Rotation`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.Rotation:real/real[4]`
- Sets the current rotation of the object.
- **Remarks:** For an MU instance, use `ConveyingDirection` for simulation-relevant rotation. For an AGV, use `setWorldPosition`'s `Angle` parameter.
- **Assignment Value:**
  - A number: rotation around the negative z-axis.
  - `real[4]`: rotation around the specified axis (values 2–4). Getting returns a 4-element array.

```simtalk
var a : any := MyStation._3D.Rotation
// returns an array of 4 values
MyStation._3D.Rotation := 30
// rotates the object by 30 degrees
MyStation._3D.Rotation := [45, 0, 1, 0]
// rotates the object by 45 degrees around the Y axis
```

### `_3D.Scale`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.Scale:real/real[3]`
- Sets the current scale of the object. Does not apply to Connectors.
- **Assignment Value:**
  - Single `real`: uniform scaling.
  - `real[3]`: different scaling factors for the three axes.

```simtalk
MyStation._3D.Scale := 1           // uniform scaling
MyStation._3D.Scale := [1, 4, 9]   // different scaling factors for the x-axis, y-axis and z-axis
```

### `_3D.ScaleAutomatically`
- **Type:** Attribute
- **Syntax:** `<MU-Path>._3D.ScaleAutomatically:boolean`
- Automatically scales the MU graphics (`true`) or not (`false`). Adjusts size and positioning to the MU's measurements and booking point.

```simtalk
.MUs.Part:1._3D.ScaleAutomatically := true
```

### `_3D.TransformationMatrix`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.TransformationMatrix → array`
- Sets the entire transformation of the object.
- **Remarks:** Accepts a one-dimensional array of `real` with 16 values or a two-dimensional array of `real` with 4×4 values. Available for all fully transformable objects. Assigning the attribute deactivates graphic inheritance.
- **Return Value:** always a 4×4 array.

### `F3DconcatenateRotations`
- **Type:** Method
- **Syntax:** `F3DconcatenateRotations(Rotation1:real[4], Rotation2:real[4]) → real[4]`
- Concatenates two rotations into one and returns the computed value.
- **Parameters:** each is an array of four `real` values (rotation angle + x/y/z components of the rotation axis).
- **Return Value:** array with four `real` values; corresponds to the input rotations executed one after the other.

```simtalk
Station._3D.Rotation := F3DconcatenateRotations(Station._3D.Rotation, [45, 0, 1, 0])
Station._3D.Rotation := F3DconcatenateRotations([90, 0, 1, 0], [45, 0, 1, 0])
```

---

## 3. Accessing Object Captions

### `_3D.NameLabelEnabled`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.NameLabelEnabled:boolean`
- Shows (`true`) or hides (`false`) the Name and Label of the object.
- **Remarks:** Assigning deactivates graphic inheritance. Underscores `_` in names are converted to spaces; underscores in labels are shown as underscores.

```simtalk
MyStation._3D.NameLabelEnabled := true
```

### `_3D.NameLabelPosition`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.NameLabelPosition:length/length[3]`
- Sets the reference point of the Name and Label. Assigning deactivates graphic inheritance.

```simtalk
MyStation._3D.NameLabelPosition := [-1, 1, 1]
```

### `_3D.NameLabelRotation`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.NameLabelRotation:real/real[4]`
- Sets the rotation of the Name and Label.

```simtalk
MyStation._3D.NameLabelRotation := 45              // degrees
MyStation._3D.NameLabelRotation := [45, 0, 1, 0]   // angle, components of the rotation axis
```

### `_3D.NameLabelScale`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.NameLabelScale:real/real[3]`
- Sets the scaling of the Name and Label. Assigning deactivates graphic inheritance.

```simtalk
MyStation._3D.NameLabelScale := [1, 0.7, 0.4]
```

---

## 4. Accessing the Background Color of Frame and Folder

### `_3D.BackgroundBrightness`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.BackgroundBrightness:real[4]`
- Sets the brightness of the four corners of the background color of the Frame/folder.
- **Assignment Value:** array of four `real` values between -1 and 1 (darker if < 0, brighter if > 0). Order: top right, top left, bottom right, bottom left.

```simtalk
MyFrame._3D.BackgroundColor := makeRGBValue(0,0,255)
MyFrame._3D.BackgroundBrightness := [1, 1, 1, 1]
```

### `_3D.BackgroundColor`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.BackgroundColor:integer`
- Sets the background color of the Frame/folder. Assign `-1` for no background color; usually set with `makeRGBValue`.

```simtalk
MyFrame._3D.BackgroundColor := makeRGBValue(0,0,255) // bright blue
print MyFrame._3D.BackgroundColor                    // returns 16711680
```

---

## 5. Accessing the Fill Level of the Buffer

### `_3D.FillLevelDimensions`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.FillLevelDimensions:length[2]`
- Sets the dimensions of the fill level display of the Buffer. First value = X-dimension, second = Y-dimension.

```simtalk
.Models.MyModel.MyBuffer._3D.FillLevelDimensions := [2, 2]
```

### `_3D.FillLevelPosition`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.FillLevelPosition:length[3]`
- Sets the position of the fill level display (X, Y, Z).

```simtalk
.Models.MyModel.MyBuffer._3D.FillLevelPosition := [0, 0, 0.5]
```

### `_3D.FillLevelRotation`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.FillLevelRotation:real/real[4]`
- Sets the rotation of the fill level display.
- **Assignment Value:**
  - A number: rotation around the negative z-axis.
  - `real[4]`: rotation angle + rotation axis components.

```simtalk
.Models.MyModel.MyBuffer._3D.FillLevelRotation := [0.5, 1, 0, 0]
```

### `_3D.ShowContentsAs`
- **Type:** Attribute
- **Syntax:** `<Path>._3D.ShowContentsAs:string`
- Sets how the Buffer shows its contents. Allowed values: `"MUs"`, `"Fill level"`, `"Both"`.

```simtalk
.Models.MyModel.MyBuffer._3D.ShowContentsAs := "Both"
```

---

## 6. Accessing the Bounding Box

Read-only attributes for measuring the bounding box of the visible graphics of an object.
- All data relate to the local object coordinate system.
- The bounding box excludes all invisible graphics.

**Relationships:**
- `(_3D.BoundingBoxMin + _3D.BoundingBoxMax) / 2` = `_3D.BoundingBoxCenter`
- `_3D.BoundingBoxMax - _3D.BoundingBoxMin` = `_3D.BoundingBoxSize`
- `_3D.BoundingBoxMax` must be ≥ `_3D.BoundingBoxMin`.

### `_3D.BoundingBoxCenter`
- **Type:** Read-only attribute
- **Syntax:** `<Path>._3D.BoundingBoxCenter → length[3]`
- Returns the center (X/Y/Z position) of the bounding box.

```simtalk
var a : real[3] := MyStation._3D.BoundingBoxCenter
```

### `_3D.BoundingBoxMax`
- **Type:** Read-only attribute
- **Syntax:** `<Path>._3D.BoundingBoxMax → length[3]`
- Returns the upper right vertex (X/Y/Z position) of the bounding box.

```simtalk
var a : length[3] := MyStation._3D.BoundingBoxMax
```

### `_3D.BoundingBoxMin`
- **Type:** Read-only attribute
- **Syntax:** `<Path>._3D.BoundingBoxMin → length[3]`
- Returns the lower left vertex (X/Y/Z position) of the bounding box.

```simtalk
var a : length[3] := MyStation._3D.BoundingBoxMin
```

### `_3D.BoundingBoxSize`
- **Type:** Read-only attribute
- **Syntax:** `<Path>._3D.BoundingBoxSize → array`
- Returns the size of the bounding box: length (X), width (Y), height (Z).
- **Remarks:** The bounding box encloses graphics and animatable objects; a Frame's box also encloses static simulation objects. MU instances do not belong to the transporting object's box.

```simtalk
var a : real[3] := MyStation._3D.BoundingBoxSize
```

---

## Source

- `Plant Simulation Help` — pages 12-666 to 12-729
- File: `access-transformation.txtx`
