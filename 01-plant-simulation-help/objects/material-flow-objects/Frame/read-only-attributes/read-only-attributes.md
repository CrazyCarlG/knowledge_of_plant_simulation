# Read-Only Attributes of the Frame

## Overview

Read-only attributes can be queried but cannot be set, because Plant Simulation computes their value at the point-in-time you query them. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

To view all methods, read-only attributes, and attributes of an object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show the members of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the **Home** ribbon tab of the Frame into which you inserted an instance, to show the members of the selected Instance.

To query the value of a read-only attribute, for example:

```simtalk
print .Models.Model.Capacity
```

The Frame provides the following read-only attributes:

- [Capacity](#capacity-simtalk---frame)
- [EventController](#eventcontroller-simtalk---frame)
- [NumberOfLimitedObjects](#numberoflimitedobjects-simtalk)
- [NumNodes](#numnodes-simtalk---frame)

---

## Capacity [SimTalk] - Frame

Returns the capacity of all static material flow objects located in the Frame designated by `<Path>`.

### Remarks

Plant Simulation does **not** include the capacities of MUs. When you place additional models into the selected model, Plant Simulation adds their capacities. If you insert at least one object with unlimited capacity (such as a Conveyor with a capacity of `-1`) in the Frame, Plant Simulation returns `-1`.

### Type

Read-only attribute

### Syntax

```simtalk
<Path>.Capacity → integer
```

### Watchable

The read-only attribute is watchable.

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Models.MyPlant.Capacity
```

---

## EventController [SimTalk] - Frame

Returns the EventController that is located in the root Frame.

### Type

Read-only attribute

### Syntax

```simtalk
EventController → object
```

### Return Value

The return value has the data type `object`.

### Example

```simtalk
print EventController // returns for example .Models.Model.EventController
```

### See also

- EventController [object]

---

## NumberOfLimitedObjects [SimTalk]

Counts the number of inserted objects per Frame containing an EventController.

### Remarks

Plant Simulation does **not** count the following objects: Lists and Tables, Methods, Variables, Comments, MUs, Connectors, Interfaces, EventControllers, the Toolbar, Folders, and Class objects.

> **Note:** `NumberOfLimitedObjects` applies to the Standard license, the Educational license, the Foundation license, and the Student license.

| License name       | Number of allowed objects |
| ------------------ | ------------------------- |
| Standard license   | 4000                      |
| Educational license| 1000                      |
| Foundation license | 500                       |
| Student license    | 80                        |

For the Student license, Plant Simulation shows the number of objects inserted into this Frame next to the name of the Frame, and the maximum number of allowed objects for the Student license, in the Class Library.

> **Note:** Plant Simulation only shows the value for Frames into which you inserted an EventController.

### Type

Read-only attribute

### Syntax

```simtalk
NumberOfLimitedObjects → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print NumberOfLimitedObjects // returns 10 for the Frame named 'Model'
```

### See also

- `numOfLimitedObjects` [SimTalk]
- Start Plant Simulation with Different Kinds of Licenses

---

## NumNodes [SimTalk] - Frame

Returns the number of objects in the Frame designated by `<Path>`.

### Remarks

Each additional Frame you insert into the selected Frame counts as a single object. Plant Simulation does **not** count the objects contained within the Frames. Connectors also count as objects.

### Type

Read-only attribute

### Syntax

```simtalk
<Path>.NumNodes → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Models.MyPlant.NumNodes
```

### See also

- `node` [SimTalk] - Frame
- Attributes of the Frame
