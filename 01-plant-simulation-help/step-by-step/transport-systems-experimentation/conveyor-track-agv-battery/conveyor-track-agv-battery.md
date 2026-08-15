# Modeling Transport Systems, AGVs, and Battery-powered Transporters

> Source: Plant Simulation Help — Modeling Transport Systems / AGV Systems / Battery-powered Transporters.

> **How to open the sample models:** Click the Window ribbon tab, click Start Page > Getting Started > Example Models > Small Examples. Then select the respective Category, Topic, and Example in the dialog **Examples Collection**, and click **Open Model**.

---

## Model Transport Systems

You will use transport systems in a variety of ways in simulation models: simple conveyors, complex electric overhead monorails, forklifts, cranes, and automated guided vehicle (AGV) systems.

Use the **Conveyor**, **Track**, and **TwoLaneTrack** objects found in the folder **MaterialFlow** in the Class Library.

| Object | Type | Description |
| --- | --- | --- |
| **Conveyor** | active | Has its own propulsion system; transports passive parts (no propulsion of their own). |
| **Track** | passive | No propulsion of its own; serves as the route on which the active **Transporter** drives forward or in reverse. |
| **TwoLaneTrack** | passive | Like Track, but two lanes. |

Characteristics to keep in mind:

- All three are **length-oriented** objects. Plant Simulation uses their **Length** and the **MU Length** of the MUs to determine how many MUs they can hold at the same time. Point-oriented objects (Station, ParallelStation, etc.) do not use a length.
- You can create **Controls** and **Sensors** for them.
- Parts transfer from a point-oriented object to a length-oriented object **in their entirety** — they are located on the Conveyor/Track in their full length as soon as their front has moved onto these objects.
- Parts transfer between two length-oriented objects with the **Speed** entered in the dialog of the length-oriented object (important when using Entrance Controls).
- Use **Conveyor** for simple transport systems.
- Use **Track** / **TwoLaneTrack** for cross-transfer systems, AGV systems, cranes, etc.
- Activating **Automatic Routing** of Transporter, Part, and Container ensures they always find their Destination on the shortest possible route.

---

## Model a Transport System with Active Objects (Conveyor)

Use the **Conveyor** to model stationary belt conveyors, roller conveyors, etc. You can model:

- A simple conveyor between two stations
- An accumulating / non-accumulating transport system
- A fixed gap or no gap conveyor
- A multiple gap or multiple pitch conveyor
- A transport system with passive objects

### Model a Simple Conveyor Between Two Stations

A basic transport system consists of a conveyor moving parts between two processing stations (SP1 and SP2). MUs are transferred from the point-oriented station SP1 onto the length-oriented Conveyor, which transports them to SP2.

- The Conveyor moves MUs from SP1 with the **Final Speed** entered, into SP2.
- Plant Simulation computes the **Transport Time** using the Final Speed and the **Length** of the Conveyor.
- **Speed, Length, and Transport Time** depend on each other. Changing Speed or Length recomputes the Transport Time; changing the Transport Time changes the speed.

### Model an Accumulating / Non-Accumulating Transport System

- **Accumulating** (check box selected): MUs move front-to-end to each other when the conveyor exit is blocked.
- **Non-accumulating** (check box cleared): all succeeding MUs stop when the preceding MU cannot exit (they retain their distance).

The default **Capacity** of `-1` means an infinite number of MUs — capacity is then defined by the conveyor's own length and the length of the parts.

- An **accumulating** Conveyor decouples stations and behaves like a **roller conveyor**.
- A **non-accumulating** Conveyor behaves like a **belt conveyor** — the belt stops when a MU blocks the exit and restarts when the MU at the exit moves on.

> In the sample: Availability = 85% and MTTR = 6:00 min for SP1 and SP2. A failed failure profile is marked red.

### Model a Fixed Gap or No Gap Conveyor

The **gap** is the distance between the rear of the preceding part and the front of the succeeding part.

- Default **MU Distance** = `-1`: the MU Distance feature is deactivated; parts can move onto the conveyor as soon as they arrive.
- **MU Distance = 0**: no gap — no space allowed between parts.
- **Fixed gap**: the space between parts is always the same (causes the conveyor to stop frequently). Example: `MU Distance = 0.5` ensures 0.5 m between parts.
- **Minimum Gap**: space between parts will not become less than the minimum gap; prevents stopping and ensures all parts exit. Example: `MU Distance Type > Minimum Gap`, `MU Distance = 1` ensures a minimum 1 m space.
- **Minimum Pitch**: minimum distance between the **front** of the preceding part and the **front** of the succeeding part; prevents the Conveyor from stopping and from waiting for new parts, enabling it to run dry.
- **Pitch**: distance between the front of the preceding part and the front of the succeeding part; the conveyor stops and waits for new parts, and can run dry.
- **Enforce MU distance** (selected): the Conveyor keeps the specified distance even if MUs accumulate.
- **Enforce MU Distance** (cleared): MUs accumulate on the Conveyor.

> Observation when running the sample: continuous flow on the minimum-gap conveyor and the conveyor without MU Distance; the no-gap and fixed-gap conveyors stop often (waiting parts).

### Model a Multiple Gap or Multiple Pitch Conveyor

**Multiple Gap** sets the distance between the rear of the preceding MU and the front of the succeeding MU. The distance can be an integer multiple of the defined MU Distance.

- Source: **Uniform** distribution with Lower Bound 0 and Upper Bound `0:04`.
- Conveyor: `MU Distance Type > Multiple Gap`, `MU Distance = 1` meter.

**Multiple Pitch** sets the distance between the front of the preceding MU and the front of the succeeding MU (integer multiple of the defined MU Distance). With this setting the Conveyor behaves like a **chain conveyor**.

> Tip: Open the **EventDebugger**, step through the simulation event by event, and watch the event types **CheckMUDistance**, **CreateMU**, and **Out**.

---

## Model a Transport System with Passive Objects (Track)

Use **Track** or **TwoLaneTrack** for passive transport systems on which the active **Transporter** drives.

Because the Track is passive, you cannot just connect it with two stations. You must:

1. Make sure a **Transporter** is available.
2. **Load** and **unload** the Transporter.
3. To prevent MUs from automatically transferring from the preceding station (SP1) onto the Track, **do not** connect them with a Connector.

### Create and insert a Transporter

- **Via Source:** Select `Attributes > Time of Creation > Number Adjustable`, enter `Amount = 1`. To create transporters, select `MU > .MUs.Transporter`.
- **Via SimTalk** method `create` in the `init` method:

```simtalk
.MUs.Transporter.create(Track)
```

This inserts a Transporter at the end of the Track. To insert at a specific position (e.g., 5.5 m along the Track):

```simtalk
.MUs.Transporter.create(Track, 5.5)
```

### Example: load at SP1, unload at SP2

Program a control in a Method and enter its name into the relevant text box on the tab **Controls**.

Without a control, the Transporter moves to the end of the Track and stops. To make it move back to the beginning after unloading, select **Front** and enter this in the Exit Control (`FrontOutCtrl`):

```simtalk
if @.empty 
   @.Backwards := true
end
```

When the Transporter backs up to the beginning of the Track, Plant Simulation activates the rear backward exit control (select **Rear** and enter the Method name into **Backward Exit**). This control must:

- Wait until a MU is ready to exit SP1.
- Load the MUs into the Transporter.
- Move the Transporter to the end of the Track.

```simtalk
waituntil Sp1.occupied and SP1.cont.finished
SP1.cont.move( @ ) // load the part
@.Backwards := false
```

- Line 1 waits until a MU is located on SP1 and is fully processed.
- Line 2 loads the MU onto the Transporter (`@` addresses the Transporter).
- Line 3 tells the Transporter to move forward again.

At the end of the Track the Transporter must wait until SP2 is empty, unload, and move back:

```simtalk
if @.empty 
   @.Backwards := true
else
   waituntil SP2.empty prio 1
   @.cont.move(SP2)
   @.Backwards := true
end 
```

---

## Model a Tugger Train

A tugger train consists of a **tractor** and a number of **trailers** it pulls. The sample model demonstrates:

- Defining the Tractor
- Modeling the Source creating the tugger trains
- Modeling the Tracks
- Configuring loading/unloading stations

### Define the Tractor

1. Duplicate the object **Transporter** in the Class Library and rename it to **Tractor**.
2. Double-click **Tractor**; select the check box **Is Tractor**.
3. To prevent the tractor from loading parts onto its bed: enter `0` as **X-Dimension** and **Y-Dimension**. For loading space types Track and Line, enter `0` as **Capacity**.

> Plant Simulation 2606 provides a pre-configured tractor unit and different trailers under **Manage Class Library > Standard Objects > Containers and Transporters**.

### Model the Source creating the Tugger Trains

Modeled in the Frame **SourceTuggerTrains** to keep the overall model uncluttered. The Frame contains:

- A **Source** that creates tractors and trailers according to a sequence table.
- A **Track** long enough to hold the entire tugger train (a tractor + four trailers, each 1.5 m → Track length 10 m).
- A **Method** that programs how trailers are hitched when they collide with the trailer in front.

### Configure the Source and Create the Sequence Table

1. In the Source, select `MU Selection > Sequence`.
2. Select the DataTable **MySequenceTable**. Create one tractor (MU class **Tractor**) and four trailers (MU class **Transporter**).
3. The characters in the **Attributes** column serve as placeholders for sub-tables; set attributes within the sub-tables:
   - Tractor: `IsTractor = true`, `Speed = 1.0 m/s`.
   - Trailers: `IsTractor = false`, `Speed = 1.1 m/s` (so they drive faster and collide with the object in front), and `CollisionCtrl` set to the collision control Method name (e.g., `hitchMethod`).

### Program the Collision Control

The collision control hitches the colliding trailer to the one in front of it (and the front trailer to the tractor):

```simtalk
if @.isTractor = false then
@.hitchFront(@.FrontMU)
end
```

### Model the Tracks

Model a **main line**, a **side line** that splits off and feeds back. Use four Tracks connected with Connectors. To move the side line over the main line, hold Shift and/or Ctrl and press the arrow keys.

Insert:

- The Frame **SourceTuggerTrains** (producing the tugger trains), connected with the Track.
- A **Source** producing parts (default settings) and a station that loads them onto the trailers.
- An **unloading station** on the main line and the side line each, plus a **Drain** each (`ShippingMain`, `ShippingSide`), with default settings.
- An **EventController** to run the simulation.

### Configure the Loading and Unloading Stations

Model loading/unloading stations with the **TransferStation** object (see also: Load, Unload, and Reload Parts with the TransferStation).

- Configure the loading station on tab **Attributes**: select which object provides the parts (**parts from** = SourceParts) and on which object the tugger train moves (**target is on** = Track).
- Enter the sensor position that triggers loading (e.g., `7` meters). The TransferStation enters these settings into the dialog **Sensor** of the Track.
- Configure `UnloadingMain` and `UnloadingSide` similarly.

---

## Stop the Transporter at Its Destination

Demonstrates stopping the Transporter at its Destination, waiting for a Part, then starting again.

Objects:

- **SourceT** produces a single Transporter.
- **SourceP** produces an infinite number of Parts and passes them to **Station1**, which processes them.
- The Transporter drives from Track2 onto the Track, accelerates, drives to its first Destination Station1, and decelerates in front of **Sensor1**. It waits there until the Part is processed and Station1 loads it onto the Transporter.
- The Transporter accelerates again, drives on, decelerates in front of **Sensor2** at Station2, waits, and passes the Part to Station2.

Define Transporter properties in the **Entrance Control** of SourceT:

```simtalk
@.XDim = 1
@.YDim = 1
@.StopAtDestination = true
@.AccelerationEnabled = true
@.Acceleration = 0.2
@.Deceleration = 0.2
@.Destination = Station1
```

**Sensor Control of Sensor1:**

```simtalk
param SensorID: integer, Front: boolean, BookPos: boolean
var station = ?.sensorID(SensorID).Destination
waituntil station.Cont /= void and station.Cont.Finished
-- Wait until the station's content is not empty and the station's 
-- content has finished processing.
station.Cont.move(@)
@.Destination = Station2
@.Stopped = false
```

**Sensor Control of Sensor2:**

```simtalk
param SensorID: integer, Front: boolean, BookPos: boolean
var station = ?.sensorID(SensorID).Destination
var part    = @.Cont
part.move(station)
waituntil part.Location /= @
-- Wait until the part's location is not empty, i.e., until a part 
-- is located there.
@.Destination = Station1
@.Stopped = false
```

> See also: **Stop at Destination**, **StopAtDestination** [SimTalk].

---

## Using Automatic Routing

Automatic routing ensures parts always reach their destination object on the shortest possible route.

- **Automatic Routing of the Transporter** (tab **Routing** of the Transporter): the Transporter finds its Destination along the **shortest** route.
- **Automatic Routing of Part and Container** (tab **Routing** of Part and Container): the Part and the Container find their Destination along the **fastest** route.

### Work with Automatic Routing of the Transporter

The Source **SourceTransporters** creates Transporters that wait for parts at the sensor of the **LoadingStation**. The Sensor Control waits until **SourceParts** has produced a part of type **MyPart**, loads it onto the Transporter, then determines the destination (Unload1, Unload2, or Unload3). After unloading, the Transporter returns to the LoadingStation.

Steps:

1. Insert and configure the Tracks.
2. Program the loading control.
3. Configure the Sources and the Transporter.
4. Program the unloading control.
5. Make the 3D model visually pleasing.

**Insert and Configure the Tracks**

- Duplicate Source, Track, Connector, Transporter, Part, Method, and DataTable into the folder **UserObjects**, rename them, and add them to the **User Objects** toolbar.
- Build the route network from three route loops (create one loop, copy and insert twice), then connect upper Tracks with Connectors. Make sure route pieces are connected.
- Rename route pieces: **LoadingStation**, **Unload1**, **Unload2**, **Unload3**. Color them (tab **Curve > Color**).
- Create a sensor on **LoadingStation** (right-click > Create Sensor).
- Insert the two Sources (Transporters and Parts), the **SequenceTable**, and the method **unload**.

**Program the Control for Loading the Transporter**

```simtalk
param SensorID: integer, Front: boolean
waituntil SourceParts.Occupied prio 1
SourceParts.Cont.move(@)
if (@.ID mod 2) = 0
   @.Destination := Unload2
elseif (@.id mod 3) = 0
   @.Destination := Unload3
else
   @.Destination := Unload1
end 
@.DestCtrl := "unload"
```

> The anonymous identifier `?` designates the part assigned to the contents of the calling object. The destination is assigned by `@.ID mod 2` / `mod 3`, so each third part receives an identical destination. The method `unload` is assigned as the **Destination Control (DestCtrl)**.

**Configure the Sources and the Transporter**

- **SourceTransporters**: `MU Selection > Sequence` with **SequenceTable**; set **LoadingStation** as Destination in the subtable **Settings**. Connect SourceTransporters to `MyTrack5` with a Connector.
- **SourceParts**: select **MyPart** as the MU (default otherwise). No Connector needed (parts moved by control).
- **MyTransporter**: activate automatic routing on tab **Routing**.
- **MyPart**: default settings.

**Program the Control for Unloading the Transporter** (method `unload`)

```simtalk
@.deleteMovables
print @,":"
print "Previous destination: ",@.Destination // write the previous
                                             // destination to the Console
@.Destination := LoadingStation
@.DestCtrl := ""
print "New destination: ",@.Destination      // write the new 
                                             // destination to the Console
@.move
```

**Make the 3D Model Visually Pleasing**

- Use **New Standard Graphics** to replace the outdated Track icon with the version 15+ icon.
- Select different colors for the lanes of the loading/unloading Tracks in 3D.
- Activate and display the **Captions** of the loading/unloading stations; click the tab **View** of the 3D ribbon tab to show names.
- Drag the mouse over a Transporter to show its name, current location, destination, and previous route in a **Tooltip**.
- **View > Route to Destination** selects the objects that are part of the route to the destination in the Frame.

### Work with Automatic Routing of Part and Container

Demonstrates how a **Pallet (Container)** automatically finds its destination on Conveyors. The Part and the Container find their Destination along the **fastest** route.

The Source **SourcePallets** creates Pallets that wait for parts at the sensor of the LoadingStation. When a Pallet reaches its destination, the part is unloaded and the Pallet returns to the LoadingStation.

Steps:

1. Insert and configure the Conveyors.
2. Configure the unloading stations.
3. Program the loading control.
4. Configure the Sources and the Pallet.
5. Program the unloading control.
6. Make the model visually pleasing.

**Insert and Configure the Conveyors**

- Duplicate Source, Conveyor, Connector, Container, Part, Method, and DataTable into **UserObjects**.
- To reuse the route network: save the Transporter model under a new name, then hold **Alt** and drag `MyConveyor` (in User Objects) onto `MyTrack` — this replaces all instances of MyTrack with MyConveyor. Rename route pieces (e.g., MyTrack1 → MyConveyor1).
- Configure the LoadingStation and the three unloading stations.
- Change the sensor of the LoadingStation (right-click > **Open Sensor**). As the Destination is the LoadingStation itself, Plant Simulation enters `self`.

**Configure the Unloading Stations**

- Create a sensor in the center of each of Unload1/2/3.
- Select **Only when Destination** to activate the sensor only when the Pallet has the same Destination.
- The Destination of the action (unloading) is the respective station (Plant Simulation enters `self`).
- Enter `unload` as the Control.

**Program the Control for Loading the Pallet**

```simtalk
param SensorID: integer, Front: boolean
waituntil SourceParts.Occupied prio 1
SourceParts.Cont.move(@)
if (@.ID mod 2) = 0
   @.Destination := Unload2
elseif (@.id mod 3) = 0
   @.Destination := Unload3
else
   @.Destination := Unload1
end
```

**Configure the Sources and the Pallet**

- **SourcePallets**: `MU Selection > Sequence` with **SequenceTable**; set **LoadingStation** as Destination in the subtable **Settings**.
- **SourceParts**: **MyPart** as MU (no Connector needed).
- **MyContainer**: activate **Automatic Routing** on tab **Routing**.
- **MyPart**: default settings.

**Program the Control for Unloading the Pallet** (method `unload`)

```simtalk
@.Cont.move(MyDrain)
print @,":"
print "Previous destination: ",@.Destination // write the previous
                                             // destination to the Console
@.Destination := LoadingStation
print "New destination: ",@.Destination      // write the new 
                                             // destination to the Console
print                                        // add an empty line
```

**Make the Model Visually Pleasing**

- Select different colors for the lanes of the Conveyors.
- Activate and display Captions; click the **View** ribbon tab to show names.
- Because the Conveyors were created by replacing Tracks, adjust the **Base Height** for each instance to `1` (Conveyors are elevated on legs, unlike Tracks placed flush on the floor).
- Drag the mouse over the Pallet to show a Tooltip.
- **View > Route to Destination [Part, Container]** selects the objects on the route.

---

## Model an Automated Guided Vehicle System (AGVS)

Use the resource objects **AGVPool** and **Marker** to model AGV systems. The AGV, starting at the AGVPool, covers the designated route along the inserted markers, driving freely within the installation space.

> **Note:** Keep Markers **aligned** to prevent Plant Simulation from computing unnecessary roundings. Misaligned Markers may occur if you inserted them while **Show Grid** was off.
> **Note:** To show/hide a Marker, click **Show Connections**.

The AGV can:

- **Cover a Route Along Omnidirectional Markers** — the AGV turns in front of the markers according to the computed angle toward the next marker.

```simtalk
var AGV : object := AGVPool.Cont
AGV.setRoute([M1,M2,M3,M4]) // sets the route
waituntil AGV.DestinationWasReached
AGV.DestinationWasReached := false 
// recognizes when the destination of the route was reached  
print "The AGV is ready for the next route."
```

- **Cover a Route Along Directional Markers** — the AGV drives onto the marker and rotates toward the marker around the default angle of 0° in the direction of the next marker.
- **Cover a Route Along Directional Markers with the Defined Angle** — the AGV drives toward the marker at a defined angle (e.g., 90°), crosses it, and leaves at that angle.
- **Cover a Route According to a Segments Table** — using the method `setRouteSegments`.

In addition:

- Load Parts Onto an AGV and Rotate Them
- Fine-position an AGV
- Prevent AGVs from Colliding

> See also: **AGV**, **Marker**, **AGVPool**.

### Cover a Route Along Omnidirectional Markers

The AGV covers the route along omnidirectional markers, turning in front of each marker toward the next marker.

1. Duplicate **Transporter** (in MUs) and **Marker** (in Resources) into **UserObjects**; rename (e.g., `MyAGV`).
2. Insert the **AGVPool** from tab **Resources** in the Toolbox (AGVs are created in the AGVPool); use the duplicated `MyAGV`.
3. Insert four Markers **M1–M4**. To see identifiers, select each Marker, press spacebar, and configure Captions.
4. Program the route in a Method (`setRoutePattern`):

```simtalk
var AGV : object := AGVPool.Cont
AGV.setRoute([M1,M2,M3,M4]) // sets the route
waituntil AGV.DestinationWasReached
AGV.DestinationWasReached := false 
// recognizes when the destination of the route was reached  
print "The AGV is ready for the next route."
```

5. Call it from the `init` method:

```simtalk
// set the route pattern
setRoutePattern()
```

6. Run the simulation (Real-time factor 3 recommended in the EventController).

### Cover a Route Along Directional Markers

1. Duplicate the omnidirectional marker model.
2. Convert the omnidirectional markers to directional markers: double-click Marker M1, select **Use Rotation of Marker** on tab **Attributes**, click OK (default angle 0°). Repeat for the remaining Markers.
3. Run the simulation — the AGV drives across the Markers from M1 to M4 and turns on each Marker with the specified angle toward the next Marker.

To use a different rotation angle (e.g., 90°):

1. Click the Marker and press spacebar to open **Edit 3D Properties**.
2. Type the rotation angle into the text box **angle** in group box **Rotation**; click **Apply** to preview.
3. Click **OK** to apply.

The AGV then drives toward the Marker at 90°, crosses it, and leaves at 90°.

### Cover a Route According to a Segments Table

The AGV covers the route according to route segments set in a table using `setRouteSegments`.

```simtalk
var AGV : object := AGVPool.Cont
var route:table[length, real, length, speed]
route.create
route.appendRow(2)
route.appendRow(void, -90, 1, 0.2)
route.appendRow(void,  90, 1, 0.2)
route.appendRow(2)
route.appendRow(void, -90)
route.appendRow(2)
route.appendRow(0.5, -90)
agv.setRouteSegments(route)
stopuntil agv.DestinationWasReached
```

- Rename the Method to `init` so the simulation runs immediately after resetting.
- To inspect the created table: insert a break point in the last row, run the Method, then double-click the cell **Value** in the column **Name** on tab **Variables** in the Method-Debugger.

Table columns:

1. **Length** of the straight segment.
2. **Angle** with which the curve changes direction.
3. **Radius** of the curved segment.
4. **Speed** with which the AGV drives on this segment.

> To trace how the AGV drives on individual segments, open the **EventDebugger** and step through segments one after another.

### Load Parts Onto an AGV and Rotate Them

Demonstrates an AGV driving underneath a Conveyor, loading a pallet, and rotating it while driving to its destination; then returning and picking up the next pallet.

**Insert the Material Flow Objects**

- **Source** produces parts of type **Container** (the pallet) every 20 seconds.
- **Conveyor1** (default settings) transports pallets to the pick-up place (where the AGV drives underneath and loads the pallet).
- Create an **Exit Control** (user-defined attribute) on Conveyor1 to set the AGV route and rotate the pallet:

```simtalk
waituntil AGVPool.NumIdleAGVs > 0
var agv := AGVPool.getIdleAGV
agv.setDim(1,1)
agv.setRoute([MarkerPick])
waituntil agv.DestinationWasReached
@.move(agv)
@.ConveyingDirection := 1
agv.setRoute([MarkerPlace])
wait 1
agv._3D.getObject(1).moveTo(90)
waituntil agv.DestinationWasReached
@.move(Conveyor2)
agv.setRoute([M1,M2,M3,M4,M5,M6,M7])
agv._3D.getObject(1).moveTo(00)
waituntil agv.DestinationWasReached
agv.IsIdle := true
```

**Create the Conveyor on Which to Place the Pallet**

- Set **Base Height = 0.4 m** for Conveyor1; add a new graphic group named `graphic`.
- Open Conveyor1 in a new window and create four posts (height 0.4 m, width and depth 0.1 m each) matching the Base Height.
- Insert **Conveyor2** (default settings) for placing pallets.
- Insert a **Drain** (default settings) to remove pallets.

**Insert the Transport Components**

- Duplicate the **Transporter** (in MUs) to avoid changing the built-in class.
- Create an animatable plate on the AGV loading space:
  - Right-click the Transporter in UserObjects > **Open in 3D**.
  - Create a **Cylinder**; right-click it > **Make Animatable Object**, name it `Plate`.
  - In the opened dialog, tab **Joint**: select **Revolute Joint**, **Velocity = 20**.
  - Type `Plate` as the **Animation Object** of the AGV.
- Insert the **AGVPool** (default creates the Transporter).
- Insert the **Markers**: M1–M7 are omnidirectional; **MarkerPick** and **MarkerPlace** are directional.

Run the simulation: the AGV drives from the AGVPool underneath Conveyor1 to MarkerPick, picks up the pallet; on its way to MarkerPlace the pallet rotates on the AGV and is placed rotated on Conveyor2. The AGV then returns and repeats.

### Fine-position an AGV

If the AGV drives freely, you sometimes need to fine-position it using the methods **rotate** and **drive** of the Transporter.

Example: the AGV drives from AGVPool via M1 to M2, rotates 90° left and drives 2 m upward, moves sideways 1.6 m left, loads a part from the Station, moves sideways 1.6 m right, drives backward to M2, rotates 90° right, drives via M3 to M4, unloads onto Station1, and drives back via M2 and M1.

```simtalk
var AGV := AGVPool.Cont
AGV.setRoute([M1, M2])             // AGV drives to the marker M2
stopuntil AGV.DestinationWasReached
AGV.rotate(-90)                    // AGV rotates 90° to the left
stopuntil AGV.DestinationWasReached
AGV.drive(2)                       // AGV drives 2m upward
stopuntil AGV.DestinationWasReached
AGV.drive(1.6, -90)                   // AGV moves sideways in a 
stopuntil AGV.DestinationWasReached   // 90° angle 1.6 m to the left
var MU := Station.Cont
waituntil MU.Finished                 // MU waits until it's processed
wait 2                                // MU waits 2 seconds
MU.move(AGV)                          // MU moves to the AGV
wait 2                                // AGV waits 2 seconds
AGV.drive(1.6, 90)                    // AGV moves sideways in a 
stopuntil AGV.DestinationWasReached   // 90° angle 1.6 m to the right
AGV.drive(-2)                         // AGV drives 2m downward
stopuntil AGV.DestinationWasReached
AGV.rotate(90)                     // AGV rotates 90° to the right
stopuntil AGV.DestinationWasReached
AGV.setRoute([M3, M4])             // AGV drives across M3 to M4
stopuntil AGV.DestinationWasReached
waituntil Station1.empty           // AGV waits until Station1 is
wait 2                             // empty, waits 2 seconds
MU.move(Station1)                  // MU moves to Station1
wait 2                             // AGV waits 2 seconds
    
AGV.setRoute([M2, M1, AGVPool])    // AGV drives via the markers M2
                                   // and M1 back to the AGVPool
```

### Prevent AGVs from Colliding

Use the **Distance Control** of the Transporter to prevent two AGVs from colliding.

1. Insert an **AGVPool** that creates the AGVs.
2. Insert four Markers for each Transporter: Transporter1 covers M11–M14; Transporter2 covers M21–M24.
3. Insert an `init` control that finds an idle AGV and sets routes.
4. Configure:
   - AGVPool: default settings (AGV is the Transporter in MUs).
   - **Safety Zones** of the Transporter: default settings.
   - **Distance Control**: default settings.

`init` control:

```simtalk
var AGV1 := AGVPool.getIdleAGV
AGV1.setRoute([M11, M12, M13, M14])
wait 2
var AGV2 := AGVPool.getIdleAGV
AGV2.setRoute([M21, M22, M23, M24])
```

> Observation: Transporter2 slows down when Transporter1 enters its Safety Zone 2, stops when it enters Safety Zone 1, and continues once Transporter1 has passed safely.
>
> To show Safety Zones: **Edit 3D Properties > Tab Appearance > Show Safety Zones**. If markers M11 and M12 are moved left so Transporter2 arrives first at the crossing, Transporter1 slows and stops instead — confirming the safety zone and Distance Control prevent collisions.

---

## Model a Battery-powered Transporter, Basic

A quick way to model a battery-powered Transporter. Transporters drive on a Track moving parts; the Track's **Exit Control** detects the battery charge — if enough power remains it continues moving parts, otherwise it drives to the charging station.

1. Duplicate the **Transporter** in the Class Library and rename it to **TransporterBattery**.
2. Configure the **Battery** tab.
3. Enter the **Charge Control**:

```simtalk
if @.BatCharge >= @.BatCapacity
   @.Stopped := false
end
```

4. Model the material flow and configure the objects:

**Source** (feeds Transporters): selected settings.

**Exit Control** of the Track (sends a low-battery Transporter onto `ChargeBattery`):

```simtalk
if @.BatCharge <= @.BatReserve
   @.move(1)
else
   @.move(2)
end
```

**Two Sensors** on the Track:
- At sensor ID 3, the **TransferStation** loads parts onto the Transporter's loading space.
- At sensor ID 1, the **PickAndPlace** robot unloads parts and places them on the Conveyor. **Sensor Control OnSensor1**:

```simtalk
param SensorID: integer, Front: boolean, BookPos: boolean
// Activating the sensor moves the parts on to the designated
// destination, namely the PickAndPlace robot.
@.Stopped := true
var Destination:object := PickAndPlace
while not @.Empty
   var MU: object := @.cont
   if not MU.move(Destination)
      stopuntil MU.Location /= @ and not Destination.IsLoading
   end
end
@.Stopped := false
```

- **SourceParts**: default settings.
- **TransferStation**: selected settings.
- **PickAndPlace**: Loading Time and Unloading Time of 2 min each, plus Exit tab settings.
- **Conveyor**: create the sensor at which the PickAndPlace robot places parts.

**Sensor in the Track `ChargeBattery`** and its **Sensor Control**:

```simtalk
param SensorID: integer, Front: boolean, BookPos: boolean
@.Stopped := true
@.BatCharging := true
NumberOfBatteryCharges += 1 // increments the number of battery charges
                            // in the Variable
```

5. Insert a graphic representing the charging station and a Variable **NumberOfBatteryCharges** (counts battery charges).

---

## Model a Battery-powered Transporter, Extended

Model a battery-powered Transporter using the tab **Battery** settings:

- The battery must be charged when the charge is lower than the **Reserve Charge**.
- Power consumption during operation consists of **Driving Consumption** and **Base Consumption**.
- In the **Charge Control**, prevent the battery from fully discharging and stopping the Transporter.
- For charging, the Transporter requires **Charge Current**; recharge time = difference between battery **Capacity** and current charge, divided by the charge current of the charging station.
- When the **Reserve Charge** (during driving) or **battery capacity** (at end of charging) is reached, the Charge Control is called. Differentiate these events using the **BatCharge** attribute.

Steps:

1. Model the material flow.
2. Program the Sensor Control for loading/unloading.
3. Configure battery-powered operation.
4. Program the battery controls.

### Model the Material Flow

- **Source** constantly creates parts of type **MyPart**.
- Parts move to a **Buffer** (standard settings).
- For the **Track**, create two sensors: parts load onto the Transporter at the Buffer, and unload at the Station. **Connect the start and end points of the Track so Transporters can drive in a circle.**
- **Station** and **Drain**: standard settings.
- Insert a Track **ChargingStation** and another Track **ParkingPosition**.
- In the **Init Control**, create one Transporter on the Track and one on the ParkingPosition:

```simtalk
// create two Transporters
.UserObjects.MyTransporter.create(Track, 8)
.UserObjects.MyTransporter.create(ParkingPosition)
```

### Program the Sensor Control for Loading and Unloading the Parts

```simtalk
param SensorID: integer, Front: boolean, BookPos: boolean
// load parts at sensor 1 from the Buffer onto the Transporter
if sensorID = 1
   @.Stopped := true
   repeat
       waituntil Buffer.Occupied prio 1
       Buffer.cont.move(@)
       wait 3 // the loading time is 3 seconds
   until @.Full
   @.Stopped := false
// unload parts at sensor 2 from the Transporter onto the Station
elseif sensorID = 2 
   @.Stopped:=true
   repeat
       waituntil Station.Empty prio 1
       @.cont.move(Station)
       wait 3 // the unloading time is 3 seconds
   until @.Empty
   @.Stopped := false
end
```

### Configure Battery-powered Operation of the Transporter

**Battery Settings** — enter settings on tab **Battery** (other settings unchanged).

**Excursus: The relative and the absolute path**

- For the **Charge Control**, if you only enter its name and click Apply, Plant Simulation highlights the text box red because it does not find the charge control within the Class Library namespace with the specified relative path. This is acceptable because the Transporters are created in the Frame `Model` and are thus located within the same namespace as the Charge Control.
- If you click the button in the Transporter dialog, navigate to the Frame `Model`, and select the charge control in **Select Object**, Plant Simulation inserts the **relative path** (designated by the tilde `~`).
- Selecting **Absolute Path** inserts the **absolute path** (designated by the asterisk `*`); the simulation then runs without errors, but renaming the Frame breaks the absolute path. **The relative path is preferred in most cases.**

**Additional Settings**

- Speed of the Transporter: `0.5 m/s`.
- **Entrance Control** of the ChargingStation: `startCharging`.
- ParkingPosition: standard Track settings.

### Program the Battery Controls

**Charge Control** `myBatteryChargeControl` — charges the battery, then moves the fully charged Transporter onto the ParkingPosition:

```simtalk
// battery charge control of the Transporter, recognizes that the battery 
has to be charge, 
// once the charge is smaller than or equal to the battery reserve
if @.BatCharge <~= @.BatReserve 
   @.BatCharging := true   // start charging the battery
   @.transfer(ChargingStation)
elseif  @.BatCharge >~= @.BatCapacity
   @.move(ParkingPosition)  // move Transporter with charged battery to 
ParkingPosition
end
```

**Entrance Control** of the ChargingStation — moves the fully charged Transporter from the ParkingPosition onto the Track:

```simtalk
// entrance control of the ParkingPosition
waituntil ParkingPosition.NumMU > 0 prio 1
ParkingPosition.Cont.move(Track, 9)
```

> When running the simulation, the Transporters circulate and first move onto the ChargingStation when the battery charge is low, then move on to the ParkingPosition.
