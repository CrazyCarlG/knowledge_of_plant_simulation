# Robot Arms, Joints & Poses (SimTalk)

SimTalk reference for robot arm animations, joint access, and poses in 3D.

---

## Accessing Robot Arm Animations

SimTalk provides methods for robot arm animations in 3D. You can buffer all animations of a type in a value of data type `any`:

```simtalk
var a : any := .PickAndPlace._3D.RobotArmAnimations
```

### `_3D.RobotArmAnimations.getTable` [SimTalk]

Returns the existing Robot Arm Animations data of the object designated by `<Path>` and writes it into the passed table.

- **Type:** Method
- **Remarks:** Plant Simulation automatically formats the passed table.

**Syntax**

```simtalk
<Path>._3D.RobotArmAnimations.getTable(Animations:table)
```

**Parameter**

The parameter `Animations` of data type `table` designates the table which contains the robot animations. The table has three columns:

- **From** (`string`) — indicates at which object a robot arm animation starts. Designates the default orientation as starting point if the cell is empty.
- **To** (`string`) — indicates to which object a robot arm animation moves. Designates the default orientation as the destination if the cell is empty.
- **Table** (`table`) — indicates the robot arm animation path. It is a subtable with three columns of data type `length` for the X, Y, and Z values of all coordinates the robot passes on its route from the `From` position to the `To` position within the robot's coordinate system.

**Example**

```simtalk
var t : table
PickAndPlace1._3D.RobotArmAnimations.getTable(t)
PickAndPlace2._3D.RobotArmAnimations.setTable(t)
```

### `_3D.RobotArmAnimations.setTable` [SimTalk]

Sets the table that contains the Robot Arm Animations of the object designated by `<Path>`.

- **Type:** Method

**Syntax**

```simtalk
<Path>._3D.RobotArmAnimations.setTable(Animations:table)
```

**Parameter**

The parameter `Animations` of data type `table` designates the table which contains the robot animations. The table has three columns:

- **From** (`string`) — indicates at which object a robot arm animation starts. Designates the default orientation as the starting point if the cell is empty.
- **To** (`string`) — indicates to which object a robot arm animation moves. Designates the default orientation as the destination if the cell is empty.
- **Table** (`table`) — indicates the robot arm animation path. It is a subtable with three columns of data type `length` for the X, Y, and Z values of all coordinates the robot passes on its route from the `From` position to the `To` position within the robot's coordinate system.

**Example**

```simtalk
var t : table
PickAndPlace1._3D.RobotArmAnimations.getTable(t)
PickAndPlace2._3D.RobotArmAnimations.setTable(t)
```

---

## Accessing Joints

SimTalk provides functions for accessing joints (see also: Joint, Poses).

### `_3D.JointUseShortestRotationDirection` [SimTalk]

Sets if the rotational joint of the object designated by `<Path>` uses the spatially shortest direction toward its target orientations (`true`) or not (`false`).

- **Type:** Attribute
- **Remarks:** If the joint uses the spatially shortest direction, you cannot specify joint limits.

**Syntax**

```simtalk
<Path>._3D.JointUseShortestRotationDirection:boolean
```

**Assignment Value:** A value of data type `boolean`.

**Example**

```simtalk
MyCrane._3D.getObject(1).JointUseShortestRotationDirection := true
```

### `JointAcceleration` [SimTalk]

Sets the acceleration of the joint of the object designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```simtalk
<Path>.JointAcceleration:acceleration
```

**Assignment Value**

- **Prismatic Joint** — acceleration in meters per second squared (data type `acceleration`).
- **Revolute Joint** — acceleration in degrees per second squared (data type `real`).

**Example**

```simtalk
MyStation._3D.getObject(1).JointAcceleration := 0.3
```

### `JointCurrentValue` [SimTalk]

Returns the current joint value of the object designated by `<Path>`.

- **Type:** Read-only attribute

**Syntax**

```simtalk
<Path>.JointCurrentValue -> length
```

**Return Value**

- **Prismatic Joint** — meters (data type `length`).
- **Revolute Joint** — degrees (data type `real`).

**Example**

```simtalk
print MyStation._3D.getObject(1).JointCurrentValue
```

### `JointDeceleration` [SimTalk]

Sets the deceleration of the joint of the object designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```simtalk
<Path>.JointDeceleration:acceleration
```

**Assignment Value**

- **Prismatic Joint** — acceleration in meters per second squared (data type `acceleration`).
- **Revolute Joint** — acceleration in degrees per second squared (data type `real`).

**Example**

```simtalk
MyStation._3D.getObject(1).JointDeceleration := 0.3
```

### `JointLowerLimit` [SimTalk]

Sets the lower limit of the joint of the object designated by `<Path>`.

- **Type:** Attribute
- **Remarks:** Plant Simulation exclusively uses limits while defining poses. It does not use them to influence any other behavior, such as `_3D.Poses.moveToCoordinate`, `_3D.Poses.moveToMU`, etc.

**Syntax**

```simtalk
<Path>.JointLowerLimit:length
```

**Assignment Value**

- **Translation** — meters (data type `length`).
- **Rotation** — degrees (data type `real`). `_3D.getObject` enables you to access animatable objects.

**Example**

```simtalk
MyStation._3D.getObject(1).JointLowerLimit := 43
```

### `JointLowerLimitActive` [SimTalk]

Sets if the lower limit of the joint of the object designated by `<Path>` is active (`true`) or not (`false`).

- **Type:** Attribute
- **Remarks:** `_3D.getObject` enables you to access animatable objects.

**Syntax**

```simtalk
<Path>.JointLowerLimitActive:boolean
```

**Assignment Value**

A value of data type `boolean`. Specify `true` to activate the limit if it has not been activated before. It will be activated with the other active limit if the other limit (upper/lower) has a value. It will be activated with `0` if no value was assigned.

**Examples**

```simtalk
MyStation._3D.getObject(1).JointLowerLimitActive

// Let's suppose: The value of the lower limit is 3
(_3D.getObject(1).JointLowerLimit = 3)
// the lower limit is activated
(_3D.getObject(1).JointLowerLimitActive = true)
// the lower limit is not activated
(_3D.getObject(1).JointUpperLimitActive = false)
_3D.getObject(1).JointUpperLimitActive := true
// activates the upper limit and sets it to 3

// Let's suppose: The lower limit is not activated
(_3D.getObject(1).JointLowerLimitActive = false)
// the upper limit is activate
(_3D.getObject(1).JointUpperLimitActive = false)
_3D.getObject(1).JointLowerLimitActive := true
// activates the upper limit and sets it to 0
```

### `JointType` [SimTalk]

Sets the type of joint of the object designated by `<Path>`.

- **Type:** Attribute
- **Remarks:** `_3D.getObject` enables you to access animatable objects.

**Syntax**

```simtalk
<Path>.JointType:string
```

**Assignment Value**

A value of data type `string`. You can specify `"Prismatic joint"` or `"Revolute joint"`.

**Example**

```simtalk
MyStation._3D.getObject(1).JointType := "Revolute joint"
```

### `JointUpperLimit` [SimTalk]

Sets the upper limit of the joint of the object designated by `<Path>`.

- **Type:** Attribute
- **Remarks:** Plant Simulation exclusively uses limits while defining poses. It does not use them to influence any other behavior, such as `_3D.Poses.moveToCoordinate`, `_3D.Poses.moveToMU`, etc.

**Syntax**

```simtalk
<Path>.JointUpperLimit:length
```

**Assignment Value**

- **Translation** — meters (data type `length`).
- **Rotation** — degrees (data type `real`). `_3D.getObject` enables you to access animatable objects.

**Example**

```simtalk
MyStation._3D.getObject(1).JointUpperLimit := 25
```

### `JointUpperLimitActive` [SimTalk]

Sets if the upper limit of the joint of the object designated by `<Path>` is active (`true`) or not (`false`).

- **Type:** Attribute
- **Remarks:** `_3D.getObject` enables you to access animatable objects.

**Syntax**

```simtalk
<Path>.JointUpperLimitActive:boolean
```

**Assignment Value:** A value of data type `boolean`.

**Example**

```simtalk
MyStation._3D.getObject(1).JointUpperLimitActive := true
```

### `JointVelocity` [SimTalk]

Sets the speed of the joint of the object designated by `<Path>`.

- **Type:** Attribute
- **Remarks:**
  - An animatable object with the `Velocity` of `0` does not rotate with the Turntable when the Turntable rotates. This applies when the insertion position of the animatable object is located on the animation rotation axis of the Turntable — i.e., the insertion point is exactly located on the animation rotation center or is reachable from there along the animation rotation axis without a sideways deviation. This behavior resembles a real Turntable with a fixed base and a rotating table.
  - `_3D.getObject` enables you to access animatable objects.

**Syntax**

```simtalk
<Path>.JointVelocity:speed
```

**Assignment Value**

- **Prismatic Joint** — velocity in meters per second (data type `speed`).
- **Revolute Joint** — angular velocity in degrees per second (data type `real`).

**Example**

```simtalk
MyStation._3D.getObject(1).JointVelocity := 25
```

### `moveTo` [SimTalk]

Moves to one or several positions or rotations of the joint of the object designated by `<Path>`.

- **Type:** Method
- **Remarks:** A `moveTo` call of an animatable object aborts a previous `moveTo` run of the same animatable object. For active movements to poses or movements started by `_3D.Poses.moveToCoordinate`, a conflict arises if this animatable object is part of the other active movement.
- **Note:** Whenever you change Limits, Velocity, Acceleration, or the Joint Type of the animatable object, the initial position for the next pose run that affects this object returns to `0`.
- **Note:** Plant Simulation does not use joint limits in this method — you can move to a position beyond the limits you specified.

**Syntax**

```simtalk
<Path>.moveTo(PositionOrRotationAngle:real[, TimeSpan:time]) → time
<Path>.moveTo(PositionsOrRotationAngles:array[real][, TimeSpan:time]) → time
<Path>.moveTo(PositionsOrRotationAngles:array[real][, TimeSpans:array[time]]) → time
```

**Parameters**

- `PositionOrRotationAngle` (`real`) — sets the position or rotation angle of the joint toward which the object moves.
- `PositionsOrRotationAngles` (`array[real]`) — sets a sequence of positions or rotation angles approached sequentially one after the other. The movement stays active until the last position or rotation is reached.
- `TimeSpan` (`time`, optional) — sets the duration of the movement.
- `TimeSpans` (`array[time]`, optional) — sets the durations of the movement.

Do not specify the parameter to run the pose movement with the time resulting from the speeds of the joint definitions. If specified:

- A single time means the entire movement takes place within the specified time.
- A sequence of times means the first position/rotation is reached within the first time span, the second in the second, etc. You must specify as many time spans as positions/rotations. You can only specify an array of times if you also specified an array of positions/rotations.

> `Station._3D.getObject(1).moveTo(3, [7.5])` results in an error, although the same number of positions is specified as time spans. `Station._3D.getObject(1).moveTo([3], [7.5])` does not result in an error, but is unnecessarily complicated — `Station._3D.getObject(1).moveTo(3, 7.5)` yields the same result.

**Return Value**

Data type `time` — the time span of simulation time the designated pose movement will probably take, provided it will not be interrupted.

**Example**

```simtalk
Station._3D.getObject(1).moveTo(3, -1)
Station._3D.getObject(1).moveTo([3, -1], 7.5)
Station._3D.getObject(1).moveTo(3, 7.5)
```

### `moveToCoordinate` [SimTalk]

Moves the joint designated by `<Path>` to the specified coordinate.

- **Type:** Method
- **Remarks:** When moving a joint to a coordinate, Plant Simulation computes the target joint state based upon a relaxed state at which the origin of the joint is located at position `[0,0,0]`. The joint points toward the direction specified in `_3D.AniTranslationDirection` in its reset coordinate system.
- **Note:** Plant Simulation does not use joint limits in this method — you can move to a position beyond the limits you specified.

**Syntax**

```simtalk
<Path>.moveToCoordinate(Coordinate:length[3][, TimeSpan:time]) -> time
```

**Parameters**

- `Coordinate` (`length[3]`) — the coordinate to which the joint is to move in the joint's coordinate system.
  - **Note:** The joint's coordinate system includes its animation state. If you first compute the coordinate, then move the joint, and then call `moveToCoordinate`, you end up at a different coordinate than intended.
- `TimeSpan` (`time`, optional) — sets the duration of the movement. If omitted, the movement runs with the time resulting from the speed from the joint definition.

**Return Value**

Data type `time` — the time span the designated movement will probably take, provided it will not be interrupted.

**Example**

```simtalk
var destObj = ?.succ
var arm = self.~._3D.getObject("Arm")
var destPos = destObj._3D.getMUAnimationPosition
destPos.z += @.MUHeight
wait arm.moveToCoordinate(arm.getPositionOfObject(destObj, destPos))
```

### `moveToMU` [SimTalk]

Moves the joint designated by `<Path>` to the specified MU instance.

- **Type:** Method
- **Remarks:** When moving a joint to an MU instance, Plant Simulation computes the target joint state based upon a relaxed state at which the origin of the joint is located at `[0,0,0]`. The joint points toward the direction specified in `_3D.AniTranslationDirection`.
- **Note:** Plant Simulation does not use joint limits in this method.

**Syntax**

```simtalk
<Path>.moveToMU(MU:object[, TimeSpan:time]) -> time
```

**Parameters**

- `MU` (`object`) — the MU instance to which the joint moves.
- `TimeSpan` (`time`, optional) — duration of the movement. If omitted, the movement runs with the time resulting from the speed from the joint definition.

**Return Value**

Data type `time` — the time span the designated movement will probably take, provided it will not be interrupted.

**Example**

```simtalk
var mu = otherObject.cont
var arm = self.~._3D.getObject("Arm")
wait arm.moveToMU(mu)
```

### `moveToMUAnimationPosition` [SimTalk]

Moves the joint designated by `<Path>` to the position and rotation in space where the specified MU instance would be located when being moved to the specified place.

- **Type:** Method
- **Remarks:**
  - When moving a joint to an MU instance, Plant Simulation computes the target joint state based upon a relaxed state at which the origin of the joint is located at `[0,0,0]`.
  - If the destination is length-oriented, `moveToMUAnimationPosition` of animatable objects computes a movement that deposits the front of the MU at the destination instead of the booking point. For place-oriented objects nothing changes.
- **Note:** Plant Simulation does not use joint limits in this method.

**Syntax**

```simtalk
<Path>.moveToMUAnimationPosition(MU:object, TargetPE:object/PE[, RelPos/AbsPos:real/length, TimeSpan:time]) -> time
```

**Parameters**

- `MU` (`object`) — the MU instance to measure when moving to the target place.
- `TargetPE` (`object`) — the place to which the item is to move. Can be a specific PE (production element) or an object if the object only has one PE.
- `RelPos/AbsPos` (`real`/`length`, optional) — if `real`, the relative position on the object between `0` and `1` (`0` = start, `1` = end/100%). If `length`, the absolute position as distance from the beginning of the object. Only used if `TargetPE` specifies a length-oriented place (e.g., a Conveyor or a Transporter with a length-oriented loadbay). Defaults to `0.0` if omitted.
- `TimeSpan` (`time`, optional) — duration of the movement. If omitted, the movement runs with the time resulting from the speed from the joint definition.

**Return Value**

Data type `time` — the time span the designated movement will probably take, provided it will not be interrupted.

**Example**

```simtalk
var mu = otherObject.cont
var arm = self.~._3D.getObject("Arm")
wait arm.moveToMUAnimationPosition(mu)
```

---

## Accessing Poses

SimTalk provides attributes and methods for poses for objects you can insert into a Frame, and for MUs.

**Remarks:** In general a pose designates a combination of position and orientation of an object. In this context a pose designates a number of translation or rotation positions for animatable objects that belong to a simulation object. This also takes the degrees of freedom into account which you set in the joint definitions of these animatable objects.

A **pose run** designates all movements that were started by any version of the methods `_3D.Poses.moveTo` and `_3D.Poses.moveToCoordinate`, both for the object itself and for any of its animatable objects.

### `_3D.MovementInterruptible` [SimTalk]

Sets if failures and pauses will interrupt pose runs of the object designated by `<Path>` (`true`) or not (`false`).

- **Type:** Attribute
- **Remarks:**
  - If you start a pose run while a failure or pause is active, the pose run will start regardless of the `MovementInterruptible` setting.
  - Applies to the objects `FluidSource`, `FluidDrain`, `Tank`, `Mixer`, `Transporter`, `Frame`, `Exporter`, and `Worker`. Also applies to all objects which can transport MUs or Workers, except the `Workplace`.

**Syntax**

```simtalk
<Path>._3D.MovementInterruptible:boolean
```

**Assignment Value:** A value of data type `boolean`.

**Example**

```simtalk
Station._3D.MovementInterruptible := true
```

### `_3D.Poses.cancelMovement` [SimTalk]

Cancels the movement toward the designated pose of the object designated by `<Path>`.

- **Type:** Method
- **Remarks:** If you do not specify the optional parameter, all movements will be canceled. Affects the designated pose, always together with the other poses to which the object moved together with this pose in a common call of `_3D.Poses.moveTo`.

**Syntax**

```simtalk
<Path>._3D.Poses.cancelMovement([Pose:string])
```

**Parameter:** `Pose` (`string`, optional) — the name of the pose toward which the object moves.

**Example**

```simtalk
Station._3D.Poses.moveTo(["Pose1", "Pose2"])
Station._3D.Poses.cancelMovement("Pose1")
// instead, you can also enter:
Station._3D.Poses.cancelMovement("Pose2")
```

### `_3D.Poses.continueMovement` [SimTalk]

Continues the movement toward the designated pose of the object designated by `<Path>`.

- **Type:** Method
- **Remarks:** If you do not specify the optional parameter, all paused movements will be continued. Affects the designated pose together with the other poses from a common `_3D.Poses.moveTo` call.

**Syntax**

```simtalk
<Path>._3D.Poses.continueMovement([Pose:string])
```

**Parameter:** `Pose` (`string`, optional) — the name of the pose which the object moves. If omitted, all paused movements will be continued.

**Example**

```simtalk
Station._3D.Poses.moveTo(["Pose1", "Pose2"])
Station._3D.Poses.continueMovement("Pose1")
// instead, you can also enter:
Station._3D.Poses.continueMovement("Pose2")
```

### `_3D.Poses.EndPoseWasReached` [SimTalk]

Returns if all pose runs for the object designated by `<Path>` came to an end (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Remarks:** It does not matter if the pose runs came to a regular end or if they were canceled with `_3D.Poses.cancelMovement` or `_3D.Poses.stopMovement`. Pose runs that are only paused by `_3D.Poses.pauseMovement` or by failures or pauses will **not** set `EndPoseWasReached` to `true`.
- **Watchable:** Yes.

**Syntax**

```simtalk
<Path>._3D.Poses.EndPoseWasReached → boolean
```

**Return Value:** Data type `boolean`.

**Example**

```simtalk
Station._3D.Poses.moveTo("Pose1")
waituntil Station._3D.Poses.EndPoseWasReached
```

### `_3D.Poses.getAnimationTime` [SimTalk]

Returns how long the movement toward the designated pose of the object designated by `<Path>` takes.

- **Type:** Method
- **Remarks:** If you do not specify the optional parameter, returns the simulation time which remains until all pose movements and movements caused by `_3D.Poses.moveToCoordinate` or `moveTo` are processed, provided `_3D.Poses.pauseMovement` does not cause a delay.

**Syntax**

```simtalk
<Path>._3D.Poses.getAnimationTime([Pose:string])
```

**Parameter:** `Pose` (`string`, optional) — the name of the pose toward which the object moves.

**Example**

```simtalk
print Station._3D.Poses.getAnimationTime
print Station._3D.Poses.getAnimationTime("Pose1")
```

### `_3D.Poses.getMUAnimationPosition` [SimTalk]

Returns the position which the MU would take on the specified PE (production element). This is the same position which would be approached with `_3D.Poses.moveToMUAnimationPosition`.

**Syntax**

```simtalk
<Path>(MU:object, TargetPE:any[, RelPos/AbsPos:real/length]) -> real[3]
```

**Parameters**

- `MU` (`object`) — the MU instance to be measured when moving to the target place.
- `TargetPE` (`any`) — the place to which the item is to move (a specific PE, or an object if the object only has one PE).
- `RelPos/AbsPos` (`real`/`length`, optional) — if `real`, the relative position between `0` and `1`. If `length`, the absolute position as distance from the beginning. Only used for length-oriented places (e.g., Conveyor or Transporter with a length-oriented load bay). Defaults to `0.0` if omitted.

**Return Value**

An array with three values of data type `real` — the X-, Y-, and Z-position of the MU on the PE.

**Example**

```simtalk
var dropPos = Robot._3D.Poses.getMUAnimationPosition(@, ParallelStation[1,2])
```

### `_3D.Poses.getTable` [SimTalk]

Returns the poses of the object designated by `<Path>` and writes them into the specified table.

- **Type:** Method

**Syntax**

```simtalk
<Path>._3D.Poses.getTable(Poses:table)
```

**Parameter:** `Poses` (`table`) — the table in which the pose data is written.

**Example**

```simtalk
var t : table
MyStation._3D.Poses.getTable(t)
MyStation._3D.Poses.setTable(t)
```

### `_3D.Poses.isMovingTo` [SimTalk]

Returns if the object designated by `<Path>` moves toward the designated pose.

- **Type:** Method
- **Remarks:** Affects the designated pose together with the other poses from a common `_3D.Poses.moveTo` call.

**Syntax**

```simtalk
<Path>._3D.Poses.isMovingTo(Pose:string) → boolean
```

**Parameter:** `Pose` (`string`) — the name of the pose toward which the object moves.

**Return Value**

Data type `boolean`: `true` if the object moves toward the pose, `false` otherwise. If the pose name is empty or does not match any existing pose, the method returns an error.

**Example**

```simtalk
print Station._3D.Poses.isMovingTo("Pose1")
```

### `_3D.Poses.moveTo` [SimTalk]

Moves to one or several poses of the object designated by `<Path>`.

- **Type:** Method
- **Remarks:**
  - Whenever you change the Lower Limit/Upper Limit, Velocity, Acceleration, or Joint Type of an animatable object, the initial position for the next pose run that affects this object returns to `0`.
  - When all pose runs of an object reach their destination, Plant Simulation enters an `EndOfTime` event into the Event List.

**Syntax**

```simtalk
<Path>._3D.Poses.moveTo(Pose:string[, TimeSpan:time]) → time
<Path>._3D.Poses.moveTo(Poses:array[string][, TimeSpan:time]) → time
<Path>._3D.Poses.moveTo(Poses:array[string][, TimeSpans:array[time]]) → time
```

**Parameters**

- `Pose` (`string`) — the name of the pose toward which the object moves.
- `Poses` (`array[string]`) — the names of several consecutive poses, approached sequentially. If you specify invalid parameters or a pose containing an animatable object that is part of a still-active movement, the Method Debugger opens with an error. A pose movement always consists of all poses specified together with `_3D.Poses.moveTo`; it stays active until the last pose is reached.
  - If the object is to move to a pose named `"init"` and no pose with that name exists, the object moves to an implicit pose that sets all animatable objects of `<Path>` to `0`.
- `TimeSpan` (`time`, optional) — duration of the movement.
- `TimeSpans` (`array[time]`, optional) — durations of the movement.

If you do not specify the parameter, the pose movement runs with the time resulting from the speeds of the joint definitions. If specified:

- A single time means the entire pose movement takes place within the specified time. The time relations of the joints and individual pose movements are retained. Example: if `Station._3D.Poses.moveTo(["Pose1", "Pose2"])` takes 3 seconds (1s for Pose1, 2s for Pose2), then `Station._3D.Poses.moveTo(["Pose1", "Pose2"], 7.5)` takes 7.5 seconds (2.5s for Pose1, 5s for Pose2).
- A sequence of times means the first pose is reached within the first time span, the second in the second, etc. You must specify as many time spans as poses. You can only specify an array of times if you also specified an array of poses.

> `Station._3D.Poses.moveTo("Pose1", [7.5])` results in an error. `Station._3D.Poses.moveTo(["Pose1"], [7.5])` does not result in an error, but is unnecessarily complicated — `Station._3D.Poses.moveTo("Pose1", 7.5)` yields the same result.

**Return Value**

Data type `time` — the time span the designated pose movement will probably take, provided it will not be interrupted.

**Example**

```simtalk
Station._3D.Poses.moveTo(["Pose1", "Pose2"])
Station._3D.Poses.moveTo(["Pose1", "Pose2"], 7.5)
Station._3D.Poses.moveTo("Pose1", 7.5)
```

### `_3D.Poses.moveToCoordinate` [SimTalk]

Moves the object designated by `<Path>` with its first animation point to the designated coordinate and rotation, as long as the identified robot configuration supports this. Works without defining a pose.

- **Type:** Method
- **Remarks:**
  - Does not support the four-axis robot with ball joint gripper.
  - Plant Simulation checks the attribute `_3D.AnimationObject` to identify the robot configuration. The objects between the simulation object (excluded) and `_3D.AnimationObject` (included) are checked for the appropriate robot configuration.
  - A robot type with more axes takes precedence over a robot type with fewer axes.
- **Note:** If Plant Simulation cannot identify the robot configuration, this is an error and the Method Debugger opens.
- **Note:** Not reaching the destination coordinate/rotation is not an error and does not open the Method Debugger. An unsuitable but recognizable axes configuration will not be recognized if, for example, eight axes exist but only the last three are recognized as part of a simpler robot type.
- **Note:** Plant Simulation does not use joint limits in this method.

**Syntax**

```simtalk
<Path>._3D.Poses.moveToCoordinate(Coordinate:length[3], Rotation:real/real[4][, TimeSpan:time]) -> time
```

**Parameters**

- `Coordinate` (`length[3]`) — the destination coordinate in the coordinate system of the object to be moved.
- `Rotation` (`real`) — a rotation around the negative z-axis. Alternatively an `array[real]` with four values designating a rotation (compare `_3D.Rotation`) which the animation point takes within its coordinate system after the pose movement.
- `TimeSpan` (`time`, optional) — duration of the movement. If omitted, the movement runs with the time resulting from the speed from the joint definition.

**Return Value**

Data type `time` — the time span the designated movement will probably take, provided it will not be interrupted.

**Examples**

```simtalk
Station._3D.Poses.moveToCoordinate([1m, 2m, 0m], 0)
Station._3D.Poses.moveToCoordinate([1m, 2m, 0m], 45, 1:00)
Station._3D.Poses.moveToCoordinate([1m, 2m, 0m], [90, 0, 1, 0])
Station._3D.Poses.moveToCoordinate(Station._3D.getPositionFromObject(OtherStations), 0)

var Rotation = Station._3D.getRotationFromObject(OtherObject)
Rotation := F3DconcatenateRotations(Station._3D.getRotationFromObject(OtherObject), [180, 0, 1, 0])
Station._3D.Poses.moveToCoordinate(Station._3D.getPositionFromObject(OtherObject), Rotation)
// grip 'OtherObject' from above
```

### `_3D.Poses.moveToMU` [SimTalk]

Moves the object designated by `<Path>` with its first animation point to the specified MU instance, as long as the identified robot configuration supports this. Works without defining a pose.

- **Type:** Method
- **Remarks:** Same robot-configuration detection notes as `_3D.Poses.moveToCoordinate` (does not support four-axis robot with ball joint gripper; checks `_3D.AnimationObject`; more axes take precedence).
- **Note:** If Plant Simulation cannot identify the robot configuration, this is an error and the Method Debugger opens.
- **Note:** Not reaching the destination MU instance is not an error.

**Syntax**

```simtalk
<Path>_3D.Poses.moveToMU(MU:object[, TimeSpan:time]) -> time
```

**Parameters**

- `MU` (`object`) — the MU instance to which the object is to move.
- `TimeSpan` (`time`, optional) — duration of the movement. If omitted, the movement runs with the time resulting from the speed from the joint definitions.

**Return Value**

Data type `time` — the time span the designated movement will probably take, provided it will not be interrupted.

**Examples**

```simtalk
var mu = otherObject.cont
var arm = self.~._3D.getObject("Arm")
wait arm.moveToMU(mu)

-- control MyRob action to pick parts at the store
-- and drop them on the station
var nextPart : object
for var i := 1 to 12
    nextPart = Store.cont
    waituntil station.empty
    -- move to part and load it
    wait MyRob._3D.Poses.MoveToMU(nextPart)
    nextPart.move(MyRob)
    wait 1
    -- move to target station and drop part there
    wait MyRob._3D.Poses.MoveToMUAnimationPosition(nextPart, Station)
    nextPart.move(Station)
    wait 1
    -- move robot to home position
    wait MyRob._3D.Poses.moveTo("home")
next
```

### `_3D.Poses.moveToMUAnimationPosition` [SimTalk]

Moves the object designated by `<Path>` with its first animation point to the position and rotation in space where the specified MU instance would be located when being moved to the specified place, as long as the identified robot configuration supports this. Works without defining a pose.

- **Type:** Method
- **Remarks:** Same robot-configuration detection notes as above. If the destination is length-oriented, computes a movement that deposits the front of the MU at the destination instead of the booking point. For place-oriented objects nothing changes.
- **Note:** Plant Simulation does not use joint limits in this method.

**Syntax**

```simtalk
<Path>_3D.Poses.moveToMUAnimationPosition(MU:object, TargetPE:object/PE[, RelPos/AbsPos:real/length, TimeSpan:time]) -> time
```

**Parameters**

- `MU` (`object`) — the MU instance to be measured when moving to the target place.
- `TargetPE` (`object`) — the place to which the item is to move (a specific PE or an object with only one PE).
- `RelPos/AbsPos` (`real`/`length`, optional) — if `real`, relative position between `0` and `1`; if `length`, absolute position from the beginning of the object. Only used for length-oriented places. Defaults to `0.0`.
- `TimeSpan` (`time`, optional) — duration of the movement. If omitted, the movement runs with the time resulting from the speeds of the joint definitions.

**Return Value**

Data type `time` — the time span the designated movement will probably take, provided it will not be interrupted.

**Examples**

```simtalk
var mu = otherObject.cont
wait self.~._3D.moveToMUAnimationPosition(mu)

-- control MyRob action to pick parts at the store
-- and drop them on the station
var nextPart : object
for var i := 1 to 12
    nextPart = Store.cont
    waituntil station.empty
    -- move to part and load it
    wait MyRob._3D.Poses.MoveToMU(nextPart)
    nextPart.move(MyRob)
    wait 1
    -- move to target station and drop part there
    wait MyRob._3D.Poses.MoveToMUAnimationPosition(nextPart, Station)
    nextPart.move(Station)
    wait 1
    -- move robot to home position
    wait MyRob._3D.Poses.moveTo("home")
next
```

### `_3D.Poses.pauseMovement` [SimTalk]

Pauses the movement toward the designated pose of the object designated by `<Path>`.

- **Type:** Method
- **Remarks:** If you do not specify the optional parameter, all movements will be paused. Affects the designated pose together with the other poses from a common `_3D.Poses.moveTo` call.

**Syntax**

```simtalk
<Path>._3D.Poses.pauseMovement([Pose:string])
```

**Parameter:** `Pose` (`string`, optional) — the name of the pose toward which the object moves.

**Example**

```simtalk
Station._3D.Poses.moveTo(["Pose1", "Pose2"])
Station._3D.Poses.pauseMovement("Pose1")

// instead, you can also enter:
Station._3D.Poses.pauseMovement("Pose2")
```

### `_3D.Poses.setTable` [SimTalk]

Sets the poses of the object designated by `<Path>` from the specified table.

- **Type:** Method

**Syntax**

```simtalk
<Path>._3D.Poses.setTable(Poses:table)
```

**Parameter:** `Poses` (`table`) — the table which contains the data of the poses.

**Example**

```simtalk
var t : table
MyStation._3D.Poses.getTable(t)
MyStation._3D.Poses.setTable(t)
```

### `_3D.Poses.stopMovement` [SimTalk]

Stops the movement toward the designated pose of the object designated by `<Path>` and, if you entered a deceleration for the joints, decelerates toward a halt.

- **Type:** Method
- **Remarks:** Do not specify the optional parameter to stop all movements. Affects the designated pose together with the other poses from a common `_3D.Poses.moveTo` call.

**Syntax**

```simtalk
<Path>._3D.Poses.stopMovement([Pose:string]) -> time
```

**Parameter:** `Pose` (`string`, optional) — the name of the pose toward which the object moves.

**Return Value:** Data type `time`.

**Example**

```simtalk
Station._3D.Poses.moveTo(["Pose1", "Pose2"])
wait Station._3D.Poses.stopMovement("Pose1")
// instead, you can also enter:
wait Station._3D.Poses.stopMovement("Pose2")
```

---

## See Also (cross-references)

- Joint
- Poses
- Model Joints and Poses
- Configuring the Robot
- Open and Close the Gate with/without Poses
- Move the Gate Up to the Height of the Part
- Joint Settings of an Animatable Object
- Edit 3D Properties > Robot Arm Animation [PickAndPlace]
- Type of Joint > Revolute Joint
- `_3D.getObject`, `_3D.Rotation`, `_3D.AnimationObject`
- `_3D.AniRotationAxis`, `_3D.AniRotationCenter`, `_3D.AniTranslationDirection`
- `_3D.getMUAnimationPosition`, `_3D.getMUAnimationRotation`
- `moveTo`, `moveToCoordinate`, `moveToMU`, `moveToMUAnimationPosition`
- Videos: [Robots (YouTube)](https://youtu.be/wfVN-mcWNsc?si=Un-c8tYPrM135pgG&t=479), [Poses (YouTube)](https://youtu.be/rQi5oRyZckQ?si=pGkDwvoDw3LOD4Wo&t=1130)
