# Source — General

This document summarizes the Plant Simulation Help content for the **Source** material flow object, located in the `general` folder. It covers the object's purpose, dialog-box tabs, attributes, MU selection, and SimTalk attributes/methods. Code examples are preserved inline.

---

## Side [SimTalk]

Sets the side of the Frame on which the Interface designated by `<Path>` is located.

- **Type:** Attribute
- **Syntax:** `<Path>.Side:string`
- **Assignment value:** data type `string`; possible values are `"Top"`, `"Right"`, `"Bottom"`, `"Left"`, or `"Angle-dependent"`.
- `"Angle-dependent"` takes the angle between the objects into account when determining the start or end point of the Connector.

```simtalk
interface.Side := "right"
```

**See also:** Side [drop-down list]

---

## Source (object)

Use the **Source** object to produce the parts that move through your model. It usually represents the receiving department of your plant or the main machine producing the parts.

### Description

- The Source has a **capacity of one** and **no processing time**.
- It produces the same or different types of MUs one after the other or in a mixed sequence.
- You can set a procedure to determine **the times at which it creates the parts** and a procedure to determine **the types of MUs to be produced**.
- As an active material flow object, the Source attempts to move the MUs it produces to the objects to which it is connected.
- You can define how the Source proceeds when it cannot move an MU to its succeeding object by selecting or clearing **Blocking**.
- Use the **Drain** to remove parts from the factory (e.g. the shipping department).
- Hover over the Source to show a tooltip; click **Show Manipulators** on the Edit ribbon tab (or press `M`) to change the graphic length and anchor points.

**Add the object:** Home ribbon tab → `Manage Class Library > Basic Objects > MaterialFlow > Source`.

---

## Dialog Box of the Source

Double-click the Source icon to open its dialog box.

- **Edit Simulation Properties:** change simulation properties; shared properties are described under *Dialog Items of the Objects*.
- **Edit Animation Properties:** click the **Edit 3D Properties** button in the lower-left corner, or select the object and press the **spacebar**.
- Press `M` (or click **Show Manipulators**) to manipulate the graphic.

---

## Tab Attributes

The **Tab Attributes** provides the settings that the object offers.

### Operating Mode [check box]

Sets how the Source proceeds if it cannot create the MUs at the Time of Creation you entered.

- **Select Blocking** — the Source remembers the time at which it was supposed to produce the next MU, and produces the following MUs at the next possible point in time (when the MU that was blocked by the successor was moved on). The Source stops creating parts when the simulation time reaches the Stop time.
- **Clear Blocking** — the Source creates another MU exclusively at the time of creation you entered.

> When the Source is temporarily not operational (failed, paused, or blocked), the times of creation may shift if you select **Blocking**; then the creation-time settings cannot be realized.

**See also:** Blocking [SimTalk], Time of Creation [Source]

### Time of Creation [Source]

Selects the point in time at which and how the Source produces MUs.

Available settings:

- **Interval Adjustable** — produces the first MU at the **Start** time; **Interval** designates the time between two creation events; produces the last MU at the **Stop** time.
  - Without a Stop time, Plant Simulation produces the amount of parts entered at most; default value `-1` = unlimited parts.
  - With a Stop time, the Source produces parts until the Stop time is reached and ignores the **Amount**.
  - A constant time produces all MUs at that point in time.
- **Number Adjustable** — produces the number of MUs typed in as **Amount**. If **Generate as Batch** is active, **Amount** designates the number of batches, not parts. Creation times are distributed according to the **Interval** distribution.
- **Delivery Table** — produces MUs according to the **Delivery Time**, **Class**, **Number**, **Name**, and **Attribute** in the Delivery Table.
  - If you assign a new Delivery Table during the simulation, it also produces parts that were to be produced in the past.
- **Trigger** — produces MUs according to values that a set of **Trigger** objects control.

Depending on the setting, the attribute `Path` (dialog item MU or Table) sets the path to the MU class, delivery list, sequence table, frequency table, or percentage table.

**SimTalk:** TimeOfGeneration [SimTalk]

### Interval Adjustable [time of creation]

Produces MUs according to the point in time defined by **Interval**, **Start**, and **Stop**.

- **Start** — point in time at which the first MU is produced.
- **Interval** — time span between two creation events.
- **Stop** — point in time at which the last MU is produced (enter `0` to produce according to **Amount**).
- You can select a **Probability Distribution** for Interval, Start, and Stop.

**Amount** — the amount of MUs the Source produces (only for *Number Adjustable* and *Interval Adjustable*).

> For *Interval Adjustable* without a Stop time, Plant Simulation produces the amount at most (`-1` = unlimited). With a Stop time, the Amount is ignored. With **Generate as Batch** active, the Source may create more parts than the Amount (batches are always produced in their entirety). For *Number Adjustable* with **Generate as Batch**, the value designates batches/lots, not MUs.

**SimTalk:** Number [SimTalk], TimeOfGeneration [SimTalk]

### Number Adjustable [time of creation]

Produces the number of MUs typed into **Amount**.

- With **Generate as Batch** active, Amount designates batches, not parts.
- Select a **Probability Distribution** from **Creation Times**; the distribution determines the creation time.
- The number of MUs is produced at the times generated by the random number generator at the start of the simulation; times are bounded if you enter lower/upper bounds.
- A **Constant** time creates all MUs at one point in time.

> For *Number Adjustable* you cannot select MU Selection > Sequence. To set Creation Times via SimTalk, use the attribute `Interval`.

**SimTalk:** Number [SimTalk], TimeOfGeneration [SimTalk]

### Delivery Table [time of creation]

Produces MUs according to the **Delivery Table** settings.

- Type the path of the Delivery Table into **Table**, or click and select a table in *Select Object*.
- The Delivery Table has five columns with data types `time`, `object`, `integer`, `string`, and `table` (instead of `time` you can also use `date`, `dateTime`, or `real`). Each row defines one production order:
  - **Delivery Time** — time at which the MUs are produced (must increase row by row; a past time creates the part immediately).
  - **MU** — class of the MU (drag-and-drop supported).
  - **Number** — number of MUs (enter `0` to take the interval into account for the next cycle but produce no part).
  - **Name** — name of the MUs (required: Delivery Time and MU; missing Number = single MU; missing Name = class name inherited).
  - **Attributes** — table/user-defined attributes set on produced MUs.

**Attribute details:** type the attribute name in column 1 of the attribute table; if it does not exist, Plant Simulation creates it. The data type of the column containing the value is assigned to the attribute. If the column data type is `table`/`list`/`stack`/`queue`, Plant Simulation creates a **reference** to the list rather than copying sublists (changing one changes the other).

> The Source does not produce parts whose creation time is in the future when you assign a Delivery Table during the simulation. Instead of a DataTable in a Frame, you can use a user-defined attribute of data type `table` of the Source as the Delivery Table.

**SimTalk:** Path [SimTalk] - Source, creationTable [SimTalk] - Source, TimeOfGeneration [SimTalk]

### Trigger [time of creation]

Produces MUs according to values that one or several **Trigger** objects control.

- Click **Trigger** and type the Trigger object name(s). Each Trigger sends orders as strings.
- Open the Trigger → tab **Values** → Trigger Type **Input** → click **Values**, then type orders on the tab **Contents**:
  - Left cells: **Point in Time** at which the Source creates MUs.
  - Right cells: **Value** of the order — a string with this format: *amount of MUs, MU type, distribution type, and distribution parameters*:

```simtalk
(<num>, <mu_Type>, <distributionType[, distribution parameters]>)
```

- You must always type the amount, the MU type, and the distribution type.
- With `Const` as distribution type, the Source produces MUs at the point in time in the **Point in Time** column (optionally with an offset in seconds).
- For other distributions, enter the distribution parameters; the distribution values set the **time offset** (must be positive) to the time in the **Point in Time** column.

**Example:** creation time computed as `1:00.000 + z_negexp(…, 20, 0, 60)` and `5:00.000 + z_normal(…, 20, 5)` respectively. The random stream used is the Source's internal stream.

If the Source is entered as a resource in the **ShiftCalendar**, Plant Simulation interrupts the production sequence during weekends:
- With **Blocking** selected, the Source does not produce MUs during the weekends.
- With Blocking cleared, the Source produces and moves MUs as soon as its shift starts again.

Useful for setting a creation time (like a delivery table) that periodically repeats (e.g. MU Selection > Sequence Cyclical).

**SimTalk:** Trigger [SimTalk], creationTable [SimTalk] - Source, TimeOfGeneration [SimTalk]

### Interval [Source]

For *Interval Adjustable*, the time span between two creation events (Source creates an infinite number of MUs). Select a distribution or `Const`.

**SimTalk:** Interval [SimTalk] - Source

### Start [Source]

The point in time at which the Source produces the first MU. Select a distribution or a constant time (`Const`).

**SimTalk:** Start [SimTalk] - Source

### Stop [Source]

The time at which the Source stops producing MUs. Select a distribution or a constant time (`Const`).

**SimTalk:** Stop [SimTalk] - Source

### MU Selection [drop-down list]

Selects which type of MUs and how the Source produces MUs. Settings:

- **Constant** — one type of MU only (path in text box **MU**).
- **Sequence Cyclical** — MUs in a fixed sequence from a table; repeats periodically after the sequence is processed.
- **Sequence** — MUs according to a sequence table; processes the sequence **only once**.
- **Random** — MUs in random frequencies according to a frequency table.
- **Percentage** — MUs in percentages according to a percentage table.
- **Order Controlled** — MUs only if ordered by a Store with **Supermarket** active or with the method `orderParts`.

Depending on the Time of Creation, the dialog item MU or Table (attribute `Path`) sets the path to the MU class, delivery list, sequence table, frequency table, or percentage table.

> To use a **copy** of the DataTable instead of a reference, assign the name `.unshare` to the subtable.

**SimTalk:** MUSelection [SimTalk], Path [SimTalk] - Source, unshare [SimTalk]

**See also:** Store as Supermarket [check box], Configuration [button], getCurrentOrderTableRow [SimTalk]

#### Constant [MU selection]

Produces one type of MU. Type the path to the MU next to **MU**, click to select a MU class (Part, Container, Transporter), or drag-and-drop from the Toolbox/Class Library.

**SimTalk:** MUSelection [SimTalk], Path [SimTalk] - Source

#### Sequence Cyclical [MU selection]

Produces parts according to a sequence table (path entered for **MU Selection > Sequence Cyclical**).

- You can preallocate user-defined attributes; a `table`-typed attribute is stored as a **reference** (memory/performance gain). To force a copy, assign `.unshare` to the subtable.
- Select **Generate as Batch** to produce the **Number** of MUs in the table in a single lot (all at once at the given start time).
- Clear the check box to produce MUs as a sequence of individual parts.
- After processing the entire sequence, it starts again from the beginning (cyclical).

**SimTalk:** MUSelection [SimTalk], Path [SimTalk] - Source, GenerateAsBatch [SimTalk], getCurrentOrderTableRow [SimTalk], unshare [SimTalk]

#### Sequence [MU selection]

Produces MUs according to a sequence table (path entered for **MU Selection > Sequence**).

- Processes the sequence **only once** (not repeatedly).
- **Not available** if Time of Generation is *Number Adjustable*.
- Same attribute-reference/`.unshare` and **Generate as Batch** behavior as Sequence Cyclical.

**SimTalk:** MUSelection [SimTalk], Path [SimTalk] - Source, GenerateAsBatch [SimTalk], getCurrentOrderTableRow [SimTalk], unshare [SimTalk]

#### Random [MU selection]

Produces MUs according to a frequency table (path entered for **MU Selection > Random**).

- Same attribute-reference/`.unshare` behavior.
- The frequency table has five columns with data types `object`, `real`, `integer`, `string`, and `table`. Each row is a production order:
  - **MU** — MU class.
  - **Frequency** — frequency of the production order.
  - **Number** — number of MUs to be produced.
  - **Name** — (optional) name of the MUs.
  - **Attributes** — (optional) attribute subtable of the produced MUs.
- Select **Generate as Batch** to produce the Number of MUs in a single lot. With *Number Adjustable* as the time of creation, the amount designates batches, not parts.
- To check which part types were produced at which time, activate **Creation Table** on the tab **Statistics**.

**SimTalk:** MUSelection [SimTalk], Path [SimTalk] - Source, GenerateAsBatch [SimTalk], getCurrentOrderTableRow [SimTalk], unshare [SimTalk]

#### Percentage [MU selection]

Produces MUs according to a percentage table (path entered for **MU Selection > Percentage**).

- Same attribute-reference/`.unshare` behavior.
- The percentage table columns: **MU** (name/path), **Portion** (percentage), **Number** (amount), and optional **Name** and **Attributes**.
- Select **Generate as Batch** to produce the Number of MUs in a single lot. With *Number Adjustable*, the amount designates batches, not parts.
- **Percentage** is a deterministic process: when selecting the next part, the Source goes to the row with the greatest need in the **Portion** column, creating periodically repeating patterns.

**SimTalk:** MUSelection [SimTalk], CreationTableActive [SimTalk], GenerateAsBatch [SimTalk], getCurrentOrderTableRow [SimTalk], unshare [SimTalk]

#### Order Controlled [MU selection]

Only produces MUs if ordered by a Store with **Supermarket** active or with the method `orderParts`.

- Automatic routing of the produced part delivers it to the ordering station (auto-enabled if deactivated).
- The Source produces MUs according to **Interval Adjustable** and the **Interval** between creation times.

**SimTalk:** MUSelection [SimTalk], orderParts [SimTalk] - Source

**See also:** Store as Supermarket [check box], Configuration [button], View > Show Orders [Source]

### Generate as Batch [check box]

Makes the Source produce the **Number** of MUs (from the table) in a single lot — all at once at the given start time, moving them onto the next object in a single lot instead of one by one.

- Applies for MU Selection > Sequence, Sequence Cyclical, Random, and Percentage.
- With *Number Adjustable* as the Time of Creation, **Amount** designates the number of batches, not parts.

**SimTalk:** GenerateAsBatch [SimTalk], CurrentBatchNumber [SimTalk]

---

## Tab Failures

Define failures as described under the **Tab Failures**.

## Tab Controls

Provides controls to modify the built-in behavior of the object.

- **Select the path to an existing Method:** click the ellipsis button and navigate in *Select Object [for controls]*.
- **Create a control that is a Method of the object:** type a meaningful name and select **Create Control [context menu]**, which inserts `self.Name_you_typed_in_for_the_control` (e.g. `self.A1Ctrl`). On an empty text box it inserts `self.OnBuilt_in_name_of_the_control` (e.g. `self.OnEntrance`).

```simtalk
self.A1Ctrl
self.OnEntrance
```

- Edit source code later with `F2`, `Shift`+double-click, **Open Object** on the context menu, or via the tab **User-defined**.
- To delete the control, delete the user-defined attribute (deleting only the name from the text box retains the attribute).

**See also:** Select Object [for controls], Entrance Control [general description], Exit Control [general description], Shift Calendar [tab Controls]

## Tab Exit

Select to which of its successors the object moves the MU. **See also:** Blocking [exit strategy], Strategy [material flow objects]

## Tab Statistics [Source]

In addition to the standard Tab Statistics values, provides the dialog items **Creation Table** and **Open**. To view Resource Statistics, select View > Show Statistics Report, right-click the Frame and select **Show Statistics Report**, or press `F6`.

### Creation Table [Source]

Check box to write all events for which the Source produced MUs during a simulation run into a table. Click **Open** to view it. The Source records creation events in addition to the resource statistics.

**SimTalk:** CreationTableActive [SimTalk], creationTable [SimTalk] - Source

### Open [creation table]

Opens the creation table (if **Creation Table** is selected). Each row lists a production event:

- **Name** — name of the MU class.
- **Path** — path of the MU class, the name of the MU, and its number.
- **Time of Generation** — time at which the Source created the individual MU.

**SimTalk:** creationTable [SimTalk] - Source

## Tab User-defined

Define your own attributes as described under the **Tab User-defined**.

---

## Menus

### Navigate Menu

Commands are described under the **Navigate Menu**.

### View Menu

Provides commands to access its functions:

- Refresh [on View menu], Forward Blocking List
- Show Statistics Report [on View menu], Exit Blocking List
- Show Attributes and Methods [on View menu], Associated Lockout Zones
- Show Orders [Source], Associated Shift Calendar
- Contents [material flow objects]

#### Show Orders [Source]

Opens a table showing the orders pending with the Source: the **Name** of the ordered part, its **Amount**, and the **Target** (the object that orders the parts).

**See also:** MU selection > Order Controlled, Supermarket [check box], Configuration [button]

### Tools Menu

Commands are described under the **Tools Menu**.

### Help Menu

Commands are described under the **Help Menu**.

---

## Methods of the Source

The Source provides:

- The methods listed in the table of contents (left).
- The **Methods of the Material Flow Objects**.
- The **Methods of All Objects**.

To view all methods, read-only attributes, and attributes: open **Show Attributes and Methods** (context menu of the Class Library, or press `F8` / click **Show Attributes and Methods** on the Home ribbon tab of the Frame).

---

## Key SimTalk Attributes & Methods Referenced

- `Side` (`<Path>.Side:string`)
- `Blocking`
- `TimeOfGeneration`
- `Number`
- `Interval`, `Start`, `Stop`
- `Path`
- `MUSelection`
- `GenerateAsBatch`, `CurrentBatchNumber`
- `CreationTableActive`, `creationTable`
- `orderParts`
- `getCurrentOrderTableRow`
- `unshare`
