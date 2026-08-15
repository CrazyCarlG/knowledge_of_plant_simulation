# WorkerPool (General)

> Source: `general.txtx` — Plant Simulation Help (pp. 11-3063 to 11-3101)

## Overview

The **WorkerPool** object models the lounge or staff room of a plant. It is the central object in the **Worker–WorkerPool–Workplace–FootPath** concept, which refines the **Broker–Importer–Exporter** concept.

- Workers are created in the WorkerPool and stay there while idle, waiting for an order.
- As soon as a Worker can provide a service, the **Broker** sends him from the WorkerPool to the work station that ordered him.
- At the end of a shift, the Worker walks back to the WorkerPool and deposits undelivered parts into the assigned **Parts Buffer**.

### How a Worker reaches his work station (Travel Mode)

- **Walk freely within area** — the Worker walks the shortest route to the Workplace and around designated obstacles.
- **Walk along footpaths** — the Worker walks on the FootPath network; time is consumed while walking.
- **Beam to workplace** — if `Beam to workplace` is activated and the Worker cannot reach the Workplace via a FootPath, the Worker is transported (beamed) directly to the Workplace.
- **Workers can work remotely** — if activated and no Workplace exists/supports the service/is free, the Worker seemingly beams to the station and performs the task (not animated there; continues to be animated in the WorkerPool).

> If no Broker exists when the Workers are created, Plant Simulation sets `AutomaticMediation` of the Workers to `false`.

### Shift handling

If the plant works in shifts, the Worker deposits parts he could not deliver into the **Parts Buffer** (any material flow object that accepts parts). If no parts buffer is assigned, Plant Simulation shows a warning and stops the simulation.

- If the **transport importer** of the parts buffer is activated, an available Worker carries the parts to the destination object after the next shift starts.
- Otherwise, parts are moved on according to the parts buffer's **Exit Strategy**.

### Visualization

- The WorkerPool initially shows no Workers; enable **Show Content** on the **Graphics** tab.
- On the **MU-Animation** tab, Workers can be shown on an **Animation Path** or an **Animation Area** (distributed along the Y-dimension).
- Drag the WorkerPool over a **Chart** to show statistics of its Workers.
- Add via: **Home ribbon tab > Manage Class Library > Basic Objects > Resources > WorkerPool**.

---

## Dialog Box

Double-click the WorkerPool icon to open its dialog box. Shared properties are described under *Dialog Items of the Objects*. Edit 3D properties via the **Edit 3D Properties** button or by selecting the object and pressing the spacebar.

---

## Tab Attributes

### Workers to Create

Click this button to open the table defining the Workers to be created and inserted into the model. Click the **deactivate Inheritance** button before entering data.

Table columns and procedure:

| Column | Description |
| --- | --- |
| **Worker** | Class of the Worker used as template, e.g. `.Resources.Worker` or `.UserObjects.MyWorker`. |
| **Amount** | Number of Workers to create. |
| **Shift** | Name of a shift defined in the associated Shift Calendar. |
| **Speed** | Optional walking speed; typing a value deactivates inheritance (class speed changes no longer affect this row). |
| **Efficiency** | Efficiency percentage, e.g. `80` for 80%. |
| **Home Location** | Path to the Workplace the Worker walks to after finishing his current job. |
| **Scope** | Path to material flow objects the Worker can be brokered to (includes sub-Frames). |
| **Additional Services** | Services the Worker provides in addition to those in the Services list. |

Notes:

- Plant Simulation resolves relative paths relative to the Frame in which the WorkerPool is inserted; unresolved paths during simulation trigger an error and prompt to stop. This also applies to the Home Location.
- Service names are **not case-sensitive**; the WorkerPool attempts to export services in the order entered.
- To save memory/improve speed, case-insensitive strings point to the same string in memory — the **first occurrence** defines its casing.
- In SimTalk, case-insensitive string comparison uses the `~=` operator.
- Changes to the Workers to Create table only affect the simulation run if made **before initialization**.
- You can change the table within the WorkerPool's **Init Control** (but not in an init method — it runs too late).

To set the **Scope**: click the Scope cell → a table with one empty cell opens → drop the target object into it → press Enter to add more cells → click OK.

Individual Workers not in the table can be created with the `create` method for a single simulation run (WorkerPool only). These Workers are deleted on reset; only the table Workers are recreated at the next Init event.

Related SimTalk:

- `AdditionalServices`, `Amount`, `Efficiency`, `getWorkersToCreateTable`, `setWorkersToCreateTable`, `setServices`, `Shift`, `Speed`, `Worker`
- `GetJobOrdersAtHomeOnly`

### Get Job Orders At Home Only

When selected, the Worker only receives new job orders at a station in the WorkerPool or at his **Home Location**.

> A Worker staying on a Workplace with **Worker Stays Here After Completing the Job** activated cannot be brokered in this case — clear that setting on all Workplaces for correct brokering.

Clear the check box to allow the Worker to get job orders anywhere (walking freely or on a FootPath).

SimTalk: `GetJobOrdersAtHomeOnly`

### Workers Can Work Remotely

When selected, the Worker does his job from his current location if no free Workplace is available at the assigned station. Useful for building models without any Workplaces (Worker stays in the WorkerPool the entire time).

> If a free Workplace is available, it is used even when this option is selected. To prevent a service from using a Workplace, use an **Exporter** or restrict Workplaces to certain services.

SimTalk: `WorkersCanWorkRemotely`

### Travel Mode

Selects how the Worker travels. Settings:

- **Move freely within area** — walks freely and around 3D obstacles.
- **Walk along footpaths** — walks on Footpaths inserted between Stations/Workplaces.
- **Beam to workplace** — beamed/teleported instantly to the Workplace if no Footpath leads there (functions like an Exporter with capacity 1).

> The Travel Mode is only transmitted from the WorkerPool to the Workers when they are created; it is not changed afterwards.

SimTalk: `WorkersTravelMode`

#### Move freely within area

- Plant Simulation automatically computes the shortest route between Workplaces and between the WorkerPool and Workplaces, using the 3D layout.
- Obstacles (walls, pillars, machines, conveyors, safety fences) are automatically detected. Material flow objects, animatable objects, and Frame graphics are marked as **Barred Areas** by default; information-flow and user-interface objects are not.
- Set obstacle behavior under **Edit 3D Properties > Graphics > Obstacle for the Worker** (for graphics: **Graphic Settings**).
- Manually create **Barred Areas** for areas the Worker may enter but should not (e.g. crane pivoting area).
- A **FootPath** can be laid through a door/wall to let the Worker pass; it must be slightly longer than the wall depth.
- For the FootPath, the length in the **scene** is decisive (starting point, end point, anchor points), not the length entered on the Attributes tab.
- Inclines: Plant Simulation **triples the height difference** when computing the effective length of inclined segments. Example: a 1 m × 1 m (x/z) segment is actually 1.414 m long, but is treated as 1 m × 3 m = 3.162 m effective length.
- The Worker always takes the route with the shortest **effective** length; speed drops to about a third on vertical climbs and about half on a 38° incline.
- Between floors, the Worker can only move via ramps/Footpaths or **Stairs** (see example model *Factory 51*).

#### Walk along footpaths

- Insert FootPaths to model distances between the WorkerPool and work stations.
- Link several FootPaths with **Connectors** to build a network; the Worker walks the shortest route within a connected network.
- Walking time depends on the Worker's **Speed** and the combined **Lengths** of the FootPaths covered.
- If the Worker does not walk on a FootPath (or is beamed), no time is consumed.

#### Beam to workplace

- Beams (teleports) the Worker to the brokered Workplace instantly if no Footpath reaches it.
- The Worker functions as an Exporter with capacity 1; useful for models without FootPaths.

SimTalk: `WorkersTravelMode`, `teleportTo`, `teleportToHome`, `teleportToPool`

### Broker

Select the Broker who assigns services to the Worker (via the ellipsis button, typing the path e.g. `.Models.Model.MyBroker`, or drag-and-drop). Press **F2** to open the dialog of the typed object.

SimTalk: `BrokerPath`

### Shift Calendar

Select the ShiftCalendar controlling when the WorkerPool works. Selecting it automatically adds the WorkerPool to the ShiftCalendar's **Resources** tab. If the Workers work in shifts, also select the **Parts Buffer**.

SimTalk: `ShiftCalendarObject`

### Parts Buffer

Select the object into which the Worker deposits undelivered parts at the end of a shift. Can be any material flow object that accepts parts. If not assigned and a Worker arrives with parts at shift end, Plant Simulation warns and stops.

- Transport importer activated → an available Worker carries parts to the destination after the next shift starts.
- Otherwise → parts move per the parts buffer's Exit Strategy.

> This setting only applies when shifts are controlled via the Shift Calendar.

SimTalk: `PartsBuffer`

---

## Tab Statistics

| Item (English) | Description | Read-only attribute (SimTalk) |
| --- | --- | --- |
| Paused | Portion of the statistics collection period during which the WorkerPool was paused | `StatPausingCount` |
| Unplanned | Portion during which the WorkerPool was unplanned (not scheduled to work) | `StatUnplannedPortion` |
| Average Traveled Distance | Average distance in meters the Worker traveled (from WorkerPool to Workplaces and between stations) | `StatAverageTraveledDistance` |

Other values match the **Tab Statistics of the Worker**. View Resource Statistics of Stationary Resources via **View > Show Statistics Report** (or right-click the Frame → Show Statistics Report, or press F6).

---

## Tab Controls

Click the ellipsis button and select a Method (or drag-and-drop, or type a name and press F2 to edit). To create a control as a user-defined attribute of data type Method:

- Type a name and select **Create Control** → inserts `self.<name>`, e.g. `self.A1Ctrl`.
- Or select **Create Control** on an empty text box → inserts `self.On<built-in-name>`, e.g. `self.OnEntrance`.

Editing the source code later: press F2, or Shift+double-click, or **Open Object** on the context menu, or open from the **User-defined** tab. To delete a control, delete the user-defined attribute (deleting only the name from the text box retains the attribute).

### Entrance Control

Called as soon as the Worker enters the WorkerPool.

SimTalk: `EntranceCtrl`

### Exit Control

Called as soon as the Worker exits the WorkerPool.

SimTalk: `ExitCtrl`

---

## Tab User-defined

Define your own attributes as described under the **Tab User-defined** (shared documentation).

---

## View Menu

Commands to access functions:

- **Assigned Workers** — opens a list of all Workers for which the WorkerPool provides services.
  - SimTalk: `getAssignedWorkersTable`, `getAssignedWorker`, `NumAssignedWorkers`
- **Working Workers** — opens a list showing:
  - the Worker providing a service or carrying parts;
  - the **Location** (object the Worker is on; the WorkerPool for a freely-walking Worker);
  - the **Target** station;
  - the **Service** currently provided.
  - SimTalk: `getWorkingWorkersTable`
- **Refresh**, **Show Statistics Report**, **Show Attributes and Methods**.

---

## Tools Menu

- **Edit Controls > Init control**
- **Edit Observers**

### Init Control

Called at the start of the simulation run during the **init phase**, *before* events are computed (normal init methods run *after* initial events are computed). Use it to change the **Workers to Create** table for the next run or initialize attributes that affect event generation (e.g. availability).

SimTalk: `InitCtrl`

---

## Methods of the WorkerPool

The WorkerPool provides the methods listed in the table of contents plus the **Methods of All Objects**. To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (F8 on a Frame instance, or via the Class Library context menu).

---

## SimTalk Reference (collected)

```simtalk
MyFootPath.Width := 2 // meters   (Width attribute — FootPath)
```

Other referenced SimTalk attributes/methods:

- WorkerPool: `AdditionalServices`, `Amount`, `Efficiency`, `Worker`, `Speed`, `Shift`, `getWorkersToCreateTable`, `setWorkersToCreateTable`, `BrokerPath`, `ShiftCalendarObject`, `PartsBuffer`, `WorkersTravelMode`, `WorkersCanWorkRemotely`, `GetJobOrdersAtHomeOnly`, `EntranceCtrl`, `ExitCtrl`, `InitCtrl`, `getAssignedWorkersTable`, `getAssignedWorker`, `NumAssignedWorkers`, `getWorkingWorkersTable`
- Statistics: `StatPausingCount`, `StatUnplannedPortion`, `StatAverageTraveledDistance`
- Teleporting: `teleportTo`, `teleportToHome`, `teleportToPool`
- Related: `setServices` (importer), `WorkerStaysHere` (Workplace)
