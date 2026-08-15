# Read-Only Attributes of the DismantleStation

The DismantleStation provides:

- The read-only attributes listed in the table of contents.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, because Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print DismantleStation.NumLeavingMU
```

---

## statBlockingTimeTable [SimTalk]

Returns the contents of the table **Blocking Times** of the DismantleStation designated by `<Path>` and writes it into the table.

- **Type:** Method
- **Syntax:** `<Path>.statBlockingTimeTable(BlockingTimes:table) → boolean`

**Parameter**

The parameter `BlockingTimes` of data type `table` designates the name of the table.

**Return Value**

The return value has the data type `boolean`.

**Example**

```simtalk
var myBlockingTimesTable: table
MyDismantleStation.statBlockingTimeTable(myBlockingTimesTable)
```

**See also**

- Tab Statistics [DismantleStation]

---

## NumLeavingMU [SimTalk]

Returns the number of MUs contained in the table **Exiting MUs** of the DismantleStation designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.NumLeavingMU → integer`

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
for var i := 1 to MyDismantleStation.NumLeavingMU
   print MyDismantleStation.leavingMU(i)
next
```

**See also**

- Exiting MUs

---

## StatAverageDwellTime [SimTalk] - DismantleStation

Returns the average time which the main parts stayed on the DismantleStation designated by `<Path>`.

**Remarks**

Plant Simulation only counts times during which the DismantleStation was not paused and not unplanned.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatAverageDwellTime → time`

**Return Value**

The return value has the data type `time`.

**Example**

```simtalk
print MyDismantleStation.StatAverageDwellTime
```

**See also**

- Tab Statistics [DismantleStation]
- Attributes of the DismantleStation
- _Attributes of the DismantleStation

The DismantleStation provides:

- The attributes listed in the table of contents.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
