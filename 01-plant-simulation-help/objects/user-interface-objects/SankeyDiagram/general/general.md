# SankeyDiagram — General

## SankeyDiagram [object]

The `SankeyDiagram` object visualizes Sankey flows of:
- Parts
- Workers (walking freely within the area or on FootPaths)
- AGVs (driving freely within the area of the model)

### Description

- To show Sankey flows of **class objects**, drag the classes `Part`, `Container`, `Worker`, `WorkerPool`, `Transporter`, or `AGVPool` from the Class Library over the picture of the `SankeyDiagram` and drop it there.
- To show Sankey flows of **individual instances** of `Part`, `Container`, `Worker`, `WorkerPool`, `Transporter`, or `AGVPool`, type the name of the instance into the cell of the list on the tab **Objects**, for example `.MUs.Part:3`.
- Hover the mouse over the `SankeyDiagram` to show a tooltip with information about it.
- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`.

### Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > UserInterface > SankeyDiagram** on the Home ribbon tab.

## TimeScale [SimTalk]

Sets the time scale of the `GanttChart` designated by `<Path>`. Plant Simulation applies this value when opening the `GanttChart`.

**Remarks:** The unit of the time scale is logical pixels per second. For a time scale of `0.5`, Plant Simulation shows a Gantt event with a duration of 60 seconds with a bar of 30 logical pixels.

- **Type:** Attribute
- **Syntax:** `<Path>.TimeScale:integer`
- **Assignment Value:** You can assign a value of data type `real`. Specify `0` to use the default time scaling.

```simtalk
MyGanttChart.TimeScale := 2.5
```

## Dialog Box of the SankeyDiagram

Double-click the icon of the `SankeyDiagram` to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:
- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Show Diagram

To show the Sankey flows in the Frame, click **Show Diagram**. To hide the Sankey flows, click **Hide Diagram**.

**Remarks:**
- Instead, you can also select the context menu command **Show/Hide**.
- Click **Update** to update the displayed Sankey flows with the current values.

## Collect Data [check box] — SankeyDiagram

To make the `SankeyDiagram` collect data, select this check box. To deactivate the collection of data, clear the check box.

## Maximum Width [SankeyDiagram]

Type the maximum width of the Sankey flows into the text box, which visualize the paths of parts and Workers in the Frame.

## Color [SankeyDiagram]

Select the color of the Sankey flows which visualize the paths of the parts and Workers in the Frame.

## Tab Attributes

The tab **Attributes** provides the settings that the object offers. The shared properties are described under *Tab Attributes*.

## Tab Objects

On the tab **Objects** you can assign objects to the `SankeyDiagram` for which it is to display Sankey flows.

### Objects [SankeyDiagram]

To show the Sankey flows for class objects, drag parts classes (`Part`, `Container`, `Transporter`), Worker classes, or WorkerPool classes from the Class Library over the respective cell in the list and drop it there.

**Remarks:** To show Sankey flows of individual parts (`Part`, `Container`, `Transporter`), Worker instances, or WorkerPool instances, type their names into the respective cells of the list, for example `.MUs.Part:3`.

**Note:** If inheritance of the objects on the tab is activated, the `SankeyDiagram` replaces the default object class with the class which you set with drag-and-drop. This makes switching the `SankeyDiagram` from parts to Workers easy, for example.

## Tab User-defined

Define your own attributes as described under *Tab User-defined*.

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

## Methods of the SankeyDiagram

The `SankeyDiagram` provides:
- The methods listed in the table of contents to the left.
- The **Methods of All Objects**.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press `F8` or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## See Also

- Show Chart [button] — GanttChart
- Show Part Flows in a SankeyDiagram
- Show AGV Flows in a SankeyDiagram
- Display a SankeyDiagram in the HtmlReport
- Update [in Frame]
- IsShown [SimTalk] — SankeyDiagram
- CollectData [SimTalk] — SankeyDiagram
- MaximumWidth [SimTalk]
- Color [SimTalk] — SankeyDiagram
- Objects [SimTalk] — SankeyDiagram
- updateDialog [SimTalk]
- Tools Menu [general description]
