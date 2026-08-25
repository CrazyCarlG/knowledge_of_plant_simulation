# Common Read-Only Attributes — Objects Reference

This document summarizes the **read-only attributes** that are common to all Plant Simulation objects (Class Library objects). Read-only attributes can be queried but cannot be set — Plant Simulation computes the value at the point in time when you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (e.g. the **Statistics** tab).

Each entry preserves the original SimTalk code samples so you can use them as starting points.

> Source: *Plant Simulation Help* (Unpublished work. © 2026 Siemens). Pages referenced: 11-732 … 11-748.

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Read-Only Attributes](#2-read-only-attributes)
  - [`~` (tilde) / `Location` — material flow objects](#--tilde--location--simtalk--material-flow-objects)
  - [`Class` — read-only attribute](#class--simtalk--read-only-attribute)
  - [`InternalClassType`](#internalclasstype--simtalk)
  - [`Location` — material flow objects (alias of `~`)](#location--simtalk--material-flow-objects)
  - [`NumAttr`](#numattr--simtalk)
  - [`NumChildren`](#numchildren--simtalk)
  - [`Origin` — general description](#origin--simtalk--general-description)
  - [`OriginRoot`](#originroot--simtalk)
  - [`RootFrame`](#rootframe--simtalk)
  - [`UUID`](#uuid--simtalk)

---

## 1. Overview

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class [general description]**.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected **Instance [general description]**.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Source.Empty
```

---

## 2. Read-Only Attributes

### `~` (tilde) [SimTalk] — material flow objects

Returns the object located directly above `<Path>` in the object hierarchy.

- For an **MU**, the location is the object on which it is currently located.
- For **all other objects**, the location is the Frame in which they are located.
- **Watchable.**
- **Returns:** `object`. `VOID` if the Worker or the AGV is on its way to its destination.

```simtalk
print "shaft is located on:", @.~
print "shaft is located on:", @.Location

print Preparing.~
-- Preparing is the name of a Conveyor
-- returns .Models.MyCarAssembly.PaintShop.PaintLine1
-- PaintLine1 is the name of the Frame

print .MUs.Part:9.~
-- location of Part 9
-- returns .Models.MyCarAssembly.PaintShop.PaintLine1.Preparing
-- Preparing is the name of a Conveyor
```

**See also:** `LocationInFrame`, Open Location [on the Home Ribbon Tab].

---

### `Class` [SimTalk] — read-only attribute

Returns the class in the Class Library from which `<Path>` was derived or instantiated, possibly over several levels.

> Example: we copied the object `Frame` three times and named it `Frame1`, `Frame2`, and `Frame3`. Then, we insert `Frame1` into `Frame2`, and `Frame2` into `Frame3`. When we call `.Frame3.Frame2.Frame1.Class`, the result will be `.Frame1` because `.Frame1` is the object in the Class Library from which `.Frame3.Frame2.Frame1` was derived.

> If you use `Class` for an instance of an object, Plant Simulation moves up in the inheritance structure until it reaches an object in the Class Library. It then opens this object.

```simtalk
if class_change
   current.Class.openDialog
end
```

**See also:** Class [general description], Open Class, Go to Class.

---

### `InternalClassType` [SimTalk]

Returns the unique built-in English object name that describes the type of `<Path>`.

> The `InternalClassType` is **not** the localized object name shown by some localized versions of Plant Simulation — it is the English object name.

#### Return Value Table (English / German)

| English Object Name | German Object Name |
|---|---|
| ActiveX | ActiveX |
| AngularConverter | Eckumsetzer |
| AssemblyStation | Montagestation |
| AttributeExplorer | AttributExplorer |
| Basis | Basis |
| Broker | Broker |
| Buffer | Puffer |
| Button | Schaltfläche |
| Chart | Diagramm |
| Checkbox | Kontrollkästchen |
| Comment | Kommentar |
| Connector | Kante |
| Container | Förderhilfsmittel |
| Converter | Umsetzer |
| Conveyor | Förderstrecke |
| Cycle | Takt |
| DataList | Kartei |
| DataStack | Stapel |
| DataTable | Tabelle |
| DatatQueue | Warteschlange |
| DePortioner | Entportionierer |
| Dialog | Dialog |
| DismantleStation | Demontagestation |
| Display | Display |
| Drain | Senke |
| DropDownList | Dropdownliste |
| EventController | Ereignisverwalter |
| Exporter | Exporter |
| FileInterface | Dateischnittstelle |
| FileLink | Dateiverknüpfung |
| FlowControl | Flusssteuerung |
| FluidDrain | Flüssigkeitssenke |
| FluidSource | Flüssigkeitsquelle |
| Folder | Ordner |
| FootPath | Fußweg |
| Frame | Netzwerk |
| GanttChart | GanttDiagramm |
| GAOptimization | GAOptimierung |
| GARangeAllocation | GABereichszuordnung |
| GASelection | GASelektion |
| GASequence | GAReihenfolge |
| GASetAllocation | GAMengenzuordnung |
| Generator | Generator |
| Interface | Übergang |
| LockoutZone | Schutzkreis |
| Method | Methode |
| Mixer | Mixer |
| MQTT | MQTT |
| ODBC | ODBC |
| OPCClassicInterface | OPCClassicSchnittstelle |
| OPCUAInterface | OPCUASchnittstelle |
| Oracle | Oracle |
| ParallelStation | Parallelstation |
| Part | Fördergut |
| PatchMatrix | PatchMatrix |
| PickAndPlace | PickAndPlace |
| Pipe | Rohr |
| PlaceBuffer | PlatzPuffer |
| Portioner | Portionierer |
| Report | Bericht |
| ShiftCalendar | Schichtkalender |
| SIMIT | SIMIT-Schnittstelle |
| Socket | Socket |
| Sorter | Sortierer |
| Source | Quelle |
| SQLite | SQLite |
| Station | Einzelstation |
| Store | Lager |
| Tank | Tank |
| Teamcenter | Teamcenter |
| TimeSequence | Zeitleiste |
| Toolbar | Symbolleiste |
| Track | Weg |
| Transporter | Fahrzeug |
| Trigger | Trigger |
| Turnplate | Drehplatte |
| Turntable | Drehtisch |
| TwoLaneTrack | ZweispurigerWeg |
| Variable | Variable |
| Worker | Werker |
| WorkerPool | WerkerPool |
| Workplace | Arbeitsplatz |
| XMLInterface | XMLSchnittstelle |

- **Syntax:** `<Path>.InternalClassType → string`

```simtalk
print MyStation.InternalClassType
-- returns "Station", works for a Station, which you inserted into a Frame

print .UserObjects.MyStation.InternalClassType
-- returns "Station"
```

**See also:** `_3D.InternalClassType`, `typeOf`.

---

### `Location` [SimTalk] — material flow objects

Returns the object located directly above `<Path>` in the object hierarchy. **Identical to the `~` (tilde) attribute.**

- For an **MU**, the location is the object on which it is currently located.
- For **all other objects**, the location is the Frame in which they are located.
- **Watchable.**
- **Returns:** `object`. `VOID` if the Worker or the AGV is on its way to its destination.

```simtalk
print "shaft is located on:", @.Location
print "shaft is located on:", @.~

print Preparing.Location
-- Preparing is the name of a Conveyor
-- returns .Models.MyCarAssembly.PaintShop.PaintLine1
-- PaintLine1 is the name of the Frame

print .MUs.Part:9.Location
-- location of Part 9
-- returns .Models.MyCarAssembly.PaintShop.PaintLine1.Preparing
-- Preparing is the name of a Conveyor
```

**See also:** `LocationInFrame`, Open Location [on the Home Ribbon Tab].

---

### `NumAttr` [SimTalk]

Returns the number of user-defined attributes of `<Path>`. The first user-defined attribute has the number 1. `0` if no user-defined attributes exist.

- **Syntax:** `<Path>.NumAttr`
- **Returns:** `integer`

```simtalk
var index: integer
for index := 1 to MyStation.NumAttr
    print MyStation.getAttrName(index)
next
```

**See also:** User-defined Attributes [general description], New [user-defined attribute].

---

### `NumChildren` [SimTalk]

Returns the number of children of `<Path>` that inherit their settings from it.

- **Syntax:** `<Path>.NumChildren → integer`

```simtalk
print MyStation.NumChildren
print Transporter.NumChildren
```

**See also:** `childNo`, Instance [general description].

---

### `Origin` [SimTalk] — general description

Returns the object from which `<Path>` was derived **most recently**.

> Example: we copied the object `Frame` three times and named it `Frame1`, `Frame2`, and `Frame3`. Then, we insert `Frame1` into `Frame2`, and `Frame2` into `Frame3`. When we call `.Frame3.Frame2.Frame1.Origin`, the result will be `.Frame2.Frame1`, as `.Frame2.Frame1` is the object from which `.Frame3.Frame2.Frame1` was derived most recently.

```simtalk
if local_change
   current.openDialog
else
   current.Origin.openDialog
end
```

**See also:** `OriginRoot`, Show Origin [class library], Open Origin, Go to Origin.

---

### `OriginRoot` [SimTalk]

Returns the root object of the inheritance chain if `<Path>` was inherited across several levels.

- **Syntax:** `<Path>.OriginRoot → object`

```simtalk
print Station2111111.OriginRoot
-- might return .MaterialFlow.Station2
```

**See also:** `Origin`.

---

### `RootFrame` [SimTalk]

Returns the root frame of `<Path>`. The root frame is the Frame located highest up in the hierarchy of Frames; it is always located in a folder.

- **Syntax:** `<Path>.RootFrame → object`
- **Returns:** `object`. `VOID` if no root frame exists — this applies to all classes that are not of type `Frame`.

```simtalk
print MyDialog.RootFrame
-- might return .Models.Model
```

---

### `UUID` [SimTalk]

Returns the UUID (Universally Unique Identifier) of `<Path>`. The UUID remains constant during the object's entire lifetime.

- **Syntax:** `<Path>.UUID → string`

```simtalk
print Station.UUID
-- returns 3daf7c80-9411-4671-966f-f3ecd2c0f478 for example
```

**See also:** What is a Folder Model?, Attributes of All Objects.

---

*Source: Plant Simulation Help — "Objects — Read-Only Attributes of All Objects". Unpublished work. © 2026 Siemens.*