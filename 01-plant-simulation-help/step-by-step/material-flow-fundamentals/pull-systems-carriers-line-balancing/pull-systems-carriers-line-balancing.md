# Pull Systems, Carriers, and Line Balancing

This document summarizes the Plant Simulation help topics covering pull material flow (supermarket/order-controlled stores), stacking parts, workpiece carriers, and production line balancing.

---

## Using the Store as Supermarket

The Store can work as a **supermarket** to represent a *pulling* material flow. In this example the Store orders two different part types from a Source. Only when the stock of these parts falls below a certain value does the Source start producing them.

To enable this behavior:

- Activate **Supermarket** in the Store.
- Select **MU Selection > Order Controlled** in the Source.

The Store then sends these parts on to an AssemblyStation, which loads them onto the respective pallets and moves them on.

The tutorial demonstrates how to:

- Model the pulling material flow.
- Configure the Store as Supermarket and the Source as Order-Controlled.
- Show the amount of waiting parts and the amount of orders.

### Model the Pulling Material Flow

When the Store works as supermarket, we model the pulling material flow. To model it:

- Insert the material flow objects so that they match the figure (Store, SourceParts, AssemblyStation, pallets, etc.).
- Duplicate the **Part** and the **Container** twice each. The parts are renamed to `PartRed` and `PartBlue`; the containers are renamed to `PalletRed` and `PalletBlue`, and colored accordingly. No other settings are changed.
- Shorten the **Processing Time** of the Station from 10 to 2 (`0:02`) seconds.
- Configure the AssemblyStation: enter only the names of the parts (not their paths).
- Shorten the **Processing Time** of the AssemblyStation from 10 to 5 (`0:05`) seconds.
- Enter the respective pallets into Source1 and Source2.

### Configure the Store as Supermarket and the Source as Order-Controlled

Open the dialog of the Store:

- Select the check box **Supermarket**.
- Click **Configuration** and fill in the configuration table:
  - Minimum stock of 2 parts for `PartRed` and `PartBlue`.
  - Maximum stock of 6 parts.
  - Initial stock of 3 parts.
  - Supplier is the Source named `SourceParts`.
  - During the simulation the column `Current` shows how many parts are located in the Store.

Then open the dialog of the Source and select **MU selection > Order Controlled**.

Run the simulation and watch what happens.

> **Note:** If the simulation does not start, check the setting **Main part from predecessor no** of the AssemblyStation and change it if necessary.

### Show the Amount of Waiting Parts and the Amount of Orders

The Store initially contains 3 parts each, which are loaded onto the pallets. Once the minimum stock is reached, the Store reorders parts from the Source, which only then starts producing them. These parts are then fed into the material flow.

- **View > Show Orders** of the Source shows the orders pending with this Source. The table contains the **Part Type** of the ordered MUs, its **Amount**, and the **Target** of the part (the object that orders the parts).
- **View > Show Orders** of the Store shows the orders pending with this Store.
- When you drag the Store (configured as a Supermarket) onto a Chart, it shows the occupancy for all parts defined in the Configuration table by default.

---

## Stack Parts in the Store

You can also stack parts in the Store. To do so, just enter the **Z-Dimension** of the Store.

In the example, the Source produces parts and moves them onto a Conveyor. The Robot then unloads the parts from the Conveyor and places them in the Store.

- For the Source and the Conveyor, the default settings are used.
- For the Robot: **Loading Time** and **Unloading Time** of 1 second (`0:01`) each, and a **Default Angle** of 180 degrees.
- The Store can store 4 parts in each dimension.

When the simulation runs, the Robot places the parts into stock and stacks them. The parts also move onto the Conveyor continually, front first.

### Loading a Container Layer by Layer

By default, Plant Simulation stacks the parts on each loading place of the Container to its maximum Z-Dimension and then starts a new layer on a new place.

You can load the parts **layer by layer** by activating **Fill Whole Layer**.

In the sample model, a Source produces parts and another Source produces pallets. The top robot loads the parts onto the pallet at the first sensor of the Conveyor. The bottom robot unloads the parts from the pallet and places them onto the lower Conveyor. The Conveyors move the pallets and the parts on to their respective Drains.

- With **Fill Whole Layer deactivated** (default), Plant Simulation stacks the parts on the Container before starting a new layer.
- With **Fill Whole Layer activated**, once a layer is loaded all the way, Plant Simulation starts a new layer.

---

## Working with Workpiece Carriers

You can use the Container as a **workpiece carrier**. Select the check box in its dialog; Plant Simulation then considers the workpiece loaded onto it (the MU), rather than the Workpiece Carrier itself. This affects, among others, the Processing Time and the Set-up Time of the part.

The example demonstrates the workpiece carrier in connection with an AssemblyStation for which the main part is attached to a workpiece carrier:

- Two Sources produce a Container each, used as workpiece carriers.
- In the **Entrance Control** of the Sources, an additional Container is produced (the main part), which is attached to the first Container (the workpiece carrier).
- Two Conveyors transport the main parts (attached to the workpiece carriers) to a Station, which is set up according to the `SetUpTable` and processes parts according to the `ProcessingTable`.
- The Containers are then delivered across an additional Conveyor to the AssemblyStations.
- The AssemblyStation is fed with two different add-on parts by two attached Sources, and attaches the add-on parts to the main parts on the workpiece carrier.
- The AssemblyStation then moves the fully assembled part on to the Drain.

The tutorial demonstrates how to:

- Configure Workpiece Carriers, Main Parts, and Add-On Parts.
- Configure the Sources for Workpiece Carriers and Main Parts.
- Configure the Processing Station, the Set-Up and Processing Table.
- Configure the Sources for the Add-On Parts.
- Configure the AssemblyStation Which Assembles the Parts.
- Run the Simulation and View the Results.

### Configure Workpiece Carriers, Main Parts, and Add-On Parts

The Container is used for both the workpiece carrier and the main parts.

- Open the folder **MUs** in the Class Library.
- Right-click the object **Container** and select **Duplicate**.
- Rename the duplicated Container in the folder `UserObjects` to `WorkpieceCarrier`.
- Duplicate the Container twice and rename the copies to `MainPartA` and `MainPartB`.
- Duplicate the Part twice and rename the copies to `AddOnPart` and `AddOnPartB`.

**Configure the WorkpieceCarrier:**

- Configure the animation object of the WorkpieceCarrier:
  - Right-click the WorkpieceCarrier and select **Open in 3D**.
  - Right-click in the background of the 3D window and select **Exchange Graphics** (a stacking box graphic is selected).
  - When Plant Simulation asks about the suggested dimensions of the stacking box, click **No** (the suggested dimensions are not used).

**Configure the MainParts:**

- The MainParts are made a little smaller than the blue stacking box so they can be attached to the WorkpieceCarriers. The default graphic of the Part is copied and pasted into the main parts.
- For the animation objects of `MainPartA` and `MainPartB`, Transformation and Appearance settings are selected; `MainPartB` just uses another color.
- For the **MU Animation**, an animation area is used.
- To make sure the add-on parts are shown on the top side of the animation area instead of on its floor, click **Show**; the setting **Center > Z > 1** ensures this.

**Configure the add-on parts:**

- For the AddOnParts that are attached to the MainParts, the default graphic is deleted and a simple cylinder is created.
- Simulation object and graphic settings are selected for `AddOnPartA` and `AddOnPartB`; `AddOnPartB` just uses another color.

No other settings are changed.

### Configure the Sources for Workpiece Carriers and Main Parts

Configure the Sources that produce the WorkpieceCarriers:

- `SourceCarrierA` produces the WorkpieceCarriers for `MainPartA`.
- An **Entrance Control** is created which creates a `MainPartA` on each WorkpieceCarrier, with this instruction:

```simtalk
.UserObject.MainPartA.create(@)
```

- For `SourceCarrierB` the same settings are used, but a `MainPartB` is created in the Entrance Control:

```simtalk
.UserObject.MainPartB.create(@)
```

### Configure the Processing Station, the Set-Up and Processing Table

The ProcessingStation processes the MainParts on the WorkpieceCarriers.

- Set the **Set-up Time** for the MainParts on the Station in a DataTable of type `List(Type)`:
  - Insert a DataTable and rename it to `SetUpTable`.
  - Select **Set-up Time > List(Type)** and drag `SetUpTable` to the text box next to it.
- Set the **Processing Time** of the MainParts on the ProcessingStation in a DataTable of type `List(Type)`:
  - Insert a DataTable and rename it to `ProcessingTable`.
  - Select **Processing Time > List(Type)** and drag `ProcessingTable` to the text box next to it.

Plant Simulation formats the DataTables automatically with two columns: one for the MU Type of the part to be set up for/processed, and one for the Processing Time/Set-up Time. The Processing and Set-up Times for the MainParts are then entered.

### Configure the Sources for the Add-On Parts

Configure the Sources that feed the AddOnParts to the AssemblyStation, which attaches them to the MainParts.

- Select `AddOnPartA` and `AddOnPartB` as the MU to be created.

No other settings are changed.

### Configure the AssemblyStation Which Assembles the Parts

Configure the AssemblyStation which attaches the AddOnParts to the MainParts.

- Select the settings and enter into the **AssemblyTable** that the respective AddOnPart is attached to the associated MainPart.

No other settings are changed.

Finally, insert a **Drain** and connect the individual material flow objects with Conveyors and Connectors. For the Drain, a constant processing time of 1 minute is entered.

### Run the Simulation and View the Results

Run the simulation and watch that the Sources first create the WorkpieceCarriers (the blue stacking boxes) and then the respective MainParts (the violet or orange plates).

After the MainParts are processed on the ProcessingStation, the AssemblyStation attaches the AddOnParts to the MainParts located on the WorkpieceCarriers.

The Product Statistics of the WorkpieceCarrier for the attached `MainPartA` or `MainPartB` show the results after leaving the AssemblyStation.

---

## Balancing a Production Line

The object **Cycle** synchronizes the transfer of parts from station to station within a production line. Use it to only move a part on to the next station within a balanced line when:

- All stations have finished processing their parts.
- None of the stations is failed, paused, or unplanned.
- The successor of the balanced line is ready to receive the part.

Insert the object **Cycle** from the folder **MaterialFlow** in the Class Library or from the toolbar **MaterialFlow** in the Toolbox.

The tutorial demonstrates how to:

- Open the Production Line Model Created in 2D.
- Convert the Production Line Model to a 3D Model.

### Open the Production Line Model Created in 2D

Open the simulation model in 3D that was created in a previous version in 2D-only mode.

- Enter the name of the first station and of the last station into the text boxes to define the balanced line.
- All stations between the first and the last station, which are connected with Connectors, form the balanced line.
- Each station must have a predecessor and a successor, and can only have a single predecessor and a single successor.

> **Note:** You can only balance production lines that consist of objects of type **Station** and **AssemblyStation**. When an AssemblyStation is part of the balanced line, the Cycle only continues balancing when the assembly process has finished.

If no stations are defined for the balanced line yet, drag an object of type Station or AssemblyStation onto the icon of the object **Cycle** and drop it there; Plant Simulation enters it as the first station of the balanced line (done with the station called `Drill`, a modified Station). Then drag another object onto it and drop it there; Plant Simulation enters it as the last station (done with the AssemblyStation). To change the last station to `TestQuality`, hold down **Shift**, drag it over the Cycle, and drop it there.

> **Note:** As each station within the balanced line can only have a single predecessor and a single successor, the Source named `TableLegsIn` (which feeds the table legs to the Assembly station) cannot be part of the balanced line.

To detect the difference between a balanced line and an unbalanced line, copy the balanced line and paste it below it. Start the simulation and check the tab **Type Statistics** of the Drain of the balanced and the unbalanced line.

### Convert the Production Line Model to a 3D Model

Convert the model originally created in 2D to a 3D model, reusing adjustments from the previously converted table assembly (`My3DAssembly.spp`).

1. Save the MUs named `TableLeg` and `TableTop` as object files `TableLeg.psobj` and `TableTop.psobj` (Save Object As). These files contain the simulation properties and the 3D graphic settings.
2. Open the DataTables named `TableLegs` and `TableTops`, select **Export Object File**, and export them as `TableLegTable.psobj` and `TableTopTable.psobj`. These files contain the attributes that set the colors of the table legs and table tops.

Then open the 2D model `MyBalancedLine.spp`:

- Save it with a new name (`My3DBalancedLine.spp`).
- Select **Visualization > 3D only** in the Model Settings.

> **Note:** If some objects (for example the DataTable) are not displayed in the 3D model, select this object in the Class Library, press F8, and double-click the attribute `CreateIn3D` so that it shows `true`.

- To use the graphics of the current version of Plant Simulation, hold down **Shift**, right-click **Basis** in the Class Library, and select **Revert all Objects to Standard Graphics**. Plant Simulation then runs with the default part settings, so the simulation settings and graphics must be re-imported.

**Import the simulation settings and graphics of the table legs and table tops:**

- Right-click the folder **Models** in the Class Library and select **Save/Load > Load Object**.
- Select `TableLeg.psobj` (exported above) and repeat for `TableTop.psobj`, then click OK.
- Rename the original classes (for example to `TableLegOriginal` and `TableTopOriginal`) and the imported classes to `TableLeg` and `TableTop`. Once everything works as expected, delete the original classes.

When the simulation runs, the table tops and table legs are produced and assembled as expected, but their colors are wrong because these are set in the production tables.

**Import the contents of the production tables:**

- Open the production tables `TableTops`, `TableLegs`, `TableTops1`, and `TableLegs1` in the Frame `TableAssembly`.
- Click **Import File** and select `TableLegTable.psobj` or `TableTopTable.psobj` (exported above).

Now the table tops and table legs show the correct color. Finally, adjust the positions of the objects and insert a Comment each showing "Balanced Line" and "Non-Balanced Line".
