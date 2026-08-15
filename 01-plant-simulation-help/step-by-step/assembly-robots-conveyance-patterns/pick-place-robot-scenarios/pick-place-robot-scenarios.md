# Pick and Place Parts with the PickAndPlace Robot

The `PickAndPlace` robot picks a part up at one station, rotates to another station, and places it there. It can pick up and deliver one or more parts. To deliver several parts, enter the **Capacity**.

You can insert the `PickAndPlace` robot from the folder **MaterialFlow** in the Class Library, or from the toolbar **Material Flow** in the Toolbox.

The examples demonstrate how to:

- Pick up parts and place them with the robot
- Pick up several parts and place them with the robot
- Place parts with a Target Control
- Load parts with an Exit Control
- Load and unload parts at the sensor of a Conveyor
- Set the conveying direction of the parts
- Unload stacked parts
- Animate the robot arm

Compare the sample models: **Window ribbon tab → Start Page → Getting Started → Example Models → Small Examples**. Then select the Category, Topic, and Example in the dialog *Examples Collection*, and click **Open Model**.

---

## 1. Pick Up Parts and Place Them with the Robot

Demonstrates the `PickAndPlace` robot with its default settings (no changes needed).

**Flow:** `Source` produces parts of type `MyPart` → processing station `Station` → `PickAndPlace` picks it up → rotates toward `Station1` → deposits the part → `Station1` moves it to the `Drain`.

To create the model, insert the objects to match the screenshot; use them without changing settings.

You can move the target station and right-click the `PickAndPlace` robot → **Calculate Angles** to recompute the connection angle. The **Angles Table** updates accordingly.

---

## 2. Pick Up Several Parts and Place Them with the Robot

The `SourceContainers` moves containers directly onto the `AssemblyStation`. The `SourceParts` moves parts to the `PickAndPlace` robot, which picks them up, rotates, and delivers them to the `AssemblyStation`. After loading parts onto the container, the `AssemblyStation` moves the loaded container onto the `Conveyor`, which delivers it to the `Drain`.

### Configure Sources, Containers, and Parts

- Set the part type for `SourceContainers` (e.g., `MyContainer`).
- Set the part type for `SourceParts` (e.g., `MyNewPart`); set **Interval** to `0:01` to produce a part every second.
- Configure the container to place parts in two rows of four: x-dimension `4`, y-dimension `2`, z-dimension `1`.

### Configure the Robot to Pick Up Several Parts

- Enter the **Capacity** — e.g., `8` to move eight parts at once.
- Connect the robot with `SourceParts` and `AssemblyStation`; Plant Simulation computes the angles and times into the **Angles Table** and **Times Table**.
- To visualize picking up eight parts, enter `2` in both **X-Dimension** and **Z-Dimension** (two parts along width, depth, and height — also stacks parts in height).
- If an empty pallet overlaps the loaded pallet at the `AssemblyStation`, press the **M** key (Show Manipulators) and adjust the border, or set the scale on the **Transformation** tab.
- To fix parts protruding from the transport box: right-click the container → **Open in 3D** → **Exchange Graphics** (e.g., `BoxFor2x1x2Entities.s3d`), then scale the part on the **Transformation** tab in **Edit 3D Properties** (e.g., scale `0.55`).

### Configure the AssemblyStation [robot]

- Select **Assembly Table → Predecessors** and click **Open**. Enter the predecessor number (`2`) and the number of parts to load (`8`).
- The robot picks up eight parts one after another, rotates, and loads them one by one onto the container in the same order it picked them up (FIFO).

---

## 3. Place Parts with a Target Control

`Source` moves its part directly to the `PickAndPlace` robot, which delivers it to the `Drain`. `Source1` moves its part to the robot, which delivers it to `Station`; after processing, `Station` feeds the part back to the robot, which delivers it to `Drain1`.

### Configure the Sources and the Parts

- Set the part type for `Source` and `Source1` (e.g., `Part1`).
- Define an **Entrance Control** on each source that sets the last station on which the part is located. `@` designates the part, `?` the station on which the part is located:

```simtalk
@.LastStation := ?
```

- Create the user-defined attribute `LastStation` for the part (double-click the part → tab **User-defined** → **New**; name `LastStation`, data type `object`).

### Configure the Processing Station

- Enter a **Processing Time** of your choice.
- Define the same **Entrance Control**:

```simtalk
@.LastStation := ?
```

### Configure the Robot

- Define the **Target Control** to determine the destination. `@` is the part, `?` is the station on which the part is located:

```simtalk
if ?.empty
   return
end
if @.LastStation = Source
   ?.setDestination(Drain)
elseif @.LastStation = Source1
   ?.setDestination(Station, true)
else
    ?.setDestination(Drain1)
end
```

---

## 4. Load Parts with an Exit Control

Modeling task:

- The robot picks a `Part` up from a `Source` and places it directly into a `Basket`.
- `Conveyor1` transports the basket to the `Station` (processes the part).
- `Conveyor2` transports the basket in the opposite direction.
- Once the basket stops, the robot picks up the part and places it in the `Drain`.

A `Variable` named `WaitingBasket` ensures the part is always put into the correct basket, and that the robot only picks up a part when a basket is available.

### Model the Material Flow and Program the Controls

- Duplicate `Part` → `MyPart` and `Container` → `Basket` (to avoid modifying built-in MU classes).
- `SourceParts` produces a part of type `MyPart` every 30 seconds.

**Exit Control** of `SourceParts` (control named `exitSourcePart`):

```simtalk
// exit control of the SourceParts
var Destination: object := Robot.getDestination
stopuntil WaitingBasket /= void and Destination /= WaitingBasket
@.Destination := WaitingBasket
@.move
```

- `SourceBasket` produces 4 baskets at an interval of 10 seconds.
- Insert `Conveyor1` (right to left) and `Conveyor2` (left to right), each with a sensor and a control.

**Sensor Control** on `Conveyor1` (sets how `MyPart` is unloaded from the basket; keeps the basket waiting until a new part is loaded):

```simtalk
param SensorID: integer, Front: boolean, BookPos: boolean
@.Stopped := true
WaitingBasket := @
stopuntil not @.Empty
WaitingBasket := void
@.Stopped := false
```

**Sensor Control** on `Conveyor2` (unloads the part from the basket):

```simtalk
param SensorID: integer, Front: boolean, BookPos: boolean
var MU : object
@.Stopped  := true // stop
var Destination:object := Robot
MU := @.Cont
MU.Destination := Drain
if not MU.move(Destination)
   stopuntil MU.Location /= @ and not Destination.IsLoading
end
@.Stopped := false
```

### Configure the Robot and Program Exit and Target Control

- Set the angles: drag `Conveyor1` then `Conveyor2` onto the robot; connect `SourceParts` → robot → `Drain` with connectors. Adjust angles in the **Angles Table** if needed.
- Set the **Exit Control** (`loadCtrl`):

```simtalk
// exit control of the Robot
if @.Destination = Conveyor1
   stopuntil WaitingBasket /= void
   @.move(WaitingBasket)
else
   @.move
end
```

- Set the **Target Control** (`targetCtrlRobot`):

```simtalk
// target control of the Robot
if @.Destination = Conveyor1 and WaitingBasket /= void
   ?.setDestination(WaitingBasket)
else
   ?.setDestination(@.Destination)
end
```

- Set **Target Selection** to *Exit strategy or target control*.

---

## 5. Load and Unload Parts at the Sensor of a Conveyor

Demonstrates placing parts from a processing station onto a Conveyor, a second robot loading parts onto pallets on a second Conveyor, and a third robot unloading pallets onto another processing station. The `Drain` removes the parts.

Configure the robots either:

- **With drag-and-drop** — the robot automatically creates the required sensors and controls, and enters the angle into the **Angles Table**.
- **Manually** on the tab **Exit** in the list **Target Selection** — you create sensors and program controls yourself.

### Configure the Material Flow Objects

- `SourceParts` → `Station1` → robot `PlacePartOnConveyor` → `Conveyor` (drag robot onto Conveyor, select **Operation → Place part**; creates the sensor automatically).
- `SourcePallets` → pallets on second Conveyor → robot `LoadPallets` loads parts from Conveyor onto pallets (**Operation → Load part**).
- Robot `UnloadPallets` unloads parts from pallets onto `Station2` (**Operation → Unload part**); exit behavior is *Exit strategy or target control*.
- `Station2` → `Drain` (`PartsOut`).

> **Note:** Connect robots with stations via connectors; connect the conveyor's start point to its end point so parts move in a circle.

- `SourceParts` uses built-in settings (unlimited `MyPart`).
- `Station1` processing time: 4 seconds.
- `SourcePallets`: 5 pallets of type `MyPallet`; pallet Length 0.55 m, Width 0.45 m, Height 0.33 m, X-Dimension 1, Y-Dimension 1, Z-Dimension 3.
- `Station2` processing time: 2 seconds.
- Conveyors use built-in settings.

### Configure the Robots

Each drag-and-drop operation automatically creates a sensor on the conveyor, creates a **Sensor Control** as a user-defined attribute, enters settings on the robot's **Exit** tab, and enters settings into the **Angles Table** (tab **Attributes**).

- `PlacePartOnConveyor`: **Operation → Place part**.
- `LoadPallets`: **Operation → Pick part**, then **Operation → Load part**.
- `UnloadPallets`: **Operation → Unload part**.

During the simulation, three parts are loaded onto the pallet, but in 3D only two appear because the standard 3D pallet has four predefined loading spaces. Fix this by exchanging the 3D graphic with `BoxFor3Entities.s3d` (**Exchange Graphics**), then set **Z-Dimension** to `3` to stack three parts.

---

## 6. Set the Conveying Direction of the Parts

Shows how to set the MU conveying direction in the `PickAndPlace` robot. Objects such as `Turnplate`, `Turntable`, `AngularConverter`, and `Conveyor` change the conveying direction of MUs (using previous length as new width and previous width as new length). The robot can also pick up and rotate a part arbitrarily.

**Flow:** `Source` → `Conveyor` → `AngularConverter` (changes direction from *Forward* to *Lateral right*) → `PickAndPlace` robot → `Conveyor1` → `Drain`.

- `Source` uses default settings.
- First `Conveyor` is 6 meters long, non-accumulating, gap of 1 meter between parts.
- `AngularConverter` has entry/exit length of 2 meters each.
- `PickAndPlace` robot: **MU Conveying Direction → Forwards**.
- `Conveyor1` is 5 meters long and accumulating.
- `Drain` uses default settings.

---

## 7. Unload Stacked Parts

The Z-Dimension of the `Store`, `Transporter`, and `Container` allow stacking parts. A `Transporter` transports pallets on which boxes (each containing three stacked parts) are stacked.

- First robot unloads pallets from the `Transporter` onto a conveyor.
- Second robot unloads boxes from the pallets onto the second conveyor.
- Third robot unloads the stacked parts from the boxes onto the third conveyor.

Drag the respective predecessor and successor onto each robot so the **Angles Tables** show them.

### Configure the Transporter, the Pallet, and the Box

- `Transporter`: Z-Dimension of storage area (type `Store`) = `1` (no pallets stacked).
- `Container`/`Pallet`: Z-Dimension = `3` (stacks 3 boxes).
- `Box` (duplicate the Container): Z-Dimension = `3` (stacks 3 parts); length/width chosen so 4 boxes fit on a pallet.

### Configure the Source and the Track

- Create 10 Transporters every 40 seconds.
- Set the parts loaded onto the Transporter in the **Entrance Control**. First set Transporter length to 3.2 m, then create a pallet and fill it with boxes, then produce parts until the boxes are full:

```simtalk
@.Length := 3.2
while not @.Full
   var pallet := .MUs.Container.create(@)
   while not pallet.Full
       var box := .MUs.Box.create(pallet)
       while not box.Full
       .MUs.Part.create(box)
       end
   end
end
```

- Create a sensor on the Track where the robot unloads pallets, plus a **Sensor Control** that stops the Track until the Transporter is fully unloaded:

```simtalk
param SensorID: integer, Front: boolean
@.stopped := true
var Destination:object := PickAndPlace
while not @.Empty
   var mu: object := @.cont
   if not mu.move(Destination)
       stopuntil mu.location /= @ and not Destination.isLoading
   end
end
@.stopped := false
```

### Configure the Conveyors

- Insert three Conveyors next to each other. The two on the left each get two sensors; the right one gets one sensor. Robots unload at the first sensor and load onto the next Conveyor at the second sensor. Unloading sensors are triggered by a light barrier at the rear of the part.
- The **Sensor Control** is the same for all three conveyors except the `Destination` variable (`PickAndPlace1` or `PickAndPlace2`):

```simtalk
param SensorID: integer, Front: boolean
@.stopped := true
var Destination:object := PickAndPlace1
while not @.Empty
   var mu: object := @.cont
   if not mu.move(Destination)
       stopuntil mu.location /= @ and not Destination.isLoading
   end
end
@.stopped := false
```

### Configure the Robots Unloading the Stacks

- Configure all three robots with the same settings: **Loading Time** and **Unloading Time** of 2 seconds each. Each robot places parts at the first sensor onto the succeeding conveyor.
- Double the first robot's graphic size with a **Uniform Scaling Factor** of `2`.

---

## 8. Animate the Robot Arm in 3D

On the tab **Robot Arm Animation** you set how the `PickAndPlace` robot arm is animated.

### Configure the Material Flow

Default settings are used. Flow: `Source` produces parts → first `Station` processes → robot picks them up → rotates to `Station1` and places them → `Station1` processes → `Drain` removes parts.

### Exchange the Graphic of the Robot

Right-click the robot → **Exchange Graphics**, and choose the PickAndPlace robot by Comau.

### Configure the Movement of the Robot Arm

- Enter `1` as the **Real-time Factor** so the motion is visible.
- Press the spacebar to open **Edit 3D Properties** → tab **Robot Arm Animation [PickAndPlace]**.
- Add the animation path **From 'Station' to 'Station1'**. Click **Show** to display the path, click **Extend** to add three path anchor points, then set each anchor point's elevation to `2.2` (stations are 2 m high).
- Move the anchor points to the correct positions (pick-up, exit station, enter next station, place part).
- Also add the path **Default Orientation to Station** (elevation `3.8` to avoid the indicator light) so the arm does not move through the parts holder and protective cage.

---

*Source: Plant Simulation Help (Siemens), "Pick and Place Parts with the PickAndPlace Robot".*
