# Methods of the Chart

The Chart provides the methods listed below, plus the Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the members of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show the members of the selected Instance.

## Syntax notation

An example of the Syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier and data type of each parameter) is listed in parentheses. `(Parameter:string)` designates a parameter of data type string. Instead of a constant, you can use a variable of the required type or a method that returns the required type.
- Optional parameters are listed within brackets, e.g. `[,Parameter:boolean]`.
- If a parameter has a default value, the signature shows it after `:=`, e.g. `:= false`.
- If the method has a return value, its data type appears after the arrow `→`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

---

## addObject

Adds the designated object to the Chart. Works the same as dragging the object onto the Chart.

- **Type:** Method
- **Syntax:** `<Path>.addObject(Object:object) → boolean`
- **Parameter:** `Object` (object) — the name of the object.
- **Return Value:** boolean

```simtalk
MyChart.addObject(MyExporter)
```

---

## copyBitmapToClipboard

Copies the contents of the display window of the Chart to the clipboard as a bitmap.

- **Type:** Method
- **Syntax:** `<Path>.copyBitmapToClipboard([Width:integer, Height:integer])`
- **Parameters:**
  - `Width` (integer, optional) — width of the bitmap in pixels.
  - `Height` (integer, optional) — height of the bitmap in pixels.

```simtalk
MyChart.copyBitmapToClipboard
MyChart.copyBitmapToClipboard(180,120)
```

---

## copyBitmapToFile

Copies the graphic of the Chart window to a file as a `.png` file.

- **Type:** Method
- **Syntax:** `<Path>.copyBitmapToFile(FileName:string, Width:integer, Height:integer)`
- **Parameters:**
  - `FileName` (string) — name of the file to which the `.png` is written.
  - `Width` (integer) — width of the bitmap.
  - `Height` (integer) — height of the bitmap.

```simtalk
.Models.MyChart.copyBitmapToFile("myChartImage",180,120)
```

---

## copyBitmapToIcon

Copies the graphic of the Chart window to an icon of the designated object.

- **Remarks:** Applies to the icon of the addressed instance, not the icon of the object class.
- **Type:** Method
- **Syntax:** `<Path>.copyBitmapToIcon(Destination:object, IconNumberOrName:integer/string[, Width:integer, Height:integer])`
- **Parameters:**
  - `Destination` (object) — the object into which the bitmap is copied.
  - `IconNumberOrName` (integer/string) — the icon; if no icon with that name/number exists, a new icon is created.
  - `Width` (integer, optional) — width of the bitmap.
  - `Height` (integer, optional) — height of the bitmap.
- If the optional parameters are omitted, the current width and height of the Chart are used.

```simtalk
MyChart.copyBitmapToIcon(Station1, -1)
```

---

## getAnnotations

Returns the contents of the table **Annotations** of the Chart.

- **Type:** Method
- **Syntax:** `<Path>.getAnnotations(AnnotationsToGet:table)`
- **Parameter:** `AnnotationsToGet` (table) — the table into which the annotations table is written.

```simtalk
MyChart.getAnnotations(MyAnnotationsTable)
```

---

## getColor

Returns the RGB value of the Color of an item in the Chart.

- **Type:** Method
- **Syntax:** `<Path>.getColor(ColorNo:integer[, byref Opacity:integer]) -> integer`
- **Parameters:**
  - `ColorNo` (integer) — the color of the element:
    - **Grid** (number **-3**) — color for the grid (bounding rectangles and grid lines).
    - **Background** (number **-2**) — color for the background of the graph.
    - **Desk** (number **-1**) — color for the area outside the grid's bounding rectangle.
    - **Text** (number **0**) — color for text.
    - **Colors** (numbers **1 through 14**) — predefined colors of the input channels.
  - `Opacity` (integer, optional, byref) — the opacity of the color.
- **Return Value:** integer

```simtalk
var rgb: integer := Chart.getColor(3)  -- reads the RGB color value of color 3
var opacity: integer
Chart2.setColor(3, Chart1.getColor(3, opacity), opacity)
-- copies the color value and the opacity of color 3 of Chart1 to Chart2
```

---

## getHTMLCode

Returns the chart graphic as HTML code in SVG format.

- **Type:** Method
- **Syntax:** `<Path>.getHTMLCode([Caption:string, Width:integer, Height:integer, inMM:boolean]) → string`
- **Parameters:**
  - `Caption` (string, optional) — desired caption of the graphic.
  - `Width` (integer, optional) — desired width of the graphic.
  - `Height` (integer, optional) — desired height of the graphic. If omitted, the Chart window's width/height are used.
  - `inMM` (boolean, optional) — whether width/height are in millimeters (`true`) or pixels (`false`).
- **Return Value:** string

```simtalk
print MyChart.getHTMLCode
```

---

## getLineStyle

Returns the line style settings of the Chart and writes them into the passed parameters.

- **Type:** Method
- **Syntax:** `<Path>.getLineStyle(ColorNumber:integer, byRef Style:string, byRef Weight:string, byRef Marker:string)`
- **Parameters:**
  - `ColorNumber` (integer) — the color (same numbering as `getColor`): Grid **-3**, Background **-2**, Desk **-1**, Text **0**, Colors **1–14**.
  - `Style` (string, byref) — the Line Style.
  - `Weight` (string, byref) — the Line Weight.
  - `Marker` (string, byref) — the Marker Type.

```simtalk
var s,w,m : string
MyChart.getLineStyle(1,s,w,m)
print s," ",w," ",m
```

---

## printChart

Prints the contents of the Chart window to the default printer.

- **Type:** Method
- **Syntax:** `<Path>.printChart([Width:real, Height:real, Orientation:integer])`
- **Parameters:**
  - `Width` (real, optional) — width of the printed Chart in millimeters.
  - `Height` (real, optional) — height of the printed Chart in millimeters.
  - `Orientation` (integer, optional) — `0` Default, `1` Landscape, `2` Portrait.

```simtalk
MyChart.printChart
MyChart.printChart(160,150,2)
```

---

## putValuesIntoTable

Writes the collected values of the Chart into the designated table.

- **Remarks:** Especially useful when Category > Histogram or Category > Plotter is selected, since the Chart collects values over time that are otherwise hard to access.
- **Type:** Method
- **Syntax:** `<Path>.putValuesIntoTable(DestinationTable:table)`
- **Parameter:** `DestinationTable` (table) — the destination table.

```simtalk
MyChart.putValuesIntoTable(MyDataTable)
```

---

## resetValues

Resets the collected values for Category > Histogram and Category > Plotter.

- **Remarks:** Deletes existing data and starts collecting anew. Useful for recording a weekly histogram or suppressing data collected during ramp-up.
- **Type:** Method
- **Syntax:** `<Path>.resetValues`

```simtalk
MyChart.resetValues
```

---

## setAnnotations

Sets the table **Annotations** of the Chart.

- **Remarks:** Plant Simulation always shows user-defined annotations in the foreground. Previously this was not the case when the Y-Axis showed time values. If you add your own annotations to such a Chart, Plant Simulation shows all annotations (including grid lines) in the foreground; in that case, hide the grid lines or set the grid color to a light color (e.g. light gray).
- **Type:** Method
- **Syntax:** `<Path>.setAnnotations(AnnotationsToSet:table)`
- **Parameter:** `AnnotationsToSet` (table) — the table that contains the annotations.

The table accepts the following columns:

- **Type** — the type of annotation:
  - `0` — Vertical Line
  - `1` — Horizontal Line
  - `2` — X-axis Label
  - `3` — Y-axis Label
  - `4` — Text
- **Value** — where the Chart displays the line:
  - Horizontal line / Y-axis label → the Y value.
  - Vertical line / X-axis label → the X value.
  - For a bar chart, value `3.5` places the X value between the third and fourth bar.
- **From** — starting point of the line (if empty, the Chart extends an existing line, allowing diagonal lines). For a horizontal line or text this is an X value; for a vertical line this is a Y value.
- **To** — end point of the line. If both `From` and `To` are empty, the line is drawn from left to right or top to bottom of the window. For a horizontal line this is an X value; for a vertical line this is a Y value.
- **Color** — the color number (defined on the Color tab).
- **Style** — line style (Type 0/1) or marker style (Type 4).
- **Text** — any text describing the line. Optional two-character prefix codes (pipe `|` + letter) control text position:
  - `|l` left inside edge
  - `|L` left outside edge
  - `|r` right inside edge
  - `|R` right outside edge
  - `|c` centered inside

### Line / marker style values

| Value | Line style | Marker style |
|------:|------------|--------------|
| 0 | thin solid line | text only (no marker) |
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
| 12 | none | solid downward triangle |
| 13 | none | small plus |
| 14 | none | small cross |
| 15 | none | small circle |
| 16 | none | small solid circle |
| 17 | none | small square |
| 18 | none | small solid square |
| 19 | none | small diamond |
| 20 | none | small solid diamond |
| 21 | none | small upward triangle |
| 22 | none | small solid upward triangle |
| 23 | none | small downward triangle |
| 24 | none | small solid downward triangle |
| 25 | none | large plus |
| 26 | none | large cross |
| 27 | none | large circle |
| 28 | none | large solid circle |
| 29 | none | large square |
| 30 | none | large solid square |
| 31 | none | large diamond |
| 32 | none | large solid diamond |
| 33 | none | large upward triangle |
| 34 | none | large solid upward triangle |
| 35 | none | large downward triangle |
| 36 | none | large solid downward triangle |
| 92 | none | arrow north |
| 93 | none | arrow north east |
| 94 | none | arrow east |
| 95 | none | arrow south east |
| 96 | none | arrow south |
| 97 | none | arrow south west |
| 98 | none | arrow west |
| 99 | none | arrow north west |

### Example

```simtalk
MyChart.Annotations := setAnnotations(myAnnotationTable)

-- Generation of a box plot for data with the descriptive statistics in tablefile 'StatisticData'
var AnnotationsTab:table
var Q0,Q25,Q50,Q75,Q100, yScaleMax, yScaleMin,delta, Mu:real
var cNo:integer
var ValName:string
Chart.active := false
AnnotationsTab := Chart.Annotations
AnnotationsTab.delete

yScaleMin := 1E300 -- all parts of the box plot must be visible
yScaleMax := 0
delta := 0.1 -- width of the column for the interval from the lower to the upper quartile (must be positive and < 0.5)
cNo := 3 -- blue, color for the intervals
Chart.title := "Box Plot"
for var ValNo := 1 to StatisticalData.xDim
    ValName := StatisticalData[ValNo, 0]
    Q0   := StatisticalData[ValNo, "Minimum"]
    Q25  := StatisticalData[ValNo, "Lower Quartile"]
    Q50  := StatisticalData[ValNo, "Median"]
    Q75  := StatisticalData[ValNo, "Upper Quartile"]
    Q100 := StatisticalData[ValNo, "Maximum"]
    Mu   := StatisticalData[ValNo, "Mean Value"]
    if Q0>Q25 OR Q25>Q50 OR Q50>Q75 OR Q75>Q100 OR Mu>Q100 OR Mu<Q0
        Promptmessage(to_str("Invalid statistical data ", when strLen(ValName) < 1 then to_str("in column ",valNo) else to_str("for '",ValName,"'"),"."))
    end
    yScaleMax := max(yScaleMax,Q100)
    yScaleMin := min(yScaleMin,Q0)

    AnnotationsTab.writeRow(1, AnnotationsTab.ydim + 1, 0, ValNo,Q25,Q0,cNo,0 )
    AnnotationsTab.writeRow(1, AnnotationsTab.ydim + 1, 0, ValNo,Q100,Q75,cNo,0 )
    AnnotationsTab.writeRow(1, AnnotationsTab.ydim + 1, 0, ValNo + delta,Q25,Q75,cNo,0 )
    AnnotationsTab.writeRow(1, AnnotationsTab.ydim + 1, 0, ValNo - delta,Q25,Q75,cNo,0 )
    AnnotationsTab.writeRow(1, AnnotationsTab.ydim + 1, 1, Q25, ValNo - delta, ValNo + delta,cNo,0 )
    AnnotationsTab.writeRow(1, AnnotationsTab.ydim + 1, 1, Q50, ValNo - delta, ValNo + delta,cNo,0 )
    AnnotationsTab.writeRow(1, AnnotationsTab.ydim + 1, 1, Q75, ValNo - delta, ValNo + delta,cNo,0 )

    AnnotationsTab.writeRow(1, AnnotationsTab.ydim + 1, 1, Q0, ValNo - delta, ValNo + delta,cNo,0 )
    AnnotationsTab.writeRow(1, AnnotationsTab.ydim + 1, 1, Q100, ValNo - delta, ValNo + delta,cNo,0 )
next

delta := (Q100 - Q0)/10
Chart.yScaleMax := Q100 + delta
Chart.yScaleMin := Q0 - delta

Chart.active := true
```

---

## setColor

Sets the Color of an item of the Chart.

- **Type:** Method
- **Syntax:** `<Path>.setColor(ColorNo:integer, RGB:integer[, Opacity:integer])`
- **Parameters:**
  - `ColorNo` (integer) — the color of the item: Grid **-3**, Background **-2**, Desk **-1**, Text **0**, Colors **1–14**.
  - `RGB` (integer) — red, green, and blue component of the color.
  - `Opacity` (integer, optional) — opacity; `0` entirely transparent, `255` completely opaque. Semi-transparent colors increase readability of Chart Type > Area.

```simtalk
MyChart.setColor(1, makeRGBValue(255,128,0))      -- sets the first color to orange
MyChart.setColor(2, makeRGBValue(255,0,0), 127))  -- sets the second color to a semi-transparent red
MyChart.setColor(-2, makeRGBValue(255,255,0))     -- sets the background color to yellow
```

---

## setLineStyle

Sets the line style settings of the Chart.

- **Type:** Method
- **Syntax:** `<Path>.setLineStyle(ColorNumber:integer, LineStyle:string[, LineWeight:string, Marker:string])`
- **Parameters:**
  - `ColorNumber` (integer) — the color: Grid **-3**, Background **-2**, Desk **-1**, Text **0**, Colors **1–14** (additional colors can be added).
  - `LineStyle` (string) — the Line Style. A shortened string (at least three characters) can be specified: e.g. `". ."` or `". . ."` instead of `". . . . . . . . ."` for a dotted line; `"_ _"` instead of `"_ _ _ _ _ _"` for a dashed line; minus signs can replace underscores, e.g. `"- -"`.
  - `LineWeight` (string, optional) — the Line Weight (kept if omitted).
  - `Marker` (string, optional) — the Marker Type.

```simtalk
MyChart.setLineStyle(1, "--", "Thick", "Diamond")
```

---

## setWindowPosition

Sets the position of the Chart window and its width and height.

- **Type:** Method
- **Syntax:** `<Path>.setWindowPosition(X:integer, Y:integer, Width:integer, Height:integer)`
- **Parameters:**
  - `X` (integer) — x-coordinate of the window.
  - `Y` (integer) — y-coordinate of the window.
  - `Width` (integer) — width.
  - `Height` (integer) — height.

```simtalk
MyChart.setWindowPosition(200,100,240,250)
```

---

## showPrintDialog

Opens the Print dialog of the Chart.

- **Type:** Method
- **Syntax:** `<Path>.showPrintDialog([Width:real, Height:real])`
- **Parameters:**
  - `Width` (real, optional) — width of the printed Chart in millimeters.
  - `Height` (real, optional) — height of the printed Chart in millimeters.

```simtalk
MyChart.showPrintDialog
MyChart.showPrintDialog(140,120)
```

---

## update

Refreshes the displayed Chart with the current values.

- **Remarks:** If the Chart is a Plotter in Sample mode, `update` additionally sets a new data point (the Chart samples once more), even when the Chart is closed (in which case it returns `false`).
- **Type:** Method
- **Syntax:** `<Path>.update -> boolean`
- **Return Value:** boolean — `true` if the Chart is open, `false` if it is closed.

```simtalk
MyChart.update
```

---

# Read-Only Attributes of the Chart

The Chart provides the Read-Only Attributes of All Objects.

You can query the values of read-only attributes but cannot set them, since Plant Simulation computes the value at the point in time when you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (e.g. the Statistics tab).
