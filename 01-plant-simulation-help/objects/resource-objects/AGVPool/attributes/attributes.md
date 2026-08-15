# AGVPool Attributes

This document summarizes the read-only attributes and attributes of the AGVPool object from the Plant Simulation Help.

## Overview

The AGVPool provides:

- The attributes listed below.
- The Attributes of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute:

```simtalk
MyAGVPool.BrokerPath := mybroker
```

- To get the value of an attribute:

```simtalk
MyAGVPool.AGV := ".UserObjects.MyAGV"
```

---

## StatAverageTraveledDistance [SimTalk]

Returns the average distance in meters which the AGVs of the AGVPool designated by `<Path>` traveled.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatAverageTraveledDistance → length
```

- **Return Value:** The return value has the data type `length`.

**Example:**

```simtalk
print AGVPool.StatAverageTraveledDistance
```

---

## AGV [SimTalk]

Sets the AGVs which the AGVPool designated by `<Path>` creates.

- **Type:** Attribute
- **Syntax:**

```simtalk
<Path>.AGV:path
```

- **Assignment Value:** You can assign a value of data type `path`.

**Remarks:**

> By default the Transporter in the folder MUs in the Class Library is the AGV. For this reason the methods, attributes, and read-only attributes of the Transporter apply to the AGV as well.

Plant Simulation creates the specified Amount of vehicles during the init phase of the simulation run.

**Examples:**

```simtalk
MyAGVPool.AGV := ".UserObjects.MyAGV"
```

```simtalk
var AGV : object := AGVPool.Cont
AGV.setRoute([M1,M2,M3,M4])
waituntil AGV.DestinationWasReached
AGV.setRoute([M1,M2,M3,M4])
```

**See also:**

- AGV [text box]
- AGV [SimTalk]
- setRoute [SimTalk] - Transporter
- setRouteSegments [SimTalk]

---

## Amount [SimTalk]

Sets the amount of AGVs which the AGVPool designated by `<Path>` creates.

- **Type:** Attribute
- **Syntax:**

```simtalk
<Path>.Amount:integer
```

- **Assignment Value:** You can assign a value of data type `integer`.

**Remarks:**

Plant Simulation creates the specified Amount of AGVs during the init phase of the simulation run.

**Example:**

```simtalk
MyAGVPool.Amount := 2
```

**See also:**

- Amount [text box] - AGVPool
- AGV [SimTalk]
- Marker

---

## Marker

Use the object **Marker** for setting waypoints in your simulation model along which the Automated Guided Vehicle drives from the AGVPool to its destination.
