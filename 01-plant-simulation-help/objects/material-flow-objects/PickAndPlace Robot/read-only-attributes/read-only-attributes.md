# Read-Only Attributes of the PickAndPlaceRobot

The PickAndPlaceRobot provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print PickAndPlaceRobot.GetCurrentAngle
```

---

## Times Table notes

If you insert Connectors or if you drag an object onto the PickAndPlace robot and drop it there, Plant Simulation enters the respective values into the Times Table. For the calculation Plant Simulation assumes that a quarter-rotation requires one second. You can change these times.

If you delete a Connector, Plant Simulation does not delete the entry of the now unconnected object from the Times Table. You have to delete the entry in the Angles Table, for example by right-clicking the respective row and selecting **Delete Row** on the context menu. When you click **Apply** in the dialog box of the PickAndPlace robot, Plant Simulation also deletes this entry from the Times Table.

Example:

```simtalk
MyPickAndPlace.setTimesTable(myTimesTable)
```

See also: `getTimesTable [SimTalk]`, Times Table [PickAndPlace], Angles Table [PickAndPlace], Default Angle [PickAndPlace], Empty [state, material flow objects].

---

## GetCurrentAngle [SimTalk]

Returns the current angle at which the PickAndPlace robot designated by `<Path>` is located.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.GetCurrentAngle → object
```

**Return Value:** The return value has the data type `object`.

**Example:**

```simtalk
print PickAndPlace.GetCurrentAngle
```

---

## GetLastDestination [SimTalk]

Returns the last target object where the PickAndPlace robot designated by `<Path>` deposited the part or picked up the part.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.GetLastDestination → object
```

**Return Value:** The return value has the data type `object`.

**Example:**

```simtalk
print MyRobot.GetLastDestination
// might return .Models.MyRobot.Source
```

**SimTalk:** `setDestination [SimTalk] - PickAndPlace`, `getDestination [SimTalk] - PickAndPlace`.

---

## IsLoading [SimTalk]

Returns if the PickAndPlace robot designated by `<Path>` is in the state loading at the moment (`true`) or not (`false`).

**Remarks:**

Use `IsLoading` to observe the beginning and the end of the Loading Time. `IsLoading` is required to ensure the correct unloading of a Container/Transporter if you entered a Loading Time.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.IsLoading → boolean
```

**Watchable:** The read-only attribute is watchable.

**Return Value:** The return value has the data type `boolean`.

**Examples:**

```simtalk
print PickAndPlace.IsLoading
```

```simtalk
param SensorID: integer, Front: boolean, BookPos: boolean
var MU : object
@.Stopped  := true // stop
var Destination:object := Robot
MU := @.Cont
MU.Destination := Drain
if not MU.move(Destination)
   stopuntil MU.Location /= @ and not Destination.IsLoading
end
@.Stopped := false
```

**SimTalk:** `LoadingTime [SimTalk] - PickAndPlace`

**See also:** Loading Time [PickAndPlace].

---

## IsRotating [SimTalk]

Returns if the PickAndPlace robot designated by `<Path>` is rotating at the moment (`true`) or not (`false`).

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.IsRotating → boolean
```

**Return Value:** The return value has the data type `boolean`.

**Example:**

```simtalk
print PickAndPlace.IsRotating
```

---

## StatRotationEmptyPortion [SimTalk] - PickAndPlace

Returns the portion of the statistics collection period during which the PickAndPlace robot designated by `<Path>` was rotating empty, i.e., without transporting a part.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.StatRotationEmptyPortion → real
```

**Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyPickAndPlace.StatRotationEmptyPortion
```

**See also:** Tab Statistics [PickAndPlace], Statistics report, Rotation Time, Empty [state, material flow objects].

---

## StatRotationEmptyTime [SimTalk] - PickAndPlace

Returns the total time during which the PickAndPlace robot designated by `<Path>` was rotating empty, i.e., without transporting a part.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.StatRotationEmptyTime → time
```

**Return Value:** The return value has the data type `time`.

**Example:**

```simtalk
print MyPickAndPlace.StatRotationEmptyTime
```

**See also:** Statistics report, Rotation Time, Empty [state, material flow objects].

---

## StatRotationLoadedPortion [SimTalk] - PickAndPlace

Returns the portion of the statistics collection period during which the PickAndPlace robot designated by `<Path>` was rotating while transporting a part.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.StatRotationLoadedPortion → real
```

**Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyPickAndPlace.StatRotationLoadedPortion
```

**See also:** Tab Statistics [PickAndPlace], Statistics report, Rotation Time.

---

## StatRotationLoadedTime [SimTalk] - PickAndPlace

Returns the total time during which the PickAndPlace robot designated by `<Path>` was rotating while transporting a part.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.StatRotationLoadedTime → time
```

**Return Value:** The return value has the data type `time`.

**Example:**

```simtalk
print MyPickAndPlace.StatRotationLoadedTime
```

**See also:** Statistics report, Rotation Time.
