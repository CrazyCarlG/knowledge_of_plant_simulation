# Working with Graphics

Plant Simulation displays objects with graphics, which are structured in one or several graphic groups. Graphic groups of objects and Frames consist of one or more graphics and have a name that is unique for the object, similar to the 2D icons of simulation objects.

A graphic group can be **external** or **internal**:

- **External graphic groups** represent the object toward the outside.
- **Internal graphic groups** decorate the inside of the object.

Which graphic groups are internal or locked, together with the graphic structure, is an object property that can be inherited. A graphic group can be permanently shown or hidden to allow switching between alternative visual representations. Each simulation object or animatable object contains at least one external graphic group named `default`, plus optionally any number of alternative or additional graphic groups that can be shown or hidden independently.

A Frame initially contains one internal graphic group named `deco`. Visibility of graphic groups is an object property that can be inherited independently from the graphic structure and the `internal`/`locked` properties.

Graphic groups are created, deleted, or configured on the **Graphics** tab in the dialog **Edit 3D Properties** and in the dialog **Show Graphic Structure**.

- An eye icon means the graphic group is **visible**.
- A crossed-out eye icon means the graphic group is **not visible, as selected**.

Each graphic of a graphic group can be deleted and edited individually — either with the mouse in a 3D window, or by specifying position, rotation, scaling, or material in the dialog **Edit 3D Properties**.

> **Note:** Changing any graphic or the graphic structure of a class object also changes all inherited objects. Changing the graphics of a derived object only changes that object, because 3D deactivates graphic inheritance if it has not already been deactivated. Deactivating graphic inheritance causes graphics to be duplicated, so make changes in the class object as far as possible.

You can create, replace, or delete the state graphic on the tab **States** in the dialog **Edit 3D Properties** by selecting the orientation of the states: **Horizontal**, **Vertical**, or **Off**. Changing this setting deletes all state graphics and creates new state graphics arranged according to the selection.

---

## Inherit Graphics

Object graphics are object data that can be inherited. Objects that inherit their graphics share the graphics with their parent object and thus preserve memory. Graphic changes in class objects are automatically visible in derived objects whose graphic inheritance is activated.

Graphic changes in derived objects **deactivate graphic inheritance**, after which the derived object contains its own changed copy of the parent graphic and requires additional memory. The following graphic changes deactivate graphic inheritance:

- Adding or deleting graphic groups or graphics.
- Transforming graphics (moving, rotating, zooming).
- Changing the material of graphics.
- Grouping or ungrouping a graphic group.
- Renaming a graphic group.
- Changing the graphic group settings `internal` or `locked`.

Graphic inheritance can be activated or deactivated by:

- Clicking the inheritance check box under **Home > Edit 3D Properties > Graphics > Graphic Groups**.
- Clicking **Inherit Graphic Groups** in the dialog **Show Graphic Structure**.

Turning graphic inheritance on makes the object use its parent's graphics again and cancels changes. Leaving it off keeps the instance's changed graphics and uses more memory.

**See also:** `_3D.InheritGraphics` [SimTalk]

---

## Duplicate Graphics

You can duplicate the graphic selected in the 3D window.

To duplicate the selected graphic, hold down **Ctrl+Shift** and click the left mouse button in the 3D window at a different position.

Plant Simulation does not create a copy; the new graphic **references** the duplicated graphic, considerably reducing memory consumption. A referenced graphic is shown with a diamond in the dialog **Show Graphic Structure**.

---

## Edit Grouped Graphics

You can edit grouped graphics (the graphic group as a whole). To move, rotate, or scale several graphics at the same time while retaining their positions relative to each other, group them and manipulate the group as a whole.

To group several graphics:

- Hold down **Shift** and click the objects, or drag a marquee over them.
- Click **Group Graphics** on the Edit ribbon tab or press **Ctrl+G**. Plant Simulation creates a single new group.
- Move, rotate, scale, or zoom the group as you would a single graphic.
- You can also transform the group on the **Transformation** tab in **Edit 3D Properties**.

To restore the previous structure:

- Select the newly created group.
- Click **Ungroup Group of Graphics** on the Edit ribbon tab or press **Ctrl+U**.

---

## Set the Material of a Graphic

You can define the surface qualities and appearance (material) of a graphic: how well it reflects light, what color it reflects, and what color it emits.

To define the material:

- Select the graphic and click **3D Properties** on the Home ribbon tab.
- Click the **Material** tab.

Options:

- **Material Active** — assign a material to the graphic.
- **Diffuse Color** — reflection of light from an uneven surface; the complement to specular reflection.
- **Ambient Color** — color of light reflected when lit by another ambient object.
- **Specular Color** — reflected color of the object's highlights.
- **Emissive Color** — color emitted by the object (e.g., a lamp shade may have a yellow base color but emit white when on).
- **Transparency** — value between `0.0` (opaque) and `1.0` (completely transparent).
- **Shininess** — value between `0.0` (very dull) and `1.0` (highly polished); sets how sharp light is reflected.

Click **Apply** to apply the material. You can also:

- Copy the current material settings.
- Paste a previously copied material.
- Remove the materials in nested graphics.

> **Note:** If several partially or fully transparent graphics sit one directly behind another from the current viewpoint, some may look wrong or seem missing due to rendering heuristics.

> **Note:** When materials are defined at different levels of the graphic structure, Plant Simulation always uses the material furthest down in the structure for rendering.

---

## Use a Different Graphic for an Object

You may want to replace the default graphics with pictures that resemble the actual machines in your plant, or use actual graphics files from the machine builder.

Graphics shipped with the program are saved in `s3d` format, with animation paths pre-defined for most and objects correctly scaled.

Options:

1. **Exchange the object graphic with another pre-defined object graphic**
   - Select the object, click **Exchange Graphics** on the Edit ribbon tab (or context menu).
   - In the **Exchange Graphics** dialog, navigate to `C:\Program Files\Siemens\Tecnomatix Plant Simulation XX\3D\s3D-graphics` and select an `.s3d` file.
   - Click **Open** to replace all graphic and animation data of the selected object (graphic groups, state graphic, and animation attributes are removed and replaced).
   - You can also drag an `.s3d` file from File Explorer onto a 3D window.

2. **Insert the graphic of an existing graphics file**
   - Select the graphic and click **Graphics** on the Edit ribbon tab of 3D.
   - Select the `.jt` graphic to use (default folder: `...\3D\jt-graphics`).
   - Imported graphics are added to the selected graphic group while keeping existing graphics; delete unneeded graphics.

3. **Create your own object graphic**
   - Open the object, click **Insert Shape** on the Edit ribbon tab, and select the shape to create.
   - The shape is added to the selected graphic group.
   - You can also copy graphics from other graphic groups via **Show Graphic Structure** and paste with **Ctrl+V**.

4. **Create a complex graphic** by inserting multiple shapes or imported graphics and positioning, rotating, scaling, or coloring them.

> **Note:** After importing, creating, or transforming object graphics, you may need to adjust animation paths or points — except when using **Exchange Graphics**.

---

## Creating Your Own Objects

To create your own graphics:

- **Duplicate or derive** a class object from the Class Library with similar properties, then edit its 3D properties.
- **Import a 3D graphic** from the Plant Simulation graphics library (`installation folder > 3D > jt graphics`), your own library, or another program. After importing, you may need to scale, rotate, and move it to the scene origin. Right-click the graphic and select **Make Simulation Object**.
- **Model your own 3D graphic** by inserting shapes and positioning/rotating/scaling/coloring them. Group multiple graphics before transforming the group into a simulation object via **Make Simulation Object**.
- **Create a simulation object with animation** to make the model look as close to reality as possible.

---

## Import a 3D Graphic

3D can import these file formats:

- All 3D Graphic Files
- JT Files (`*.jt`) — recommended whenever possible
- Parasolid Files (`*.x_b`, `*.x_t`, `*.xmt_bin`, `*.xmt_txt`)
- IGES Files (`*.igs`, `*.iges`)
- STEP Files (`*.stp`, `*.step`)
- VRML Files (`*.wrl`)
- STL Files (`*.stl`)
- Catia V4 Files (`*.exp`, `*.model`)
- CAD Layout Files (`*.dgn`, `*.dwg`, `*.dxf`)

To import a graphic containing animation structures (e.g., JT files):

- Click **Import Graphics** on the Edit ribbon tab, select the file type, navigate to the file, and click **Open**.
- To replace an object's graphic with another that contains animation structures, right-click the object and select **Exchange Graphic**, then select 3D Files.

---

## Model Your Own 3D Graphic

You can model your own 3D graphic by inserting one or more of these shapes: **Barred Area, Box, Cone, Cuboid, Cylinder, Dimensioning, Factory Walls, Fence, Mezzanine, Rack, Sphere, Stairs, Text, or Textured Plate**.

- Click the shape to create (e.g., Cuboid).
- Select the **Graphic Group** to which to add it.
- Type the **Dimension X/Width**, **Y/Depth**, and **Z/Height**.
- Click **Create**; 3D attaches the shape to the mouse pointer. Drag to position and left-click to insert. Right-click or press **Esc** to cancel.
- To change position/rotation/scale, select the shape and use **3D Properties > Transformation** tab.
- To set whether the shape is an obstacle for the worker, use **Edit 3D Properties > Graphic Settings** tab.
- To assign a color/material, use **3D Properties > Material** tab.
- To delete the shape, right-click it and use the mini toolbar, or use **Show Graphic Structure** and select **Delete**.

> **Note:** When inserting a new shape into an external graphic group, Plant Simulation automatically activates **Show External Graphic Groups** so you can align the new graphic with other graphics of the destination group.

---

## Create a Textured Plate

- Click **Textured Plate** on the Edit ribbon tab of the 3D window.
- Select an image and settings (e.g., orientation, fit).
- Click **Create**, then drag and click to place (right-click or **Esc** to cancel).

Orientations:

| Orientation | Appearance |
|---|---|
| Floor | flat on the floor |
| Front wall | on the front wall |
| Side wall | on the side wall |

- **Show on Both Sides** — shows the image on the top/front and bottom/back of the plate.
- **Fit Image Size** with 2 tiles in each dimension inserts two tiles of the image per dimension.
- Move the plate by dragging with the mouse; move up using **Ctrl + Up arrow**.
- Change size via **Edit 3D Properties > Transformation**.
- Set obstacle for the worker via **Graphic Settings**; assign material via **Material** tab.

---

## Create a Non-textured Plate [example]

- Click **Cuboid** on the Edit ribbon tab.
- Enter `0` into the respective text box to create the plate on that plane.
- Click **Create** and proceed as for a textured plate to place or move it.

---

## Model a Bottle

Using the 3D shapes **Cylinder** and **Cone Frustum**, you can put together a bottle or similar item. Use easily distinguishable colors to tell the components apart.

1. **Bottom of the bottle** — a flat Cylinder.
2. **Body of the bottle** — a Cylinder open at the bottom and top.
3. **Bottleneck** — a **Cone Frustum**.
4. **Cap** — a Cylinder with the same radius as the neck.

Assemble:

- Place the body onto the bottom, then click **Align to Grid** on the Edit ribbon tab; group these parts.
- Place the bottleneck, then **Align to Grid**.
- Move the bottleneck downward in the Z-dimension (via **Edit 3D Properties**) until it sits flush.
- Group the parts.
- Place the cap: hold **Ctrl** and press the **Up arrow** to move it over the neck, then the **Left arrow** to position it; click **Align to Grid**, then adjust the Z-dimension until it fits.

---

## Set How Plant Simulation Shows an Object

An object can look different depending on the level of the object hierarchy in which you open a window. Plant Simulation distinguishes the **outside representation** and the **inside representation**:

**Outside representation of a Frame** (selected when you click the Frame in a window that opened its location):

- Its graphic groups marked **Visible** and **External**.
- Contained objects not explicitly excluded (only if **Show Content** is selected for the Frame).

**Outside representation of other objects**:

- Graphic groups marked **Visible**.
- State graphics set according to the **Orientation**.
- Material flow direction (if length-oriented).

**Inside representation of a Frame** (shown when you open a Frame):

- Graphic groups marked **Visible** and **Internal**.
- Outside representation of its contained objects and Frames.

**Inside representation of other objects**:

- Graphic groups marked **Visible**.
- State graphics according to **Orientation**.
- Outside representation of contained objects.

To show outside and inside representations at the same time, activate **Show External Graphic Groups** in a window containing the object you are editing.

In the active window you can additionally show/hide:

- All Connectors, Interfaces, and Markers via **Show Connections**.
- Material flow direction arrows via **Show Material Flow Directions**.

---

## What Plant Simulation Shows in a Window

What is shown depends on the content of the object/Frame, the settings of that content, and window settings:

- **An object** (excluding Frame/connection/sensor): shown if its location is open in the window AND at least one of its graphic groups is Visible, External, and contains graphics.
- **A Frame**: shown if its location is open AND (at least one graphic group is Visible/External/contains graphics OR the Frame shows Content and contains at least one object/Frame not Excluded From Show Content).
- **External graphic group of a Frame**: shown if the group is Visible AND (the Frame is shown in the window OR the Frame is open and the window shows External Graphics).
- **Internal graphic group of a Frame**: shown if Visible AND the Frame is open in the window.
- **Graphic group of an object**: shown if Visible AND (the object is open OR shown in the window).
- **Name of a Frame/object**: shown if the object shows Captions AND the Frame/object is shown and the window shows Names.
- **Label of a Frame/object**: shown if the object shows Captions AND shown and the window shows Labels.
- **State graphics of an object**: shown if the object shows States AND (open OR shown in the window).
- **Connector of a Frame**: shown if the window shows Connections AND (Frame open OR shown with Content, with both connected objects not Excluded From Show Content).
- **Interface/Marker of a Frame**: shown if the window shows Connections AND (Frame open OR shown with Content, and the Interface/Marker is not Excluded From Show Content).
- **Sensor of a length-oriented object**: shown if the object shows Sensors AND (open OR shown).
- **Material Flow Directions of a length-oriented object**: shown if the window shows Flow Directions AND the object is shown.

---

## Using Alternative Graphic Groups

This sample models a simplified airplane and shows the progress of the airplane assembly by showing selected graphic groups that display the finished components.

Modeling tasks:

- Create a new MU class for the object.
- Create alternative graphic groups for the components.
- Show the progress of the airplane assembly.

### Create a New MU Class for the Object

- Open the folder **MUs** in the Class Library.
- Right-click **Container** and select **Duplicate**.
- Press **F2** and rename the new Container to `Airplane`.

### Create Alternative Graphic Groups for the Components

- Open the Frame containing the simulation model.
- Edit the MU class `Airplane` (right-click in the Class Library, select **Open in 3D**; right-click the background of `.UserObjects.Airplane` and select **Edit 3D Properties**).
- Delete the default graphic (the pallet named `default`).
- Click **Add** to add new graphic groups: `Fuselage`, `Cockpit`, `RightWing`, `LeftWing`, `TailAssembly`.
- For each group, create the actual graphic on the Edit ribbon tab:
  - **Fuselage** — a Cylinder, rotated 90° to horizontal.
  - **Cockpit** — a Cone Frustum, rotated 90° and placed at the right of the fuselage.
  - **RightWing** and **LeftWing** — placed at appropriate positions on the fuselage.
  - **TailAssembly** — a Cone (vertical stabilizer) and a Sphere (horizontal stabilizer, scaled and flattened).

> **Note:** Clear **Scale automatically** on the Transformation tab, otherwise the graphic will not show the entered settings.

---

## Show the Progress of the Airplane Assembly

Show the assembly progress by successively hiding and showing graphic groups as the airplane moves from station to station.

### Insert and Configure the Source and Processing Stations

- Insert a **Source** that produces an MU of type `Airplane`; select `hidePlane` as the **Exit Control** on the Controls tab.
- Insert **Station** with a processing time of 10 seconds (`0:10`); select `showFuselage` as **Entrance Control**.
- Insert **Station1** (10 seconds); select `showTailAssembly` as **Entrance Control**.
- Insert **Station2** (10 seconds); select `showWings` as **Entrance Control**.
- Connect the stations with Connectors.

### Program the Visibility Controls

Use the attribute `Visible` to hide/show graphic groups.

`hidePlane` (Exit Control of the Source) hides all components, then moves the airplane to the next station:

```simtalk
@._3D.getGraphic("Fuselage").Visible := false
@._3D.getGraphic("Cockpit").Visible := false
@._3D.getGraphic("LeftWing").Visible := false
@._3D.getGraphic("RightWing").Visible := false
@._3D.getGraphic("TailAssembly").Visible := false
@.move -- move the airplane on to the next station
```

`showFuselage` (Entrance Control of `Station`) shows the fuselage and cockpit:

```simtalk
@._3D.getGraphic("Fuselage").Visible := true
@._3D.getGraphic("Cockpit").Visible := true
```

`showTailAssembly` (Entrance Control of `Station1`) shows the tail assembly:

```simtalk
@._3D.getGraphic("TailAssembly").Visible := true
```

`showWings` (Entrance Control of `Station2`) shows the wings:

```simtalk
@._3D.getGraphic("LeftWing").Visible := true
@._3D.getGraphic("RightWing").Visible := true
```

Set a Real-time factor of 16 in the EventController dialog for a smooth animation.

### Change Orientation and Position of the Object on the Stations

- To rotate the airplane 90° to the right: right-click the airplane class, select **Open in 3D**, right-click the background, select **Edit 3D Properties**, and enter `90` into **Angle** on the **Transformation > Rotation** tab.
- To change position: open the class in a new window, press **Ctrl+A** to select all graphic groups, move them left with the left arrow key until the center of the wings is on the y-axis, and move up on the z-axis with **Ctrl+Shift+Up arrow**.

---

## Show Object States

You can show the states of objects with **state graphics**. State graphics show the **States** of the Material Flow Objects, and a state graphic can show several states at the same time. Settings are on the **States** tab in **Edit 3D Properties**.

### Show States on a Signal Post Above the Machine

Vertically arranged state graphics are shown with a signal lamp on a gray signal post positioned at the left top rear corner of the standard graphics by default.

To activate vertically arranged state graphics, open the object in 3D, right-click the background of the 3D window, and select **Edit 3D Properties**.

### Show States at the Front of the Machine

Plant Simulation shows states as horizontally arranged cubes at the back of the machine graphic by default. Depending on the machine graphic, this may hide the state graphics.

To show state graphics at the front of the machine:

- Open the object in 3D, right-click the background, and select **Edit 3D Properties**.
- Click **Show All Possible States** and rotate the machine to view the state graphics.
- Move the horizontal states to the front:
  - With arrow keys: select the state graphics bar; **Up/Down** moves in Y, **Left/Right** moves in X, **Ctrl+Up/Down** moves in Z.
  - With the mouse: drag left/right for Y, back/forth for X, **Ctrl+drag** up/down for Z.
  - With precise values: right-click the machine, select **Show Graphic Structure**, then **Edit 3D Properties**, and on the **Transformation** tab set `X = -1.07`, `Y = -0.2`, `Z = 0.25`. Click **Apply**.
- If too high, scale in Z: clear the **Uniform** check box and enter `0.9` into **Z**.
