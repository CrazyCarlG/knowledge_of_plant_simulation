# Worker [object]

Use the object **Worker** for doing a job on a Workplace at a station.

## Description

The Worker–WorkerPool–Workplace–FootPath concept refines the Broker–Importer–Exporter concept. Unlike the Exporter, the Worker consumes time when walking to the Workplace at which he does his job. The Worker has the same statistics values as the Exporter, and additionally provides a statistics value for being *En-route to the Job*.

If your Worker does not walk, make sure the importer on the **Importer** tab of the station is activated, on whose Workplace the Worker is to work.

The Workers are created in the WorkerPool and stay there if they are not working and waiting for a work order. As a rule you type names of Workers into the **Workers to Create** table, or drag Workers from the Class Library onto the WorkerPool icon. You can also create individual Workers with the method `create` for a single simulation run (only in the WorkerPool). Plant Simulation deletes such a Worker when you reset the model and only creates Workers from the **Workers to Create** table at the next Init event.

The **Broker** brokers Workers to work stations. As soon as a Worker can provide a service, the Broker sends him from the WorkerPool to the requesting work station.

Notes:
- A paused Worker always returns to the WorkerPool. A failed Worker stays at the Workplace.
- A Worker who is automatically brokered does not return to the WorkerPool when he becomes paused or unplanned while staying at the Workplace.
- A Worker who is not automatically brokered stays at the Workplace to which he was sent, no matter if **Worker Stays Here After Completing the Job** / `WorkerStaysHere` is activated in the Workplace.
- A Worker walks to the closest Workplace if several Workplaces are assigned to the work station.

The SankeyDiagram visualizes the paths of the Worker who walks freely within the area. To show a tooltip with information about the Worker, hover over it with the mouse. To show statistics of the Workers managed by the WorkerPool, drag it over a Chart and drop it there.

### Add the Object to the Simulation Model
Click **Manage Class Library > Basic Objects > Resources > Worker** on the Home ribbon tab.

## Travel Mode [drop-down list]

The Travel Mode determines how the Worker finds the shortest route from the WorkerPool and the Workplaces and between the Workplaces. Selectable modes:

- Move freely within area
- Walk along footpaths
- Beam to workplace

### Move freely within area
Makes the Worker walk freely within the area of the simulation model and walk around the obstacles which you defined.

Plant Simulation automatically computes the shortest route between the Workplaces and between the WorkerPool and the Workplaces, using the 3D layout of the model. Obstacles (walls, pillars, machines, conveyors, safety fences, etc.) are automatically detected as **Barred Areas**. By default, material flow objects, animatable objects, and graphics belonging to the Frame are marked as Barred Areas; information flow objects and user interface objects are not. Set this under **Edit 3D Properties > Tab Graphics > Obstacle for the Worker** (or **Graphic Settings** for graphics).

To designate an area the Worker can enter but should not (e.g. the pivoting area of a crane), manually create a Barred Area. To let the Worker walk around or through obstacles, use a FootPath (e.g. a FootPath through a door in a wall; the FootPath must be a little longer than the depth of the wall).

The decisive length is the FootPath length **in the scene**, not the length typed on the Attributes tab. The distance covered is determined by the start/end points and anchor points.

Inclines: the Worker moves slower on an incline. Plant Simulation triples the height difference when computing the effective length of an inclined segment. Example: a segment of 1 m in x and 1 m in z is actually 1.414 m, but the imagined dimensions are 1 m x and 3 m z, giving an effective length of 3.162 m.

The Worker always walks the route with the shortest effective length (which he can cover in the shortest time), which can cause him to take a longer but flatter route. Speed decreases to a third when moving vertically (climbing a ladder) and to about half on a 38-degree incline (a stairway).

To get to a different floor, the Worker must walk a ramp on a FootPath or Stairs (see example model *Factory 51*).

**SimTalk:** `WorkersTravelMode [SimTalk]`

### Walk along footpaths
Makes the Worker walk on the Footpaths inserted between the Stations/Workplaces.

Insert FootPaths to model distances between the WorkerPool and work stations or between stations. Link several FootPaths with Connectors to create a network. If the WorkerPool and the Workplace are connected to the same network, the Worker walks the shortest possible route.

The time taken depends on his **Speed** and the combined **Lengths** of the FootPaths. Plant Simulation recognizes on which FootPaths the Worker walks if he exits a FootPath at another end than the one at which he entered. If he does not walk on a FootPath (or is beamed), he consumes no time.

**SimTalk:** `WorkersTravelMode [SimTalk]`

### Beam to workplace
Beams (teleports) the Worker to the Workplace to which he was brokered, instantly and without using time, provided he cannot get there on any Footpath. In this case the Worker functions as an Exporter with a capacity of 1.

Useful for building a model without FootPaths; the Worker always jumps between the WorkerPool and the Workplaces.

**SimTalk:** `WorkersTravelMode [SimTalk]`, `teleportTo [SimTalk]`, `teleportToHome [SimTalk]`, `teleportToPool [SimTalk]`

## How the Worker Decides Where to Work

While brokering, the Broker and the Worker proceed as follows:

1. The Broker first checks the **Priority** of the current request in the Worker dialog. If the job has the highest priority, he stays on the current Workplace and finishes the job.
2. The Worker then checks if the material flow object to which the Workplace is assigned has a **Scope** with the respective Objects. If it is part of the correct Scope, he stays and finishes.
3. The Broker also checks if **Choose the Nearest Worker** is selected.
4. If the Worker has the highest Priority, a matching or no Scope, and the shortest route to the Workplace, the Broker mediates him to that Workplace.

Plant Simulation computes a route to the Workplace for all eligible Workers while brokering them; the more Workers that can be brokered, the more computation time (and the slower the simulation).

## How the Worker Carries Parts

The Worker can carry parts from one station to another. This requires a Workplace attached at the pick-up station and at the target station, plus a Broker and a WorkerPool.

Travel Mode requirements:
- **Move freely within area**: the Worker automatically finds his way.
- **Walk along Footpaths**: connect the Workplaces with Footpaths, and connect the WorkerPool to the pick-up Workplace with a Footpath.

Activate the transport importer on **Importer > Transport** of the material flow object where the Worker picks up the part. Specify the Broker; if the part has no destination, specify the **MU Target** (the Workplace at the next station, or the station itself).

- If the Worker can carry a single part (X-, Y-, Z-Dimension all = 1), he picks it up and carries it to the destination.
- If the Worker can carry several parts, he waits until his capacity is reached; use **Maximum Dwell Time** to prevent waiting too long, after which he moves to the target.

The Worker evaluates MU Targets and moves to the closest one first, placing all parts destined for that station, then moving on until all parts are placed. In shift operation, at the end of his shift he returns to the WorkerPool and deposits undelivered parts into the assigned **Parts Buffer** (otherwise Plant Simulation shows a warning and stops the simulation).

## Dialog Box of the Worker
Double-click the icon to open the dialog. Edit simulation properties, or edit 3D properties via **Edit 3D Properties** or by selecting the object and pressing the spacebar. Press **M** (or **Show Manipulators**) to manipulate the graphic.

## Tab Attributes

### Stopped [check box]
Select to stop the Worker on his way to/from the destination. If the Worker stays in the WorkerPool or on a Workplace, you cannot stop him. Clear to let him continue.

**SimTalk:** `Stopped [SimTalk] - Worker`

### Priority [Worker]
Integer value for the urgency of a work order; higher = more urgent. Plant Simulation provides a Worker with Priority 10 before one with Priority 1. Applies only to Workers registered with the same Broker. For identical priority, brokering order is: Workers already on a suitable Workplace at the station, then Workers at the station on the wrong Workplace, then Workers not on a Workplace, then Workers on a Workplace assigned to another station.

**SimTalk:** `Priority [SimTalk] - Worker`

### Efficiency [text box]
Percent value determining how fast the Worker works.
- 100% → exact processing time
- 200% → half the processing time
- 50% → twice the processing time

If more than one Worker performs jobs at the station, the efficiency of the slowest Worker determines the processing time of the MU.

**SimTalk:** `Efficiency [SimTalk] - Worker`

### Speed [Worker]
Speed with which the Worker walks on the FootPath or freely within the area.

**SimTalk:** `Speed [SimTalk] - Worker`, `CurrentSpeed [SimTalk] - Worker`

### X-Dimension / Y-Dimension / Z-Dimension [Worker]
How many parts the Worker can carry in each dimension. Carrying capacity = X × Y × Z; greatest allowed value is one million. Z-Dimension enables stacking parts. If you decrease capacity, make sure no parts occupy the deleted places.

**SimTalk:** `XDim [SimTalk] - Worker`, `YDim [SimTalk] - Worker`, `ZDim [SimTalk] - Worker`

### Shift [Worker]
Name of the Shift during which the Worker works. If no specific shift is given on the Tab Shift Times of the ShiftCalendar, the Worker works during all defined shifts.

**SimTalk:** `Shift [SimTalk] - Worker`

### Services [Worker]
Click to open a list of the services the Worker provides. Click the Inheritance check box before typing. The Worker attempts to provide services in the order typed. Service names are not case-sensitive (compare with the `~=` operator in SimTalk). If a Priority and Efficiency are typed per service, Plant Simulation uses them; otherwise it uses the Worker's Priority/Efficiency values. Inserted services appear in the Broker's **View > Offered Services**.

**SimTalk:** `getServices [SimTalk] - Worker`, `setServices [SimTalk] - Worker`, `Services [SimTalk] - Worker`

### Service [text box]
Shows the name of the brokered/assigned service. If the Worker carries parts, the assigned service (corresponding to the brokered service during loading) is shown and remains assigned until all parts are unloaded.

### Broker [Worker]
Select the Broker who assigns services (via ellipsis button, typing a path like `.Models.Model.MyBroker`, or drag-and-drop). F2 opens the dialog of the object.

**SimTalk:** `BrokerPath [SimTalk] - Worker`

### Home Location
Select the Workplace to which the Worker walks when he has finished his current job.

- Workers with a Home Location and Shift are transferred to the Home Location at the start of the shift; at the end of the shift they are transferred directly to the WorkerPool.
- Workers with a Home Location but no Shift are transferred there at the start of the simulation.
- Relative paths resolve in relation to the Frame containing the WorkerPool.

**SimTalk:** `HomeLocation [SimTalk] - Worker`, `goTo [SimTalk]`, `goToHome [SimTalk]`, `goToPool [SimTalk]`, `teleportTo [SimTalk]`, `teleportToHome [SimTalk]`, `teleportToPool [SimTalk]`

## Tab Failures
Define failures as described under the Tab Failures.

## Tab Scope
Assign built-in material flow objects (or a Frame) to which the Worker can be brokered. Drag objects from the Frame window over the Worker icon (multiple selection possible). Relative paths resolve relative to the Frame containing the WorkerPool. You can also enter the Scope into the Workers to Create table.

**SimTalk:** `Scope [SimTalk] - Worker`, `setWorkersToCreateTable [SimTalk]`

### Objects [Scope]
The material flow objects/Frames forming the Scope. Type a path, or drag-and-drop one or several objects onto the Worker icon. Specifying a Frame includes all inserted objects and sub-Frames.

## Tab Controls [Worker]
Click the ellipsis button and select a Method, or type a name and use **Create Control** to create a user-defined attribute of data type Method (e.g. `self.A1Ctrl` or `self.OnEntrance`). Edit via F2, Shift+double-click, **Open Object**, or the User-defined tab.

### Order Control [Worker]
Modifies the built-in behavior; called whenever the Worker is assigned to an importer.

The standard order control as a user-defined attribute looks like this:

```SimTalk
-- (standard order control body)
```

Parameters:
- `Importer` (object) — the importer
- `Type` (integer) — 0 = failure/remove-failure importer, 1 = set-up importer, 2 = processing importer, 3 = transport importer

**SimTalk:** `OrderCtrl [SimTalk] - Worker`

### Release Control [Worker]
Called as soon as an importer releases the Exporter/Worker (which has already left the importer). You must assign new importers yourself (e.g. `findNewImporter`); otherwise the Worker will not automatically register as available with its Broker.

The standard release control as a user-defined attribute looks like this:

```SimTalk
-- (standard release control body)
```

Parameters:
- `Importer` (object) — the importer
- `Type` (integer) — 0 = failure/remove-failure importer, 1 = set-up importer, 2 = processing importer, 3 = transport importer

The Release Control for the transport-importer is called when the Worker starts to carry parts away (when **Maximum Dwell Time** has passed or when X/Y/Z-Dimension capacity is used up).

**SimTalk:** `ReleaseCtrl [SimTalk] - Worker`

## Tab Statistics [Worker]

Shows the most important statistical data. The Services and Worker blocks each add up to 100 percent. Failed times are collected only during processing time (outside paused/unplanned time). Waiting times accumulate only while the Worker is available.

| Item | Description | Read-only attribute |
|---|---|---|
| Services > Setting-up | Portion of set-up time | `StatServicesSetupPortion [SimTalk] - Worker` |
| Services > Processing | Portion of working time | `StatServicesWorkingPortion [SimTalk] - Worker` |
| Services > Repairing | Portion of repairing time | `StatServicesRepairingPortion [SimTalk] - Worker` |
| Services > Transporting | Portion of transport time | `StatServicesTransportingPortion [SimTalk]` |
| Services > En-route to Job | Portion of time spent getting to the Workplace/back | `StatServicesEnRouteToJobPortion [SimTalk]` |
| Services > Waiting | Portion of waiting time | `StatServicesWaitingPortion [SimTalk] - Worker`, `StatServicesWaitingImpPortion [SimTalk] - Worker`, `StatServicesWaitingMUPortion [SimTalk] - Worker`, `StatServicesEnRouteIdlePortion [SimTalk]` |
| Services > Failed | Portion of failed time | `StatServicesFailedPortion [SimTalk] - Worker` |
| Exporter > Operational | Portion operational | `StatExporterOperationalPortion [SimTalk]` |
| Exporter > Paused | Portion paused | `StatExporterPausedPortion` |
| Exporter > Unplanned | Portion unplanned | `StatExporterUnplannedPortion [SimTalk]` |
| Exporter > Failed | Portion failed | `StatExporterFailedPortion [SimTalk]` |
| Worker > Traveled Distance | Distance traveled in meters | `StatTraveledDistance [SimTalk] - Worker` |

To collect statistics, select **Exporter Statistics**. View via **View > Show Statistics Report**, right-click in the Frame, or press F6. Note: the Worker stays at the station while it is failed, paused, or stopped; Statistics does not count this time as waiting.

### Exporter Statistics [Worker]
Select to collect statistics data of the Worker.

**SimTalk:** `ExpStatOn [SimTalk]`

## Tab User-defined
Define your own attributes as described under the Tab User-defined.

## Navigate Menu
Commands are described under the Navigate Menu.

## View Menu [Worker]
Provides: Refresh, Show Statistics Report, Show Attributes and Methods, Contents, Position, Importers, Exported Services, Route to Destination, Associated Shift Calendar.

### Contents [Worker]
Opens a table showing all MUs the Worker carries. For capacity 1 there is one column; otherwise as many columns as the capacity (X-, Y-, Z-Dimension).

**SimTalk:** `Cont [SimTalk] - MUs`, `contentsList [SimTalk] - material flow objects`, `deleteMovables [SimTalk] - MUs`, `mu [SimTalk] - material flow objects`, `muPart [SimTalk]`, `NumMU [SimTalk] - MUs`, `NumMUParts [SimTalk] - MUs`, `pe(Y,Y) / [X,Y] [SimTalk] - MUs`

### Position [Worker]
Opens a table showing the object on which the Worker is located.

### Importers [Worker]
Opens a table showing all importers for which the Worker provides services (column 1) and their Type (column 2): 0 = failure, 1 = set-up, 2 = processing, 3 = transport.

**SimTalk:** `findNewImporter [SimTalk]`, `getImporters [SimTalk]`

### Exported Services [Worker]
Opens a table of all services the Worker currently provides. Double-click a service to open a subtable with Importer, Type, and Amount. Type 0 = failure, 1 = set-up, 2 = processing, 3 = transport.

**SimTalk:** `getExportedServices [SimTalk]`, `Services [SimTalk] - Worker`

### Route to Destination [Worker]
Selects all objects along the route to the destination object of the selected Worker instance.

**SimTalk:** `getRouteLength [SimTalk] - Worker`, `getRouteCoordinates [SimTalk]`, `getRouteLength [SimTalk] - Workplace`

## Tools Menu
Provides **Edit Controls** and **Edit Observers**. The Worker also provides the **Available** control and the **Not-available** control.

## Help Menu
Commands are described under the Help Menu.

## States of the Worker
Select a setting on **Tab States > States Orientation**:
- **Horizontal**: shows the state as a horizontally arranged cube along the bottom of his picture (all states can be shown).
- **Color**: colors the entire picture of the Worker.

## Methods of the Worker

The Worker provides:
- The methods listed in the table of contents.
- The `_Methods of the Exporter` (the Worker is an Exporter with capacity 1).
- The `Methods of All Objects`.

Note: If you do not use a FootPath, Plant Simulation beams/teleports the Worker to the Workplace.

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (context menu of the Class Library, or F8 / **Show Attributes and Methods** on the Home ribbon tab for an instance).

## See also
- How the Broker Mediates Jobs to the Worker
- Model Workers and the Jobs They Do
- Model a Worker Who Carries Parts Between Workplaces
- Model Workers with Importer, Broker, and Exporter
- How the Worker Finds the Shortest Route
- How the Worker Decides Where to Work
- How the Worker Carries Parts
- How Workers Queue Up in Front of the Workplace
- Show Worker Statistics in a Chart
- How the Worker Travels in the Plant
- Video on YouTube: https://youtu.be/HiPziA8kxc0?si=QnyvMaEQeVyaDoHo
