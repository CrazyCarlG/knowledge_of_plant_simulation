# Attributes of the PickAndPlace Robot

The PickAndPlace robot provides:
- The attributes listed below.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods** (context menu of the Class Library, or press F8 on the Frame into which an instance was inserted).

You can set and get attribute values via dialog windows or by assigning values in SimTalk:
- Set: `MyPickAndPlace.Capacity := 12`
- Get: `print MyPickAndPlace.TimeFactor` / `posit := MyStation.Cont.XPos`

---

## StatRotationLoadedTime [SimTalk] — PickAndPlace

Returns the total time during which the PickAndPlace robot designated by `<Path>` was rotating while transporting a part.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatRotationLoadedTime → time`
- **Return Value:** data type `time`

**Example:**
```simtalk
print MyPickAndPlace.StatRotationLoadedTime
```

**See also:** Statistics report, Rotation Time

---

## BlockingAngle [SimTalk]

Sets the Blocking Angle of the PickAndPlace robot designated by `<Path>`.

- The Blocking Angle is the angle in degrees which the PickAndPlace robot cannot cross. It prevents the robot from taking the shortest way.
- The Blocking Angle only affects the animation; the simulation is controlled by the rotation times defined in the Times Table.

- **Type:** Attribute
- **Syntax:** `<Path>.BlockingAngle:real`
- **Assignment Value:** data type `real`, angle between 0 and 360 degrees. Default `-1` means no blocking angle applies (robot takes the shortest way).

**Example:**
```simtalk
MyPickAndPlace.BlockingAngle := 5
```

**See also:** Blocking Angle [text box], Times Table [PickAndPlace]

---

## Capacity [SimTalk] — PickAndPlace

Sets the Capacity of the PickAndPlace robot designated by `<Path>`.

- The Capacity is the number of MUs that the PickAndPlace robot can transport at any one time.
- Enables transporting more than one part at a time (e.g., pick up several bottles and place them into slots one at a time — FIFO). For other rules (e.g., LIFO), program an Exit Control.

- **Type:** Attribute
- **Syntax:** `<Path>.Capacity:integer`
- **Watchable:** yes
- **Assignment Value:** data type `integer`, value greater than 1.

**Example:**
```simtalk
MyPickAndPlace.Capacity := 12
```

**See also:** Capacity [text box] — PickAndPlace

---

## DefaultAngle [SimTalk] — PickAndPlace

Sets the Default Angle of the PickAndPlace robot designated by `<Path>`.

- The Default Angle is the rotation angle in degrees to which the side of the end point rotates when `GoToDefaultPosition` is `true`. Add 180° to rotate to the side where the start point is located.
- Also used as the start position after a Reset, regardless of whether Go to Default Position is activated.

- **Type:** Attribute
- **Syntax:** `<Path>.DefaultAngle:real`
- **Assignment Value:** data type `real`, value between 0° and 360°.

**Example:**
```simtalk
MyPickAndPlace.DefaultAngle := 5
```

**See also:** GoToDefaultPosition [SimTalk]

---

## GoToDefaultPosition [SimTalk] — PickAndPlace

Rotates the PickAndPlace robot designated by `<Path>` back to its default position when it has deposited the part (`true`) or not (`false`).

- When `true`, the robot uses `DefaultAngle` when the model is reset. `DefaultAngle` sets the actual Default Angle.

- **Type:** Attribute
- **Syntax:** `<Path>.GoToDefaultPosition:boolean`
- **Assignment Value:** data type `boolean`.

**Example:**
```simtalk
MyPickAndPlace.GoToDefaultPosition := true
```

**See also:** Go to Default Position [check box], Default Angle [PickAndPlace]

---

## LoadingTime [SimTalk] — PickAndPlace

Sets the Loading Time which the PickAndPlace robot designated by `<Path>` uses for picking up a part at a station. If the robot is full, it rotates to the target station and places the part there.

- **Point-oriented delivering station:** the part is booked on the robot while it picks it up; the station is locked until loading time elapses.
- **Length-oriented delivering station:** the part remains on the station during loading time and is then moved onto the robot.

**Notes:**
- Interruptions of the PickAndPlace robot extend the loading time; the delivering station remains locked during the interruption.
- Interruptions of the delivering station do not affect loading; loading continues.
- The entrance is open while Loading Time runs, closes once the part is moved on, and reopens after Unloading Time has passed.

- **Type:** Attribute
- **Syntax:** `<Path>.LoadingTime:time`
- **Assignment Value:** data type `time`.

**Examples:**
```simtalk
MyPickAndPlaceRobot.LoadingTime := 1:00
MyPickAndPlaceRobot.LoadingTime.setTypeAndAttr("Normal",30,10)
```

**See also:** Loading Time [PickAndPlace], LoadingTime.Type [SimTalk], IsLoading [SimTalk]

---

## MUConveyingDirection [SimTalk]

Sets the conveying direction of the MU on the PickAndPlace robot designated by `<Path>`.

- For **Retain, Rotate by 90° to the right, Rotate by 90° to the left, Rotate by 180°** the robot executes a relative rotation depending on the direction from which the MU arrives.
- For **Forwards, Lateral right, Backwards, Lateral left** the rotation is absolute, independent of the direction from which the MU arrives.

| Conveying direction | Description |
|---|---|
| Retain | Continue conveying in the same direction the part arrives. |
| Rotate 90° to the right | Rotate 90° right and place on successor. |
| Rotate 90° to the left | Rotate 90° left and place on successor. |
| Rotate 180° | Rotate 180° and place on successor. |
| Forwards | Rotate so it rests forward on the successor. |
| Lateral right | Rotate so it rests laterally to the right. |
| Backwards | Rotate so it rests backward. |
| Lateral left | Rotate so it rests laterally to the left. |

- **Type:** Attribute
- **Syntax:** `<Path>.MUConveyingDirection:string`
- **Assignment Value:** data type `string`; one of `"Retain"`, `"Rotate 90° to the right"`, `"Rotate 90° to the left"`, `"Rotate 180°"`, `"Forwards"`, `"Lateral right"`, `"Backwards"`, `"Lateral left"`.

**Example:**
```simtalk
MyPickAndPlace.MUConveyingDirection := "Forwards"
```

**See also:** MU Conveying Direction [drop-down list]

---

## OnlyForEmptyBlockingList [SimTalk]

Only rotates the PickAndPlace robot designated by `<Path>` back to its default position when its blocking list is empty (`true`), i.e., when no additional requests are registered, or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.OnlyForEmptyBlockingList:boolean`
- **Assignment Value:** data type `boolean`.

**Example:**
```simtalk
MyPickAndPlace.OnlyForEmptyBlockingList := true
```

**See also:** Go to Default Position [check box]

---

## PullCtrl [SimTalk] — PickAndPlace

Designates a Method object of the object designated by `<Path>`.

- Plant Simulation calls the Pull Control whenever the robot is ready to pick up a new part or a new MU is waiting at its entrance.
- If `TargetSelection` is `"Load part onto MU at sensor"`, the robot only counts as ready if a Container/Transporter is waiting at the sensor (also applies to a programmed Pull Control).
- In the Pull Control, determine which parts the robot accepts via `fwBlockList` and `unblock`.

- **Type:** Attribute
- **Syntax:** `<Path>.PullCtrl:method`
- **Assignment Value:** data type `method`.

**Example:**
```simtalk
MyPickAndPlace.PullCtrl := &myPullControl
```

**See also:** Pull Control [PickAndPlace]

---

## TargetCtrl [SimTalk] — PickAndPlace

Designates a Method object of the object designated by `<Path>`.

- Runs as soon as the robot has completely picked up the part; determines the successor onto which the robot deposits the part. Set the target with `setDestination`.
- Also called after the robot has deposited the part (in which case the active element `@` is void); set the next pickup object with `setDestination`.
- Only called while unloading if **Go to Default Position** is cleared.

- **Type:** Attribute
- **Syntax:** `<Path>.TargetCtrl:method`
- **Assignment Value:** data type `method`.

**Example:**
```simtalk
if ?.empty
   return
end
if @.LastStation = Source
   ?.setDestination(Drain)
elseif @.LastStation = Source1
   ?.setDestination(Station, true)
else
   ?.setDestination(Drain1)
end
```
```simtalk
MyPickAndPlace.TargetCtrl := &myTargetControl
```

**See also:** setDestination [SimTalk], Target Control [PickAndPlace]

---

## TargetObject [SimTalk]

Designates the length-oriented Target Object at which the PickAndPlace robot designated by `<Path>` places or loads the part.

- **Type:** Attribute
- **Syntax:** `<Path>.TargetObject:path`
- **Assignment Value:** data type `path`.

**Example:**
```simtalk
MyPickAndPlace.TargetObject := .Models.MyModel.Conveyor
```

**See also:** Target Object

---

## TargetSelection [SimTalk]

Sets how the PickAndPlace robot designated by `<Path>` selects the target for the part to be moved.

- **Type:** Attribute
- **Syntax:** `<Path>.TargetSelection:string`
- **Assignment Value:** data type `string`. Possible values:
  - `"Exit strategy or target control"` — default behavior of previous versions; target set by Exit Strategy or Target Control.
  - `"Load part onto MU at sensor"` — requires a manually created front-triggered sensor with light-barrier mode on the length-oriented target object, plus Target Object and Target sensor ID. Stopping/loading/sending the Container/Transporter works automatically only if no control is entered; otherwise program it in the control. The robot only picks the part when a Container/Transporter is waiting at the sensor.
  - `"Place part at sensor"` — requires a manually created rear-triggered sensor with light-barrier mode on the length-oriented target object, plus Target Object and Target Sensor ID.

**Example:**
```simtalk
MyPickAndPlace.TargetSelection := "Load part onto MU at sensor"
```

**See also:** Target Control [PickAndPlace], Target Object, Target Sensor ID [text box]

---

## TargetSensorID [SimTalk]

Sets the sensor ID of the target object at which the PickAndPlace robot designated by `<Path>` places or loads the part.

- Plant Simulation does not create the sensor automatically; create it manually or with `createSensor`.

- **Type:** Attribute
- **Syntax:** `<Path>.TargetSensorID:integer`
- **Assignment Value:** data type `integer`.

**Example:**
```simtalk
MyPickAndPlace.TargetSensorID := 2
```

**See also:** createSensor [SimTalk], Target Sensor ID [text box]

---

## TimeFactor [SimTalk]

Sets the Time Factor with which all times in the Times Table of the PickAndPlace robot designated by `<Path>` are multiplied.

- Enables simulating the robot with different speeds without manually changing table times.

- **Type:** Attribute
- **Syntax:** `<Path>.TimeFactor:real`
- **Assignment Value:** data type `real`.

**Example:**
```simtalk
MyPickAndPlace.TimeFactor := 5
```

**See also:** Time Factor [PickAndPlace], Times Table [PickAndPlace]

---

## UnloadingTime [SimTalk] — PickAndPlace

Sets the Unloading Time of the PickAndPlace robot designated by `<Path>` for placing the picked-up part onto the target station.

- **Point-oriented target station:** the part is booked on the robot while it places it; the station is locked until unloading time elapses.
- **Length-oriented target station:** the part is moved onto the length-oriented object before the unloading time starts.

**Notes:**
- Interruptions of the PickAndPlace robot extend the unloading time; the target station remains locked.
- Interruptions of the target station do not affect unloading; unloading continues.
- The entrance is open while Loading Time runs, closes once the part is moved on, and reopens after Unloading Time has passed.

- **Type:** Attribute
- **Syntax:** `<Path>.UnloadingTime:time`
- **Assignment Value:** data type `time`.

**Examples:**
```simtalk
MyPickAndPlaceRobot.UnloadingTime := 1:00
MyPickAndPlaceRobot.UnloadingTime.setTypeAndAttr("Normal",30,10)
```

**See also:** Unloading Time [PickAndPlace], UnloadingTime.Type [SimTalk], IsLoading [SimTalk]

---

## UseKinematicsForTimes [SimTalk]

Sets if the PickAndPlace robot designated by `<Path>` uses 3D kinematics to determine its timing (`true`) instead of the times defined in the Angles Table and Times Table (`false`).

- The robot can only use 3D kinematics if supported robot kinematics are found (as described under Configuring the Robot).
- 3D kinematics can come from an imported robot graphic or be defined in Plant Simulation.
- Supported kinematics include those used by `_3D.Poses.moveToCoordinate`, `_3D.Poses.moveToMU`, and `_3D.Poses.moveToMUAnimationPosition`, except linear robots.
- Define Joint Settings of an Animatable Object on the **Joint** tab.

- **Type:** Attribute
- **Syntax:** `<Path>.UseKinematicsForTimes:boolean`
- **Assignment Value:** data type `boolean`.

**Example:**
```simtalk
MyPickAndPlace.UseKinematicsForTimes := true
```

**See also:** Use Kinematics for Times, Configuring the Robot, Joint, JointVelocity [SimTalk], Times Table [PickAndPlace]

---

## WaitForFreeTarget [SimTalk] — PickAndPlace

Sets if the PickAndPlace robot designated by `<Path>` only rotates to a part that wants to exit the predecessor to pick it up if the destination object is ready to accept it (`true`) or not (`false`).

- Specify `false` to make the robot rotate to the part immediately.
- Only evaluated for the setting **Target Selection > Exit strategy or target control**.
- Parts that cannot be transported are entered into the Exit Blocking List of the target object.
- When `true`, Plant Simulation already evaluates the Exit Strategy or Target Control before the robot rotates to pick up the part, and enters the determined target into `TargetObject`.

- **Type:** Attribute
- **Syntax:** `<Path>.WaitForFreeTarget:boolean`
- **Assignment Value:** data type `boolean`.

**Example:**
```simtalk
MyPickAndPlace.WaitForFreeTarget := true
```

**See also:** ReservedFor [SimTalk], ReservedPlace [SimTalk], contentsAndReservedList [SimTalk], TargetSelection [SimTalk], Wait for Free Target [PickAndPlace]

---

> **Note:** The source file ends with an unrelated section describing the **Store** object (a warehouse object whose MUs remain until removed, with X/Y/Z dimensions, Entrance Control determining storage place, and no Set-up or Processing Time). It is reproduced here for completeness but is not an attribute of the PickAndPlace robot.
