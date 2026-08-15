# Navigation, Camera & Grid Control

> Summary of the Plant Simulation Help section on visualizing the material flow, working with the scene, controlling the view, and working with the grid.

## Visualizing the Material Flow

Introduces the most important tasks for creating and visualizing a simulation model.

Plant Simulation distinguishes between these object types:

- Simulation Object
- Animatable Object
- Graphic Group [defined]
- State Graphic [defined]
- Graphic [defined]

The **Show Graphic Structure** context-menu dialog shows these object types in a tree structure. A 3D window shows objects with these colors:

- A selected **simulation object** is shown in **green** (opening it shows a green border on the inside).
- A selected **animatable object** is shown in **purple** (opening it shows a purple border on the inside).
- A selected **graphic** is shown in **yellow green**.

## Creating a Simulation Model

You create a simulation model in several steps.

- To create a new model, click **Create New Model** on the Start Page, or select **File > New**.
- To show built-in simulation objects and their graphics, right-click the **MaterialFlow** folder in the Class Library and select **Open in 3D**. The same works for other folders.
- To show the name of an object, drag the mouse over it.

### Mouse navigation (basic)

- **Rotate** the scene: hold the left and right mouse buttons and drag, or hold **Ctrl** + right mouse button and drag.
- **Pan** the scene: hold the right mouse button and drag.
- **Move camera forward/backward**: roll the mouse wheel.
- **Zoom** in/out: roll the mouse wheel, or hold **Shift** + right mouse button and drag.

> **Note:** On a three-button mouse, click the middle button where the description says to click the mouse wheel.
>
> **Note:** If mouse manipulation does not work, check the Mouse Properties for the Wheel in the Mouse Control Panel under **Start > Control Panel**.

### Inserting objects

- To open a new window, go to the Class Library, right-click the folder, and select **Open in 3D**.
- To insert an object into the window:
  - Make sure **Show Grid** on the View ribbon tab is active. It is recommended to show the grid before inserting so you can place objects exactly where you want. Without the grid, Plant Simulation uses the source object's original coordinates by default.
  - Select the object in the Toolbox, drag to the desired position, and left-click to insert it.
  - As long as an object is selected in the Toolbox, Plant Simulation shows a preview to help positioning.
  - To cancel inserting, click the right mouse button.
  - Example: insert a **Source**, a **Conveyor**, a **Station**, and a **Drain**.

### Connecting objects

- Make sure **Show Connections** on the View ribbon tab is active (3D does not show Connectors by default).
- Click the **Connector** in the Toolbox on the **MaterialFlow** tab.
- Click the source object once; Plant Simulation attaches a line symbolizing the Connector to the mouse pointer.
- Drag to the destination object and click once to establish the connection.
- 3D shows the Connector as a line between the connected internal interfaces; the pointed cone shows the direction.
- To terminate connect mode before clicking the destination, right-click or press **Esc**.
- To connect several objects in a row without interrupting, hold **Ctrl**, attach the outgoing connection to the first object, drag to the next, and click to attach the incoming connection.

### Starting the simulation

- Control the simulation with the buttons on the **Home** ribbon tab, or
- Double-click the **EventController** icon and use its buttons.
- Watch how the produced parts move across the simulation objects.

## Modeling Hierarchically [in 3D]

Hierarchical modeling lets you add any level of detail to areas and machines. You create a machine, production area, etc. in a **Frame** using built-in object classes and/or custom classes, then insert that Frame into another Frame (e.g., insert the production area into the Frame containing your entire factory).

## Working with the Scene

You can:

- Manipulate the Scene with the Mouse
- Align the View to the Main Directions
- Save a View with the Model and Return to It
- Fly on a Defined Path Through the Scene

Press **F** to show/hide scene information: Frames per Second (FPS), summed number of nodes, summed number of polygons, summed memory usage, OpenGL version, and display driver information.

### Manipulate the Scene with the Mouse

Instead of a normal mouse, you can also use a **Space Navigator** mouse.

- **Rotate the scene**: hold left + right mouse buttons and drag, or **Ctrl** + right mouse button and drag.

Rotation behavior:

- If you start rotating and hold the position for at least 400 ms with an object/graphic under the pointer, Plant Simulation rotates around the position under the pointer.
- Otherwise, it rotates around the projection of the window center on the insertion plane (or a matching orthogonal when rotated 90°). The pointer position does not matter in this case.

- **Pan the scene**: hold the right mouse button and drag (or middle mouse button on a three-button mouse).
- **Move camera forward/backward**: roll the mouse wheel, or hold **Shift** + right mouse button and drag.
  - Move at **1/10 speed**: hold **Ctrl** + roll the wheel.
  - Move at **10× speed**: hold **Shift** + roll the wheel.

**In Planning View:**

- Move the scene on the plane: hold the right mouse button and drag.
- Zoom: roll the mouse wheel, or hold **Shift** + right mouse button and drag.
  - Zoom at **1/10 speed**: hold **Ctrl** + roll the wheel.
  - Zoom at **10× speed**: hold **Shift** + roll the wheel.

### Align the View to the Main Directions

Use the commands on the **View** ribbon tab to look at the scene from a predefined direction:

- **Top**, **Front**, **Left**, **Right**, **Back**, or **Bottom**.

- View the entire scene from the **top** looking down.
- View from the **front**.
- View from the **left**.
- View from the **bottom** (looking upward along the negative z-axis).

Notes:

- If **Show Grid** is active, the grid is shown below the object viewed from below.
- If **Show Base Plate** is active, the base plate is shown below the object and hides the object itself.
- If something is selected, the command fits the selection rather than the whole scene.
- **View All** fits the entire scene into the window and shows all objects.

### Save a View with the Model and Return to It

Save the current camera position/orientation with the model and return to it later.

- In 3D, click **Camera Marks** on the View ribbon tab.
- Enter a **Name** in the dialog **Mark Current Camera Settings**.
- 3D shows the scene path in the **Scene Path** field.
- Click **OK**. The setting is saved with the active root object in the model file.

To return to a saved view, click the down arrow on **Camera Marks** and select the camera mark from the list, or select the **Camera Marks** command, choose a saved scene, and click **Activate**.

- To rename or delete a camera mark, select it and click **Rename** or **Delete**.
- Move a camera mark up/down in the list with the up/down arrow buttons.

### Set the Background Color of the Scene

Set the background color of a selected Frame or Class Library folder in the 3D window.

- Click **Edit 3D Properties** on the Home ribbon tab (or right-click the Frame window and select **Edit 3D Properties**), then open the **Background** tab.
  - You can also open **Edit 3D Properties** by pressing the **spacebar**.
- Select **Assign a Background Color of Its Own**.
- Select the **Base Color** (predefined color, or **More Colors** → **Select** to pick a color in the matrix).
- Set **Corner Brightness** for the four corners with sliders to define a color gradient.

> **Note:** If no background color is defined, Plant Simulation uses the parent object's background color.

## Flying on a Defined Path Through the Scene

Attach a camera to an object and view the scene through the lens of that object. The camera moves with the object during a simulation run. Three cameras exist:

- **Main camera** — normal view.
- **Object camera** — attached to an object (e.g., a part or Worker) and moves with it.
- **Animation camera** — moves along a defined animation path.

To define a tracking shot:

- Left-click an object to select it.
- Click **Animate Camera** on the View ribbon tab to open **Fly on Path** (if no object is selected, the dialog refers to the current root object).
- Select a camera path. Define/edit paths in **Edit 3D Properties > Tab Camera Animation** of the Frame.

### Attach a Camera to an Object

- Select a single object.
- Click **Attach Camera** on the View ribbon tab of the 3D window.
- Plant Simulation attaches the camera at the center of the top of the object's bounding box, with an offset of `(0, 0, 0.1)` so your eyes sit above the top plane.
- By default, the object camera looks along the positive x-axis using the positive z-axis as Up direction.

As the object moves, the camera moves with it automatically.

### Detach the Camera from an Object

Click **Detach Camera** on the View ribbon tab to return to normal view.

The object camera is also detached:

- When you delete the object the camera is attached to.
- When you change the scene.

### Animate the Object Camera

Animate the camera on a camera animation path of the selected Frame to create a fly-through effect.

> **Note:** Define a camera animation path on the **Tab Camera Animation** of the Frame first.

- Go to the View ribbon tab and click **Animate**.
- Select the animation path name in **Fly on Path** from **Path Name [MU animation]**.
- Select **Backwards** to move toward the starting point (Plant Simulation enters a negative velocity).
- Click **Play** to start.
- Click **Pause** to pause (independent of the simulation).
- Click **Stop** to stop (independent of the simulation).

At the end of the animation, 3D sets the main camera to the last point of the animation camera and deletes the animation camera. The animation camera uses a lens offset of `(0, 0, 0.1)`.

To test the path, use the **Test** tab in **Edit Path**, select an animated graphic, and start the test animation.

## Controlling Your View in the Scene

The 3D window controls the camera that represents the viewer's eyes. You can:

- Set the Main Directions
- Set View Points
- Attach a Camera to an Object/Frame and Detach it
- Animate the Camera

### Set the Main Directions

Independent of the active camera, adjust the view to any main direction of the view or an object at any time. When an object is selected, the 3D window zooms it out and adapts the camera direction to the selected main direction of the object's coordinate system.

### Set View Points

Save any view (position/orientation of the main camera) and return to it later. You can also save the active camera setting with the active root object under a meaningful name as a **Camera Mark**.

Unlike automatically saved view points, you can save any number of Camera Marks (saved in the model file) and rename/delete them at will.

### Attach a Camera to an Object/Frame and Detach it

Attach a camera to any object and view through its lens; detach when done. When the object moves (e.g., during simulation), the camera moves with it.

Plant Simulation also:

- Visualizes the attached camera as an animatable object.
- Lets you switch between object view and normal view.
- Lets you manually transform the camera (change view in object view, or manipulate the object in normal view).
- Lets you set speed and direction of the animation.
- Lets you pause, continue, and stop camera animation independent of other animations/simulations.

### Animate the Camera

Make the camera move on any animation path of the selected object or root object, flying on the path and viewing the scene from it.

Plant Simulation also:

- Visualizes the animated camera as an animatable object.
- Lets you switch between animation view and normal view during the animation.
- Lets you manually transform the animated camera.
- Lets you define animation speed and direction.
- Lets you pause, continue, and stop camera animation independent of other animations/simulations.

## Working with the Grid

Plant Simulation uses the grid as the surface onto which it inserts objects.

> Showing or hiding the grid affects object behavior:
> - When the grid is **shown**, manipulating objects refers to the **grid plane**.
> - When the grid is **hidden**, manipulating objects refers to the **view plane** (perpendicular to the viewing direction).

- To change grid settings for the current model, click **Settings** on the View ribbon tab to open **Edit Grid and Base Plate Settings**.
- To change grid settings for new models, select **File > Preferences > 3D**.

Grid behavior:

- The grid origin is at the top-left corner of the window, offset one grid unit to the right and down each.
- Plant Simulation re-creates the grid after each model change when redrawing the scene; the grid expands/shrinks to show all objects.
- The grid is a modeling aid — usually hide it when presenting the model by pressing the **Ins** key.
- The origin lines (red by default) are always part of the grid.
- Grid size is always a multiple of the smallest visible grid distance.

You can:

- Show and Hide the Grid
- Set Grid Properties
- Edit Grid Lines
- Position the Grid on Different Planes
- Move the Grid in the Window

After inserting objects, you can align them to the grid, snap them to the grid, snap them to other objects, or arrange them on the grid (ensure **Show Grid** is on).

### Show and Hide the Grid

- Click **Show Grid** on the View ribbon tab, or
- Press the **Ins** key.

### Set Grid Properties

Click **Edit Grid and Base Plate Settings** on the View ribbon tab.

- To assign a material to the base plate below the grid lines, click the color box and select material components in the **Material** dialog (Tab Material). Show/hide the base plate with **Show Base Plate**.
- To assign a color to the coordinate axes (x-axis and y-axis), use the **Axes Color** drop-down.
- To define grid line settings, edit the table on the tab.

### Edit Grid Lines

Edit existing grid lines or add new ones in the **Grid Lines** group box.

- To add a grid line, click **Add**.
  - Enter the distance between two grid lines (example: 2 meters).
  - Select a color (example: bright blue).
  - Select **Visible** to show the grid line.
  - Select whether inserted objects snap to this grid line (snapping enables precise placement with the mouse).
- To edit an existing grid line, select it and edit its distance, color, snap behavior, and visibility.

### Position the Grid on Different Planes

Plant Simulation uses a **left-handed coordinate system**:

- **x-axis**: left-to-right
- **z-axis**: bottom-to-top
- **y-axis**: front-to-back

To place the grid on different planes, click **Transform** on the View ribbon tab and select the radio button in **Grid Position and Orientation**:

- **XY Plane** — grid on the plane defined by the x-axis and y-axis.
- **XZ Plane** — grid on the plane defined by the x-axis and z-axis.
- **YZ Plane** — grid on the plane defined by the y-axis and z-axis.

> **Note:** Plant Simulation does not save these dialog settings; they only apply while the dialog is open.

### Move the Grid in the Window

Click **Transform** on the View ribbon tab and use the text boxes/buttons under **Position** in **Grid Position and Orientation** to move the grid origin.

> **Note:** These settings are not saved; they apply only while the dialog is open.
>
> **Note:** Moving the origin uses the length unit from **Model Settings > Units > Length**.

Wheel adjustments (click in a text box and roll the mouse wheel):

| Axis / direction | 0.01 units | 0.1 units | 1 unit |
|---|---|---|---|
| x right | Ctrl + forward | forward | Shift + forward |
| x left | Ctrl + backward | backward | Shift + backward |
| y back | Ctrl + forward | forward | Shift + forward |
| y front | Ctrl + backward | backward | Shift + backward |
| z up | Ctrl + forward | forward | Shift + forward |
| z down | Ctrl + backward | backward | Shift + backward |

- **Scene Origin** — reset x/y/z to the default values `0, 0, 0`.
- **Object Origin** — set x/y/z to the position of a single selected object.
