# Attributes of the LockoutZone

The LockoutZone provides:

- The attributes listed in the table of contents.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:
  ```simtalk
  MyLockoutZone.StopMode := "stop when service arrives"
  ```
- To get the value of an attribute, you might, for example, type:
  ```simtalk
  print MyLockoutZone.StopMode
  ```

---

## StatStoppedTime [SimTalk]

Returns the total time during which the LockoutZone designated by `<Path>` stopped the processing operations of the assigned stations.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoppedTime → time`
- **Watchable:** The read-only attribute is watchable.
- **Return Value:** The return value has the data type `time`.

**Example**

```simtalk
print MyLockoutZone.StatStoppedTime
```

**See also:** Tab Statistics [LockoutZone]

---

## Active [SimTalk] - LockoutZone

Activates the object designated by `<Path>` (true) or deactivates it (false).

- **Remarks:** It then creates and forwards failures for the assigned objects.
- **Type:** Attribute
- **Syntax:** `<Path>.Active:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example**

```simtalk
MyLockoutZone.Active := true
```

**See also:** Active [check box] - LockoutZone

---

## Objects [SimTalk] - LockoutZone

Sets the resource objects which you want to assign to the LockoutZone designated by `<Path>`.

- **Remarks:** The LockoutZone also returns these resources.
- **Type:** Attribute
- **Syntax:** `<Path>.Objects:array`
- **Assignment Value:** You can assign a value of data type `array` which contains the resources.

**Examples**

```simtalk
var a : object[] := [MyStation1, MyStation2]
LockoutZone.Objects := a
```

```simtalk
print MyLockoutZone.Objects 
// might, for example, return 
[*.Models.MyEnginePlant.Station1, *.Models.MyEnginePlant.Frame, 
*.Models.MyEnginePlant.Station2, *.Models.MyEnginePlant.Station3, 
*.Models.MyEnginePlant.ParallelStation]
```

**See also:** Tab Objects

---

## ResumeCtrl [SimTalk]

Designates a Method object of the object designated by `<Path>`.

- **Remarks:** Plant Simulation calls the Method when all failures of the objects assigned to the LockoutZone designated by `<Path>` were removed and the objects can thus continue processing parts.
- **Type:** Attribute
- **Syntax:** `<Path>.ResumeCtrl:method`
- **Assignment Value:** You can assign a value of data type `method`.

**Examples**

```simtalk
MyLockoutZone.ResumeCtrl := &myResumeCtrl
```

```simtalk
var row: integer := ReportStopping.ydim
ReportStopping["Last Failed Station",row] := @.name
ReportStopping["End Stopping",row] := eventcontroller.simTime
ReportStopping["Duration",row] := ReportStopping["End Stopping",row] - 
ReportStopping["Start Stopping",row]
```

**See also:** Resume Control [LockoutZone]

---

## StopCtrl [SimTalk]

Designates a Method object of the object designated by `<Path>`.

- **Remarks:** Plant Simulation calls the Method when one of the objects assigned to the LockoutZone designated by `<Path>` fails. The anonymous identifier `@` designates the triggering station, the anonymous identifier `?` designates the LockoutZone.
- **Type:** Attribute
- **Syntax:** `<Path>.StopCtrl:method`
- **Assignment Value:** You can assign a value of data type `method`.

**Examples**

```simtalk
MyLockoutZone.StopCtrl := &myStopCtrl
```

```simtalk
var row:integer := ReportStopping.ydim + 1
ReportStopping["First Failed Station",row] := @.name
ReportStopping["Start Stopping",row] := eventcontroller.simTime
```

**See also:** Stop Control [LockoutZone]

---

## StopMode [SimTalk]

Sets the Stop Mode of the LockoutZone designated by `<Path>`.

- **Remarks:** The LockoutZone does not affect the Recovery Time and the Cycle Time of the stations which it controls. The LockoutZone stops these objects and records statistics values for the state stopped. If you deactivate the LockoutZone while it is in the process of stopping other stations, Plant Simulation immediately releases all objects stopped by the LockoutZone. When you reset your model, all objects change their state from stopped to operational.
- **Type:** Attribute
- **Syntax:** `<Path>.StopMode`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type `string`.

You can specify:

- **"Stop immediately"** — immediately stops the processing operations of all other objects within the LockoutZone as soon as one of the objects assigned to the LockoutZone fails. The objects do not fail! Within this period of time additional failures can take place for the assigned stations, several failures of differing objects can thus overlap. The stations only start processing parts again after all failures were removed. They only use up the remaining processing time.
- **"Stop when Service arrives"** — only stops the objects assigned to the LockoutZone when the services, which the failed station requested, are assigned. Depending on your modeling situation this can be at a different point in time. If you modeled Footpaths on which the Worker walks to the station, Plant Simulation considers the Worker as received once he has reached the station. For Exporters/Workers who can be beamed, the service is considered to be received once the Broker has assigned the service. This matches the behavior of the Receive Control.

**Example**

```simtalk
MyLockoutZone.StopMode := "Stop when Service arrives"
```

**See also:** Stop Mode [drop-down list], Stopped [state, material flow objects]

---

## Stopped [SimTalk] - LockoutZone

Sets if the LockoutZone designated by `<Path>` is stopped (true) or if it is not stopped (false).

- **Remarks:** Stopped means that all of the processing operations of the objects, which the LockoutZone controls, come to a halt.
- **Syntax:** `<Path>.Stopped`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example**

```simtalk
MyLockoutZone.Stopped := true
```
