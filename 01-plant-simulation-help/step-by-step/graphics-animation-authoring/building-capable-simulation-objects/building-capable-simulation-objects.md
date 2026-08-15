# Building Capable Simulation Objects

This document summarizes two step-by-step Plant Simulation tutorials: **Creating a Simulation Object with Animation** and **Modeling a Complex Receiving Department**. Both demonstrate how to build simulation objects that animate a work process in 3D.

---

## 1. Creating a Simulation Object with Animation

This tutorial models a custom screwdriver station in a Frame. It covers creating the simulation object, adding animations and interactions, testing, and fine-tuning.

### 1.1 Create the Simulation Object

1. Create a new Frame and open it. Open **Edit 3D Properties** → tab **Graphics**, and select **Show Content** to show contained objects.
2. Click **Show External Graphic Groups** on the **View** ribbon tab, then delete the graphic in the graphic group named `default`.
3. Click **Import Graphics** on the **Edit** ribbon tab to import a JT file (e.g. `Screwdriver.jt`) into the `default` graphic group.
4. Extract the first simulation object:
   - Click the floor plate of the station and press `+` until only the floor plate is selected (shown yellowish green).
   - Right-click the graphic and select **Make Simulation Object**.
   - Select `.MaterialFlow.Station` as the class, name it `PartCarrierStation`, and adjust the **Object Position** coordinates to center it on the screwdriver.
5. Select the trestle holding the screwdriver. Dark green = selected object; yellowish green = selected graphic (usable with `+` to contract selection).
6. Create a second simulation object: `.MaterialFlow.Station`, named `Trestle`, positioned at the center of the screwdriver.

### 1.2 Add Animations and Interactions

1. Right-click the trestle → **Open in New Window** (opens `.Models.MyScrewdriver.Trestle`). Press `+` until only the screw arm graphic is selected.
2. Right-click the graphic → **Make Animatable Object**. Name it `Arm`, and set its **Object Position** to the center of the screw arm.
3. Right-click the animatable object → **Use as Animation Object**. This forwards MU animation to `Arm`.
4. Close the Trestle frame. Right-click `Trestle` → **Edit 3D Properties** → **MU Animation** tab — the `Arm` now appears as the animation object (you could also type its name manually).

**Configure the self-animation of the Arm:**

- Open the Trestle in a new window, right-click `Arm` → **Self Animation**.
- Add four animation paths of type **Lines**: `Setup`, `DownAdvance`, `Reset`, `DownFinal`.
- For each path, click **Edit** and define two anchor points (click **Add** in *Path Anchor Points*, select the point, click **Edit Values**):

  ```
  Setup:       0, 0, 0    to  0, 0, 0.9
  DownAdvance: 0, 0, 0.9  to  0, 0, -0.1
  DownFinal:   0, 0, -0.1 to  0, 0, -0.22
  Reset:       0, 0, -0.22 to 0, 0, 0
  ```

- Change to the **MU Animation** tab, add a path named `Default` with a single animation point `0, 0, -0.38`.

**Configure the simulation side:**

- `PartCarrierStation`: Processing Time of `0:10` (10 seconds).
  - Exit Control `self.OnExit`:

    ```simtalk
    if ?.ExitCtrlFront 
       self.~.~.Trestle.EntranceLocked := false
       @.move
    end
    ```

  - User-defined attribute `init` (method):

    ```simtalk
    self.~.EntranceLocked := true
    ```

- `Trestle`: Set-up Time of `0:06` (6 seconds).
  - Entrance Control `self.OnEntrance`:

    ```simtalk
    var animations : any := self.~._3D.getObject("Arm").SelfAnimations 
    animations.resetAnimation
    animations.DownAdvance.schedule
    animations.startNextAnimationBlock
    animations.DownFinal.schedule
    animations.scheduleRotation(0, 360, 90)
    @.outIn(animations.AnimationTimeTotal)
    animations.playAnimation
    ```

  - Exit Control `self.OnExit`:

    ```simtalk
    if ?.ExitCtrlFront
       @.deleteObject
       var animations : any := self.~._3D.getObject("Arm").SelfAnimations
       animations.resetAnimation
       animations.Reset.schedule
       animations.playAnimation
       self.~.EntranceLocked := true
    end
    ```

  - Setup Control `self.OnSetup`:

    ```simtalk
    param setupStart: boolean 
    if setupStart 
       var animations : any := self.~._3D.getObject("Arm").SelfAnimations
       animations.resetAnimation
       animations.Setup.schedule
       animations.playAnimation
    else
       self.~.~.PartCarrierStation.EntranceLocked := false
    end
    ```

  - User-defined attribute `init` (method):

    ```simtalk
    self.~.EntranceLocked := false
    ```

### 1.3 Test the Station in the Simulation Model

- Insert a `Source` (`SourcePallets`) producing pallets, and a second `Source` (`SourceScrews`) feeding screws (JT file received from a colleague).
- Insert a `Drain` for finished pallets.
- Insert the Screwdriver station and three `Conveyors`.
- Connect all objects with **Connectors**:
  - `SourcePallets` (produces `MU > PartsCarrier`) → `ConveyorPallets` → `InterfaceInPallet` of the Screwdriver.
  - `SourceScrews` (produces `MU > Screw`) → `ConveyorScrews` → interface `InScrew`.
  - `ConveyorOut` → interface `Out` → `Drain`.

**Conveyor inclination setup:**

- `ConveyorPallets`: in **Line/Arc Parameters**, set Anchor Point Height `1 m` (first) and `0.15 m` (second) to match `SourcePallets`.
- `ConveyorOut`: **Edit 3D Properties → Appearance**, Base Height `0.15 m`; then **Segments** with Z dimension `1 m` to connect to the Drain.
- Run with a low real-time factor to observe the screwing action.

### 1.4 Fine-tune the Station

1. **Pallet at top instead of bottom:** Open the Screwdriver class, `PartCarrierStation` → **Edit 3D Properties → MU Animation**, show the `Default` path. Select the path marker (downward wedge), hold `Ctrl`, and move it down with the down arrow key until flush on `PartCarrierStation`.
2. **Screw not attached to arm tip:** Open the Screwdriver class → Trestle → `Arm` → **Edit 3D Properties → MU Animation**, visualize `Default`. Select the path marker, hold `Ctrl`, move down until flush at the tip of the Arm.
3. **Wrong side of screw attached:** Open the Screwdriver class → Trestle → **Edit 3D Properties → MU Animation**, visualize `Default`, and select **Top** as the side to attach the MU.

Run the simulation again to confirm correct behavior.

---

## 2. Modeling a Complex Receiving Department

This sample model shows three Sources producing bricks, glass bricks, and brick carriers. Bricks and glass bricks are loaded onto carriers, moved to a `ParallelStation`, then a `TransferStation` loads them onto a truck produced by a fourth Source.

### 2.1 Insert the Objects Required for Modeling the Source

1. Create a new Frame in the Class Library, named `MySourceTruckLoadedWithBricks`.
2. Insert three `Source` objects (class `MySource`, modified 3D graphic) on the left: `SourceGlassBricks`, `SourceBricksCarrier`, `SourceBricks`.
3. Insert two `AssemblyStation` objects to the right: `AssemblyGlassBricks` and `AssemblyBricks` (each places 50 bricks onto a pallet).
4. Insert a `TransferStation`, a short `Track`, and a `Source` named `SourceTrucks` (produces trucks).
5. Insert an `Interface` to connect the receiving department to the rest of the model.

> **Note:** Because the AssemblyStation connects to two stations, the order of connecting predecessors matters. If assembly fails, check predecessor numbering. Plant Simulation shows predecessors/successors in a tooltip when hovering over a Connector. Enter the correct predecessor number in **Main MU from Predecessor**.

### 2.2 Configure the Individual Stations

**Configure the MUs:**

- **Truck**: duplicate `.MUs.Transporter`, rename to `Truck`. Delete its graphic and import `Truck.jt`. Size `6.3 × 2.2 × 1.6 m`.
- **BricksCarrier**: duplicate `.MUs.Container`, rename to `BricksCarrier`. Import `BricksCarrier.jt`. Size `1.1 × 1.1 × 0.15 m`, capacity 50 parts (X-Dimension 5 × Y-Dimension 10).
- **Brick** and **GlassBrick**: duplicate `.MUs.Part` twice and rename. Both `0.2 × 0.1 × 0.05 m`.

For the bricks, use automatically generated graphics instead of JT files:

- Open the class → **Edit 3D Properties → Transformation**, activate **Scale Automatically**.
- For `GlassBrick`: activate **Material Active**, select a bluish-gray **Diffuse Color**, and a **Transparency** factor of `0.6` for a semi-transparent look. (Also activate **Material Active** and select orange as Diffuse Color.)

**Configure other objects:**

- Configure each Source to produce the MU matching its name (no other changes).
  > **Note:** Use absolute paths for MUs (leading `*`); relative paths start with `~`.
- Configure the AssemblyStations to attach MUs and let the Main MU exit. Click **Open** next to **Assembly Table**, enter `50` in the **Number** column to load 50 parts onto the carrier.
- Drag the `ParallelStation` onto the `TransferStation` to use it as the **Part Source** (default settings).
- Drag the `Track` onto the `TransferStation` as the **Target Station**, accepting `0` as Sensor Position. To make the truck stop and wait until fully loaded, select **Always Stop Container** on the **Advanced Attributes** tab.
- Open `MySourceTruckLoadedWithBricks` → **Edit 3D Properties → Graphics**, clear **Show Content**.

Insert the receiving station into the model, connect it with a Track and a Drain, and run. It creates trucks transporting two types of carriers — one loaded with normal bricks, one with glass bricks.

### 2.3 Animate Bricks on the Animation Area of the Brick Carrier

Plant Simulation automatically distributes placed objects (bricks onto the carrier) evenly across the animation area, based on object size and the carrier's size/dimensions.

Example: the carrier holds 50 bricks (each 20 cm long × 10 cm wide) on a 110 × 110 cm area. With x-dimension 5, five bricks fit side by side in x; with y-dimension 10, ten fit in y. Default container settings are used.

### 2.4 Animate Brick Carriers on the Animation Area of the Truck

Plant Simulation places objects onto the truck's loading space (animation area). Animation areas are predefined for `ParallelStation`, `Sorter`, `Store`, `Transporter`, and `Container`.

Because the truck graphic was changed (derived from `Transporter`), the animation area must be adjusted:

1. In the Class Library, right-click `MUs > Truck` → **Open In 3D**.
2. Right-click in `.MUs.Truck` → **Edit 3D Properties → MU Animation**.
3. Adjust **animation area** settings so brick carriers distribute evenly across the loading space. Plant Simulation computes the area when you click **Apply**.

**Replacing the truck graphic (TruckDumper):**

- Duplicate the `Transporter`, rename to `TruckDumper`, exchange its graphic.
- Enter the dumper as the MU in `SourceTruck`.
- Now only 6 brick carriers load instead of 8 — fix by increasing the **X-Dimension** of the loading space from `3` to `4`.
- Adjust the bed animation area: open `TruckDumper` in a new window, click the background, press the spacebar, activate and show the **Animation Area** on the **MU Animation** tab, then click the text boxes and roll the mouse wheel until the area is correct.

### 2.5 Show the Content of the Frame

Show the content of `MySourceTruckLoadedWithBricks` inside `MyPlant` instead of the Frame icon:

1. Select the Frame, press the spacebar.
2. Select **Show Content**.
3. Adjust content:
   - Clear **Visible** for the graphic group `default` so the Frame's default graphic doesn't overlay the content.
   - Delete the `Interface` of type `Exit` (not needed since the sub-Frame has only one external material flow object). Connect the sub-Frame with the Track.
4. Adjust object positions and run the simulation.

---

*Source: Plant Simulation Help, "Creating a Simulation Object with Animation" and "Modeling a Complex Receiving Department" — unpublished work, © 2026 Siemens.*
