# Methods of the GanttChart

The GanttChart provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

## Syntax line conventions

An example of the Syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. `(Parameter:string)`, for example, designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

---

## exportChart [SimTalk]

Exports the GanttChart designated by `<Path>` to an HTML file.

- **Type:** Method
- **Syntax:** `<Path>.exportChart(FileName:string[, TimeScale:real])`

**Parameters**

- `FileName` (data type `table`) designates the table into which Plant Simulation writes the HTML file.
- `TimeScale` (optional, data type `real`) designates the time scale. The time scale is shown in pixels per second.
  - For the value of `0.5`, a Gantt event that has a duration of 60 seconds is displayed by a bar of a length of 30 pixels.

**Examples**

```
MyGanttChart.exportChart("MyExportedGanttChart.html", 0.5) 
// exports the file to the folder in which the simulation model is located
MyGanttChart.exportChart("D:\MyModels\MyExportedGanttChart.html") 
// exports the file to the designated folder
```

---

## getData [SimTalk]

Returns the data which the GanttChart designated by `<Path>` shows and writes it to a table.

- **Type:** Method
- **Syntax:** `<Path>.getData(DataTable:table)`

**Parameter**

- `DataTable` (data type `table`) designates the table into which Plant Simulation writes data that the GanttChart shows.

The format of the data table is described under `setData`.

**Example**

```
MyGanttChart.getData(MyGanttDataTable)
```

---

## getHTMLCode [SimTalk] - GanttChart

Returns the chart graphic as HTML code in the format SVG of the GanttChart designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.getHTMLCode([Caption:string, Scale:real]) → string`

**Parameters**

- `Caption` (optional, data type `string`) designates the desired caption of the graphic. Specify the caption to show the GanttChart with this caption.
- `Scale` (optional, data type `real`) designates the scaling of the graphic.

**Return Value**

The return value has the data type `string`.

**Example**

```
HtmlReport.content := "<<" + GanttChart.getHtmlCode("Test (half size)", 
0.5) + ">>"
HtmlReport.show
```

**See also:** Display a HtmlReport

---

## getLanes [SimTalk]

Returns the lanes which you defined for the GanttChart designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.getLanes(TableToWrite:table)`

**Parameter**

- `TableToWrite` (data type `table`) designates the table into which Plant Simulation writes lanes of the GanttChart.

A lane is defined by the settings `Top` and `Height`. Both have the data type `integer`.

**Example**

```
MyGanttChart.getLanes(MyLanesTable)
```

**See also:** `setLanes`, Edit Lanes

---

## setData [SimTalk]

Sets the data which the GanttChart designated by `<Path>` is going to show.

> **Remarks:** You cannot manually set the data and automatically collect the data simultaneously. When you use the method `setData`, set `CollectData` to `false`.

- **Type:** Method
- **Syntax:** `<Path>.setData(DataTable:table)`

**Parameter**

`DataTable` (data type `table`) designates the table that contains the data which the GanttChart is going to show.

The table has eight columns. The first three columns have to contain data. Of the second three columns, one column at least has to contain data. Each row in the table describes a Gantt event that is visualized as a bar.

- **Start Date** denotes the start date of the event.
- **End Date** denotes the end date of the event.
- **Resource** — depending on the data of the following three columns, Resource either denotes the resource that takes the specified state, or the specified part, or both. You can type in the path of the resource in the Frame, or you can drag the resource onto the respective cell and drop it there, or enter free resource text.
- **Resource State** denotes the state in which the Resource is. You can enter one of these states: `Working`, `Setting-up`, `Waiting`, `Blocked`, `PoweringUpDown`, `Failed`, `Stopped`, `Paused`, or `Unplanned`. The value does not have to correspond to any existing material flow instance.
- **Part** denotes the part that is processed by the resource. Type in the path of the parts class, a colon, and the number of the part instance. You can, for example, enter `.MUs.Part:1`. Instead, you can also enter free part text.
- **Part Name** is any string that the GanttChart shows as a Tooltip.
- **Lane** denotes the lane of the Gantt event.
- **Color** denotes the color of the Gantt event. If you do not enter a color, Plant Simulation automatically assigns a color, in Resource View according to the part, in Part View according to the resource.

**Example**

```
MyGanttChart.setData(MyGanttData)
```

**See also:** `getData`, `setLanes`, Show Chart [button] - GanttChart, CollectData [SimTalk] - GanttChart

---

## setLanes [SimTalk]

Sets the lanes which the GanttChart designated by `<Path>` is to show.

- **Type:** Method
- **Syntax:** `<Path>.setLanes(TableToRead:table)`

**Parameter**

- `TableToRead` (data type `table`) designates the table which contains the lanes that the GanttChart shows.

A lane is defined by the settings `Top` and `Height`. Both have the data type `integer`.

**Example**

```
MyGanttChart.setLanes(MyLanesTable)
MyGanttChart.ShowResourceStates := true
```

**See also:** `getLanes`, Edit Lanes, Show Chart [button] - GanttChart

---

## update [SimTalk] - GanttChart

Refreshes the displayed GanttChart designated by `<Path>` with the current values.

- **Type:** Method
- **Syntax:** `Path.update`

**Example**

```
MyGanttChart.update
```

---

# Read-Only Attributes of the GanttChart

The GanttChart provides the _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
