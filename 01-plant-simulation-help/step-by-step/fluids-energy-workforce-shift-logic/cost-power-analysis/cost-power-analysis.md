# Cost and Power Analysis

This section covers two topics from the Plant Simulation Help:

1. Simulating the accrued costs of the machines
2. Simulating the power consumption in your facility

---

## Simulating the Accrued Costs of the Machines

You can simulate the accrued costs of the machines, which you entered on the tab **Costs**, with the object **CostAnalyzer**.

With the object **CostAnalyzer** you can analyze the costs that accrue for the active material flow objects, for the **Part**, and for the **Container** in your plant. You can enter the respective costs on the tab **Costs** of the material flow objects, and on the tab **Costs** of the Part and of the Container.

The workflow demonstrates how to:

- Specify the Costs of the Conveyors
- Specify the Costs of the Stations and the Parts
- Configure the Costs Report
- View the Costs Report

### Specify the Costs of the Conveyors

Enter the costs that the Conveyors create. To show how the costs from sub-Frames are collected and displayed, part of the model is modeled in a sub-Frame named `SubFrame`.

- For **Conveyor1** costs are typed in.
- For the **Conveyor in the sub-Frame** values are typed in.
- For the **Conveyor connecting the AssemblyStation with the Drain** values are typed in.

### Specify the Costs of the Stations and the Parts

Enter the costs that the Stations create. To show how the costs from sub-Frames are collected and displayed, part of the model is modeled in the sub-Frame named `SubFrame`.

To show the content of the sub-Frame instead of its icon, activate **Show Content** on the tab **Graphics** of the sub-Frame (in 3D).

- For **Station1**: costs are entered, plus a constant processing time of 10 minutes.
- For the **Station in the sub-Frame**: costs are entered, plus a constant processing time of 15 minutes.
- For the **AssemblyStation**: costs are entered.
- For the part types, costs are entered for the **Part** and for **MyMountingPart**.
- The **Sources** named `SourceMainParts` and `SourceMountingParts` are configured by typing in a creation interval each.

> **Note:** Only type the name of the mounting part into the Assembly Table, not the entire path.

### Configure the Costs Report

You cannot configure the CostAnalyzer as such. To show the results of the cost analysis, drag the **CostAnalyzer** from the Frame onto the icon of the **HtmlReport** and drop it there.

- If the Content of the HtmlReport is inherited, the data of the CostAnalyzer replaces the pre-defined content of the HtmlReport. Plant Simulation opens the display window of the HtmlReport automatically.
- If the Content of the HtmlReport is not inherited, Plant Simulation appends the data of the CostAnalyzer to the pre-defined content of the HtmlReport. Plant Simulation opens the display window of the HtmlReport automatically.

You can also drag the object **CostAnalyzer** into the open window of the HtmlReport and drop it there (for example below the heading *Statistics*). Then the HtmlReport also shows the pre-defined *General Information* when you click **Show Report**.

This adds the following instruction to the HtmlReport:

```html
# Statistics
## CostAnalyzer
[CostAnalyzer]
```

### View the Costs Report

The HtmlReport shows the costs report with the settings that were defined.

- **Investment Costs table:** shows the summed-up investment costs of the Frame in the unavailable cells. Below it lists the investment costs, the depreciation period, and the operating costs of the individual objects inserted into this Frame, row by row.

  You can also query the investment costs with the method `putInvestmentCostsIntoTable`.

- **Piece Costs table:** shows the summed-up piece costs of the used MU type (in this case the Part):
  - **MU Type** (part type): the name of the parts when they arrive in the Drain. When parts change their name during the simulation (for example during different production phases), the costs are assigned to the final product.
  - **Piece costs** (sum of material costs, accrued costs, and general costs): 8.32 €.
  - **Material costs** (accruing when a new part enters production): 8.00 €.
  - **Accrued costs** (assigned to the part while it is processed on the material flow object): 0.17 €.
  - **General costs** (accruing when a material object is empty during the simulation): 0.15 €. These costs are distributed across the part types that were processed by the material flow object.
  - **Throughput**: number of parts processed and moved through the production line (10,650 parts in this case).
  - **Work in process**: number of parts currently passing through the production process (6 parts in this case).

Click **Investment Costs** in the dialog of the CostAnalyzer to show the investment costs, or query them with `putInvestmentCostsIntoTable`.

Click **Piece Costs** in the dialog of the CostAnalyzer to show the piece costs, or query them with `putPieceCostsIntoTable`.

---

## Simulating the Power Consumption in Your Facility

Plant Simulation provides features to keep track of energy consumption in the face of rising energy costs and the depletion of energy resources.

The features on the tab **Energy** provide these evaluations regarding energy consumption during the production process in the plant:

- Power consumption per machine
- Total power consumption for all objects contained within a Frame

The workflow demonstrates how to:

- Configure the Processing Stations and the Conveyor
- Configure the ShiftCalendar
- Check the Power Consumption in the Dialogs of the Objects
- Check the Power Consumption in the Statistics Report
- Check the Power Consumption in the Chart

Most of the material flow objects use their default settings; only energy-related settings are entered and failures are defined for some objects.

### Configure the Processing Stations and the Conveyor

Insert the following stations to simulate parts moving through the factory:

- **Source**: feeds the parts into the plant. Default settings unchanged.
- **Station** (first machine): processes the parts for 1 minute each. The kilowatts used in each possible state are entered, along with the times required for switching from one energy state to another.
- **Station1** (second machine): processes the parts for 2 minutes each. Kilowatts per state and switching times are entered.
- **Conveyor**: transports the parts from Station1 to the ParallelStation. Kilowatts per state and switching times are entered. The length-oriented object Conveyor provides fewer energy settings than the point-oriented objects Station and ParallelStation.
- **ParallelStation** (third machine): processes the parts for 1 minute each. Kilowatts per state and switching times are entered.
- **Drain**: removes the parts from the factory. Default settings unchanged.
- **Charts**: display a resource statistics chart and an energy statistics chart for the selected objects.

Failure profiles with the entered settings are also defined for Station1 and the Conveyor to simulate a real situation.

### Configure the ShiftCalendar

Insert a **ShiftCalendar** that controls the hours during which people and machines work in the factory. The default shift times are unchanged; only the material flow objects are entered.

To do so, hold down **Shift** and drag a marquee over the objects. Then drag the selected objects onto the ShiftCalendar and drop them there.

### Check the Power Consumption in the Dialogs of the Objects

View the energy consumption values collected by the objects in their dialogs:

1. Double-click the icon of the respective object and click the tab **Statistics**.
2. Click **Energy Statistics** to view more detailed values about the different portions of energy consumption.

### Check the Power Consumption in the Statistics Report

Check the power consumption of the material flow objects in the simulation model in the **StatisticsReport**.

To view the total energy consumption and the portions of the different energy states, select **Energy Statistics** in the drop-down list of the Statistics Report. The values are described under *Energy Statistics — Energy Statistics*.

> **Note:** The energy states of the material flow objects differ from the resource states with the same name. The values for the resource states refer to the statistics collection period, while the values for the energy states refer to the total energy consumption.

The material flow objects also show these values on the tab **Statistics** and in the dialog opened by clicking **Energy Statistics**.

### Check the Power Consumption in the Chart

View the energy consumption values collected by the objects in a **Chart**:

1. Select the objects to display in the Chart.
2. Drag them onto the Chart.
3. Select the **Statistics Type > Energy Statistics** in the dialog that opens and click **OK**.
