# Converter, Turntable-Based Routing

This section covers material-flow objects that change the conveying direction, orientation, and routing of parts: the **Converter**, **AngularConverter**, **Turnplate**, and **Turntable**.

---

## Convey Parts Laterally with the Converter

The **Converter** can convey a part either straight through, to the left-hand side, or to the right-hand side.

Insert it from the folder `MaterialFlow` in the Class Library, or from the toolbar `Material Flow` in the Toolbox.

### Examples covered

- Convey Parts Straight Through
- Convey Parts Laterally According to Their Name
- Convey Parts According to a Strategy Control
- Send Parts to the Default Exit
- Feed Parts from a Branch Line into the Main Line

---

### Convey Parts Straight Through

Demonstrates the Converter with default settings (no changes).

- The **Source** produces parts and moves them onto a connected **Conveyor**.
- The **Converter** passes parts straight through to the succeeding **Conveyor**.
- To limit the number of parts, the Source produces 5 parts only.
- Parts move first from right to left, then from bottom to top; the notch of the part is located on its right side.

---

### Convey Parts Laterally According to Their Name

The Source produces six different part types with different frequencies. Parts move over several Conveyors to two pairs of Converters, which convey them laterally onto and off two processing stations according to their name.

#### Configure the Source

- Select time and interval at which parts are produced (adjustable interval, normally distributed time).
- Select part type and production frequency:
  - Random frequency.
  - Select the frequency table `MyParts` (a DataTable). Selecting the table automatically applies the correct format.

#### Configure the Converters to/from ProcessingA

- Open `ConverterToA`, select `Strategy > MU Name`.
- Click `Open List` and enter the part names to move to ProcessingA. For parts `A1`, `A2`, `A3` select **side 3** (exit to the left).
- Open `ConverterFromA`, select `Strategy > MU Name`.
- Click `Open List` and enter `A1`, `A2`, `A3` with **side 0** (straight on).

#### Configure the Stations ProcessingA and ProcessingB

- Insert two stations of type `ParallelStation`.
- Enter capacity: `5` as X-Dimension and `5` as Y-Dimension (25 processing places each).
- Enter a normally distributed **Processing Time**.

#### Configure the Converters to/from ProcessingB

- Open `ConverterToB`, select `Strategy > MU Name`; enter `B1`, `B2`, `B3` with **side 3** (lateral left).
- Open `ConverterFromB`, select `Strategy > MU Name`; enter `B1`, `B2`, `B3` with **side 0** (straight on).

> **Note:** Moving a part laterally to the left rotates it 90 degrees clockwise. A second lateral move rotates it another 90 degrees clockwise, so it moves backward toward the Drain.

---

### Convey Parts According to a Strategy Control

The Source produces 10 parts each of three types. A Converter conveys them laterally left, laterally right, or straight through based on their name, controlled by a **Strategy Control** method.

#### Configure the Source

- Select a **Delivery Table** and its name (a DataTable), which automatically applies the correct format.

#### Configure the Converter

- Select `Strategy > Method`.
- Right-click into the `Strategy Method` text box and select **Create Control**; Plant Simulation enters `self.OnStrategy` and opens the method.
- Enter the following code:

```simtalk
param entranceNo: integer
if @.name = "C" 
   ?.ExitForMU := 0 /* number of the exit of the converter*/
elseif @.name = "A" 
  if entranceNo = 2 
       ?.ExitForMU := 3
   else
       ?.ExitForMU := 0
   end
else
   if entranceNo = 2
       ?.ExitForMU := 1
   else
       ?.ExitForMU := 0
   end
end
```

The code conveys parts named `A` laterally left (exit 3), parts named `B` laterally right (exit 1), and parts named `C` straight on (exit 0).

---

### Send Parts to the Default Exit

The Converter sends all arriving parts to a selected **Default Exit**.

- Open the Converter dialog.
- Select `Strategy > Default Exit`.
- Select the number of the Default Exit (e.g., `3` to exit upward).

---

### Feed Parts from a Branch Line into the Main Line

The Converter feeds parts from a branch line into the main line once the configured gap is large enough.

#### Configure the Source (main line)

- Constant interval of `30` seconds.
- Part type `Part` (with a direction arrow added to its icon).

#### Configure the Converter

- Select `Strategy > Feed in`.
- Enter the gap size (**Free Space**) between parts, e.g., `5` meters.

The Converter moves parts from the branch line into the main line with the orientation in which they were fed in.

---

## Change the Conveying Direction with the AngularConverter

The **AngularConverter** changes conveying direction from lengthwise to crosswise (or vice versa). It can contain a single part at any one time.

Insert it from `MaterialFlow` in the Class Library or the `Material Flow` toolbar.

In the sample model:

- The Source `PartsIn` produces parts of type `MyCarbody` and moves them to the AngularConverter.
- The AngularConverter changes their conveying direction; the length occupied changes from **MU Length** to **MU Width**, using up the **Moving Time**.
- After the part exits, the AngularConverter returns to its original position and is ready for the next MU.

### Configuration steps

- Insert and configure the Source: name it `PartsIn`, select part `MyCarbody` (created in `UserObjects`).
- Insert the feeder Conveyor (e.g., 10 meters long).
- Insert the first AngularConverter; enter **Entry Length** and **Exit Length** of `5` meters each.
- Insert the `ProcessingConveyor`:
  - Length `2.5` meters.
  - Speed `0.001` m/s (so the part stays on the line instead of moving on). This equals a time of 41 minutes 40 seconds.
- Insert the second AngularConverter, another Conveyor, and the Drain; connect all objects with Connectors.

> The part's **Conveying Direction** is `forward` up to the change point, then `lateral right`, then `backward` toward the Drain.

---

## Align and Shrink-Wrap Parts with the Turnplate

The **Turnplate** models a rotating platform that rotates the loaded part and ensures uniform orientation of leaving parts (e.g., parcel shipping where parcels must face a barcode scanner).

Insert it from `MaterialFlow` in the Class Library or the `Material Flow` toolbar.

### Examples covered

- Align Parts with the Turnplate
- Model a Shrink Wrapper

---

### Align Parts with the Turnplate

The Source produces four parts of type `MyPart` and moves them onto the feeder line; the Turnplate rotates each part 90 degrees to the right and moves it on.

- Configure the Source: `Time of Creation > Number Adjustable`, Amount `4`, part `MyPartColored` (from `UserObjects`).
- Insert the feeder Conveyor and the Turnplate, plus a Conveyor to the Drain.
- Configure the Turnplate with default settings: `Strategy > Angle` and rotation `Angle` of `90` degrees.
- Reduce simulation speed (adjust the Simulation Time in the EventController, or drag the slider left) to observe the rotation.

---

### Model a Shrink Wrapper

Uses the Turnplate to apply an overwrap around parts on a pallet.

Flow: `SourceParts` creates nine parts → `Conveyor1` feeds the Turnplate (rotates parts 90° right) → successor line → `ParallelStation` (processes 2 minutes) → `TransferStation` (loads parts onto a pallet) → `ConveyorPallet` moves the pallet back to the Turnplate (shrink wraps) → Drain.

#### Configure the Source and Feeder Line

- Source: `Time of Creation > Number Adjustable`, Amount `9`, part `MyPart` (from `UserObjects`).
- Feeder line: Conveyor with default settings.

#### Configure the Turnplate

The Turnplate has two tasks: rotate parts 90° right, and rotate the pallet to simulate the shrink wrapper.

- Select `Strategy > Method`.
- Right-click the `Strategy Method` text box and select **Create Control**; Plant Simulation enters `self.OnStrategy` and opens the method.
- Enter the following code:

```simtalk
var rotAngle: integer
if @.typeOf(.UserObjects.MyPart)           // rotates the part
   rotAngle := 90
else
   if @.typeOf(.UserObjects.MyPallet)      // rotates the pallet
       rotAngle := -(4 * 360)              // minus (-) designates 
counterclockwise rotation
   end
end
?.rotatePart(rotAngle)
```

The leading sign sets the rotation direction: `+` clockwise, `-` counterclockwise. The example rotates the pallet four times by 360 degrees counterclockwise.

#### Configure the Conveyor Which Transfers the Parts

- Click the tab `Controls`.
- Define a length-oriented sensor that is **front triggered**.
- Right-click the `Control` text box and select **Create Control**.
- Copy the following code:

```simtalk
param sensorID: integer, front: boolean
if @.typeOf(.UserObjects.MyPart)
   @.move(ParallelStation)
end
```

#### Configure the Stations Which Handle the Pallet

- Source (pallet): `Time of Creation > Number Adjustable`, Amount `1`, Creation Times `10:00`, MU `MyPallet`.
- Insert the `ParallelStation` (no setting changes needed).
- Insert and configure the `TransferStation`:
  - Drag the ParallelStation onto the TransferStation (enters the Exit Control).
  - Drag the pallet source `ConveyorPallet` onto the TransferStation; select station type **Load** and set the sensor position.
- Reduce simulation speed with a reset method:

```simtalk
EventController.Speed := 60
```

#### Adjust Shrinkwrapper and Parts

- Set part height to `0.1` m (keep length/width `0.8` m).
- If parts show an offset, check **Booking Point Length** and **Booking Point Width** (booking point centered vs. offset).
- Replace the pallet's 3D graphic (`MyPallet` → 3D → `Exchange Graphics`, e.g., an EUR-pallet).
- Reduce part size in 3D: right-click `MyPart` → `Edit 3D Properties` → tab `Transformation` → reduce scaling (e.g., uniform scale `0.5`); clear `Scale automatically` if needed.
- Rotate the ParallelStation 90 degrees to avoid parts breaking through the glass plates.
- Save as a **3D Only** model with a different name.
- Set the EventController **Real-time factor** to `10` (makes the reset method redundant).
- Shorten the pallet's Time of Creation to `1` minute and adjust the ParallelStation processing time.
- Optionally increase pallet capacity in the Z-Dimension from `1` to `3` and triple the Source's part count.

---

## Move Parts On with the Turntable

The **Turntable** models a rotating platform that moves a part onto one of several connected material flow objects.

Insert it from `MaterialFlow` in the Class Library or the `Material Flow` toolbar.

In the sample model, the Source `PartsIn` produces parts of type `MyPart` and moves a single part onto the Turntable feeder line. The Turntable moves parts cyclically onto its successors (the feeder lines of the Drains `OutA` and `OutB`).

### Configuration steps

- Configure the Source: negative exponential distribution with parameters `0:10`, `0`, `1:40`; part `MyPart` (from `UserObjects`).
- Insert the feeder Conveyor.
- Insert the Turntable and its direct successors (feeder lines of the Drains), then connect them. The Turntable needs successors to configure its **Entry Angle Table** and **Exit Angle Table**.
- Set Turntable length `4` meters with the **Rotation Point** in the center (at `2` meters).
- Connect the Turntable to successors using the Connector (drag from the Turntable end point to the successor start point). Plant Simulation computes the angle at which the successor is located; view angles via `Exit Angles Table`.
- Configure the Drains and run the simulation.
- To turn the part around before moving onto the top feeder line, open the **Exit Angle Table** and select `Which Side > MU leaves backward` for `FeederPartA`.

### Adding a stationary base in 3D

By default the Turntable floats in the air in 3D without legs; if legs are defined, the whole Turntable (including legs) rotates. To fix this, create a cylindrical base that does not rotate:

- Open the Turntable in a new window.
- Right-click → `Edit 3D Properties` → tab `Graphics` → `Add` a new graphic group named `base`.
- On the ribbon tab `Edit`, click `Cylinder` to create the base cylinder.
- Insert the base at the grid intersection below the Turntable center.
- Right-click the base → `Make Animatable Object`, name it `base`.
- In `Edit 3D Properties`, on the `Joint` tab select `Revolute Joint` and enter `0` as the **Velocity**, so the base does not rotate when the Turntable rotates.
