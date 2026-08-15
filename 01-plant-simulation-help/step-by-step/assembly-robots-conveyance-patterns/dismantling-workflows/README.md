# Assembling & Dismantling Workflows

This directory documents Plant Simulation help topics for two material-flow stations:

- **AssemblyStation** — adds (mounts) parts to a main part.
- **DismantleStation** — removes parts from a main part.

> Source: `dismantling-workflows.md`. Both stations are inserted from the **MaterialFlow** folder in the Class Library, or the **Material Flow** toolbar in the Toolbox. Sample models can be opened via *Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples*.

---

## 1. Assembling with the AssemblyStation

The **AssemblyStation** attaches mounting parts (e.g. doors to a car body, legs to a table top) to a main MU. Depending on the **Assembly Table**, it either moves the mounting parts onto the main MU or deletes them.

### Example workflows

| Example | What it demonstrates | Key configuration |
|---------|----------------------|-------------------|
| **Assemble Kitchen Tables** | Attach table legs to two types of table tops | `Assembly Table > Predecessors` (predecessor number + part count), `Assembly Mode = Attach MUs`, correct predecessor wiring for the Main MU |
| **Always Fill-up the Main MU** | Fill a pallet with as many parts as it holds (type irrelevant) | `Assembly Table > Fill-up Main MU`; no Assembly Table used — accepts parts until the Container capacity is reached |
| **Assemble Parts Sequentially** | Sequence-based assembly | `Assembly Table > Depends on Main MU` (part, into-part, assembly time, sequence number) |
| **Assemble Parts Sequentially with the Worker** | A Worker carries parts from a Store and assembles them in sequence | `Assembly Table > Depends on Main MU`, Store with Transport Importer + Workplaces |
| **Set How Workers Deliver Mounting Parts** | Parallel vs. sequential delivery | `Workers Sequentially Deliver MUs to Assemble` (cleared = parallel, selected = sequential); Worker dimensions to carry multiple parts |

### Key notes

- Check predecessor connection order if assembly does not work — the Main MU must arrive from the correct predecessor (the Connector tooltip shows its number).
- 3D graphics and colors are set via the Class Library → **Open in 3D**, and part names are mapped to graphic groups using user-defined attributes and observers (`OnPictureName3DChanged`).
- The **Event Debugger** helps follow assembly step-by-step.

---

## 2. Removing parts with the DismantleStation

The **DismantleStation** removes mounting parts from a main part. The sample strips parts from a car in a junk yard, then tests and distributes the removed parts.

### Configuration steps

1. **Source** — `CarsIn` produces `Car` parts (uniform inter-arrival time, 29–35 min) onto a Conveyor.
2. **DismantleStation**
   - `Sequence = Main MU after other MUs` (moves mounting parts first, then the stripped car).
   - **Dismantle Table**: 4 wheels, 2 mirrors, 1 trunk lid → successor 2.
   - `Dismantle Mode = Create MUs`, Main MU successor = 1, processing time = 30 min.
   - Entrance Control on the Conveyor switches the car icon: `@.CurrIconNo := 1`.
3. **TestParts station** — `Exit Strategy = Percentage` (10 % bad → scrap press, 90 % good → sold).
4. **FlowControl** — `Exit Strategy = MU Attribute` on the `Name` attribute routes `Wheel`, `Mirror`, `TrunkLid` to their own Drains.

### Result

The DismantleStation strips the car; the stripped car goes to the scrap press, and the removed parts go to the test station (bad → scrap press, good → distributed to Drains). Press **F6** for the Statistics Report.
