# Converter

## Description

Use the Converter to model materials handling equipment. If an MU moves onto the Converter it either passes straight through in the conveying direction, or it is lifted onto a laterally moving transport level by a lifting mechanism and then conveyed laterally to the left or to the right.

- If the part enters on **side 1 or 3**, *straight* means the part keeps its conveying direction and exits on the opposite side.
- The insertion direction for lateral movement is from side 3 to side 1 when the insertion direction of the Converter is from left to right (i.e., up to down).
- You can query the side on which the part enters the Converter with the method `getObjectOfSide` [SimTalk].

The Converter can only be connected to a **single object per side**. The numbers designate the side of the Converter at which the MU exits.

### Side definitions (insertion direction left to right)

| Side | Meaning |
|------|---------|
| 3 | laterally to the left |
| 1 | laterally to the right |
| 0 | along the insertion direction (straight through) |

- **Side 3 (laterally to the left):** The MU moves with its front in the direction of motion. After the Converter has lifted the MU, it moves with its left-hand side in the direction of motion. As top-to-bottom is assumed for the insertion direction of lateral movement, the Converter then moves backward and the left side of the MU is the rear as long as the MU is booked on the Converter.
- **Side 1 (laterally to the right):** The MU moves with its front in the direction of motion. After the Converter has lifted the MU, it moves with its right-hand side in the direction of motion.
- **Side 0 (along insertion direction):** The MU moves with its front in the direction of motion and retains that orientation while being conveyed straight through.

## Capacity and conveying behavior

- As long as MUs are only conveyed in one direction, the Converter can accommodate **any number of MUs**.
- If the MU is to change its conveying direction, the Converter can only lift and transport a **single MU**.
- MUs can arrive from all sides and be conveyed to all sides.
- The destination side is determined in the **Strategy Method**. Destination objects can be switched to the respective conveying direction at the same time.
- The **preferred direction** is the direction in which you inserted the Converter; it conveys MUs in this direction without any time delay.
- If an MU leaves the preferred direction, it has to move onto the Converter, is lifted (while the **Moving Time** elapses), and can then exit on either side.
- After conveying an MU to a side, the Converter must be lowered back to its default position before conveying the next part. The lifting/lowering time is specified by the **Moving Time**.

### Connecting predecessors/successors

When connecting the Converter, you can determine with the mouse at which side the Connector docks (left, bottom, top, or right). You can also set the side with the `connect` method of the Connector.

### Length-oriented object

The Converter is length-oriented. You can specify the **Relative Converting Point For Length** and/or the **Relative Converting Point For Width**.

## Note: space requirement at the converting point

If the MU is converted at the converting point, the Converter must provide enough space:

- The distance of the **Booking Point Length** from the rear of the MU can be at most as great as the distance of the converting point for length from the left side of the Converter.
- The distance of the Booking Point Length from the front of the MU can be at most as great as the distance of the converting point for length from the right side of the Converter.
- The distance of the **Booking Point Width** from the left side of the MU can be at most as great as the distance of the converting point for width from side 3 of the Converter.
- The distance of the Booking Point Width from the right side of the MU can be at most as great as the distance of the converting point for width from side 1 of the Converter.

You can select different configurations for the Converter on the tab **Appearance**.

## Display and interaction

- To show a tooltip with information about the Converter, hover with the mouse over it.
- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.
- To add the Converter: **Manage Class Library > Basic Objects > MaterialFlow > Converter** on the Home ribbon tab.

## Dialog Box of the Converter

Double-click the icon to open its dialog box.

- **Edit Simulation Properties:** shared properties are described under *Dialog Items of the Objects*.
- **Edit Animation Properties:** click **Edit 3D Properties** in the lower left corner, or select the object and press the spacebar. To manipulate the graphic, click **Show Manipulators** or press **M**.

## Tab Attributes

### Length [text box]
Type the Length of the Converter. If the MU is conveyed straight through along the insertion direction, its length and the length of the MUs determine how many MUs it can accommodate. If the Converter conveys MUs perpendicular, it must provide enough room for the Length and Width of the MU to completely fit when the booking point is located on the converting point in the center.
- **SimTalk:** `Length`

### Width [text box]
Type the Width of the Converter. Standard width is 1 meter.
- **SimTalk:** `Width`

### Speed [text box]
Type the Speed with which the Converter conveys MUs. Type `-1` for an infinite speed.
- **SimTalk:** `Speed`

### Capacity [text box]
Type the Capacity, i.e., the number of MUs the Converter can hold at one time. Default value `-1` stands for infinite capacity. If the Converter conveys MUs along the insertion direction, Capacity can limit how many MUs it conveys at the same time (it still conveys a single MU at a time).
- **SimTalk:** `Capacity`

### Relative Converting Point For Length
Relative position of the converting point along the length (a value between 0.0 and 1.0). The converting point is where the Converter changes the conveying direction. The location is not shown on the graphic.
- **SimTalk:** `RelConvertingPointL`

### Relative Converting Point For Width
Relative position of the converting point along the width (a value between 0.0 and 1.0).
- **SimTalk:** `RelConvertingPointW`

### Automatic Stop [check box]
Set the Current Speed of the Converter to 0 when it does not transport a part (e.g., empty or blocked). If the Speed is 0, the Energy State changes to Operational.
- **SimTalk:** `AutomaticStop`

### Go to Default Position [check box]
Make the Converter return to its default position after the MU has left. It does not return if an MU is waiting that wants to enter laterally.
- **SimTalk:** `GoToDefaultPosition`

### Strategy [drop-down list]
Select the Strategy according to which the Converter conveys MUs to the next material flow object:

- **Default Exit** — all MUs exit through the Default Exit selected on the successor.
- **Straight** — conveys the MU straight through to the next station. If several equally fast routes exist, the straight-through route is preferred (parts do not have to be singularized). Among equally fast routes, Plant Simulation selects the route where the part must be converted the least.
- **MU Attribute** — conveys MUs according to a built-in or user-defined attribute. Click **Open List** and enter the attribute name, value, and exit side; repeat for each attribute.
- **MU Name** — conveys the MU according to its name. Click **Open List**, enter the MU name and exit side.
- **Method** — conveys MUs according to the attribute `ExitForMU` entered in the Strategy Method.
- **Feed in** — enables MUs from a branch line to enter the main line only if no MU is located on the main line within the **Free Space** (distance between two successive MUs).

> **Note:** The first-come-first-served principle applies for all strategies except **Feed In**. The main conveyor only has precedence for **Feed In**.

- **Method at Converting Point** — determines the target with the attribute `ExitForMU` at the converting point (not before the MU enters). Only available for a Capacity of 1. The MU always stops at the converting point; Plant Simulation then calls the method (e.g., `?.ExitForMU := 1`).

> **Note:** The Strategy Method is not called if the MU has a route and Automatic Routing is activated.

- **SimTalk:** `Strategy`, `Strategy Method`, `ExitForMU`

### Strategy Method [Converter]
Modifies the built-in behavior. The object calls the Strategy Method as soon as the MU wants to exit the Converter. It sets the exit side with the attribute `ExitForMU`. For **Strategy > Method at Converting Point**, it is executed when the MU reaches the converting point.

> **Note:** Do not use an Entrance Control or an Exit Control for determining the target — the point in time at which they are called is too late.

The default strategy method as a user-defined attribute looks like this:

```simtalk
param entranceNo: integer
?.ExitForMU := 0 /* number of exit */
```

- **SimTalk:** `StrategyCtrl`

### Default Exit [drop-down list]
Select the Default Exit for the strategies **Default Exit**, **MU Attribute**, and **MU Name**:

| Value | Meaning |
|-------|---------|
| 1 | laterally to the right in the insertion direction |
| 2 | against the insertion direction |
| 3 | laterally to the left in the insertion direction |
| 0 | along the insertion direction |

- **SimTalk:** `DefaultExit`

### Open List [button]
Opens the exit list for the MUs (for **MU Attribute** and **MU Name** strategies).
- **SimTalk:** `AttributeType`

### Attribute Type [drop-down list]
For **Strategy > MU Attribute**, selects the data type of the attribute that determines the material flow object to which the part moves.

## Tab Times

Define times as described under the Tab Times. Select a distribution and type the required values; use **Const** for a constant time. You can set the distribution type and parameters with `setTypeAndAttr` [SimTalk].

The Converter additionally provides the **Moving Time**.

### Moving Time [drop-down list]
The time it takes the Converter to lift the MU onto a different conveying level, lower itself, and move back to the default position. It always elapses when the Converter changes the direction of the MU and when an MU enters from a side (not along the preferred insertion direction).

With the **Formula** distribution you can type a numeric expression or the name of a Method, and use the anonymous identifier `@` to access the part.

- **SimTalk:** `MovingTime`, `MovingTime.Type`, `putAttributeNamesIntoTable`

## Tab Failures

Define failures as described under the Tab Failures.

## Tab Controls

Provides controls to modify the built-in behavior. Select an existing Method (via the ellipsis button / **Select Object**), or create a control as a user-defined attribute of data type Method:

- Type a meaningful name and select **Create Control** → inserts `self.Name_you_typed_in_for_the_control` (e.g., `self.A1Ctrl`).
- Select **Create Control** on an empty text box → inserts `self.OnBuilt_in_name_of_the_control` (e.g., `self.OnEntrance`).

To edit later: press **F2**, hold Shift and double-click, select **Open Object** on the context menu, or use the **User-defined** tab. To delete, delete the user-defined attribute.

## Tab Statistics

Statistics is described under the Tab Statistics. In addition, the Converter collects:

| Item | Description | Read-only attribute |
|------|-------------|---------------------|
| Moving Empty | Portion of the statistics collection period during which the Converter was raising/lowering itself without conveying an MU | `StatMovingEmptyPortion` |
| Moving Loaded | Portion of the statistics collection period during which the Converter was raising/lowering itself while conveying an MU | `StatMovingLoadedPortion` |

To view Moving Time in the Statistics Report: **View > Show Statistics Report**, right-click in the Frame and select **Show Statistics Report**, or press **F6**.

## Tab Energy

Select energy settings as described on the Tab Energy.

## Tab Costs

While the Converter transports parts, costs accrue from the sum of total investment costs and total operating costs.

> **Note:** Total investment costs only accrue during the Depreciation Period. Costs are allocated to the part proportional to the length of the part relative to the active length of the Converter (a longer part is allocated higher costs). If the Converter is empty, costs remain with the Converter as general costs.

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

## Menus

- **Navigate Menu** — described under the Navigate Menu.
- **View Menu** — provides Refresh, Show Statistics Report, Show Attributes and Methods, and Contents.
- **Tools Menu** — described under the Tools Menu.
- **Tabs Menu** — show/hide individual tabs; click OK, close, and reopen the dialog to apply. The command **Inherit** toggles inheritance of the displayed/hidden tabs.
- **Help Menu** — described under the Help Menu.

## Methods of the Converter

The Converter provides:

- The methods listed in the table of contents.
- The _Methods of Curved Objects.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open the **Show Attributes and Methods** window (via the context menu of the Class Library).

## See also

- Convey Parts Laterally with the Converter (Video: https://youtu.be/hOvdrDnvXXo?si=TgnQivMCDc9eD3nU&t=13)
- Convey Parts According to a Strategy Control
- Convey Parts Laterally According to Their Name
- Data Held in Tabular Form in Attributes [material flow objects]
- Recovery Time / Recovery Time Starts
- Cycle Time
- Resource Statistics [check box] / Resource Type
- Simulate the Accrued Costs of the Machines
- CostAnalyzer topics
