# Interface

## Overview

The **Interface** object models transitions between Frames, i.e., from one part of the model to another. It also facilitates hierarchic modeling.

The Interface, which can be an **entrance** or an **exit**, is the place at which MUs move from one Frame to another in the simulation model. You can position the Interface anywhere in a Frame and address these connections via their names.

Key rules:

- You always have to insert Interfaces into a sub-Frame when it contains more than one material flow object. If a sub-Frame contains Interfaces, the materials always flow across these.
- For an Interface inserted into a Frame, Plant Simulation shows whether the Interface is connected to another object with a Connector, and recognizes if it is an Entrance or an Exit.
- If the sub-Frame only contains a single material flow object, you do not have to insert Interfaces, but can connect the sub-Frame directly with its predecessor and successor. Connections without Interfaces only work across a single lower hierarchy level, not across several nested hierarchy levels.
- If Interfaces are inserted into the model, the simulation in 3D runs across these Interfaces.

## Working with Interfaces

- To open the list showing all externally connected objects, select **Open External Connections List** on the context menu or **Tools > External Connections** in the dialog.
- To show a tooltip containing the externally connected objects, roll the mouse over the Interface in the Frame.
- To select the objects connected with this Interface, select **Show External Connected Objects** on the context menu.
- The Interface shows the number of the next selected exit on the tab **Exit**, provided you already determined it (e.g., by calling the method `succ` for the successor object).

## Adding the Object to the Model

To add the Interface object, click **Manage Class Library > Basic Objects > MaterialFlow > Interface** on the Home ribbon tab.

## Dialog Box

Double-click the icon of the Interface to open its dialog box.

- **Edit Simulation Properties**: change the simulation properties of the object (shared properties described under *Dialog Items of the Objects*).
- **Edit Animation Properties**: click **Edit 3D Properties** in the lower left corner, or select the object and press the spacebar.
- To manipulate the graphic, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Tab Attributes

### Type [Interface]
An Interface object, inserted into a Frame and connected with a Connector, shows its type. The Interface can be:
- An **Entrance** interface through which MUs enter the Frame.
- An **Exit** interface through which MUs exit the Frame.

### Maximum Number of External Connections [Interface]
Type in the maximum number of external connections the Interface may have. Depending on the type, any number of Interfaces may have more than one predecessor or successor. The default value `-1` designates an unlimited number of external connections.

### Side [drop-down list]
Select the side at which Plant Simulation places the Interface. Options: **Top**, **Right**, **Bottom**, **Left** of the Frame, or **Angle-dependent** (takes the angle between the objects into account when determining the start/end point of the Connector).

### Position in % [Interface]
Type in the position at which Plant Simulation shows an arriving or leaving Connector at the icon of the Frame. Value between `0` and `100`%. Position 0 is the top or left-hand side, position 100 the bottom or right-hand side.

Plant Simulation uses this value when you activate **File > Preferences > General > Connect Objects Automatically**. Connecting objects automatically only works if the exit of FrameA and the entrance of FrameB are not more than three pixels apart.

## Tab Exit [Interface]

Select to which of its successors the object moves the MU on the tab **Exit**.

Notes:
- If Plant Simulation determines the n-th successor (e.g., with `print MyStation.succ(n)`) and the n-th successor is an Interface, Plant Simulation returns the successor of the Interface according to the Exit strategy, not the Interface itself.
- If a non-blocking exit strategy is selected, Plant Simulation returns the next available successor according to the exit strategy, or `VOID` when no successor can receive parts.
- When the Interface has a single successor, Plant Simulation returns this successor even with a non-blocking exit strategy, even if the successor is occupied or failed/paused.

## Tab User-defined
Define your own attributes (described under *Tab User-defined*).

## Menus

### Navigate Menu
Commands described under the *Navigate Menu*.

### View Menu
- **Refresh**
- **Show Attributes and Methods**
- **External Connections**: opens a table displaying the paths of the external connections in the Frame. Column **Connector** designates the Connector at the exit of the Frame; column **Object** designates the object name of the succeeding object. (Also available via context menu **Open External Connections List**.)
- **Forward Blocking List**

### Tools Menu / Help Menu
Commands described under the respective menus.

## Methods

The Interface provides the *Methods of All Objects*. View them via **Show Attributes and Methods** (context menu of the Class Library for the Class, or the F8 key / Home ribbon tab for the Instance).

An example of the Syntax line:

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## SimTalk References

| Topic | SimTalk |
|---|---|
| Unplanned (Frame) | `<Path>.Unplanned:boolean` |
| Type | `IsEntry [SimTalk]`, `IsExit [SimTalk]` |
| Maximum external connections | `MaxConnections [SimTalk] - Interface` |
| Side | `Side [SimTalk]` |
| Position | `Position [SimTalk] - Interface` |
| View menu | `updateDialog [SimTalk]` |

### Unplanned Example

```simtalk
EngineAssembly.Unplanned := false
```

Set `false` to set it to planned to work; the Frame is unplanned when the current time is outside any shift of the ShiftCalendar to which the Frame is assigned.

## See Also
- States of the Frame
- Unplanned [state, material flow objects]
- Model Transitions Between Frames
- Adapt the 3D Model to the 2D Model
- Connect Objects Automatically [model settings]
- Tab Exit [general description]
- Blocking [exit strategy]
- Strategy [material flow objects]
