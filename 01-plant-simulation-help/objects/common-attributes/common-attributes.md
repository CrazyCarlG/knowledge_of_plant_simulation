# Common Attributes — Objects Reference

This document summarizes attributes that are common to all Plant Simulation objects (Class Library objects). It covers the **general attributes**, **control-method attributes**, and **attributes of user-defined attributes** used in SimTalk, plus the introductory section describing how object attributes are addressed, set, and queried.

Each entry preserves the original SimTalk code samples so you can use them as starting points.

> Source: *Plant Simulation Help* (Unpublished work. © 2026 Siemens). Pages referenced: 11-748 … 11-821.

---

## Table of Contents

- [1. UUID [SimTalk]](#uuid-simtalk)
- [2. Attributes of All Objects — Overview](#2-attributes-of-all-objects--overview)
- [3. Data Held in Tabular Form in Attributes](#3-data-held-in-tabular-form-in-attributes-material-flow-objects)
- [4. General Attributes](#4-general-attributes)
  - [Coordinate3D](#coordinate3d-simtalk--general-description)
  - [CreateIn3D](#createin3d-simtalk)
  - [Label](#label-simtalk)
  - [Name](#name-simtalk--general-description)
  - [RootFolder](#rootfolder-simtalk--attribute)
- [5. Attributes of the Controls](#5-attributes-of-the-controls)
  - [AvailableCtrl](#availablectrl-simtalk)
  - [ChangePathCtrl](#changepathctrl-simtalk)
  - [CloseCtrl](#closectrl-simtalk)
  - [ConnectCtrl](#connectctrl-simtalk)
  - [ConstructorCtrl](#constructorctrl-simtalk)
  - [DestructorCtrl](#destructorctrl-simtalk)
  - [DragDropCtrl](#dragdropctrl-simtalk)
  - [FailCtrl](#failctrl-simtalk)
  - [InitCtrl](#initctrl-simtalk--general-description)
  - [MoveInFrameCtrl](#moveinframectrl-simtalk)
  - [MoveToFolderCtrl](#movetofolderctrl-simtalk)
  - [NotAvailableCtrl](#notavailablectrl-simtalk)
  - [OpenCtrl](#openctrl-simtalk)
  - [PauseCtrl](#pausectrl-simtalk)
  - [PermitDeleteCtrl](#permitdeletectrl-simtalk)
  - [PlausibilityCtrl](#plausibilityctrl-simtalk)
  - [RelabelCtrl](#relabelctrl-simtalk)
  - [RenameCtrl](#renamectrl-simtalk)
  - [SelectCtrl](#selectctrl-simtalk)
  - [UnplannedCtrl](#unplannedctrl-simtalk)
- [6. Attributes of User-defined Attributes](#6-attributes-of-user-defined-attributes)
  - [Alignment, asString, BackgroundColor, Color, DataType, DecimalPlaces, Font, HasInitValue, InitValue, IntegerPlaces, Name, Position, Rotation, Scale, ShowDataType, ShowExternally, ShowIn3D, ShowInTooltip, ShowName, ShowUnit, StatisticsActive, Transparent](#userdefined-attribute-attributes)
- [7. Methods of the Material Flow Objects — Introduction](#7-methods-of-the-material-flow-objects--introduction)

---

## UUID [SimTalk]

Returns the UUID (Universally Unique Identifier) of the object designated by `<Path>`. The UUID remains constant during the object's entire lifetime.

- **Type:** read-only attribute
- **Syntax:** `<Path>.UUID → string`

```simtalk
print Station.UUID
// returns 3daf7c80-9411-4671-966f-f3ecd2c0f478 for example
```

---

## 2. Attributes of All Objects — Overview

Objects in the Class Library have predefined attributes that control their behavior or represent their state.

- In dialog windows, you configure object attributes via check boxes, text boxes, and drop-down lists on the object's tabs.
- In SimTalk, you assign values to the corresponding attributes directly.
- Most attributes are both **settable** and **gettable**. Some attributes are **read-only** (you can only query their value).

```simtalk
-- Set the value of an attribute
MyStation.Pause := true

-- Get the value of an attribute
print MyStation.Pause
posit := MyStation.Cont.XPos
```

Filter the displayed attributes and methods using the toolbar in *Show Attributes and Methods*. A dedicated filter shows only read-only attributes.

You can view all methods, read-only attributes, and attributes of an object via the **Show Attributes and Methods** window:

- Right-click a Class Library entry → **Show Attributes and Methods** (shows the Class [general description]).
- Press **F8** in a Frame, or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which the instance was inserted (shows the Instance [general description]).

### See also
- _General Attributes
- _Attributes of the Controls
- _Attributes of User-defined Attributes

---

## 3. Data Held in Tabular Form in Attributes [material flow objects]

Plant Simulation does **not** save table-typed attribute data in a fully fledged table internally.

- When you **get** the value of such an attribute, the internally held data is copied into a table and that table is returned. Modifying the returned table **does not** affect the internal data.
- To change the internal data, **assign** a table to the attribute. The data is then copied back into the attribute.

This applies to lists and tables on the **Exit** tabs of material flow objects, the **Exit Strategy / Entry Strategy** tabs of `FlowControl`, and other tables opened via *Open List / Open Table*.

```simtalk
var t:table[string,string,integer]
t := MyStation.ExitStrategyMUAttributeList
t.appendRow("Name", "A", 1)                  -- the internal data remains unchanged
MyStation.ExitStrategyMUAttributeList := t    -- writes data back into the attribute
```

---

## 4. General Attributes

The objects provide the following general attributes (see TOC above).

Use *Show Attributes and Methods* to view the complete list for any object.

```simtalk
MyStation.Pause := true        -- set
print MyStation.Pause          -- get
posit := MyStation.Cont.XPos   -- get
```

### Coordinate3D [SimTalk] — general description

Sets the 3D coordinate of the object designated by `<Path>`.

- **Remarks:** the attribute is not inherited. You cannot query Coordinate3D for MU instances.
- **Type:** attribute
- **Syntax:** `<Path>.Coordinate3D:array`

```simtalk
MyStation.Coordinate3D := [-10, 11, 0]
print MyStation.Coordinate3D   // returns [-10, 11, 0]
```

**See also:** `_3D.inheritAttribute`, `_3D.getPositionOfObject`, `_3D.getWorldCoordinate`.

### CreateIn3D [SimTalk]

Sets whether Plant Simulation creates the object in 3D (`true`) or not (`false`).

By default this is enabled for all simulation-relevant objects (material flow, fluid, moving, resource, and tool objects). When inserting such an instance into the 3D Scene, its icon is shown.

> If you deactivate the attribute for an object class and reactivate it, the built-in state is restored — any user changes to the 3D simulation object are discarded.
>
> If the origin's `CreateIn3D` is `false`, the resulting object also has `CreateIn3D = false` and cannot be re-enabled.

- **Type:** attribute
- **Syntax:** `<Path>.CreateIn3D:boolean`

```simtalk
MyStation.CreateIn3D := true
```

### Label [SimTalk]

Sets the label of the object designated by `<Path>`.

- Allowed characters: letters, numbers, blanks, and special characters.
- Use the label to display objects with the same functionality under the same identifier in the Frame; **the Name must still be unique**.
- Enabled via **Options → Show Object Labels** on the View ribbon tab.
- For `Report`, `Dialog`, `AttributeExplorer`, and `Chart` objects, the label is shown in the title bar (the object's name is shown when no label is entered).
- The same applies to toolbars added to the Toolbox.
- **Type:** attribute (watchable)
- **Syntax:** `<Path>.Label:string`

```simtalk
print MyStation.Label
Station1.Label := "Lathe left"
```

### Name [SimTalk] — general description

Sets the name of the object designated by `<Path>`.

- The name must be unique within the Frame's namespace.
- Allowed characters: letters, digits, and underscore (`_`). Names cannot start with a digit.
- You cannot rename the `EventController` or `Connector`.
- After renaming, address the object only by its new name.
- **Type:** attribute (watchable)
- **Syntax:** `<Path>.Name:string`

```simtalk
print MyStation.Name
Station1.name := "shaft"
```

**See also:** `setName`, `isNameUnique`, Name [general description], Namespace.

### RootFolder [SimTalk] — attribute

Sets whether the anonymous identifier `rootFolder` takes the folder designated by `<Path>` into account when searching the Class Library (`true`) or not (`false`).

- Sets which folder Plant Simulation uses as the root folder (a capital **R** appears on the folder icon in the Class Library).
- Can also be set in *Show Attributes and Methods*.
- **Type:** attribute
- **Syntax:** `<Path>.RootFolder:boolean`

```simtalk
.ApplicationObjects.Transport.RootFolder := true
```

**See also:** *Set the Root Folder for Your Simulation Model*, `rootfolder` (anonymous identifier).

---

## 5. Attributes of the Controls

Most objects provide some/all of the attributes listed below to bind control methods. The method being assigned has the data type `method`. Use `&Method` or `PathToMethod.&Method` to assign an object reference to a method, a string for a relative path, or `VOID` to deactivate the control. **Not all objects provide every control.**

> The expressions `&Method` or `PathToMethod.&Method` both assign an object reference to a method. Use a string to assign the relative path to a method. Specify `void` to deactivate a control.

Use **Show Attributes and Methods** to inspect which controls a given object exposes.

```simtalk
MyStation.Pause := true        -- set
print MyStation.Pause          -- get
posit := MyStation.Cont.XPos   -- get
```

### AvailableCtrl [SimTalk]

Designates a Method object of `<Path>`. Called by Plant Simulation whenever the state of the Exporter or Worker changes to *available*. Within the control you can use the anonymous identifier `?` to access the triggering object.

- **Type:** attribute
- **Syntax:** `<Path>.AvailableCtrl:method`

```simtalk
MyExporter.AvailableCtrl := &myAvailableCtrl
```

### ChangePathCtrl [SimTalk]

Designates a Method object of `<Path>`. Plant Simulation executes the Change Path Control:

- When the name of the Folder/Frame changes (called for all contained objects; `@` points to the renamed object).
- When the Folder/Frame is moved (called for all contained objects; `?` gives the moved object).

> A `Move` from one Frame to another actually deletes and re-creates the object. Specify `""` as the new location to interpret it as the top level of the object hierarchy.

- **Parameters:** `oldPath: string, newPath: string, manually: boolean`

```simtalk
ParallelStation.ChangePathCtrl := &myChangePathCtrl
```

```simtalk
param oldPath, newPath: string, manually: boolean
print oldPath
print newPath
print manually
```

### CloseCtrl [SimTalk]

Called when the window of the object is closed.

- **Parameter:** `boolean` indicating whether the contents have changed.

```simtalk
MyFrame.CloseCtrl := &myCloseCtrl
```

### ConnectCtrl [SimTalk]

Called when the object is connected to another via a Connector, or when that connection is deleted.

> Inserting a Connector triggers the Connect Control of the Connector first, then the Connect Controls of the connected objects. Deleting a Connector triggers the Connect Control of the connected objects first, then the Destructor Control.

- **Parameters (three parameters required):**
  - `predecessor: object` — source of the connection
  - `successor: object` — destination of the connection
  - `connectorEstablished: boolean` — true = connection created, false = connection deleted

```simtalk
MyStation.ConnectCtrl := &myConnectCtrl
```

```simtalk
param ConnectionStart, ConnectionEnd: object, ConnectionEstablishedDeleted: boolean
if ConnectionEstablishedDeleted
   print "New"
else
   print "Deleted"
end
print "from:", ConnectionStart, " to:", ConnectionEnd
```

> If an external Frame Interface is connected, the Interface is passed to the `predecessor`/`successor` parameter.

### ConstructorCtrl [SimTalk]

Called when the object is duplicated, derived, or instantiated (inserted into a Frame or simulation model).

- **Optional parameter:** `onCreate3D: boolean` — if declared, the control is also called a second time when the 3D part is created (with `true`).
- The object already exists by the time the control runs.

```simtalk
MyStation.ConstructorCtrl := &myConstructorMethod
```

### DestructorCtrl [SimTalk]

Called when the object is deleted. When a Frame contains Sub-Frames and objects, Destructor Controls in these Frames are called as well. **The object still exists** when its control runs.

> Plant Simulation calls a Connect Control *before* a Destructor Control.

```simtalk
MyStation.DestructorCtrl := &myDestructorMethod
```

### DragDropCtrl [SimTalk]

Called when an object (or text) is dragged and dropped onto the object designated by `<Path>`. **Only works in a Frame**, not in the Class Library.

For point-oriented objects:

```simtalk
param draggedObjects: object[]
-- one-dimensional array with n objects
-- the size of which can change
var obj: object
-- @,?: drop target
for var i := 1 to draggedObjects.dim
   obj := draggedObjects[i]
   -- enter your source code here
   print i, ": ", draggedObjects[i]   -- prints dragged objects to the Console
next
```

For length-oriented objects, the control additionally exposes `dropPosition: length` (drop distance from the start of the length-oriented object) and, on `TwoLaneTrack`, `dropLane: string` (`"A"` or `"B"`).

Sensor example that creates a sensor at the drop position:

```simtalk
param droppedObjects: object[], dropPosition: any := void, lane: any := void
-- @,?: drop target
if lane = void
   if dropPosition /= void    -- length-oriented object
      ?.createSensor(dropPosition, "Length", void, true, false)
   end
else                          -- TwoLaneTrack
   if lane = "A"
      ?.A.createSensor(dropPosition, "Length", void, true, false)
   else
      ?.B.createSensor(dropPosition, "Length", void, true, false)
   end
end
```

```simtalk
MyStation.DragDropCtrl := &myDragAndDrop
```

### FailCtrl [SimTalk]

Called when the *Failed* state of the object changes (via the dialog control or by assigning to the `Failed` attribute). Inside the control, `?` references the triggering object.

- **Optional parameters:**
  - `FailureStartEnd: boolean` — true = failure starts, false = failure ends
  - `FailureProfileName: string` — name of the failure profile that triggered the failure

> If both parameters are declared, the control fires for every state change *and* every failure-profile change. With no/one parameter, it fires only when the object's *overall* state changes.

```simtalk
.MUs.Transporter.FailCtrl := &myFailCtrl
```

```simtalk
if ?.failed
    if ?.occupied and (NOT ?.cont.finished)
        ?.imp.releaseExporters
    end
else
    if ?.occupied and (NOT ?.cont.finished)
        ?.imp.import
    end
end
```

### InitCtrl [SimTalk] — general description

Called **once at the beginning of the simulation run during the init phase**, before the object is initialized and before the init controls execute.

Useful for initializing transporters, populating the `Workers to Create` table of a `WorkerPool`, and configuring attributes that affect event generation (e.g. Availability). The Init Controls execute before events are computed — regular init methods execute afterwards.

```simtalk
.MUs.Transporter.InitCtrl := &myInitCtrl
M1.setupFor("C", false)
M2.setupFor("B", false)
M3.setupFor("A", false)
M1._3D.getObject("SetupType").setGraphicMaterial(
   [1], ~.UserObjects.C._3D.MaterialDiffuseColor, 0, 0, 0, 0, 0)
M2._3D.getObject("SetupType").setGraphicMaterial(
   [1], ~.UserObjects.B._3D.MaterialDiffuseColor, 0, 0, 0, 0, 0)
M3._3D.getObject("SetupType").setGraphicMaterial(
   [1], ~.UserObjects.A._3D.MaterialDiffuseColor, 0, 0, 0, 0, 0)
```

### MoveInFrameCtrl [SimTalk]

Called when the object actually moves within its Frame. Inside the control, `?` is the moved object.

- **Parameters:** `old: length[3], new: length[3]` (x, y, z)

```simtalk
MyStation.MoveInFrameCtrl := &myMoveInFrameCtrl
```

```simtalk
param old, new: length[3]
print "xv:", old[1], " yv:", old[2], " zv:", old[3],
      "xn:", new[1], " yn:", new[2], " zn:", new[3]
```

### MoveToFolderCtrl [SimTalk]

Called when the object is moved from one folder/Frame to another. Inside the control, `?` is the moved object and `@` is the new location.

- **Parameters:** `oldFolder: string, newFolder: string, manually: boolean`

```simtalk
MySource.MoveToFolderCtrl := &MoveToFolderCtrl
```

```simtalk
param oldFolder, newFolder: string, manually: boolean
-- @: new folder
-- ?: moved object
-- ?: the object for which the control was called
```

### NotAvailableCtrl [SimTalk]

Called whenever the Exporter or Worker changes to *not available*. Inside the control, `?` references the triggering object.

```simtalk
MyExporter.NotAvailableCtrl := &myNotAvailableCtrl
```

### OpenCtrl [SimTalk]

Called when the object is opened (e.g. via a double-click). **Plant Simulation does *not* show the default dialog** — the control is fully responsible for the UI flow.

- For sub-tables or sub-objects of `Variable`, the sub-table/sub-object is **not** opened; the control is executed instead.
- Hold **Alt** while double-clicking to bypass the Open Control and open normally.
- The **Open Location / Open Origin** ribbon buttons respect Alt the same way.

> ⚠️ If you use an **encrypted** Method as the Open Control and the encrypted password is lost, the object becomes effectively un-openable. Use `decrypt("MyPassword123")` to remove.

**Optional parameters (for all objects except `DataList` and `DataTable`):**

- `from3D: boolean` — true if opened from a 3D window
- `inLockedFolder: boolean` — true if the object sits inside a locked library/folder. If undeclared and the object is inside a locked folder, the Open Control will *not* run (an error is shown instead).

```simtalk
MyStation.OpenCtrl := VOID            -- delete entry
MyParallelStation.OpenCtrl := &myOpenControl
```

```simtalk
param from3D: boolean
var passwordHash:string := computeSHA1Hash(prompt("Password:"))
if passwordHash = "686483805ac47ca14e03514f7481a7973b401762"
   -- password "abc" specified?
   if from3D
      ?._3D.openWindow
   else
      ?.openDialog
   end
end
```

```simtalk
param from3D, inLockedFolder: boolean
if inLockedFolder
   if messageBox("The object is inside a locked folder."+strChr(10)+
                 "Do you want to open the object anyway?", 48, 2) = 32  -- "No"?
       return
   end
end
?.openDialog
```

### PauseCtrl [SimTalk]

Called whenever the *paused* state of the object changes (via the drop-down list or by assigning to the `Pause` attribute). When you read the paused state inside the control, you see the state **after** the change.

- **Optional parameters:**
  - `Duration: real` — length of the pause (or `-1` if unknown / called at the end of a pause).
  - `NewValue: boolean` — when declared, the control fires **only** when the `ShiftCalendar` changes the state. The object is **not** automatically set to the new state — the control must do so itself (the requested state is in `NewValue`).

```simtalk
Transporter.PauseCtrl := &myPauseCtrl
print "Current pause ", current.pause
MyStation.pause := current.pause
var shift := root.ShiftCalendar.GetCurrShift
print "Current shift: ", shift

if not current.unplanned
   if current.pause
      current.currIcon := "pause"
   else
      current.currIcon := "working"
   end
end
```

Example waiting for the current part to finish processing before pausing:

```simtalk
param Duration: real, NewValue: boolean
if ?.Cont /= void
   wait ?.Cont.RemainingProcTime
end
?.Pause := NewValue
```

### PermitDeleteCtrl [SimTalk]

Applies only to **Frame** and **Folder**. Called when the user tries to delete the object. Return values:

- `false` — object is **not** deleted
- `true` — object **is** deleted, then a `DestructorCtrl` (if defined) is called

```simtalk
Frame.PermitDeleteCtrl := &myPermitDeleteCtrl
```

### PlausibilityCtrl [SimTalk]

Called when you click **OK** or **Apply** in the dialog of the object (or in the windows of list objects), to verify or interpret your changes.

- With **no parameters** → called only when the list/table is closed after a change (including file loads).
- With **two optional `integer` parameters** `column, row` → also called after each cell edit (with the column and row numbers; `-1, -1` when closing).

```simtalk
MyStation.PlausibilityCtrl := &myPlausibilityCtrl
```

```simtalk
param column, row: integer
switch column
case 1
   -- column-specific action
end
```

### RelabelCtrl [SimTalk]

Called whenever the **Label** of the object changes. Plant Simulation calls the control for the relabeled object first, then for the inheriting objects.

- **Parameters:** `CurrentLabel: string, NewLabel: string, ManualRename: boolean`

```simtalk
MyStation.RelabelCtrl := void
```

```simtalk
param CurrentLabel, NewLabel: string, ManualRename: boolean
print CurrentLabel
print NewLabel
print ManualRename
```

### RenameCtrl [SimTalk]

Called whenever the **Name** of the object changes. Called first for the renamed object, then for inheriting objects.

> Plant Simulation does *not* call the control when you insert the object into a Frame and then assign a new name.

- **Parameters:** `CurrentName: string, NewName: string, ManualRename: boolean`

```simtalk
MyStation.RenameCtrl := &myRenameCtrl
```

```simtalk
param CurrentName, NewName: string, ManualRename: boolean
print CurrentName
print NewName
print ManualRename
```

### SelectCtrl [SimTalk]

Called when you click the object with the left mouse button. Plant Simulation does *not* select the object — your control decides what to do (e.g. open the object, or confirm via `Selected`).

In 3D, the Method is called on mouse click; hold **Ctrl** while clicking to prevent the control from running.

```simtalk
MyStation.SelectCtrl := .Tools.&mySelectCtrl
print @.Selected
@.Selected := true
```

### UnplannedCtrl [SimTalk]

Called whenever the *Unplanned* state of the object changes — i.e. whether the object is scheduled to work during the shift defined in the `ShiftCalendar`. The state can be toggled via the drop-down list or by assigning to the `Unplanned` attribute.

- **Optional parameters:**
  - `Duration: real` — length of the shift pause, or `-1` when unknown/at end of shift pause.
  - `NewValue: boolean` — when declared, the control fires **only** when `ShiftCalendar` drives the change. The state itself must be applied by the control.

Standard usage pattern (with state manually applied):

```simtalk
param Duration: real, NewValue: boolean
if ?.Cont /= void
   wait ?.Cont.RemainingProcTime
end
?.Unplanned := NewValue
```

End-of-shift illustration:

```simtalk
MyStation.SelectCtrl := &myUnplannedCtrl
print "Frame unplanned: ", current.unplanned
MyStation.unplanned := current.unplanned
if current.unplanned
   current.currIcon := "unplanned"
else
   if current.pause
      current.currIcon := "pause"
   else
      current.currIcon := "working"
   end
end
```

---

## 6. Attributes of User-defined Attributes

Plant Simulation addresses the attributes of user-defined attributes as **sub-attributes** of the respective user-defined attribute.

```simtalk
MyStation.myAttribute.Alignment := "Left"
```

The **Show Attributes and Methods** window shows both the user-defined attribute and its value.

> See also: *User-defined Attributes [general description]*, *Create a User-defined Attribute Manually*, *Create a User-defined Attribute During the Simulation*.

### User-Defined Attribute Attributes

The following attributes are accessible on any user-defined attribute `<UserDefinedAttribute>`:

| Attribute | Type | Description / Example |
|---|---|---|
| `Alignment` | `string` | `"Left"`, `"Name"`, `"Value"`, `"Right"` |
| `asString` (read-only) | `string` | Returns the attribute's value as a string (relative path for `object`-typed values). |
| `BackgroundColor` | `integer` | Background color in 3D; build via `makeRGBValue`. |
| `Color` | `integer` | Color of the visualized value in 3D; build via `makeRGBValue`. |
| `DataType` | `string` | Set the data type of a **non-inherited** user-defined attribute. |
| `DecimalPlaces` | `integer` | Number of decimal places shown in 3D (up to 15; `-1` = all available). Applies to `real`, `length`, `money`, `weight`, `time`, `speed`, `acceleration`. |
| `Font` | `integer` | Font size in 3D: 1 = Small, 2 = Medium, 3 = Large, 4 = Extra Large. |
| `HasInitValue` | `boolean` | Whether the attribute has an initial value. |
| `InitValue` | `any` | The initial value (cannot be specified for `table`, `list`, `stack`, `queue`, `randTime`, `method`). |
| `IntegerPlaces` | `integer` | Number of integer places shown in 3D (up to 15). Applies to `integer`, `real`, `length`, `money`, `weight`, `time`, `speed`, `acceleration`, `randTime`. |
| `Name` | `string` | The name of a not-inherited user-defined attribute. |
| `Position` | `length[3]` | 3D position (x, y, z). Does not apply to MU/Connector instances. |
| `Rotation` | `real` or `real[4]` | Rotation in degrees around the negative z-axis (single value) or around an arbitrary axis given by the 4-value quaternion. Reads always return 4 values. |
| `Scale` | `real` or `real[3]` | Uniform scale (single value) or per-axis scale (array). Does not apply to Connectors. |
| `ShowDataType` | `boolean` | Show the data type in the 3D Frame (true) or hide (false). |
| `ShowExternally` | `boolean` | Show in the outside representation (`true`) or inside (false). |
| `ShowIn3D` | `boolean` | Show the attribute in 3D (true) or hide (false). |
| `ShowInTooltip` | `boolean` | Show Name and Value in the object's tooltip. |
| `ShowName` | `boolean` | Show the attribute's name (true) or hide (false). |
| `ShowUnit` | `boolean` | Show the units of the value in the Frame (true) or hide (false). |
| `StatisticsActive` | `boolean` | Collect statistics values (true) or not (false). |
| `Transparent` | `boolean` | Render the background transparent in 3D (true) or white (false). |

Representative examples (syntax follows the pattern `<Path>.<UserDefinedAttribute>.<SubAttr>`):

```simtalk
-- Alignment
MyStation.myAttribute.Alignment := "Left"

-- asString (read-only)
Station5.ObjAttribute := "~.ProdMgr.prodplan"
var a1 := Station5.ObjAttribute             -- assigns .Models.Model.ProdMgr.prodplan
var a2 := Station5.&ObjAttribute.asString   -- assigns "~.ProdMgr.prodplan"

-- BackgroundColor / Color
MyStation.myAttribute.BackgroundColor := makeRGBValue(100,100,100)
MyStation.myAttribute.BackgroundColor := 6579300            -- same color above, decimal form
MyStation.myAttribute.Color          := makeRGBValue(0,255,0)

-- DataType
MyStation.myAttribute.DataType := "String"

-- DecimalPlaces / IntegerPlaces / Font
MyStation.myAttribute.DecimalPlaces  := 8
MyStation.myAttribute.IntegerPlaces  := 6
-- value "123"     -> "   123"
-- value "123456"  -> "123456"
-- value "1234567" -> "1234567"
MyStation.myAttribute.Font          := 2      -- Medium

-- HasInitValue / InitValue
MyStation.myAttribute.DataType     := "integer"
MyStation.myAttribute.HasInitValue := true
MyStation.myAttribute.InitValue    := 12

-- Name
MyStation.myAttribute.Name := "MyNewName"

-- Position / Rotation / Scale
MyStation.myAttribute.Position := [5, 3, 0]
var a : any := MyStation.myAttribute.Rotation                 -- returns array of 4 values
MyStation.myAttribute.Rotation := 30                          -- 30 degrees around -z
MyStation.myAttribute.Rotation := [45, 0, 1, 0]               -- 45 degrees around Y axis
MyStation.myAttribute.Scale   := 1                            -- uniform
MyStation.myAttribute.Scale   := [1, 4, 9]                    -- x / y / z

-- Show*
MyStation.myAttribute.ShowDataType  := false
MyStation.myAttribute.ShowExternally := false
MyStation.myAttribute.ShowIn3D       := true
MyStation.myAttribute.ShowInTooltip  := true
MyStation.myAttribute.ShowName       := true
MyStation.myAttribute.ShowUnit       := true

-- StatisticsActive / Transparent
MyStation.myAttribute.StatisticsActive := true
MyStation.myAttribute.Transparent     := true
```

**Relevant SimTalk helpers:** `getAttrType`, `setAttrType`, `inheritAttribute`, `getAttribute`, `setAttribute`, `setAttrValue`, `makeRGBValue`.

---

## 7. Methods of the Material Flow Objects — Introduction

All material flow objects share the methods described in the following sub-chapters; the per-object chapters list additional methods. A method:

- Gets information from an object and returns a value.
- Computes a value.
- Starts one or several actions controlling the behavior of the object.

Open **Show Attributes and Methods** to inspect a given object's method set (right-click in the Class Library, or press **F8** in the Frame).

The signature syntax, e.g.:

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

means `<Path>` is the object path; the parenthesized list shows identifier + data type of each parameter. You may pass a constant, a variable of the matching type, or another method that returns that type.

> ⚠️ Always include the parentheses for sub-expressions in parameter lists (e.g. `(a+b)`). Forgetting them may open the Debugger unexpectedly.

---

*Source: Plant Simulation Help — "Objects — Common Attributes". Unpublished work. © 2026 Siemens.*
