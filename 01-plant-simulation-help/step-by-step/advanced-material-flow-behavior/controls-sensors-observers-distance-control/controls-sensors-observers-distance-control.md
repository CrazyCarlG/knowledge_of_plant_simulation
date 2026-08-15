# Controls, Sensors, Observers, Distance Control

> Summary of *Modeling the Flow of Materials, Advanced* — advanced material flow behavior: customizing object behavior with controls and user-defined attributes, entrance/exit controls, sensors, observers, and distance control.

## Overview

This chapter introduces advanced features for modeling the flow of materials. You will learn how to:

- Customize the behavior of objects with **controls** and **user-defined attributes**.
- Program **entrance controls** and **exit controls** that override the built-in, default transfer behavior of material flow objects.
- Define **sensors** on length-oriented objects that are triggered by the MUs moving on them.
- Define **observers** that are triggered when the value of a watchable attribute, read-only attribute, or method changes.
- Create and work with a **distance control** to prevent Transporters from colliding.

---

## Customizing the Behavior of Objects

You can customize the behavior of most Plant Simulation objects:

- Program and assign **control methods** to an object, so it reacts to certain user actions (inserting/deleting objects, etc.).
- Create **user-defined attributes** that an object does not provide by default.

### Defining Controls

You can assign a control method that makes an object take a desired action.

- **Shared control (Method object):** Program the action in a Method object and insert it into a Frame or a folder in the Class Library, so several objects can use it.
- **Object-specific control:** Create a control that applies only to the selected object, programmed in a user-defined attribute of data type `method`. The control becomes part of the object and travels with it when inserted into other Frames.

**Assign a control method** (from a Method object):

1. Program the control in a Method object.
2. Click the object to which you want to assign the control.
3. Select **Tools > Edit Controls**.
4. In the dialog *Controls*, select the Method to activate (navigate to the Frame/folder holding the Method object and click OK).

**Create a control that is part of the object** (user-defined attribute of data type `method`):

- Type a meaningful name into the text box, right-click, and select **Create Control**. Plant Simulation inserts `self.Name_you_typed`, e.g. `self.mySelectControl`.
- Or right-click and select **Create Control** to insert `self.OnBuilt_in_name`, e.g. `self.OnCreate`.

To open/modify the control:

- Click in the text box and press **F2**, or
- Hold **Shift** and double-click in the text box, or
- Select the tab **User-defined** and double-click the name of the Method.

### Creating a User-defined Attribute Manually

In addition to built-in attributes, you can add user-defined attributes (also called attribute methods) to most objects. They do not affect the built-in properties. A user-defined attribute provides most functions of a global variable — commonly used for internal purposes (e.g. attaching an article type or order number to an MU).

Example: create an attribute `Quality` for a part, change its value via a Method, then route the part to a rework station if bad.

To create a user-defined attribute:

1. Scroll to the tab **User-defined** and click **New**.
2. Enter a meaningful, **unique** name (must not collide with any built-in or user-defined attribute/method name).
3. Select a **Data Type**.
4. Enter a value compatible with the data type.
5. Click **OK** — Plant Simulation sorts the attribute alphabetically into the list.

> **Note on deleting attribute methods during execution:** If a user-defined attribute of data type `method` is deleted while executing (e.g. its MU is deleted in the Drain), execution is terminated immediately — instructions after a `waituntil` will not execute. If the attribute method was called from another Method, execution of that calling Method continues; a partially set `result` value is returned. The return value (or `VOID`) is returned to any caller (e.g. an Entrance Control), whose execution continues.

### Creating a User-defined Attribute During the Simulation

Instead of manually creating attributes, you can dynamically create/delete them during the simulation via methods.

Example model: parts with the attribute (property) `Bad` are removed after the paint shop, moved to a rework station, repainted, and fed back into the line.

**Steps to build the model:**

1. **Source** — produces a part of type `MyPart` every two minutes.
2. **Visualize good/bad parts** — create graphic groups `Good` and `Bad` (via *Open in 3D* → *Edit 3D Properties* → tab *Graphics*), each with a graphic (e.g. blue Sphere for Good, red Cuboid for Bad).
3. **Dynamically create the attribute** — a method `createMyAttr` (entered as Entrance Control of Station1) creates the attribute `Paint`:

```simtalk
@.createAttr("Paint","boolean")
```

4. **Check the paint job** — method `checkPaintJob` (entered as Entrance Control of PaintShop):

```simtalk
var val := z_uniform(1,0,1)                // random number stream, lower bound, upper bound
if val < 0.1                               // checks the value
   @.Paint := false                        // bad paint job
   @.CurrIcon := "Bad"                     // switch icon
else
   @.Paint := true                         // good paint job
   @.CurrIcon := "Good"                    // don't change icon
end
@._3D.VisibleGraphicGroups := [@.CurrIcon] // code to show graphic groups in 3D
print "Value: ",val,": ",@.CurrIcon        // prints the value and Good or Bad to the Console
```

> `z_uniform(1,0,1)` creates values between 0 and 1. Values below 0.1 set `Paint` to false (bad). This yields roughly one bad part per ten good parts.

5. **Branch on the attribute** — method `checkMyAttr` (entered as Exit Control of the station `BranchOff`):

```simtalk
if @.Paint     // checks the user-defined attribute
   @.move(1)   // moves the part along on Connector1
else
   @.move(2)   // moves the part along on Connector2
end
```

6. **Delete the attribute** — method `deleteMyAttr` (entered as Entrance Control of Station2):

```simtalk
@.deleteAttr("Paint")
```

### Creating a Tooltip as a User-defined Attribute

1. Double-click the object → tab **User-defined** → **New**.
2. Name it `Tooltip`, Data Type `string`, and enter the tooltip text into **Value**.
3. Click **Apply** and right-click the object in the 3D window to check.

The standard tooltip shows: object name (bold) → origin (`Origin: .MaterialFlow.Station`) → your tooltip text.

- To show **only** your text (without the standard info), prefix the text with a colon (`:`).
- For sub-Frames, select **Show Externally** to show the tooltip in the 3D window.

---

## Creating Entrance and Exit Controls

You can modify the built-in transfer behavior of material flow objects by programming an **Entrance Control** and/or **Exit Control**. The object calls the Method whenever an MU intends to enter or exit. These controls **override** the standard transfer behavior — you must ensure the MU moves to the correct station yourself.

Typical use: count incoming MUs and, after a specified number, route following MUs to a different successor.

A control Method can be:

- A **Method object** in a folder or Frame (Frame for objects in the same Frame; Class Library for objects across Frames), or
- A **user-defined attribute of data type `method`** (only usable by that object; typically created in the class when all instances should share it).

**Ways to specify the Method** (same process for Entrance, Exit, Backward Entrance, and Backward Exit Controls):

- Click the button and select a Method in a Frame → Plant Simulation enters the **relative path**.
- Select **Before Actions** to activate the entrance control before standard actions (e.g. Processing Time, Set-up Time, importer Services, assembly table) are started.
- Drag a Method with **Shift+Ctrl** into the text box → Plant Simulation enters the **absolute path**.
- Right-click the text box → **Create Control** to create the control as a user-defined attribute:
  - Type a name → inserts `self.Name_you_typed` (e.g. `self.ExitControlEnginePlant`), or
  - Just **Create Control** → inserts `self.OnBuilt_in_name` (e.g. `self.OnEntrance`).

To open the Method editor: press **F2**, right-click → **Open Object**, or **Shift+double-click** the text box.

> **Note:** A control created with *Create Control* is a user-defined attribute of the object, **not** a Method object. To delete it, delete the user-defined attribute (deleting the name from the text box only removes the name, not the attribute).

> **Note:** The Exit Control can have an optional parameter of data type `object`. When present, the successor object that pulls the MU (because the MU is in its blocking list) is assigned to this parameter.

---

## Defining Controls for Point-Oriented Objects

**Point-oriented objects** provide processing stations but have no length and do not consider MU length: `Station`, `ParallelStation`, `AssemblyStation`, `DismantleStation`, `Buffer`, `PlaceBuffer`, `Store`, `Sorter`, `Source`, `Drain`.

- **Entrance Control:** activated once the MU has fully entered the object (default; *Before Actions* checkbox cleared). Select **Before Actions** to activate it before standard actions start — you can then, e.g., change the Processing Time affecting the entering part.
- **Exit Control:** activated when an MU exits.
- **Front / Rear check boxes** set when the MU triggers the Method:
  - **Front** — activates as soon as the MU is ready to exit; the Exit Control must move the part onward (built-in behavior overridden).
  - **Rear** — activates once the rear of the MU has completely exited; does **not** override built-in behavior.
  - Front and Rear are not mutually exclusive.

> **Note:** The same MU can call the front-triggered Exit Control more than once if it couldn't exit and entered the destination's Blocking List — a new `Out` event re-triggers it. The rear-activated Exit Control is called **once only**.

### Change the Processing Time in the Entrance Control

Model: a `ParallelStation` with Processing Time `2:00`, and a method `MyEntranceControl` as Entrance Control (with **Before Actions**). The Source uses a Delivery Table.

```simtalk
switch @.Name
case "PartA"
      ?.ProcTime := str_to_time("10:0") // PartA will be processed for 10 minutes
case "PartB"
      ?.ProcTime := str_to_time("2:0")  // PartB will be processed for 2 minutes
end
```

Plant Simulation prompts to activate **Before Actions** when you click Apply. Run and observe events (`CreateMU`, `Out`, `StartActions`).

### Change the Importer Services in the Entrance Control

Model: a `Station` with a processing importer (tab *Importer*), Workplaces, FootPaths, WorkerPool, and Broker. `MyEntranceControl` (with **Before Actions**) rewrites the importer's services table per part name:

```simtalk
var servicesTable: table[string,integer,string]
Station.imp.getServices(servicesTable)
servicesTable.delete
switch @.Name
   case "PartA"
       servicesTable.writeRow(1,1, "ServiceA",2)
   case "PartB"
       servicesTable.writeRow(1,1, "ServiceB",1)
   case "PartC"
       servicesTable.writeRow(1,1, "ServiceA",1)
       servicesTable.writeRow(1,2, "ServiceB",1)
end
Station.imp.setServices(servicesTable)
```

### Change the Assembly Table in the Entrance Control

Model: two Sources (`SourceContainer` for pallets, `SourceParts` for parts), a `ParallelStation`, and an `AssemblyStation` with **Assembly Mode > Attach MUs**. `MyEntranceControl` (with **Before Actions**) builds the assembly list per container name:

```simtalk
var assyList: table[string,integer]
assyList.create
switch @.Name
   case "A"
       assyList.writeRow(1,1, "MyPartX",1)
       assyList.writeRow(1,2, "MyPartY",2)
   case "B"
       assyList.writeRow(1,1, "MyPartX",2)
       assyList.writeRow(1,2, "MyPartY",1)
end
Assembly.AssemblyTable := assyList
```

### Distribute Parts with an Exit Control

Model: Source produces 1000 parts to a Station; an Exit Control counts incoming parts and routes them to different successors.

```simtalk
var n: integer
n := Station.StatNumIn
if n <= 100
   @.move(Station1)
elseif n <= 300
   @.move(Station2)
else
   @.move(Station3)
end
```

- First 100 parts → `Station1`; next 200 → `Station2`; remaining 700 → `Station3`. The `@` identifies the part being moved.

---

## Defining Controls for Length-Oriented Objects

**Length-oriented objects** account for their own length and MU length: `Track`, `TwoLaneTrack`, `Conveyor`, `Turnplate`, `Turntable`, `AngularConverter`, `Converter`.

In addition to forward Entrance/Exit Controls, they provide **Backward Entrance** and **Backward Exit Controls**, activated when a `Transporter` drives in reverse.

> **Note:** A Transporter **backs up** on the Track — it does not turn around; its front still points in the direction of material flow.

> **Front direction note:** The Front of a part always points toward the end of the length-oriented object in the direction you inserted it. This also applies when moving backward.

**Entrance Control activation:**

- **Front** — when the front of the MU has entered the object. (Changing the processing time here does not affect the MU that already entered; use a formula for per-MU processing times.)
- **Rear** — when the rear of the MU has entered the object.

**Backward Entrance Controls** (Transporter backing up): **Rear** when the rear has moved on, **Front** when the front has moved on; both can be selected.

**Backward Exit Controls** (Transporter backing up at the exit): **Rear** (called once, does not override default exit strategy) or **Front** (overrides built-in behavior — must move the part onward).

> The same MU can call the front-triggered Exit Control more than once if it enters the destination's Blocking List; a new `Out` event re-triggers it.

---

## Creating a Sensor (material flow objects)

Length-oriented objects (`Track`, `TwoLaneTrack`, `Turntable`, `Conveyor`), `Transporter`, and `Tank` let you define **sensor controls** anywhere on the object, in addition to entrance/exit controls. The object activates the assigned Method once an MU passes the sensor (like a light barrier). Example actions: set transfer conditions, or change a Transporter's target velocity/icon when its front reaches the sensor.

To create a sensor:

- Right-click the position on the object → **Create Sensor**, and specify the sensor's data, or
- Click the tab **Controls** (Transporter: button **Sensors** on the *Load Bay* tab, visible when Track/Line selected and Apply clicked).

In the *Sensor* dialog:

- **ID** — auto-assigned unique number used to access the sensor from Methods.
- **Position type** — `Relative` (0..1) or `Length` (0..object length, in the unit from *File > Model Settings/Preferences > Units > Length*; invalid values turn the box red).
- **Trigger condition** — always, or only when the MU has the same **Destination** as entered in the sensor. (Automatic Routing uses this destination; the MU drives to the nearest sensor when reachable on a shorter route.)
- **Method** — the Method the sensor calls. The sensor passes the **Sensor ID** as an integer parameter if the Method declares one; otherwise the Method is called without a parameter. Or use **Create Control** to make it a user-defined attribute.

Example Method `accelerate`:

```simtalk
@.Speed := 50
@.currIcon := "car_fast"
```

- **Front / Rear** — whether the front, rear, or both activate the Method.
- **Booking Point** — the Booking Point Length of the MU calls the Method.

Manage sensors via **New / Edit / Delete** buttons; a sensor appears as a red line on the object's icon (double-click or right-click → *Open Sensor* to edit; hover for a tooltip).

---

## Creating and Deleting an Observer

Create **observers** for most built-in objects to trigger actions when the **watchable** values of attributes, read-only attributes, or methods change. The observer executes one or several methods when the value changes (a Method object or a user-defined attribute of data type `method`).

> **Note:** Only works if the value is watchable — check the column **Watchable** in *Show Attributes and Methods*.

> **Note:** Observer methods are called **after all other controls**. To react before other controls, use `stopuntil` or `waituntil` instead.

Example uses: watch `NumMUs` (a certain number of MUs on the object) or `Empty` (whether an object is empty).

**Example:** Move Station1's contents to Station2 when the read-only attribute `Occupied` of Station1 changes.

1. Open Station1 → **Tools > Edit Observers** → **New**.
2. Select the **Attribute** to watch (e.g. `Occupied`).
3. Select the **Method** to execute (e.g. `occupiedObserver`), or use **Create Control** for a user-defined attribute method.

Example Method `occupiedObserver`:

```simtalk
param attribute: string, oldValue: any
if ?.occupied
   ?.cont.move(Station2)
end
```

- `attribute` — the name of the watched value (lets a single Method serve several attributes).
- `oldValue` — the previous value (accessible after the change).
- Within the Method, `?` and `@` address the object whose value changed (Station1 here).

To delete an observer, click **Remove** in the dialog, or program it:

```simtalk
Station1.removeObserver("Occupied","OccupiedObserver")
 // "Occupied" is the name of the observer, "OccupiedObserver" is the name of the method
```

---

## Working with a Distance Control without AGVPool

To prevent a Transporter that reduces speed from being rear-ended, the following Transporter must reduce speed in time. This is done in the **Distance Control** of the Transporter.

Example: braking distance is 5 m; the Distance Control is called at 6 m to keep a 1 m safety distance.

Model setup:

1. **Configure the Source** — produces `MyTransporter1` (duplicated in Class Library folder `MUs`, renamed `MyTransporter` in `UserObjects`) via a Delivery Table (first at 0 min, second at 2 min).
2. **Configure the Track** — add a sensor at 10 m; its control stops the first Transporter:

```simtalk
param sensorID: integer, Front: boolean
if @.ID = 1
   @.Speed := 0
   print EventController.simTime, " The first Transporter stopped."
end
```

3. **Configure the Transporter** — in Class Library folder `MUs`, activate **Acceleration** and set Acceleration/Deceleration to 10 m/s² each. On tab *Controls*, select the **Distance Control** and enter the distance at which it is called (6 m).

> **Note:** When selecting a control in the object's class, activate **Absolute Path** in the *Select Object* dialog, otherwise instances won't find it.

Distance Control `myDistanceControl`:

```simtalk
// This example only applies when acceleration is activated for the Transporter.
// For Transporters without acceleration you have to delay re-starting-up,
// for example with wait 0.01 before setting the speed. This prevents that the
// distance control will be called anew because the distance is exceeded again immediately.
// ? is the transporter for which you entered the distance control and the distance
// @ is the transporter for which the distance became too great or too small
param DistanceObjectBelowLimit: boolean
if DistanceObjectBelowLimit // once the distance between the transporters
   ?.Speed := 0             // is less than 6 meters, the following one stops
   print EventController.simTime," The second Transporter decelerated."
else
   ?.Speed := 10
   print EventController.simTime," The second Transporter accelerated."
// when the distance reaches more than 6 meters, the second transporter starts again
end
```

To restart the first Transporter, an `init` method:

```simtalk
// Restarts the first transporter after a certain time.
EventController.Speed := 60 // reduces the simulation speed to better see
                            // what is going on in the model
   &reStart.methCall(10)    // calls the method 'reStart' after 10 seconds
```

And the `reStart` method:

```simtalk
Track.MU(1).Speed := 10
```

Once the distance exceeds 6 m again, the second Transporter accelerates too — Plant Simulation calls the Distance Control both when the distance becomes too small and when it becomes too great.
