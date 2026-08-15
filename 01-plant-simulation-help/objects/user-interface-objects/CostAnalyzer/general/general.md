# CostAnalyzer (General)

## Objects [SimTalk] - SankeyDiagram

Sets the objects (Parts or Workers) whose Sankey flows the `SankeyDiagram` designated by `<Path>` visualizes in the Frame.

**Type:** Attribute  
**Syntax:** `<Path>.Objects:array`

**Assignment Value:** You can assign a value of data type `array`.

**Example**

```simtalk
MySankeyDiagram.Objects := [.Resources.Worker]         // all Workers of this class
MySankeyDiagram.Objects := [.Resources.WorkerPool]     // all WorkerPool classes
MySankeyDiagram.Objects := [.Models.Model.WorkerPool]  // all Workers of the WorkerPool in the Frame named Frame
MySankeyDiagram.Objects := [.Resources.Worker:1]       // the Worker with the number 1
```

**See also:** Objects, tab

---

## CostAnalyzer

Use the object **CostAnalyzer** for analyzing the costs that the individual machines and the Workers cause. The CostAnalyzer computes the costs that accrue for the material flow objects while processing the parts in the facility.

### Description

The CostAnalyzer also computes the summed-up investment costs of the objects. You cannot configure the CostAnalyzer as such.

To show the results of the cost analysis, drag the CostAnalyzer from the Frame onto the icon of the **HtmlReport** and drop it there.

- If the Content of the HtmlReport is **inherited**, the data of the CostAnalyzer replaces the pre-defined content of the HtmlReport. Plant Simulation opens the display window of the HtmlReport automatically.
- If the Content of the HtmlReport is **not inherited**, Plant Simulation appends the data of the CostAnalyzer to the pre-defined content of the HtmlReport. Plant Simulation opens the display window of the HtmlReport automatically.

To show the results of the analysis, you can also drag the object CostAnalyzer into the open window of the HtmlReport and drop it there, for example below the heading *Statistics*. Then click **Show Report**.

Type in the respective costs on the **tab Costs** of the active material flow objects and the tab Costs of the Part and of the Container.

### Note

At the moment you can only set if the CostAnalyzer collects data or not. We do not provide any other configuration settings. To show a tooltip with information about the CostAnalyzer, hover with the mouse over it.

To change the length of the graphic and the anchor points of the CostAnalyzer, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

### Add the Object to the Simulation Model

To add the object CostAnalyzer to your simulation model, click **Manage Class Library > Basic Objects > UserInterface > CostAnalyzer** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog *Examples Collection*, and click **Open Model**.

**See also:**
- Simulate the Accrued Costs of the Machines
- How the CostAnalyzer Assigns Costs to Part Types
- Costs Shown in the Costs Report

---

## How the CostAnalyzer Assigns Costs to Part Types

The material flow objects generate costs during the simulation which result from the total investment costs and the total operating costs per time. These costs are distributed as accrued costs to the parts which the material flow objects process.

### Remarks

- If no parts are located on the material flow objects, the costs are allocated to the respective material flow object as **general costs**.
- If the CostAnalyzer computes the result, these general costs are distributed across the part types which the material flow object processed during the simulation. Parts with the same name are allocated to the same part type (MU Type). Plant Simulation uses the name that the part has when it arrives at the Drain.

### Note

For the **Work in process** the final production costs are not known. For this reason they only contribute with **50 %** to the production costs. The assumption is that the work-in-process parts have covered about half of their production process on average.

Costs for parts which are currently passing through the production process are not precise. Piece costs are only then meaningful if the **Throughput** is considerably higher than the **Work in process**.

Not all material flow objects proceed the same during this process:

- The **AssemblyStation** assigns the costs to the main part. Costs which accrued for the mounting parts until then are transferred to the main part.
- The **Conveyor** assigns the costs proportionately according to the length of the part.
- The **DismantleStation** assigns the costs to the main part.
- The **ParallelStation** distributes the costs evenly across its processing places.
- The **Container** distributes the accrued costs evenly across the storage places if **Distribute costs** is activated.

In addition, material costs accrue during the simulation when a new part enters the production process.

**See also:**
- Depreciation Period [text box]
- Investment Costs [text box]
- Investment Costs per Length [text box]
- Operating Costs [text box]
- Operating Costs per Length [text box]
- Material Costs per Piece [text box]
- Distribute Costs [check box]

---

## Costs Shown in the Costs Report

The HtmlReport shows the tables **Investment Costs** and **Piece Costs** of the cost analysis by default.

### Remarks

You cannot configure the object CostAnalyzer as such. To show the results of the analysis, drag the object CostAnalyzer into the open window of the HtmlReport and drop it there, for example below the heading *Statistics*. Then click **Show Report**.

Compare **View the Costs Report** in the Step-by-Step help.

### Investment Costs

The table **Investment Costs** shows the investment costs, the depreciation period, and the operating costs of the material flow objects inserted into the model, hierarchically structured.

**Note:** The HtmlReport shows the investment costs statically, i.e., the values do not change during the simulation run.

- For **Frames** in the hierarchy the table shows the summed-up investment costs. These costs are highlighted in light gray. The first row shows the summed-up investment costs of the entire model.
- For **sub-Frames** in the hierarchy the table shows the summed-up investment costs as well. These costs are highlighted in light gray. The first row shows the summed-up investment costs of this sub-Frame.

**SimTalk:**
- `putInvestmentCostsIntoTable` [SimTalk]
- `getInvestmentCostsTable` [SimTalk]

### Piece Costs

The table **Piece Costs** shows the costs which accrued for the part types in the individual rows during the simulation.

- **MU Type** (part type) designates the name of the parts when they arrive in the Drain. When parts change their name during the simulation run, for example during the different production phases, the costs are assigned to the final product.
- **Material costs** designate the costs which accrue during the simulation when a new part enters the production.
- **Accrued costs** designate the costs which are assigned to the part while it is processed on the material flow object.
- **General costs** designate the costs which accrue when a material object is empty during the simulation. These costs are distributed across the part types which were processed by the material flow object.
- **Piece costs** is the sum of the material costs, the accrued costs, and the general costs.
- **Throughput** designates the number of parts which were processed and moved through the production line.
- **Work in process** designates the number of parts which are currently passing through the production process. These parts only contribute by half for computing the piece costs.

All costs are averaged per piece.

**Note:** For the **Work in process** the final production costs are not known. For this reason they only contribute with **50 %** to the production costs. The assumption is that the work-in-process parts have covered about half of their production process on average. Costs for parts which are currently passing through the production process are not precise. Piece costs are only then meaningful if the **Throughput** is considerably higher than the **Work in process**.

**SimTalk:**
- `getPieceCostsTable` [SimTalk]
- `putPieceCostsIntoTable` [SimTalk]

**See also:**
- Depreciation Period [text box]
- Investment Costs [text box]
- Investment Costs per Length [text box]
- Operating Costs [text box]
- Operating Costs per Length [text box]
- Material Costs per Piece [text box]
- Distribute Costs [check box]

---

## Dialog Box of the CostAnalyzer

Double-click the icon of the CostAnalyzer to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under **Dialog Items of the Objects**.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

**See also:**
- Collect Data [check box] - CostAnalyzer
- Investment Costs [button]
- Piece Costs [button]

---

## Collect Data [check box] - CostAnalyzer

To make the CostAnalyzer collect data during the simulation run, select this check box. To deactivate data collection, clear the check box.

**SimTalk:** `CollectData` [SimTalk] - CostAnalyzer

---

## Investment Costs [button]

To open a list, which contains the investment costs which the CostAnalyzer computed, click this button.

**SimTalk:** `getInvestmentCostsTable` [SimTalk]

**See also:** View the Costs Report

---

## Piece Costs [button]

To open a list, which contains the piece costs which the CostAnalyzer computed, click this button.

**SimTalk:** `getPieceCostsTable` [SimTalk]

**See also:** View the Costs Report

---

## Tab User-defined

Define your own attributes as described under the **Tab User-defined**.

---

## Navigate Menu

The commands are described under the **Navigate Menu**.

---

## View Menu

The commands are described under the **View Menu**.

**SimTalk:** `updateDialog` [SimTalk]

---

## Tools Menu

The Tools Menu provides commands to access its functions.

- Edit Controls
- Edit Observers

**See also:** Tools Menu [general description]

---

## Help Menu

The commands are described under the **Help Menu**.

---

## Methods of the CostAnalyzer

The CostAnalyzer provides:

- The methods listed in the table of contents to the left.
- The **Methods of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].
