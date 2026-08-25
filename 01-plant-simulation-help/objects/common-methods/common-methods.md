# Common Methods — Objects Reference

This document summarizes the methods that are common to **all objects** in the Plant Simulation Class Library, addressable from SimTalk. It covers general methods, object-icon methods, location/predecessor/successor methods, inheritance methods, attribute-management methods, user-defined-attribute methods, and miscellaneous user-defined-attribute methods.

Each entry preserves the original SimTalk code samples so you can use them as starting points.

> Source: *Plant Simulation Help* (Unpublished work. © 2026 Siemens). Pages referenced: 11-631 … 11-732.

---

## Table of Contents

- [1. Methods of All Objects — Overview](#1-methods-of-all-objects--overview)
- [2. General Methods](#2-general-methods)
  - [addObserver, attributeWatchable, closeDialog, deleteObject, derive, duplicate, extendPath, getHTMLCode, getObservers, getXYWH, isNameUnique, memUsage, moveToFolder, openDialog, removeAllObservers, removeObserver, replace, setName, setPosition, setXYWH, showObject, updateDialog, writeObject](#general-methods-index)
- [3. Methods for Object Icons](#3-methods-for-object-icons)
  - [createIcon, deleteIcon, existsIcon, getIconSize, getPixel, putIconToClipboard, saveIconToFile, setCurrIconFromClipboard, setIconFromFile, setIconSize, setPixel](#object-icons-index)
- [4. Methods for the Location, Predecessor, and Successor](#4-methods-for-the-location-predecessor-and-successor)
  - [pred, predConnector, succ, succConnector](#location-pred-succ-index)
- [5. Methods for Managing Inheritance Relations](#5-methods-for-managing-inheritance-relations)
  - [childNo, hasAttribute, inheritAttribute (object), typeOf](#inheritance-index)
- [6. Methods for Managing Attributes](#6-methods-for-managing-attributes)
  - [getAttribute (object), getSubAttribute, putAttributeNamesIntoTable, setAttribute (object), setSubAttribute](#attribute-management-index)
- [7. Methods for Managing User-defined Attributes](#7-methods-for-managing-user-defined-attributes)
  - [createAttr, deleteAttr, getAttribute (UDA), getAttrName, getAttrNo, getAttrType, getAttrValue, inheritAttribute (UDA), setAttribute (UDA), setAttrType, setAttrValue, unshare](#user-defined-attribute-management-index)
- [8. Miscellaneous Methods of User-defined Attributes](#8-miscellaneous-methods-of-user-defined-attributes)
  - [getStatisticsTable, increment](#miscellaneous-uda-index)
- [9. Read-Only Attributes of All Objects — Introduction](#9-read-only-attributes-of-all-objects--introduction)

---

## 1. Methods of All Objects — Overview

A method can

- query information from an object and return a value,
- make calculations,
- start one or several actions that control the behavior of the object.

Methods are grouped in the Plant Simulation Help according to their function. Use **Show Attributes and Methods** (right-click in the Class Library, or press **F8** in a Frame) to view the complete list for any object.

A typical syntax line:

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` — path of the object the method applies to.
- Parenthesized list — method signature, identifier and data type of each parameter. You can pass a constant, a variable of the matching type, or another method that returns the matching type.

> ⚠️ Always include the parentheses for sub-expressions inside parameter lists. Missing parentheses can open the Debugger.

- Optional parameters are wrapped in **square brackets**, e.g. `[,Parameter:boolean]`.
- Default values follow the parameter with `:=`, e.g. `:= false`.
- Return value data type appears after `→`, e.g. `→ boolean`.

### See also
- _General Methods
- _Methods of Object Icons
- _Methods for the Location, Predecessor, and Successor
- _Methods for Managing Inheritance Relations
- _Methods for Managing Attributes
- _Methods of User-defined Attributes

---

## 2. General Methods

Most objects provide the methods listed below. The signature follows the conventions described in §1.

### addObserver [SimTalk]

Adds an observer to the object designated by `<Path>`.

- **Syntax:** `<Path>.addObserver(AttributeName:string, Method:object)`
- **Parameters:**
  - `AttributeName: string` — name of the watchable attribute or read-only attribute.
  - `Method: object` — Method to call when the value changes.
- Inside the called Method, `?` and `@` both address the object whose attribute changed. Two parameters are passed:
  - the name of the attribute that changed,
  - the **previous** value.

```simtalk
MyStation.addObserver("occupied", &myMethod)
```

**See also:** Edit Observers, `removeObserver`, `removeAllObservers`, `attributeWatchable`.

### attributeWatchable [SimTalk]

Returns whether an attribute is watchable (`true` / `false`).

- **Syntax:** `<Path>.attributeWatchable(AttributeName:string) → boolean`

```simtalk
print ParallelStation.attributeWatchable("NumMU")
```

### closeDialog [SimTalk] — all objects

Closes the dialog of the object.

- **Syntax:** `<Path>.closeDialog([ApplyChanges:boolean:=true]) → boolean`
- `ApplyChanges` default: `true` (apply changes). Use `false` to discard them.

```simtalk
MyStore.closeDialog            -- apply changes
MyTrack.closeDialog(false)     -- do not apply changes
```

**See also:** `_3D.closeWindows`, OK button, Cancel button.

### deleteObject [SimTalk]

Deletes the object designated by `<Path>`.

> You cannot delete objects that are currently active (e.g. a Method that is running — including the Method itself if it lives inside the Frame you are trying to delete). Deleting a class object automatically deletes all its instances without warning. To delete a MU, prefer the `delete` method (MUs).

- **Syntax:** `<Path>.deleteObject → boolean`
- Returns `true` if the object was deleted successfully, `false` otherwise.

```simtalk
.Materialflow.MyStation.deleteObject   -- deletes from the Class Library
MyStation.deleteObject                 -- deletes from the Frame
```

**See also:** Delete [Home ribbon].

### derive [SimTalk]

Derives the object in the Class Library, i.e. creates a subclass that inherits from it. Changes are applied immediately.

- **Syntax:** `<Path>.derive([Destination:object, Name:string, NextRandomSeedValue:integer]) → object`
- **Parameters:**
  - `Destination: object` (optional) — where to create the new object.
  - `Name: string` (optional) — name for the new object. If the name is not unique, an error is shown.
  - `NextRandomSeedValue: integer` (optional) — seeds the next random value, enabling reproducible behavior when objects are created during a simulation run.
- **Return:** the derived object, or `VOID` if it failed.

```simtalk
var Station := .MaterialFlow.Station.derive
-- Creates a new class in folder MaterialFlow derived from object named Station.
Station.Name := "TestCenter"
Station.Coordinate3D := [4.0, 5.0, 0.0]

var NewVariable : object := .InformationFlow.&Variable.derive
-- To derive a Variable, use the &-operator so 'derive' applies to the variable itself,
-- not its value.
```

**See also:** Derive, Cut Inheritance, Random Seed Value, `RandomSeed`, `setRandomSeedCounter`, `create` (MUs).

### duplicate [SimTalk]

Copies the object in the Class Library and creates a new class. Inheritance relations to the original are cut. Use the `Coordinate3D` attribute to control the position of the new object.

- **Syntax:** `<Path>.duplicate([Destination:object, Name:string]) → object`
- **Return:** the duplicated object, or `VOID` if duplication failed.

```simtalk
.MaterialFlow.Conveyor.duplicate
.MaterialFlow.Conveyor.duplicate(.Models.MyPlant, "MyConveyor")
.InformationFlow.&Variable.duplicate
.InformationFlow.&Method.duplicate

var myConveyor: object := .MaterialFlow.Conveyor.duplicate(.Models.Model, "MyConveyor")
MyConveyor.setPosition := [100, 100]   -- sets pixel coordinates
```

**See also:** Derive, Delete, `Coordinate3D`.

### extendPath [SimTalk]

Extends the path of `<Path>`, letting you reach contained objects.

- **Syntax:** `<Path>.extendPath(PathExtension:string) → object`

```simtalk
var obj := MyFrame.extendPath("Station3")
if obj /= void
   obj.ProcTime := 63.5
end
current.extendPath("Station")   -- true if "Station" exists in current Frame
```

**See also:** `existsObject`.

### getHTMLCode [SimTalk] — all objects

Returns the HTML code of the object's statistics block (same syntax as `HtmlReport`).

- **Syntax:** `<Path>.getHTMLCode([Caption:string, StatisticsType:string, ColumnOrColumnRange:any]) → string`
- `StatisticsType` strings (start with `%`):

| English | German |
|---|---|
| `%ResStates` | `%Stati` |
| `%MatFlowProperties` | `%Matflusseigenschaften` |
| `%RotationTime` (Turnplate, Turntable, PickAndPlace) | `%Drehungszeit` |
| `%MovingTime` (Converter) | `%Umsetzzeit` |
| `%WorkingTime` | `%Arbeitszeit` |
| `%SetupTime` | `%Rüstzeit` |
| `%WaitingTime` | `%Wartezeit` |
| `%BlockedTime` | `%Blockiertzeit` |
| `%PowerUpDownTime` | `%HochHerunterfahrzeit` |
| `%StoppedTime` | `%Angehaltenzeit` |
| `%FailedTime` | `%Störungszeit` |
| `%PausedTime` | `%Pausenzeit` |
| `%EmptyTime` | `%Leerzeit` |
| `%MUMatFlowProperties` | `%BEMatflusseigenschaften` |
| `%MUEmptyTime` | `%BELeerzeit` |
| `%DrainCumulated` | `%SenkeKumuliert` |
| `%DrainAllTypes` | `%SenkeAlleTypen` |
| `%DrainTypesPortions` (non-summable) | `%SenkeTypenanteile` |
| `%DrainTypesTimes` (non-summable) | `%SenkeTypenzeiten` |
| `%Energy` | `%Energie` |
| `%MUClassStatistics` | `%BEKlassenStatistik` |
| `%MUClassTimePortions` | `%BEKlassenZeitanteile` |
| `%MUTimePortions` | `%BEZeitanteile` |
| `%TransUsageTime` | `%TransVerwendungszeit` |
| `%TransReadyTime` | `%TransBereitzeit` |
| `%TransPausedTime` | `%TransPausenzeit` |
| `%TransFailedTime` | `%TransStörungszeit` |
| `%TransTraveledDistance` | `%TransWegstrecke` |
| `%TransBatteryTime` | `%TransBatteriezeit` |
| `%Broker` | `%Broker` |
| `%BrokerMediationTime` | `%BrokerVermittlungsdauer` |
| `%BrokerDwellTime` | `%BrokerVerweildauer` |
| `%Exporter` | `%Exporter` |
| `%ExporterTimePortions` | `%ExporterZeitanteile` |
| `%WorkerTraveleledDistance` | `%WerkerWegstrecke` |
| `%ImporterWaiting` | `%ImporterWartend` |
| `%ImporterWaitingTime` | `%ImporterWartezeit` |
| `%ImporterMUWaitingTime` | `%ImporterBEWartezeit` |
| `%ImporterSetpWaitingTime` | `%ImporterRüstWartezeit` |

- **Column identifiers** (same as `HtmlReport`):

| Identifier | Meaning |
|---|---|
| `#Sum` | column with index or name `Sum` |
| `0` | row-index column (error if not available) |
| `3` | column number 3 |
| `2..5` | columns 2 to 5 |
| `..5` | first available column to column 5 |
| `*..5` | first available column to column 5 |
| `5..` | column 5 onward |
| `5..*` | column 5 onward |
| `*` | last column of the table |

```simtalk
print Source.getHtmlCode
Comment1.Cont := DataTable.getHtmlCode()              -- entire table
Comment2.Cont := DataTable.getHtmlCode("caption")     -- with caption
Comment3.Cont := DataTable.getHtmlCode(1, 3)          -- numeric column index
Comment4.Cont := DataTable.getHtmlCode("1", 3)        -- mixed numeric / string indexes
Comment5.Cont := DataTable.getHtmlCode("1..2")        -- column index range
Comment6.Cont := DataTable.getHtmlCode("#A")          -- named column
```

**See also:** Display an HtmlReport, Display a Frame.

### getObservers [SimTalk]

Returns all observers of `<Path>`.

- **Syntax:** `<Path>.getObservers → table`
- Returns a table with three columns:
  - `string` — observed value name
  - `object` — Method (as object reference or relative path)
  - `boolean` — `true` if the observer was created in this object (not inherited)

```simtalk
-- deletes all observers of a Station
var observerTable := Station.getObservers
for var row := 1 to observerTable.ydim
   if observerTable[3, row]                       -- only delete non-inherited observers
       if observerTable[2, row] /= void          -- observer is an object reference
           Station.removeObserver(observerTable[1, row], observerTable[2, row])
       else                                        -- observer is a relative path
           Station.removeObserver(observerTable[1, row], observerTable.asString(2, row))
       end
   end
next
```

**See also:** Edit Observers, New [observer], `asString` (DataTable).

### getXYWH [SimTalk]

Returns the dialog's screen coordinates and size. For a maximized window `x` and `y` are `-1`, while width and height are correct.

- **Syntax:** `<Path>.getXYWH(byRef X:integer, byRef Y:integer, byRef Width:integer, byRef Height:integer)`

```simtalk
Frame1.getXYWH(x, y, w, h)
print x, " ", y, " ", w, " ", h
```

**See also:** `setXYWH`.

### isNameUnique [SimTalk] — identifier

Returns whether the identifier is unique in the namespace of `<Path>`.

- **Syntax:** `<Path>.isNameUnique(NameToBeChecked:string) → boolean`

> Use this to predict renaming conflicts before triggering a runtime error.

```simtalk
print .Hall2.isNameUnique("Station1")             -- instance inserted into Frame
print .Hall2.isNameUnique("Name")                 -- built-in attribute
print .Hall2.isNameUnique("~")                    -- built-in method
print .Hall2.isNameUnique("myUserDefinedAttribute")
```

**See also:** `hasAttribute`, Namespace.

### memUsage [SimTalk]

Computes the memory used by the object (in bytes).

- **Syntax:** `<Path>.memUsage → integer`

```simtalk
print FootPath1.memUsage   -- might return 9685 (≈ 9.5 KB)
print MyStation.memUsage   -- might return 4975  (≈ 4.9 KB)
```

**See also:** Show Structure [class library], `_3D.memUsage`.

### moveToFolder [SimTalk]

Moves the object into the folder designated by `Folder`.

- **Syntax:** `<Path>.moveToFolder(Folder:Path) → object`

```simtalk
.Resources.Exporter.moveToFolder(.Models)
```

**See also:** Move to Folder Control, `MoveToFolderCtrl`.

### openDialog [SimTalk] — all objects

Opens the dialog of the object (and runs any Open Control if requested).

- **Syntax:** `<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`
- Default for `CallOpenControl` is `false` (skip the Open Control).

```simtalk
Buffer.openDialog
.drill.openDialog(false)
basis.Materialflow.Source.openDialog(true)
self.~.~.&MyMethod.openDialog      -- opens the window of MyMethod instead of executing it
```

**See also:** `_3D.openDialog`, Open Control.

### removeAllObservers [SimTalk]

Deletes all observers of `<Path>`.

- **Syntax:** `<Path>.removeAllObservers → boolean`
- Returns `true` if inherited observers exist.

```simtalk
MyStation.removeAllObservers
```

**See also:** `removeObserver`, `addObserver`, Delete [observer].

### removeObserver [SimTalk]

Deletes the specified observer. Pass `void` to remove all observers that point to non-existent Methods.

- **Syntax:** `<Path>.removeObserver(AttributeName:string, Method:method/void) → boolean`

```simtalk
MyStation.removeObserver("occupied", "myMethod")
MyStation.removeObserver("occupied", &myMethod)
```

**See also:** Edit Observers, Delete [observer].

### replace [SimTalk]

Replaces `ObjectToReplace` with `<Path>`. Both must be classes (to merge) or instances.

- **Syntax:** `<Path>.replace(ObjectToReplace:object[, RetainInheritedValues:boolean:=false])`
- `RetainInheritedValues` (default `false`) — only meaningful for instances: if `true`, cuts inheritance on the new instance where the new class's value differs from the previous one.

```simtalk
.MaterialFlow.Station.replace(.MaterialFlow.MyStation, false)
```

**See also:** Replacing and Merging Objects with Drag-and-Drop, Load Object, Replacement Mode.

### setName [SimTalk]

Sets the object's name. Allowed characters: letters, digits, underscore (`_`). Cannot start with a digit. Cannot rename `EventController` or `Connector`.

- **Syntax:** `<Path>.setName(NewName:string) → boolean`

```simtalk
print MyStation.setName("MyStation")   -- returns true
```

Unlike assigning to `Name`, this returns whether the assignment succeeded. **See also:** Name, Rename.

### setPosition [SimTalk]

Sets the icon position of `<Path>` in the Frame (pixel coordinates).

- **Syntax:** `<Path>.setPosition(X:integer, Y:integer[, CallMoveInFrameControl:boolean:=true])`
- `CallMoveInFrameControl` default `true`; pass `false` to skip the Move-in-Frame control.

```simtalk
MyStation.setPosition(15, 400)
ParallelStation.setPosition(80, 200, true)
```

**See also:** Move in Frame Control.

### setXYWH [SimTalk]

Sets the dialog screen position and size. Negative X/Y centers the dialog on screen. Also applies to `DataTable` opened as a foreground dialog.

- **Syntax:** `<Path>.setXYWH(X:integer, Y:integer, Width:integer, Height:integer[, TotalSize:boolean:=true])`
- `TotalSize` default `true` — total size; `false` = inside the frame border.
- Only Frame, Method, Method Debugger, DataQueue, DataStack, DataList, DataTable, and Icon Editor are resizable.

```simtalk
MyStation.setxywh(10, 100, 10, 20)
Model1.setxywh(500, 100, 15, 25)
MyDataTable.openDialogBox
MyDataTable.setxywh(-500, 100, 15, 25)   -- centered on screen
```

**See also:** `getXYWH`.

### showObject [SimTalk]

Selects and shows the object. For instances, selects in the Frame view (opens the Frame if closed). For classes, expands the folder in the Class Library.

- **Syntax:** `<Path>.showObject`

```simtalk
MyFrame.ParallelStation.showObject
.MaterialFlow.ParallelStation.showObject
```

### updateDialog [SimTalk]

Updates the contents of the object's open dialog (useful when assignments inside a Method change settings).

- **Syntax:** `<Path>.updateDialog → boolean`

```simtalk
EventController.StartDate := sysdate
EventController.updateDialog
```

**See also:** Refresh [View menu].

### writeObject [SimTalk]

Saves the object to a file (`.psobj`) in the active folder (compare `setCurrentDirectory`) or to the given absolute path. Applies to all classes and folders in the Class Library.

- **Syntax:** `<Path>.writeObject(FileName:string[, SaveAsLibrary:boolean:=false, Password:string]) → boolean`
- `SaveAsLibrary` default `false`; pass `true` to save as a `.pslib` library.
- `Password` encrypts the saved file.

```simtalk
.Informationflow.DataList.writeObject("MyDataList.psobj")
.Materialflow.ParallelStation.writeObject("mypp.psobj")
.ApplicationObjects.Productionsystem.writeObject("MyLibrary.pslib", true)
```

**See also:** Save Object As, Save Folder As, Save Library As, `setLibraryInfo`, `setCurrentDirectory`.

---

## 3. Methods for Object Icons

These methods are used to animate and manipulate object icons. Applies to all objects (with documented restrictions).

### createIcon [SimTalk]

Creates a new icon for the object instance (not the class). Transparency is enabled by default and the background is filled with the transparency color.

- **Syntax:** `<Path>.createIcon(IconName:string, Width:integer, Height:integer) → integer`

```simtalk
MyStation.createIcon("state", 20, 30)
```

**See also:** Activate Transparency, New Icon, Icon Editor.

### deleteIcon [SimTalk]

Deletes an icon by name or by number. Affects the instance, not the class.

- **Syntax:**
  - `<Path>.deleteIcon(IconName:string)`
  - `<Path>.deleteIcon(IconNumber:integer)`

```simtalk
MyParallelStation.deleteIcon("MyIcon")
MyParallelStation.deleteIcon(1)
```

### existsIcon [SimTalk]

Returns `true` if the icon exists.

- **Syntax:**
  - `<Path>.existsIcon(IconName:string) → boolean`
  - `<Path>.existsIcon(IconNumber:integer) → boolean`

```simtalk
press.existsIcon("failed")
press.existsIcon(2)
```

### getIconSize [SimTalk]

Returns the width and height of the current icon.

- **Syntax:** `<Path>.getIconSize(byRef Width:integer, byRef Height:integer)`

```simtalk
var w, h: integer
MyStation.getIconSize(w, h)
print w, " ", h
```

**See also:** Set Icon Size.

### getPixel [SimTalk]

Returns the RGB value of a pixel (as `integer`). Applies to all objects except `Variable`, `Comment`, folder, and toolbar.

- **Syntax:** `<Path>.getPixel(X:integer, Y:integer) → integer`

```simtalk
var rgb, red, green, blue: integer
rgb := MyStation.getPixel(1, 1)
red   := rgb mod 256
green := (rgb div 256) mod 256
blue  := rgb div (256*256)
```

**See also:** Pick Color, Replace Color.

### putIconToClipboard [SimTalk]

Opens the Windows clipboard and stores the icon as a `CF_BITMAP`.

- **Syntax:**
  - `<Path>.putIconToClipboard(IconName:string) → boolean`
  - `<Path>.putIconToClipboard(IconNumber:integer) → boolean`

```simtalk
MyStation.putIconToClipboard(3)
```

**See also:** `setCurrIconFromClipboard`.

### saveIconToFile [SimTalk]

Saves the icon as a `.png` to the Plant Simulation installation folder.

- **Syntax:**
  - `<Path>.saveIconToFile(IconName:string, FileName:string) → boolean`
  - `<Path>.saveIconToFile(IconNumber:integer, FileName:string) → boolean`

```simtalk
sp1.saveIconToFile(3, "iconfile")
sp1.saveIconToFile("icon_name", "iconfile")
```

**See also:** Export Icon to File.

### setCurrIconFromClipboard [SimTalk]

Reads a bitmap from the clipboard, converts it, and assigns it as the current icon. Applies to the instance, not the class.

- **Syntax:**
  - `<Path>.setCurrIconFromClipboard(IconName:string) → boolean`
  - `<Path>.setCurrIconFromClipboard(IconNumber:integer) → boolean`

```simtalk
MyFrame.setCurrIconFromClipboard(3)
MyFrame.setCurrIconFromClipboard("MyIcon")
```

**See also:** Paste Contents of the Clipboard [Home ribbon].

### setIconFromFile [SimTalk]

Replaces the icon with a graphics file. Applies to the instance, not the class.

- **Syntax:**
  - `<Path>.setIconFromFile(IconName:string, FileName:string) → boolean`
  - `<Path>.setIconFromFile(IconNumber:integer, FileName:string) → boolean`

```simtalk
MyStation.setIconFromFile(3, "outOfOrder.gif")
MyStation.setIconFromFile("failed", "C:\graphics\outOfOrder.gif")
```

**See also:** Import.

### setIconSize [SimTalk]

Sets the current icon's width and height.

- **Syntax:** `<Path>.setIconSize(Width:integer, Height:integer)`

```simtalk
MyStation.setIconSize(44, 44)
```

**See also:** `getIconSize`.

### setPixel [SimTalk]

Sets the color of an icon pixel. Since classes share icons, this changes the pixel in the class and all derivatives. Applies to all objects except `Variable`, `Comment`, folder, and toolbar.

- **Syntax:** `<Path>.setPixel(X:integer, Y:integer, RGB:integer) → integer`
- Build RGB with `makeRGBValue`.

```simtalk
-- sets the pixel in the upper left corner to pink
MyStation.setPixel(1, 1, makeRGBValue(255, 0, 255))
MyStation.redraw
```

**See also:** `getPixel`, `makeRGBValue`, Replace Color.

---

## 4. Methods for the Location, Predecessor, and Successor

Most objects provide methods to query their location, predecessor, and successor.

### pred [SimTalk] — general description

Returns the direct predecessor (or the `n`-th predecessor).

- **Syntax:**
  - `<Path>.pred → object`
  - `<Path>.pred([PredecessorNumber:integer:=1]) → object`

> If the predecessor is an Interface, the method follows it to a material-flow object that can receive MUs. If the predecessor is a Frame, the method follows the inserted Interface.

```simtalk
if model.pred(3).name = "press"
   ...
end
```

**See also:** `pred` (lane A or B), `predConnector`, `NumPred`.

### predConnector [SimTalk] — general description

Returns the Connector to the predecessor (or the `n`-th predecessor). Returns `VOID` if the connector doesn't exist. Adding/removing connections may change the index.

- **Syntax:**
  - `<Path>.predConnector → object`
  - `<Path>.predConnector([PredecessorNumber:integer:=1]) → object`

```simtalk
for var i := MyTrack.NumPred downto 1
   MyTrack.predConnector(i).deleteObject
next
```

**See also:** `pred`, `predConnector` (lane A or B).

### succ [SimTalk] — general description

Returns the direct successor (or the `n`-th successor).

- **Syntax:**
  - `<Path>.succ → object`
  - `<Path>.succ([SuccessorNumber:integer:=1]) → object`

> If the successor is an Interface, the method follows it until it reaches a material-flow object that can receive MUs. With multiple successors on an Interface, the Exit Strategy picks one; blocking Exit Strategies pick regardless of whether the successor can currently receive a MU, non-blocking ones pick the next one that can. If none can receive a MU, `VOID` is returned.

```simtalk
@.move(ParallelStation.succ(3))
```

**See also:** `succ` (lane A or B), `succConnector`, `NumSucc`.

### succConnector [SimTalk] — general description

Returns the Connector to the successor (or the `n`-th successor). Returns `VOID` if it doesn't exist. Adding/removing connections may change the index.

- **Syntax:**
  - `<Path>.succConnector → object`
  - `<Path>.succConnector([SuccessorNumber:integer:=1]) → object`

```simtalk
MyTrack.succConnector.deleteObject   -- delete the connector to the succeeding object
```

**See also:** `succ`, `succConnector` (lane A or B).

---

## 5. Methods for Managing Inheritance Relations

### childNo [SimTalk]

Returns the instance with the given number. Independent of the instance name or the Frame it lives in.

- **Syntax:** `<Path>.childNo(Number:integer) → object`
- Use the read-only attribute `NumChildren` to get the size of the list.

```simtalk
for var index := 1 to .MUs.Transporter.NumChildren
   print .MUs.Transporter.childNo(index)   -- outputs all children
next
```

**See also:** `NumChildren`, Instance [general description].

### hasAttribute [SimTalk] — objects

Returns whether the object has a readable attribute or method with the given name.

- **Syntax:** `<Path>.hasAttribute(AttributeName:string) → boolean`
- Returns `false` for `Imp`, `SetupImp`, `FailImp` when those attributes don't exist on the object.

```simtalk
print Station.hasAttribute("Availability")
print Conveyor.hasAttribute("Imp")
print Conveyor.hasAttribute("FailImp")
print Conveyor.hasAttribute("SetupImp")
```

**See also:** `_3D.hasAttribute`, `isNameUnique`.

### inheritAttribute [SimTalk] — object

Re-activates inheritance for the specified attribute on `<Path>`.

- **Syntax:** `<Path>.inheritAttribute(AttributeName:string)`

```simtalk
Conveyor.inheritAttribute("Length")
Conveyor.Sensors.ID1.inheritAttribute("Position")
Station.Failures.Failure.inheritAttribute("Availability")
Station.Imp.inheritAttribute("Priority")
Station._3D.inheritAttribute("VisibleGraphicGroups")
&Variable.inheritAttribute("Value")
```

**See also:** Instance, `_3D.inheritAttribute`.

### typeOf [SimTalk]

Returns whether `<Path>` has the same internal class type as the comparison object.

- **Syntax:** `<Path>.typeOf(ObjectToBeCompared:object) → boolean`

```simtalk
print MyStation.typeOf(station2)   -- true if both are of type Station
```

**See also:** `inheritAttribute` (object), `_3D.InternalClassType`.

---

## 6. Methods for Managing Attributes

### getAttribute [SimTalk] — object

Returns the value of an attribute.

- **Syntax:** `<Path>.getAttribute(AttributeName:string[, byRef Inherited:boolean, byRef CanInherit:boolean]) → any`

> For user-defined attributes of `method` data type, `getAttribute` returns the method itself — not the result of executing it. To execute, call `.execute` explicitly.

```simtalk
print MyStation.getAttribute("ProcTime")

-- checks if inheritance of the attribute 'Accumulating' is active
var inherited: boolean
print MyConveyor.getAttribute("Accumulating", inherited)
print inherited

-- method-typed user-defined attribute: get the method itself vs. the result
var bInherited: boolean
Station.getAttribute("MyMethodAttribute", bInherited)        -- does NOT call MyMethodAttribute
Station.getAttribute("MyMethodAttribute").execute            -- explicitly executes

var ResultOfMethod := Station.getAttribute("MethodAttributeWithoutParameters")
var Result        := Station.getAttribute("MethodAttributeWith2Parameters").execute(5, 9)

-- check whether the source code of a Method is inherited
var bInherit: boolean
&Method.getAttribute("Program", bInherit)
print bInherit
```

**See also:** `getSubAttribute`, `setSubAttribute`, `setAttribute`, `putAttributeNamesIntoTable`, `_3D.getAttribute`, `isNameUnique`.

### getSubAttribute [SimTalk]

Returns the value of a sub-attribute.

- **Syntax:**
  - `<Path>.getSubAttribute(AttributeName:string, SubAttributeName:string) → any`
  - `<Path>.getSubAttribute(AttributeName:string, SubAttributeName:string[, Inherited:boolean]) → any`
- When `Inherited` is passed by reference, it receives `true` if the attribute is inherited.

```simtalk
var b: boolean
print MyStation.getSubAttribute("ProcTime", "Type", b)
print b   -- true = inherited, false = not inherited

print MyStation.getSubAttribute("ProcTime", "Type")   -- "Normal"
print MyStation.getSubAttribute("ProcTime", "Mu")     -- 1:00.0000
```

**See also:** `getAttribute`, `setSubAttribute`, `putAttributeNamesIntoTable`.

### putAttributeNamesIntoTable [SimTalk] — objects

Writes the names and data types of all attributes into a table.

- **Syntax:**
  - `<Path>.putAttributeNamesIntoTable(Table:table)`
  - `<Path>.putAttributeNamesIntoTable(Table:table[, IncludeUserDefinedAttribute:boolean:=false, IncludeMethods:boolean:=false, Language:integer:=ModelLanguage])`
- If no optional parameters are given, read-only attributes are NOT included.
- `IncludeUserDefinedAttribute` default `false`.
- `IncludeMethods` default `false`. When `true`, includes method and read-only attribute names (user-defined methods too when `IncludeUserDefinedAttribute` is also `true`).
- `Language` default `ModelLanguage`. `0` = German, `1` = English.
- The column **Signature** holds the complete signature for built-in Methods. The **Side Effect** column is a boolean flag indicating whether read access has side effects.

```simtalk
Station.putAttributeNamesIntoTable(DataTable, true, true, UserInterfaceLanguage)
MyStation.putAttributeNamesIntoTable(MyDataTable)
```

**See also:** `getAttribute`, `getSubAttribute`, `setAttribute`, `setSubAttribute`, `userInterfaceLanguage`, `isNameUnique`.

### setAttribute [SimTalk] — object

Sets the value of the specified attribute.

- **Syntax:** `<Path>.setAttribute(AttributeName:string, Value:any)`

```simtalk
MyStation.setAttribute("ProcTime", 5)
```

**See also:** `getAttribute`, `getSubAttribute`, `putAttributeNamesIntoTable`, `setSubAttribute`, `isNameUnique`.

### setSubAttribute [SimTalk]

Sets the value of a sub-attribute.

- **Syntax:** `<Path>.setSubAttribute(AttributeName:string, SubAttributeName:string, Value:any)`

```simtalk
MyStation.setSubAttribute("ProcTime", "Type", "uniform")
```

**See also:** `getAttribute`, `getSubAttribute`, `setAttribute`, `setTypeAndAttr`, `isNameUnique`.

---

## 7. Methods for Managing User-defined Attributes

User-defined attributes are defined on the **Tab User-defined** of an object. The *Show Attributes and Methods* window shows both the attribute and its value.

### createAttr [SimTalk]

Creates the designated user-defined attribute. The attribute is propagated to all instances.

- **Syntax:** `<Path>.createAttr(AttributeName:string, DataType:string) → boolean`
- Returns `false` if the name or data type is invalid.

```simtalk
MyStation.createAttr("lotsize", "integer")
MyStation.createAttr("inventoryNo", "string")
@.createAttr("Paint", "boolean")
```

**See also:** `deleteAttr`, User-defined Attributes, Create a User-defined Attribute During the Simulation.

### deleteAttr [SimTalk]

Deletes a user-defined attribute. Can only delete attributes that are not inherited and were created for this object; deletion propagates to all instances. Deleting an object also deletes all its user-defined attributes.

- **Syntax:** `<Path>.deleteAttr(AttributeName:string) → boolean`

```simtalk
.MUs.Part.deleteAttr("lotsize")
@.deleteAttr("Paint")
```

**See also:** `createAttr`, Delete [user-defined attribute].

### getAttribute [SimTalk] — user-defined attribute

Returns the inheritance status of the designated user-defined attribute.

- **Syntax:** `<Path>.<UserDefinedAttribute>.getAttribute(AttributeName:string, byref Inherited:boolean, byref CanInherit:boolean) → any`
- `Inherited` receives `true` if the attribute inherits its value. For non-inheritable attributes it always returns `false`.
- `CanInherit` receives `true` if the attribute value **can** be inherited.

```simtalk
var bInherited, bCanInherit: boolean
MyStation.On.getAttribute("Value",       bInherited, bCanInherit)
MyStation.On.getAttribute("InitValue",   bInherited, bCanInherit)
MyStation.On.getAttribute("HasInitValue", bInherited, bCanInherit)
```

**See also:** `setAttribute` (UDA), User-defined Attributes.

### getAttrName [SimTalk]

Returns the name of the user-defined attribute with the given index. Errors if the index is out of range.

- **Syntax:** `<Path>.getAttrName(AttributeNumber:integer) → string`

```simtalk
-- lists all user-defined attributes of the object
for var index := 1 to MyStation.NumAttr
   print MyStation.getAttrName(index)
next
```

**See also:** User-defined Attributes, New [user-defined attribute].

### getAttrNo [SimTalk]

Returns the index of the user-defined attribute with the given name; `0` if not found.

- **Syntax:** `<Path>.getAttrNo(AttributeName:string) → integer`

```simtalk
param lookFor: string -> any
-- checks if a user-defined object exists and returns its value if it does
var index: integer := MyStation.getAttrNo(lookFor)
if index > 0
   return MyStation.getAttrValue(index)
end

param lookFor: string -> boolean
-- checks if a user-defined object exists
var index: integer
index := MyStation.getAttrNo(lookFor)
if index = 0
   result := false   -- does not exist
else
   result := true    -- exists
end
```

**See also:** User-defined Attributes, New [user-defined attribute].

### getAttrType [SimTalk]

Returns the data type of the user-defined attribute with the given index.

- **Syntax:** `<Path>.getAttrType(AttributeNumber:integer) → string`

```simtalk
for var index := 1 to MyStation.NumAttr
   print MyStation.getAttrType(index)
next
```

**See also:** User-defined Attributes, New [user-defined attribute].

### getAttrValue [SimTalk]

Returns the value of the user-defined attribute with the given index.

- **Syntax:** `<Path>.getAttrValue(AttributeNumber:integer) → any`

```simtalk
print MyStation.getAttrValue(1)
```

**See also:** User-defined Attributes, New [user-defined attribute].

### inheritAttribute [SimTalk] — user-defined attribute

Turns inheritance **on** for the specified attribute of a user-defined attribute.

> When several attributes are inherited together, turning inheritance on for any single attribute of the group also turns it on for the rest.

- **Syntax:** `<Path>.<UserDefinedAttribute>.inheritAttribute(AttributeName:string)`

```simtalk
Station.MyInheritedAttribute.inheritAttribute("Transparent")
MyStation.MyAttribute.inheritAttribute("InitValue")
MyStation.MyAttribute.inheritAttribute("HasInitValue")
```

**See also:** User-defined Attributes.

### setAttribute [SimTalk] — user-defined attribute

Sets the value of the specified attribute of a user-defined attribute.

- **Syntax:** `<Path>.<UserDefinedAttribute>.setAttribute(AttributeName:string, Value:any)`

```simtalk
MyStation.Color.setAttribute("BackgroundColor", makeRGBValue(255, 87, 192))
-- sets the Background Color of the user-defined attribute named Color
```

**See also:** `getAttribute` (UDA), User-defined Attributes.

### setAttrType [SimTalk]

Sets the data type of a user-defined attribute. Supported types: `boolean, integer, real, string, object, table, list, stack, queue, time, money, length, weight, speed, acceleration, date, dateTime, randtime`.

- **Syntax:** `<Path>.setAttrType(AttributeNumber:integer, DataType:string) → boolean`

```simtalk
var index: integer
index := MyStore.getAttrNo("Sale")
MyStore.setAttrType(index, "boolean")
```

**See also:** User-defined Attributes, New [user-defined attribute].

### setAttrValue [SimTalk]

Sets the value of the user-defined attribute with the given index.

- **Syntax:** `<Path>.setAttrValue(AttributeNumber:integer, Value:any) → boolean`

```simtalk
var index: integer
index := MyStore.getAttrNo("Sale")
MyStore.setAttrValue(index, true)
```

**See also:** User-defined Attributes, New [user-defined attribute].

### unshare [SimTalk]

For a user-defined attribute or `Variable` of data type `table/list/stack/queue`, breaks the shared reference and gives the attribute its own copy.

> When assigning one user-defined attribute (or `Variable`) of `table/list/stack/queue` to another, Plant Simulation creates a reference — both attributes share the same list. Call `unshare` to make them independent.

- **Syntax:** `<Path>.unshare`

```simtalk
Station.TabAttr := ParallelStation.TabAttr
Station.TabAttr[1, 1] := "Alice"
-- share the user-defined table attributes
ParallelStation.TabAttr[1, 1] := "Bob"        -- changes the common table
print Station.TabAttr[1, 1]                   -- prints Bob

ParallelStation.TabAttr.unshare               -- now each has its own table
ParallelStation.TabAttr[1, 1] := "Charlie"
print Station.TabAttr[1, 1]                   -- prints Bob (unchanged)
```

**See also:** Sequence Cyclical, Sequence, Random, Percentage, Value [Variable] > Unshare, Variable, Unshare a List or Data Table.

---

## 8. Miscellaneous Methods of User-defined Attributes

Methods available on user-defined attributes themselves.

### getStatisticsTable [SimTalk] — user-defined attribute

Returns the statistics table of the user-defined attribute and writes it into `TargetTable`. For `string`-typed attributes, values in the first column are always lower-cased.

- **Syntax:** `<Path>.<UserDefinedAttribute>.getStatisticsTable(TargetTable:table)`

```simtalk
MyStation.MyAttribute.getStatisticsTable(MyStatstable)
```

**See also:** User-defined Attributes, Statistics Table.

### increment [SimTalk] — user-defined attribute

Adds 1 (or the supplied number) to the user-defined attribute. Only applies to numerical types and to `Variable`.

- **Syntax:**
  - `<Path>.<UserDefinedAttribute>.increment`
  - `<Path>.<UserDefinedAttribute>.increment(Number:integer)`
  - `<Path>.<UserDefinedAttribute>.increment(Number:real)`

```simtalk
MyStation.MyAttribute.increment            -- same as MyStation.attrib := MyStation.MyAttribute + 1
MyStation.MyAttribute.increment(-1)        -- same as MyStation.MyAttribute := MyStation.MyAttribute - 1
```

**See also:** User-defined Attributes.

---

## 9. Read-Only Attributes of All Objects — Introduction

Simulation objects and 3D objects share the read-only attributes described in the *Read-Only Attributes of All Objects* chapter. You can query these attributes but cannot set them — Plant Simulation computes the value at the time of the query. Most correspond to an unavailable dialog item (e.g. on the Statistics tab).

Use **Show Attributes and Methods** to view the read-only attributes of an object. To query one, e.g.:

```simtalk
print Source.Empty
```

---

*Source: Plant Simulation Help — "Objects — Methods of All Objects". Unpublished work. © 2026 Siemens.*