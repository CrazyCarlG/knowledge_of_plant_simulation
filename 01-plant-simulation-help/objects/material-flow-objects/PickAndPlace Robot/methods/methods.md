# Methods of the PickAndPlace Robot

The PickAndPlace robot provides:

- The methods listed in the table of contents.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show them for the selected Instance.

## Syntax line example

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The method signature (identifier and parameter data types) is listed in parentheses. `(Parameter:string)` designates a parameter of data type string. Instead of a constant, you can use a variable of the required type or a method that returns the required type.
- Optional parameters are listed in brackets, e.g. `[,Parameter:boolean]`.
- Default values are shown after the parameter with `:=`, e.g. `:= false`.
- Return values are shown after the arrow `→`, e.g. `→ boolean`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

---

## calculateAngles [SimTalk] - PickAndPlace

Computes the angles at which the PickAndPlace robot (designated by `<Path>`) is connected with its predecessor and successor in the Frame.

**Remarks:** The PickAndPlace robot enters the angles into the Angles Table.

**Type:** Method

**Syntax:**

```
<Path>.calculateAngles
```

**Example:**

```
MyPickAndPlace.calculateAngles
```

**See also:** `getAnglesTable`, `setAnglesTable`, Calculate Angles, Angles Table.

---

## getAnglesTable [SimTalk]

Returns the Angles Table of the PickAndPlace robot (designated by `<Path>`) and writes it into a table.

**Type:** Method

**Syntax:**

```
<Path>.getAnglesTable(AnglesTable:table) -> table
```

**Parameter:** `AnglesTable` (data type `table`) designates the name of the table. It contains:

- The **Name** of the predecessor where the robot picks the part up, or the **Name** of the successor where the robot deposits the part. The `Name` column can also contain a sensor on the Conveyor, e.g. `Conveyor.sensorID(1)`.
- The **Angle** between the station in the `Name` column and the PickAndPlace robot.

When you insert Connectors or drag an object onto the PickAndPlace robot and drop it, Plant Simulation adds the respective values to the angles table. Deleting a Connector does **not** remove the corresponding entry from the table; you must do this manually. You can also manually change values/names or add new stations — useful, for example, for requesting the robot in a Sensor Control.

> **Note:** Plant Simulation automatically applies changed names of stations to the Times Table.

**Return Value:** data type `table`.

**Example:**

```
var myAnglesTable: table
MyPickAndPlace.getAnglesTable(myAnglesTable)
```

**See also:** `setAnglesTable`, `calculateAngles`, Angles Table, Times Table.

---

## getDestination [SimTalk] - PickAndPlace

Returns the target object where the PickAndPlace robot (designated by `<Path>`) is to pick up or deposit the part.

**Type:** Method

**Syntax:**

```
<Path>.getDestination → any
```

**Return Value:** data type `any`. It is either the target object, the target place on the target object, or a sensor on the target object. It also returns a target object if the robot rotates to the target without transporting a part.

**Examples:**

```
// sets and gets the target of the part
PickAndPlace.setDestination(@.target, true)
print PickAndPlace.getDestination

end
MyStation := ?.getDestination
```

**See also:** `setDestination`, `GetLastDestination`.

---

## getTimesTable [SimTalk]

Returns the Times Table of the PickAndPlace robot (designated by `<Path>`) and writes it into a table.

**Type:** Method

**Syntax:**

```
<Path>.getTimesTable(TimesTable:table) -> table
```

**Parameter:** `TimesTable` (data type `table`) designates the name of the table. The times table contains:

- The **Names** of all objects the robot is to serve, and the **Default Angle** to which the robot moves after depositing the part.
- The **Times above the diagonal** are the times during which the robot rotates empty.
- The **Times below the diagonal** are the times during which the robot rotates full (while a part is located on it).
- The diagonal runs from the topmost cell in the "default angle" column to the bottommost cell in the last column.

In the example, cell A contains the rotation time from the Station to the Source with picked-up parts (0.3743 seconds), cell B the rotation time from the Drain to the Source without parts, and cell C the rotation time from Drain1 to the Default Angle without parts.

When you insert Connectors or drag an object onto the robot and drop it, Plant Simulation enters the respective values into the Times Table. For the calculation, Plant Simulation assumes a quarter-rotation takes one second. You can change these times.

If you delete a Connector, Plant Simulation does **not** delete the entry of the now-unconnected object from the Times Table. You have to delete the entry in the Angles Table (e.g. right-click the row → Delete Row). When you click **Apply** in the robot's dialog, Plant Simulation also deletes this entry from the Times Table.

**Return Value:** data type `table`.

**Examples:**

```
MyPickAndPlace.getTimesTable(myTimesTable)
var myTimesTable: table
MyPickAndPlace.getTimesTable(myTimesTable)
```

**See also:** `setTimesTable`, Times Table, Angles Table, Default Angle, Empty.

---

## setAnglesTable [SimTalk]

Assigns an Angles Table to the PickAndPlace robot (designated by `<Path>`).

**Type:** Method

**Syntax:**

```
<Path>.setAnglesTable(AnglesTable:table)
```

**Parameter:** `AnglesTable` (data type `table`) designates the name of the table. You can change these values:

- The **Name** of the predecessor where the robot picks up the part, or the **Name** of the successor where the robot deposits the part. You can also enter a sensor on the Conveyor (e.g. `Conveyor.Sensors.id1`), useful to set several angles on the Conveyor.
- The **Angle** between the station in the `Name` column and the PickAndPlace robot.

When you insert Connectors or drag an object onto the robot, Plant Simulation adds the respective values. Deleting a Connector does not remove the entry; do this manually. You can also manually change values/names or add new stations (e.g. for requesting the robot in a Sensor Control).

> **Note:** Plant Simulation automatically applies changed names of stations to the Times Table.

**Example:**

```
MyPickAndPlace.setAnglesTable(myAngleTable)
```

**See also:** `getAnglesTable`, `calculateAngles`, Angles Table, Times Table.

---

## setDestination [SimTalk] - PickAndPlace

Sets the target object at which the PickAndPlace robot (designated by `<Path>`) deposits the part or wants to pick up a new part.

**Remarks:** Typically used in the Target Control / TargetCtrl. When you send the robot to a station with `setDestination`, the MUs on that station are unblocked as follows:

1. First, an already-waiting MU for which the robot was requested is unblocked.
2. If not the case, the Pull Control is called (if it exists).
3. If neither applies, the MU in the Blocking List that was scheduled first is unblocked.

**Type:** Method

**Syntax:**

```
<Path>.setDestination(DestinationObject:any[, WaitAtTarget:boolean])
<Path>.setDestination(DefaultPosition:void)
```

**Parameters:**

- `DestinationObject` (data type `any`) designates the target object, the target place on the target object, or a sensor on the target object. It can also be an MU or a storage place on an MU.
- `WaitAtTarget` (optional, data type `boolean`) sets whether the robot waits at the target station (`true`) or not (`false`).
- If the robot is empty, send it to its default position with `setDestination(void)`.

**Examples:**

```
// set the target of the part
if @.target = SP3
   PickAndPlace.setDestination(@.target, false)
else
   PickAndPlace.setDestination(@.target, true)

end

print PickAndPlace.getDestination
// a target control with a sensor might, for example, look like this:
if not ?.Empty
   if @.PreviousLocation = Conveyor
       ?.setDestination(Station, false)
   else
       ?.setDestination(Conveyor.Sensors.id2, false)
   end
end
?.setDestination(MyStore[2,7])
MyPickAndPlace.setDestination(Conveyor.sensorID(1))
```

**See also:** `getDestination`, `TargetCtrl`, Target Control, Empty.

---

## setTimesTable [SimTalk]

Assigns a Times Table to the PickAndPlace robot (designated by `<Path>`).

**Type:** Method

**Syntax:**

```
<Path>.setTimesTable(TimesTable:table)
```

**Parameter:** `TimesTable` (data type `table`) designates the name of the table. You can enter these settings:

- The **Names** of all objects the robot is to serve, and the **Default Angle** to which the robot moves after depositing the part.
- The **Times above the diagonal** are the times during which the robot rotates empty. The **Times below the diagonal** are the times during which the robot rotates full (while a part is on it). The diagonal runs from the topmost cell in the "default angle" column to the bottommost cell in the last column.

In the example, cell A contains the rotation time from the Source to the Station with picked-up parts (0.5 seconds), cell B the rotation time from the Drain to the Source without parts, and cell C the rotation time from Drain1 to the Default Angle without parts.

When you insert Connectors or drag an object onto the robot, Plant Simulation enters the respective values into the Times Table. For the calculation, a quarter-rotation takes one second. You can change these times.

If you delete a Connector, Plant Simulation does not delete the entry of the now-unconnected object from the Times Table. Delete the entry in the Angles Table (right-click the row → Delete Row); clicking **Apply** in the robot's dialog also deletes the entry from the Times Table.

**Example:**

```
MyPickAndPlace.setTimesTable(myTimesTable)
```

**See also:** `getTimesTable`, Times Table, Angles Table, Default Angle, Empty.

---

# Read-Only Attributes of the PickAndPlaceRobot

The PickAndPlaceRobot provides:

- The read-only attributes listed in the table of contents.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of read-only attributes but cannot set them, as Plant Simulation computes the value at the point in time you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (e.g. Statistics).
