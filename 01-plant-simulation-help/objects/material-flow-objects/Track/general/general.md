# Track — General Description

## Description

The `Track` object, together with the `Transporter`, is used to model an AGV (automated guided vehicle) system.

- The time a `Transporter` remains on the `Track` is determined by:
  - The `Track`'s **Length**
  - The `Transporter`'s **MU Length**
  - The `Transporter`'s **Speed**
- Unlike point-oriented material flow objects, Plant Simulation uses the actual **Length** typed in during the simulation run.
- A `Transporter` cannot pass another `Transporter` moving in front of it. Transporters retain their order of moving onto and off the `Track` (**FIFO**).
- If a faster `Transporter` collides with a slower one, Plant Simulation activates the **Collision Control** of the faster `Transporter` and automatically reduces its speed to match the slower one.
- The maximum capacity is defined by the `Track`'s length and the lengths of the individual Transporters (e.g., a three-yard Track accepts at most three one-yard Transporters). The **Capacity** can further restrict this number.
- The `Transporter` can drive **forward** and **backward** (drive onto the Track at its Exit and exit at its Entrance). Forward/backward are properties of the `Transporter`, not the `Track`.
- The `Track` can be inserted into a Frame:
  - As a **curved object** (default).
  - By inserting any sequence of **curved segments and straight segments** to model curved conveyor systems.
- Different configurations can be selected on the **Appearance** tab.

## Show Manipulators

- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`.
- The manipulator at the start and end of the length-oriented object is cut off. Attaching an object of the same type recombines the two halves into a complete manipulator.
- Hovering over a manipulator shows a Tooltip.

## Add the Object to the Simulation Model

- Click **Manage Class Library > Basic Objects > MaterialFlow > Track** on the Home ribbon tab.
- Sample models: **Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples**, then select Category, Topic, and Example in the *Examples Collection* dialog and click **Open Model**.

## Routing [Track]

To facilitate a branching Track, Plant Simulation uses (in priority order):

1. The **Exit Control** of the Track (highest priority).
2. **Automatic Routing** of the Transporter (uses destination lists of successors).
3. The **Driving Control** of the Transporter.
4. The **built-in properties** of the Track (moves Transporters to each connected successor in turn).

- If no Exit Control is defined and a destination list is typed for the Transporter, Automatic Routing moves the Transporter to the proper successor using the successors' destination lists.
- The Track has a **Forward Destination List** and a **Backward Destination List**, listing all destinations reachable when driving forward/backward.
- If the Track does not find the destination, it moves the Transporter to the next successor in turn.
- The search terminates after the first instance of the Destination is found.
- Automatic routing is inactive if no Destination is typed for the Transporter, or if an Exit Control is typed for the Track.

## Dialog Box of the Track

- Double-click the icon to open the dialog box.
- **Edit Simulation Properties**: shared properties described under *Dialog Items of the Objects*.
- **Edit Animation Properties** (3D properties):
  - Click **Edit 3D Properties** in the lower left corner of the simulation properties dialog box, or
  - Select the object and press the **spacebar**.
- To manipulate the graphic, click **Show Manipulators** or press `M`.

### Tab Attributes

Settings offered by the object (shared properties under *Tab Attributes*).

#### Length [text box]
- Type the Length of the Track. After insertion, Plant Simulation shows its length here.
- The length and the sum of the lengths of all Transporters on it determine how many Transporters it can accommodate.
- Change the graphic length/anchor points via **Show Manipulators** or pressing `M`.

SimTalk:
- `Length` [SimTalk] — see also `OccupiedLength` [SimTalk]

#### Width [text box]
- Type the Width of the Track.

SimTalk:
- `Width` [SimTalk]

#### Capacity [text box]
- The maximum number of Transporters that may be located on the Track (whole or in part) at any one time.
- Default value `-1` = infinite capacity.

SimTalk:
- `Capacity` [SimTalk]

#### Backward Destination List [text box]
- Click the ellipsis button and select a List object, or type the path to a list.
- Lists all destination objects the Track can reach when the Transporter moves in reverse.
- Evaluated when a Transporter is to be moved to a successor. Plant Simulation searches the destination lists of all succeeding Tracks directly connected with Connectors.
- If a succeeding Track is connected via an Interface, the Interface should have only a single successor (only the first successor is searched).
- Note: moving forward/reverse are properties of the `Transporter`, not the `Track`.

SimTalk:
- `BwDestList` [SimTalk]

#### Forward Destination List [text box]
- Lists all destination objects the Track can reach when the Transporter drives forward.
- Same evaluation rules as the Backward Destination List.

SimTalk:
- `FwDestList` [SimTalk]

### Tab Times
- Define Times as described under *Tab Times*. Select a distribution from the drop-down list and type the required values. Can select a constant time (**Const**).
- Set distribution type and parameters with the method `setTypeAndAttr` [SimTalk].

### Tab Failures
- Define failures as described under *Tab Failures*.

### Tab Controls [Track]
Provides controls to modify the built-in behavior.

**Select the Path to an Existing Method:**
- Click the ellipsis button, navigate to the Method, click OK.
- Press `F2` in the text box to open the Method and type the source code.
- Alternatively, drag a Method from a Frame and drop it into the text box.

**Create a Control That Is a Method of the Object:**
- Type a meaningful name and select **Create Control** — inserts `self.Name_you_typed_in_for_the_control` (e.g., `self.A1Ctrl`).
- Select **Create Control** on an empty text box — inserts `self.OnBuilt_in_name_of_the_control` (e.g., `self.OnEntrance`).

Edit the source code later via:
- Press `F2`
- Hold `Shift` and double-click into the text box
- Select **Open Object** on the context menu
- Click the **User-defined** tab and double-click the Method name

- To delete a control, delete the user-defined attribute (deleting only the name from the text box retains the attribute).
- Sensors can also be created/inserted. Sensors are shown on the graphic; hold `Alt` and double-click a sensor to open the Sensors dialog.

See also: Define Controls for Length-Oriented Objects, Entrance Control, Exit Control, Backward Entrance Control, Backward Exit Control, Pull Control, Shift Calendar.

### Tab Exit
- Select to which successor the object moves the MU. See Blocking (exit strategy) and Strategy (material flow objects).

### Tab Statistics
- Described under *Tab Statistics*.
- View **Resource Statistics** of Stationary Resources: **View > Show Statistics Report**, or right-click in the Frame and select **Show Statistics Report**, or press `F6`.
- See also: Resource Statistics [check box], Resource Type.

### Tab User-defined
- Define your own attributes as described under *Tab User-defined*.

## Navigate Menu
- Commands described under the *Navigate Menu*.

## View Menu
Provides commands to access functions:

| Command | Related Item |
|---|---|
| Refresh | Backward Blocking List |
| Show Statistics Report | Exit Blocking List |
| Show Attributes and Methods | Associated Lockout Zones |
| Contents (material flow objects) | Associated Shift Calendar |
| | Forward Blocking List |

## Tools Menu
- Commands described under the *Tools Menu*.

## Tabs Menu
- Show or hide individual tabs of selected material flow objects (hiding unused tabs opens the dialog faster).
- To apply changed settings, click **OK**, close, and reopen the dialog.
- A check mark appears to the left of displayed tabs.
- **Inherit** turns inheritance of displayed/hidden tabs off or on.

## Help Menu
- Commands described under the *Help Menu*.

## Methods of the Track
The Track provides:
- The method `getRouteLength` [SimTalk].
- The methods of **Curved Objects**.
- The methods of **Material Flow Objects**.
- The methods of **All Objects**.

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (context menu of the Class Library) to show them for the selected Class.
