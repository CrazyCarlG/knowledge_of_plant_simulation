# Frame Modeling, Simulation Control, and Drag-and-Drop

This document summarizes the Plant Simulation help topics covering hierarchical modeling, working with Frames, connecting objects, controlling the simulation with the EventController, and drag-and-drop.

---

## Modeling Hierarchically

Modeling hierarchically means inserting components (modeled in a Frame) into other Frames. This lets you model and test individual components detached from the Frame holding the complete simulation model.

- Any number of components can be combined in the Frame where you build the overall model.
- Example: a component modeled in Frame `MyComponent1` is inserted into Frame `MyPlantAnytown`, which holds the complete model.
- To open the Frame from which the current Frame derived, click **Open Origin** (opens `MyComponent1` in `ApplicationObjects > Components` in the Class Library).
- Components (large machines, entire departments) can be modeled to closely match their real-life counterparts, inserted multiple times, given icons, and used like any other object.
- **Advantages:** clear model structure; distribute development among several colleagues or sites, integrating components later.

### Test a Component You Modeled

Hierarchical modeling lets you test components before integration. Create a test environment: insert the component into a test Frame, add a Source and a Drain, connect all objects, and start the simulation.

---

## Working with the Frame

Simulation models are typically created in the Frame placed in the `Models` folder in the Class Library. You can also insert additional Frames.

**Rename a Frame** — one of:
- Right-click it in the Class Library and select **Rename**.
- Select it and press **F2**.
- In the Frame window, click **Rename** on the Home ribbon tab or press **F4**.

**Build the model:** insert built-in or user-designed objects and connect them (representing stations) with the **Connector**.

**Run the simulation:** insert an **EventController** to start, stop, and reset the simulation.

**Hierarchical structure:** place Frames within Frames to build models that match real-world systems and break complex tasks into manageable chunks.

### Select View Options in the Frame

- General options: **File > Preferences/Model Settings** in the Plant Simulation window.
- Frame-specific options: buttons on the **View** ribbon tab of the Frame.

| To do this | Action |
|---|---|
| Hide/show object names | toggle on View tab |
| Hide/show Connectors | toggle on View tab |
| Hide/show Comment objects | toggle on View tab |
| Hide/show grid | toggle on View tab |
| Set additional view options | via View tab |

- New Frames use settings from **File > Preferences/Model Settings**.
- To restore built-in settings and deactivate changes, select **Inherit Settings**.

---

## Model with Objects from the Class Library

Create a simulation model by inserting instances of class objects from Class Library folders into your model (usually the Frame in the `Models` folder). You can modify and expand the Class Library structure (add folders for models, test runs, components).

> **Note:** Renaming objects entered as entrance/exit controls, or as `Source > Attributes > MU Selection > MU`, can break path statements and cause the model to stop running correctly.

### Insert an Object from the Class Library

1. Navigate to the folder and object (grouped by function and frequency of use).
2. Click the object to select it (insert cursor appears).
3. Hold the mouse button and drag the object to the target position in the Frame, then drop it.

### Insert an Object from the Toolbox

1. Click the toolbar/tab containing the object (e.g., **Material Flow**).
2. Move the mouse to the object's icon and click to select it.
3. Move to the target position in the Frame and click once.
4. To insert several instances of the same class, hold **Shift** or **Ctrl** while clicking in the Frame.
5. To go to an object's class, press **Ctrl** and click the object in the Toolbox (highlights the class in the Class Library). Double-click it in the tree to edit class properties, or press **Ctrl+Alt** and click in the Toolbox.

---

## Insert Objects into the Frame

**Start a new model:** Click **Create New Model** on the Start Page, or **File > New**. This opens the Class Library, Toolbox, and an empty Frame in `Models`.

**Insert an object** — one of:
- Click the object icon in the Toolbox; the mouse pointer turns into crosshairs (+); click the location in the Frame.
- Drag-and-drop from the Class Library into the Frame.

**Insert several instances:** click the object in the Toolbox, hold **Ctrl** or **Shift**, click positions repeatedly, then release the key.

**Example model:** insert from **Material Flow** a Source, three Stations, and a Drain; from **User Interface** insert a Chart.

**Move an object** — one of:
- Click, hold, drag to the desired location, release.
- Press arrow keys to move one pixel at a time.
- Hold **Shift** + arrow key to move one grid unit at a time.

**Other actions:**
- **Align to Grid:** select all objects (drag a marquee) and click **Align to Grid** on the Icons ribbon tab.
- **Delete:** press **Delete** or right-click and select **Delete**.

---

## Connect Objects with the Connector

Material flow objects have entrance points (receive parts) and exit points (parts move on). The **Connector** establishes material flow connections using these points.

### Automatic connection
- Place objects next to each other when inserting (works when **Connect Objects Automatically** is on; works best in **Planning View**).
- To verify connections, select an object, move it, then click **Undo**.
- Automatic connection requires **File > Preferences/Model Settings > User Interface > Connect Objects Automatically**, with the exit of one object and the entrance of the next no more than **3 pixels** apart.

### Manual connection
1. Click the **Connector** in the Toolbox to activate connect mode (cursor becomes crosshairs).
2. Click object A, then object B.
3. Connections are only shown when **Show Connections** is selected on the View ribbon tab.
4. Dragging the Connector onto an object automatically places its starting point there.

### Connector modifier keys
| Action | Effect |
|---|---|
| Connector (no key) | Aligns connection to grid points next to the click location |
| **Connector + Ctrl** | Stays in connect mode to connect several objects consecutively |
| **Connector + Shift** | Inserts connection at a right angle |
| **Connector + Alt** | Sets anchor points at click location (freehand-like) |

### Anchor points and connection shapes
- **Non-straight connection:** click object A, then point 1, point 2, ..., then object B.
- **Right-angled connection:** hold **Shift** and click to set the anchor point.
- **Move an anchor point:** click it, hold the mouse button, and drag the handle.

### Other Connector operations
- **Check unconnected objects:** click **Unconnected Objects** on the View ribbon tab.
- **Line thickness:** enter a number in the **Weight** text box (higher = thicker, lower = thinner).
- **Line color:** in the **Colors** dialog, click the field next to **Color** (predefined colors or **More Colors > Select**).
- **Show source/target tooltip:** drag the mouse over the Connector.
- **Exchange successor:** select the Connector's end point and drag it to another object.
- **Exchange predecessor:** select the starting point and drag it to another object.
- **Insert object between two connected objects:** drag the object onto the Connector spot and drop it (Plant Simulation exchanges the successor). Also works with a Frame containing exactly one suitable entrance Interface and one suitable exit Interface.
- **Retain Connector when deleting an object:** hold **Ctrl** and press **Del**, then click **Yes**.
- **Auto-connect predecessor/successor on delete:** hold **Ctrl** while deleting via the context menu command **Delete**.
  > Does not work when an object has more than one predecessor and successor. If a successor exists, Plant Simulation exchanges the successor of all preceding Connectors; if a predecessor exists, it exchanges the predecessor of all succeeding Connectors.
- **Change Width/Color:** double-click the Connector icon and enter settings.
- **Reorder successors:** right-click the object, select **Reorder Successors**, and use the Up/Down buttons.

---

## Add a Background Graphic to the Frame

**Add a graphic:**
- Drag a `.gif`, `.bmp`, `.ppm`, `.ppm raw`, `.dgn`, `.dxf`, or `.dwg` file from Windows Explorer/Internet Browser over the Frame background and drop it.
- Drag a layout drawing over the background and drop it (usable as the actual background with objects on top, feasible for not-too-complex models).

**Notes:**
- `.dxf`, `.dgn`, `.dwg` files are vector-based, while Plant Simulation uses pixel-based graphics — plan the size conversion.
- If the CAD drawing contains units and its dimension is ≤ 32000×32000 pixels, Plant Simulation uses a **Corrective Scaling of 1**.
- If greater than 32000×32000 pixels, Plant Simulation scales the drawing to fit the Frame window.
- The Console window shows the origin and dimension of the `.dwg` drawing.

---

## Create Your Own Ribbon Tab/Context Menu in the Frame

Create a user-defined ribbon tab or context menu with frequently used commands.

1. Click **Configure User-defined Ribbon Tab** or **Configure User-defined Context Menu** on the Frame ribbon tab (button is highlighted if a tab exists).
   > To create a user-defined ribbon tab in a nested Frame, deactivate the **Inherit** command first.
2. Type in the **Title** (e.g., `My Ribbon Tab`).
3. Select **Active** to show the tab for that Frame.
4. Type the command name. Prefix a letter with `&` to make it an access key.
5. **Formulas as commands:** a leading `?` designates a formula. Examples:
   - `?Method1` calls the method `Method1`; the return value must be a string (allows switching text, e.g., Activate/Deactivate, or translating commands).
   - An empty string `""` hides the command.
   - Any formula works, e.g., `?Method1(42)` or `?DataTable[1,3]`.
6. Type the **Methods** to execute in the **Method to execute** text boxes. Methods expecting a parameter receive a list of the selected objects in the same Frame.
   - When called from a user-defined ribbon tab, the anonymous identifier `?` points to the Frame where the command was selected.
   > Context menu commands only apply to the selected object(s) within the Frame; the Class Library does not show the user-defined context menu.
7. Click **OK** to create (the tab appears to the right of the predefined tabs).

**Open a user-defined dialog from the tab:**
1. Enter the command name in **Text to display**.
2. Enter the path/name of the Method that opens the dialog in **Method to execute**.
3. Create the Method with that name containing:

```
name_of_your_user_defined_dialog.open
```

---

## Work with Objects in the Frame Window

- **Open object/Frame window:** double-click the object or Frame.
- **Insert object:** select it in the Class Library/Toolbox, drag over the Frame window, and drop.
- **Show/hide grid:** click the grid toggle (makes precise insertion easier).
- **Select object:** click it; drag to move.
- **Nudge:** arrow keys move one pixel; **Shift** + arrow key moves one grid unit.
- **Deselect:** click another object or anywhere in the Frame.
- **Select multiple:** hold **Shift** and click objects, or drag a marquee around them. **Ctrl+A** selects all.
- **Find object:** click **Incremental Find Object** on the Frame ribbon tab and type its name.
- **Connector handles:** select a Connector to show handles; click a handle to reshape it.
- **Show/hide connections:** toggle on the View ribbon tab.
- **Show unconnected objects:** click the toggle on the Frame ribbon tab.
- **Zoom in/out:** roll the mouse wheel forward/backward.
- **Show/hide object names:** toggle.
- **Prevent modification:** click the lock toggle.
- **Edit icons/add animations:** click the icon-edit button on the Home ribbon tab.
- **Model transitions between Frames:** use the **Interface**. When connecting Frames with several Interfaces, Plant Simulation opens **Select Interface** — select the Interface and click OK.
  > If a sub-Frame contains only a single object, you can connect it without Interfaces.
- **Open sub-Frame and close parent:** hold **Shift** and double-click a Frame.
- **Move down in hierarchy:** select **Down one Level** on the context menu.
- **Open origin Frame:** click **Open Origin** on the Home ribbon tab.
- **Close active Frame and open its location:** click **Open Location**.
- **Frame states:** use attributes `StateBlocked`, `StateEntryShut`, `StateResourceMissing`, `StateSetup`, `StateWorking`, `Stopped`, and `Unplanned`. Plant Simulation shows state as a colored ring on a pole.
- **Open help for a selected object:** press **F1**.

### Frame state colors

| Color | Frame state |
|---|---|
| red | Failed |
| pink | Stopped |
| blue | Paused |
| light blue | Unplanned |
| green | Working |
| yellow | Blocked |
| brown | Setting-Up |
| cyan | recovering or closed entrance |
| orange | Waiting for a resource (Exporter) |

---

## Show Tooltips of Objects in the Frame

Drag the mouse over an object and hover to show a tooltip. All objects show the name (bold) and origin; state and type add further information.

| Object type | Tooltip information |
|---|---|
| **EventController** | Current simulation time and End Time |
| **Point-oriented objects** (Source, Station, Buffer, Label, PickAndPlace) | Next event / deposit station, etc. |
| **Length-oriented objects** (Conveyor, Track, TwoLaneTrack) | Predecessor/successor, connected tracks, sensors |
| **Interface** | Connected objects |
| **Connector** | Connections |
| **Transporter** | Length of route, route (e.g., tractor of tugger train) |
| **Mobile objects** | Stacking order (e.g., Part on Pallet on Transporter; Part carried by Worker) |
| **Fluid objects** (PatchMatrix, Pipe, Tank, DePortioner) | Connected pipes/objects, next event, state |
| **Worker / Workplace** | Route, destination, assignment/reservation (filled vs. hollow arrow) |
| **SubFrame** | — |
| **Dialog** | — |
| **Method** | User-defined tooltip, source code comment, suspended |
| **User-defined attribute** | As tooltip in SubFrame / model Frame |
| **TransferStation** | — |

---

## Model Transitions Between Frames

When modeling hierarchically, connect a component (Frame) to preceding/succeeding material flow objects or Frames using the **Interface**. Transitions are where MUs move from one Frame to another, or between a material flow object and a Frame.

- Plant Simulation shows whether an Interface is connected, and whether it is an entrance or exit.
- If the sub-Frame contains only a single material flow object, connect the sub-Frame directly without Interfaces.
- The Tooltip shows externally connected objects. Plant Simulation does not insert a Connector to/from the object inside the sub-Frame.
- By default, `Graphics > Show Content` is active (3D view shows content). Clear **Show Content** to show only the sub-Frame.
- Insert the **Interface** from `MaterialFlow` (Class Library) or the **Material Flow** toolbar (Toolbox).

**Configure an Interface:**
1. Select the side of the Frame icon: **Top**, **Right**, **Bottom**, or **Left**.
2. Enter the maximum number of external connections (predecessors/successors).
   - **Predecessor:** connected object located before it in the sequence of stations.
   - **Successor:** connected object located after it in the sequence of stations.
3. Enter the **Position in %** (0–100) of the Interface on the side of the Frame. Used when **File > Preferences > General > Connect Objects Automatically** is active; auto-connection requires the exit of FrameA and entrance of FrameB to be no more than three pixels apart.
4. An Interface connected with a Connector shows its **Type** (Entrance or Exit).
5. Optionally select an **Exit Strategy** on the **Exit** tab.

---

## Controlling the Simulation with the EventController

The **EventController** coordinates and synchronizes events during a simulation run. When a part enters a Station, Plant Simulation computes processing time and enters that event/time into the **List of Scheduled Events**.

**Insert the EventController** from `MaterialFlow` (Class Library), the **Material Flow** toolbar (Toolbox), or by clicking its button on the Home ribbon tab.

### Time display (box next to Time)
- **Relative time:** resets to zero at simulation start (default).
- **Current time plus simulation time:** adds simulation time to the start time/date.
  - Example: today is March 13, 12:00 noon, run for two days → relative shows `2:00:00:0000`; current+simulation shows `We, 2023/03/15 12:00:00.0000`.

### Simulation controls
- **Initialize / Start-Stop Simulation:** executes all Methods named `Init` first; initializes before the next scheduled event.
  > `Init` methods auto-execute on first simulation start, or after stopping and clicking Reset Simulation without clicking Start/Stop before restarting.
- **Reset Simulation:** calls all Methods named `Reset`, deletes unprocessed events, resets time to 0, resets statistics, and clears pauses/failures. If running, Plant Simulation finishes the active event first.
- **Start the simulation:**
  - Click **Start/Stop Simulation** in the EventController, or on the Home ribbon tab.
  - Double-click the EventController icon while holding **Shift**.
- **Start without animation (max speed):** click **Start Fast Forward Simulation**.
- **Stop the simulation** (after active event processed): click **Start/Stop Simulation** again, or double-click the EventController icon while holding **Shift**.
- **Start with animation at full speed:** click **Start Full Speed Simulation**.
- **Step through events:** click **Single Step Simulation** (processes next event, then stops).
- **Open Event Debugger list:** click **List** (shows scheduled events ascending).

### List of scheduled events columns
| Column | Description |
|---|---|
| **Breakpoint** | Shows `S` for a breakpoint (inserted by double-clicking a cell) |
| **Type** | Event type, e.g., `Out`, `Pause`, `PauseEnd` |
| **Time** | Scheduled execution time |
| **Receiver** | Object receiving the breakpoint |
| **Sender** | Object sending the breakpoint |

### Speed and real-time mode
- **Increase speed:** drag slider left or press left arrow. **Decrease:** drag right or press right arrow.
- **Real-time mode:** enter the **Scaling Factor**. Plant Simulation is discrete-event and normally ignores time between events; the scaling factor sets real-time duration between two events. Duration = simulation time ÷ scaling factor (integer result).

---

## Select Settings for the Simulation

On the **Settings** tab of the EventController:
- **Time display:** relative time (default) or current time + simulation time.
  - Example: January 2, 12:00 noon, run for two days → relative `2:00:00:0000`; current+simulation `Mi, 2023/01/04 12:00:00.00`.
- **Date and time:** base for absolute time.
- **End time:** relative period the simulation runs; Plant Simulation stops when simulation time matches it. Example: enter `2:00:00:00` (or `2:::` and click **Apply**) for two days.
- **Statistics reset time:** the time from which Plant Simulation restarts collecting statistical data.

---

## Working with the Event Debugger

The **Event Debugger** precisely controls simulation event execution when using **Single Step Simulation**, helping detect errors. It supports conditions for stopping.

### Open and use the Event Debugger
1. Open the EventController.
2. Click **List** on the **Controls** tab (events sorted ascending by time, showing type, time, recipient, sender).
   - Double-click a cell to insert a single breakpoint (stops immediately before processing that event); double-click again to delete.
3. Select **Breakpoints Active**.
4. Click **Breakpoints** to open the list of defined breakpoints.
5. Click **Insert** in the **Breakpoint** dialog to add a breakpoint.
6. **Trace file:** enter a name in **Trace File** and select the checkbox to track all events. For a single event, enter a filename in the **Breakpoint** dialog.
7. **Stop at Selected Event:** select an event in the list and click this to add it as a breakpoint.
8. **Single Step Simulation:** process one event, then stop.
9. **Start/Stop Simulation:** run until the next breakpoint.

### Examples

**Example 1 — track a part's course:** watch all `Out` events for the Part with ID 1. To create a breakpoint for each Part, delete the MU's ID.

**Example 2 — all MUs leaving Station1:** no Receiver entered; Sender is `Station1` (breakpoint for each leaving part).

**Example 3 — class + time span:** breakpoint when a part of class `.MUs.Part` located on `Station1` creates an `Out` event between 1 and 3 hours. Use **Condition** for value/state/property conditions, or methods returning a boolean.

**Example 4 — property as condition:** breakpoint when a part of class `.MUs.Part` less than 100 meters long causes an `Out` event on `Station1` (unit depends on **File > Model Settings/Preferences > Units > Length**).

**Example 5 — trace file:** track Part ID 9's course and write stations to `c:\Exercises\trace3.txt`. Requires **Trace File** selected in the Event Debugger dialog. Clearing **Breakpoints Active** writes the trace file without stopping the simulation.

> Any event type can be used, not just `Out` events.

---

## Delete Parts with the Mouse or when Resetting the Model

- **Delete a single MU:** select it and press **Delete**.
- **Delete all MUs** in the active Frame and its sub-Frames: click **Delete MUs** on the Home ribbon tab.
- **Delete MUs on reset:** enter `deleteMovables` into a Method named `reset` inserted into the model.

> If the model still contains parts (new runs don't start numbering at `.MUs.Part:1`), check for additional Frames with inserted EventControllers and reset those as well.

---

## Working with Drag-and-Drop

Drag-and-drop has many applications in Plant Simulation:
- Insert objects from the Class Library into the Frame.
- Insert objects (Broker, ShiftCalendar, control method, table, etc.) into dialog text boxes — this enters the **relative path**, starting from the Frame containing the object using the path.
- To insert the **absolute path**, hold **Shift + Ctrl**.
- Use an **object reference** instead of an absolute path by typing `*` in front of the path, e.g.:

```
*.Models.FinePositioningAGV.Broker
```

- To use a relative path instead of absolute, click **Select Object**.
- **Duplicate/copy** an object to create a new class: hold **Ctrl**, drag to another Class Library location, release **Ctrl**.

### Use a Drag-and-Drop Control for Several Objects

Plant Simulation supports multiple drag-and-drop for objects whose drag-and-drop control accepts the selected objects as an **array** parameter, plus:
- AttributeExplorer, Method (objects passed in an array), Chart, HtmlReport
- Cycle (max two objects: first and last station), ShiftCalendar, LockoutZone
- Dragging several objects to the Class Library structure to create class objects.

**Example workflow:**
1. Insert material flow objects (Source, Station, Conveyor, Drain) and connect them.
2. Insert a Frame and rename it (e.g., `MyFrame`).
3. Open the Frame, click **Edit Controls** on the Home ribbon tab.
4. Right-click next to **drag-and-drop** and select **Create Control**.
5. Change the source code to:

```
param draggedObjects: object[] // one-dimensional array with n objects
                               // the size of which can change
var obj: object
debug
// @,?: drop target
for var i := 1 to draggedObjects.dim loop
   obj := draggedObjects[i]
   // enter your source code here
   print i, ": ", draggedObjects[i] // prints the dragged objects to the Console
next
```

6. Select the production line, drag it over the Frame, and drop it. The Console shows the dropped objects.
7. Adding `debug` opens the Method debugger; the variable `draggedObjects` on the **Variables** tab shows the array of dropped objects.

---

## Related Topics

- Model Hierarchically [general]
- Working with the Frame
- Show the Contents of a Frame in the Class Library
- Model Transitions Between Frames
- Show Reports in a Hierarchically Structured Model
- Auto-connect Length-oriented Objects
- Undo [3D] and Redo [3D]
- Transfer Parts from Station to Station
- Work with the Event Debugger
- Object Paths in SimTalk
- Drag-and-Drop in the Icon Editor / Method Editor / Lists and Tables / Chart
- Work with Data in the DataTable
- Configuring the TransferStation
- User-defined Attributes [general description]
- Create a Tooltip as a User-defined Attribute
