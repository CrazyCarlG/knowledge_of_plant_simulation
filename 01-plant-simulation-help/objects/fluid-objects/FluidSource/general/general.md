# FluidSource

Use the object **FluidSource** to produce the ingredients of the product, either bulk goods or fluids, which are processed in the plant.

## Description

- Use the **FluidDrain** to remove the processed and mixed products from the plant.
- To change the length of the graphic and the anchor points of the FluidSource, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.
- To show a tooltip with information about the FluidSource, hover with the mouse over it.

## Add the Object to the Simulation Model

To add the object FluidSource to your simulation model, click **Manage Class Library > Basic Objects > Fluids > FluidSource** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog Examples Collection, and click Open Model.

## See also

- Configure the FluidSources Providing the Materials
- Configure the FluidSources Which Produce the Materials
- Produce Fluids in a Fixed Sequence
- Dialog Box of the FluidSource

## Dialog Box of the FluidSource

Double-click the icon of the FluidSource to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under Dialog Items of the Objects.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Tab Attributes

The tab **Attributes** provides the settings, which the object offers. The settings are listed in the table of contents to the left. The shared properties are described under the Tab Attributes.

### Outflow Rate [FluidSource]

Type the Outflow Rate into the text box with which the material flows out of the Tank. The material then flows through the objects of type Pipe to the next object in the flow of materials.

**Remarks**

The Outflow Rate is the amount of liters of the material that flows off in a second.

**Note**

The current Outflow Rate depends on the number of attached Pipes. If you attached two Pipes, the specified Outflow Rate flows through each one of these Pipes in case the Outflow Rate of the connected Pipes enables this.

If you just want to let the specified amount flow out of the object, attach a single Pipe and split that up into several Pipes later on.

**SimTalk**

```simtalk
OutflowRate [SimTalk] - FluidSource
```

**See also:** Pipe

### Material Selection [drop-down list]

Select how the FluidSource selects the material it produces.

**Note**

Depending on what you select here, the setting Material either defines the Material itself or the path to the sequence table.

You can select one of these settings:

- **Constant** — The FluidSource produces a single type of material only. Type the name of the material into the text box Material.
- **Sequence Cyclical** — The FluidSource produces the materials in the sequence and with the amount in the order in which you type them into the Sequence Table. Once the FluidSource has processed the entire sequence, it starts processing the information in the table again starting at the beginning of the sequence. Type the name of the Sequence Table into the text box Material, or click and select the name of the table in the dialog Select Object. Plant Simulation automatically formats the table.
- **Sequence** — The FluidSource produces the materials in the sequence and with the amount in the order in which you type them into the Sequence Table. As opposed to Sequence Cyclical, the setting Sequence processes the sequence only once, not repeatedly. If the sequence is processed once, the FluidSource does not produce any additional materials.

**SimTalk**

```simtalk
MaterialSelection [SimTalk]
```

**See also**

- Produce Fluids in a Fixed Sequence
- Material [text box] - FluidSource
- Material [SimTalk] - FluidSource

### Material [text box] - FluidSource

Type the name of the Material into the text box, which the FluidSource is to produce.

**Note**

What you type in as the Material depends on the setting you selected as the Material Selection.

You can select one of these settings:

- **Constant** — The FluidSource produces a single type of material only. Type the name of material into the text box Material.
- **Sequence Cyclical** — The FluidSource produces the materials in the sequence and with the amount in the sequence in which you type them into the Sequence Table. Once the Source has processed the entire sequence, it starts processing the information in the table again starting at the beginning of the sequence. Type the name of the Sequence Table into the text box Material, or click and select the name of the table in the dialog Select Object. Plant Simulation automatically formats the table.
- **Sequence** — The FluidSource produces the materials in the sequence and with the amount in the sequence in which you type them into the Sequence Table. As opposed to Sequence Cyclical, the setting Sequence processes the sequence only once, not repeatedly.

### Sequence Table

Define the materials, which the FluidSource is to produce in the Sequence Table.

You can type in:

- The name of the Material, for example MatA, MatB, MatC, MatD, etc.
- The Amount in liters of the Material that the FluidSource is to produce.

Define the names of the material in the MaterialsTable.

If the product consists of more than ten ingredients, add additional ingredients to the MaterialsTable, compare Add Additional Ingredients to the MaterialsTable.

**SimTalk**

```simtalk
Material [SimTalk] - FluidSource
```

**See also**

- Produce Fluids in a Fixed Sequence
- Material Selection [drop-down list]
- MaterialSelection [SimTalk]

### Materials Table [FluidSource]

The MaterialsTable object contains the data of the different materials which the FluidSource can produce.

**Remarks**

Click the ellipsis button and select the MaterialsTable in the dialog Select Object. Or select the MaterialsTable in a Frame, drag it to the text box and drop it there.

**SimTalk**

```simtalk
MaterialsTable [SimTalk] - FluidSource
```

**See also**

- MaterialsTable
- Select Object [for controls]

### Shift Calendar [FluidSource]

Select the ShiftCalendar. It contains the data of the shifts in your installation and controls during which shifts the FluidSource works.

**Remarks**

Click the ellipsis button and select the ShiftCalendar in the dialog Select Object. Instead of clicking the ellipsis button, you can also select the ShiftCalendar in a Frame, drag it to the text box, and drop it there.

This automatically enters the object into the list of Objects on the tab Resources of the ShiftCalendar.

**SimTalk**

```simtalk
ShiftCalendarObject [SimTalk] - material flow objects
```

**See also**

- ShiftCalendar [object]
- Associated Shift Calendar
- Select Object [for controls]

### Current Outflow Rate [FluidSource]

Shows the Current Outflow Rate, i.e., the amount of liters of the material that flows out of the FluidSource in a second and that flows through objects of type Pipe to the next object in the flow of materials.

**SimTalk**

```simtalk
CurrentOutFlowrate [SimTalk]
```

**See also:** Pipe

## Tab Failures

Define failures as described under the Tab Failures.

## Tab Statistics [FluidSource]

In addition to the values described under the Tab Statistics, the tab Statistics of the FluidSource shows this object-specific value.

| Item (English) | Description | Read-only attribute | Item (German) |
| --- | --- | --- | --- |
| Amount of Material | Shows the amount of material that flowed out of the FluidSource. | `StatAmount [SimTalk]` | Materialmenge |

**See also:** Statistics Report [described]

## Tab User-defined Attributes

Define your own attributes as described under the Tab User-defined.

## Navigate Menu

The commands are described under the Navigate Menu.

## View Menu

The commands are described under the View Menu.

**SimTalk**

```simtalk
updateDialog [SimTalk]
```

## Tools Menu

The commands are described under the Tools Menu.

## Help Menu

The commands are described under the Help Menu.

## Methods of the FluidSource

The FluidSource provides:

- The Methods of the Fluid Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].
