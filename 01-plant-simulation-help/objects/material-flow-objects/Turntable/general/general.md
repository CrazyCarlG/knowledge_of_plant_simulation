# Turntable

The **Turntable** object models a rotating platform that moves a part onto one of several connected material flow objects and/or turns it around.

## Description

The Turntable has a **capacity of one** — only one part can be located on it at any one time. The length of the MU must not be longer than the **Length** of the Turntable itself.

### How the Turntable moves parts to its successors

- The MU arrives at the exit of the predecessor and notifies the turntable that it wants to be rotated.
- The turntable determines whether it accepts the MU for rotation:
  - Without a **Pull Control**, the turntable is notified that a MU wants to be rotated and accepts it.
  - With a **Pull Control**, the turntable executes it; when the MU is selected, it is rotated.
- The turntable rotates to the respective predecessor, and the MU moves onto it.
- Once one of the following conditions is met, the turntable looks for the target station and starts rotating toward it:
  - The MU has completely entered the turntable.
  - The MU has reached the rotation point on the table.
  - The part is located in the center of the turntable (both ends of the part have the same distance from the ends of the turntable).
  - For manual control, select **User-defined with Sensor**; in the **Sensor Control**, tell the turntable to call the method `setDestination`.
- The turntable determines the target station using its default exit strategies or the **Target Control**. Within this method, set the target station with `setDestination`.

> **Note:** Do not use an **Exit Control** for determining the target of the MU — an Exit Control is called only when the MU is ready to exit the Turntable, which is too late.

- The turntable rotates to the target and the MU moves on once the final rotation position is reached. Only then can a new MU move onto the Turntable (Capacity of 1).

> **Note:** Query the current rotation angle with the read-only attribute `CurrentAngle [SimTalk]`.

> **Note:** If an object from/onto which the MU is to be moved does not exist in the respective angle table, the Turntable checks the **Exit Angle Table** (for an entering MU) or the **Entry Angle Table** (for a leaving MU), and otherwise uses the angle from the layout in the Frame.

You can select different configurations on the tab **Appearance** of the Length-oriented Objects.

An animatable object with **Velocity** of 0 does not rotate with the Turntable when it rotates, if its insertion position is located on the animation rotation axis (the insertion point is exactly on the animation rotation center, or reachable from there along the axis without sideways deviation). This resembles a real turntable with a fixed base and a rotary table.

## Adding the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > MaterialFlow > Turntable** on the Home ribbon tab.

Sample models: **Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples**, then select the Category, Topic, and Example in the **Examples Collection** dialog, and click **Open Model**.

## See also

- Move Parts On with the Turntable
- Video on YouTube: https://youtu.be/hOvdrDnvXXo?si=Cs5gOF4JB5PBlVma&t=532

---

# Dialog Box of the Turntable

Double-click the icon of the Turntable to open its dialog box.

- **Edit Simulation Properties** — change the simulation properties (shared properties are described under *Dialog Items of the Objects*).
- **Edit Animation Properties** — edit the 3D properties in **Edit 3D Properties**:
  - Click **Edit 3D Properties** in the lower left corner of the simulation properties dialog box, or
  - Select the object and press the spacebar.
- Click **Show Manipulators** on the Edit ribbon tab or press `M` to manipulate the graphic.

## Tab Attributes

### Length [text box]
The **Length** of the Turntable. The Turntable only rotates parts that are shorter than or as long as this value.

SimTalk: `Length [SimTalk]` — see also `OccupiedLength [SimTalk]`.

### Width [text box]
The **Width** of the Turntable.

SimTalk: `Width [SimTalk]`.

### Rotation Point [text box]
The position of the fulcrum around which the Turntable rotates. A value between 0 and the Length of the Turntable; 0 designates the start point of insertion.

- **Center of Rotation** — the fulcrum around which the table rotates.
- **Start Point** — where you click to start inserting the Turntable.
- **End Point** — where you click to finish inserting the Turntable.

SimTalk: `RotationPoint [SimTalk]`.

### Conveyor Speed [text box]
The speed with which the Turntable transports the MU while it is on the table.

SimTalk: `Speed [SimTalk]` — see also `Velocity [joint]`.

### Rotation Time per 90° [text box]
The time it takes the Turntable to rotate by 90 degrees. To rotate the MU immediately, type 0.

SimTalk: `RotationTimePer90Degrees [SimTalk]`.

### Rotate When [drop-down list]
Select when the Turntable rotates toward its target object:

- When the MU has completely entered the Turntable.
- When the MU has reached the rotation point / fulcrum on the table.
- When the MU is located in the center of the Turntable (both ends have the same distance from the edges).
- **User-defined with Sensor** — the Turntable does not rotate automatically; in the Sensor Control, call `setDestination`.

SimTalk: `RotateWhen [SimTalk]`.

### Go to Default Position [check box]
Rotate the Turntable back to its **Default Position** when the MU has left and no new MU is ready to be rotated. When selected, the Turntable uses the **Default Angle** when the model is reset.

SimTalk: `GoToDefaultPosition [SimTalk]` — see also `Default Angle` / `DefaultAngle [SimTalk]`.

### Default Angle [text box]
The angle to which the Turntable rotates when **Go to Default Position** is selected. To rotate to the side on which the start point is located, add 180 degrees.

SimTalk: `DefaultAngle [SimTalk]`.

### MU Leaves Backwards Depends On
Name of a user-defined attribute of the MU that triggers rotation so it exits driving backward. This can be a boolean attribute or a Method returning a boolean. Evaluated only when **Any** is selected as the side in the **Exit Angle Table**.

SimTalk: `MURotationAttribute [SimTalk]`.

### Entry Angle Table
Opens the table of Entry Angles at which MUs move onto the Turntable. Settings:

- Number and name of the Predecessor.
- Angle at which the Connector from the predecessor connects to the Turntable.
- At which side it turns toward the predecessor:
  - **Start Point** — turns the side where insertion started toward the predecessor.
  - **End Point** — turns the side where insertion finished toward the predecessor.
  - **Any** — computes the smallest angle and turns with that side toward the predecessor.

> **Note:** The button is only active after connecting the Turntable with its predecessor. To compute the angles, right-click and select **Calculate Angles**.

SimTalk: `setEntryAngles [SimTalk]`, `getEntryAngles [SimTalk]`, `calculateAngles [SimTalk]`.

### Exit Angle Table
Opens the table of Exit Angles at which MUs leave the Turntable. Settings:

- Number and name of the Successor.
- Angle at which the Connector from the Turntable connects toward the successor.
- At which side it turns toward the successor:
  - **Start Point** / **End Point** — as above, toward the successor.
  - **Any** — computes the smallest angle; the MU can leave backward or forward.
  - **MU keeps Direction** — turns the side that makes the MU keep its direction.
  - **MU leaves backward** — turns the side so the Turntable turns the MU around and it leaves backward. Compare **MU Leaves Backwards Depends On**.

> **Note:** The button is only active after connecting the Turntable with its successor. To compute the angles, right-click and select **Calculate Angles**.

SimTalk: `setExitAngles [SimTalk]`, `getExitAngles [SimTalk]`, `calculateAngles [SimTalk]`.

### Automatic Stop [check box]
Sets the Current Speed of the Turntable to 0 when it does not transport a part (e.g., empty or blocked). If speed is 0, the Energy State changes to Operational.

SimTalk: `AutomaticStop [SimTalk]`.

## Tab Times
Define Times as described under the Tab Times. Select a distribution and type the required values; a constant time (**Const**) is also possible.

> **Note:** The Turntable does not provide the **Cycle Time**. Set the distribution type and parameters with `setTypeAndAttr [SimTalk]`.

## Tab Failures
Define failures as described under the Tab Failures.

## Tab Controls
Provides controls to modify the built-in behavior of the object.

**Select the Path to an Existing Method:** click the ellipsis button and navigate to the Method in **Select Object [for controls]**, then click OK. Press `F2` in the text box to open and edit the Method. Alternatively, drag a Method from a Frame and drop it into the text box.

**Create a Control That Is a Method of the Object:**
- Type a name into the text box and select **Create Control**; Plant Simulation inserts `self.Name_you_typed_in`, e.g. `self.A1Ctrl`.
- Or select **Create Control** on an empty text box; Plant Simulation inserts `self.OnBuilt_in_name_of_the_control`, e.g. `self.OnEntrance`.

Edit the source code via `F2`, `Shift`+double-click, **Open Object**, or the **User-defined** tab. To delete, delete the user-defined attribute.

See also: Entrance Control, Exit Control, Pull Control, Target Control.

### Target Control
Called as soon as the MU has completely moved onto the Turntable or reached the center of rotation. Unlike the Exit Control, the MU is not yet ready to exit.

> **Note:** Do not use an Exit Control to determine the target — it is called too late.

The standard target control looks like this:

```simtalk
TargetCtrl [SimTalk] - Turntable
```

See also: `setDestination [SimTalk]`, `getDestination [SimTalk]`.

## Tab Exit
Select to which successor the object moves the MU. See also *Blocking [exit strategy]* and *Strategy [material flow objects]*.

## Tab Statistics
Statistics are described under the Tab Statistics. In addition, the Turntable collects:

| Item | English Description | Read-only attribute |
|------|---------------------|---------------------|
| Rotation Empty | Portion of the collection period during which the object was rotating empty (without moving a part). | `StatRotationEmptyPortion [SimTalk]` |
| Rotation Loaded | Portion of the collection period during which the object was rotating while moving a part. | `StatRotationLoadedPortion [SimTalk]` |

To view Rotation Time in the Statistics Report, select **View > Show Statistics Report**, right-click in the Frame and select **Show Statistics Report**, or press `F6`.

## Tab Energy
Select energy settings on the Tab Energy.

## Tab Costs
Select costs settings on the Tab Costs. Costs accrue while the Turntable transports MUs, resulting from total investment costs and total operating costs.

> **Note:** Total investment costs only accrue during the Depreciation Period. If the Turntable is empty, costs remain with the Turntable as general costs.

## Tab User-defined
Define your own attributes as described under the Tab User-defined.

## Menus

- **Navigate Menu** — described under the Navigate Menu.
- **View Menu** — provides: Refresh, Show Statistics Report, Show Attributes and Methods, Contents, Forward Blocking List, Backward Blocking List, Exit Blocking List, Associated Lockout Zones, Associated Shift Calendar.
- **Tools Menu** — described under the Tools Menu.
- **Tabs Menu** — show or hide individual tabs of the selected material flow objects. Hiding unused tabs opens the dialog faster. To apply changes, click OK, close, and reopen. **Inherit** turns inheritance of displayed/hidden tabs on or off.
- **Help Menu** — described under the Help Menu.

---

# Methods of the Turntable

The Turntable provides:

- The methods listed in the table of contents.
- The Methods of Curved Objects.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (select it on the context menu of the Class Library).
