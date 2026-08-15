# Attributes of the GanttChart

The GanttChart provides:

- The attributes listed below.
- The Attributes of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance.

You can set and get attribute values either with check boxes, text boxes, and drop-down lists in dialog windows, or by assigning values in SimTalk.

To query the value of a read-only attribute:

```simtalk
print MyGanttChart.UUID
```

To set the value of an attribute:

```simtalk
MyGanttChart.IsShown := true
```

To get the value of an attribute:

```simtalk
print MyGanttChart.IsShown
posit := Station.Cont.XPos
```

---

## CollectData [SimTalk] - GanttChart

Sets if the GanttChart designated by `<Path>` collects data (`true`) or does not collect data (`false`).

**Remarks**

You cannot use `setData` and automatically collect the data simultaneously. When you assign `true` to `CollectData`, do not call the method `setData`.

**Type:** Attribute

**Syntax**

```
<Path>.CollectData:boolean
```

**Assignment Value:** You can assign a value of data type boolean.

**Example**

```simtalk
MyGanttChart.CollectData := true
```

**See also:** Collect Data [check box] - GanttChart, CollectData [SimTalk] - GanttChart

---

## EnableVisualTracking [SimTalk]

Activates (`true`) or deactivates (`false`) visual tracking of parts or resources in the GanttChart designated by `<Path>`.

**Type:** Attribute

**Syntax**

```
<Path>.EnableVisualTracking:boolean
```

**Assignment Value:** You can assign a value of data type boolean.

**Example**

```simtalk
MyGanttChart.EnableVisualTracking := true
```

**See also:** Show Chart [button] - GanttChart, EnableVisualTracking [SimTalk]

---

## IsShown [SimTalk] - GanttChart

Activates (`true`) or deactivates (`false`) the display of the GanttChart designated by `<Path>`.

**Type:** Attribute

**Syntax**

```
<Path>.IsShown:boolean
```

**Assignment Value:** You can assign a value of data type boolean.

**Example**

```simtalk
MyGanttChart.IsShown := false
```

**See also:** Show Chart [button] - GanttChart, IsShown [SimTalk] - GanttChart

---

## NumVisibleBars [SimTalk]

Sets the maximum number of visible bars in the GanttChart designated by `<Path>`.

**Remarks**

The default setting is `100000`. If this number is exceeded, older bars will not be shown any more. You can reduce this number if performance is impaired.

**Type:** Attribute

**Syntax**

```
<Path>.NumVisibleBars:integer
```

**Assignment Value:** You can assign a value of data type integer.

**Example**

```simtalk
MyGanttChart.NumVisibleBars := 8000
```

**See also:** Show Chart [button] - GanttChart, NumVisibleBars [SimTalk]

---

## Parts [SimTalk]

Sets the parts, i.e., the MUs that the GanttChart designated by `<Path>` visualizes.

**Remarks**

You can watch classes of parts or you can watch individual instances of parts.

**Type:** Attribute

**Syntax**

```
<Path>.Parts:array
```

**Assignment Value:** You can assign a value of data type array.

**Example**

```simtalk
MyGanttChart.Parts := [*.MUs.Entity]   // all parts of this class
MyGanttChart.Parts := [*.MUs.Entity:1] // the part with the number 1
```

**See also:** Tab Parts [GanttChart], Parts [SimTalk]

---

## Resources [SimTalk] - GanttChart

Sets the resources, i.e., the material flow objects that the GanttChart designated by `<Path>` visualizes.

**Remarks**

You can watch classes of resources or you can watch individual instances of resources.

**Type:** Attribute

**Syntax**

```
<Path>.Resources:array
```

**Assignment Value:** You can assign a value of data type array.

**Example**

```simtalk
MyGanttChart.Resources := [Source, Station, Station1, Drain]
```

**See also:** Tab Resources [GanttChart], Resources [SimTalk] - GanttChart

---

## ShowBarText [SimTalk]

Sets if the GanttChart designated by `<Path>` shows the part name as text on the Gantt bar (`true`) or not (`false`).

**Type:** Attribute

**Syntax**

```
<Path>.ShowBarText:boolean
```

**Assignment Value:** You can assign a value of data type boolean.

**Example**

```simtalk
MyGanttChart.ShowBarText := true
```

**See also:** Show Bar Text [check box], ShowBarText [SimTalk]

---

## ShowPartView [SimTalk]

Sets if the GanttChart designated by `<Path>` shows the resources in the Resource View (`false`) or the parts in the Part View (`true`).

**Type:** Attribute

**Syntax**

```
<Path>.ShowPartView:boolean
```

**Assignment Value:** You can assign a value of data type boolean.

**Example**

```simtalk
MyGanttChart.ShowPartView := true
```

**See also:** Show Chart [button] - GanttChart, ShowPartView [SimTalk]

---

## ShowResourceLabels [SimTalk]

Sets if the GanttChart designated by `<Path>` shows the labels of the resources (`true`) or their names (`false`).

**Type:** Attribute

**Syntax**

```
<Path>.ShowResourceLabels:boolean
```

**Assignment Value:** You can assign a value of data type boolean.

**Example**

```simtalk
MyGanttChart.ShowResourceLabels := true
```

**See also:** Show Resource Labels [check box], ShowResourceLabels [SimTalk]

---

## ShowResourceStates [SimTalk]

Sets if the GanttChart designated by `<Path>` shows the states of the resources as color of the bars (`true`) or not (`false`).

**Type:** Attribute

**Assignment Value:** You can assign a value of data type boolean.

**Example**

```simtalk
MyGanttChart.setLanes(MyLanesTable)
MyGanttChart.ShowResourceStates := true
```

**See also:** Show Resource States [check box], States of the Material Flow Objects, ShowResourceStates [SimTalk]

---

## TimeScale [SimTalk]

Sets the time scale of the GanttChart designated by `<Path>`. Plant Simulation applies this value when opening the GanttChart.

**Remarks**

The unit of the time scale is logical pixels per second. For a time scale of `0.5`, Plant Simulation shows a Gantt event with a duration of 60 seconds with a bar of a length of 30 logical pixels.

**Type:** Attribute

**Syntax**

```
<Path>.TimeScale:integer
```

**Assignment Value:** You can assign a value of data type real. Specify `0` to use the default time scaling.

**Example**

```simtalk
MyGanttChart.TimeScale := 2.5
```

**See also:** Show Chart [button] - GanttChart, SankeyDiagram
