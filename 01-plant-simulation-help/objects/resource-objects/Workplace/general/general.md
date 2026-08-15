# Workplace — General

## Overview

The `Workplace` object models the actual place at a station where a Worker performs his job.

Plant Simulation **resource objects** include:

- **Exporter** — provides/export services; represents a group of people whose individual members you cannot distinguish or address.
- **FootPath** — models a path the Worker walks from the WorkerPool to the Workplace.
- **LockoutZone** — controls a group of material flow objects; if one fails, all others stop processing parts.
- **Marker** — sets milestones along which AGVs drive from the AGVPool to their destination.
- **ShiftCalendar** — models a shift work system.
- **Worker** — does a job on a workplace at a station. (Not shown in the Resources toolbar; access its class in the Class Library.)
- **WorkerPool** — models the staff room.
- **Workplace** — models the actual place attached to the station where the Worker performs his job.

> Do not confuse resource objects with **material flow resources** (any built-in Material Flow Objects, Fluid Objects, or a Frame in which you modeled a machine).

## Description

The Worker-WorkerPool-Workplace-FootPath concept refines the Broker-Importer-Exporter concept.

- You can assign a Workplace to material flow objects that support an **Importer** (processing or repairing importers).
- For the **transport importer** (how Workers carry parts), you can also assign a Workplace to the Buffer, PlaceBuffer, Source, Sorter, and Store.

Notes:

- You can, but do not have to, assign a Workplace to a station. Without a FootPath, the Worker is transported directly to the Workplace (functioning as an Exporter with capacity 1).
- Workers are created in the WorkerPool and stay there when idle.
- The **Broker** procures the Worker for each work station.
- If the Worker walks freely, he walks the shortest route and consumes time.
- If the WorkerPool and Workplace are connected by a FootPath, the Worker is animated while moving and working; walking the FootPath consumes time.
- With **Beam to workplace** activated and a Workplace the Worker cannot reach via FootPath, Plant Simulation beams him directly to the Workplace.
- With **Workers can work remotely** activated, or no Workplace / no supporting Workplace / all Workplaces occupied, the Worker does the job at the work station but continues to be animated in the WorkerPool.

Queue visualization legend (graphic arrow meanings):

- Part Carried by Worker with Route
- Part Carried by Worker Destination
- Workplace Assigned to Station
- Workplace Reserved for Worker (filled arrow)
- Workplace Reserved for Worker on his Way (hollow arrow)

To change the graphic length and anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.

### Add the Object to the Model

Click **Manage Class Library > Basic Objects > Resources > Workplace** on the Home ribbon tab.

## How Workers Queue Up in Front of the Workplace

Workers who cannot step onto the Workplace wait in a queue in front of it (without additional FootPaths).

- The waiting position depends on the Worker's position in the **Forward Blocking List** and the **Distance in Queue**.
- In new models, the queue is visualized on the **MU Animation Path** named `Queue`; if longer than the pre-defined path, it elongates toward the end of the queue.
- To have the Worker walk to the end of the MU Animation Path rather than the Workplace, select **Walk Along the Animation Path of the Queue**.
- The end of the animation path should be at the same height (Z-position) as the Workplace; otherwise a route may not be computable.
- If the Worker arrives at an occupied Workplace/waiting position, Plant Simulation moves him directly to the correct waiting position.
- Walking directly to the Workplace uses no time for reaching the waiting position; moving up within the queue is executed by the Worker's animation.

## Dialog Box of the Workplace

Double-click the Workplace icon to open its dialog box.

- **Edit Simulation Properties** — shared properties under "Dialog Items of the Objects".
- **Edit 3D Properties** — click **Edit 3D Properties** button, or select the object and press spacebar. To manipulate the graphic, click **Show Manipulators** or press **M**.

### Tab Attributes

#### Station [Workplace]

The Station is a material flow object that supports an importer (e.g., Source, Drain, Station, ParallelStation, AssemblyStation, DismantleStation, Conveyor). Click the ellipsis button and select the Station in **Select Object**. To auto-enter, drag the Workplace close to a side of the material flow object.

- An unassigned Workplace and an assigned Workplace have different icons.
- **F2** opens the dialog of the object named in the text box.
- SimTalk: `Station`

#### At Entrance [check box]

Attach the Workplace to the entrance of a Conveyor. For place-oriented objects, Plant Simulation selects At Entrance and At Exit by default.

Drag-and-drop: select the Workplace and drag it to the entrance of the Conveyor (tooltip shows `Conveyor @ Entrance`), or select the Conveyor, hold Shift, and drag it onto the Workplace icon. Assigning a new station via SimTalk does not change the current entrance/exit assignment.

- SimTalk: `AtEntrance`

#### At Exit [check box]

Attach the Workplace to the exit of a Conveyor (tooltip `Conveyor @ Exit`). Same drag-and-drop behavior as At Entrance.

- SimTalk: `AtExit`

#### Capacity [text box] - Workplace

Maximum number of Workers that can stay on this Workplace at any one time. Important when several tasks are accomplished here or come together.

- Plant Simulation uses the Workplace coordinate to find the shortest route; the Worker walks to this coordinate, then jumps to the animation point.
- Workers are shown distributed across an **Animation Area**.
- Capacity can only be changed while the Workplace is empty.
- A **Recovery Time** can be defined only for a Workplace with Capacity 1; it starts once a Worker leaves.
- SimTalk: `Capacity`

#### Supported Services [button]

Opens the list of services the Workplace supports.

- Click the **Inheritance** check box before typing data, then type expressions (e.g., `drilling`, `milling`, `turning`) and click Apply.
- Names are **not case-sensitive**. Case-insensitive strings share one string in memory; the first occurrence defines the casing. In SimTalk, compare case-insensitively with the `~=` operator.
- If no services are listed, the Worker can execute any service on this Workplace.
- If no Workplace exists that supports a service (or all are occupied), the Worker works at the work station but is not animated there.
- SimTalk: `SupportedServices`

#### Worker Stays Here After Completing the Job

Select to keep the Worker on the Workplace after completing his job; clear to make him return to the WorkerPool or Home Location. Clear it if **Get Job Orders At Home Only** is activated in the WorkerPool.

- A Worker who is not automatically brokered stays on the Workplace regardless of this setting.
- If a staying Worker occupies the Workplace and capacity is used up, Plant Simulation shoves the non-working Worker aside; he exits and returns to the WorkerPool/Home Location.
- SimTalk: `WorkerStaysHere`

#### Distance in Queue

Distance between Workers in the queue on the animation path; they attempt to keep this distance while waiting.

- SimTalk: `DistanceInQueue`

#### Walk to the End of the Animation Path of the Queue

Make the Worker first walk to the end of the animation path, then on to his destination.

- SimTalk: `WalkToQueuePathEnd`

#### Walk Along the Animation Path of the Queue

Make the Worker walk along the animation path to his waiting position or to the Workplace after reaching the MU Animation Path.

- Only takes effect if **Walk to the End of the Animation Path of the Queue** is also selected.
- Obstacles are not taken into account when walking along the MU Animation Path.
- SimTalk: `WalkAlongQueuePath`

#### Pick/Drop at Store

Sets what the Worker does when picking up or dropping parts at a Store-attached Workplace. Only shown if the Station is a Store.

Options:

- **Walk to Workplace** (default) — Worker walks to the Workplace to pick up/drop parts; all Workplace settings available. Only this setting supports route computations with `getRouteLength` and `getRouteCoordinates` (other settings return `-1` and an empty array, respectively).
- **Walk to Store Column** — Worker walks to the store column without restrictions. Unavailable: Capacity (assumed infinite), Worker Stays Here After Completing the Job, Distance in Queue, Walk to the End/Walk Along the Animation Path. Locations determined by the Store side dimensions, number of columns, and the Workplace's center-point distance to the Store. Large Stores with many columns increase route computation complexity and impact performance.
- **Walk Along Store to Store Column** — Worker walks to the first/last column, then extends his route along the Store to the target column. Routes are restricted; each column reachable only from previous/next column (first and last columns have no restrictions). Ignores obstacles when extending the route. Same unavailable features as "Walk to Store Column". Smaller performance impact than "Walk to Store Column".

- SimTalk: `PickDropAtStore`

### Tab Times

Define Times as described under Tab Times. Settings:

- **Loading Time [Workplace]** — time for the Worker to pick up a single part at a station. The part is booked on the Worker while picked up; the processing station is locked until elapsed. The entrance of the Workplace is closed while Loading Time runs. During Worker interruptions, Loading Time extends by failure times (station stays locked); if the Worker pauses or the shift ends, Loading Time is canceled and considered fully elapsed. Processing station failures/stop/pause/unplanned do not affect loading. Formula distribution: `@` accesses the part, `?` points to the Workplace, `?.Cont` accesses the Worker.
- **Unloading Time [Workplace]** — time to place a picked-up part onto the target station; accrues per part. The part is booked on the Worker while placed; the target station is locked until elapsed. During Worker interruptions, Unloading Time extends by failure times (target stays locked); pause/shift-end cancels it. The Worker only starts unloading when the target station can accept the part; otherwise the part enters the Forward Blocking List.
- **Recovery Time [Workplace]** — prevents a Worker from stepping onto the Workplace before the previous Worker has left it entirely. Only for Capacity 1 Workplaces; starts once a Worker leaves. Does not take effect if the Workplace is set as a Worker's Home Location.

Use `setTypeAndAttr` to set the distribution type and parameters. Select a distribution or a constant (`Const`).

### Tab Controls

Click the ellipsis button and select a Method in **Select Object**, or press F2 to open it, or drag a Method from a Frame into the text box.

To create a control as a user-defined attribute of data type Method: type a name and select **Create Control** (inserts `self.Name`, e.g., `self.A1Ctrl`), or select **Create Control** on an empty box (inserts `self.OnBuilt_in_name`, e.g., `self.OnEntrance`). To delete a control, delete the user-defined attribute (deleting only the name retains the attribute).

#### Entrance Control [Workplace]

Called as soon as the Worker steps onto the Workplace. SimTalk: `EntranceCtrl`

#### Exit Control [Workplace]

Called as soon as the Worker steps off the Workplace. SimTalk: `ExitCtrl`

#### Load Control

Called as soon as the Worker steps onto the Workplace; sets how a part is transferred from the work station to the Worker. Also called when the Worker is already on the Workplace and loads parts to carry to a target object.

Standard load control (user-defined attribute):

```simtalk
// workplace load control ...
// ... to transfer MUs from the associated station to the worker on the workplace
// @: worker
// ?: workplace
if @.failed = false and @.pause = false
   // get the first MU to exit and repeat this until no MU is about to exit
   var mu:object := ?.station.cont
   while mu /= void and @.full = false
        // transfer the exiting MU to the worker
        mu.move(@)
        // with configured load time on workplace, wait for EndOfTime event causing the transfer to worker
        waituntil mu.~ = @
        mu := ?.station.cont
   end
end
```

SimTalk: `LoadCtrl`

#### Unload Control

Called as soon as the Worker steps onto the Workplace attached to the target station; sets how the Worker places the carried part onto the attached work station.

Standard unload control (user-defined attribute):

```simtalk
// workplace unload control ...
// ... to transfer all MUs from a worker on the workplace to the associated station
// @: worker
// ?: workplace
if @.failed = false and @.Pause = false
   // remember the station associated to the workplace
   var station:object := ?.station
   // get the first MU about to exit to repeat this until no MU wants to exit anymore
   var mu:object := @.cont
   while mu /= void and station.full = false
        // wait until the entrance is free (for example for conveyors)
        waituntil station.EntranceFree
        // transfer the MU from the carrying worker to the station
        mu.move(station)
        // with configured unload time on workplace, wait for EndOfTime event causing the transfer from worker to station
        waituntil mu.~ = station
        mu := @.cont
   end
end
```

SimTalk: `UnloadCtrl`

### Tab User-defined

Define your own attributes as described under Tab User-defined.

## Menus

- **Navigate Menu** — described under the Navigate Menu.
- **View Menu** — commands: Refresh, Show Statistics Report (Contents and Reserved Places), Show Attributes and Methods (Forward Blocking List).
  - **Contents [Workplace]** — list of all Workers staying on the Workplace. SimTalk: `contentsList`
- **Tools Menu** — Edit Controls, Edit Observers.
- **Help Menu** — described under the Help Menu.

## Methods of the Workplace

The Workplace provides:

- The methods listed in the table of contents.
- The Methods of All Objects.
- The Methods of the Material Flow Objects.

To view all methods/attributes, open **Show Attributes and Methods** (context menu of the Class Library, F8, or the Home ribbon tab).

## See Also

- Model Workers and the Jobs They Do
- Model a Worker Who Waits in Line
- Worker-WorkerPool-Workplace-FootPath concept
- Broker-Importer-Exporter concept
- Videos:
  - https://youtu.be/HiPziA8kxc0
  - https://youtu.be/gU1pqu7sWA8
