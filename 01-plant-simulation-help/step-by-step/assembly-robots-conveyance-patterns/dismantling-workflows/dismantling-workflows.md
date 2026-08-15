# Assembling & Dismantling Workflows

Summary of Plant Simulation help topics covering the **AssemblyStation** (assembling parts) and the **DismantleStation** (removing parts).

---

## 1. Assembling Parts with the Assembly Station

The **AssemblyStation** adds mounting parts to a main part (e.g. doors to a car body, legs to a table top). It either moves the mounting parts to the main MU — according to the value entered in the **Assembly Table** — or deletes them.

Insert it from the folder **MaterialFlow** in the Class Library, or from the toolbar **Material Flow** in the Toolbox.

The examples cover:

- Assemble Kitchen Tables
- Always Fill-up the Main MU with Parts
- Assemble Parts Sequentially
- Assemble Parts Sequentially with the Worker
- Set How Workers Deliver Mounting Parts

> **Compare sample models:** Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples. Select Category, Topic, Example, then click Open Model.

---

### 1.1 Assemble Kitchen Tables

Basic sample that produces two table types and attaches table legs to table tops.

- **Source `TableTopsIn`** produces two brown + two white table tops (via `MU Selection > Sequence Cyclical` using DataTable `TableTops`).
- **Source `TableLegsIn`** produces legs in different colors (via `MU Selection > Sequence Cyclical` using DataTable `TableLegs`).
- Sources send parts to the **AssemblyStation**, which attaches matching legs to tops, then sends finished tables to a **Drain**.

#### Create the Assembly

- Sources are configured to produce parts (table tops and table legs).
- `TableTopsIn`: MU Selection > Sequence Cyclical → select DataTable `TableTops`.
- `TableLegsIn`: MU Selection > Sequence Cyclical → select DataTable `TableLegs`.
- Sequence Table entries: drag the MU (e.g. `TableTop`) into the `MU` cell, enter the `Number` (e.g. `2`), and the part name/icon (e.g. `TableTop_A`) into the `Attributes` subtable named `a1`.

AssemblyStation configuration:

- `Assembly Table > Predecessors` → click **Open**, enter predecessor number (e.g. `2` for legs) and number of parts to attach (e.g. `4`).
- **Assembly Mode** → `Attach MUs`.
- **Main MU** → the finished table (arrives from predecessor 1).

> **Note:** If assembly does not work as expected, check the sequence in which predecessors are connected. Dragging the mouse over a Connector shows its number in the tooltip. Ensure the Main MU arrives from the correct predecessor.

#### Adjust the Graphics

- Set `MU Size` for the `TableLeg` and `TableTop` classes.
- Create 3D graphics for legs/tops: right-click object in Class Library → **Open in 3D** → spacebar → **Graphics** tab → add graphic groups (`Leg_A`, `Leg_B`, `TableTop_A`, `TableTop_B`) → delete the `default` graphic → **Edit** tab → insert a **Cylinder** (legs) or **Cuboid** (tops) → **Material** tab → `Material Active` + color.

To display the correct color based on the arriving part name, a user-defined attribute and an observer are used. Example observer source code (table leg, `OnPictureName3DChanged`):

```simtalk
// param attribute: string, oldValue: string, newValue: string
// param attribut: string, oldValue: string
param newValue: string
self.~._3D.VisibleGraphicGroups := [newValue]
```

For the table top observer `OnPictureName3DTableTopChanged`:

```simtalk
// param Attribute: string, oldValue: string, newValue: string
// param Attribut: string, oldValue: string
param newValue: string
self.~._3D.VisibleGraphicGroups := [newValue]
```

The attribute name (`PictureName3D`, `PictureName3DTableTop`) and the graphic group name are entered into subtables `a1` and `a2` of `TableLegs` / `TableTops`.

- Correct MU position: click the AssemblyStation → spacebar → **MU Animation** tab → show path `default` → **Edit** and adjust values so the table top lies flat and legs do not touch the assembly boxes.

---

### 1.2 Always Fill-up the Main MU with Parts

Demonstrates filling a pallet (main MU) with as many parts as it can hold; the part type loaded does not matter.

#### Configure the Material Flow

- Duplicate `Part` twice → `PartRed` and `PartBlue` (assign colors). Duplicate the `Container`.
- `SourceMainParts` produces two container types sequentially (`ProductsTable`).
- `SourceMainParts` sends pallets along a Conveyor to the AssemblyStation.
- `SourceParts` produces two part types cyclically (`PartsTable`).
- `SourceParts` sends `PartBlue` → ParallelStation `BlueParts`, `PartRed` → ParallelStation `RedParts`.
- ParallelStation settings: clear **Start Processing When Full** (to fill with different part types); set processing time 10 s on **Times** tab.
- ParallelStations send processed parts to the AssemblyStation.

#### Configure the Assembly Table

- Select `Assembly Table > Fill-up Main MU`. No other changes.
- Note: although `Fill-up Main MU` appears as an Assembly Table option, the AssemblyStation does **not** use an Assembly Table here — it accepts parts from any predecessor until the main MU (Container) capacity is reached.

Result: pallets are always filled with four parts (all red, all blue, or mixed).

> **Compare** `Fill-up Main MU` with `Assembly Table > MU Types` in Example model `AssemblyStation > Change Assembly List` (parts moved per Assembly Table + Entrance Control `setBOM`; never fills to capacity).

---

### 1.3 Assemble Parts Sequentially

Demonstrates sequential assembly with the AssemblyStation using `Assembly Table > Depends on Main MU`.

#### Configure the Material Flow

- `SourceBoxA` produces `BoxA`, `SourceBoxB` produces `BoxB` (both in folder `UserObjects`).
- Conveyor transporting boxes to the AssemblyStation: 4 m long, default settings.
- Conveyor from AssemblyStation to Drain: default settings.
- `SourcePartA` produces `PartA`, `SourcePartB` produces `PartB`.
- `Conveyor2` (PartA) and `Conveyor3` (PartB): **MU Distance** = 2 m, select **Enforce MU Distance**.

#### Configure the Assembly Table

Select `Depends on Main MU` → **Open**. Enter Assembly Time and Sequence Number:

| Amount | Part  | Into  | Assembly Time | Sequence Number |
|--------|-------|-------|---------------|-----------------|
| 1      | PartA | BoxA  | 5 min         | 1               |
| 2      | PartB | BoxA  | 10 min        | 2               |
| 1      | PartB | BoxB  | 3 min         | 1               |
| 2      | PartA | BoxB  | 6 min         | 2               |

Use the **Event Debugger** to follow assembly step-by-step.

---

### 1.4 Assemble Parts Sequentially with the Worker

A **Worker** carries parts from a Store to the AssemblyStation and places them on a pallet in a defined sequence, using `Assembly Table > Depends on Main MU`.

#### Configure the AssemblyStation

- `SourceContainer` produces 4 pallets.
- Conveyor transports pallets to the AssemblyStation: **MU Distance** = 0.5, **Enforce MU Distance**.
- Worker picks parts up at the Workplace attached to the Store, steps onto the Workplace attached to the AssemblyStation, and places parts on the pallet.
- AssemblyStation: `Assembly Table > Depends on Main MU` → **Open**, type the assembly sequence into **Sequence Number** (e.g. red → red → green → yellow).
- Workplace (attached to AssemblyStation): default settings.
- Conveyor to Drain and Drain: default settings.

#### Configure the Store

- X Dimension = 3, Y Dimension = 4, Z Dimension = 1.
- Activate **Transport Importer**; Worker waits for a free target.
- Configure the Workplace attached to the Store.

#### Watch the Assembly

1. Sources produce four red, green, and yellow parts.
2. Worker steps onto the Store's Workplace, picks up a red part, turns around, walks to the AssemblyStation's Workplace, places it on the pallet.
3. Worker walks back and repeats in the sequence entered into the Assembly Table.

Use the **Event Debugger** to follow step-by-step.

---

### 1.5 Set How Workers Deliver Mounting Parts

Controls whether Workers deliver mounting parts in parallel or sequentially:

- **Clear** `Workers Sequentially Deliver MUs to Assemble` → several Workers deliver one part each in parallel.
- **Select** `Workers Sequentially Deliver MUs to Assemble` → a single Worker delivers parts one after another.

#### Make Several Workers Deliver Parts in Parallel

- `SourcePallets` produces pallets (main parts) carried by `WorkerMainParts`.
- `SourceParts` produces mounting parts carried by `WorkerOtherParts` (four Workers of this class).
- Attach a Workplace to `SourceParts`, `SourcePallets`, and the AssemblyStation.
- Configure the **WorkerPool** and `WorkerOtherParts`.

Result: `WorkerMainPart` carries the pallet to the AssemblyStation; meanwhile four `WorkerOtherParts` Workers each pick up a part and place it onto the pallet.

**A Single Worker Delivers Part After Part:** select `Workers Sequentially Deliver MUs to Assemble` → Worker `WorkerOtherParts:1` delivers four parts one after the other, then returns to the WorkerPool.

#### Make a Single Worker Deliver Several Parts at Once

- `SourcePallets` produces pallets moved automatically onto the AssemblyStation.
- `SourceParts` produces mounting parts carried by the Worker.
- Attach a Workplace to `SourceParts` and the AssemblyStation.
- Configure the **WorkerPool**.
- Increase the Worker's X-Dimension and Y-Dimension to `2` each so he can carry four parts.

Result: the Worker walks to `SourceParts`, waits until four parts are produced, picks them up one by one, carries them to the AssemblyStation's Workplace, and places them one by one.

---

## 2. Removing Parts with the Dismantle Station

The **DismantleStation** removes mounting parts from a main part. Insert it from **Material Flow** in the Class Library or Toolbox.

The sample removes parts from a car in a junk yard. Steps:

- Configure the Source where the cars enter the junk yard.
- Configure the DismantleStation that removes the parts.
- Configure the station that tests the parts.
- Configure the station that distributes the removed parts.

### 2.1 Configure the Source

- `Source CarsIn` produces `Car` parts, moved on a Conveyor to the DismantleStation.
- DismantleStation removes trunk lid, outside mirrors, and wheels; sends the stripped car to the scrap press; removed parts go to `TestParts`.
- Source settings: adjustable interval, uniform distribution (`Car` part). Inter-arrival time uniformly distributed between 29 and 35 minutes.
- Activate **Captions** (object → spacebar → Captions tab → `Name/label activated`) to identify objects. Toggle all captions with the **Names** button on the View ribbon tab.

### 2.2 Configure the DismantleStation

- **Sequence** → `Main MU after other MUs` (first moves mounting parts, then the stripped car).
- **Dismantle Table** entries:
  - 4 wheels → successor 2
  - 2 mirrors → successor 2
  - 1 trunkLid → successor 2
- Assign different materials (colors) to `wheel`, `mirror`, `trunk lid`: right-click object in Class Library → **Open in 3D** → click `Default` graphic → spacebar → **Material** tab → `Material active` + color (wheel blue, mirror red, trunk lid green).
- **Dismantle Mode** → default `Create MUs` (creates a new part for each successor).
- **Successor** for the main MU (stripped car) → default `1`.
- Main MU movement → default `Main MU`.
- **Processing Time** → 30 minutes (Times tab).
- Draw an icon of the car without removed parts (icon number 1), and create an Entrance Control for the Conveyor to switch to that icon once the car moves onto it:

```simtalk
@.CurrIconNo := 1
```

### 2.3 Configure the Station That Tests the Parts

- Station `TestParts` checks whether parts can be resold or scrapped.
- **Exit Strategy** → `Percentage`.
- **Open List** entries:
  - 10 % → successor 1 (bad → scrap press)
  - 90 % → successor 2 (good → sold)

### 2.4 Configure the Station That Distributes the Removed Parts

- **FlowControl** moves parts to type-specific Drains based on a part attribute.
- **Exit Strategy** → `MU Attribute`.
- **Open List** (Attribute List) using the attribute `Name` (entered once in the Attribute column, left empty for the remaining two parts):
  - `Name` = `Wheel` → successor 1
  - `Mirror` → successor 2
  - `TrunkLid` → successor 3

Run the simulation to see the DismantleStation strip the car; the stripped car goes to the scrap press, removed parts go to the test station (bad → scrap press, good → distributed to Drains). Press **F6** for the Statistics Report.
