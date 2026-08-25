# Methods of All Objects

This reference summarizes SimTalk methods shared by Plant Simulation objects. Use **Show Attributes and Methods** (F8) to inspect the members supported by a particular class or instance.

## Syntax conventions

- `<Path>` is the object to which a method applies.
- Square brackets (`[]`) indicate optional parameters; `:=` introduces a default value.
- `byRef` parameters receive a value from the method.
- `→` indicates the return type. A failed object-creation operation commonly returns `void`.
- Enter parentheses for expressions inside a method call; omitting them can lead to unexpected results.

## Distribution parameters

Distribution attributes can be configured with `setTypeAndAttr`. Supply all parameters either as one comma-separated string or as individual arguments. `getAttr` returns a parameter set that `setTypeAndAttr` can consume.

```simtalk
-- Set distribution parameters as a string.
MyStation.ProcTime.setTypeAndAttr("Uniform", "0:15, 0:20")

-- Set distribution parameters as individual values.
MyStation.ProcTime.setTypeAndAttr("Uniform", 0:15, 0:20)

var type: string := Station.ProcTime.type
var parameters: string := Station.ProcTime.getAttr
StationNew.ProcTime.setTypeAndAttr(type, parameters)
```

## General methods

| Method | Signature | Purpose |
|---|---|---|
| `addObserver` | `<Path>.addObserver(AttributeName:string, Method:object)` | Calls a method when a watchable attribute changes. The callback receives the attribute name and its old value; `?` and `@` refer to the changed object. |
| `attributeWatchable` | `<Path>.attributeWatchable(AttributeName:string) → boolean` | Tests whether an attribute or read-only attribute can be observed. |
| `closeDialog` | `<Path>.closeDialog([ApplyChanges:boolean:=true]) → boolean` | Closes an object dialog, optionally applying pending edits. |
| `deleteObject` | `<Path>.deleteObject → boolean` | Deletes an object. Deleting a class also deletes its instances; use MU `delete` for MUs. Active objects cannot be deleted. |
| `derive` | `<Path>.derive([Destination:object, Name:string, NextRandomSeedValue:integer]) → object` | Creates a derived class, optionally at a destination with a name and deterministic next random seed. |
| `duplicate` | `<Path>.duplicate([Destination:object, Name:string]) → object` | Creates an independent class copy and cuts inheritance from the original. |
| `extendPath` | `<Path>.extendPath(PathExtension:string) → object` | Resolves an object located below a path. |
| `getHTMLCode` | `<Path>.getHTMLCode([Caption:string, StatisticsType:string, ColumnOrColumnRange:any]) → string` | Returns HTML equivalent to a report statistics table. |
| `getObservers` | `<Path>.getObservers → table` | Returns a table of observers. |
| `getXYWH` | `<Path>.getXYWH(byRef X:integer, byRef Y:integer, byRef Width:integer, byRef Height:integer)` | Retrieves dialog position and size. |
| `isNameUnique` | `<Path>.isNameUnique(NameToBeChecked:string) → boolean` | Tests whether an identifier is available in the object's namespace. |
| `memUsage` | `<Path>.memUsage → integer` | Returns object memory usage. |
| `moveToFolder` | `<Path>.moveToFolder(Folder:Path) → object` | Moves an object to a Class Library folder. |
| `openDialog` | `<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean` | Opens a dialog; optionally runs its Open Control. |
| `removeAllObservers` | `<Path>.removeAllObservers → boolean` | Removes all observers. |
| `removeObserver` | `<Path>.removeObserver(AttributeName:string, Method:method/void) → boolean` | Removes an observer. Pass `void` to remove references to nonexistent methods. |
| `replace` | `<Path>.replace(ObjectToReplace:object[, RetainInheritedValues:boolean:=false])` | Replaces an instance or merges/replaces a class with the calling Class Library class. |
| `setName` | `<Path>.setName(NewName:string) → boolean` | Renames an object and reports success. Names may contain letters, digits, and `_`, but cannot start with a digit. |
| `setPosition` | `<Path>.setPosition(X:integer, Y:integer[, CallMoveInFrameControl:boolean:=true])` | Places an instance icon in its Frame. |
| `setXYWH` | `<Path>.setXYWH(X:integer, Y:integer, Width:integer, Height:integer[, TotalSize:boolean:=true])` | Sets dialog position and size. Negative X or Y centers the dialog. |
| `showObject` | `<Path>.showObject` | Selects and reveals an instance or class. |
| `updateDialog` | `<Path>.updateDialog → boolean` | Refreshes an already open dialog. |
| `writeObject` | `<Path>.writeObject(FileName:string[, SaveAsLibrary:boolean:=false, Password:string]) → boolean` | Saves a Class Library class or folder as an object or library file. |

### Observers

`getObservers` returns a three-column table: observed value name, callback (object reference or relative path), and a Boolean that is true when the observer was created locally rather than inherited.

```simtalk
MyStation.addObserver("occupied", &myMethod)
print ParallelStation.attributeWatchable("NumMU")

// Delete locally created observers only.
var observerTable := Station.getObservers
for var row := 1 to observerTable.ydim
	if observerTable[3,row]
		if observerTable[2,row] /= void
			Station.removeObserver(observerTable[1,row], observerTable[2,row])
		else
			Station.removeObserver(observerTable[1,row], observerTable.asString(2,row))
		end
	end
next

MyStation.removeAllObservers
MyStation.removeObserver("occupied", "myMethod")
MyStation.removeObserver("occupied", &myMethod)
```

### Dialogs, naming, display, and memory

```simtalk
MyStore.closeDialog             // Apply dialog changes.
MyTrack.closeDialog(false)      // Discard dialog changes.

Buffer.openDialog
.drill.openDialog(false)
basis.Materialflow.Source.openDialog(true)
self.~.~.&MyMethod.openDialog  // Open the method editor instead of executing it.

Frame1.getXYWH(x, y, w, h)
print x, " ", y, " ", w, " ", h
MyStation.setXYWH(10, 100, 10, 20)
MyDataTable.setXYWH(-500, 100, 15, 25)

print .Hall2.isNameUnique("Station1")
print .Hall2.isNameUnique("Name")
print MyStation.setName("MyStation")
print FootPath1.memUsage

MyStation.setPosition(15, 400)
MyFrame.ParallelStation.showObject
EventController.StartDate := sysdate
EventController.updateDialog
```

### Object lifecycle and paths

Be especially careful with `deleteObject`: a class deletion removes all its instances. The EventController and Connector cannot be renamed.

```simtalk
.MaterialFlow.MyStation.deleteObject  // Delete a class.
MyStation.deleteObject                // Delete an instance.

var station := .MaterialFlow.Station.derive
station.Name := "TestCenter"
station.Coordinate3D := [4.0, 5.0, 0.0]
var newVariable: object := .InformationFlow.&Variable.derive

.MaterialFlow.Conveyor.duplicate(.Models.MyPlant, "MyConveyor")
var myConveyor: object := .MaterialFlow.Conveyor.duplicate(.Models.Model, "MyConveyor")
myConveyor.setPosition(100, 100)

var obj := MyFrame.extendPath("Station3")
if obj /= void
	obj.ProcTime := 63.5
end

.Resources.Exporter.moveToFolder(.Models)
.MaterialFlow.Station.replace(.MaterialFlow.MyStation, false)
```

### HTML reporting and saving

`getHTMLCode` accepts report statistics such as `%WorkingTime`, `%ResStates`, `%MatFlowProperties`, `%Energy`, `%DrainCumulated`, and transport/broker/importer/exporter statistics. Column selectors follow HtmlReport notation: `#Name`, `0`, `3`, `2..5`, `..5`/`*..5`, `5..`/`5..*`, and `*`.

```simtalk
print Source.getHTMLCode
Comment1.Cont := DataTable.getHTMLCode()          // Entire table.
Comment2.Cont := DataTable.getHTMLCode("caption")
Comment3.Cont := DataTable.getHTMLCode(1, 3)
Comment4.Cont := DataTable.getHTMLCode("1", 3)
Comment5.Cont := DataTable.getHTMLCode("1..2")
Comment6.Cont := DataTable.getHTMLCode("#A")

.InformationFlow.DataList.writeObject("MyDataList.psobj")
.MaterialFlow.ParallelStation.writeObject("mypp.psobj")
.ApplicationObjects.ProductionSystem.writeObject("MyLibrary.pslib", true)
```

## Object icon methods

Most icon methods affect the addressed **instance** icon. `getPixel` and `setPixel` do not apply to Variables, Comments, folders, or toolbars. Because class members share icons, `setPixel` changes the class icon and its derivatives.

| Method | Signature | Purpose |
|---|---|---|
| `createIcon` | `<Path>.createIcon(IconName:string, Width:integer, Height:integer) → integer` | Creates a transparent icon and returns its number. |
| `deleteIcon` | `<Path>.deleteIcon(IconName:string)` or `(IconNumber:integer)` | Deletes an icon. |
| `existsIcon` | `<Path>.existsIcon(IconName:string) → boolean` or `(IconNumber:integer)` | Tests whether an icon exists. |
| `getIconSize` | `<Path>.getIconSize(byRef Width:integer, byRef Height:integer)` | Retrieves current icon dimensions. |
| `getPixel` | `<Path>.getPixel(X:integer, Y:integer) → integer` | Retrieves packed RGB pixel data. |
| `putIconToClipboard` | `<Path>.putIconToClipboard(IconName:string) → boolean` or `(IconNumber:integer)` | Copies an icon to the Windows clipboard as `CF_BITMAP`. |
| `saveIconToFile` | `<Path>.saveIconToFile(IconName:string, FileName:string) → boolean` or `(IconNumber:integer, FileName:string)` | Exports an icon as PNG. |
| `setCurrIconFromClipboard` | `<Path>.setCurrIconFromClipboard(IconName:string) → boolean` or `(IconNumber:integer)` | Imports a bitmap from the clipboard and makes it current. |
| `setIconFromFile` | `<Path>.setIconFromFile(IconName:string, FileName:string) → boolean` or `(IconNumber:integer, FileName:string)` | Replaces an icon with an image file. |
| `setIconSize` | `<Path>.setIconSize(Width:integer, Height:integer)` | Resizes the current icon. |
| `setPixel` | `<Path>.setPixel(X:integer, Y:integer, RGB:integer) → integer` | Sets a pixel using an RGB value, e.g. from `makeRGBValue`. |

```simtalk
MyStation.createIcon("state", 20, 30)
MyParallelStation.deleteIcon("MyIcon")
print press.existsIcon("failed")

var w, h: integer
MyStation.getIconSize(w, h)
print w, " ", h

var rgb, red, green, blue: integer
rgb := MyStation.getPixel(1, 1)
red := rgb mod 256
green := (rgb div 256) mod 256
blue := rgb div (256 * 256)

MyStation.putIconToClipboard(3)
sp1.saveIconToFile("icon_name", "iconfile")
MyFrame.setCurrIconFromClipboard("MyIcon")
MyStation.setIconFromFile("failed", "C:\graphics\outOfOrder.gif")
MyStation.setIconSize(44, 44)
MyStation.setPixel(1, 1, makeRGBValue(255, 0, 255))
MyStation.redraw
```

## Location, predecessors, and successors

| Method | Signature | Purpose |
|---|---|---|
| `pred` | `<Path>.pred([PredecessorNumber:integer:=1]) → object` | Returns the selected material-flow predecessor. Interfaces and Frames are traversed to the effective predecessor. |
| `predConnector` | `<Path>.predConnector([PredecessorNumber:integer:=1]) → object` | Returns the connector from a predecessor, or `void`. Connection indexes can change after edits. |
| `succ` | `<Path>.succ([SuccessorNumber:integer:=1]) → object` | Returns the selected effective successor. For multi-successor Interfaces it obeys their exit strategy; a non-blocking strategy can return `void`. |
| `succConnector` | `<Path>.succConnector([SuccessorNumber:integer:=1]) → object` | Returns the connector to a successor, or `void`. |

```simtalk
if model.pred(3).name = "press"
	-- ...
end

for var i := MyTrack.NumPred downto 1
	MyTrack.predConnector(i).deleteObject
next

@.move(ParallelStation.succ(3))
MyTrack.succConnector.deleteObject
```

## Inheritance and attribute discovery

| Method | Signature | Purpose |
|---|---|---|
| `childNo` | `<Path>.childNo(Number:integer) → object` | Returns the indexed instance (child) of a class. Use `NumChildren` for the count. |
| `hasAttribute` | `<Path>.hasAttribute(AttributeName:string) → boolean` | Tests whether a readable attribute or method exists. |
| `inheritAttribute` | `<Path>.inheritAttribute(AttributeName:string)` | Re-enables inheritance for a built-in attribute. |
| `typeOf` | `<Path>.typeOf(ObjectToBeCompared:object) → boolean` | Tests whether two objects have the same internal class type. |

```simtalk
for var index := 1 to .MUs.Transporter.NumChildren
	print .MUs.Transporter.childNo(index)
next

print Station.hasAttribute("Availability")
print Conveyor.hasAttribute("Imp")
Conveyor.inheritAttribute("Length")
Station._3D.inheritAttribute("VisibleGraphicGroups")
print MyStation.typeOf(station2)
```

## Managing object attributes

| Method | Signature | Purpose |
|---|---|---|
| `getAttribute` | `<Path>.getAttribute(AttributeName:string[, byRef Inherited:boolean, byRef CanInherit:boolean]) → any` | Gets an attribute value and, optionally, inheritance metadata. For a method-valued user attribute, it returns the method object. |
| `getSubAttribute` | `<Path>.getSubAttribute(AttributeName:string, SubAttributeName:string[, Inherited:boolean]) → any` | Gets a sub-attribute; the optional variable receives inheritance state. |
| `putAttributeNamesIntoTable` | `<Path>.putAttributeNamesIntoTable(Table:table[, IncludeUserDefinedAttribute:boolean:=false, IncludeMethods:boolean:=false, Language:integer:=ModelLanguage])` | Lists attributes and optionally user attributes, methods, and read-only attributes. Language `0` is German and `1` is English. |
| `setAttribute` | `<Path>.setAttribute(AttributeName:string, Value:any)` | Sets an attribute value. |
| `setSubAttribute` | `<Path>.setSubAttribute(AttributeName:string, SubAttributeName:string, Value:any)` | Sets a sub-attribute value. |

```simtalk
print MyStation.getAttribute("ProcTime")
var inherited: boolean
print MyConveyor.getAttribute("Accumulating", inherited)

// Call a method-valued user-defined attribute explicitly.
var result := Station.getAttribute("MethodAttributeWith2Parameters").execute(5, 9)

var subAttributeInherited: boolean
print MyStation.getSubAttribute("ProcTime", "Type", subAttributeInherited)
MyStation.setAttribute("ProcTime", 5)
MyStation.setSubAttribute("ProcTime", "Type", "uniform")
Station.putAttributeNamesIntoTable(DataTable, true, true, UserInterfaceLanguage)
```

## User-defined attributes

### Definition and indexed access

| Method | Signature | Purpose |
|---|---|---|
| `createAttr` | `<Path>.createAttr(AttributeName:string, DataType:string) → boolean` | Creates a user-defined attribute and propagates it to instances. |
| `deleteAttr` | `<Path>.deleteAttr(AttributeName:string) → boolean` | Deletes a locally created, non-inherited user-defined attribute from the object and its instances. |
| `getAttrName` | `<Path>.getAttrName(AttributeNumber:integer) → string` | Returns the name at an attribute index. |
| `getAttrNo` | `<Path>.getAttrNo(AttributeName:string) → integer` | Returns the attribute index, or `0` if absent. |
| `getAttrType` | `<Path>.getAttrType(AttributeNumber:integer) → string` | Returns the data type at an index. |
| `getAttrValue` | `<Path>.getAttrValue(AttributeNumber:integer) → any` | Returns the value at an index. |
| `setAttrType` | `<Path>.setAttrType(AttributeNumber:integer, DataType:string) → boolean` | Changes the type. Supported types include `boolean`, `integer`, `real`, `string`, `object`, collection types, and units such as `time`, `money`, and `length`. |
| `setAttrValue` | `<Path>.setAttrValue(AttributeNumber:integer, Value:any) → boolean` | Changes the value at an index. |
| `unshare` | `<Path>.unshare` | Gives a table/list/stack/queue user attribute or Variable its own copy instead of a shared reference. |

```simtalk
MyStation.createAttr("lotsize", "integer")
MyStation.createAttr("inventoryNo", "string")
@.createAttr("Paint", "boolean")
.MUs.Part.deleteAttr("lotsize")

for var index := 1 to MyStation.NumAttr
	print MyStation.getAttrName(index)
	print MyStation.getAttrType(index)
next

var index: integer := MyStore.getAttrNo("Sale")
MyStore.setAttrType(index, "boolean")
MyStore.setAttrValue(index, true)
```

### Attribute presentation and inheritance

The user-defined attribute object supports its own `getAttribute`, `setAttribute`, and `inheritAttribute`. These operate on its metadata, such as initial value or presentation properties.

```simtalk
var isInherited, canInherit: boolean
MyStation.On.getAttribute("Value", isInherited, canInherit)
MyStation.Color.setAttribute("BackgroundColor", makeRGBValue(255, 87, 192))
MyStation.MyAttribute.inheritAttribute("InitValue")
```

### Collections, statistics, and incrementing

Collection assignments share the underlying collection by reference. Call `unshare` on one attribute before changing it when the values must become independent. `getStatisticsTable` writes an attribute's statistics to a target table; string values in its first column are lower-cased. `increment` is available only for numeric user-defined attributes and Variables.

```simtalk
Station.TabAttr := ParallelStation.TabAttr
Station.TabAttr[1, 1] := "Alice"
ParallelStation.TabAttr[1, 1] := "Bob"
print Station.TabAttr[1, 1]       // Prints Bob: both share the table.

ParallelStation.TabAttr.unshare
ParallelStation.TabAttr[1, 1] := "Charlie"
print Station.TabAttr[1, 1]       // Still prints Bob.

MyStation.MyAttribute.getStatisticsTable(MyStatisticsTable)
MyStation.MyAttribute.increment
MyStation.MyAttribute.increment(-1)
```
