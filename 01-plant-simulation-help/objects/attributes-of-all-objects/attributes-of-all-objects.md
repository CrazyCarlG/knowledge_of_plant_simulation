# Attributes of All Objects

Plant Simulation objects expose predefined attributes that either configure behavior or report state. Most attributes can be read and assigned; **read-only attributes** can only be queried because their values are calculated when accessed. Use **Show Attributes and Methods** (Class Library context menu, or `F8` for an instance) to inspect an object's available attributes, read-only attributes, and methods.

```simtalk
MyStation.Pause := true
print MyStation.Pause
posit := MyStation.Cont.XPos
print Source.Empty
```

## Read-only attributes

| Attribute | Syntax and return type | Purpose |
| --- | --- | --- |
| `~` / `Location` | `<Path>.~` or `<Path>.Location -> object` | Returns the containing object. For an MU, this is the object on which it is currently located; for other objects it is normally the containing Frame. It returns `VOID` while a Worker or AGV is travelling. Both forms are watchable. |
| `Class` | `<Path>.Class -> object` | Returns the Class Library class from which the object was derived or instantiated. |
| `InternalClassType` | `<Path>.InternalClassType -> string` | Returns the unique built-in English object type, such as `Station`, `Buffer`, `Conveyor`, `Frame`, `Source`, `Transporter`, or `Worker`. It is not a localized display name. |
| `NumAttr` | `<Path>.NumAttr -> integer` | Returns the number of user-defined attributes. Attribute indexing begins with `1`; returns `0` when none exist. |
| `NumChildren` | `<Path>.NumChildren -> integer` | Returns the number of children that inherit settings from the object. |
| `Origin` | `<Path>.Origin -> object` | Returns the object from which this object was most recently derived. |
| `OriginRoot` | `<Path>.OriginRoot -> object` | Returns the root object in the inheritance chain. |
| `RootFrame` | `<Path>.RootFrame -> object` | Returns the highest Frame in the Frame hierarchy. Returns `VOID` if no root Frame exists, for example for a non-Frame class. |
| `UUID` | `<Path>.UUID -> string` | Returns the object's permanent universally unique identifier. |

```simtalk
print "shaft is located on:", @.~
print "shaft is located on:", @.Location

print Preparing.~
-- returns .Models.MyCarAssembly.PaintShop.PaintLine1

print .MUs.Part:9.Location
-- returns .Models.MyCarAssembly.PaintShop.PaintLine1.Preparing

if class_change
	current.Class.openDialog
end

print MyStation.InternalClassType
-- returns "Station"

var index: integer
for index := 1 to MyStation.NumAttr
	print MyStation.getAttrName(index)
next

print MyStation.NumChildren
print Transporter.NumChildren

if local_change
	current.openDialog
else
	current.Origin.openDialog
end

print Station2111111.OriginRoot
print MyDialog.RootFrame
print Station.UUID
```

## Table-valued attributes

Many attributes declared as `table` are returned as copies. Editing the retrieved table does **not** change the object. Assign the altered table back to the attribute to persist the changes.

```simtalk
var t: table[string,string,integer]
t := MyStation.ExitStrategyMUAttributeList
t.appendRow("Name", "A", 1)                 // internal data is unchanged
MyStation.ExitStrategyMUAttributeList := t  // write the data back
```

## General writable attributes

### 3D and identity

| Attribute | Syntax | Notes |
| --- | --- | --- |
| `Coordinate3D` | `<Path>.Coordinate3D: array` | Assign a three-element `length` array. It is not inherited and cannot be queried for MU instances. |
| `CreateIn3D` | `<Path>.CreateIn3D: boolean` | Controls whether the object is created in 3D. If it is `false` in the origin, it cannot be enabled in a descendant. Turning it off and on for a class restores the built-in 3D state and discards class-specific 3D changes. |
| `Label` | `<Path>.Label: string` | User-facing label; it may contain spaces and special characters and need not be unique. It can be shown in Frames and is used in some window titles. |
| `Name` | `<Path>.Name: string` | Unique object identifier within its Frame. It may contain letters, digits, and `_`, but cannot start with a digit. `EventController` and `Connector` cannot be renamed. After a rename, use the new name to address the object. |
| `RootFolder` | `<Path>.RootFolder: boolean` | Makes a Class Library folder a root considered by the `rootfolder` anonymous identifier. |

`Label` and `Name` are watchable attributes.

```simtalk
MyStation.Coordinate3D := [-10, 11, 0]
print MyStation.Coordinate3D

MyStation.CreateIn3D := true

print MyStation.Label
Station1.Label := "Lathe left"

print MyStation.Name
Station1.Name := "shaft"

.ApplicationObjects.Transport.RootFolder := true
```

## Control attributes

Control attributes hold a method reference. Assign `&Method` or `PathToMethod.&Method`; a relative method path can also be supplied as a string. Assign `void` to disable a control. Availability depends on the object type.

### Lifecycle, structure, and user interaction

| Control | Invocation and parameters |
| --- | --- |
| `AvailableCtrl` | Called when an `Exporter` or `Worker` becomes available. `?` refers to the triggering object. |
| `NotAvailableCtrl` | Called when an `Exporter` or `Worker` becomes unavailable. `?` refers to the triggering object. |
| `ChangePathCtrl` | Called for contained objects when a containing Folder or Frame is renamed or moved. Parameters: `oldPath, newPath: string, manually: boolean`. `@` refers to a renamed object and `?` to a moved object. Moving between Frames may recreate an object rather than physically move it. |
| `CloseCtrl` | Called when an object window closes. It receives a `boolean` indicating whether the window contents changed. |
| `ConnectCtrl` | Called when a Connector is created or removed. Receives source, destination, and connection state. For creation, the Connector is supplied; when removing it, `VOID` is supplied. Connector controls run first on creation; on deletion, connected-object controls run before the destructor control. |
| `ConstructorCtrl` | Called after an object is duplicated, derived, or instantiated. An optional `onCreate3D: boolean` is `true` when the 3D part is created and `false` otherwise. |
| `DestructorCtrl` | Called while an object still exists, immediately before deletion. Subframe contents are also processed. |
| `DragDropCtrl` | Called for an object receiving dropped objects or text inside a Frame. Point-oriented objects receive `draggedObjects: object[]`. Length-oriented objects may also receive `dropPosition`; a `TwoLaneTrack` may additionally receive `dropLane`. |
| `MoveInFrameCtrl` | Called when an object actually changes position inside its Frame. Parameters: old and new three-element `length` arrays. `?` is the moved object. |
| `MoveToFolderCtrl` | Called when an object moves from a Folder or Frame to another Folder. Parameters: `oldFolder, newFolder: string, manually: boolean`; `?` is the moved object and `@` is its new location. |
| `OpenCtrl` | Replaces normal dialog opening with custom code. Optional parameters are `from3D: boolean` and `inLockedFolder: boolean`. Hold `Alt` while opening to bypass it unless an encrypted user-defined method is used. |
| `PermitDeleteCtrl` | Available only on `Frame` and `Folder`. Return `false` to reject deletion or `true` to allow deletion; a configured destructor then runs. |
| `PlausibilityCtrl` | Called on Apply/OK to validate or interpret dialog input. For lists/tables, `column, row: integer` allows per-cell validation; `-1, -1` is passed when a changed table is closed. |
| `RelabelCtrl` | Called when `Label` changes, first on the relabeled object and then on inheriting objects. Parameters: `currentLabel, newLabel: string, manually: boolean`. |
| `RenameCtrl` | Called when `Name` changes, first on the renamed object and then on inheriting objects. Parameters: `currentName, newName: string, manually: boolean`. It is not called for the initial rename performed when inserting an object into a Frame. |
| `SelectCtrl` | Called when the object is left-clicked; the object is not selected automatically, so the control must perform the desired action. It also works in 3D; use `Ctrl` while clicking to bypass the control. |

```simtalk
MyExporter.AvailableCtrl := &myAvailableCtrl
MyExporter.NotAvailableCtrl := &myNotAvailableCtrl

ParallelStation.ChangePathCtrl := &myChangePathCtrl
param oldPath, newPath: string, manually: boolean
print oldPath
print newPath
print manually

MyFrame.CloseCtrl := &myCloseCtrl

MyStation.ConnectCtrl := &myConnectCtrl
param connectionStart, connectionEnd: object, connectionEstablishedDeleted: boolean
if connectionEstablishedDeleted
	print "New"
else
	print "Deleted"
end
print "from:", connectionStart, " to:", connectionEnd

MyStation.ConstructorCtrl := &myConstructorMethod
MyStation.DestructorCtrl := &myDestructorMethod

MyStation.DragDropCtrl := &myDragAndDrop
param draggedObjects: object[]
var obj: object
for var i := 1 to draggedObjects.dim
	obj := draggedObjects[i]
	print i, ": ", draggedObjects[i]
next

param droppedObjects: object[], dropPosition: any := void, lane: any := void
// @, ?: drop target
if lane = void
	if dropPosition /= void
		?.createSensor(dropPosition, "Length", void, true, false)
	end
else
	if lane = "A"
		?.A.createSensor(dropPosition, "Length", void, true, false)
	else
		?.B.createSensor(dropPosition, "Length", void, true, false)
	end
end

MyStation.MoveInFrameCtrl := &myMoveInFrameCtrl
param old, new: length[3]
print "xv:", old[1], " yv:", old[2], " zv:", old[3], " xn:", new[1], " yn:", new[2], " zn:", new[3]

MySource.MoveToFolderCtrl := &MoveToFolderCtrl
param oldFolder, newFolder: string, manually: boolean
// @: new folder; ?: moved object

MyStation.OpenCtrl := void
MyParallelStation.OpenCtrl := &myOpenControl
param from3D: boolean
var passwordHash: string := computeSHA1Hash(prompt("Password:"))
if passwordHash = "686483805ac47ca14e03514f7481a7973b401762"
	if from3D
		?._3D.openWindow
	else
		?.openDialog
	end
end

Frame.PermitDeleteCtrl := &myPermitDeleteCtrl

MyStation.PlausibilityCtrl := &myPlausibilityCtrl
param column, row: integer
switch column
case 1
	// column-specific action
end

MyStation.RelabelCtrl := void
param currentLabel, newLabel: string, manualRename: boolean
print currentLabel
print newLabel
print manualRename

MyStation.RenameCtrl := &myRenameCtrl
param currentName, newName: string, manualRename: boolean
print currentName
print newName
print manualRename

MyStation.SelectCtrl := .Tools.&mySelectCtrl
print @.Selected
@.Selected := true
```

### Simulation state controls

| Control | Invocation and behavior |
| --- | --- |
| `FailCtrl` | Called when the `Failed` state changes. Optional parameters are `failureStartEnd: boolean` and `failureProfileName: string`. If the method declares the profile name, it is called for every profile failure/removal, even if the overall failed state stays unchanged. `?` is the affected object. |
| `InitCtrl` | Called once during the init phase, before object initialization, other init controls, and initial event calculation. Use it for setup that must occur before events are generated. |
| `PauseCtrl` | Called when the paused state changes. With `duration: real, newValue: boolean`, it is called only for ShiftCalendar changes and the method must set `?.Pause` itself. `duration` is `-1` when unknown or at the end of a pause. Without parameters, it runs for every state change. |
| `UnplannedCtrl` | Equivalent to `PauseCtrl` for the `Unplanned` state set by a ShiftCalendar. With `duration: real, newValue: boolean`, the method must set `?.Unplanned`; without parameters it runs for every state change. |

```simtalk
.MUs.Transporter.FailCtrl := &myFailCtrl
if ?.Failed
	if ?.Occupied and (not ?.Cont.Finished)
		?.Imp.releaseExporters
	end
else
	if ?.Occupied and (not ?.Cont.Finished)
		?.Imp.import
	end
end

.MUs.Transporter.InitCtrl := &myInitCtrl
M1.setupFor("C", false)
M2.setupFor("B", false)
M3.setupFor("A", false)
M1._3D.getObject("SetupType").setGraphicMaterial([1], ~.UserObjects.C._3D.MaterialDiffuseColor, 0, 0, 0, 0, 0)
M2._3D.getObject("SetupType").setGraphicMaterial([1], ~.UserObjects.B._3D.MaterialDiffuseColor, 0, 0, 0, 0, 0)
M3._3D.getObject("SetupType").setGraphicMaterial([1], ~.UserObjects.A._3D.MaterialDiffuseColor, 0, 0, 0, 0, 0)

param duration: real, newValue: boolean
if ?.Cont /= void
	wait ?.Cont.RemainingProcTime
end
?.Pause := newValue

Transporter.PauseCtrl := &myPauseCtrl
print "Current pause ", current.Pause
MyStation.Pause := current.Pause
var shift := root.ShiftCalendar.GetCurrShift
print "Current shift: ", shift
if not current.Unplanned
	if current.Pause
		current.CurrIcon := "pause"
	else
		current.CurrIcon := "working"
	end
end

param duration: real, newValue: boolean
if ?.Cont /= void
	wait ?.Cont.RemainingProcTime
end
?.Unplanned := newValue

MyStation.UnplannedCtrl := &myUnplannedCtrl
if current.Unplanned
	current.CurrIcon := "unplanned"
else
	if current.Pause
		current.CurrIcon := "pause"
	else
		current.CurrIcon := "working"
	end
end
```

## User-defined attribute metadata

User-defined attribute settings are accessed as subattributes, for example `MyStation.myAttribute.Alignment := "Left"`. Settings that change metadata, including `DataType` and `Name`, apply only to non-inherited attributes where stated.

| Attribute | Syntax | Purpose and valid values |
| --- | --- | --- |
| `Alignment` | `<Path>.<Attribute>.Alignment: string` | Text alignment: `"Left"`, `"Name"`, `"Value"`, or `"Right"`. |
| `asString` | `<Path>.<Attribute>.asString -> string` | Read-only string representation. Particularly useful for object attributes because it preserves a stored relative path. |
| `BackgroundColor` | `<Path>.<Attribute>.BackgroundColor: integer` | 3D text background color; use `makeRGBValue`. |
| `Color` | `<Path>.<Attribute>.Color: integer` | 3D value/font color; use `makeRGBValue`. |
| `DataType` | `<Path>.<Attribute>.DataType: string` | Sets the type of a non-inherited user-defined attribute. |
| `DecimalPlaces` | `<Path>.<Attribute>.DecimalPlaces: integer` | 3D fractional display precision. `-1` shows all available digits (for time, its default display applies); up to 15 places. Applies to real, length, money, weight, time, speed, and acceleration. |
| `Font` | `<Path>.<Attribute>.Font: integer` | 3D font size: `1` small, `2` medium, `3` large, `4` extra large. |
| `HasInitValue` | `<Path>.<Attribute>.HasInitValue: boolean` | Enables or disables an initial value. |
| `InitValue` | `<Path>.<Attribute>.InitValue: any` | Value restored during reset and the next initialization phase. Not available for table, list, stack, queue, randTime, or method attributes. |
| `IntegerPlaces` | `<Path>.<Attribute>.IntegerPlaces: integer` | Minimum number of integer positions in the 3D display. `-1` applies no minimum; up to 15. Applies to integer, real, length, money, weight, time, speed, acceleration, and randTime. |
| `Name` | `<Path>.<Attribute>.Name: string` | Renames a non-inherited user-defined attribute. |
| `Position` | `<Path>.<Attribute>.Position: length[3]` | 3D X/Y/Z position. Does not apply to MU or Connector instances. |
| `Rotation` | `<Path>.<Attribute>.Rotation: real / real[4]` | A number rotates around the negative Z-axis; a four-element array specifies angle and axis. Reading returns a four-element array. |
| `Scale` | `<Path>.<Attribute>.Scale: real / real[3]` | Uniform scale or independent X/Y/Z scale. Does not apply to Connectors. |
| `ShowDataType` | `<Path>.<Attribute>.ShowDataType: boolean` | Shows/hides the data type in the 3D Frame. |
| `ShowExternally` | `<Path>.<Attribute>.ShowExternally: boolean` | Shows the attribute in the object's external representation; `false` uses its internal representation. |
| `ShowIn3D` | `<Path>.<Attribute>.ShowIn3D: boolean` | Shows/hides the attribute in 3D. |
| `ShowInTooltip` | `<Path>.<Attribute>.ShowInTooltip: boolean` | Shows the attribute name and value in the object tooltip. |
| `ShowName` | `<Path>.<Attribute>.ShowName: boolean` | Shows/hides the attribute name. |
| `ShowUnit` | `<Path>.<Attribute>.ShowUnit: boolean` | Shows/hides units in the Frame. |
| `StatisticsActive` | `<Path>.<Attribute>.StatisticsActive: boolean` | Enables/disables statistics collection for the attribute. |
| `Transparent` | `<Path>.<Attribute>.Transparent: boolean` | Makes its 3D background transparent; `false` uses a white background. |

```simtalk
MyStation.myAttribute.Alignment := "Left"

Station5.ObjAttribute := "~.ProdMgr.prodplan"
var a1 := Station5.ObjAttribute
// assigns .Models.Model.ProdMgr.prodplan
var a2 := Station5.&ObjAttribute.asString
// assigns "~.ProdMgr.prodplan"

MyStation.myAttribute.BackgroundColor := makeRGBValue(100, 100, 100)
MyStation.myAttribute.BackgroundColor := 6579300
MyStation.myAttribute.Color := makeRGBValue(0, 255, 0)

MyStation.myAttribute.DataType := "String"
MyStation.myAttribute.DecimalPlaces := 8
MyStation.myAttribute.Font := 2

MyStation.myAttribute.DataType := "integer"
MyStation.myAttribute.HasInitValue := true
MyStation.myAttribute.InitValue := 12

MyStation.myAttribute.IntegerPlaces := 6
-- "123"     displays as "   123"
-- "123456"  displays as "123456"
-- "1234567" displays as "1234567"

MyStation.myAttribute.Name := "MyNewName"
MyStation.myAttribute.Position := [5, 3, 0]

var a: any := MyStation.myAttribute.Rotation
// returns an array of 4 values
MyStation.myAttribute.Rotation := 30
MyStation.myAttribute.Rotation := [45, 0, 1, 0]

MyStation.myAttribute.Scale := 1
MyStation.myAttribute.Scale := [1, 4, 9]

MyStation.myAttribute.ShowDataType := false
MyStation.myAttribute.ShowExternally := false
MyStation.myAttribute.ShowIn3D := true
MyStation.myAttribute.ShowInTooltip := true
MyStation.myAttribute.ShowName := true
MyStation.myAttribute.ShowUnit := true
MyStation.myAttribute.StatisticsActive := true
MyStation.myAttribute.Transparent := true
```
