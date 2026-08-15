# AGVPool (General)

## Code Example

```simtalk
t.create
obj.imp.getAlternativeServices(t)
service := t[1,1][1,1]
part := @ --if part.id = 4 then debug 
end
tab.create; allWorker := WorkerPartAssignment
if part /= void 
    j := allWorker.getRowNo(part)
    if j = -1 
        j := 1
        while j<= allWorker.yDim AND allWorker[0,j]/=void 
            j := j + 1
        end
        if j<= allWorker.yDim 
            allWorker[0,j] := part
            expObj := allWorker[1,j]
            tab.writeRow(1,1, expObj, service, 1 )
            broker.engage( obj, type, tab )
        end
    else
        expObj := allWorker[1,j]
        tab.writeRow(1,1, expObj, service, 1 )
        broker.engage( obj, type, tab )
    end
end
```

Related: `engage` [SimTalk], see also **Importer Request Control [Broker]**.

## Overview

The **AGVPool** object is used for creating automated guided vehicles (AGVs). It lets you model AGV
systems in which the AGVs are **not bound to a permanently installed route network**.

Use it to model the supervisor of a plant or the foreman of a shop. The AGVPool creates automated
guided vehicles, enabling AGV systems where vehicles are not tied to fixed routes.

This is especially helpful for producing smaller lot sizes with a high variant mix on a single
production line. Instead of fixed production lines, AGVs transport loaded products through a
modular installation. The AGVs can create and change virtual tracks depending on the situation.

The AGVPool initially does not show any AGV. To show them:
1. Select the check box **Show Content** on the tab **Graphics** of the AGVPool.
2. Click **Start Simulation**.

Use the object **Marker** to set waypoints along which the AGV drives from the AGVPool to its
destination.

Hover over the AGVPool with the mouse to show a tooltip. To change the length of the graphic and the
anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.

### Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > Resources > AGVPool** on the Home ribbon tab.

See also: *Model an Automated Guided Vehicle System (AGVS)*, *Dialog Box of the AGVPool*.

## Dialog Box of the AGVPool

Double-click the icon of the AGVPool to open its dialog box.

### Edit Simulation Properties
Change the simulation properties of the object here. Shared properties are described under
*Dialog Items of the Objects*.

### Edit Animation Properties
To edit the 3D properties in the dialog **Edit 3D Properties**:
- Click **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic, click **Show Manipulators** on the Edit ribbon tab or press **M**.

## Tab Attributes

The tab **Attributes** provides the settings the object offers. Shared properties are described under
the *Tab Attributes*.

### AGV [text box]
Select the vehicle to use for the Automated Guided Vehicle (AGV) of the Automated Guided Vehicle
System (AGVS).

> **Note:** By default, the **Transporter** in the folder *MUs* in the Class Library is the AGV. For
> this reason the methods, attributes, and read-only attributes of the Transporter apply to the AGV as
> well.

Plant Simulation creates the specified **Amount** of AGVs during the init phase of the simulation run.

For a freely driving AGV, these **Distance Control** settings can be defined:
- Length Zone 1
- ΔWidth Zone 1
- Length Zone 2
- ΔWidth Zone 2

SimTalk references: `AGV`, `AGVPool` (of the Transporter), `StoppingCounter` (of the Transporter).
See also: `setRoute` [SimTalk - Transporter], `setRouteSegments` [SimTalk].

### Amount [text box] - AGVPool
Type in the number of vehicles to use for the AGVS.

Plant Simulation creates the specified amount of AGVs during the init phase of the simulation run.

SimTalk: `Amount` [SimTalk - AGVPool].

### Shift Calendar [AGVPool]
Select the **ShiftCalendar**, which contains the shift data and controls during which shifts the
AGVPool works.

- Click the ellipsis button and select the ShiftCalendar in the dialog *Select Object*.
- Or select the ShiftCalendar in a Frame, drag it to the text box and drop it. Plant Simulation then
  automatically enters the objects into the list on the tab **Resources** of the ShiftCalendar.

Edit the contents of the text boxes with the commands on the *Context Menu of Embedded Lists*.

SimTalk: `ShiftCalendarObject` [SimTalk - material flow objects].
See also: *ShiftCalendar [object]*, *Select Object [for controls]*.

## Tab Statistics [AGVPool]

The tab **Statistics** shows the most important statistics values.

| Item | Description | Read-only attribute | German |
|------|-------------|---------------------|--------|
| Paused | Portion of the statistics collection period during which the AGVPool was paused. | `StatPausingCount` [SimTalk] | Pausiert |
| Unplanned | Portion of the statistics collection period during which the AGVPool was unplanned (not scheduled to work). | `StatUnplannedPortion` [SimTalk] | Ungeplant |
| Average Traveled Distance | Average distance in meters the AGV traveled from the AGVPool to its destination. | `StatAverageTraveledDistance` [SimTalk - AGVPool] | Durchschnittlich zurückgelegter Weg |

To view Resource Statistics of Stationary Resources in the Statistics Report: select
**View > Show Statistics Report** in the dialog, click **Show Statistics Report** on the Home ribbon
tab, or right-click the object in the Frame and select **Show Statistics Report**.

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

## Navigate Menu

Commands are described under the *Navigate Menu*.

## View Menu

The View Menu provides commands to access its functions:
- Refresh [on View menu]
- Show Attributes and Methods [on View menu]
- Assigned AGVs [AGVPool]
- Associated Shift Calendar

SimTalk: `updateDialog` [SimTalk].
See also: *View Menu [general description]*.

### Assigned AGVs [AGVPool]
Opens a list showing all the AGVs that the AGVPool manages.

SimTalk: `getAssignedAGVsTable` [SimTalk].

## Tools Menu

The Tools Menu provides these menu commands:
- Edit Controls > Init control
- Edit Observers

## Help Menu

Commands are described under the *Help Menu*.

## Methods of the AGVPool

The AGVPool provides:
- The methods listed in the table of contents.
- The *Methods of All Objects*.

To view all methods, read-only attributes, and attributes of the object, open the window
**Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the members
  of the selected *Class*.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which
  you inserted an instance, to show the members of the selected *Instance*.
