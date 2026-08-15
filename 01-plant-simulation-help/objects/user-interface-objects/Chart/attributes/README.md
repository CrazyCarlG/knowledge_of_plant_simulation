# Chart — Attributes

This README summarizes the attributes of the **Chart** user-interface object, based on the content of `attributes.md` in this directory.

The Chart provides:

- The attributes listed below.
- The attributes of all objects (see *Attributes of All Objects*).

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods**:

- In the Class Library, select **Show Attributes and Methods** on the context menu to show them for a Class.
- For an inserted Instance, press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame.

Attributes can be set and read via dialog controls or by assigning values in SimTalk, for example:

```simtalk
MyChart.DataRange := "{0,0}..{2,4}"   -- set
print MyChart.DataRange               -- get
print MyChart.UUID                    -- query a read-only attribute
```

---

## Attribute summary

| Attribute | Type | Description | Notes |
|---|---|---|---|
| Accumulated | boolean | Creates an accumulated histogram (`true`) or not (`false`). | Category > Histogram. Last accumulated value is 100 %. |
| Category | string | Category the Chart displays. | `"Chart"`, `"Histogram"`, `"Plotter"`, `"3D Chart"`, `"3D Histogram"`. |
| ChartType | string | Chart type the Chart displays. | For 3D types, `Height` and `Rotation` also apply. |
| CollectData | boolean | Collects data (`true`) or not (`false`). | Histogram / Plotter. |
| DataInColumn | boolean | Shows data in columns (`true`) or rows (`false`). | |
| DataRange | string | Data range used by the Chart's data table. | Supports `{row,col}..{row,col}` with `*` and negative indices. |
| DataTable | object | Table containing the data to display. | |
| DisplayInFrame | boolean | Shows Chart contents in the Frame (`true`) or its icon (`false`). | When `true`, line styles/weights cannot be freely combined. |
| Effect | string | 3D effect for a number of chart types. | `"None"`, `"Shadow"`, `"3D"`. |
| FeedRate | real | Scroll feed rate when the Chart reaches the right edge. | Category > Plotter. `0.1` = smooth, `12` = whole page. |
| FirstInterval | integer | Smallest value shown by the Histogram. | Left text box value. |
| GapWhenNull | boolean | Interrupts the line for undefined values (`true`) or keeps drawing (`false`). | |
| GraphTable | string | What the Chart shows. | `"Graph"`, `"Table"`, `"Graph and Table"`. |
| Height | integer | Height of the viewing angle for 3D chart types. | Range −50 … 50. |
| ImageQuality3D | string | Image quality shown in the Frame. | Active when `DisplayInFrame` is `true`; only in a 3D model. |
| InputChannels | table | Table defining all input channels. | Assignment with `:=` deactivates inheritance. |
| IsShown | boolean | Activates (`true`) / deactivates (`false`) the Chart display. | Watchable. |
| LabelFont | string (+ sub) | Properties of the axis labels. | Sub-attributes: `Size` (1–8), `Bold`, `Italic`. |
| LegendLocation | string | Type and position of the Legend. | |
| Mode | string | Operating mode. | Category > Histogram. `"Sample"`, `"Watch"`, `"Plot"`. |
| NullValue | real | Value treated as undefined (not displayed). | Default `-999999`. |
| NumIntervals | integer | Number of intervals for a Histogram's frequency distribution. | |
| NumValues | integer | Number of values collected over time per channel. | Category > Plotter. |
| Rotation | integer | Rotation angle (degrees) for 3D chart types. | |
| SampleInterval | time | Period between two sampling actions (Sample mode). | `0` prevents updates; use the `update` method. |
| ScrollBar | boolean | Shows a scrollbar (`true`) or not (`false`). | Category > Plotter. |
| SizeInFrame | array[2] | Width and height of the Chart in length units in the Frame. | Two integers. |
| StepCurve | boolean | Creates a step curve (`true`) or not (`false`). | Category > Plotter. |
| StepSize | real | Width of the intervals of the frequency distribution. | Category > Histogram. |
| SubTitle | string | Subtitle shown in the Chart window. | |
| SubtitleFont | string (+ sub) | Properties of the Subtitle. | Sub-attributes: `Bold`, `Italic`. |
| TableFont | string (+ sub) | Properties of the labels shown as a Table. | Sub-attribute: `Size` (1–8). |
| Title | string | Title shown in the Chart window. | |
| TitleFont | string (+ sub) | Properties of the Title. | Sub-attributes: `Size` (1–8), `Bold`, `Italic`. |
| UseInputChannels | boolean | Takes data from input channels (`true`) or a DataTable (`false`). | |
| UseMetricPrefix | boolean | Shows a unit prefix on the y-axis (`true`) or not (`false`). | e.g. `100K` instead of `100000`. |
| XGrid | boolean | Shows the grid on the x-axis (`true`) or not (`false`). | |
| XGridlines | integer | Number of grid lines on the x-axis. | Grid lines are limited by the number of data sets. |
| XLabel | string | Label of the x-axis. | Applies to 3D Columns, 3D Wire Frame, 3D Surface. |
| XLog | boolean | Logarithmic x-axis (`true`) or not (`false`). | |
| XRange | time | Time span (seconds of simulation time) shown in the display. | Category > Plotter. |
| XScaleMax | integer | Upper bound for scaling on the x-axis. | |
| XScaleMin | integer | Lower bound for scaling on the x-axis. | |
| YGrid | boolean | Shows the grid on the y-axis (`true`) or not (`false`). | |
| YGridLineInterval | real | Interval between grid lines on the y-axis. | `0` = auto-determined interval. |
| YLabel | string | Label of the y-axis. | Applies to 3D Columns, 3D Wire Frame, 3D Surface. |
| YLog | boolean | Logarithmic y-axis (`true`) or not (`false`). | Requires `YScaleMin` > 0. |
| YScaleMax | integer | Upper bound of the range on the y-axis. | |
| YScaleMin | integer | Lower bound of the range on the y-axis. | Requires value > 0 when `YLog` is active. |
| ZLabel | string | Label of the z-axis. | Applies to 3D Columns, 3D Wire Frame, 3D Surface. |

---

## Font sub-attributes

The font attributes (`LabelFont`, `SubtitleFont`, `TableFont`, `TitleFont`) accept these sub-attributes:

- `Size` — integer, font size from 1 to 8 (available on `LabelFont`, `TableFont`, `TitleFont`).
- `Bold` — boolean (available on `LabelFont`, `SubtitleFont`, `TitleFont`).
- `Italic` — boolean (available on `LabelFont`, `SubtitleFont`, `TitleFont`).

Supported font names: Arial, Arial Narrow, Comic Sans MS, Courier New, Haettenschweiler, Lucida Console, MS UI Gothic, Tahoma, Times New Roman, Trebuchet MS, Verdana.

> **Note:** MS UI Gothic is intended for Japanese users and may not be present by default on English or German Windows installations.

---

## Metric prefixes (`UseMetricPrefix`)

| Prefix | Meaning |
|---|---|
| p | pico |
| n | nano |
| u | micro |
| m | milli |
| K | kilo |
| M | million |
| B | billion |
| T | trillion |

---

## Related

- **GanttChart [object]** — visualizes the chronological sequence of activities as bars on the time axis (parts on material-flow resources).
