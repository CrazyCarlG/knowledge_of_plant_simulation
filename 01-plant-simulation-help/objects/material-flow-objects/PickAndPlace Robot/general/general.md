# PickAndPlace Robot — General

Use the object **PickAndPlace robot** for picking up a part at one station, rotating it, and placing it onto another station.

## Assignment Value

You can assign a value of data type `string` (e.g. for the `Sequence` drop-down). Possible values include:

- `"MUs to all successors"`
- `"MUs exiting independent of other MUs"`
- `"Main MU after other MUs"`

```simtalk
MyDismantleStation.Sequence := "Main MU after other MUs"
```

---

## PickAndPlace Robot

The PickAndPlace robot picks up a part at one station, rotates it, and places it onto another station. It can pick up and deliver one or more parts (set via **Capacity**).

### Flow of materials

1. The part arrives at the exit of the predecessor and notifies the PickAndPlace robot that it wants to be picked up.
2. The robot determines whether to pick the part up:
   - Without a **Pull Control**, the robot is notified and accepts the part.
   - With a **Pull Control**, the robot executes it and picks up the part when it is selected.
3. The robot rotates to the respective predecessor and picks the part up.
4. For the target station, the robot uses its default **Exit Strategies** or the **Target Control** (in which you set the target station). The Target Control is called when the robot picks up or places a part; within the method `setDestination`, the boolean parameter controls whether the robot waits at the target station.
5. The robot rotates to the target station and places the part.
6. It then rotates back to the standard position.

The PickAndPlace robot can emulate most of the functions of the TransferStation.

### Show Manipulators

To change the length of the graphic and anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`. The rotation manipulator sets the rotation of the object with the mouse and keyboard:

- Drag right → rotate clockwise around the z-axis; drag left → counter-clockwise.
- Click the manipulator and press left/right arrow → rotate by 1°.
- Hold `Shift` + left/right arrow → rotate by 45°.

> Note: A rotation manipulator cannot be selected together with anything else in a 3D window at the same time.

### Adding to the model

Click **Manage Class Library > Basic Objects > MaterialFlow > PickAndPlace** on the Home ribbon tab. Sample models: Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples.

---

## Configuring the Robot with Drag-and-Drop

Drag the PickAndPlace robot over a Conveyor, Track, or TwoLaneTrack and select the operation. Drag-and-drop only works for length-oriented objects for which you can define sensors. A complete configuration requires two drag-and-drop operations (one pick/unload + one place/load).

| Operation | Behavior |
|-----------|----------|
| **Pick part** | Picks parts from a length-oriented object at a sensor. Creates a front-triggered sensor with light-barrier mode plus a sensor control for moving the part to the robot. |
| **Unload part** | Unloads parts from a Container or Transporter at a sensor. Creates a front-triggered sensor with light-barrier mode plus a sensor control for unloading to the robot. |
| **Place part** | Places parts onto a length-oriented object at a sensor. Creates a rear-triggered sensor with light-barrier mode without a sensor control; also sets Target Selection, Target Object, and Target Sensor ID. |
| **Load part** | Loads parts onto a Container or Transporter at a sensor. Creates a sensor triggered by the booking point, without a sensor control; sets Target Selection, Target Object, and Target Sensor ID. |

For all cases, Plant Simulation creates an entry in the **Angles Table** and the **Times Table**.

---

## Configuring the Robot (Robot Arm Animation)

The **Robot Arm Animation** tab determines the paths the robot touches before picking up or depositing a part. Robot arm animation paths are only used for robots with at least three axes.

Animation objects are defined in the **Animation Object** text box on the **MU Animation** tab. The robot checks the robot types top-to-bottom and stops at the first match:

1. Six Axis Robot
2. Five Axis Robot
3. Four Axis Robot with Ball Joint Gripper
4. SCARA Robot with Concluding Revolute Joint
5. SCARA Robot with Concluding Prismatic Joint
6. Three Axis Robot
7. One Axis Robot
8. Linear Robot

If none is recognized, the robot rotates completely around rotation axis `[0,0,-1]` through rotation center `[0,0,0]`.

> Note: The default robot before Plant Simulation 13.0 was a one axis robot; such robots are not changed when loaded from older models.

The CranesAndMore library provides a seven axis robot moving on rails as a demonstrator. You can transform any material flow or fluid object into a robot by exchanging its graphic with one of the robots in `3D\s3d-graphics`.

### Six Axis Robot

Recognized if exactly these criteria are met (revolute joints through rotation center `[0,0,0]`):

1. First animatable object: revolute joint around `[0,0,1]` or `[0,0,-1]`.
2. Next lower level: revolute joint around `[0,1,0]` or `[0,-1,0]`.
3. Next lower level: revolute joint around `[0,1,0]` or `[0,-1,0]`.
4. Next lower level: revolute joint around `[0,0,1]`, `[0,0,-1]`, `[1,0,0]`, or `[-1,0,0]`.
5. Next lower level: revolute joint around `[0,1,0]` or `[0,-1,0]`.
6. Next lower level: revolute joint around `[0,0,1]`, `[0,0,-1]`, `[1,0,0]`, or `[-1,0,0]` (the latter two only if axis 4 also used `[1,0,0]`/`[-1,0,0]`).
7. `_3D.AnimationObject` references the respective lowest animatable object.
8. A suitable animation path exists for that object.

A six axis robot can reach all points in its gripping range and position the MU in all positions it can reach. Changing rotations of the lowest three animatable objects (or a toolholder perpendicular above the insertion point) may prevent positioning. The robots `PickAndPlaceComau.s3d` and `PickAndPlaceKuka.s3d` are six axis robots.

### Five Axis Robot

Recognized if exactly these criteria are met:

1. Revolute joint around `[0,0,1]` or `[0,0,-1]`.
2–4. Revolute joints around `[0,1,0]` or `[0,-1,0]` (three levels).
5. Revolute joint around `[0,0,1]` or `[0,0,-1]`.
6. `_3D.AnimationObject` references the lowest animatable object.
7. A suitable animation path exists.

A five axis robot can position the MU in most, but not all, positions.

### Four Axis Robot with Ball Joint Gripper

Recognized if exactly these criteria are met:

1. Revolute joint around the z-axis through `[0,0,0]`.
2–3. Revolute joints around `[0,1,0]` or `[0,-1,0]` (two levels).
4. Revolute joint through rotation center `[0,0,0]`.
5. `_3D.AnimationObject` references the lowest animatable object.
6. A suitable animation path exists.

The default robot in Plant Simulation is a four axis robot with ball joint gripper. You cannot move its poses and joints with the mouse or keyboard.

### SCARA Robot with Concluding Revolute Joint

Recognized if exactly these criteria are met:

1–2. Revolute joints around `[0,0,1]` or `[0,0,-1]`.
3. Prismatic joint with translation direction `[0,0,1]` or `[0,0,-1]`.
4. Revolute joint around `[0,0,1]` or `[0,0,-1]`.
5. `_3D.AnimationObject` references the lowest animatable object.
6. A suitable animation path exists.

It can only place MUs in positions described exclusively by a rotation around the z-axis.

### SCARA Robot with Concluding Prismatic Joint

Recognized if exactly these criteria are met:

1–3. Revolute joints around `[0,0,1]` or `[0,0,-1]` (three levels).
4. Prismatic joint with translation direction `[0,0,1]` or `[0,0,-1]`.
5. `_3D.AnimationObject` references the lowest animatable object.
6. A suitable animation path exists.

`PickAndPlaceComauSCARA.s3d` is a SCARA robot.

### Three Axis Robot

Recognized if exactly these criteria are met:

1. Revolute joint around `[0,0,1]` or `[0,0,-1]`.
2–3. Revolute joints around `[0,1,0]` or `[0,-1,0]` (two levels).
4. `_3D.AnimationObject` references the lowest animatable object.
5. A suitable animation path exists.

The MU is attached rigidly at the gripper and only rotated by the robot movement.

### One Axis Robot

Recognized if exactly these criteria are met:

1. Revolute joint around `[0,0,1]` or `[0,0,-1]`.
2. `_3D.AnimationObject` references the lowest animatable object.
3. A suitable animation path exists.

A one axis robot cannot reach all points in its gripping range, and does not use user-defined robot arm animations.

### Linear Robot

Recognized if exactly these criteria are met:

1. First animatable object has a prismatic joint.
2. Next lower level: prismatic joint with translation direction orthogonal to the one above.
3. Next lower level: prismatic joint with translation direction orthogonal to both above.
4. `_3D.AnimationObject` references the lowest animatable object.
5. A suitable animation path exists.

A linear robot is still recognized if the latter animatable object does not exist.

---

## Dialog Box of the PickAndPlace Robot

Double-click the icon to open its dialog box. Shared simulation properties are described under *Dialog Items of the Objects*. To edit 3D properties, click **Edit 3D Properties** or press the spacebar.

---

## Tab Attributes

### Angles Table [PickAndPlace]

Opens the table of the angles at which the robot picks up or places a part. View/fine-tune:

- **Name** — the predecessor (pick up) or successor (deposit). You can also type a sensor, e.g. `Conveyor.Sensors.ID1`.
- **Angle** — between the station and the robot.

Connectors/drag-and-drop add values automatically. Deleting a Connector does not delete the entry; delete it yourself. Right-click the robot and select **Calculate Angles** to recompute angles.

SimTalk: `setAnglesTable`, `getAnglesTable`, `calculateAngles`.

### Times Table [PickAndPlace]

Opens the table of rotation times between stations (and back). Also includes a **Time Factor** multiplying all times.

- **Names** of all objects served and the **Default Angle**.
- Times **above the diagonal** = rotation **empty**; **below the diagonal** = rotation **full** (with a part).

A quarter-rotation is assumed to take one second when auto-populated. Deleting a Connector does not delete the entry; delete it in the Angles Table, and clicking Apply removes it from the Times Table too.

SimTalk: `setTimesTable`, `getTimesTable`.

### Go to Default Position [check box]

Rotate the robot back to its default position after depositing a part. When active, you can also activate **Only for Empty Blocking List**.

SimTalk: `GoToDefaultPosition`, `OnlyForEmptyBlockingList`, `DefaultAngle`.

### Only for Empty Blocking List

Only rotate back to the default position if the blocking list is empty (no additional requests). Only changeable when **Go to Default Position** is active.

### Use Kinematics for Times

Uses the 3D kinematics of the robot to calculate timing instead of the Angles/Times tables. Only works with supported robot kinematics. Supports all kinematics used for `_3D.Poses.moveToCoordinate`, `_3D.Poses.moveToMU`, and `_3D.Poses.moveToMUAnimationPosition`, except linear robots. Increase the **Joint Velocity** to move the arm faster.

SimTalk: `UseKinematicsForTimes`.

### Time Factor

Multiplies all times in the Times Table, simulating different speeds without editing the table.

SimTalk: `TimeFactor`.

### Default Angle

The angle (in degrees) the robot rotates to when **Go to Default Position** is selected. Add 180° to face the start position. Range 0°–360°. Also used as the start position after a Reset regardless of the check box.

SimTalk: `DefaultAngle`.

### Blocking Angle [text box]

An angle the robot cannot cross while rotating (prevents the shortest way). Default `-1` = no blocking angle. Range 0–360. Affects animation only; simulation is controlled by the Times Table.

SimTalk: `BlockingAngle`.

### Capacity [text box]

Number of MUs the robot can transport at one time (greater than 1). Enables picking up several parts and placing them one at a time (FIFO). Use an **Exit Control** for other rules (e.g. LIFO).

SimTalk: `Capacity`.

### MU Conveying Direction [drop-down list]

Select the conveying direction of the MU when the robot passes it on to the successor.

| Setting | Description |
|---------|-------------|
| **Retain** | Continues conveying in the arrival direction. |
| **Rotate 90° to the right** | Rotates 90° right (relative). |
| **Rotate 90° to the left** | Rotates 90° left (relative). |
| **Rotate 180°** | Rotates 180° (relative). |
| **Forwards** | Rotates so it rests forward (absolute). |
| **Lateral right** | Rests laterally to the right (absolute). |
| **Backwards** | Rests backward (absolute). |
| **Lateral left** | Rests laterally to the left (absolute). |

> Note: `Retain`, `Rotate by 90°`, and `Rotate by 180°` are relative rotations; `Forwards`, `Lateral right`, `Backwards`, `Lateral left` are absolute.

SimTalk: `MUConveyingDirection`.

### Loading Time

Time to pick up a part at a station.

- Point-oriented station: part is booked on the robot while picking up; station locked until loading time elapses.
- Length-oriented station: part remains on the station during loading, then moves to the robot.

Choose a distribution (or constant `Const`). For `Formula`, you can enter a numeric expression or a Method name; use `@` for the part and `?` for the robot. During loading no part can be placed on the delivering station. Interruptions of the robot extend the loading time; interruptions of the delivering station do not affect loading.

SimTalk: `LoadingTime`, `LoadingTime.Type`, `IsLoading`, `putAttributeNamesIntoTable`.

### Unloading Time

Time to place the picked part onto the target station.

- Point-oriented station: part booked on the robot while placing; target station locked until unloading time elapses.
- Length-oriented station: part moved onto it before unloading time starts.

Same distribution/Formula options (`@` = part, `?` = robot). Robot interruptions extend unloading; target-station interruptions do not affect it.

SimTalk: `UnloadingTime`, `UnloadingTime.Type`, `IsLoading`, `putAttributeNamesIntoTable`.

---

## Tab Failures

Defined as described under the general **Tab Failures**.

---

## Tab Controls

Controls modify the built-in behavior. Select an existing Method via the ellipsis button, press `F2` to edit source code, or drag a Method into the text box.

To create a control as a user-defined attribute of type Method:

- Type a name and select **Create Control** → inserts `self.Name`, e.g. `self.A1Ctrl`.
- Or select **Create Control** on an empty box → inserts `self.OnBuilt_in_name`, e.g. `self.OnEntrance`.

Delete a control by deleting the user-defined attribute (deleting only the name retains the attribute).

### Target Control

Called as soon as the robot has picked up the part (before it is ready to exit). Sets the target where the robot places the part. Also called after depositing the part, where you set the next pick-up object via `setDestination`; in this case `@` is void. Only called while unloading if **Go to Default Position** is cleared. You must use `setDestination` to determine the target object.

> Note: Do not use an Exit Control to determine the target — it is called too late (only when the MU is ready to exit).

SimTalk: `TargetCtrl`, `setDestination`, `getDestination`.

### Pull Control

Called whenever the robot is ready to pick up a new part. Determines which waiting part the robot accepts: get the Forward Blocking List with `fwBlockList` and unblock a MU with `unblock`. For faster access to the first entry use the read-only attribute `FwBlockListEntry1`. It selects among parts already determined to move to this successor (it does not choose the successor).

Example use case: pull red parts first (priority), then other colors.

SimTalk: `PullCtrl`.

---

## Tab Exit

Select how the robot moves parts to its target stations.

- **Target Selection > Exit strategy or target control**: select the exit strategy; the robot must be connected via Connectors. Select **Wait for Free Target** to only rotate/pick up if the destination is ready.
- **Target Selection > Place part at sensor** / **Load part onto MU at sensor**: shows **Target Object** and **Target Sensor ID**; the robot uses a sensor you create (no Connector needed).

### Wait for Free Target

Only rotate to a part and pick it up if the destination is ready to receive it. Prevents transporting parts to an occupied/reserved Station or Conveyor, keeping the robot available. Only evaluated for **Exit strategy or target control**. The part enters the Forward Blocking List of the target. The exit strategy/Target Control is evaluated before the robot rotates to pick up.

SimTalk: `WaitForFreeTarget`, `TargetSelection`, `ReservedFor`, `ReservedPlace`, `contentsAndReservedList`.

### Target Selection [drop-down list]

- **Exit strategy or target control** — default; set target via Exit Strategy or Target Control.
- **Load part onto MU at sensor** — requires a manually created front-triggered light-barrier sensor on the length-oriented target, plus Target Object and Target Sensor ID. Stopping/loading/sending works automatically only without a control.
- **Place part at sensor** — requires a manually created rear-triggered light-barrier sensor plus Target Object and Target Sensor ID.

SimTalk: `TargetSelection`.

### Target Object

Path to the length-oriented object where the part is placed/loaded (or select via **Select Object**).

SimTalk: `TargetObject`.

### Target Sensor ID [text box]

Sensor ID of the target sensor. The sensor is not created automatically — create it manually or use drag-and-drop.

SimTalk: `TargetSensorID`.

---

## Tab Statistics

In addition to standard statistics, the robot collects:

| Item | Description | Read-only attribute |
|------|-------------|---------------------|
| **Rotation Empty** | Portion of the period rotating without a part. | `StatRotationEmptyPortion` |
| **Rotation Loaded** | Portion of the period rotating while moving a part. | `StatRotationLoadedPortion` |

View in the Statistics Report (`F6` or View > Show Statistics Report).

---

## Tab Importer

The PickAndPlace robot only provides the **Failure Importer**.

---

## Tab Energy

Select energy settings as described under the general **Tab Energy**.

---

## Tab Costs

Costs accrue while the robot picks up, rotates, and places parts (investment + operating costs). Investment costs only accrue during the Depreciation Period. Costs are allocated to the part as accrued costs; if the robot is empty, costs remain with the robot as general costs.

---

## Tab User-defined

Define own attributes as described under the general **Tab User-defined**.

---

## Menus

- **Navigate Menu** — described under the general Navigate Menu.
- **View Menu** — provides *Refresh*, *Show Statistics Report*, *Show Attributes and Methods*, and *Contents* (Forward/Exit Blocking List, Associated Lockout Zones, Associated Shift Calendar).
- **Tools Menu** — described under the general Tools Menu.
- **Tabs Menu** — show/hide individual tabs; use **Inherit** to toggle inheritance of tab visibility.
- **Help Menu** — described under the general Help Menu.

---

## Methods of the PickAndPlace Robot

The PickAndPlace robot provides:

- The methods listed in the table of contents.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods/attributes, open **Show Attributes and Methods** (context menu of the Class Library, or `F8` / Home ribbon tab for an instance).
