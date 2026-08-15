# Attributes of the SankeyDiagram

The SankeyDiagram provides:

- The attributes listed below.
- The **Attributes of All Objects**.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

## Accessing Attributes

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows or by assigning values to the respective attributes.

### Examples

To query the value of a read-only attribute:

```simtalk
print MySankeyDiagram.UUID
```

To set the value of an attribute:

```simtalk
MySankeyDiagram.IsShown := true
```

To get the value of an attribute:

```simtalk
print MySankeyDiagram.IsShown
posit := Station.Cont.XPos
```

---

## CollectData [SimTalk] - SankeyDiagram

Sets if the SankeyDiagram designated by `<Path>` collects data (`true`) or does not collect data (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.CollectData:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**

```simtalk
MySankeyDiagram.CollectData := true
```

**See also:** Collect Data [check box] - SankeyDiagram, CollectData [SimTalk] - SankeyDiagram

---

## Color [SimTalk] - SankeyDiagram

Sets the color which Plant Simulation uses for displaying the Sankey flows of the parts and Workers of the SankeyDiagram designated by `<Path>` in the Frame.

**Remarks:** Set the RGB values of the color with the method `makeRGBValue`.

- **Type:** Attribute
- **Syntax:** `<Path>.Color:integer`
- **Assignment Value:** You can assign a value of data type integer.

**Example:**

```simtalk
MySankeyDiagram.Color := makeRGBValue(255,0,0)
```

**SimTalk:** makeRGBValue [SimTalk]

**See also:** Color [SankeyDiagram], Color [SimTalk] - SankeyDiagram

---

## IsShown [SimTalk] - SankeyDiagram

Activates (`true`) or deactivates (`false`) the display of the SankeyDiagram designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.IsShown:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**

```simtalk
MySankeyDiagram.IsShown := false
```

**See also:** Show Diagram, IsShown [SimTalk] - SankeyDiagram

---

## MaximumWidth [SimTalk]

Sets the maximum width with which Plant Simulation visualizes the Sankey flows of the parts and Workers of the SankeyDiagram designated by `<Path>` in the Frame.

- **Type:** Attribute
- **Syntax:** `<Path>.MaximumWidth:length`
- **Assignment Value:** You can assign a value of data type length.

**Example:**

```simtalk
MySankeyDiagram.MaximumWidth := 1.0 -- meters
```

**See also:** Maximum Width [SankeyDiagram], MaximumWidth [SimTalk]

---

## Objects [SimTalk] - SankeyDiagram

Sets the objects, i.e., the Parts or Workers whose Sankey flows the SankeyDiagram designated by `<Path>` visualizes in the Frame.

- **Type:** Attribute
- **Syntax:** `<Path>.Objects:array`
- **Assignment Value:** You can assign a value of data type array.

**Example:**

```simtalk
MySankeyDiagram.Objects := [.Resources.Worker]         // all Workers of this class
MySankeyDiagram.Objects := [.Resources.WorkerPool]     // all WorkerPool classes
MySankeyDiagram.Objects := [.Models.Model.WorkerPool]  // all Workers of the WorkerPool in the Frame named Frame
MySankeyDiagram.Objects := [.Resources.Worker:1]       // the Worker with the number 1
```

**See also:** Objects, tab, CostAnalyzer, CostAnalyzer

> Use the object **CostAnalyzer** for analyzing costs that the individual machines and the Worker cause. The CostAnalyzer computes the costs that accrue for the material flow objects while processing the parts in the facility.
