# Chart

The **Chart** object presents current data and simulation run results. You insert a Chart into a Frame to visualize data.

Data to be plotted can be defined by:

- Using a **Table** containing the data (e.g. simulation results).
- Defining **Input Channels** that record values of attributes of interest of the objects.

A Chart inserted into a Frame provides the **Statistics Wizard** (open via the Frame's context menu command *Statistics Wizard*).

- Hover the mouse over the Chart to show a tooltip.
- Drag a **WorkerPool** over a Chart to show statistics of the Workers it manages.
- Click **Show Manipulators** on the Edit ribbon tab (or press `M`) to change the graphic length and anchor points.

**Add to model:** Home ribbon tab → *Manage Class Library > Basic Objects > UserInterface > Chart*.

---

## Statistics Wizard

A Chart inserted into a Frame shows the Statistics Wizard. Select *Statistics Wizard* on the Frame's context menu to open it.

- Select the class(es) of objects to show statistics for. The Chart only adds material flow objects for which the check box **Resource Statistics** is selected on the **Statistics** tab.
- Select **Inherit Settings** to inherit settings.
- **Class** group box: select object classes to show. You can select any number of classes.
- **Resource Type** (on an object's Statistics tab) restricts which objects are shown.
  - **Production** — default for Source, Drain, Station, ParallelStation, AssemblyStation, DismantleStation.
  - **Transport** — default for PlaceBuffer, Buffer, Sorter, Track, TwoLaneTrack, Conveyor, AngularConverter, Turntable, Transporter, Container.
  - **Storage** — default for Store.
- **Sort Criterion** drop-down:
  - *Name* — sort stations alphabetically (A–Z).
  - Drag stations onto the Chart in the desired order to sort manually.
  - Reorder later by cutting/pasting columns in the Input Channels table.
- **Statistics type**: Resource Statistics, Energy Statistics, or Occupancy.
- **Include Subframes** — also show objects contained in sub-Frames.
- **Reapply at Init** — reapply settings while the model is initialized.
- Click **OK** to display the Chart window.

Dragging a material flow object onto an unconfigured Chart requires selecting a statistics type (Resource or Occupancy; Energy if energy features are activated).

- **Resource** — shows object Name and states: Working, Setting-Up, Waiting, Blocked, Powering up/down, Failed, Stopped, Paused, Unplanned.
- **Energy** — shows energy states: Working, Setting-up, Operational, Failed, Standby, Off. (Energy-state values refer to total energy consumption, unlike resource states which refer to the statistics collection period.)
- **Occupancy** — shows object Name and the number of parts located on it; colored bars differentiate objects.

The diagram picture can also be shown in an **HtmlReport** (compare *Display a Chart*).

---

## Drag-and-Drop in the Chart

| To do this | Drag | To | Accelerator |
|---|---|---|---|
| Show statistics of a single material flow object | material flow object | Chart | `*` |
| Show statistics of multiple material flow objects | material flow objects | Chart | `*` |
| Show Driving statistics of the Transporter | Transporter | Chart | `*` |
| Show Services statistics of the Worker/Exporter | Worker/Exporter | Chart | `*` |
| Show Exporter statistics of the Worker/Exporter | Worker/Exporter | Chart | `Shift` |
| Show statistics of Workers controlled by a WorkerPool | WorkerPool | Chart | — |
| Show frequency distribution of the number of MUs | PlaceBuffer, Buffer or Store | Chart | `*` |
| Show frequency distribution for individual part types of Supermarket | Store configured as Supermarket | Chart | — |
| Show statistics of all resources assigned to the LockoutZone | LockoutZone | Chart | `*` |
| Show contents of a table | DataTable, TimeSequence | Chart | — |
| Show value of a Variable inserted into a Frame | Variable | Chart | `*` |
| Show statistics of a Frame with attribute `StatisticsObject` | User-defined object (Frame) | Chart | `*` |
| Show statistics of Workplace in a Frame with attribute `AOLType` | User-defined object (Frame) | Chart | `*` |

`*` Holding **Shift** while dropping deletes the existing entries from the input channels instead of adding the dropped object.

The method **`addObject`** accomplishes the same as the drag-and-drop actions above.

- To delete one displayed object: click **Data Table** next to Data Source and delete it.
- To delete the entire input channels table: hold **Shift** while drag-and-dropping a new object.
- To make a custom Frame behave like a built-in object when dropped, create a user-defined attribute of data type **object** named `StatisticsObject` (may designate any material flow object).
- To show statistics of several objects, assign data type **table** to `StatisticsObject`; the first column must be of type **string**.

---

## Dialog Box of the Chart

Double-click the Chart icon to open its dialog box.

- **Edit Simulation Properties** — shared properties are described under *Dialog Items of the Objects*.
- **Edit 3D Properties** — click *Edit 3D Properties* (lower-left of the simulation properties dialog), or select the object and press the spacebar.

---

## Show Chart button

Click this button to show the data the Chart collected in the display window.

- Double-click anywhere in the display window to open the Chart dialog.
- Right-click the Chart in the Frame and select **Show** to display data.
- Zoom by dragging a selection rectangle over an area of interest.

**Keyboard accelerators in the Chart window:**

| To do this | Key |
|---|---|
| Switch between monochrome and color viewing | `S` |
| Show the Export dialog | `X` |
| Maximize the window to full screen | `M` |
| Zoom all (show all data without scrollbar) | `Z` |
| Show the Text/Data export dialog | `D` |
| Show the Print dialog | `P` |
| Scroll vertical/horizontal scrollbars by one line | Arrow keys |
| Page vertical scrollbar | `PgUp`/`PgDown` |
| Page horizontal scrollbar right | `Shift+PgUp` |
| Page horizontal scrollbar left | `Shift+PgDown` |
| Move vertical scrollbar to first position | `Home` |
| Move vertical scrollbar to last position | `End` |
| Move horizontal scrollbar left-most | `Shift+Home` |
| Move horizontal scrollbar right-most | `Shift+End` |

**SimTalk:** `IsShown`

---

## Collect Data check box

Select this check box to make a Chart of Category **Histogram** or **Plotter** collect data during the simulation run. Clear it to deactivate data collection.

**SimTalk:** `CollectData`

---

## Tab Data

On the **Data** tab you select the **Data Source** and the **Mode**.

### Data Source

- **Data Table** — shows the contents of a DataTable as a diagram.
  - Type the name/path of the table, or click the button and select the table in *Select Object*.
  - **Range** of table cells (e.g. `{*,*}..{*,*}`, `{1,1}..{1,4}`, `{1,1}..{1,*}`, `{-2,*}..{-2,*}`, `{-2,*}..{*,*}`).
- **Input Channels** — shows the channels in the Input Channels table (paths to attributes/methods, or complex expressions such as method calls, formulas, or sums). Type row/column headers as labels.
  - To specify a formula, type it directly into the cell (do not click the formula button on the List ribbon tab).
- **Worker Pools** — shows Workers managed by WorkerPools.
  - Group Workers by **Pool** (entire WorkerPool) or **Creation Table** (Workers in the *Workers to Create* table).
  - Occupancy statistics: **Operational + failed** or **Overall Time**.

**SimTalk:** `DataRange`, `DataTable`, `InputChannels`, `UseInputChannels`

### Data

Select how the Chart shows the data: **In Rows** or **In Columns**.

**SimTalk:** `DataInColumn`

### Mode

- **Sample Mode** — updates periodically after the entered interval.
- **Watch Mode** — updates whenever watchable input data changes (see the *Watchable* column in *Show Attributes and Methods*).
- **Plot Mode** — updates whenever a simulation event takes place.

**SimTalk:** `update`, `NumIntervals`, `Mode`, `SampleInterval`

---

## Tab Display

- Category **Histogram**: can show data **Accumulated**.
- Category **Plotter**: can show data as a **Step Curve**.

### Category drop-down list

- **Chart** — a number of values or several sets of values.
- **Histogram** — frequency distribution for one or several input channels (check box *Accumulated* available). Input channels should be watchable for exact values.
- **Plotter** — progression of one or more values over time (check box *Step Curve* available).
- **3D Chart** — a 3D Chart embedded in the 3D display window (cannot be opened in its own window).
- **3D Histogram** — a 3D Histogram embedded in the 3D display window.
- **XY Graph** — x-y pairs of values (only active for Data Source **Table File**). x-values in first row/column; the range determines y-values.

**SimTalk:** `Category`, `putValuesIntoTable`, `resetValues`

### Category — 3D Chart / 3D Histogram

- Fixed **Font Size** (only *Bold* affects it). For width/height > 5 m the font size is absolutely fixed; smaller sizes scale down.
- Uses **Color** and **Line Weight** from the Color tab for Chart Type **Line**; no Marker Type or Line Style.
- Set the **Opacity** of Background and Desk to 0 to hide the base plate/background (transparent chart/histogram).
- Base plate thickness defaults to 20 cm (10 cm when Background opacity = 0); scales down for sizes < 5 m.

### Chart Type drop-down list

| Type | Description |
|---|---|
| Columns | Each record as a column; several records placed next to each other |
| Stacked Columns | Columns stacked on top of each other |
| 100% Stacked Columns | Stacked columns showing percentage of 100% |
| Bars | Horizontal bars; records placed next to each other |
| Stacked Bars | Bars stacked horizontally |
| 100% Stacked Bars | Horizontal bars showing percentage of 100% |
| Area | Areas stacked one behind the other |
| Stacked Area | Areas stacked on top of each other |
| 100% Stacked Area | Areas showing percentage of 100% |
| Line | Each record as a line |
| Line with Markers | Line with markers |
| Spline | Each record as a curve |
| Spline with Markers | Curve with markers |
| Markers | Each record as a set of different markers |
| Points and Best Fit Conveyor | Data points with best-fit straight line (least squares) |
| Points and Best Fit Curve | Data points with best-fit curved line (least squares) |
| Pie | Slices depicting percentage of the whole |
| XY Points | x-y pairs as data points |
| Line | x-y pairs connected with a line |
| Sticks | Vertical bar for each x-y pair from the zero line |
| Area | Connected x-y points with filled areas |
| 3D Columns | Columns stacked in 3D space (Rotation/Height to turn) |
| 3D Wire Frame | Wire-frames stacked in 3D space |
| 3D Surface | Solid areas stacked in 3D space |

**SimTalk:** `ChartType`, `Rotation`, `Height`

### 3D Effect

- **None**, **Shadow** (black shadow), **3D** (3D depth), **Gradient Bars** (for Columns and Bars), **Contoured** (for 3D Columns and 3D Surface).

**SimTalk:** `Effect`

### Graph/table drop-down list

- **Graph** — records as graph only.
- **Table** — records as table only.
- **Graph and Table** — records as graph and table.

**SimTalk:** `GraphTable`

### Display in Frame check box

Display the Chart itself in the Frame (instead of the icon). Type in **Width** and **Height**, and set **3D Image Quality**.

**SimTalk:** `DisplayInFrame`

### Width / Height text boxes

Activate *Display in Frame* and type the Width/Height in meters.

**SimTalk:** `SizeInFrame`

### 3D Image Quality drop-down list

Only available with *Display in Frame*: **High quality**, **Balanced**, **High performance**.

**SimTalk:** `ImageQuality3D`, `DisplayInFrame`

### Gap When Null check box

Interrupt the line for undefined values (clear to continue the line). **Undefined Value**: value treated as undefined (default `-999999`).

**SimTalk:** `GapWhenNull`, `NullValue`

### Accumulated check box

Creates an accumulated histogram (adds sum of all previous values; last value = 100%). Only for Category **Histogram**.

**SimTalk:** `Accumulated`

### Step Curve check box

Show a Step Curve instead of straight lines. Only for Category **Plotter**.

**SimTalk:** `StepCurve`

---

## Tab Axes

Different settings depending on the Category.

### Grid Lines Y-Axis

Show/hide Y-axis grid lines. **Interval** sets distance of horizontal grid lines and labels (empty = auto).

**SimTalk:** `XGrid`, `YGrid`, `YGridLineInterval`

### Grid Lines X-Axis

Show/hide X-axis grid lines. **Number** sets maximum grid lines shown. For Category **XY-Graph**, the Number is only evaluated with a fixed Range X (no asterisk).

**SimTalk:** `XGrid`, `YGrid`, `XGridlines`

### Logarithmic Y-Axis

Activate logarithmic scaling on the y-axis (useful for data scattered across several orders of magnitude; cannot show negative values). Requires Range Y value > 0 (e.g. `0.1`).

**SimTalk:** `YLog`

### Logarithmic X-Axis

Logarithmic scaling on the x-axis (only for Chart Type **XY-Graph**; not shown for all chart types).

**SimTalk:** `XLog`

### Number of Values text box

Number of values collected over time per channel (applies to Category **Plotter**). Older values are dropped once the number is reached.

**SimTalk:** `NumValues`

### Scrollbar check box

Add a scrollbar to the Chart window for Category **Plotter**. When active, a **Feed Rate** can be entered.

**SimTalk:** `ScrollBar`

### Feed Rate text box

Number of grid units by which the Chart scrolls when it reaches the right border (Plotter). Value between `0.1` (smooth) and `12` (entire page).

**SimTalk:** `FeedRate`

### Step Size text box

Width of intervals for the frequency distribution (Category **Histogram**).

**SimTalk:** `StepSize`

### Range Y

First/last value of the y-axis range. Default `0 … *` (0 to largest value). Use `*` for open/semi-open ranges:

| Type in | To do this |
|---|---|
| `* … *` | Values between smallest and greatest |
| `0 … *` | Values between 0 and greatest |
| `* … 7.5` | Values between smallest and 7.5 |
| `-20 … 20` | Values between -20 and +20 |

**SimTalk:** `YScaleMin`, `YScaleMax`, `XScaleMin`, `XScaleMax`

### Range X

First/last value of the x-axis range. Default `0 … 0` shows the entire range of definition. Use `*` for open/semi-open ranges (see Range Y examples). For **Histogram**, Range X defines the range of definition (type `0` right to auto-adjust; use Step Size). For **Plotter**, Range X defines the displayed time span.

**SimTalk:** `XScaleMin`, `XScaleMax`, `XRange`, `FirstInterval`, `NumIntervals`, `StepSize`

---

## Tab Labels

Type a **Title**, **Subtitle**, and labels for the **X-Axis**, **Y-Axis**, and **Z-Axis**. Select Legend position and Annotations.

**Title** — text shown as the Chart title (font on Tab Font). **SimTalk:** `Title`

**Subtitle** — text shown as the Chart subtitle. **SimTalk:** `SubTitle`

**X-Axis** — text on the x-axis. **SimTalk:** `XLabel`

**Y-Axis** — text on the y-axis. **SimTalk:** `YLabel`

**Z-Axis** — text on the z-axis (only for 3D Chart Types). **SimTalk:** `ZLabel`

**Note:** If neither Title nor Subtitle is specified, the upper part of the Y range may be cut off; enter a blank space in Subtitle to prevent this.

### Legend

Select legend position: **Off**, **On the Right** (one/two lines/stacked), **On the Left** (one/two lines), **At the Top** (one/two lines), **At the Bottom** (one/two lines).

**SimTalk:** `LegendLocation`

### Annotations button

Opens the Annotations table to add lines and text. Settings:

- **Type** — `0` Vertical Line, `1` Horizontal Line, `2` X-axis Label, `3` Y-axis Label, `4` Text.
- **Value** — where the line is displayed (Y-value for horizontal/Y-axis; X-value for vertical/X-axis).
- **From** / **To** — start/end point of the line (allows diagonal lines).
- **Color** — color number (define on Tab Color).
- **Style** — line style (types 0/1) or marker style (type 4).

| Value | Line style | Marker style |
|---|---|---|
| 0 | thin solid line | text only, no marker |
| 1 | dashed line | plus sign |
| 2 | dotted line | cross |
| 3 | dash-dot line | circle |
| 4 | dash-dot-dot line | filled circle |
| 5 | medium thin solid line | square |
| 6 | thick solid line | filled square |
| 7 | grid tick | diamond |
| 8 | grid line | filled diamond |
| 9 | none | upward triangle |
| 10 | medium thick solid line | solid upward triangle |
| 11 | extra thick solid line | downward triangle |
| 12–24 | none | various triangle/circle/square/diamond markers (small) |
| 25–36 | none | large markers |
| 92–99 | none | arrow north/north east/east/south east/south/south west/west/north west |

- **Text** — description text, optionally with two-character prefix codes (`|` + letter):

| Prefix | Position |
|---|---|
| `|l` | left inside edge |
| `|L` | left outside edge |
| `|r` | right inside edge |
| `|R` | right outside edge |
| `|c` | centered inside |

User-defined annotations are always shown in the foreground.

**SimTalk:** `getAnnotations`, `setAnnotations`

---

## Tab Color

Select colors for **Grid**, **Background**, **Desk**, **Text**, the plotted data (numbers 1–14), and additional colors. Add/Delete colors, set **Opacity**, **Line Style**, **Line Weight**, and **Marker Size**.

**SimTalk:** `setColor`, `setLineStyle`, `getColor`, `getLineStyle`

### Color

| Item | Number |
|---|---|
| Grid | -3 |
| Background | -2 |
| Desk | -1 |
| Text | 0 |
| Colors (predefined input channels) | 1–14 |

Double-click the Color box to open the MS Windows *Colors* dialog.

### Opacity

`0` = entirely transparent, `255` = completely opaque.

### Line Style / Line Weight / Marker Type

Configure line properties (used for Chart Types **Line** and **Spline**; **Marker Type** for **Line with Markers** and **Spline with Markers**).

**SimTalk:** `setLineStyle`, `getLineStyle`

### Add / Delete

Add additional colors to the color table; delete the selected color.

### Marker Size

Select marker size (applies to **Line with Markers** and **Spline with Markers**).

---

## Tab Font

Select a font, text effects, and zoom factor for **Labels**, **Title**, **Subtitle**, and **Table** data.

- **Labels** — font for labels (not Title/Subtitle/Table). **SimTalk:** `LabelFont`
- **Title** — font for the Title. **SimTalk:** `TitleFont`
- **Subtitle** — font for the Subtitle. **SimTalk:** `SubtitleFont`
- **Table** — font for Table-format data. **SimTalk:** `TableFont`

Font Size numbers are factors, not actual point sizes.

---

## Tools Menu

### Use Metric Prefix

Show a unit prefix on the y-axis for very large/small values (e.g. `100K` instead of `100000`). Prefixes: p (pico), n (nano), u (micro), m (milli), K (kilo), M (million), B (billion), T (trillion).

**SimTalk:** `UseMetricPrefix`

### Reset Values

Deletes all values the Chart collected. **SimTalk:** `resetValues`

### Print

Opens the Print dialog. **SimTalk:** `showPrintDialog`

### Copy to Clipboard

Copies the Chart window content as a bitmap. **SimTalk:** `copyBitmapToClipboard`

---

## Methods of the Chart

The Chart provides the methods listed above plus the **Methods of All Objects**. View all methods, read-only attributes, and attributes via **Show Attributes and Methods** (context menu of the Class Library, or `F8` in a Frame).

Key SimTalk methods/attributes referenced throughout:

`addObject`, `IsShown`, `CollectData`, `DataRange`, `DataTable`, `InputChannels`, `UseInputChannels`, `DataInColumn`, `update`, `NumIntervals`, `Mode`, `SampleInterval`, `Category`, `putValuesIntoTable`, `resetValues`, `ChartType`, `Rotation`, `Height`, `Effect`, `GraphTable`, `DisplayInFrame`, `SizeInFrame`, `ImageQuality3D`, `GapWhenNull`, `NullValue`, `Accumulated`, `StepCurve`, `XGrid`, `YGrid`, `YGridLineInterval`, `XGridlines`, `YLog`, `XLog`, `NumValues`, `ScrollBar`, `FeedRate`, `StepSize`, `YScaleMin`, `YScaleMax`, `XScaleMin`, `XScaleMax`, `XRange`, `FirstInterval`, `Title`, `SubTitle`, `XLabel`, `YLabel`, `ZLabel`, `LegendLocation`, `getAnnotations`, `setAnnotations`, `setColor`, `setLineStyle`, `getColor`, `getLineStyle`, `LabelFont`, `TitleFont`, `SubtitleFont`, `TableFont`, `UseMetricPrefix`, `showPrintDialog`, `copyBitmapToClipboard`, `updateDialog`
