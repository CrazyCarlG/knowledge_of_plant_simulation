# HtmlReport [object]

Use the object **HtmlReport** for presenting current data and results of the simulation run in a report that you can share with co-workers and customers.

You can save the HtmlReport as an `.htm` file and open it in any HTML browser (Microsoft Edge, Firefox, Google Chrome, etc.). Plant Simulation is **not** required to view it on another computer.

> **Note:** The easiest way to configure the contents is to drag an object from the Frame to the tab **Content** and drop it there. You can type additional content and formatting in the built-in markup language on the tab Content. You can also show another HtmlReport within an HtmlReport.

To add the object to the simulation model: click **Manage Class Library > Basic Objects > UserInterface > HtmlReport** on the Home ribbon tab.

---

## Dialog Box of the HtmlReport

Double-click the icon to open its dialog box.

- **Edit Simulation Properties** — change the simulation properties of the object (shared properties described under *Dialog Items of the Objects*).
- **Edit Animation Properties** — click **Edit 3D Properties** in the lower left corner, or select the object and press the spacebar.

---

## Show Report

To open the display window of the HtmlReport, click **Show Report** (or right-click the object in the Frame and select **Show**).

The Display Window contains:

- **Display Pane** (right) — shows the content of the report defined on the tab Content.
- **Structure Pane** (left) — shows the first two heading levels; click a heading to jump to it.

### Structure Pane of the Display Window

- Click a level 1/2 heading to jump to it in the display window.
- Print the report.
- Save the content as a web page (`.htm`/`.html`).
- Refresh the report with current model data.
- Scroll with mouse wheel; zoom with `Ctrl` + mouse wheel.

> **Note:** Print and Save do not work if local security policies deny access to the operating system within the HTML functionality.

### Display Pane of the Display Window

Displays the report content defined on the tab Content. Scroll/zoom with the mouse wheel (hold `Ctrl` to zoom). Click the link of a caption line to open the respective Frame/object.

---

## Tab Content

Define the content the HtmlReport shows. The built-in report provides examples of the most important items.

The check box to the right of the canvas toggles **inheritance**:

- **Green** — inheritance is on; the object uses the value from its parent.
- **Orange with minus** — inheritance is off; values apply only to the selected object.

You can type content as text, or use the dialog **Object Parameters**. The markup language is a superset of HTML (readable, easier than raw HTML). You can also drag objects from the Frame onto the tab Content or onto the HtmlReport icon:

- If Content is **inherited**, the object's data **replaces** the pre-defined content.
- If Content is **not inherited**, Plant Simulation **appends** the data.

You can use default settings, define headings, create lists, bold/italicize, indent, center, add references/images, collect object instances, insert comments, horizontal lines, HTML tags, protect characters, and use strings unchanged.

---

## Toolbar of the HtmlReport

| To do this | Key combination |
|---|---|
| Undo last action | `Ctrl+Z` |
| Bold selected text | `Ctrl+B` |
| Italicize selected text | `Ctrl+I` |
| Numbered list | — |
| Bulleted list | — |
| Increase indent | `Ctrl+M` |
| Decrease indent | `Ctrl+Shift+M` |
| Insert nonbreaking space | `Ctrl+Shift+-` |
| Insert page break (print only) | `Ctrl+Shift+Enter` |
| Add a reference to an object | `Ctrl+K` |
| Add an image of an object | — |
| Add a bitmap file | — |
| Spell check | `Ctrl+S` |

Markup insertion shortcuts:

| To do this | Key combination |
|---|---|
| Heading level 1–6 | `Ctrl+1` … `Ctrl+6` |
| Remove all heading markups | `Ctrl+0` |
| Center a line | `Ctrl+E` |
| Insert soft hyphen | `Ctrl+-` |

---

## Default Settings of the HtmlReport

The `## Drain Statistics` setting shows these values by default (columns: English, German, read-only attribute).

- **Object** — names of all Drain objects that removed parts.
- **Name** — names of part types the Drain removed.
- **Mean Life Time** — `StatAvgLifeSpan` (mittlere Durchlaufzeit).
- **Total Throughput** — `StatDeleted` (Durchsatz).
- **Throughput per Hour** — `StatThroughputPerHour` (Durchsatz pro Stunde).
- **Production** — time portion on production resources.
- **Transport** — time portion on transport resources.
- **Storage** — time portion on storage resources.
- **Value Added** — `StatProdWorkingPortion` (Wertschöpfung).
- **Portion** — accumulated values as bar segments.

### Colors for the Portion
Colored bars show accumulated values: Production (green), Transport (orange), Storage (red).

---

## Formatting Syntax

### Define a Heading

`#` at the start of a line → heading level 1. `##` → level 2. Maximum four levels (`#####`). Levels 1 and 2 appear in the structure pane.

```
# Heading 1
## Heading 1.1
Text below Heading 1.1.
## Heading 1.2
Text below Heading 1.2.
```

### Create a Bulleted List

`* ` (asterisk + space) at the start of a line. Terminate with an empty line. Sublists via tab stop or four spaces before `*`.

```
* List item 1
* List item 2
    * Sublist item 2.1
    * Sublist item 2.2
* List item 3
Text after the list...
```

### Create a Numbered List

`1. ` at the start of a line. Any number works (Plant Simulation always numbers starting at 1). Sublists via tab/four spaces before `1.`.

```
1. Numbered item 1
1. Numbered item 2
    1. Numbered item 2.1
    1. Numbered item 2.2
1. Numbered item 3
```

Bulleted sublists can be nested inside numbered lists:

```
1. Numbered item 1
1. Numbered item 2
        * Sublist item 2.1
        * Sublist item 2.2
1. Numbered item 3
```

### Highlight Text (Bold / Italic)

- `*text*` → italic
- `**text**` → bold
- `***text***` → bold + italic

```
Text can be *italicized* or **bolded** or ***bolded and italicized.***
**Important: *Essential information.* Do not ignore!**
```

> **Note:** The combination space + asterisk is not treated as italic start, so object references like `*.MUs.Part:1` are not misinterpreted.

### Indent Text

`>` at the start of a line indents a paragraph. More `>>` indents further.

```
> This paragraph
is indented.
Non-indented body text after the indented paragraph.
```

### Center Text

`><` at the start of a line centers the text.

```
>< This text is centered.
This text is left-aligned.
```

---

## Adding Object References

To access an object, type `[ObjectName]`. Relative paths resolve from the Frame containing the HtmlReport. Use `self` to reference the HtmlReport itself.

Arguments can be positional (comma-separated) or named (space-separated); both produce the same output:

```
[.Models.Model._3D, "caption", 100%, %planningview]
[.Models.Model._3D Caption="caption" ScaleTo=100% PlanningView=true]
```

Round floating point values by appending the number of decimal places. Prefix `0` to force trailing zeros:

```
[Station1.statFailPortion]
[Station1.statFailPortion, 2]  // round to 2 digits
[Station1.statFailPortion, 02] // 2 decimal places
```

### Display all instances of an object

Append `*` after the path to display all instances (direct/indirect inheritance) in the Frame, including sub-Frames:

```
[.UserInterface.HtmlReport*]
```

---

## Specific Object Displays

### Display an Attribute of an Object

Named argument `Precision` (for Real, Length, Weight, Speed, Time, Acceleration) sets integer/decimal places:

```
[Station.a precision=2]
```

### Display an AttributeExplorer

```
[AttributeExplorer]
[AttributeExplorer, "Tab. 1: Mean value of the throughput times"]
[AttributeExplorer, 0, 2..4, 7]
[AttributeExplorer, *..4, 7]
[AttributeExplorer, 0, 2..4, 7..*]
[AttributeExplorer, 0, 2..4, 7, #ColumnName]
```

### Display a Broker

```
[MyBroker]
[MyBroker, "Tab. 1: Broker Service Statistics"]
[Broker1, 0, 2..4, 7]
[Broker2, *..4, 7]
[Broker3, 0, 2..4, 7..*]
```

### Display a Chart

```
[StationChart]
[StationChart, 80, 60]
[StationChart, "This is my caption"]
[StationChart, "This is my caption", 80, 60]
```

Named arguments: `Caption`, `Size`.

```
[Chart Caption="This is my caption"]
[Chart Size=80,60]
```

Size forms: no argument (default), `[*, y]` (height y), `[x, *]` (width x), `[x, y]` (scale, may distort).

### Display a Checkbox

```
[Checkbox] or [Checkbox, true]   // label right of icon
[Checkbox, false]                // label left of icon
```

Named argument `CheckBeforeText` (default `false`):

```
[Checkbox CheckBeforeText=true]
```

### Display an Object of Type Comment

```
[Comment]
```

### Display a DataTable or a DataList

```
[ThroughputList]
[ThroughputList, "Figure 1: Mean value of the throughput times"]
[ThroughputList, 0, 2]
[ThroughputList, *..4, 7]
[ThroughputList, 0, 2..4, 7..*]
[ThroughputList, 0, 2..4, 7, #MyColumnName]
```

Access cells (similar to formulas):

```
[MyDataTable[Column, Row]]
[MyDataTable[1, 1]]
[MyDataTable["Name", 1]]
[MyDataTable["Name", "Part type 1"]]
[MyDataTable[#Name, 1]]
[MyDataTable[#Name, #Part type 1]]
```

Protect special characters inside column index text:

```
[MyDataTable["\"Name\"", 1]]
[MyDataTable["Speed\, km/h", 1]]
[MyDataTable[#Speed\, km/h, 1]]
```

Named arguments: `Caption`, `Columns`.

```
[DataTable Caption=Test Columns=[1,3,4]]
```

### Display an Object of Type Display

Optional `true`/`false` (use the Display's color/font size):

```
[Display]
[Display, true]
[Display, false]
```

Named argument `UseFontStyle` (default `false`):

```
[Display UseFontStyle=true]
```

### Display a Drain

```
[Shipping, "Statistics of the Drain 'Shipping", %DrainTypesPortions]
```

If no Statistics Type Table is selected, the Drain report equals the EventController's *Show Summary Report* (without the first Drain-name column).

### Display a Dropdown List

```
[DropDownList]
```

### Display a FileLink

```
[FileLink, "Siemens logo imported via the FileLink", 110%]
```

Named arguments: `Caption`, `Size`.

```
[FileLink Caption="Siemens logo imported via the FileLink"]
[FileLink Size=110%]
```

### Display a Frame

Screenshot of a Frame (caption defaults to the path). Size options: `*` (zoom out with window), `N%` (percent), or width/height in millimeters (either may be `*`).

```
[MyEngines]
[MyEngines, *]
[MyEngines, 150%]
[MyEngines, 100, 150]
[MyEngines, 100, *]
[MyEngines, *, 150]
[MyEngines, "This is my caption"]
[MyEngines, "This is my caption", *]
[MyEngines, "This is my caption", 150%]
[MyEngines, "This is my caption", 100, 150]
[MyEngines, "This is my caption", 100, *]
[MyEngines, "This is my caption", *, 150]
```

A user-defined attribute `ReportObject` (type object/table/method) makes Plant Simulation display the referenced object instead; alternatively rename an inserted object to `ReportObject`.

### Display a GanttChart

```
## GanttChart
[GanttChart, "My Caption", 0.5]
```

Named arguments: `Caption`, `Scale`.

```
[GanttChart Caption="My Caption"]
[GanttChart Scale=0.5]
```

### Display a HtmlReport

You can pass an object argument, accessed in the called report via `[@]`. Number signs `#` increase heading levels by 1 each.

```
[HtmlReport2]
[HtmlReport2, Station1]
[HtmlReport2, Station1, #]
```

Create sub-reports for all instances with `*`:

```
[HtmlReport2, .MaterialFlow.Station*]
```

### Display an Icon of an Object

Named-argument icon statements require a leading `!`.

```
[!.Models.Model.Station, "Operational", "Operational icon", 200, 200]
[!Station Icon=Operational]
```

Named arguments: `Icon` (name or number; default = active icon), `Caption`, `Size`.

### Display a Method

Run a Method and display its return value:

```
[Method]
[Method(Argument1, Argument2])
```

Example source code:

```
param obj: object -> string
return to_str("x=", obj.XPos, ", y=", obj.YPos)
```

```
[MyMethod(MyStation)]
```

### Display a PythonModule

```
[PythonModule]
```

Named argument `Call` (function whose string return value is shown):

```
[PythonModule Call="multiply"]
```

### Display a SankeyDiagram

```
[SankeyDiagram, Workers Sankey flows, 90, 90]
[SankeyDiagramm1, Parts Sankey flows, 85%]
```

With camera position/rotation:

```
Path[, Title][, SizeParameters][[CameraPosX, CameraPosY, CameraPosZ], CameraRotX, CameraRotZ]
```

Named argument `Type` (default `"exclusive"`):

```
[SankeyDiagram Type="exclusive"]
[SankeyDiagram Type="additional"]
[SankeyDiagram Type="all"]
```

> **Note:** `exclusive`/`additional`/`all` work only in English/Chinese/Japanese/Hungarian models; German uses `exklusiv`/`zusätzlich`/`alle`.

### Display Statistics Values of an Object as a Table

```
[Receiving, "Statistics of the Source 'Receiving'", %Stati]
[Receiving, "Statistics of the Source 'Receiving", %Stati, 4,6]
```

General syntax:

```
[Object path, caption, statistics table type]
[Receiving, "Statistics of the Source 'Receiving'", %States]
[Station, "My values", %States, 1..4]
[Station, "My values", %States, #Working, #SettingUp]
```

Statistics Table Type codes (English / German):

| Type | English | German |
|---|---|---|
| Portions of the States | `%ResStates` | `%Stati` |
| Material Flow Properties | `%MatFlowProperties` | `%Matflusseigenschaften` |
| Rotation Time | `%RotationTime` | `%Drehungszeit` |
| Moving Time (Converter) | `%MovingTime` | `%Umsetzzeit` |
| Working Time | `%WorkingTime` | `%Arbeitszeit` |
| Set-up Time | `%SetupTime` | `%Rüstzeit` |
| Waiting Time | `%WaitingTime` | `%Wartezeit` |
| Blocked Time | `%BlockedTime` | `%Blockiertzeit` |
| Powering up/down Time | `%PowerUpDownTime` | `%HochHerunterfahrzeit` |
| Stopped Time | `%StoppedTime` | `%Angehaltenzeit` |
| Failed Time | `%FailedTime` | `%Störungszeit` |
| Paused Time | `%PausedTime` | `%Pausenzeit` |
| Empty Time | `%EmptyTime` | `%Leerzeit` |
| Material Flow Properties of Mobile Units | `%MUMatFlowProperties` | `%BEMatflusseigenschaften` |
| Empty Time of Mobile Units | `%MUEmptyTime` | `%BELeerzeit` |
| Cumulated Statistics (Drain) | `%DrainCumulated` | `%SenkeKumuliert` |
| Part Types (Drain) | `%DrainAllTypes` | `%SenkeAlleTypen` |
| Detailed Portions of Part Types | `%DrainTypesPortions` | `%SenkeTypenanteile` |
| Detailed Times of Part Types | `%DrainTypesTimes` | `%SenkeTypenzeiten` |
| Total Consumption / Energy States | `%Energy` | `%Energie` |
| Product-Oriented Statistics (MU classes) | `%MUClassStatistics` | `%BEKlassenStatistik` |
| Mean Time Portions of a MU Class | `%MUClassTimePortions` | `%BEKlassenZeitanteile` |
| Mean Time Portions of an Individual MU | `%MUTimePortions` | `%BEZeitanteile` |
| Usage of the Transporters | `%TransUsageTime` | `%TransVerwendungszeit` |
| Ready Times | `%TransReadyTime` | `%TransBereitzeit` |
| Pauses | `%TransPausedTime` | `%TransPausenzeit` |
| Failures | `%TransFailedTime` | `%TransStörungszeit` |
| Traveled Distance | `%TransTraveledDistance` | `%TransWegstrecke` |
| Battery | `%TransBatteryTime` | `%TransBatteriezeit` |
| Broker Statistics | `%Broker` | `%Broker` |
| Mediation Time | `%BrokerMediationTime` | `%BrokerVermittlungsdauer` |
| Dwelling Time | `%BrokerDwellTime` | `%BrokerVerweildauer` |
| Capacities and States of the Exporters | `%Exporter` | `%Exporter` |
| Time Portions of the Exporters | `%ExporterTimePortions` | `%ExporterZeitanteile` |
| Traveled Distance by Workers | `%WorkerTraveleledDistance` | `%WerkerWegstrecke` |
| Importers Waiting for Services and Parts | `%ImporterWaiting` | `%ImporterWartend` |
| Waiting Times for Services and Parts | `%ImporterWaitingTime` | `%ImporterWartezeit` |
| Waiting Times for Parts | `%ImporterMUWaitingTime` | `%ImporterBEWartezeit` |
| Waiting Times for Set-up Exporters | `%ImporterSetpWaitingTime` | `%ImporterRüstWartezeit` |

Default statistics types (English / German):

| Object | English | German |
|---|---|---|
| Part | `%MUTimePortions` | `%BEZeitanteile` |
| Container | `%MUMatFlowProperties` | `%BEMatFlusseigenschaften` |
| Transporter | `%TransUsageTime` | `%TransVerwendungszeit` |
| Worker | `%WorkerTraveledDistance` | `%WerkerWegstrecke` |
| Turnplate/Turntable/PickAndPlace | `%RotationTime` | `%Drehungszeit` |
| Converter | `%MovingTime` | `%Umsetzzeit` |
| Drain | `%DrainCumulated` | `%SenkeKumuliert` |
| Exporter | `%Exporter` | `%Exporter` |
| Broker | `%BrokerMediationTime` | `%BrokerVermittlungsdauer` |
| All other objects | `%States` | `%Stati` |

### Display a Table from the SQLite Interface

```
[MySQLite, "select * from MUTrace"]
```

Named arguments: `Statement`, `MaxRows`.

```
[MySQLite Statement="select * from MUTrace"]
[MySQLite MaxRows=5]
```

### Display a Variable

For numeric types (real, length, money, weight, time, speed, acceleration), specify decimal/integer places. DataTable/List contents are parametrized like a DataTable. Object references show the path (or `?` if missing).

```
[Variable]
[Variable, "Tab. 1: List of all tabular values"]
[Variable, 0, 2..4, 7]
[Variable, *..4, 7]
[Variable, 0, 2..4, 7..*]
[>Variable] // shows object-specific content instead of path
```

Named argument `Precision`:

```
[Variable Precision=5]
```

### Display a Picture of a Scene (3D)

```
[Object._3D]
[Object._3D, w, h]
[Object._3D, [caption,] w, h]
[Object._3D, w, h, crx, crz]
[Object._3D, [caption,] w, h, crx, crz]
[Object._3D, w, h, cpx, cpy, cpz, crx, crz]
[Object._3D, [caption,] w, h, cpx, cpy, cpz, crx, crz]
```

`[Object._3D, w, h]` creates a View All view with `crx=45°`, `crz=15°`.

Arguments: `caption`, `object`, `w` (width px), `h` (height px), `cpx`/`cpy`/`cpz` (camera position), `crx`/`crz` (camera rotation).

```
[Station._3D, 150, 100, -29.596, -31.985, 39.985, 46.983, -36.669]
```

Planning View code (generated via *Generate HtmlReport Code and Copy to Clipboard*):

```
[.Models.Model._3D Size=[874,491] PlanningView=true ViewPos=[21.483,-11.597] ViewZoom=23.294]
```

Modeling View code:

```
[.Models.Model._3D Size=[874,491] PlanningView=false CameraPos=[15.211,-46.816,29.319] CameraRotX=48.000 CameraRotZ=-8.500]
```

Camera-only/position+rotation with two asterisks:

```
[current, *, *, -45.0]
[current, *, *, -7.12, 8.123, 1.24, -45.0, 15,0]
```

Keywords `%planningview` and `%modelingview`:

```
[current, *, *, %planningview]
[current, *, *, %modelingview]
```

Named arguments: `Caption` (default = object path), `PlanningView` (default = Frame's view option, else `false`), `Size` (default `700 x 500`), `ScaleTo` (default `100%`), plus planning-view arguments `ViewPos`, `ViewZoom` and modeling-view arguments `CameraPos`, `CameraRotX`, `CameraRotZ`.

---

## Compute a Formula

Type a formula between `[=` and `]`. Optional decimal places (prefix `0` to force zeros):

```
[=Station1.statWorkingPortion + Station1.statBlockingPortion]
[=Station1.statWorkingPortion + Station1.statBlockingPortion, 2]
[=Station1.statWorkingPortion + Station1.statBlockingPortion, 02]
```

To display an object itself (not its path), use `[>`:

```
[>Source.path]
[>@.~]
[>=str_to_obj(Variable)]
```

---

## Add an Image of an Object

Type `[!MyObject]`. To show a specific icon, add its name or number:

```
[!Station1]
[!Station1, Default]
[!Station1, 0]
```

Size options: `*`, `N%`, or width/height in mm (one may be `*`):

```
[!Station1, "Operational","My Station 50 x 50%", 50, 50]
[!Station1, "Operational", "My Station scaled to 110%", 110%]
```

Example with full settings:

```
[!MyMethod, "ExitCtrl", "My icon of the object 'Method'", 110%]
```

---

## Add a Bitmap File

Creates an icon from a bitmap file:

```
[!self, "SiemensLogo", "Show Siemens Logo"]
```

---

## Collect Object Instances and Show Them

Append `*` to the object path:

```
# Collect all instances of the object 'DataTable'
[.InformationFlow.DataTable*]
```

Titles can contain formulas (start with `=`). Use `@` for the anonymous instance. Protect inner quotes with `\`:

```
# Collect object instances as per @.Label
[.InformationFlow.DataTable*, "=@.Label"]
[.UserInterface.Chart*, "=@.Label"]

# Collect object instances as per @.Name
[.InformationFlow.DataTable*, "=@.Name"]

# Normal caption formula evaluations
[.InformationFlow.DataTable*, "=@.Location"]
[.InformationFlow.DataTable*, "=@.Name + \" in \" + to_str(@.Location)"]

# Complex expressions
[.InformationFlow.DataTable*, "=1+sin(pi/2)"]
[.InformationFlow.DataTable*, "=\"#\" + @.Name"]
[.UserInterface.Chart*,"=1+sin(pi/2)"]
```

If `@.Name` or `@.Label` is used, Plant Simulation adds a link to open the instance. Any title containing a valid path is underlined as a link.

> **Note:** Statistics data do not support caption formulas:

```
[.MaterialFlow.Station*, "=@.Name"]
```

---

## Insert a Comment into Your Report

Two hyphens `--` start a comment that extends to the end of the line:

```
This text will be displayed. -- This text will not be displayed.
```

---

## Insert a Horizontal Line

Three (or more) hyphens `---` not followed by text create a horizontal line:

```
Text above the line.
------
Text below the line.
--- This is a comment ---
```

---

## Insert HTML Tags

Type HTML tags within angle brackets. Recognized only if no space follows `<` and the closing `>` is on the same line. Markup language is not analyzed inside the tags.

```
<span style="color:blue">My blue text</span>
<a href="http://www.siemens.com">Visit us on the Siemens Homepage</a>
<!-- This is an HTML comment which is exported to the .htm file. -->
<a href="mailto:Max.Mustermann@siemens.com?subject=Simulation report">Max.Mustermann@siemens.com</a>
```

---

## Protect Characters

Prefix a special character with `\` to display it literally:

```
\-- This is not a comment.
1\. This is not a numbered list.
\[%\] This is a percentage sign within brackets.
```

Protectable characters: `\` (`\\`), `*` (`\*`), `#` (`\#`), `[` (`\[`), `]` (`\]`), `-` (`\-`), `.` (`\.`), `<` (`\<`), `>` (`\>`).

---

## Spell Check the Content of the HtmlReport

Click the button or press `Ctrl+S`. Uses the Windows spell checker; ignores text within `[` `]`.

> **Note:** Does not work for Chinese and Japanese.

---

## Use a String Unchanged in the HTML Code

Enclose the string between `<<` and `>>`. Any length, any number of line breaks.

- Prevents long strings being interpreted as markup (e.g., `<<------>>` instead of protecting each hyphen).
- Generates characters with special HTML meaning literally (e.g., `<<“>>`, `<<&#8240;>>`).

---

## Tab User-defined

Define your own attributes as described under *Tab User-defined*.

---

## Menus

- **Navigate Menu** — commands described under *Navigate Menu*.
- **View Menu** — commands described under *View Menu*.
- **Tools Menu** — provides *Edit Controls* and *Edit Observers*.
- **Help Menu** — commands described under *Help Menu*.

---

## Methods of the HtmlReport

The HtmlReport provides:

- The methods listed in the table of contents (see the Help's methods section).
- The *Methods of All Objects*.

To view all methods/read-only attributes/attributes, open **Show Attributes and Methods** (`F8`, or via the Class Library context menu).
