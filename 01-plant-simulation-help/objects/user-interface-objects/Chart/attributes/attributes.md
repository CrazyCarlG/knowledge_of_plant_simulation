# Attributes of the Chart

The Chart provides:
- The attributes listed in the table of contents below.
- The Attributes of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show them for the selected Instance.

You can set the value of an attribute and get its value, either with the check boxes, text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

To set the value of an attribute:

```simtalk
MyChart.DataRange := "{0,0}..{2,4}"
```

To get the value of an attribute:

```simtalk
print MyChart.DataRange
```

To query the value of a read-only attribute:

```simtalk
print MyChart.UUID
```

---

## Attribute Reference

### Accumulated [SimTalk]
Sets if the Chart creates an accumulated histogram (`true`) or not (`false`).

Applies to the setting **Category > Histogram**. The accumulated histogram adds the sum of all previous values to each value; the last value thus is 100 percent.

| X Value | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Y Value, not accumulated | 0 | 25 | 30 | 23 | 12 |
| Y Value, accumulated | 10 | 35 | 65 | 88 | 100 |

```simtalk
<Path>.Accumulated:boolean
```

```simtalk
MyChart.Accumulated := true
```

---

### Category [SimTalk]
Sets the Category that the Chart displays.

```simtalk
<Path>.Category:string
```

You can specify `"Chart"`, `"Histogram"`, `"Plotter"`, `"3D Chart"`, or `"3D Histogram"`.

```simtalk
MyChart.Category := "Plotter"
```

---

### ChartType [SimTalk]
Sets the Chart Type that the Chart displays. For the 3D Chart Types you can also set the Height and the Rotation of the Chart.

```simtalk
<Path>.ChartType:string
```

```simtalk
MyChart.ChartType := "Stacked Bars"
```

---

### CollectData [SimTalk] - Chart
Sets if the Chart of type Histogram or Plotter collects data (`true`) or does not collect data (`false`).

```simtalk
<Path>.CollectData:boolean
```

```simtalk
MyChart.CollectData := true
```

---

### DataInColumn [SimTalk]
Sets if the Chart shows the data in Columns (`true`) or in Rows (`false`).

```simtalk
<Path>.DataInColumn:boolean
```

```simtalk
MyChart.DataInColumn := true
```

---

### DataRange [SimTalk]
Sets the data range, which the objects table of the Chart uses.

```simtalk
<Path>.DataRange:string
```

```simtalk
MyChart.DataRange := "{*,*}..{*,*}"    // no limitations
MyChart.DataRange := "{1,1}..{1,4}"    // designates the first four rows in the first column
MyChart.DataRange := "{1,1}..{1,*}"    // designates the entire first column
MyChart.DataRange := "{-2,*}..{-2,*}"  // designates the one but last column of the DataTable
MyChart.DataRange := "{-2,*}..{*,*}"   // designates the two last columns of the DataTable
```

---

### DataTable [SimTalk] - Chart
Sets the table containing the data, which the Chart displays.

```simtalk
<Path>.DataTable:object
```

```simtalk
MyChart.DataTable := DataTable
```

---

### DisplayInFrame [SimTalk]
Displays the contents of the Chart in the Frame itself when inserted into a Frame (`true`) or in its icon (`false`).

> **Note:** If you set DisplayInFrame to `true`, you cannot freely combine line styles and line weights of the Chart.

```simtalk
<Path>.DisplayInFrame:boolean
```

```simtalk
MyChart.DisplayInFrame := true
```

---

### Effect [SimTalk]
Sets the 3D effect for a number of Chart Types of the Chart.

```simtalk
<Path>.Effect:string
```

You can specify `"None"`, `"Shadow"`, or `"3D"`.

```simtalk
MyChart.Effect := "3D"
```

---

### FeedRate [SimTalk]
Sets the feed rate by which the Chart scrolls, when it reached the right-hand side of the display.

Applies for the setting **Category > Plotter**.

```simtalk
<Path>.FeedRate:real
```

Specify `0.1` for smooth scrolling, or `12` to scroll the entire page.

```simtalk
MyChart.ScrollBar := true
MyChart.FeedRate := 4
```

---

### FirstInterval [SimTalk]
Sets the smallest value that the Histogram of the Chart shows.

The first interval is the value in the left text box.

```simtalk
<Path>.FirstInterval:integer
```

```simtalk
MyChart.FirstInterval := 2
```

---

### GapWhenNull [SimTalk]
Sets if the Chart interrupts the line it draws for values that are not defined (`true`) or if it continues drawing the line (`false`).

```simtalk
<Path>.GapWhenNull:boolean
```

```simtalk
MyChart.GapWhenNull := false
```

---

### GraphTable [SimTalk]
Sets what the Chart shows.

```simtalk
<Path>.GraphTable:string
```

You can specify `"Graph"`, `"Table"`, or `"Graph and Table"`.

```simtalk
MyChart.GraphTable := "Graph and Table"
```

---

### Height [SimTalk] - 3D charts
Sets the height of the viewing angle for 3D Chart Types of the Chart.

```simtalk
<Path>.Height:integer
```

You can specify a number between -50 and 50.

```simtalk
MyChart.ChartType := "3D Columns"
MyChart.Height := 45
```

---

### ImageQuality3D [SimTalk]
Sets the image quality with which the image of the Chart is shown in the Frame.

Applies if you assigned `true` to the attribute DisplayInFrame. The 3D Image Quality is only active in a 3D model.

```simtalk
<Path>.ImageQuality3D:string
```

You can specify:
- `"High quality"` — high resolution and improved image quality with bad performance.
- `"Balanced"` — medium resolution, a good compromise between image quality and performance.
- `"High performance"` — low resolution and bad image quality with better performance.

```simtalk
MyChart.ImageQuality3D := "Balanced"
```

---

### InputChannels [SimTalk]
Designates a table containing the definitions of all input channels of the Chart.

> **Note:** When you assign a table to InputChannels with the assignment operator `:=`, Plant Simulation deactivates inheritance. Any other kind of writing access does not deactivate inheritance.

```simtalk
<Path>.InputChannels:table
```

```simtalk
MyChart.InputChannels.delete
MyChart.InputChannels.insertList(1,1,table.copy)
MyChart.Inputchannels := MyDataTable.copy({0,0}..{*,*})
print MyChart.InputChannels[1,1]
```

---

### IsShown [SimTalk] - Chart
Activates (`true`) or deactivates (`false`) the display of the Chart.

The attribute is **watchable**.

```simtalk
<Path>.IsShown:boolean
```

```simtalk
MyChart.IsShown := false
```

---

### LabelFont [SimTalk]
LabelFont and its sub-attributes set the properties of the Labels of the axes in the Chart.

```simtalk
<Path>.LabelFont:string
<Path>.LabelFont.Size:integer
<Path>.LabelFont.Bold:boolean
<Path>.LabelFont.Italic:boolean
```

You can specify one of these fonts: Arial, Arial Narrow, Comic Sans MS, Courier New, Haettenschweiler, Lucida Console, MS UI Gothic, Tahoma, Times New Roman, Trebuchet MS, Verdana.

> **Note:** MS UI Gothic is intended for Japanese users. The English or German version of Microsoft Windows might not provide this font by default.

```simtalk
MyChart.LabelFont:= "Tahoma"
```

**Size** — the sub-attribute `Size`, of data type integer, sets the font size (1 to 8).

```simtalk
MyChart.LabelFont.Size := 4
```

**Bold** — sets if the Chart shows the labels in bold face (`true`) or not (`false`).

```simtalk
MyChart.LabelFont.Bold := true
```

**Italic** — sets if the Chart shows the labels in italics (`true`) or not (`false`).

```simtalk
MyChart.LabelFont.Italic := false
```

---

### LegendLocation [SimTalk]
Sets the type and the position of the Legend which the Chart shows.

```simtalk
<Path>.LegendLocation:string
```

```simtalk
MyChart.LegendLocation := "Left"
```

---

### Mode [SimTalk] - Chart
Sets the mode with which the Chart operates.

Applies to the setting **Category > Histogram**.

```simtalk
<Path>.Mode:string
```

You can specify:
- `"Sample"` mode updates the Chart regularly within a predefined period.
- `"Watch"` mode updates the Chart when the values to be displayed change.
- `"Plot"` mode updates the Chart whenever a simulation event takes place.

```simtalk
Mode.Sampler := "Plot"
```

---

### NullValue [SimTalk]
Sets the value the Chart takes to be as an undefined value.

When a point takes this value, the Chart does not display it. The default value is `-999999`.

```simtalk
<Path>.NullValue:real
```

```simtalk
MyChart.NullValue := -1
```

---

### NumIntervals [SimTalk]
Sets into how many intervals the Chart divides the frequency distribution for a Histogram.

```simtalk
<Path>.NumIntervals:integer
```

```simtalk
MyChart.NumIntervals := 8
```

---

### NumValues [SimTalk]
Sets the number of values which the Chart collects over time per channel.

Applies to the setting **Category > Plotter**. The more values the Chart collects, the more memory Plant Simulation uses.

```simtalk
<Path>.NumValues:integer
```

```simtalk
MyChart.NumValues := 5000
```

---

### Rotation [SimTalk] - Chart
Sets the angle of rotation for 3D Chart Types of the Chart in degrees.

```simtalk
<Path>.Rotation:integer
```

```simtalk
MyChart.ChartType := "3D Columns"
MyChart.Rotation := 90
```

---

### SampleInterval [SimTalk]
Sets the period of time between two successive sampling actions for the Chart for Sample mode.

```simtalk
<Path>.SampleInterval:time
```

```simtalk
MyChart.SampleInterval := 3600
MyChart.sampleInterval := 0 // Prevents the Chart from being updated.
                            // To update values, use the method 'update'.
```

---

### ScrollBar [SimTalk]
Sets if the Chart shows a scrollbar (`true`) or not (`false`).

Applies to the setting **Category > Plotter**.

```simtalk
<Path>.ScrollBar:boolean
```

```simtalk
MyChart.ScrollBar := true
MyChart.FeedRate := 4
```

---

### SizeInFrame [SimTalk]
Sets the Width and the Height of the Chart in length units when it is shown in the Frame.

```simtalk
<Path>.SizeInFrame:array[2]
```

You can assign a value of data type array with two values of data types integer.

```simtalk
MyChart.SizeInFrame := [6, 4.5]
```

---

### StepCurve [SimTalk]
Sets if the Chart creates a step curve (`true`) or not (`false`).

Applies to the **Category > Plotter**.

```simtalk
<Path>.StepCurve:boolean
```

```simtalk
MyChart.StepCurve := true
```

---

### StepSize [SimTalk]
Sets the width of the intervals into which the Chart divides the frequency distribution.

Applies to the **Category > Histogram**.

```simtalk
<Path>.StepSize:real
```

```simtalk
MyChart.StepSize := 5
```

---

### SubTitle [SimTalk]
Sets the Subtitle which the Chart displays in the Chart window.

```simtalk
<Path>.SubTitle:string
```

```simtalk
MyChart.SubTitle := "line 1, block"
```

---

### SubtitleFont [SimTalk]
SubtitleFont and its sub-attributes set the properties of the Subtitle in the Chart window.

```simtalk
<Path>.SubtitleFont:string
<Path>.SubtitleFont.Bold:boolean
<Path>.SubtitleFont.Italic:boolean
```

You can specify one of these fonts: Arial, Arial Narrow, Comic Sans MS, Courier New, Haettenschweiler, Lucida Console, MS UI Gothic, Tahoma, Times New Roman, Trebuchet MS, Verdana.

```simtalk
MyChart.SubtitleFont:= "Verdana"
```

**Bold** — sets if the Chart shows the subtitle in bold face (`true`) or not (`false`).

```simtalk
MyChart.SubtitleFont.Bold := true
```

**Italic** — sets if the Chart shows the subtitle in italics (`true`) or not (`false`).

```simtalk
MyChart.SubtitleFont.Italic := false
```

---

### TableFont [SimTalk]
TableFont and its sub-attributes set the properties of the labels which the Chart shows as a Table in the Chart window.

```simtalk
<Path>.TableFont:string
<Path>.TableFont.Size:integer
```

You can specify one of these fonts: Arial, Arial Narrow, Comic Sans MS, Courier New, Haettenschweiler, Lucida Console, MS UI Gothic, Tahoma, Times New Roman, Trebuchet MS, Verdana.

```simtalk
MyChart.TableFont:= "Tahoma"
```

**Size** — the sub-attribute `Size`, of data type integer, sets the font size (1 to 8).

```simtalk
MyChart.TableFont.Size := 4
```

---

### Title [SimTalk]
Sets the Title which the Chart shows in the Chart window.

```simtalk
<Path>.Title:string
```

```simtalk
MyChart.Title := "Engine assembly"
```

---

### TitleFont [SimTalk]
The attribute TitleFont and its sub-attributes set the properties of the Title in the Chart window.

```simtalk
<Path>.TitleFont:string
<Path>.TitleFont.Size:integer
<Path>.TitleFont.Bold:boolean
<Path>.TitleFont.Italic:boolean
```

You can specify one of these fonts: Arial, Arial Narrow, Comic Sans MS, Courier New, Haettenschweiler, Lucida Console, MS UI Gothic, Tahoma, Times New Roman, Trebuchet MS, Verdana.

```simtalk
MyChart.TitleFont:= "Trebuchet MS"
```

**Size** — the sub-attribute `Size`, of data type integer, sets the font size (1 to 8).

```simtalk
MyChart.TitleFont.Size := 4
```

**Bold** — sets if the Chart shows the title in bold face (`true`) or not (`false`).

```simtalk
MyChart.TitleFont.Bold := true
```

**Italic** — sets if the Chart shows the title in italics (`true`) or not (`false`).

```simtalk
MyChart.TitleFont.Italic := false
```

---

### UseInputChannels [SimTalk]
Sets if the Chart takes data it displays from input channels (`true`) or from a DataTable you defined (`false`).

```simtalk
<Path>.UseInputChannels:boolean
```

```simtalk
MyChart.UseInputChannels := true
```

---

### UseMetricPrefix [SimTalk]
Sets if the Chart shows a unit prefix on the y-axis for very great or very small values, for example `100K` instead of `100000` (`true`) or not (`false`).

The prefix stands for:

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

```simtalk
<Path>.UseMetricPrefix:boolean
```

```simtalk
MyChart.UseMetricPrefix := true
```

---

### XGrid [SimTalk]
Sets if the Chart shows the grid on the x-axis in the Chart window (`true`) or not (`false`).

```simtalk
<Path>.XGrid:boolean
```

```simtalk
MyChart.XGrid := true
```

---

### XGridlines [SimTalk]
Sets the number of grid lines that the Chart shows on the x-axis.

The Chart also shows a label for each grid line on the x-axis. If you are displaying a large number of data sets, it makes sense to enter a smaller number so that the labels can be shown completely.

If the number of grid lines is greater than the number of data sets on the x-axis, the Chart only shows as many grid lines as there are data sets. If the number of grid lines is smaller than the number of data sets, the Chart reduces the number of grid lines and labels.

> **Note:** If you select the **Category > XY-Graph**, the Chart only evaluates the Number if you also enter a fixed Range X, i.e., if you did not enter an asterisk `*`.

```simtalk
<Path>.XGridlines:integer
```

```simtalk
MyChart.XGridlines := 10
```

---

### XLabel [SimTalk]
Sets the label of the x-axis which the Chart shows in the Chart window.

Applies to the 3D chart types 3D Columns, 3D Wire Frame, and 3D Surface.

```simtalk
<Path>.XLabel:string
```

```simtalk
MyChart.XLabel := "Month"
```

---

### XLog [SimTalk]
Sets if the x-axis of the Chart uses a logarithmic representation (`true`) or not (`false`).

```simtalk
<Path>.XLog:boolean
```

```simtalk
MyChart.XLog := true
```

---

### XRange [SimTalk]
Sets the time span, in seconds of simulation time, which the Chart shows in the display.

Applies to the **Category > Plotter**.

```simtalk
<Path>.XRange:time
```

```simtalk
MyChart.XRange := 3600
```

---

### XScaleMax [SimTalk]
Sets the upper bound for scaling on the x-axis of the Chart.

```simtalk
<Path>.XScaleMax:integer
```

```simtalk
MyChart.XScaleMax := 3
```

---

### XScaleMin [SimTalk]
Sets the lower bound for scaling on the x-axis of the Chart.

```simtalk
<Path>.XScaleMin:integer
```

```simtalk
MyChart.XScaleMin := 2
```

---

### YGrid [SimTalk]
Sets if the Chart shows the grid on the y-axis in the Chart (`true`) or not (`false`).

```simtalk
<Path>.YGrid:boolean
```

```simtalk
MyChart.YGrid := false
```

---

### YGridLineInterval [SimTalk]
Sets the interval between the grid lines on the y-axis of the Chart.

YGridLineInterval sets the distance of the horizontal grid lines and the labels on the y-axis.

```simtalk
<Path>.YGridLineInterval:real
```

Specify `0` to make Plant Simulation determine a meaningful interval based on the displayed values.

```simtalk
MyChart.YGridLineInterval := 2
```

---

### YLabel [SimTalk]
Sets the label of the y-axis that the Chart shows in the Chart window.

Applies to the 3D chart types 3D Columns, 3D Wire Frame, and 3D Surface.

```simtalk
<Path>.YLabel:string
```

```simtalk
MyChart.YLabel := "Number of Trunks"
```

---

### YLog [SimTalk]
Activates logarithmic representation (`true`) of the y-axis of the Chart or deactivates it (`false`).

> **Note:** If you activate YLog, you also have to enter a value greater than 0, for example `0.1`, for the YScaleMin, so that Plant Simulation can display the scale logarithmically.

```simtalk
<Path>.YLog:boolean
```

```simtalk
MyChart.YLog := false
```

---

### YScaleMax [SimTalk]
Sets the upper bound of the range on the y-axis of the Chart.

```simtalk
<Path>.YScaleMax:integer
```

```simtalk
MyChart.YScaleMax := 1.5
```

---

### YScaleMin [SimTalk]
Sets the lower bound of the range on the y-axis of the Chart.

> **Note:** If you activate YLog, you also have to enter a value greater than 0, for example `0.1`, for the YScaleMin, so that Plant Simulation can display the scale logarithmically.

```simtalk
<Path>.YScaleMin:integer
```

```simtalk
MyChart.YScaleMin := 0.5
```

---

### ZLabel [SimTalk]
Sets the label of the z-axis that the Chart shows in the Chart window.

Applies to the 3D chart types 3D Columns, 3D Wire Frame, and 3D Surface.

```simtalk
<Path>.ZLabel:string
```

```simtalk
MyChart.ZLabel := "Number of Stacked Rows"
```

---

## Related

- **GanttChart [object]** — Use the object GanttChart for showing the chronological sequence of activities as bars on the time axis. The GanttChart visualizes parts on resources (the material flow objects, not the resource objects).
