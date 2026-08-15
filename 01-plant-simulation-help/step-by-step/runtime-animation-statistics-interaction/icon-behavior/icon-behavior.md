# Icon Behavior

## Overview

This section covers two related topics from the Plant Simulation Help:

1. Creating and managing **Live Connections** and **Filesystem Connections** to Omniverse (via `MVA_WriteUSD`).
2. **Animating the simulation model** and **working with object icons** (the Icon Editor).

---

## Live Connection and Filesystem Connection

For a **live connection**, the project file and system root folder is typically a subfolder in the
Omniverse Nucleus project folder managed by the Omniverse Nucleus server.

### Create and Activate a Live Connection or a Filesystem Connection

Use the following instructions to create and activate a **Filesystem Connection** with `MVA_WriteUSD`:

```javascript
var system_root_path:string = "D:/USD_DataFiles/My_Project01/Library"
var output_path:string = "file://d:/USD_DataFiles/My_Project01A/myExport.usd"
MVA_writeUSD(output_path+"?sysroot="+system_root_path)
```

### Terminate an Open Live Connection or a Filesystem Connection

Type an empty string to terminate an open Live Connection or an open Filesystem Connection:

```javascript
MVA_writeUSD("")
```

### Notes

- Make sure that Omniverse Composer does not have an open connection to a previously exported
  simulation while starting a new export from Plant Simulation with the same project file and system root.
- For a **Nucleus Live Connection**, the function `MVA_writeUSD()` is not yet supported.

---

## Animating the Simulation Model and Viewing the Results

This section introduces animating your simulation model and viewing the results of simulation runs:

- Animate the Simulation Model
- View and Visualize Statistics
- Switch States and Execute Actions

### Animating the Simulation Model

One task when creating a simulation model is to visually show the flow of materials through the plant.
Plant Simulation shows the animation settings in 3D on the **Tab MU Animation** in the dialog **Edit 3D Properties**.

#### Activating and Deactivating the Animation

During the simulation run, the animation shows:

- The state of the objects.
- The position and movements of the MUs in the simulation model.

> **Note:** As animating parts and object icons slows down the simulation, only activate it when you
> actually want to show the model or check that it behaves correctly. For overnight batch runs, it is
> recommended to deactivate it.

- You can activate or deactivate **MU** and **State Animation** only together, not individually.
- When you **activate MUs and States**, you immediately see the flow of the parts and the blocked
  stations where MUs pile up.
- When you **deactivate MUs and States** while an object intends to change its state, Plant Simulation
  delays its display on screen until you activate the animation again or until the object is selected.
- To deactivate MUs and States, click the corresponding button on the **Home** ribbon tab.
- To run the simulation with the setting you selected, click **Start/Stop Simulation** in the EventController.

> **Note:** Clicking the button on the **Home** ribbon tab activates MU and State Animation. To start the
> simulation without animating objects and MUs, click the other animation button.

---

## Working with Object Icons

### Overview

The **Icon Editor** is provided to edit icons for backward compatibility.

In previous versions, the 2D visualization of Plant Simulation used an object's icons to display it in
the Class Library, the Toolbox, and the Frame. The icons could also display the object's state of
operation, such as failed, paused, unplanned, etc.

You can still modify icons in simulation models created in previous versions by clicking
**Edit Icons [Home ribbon]** to open the Icon Editor.

> The 3D visualization of Plant Simulation 2606 no longer uses icons.

### Create an Icon

You can create a new icon and then open an existing drawing to use.

Do one of the following:

- Click **New Icon** on the **Edit** ribbon tab. If the drawing you open is larger than the default icon
  size of **41 by 41 pixels**, enter another width and/or height.
- Click **Import > Import Bitmap File / Import Icon Resource**, navigate to the folder containing the
  drawing you want to use, select the file, and click **Open**.
- Drag a graphics file (`.gif`, `.bmp`, `.ppm`, `.ppm raw`, `.dxf`, or `.dwg`) from Windows Explorer over
  the drawing window and drop it there.
- Enter a meaningful **Name** for the icon.
- To draw a line or shape, select a drawing color and one of the drawing tools on the **Edit** ribbon tab,
  then draw the shape in the drawing window.
- To change the color:
  - **of one or several pixels:** select a color in the color palette and click the pixel(s) whose color
    you want to change with one of the drawing tools.
  - **of a contiguous color area:** select a color in the color palette and click the area whose color you
    want to change.
- To draw with two colors, assign a color each to the left and right mouse buttons:
  - Click a color in the color palette with the left mouse button to add it to the top drawing color field; or
  - Double-click the color field and define a color of your choice in the **Colors** dialog.
  - Then click the respective mouse button to draw with that color.
- You can make pixels or areas transparent:
  - **one or several pixels:** click the transparency field and click the pixel(s) you want to make
    transparent with one of the drawing tools.
  - **a contiguous color area:** click the transparency field and click the area you want to make transparent.

> **Note:** The background of the Frame shines through any area marked as transparent.

- Click the apply button to apply the changes and close the Icon Editor.

### Edit an Icon

You can edit an object's icon. Do one of the following:

- Right-click the object in the Frame and select **Edit Icons**.
- Select the object in the Frame and click **Edit Icons** on the **Home** ribbon tab.
- Right-click the object in the Class Library and select **Edit Icons**.
- Click the corresponding button on the **Home** ribbon tab to edit the icons of the selected Frame.
- Click the corresponding button on the **Home** ribbon tab to edit the icons of the selected object.
- Then use the functions on the **Edit Ribbon Tab** of the Icon Editor to actually edit the icon.
- Click the apply button to apply the changes.

### Make Areas of an Icon Transparent

You can make a contiguous area of an opened graphics file transparent so the background color of the
Frame shines through.

Proceed as follows:

1. Open the Icon Editor by clicking **Edit Icons** on the **Home** ribbon tab.
2. Click the navigation buttons to navigate to the icon you want to make transparent.
3. Click the **color picker** and click in the background of the icon. This makes that color the active
   drawing color, which you want to replace.
4. Select the transparency color that replaces the active drawing color in the **Color Palette proper** —
   not in the transparency color field.
