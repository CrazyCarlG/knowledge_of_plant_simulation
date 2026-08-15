# Charts, Reports & Visual Analytics

Summary of the Plant Simulation Step-by-Step Help chapter on viewing and visualizing statistics.

## Viewing and Visualizing Statistics

By default, all material flow objects collect statistics values from the beginning to the end of a simulation run. To disable collection, clear the check box **Resource Statistics** (tab *Statistics*) or **Product Statistics** (tab *Product Statistics*). Material flow objects also provide **Energy Statistics** values.

The **EventController** controls when statistics collection starts and is reset:
- On the tab *Settings*, the text box **Statistics** sets the time at which the EventController resets statistics and deletes all previously collected values (see *Statistics Collection Period*). This lets you discard warm-up-phase data that might distort results.
- Clicking **Reset Simulation** deletes statistics data of all objects and resets values to 0. During a run, the method `initStat` achieves the same effect.

## View Statistics in the Dialogs of the Objects

Material flow objects show their most important statistics on the tab **Statistics**. The pre-selected resource type is:

- **Production** — Station, ParallelStation, AssemblyStation, DismantleStation.
- **Transport** — PlaceBuffer, Buffer, Sorter, Track, TwoLaneTrack, Conveyor, Transporter, Container.
- **Storage** — Store.

The resource type affects statistics of mobile objects.

> The percentages for Working, Setting-Up, Waiting, Blocked, Powering up/down, Failed, Stopped, Paused, and Unplanned should add up to 100 percent.

> Plant Simulation does not dynamically update the values during a run while the dialog is open. Select **Refresh** in the View menu or press **F5**.

### Statistics Table

| Item | Description |
|------|-------------|
| Working | Portion of the collection period the object was working. |
| Setting-up | Portion the object was setting-up. |
| Waiting | Portion the object was waiting. |
| Blocked | Portion the object was blocked. |
| Powering up/down | Portion the object was powering up/down. |
| Failed | Portion the object was failed. |
| Stopped | Portion the object was stopped by a LockoutZone. |
| Paused | Portion the object was paused. |
| Unplanned | Portion the object was unplanned (not scheduled to work). |
| Relative Occupation | Capacity-based portion of the occupied time (not paused/failed) relative to available time. |
| Relatively Empty | Portion the object was empty in relation to available time. |
| Contents | Number of MUs currently on the object. |
| Minimum Contents | Minimum number of MUs on the object. |
| Maximum Contents | Maximum number of MUs on the object. |
| Entries | Number of MUs that entered (a Container counts as 1, not its contents). |
| Exits | Number of MUs that exited (a Container counts as 1, not its contents). |
| Average Dwell Time | Average time of all parts that stayed on the station (excluding paused/unplanned time). |

Click **Show Statistics Report** on the Home ribbon tab to view the collected values. Most values can be queried with the methods listed next to each value.

### Energy Statistics

Click the energy icon to open a dialog of its own:

| Item | Description |
|------|-------------|
| Total Consumption | Sum of total energy consumption. |
| Working | Portion of total consumption while working. |
| Setting-up | Portion while setting-up. |
| Operational | Portion while operational. |
| Failed | Portion while failed. |
| Standby | Portion while on standby. |
| Off | Portion while off. |

> The energy states differ from the resource states with the same name: resource states refer to the statistics collection period, energy states refer to the total energy consumption.

To view Energy Statistics in the Statistics Report, select the object in the Frame and press **F6**.

### Check How Many Parts Were Introduced into the Plant

The **Source** can record which MUs it created and when:
- Select **Creation table** on the tab *Statistics*.
- Click **Open** to view the creation table. Columns: **Name** (MU class name), **Path** (path, name, number), **Time of Generation**.

### Check How Many Parts Left the Plant

The **Drain** can record type-dependent (product) statistics for MUs with the same name. Select **Type Dependent Statistics**.

| Item | Description |
|------|-------------|
| Working / Setting-up / Waiting / Stopped / Failed / Paused | Percentage of MU times spent on objects in each state relative to the MUs' collection periods (generally their life time). |
| Average Lifespan | Average lifespan of MUs created and removed during the period (only MUs with active product statistics). |
| Average Exit Interval | Average interval between exits; counting starts only when the first MU arrived. |
| Total Throughput | Number of MUs removed since Type dependent statistics was activated. |
| Throughput per Hour | Average MUs removed per hour. |
| Throughput per Day | Average MUs removed per day. |

### Check Statistics of the Individual Stations

All material flow objects show the standard statistics. The **AssemblyStation** and **DismantleStation** show additional values: **Waiting for parts** (mounting parts) and **Waiting for resources**. The table *Waiting Times* shows the sum of waiting times of MUs per predecessor.

### Check the Contents List of the Stations

You can open the Contents List via **View > Contents** in the object dialog:
- Point-oriented objects with capacity 1 show the current part's path.
- Point-oriented objects with capacity > 1 show all parts.
- **ParallelStation** shows parts positioned per their x-y coordinates.
- Length-oriented objects (**Conveyor**, **Track**, **TwoLaneTrack**, **Transporter**) show **Object**, **From**, and **To** columns (position in the selected length unit).

The internal Contents List is deleted when the model is reset, so save it if needed. Write the array returned by `contentsList` into a table with `copyToTable`:

```simtalk
// Copies the contents lists into the table MyContentsList
// as an array with the method copyToTable
var x,y : real; var row : integer
MyContentsList.delete
var a : any := Buffer.contentsList
MyContentsList[1,1] := "Buffer"
a.copyToTable(MyContentsList,2,1)
row := MyContentsList.yDim + 2 // inserts an empty line
MyContentsList[1,row] := "Conveyor"
print a // prints the contents list as an array to the console
print "Number of items: ",a.yDim
var b := Conveyor.contentsList // local variable is of data type any
print b
print "Number of items: ",b.yDim
b.copyToTable(MyContentsList, 2,row)
MyContentsList.openDialog
```

Legacy style for writing the contentsList into a table:

```simtalk
// Writes the contentsList into a table
// as previous versions of Plant Simulation did
Buffer.contentsList(ContentsListBuffer)
Conveyor.contentsList(ContentsListConveyor)
```

To delete the saved list in a reset method:

```simtalk
MyContentsList.delete
```

To print the contents list to the Console as an array:

```simtalk
print Buffer.contentsList
print Conveyor.contentsList
```

### Check Product Statistics of Parts

All MUs (Part, Container, Transporter) show the percentage of time spent waiting or working on a resource of type Production, Transport, or Storage on the tab **Product Statistics**. Use **Home > Show Statistics Report** for all product statistics. Container and Transporter also provide resource statistics because they can load and transport parts.

### Check Statistics of Exporter and Worker

For the **Exporter** and **Worker**, the tab *Statistics* shows service and exporter values (each block sums to 100 percent). Selecting **Fail Services** (tab *Attributes*) makes the Exporter also collect failure times of its services. The Exporter only collects failed times during processing/set-up time; waiting times only accumulate while available.

Key values: Services Setting-up / Processing / Repairing / Waiting / Failed; Exporter Operational / Paused / Unplanned / Failed; Free Capacity; Mediated Capacity; Free/Mediated Capacity (sum); Minimum/Maximum Free Capacity; Minimum/Maximum Mediated Capacity (shown as `-1` until a valid value exists).

### Viewing the Statistics Report

Select several objects (Shift+click or marquee) and press **F6** to open the Statistics Report. The report adds selected objects to a drop-down list. Main topics show resource statistics split by state (working, waiting, set-up, blocked, powering up/down, failed, stopped, paused, unplanned — summing to 100%).

State bar colors:

| Color | State |
|-------|-------|
| green | Working |
| brown | Setting-Up |
| gray | Waiting |
| yellow | Blocked |
| purple | Powering up/down |
| red | Failed |
| pink | Stopped |
| blue | Paused |
| light blue | Unplanned |

- Hover over a column header to see the read-only attribute name.
- **Save** exports as HTML or text; **Refresh** updates; **Print** prints the report.

## Show Statistics in a Chart

Insert the **Chart** from the folder *UserInterface* in the Class Library or the *User Interface* toolbar. It displays data from a table or from input channels that record attribute values dynamically.

Drag-and-drop sources:
- Material flow object / Portioner / DePortioner → shows statistics.
- PlaceBuffer / Buffer / Store → frequency distribution of the number of MUs.
- DataTable / TimeSequence / MaterialsTable → table contents.
- Variable → variable value.

Click **Apply** to apply settings, **Show Chart** to display, double-click to open the dialog. For Histogram/Plotter select **Collect data** to record during the run. **Tools > Reset Values** deletes collected values.

### Statistics Wizard

Right-click the Chart and select **Statistics Wizard**:
- Select object class(es) (only objects with **Resource Statistics** enabled are added).
- Select **Resource type** (Production, Transport, Storage).
- Select **Include Subframes** to include objects in inserted Frames.
- Select **Sort Criterion** (Name or a state).
- Click **OK** to open the display window.

### Select Where the Data Comes From

**Data Source**:
- **Input Channels** — click **Data Table** to define channels (paths to attributes, read-only attributes, methods, or complex expressions). Type legend text into the row index.
- **Data Table** — show table contents as a diagram. Enter name/path and **Range**, e.g.:
  - `{*,*}..{*,*}` — all cells.
  - `{1,1}..{1,4}` — first four cells of column one.
  - `{1,1}..{1,*}` — all cells in column one.
  - `{-2,*}..{-2,*}` — one but last column.
  - `{-2,*}..{*,*}` — last two columns.

**Update mode**:
- **Sample** — updates periodically after **Interval**.
- **Watch** — updates when a watchable read-only attribute (e.g., `NumMU`, `StatNumIn`) or watchable attribute (e.g., `Pause`, `Speed`) changes. The **Watchable** column in *Show Attributes and Methods* lists what can be watched.
- **Plot** — updates on every simulation event.

### Select How the Chart Shows the Data

Categories (tab *Display* → *Category*): **Chart**, **3D Chart**, **Histogram**, **3D Histogram**, **Plotter** (value progression over time), **XY Graph** (only with *Data Source > Data Table*).

### Chart Types

Available depending on category:

| Chart Type | Description |
|------------|-------------|
| Columns | Each record as a column, side by side. |
| Stacked Columns | Columns stacked vertically (positive up, negative down). |
| 100% Stacked Columns | Stacked columns showing percentage of 100%. |
| Bars | Horizontal bars side by side. |
| Stacked Bars | Horizontal bars stacked (positive right, negative left). |
| 100% Stacked Bars | Stacked bars showing percentage of 100%. |
| Area | Areas stacked one behind the other. |
| Stacked Area | Areas stacked on top of each other. |
| 100% Stacked Area | Areas showing percentage of 100%. |
| Line | Each record as a line. |
| Line with Markers | Line with markers. |
| Spline / Spline with Markers | Curves (with or without markers). |
| Markers | Set of markers. |
| Points and Best Fit Conveyor | Data points with best-fit straight line (least squares). |
| Points and Best Fit Curve | Data points with best-fit curved line. |
| Pie | Slices of a pie (negative prefix offsets a slice). |
| XY Points | x-y pairs as data points (first record = x-coordinates). |
| Line (XY) | x-y pairs connected by a line. |
| Sticks | Vertical bar per x-y pair from the zero line. |
| Area (XY) | Connected x-y points with filled area. |
| 3D Columns / 3D Wire Frame / 3D Surface | Records in 3D space; rotate via Rotation angle or sliders, set Height. |

### Additional Display Options

- Show records as **Graph**, **Table**, or **Graph and Table**.
- **3D Effect**: None, Shadow, 3D, Gradient Bars, Contoured (for 3D Columns/Surface); set Rotation angle and Height.
- **Color** tab: change Background and Desk colors.
- **Display in Frame** (tab *Display*) to show the Chart in the Frame instead of its icon.
- **Gap When Null** to interrupt lines for undefined values.
- **Tools > Print** and **Tools > Copy to Clipboard**.
- Grid lines: **X-axis** (set max number of grid lines) and **Y-axis** on tab *Axes*.
- y-axis **Range**: left/right text boxes; default `0 … 0` scales automatically. Enter a blank in **Subtitle** if the upper y-range is cut off.

### Labels and Legend

Enter **Title**, **Subtitle**, x-axis text, y-axis text, and choose the legend side. Fonts on tab *Font*; text color on tab *Color*. Legend text is entered in the row index of the input channel table.

### Annotations

Click **Annotations** and fill in the table. Columns: **Type**, **Value**, **From**, **To**, **Color**, **Style**, **Text**.

Types: `0` Vertical Line, `1` Horizontal Line, `2` X-axis Label, `3` Y-axis Label, `4` Text.

- **Value** — line position (Y value for horizontal/Y-axis; X value for vertical/X-axis).
- **From / To** — line start/end (can create diagonal lines). Empty means edge-to-edge.
- **Style** — line style or marker style.

Line / marker style values (partial list):

| Value | Line style | Marker style |
|-------|-----------|--------------|
| 0 | thin solid line | text only, no marker |
| 1 | dashed line | plus sign |
| 2 | dotted line | cross |
| 3 | dash-dot line | circle |
| 4 | dash-dot-dot line | filled circle |
| 5 | medium thin solid line | square |
| 6 | thick solid line | filled square |
| 7 | grid tick | diamond |
| 8 | grid line | filled diamond |
| 9–12 | none / medium / extra thick solid | triangles (up/down, hollow/solid) |
| 13–36 | none | small/large plus, cross, circle, square, diamond, triangles |
| 92–99 | none | arrows (N, NE, E, SE, S, SW, W, NW) |

Text prefix positions:

| Prefix | Position |
|--------|----------|
| `|l` | left inside edge of the graph |
| `|L` | left outside edge of the graph |
| `|r` | right inside edge of the graph |
| `|R` | right outside edge of the graph |
| `|c` | centered inside of the graph |

## Show Statistics and Other Values in a Report (HtmlReport)

Use **HtmlReport** (folder *UserInterface*) to present all simulation results as an HTML page, which you can print, save, or share. Configure it on the tab **Content** using a simple bracket-based syntax. You can also select an object, click the toolbar button, and set parameters in the **Object Parameters** dialog.

Example content:

```text
[!self, logo, *]                      // show icon 'logo', zoom with report
# General Information                  // level-1 heading
Below we provide:
1. An **overview** of the model        // numbered list; **bold**
1. Various **statistics tables**
1. A **resource chart**
## Model Overview                     // level-2 heading
Below we provide this information about the simulation model:
* Model file: [=modelFile]           // formula (function)
* Simulation root: [EventController.Location]
* Simulation time: [EventController.SimTime]
* End time: [EventController.EndTime]
## Simulation Model
The simulation model looks like this:
><**[current, "Test Simulation"]**     // centered screenshot, caption "Test Simulation"
# Statistics Tables
These **statistics values** are of general interest. Feel free to add more.
## Drain Statistics
Drain statistics shows the contents of the *summary report* table.
[.MaterialFlow.Drain*]                // DataTable contents
## Deliveries
Deliveries shows the contents of the table object *DeliveryList.*
[DeliveryList]
# Resource Chart
The *resource chart* for the *Stations* look like this. Feel free to add more.
## Stations
The utilization of the processing *Stations* is as follows:
><[StationChart, 150, 100]           // centered screenshot, width 150, height 100
---                                   // solid horizontal line
> Cedar Rapids, [=day(sysdate)].[=month(sysdate)].[=year(sysdate)+1900]
Best regards,
<span style="font-family: Segoe Script; font-size:16pt">H. Thompson</span>
```

Key syntax rules:
- `[ObjectName]` — address an object.
- `[!self, iconName, *]` — show an icon (asterisk = zoom with report).
- `#` / `##` — heading levels 1 and 2.
- `1.` — numbered list; `*` — bulleted list; `**text**` — bold.
- `[=function]` — formula (function name).
- `[Object.Attribute]` — attribute value.
- `><[current, "caption"]` or `><[Chart, width, height]` — centered screenshot; `><` centers it.
- `[TableName]` or `[.Path.To.Object*]` — show table/DataTable contents.
- `---` — horizontal line.
- HTML tags (e.g., `<span>`, `<a href>`) are supported.

## Show Reports in a Hierarchically Structured Model

For a complex model, insert an **HtmlReport** named `ReportObject` into each sub-Frame. The name `ReportObject` is special: Plant Simulation uses it when the Frame is referenced in brackets.

In the overall HtmlReport (`.Models.MyCarAssembly.HtmlReport`):

```text
# Production Areas
The car assembly encompasses three production areas:
* CarBody
* PaintShop
* FinalAssembly
[CarBody, #]        // Show the HtmlReport of the Frame 'CarBody' instead of the Frame itself
[PaintShop, #]      // Show the HtmlReport of the Frame 'PaintShop' instead of the Frame itself
[FinalAssembly, #]  // Show the HtmlReport of the Frame 'FinalAssembly' instead of the Frame itself
```

The `#` argument renders the sub-Frame's `ReportObject` one heading level lower.

### Building the Model

- **Create classes** (Glass Box Frames) in *UserObjects* for cells/lines (e.g., `CarBodyCell`, `PaintShop`, `AssemblyLine`), and duplicate the **Comment** object as a custom class `ToDo` so Plant Simulation gathers all `ToDo` instances into the report.
- **Model the Car Body Cell** — Interface/Entrance, two AssemblyStations with Buffers between, Interface/Exit, three Sources (`CarBody`, `Trunk`, `Roof`), an HtmlReport (`ReportObject`), and a Chart histogram (`BufferOccupancy`). Configure normally distributed processing times, failures, energy settings, Buffer capacity (4), and histogram input channels (drag the two Buffers onto the Chart).
- **Model the Paint Line** — Interface/Entrance, Conveyors `Preparing` (6 m), `Painting` (8 m), `Drying` (6 m), Interface/Exit, and an HtmlReport.
- **Model the Assembly Line** — Interface/Entrance, four Conveyors (5 m, 5 m, 5 m, 4 m), three Stations (`Step1`, `Step2`, `Step3`) each with an attached Workplace, an HtmlReport, and a `ToDo` Comment. Configure failures and processing importer with `~.Broker`.
- **Model the Installation** — Source (`Receiving`) with `Mu Selection > Sequence Cyclical` using a `PartsTable`; three Frames (`CarBody`, `PaintShop`, `FinalAssembly`) converted from Glass-Box to Black-Box Frames; configure Receiving, Body Assembly, Paint Shop, Final Assembly, and the overall HtmlReport.

ReportObject example for the Car Body Cell:

```text
# [current.name]               // name of the Frame as heading on the first level
The above car body cell looks like this: // descriptive text
## Layout                      // second level heading
><[current, *]                 // centered screenshot, adjusted to maximum window width
## Buffer Occupancy            // second level heading
The occupancy of the individual Buffers looks like this: // descriptive text
><[BufferOccupancy, 150, 100]  // centered screenshot, size 150 mm x 100 mm
[Buffer]                       // show statistics values of the object 'Buffer' as a table
[Buffer1]                      // show statistics values of the object 'Buffer1' as a table
## Statistics                  // second level heading
Statistics of the AssemblyStations and the Buffers looks like this: // descriptive text
[AssemblyStation, "Assembly statistics"]    // table with caption "Assembly statistics"
[AssemblyStation1]
[AssemblyStation2]
[Buffer, "Buffer statistics ", %MatFlowProperties]  // show material flow properties
[Buffer1]
```

ReportObject example for the Paint Line:

```text
# [current.name]
The above paint line of the car assembly looks like this:
## Layout
><[current, *]
## Statistics
Statistics of our paint lines look like this:
><[Painting, "Flow statistics", %MatFlowProperties]
[Preparing]
[Drying]
```

ReportObject example for the Assembly Line:

```text
# [current.name]               // name of the Frame as first level heading
The above assembly line of the car assembly looks like this:    // descriptive text
## Layout                      // second level heading
><[current, *]                 // centered screenshot, adjusted to maximum width
## Statistics                  // second level heading
Statistics of the stations Step1, Step2, and Step3              // descriptive text
[Step1, "Station statistics"]  // table with caption "Station statistics"
[Step2]
[Step3]
```

ReportObject example for the Body Assembly:

```text
# [current.name]
The car body section of our car assembly looks like this:
## Layout
><[current, *]
## CarBodyCells
The car body section encompasses several CarBodyCells:
[CarBodyCell.Origin*, ##]  // shows the heading two levels lower
[EnergyAnalyzer, #]        // shows the heading one level lower
```

ReportObject example for the Paint Shop:

```text
# [current.name]
The PaintShop section of the car assembly looks like this:
## Layout
><[current, *]
## PaintLines
The PaintShop encompasses several PaintLines.
[PaintLine.Origin*, ##]
```

ReportObject example for the Final Assembly:

```text
# [current.name]
The final assembly section of the car assembly looks like this:
## Layout
><[current, *]
## Broker Statistics
The Broker collected these statistics values:
[Broker]
## Worker Chart
The worker chart shows statistics of all Workers that are staying in the WorkerPool.
[WorkerChart]
## Assembly Lines
The final assembly section encompasses several assembly lines.
[AssemblyLine.Origin*, ##]
```

Overall HtmlReport for the car assembly plant:

```text
><[!self, Header, *]
# General Information
## Overview
* Model file: [=modelFile]
* Simulation root: [self.location]
* Simulation time: [EventController.simtime]
* End time: [EventController.EndTime]
* Generated on: [=sysdate]
* Contact: <a href="mailto:John.Doe@siemens.com?subject=Simulation report">John.Doe@siemens.com</a>
## Model
The car assembly model looks like this:
><[current, *]
## Receiving
The receiving section delivers these parts:
><[PartsTable, 1..3]
--
# Statistics
Drain statistics data suffices for our purposes.
## Drain Statistics
Drain statistics shows detailed information about the parts that the shipping section removed from the plant.
[.MaterialFlow.Drain*]
--
# Production Areas
The car assembly encompasses three production areas:
* CarBody
* PaintShop
* FinalAssembly
[CarBody, #]
[PaintShop, #]
[FinalAssembly, #]
--
# ToDo
These tasks still have to be completed:
[.UserObjects.ToDo*]
Cedar Rapids, [=day(sysdate)].[=month(sysdate)].[=year(sysdate)+1900]
<span style="font-family: Segoe Script; font-size:32pt">>H. Thompson</a>
```

### Run and Show the Report

- Set the EventController end time (e.g., `1:00:00:00` for one day), run the simulation, then right-click the HtmlReport and select **Show**.
- To auto-show after the simulation ends, add a user-defined `endSim` method on the HtmlReport:

```simtalk
self.~.show
```

> When the 3D model contains many objects, showing the HtmlReport can take time because the scene must be rendered before screenshots are taken.

### Study the HtmlReport

The table of contents shows four heading levels by default; set the attribute **TOCLevels** to show fewer. You can display Production Areas (using `[Frame, #]` to insert sub-reports), the Energy Analysis (via `[EnergyAnalyzer, #]`), and the ToDos (`[.UserObjects.ToDo*]`). Clicking a ToDo link opens its Comment object; use **Navigate > Open Location** to jump to the Frame.

## Show Values During the Simulation with the Display

Use the **Display** (folder *UserInterface*) to show an attribute, method, or Variable value throughout a run (e.g., Buffer fill level).

### Select Which Data the Display Shows

- Enter the path and name of the object, then the value after the path, e.g. `buffer.numMU`, `.Models.Model.ParallelStation.statNumOut`, `store.XDim`. Supported data types: boolean, integer, real, string, object, time, money, length, weight, speed, date, datetime. An invalid path turns the text box background red.
- Optionally enter a **Comment** (shown below the value).
- **Update mode**:
  - **Sample** — updates periodically after **Interval**.
  - **Watch** — updates when a watchable value changes (e.g., `NumMU`, `StatNumIn`, `Pause`, `Speed`).

### Select How the Display Shows the Data

- **Text**, **Bar**, or **Pie** (Bar/Pie only for numerical values).
  - Bar/Pie show the value relative to **Minimum**/**Maximum**; empty = below lower bound, full = above upper bound. Resize with Shift+Ctrl+drag. Actual min/max shown as dashed lines; view exact values on tab *Data*; **Reset Values** resets to 0.
  - Text mode lets you select font size for the value and Comment.
- **Transparent** makes the background transparent.
- Select text/outline **Color**.

## Accessing Statistics with SimTalk

Most statistics values are accessible via methods, read-only attributes, and attributes. The read-only attribute names are listed next to each value in the Statistics Report descriptions (material flow objects, Drain, Exporter/Worker, MUs, Transporter driving statistics). See also *Read-Only Attributes for Accessing Statistics*, *Attributes for Statistics*, *Methods for Accessing Statistics of the MUs*, and *_Attributes of All MUs*.

## Show Part Flows in a SankeyDiagram

The **SankeyDiagram** (folder *User Interface*) visualizes how parts or Workers move from object to object. It shows the flows after the simulation run.

- Model a Source, Station `Roughing`, Station `FineMachining`, and Drain.
- Configure the carrying operation with a **Broker** (default), **WorkerPool** (Travel Mode > *Walk along footpaths*, *Get Job Orders at Home Only*), **Workplaces** attached to each station (clear *Worker Stays Here After Completing the Job*), and **FootPaths** between Workplaces and WorkerPool (connected with Connectors).
- Configure a SankeyDiagram for the Worker (turn off inheritance on tab *Objects* and drag the Worker class onto it) and one for the Parts (only changed flow color).
- Run the simulation and right-click a SankeyDiagram → **Show** to view flows. Use **Hide** to hide them.

For a Worker walking freely within an area (clear *Get Job Orders at Home Only*, Travel Mode > *Move freely within area*), the SankeyDiagram shows the free-flowing paths.

## Show AGV Flows in a SankeyDiagram

The SankeyDiagram also visualizes how AGVs drive from Marker to Marker.

- Duplicate the **AGVPool**, **Marker**, and **Transporter**; rename the Transporter to `AGV` in *UserObjects*.
- Insert the AGVPool and Markers at chosen positions.
- Program an `init` method to set the routes:

```simtalk
var agv1: object := AGVPool.getIdleAGV
agv1.setRoute([M03, M04, M05, M06, M07, M10])
wait 10
var agv2: object := AGVPool.getIdleAGV
agv2.setRoute([M01, M04, M05, M06, M07, M08])
```

- Drag the AGVPool onto the SankeyDiagram. Run the simulation and click **Show Diagram**. Routes appear as blue bars; thicker bars indicate the shared part of the route.

## Show Parts on Resources in a GanttChart

The **GanttChart** (folder *UserInterface*) shows how parts move from resource to resource (here "resources" means material flow objects).

- Configure a **Source** that produces different parts per a **Delivery Table** (tab *Attributes*).
- Configure a **ParallelStation** (X-Dimension 2, Y-Dimension 1), set processing times in `MyProcessingTimes` (tab *Times*), and add failures (tab *Failures*). Clear **Start Processing When Full** or the model may not run.
- Configure the GanttChart: activate **Collect Data**; the part `Part` is pre-configured; add more parts by dragging them from the Class Library onto the tab *Parts*. Add resources by dragging them onto the tab *Resources* (leave empty to watch all resources).
- Run the simulation and click **Show Chart** (or right-click → **Show**).

The GanttChart provides two views (tab *Attributes* or context menu):

- **Resource view** — resources along the vertical axis, time along the horizontal axis.
- **Part view** — parts along the vertical axis, time along the horizontal axis.

> Resources/parts are shown in the order they were first processed; this order cannot be changed. With default settings, a part is shown on all resources in the same color (Resource view), and a resource is shown for all parts in the same color (Part view).
