# Working with Objects in the Frame

This document summarizes the Plant Simulation help topic **"Working with Objects in the Frame"** — how to insert, select, move, rotate, scale, and edit objects in the 3D scene, with particular focus on length-oriented objects and precise transformation editing.

---

## Overview

Plant Simulation provides several ways to work with objects in the 3D scene:

- Insert Objects into the Scene
- Select Objects
- Simultaneously Paste Multiple Copies
- Connect Objects with the Connector
- Move an Object With Keyboard Keys / With the Mouse
- Rotate Objects in the Frame
- Scale Objects in the Frame
- Edit Grouped Graphics
- Set the Material of a Graphic
- Use a Different Graphic for an Object
- Add a JT Layout File to Your Simulation Model
- Work with Length-oriented Objects
- Set the Capacity of a Material Flow Object
- Set How Plant Simulation Shows an Object
- Adapt the 3D Model to the 2D Model
- Create Your Own Objects

---

## Insert Objects into the Scene

Objects can be inserted from the **Toolbox** or the **Class Library** (both contain the same objects by default).

- **Toolbox:** click the object with the left mouse button and drag to the 3D window position, then click to insert. Cancel with right-click or `Esc`.
- **Class Library:** click, hold, drag to the position, and release the mouse button. A preview is shown while the button is held. Cancel by releasing outside the 3D window.
- **Pasted copy:** copy with `Home > Copy` or `Ctrl+C`, then press `Ctrl+V` in the 3D window. The copy is pasted at the same position the copied object occupies within its location.

**Snapping:** click the snap button on the Edit ribbon tab to snap the object to the closest grid-line intersection. Leave it off to place the object freely (according to grid/object alignment settings).

> **Note:** When inserting Markers, keep them aligned to avoid unnecessary roundings. Misaligned Markers can occur if inserted while *Show Grid* is off.

Fine-tune location in the **3D Properties** dialog (opened from the Home ribbon tab). Open the simulation object's dialog via the button in the bottom-left corner of 3D Properties, or by double-clicking the object.

**Inserting multiple copies of the same object:** hold `Ctrl` and select the object in the Toolbox — it remains selected after inserting, so you can insert several one after another. Exit with right-click or `Esc`.

After inserting, you can align to grid, snap to grid, snap to objects, or arrange on the grid (requires *Show Grid* to be on).

---

## Select Objects

Click an object with the left mouse button to select it. Selection color indicates the element type:

- **Simulation object** (directly in the opened object) — green
- **Animatable object** (belongs to the simulation object) — purple
- **Graphic** (visualizes the simulation object) — yellow-green
- **Displayed manipulator**

Selection techniques:

- Hold `Shift` or `Ctrl` and click to select multiple items.
- Drag a marquee around objects:
  - Without `Shift`/`Ctrl`: cancels the existing selection.
  - With `Shift`/`Ctrl`: adds to the existing selection.
- `Ctrl+A` selects all objects in the scene.
- Use `+` and `-` keys to modify the selection.
- Hold `Shift` and click objects one after another to record the selection sequence (used, e.g., for the statistics report order).

---

## Simultaneously Paste Multiple Copies

Paste more than one copy of a copied object (e.g., create a Store with several shelves):

1. Insert the object (e.g., a Station) into the scene.
2. Select it and copy with `Ctrl+C`.
3. Click `Paste > Multiple Paste` on the Home ribbon tab.
4. Enter the number of copies in the **Count** combo box.
5. Enter the **Offset** from the original object.

> Example: a Station 2.0 meters wide with an offset of 2.0 m on the X-axis pastes 4 copies toward the right. There is an initial predefined offset (right and downwards) to prevent pasting copies on top of each other.

Click **Paste**. If needed, move the pasted copies afterward.

---

## Move Objects in the Frame

Ways to move an object: with the mouse, with keyboard keys, or precisely.

### Move an Object With the Mouse

- Drag with the left mouse button to move freely on the grid plane (or view plane when the grid is hidden).
- Hold `Alt`/`Alt Gr` + left mouse button and drag to move vertically up/down.

> **Note:** In a Frame with visible content, pressing `Alt`/`Alt Gr` before clicking selects simulation objects within the Frame; holding it down still moves the selected object vertically. If the keyboard has no `Alt Gr` key, use `Ctrl-right + Alt-right`.

### Move an Object With Keyboard Keys

Use `Ctrl` or `Shift` plus arrow keys:

- Arrow key alone: move by **10%** of the grid snapping distance.
- `Shift` + arrow key: move by the full grid snapping distance.
- `Ctrl` + Up/Down arrow: move vertically in the z-direction (10% step; `Shift+Ctrl` for full step).
- `Ctrl` + Left/Right arrow: rotate counterclockwise/clockwise by 1°.
- `Shift+Ctrl` + Left/Right arrow: rotate by 45°.

### Move an Object Precisely

Enter exact values in **3D Properties > Tab Transformation**:

1. Select the object.
2. Press the spacebar (or the Home ribbon tab button) and click the **Transformation** tab.
3. Click a text box and roll the mouse wheel to adjust in 0.1 m steps; hold `Shift` while rolling for 1 m steps.
4. Click **Apply** to preview, then **OK** when satisfied.

---

## Rotate Objects in the Scene

### Rotate an Object with Keyboard Keys

Keyboard rotation uses the settings under **3D Properties > Transformation > Settings for the Rotation**.

- `Ctrl` + Left/Right arrow: rotate 1° left/right.
- `Ctrl+Shift` + Left/Right arrow: rotate 45° left/right.
- Numeric keypad: `7`/`8` = 10° on x-axis, `4`/`5` = 10° on y-axis, `1`/`2` = 10° on z-axis.

To define rotation settings: select **3D Properties > Transformation > Settings for the Rotation**, and either click an axis button or enter x/y/z components of an arbitrary rotation axis. Click **Apply** to activate.

### Rotate an Object Precisely

Enter exact values in **3D Properties > Tab Transformation**:

1. Select the object.
2. Press spacebar or click the Home ribbon tab button.
3. Enter the x/y/z components of the rotation axis.
4. Enter the rotation offset to the object center for x/y/z (defaults `0, 0, 0` rotate around the center).
5. Enter the rotation angle in degrees.
6. Click **Apply**.

> **Note:** Transformations (move/rotate/scale) in one 3D window are not immediately updated in other 3D windows — only after you deselect the changed object.

---

## Scale Objects in the Frame

Type exact values in **3D Properties > Tab Transformation > Scale**:

1. Select the object and press spacebar (or the Home ribbon tab button).
2. **Uniform:** scale all three dimensions by the same factor (entering a value in one box auto-fills the others, avoiding distortion).
3. Enter values for x/y/z axes (e.g., `0.5` halves size, `2` doubles it). Only non-zero values are allowed.
4. **Clear Uniform** to scale each dimension with different factors (distorts the object).
5. **Set Dimensions:** type in the physical size of the scaled object.

---

## Work with Length-oriented Objects

Length-oriented objects use their length and dimensions during simulation. These are the **Conveyor, Track, TwoLaneTrack, Footpath, Container, Transporter, and Pipe**. Plant Simulation also auto-generates graphics for the **Turnplate, Turntable, Converter, AngularConverter, and Store**.

To create a class from a Conveyor, Turntable, Track, TwoLaneTrack, or FootPath, model it in the Frame and drag it to the Class Library.

Topics covered:

- Insert Curved and Straight Segments
- Auto-connect Length-oriented Objects
- Draw Straight and Curved Segments with a 90° Angle
- Draw Straight and Curved Segments without Fixed Values
- Change the Shape of a Segment
- Create a Curved Object with SimTalk Commands
- Reuse the Segments of a Length-oriented Object
- Keyboard Shortcuts
- Edit Length-oriented Objects with Mouse / Keyboard Keys / Precisely
- Model Differences in Height Between Conveying Elements
- Model a Spiral Conveyor

### Insert Curved and Straight Segments

1. Zoom the Frame to accommodate the object.
2. Click the length-oriented object in the Toolbox and drag to the Frame; click the start point (opens **Edit Parameters of Curve**).
3. Draw a **straight segment**: click a second time at the end position.
4. Draw a **curved segment**: hold `Ctrl`, drag the mouse, and click once to set the curve.
5. Release `Ctrl` and click to draw the next straight segment.
6. Click an existing end segment to start a new connected sequence (Plant Simulation connects them automatically; hold `Alt` to prevent this).
7. Right-click or click **Finish** to exit Insert mode; press `Esc` or click **Abort** to terminate without inserting; click **Delete Last Point** to remove the last anchor point.

**Fixed values** (type into the dialog and check the *fixed* box):

- Line segment: **Line Length** and **Tangential Angle** (relative to previous segment).
- Curved segment: **Arc Length**, **Radius**, and **Curve Angle** (positive = clockwise, negative = counterclockwise; 360° auto-connects end to start).
- Both segment types: **Anchor Point Height** (height/distance from floor to the next anchor point — useful for ramps).

> When the grid is active, points are placed on grid points where possible; fixed values take precedence. A non-grid-fitting value (e.g., radius 2.5 m) causes a non-tangential transition.

> When inserting a straight segment after a curved segment, Plant Simulation always enforces a tangential angle of 0°.

**Start tangential angle rules:**

- After clicking an existing object, the angle from the previous object is applied (also applies to icons).
- For a straight segment on an existing object, Plant Simulation uses the object's angle or ±90° depending on mouse position.
- For a curved segment without clicking an existing object, a typed angle is used for straight segments; with `Ctrl` held, 0/±90/180° is used depending on mouse position.

The extrusion path initially consists only of the starting point (insertion point or end point of the picked object). Insert straight segments with left-click, curved segments with `Shift`+left-click. A length-oriented object is not inserted if it has fewer than two segments/points after finishing.

### Auto-connect Length-oriented Objects

When you click another object as the successor of a length-oriented object, Plant Simulation attempts to bridge the gap with additional straight/curved segments so the connection is tangential.

- Direction is determined by the last/first segment (length-oriented), the X-axis of a point-oriented object, or the X-axis of the scene.
- Height differences in the last segment are automatically corrected.

Gap-closing conditions:

- Curve Angle fixed to 90° and Radius fixed.
- Objects aligned parallel or perpendicular.
- Gap closable with at most two right-angled curve segments.
- Objects not rotated around any axis other than the z-axis.

Supported cases (objects need not be grid-aligned):

- Objects aligned and pointing the same direction.
- Objects parallel and pointing the same direction (tangential and vertical distance ≥ double radius).
- Objects parallel, pointing opposite directions (vertical distance ≥ double radius).
- Objects at a right angle to each other (tangential and vertical distance ≥ radius).

If the gap cannot be closed, Plant Simulation suggests a straight line to the successor (unless `Ctrl` is held). You can accept it (click the successor) or manually define separate tangential segments.

### Draw Straight and Curved Segments with a 90° Angle

1. Click the Conveyor icon in the Toolbox.
2. Drag to the Frame and click to set the starting point.
3. In **Edit Parameters of Curve**, defaults for a 90° curve are set (fixed tangential angle 0°, fixed curve angle 90°, fixed radius 2 m). You can type a different radius.
4. Draw the curve: hold `Ctrl`, drag downward, click once.
5. For a curve pointing left: keep *Fixed* for curve angle activated and type `90`, then drag and click.
6. Release `Ctrl` and click for the next straight segment.
7. Right-click to exit Insert mode.

> Plant Simulation saves the last set of dialog settings for reuse.

For tangential transitions when snap causes misalignment, either deactivate Snap to Grid by holding `Alt` when clicking, or type a fixed tangential angle of 0° for that segment.

To draw a curved segment **without** fixed values, click the left mouse button three times (holding `Ctrl` on the first click to activate curve mode): first click sets start, second sets radius, third sets arc length/curve angle.

### Draw Straight and Curved Segments without Fixed Values

**Straight segment:**
1. Click once to set the start point (a Connector icon attaches to the cursor; text boxes show live values).
2. Drag in the desired direction and click to set the first anchor point.
3. Continue until the object has the desired length/shape.
4. Right-click to set the end point and exit Insert mode.

**Curved segment:**
1. Hold `Ctrl` and click once to set the start point.
2. Drag to set the Tangential Angle.
3. Continue dragging and click to set the Radius.
4. Continue dragging and click to set the Arc Length.
5. Right-click to set the end point.
6. Use **Delete Last Point** in the dialog to remove the last anchor point.

### Change the Shape of a Segment

- Change a straight segment shape: click **Show Manipulators** and drag the manipulators.
- Delete an anchor point: right-click it and select **Delete Anchor Point**.
- Extend a curved segment without adding an anchor point: drag the drag point.
- Append anchor points: right-click the curve and select **Segments > Append [segment]**.
- Edit/insert segments: select **Segments > Edit [segment]** to open the **Segments Table** (also allows inserting a segment at the beginning, which is not possible with the mouse). Example: insert a curved segment at the start of a Pipe so it attaches seamlessly to a FluidSource (press `F7` to open the Segments table, insert a row).
- Change direction (e.g., right to left): edit the **Curve angle** in the Segments table.
- Replace a right angle with a curve: insert a row in the Segments table and type the curve values (can copy from a template object).
- Reverse direction of motion: right-click the object and select **Reverse [segment]**.
- Split the object into separate segments: click a point and select **Split Up [segment]**.
- Move the whole object: click and drag, or use arrow keys (one pixel; `Shift`+arrow = one grid unit).
- Delete the whole object: click once and press `Delete`.
- Extend without a new anchor point: grab the handle and drag.
- Link two length-oriented objects: insert a **Connector** between them.
- Connect a new straight object to an existing one: click the end of the first, move to the beginning of the second, and click.

### Create a Curved Object with SimTalk Commands

Use the methods `derive` and `duplicate`:

```simtalk
var obj := .Materialflow.Conveyor.derive(.Models.Frame)
obj.Coordinate3D := [5, 5, 0]
var obj1 := .Materialflow.Conveyor.derive(.Models.Frame)
obj1.Coordinate3D := [1, 1, 0]
```

See also the methods `getCurveSegments` and `setCurveSegments` (below).

### Reuse the Segments of a Length-oriented Object

For small segments tables, open two models and copy/paste the values directly between the tables (right-click a row index and select **Append Row** to add rows).

**Export the segments table** (write coordinates into a Variable with a Method using `getCurveSegments`):

```simtalk
Conveyor.getCurveSegments(MySegmentsVariable)
```

**Import the segments table** (overwrite a Conveyor's settings with `setCurveSegments`):

```simtalk
Conveyor.setCurveSegments(MySegmentsVariable)
```

To reuse settings in another simulation model, insert a DataTable and save the segments table as an object file (`.psobj`), then import it into a DataTable in the other model.

### Keyboard Shortcuts for Inserting Straight and Curved Segments

| Action | Press/click |
| --- | --- |
| Set start of a straight segment | Left mouse button |
| Set start of a curved segment | `Ctrl` + left mouse button |
| Deactivate Snap To Grid | `Alt` + left mouse button |
| Deactivate Snap To Grid for the last point | `Alt` + right mouse button |
| Draw straight segment horizontally/vertically and deactivate Snap To Grid | `Shift` + left mouse button |
| Terminate Insert mode | Right mouse button |
| Insert a new curved object of the same class | `Ctrl` + right mouse button, then left mouse button |
| Draw last straight segment horizontally/vertically and deactivate Snap To Grid | `Shift` + right mouse button |
| Deactivate default settings | `Shift` + `Alt` |
| Insert icon against default values | `Shift` + first left click |
| Open the dialog Sensor | `Alt` + double-click red Sensor line |
| 3D: insert ascending curve | Up key, then left mouse button |
| 3D: insert descending curve | Down key, then left mouse button |

### Edit Length-oriented Objects with the Mouse

Click **Show Manipulators** on the Edit ribbon tab to show all manipulators, then click and drag a manipulator to a new position.

- Manipulator appearance differs per object; for length-oriented objects, the start/end manipulators are "cut off" (two attached objects form a complete manipulator).
- A tooltip appears when hovering over a manipulator.

Examples:

- Select an anchor point and drag to shorten a segment.
- Select an anchor point, hold `Ctrl`, and press the Up arrow to raise a segment (repeat to move step-by-step — allows workers/forklifts to pass underneath).
- Drag the top-right corner of a Store to resize its graphic (reflected in width/depth and animation area).
- Use the rotation manipulator to rotate the Store around its center.

### Edit Length-oriented Objects with Keyboard Keys

**Manipulators:** `Page Up` lengthens and `Page Down` shortens the selected manipulator.

- Select the **first** manipulator and press `Page Up`: lengthens the neighboring linear segment, increases the curve angle for a horizontal curved segment (no effect on vertical curves).
- Select the **last** manipulator and press `Page Up`: shortens the neighboring segment, decreases the curve angle for a horizontal curved segment.
- Select the **first** manipulator and press `Page Down`: shortens the segment, decreases the curve angle for horizontal curves.
- Select the **last** manipulator and press `Page Down`: lengthens the segment, increases the curve angle for horizontal curves.

**Sensors:** `Page Up` (or left arrow) moves a sensor left; `Page Down` (or right arrow) moves it right.

### Edit Length-oriented Objects Precisely

1. Select the object.
2. Press spacebar or click the Home ribbon tab button, then click the **Transformation** tab.
3. Edit position, rotation, and scaling values.
4. Click **Apply**.
5. Edit additional settings on the **Appearance** tab if needed.

### Model Differences in Height Between Conveying Elements

**Straight ascending/descending slopes:**
1. Insert the length-oriented object (e.g., a 4 m Conveyor) and click **Show Manipulators**.
2. Click the right manipulator with the right mouse button, hold `Ctrl`, and press the Up arrow until the side reaches the required height.
3. To append a segment, right-click the Conveyor and select **Segments > Append**; type radius/angle in **Line/Arc Parameters**, click in the scene, and click **Finish**.

**Curved ascending/descending slopes:**
1. Insert the length-oriented object (e.g., a Conveyor).
2. Press the Up arrow to insert an ascending curve (upward in z) or Down arrow for a descending curve.
3. Type the Radius and Angle in **Line/Arc Parameters** (maximum curve angle is 90°).
4. Click in the scene to insert, then click **Finish**.

The Segments dialog shows a checked box indicating the Conveyor contains a vertical curve.

### Model a Spiral Conveyor

1. Click the Conveyor on the MaterialFlow tab of the Toolbox and drag to insert it.
2. Use standard settings in **Line/Arc Parameters** (enter a greater radius for a wider arc).
3. Hold `Ctrl` and click several times to insert arc segments (initially placed on a single layer, directly above each other). Example: straight segment, 13 arc segments, then a straight segment.
4. Press `F7` to open the Segments table.
5. Enter the additional offset to the base height of the preceding segment into the cell **ΔZ** (e.g., 0.5 m).
6. Click OK.

Change spiral settings on the **Appearance** tab.

---

## Setting the Capacity of a Material Flow Object

- **Capacity** (number of parts for ParallelStation, Sorter, Store, Transporter, Container) is set in two dimensions on the **Attributes** tab (X-Dimension and Y-Dimension).
- **Animation area** (3D placement of parts) is set via **Edit 3D Properties > MU Animation > Area > Animation Area** for objects with matrix loading space (Store type: ParallelStation, Sorter, Store, Transporter, Container), PlaceBuffer, and Worker.

### Define the Animation Area of a Simulation Object

Example: place cylinder-shaped containers in a storage box (bottling plant).

1. Insert two Sources, an AssemblyStation, a Conveyor, a Station, and a Drain; connect them with Connectors.
2. Duplicate `Part` and `Container` in the MUs folder of the Class Library to create custom MU types.
3. Rename the duplicated container to `StorageBox` (F2); open it and use **Exchange Graphics** to select a storage-box graphic (s3D files also contain dimensions and animation data).
4. Configure dimensions in X/Y/Z-Dimension to set capacity.
5. Rename the duplicated part to `Canister`; delete its default graphic and create a custom cylinder graphic (Edit ribbon tab > Cylinder).
6. Define the Canister's length, width, and height.
7. Run the simulation — the AssemblyStation places 12 containers per storage box; the activated animation area distributes them evenly.

Notes on animation area settings:

- **Show/Hide** displays the animation area (red with a red orientation indicator in the center).
- **Orientation > XY plane** distributes containers in the x-y direction.
- Plant Simulation uses 94% of the graphic length and 92% of the width (subtracting the wall thickness), based on the s3D graphic's area settings.
- The Z-position of the center may be auto-set (e.g., 0.05 m for a 5 cm bottom height).

---

## Context Menu of the Background of the Scene

Right-click an empty area in the window to open the context menu. You can leave the mini toolbar open by clicking its border.

Commands include:

- Reset Simulation, Show Structure, Start/Stop Simulation, Start Fast Forward Simulation, Open Location, Open Origin, Open Class
- Show Graphic Structure, Show Inheritance, Show Attributes and Methods, Edit User-defined Attributes, Create User-defined Attribute
- Snap to Grid, Snap to Objects, Lock Structure, Exchange Graphics, Apply Changes (MUs), Paste Contents of the Clipboard / Multiple Paste, Unhide Objects, Find Object
- Previous Scene, View All, Edit 3D Properties, View Options

> Do not confuse the selected object with the selected graphic of the object.

---

## Create User-defined Attribute

Select this command to create a user-defined attribute at the mouse-click position (does not apply to a Frame or folder). The dialog **User-defined Attribute** opens with the last-used Transformation and Display Settings; **Show in 3D** is selected by default. Enter settings and click OK.

---

## Previous Scene

Returns to the previously active hierarchy level or camera mark.

---

## Adapt the 3D Model to the 2D Model

When a 2D model is created while 3D is active and contains a Frame with objects, the 3D view may look unexpected with default settings.

If **Show Content** is active, the Frame's content (e.g., Interfaces and a Station) is shown on the same layer as other material flow objects. To make the 3D model match the 2D model, clear the **Show Content** check box.

---

*Source: Plant Simulation Help — "Working with Objects in the Frame" (10-920 ff.). Unpublished work. © 2026 Siemens.*
