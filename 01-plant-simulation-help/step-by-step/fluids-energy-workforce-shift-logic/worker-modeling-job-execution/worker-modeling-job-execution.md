# Modeling Workers and the Jobs They Do

> **Note:** The energy states of material flow objects differ from the resource states with the same name. Resource-state values refer to the statistics collection period, while energy-state values refer to total energy consumption.

## Overview

When simulating a plant, you must model **Workers** who operate or repair machines. Key objects:

- **Worker** — performs jobs at a `Workplace` attached to a machine.
- **Workplace** — where the Worker stands while working/repairing at a machine.
- **WorkerPool** — where Workers are created and where they wait for a job (e.g., lounge/staff room).
- **Broker** — the "foreman" that assigns Workers to jobs at machines.
- **FootPath** — the path a Worker walks along from the WorkerPool to a Workplace.

The Worker walks on a FootPath from the WorkerPool to the Workplace of a machine to perform a job, and can also walk freely within the model (not bound to a FootPath network).

You can also use **Broker** and **Exporter** to model Workers and the tools they need. As a rule, use the `Worker` when the travel time to a machine matters; use `Importer`, `Broker`, and `Exporter` when producing a part requires shared resources.

Insert objects from the folder **Resources** in the Class Library or from the toolbar **Resources** in the Toolbox.

> **Note:** If a Worker does not walk in the model, ensure the importer on the tab **Importer** of the station (whose attached Workplace the Worker uses) is activated.

The examples covered:
- Model a Worker Who Works at a Machine
- Model a Worker Who Repairs a Machine
- Model a Worker Who Carries Parts Between Workplaces
- Model a Worker Who Walks Freely
- Model a Worker Who Waits in Line
- Model a Worker Who Returns to the Home Location
- Set How Many Workers Are Created During Initialization
- Model Workers with Importer, Broker, and Exporter
- Set How Workers Deliver Mounting Parts

---

## Model a Worker Who Works at a Machine

1. **Configure the WorkerPool:**
   - Insert a `WorkerPool` object.
   - Deactivate inheritance of the **Workers to Create** table (uncheck inheritance checkbox).
   - Open the table and add the path of the Worker class, e.g. `.Models.Worker.myWorker`.
2. **Insert a Broker** — manages all Workers. Click **Browse** and add the Broker to the WorkerPool.
3. **Insert a Workplace** and attach it to the machine:
   - Click `WorkPlace` on the toolbar **Resources** and place it next to the machine.
   - Drag the machine (e.g., Station `MyMachine`) onto the Workplace dialog to set the **Station** text box.
   - Deactivate inheritance of the **Supported Services** table; open it and type `StandardService`.
4. **Tell the machine to request the Worker:** Select **Active** on the sub-tab **Processing** of tab **Importer**; add the Broker path via **Browse**.
5. **Insert the FootPath** and connect WorkerPool and FootPath with a Connector.
6. Reduce simulation speed, then start. The Worker walks the FootPath from WorkerPool to Workplace, works one part (performs 1 StandardService), then returns.

> **Case-insensitivity note (repeated throughout):** Service names, attribute names, and method names are not case-sensitive. The first occurrence of a string defines its casing; use the `~=` operator in SimTalk for case-insensitive comparison.

---

## Model a Worker Who Repairs a Machine

Continuing from the previous model:

1. Insert a FootPath from WorkerPool to the machine; connect them.
2. Insert a Workplace where the repair Worker stays; turn off inheritance of **Supported Services** and type the service `repair`.
3. Add a second Worker to the **Workers to Create** table (right-click → Append Row); drag the Worker into the Worker cell; enter `repair` in **Additional Services**.
4. Configure the machine to create failures and request a repair Worker:
   - Select **Active** on tab **Failures**. Type `9:` in **Interval** (mean time between failures) and `1:` in **Duration** (mean time to repair).
   - Select **Active** on sub-tab **Failure** of tab **Importer**; add the Broker path.
   - Deactivate inheritance; open **Services for Repairing** and replace `StandardService` with `repair`.
5. Start the simulation — the top Workplace Worker processes parts while the bottom Workplace Worker repairs the machine when it fails.

---

## Model a Worker Who Carries Parts Between Workplaces

The Worker can pick up parts ready to leave a station and carry them to a destination object. While loading, the Worker is brokered to the station; procurement ends when the Worker leaves the Workplace with the part (service stays assigned but is no longer brokered).

- Enter **Loading Time** / **Unloading Time** on the Workplace attached to the station.
- The Worker evaluates part targets (set on sub-tab **Transport**) and walks to the closest one first; at each target station he deposits all parts destined there.
- At shift end, the Worker returns to the WorkerPool and deposits undelivered parts in the **Parts Buffer** assigned to the WorkerPool. Without a parts buffer, Plant Simulation warns and stops.
- If the parts buffer's transport importer is active, a Worker carries buffered parts to the target after the next shift; otherwise they move per the buffer's exit strategy.

Sub-examples: Walk on FootPaths; Carry Several Parts; Wait for a Free Target.

### Model a Worker Who Walks on FootPaths

1. Attach a Workplace to the pickup station.
2. Attach a Workplace to the target station (drag close to a side to auto-enter the Station).
3. Connect the Workplaces with a FootPath.
4. Connect the WorkerPool and the pickup Workplace with a FootPath.
5. Activate the transport importer on the pickup station's **Importer** tab; select the Broker (e.g., `MyBroker`); accept the default `StandardService`; select the **MU Target** (e.g., `Workplace2`).
6. Set **Maximum Dwell Time** so the Worker doesn't wait too long for more parts.
7. Select the Worker (e.g., `MyWorker`) and Broker (`MyBroker`) in the WorkerPool, then start the simulation.

### Model a Worker Who Carries Several Parts (3D)

Two approaches: the predefined **animation area** (recommended) or **animation paths**.

**Using the Animation Area:**
1. Duplicate the Worker in the Class Library and rename (e.g., `MyWorker2Parts`).
2. Set **Y-Dimension** and **Z-Dimension** to `2` (one part per hand), keep **X-Dimension** at `1`.
3. Set **Maximum Dwell Time** on the transferring station (e.g., `2:00`) — longer than the Processing Time — so the Worker waits for the second part.
4. Right-click the Worker in the Class Library → **Open in 3D** → right-click background → **Edit 3D Properties** → tab **MU Animation** → sub-tab **Animation Area**.
5. Activate the animation area and adjust X/Y/Z position and width so parts sit correctly on the Worker's hands.
6. Start the simulation. Statistics show carrying percentages and en-route times under **Transporting** and **En-route to job** (press F6 for the statistics report).

**Using Animation Paths:**
1. Double-click `MyWorker2Parts`; set X/Y/Z-Dimension to `2`.
2. Open in 3D → Edit 3D Properties → **MU Animation** → **Animation Paths**.
3. Add two `Lines`-type animation paths named `#0#0` (left hand) and `#1#0` (right hand).
4. Move each path via **Edit → Position** (Edit Anchor Values) and click **Apply** in Path Anchor Points to preview.
5. Adjust part size (uniform scale factor, e.g. `0.6`, or check **Scale automatically**) and X-Position toward the body.
6. Repeat for the left-hand path, then run.

> Defining animation paths is involved — prefer the predefined animation area.

### Model a Worker Who Waits for a Free Target

Two Workers pick up parts from Workplaces attached to Sources, carry them to a Workplace at the entrance of a `ParallelStation` (four processing places), and place them; when all places are full they walk around to the exit Workplace, pick processed parts, and place them on a `Conveyor`.

Steps:
1. Insert two Sources (default settings). Ensure **Wait for Free Target** is on in **Importer > Transport** so a Worker is requested only when the target is free.
2. Insert a Workplace next to each Source (drag close to the side); Plant Simulation activates the Transport Importer, enters the Station, and selects **At Entrance** and **At Exit**.
3. Insert the `ParallelStation` (5-second Processing Time). Insert a Workplace on the left (entrance — clear **At Exit**) and one on the right (exit — clear **At Entrance**).
4. Insert a Conveyor with a Workplace on its left side (**At Entrance** selected).
5. Insert and configure a WorkerPool; select the Broker (default settings).
6. Connect material flow objects with Connectors (Workers walk along them).
7. Run and observe the Workers waiting until a processing place is free.

Useful checks (View menu / read-only attributes):
- Exporter/Imported Service names; associated Workplaces; **Contents** and **Reserved Places** list.
- `Conveyor.ReservedFor` — part for which a place is reserved.
- `Part.ReservedPlace` — the place reserved on a material flow object.
- Worker and Workplace tooltips.

---

## Model a Worker Who Walks Freely

A Worker can walk freely (not forced onto FootPaths), walking around obstacles such as machines, safety fences, AGV paths, or structural elements (columns, stairways). Some free-walking functions can only be set in 3D, so select **3D** when creating the model.

Sub-examples: Walk Freely Within the Model; Walk One-Way; Walk Through Doors; Climb Stairs.

### Walk Freely Within the Model

1. Double-click the WorkerPool in 3D → **Travel Mode > Move freely within the area**.
2. Insert an obstacle: ribbon tab **Edit** → **Barred Area**; choose graphic group, form, dimensions, material.
3. By default the barred area is an obstacle; press the **o** key to show all obstacles.
4. Run the simulation; the Worker ignores FootPaths and walks around the barred area.

Bounding-box notes:
- Workplaces show two bounding boxes with a gap, keeping the Worker in the middle.
- Length-oriented objects approximate their bounding box to the curve (not smooth).
- On the **Graphics** / **Graphic Settings** tab of Edit 3D Settings, most 3D objects can be marked as an obstacle; built-in material flow objects use the graphic's bounding box.

### Walk One-Way

Insert a Barred Area with **Form > One-sided delimitation**. The Worker can cross the dashed-line side but not the solid-line side (direction depends on insertion). Example: a safety-fenced Source where the Worker enters one one-way gate, picks the part, exits through the second, and must loop around to return.

### Walk Through Doors

Even for free-walking Workers, FootPaths are needed to pass through obstacles. Use a factory layout file as the 3D background; its graphics are a single obstacle the Worker cannot cross (visible as a continuous red border with the **o** key). Lay FootPaths through doorways — slightly longer than the obstacle depth.

Effective route length and speed:
- The decisive length is the FootPath's length in the 3D scene (start/end points and anchor points), not the **Attributes** tab value.
- On an incline, Plant Simulation **triples the height difference** when computing effective length (e.g., a 1 m × 1 m segment is physically 1.414 m but treated as 1 m × 3 m = 3.162 m effective).
- Workers take the shortest *effective* route (may choose a flatter, physically longer path).
- Speed drops to a third when climbing vertically (ladders) and to about half on a 38° incline (stairways).

### Walk Through Doors / Climb Stairs

Model an overpass using **Stairs → Mezzanine → Stairs** so Workers can safely cross conveyors:

1. **Insert the Mezzanine:** 3D **Edit** ribbon → **Edit > Insert Shape > Mezzanine**; select settings.
2. **Insert Staircases:** **Edit > Insert Shape > Stairs** for each side; rotate/move to touch the mezzanine.
3. **Remove railing sections** where stairs connect: click the mezzanine, press `+` until only the railing part is selected, press `Del`; repeat at the other end.
4. Fix dimensions if needed (e.g., set **Dimension Y** to `4.5` meters by selecting and pressing spacebar).
5. Run — the Worker climbs the stairs, crosses the overpass, and descends.

> **Obstacle gap note:** There is a 40 cm gap between obstacles and objects/graphics because the assumed Worker width is 80 cm. Change **Worker Width** in Model Settings/Preferences (reducing it too much can cause unrealistic simulation due to safety regulations or carried parts).

---

## Model a Worker Who Waits in Line

Workers who walk freely can queue in front of an occupied Workplace. Sub-examples: Queue Up; Walk to the End of the Queue; Walk Along the Queue.

### Queue Up

Model: WorkerPool (7 Workers, distinct T-shirt colors), Broker (default), Source (7 Parts, Transport importer active, **Wait for Free Target** cleared), Workplace at Source, Station (default) with a Workplace (Transport Importer, **At Entrance**), and Drain; connect with Connectors.

Workers first walk to `Workplace1`, jump into the queue, and wait until they can step on. To fix Workers appearing to walk through each other (straight default animation path), select the Workplace, press spacebar, go to **MU Animation > Animation Paths**, show the path, and move the markers down (Shift + Down Arrow).

Use the **EventDebugger** to step through a Worker's route (e.g., Worker4 steps onto Workplace1 at time 18.1608, then jumps to the end of the queue).

### Walk to the End of the Queue

Select **Walk to the End of the Animation Path of the Queue** in the Workplace attached to the Station. Workers walk to the end of the queue, then move up to the Workplace when a place frees up (visible in the **Forward Blocking List** of Workplace1).

### Walk Along the Queue

Additionally select **Walk Along the Animation Path of the Queue**. Workers walk to the end, then along the queue (keeping their place) to the Workplace. The queue path may be a spline. Clearing both options makes Workers walk directly to Workplace1 when free; otherwise they wait in line on the animation path.

When a Workplace's Capacity is used up, a Worker standing there is "shoved aside" and exits to the WorkerPool (or Home Location); he may receive a new work order en route.

---

## Model a Worker Who Returns to the Home Location

A Worker returns to his **Home Location** after finishing a job within his defined **Scope** (the material flow objects he can be brokered to).

### Model the Material Flow for Home Location and Scope

Build the processing line: Source → Conveyor → Station1 (Workplace) → Conveyor → Station2 (Workplace) → Conveyor → Drain, plus a Broker and a WorkerPool.

- Insert the Broker (entered into the relevant objects' text boxes automatically).
- Insert the first Station (`Station1`), then a Workplace below it (clear **Worker stays here after completing the job**). Plant Simulation activates the Processing Importer and enters `1 Processing` service.
- Insert the Home Location Workplace (e.g., `Home1`, default settings) — the Workplace the Worker always returns to.
- Insert remaining material flow objects; make the last Conveyor 3 m (others 4 m).
- Insert the WorkerPool (configure next).

### Set Home Location and Scope for the Worker

Configure the WorkerPool's **Workers to Create** table:
1. Drag the Worker into the **Worker** cell.
2. Drag the `Home1` Workplace into the **Home Location** cell.
3. Double-click **Scope** and drag the stations the Worker can be brokered to (e.g., Station1, Station2). Plant Simulation separates multiple entries with semicolons.

Run — the Worker walks to Station1, does the job, returns to `Home1`, waits, then walks to Station2, and returns to `Home1`. A second processing line (Station11/Station21, Home11) can be copied and configured likewise.

---

## Model a Worker Picking Up / Placing Parts At a Store

A Worker who walks freely picks up a part at a Source and places it in a Store. Sub-examples: Walk to a Workplace Attached to a Store; Walk to a Store Column; Walk Along the Store to a Store Column.

### Walk to a Workplace Attached to a Store

Objects: Source (default), `WPSource` (Transport Importer), Store, `WPStore` (Transport Importer; **Pick/Drop at Store > Walk to Workplace**), Drain + `WPDrain`; connect them.

The Worker picks a part at WPSource, steps onto WPStore, and fills the leftmost bay of the top row, then repeats until both rows are full. An observer on the Store's read-only attribute `Full` locks the Source exit and empties the Store to the Drain. Source code:

```simtalk
-- param attribute: string, oldValue, newValue: boolean
-- param attribute: string, oldValue: boolean
param newValue: boolean
Source.ExitLocked := true
if newValue
    var p:object := ?.cont
    while p /= VOID
        p.move
        waituntil p.location /= ?
        p := ?.cont
    end
end
waituntil ?.Empty
Source.ExitLocked := false
```

A `SankeyDiagram` can show the Worker's route/Sankey flows. For realism, change the Store's 3D appearance to **Rack with round posts (dynamic)** and set **Slot Dimension Z** to `0.5` m.

### Walk to a Store Column

Select **Pick/Drop at Store > Walk to Store Column** on WPStore (deactivates non-applicable settings). The Worker walks to the storage bays in the column (not onto WPStore), fills the top-left bay, and proceeds; Sankey flows thicken as the bottom row fills. When done he returns to the WorkerPool, then empties the Store to the Drain in placement order.

### Walk Along the Store to a Store Column

Select **Pick/Drop at Store > Walk Along Store to Store Column**. The Worker walks to the Store's left corner, turns right, places the part, then works along the row toward the right. Emptying follows placement order.

---

## Show Worker Statistics in a Chart

### Configure the Stations and the Workplaces

- **Station1:** Processing Time `1` second; activate Transport Importer. **WP1:** Loading Time `1.5` seconds.
- **Station2:** Processing Time `10` seconds. **WP2:** Unloading Time `2` minutes; Recovery Time `1` second.

### Configure the WorkerPools for the Chart

For each Worker (`Jack`, `Jill`): click **Workers to Create**, drag the Worker from UserObject to the **Worker** cell, set **Amount** (`2` for Jack), set **Home Location** to the workplace (e.g., `WpHomeJack` with Capacity `5`).

### Configure the Chart and View Worker Statistics

1. Chart settings: **Data Source = Worker Pools**; drag `WorkerPoolJack` and `WorkerPoolJill` into the **List of Worker Pools** table; group by **Creation Table**; **Occupancy = Operational + failed**; **Sample Mode** with Interval `1` minute.
2. Run and watch Jack and Jill carry finished parts between stations.
3. Right-click the Chart → **Show** to display Worker statistics; the SankeyDiagram shows Worker flows.

---

## Set How Many Workers Are Created During Initialization

Change the WorkerPool's **Workers to Create** for the next run via the EventController's **Init Control**, which is called once at the beginning of the run before objects are initialized and before init methods execute.

Steps:
1. Insert material flow and resource objects. Use **Beam to workplace** (no FootPaths) so Workers teleport to Workplaces without time.
2. Insert a Method for the init control (e.g., `myInitControl`).
3. Double-click the EventController → **Tools > Edit Controls**, add the method as the init control.
4. Insert a `DataTable` (e.g., `MyWorkersTable`) with columns **Worker** and **Amount**; drag the Worker(s) (e.g., John, Nellie) into the Worker column.
5. Program the amounts and assign the table to the WorkerPool:

```simtalk
MyWorkersTable[2,1] := 2 // enters the desired amount of the worker John
MyWorkersTable[2,2] := 1 // enters the desired amount of the worker Nellie
WorkerPool.setWorkersToCreateTable(MyWorkersTable)
```

6. In the EventController, open the scheduled events list — the first event is the **Init** event; processing it enters the Worker counts into **Amount** and places Worker graphics on the WorkerPool.

---

## Model Workers with Importer, Broker, and Exporter

Instead of the `Worker`, use the **Broker–Importer–Exporter** mechanism to simulate jobs done by a person or group (shared resources). Basic steps:

- Tell the station which services a job requires (services list on the **Importer** sub-tabs).
- Tell the station which Broker assigns the services (Broker text box on the Importer sub-tabs).
- Tell an Exporter which services it supplies (services list on its **Attributes** tab).
- Tell the Exporter which Broker manages its services (Broker text box on the Attributes tab).

### Model Processing Jobs

The Exporter provides services; the Broker assigns the Exporter to a Station. Stations Station1 and Station3 require `ExporterJob1` (service `Job1`); Station2 requires `Job2` from `ExporterJob2`.

Steps:
1. Insert a Source, three Stations, a Drain (connect), two Exporters, a Broker, and a Method named `reset` with source code `deleteMovables`.
2. For each Station: **Importer > Processing** → select **Active**; ensure **Common Resources** (sub-tab Set-up) is selected; deactivate inheritance for Services; enter the service (`Job1`/`Job2`/`Job1`); select the Broker (`MyBroker`).
3. For each Exporter: turn off Services inheritance; enter the service (`Job1`/`Job2`); select the Broker.
4. Plant Simulation enters the Exporters and services into the Broker (view via **View > Exporters** and **View > Offered Services**).
5. Run — because an Exporter works at one station at a time and Station1/Station3 share `ExporterJob1`, short standstills occur (one station blocked, the other waiting).

### Model Processing and Set-up Jobs

Adds a setup service. `Exporter3` provides `Setup` for all stations; `Exporter1` provides `Job1` and `Job2` for Station1/Station3; `Exporter2` provides `Job2` for Station2.

Steps:
1. Insert a Source, three Stations, a Drain (connect), three Exporters, a Broker, a product table, and a `reset` Method (`deleteMovables`).
2. Configure the Source: **MU selection > Sequence Cyclical**; select the product table; in the table enter the MU class (**MU**), amount (**Number**), and part name (**Name**).
3. For each Station: **Importer > Processing** → **Active**, enter its service (`Job1`/`Job2`/`Job3`), select Broker. Then **Sub-tab Set-up** → **Active**, clear **Common Resources**, enter `Setup`, select Broker.
4. For each Exporter: turn off Services inheritance; enter services (`Job1` + `Job3` for Exporter1; `Job2` for Exporter2; `Setup` for Exporter3); select Broker.
