# Simulating Free-Flowing Materials and Fluids

Plant Simulation provides the **Fluid Objects** for simulating free-flowing materials. These materials can be in liquid, gaseous, or pourable form. The fluid objects are suited for the food and beverages and for the pharmaceutical industries.

The examples demonstrate how to model the following scenarios:

- Model the Production of Chocolate Bars
- Continuously Mix Juice and Water
- Portion and Deportion Materials
- Produce Fluids in a Fixed Sequence

> You can also check out the extended model containing additional stations and controls in the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog Examples Collection and click **Open Model**.

---

## Modeling the Production of Chocolate Bars

A simple production line for making chocolate bars:

- The **FluidSources** provide the ingredients milk, sugar, and cocoa. These flow through **Pipes** to their individual **Tanks**, where they are temporarily stored before flowing into the first **Mixer**.
- It mixes them into the first intermediate product, the base chocolate. The base chocolate is then pumped to the next **Mixer**, which stirs the mixture to the desired consistency. The resulting chocolate mass flows on to the final **Mixer**, which blends in the refining material chili that is fed in from its own **FluidSource**.
- The resulting chili chocolate flows to the **Portioner**, which pours the individual chocolate bars. These are then moved on a **Conveyor** to the **Drain**, which removes the chocolate bars from the plant.

Steps demonstrated:

- Configure the Recipe in the MaterialsTable
- Configure the FluidSources Providing the Materials
- Configure the Tanks Storing the Materials
- Configure the Mixers Transmuting the Materials
- Configure the Source Providing the Refining Material
- Configure the Portioner Pouring the Chocolate Bars
- Configure the Conveyor and Run the Simulation
- Change the Shape of the Pipes

### Configure the Recipe in the MaterialsTable

Define the ingredients and the products in the object **MaterialsTable**. These are then used by the **FluidSource** and by the **Mixer**.

- You can enter the materials and the information in any order. As long as the materials are contained in the MaterialsTable, the object that needs them will find them.
- In most cases you can do that in the MaterialsTable in the class library, meaning that you do not have to insert an instance of it into the Frame that contains your simulation model.
- If your model contains a number of Frames which require a vast number of different materials, insert different MaterialsTables into the Frames. A single MaterialsTable might become too large and unwieldy.

Enter the base products, their density, their color, and the amount to produce. Also enter the intermediate products and the final product, their density, color, amount, and the ingredients these products require.

> **Note:** When you change the name of materials or ingredients later in the MaterialsTable, you also have to manually change this name in the text box **Material** of the FluidSource and/or the text box **Product** of the Mixer. Plant Simulation does not automatically do that for you.

### Configure the FluidSources Providing the Materials

Insert a **FluidSource** each for the base materials milk, sugar, and cocoa. Type the name of the material into the text box **Material** (Milk, Sugar, Cocoa). No other settings are changed.

### Configure the Tanks Storing the Materials

Insert a **Tank** each for the base materials milk, sugar, and cocoa. Enter:

- The outflow rate for each material into the text box **Outflow Rate**.
- The volume for each material into the text box **Volume**.

Then insert **Pipes** between the FluidSources and the respective Tanks, and connect them with **Connectors**.

> **Note:** You have to connect the individual fluid objects with Connectors. You cannot connect them with Pipes only.

### Configure the Mixers Transmuting the Materials

Insert three objects of type **Mixer**, which transmute the base materials and the intermediate product to create the end product (chili chocolate bars). Enter:

- The outflow rate of each product into **Outflow Rate**.
- The volume of each product into **Volume**.
- The name of each product into **Product**.
- A processing time for each Mixer on the tab **Times**.

Then connect the Mixers with Pipes and Connectors.

### Configure the Source Providing the Refining Material

To produce chili chocolate bars, add the chili powder in the last Mixer. Insert a **FluidSource** named `SourceChili`, type `ChiliPowder` into **Material**, then connect it with a Pipe and a Connector to `MixerFinal`.

### Configure the Portioner Pouring the Chocolate Bars

The **Portioner** pours the individual chocolate bars. Enter:

- Select the MU that the Portioner is to create from the products: `ChiliChocolate`.
- Enter the **Amount per MU** of the product (0.1 liters of chili chocolate per chocolate bar).

To represent the chocolate bar, create a new MU class in the Class Library named `ChiliChocolate`.

### Configure the Conveyor and Run the Simulation

Insert a **Conveyor** to transport the chocolate bars from the Portioner to the **Drain**. Set the **Speed** of the Conveyor to 40 meters per second. Insert a **Drain** with default settings and run the simulation.

The Tanks, Mixers, and Pipes show the color of the material set in the MaterialsTable. The chili chocolate bar (MU) shows the color set on the tab **Graphics**. To display the chocolate bar properly, right-click the class `ChiliChocolate` in the Class Library and select **Edit 3D Properties**, click the tab **Transformation**, and activate **Scale Automatically**.

### Change the Shape of the Pipes

If pipes were not inserted with curves initially, change the shape of three Pipes so they match real-life pipes. Instead of re-inserting pipes with curves, edit their **Segments** tables:

- Click `Pipe3` once and press the spacebar. Click **Segments**.
- Click in the last row of the table and select **Append Row**.
- Enter the values to bend the Pipe.

> **Note:** To get an idea about the values to enter, insert a Pipe with the approximate shape of the existing Pipe, experiment with the values, and then delete it again.

- Repeat for `Pipe5`.
- For the Pipe connecting `SourceChili` with `MixerFinal`, insert a seamless connection. Click `Pipe8` with the right mouse button and select **Segments [context menu] > Edit [segment]**.
- To insert a segment at the beginning of the object (not possible manually with the mouse): click the Pipe and press `F7`. This opens the **Segments [tab Appearance]** table. Click in row 2 and select **Insert Row**. This inserts an empty row above row 2. Type in the values and adjust the position of the Pipe.

---

## Continuously Mix Juice and Water

A simple line for producing Apfelschorle by mixing apple juice and sparkling water.

The **FluidSources** provide apple juice and sparkling water. These flow through **Pipes** to the **ContinuousMixer**, which mixes them. The Apfelschorle then flows to the **Tank**, where it is stored until it is filled into bottles.

Steps demonstrated:

- Configure the Recipe for Mixing the Fluids
- Configure the ContinuousMixer and Run the Simulation

### Configure the Recipe for Mixing the Fluids

Define the ingredients and the end product in the **MaterialsTable**. Type in the Materials, the Product amount, the Unit, Ingredient 1 and its Unit, and Ingredient 2 and its Unit. Also select the Colors of the individual Materials.

Then type `AppleJuice` and `SparklingWater` into the respective FluidSources to make them produce these materials.

### Configure the ContinuousMixer and Run the Simulation

Type `Apfelschorle` into the text box **Materials Table** to tell the ContinuousMixer which Product it has to create. Use the **Tank** with default settings (Outflow Rate of 1 liter per second, Volume of 3000 liters). Connect the objects with Pipes and Connectors and run the simulation.

The FluidSources produce the materials with their respective color (shown by the transparent Pipes), the ContinuousMixer mixes them, and sends the Apfelschorle to the Tank. The Tank shows its fill level with the indicator at the side of the outflow valve.

---

## Portioning and Deportioning Materials

Mix two different raw materials in the **Mixer** into two products. The Mixer passes these products to the **Portioner**, which portions them into MUs, and moves them on a Conveyor to the **DePortioner**. The DePortioner splits the products and lets them flow off into the respective Tanks. A tanker truck may then pick them up from there.

The model also shows how to connect the transport of fluids and bulk goods with the normal continuous material flows (using a Conveyor).

> **Note:** You cannot connect the Pipes directly with the fluid objects; you have to use Connectors.

Steps:

- Create the Required Parts
- Configure the Recipe of the Product in the MaterialsTable
- Configure the FluidSources Which Produce the Materials
- Configure the Tanks Which Buffer the Materials
- Configure the Mixer Which Mixes the Materials
- Configure the Portioner Which Portions the Product
- Configure the DePortioner
- Configure the Tanks at the End of the Plant

### Create the Required Parts

Create two parts for transporting the bulk goods or fluid:

- Change to the folder **MUs** in the Class Library.
- Right-click **Parts** and select **Duplicate**. Repeat this.
- Change to the folder **UserObjects** where Plant Simulation placed the duplicated parts.
- Rename the duplicated MUs to `ForX` and `ForY` and enter the MU Size.
- On the tab **Appearance**, select different colors for the MUs.
- To make 3D scale the MUs, open their class in the Class Library, click the tab **Transformation** in **Edit 3D Properties**, and select **Scale Automatically**.

The Portioner fills the materials, which the Mixer mixed, into these MUs.

### Configure the Recipe of the Product in the MaterialsTable

Define the ingredients and the products in the **MaterialsTable**. Enter the materials, their density, color, the amount to produce, and ingredient 1 and ingredient 2 with their respective amount and unit.

> **Note:** As the product amount of the Mixer for Product Y differs from the product amount in the MaterialsTable, Plant Simulation adjusts the amounts of the individual ingredients so that the ratio of the ingredients in the recipe is maintained.

> **Note:** When you change the name of materials or ingredients later in the MaterialsTable, you also have to manually change this name in the text box **Material** of the FluidSource and of the DePortioner, and/or the text box **Product** of the Mixer.

### Configure the FluidSources Which Produce the Materials

Insert a **FluidSource** each for Raw material 1 and Raw material 2. Enter the material name into **Material**. Use an outflow rate of 2 liters per second for the first FluidSource and 1.5 liters per second for the second.

### Configure the Tanks Which Buffer the Materials

Insert a **Tank** each for Raw material 1 and Raw material 2. Enter:

- Outflow rate of 1 liter per second into **Outflow rate**.
- Volume of 5 liters into **Volume**.
- Two sensors and their controls.

Then program the Sensor Controls and Reset Control:

```simtalk
// Sensor Control 1
param SensorID: integer, Exceeded: boolean
self.~.EntranceLocked := false
```

```simtalk
// Sensor Control 2
param SensorID: integer, Exceeded: boolean
self.~.EntranceLocked := true
```

```simtalk
// Reset Control
self.~.EntranceLocked := false
```

Repeat these steps for the second Tank. Insert Pipes between the FluidSources and the respective Tanks, and connect with Connectors.

### Configure the Mixer Which Mixes the Materials

Insert a **Mixer**. Enter:

- Outflow Rate of 1 liter per second.
- Volume of 6 liters.
- The name of the Product.
- A Processing Time on the tab **Times**.
- An **Init Control** on the tab **User-defined** (makes sure the first product mixed is always the same).
- An observer for the read-only attributes `ResWorking` and `Empty` and the corresponding controls so that the Mixer changes the recipe of the material.

```simtalk
// observer for ResWorking
param Attribute: string, previousValue: any
if NOT ?.ResWorking AND NOT ?.Failed AND NOT ?.Stopped 
   if ?.Product = "Product X" 
      ?.Product := "Product Y"
   else
      ?.Product := "Product X"
   end
end
```

```simtalk
// observer for Empty
param Attribute: string, previousValue: any
if ?.Leer
   if ?.Product = "Product Y"
      Portioner.MUPath := .UserObjects.ForY
      Portioner.AmountPerMU := 3
   else
      Portioner.MUPath := .UserObjects.ForX
      Portioner.AmountPerMU := 2
   end
end
```

The observer for `ResWorking` changes the product for the following processing step of the Mixer at the end of the processing time. The product can only be changed once the Mixer is empty. At this point, which the observer for `Empty` recognizes, the Portioner can be prepared for the new product.

Finally connect the Mixer and the Portioner with a Pipe and Connectors.

### Configure the Portioner Which Portions the Product

- Select the MU the Portioner is to create from the products (the MU named `ForY`).
- Enter the **Amount per MU** of the product (2 liters per MU).

### Configure the DePortioner

Insert a **Conveyor** between the Portioner and DePortioner. Configure the **DePortioner**:

- Outflow rate of 1 liter per second (default).
- Select **Fluid Depends On > MU Name** so the DePortioner creates the material and the amount of fluid depending on the MU names defined in the Mapping Table.
- Select the DataTable named `MyTable` as the mapping table. Enter the MU name, the Material, and the Amount.
- Enter a Set-up Time of 2 minutes to set the DePortioner up for the new product when the product changes.
- The Entrance Control named `partArrives` opens or closes the Pipes to the individual Tanks.

```simtalk
// entrance control of the DePortioner
if @.MaterialName = "Product X"
   PipeX.PipeOpened := true
   PipeY.PipeOpened := false
   @.MaterialName := "Product Y"
else
   PipeX.PipeOpened := false
   PipeY.PipeOpened := true
end
```

Insert the Pipes connecting the DePortioner with the succeeding Tanks and connect with Connectors.

### Configure the Tanks at the End of the Plant

Configure the two Tanks at the end of the facility. Enter an outflow rate of 0.1 liter per second and a volume of 2000 liters for both Tanks. Create a sensor in each Tank with the following settings.

The sensor control named `xyFull`:

```simtalk
// sensor control of TankX and TankY
param SensorID: integer, Exceeded: boolean
EventController.stop(true)
```

Create a user-defined attribute named `reset` for both Tanks:

```simtalk
self.~.EntranceLocked := false
```

When running the simulation, the Mixer mixes two products from the two raw materials, the Portioner splits them into portions, the Conveyor moves the filled portions to the DePortioner, which dissolves the portions and lets them flow off to the designated Tanks. As soon as one Tank reaches its defined volume of 2000 liters, the simulation stops.

---

## Producing Fluids in a Fixed Sequence

A simple production line in which a **FluidSource** produces three materials in a fixed sequence.

The FluidSource produces the materials in the sequence and with the amount in the order entered into the sequence table. The materials flow through Pipes to a **PatchMatrix**, which distributes the materials via three Pipes to the **Tanks** storing the individual materials. How the PatchMatrix fills the Tanks is defined in a Method, which is called by the init method.

Steps demonstrated:

- Configure FluidSource, MaterialsTable, and SequenceTable
- Configure the Tanks Receiving the Materials
- Define How the PatchMatrix Fills the Tanks
- Run the Simulation to View the Results

> Remember that you have to establish connections between Pipes and fluid objects with Connectors.

### Configure FluidSource, MaterialsTable, and SequenceTable

- Select **Material Selection > Sequence** on the tab **Attributes** to produce in a fixed sequence.
- The FluidSource produces the materials in the sequence and with the amount in the order entered into the Sequence Table. The setting `Sequence` processes the sequence only once, not repeatedly. When the sequence is processed once, the FluidSource does not produce any additional materials.
- Enter the materials `MatA`, `MatB`, and `MatC` into the MaterialsTable, assigning different colors to distinguish them.
- Enter the sequence into the SequenceTable: the FluidSource first produces 1000 liters of `MatB`, then 1500 liters of `MatC`, and finally 800 liters of `MatA`.

### Configure the Tanks Receiving the Materials

Insert a **Tank** each for the three materials. Since the settings are the same (Outflow rate of 1 liter per second, Volume of 3000 liters), enter them into the class of the Tank.

### Define How the PatchMatrix Fills the Tanks

When connecting the PatchMatrix with the incoming and outgoing Pipes, they are entered into the **Connections** table. Normally the outgoing Pipes the PatchMatrix connects with the incoming Pipes are set by selecting the respective check box(es).

In this situation the FluidSource produces different amounts of three materials in a fixed sequence, so the PatchMatrix must connect the incoming Pipe with the respective outgoing Pipe to fill the three Tanks with the correct material. This is programmed in the method `fillTanks`:

```simtalk
var currMaterial = "" 
waituntil FluidSource.CurrentMaterial /= currMaterial
currMaterial = FluidSource.CurrentMaterial
PatchMatrix.setConnections(1, 1, true)    // lets the first material flow into the outgoing Pipe1
waituntil FluidSource.CurrentMaterial /= currMaterial
currMaterial = FluidSource.CurrentMaterial
PatchMatrix.setConnections(1, 1, false)   // closes Pipe1
PatchMatrix.setConnections(1, 2, true)    // lets the second material flow into the outgoing Pipe2
waituntil FluidSource.CurrentMaterial /= currMaterial
currMaterial = FluidSource.CurrentMaterial
PatchMatrix.setConnections(1, 2, false)   // closes Pipe2
PatchMatrix.setConnections(1, 3, true)    // lets the third material flow into the outgoing Pipe3
```

The method `fillTanks` is called in the init method:

```simtalk
PatchMatrix.resetConnections
fillTanks
```

The connections of the PatchMatrix are also reset in the reset method:

```simtalk
PatchMatrix.resetConnections
```

### Run the Simulation to View the Results

When the simulation runs, the FluidSource produces the materials in the sequence specified in the SequenceTable one after the other. The color of the Pipe shows which material flows. The PatchMatrix sends the arriving material to the correct Tank by opening the respective Pipe.

To better see the results, set a real-time factor of 42 in the EventController.

First the FluidSource produces 1000 liters of `MatB` (green) and passes it to the PatchMatrix, which opens Pipe1 to let `MatB` flow into `TankMatB`. Next flows `MatC` and finally `MatA`. At the end, all Tanks are filled with the specified amount of the specified material.

To run the same sequence again with a pause in between, program a Method named `startSecondSequence`:

```simtalk
print EventController.SimTime
FluidSource.Material = void
FluidSource.Material = SequenceTable
fillTanks
```

To execute it during the simulation run, enter this instruction into the init method:

```simtalk
&startSecondSequence.executeIn(1:00:00)
PatchMatrix.resetConnections
fillTanks
```

At the end of the simulation run the Tanks consequently contain twice the amount of the materials.
