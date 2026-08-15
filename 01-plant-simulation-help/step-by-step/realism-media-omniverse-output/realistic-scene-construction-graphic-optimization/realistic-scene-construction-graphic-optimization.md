# Realistic Scene Construction & Graphic Optimization

> Source: Plant Simulation Help (10-1119 – 10-1149). Unpublished work. © 2026 Siemens.

This guide explains how to create a visually pleasing, realistic-looking simulation model in Plant Simulation, covering factory walls and passageways, gates, text and display boards, JT layout files, point clouds, imported JT graphics, and graphic optimization.

The example model **Factory 51** (available from the Start Page under *Example Models*) demonstrates these techniques.

---

## 1. Creating a Realistic Looking Model

You can make a realistic-looking model by:

- Inserting Factory Walls and Creating Passageways
- Adding Text and Display Boards
- Adding a JT Layout File to Your Simulation Model
- Adding a Point Cloud
- Importing JT Graphics Representing an Object

Video: https://youtu.be/wfVN-mcWNsc?si=LepG6cgh0MDLKilQ&t=22

### Enhance the Visualization in Omniverse

Use the **Omniverse Connector** to create a good-looking visualization of your simulation model in Omniverse:

- https://support.sw.siemens.com/en-US/okba/KB000179528_EN_US
- https://support.sw.siemens.com/en-US/knowledge-base/KB000179496_EN_US

---

## 2. Insert Factory Walls and Create Passageways

In the sample model, four factory walls are created around a conveyor.

**Procedure:**

1. Click the **Edit** ribbon tab in 3D, then **Edit > Insert Shape > Factory Walls**.
2. Select the settings for the walls.
3. The model shows the walls around the conveyor.

Next, cut a passageway through the wall between the Station and the Conveyor so the conveyor can extend through it. This covers:

- Cutting an Open Passageway in a Wall
- Creating a Passageway and a Gate

### Cut an Open Passageway in a Wall

**Procedure:**

1. Click the mouse at the position in the factory wall where you want to cut the passageway.
2. Press the **+** key until only the segment you want to cut is selected.
3. Press **Del** to delete the segment (the graphic). Confirm the message box with **Yes**.
4. Add a **lintel** (a Cube, or a Textured Plate) so the passageway is not open at the top.

Because the Cube's Thickness cannot be changed after insertion, note the factory wall's **Thickness** value first (0.3 meters in the example) and match the cube's Width to it.

**Lintel steps:**

- Click the Cube, set its Width to 0.3 meters (matching the wall Thickness). Click **Create**, drag to the passageway position, and click to insert.
- Change to **Planning View** and place the lintel roughly with the arrow keys.
- Right-click the lintel, select **Show 3D Properties**, click in the **X-Position** text box, and roll the mouse wheel until the position looks correct.
- Deactivate Planning View and adjust the **Z-Position** the same way.
- Match the lintel material to the walls: open **Factory Wall Settings > Wall Material**, copy the material, then paste it in the lintel's 3D properties on the **Material** tab.
- Extend the conveyor so it goes through the passageway.
- Optionally raise the lintel by changing the **Scaling** in the Z dimension.

### Create a Passageway and a Gate

A passageway can be covered by a PVC strip curtain for through traffic. Here a gate is created that opens automatically when a part approaches and closes once the part is out. This is modeled with a plate that moves up and down.

**Procedure:**

1. Cut the selected segment out of the factory wall (as described above).
2. Insert a pillar (cuboid) left and right of the passageway, plus a lintel resting on the pillars.
3. Fine-tune positions on the **Transformation** tab — click in the text box, hold **Ctrl**, and roll the mouse wheel.

The gate can then be controlled in several ways:

- Open and Close the Gate with Poses
- Open and Close the Gate without Poses
- Move the Gate Up to the Height of the Part

#### Open and Close the Gate with Poses

Model opening/closing the gate using a joint and two poses, plus three controls.

**Procedure:**

1. Create the gate graphic (a flattened cuboid) and position it between the pillars.
2. Color the gate so it stands out from the wall.
3. Insert a Conveyor between the Station (inside) and the Drain (outside). A spiral conveyor overcomes the 1-meter height difference.
4. Make the gate an animatable object: right-click the gate, select **Make Animatable Object**, click **OK**.
5. On the **Tab Joint**, set a **Prismatic Joint** that starts at 0 meters and moves up to 2 meters.
6. In the background Frame named `FactoryWalls`, select **Edit 3D Properties**, go to the **Tab Poses**, and add two poses:
   - `GateUp` — moves the gate up to 2 meters.
   - `GateDown` — moves the gate back to 0 meters.
7. Control the timing in the Entrance Control and Exit Control of the conveyor.

**Entrance Control:**

```simtalk
self.~.EntranceLocked := true
_3D.Poses.moveTo("GateUp")
self.~.ExitLocked := false
```

**Exit Control:**

```simtalk
self.~.ExitLocked := true
wait _3D.Poses.moveTo("GateDown")
@.move
self.~.EntranceLocked := false
```

**Init (user-defined attribute)** — ensures the exit is closed and the entrance open when the model resets:

```simtalk
self.~.ExitLocked := true
self.~.EntranceLocked := false
```

When the simulation runs, the gate moves up as a part approaches, stays up until the part has passed, then moves down.

#### Open and Close the Gate without Poses

Use the method `moveTo` instead of poses. The gate still moves 2 meters up, stops, and returns to 0 meters after the part passes.

**Entrance Control:**

```simtalk
self.~.EntranceLocked := true
wait _3D.getObject("Gate").moveTo(2) // gate moves 2 meters up
// wait _3D.Poses.moveTo("GateUp")
self.~.ExitLocked := false
```

**Exit Control:**

```simtalk
self.~.ExitLocked := true
wait _3D.getObject("Gate").moveTo(0) // moves the gate back to initial position
// wait _3D.Poses.moveTo("GateDown")
@.move
self.~.EntranceLocked := false
```

The Init Control source code is unchanged.

#### Move the Gate Up to the Height of the Part

Move the gate only as high as the part itself (plus clearance).

**Entrance Control:**

```simtalk
self.~.EntranceLocked := true
wait _3D.getObject("Gate").moveTo(@.MUHeight+0.1m)
// moves the gate up to the height of the part
// plus 10 cm for the height of the conveyor
wait _3D.Poses.moveTo("GateUp")
self.~.ExitLocked := false
```

**Exit Control:**

```simtalk
self.~.ExitLocked := true
wait _3D.getObject("Gate").moveTo(0.1m)
// moves the gate back to the initial position
wait _3D.Poses.moveTo("GateDown")
@.move
self.~.EntranceLocked := false
```

**Init Control:**

```simtalk
self.~.ExitLocked := true
self.~.EntranceLocked := false
_3D.getObject("Gate").moveTo(0.1m, 0) 
// 0 means that the target position becomes 
// active immediately without moving there
```

---

## 3. Adding Text and Display Boards

- For **static text** that never changes: insert **3D Text** (`Edit > Insert Shape`), or import a JT file created e.g. in NX (the "Plant Simulation" lettering in Factory 51 is done this way).
- For an **editable display board**: use the **Comment** object from the *User Interface* toolbar.

### Show Text

**Procedure:**

1. Click **Text** under **Edit > Insert Shape**.
2. Type the text and select settings in the dialog. Click **Create**.
3. Drag to a position and click the left mouse button — the text is inserted flat on the floor (initially far too small).

To fix the scale:

- Right-click the text, select **Edit 3D Properties**.
- Use **Uniform Scaling** with a factor of 3 (example).
- Rotate 45 degrees around the X axis.
- Move up on the Z axis until the lower border sits flat on the floor.

### Show a Display Board

**Procedure:**

1. Click the **Comment** object on the *User Interface* toolbar and insert it into the model.
2. Double-click the Comment and type the text (e.g. "My factory in Crailsheim, Baden-Württemberg, Germany"), selecting **Font Size > Extra Large**. Click **OK**.
3. To orient it to the factory floor above the hall's upper border: right-click, **Edit 3D Properties**, rotate 45 degrees around the X axis, and move up on the Z axis.

---

## 4. Add a JT Layout File to Your Simulation Model

A layout graphic adds a realistic touch.

**Procedure:**

1. Drag the layout graphic (e.g. `Layout_Factory_Training.jt`) from Windows Explorer into the open Frame window. Plant Simulation attaches the graphic to the mouse pointer and opens the **Insert Graphic** dialog — accept defaults and click **OK**.
2. Drag to the upper-left corner of the Frame (coordinates 0, 0) and click to place it.

You can then continue inserting objects and manipulating them. Instead of a JT-layout file, you can also use a point cloud as the background.

---

## 5. Add a Point Cloud

A point cloud is a set of 3D data points defined by their X-, Y-, and Z-coordinates. Use it to visualize your actual factory layout and arrange machines on it realistically.

**Procedure:**

1. Click into the background of the model and select **Edit 3D Properties**, then the **Tab Point Cloud**.
2. Click the button and select the point database file (`*.pod`). A relative path refers to the folder of the simulation model.
3. To remove the point cloud, delete its name from the text box.
4. Click **OK** or **Apply** to show the point cloud.

**Notes:**

- Initially only small parts of the point cloud may show; rotating the view reveals additional parts.
- Loading is significantly faster if the point cloud file is on an **SSD**.
- Toggle visibility with **Show Point Clouds** on the *View* ribbon tab.
- Adjust position/orientation via **Edit 3D Properties > Tab Point Cloud** (Position and Rotation Angle).
- **Show Point Clouds is deactivated by default** for performance; re-enable it after reopening the model.

---

## 6. Import JT Graphics Representing an Object

Instead of creating shapes in 3D, import graphics to represent objects. Example: building a dune buggy from JT graphics received from a colleague.

**Procedure:**

1. Duplicate the part `.MUs.Part` in the Class Library and rename it (e.g. `DuneBuggy`). Add graphic groups for the components on the **Tab Graphics**.
2. Import JT graphics into the matching graphic groups. Import `Body.jt` and `Seats.jt` into all graphic groups whose names start with `Body` or `Seats`.
   - Go to the 3D ribbon tab **Edit**, click **Import Graphics**, navigate to the folder, and click **Open**.
   - Drag the JT graphic roughly to the desired position in the Frame (`.MUs.DuneBuggy`) and click. Select the target graphic group.
   - Repeat for all JT files.
3. Arrange the components with the arrow keys and the **Edit 3D Properties** dialog.
   - Place the three body panels at exactly the same position; do the same for the three seat assemblies. This lets you show/hide panels and seats to test color combinations.
4. To change a graphic's color: right-click the background of `.MUs.DuneBuggy`, select **Show Graphic Structure**.
   - Expand the graphic group (e.g. `BodyRed`).
   - Find the node ending in `-M` (designates a material).
   - Right-click that node (e.g. `1-JtGroup-M`) and select **Edit 3D Properties**. Experiment with material colors to fine-tune glossy effects.

---

## 7. Optimizing a Graphic

Optimizing a graphic — i.e. flattening the hierarchy of an object — deletes unnecessary information, allowing faster rendering and quicker display.

Imported graphics are usually designed for a different purpose (e.g. manufacturing an engine with every detail). For simulation users, speed and smooth animation matter more than those details.

> **Advice:** Optimize every graphic you import. Do this as soon as possible, but **not before** extracting all structural information you need (e.g. when creating a simulation object with animation).

**Prerequisite:** First make the graphic an animatable object (**Make Animatable Object**).

**Procedure:**

1. Click the animatable object whose graphic you want to optimize in the scene window.
2. Click **Optimize Selected Graphic** on the *Edit* ribbon tab of the 3D window.
3. Experiment with the settings:
   - **Step 1: Prune Tiny Graphics**
   - **Step 2: Flatten Structure**
   - **Step 3: Visibility Filter**

**Notes:**

- Click **Show External Graphic Group** on the *View* ribbon tab to display the external graphics of the open 3D object.
- Under **Graphic Complexity**, Plant Simulation shows two characteristics: the number of **nodes** and the number of **polygons**. The optimization strategies mainly affect these two values.
