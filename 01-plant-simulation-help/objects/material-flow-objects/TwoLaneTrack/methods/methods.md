# Methods of the TwoLaneTrack

The TwoLaneTrack provides:

- The methods listed below.
- The Methods of Curved Objects.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

> **Note:** A number of methods shared with the other material flow objects apply to a **lane** instead of to the entire object.

To view all methods, read-only attributes, and attributes of the object, open **Show Attributes and Methods**. For the TwoLaneTrack, the dialog shows `A` and `B` for the respective lane, but not the methods proper for these lanes.

You can:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance.

An example of the syntax line of individual methods:

```
<Path>.A.exitBlockList([ExitBlockingList:table]) -> object[]
<Path>.B.exitBlockList([ExitBlockingList:table]) -> object[]
```

- `<Path>` designates the path of the object to which the method applies.
- `A` or `B` designates the lane of the TwoLaneTrack you want to access.
- The signature (identifier and parameter data type) is listed in parentheses. `(Parameter:string)` designates a parameter of data type string.
- Optional parameters are listed within brackets, e.g. `[,Parameter:boolean]`.
- If a parameter has a default value, the signature shows the default value after the parameter.
- If a method has a return value, the signature shows its data type after the arrow `->`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses (…). Not entering them may lead to unexpected results and open the Debugger.

---

## Methods

### bwBlockList [SimTalk] - lane A or B

Returns the blocking list in the backward direction of the specified lane of the TwoLaneTrack designated by `<Path>`.

**Syntax**

```
<Path>.A.bwBlockList([BackwardBlockingList:table]) → any
<Path>.B.bwBlockList([BackwardBlockingList:table]) → any
```

**Parameter**

- `BackwardBlockingList` (table, optional): name of the table (a DataTable or a local variable) into which the method writes the values. Plant Simulation automatically generates a table with two columns:
  - Column 1 (object): all Transporters that unsuccessfully tried to move to the object.
  - Column 2: the simulation time at which the Transporters attempted to enter the object.

**Return Value**

- `any` — an array containing all MUs in the Backward Blocking List of the specified lane, if you do not specify the optional parameter.

**Example**

```
MyTwoLaneTrack.B.bwBlocklist(DataTable)
```

**See also:** Backward Blocking List, Check the Contents List of the Stations, `BlockingStarttime [SimTalk]`, `BwBlockListEntry1 [SimTalk]`

---

### contentsList [SimTalk] - lane A or B

Returns the entire Contents — all Transporters located on the specified lane of the Contents List of the TwoLaneTrack designated by `<Path>`.

**Syntax**

```
<Path>.A.contentsList([ContentsList:table]) → any
<Path>.B.contentsList([ContentsList:table]) → any
```

**Parameter**

- `ContentsList` (table, optional): name of the table. Plant Simulation automatically generates the format and deletes any existing format and contents. The contents list is a table with three columns:
  - Column 1 (object): path to the Transporters.
  - Column 2 (length): start position of the MU part.
  - Column 3 (length): end position.

**Return Value**

- `any` — an array containing the objects in the Contents List if you do not specify the optional parameter.

**Examples**

```
MyTwoLaneTrack.A.contentsList(DataTable)
print TwoLaneTrack.A.contentsList
// might, for example, return [.MUs.Transporter:314, 34.488399, 35.988399]
// [.MUs.Transporter:316, 32.988399, 34.488399]
// [.MUs.Transporter:318, 31.488399, 32.988399]
// [.MUs.Transporter:320, 29.988399, 31.488399] in the Console
```

**See also:** Contents [material flow objects], Check the Contents List of the Stations

---

### exitBlockList [SimTalk] - lane A or B

Returns the Exit Blocking List of the specified lane of the TwoLaneTrack designated by `<Path>`.

**Syntax**

```
<Path>.A.exitBlockList([ExitBlockingList:table]) -> object[]
<Path>.B.exitBlockList([ExitBlockingList:table]) -> object[]
```

**Parameter**

- `ExitBlockingList` (table, optional): name of the table (a DataTable or a local variable). Plant Simulation automatically generates a table with two columns:
  - Column 1 (object): Transporters that unsuccessfully tried to exit the object.
  - Column 2: simulation time at which the Transporters attempted to enter the object.

**Return Value**

- `any` — an array containing the objects in the Exit Blocking List (one-dimensional, only the objects in the blocking list), if no optional parameter is given.

**Example**

```
MyTwoLaneTrack.B.exitBlockList(DataTable)
```

**See also:** Exit Blocking List, Check the Contents List of the Stations, `BlockingStarttime [SimTalk]`

---

### fwBlockList [SimTalk] - lane A or B

Returns the Blocking List in the forward direction of the specified lane of the TwoLaneTrack designated by `<Path>`.

**Syntax**

```
<Path>.A.fwBlockList([ForwardBlockingList:table]) -> any
<Path>.B.fwBlockList([ForwardBlockingList:table]) -> any
```

**Parameter**

- `ForwardBlockingList` (table, optional): name of the table (a DataTable or a local variable). Plant Simulation automatically generates a table with two columns:
  - Column 1 (object): Transporters that unsuccessfully tried to move to the object.
  - Column 2: simulation time at which the Transporters attempted to enter the object.

**Return Value**

- `any` — an array containing the objects in the Forward Blocking List, if no optional parameter is given.

**Example**

```
MyTwoLaneTrack.B.fwBlockList(DataTable)
```

**See also:** Forward Blocking List, Check the Contents List of the Stations, `BlockingStarttime [SimTalk]`

---

### getRouteLength [SimTalk] - lane A or B

Returns the shortest route from the lane of the TwoLaneTrack designated by `<Path>` to the target and returns the length of this route.

**Syntax**

```
<Path>.A.getRouteLength(Target:path[, Backwards:boolean, Position:length, ObjectsAlongRoute:table, RouteWeightingAttribute:string] → length
<Path>.B.getRouteLength(Target:path[, Backwards:boolean, Position:length, ObjectsAlongRoute:table, RouteWeightingAttribute:string] → length
```

**Parameters**

- `Target` (path): designates the target. Can be a material flow object reached directly via Connectors, or a destination typed into a sensor.
- `Backwards` (boolean, optional): direction in which Plant Simulation looks for a route. `true` = backward, `false` = forward (default).
- `Position` (length, optional): position on the lane at which the search starts. If omitted, Plant Simulation starts at the end of the lane (forward) or at the beginning (backward).
- `ObjectsAlongRoute` (table, optional): writes the objects along the route into the specified table.
- `RouteWeightingAttribute` (string, optional): name of the attribute for route weighting for automatic routing. If not passed, Plant Simulation does not weight the route lengths.

> **Note:** As the route is intended for Transporters, Plant Simulation only takes objects of type Track and TwoLaneTrack into consideration when computing the route.

**Return Value**

- `length` — `-1` if Plant Simulation did not find a route.

**Example**

```
print TwoLaneTrack5.B.getRouteLength(Track26)
```

**See also:** Destination [SimTalk] - sensors, RouteWeightingAttr [SimTalk] - Transporter

---

### pred [SimTalk] - lane A or B

Returns the direct predecessor of the designated lane of the TwoLaneTrack designated by `<Path>`.

**Syntax**

```
<Path>.A.pred([PredecessorNumber:integer:=1]) → object
<Path>.B.pred([PredecessorNumber:integer:=1]) → object
```

**Parameter**

- `PredecessorNumber` (integer, optional): the n-th predecessor. Objects have to be connected. Default value is `1`.

**Return Value**

- `object`

**Example**

```
if MyTwoLaneTrack.A.pred(3) = TwoLaneTrack1
  ...
end
```

**See also:** succ [SimTalk] - lane A or B

---

### predConnector [SimTalk] - lane A or B

Returns the incoming Connector connected directly with the specified lane of the TwoLaneTrack designated by `<Path>`.

> Adding and deleting connections may change the index number of a connection.

**Syntax**

```
<Path>.A.predConnector([PredecessorNumber:integer:=1]) → object
<Path>.B.predConnector([PredecessorNumber:integer:=1]) → object
```

**Parameter**

- `PredecessorNumber` (integer, optional): n-th preceding Connector. Default value is `1`.

**Return Value**

- `object` — `VOID` if the connection does not exist.

**Example**

```
for var i := MyTwoLaneTrack.B.NumPred downto 1 // deletes connections
   MyTwoLaneTrack.B.predConnector(i).deleteObject
next
```

**See also:** succConnector [SimTalk] - lane A or B

---

### predLane [SimTalk] - lane A or B

Returns the direct predecessor of the designated lane of the TwoLaneTrack designated by `<Path>`.

**Syntax**

```
<Path>.A.predLane([Predecessor:integer]) → any
<Path>.B.predLane([Predecessor:integer]) → any
```

**Parameter**

- `Predecessor` (integer, optional): the lane of the n-th predecessor of the TwoLaneTrack. Objects have to be connected.

**Return Value**

- `any`

**Example**

```
if MyTwoLaneTrack.A.predLane(3) = TwoLaneTrack1.B
  ...
end
```

**See also:** succLane [SimTalk] - lane A or B

---

### predLaneNo [SimTalk] - lane A or B

Returns the number of the preceding lane of the specified lane of the TwoLaneTrack designated by `<Path>`.

> Only works if the objects are connected.

**Syntax**

```
<Path>.A.predLaneNo([Predecessor:integer]) → integer
<Path>.B.predLaneNo([Predecessor:integer]) → integer
```

**Parameter**

- `Predecessor` (integer, optional): the number of the lane of the n-th predecessor. Objects have to be connected.

**Return Value**

- `integer`

**Example**

```
if MyTwoLaneTrack.A.predLaneNo(3) = 2
   print "third preceeding lane is lane B"
end
```

**See also:** succLaneNo [SimTalk] - lane A or B

---

### succ [SimTalk] - lane A or B

Returns the direct successor of the specified lane of the TwoLaneTrack designated by `<Path>`.

**Syntax**

```
<Path>.A.succ([SuccessorNumber:integer:=1]) → object
<Path>.B.succ([SuccessorNumber:integer:=1]) → object
```

**Parameter**

- `SuccessorNumber` (integer, optional): the number of the successor on the specified lane. Default value is `1` (the first successor on the lane).

**Return Value**

- `object`

**Notes:**

- If the n-th successor is an **Interface**, Plant Simulation does not return the Interface itself but the successor of the Interface (tracked until a material flow object that can accept MUs is reached).
- If the n-th successor is a **Frame**, Plant Simulation returns the successor of the Interface inserted into the Frame.
- If an Interface has a single successor, that successor is uniquely identified and used independent of the exit strategy.
- If an Interface has several successors, the successor is identified according to its exit strategy (blocking strategy determines the successor regardless of whether it can accept an MU; non-blocking strategy searches for the next successor that can accept an MU).
- If none of the successors can accept an MU, the method returns `VOID` (except when there is only a single successor).

**Example**

```
if MyTwoLaneTrack.B.succ = TwoLaneTrack1
  ...
end
```

**See also:** pred [SimTalk] - lane A or B

---

### succConnector [SimTalk] - lane A or B

Returns the outgoing Connector connected directly with the specified lane of the TwoLaneTrack designated by `<Path>`.

> Adding and deleting connections may change the index number of a connection.

**Syntax**

```
<Path>.A.succConnector([SuccessorNumber:integer:=1]) → object
<Path>.B.succConnector([SuccessorNumber:integer:=1]) → object
```

**Parameter**

- `SuccessorNumber` (integer, optional): the successor on the specified lane. Default value is `1` (the first succeeding connector on the lane).

**Return Value**

- `object` — `VOID` if the connection does not exist.

**Example**

```
myTwoLaneTrack.B.succConnector.deleteObject
```

**See also:** predConnector [SimTalk] - lane A or B

---

### succLane [SimTalk] - lane A or B

Returns the direct successor of the designated lane of the TwoLaneTrack designated by `<Path>`.

**Syntax**

```
<Path>.A.succLane([Successor:integer]) → any
<Path>.B.succLane([Successor:integer]) → any
```

**Parameter**

- `Successor` (integer, optional): the lane of the n-th successor of the TwoLaneTrack. Objects have to be connected.

**Return Value**

- `any`

**Example**

```
if MyTwoLaneTrack.B.succLane = TwoLaneTrack1.A
  ...
end
```

**See also:** predLane [SimTalk] - lane A or B

---

### succLaneNo [SimTalk] - lane A or B

Returns the number of the succeeding lane of the specified lane of the TwoLaneTrack designated by `<Path>`.

**Syntax**

```
<Path>.A.succLaneNo([LaneNumber:integer]) → integer
<Path>.B.succLaneNo([LaneNumber:integer]) → integer
```

**Parameter**

- `LaneNumber` (integer, optional): the number of the lane of the n-th successor lane. Objects have to be connected.

**Return Value**

- `integer`

**Example**

```
if MyTwoLaneTrack.A.succLaneNo = 1
   print "succeeding lane is lane A"
end
```

**See also:** predLaneNo [SimTalk] - lane A or B

---

## Read-Only Attributes of the TwoLaneTrack

The TwoLaneTrack provides:

- The read-only attributes listed in the table of contents.
- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.
