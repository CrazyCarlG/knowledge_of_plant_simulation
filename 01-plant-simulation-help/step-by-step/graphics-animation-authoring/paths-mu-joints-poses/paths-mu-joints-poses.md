# Working with Animation Paths

Animation paths consist of a set of points in space describing the path on which an animated moving object moves on the material flow objects or through the scene. Cameras, through which you view the scene when you fly through it, also use animation paths.

There are three kinds of animatable object paths. The procedures for creating and editing the different path types differ only slightly, so the common properties are described together.

## Path types

### MU animation paths
Create and edit animation paths and the animation area, on which parts are animated, under **Edit 3D Properties > Tab MU Animation** on the Home ribbon tab.

### Self animation paths
Create and edit paths on which the object itself is animated by clicking **Edit 3D Properties > Tab Self Animation** on the Home ribbon tab.

- The anchor points of self animation paths are the vertices of the line, polycurve, or spline on which the selected object itself moves. For example, a self animation path can simulate the movement of a robot.
- Polycurve animation anchor points are the vertices of a curved path (a sequence of curved and straight lines) on which the material flow object itself moves.
- Spline animation anchor points are the vertices of a spline curve.

### Camera animation paths
Create and edit paths on which the camera moves through the 3D scene in the Frame by clicking **Edit 3D Properties > Tab Camera Animation** on the Home ribbon tab.

- The anchor points of camera animation paths are the vertices of the line, polycurve, or spline on which the camera moves through the scene in the Frame.
- Polycurve animation anchor points are the vertices of a curved path (a sequence of curved and straight lines) on which the camera moves.
- Spline animation anchor points are the vertices of a spline curve.

## Create an Animation Path

You can create three types of animation path:
- A path on which the MU is animated while it moves through the plant.
- A path on which the material flow object itself is animated.
- A path on which the camera moves through the Frame.

Proceed as follows:

1. Open the dialog **Edit 3D Properties**. Click the **Tab MU Animation**, **Tab Self Animation**, or **Tab Camera Animation**, depending on the path you want to create.
2. Click **Add**.
3. Enter a unique name for the path if you are creating an animation path. As a rule you will use the `Default` path for the animation.
4. Select the **Path type** you would like to create.
   - If objects such as the Store or the ParallelStation have several defined locations for placing incoming mobile objects, you can distribute them on the animation area on the tab MU Animation.
5. Click **OK** to create the path. Initially the path consists of a single anchor point located at the origin of the selected object.
6. Extend and/or edit the new initial path by clicking **Edit 3D Properties > MU Animation/Self Animation/Camera Animation > Edit > Path Anchor Points** on the Home ribbon tab.

## Create an Animation Path that Rotates Objects

You can create an animation path that causes a circular rotation of an object (for example, the movement of a crane arm) by setting rotation parameters instead of editing anchor points.

Proceed as follows:

1. Select the material flow object or scene object and click **Edit 3D Properties** on the Home ribbon tab.
2. To rotate the MUs that the selected object processes, click **Tab MU Animation**. To rotate the object itself, click **Tab Self Animation**.
3. Click **Add**. Enter a name for the rotation path in the dialog **Create Rotation Path** that opens. Select **Path Type > Rotation Path [MU animation] - Lines**.
4. Edit the settings in the dialog **Create Rotation Path**:
   - **Start Angle** — where the rotation starts.
   - **End Angle** — where the rotation ends. 3D only rotates the MU if these values are not identical. The values can be greater than 360 degrees and smaller than -360 degrees to execute more than an entire rotation.
   - Start Angle and End Angle set the rotation direction, depending on which value is greater:
     - An End Angle greater than the Start Angle results in a clockwise rotation.
     - An End Angle smaller than the Start Angle results in a counter-clockwise rotation.
   - **Axis** — the values around which you want to rotate the MUs. Normally you will use the Z-axis `(0,0,1)` to rotate on the XY plane; the Y-axis `(0,1,0)` to rotate on the XZ plane; or the X-axis `(1,0,0)` to rotate on the YZ plane. Any other axis rotates the object diagonally in 3D space. To tilt the rotation axis, enter a value into at least two text boxes.
   - **Center point** — the center of the rotation in the coordinate system of the selected object. If the center is not the same as the start position, the rotated object moves on a circular arc and stops at a different position than its starting point, except after a 360-degree rotation.
5. Click **Apply** to compute the animation path. This path is the trace on which the animated object moves; the movement on this path is the rotation.

> **Note:** You can use the method `_3D.SelfAnimations.scheduleRotation` to run self-rotations or camera-rotations without having to create a path.

6. To test the rotation path, select an object and start the test animation.
7. If the rotation movement does not meet your expectations, reopen the dialog **Create Rotation Path**, edit the parameters, click **Apply**, and test again until the rotation meets your needs.
8. To change the duration of one or more individual rotation steps:
   - Select the path in the list and click **Edit**.
   - Select the anchor point in the dialog **Path Anchor Points** and click **Edit Values** to open the dialog **Edit Anchor Point**. Under **Time** you can edit the time of every anchor point, which matches the rotation steps.

## Edit an Animation Path

You can edit the different animation paths in the dialog **Edit 3D Properties**.

To work with animation paths of parts (MUs) on an object:
- Select the object and click **Edit 3D Properties** on the Home ribbon tab.
- Click the **Tab MU Animation** and create or edit an animation path.

To work with animation paths on which the object itself is animated in the scene:
- Select the object and click **Edit 3D Properties** on the Home ribbon tab.
- Click the **Tab Self Animation** and create or edit an animation path.

To work with camera animation paths of the Frame:
- Select the Frame and click **Edit 3D Properties** on the Home ribbon tab.
- Click the **Tab Camera Animation** and create or edit a camera animation path.

> **Note:** Only the Frame provides the tab Camera Animation.

In or from the dialog you can:
- Create an Animation Path.
- Test an Animation Path.
- Edit an Animation Path with the Mouse.
- Edit an Animation Path via Anchor Points.
- Create an Animation Path that Rotates Objects.
- Rename an animation path.
- Delete an animation path.

## Edit an Animation Path with the Mouse

You can edit an animation path with the mouse in the Frame window.

1. Open the dialog **Edit 3D Properties**. Click the **Tab MU Animation**, **Tab Self Animation**, **Tab Camera Animation** [Frame], or **Tab Robot Arm Animation** [PickAndPlace], depending on the path you want to edit.
2. To show the selected path in the scene window, click the button in the cell **Show** under animation paths. Plant Simulation then shows the path with its anchor points.
3. To add new anchor points, click **Extend** and click the left mouse button at the position where you would like to insert a new anchor point. Repeat until the path has the shape you want.
4. To change the shape of the path, select an anchor point and manipulate it with the mouse, and/or use the settings by clicking **Edit 3D Properties > Tab Transformation**. When you drag an anchor point in the X/Y-direction, Plant Simulation also drags the connected curved segments in both directions (until the next straight segment follows).
5. To rotate an anchor point, click it, hold down the left mouse button, and drag the mouse, and/or click **Edit 3D Properties > Transformation**.

> **Note:** When you rotate an anchor point describing an animation path, this also rotates any MU moving along that path.

6. To delete part of the path, select an anchor point and press **Delete**. This removes the selected anchor point from the path, modifying its shape.

## Edit a Curved Path with the Mouse

You can edit and extend a curved path with the mouse in a number of ways. In addition to editing any path type with the mouse, you can edit polycurve paths as follows:

- Add new anchor points to the animation path by clicking **Extend**:
  - To add a straight segment, click the left mouse button at the position where you would like to insert a new anchor point.
  - To add a curved segment, hold down **Ctrl** and click the left mouse button at the position where you would like to insert a new anchor point.
  - Repeat until the path has the shape you want.
- Change the shape of a straight segment by selecting an anchor point and dragging the mouse. When you drag an anchor point in the X/Y-direction, 3D also drags attached curved segments (until the next straight segment follows) in both directions.

## Edit an Animation Path via Anchor Points

You can edit an animation path by entering exact values into the dialog **Path Anchor Points** — useful when editing with the mouse is not precise enough.

1. Open the dialog **Edit 3D Properties**. Select the animation path on the **Tab MU Animation**, **Tab Self Animation**, or **Tab Camera Animation**.
2. Click **Edit**.
3. Select the anchor point in the dialog **Path Anchor Points**, then click **Edit Values**, or double-click the row in the table.
4. Enter or select the new settings for the **Position** and **Rotation** of this anchor point in the dialog **Edit Anchor Point**.
5. To add a new anchor point to the end of the selected path, click **Add**. The list adds the settings of the new anchor point to its bottom. You can then edit its settings.
6. To insert a new anchor point before the selected anchor point, click **Insert Before**.
7. To delete an anchor point, select it in the list and click **Delete**.
   - To delete contiguous anchor points, hold down **Shift** and click the first anchor point in the range, then the last anchor point.
   - To delete non-contiguous anchor points, hold down **Ctrl** and click the anchor points one after the other.
8. To move the selected anchor point up one position in the list, click **Move Up**.
9. To move the selected anchor point down one position in the list, click **Move Down**.
10. To duplicate the settings of the selected anchor point and insert the duplicated anchor point below the original, click **Duplicate**.

> **Note:** You can edit paths of type Polycurve in the dialog Edit.

## Test an Animation Path

After defining the animation path, you can test the settings on the Animation tabs in the group box **Test Path** without running a simulation.

Proceed as follows:

1. Select the **Test Object** — an MU whose graphic 3D copies and uses as the test object.
2. Enter the **Velocity** with which the test object moves on the path.
3. Select whether the test object moves in the forward direction or **Backwards**. 3D automatically enters a negative velocity when you select Backwards.
4. Click play to run the animation with the selected settings.
5. Click pause to pause the test animation.
6. Click stop to stop the test animation.

# Controlling the MU Animation

On the tab **MU Animation** you can define how mobile objects (MUs) are animated on the material flow objects. The Frame also counts as a material flow object. The tab looks different for objects without loading space and for objects with loading space.

- On the **Sub-tab Animation Paths** you can define:
  - MU Animation on Length-Oriented Objects
  - MU Animation on Point-Oriented Objects
  - MU Animation on Point-Oriented Objects Holding Several Parts
  - MU Animation on Animation Paths on the Workplace
- On the **Sub-tab Animation Area** you can define the MU Animation on Objects with Loading Space by activating the Animation Area.

Objects with a loading space — AGVPool, Container, ParallelStation, PlaceBuffer, Store, Transporter, Worker, Workplace, and WorkerPool — use the Animation Area, provided you activated it. If it is not activated, the objects use animation paths. Except for the AGVPool, you have to create the animation paths yourself.

## MU Animation on Length-Oriented Objects

Length-oriented objects animate parts automatically. If a path named `Default` exists, the objects use that path.

- The length-oriented objects **AngularConverter, FootPath, Turnplate, and Turntable** can each hold and transport a single part.
- The length-oriented objects **Conveyor, Track, and TwoLaneTrack** can hold and transport several parts.
- For all length-oriented objects you can add an **Animation Offset** and select or clear **Gravity Mode**. Press the **M** key to show the manipulators in the scene.
- The **Conveyor** animates parts on the blue line in the center of the conveyor.
- The **FootPath** animates Workers on the blue line in the center.
- The **Converter** animates parts automatically. If a path named `Default` exists for length-wise movements and `Cross` for cross-wise movements, it uses that path.
- The **Track** animates Transporters in the center of the travel track.
- The **TwoLaneTrack** animates Transporters automatically. If paths named `A` or `B` exist (depending on the lane and the setting for right-hand or left-hand traffic), it uses those.

## MU Animation on Point-Oriented Objects

For point-oriented objects that hold a single part (for example, the Station), you can:
- Specify the **Animation Object** and the **MU Side to Attach**.
- Add, extend, edit, and delete an animation path.

The point-oriented objects that hold a single part animate parts as follows:
- The **Station** uses the path named `Default` for animating the parts. Click **Show** to show the MU animation path. As the Station can only process a single part, the path consists of a single point. The path tool (the red pyramid) shows where the part is going to be animated; you can click the path tool and move it with the arrow keys.
- The **DePortioner** uses the path named `Default`.
- The **Portioner** uses the path named `Default`.

## MU Animation on Point-Oriented Objects Holding Several Parts

For point-oriented objects that hold several parts, you can:
- Specify the **Animation Object** and the **MU Side to Attach**.
- Add, extend, edit, and delete an animation path.

The point-oriented objects that hold several parts animate parts as follows:
- The **Buffer** stacks parts along the standard animation path upward, one on top of the other. Set the Buffer capacity in the dialog of the simulation properties on the tab Attributes.
- The **PickAndPlace** robot animates parts automatically. If a path exists, it uses the first path for the first MU, the second path for the second MU, etc. If no suitable path exists but a path named `Default` exists, the robot uses that path.
- The **WorkerPool** lets you select whether it shows Workers on animation paths or on an animation area distributed along the Y-dimension. The WorkerPool in the Class Library only shows created Workers when you activate **Show Content** on the tab Graphics.
  - For the setting **Animation Path**, the WorkerPool uses the first path for the first MU, the second path for the second MU, etc. If no suitable path exists but a path named `Default` exists, the WorkerPool uses that path.
- The **Workplace** lets you select whether it shows Workers on animation paths or on an animation area distributed along the X-dimension.

If you do not use an animation area: Plant Simulation animates the first Worker on the first animation path, the second Worker on the second animation path, and the third Worker on the third animation path. You have to define these animation paths yourself. If no third path exists for the third Worker, Plant Simulation uses the default animation path. If no default animation path exists, Plant Simulation does not animate the Worker at all.

## MU Animation on Objects with Loading Space

Plant Simulation animates MUs on objects with a loading space on their animation area.

Objects with a loading space — AGVPool, Container, ParallelStation, PlaceBuffer, Store, Transporter, Worker, Workplace, and WorkerPool — use the animation area, provided you activated it. If it is not activated, the objects use animation paths.

> **Note:** The indexes for paths start with 0, not with 1. The signature `#0#0` designates the first animation point; `#1#2` designates the position with the X-index 2 and the Y-index 3.

As a rule, you can use the factory settings for these objects unless they do not meet your requirements. Plant Simulation distributes parts evenly across the animation area, which is defined by its length and width.

> **Note:** Plant Simulation recommends using the Animation Area instead of animation paths because it requires substantially less modeling effort (you do not have to create the animation paths).

The objects with a loading space animate parts as follows:

- **AGVPool** only shows created Transporters if you activate **Show Content** on the tab Graphics.
  - If the Animation Area is active, the AGVPool uses it. The index of the MU is the index of the area in the Y-direction; the capacity in the X-direction is always 1.
  - If the Animation Area is not active, the AGVPool uses the first path for the first MU, the second path for the second MU, etc. If no suitable path exists but a path named `Default` exists, the AGVPool uses that path.
- **Container** (standard setting, two parts each in two rows) shows four loaded parts.
- **ParallelStation** has a Capacity of four parts by default. The standard setting distributes these parts across the animation area. Increase the Capacity in the X-Dimension (for example to three parts) or the length of the animation area to redistribute the parts evenly.
- **PlaceBuffer** has a Capacity of four parts by default:
  - If the Animation Area is active, the PlaceBuffer uses it. The index of the MU is the index of the area in the Y-direction; the capacity in the X-direction is always 1.
  - If a MU animation path named `Default` with more than one anchor point exists, the index of the MU is converted to a relative position; Plant Simulation evenly distributes the MUs on this line.
  - Otherwise the PlaceBuffer uses the first path for the first MU, the second path for the second MU, etc. If no suitable path exists but a path named `Default` consisting of a single point exists, the PlaceBuffer uses that path.
- **Store** (standard setting, three parts each in three rows) shows nine parts that fit the individual storage compartments. You can change the dimensions of the individual storage compartments and the Capacity of the Store in the Z-Dimension to stack several parts in the individual compartments. The storage area is placed on the XZ plane.
- **Transporter** with the standard settings (Store and Animation Area, three parts each in two rows) shows six loaded parts.
  - The Transporter with an active loading space of type Line uses the animation path named `Line`.
  - The Transporter with a passive loading space of type Track uses the animation path named `Track`.
- **Worker** has a Capacity of one part in the X-Dimension and in the Z-Dimension by default. To carry two stacked parts, type `2` as Z-Dimension. To carry two parts in each hand, type `2` as X-Dimension and clear **Animation Area**; the Worker then uses the defined Animation Paths.

## MU Animation on Animation Paths on the Workplace

The Workplace provides a single MU animation path named `Queue` by default. Plant Simulation animates Workers waiting in front of a Workplace they cannot enter on this animation path, which visualizes the queue.

> **Note:** If a Workplace does not provide a MU animation path named `Queue`, all Workers wait at the same position until they can enter the Workplace.

- Set the **Distance in Queue** in the dialog of the Workplace.
- Click **Show** to show the MU animation path. The path tool (the pyramid) shows where the Worker is going to be animated; you can click it and move it with the arrow keys.
- You can also define a path of type Polycurve, Spline, or Rotation path. Before doing so, rename the original predefined path named `Queue` (for example to `MyQueue`), then create a new path of the desired type named `Queue`.
- To use the default path again, rename your path and change the name of the original path back to `Queue`.
- To animate the Worker on an animation area, select the check box **Animation Area** and define the settings.

If you do not use an animation area: Plant Simulation animates the first Worker on the first animation path, the second Worker on the second animation path, and the third Worker on the third animation path. You have to define these animation paths yourself. If no third path exists for the third Worker, Plant Simulation uses the default animation path. If no default animation path exists, Plant Simulation does not animate the Worker at all.

In most cases an animation path is the suitable way to animate the Workers on the Workplace, but you can also animate the Workers on an animation area if your modeling situation requires it.

# Modeling Joints and Poses

In the sample model, realistic kinematics are modeled with joints and poses. The respective settings are on the tabs **Joint** and **Poses** in the dialog **Edit 3D Properties**.

You can use poses to animate the object itself. As opposed to normal self animation, with poses you only have to set the place to which the animation is to move. Plant Simulation knows the previous position and internally creates self animations that ensure a smooth transition from the previous to the new state.

In the sample model: the Source produces parts, the Conveyor transports the part to the processing station which processes it. A revolute joint rotates the ToolHead to the right and left, and a prismatic joint moves the ToolHolder up and down. The Station then passes the part on to the Drain, which removes it from the installation.

The demonstration covers how to:
- Configure the Simulation Objects
- Create the Animation Objects
- Configure the Joints
- Configure the Poses

The sample model Factory 51 on the Start Page shows additional usages for revolute and prismatic joints.

## Configure the Simulation Objects

- **Source** — entered a constant Time of Creation of 10 seconds; otherwise default settings.
- **Conveyor** — entered a Capacity of 1 so that it only transports a single part; otherwise default settings.
- **Station** — entered a Processing Time of 20 seconds and a Recovery Time of 5 seconds; otherwise default settings.
- **Drain** — default settings.

## Create the Animation Objects

When the part is located on the machine, the ToolHead rotates to the right and the ToolHolder moves up. Then ToolHead and ToolHolder remain at their new position while the Processing Time passes. After that, they both return to their original pose.

Proceed as follows to create the animation object of the machine:

1. Click the Station with the right mouse button and open it in a new window.
2. Click the part of the graphic called `default.tool` with the right mouse button.
3. Select **Make Animatable Object**. Type `ToolHead` as the Name. Click **OK**.

> **Note:** The **Object Position** sets the origin of the rotation around which the tool head is rotated. If the object does not rotate as expected, check the values for the individual axes of the origin of the rotation.

4. Then set the joint settings on the Tab Joint (described in the next topic).
5. Click the ToolHead with the right mouse button and open it in a new window.
6. Click the ToolHead with the left mouse button. Press the **+** key (the square part with the telescopic holder) to select the ToolHolder. Click it with the right mouse button and select **Make Animatable Object**, then enter the Name. During the simulation the ToolHolder moves up and down.

## Configure the Joints

Equip the ToolHead with a Revolute Joint and the ToolHolder with a Prismatic Joint.

- Click the ToolHead with the right mouse button and select **Edit 3D Properties**. Change to the **Tab Joint** and select the Joint Settings for the Revolute Joint.
- Click the ToolHolder with the left mouse button and press the **Spacebar**. Change to the tab Joint. As the ToolHolder is to move up in the z-direction, click the button next to **Z** to set the z-direction as the Translation Direction, then select the Joint Settings.

## Configure the Poses

On the **Tab Poses**:

1. Click into the background of the window of the Station with the right mouse button. Add `Pose1` and `Pose2`.
2. Click `Pose1` with the left mouse button and click **Edit**. The dialog shows the settings selected on the tab Joint.
3. Click `Pose2` with the left mouse button and click **Edit**. The dialog shows the settings selected on the tab Joint.
4. Now that joints and poses are configured, program the movements in the respective controls. Return to the simulation object and change to the tab **Controls**, where you create an **Entrance Control** and an **Exit Control**.

Within the controls, define to which poses the ToolHead and the ToolHolder move.

For the Entrance Control:

```
?._3D.Poses.moveTo("Pose2") // moves to Pose2
```

For the Exit Control:

```
wait ?._3D.Poses.moveTo("Pose1") // returns to Pose1
@.move                           // and moves the part
```

When the simulation starts, you can watch the ToolHead rotate and the ToolHolder move up and then down again. To better view the sequence, select the Real time factor x 3.

### Showing and hiding poses

You can show and hide poses with the toggle button. Plant Simulation only shows a single pose at a time. If you show a different pose, Plant Simulation first hides the pose that is already shown, then moves the object to the state that corresponds to the pose.

While the pose is shown and the dialog is open, you can change the state of the pose stepwise by clicking the left or right arrow key:

- Rotate the pose by 1° of the range from the joint settings if both limits are defined.
- Move the pose by 0.1 m if at least one limit is missing when a Prismatic Joint is selected.
- Rotate the pose by 1° if at least one limit is missing when a Revolute Joint is selected.

The left arrow key moves the pose toward the lower limit; the right arrow key moves the pose toward the upper limit, independent of rotation axis or translation direction.
