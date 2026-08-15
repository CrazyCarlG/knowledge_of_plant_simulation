# GanttChart

The `GanttChart` object shows the chronological sequence of activities as bars on the time axis.

## Description

The GanttChart visualizes parts on resources. In this context, resources are the **material flow objects**, not the resource objects.

In addition to the mere occupancy data, the GanttChart can also display:
- failures of machines
- pausing times
- blocking times

This way the GanttChart immediately shows which machines or stations are overloaded or have a low utilization, and which production orders or products have long waiting times during the production process.

To show a tooltip with information about the GanttChart, hover with the mouse over it. To change the length of the graphic and the anchor points of the GanttChart, click **Show Manipulators** on the Edit ribbon tab or press `M`.

### Add the Object to the Simulation Model

To add the object GanttChart to your simulation model, click **Manage Class Library > Basic Objects > UserInterface > GanttChart** on the Home ribbon tab.

> **Note:** The object GanttChart is not part of the Plant Simulation standard program package.

> **Note:** If you are using the GanttChart, replace the GanttChart of previous versions with the GanttChart of the current version. Adjust the source code programmed in SimTalk of previous versions to the current version; compare *Methods of the GanttChart* and *Attributes of the GanttChart*.
>
> Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then select the respective Category, the Topic, and the Example in the dialog *Examples Collection*, and click **Open Model**.

## Dialog Box of the GanttChart

Double-click the icon of the GanttChart to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:
- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Collect Data [check box] - GanttChart

To make the GanttChart collect data during the simulation run, select this check box. To deactivate data collection, clear the check box.

**Remarks:** You cannot use the method `setData` and automatically collect the data simultaneously. When you select **Collect Data**, do not call the method `setData`.

## Show Chart [button] - GanttChart

To show the data which the GanttChart collected in the display window, click this button.

**Remarks:** Define how the GanttChart shows the collected data on the tab **Attributes**.

The GanttChart provides two views:

### Resource View

Resource View shows the resources which are occupied by the parts. The GanttChart shows the resources along the vertical axis and the elapsing time along the horizontal axis.

> **Note:** The GanttChart shows the resources in the order in which they processed parts for the first time. The resource which processed a part first is shown in the first lane; the resource which processed a part after that is shown in the lane below, etc. You cannot change the order of the resources.

With the default settings the GanttChart shows a part on all resources with the same color.

### Part View

Part View shows the parts which occupy the resources. The GanttChart shows the parts along the vertical axis and the elapsing time along the horizontal axis.

> **Note:** The GanttChart shows the parts in the order in which they were processed by a resource for the first time. The part which was processed by a resource first is shown in the first lane; the part which was processed after that is shown in the lane below, etc. You cannot change the order of the parts.

With the default settings the GanttChart shows a resource for all parts with the same color. The displayed resource states refer to the resource which is currently occupied by the displayed part.

### Show Longer or Shorter Time Intervals

- To show longer time intervals, hold down `Ctrl` and press the `-` key or roll the mouse wheel backward. This zooms the view in.
- To show shorter time intervals, hold down `Ctrl` and press the `+` key or roll the mouse wheel forward. This zooms the view out.
- To change the displayed time intervals in greater steps, hold down `Shift` in addition to `Ctrl`.
- To return to the default zoom factor, hold down `Ctrl` and press the `0` key.

## Tab Attributes [GanttChart]

Set how the GanttChart shows the data it collected on the tab **Attributes**.

You can:
- Select the **View Mode** (Resource view or Part view).
- Select to **Show Resource Labels** or to hide them.
- Select to **Show Bar Text** or to hide it.
- Select to **Show Resource States** or to hide them.
- Edit **Lanes** on which the Gantt data is shown.

### View Mode

Select the View Mode with which the GanttChart shows the Gantt data.

- **Resource View** shows the resources occupied by the parts (resources along the vertical axis, time along the horizontal axis). The resources appear in the order they first processed parts; the order cannot be changed. For parts being transported by a Transporter or carried by a Worker, Resource View shows the Transporter or the Worker as the resource instead of the Track or the Footpath. With default settings, a part is shown on all resources with the same color.
- **Part View** shows the parts which occupy the resources (parts along the vertical axis, time along the horizontal axis). The parts appear in the order they were first processed by a resource; the order cannot be changed. With default settings, a resource is shown for all parts with the same color.

You can select the view mode on the drop-down list or on the context menu.

The displayed resource states refer to the resource which is currently occupied by the displayed part.

You can adjust the timescale of the GanttChart by holding down `Ctrl` while rolling the mouse wheel:
- Hold down `Ctrl` and roll the mouse forward to show shorter time intervals (additional details).
- Hold down `Ctrl` and roll the mouse backward to show shorter time intervals (a rough overview).

When you roll the mouse over a bar, **Resource View** highlights the respective part on all resources; **Part View** highlights the respective resource for all parts. This way you can follow the way of the part across the simulation.

- In **Resource View** the Tooltip shows the name of the part, its absolute path, the start date, the end date, and the duration. If several parts are located on the same station, the Tooltip shows information about these parts; the part that moved last onto the station is at the top of the list.
- In **Part View** the Tooltip shows the name of the part, the occupied resource, the start date, the end date, and the duration.

Resource View refreshes the display continuously during the simulation. Part View must be refreshed manually by pressing `F5` or selecting the context menu command **Refresh**.

- To show the labels of the resource objects instead of their names, use **Show Resource Labels**.
- To show or hide the Gantt bar text of the resources, use **Show Bar Text** (bar texts can overlap).
- To show or hide the resource states, use **Show Resource States**.
- To set the distance of the Gantt bars to the top and the height of the bars, use **Edit Lanes**.
- To set whether the GanttChart shows the parts which occupy resources in Part View or the occupied resources in Resource View, use the attribute `ShowPartView`.

### Show Resource Labels [check box]

To show the labels of the resources, select this check box. To hide the labels and show the names instead, clear the check box.

### Show Bar Text [check box]

To show the text on the Gantt bars, select this check box. Bar texts can overlap; the bar text shows the name of the part. To hide the bar text of the resource, clear the check box.

### Show Resource States [check box]

To show the states of the resources as colored bars below the timeline, select this check box. The colors of the parts are the same as the state colors of the objects (compare *States of the Material Flow Objects*). To hide them, clear the check box.

### Edit Lanes

Click **Edit Lanes** and enter the distance of the Gantt bars to the top and the height of the bars themselves. To apply the changed values, click **Apply** in the dialog *getLanes* and then **Apply** in the dialog of the GanttChart.

The GanttChart always collects data in lane 1. Specify your own data with the method `setData` to distribute them across several lanes.

## Tab Parts [GanttChart]

Add the parts that the GanttChart is to display on the tab **Parts**.

**Remarks:**
First, clear the check box **Inheritance** so that it looks like unchecked. Then drag the part types you would like to watch from the Class Library to an empty row on the tab.

Instead, you can also select the part in the Class Library, drag it on the icon of the GanttChart, and drop it there. This automatically deactivates inheritance and adds the part to an empty row on the tab **Parts**.

You can watch classes of parts or individual instances of parts. You can edit the content of the text boxes with the commands on the *Context Menu of Embedded Lists*.

## Tab Resources [GanttChart]

Add the resources that the GanttChart is to display on the tab **Resources**.

**Remarks:**
The GanttChart considers the material flow objects as resources, not the resource objects.

If you want to watch all resources in the simulation model, leave the tab **Resources** empty. The GanttChart then shows all resources on which parts (set on the tab **Parts**) move during the simulation.

First, clear the check box **Inheritance** so that it looks like unchecked. Then drag the resource types you would like to watch from the Class Library to an empty row on the tab.

Instead, you can also select one or several resources in the Frame, drag them on the icon of the GanttChart, and drop them there. This automatically deactivates inheritance and adds the resources to an empty row each on the tab **Resources**.

You can watch resource classes or individual resource instances. You can edit the content of the text boxes with the commands on the *Context Menu of Embedded Lists*.

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

## Navigate Menu

The commands are described under the *Navigate Menu*.

## View Menu

The commands are described under the *View Menu*.

## Tools Menu

The Tools Menu provides commands to access its functions:
- Edit Controls
- Edit Observers

## Help Menu

The commands are described under the *Help Menu*.

## Methods of the GanttChart

The GanttChart provides:
- The methods listed in the table of contents to the left.
- The *Methods of All Objects*.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods** (the figure illustrates this using the example of the object Station):
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected *Class*.
- Press the `F8` key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected *Instance*.

---

## SimTalk Reference

### ZLabel [SimTalk]

Sets the label of the z-axis that the Chart designated by `<Path>` shows in the Chart window.

**Remarks:** Applies to the 3D chart types 3D Columns, 3D Wire Frame, and 3D Surface.

**Type:** Attribute

**Syntax**

```
<Path>.ZLabel:string
```

**Assignment Value:** You can assign a value of data type string.

**Example**

```
MyChart.ZLabel := "Number of Stacked Rows"
```

**See also:** Z-Axis [text box] - Chart

### SimTalk Methods and Attributes Referenced

- `CollectData [SimTalk]` - GanttChart
- `IsShown [SimTalk]` - GanttChart
- `setData [SimTalk]`
- `getData [SimTalk]`
- `setLanes [SimTalk]`
- `getLanes [SimTalk]`
- `ShowPartView [SimTalk]`
- `ShowResourceLabels [SimTalk]`
- `ShowBarText [SimTalk]`
- `ShowResourceStates [SimTalk]`
- `Parts [SimTalk]`
- `Resources [SimTalk]` - GanttChart
- `updateDialog [SimTalk]`
