# Sources, Routing, and Transfer Logic

This document summarizes the Plant Simulation Help section on **Modeling the Flow of Materials — Basics**, covering how to create parts with the Source, process them with stations, route them from station to station, and remove them with the Drain.

---

## 1. Modeling the Flow of Materials, Basics

Plant Simulation offers several modeling techniques. The basics of modeling material flow cover:

- How to create or introduce parts into the model with the object **Source**.
- How to select and enter how long a **station** processes the parts that move onto it.
- How to set a station up to process another type of part.
- How to transfer parts from processing station to processing station.
- How to model failures and failure times of the processing stations.
- How to remove the processed parts from the model with the object **Drain**.

---

## 2. Active and Passive Objects

Mobile and stationary material flow objects are the basic building blocks of a simulation model.

### Mobile material flow objects (MUs)
- **Part**, **Container**, and **Transporter** represent the physical or logical parts moving through the installation.
- These mobile objects (MUs) require active and passive material flow objects to process and transport them.

### Sources and drains
- The **Source** creates mobile objects at the beginning of the material flow.
- The **Drain** removes MUs from the plant after they have been processed.
- The **FluidSource** creates fluids at the beginning of the fluid flow.
- The **FluidDrain** removes fluids from the plant after fluid objects have processed them.

### Active material flow objects
The active material flow objects **Drain, Station, ParallelStation, AssemblyStation, DismantleStation, Conveyor, Sorter, PlaceBuffer, and Buffer** receive MUs, process them for a certain time, and then attempt to actively transfer them to the next object along material flow connections (symbolized by the **Connector**) using the **push-block principle**.

They represent work stations in a factory (lathe, drilling station, etc.). They differ in:
- The number of MUs they can process at the same time (single or several).
- The way they process them (in series or in parallel).

The **Conveyor** transports MUs at a given speed over a given distance.

### Active fluid objects
**FluidDrain, Tank, Mixer, Portioner, and DePortioner** receive fluids, process them for a certain time, then actively transfer them to the next object using the push-block principle.

### Passive material flow objects
**Store, Track, and TwoLaneTrack** do not automatically transfer MUs:
- A MU remains in the **Store** until removed (for example by a Method).
- The **Track** and **TwoLaneTrack** are used with the **Transporter**, which drives along them at the speed you set.
- Model diverging and converging strategies with the **FlowControl**.

### Passive fluid objects
**Pipe** and **PatchMatrix** transport fluids to their successor in the flow of materials.

### Active vs. passive MUs
- **Active MUs** move by themselves — the **Transporter** (self-propelled) and the **Worker** (a human).
- **Passive MUs** are transported and processed — the **Part** (any workpiece) and the **Container** (any receptacle, such as a storage bin or pallet).

### Point-oriented vs. length-oriented objects
- **Point-oriented objects**: MUs are located on a fixed processing place. For **Source, Drain, Station, ParallelStation, AssemblyStation, DismantleStation, Sorter, PlaceBuffer, Buffer, FluidSource, FluidDrain, Tank, Mixer, ContinuousMixer, Portioner, DePortioner, and PatchMatrix**, their own length/dimension and the MUs' length/dimension are irrelevant to the simulation.
- **Length-oriented objects**: their own length/dimension and the MUs' length/dimension are used during simulation. These are **Conveyor, Track, TwoLaneTrack, FootPath, Pipe, Container, and Transporter**.
  - **Turntable**: a single straight segment.
  - **Turnplate**: a straight segment setting the diameter.
  - **AngularConverter**: two straight segments.
  - **Converter**: a single straight segment.
  - Length-oriented objects are called **extrusion objects** in 3D.

---

## 3. Producing Parts with the Source

The **Source** creates the MUs handled by the material flow objects. It can represent a receiving department or a machine producing parts. The **Drain** removes parts (e.g., models the shipping department).

Insert the Source from the folder **MaterialFlow** in the Class Library, or from the toolbar **Material Flow** in the Toolbox.

### 3.1 Select How the Source Proceeds When It Cannot Produce MUs

Use the **Operating Mode > Blocking** setting to control behavior when the Source cannot create MUs at the entered creation time (because it fails, is paused, or is blocked):

- **Select Blocking** — the Source remembers when it was supposed to produce the next MU but could not, and produces it at the next possible point in time (once the blocking MU has moved on).
- **Clear Blocking** — the Source creates another MU exclusively at the time of creation you entered.

> **Note:** With **Blocking** selected, creation times may shift when the Source is Failed, Paused, or Blocked, so the settings for times of creation may not be realized exactly.

### 3.2 Produce Parts According to a Delivery Table

For most installations, use a **Delivery Table** containing the parts a machine produces or that are delivered. Delivery tables usually come as Excel (`*.xls`) files, which you open in a Plant Simulation table and save.

To produce MUs according to time, type, and number from a Delivery Table:
- Select **Time of Creation > Delivery Table**.
- Click the button and select the delivery table in the **Select Object** dialog, or drag the table over the **Table** text box and drop it there.
- Click **OK**.

The Delivery Table has **five columns** and may contain attribute values in addition to name and number:

| Column | Purpose |
| --- | --- |
| **Delivery Time** | The time at which the Source produces the MUs. |
| **MU** | The class of the MU (drag-and-drop of the MU class also works). |
| **Number** | The number of MUs to be produced. |
| **Name** | A name for the produced MUs. |
| **Attributes** | Optional name of a subtable with attributes to set/create. |

Rules:
- `Delivery Time` and `MU` are required.
- If no `Number` is entered, the Source produces a single MU.
- If no `Name` is entered, MUs use the name of their class.
- Typing `0` as `Number` still takes the interval for the next cycle into account — the row is not skipped, but no part is produced during that cycle.
- For `Delivery Time`, instead of the data type `time` you can use `date`, `dateTime`, or `real`. With `date`/`dateTime`, the simulation start time must be before the entered time.

To open the attributes subtable: double-click the cell, click into the cell and press **F2**, or right-click and select **Open Object**. Enter the built-in or user-defined attribute name in column 1 and the value in the matching data-type cell to the right. Plant Simulation assigns the data type of the value column to the attribute.

### 3.3 Produce Parts During an Interval You Define

- Select **Time of Creation > Interval Adjustable**.
- The Source:
  - Produces the first MU at the time entered for **Start**.
  - Produces the next MU after the **Interval** has elapsed.
  - Stops producing at **Stop**. Enter `0` for no time limit.

With **Interval Adjustable** or **Number Adjustable**, you can select which types of MUs are produced via **MU Selection**.

#### 3.3.1 Produce a Single Part Type Only
- Select **MU Selection > Constant**.
- Click the button and select the MU class in the **Select Object** dialog.

#### 3.3.2 Produce Parts in a Fixed Sequence Over and Over Again
- Select **MU Selection > Sequence Cyclical**.
- Insert a table into a Frame or a folder in the Class Library.
- Designate the table (via the button, drag-and-drop, or typing the name/path).
- Enter MU class names below **MU**, and the number to produce below **Number** (columns 3 and 4 for Name/Attributes are optional).
- **Generate as Batch**: select this to produce the number of MUs in a row all at once as a single batch before moving the whole batch on. When cleared, MUs are produced as a sequence of individuals.
- Once the Source has processed the entire sequence, it restarts from the beginning.

#### 3.3.3 Produce Parts in a Fixed Sequence One Time Only
- Select **MU Selection > Sequence** (note: **Sequence** is not available when **Time of Generation** is **Number Adjustable**).
- Same table setup as above; the sequence is processed one time only.

#### 3.3.4 Produce Parts With a Random Frequency Entered into a Data Table
- Select **MU Selection > Random**.
- Enter MU class names below **MU** and frequency numbers below **Frequency**.
- Plant Simulation selects and processes a random generation order according to the entered frequency.
- Optionally activate the **Creation table** checkbox on the **Statistics** tab to check which part types were produced at which time.

#### 3.3.5 Produce Parts With a Percentage Entered into a Data Table
- Select **MU Selection > Percentage**.
- Enter MU class names below **MU**, percentage portions below **Portion**, and the number of parts below **Number**.

### 3.4 Produce the Number of Parts You Need

- Select **Time of Creation > Number Adjustable**.
- Enter the **Amount** (number of MUs to create).
- Select the **Creation Times** distribution from the drop-down list and enter the values the distribution requires.

The Source produces the number of MUs at times generated by the random number generator at the start of the simulation (bounded if you enter a lower/upper bound). A **Constant** time creates all MUs at one point in time.

> **Note:** With SimTalk, use the attribute `Interval` to set Creation Times.
> **Note:** For **Number Adjustable** you cannot select **MU Selection > Sequence**.

### 3.5 Produce Parts Using a Trigger Object

A **Trigger** can control a Source (for example, to combine a delivery-table-like time of creation with a periodically repeated sequence).

Procedure:
- Select **Time of Creation > Trigger** in the Source dialog.
- Enable the **Inheritance** checkbox.
- Click **Trigger**, and drag the Trigger controlling the Source from the Frame into the list.
- In the Trigger dialog, enter the **Active Interval** (the interval during which the Trigger is active) and the **Period Length** (the Trigger's cycle duration).
- On the **Values** tab, select **Trigger Type > Input**.
- Click **Values** and enter into the **TimeSequence** object:
  - The point in time the Source creates MUs into the left-hand cells.
  - The sequence of values into the right-hand cells.

The order is a string with this format:

```
amount,mu_Type,distributionType[,distribution parameters]
```

> **Note:** The string may not contain blank spaces. You must enter the amount, the type, and at least a constant value. `Const` alone produces the MUs at the time typed in the left cell; a number after `Const` is an offset in seconds. A distribution sets the time offset to the time in the corresponding left cell (the offset must be positive).

- On the **Actions** tab, click **Objects** — the Trigger shows the Source in the table.

---

## 4. Produce and Process Parts with a Work Plan

A **work plan** (operations plan) determines how a product is produced, listing production steps in execution sequence. In Plant Simulation, cost centers and allowed times per step are handled in **Process Designer**, not here.

In the example, each operation is executed by a single station, so the work plan is a sequence of stations:

| Position | Station |
| --- | --- |
| 0 | Receiving (Source) |
| 1 | Milling |
| 2 | Drilling_A or Drilling_B |
| 3 | Packing |

The modeling approach:
- Create the work plan in a **DataTable** inserted into the Frame, with set-up times and processing times in sub-tables.
- Produce two part types with a **Source** using a sequence table. Parts need two user-defined attributes: part name and position in the work plan.
- Program a **Method** as an **Exit Control** that finds the next station after each processing step and moves the part on.

### 4.1 Create the Processing Stations

- Right-click **Station** in the **MaterialFlow** folder and select **Derive**.
- Move the derived station to the model folder (hold **Shift** and drag), rename it (e.g., `MyStation`). Plant Simulation places derived objects in `UserObjects` by default.
- Insert it three times and rename instances (e.g., `Milling`, `Drilling_A`, `Drilling_B`, `Packing`).
- Set shared features in the class, which passes properties on to its instances.

### 4.2 Define Times in the Class of the Processing Stations

The Processing Time and Set-up Time are defined via formulas referencing the work plan `MyWorkPlan` (in the root Frame).

**Processing Time** uses a Method called from the formula (`ProcessingTimeInFormula`):

```simtalk
-> time
var PartType := @.EntityType
var Station  := ?
var WorkPlan := root.myWorkPlan["Operations", PartType]
result       := WorkPlan["Processing time",Station]
```

**Set-up Time** uses a formula typed directly into the text box. `Self` identifies the station contained in the row of the subtable:

```simtalk
root.MyWorkPlan["Operations",@.EntityType]["Setup time",Self]
```

### 4.3 Define Set-up Behavior in the Class

To automatically set the stations up depending on a user-defined attribute of the MU:
- Select the **Automatic** checkbox.
- Select **User-defined Attribute** from **Set-up depends on**, and enter the attribute name (e.g., `EntityType`) defined in the Sequence table.

### 4.4 Specify the Name of the Exit Control

Enter the name of the **Exit Control** that finds the next station and moves the part on (see 4.6).

### 4.5 Create the Work Plan

- Insert a **DataTable** into the Frame. Activate the column index and row index.
- Assign the data type `Table` to the column containing the operations subtable.
- Format the column so all subtables share the same format (right-click the column header **Operations** > **Format**; on the **Contents** tab, activate column/row index of the subtables).
- Assign data type `Object` to the column-index column and `Time` to the next two columns.
- Enter an identifier in the cell (e.g., `Operations` for `MyPart A` / `MyPart B`) to create the subtable; double-click the cell to open it and enter operation/station names, set-up times, and processing times.

### 4.6 Produce the Parts with a Source Using a Sequence Table

- Insert a **Source** and select **MU Selection > Sequence Cyclical**.
- Insert a **DataTable** and drag it over the **Table** text box (Plant Simulation assigns correct data types/headers).
- Enter the part type, number, name, and attributes subtable name. In the example, the Source produces 1 part each named `MyPartA` and `MyPartB`.
- Create a subtable for user-defined attributes (enter an identifier below **Attributes**, then double-click). Define:
  - `PartType` = `MyPartA` or `MyPartB` (name of the part).
  - `PositionInWorkPlan` = the position in the work plan (starts at 0 = Source; Milling = 1, Drilling_A/B = 2, Packing = 3).
- Enter the name of the Exit Control.

### 4.7 Program the Exit Control

All stations and the Source access this source code to find the next station and move the part on:

```simtalk
// This is the exit control for all stations and for the source.
// This control can be called several times until the move command is
// successful.
var WorkPlan := root.MyWorkPlan["Operations",@.EntityType]
if @.PositionInWorkPlan = WorkPlan.ydim
   @.Move(root.Shipping) // end of production
else
   var NextStation := WorkPlan["Operation", @.PositionInWorkPlan + 1]
   if @.Move(NextStation)
      @.PositionInWorkPlan := @.PositionInWorkPlan + 1
   end
end
```

---

## 5. Remove Parts from the Installation with the Drain

The **Drain** removes processed parts from the plant (e.g., the shipping department). It has a single processing place, and its built-in properties match those of the **Station**. After set-up and processing, the Drain removes the MU (instead of moving it to a successor) and collects statistics.

Insert the Drain from **MaterialFlow** in the Class Library or the **Material Flow** toolbar.

---

## 6. Transferring Parts from Station to Station

You can transfer parts between stations using:

- The **Standard Transfer Behavior** (push-block principle).
- An **Exit Strategy** that distributes parts to successors by criteria you set.
- The **FlowControl** to distribute parts among successors.
- An **observer** to move a part when a processing-station attribute changes.
- An **Exit Strategy in the Interface** when parts move across Frames.
- The **TransferStation** to load, unload, and reload parts.

### 6.1 How Plant Simulation Moves Parts On

Movement depends on the object types:

- **Point-oriented → point-oriented**: the MU moves completely and instantaneously from booking point to booking point.
- **Point-oriented → length-oriented** (e.g., Source/Station → Conveyor): the front of the MU moves to the start of the Conveyor. If not placed side by side, the MU appears to hang in thin air; placed side by side, it still seems located on the predecessor.
- **Length-oriented → length-oriented** (e.g., Conveyor → Conveyor): the MU moves continually — only its front moves on while the remainder follows at the specified **Speed**. When transport speeds differ, Plant Simulation uses the speed of the Conveyor where the **Booking Point Length** of the MU is located. A very long MU can be located on several Conveyors.
- **Length-oriented → point-oriented** (e.g., Conveyor → Station): the MU always moves completely and instantaneously onto the object as a whole.

### 6.2 Use the Standard Transfer Behavior

By default, Plant Simulation uses the **push-block principle** when transferring parts along Connector connections or via a Method:

- An object that has processed a part actively attempts to move it to its successor (**push**).
- If the successor cannot receive the part, the **block** principle guarantees the object is re-activated as soon as the successor is ready.
- This ensures parts are transferred using built-in functionality and that the event stream is not interrupted by failures or pauses.

The standard transfer strategy is **cyclic, non-blocking**: the current object moves the MU to the first non-blocked successor; when it reaches the end of the successor list, it wraps to the beginning and stops when it returns to the successor from the previous search.

**Example (push-block):**
- Milling is the first station, Drilling_A the second. Part:1 is on Drilling_A; Part:2 is on Milling and wants to move to Drilling_A.
- When Part:2 is fully processed, it notifies Drilling_A that it intends to move there.
- If Drilling_A can receive Part:2, it notifies Part:2, and Part:2 moves.
- If Drilling_A cannot receive Part:2 (busy, entrance locked, etc.), Part:2 enters itself into the **forward blocking list** of Drilling_A and of all other stations it intends to move to.
- When Part:1 exits Drilling_A, Drilling_A schedules an **Out** event for all MUs in its Forward Blocking List (including Part:2), then deletes all entries.
- If Drilling_A can then receive Part:2, Part:2 deletes all references to itself from all blocking lists and moves to Drilling_A.

The material flow objects **Station, ParallelStation, AssemblyStation, DismantleStation, Conveyor, Sorter, PlaceBuffer, and Buffer** handle MUs that transfer onto them using:

1. **Times you define:**
   - **Processing Time** — the time the MU remains on the object to be processed (between set-up and moving on).
   - **Set-up Time** — the time to set up the object for a different MU type (an identical name means same type; no set-up needed).
   - **Recovery Time** — the time to set a station into a defined state before processing the next part (e.g., a robot inserting/removing workpieces, or a hot part cooling off).
   - **Cycle Time** — the time between points where parts can enter (e.g., chain conveyors with a fixed chain interval).
   - *You do not have to define all of these times.*
2. **Failures** you define and activate.

The objects then transfer MUs using the **Exit Strategy** you select.

### 6.3 Selecting an Exit Strategy

On the **Exit** tab, select another **Strategy** when you don't want standard transfer behavior. Exit strategies distribute the material flow when the sequence of operations doesn't uniquely designate the next object (aiming for a near-optimal choice in cost/time, but not in all respects).

> **Note:** For length-oriented objects, the Exit Strategy is only considered when the part is moving forward.
> **Note:** Click **Apply** to display additional dialog items the strategy requires.

Available strategies:

| Strategy | Behavior |
| --- | --- |
| **Cyclic** | Move the part cyclically to the next successor in line. |
| **Cyclic Sequence** | Cyclically move to successors in the order you typed into the list (attribute: `ExitStrategySequence`). |
| **Least Recent Demand** | Move to the successor that has been waiting the longest for a MU. |
| **Linear Sequence** | Move to successors linearly, once, in the order you typed (attribute: `ExitStrategySequence`). |
| **Maximum Contents** | Move to the successor with the greatest number of MUs. |
| **Maximum Number In** | Move to the successor that received the most MUs. |
| **Maximum Processing Time** | Move to the successor with the longest processing time. |
| **Maximum Relative Occupation** | Move to the successor with the highest relative occupancy. |
| **Maximum Set-up Time** | Move to the successor with the longest set-up time. |
| **Minimum Contents** | Move to the successor with the smallest number of MUs. |
| **Minimum Number In** | Move to the successor that received the smallest number of MUs. |
| **Minimum Processing Time** | Move to the successor with the shortest processing time. |
| **Minimum Relative Occupation** | Move to the successor with the lowest relative occupancy. |
| **Minimum Set-up Time** | Move to the successor with the shortest set-up time. |
| **Most Recent Demand** | Move to the successor waiting the least time for a MU. |
| **MU Attribute** | Move to a successor according to an attribute of the MU (attribute: `ExitStrategyMUAttributeList`). |
| **Percentage** | Move to successors according to a percentage distribution (attribute: `ExitStrategyPercentageValues`). |
| **Random** | Move to successors in a random fashion. |
| **Start at Successor 1** | Always move to successor number 1. |

> **Note:** The strategies **Maximum/Minimum Contents, Number In, Processing Time, Relative Occupation, and Set-up Time** only work correctly when resource statistics of the successor or predecessor is active.

#### Strategy details

**Cyclic**
- **Blocking** selected: move to the object that immediately follows the object onto which a MU last transferred.
- **Blocking** cleared: move to the next object in the sequence that can receive a part. Search wraps to the beginning and stops at the previous successor.

**Cyclic Sequence**
- Click **Open List** and type successor numbers into the cells. Example: `2` in row 1 means the object first moves the MU to successor number 2.
- The successor is the next in line that can receive the MU. After the last entry, the list restarts. The same successor may appear multiple times consecutively.
- **Blocking** selected: only move when the designated successor is ready. **Blocking** cleared: attempt from the active entry onward, wrapping around.

**Linear Sequence**
- Click **Open List** and type successor numbers. Example: `3` in row 1 means move to successor number 3 first.
- The successor is the first in line that can receive the MU.
- **Blocking** selected: only move to the first successor in the list. **Blocking** cleared: move to the first available successor.

**Least Recent Demand** — the successor that has not received a part for the longest time receives the next MU.

**Most Recent Demand** — the successor that last received a MU receives the next MU.

**MU Attribute**
- Click **Apply** to display the strategy's items.
- **Blocking** selected: always move to the designated successor (block if it isn't ready).
- **Blocking** cleared: move on when any successor can receive it (enter successor numbers into the attribute list for each attribute value).
- Click **Open List** to enter attribute names, values, and successor numbers. The object searches the table top-to-bottom and moves to the first matching attribute's successor.
- Create user-defined attributes for the MUs on the **User-defined** tab.
- **Default Successor**: the successor used when the MU has no attribute with a matching value. Enter `0` to show a message instead. **Attribute Type**: select the attribute's data type.

**Percentage**
- Click **Open List** and type percentages. The n-th row defines the n-th successor's portion (e.g., `20` in row 1 → 20% to successor 1).
- The object always moves the MU to the successor with the greatest difference between rated and current value.
- **Blocking** selected: move to the successor with the highest deviation from the nominal percentage. **Blocking** cleared: move to the receiving successor with the highest deviation.
- Actual percentages may differ from nominal due to a low number of transfers and successor blocking. Prior transfers affect the strategy.
- Plant Simulation sums the values to obtain 100%; only relative sizes matter. Examples of generated sequences:
  - Values `1` and `2`: `2 1 2 2 1 2 2 1 2 2 1 2 2 1 2`
  - Values `2` and `3`: `2 1 2 1 2 2 1 2 1 2 2 1 2 1 2`
  - Values `1, 2, 4, 8`: `4 3 4 2 4 3 4 1 4 3 4 2 4 3 4 4 3 4 2 4 3 4 1 4 3 4 2 4 3 4`

**Random**
- Click **Open List** and type percentages (n-th row = n-th successor's portion).
- **Blocking** selected/cleared: determine the successor with the built-in random-number generator (cleared: iterate until a receiving successor is found or all successors are iterated through).
- A previous call to the random number generator affects the Random strategy; iteration order is not predictable.

**Start at Successor 1**
- **Blocking** selected: move to the first successor in the list. **Blocking** cleared: move to the first successor that can receive the MU.
- A previous search does not affect this strategy.

---

## 7. Distributing Parts with the FlowControl

The **FlowControl** models common strategies for splitting up and bringing together material flow. It does **not** store or process the MU — it only distributes them among its successors. The number of predecessors and successors is usually unlimited.

Insert the FlowControl from **Material Flow** in the Class Library or the **Material Flow** toolbar.

In the example, the FlowControl moves parts to successors according to a part attribute. If a part has more than one attribute, it suffices if one attribute meets the criteria in the attribute list. The **default successor** determines what happens when no attribute meets the criteria:

| Default Successor value | Behavior |
| --- | --- |
| `1` (or another successor number) | Move the part to that successor. |
| `0` | Do not move the part; it remains in front of the FlowControl, blocking following parts. |
| `-1` (or any negative) | Plant Simulation shows an error message. |

### 7.1 Configure the Source [FlowControl example]

- Select when and how many parts are produced (a **Delivery Table** in the example, named `MyDeliveryTable`).
- The Source (named `PartsIn`) produces six different parts with names in the **Name** column.
- To enter attributes for distribution, type a name in the **Attributes** column to create a subtable, then double-click it:
  - Part `Red`: attribute `Color` = `Red`.
  - Part `BlackSquare`: attribute `Color` = `Black`, `Shape` = `Square`.
  - Part `BlackOctagonal`: attribute `Color` = `Black`, `Shape` = `Octagonal`.

The Source creates these as user-defined attributes of data type `string`.

### 7.2 Configure the FlowControl

- Select **Strategy > MU Attribute**.
- Click **Open List** and type attribute names, values, and successor numbers. The FlowControl searches top-to-bottom and moves the part to the first matching attribute's successor.
- The **default successor** decides where parts with no matching attribute go. In the example, neither `Color` nor `Shape` of `BlackOctagonal` matches the criteria.
- Run the simulation to observe the default-successor behavior described above.

---

## 8. Loading, Unloading, and Reloading Parts with the TransferStation

The **TransferStation** defines custom part-transfer behavior. Insert it from **Tools** in the Class Library or the **Tools** toolbar.

> **Note:** The TransferStation is not shown by default in new models. The **PickAndPlace** robot can emulate most of its functions.

**Example scenario:** load a block of four parts onto a pallet → transport by conveyor → unload in blocks of two from pallets and reload onto a transport vehicle → unload in blocks of one onto a processing station → remove from the plant.

### 8.1 Load Parts with the TransferStation

Loading takes parts from the parts station and loads them onto a means of transport (**Container** or **Transporter**) located at the target station. The loading process starts as soon as part and means of transport are ready.

Steps:
- Insert the **Conveyor** that transports the parts.
- Insert a **Source** (e.g., `SourceParts`) that creates the parts.
- Insert a **ParallelStation** that processes parts before loading.
- Insert a **Source** (e.g., `SourcePallets`) that creates the pallets.
- Insert a **TransferStation** (e.g., `LoadingStation`) and configure it:
  - **Station type**: `Load`.
  - Click the button and select the **ParallelStation** as the source of the parts.
  - Click the button and select the **Conveyor** as the location of the means of transport.
  - On the **Attributes** tab, type the sensor position (e.g., `0` meters) where loading occurs — the LoadingStation inserts this sensor into the Conveyor automatically.
- On the **Advanced Attributes** tab, set how parts are loaded (e.g., blocks of 4).

> **Note:** Ensure the target station provides enough space for the incoming MU.

### 8.2 Reload Parts with the TransferStation

Reloading takes parts from a means of transport (Container/Transporter) at the parts station and places them onto a Container/Transporter at the target station. The reloading process starts as soon as both means of transport are ready.

Steps:
- Insert a **Source** (e.g., `SourceTransporters`) that creates the Transporters.
- Insert the **Track** on which the Transporter transports the loaded parts.
- Insert a **TransferStation** (e.g., `ReloadingStation`) and configure it:
  - **Station type**: `Reload`.
  - Drag the **Line/Conveyor** from the Frame into the text box (source of the parts to be reloaded).
  - Drag the **Track** into the text box (location of the means of transport).
  - Enter the sensor position (e.g., `22` meters) on the Line/Conveyor where parts are removed from pallets.
  - Enter the sensor position (e.g., `15` meters) on the Track where parts are loaded onto the Transporter.
- On the **Advanced Attributes** tab, set how parts are reloaded (e.g., blocks of 2).

### 8.3 Unload Parts with the TransferStation

Unloading takes parts from a Container/Transporter at the parts station and places them onto the target station. Unloading starts as soon as a means of transport is ready at the parts station.

Steps:
- Insert a **Station** onto which parts are unloaded.
- Insert a **Drain** that removes parts from the plant.
- Insert a **TransferStation** (e.g., `UnloadingStation`) and configure it:
  - **Station type**: `Unload`.
  - Drag the **Track** into the text box (source of the parts).
  - Drag the **Station** into the text box (location of the means of transport).
  - Enter the sensor position (e.g., `43` meters) on the Track where parts are unloaded.
- On the **Advanced Attributes** tab, set how parts are unloaded (e.g., blocks of 1).
- Insert a **Method**, enter `deleteMovables` as the source code, and name it `reset`.
- Insert an **EventController** into the Frame and run the simulation.

You can then change settings (Transporter/Container dimensions, block size, number of blocks, etc.) and observe the effects.
