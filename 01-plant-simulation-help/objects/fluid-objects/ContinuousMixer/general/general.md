# ContinuousMixer — General

## Volume [SimTalk] - Mixer

Sets the Volume that is available for the ingredients or the product respectively in the mixing container of the Mixer designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Volume:real`
- **Assignment Value:** You can assign a value of data type `real`.

**Example**

```simtalk
MyMixer.Volume := 10
```

**See also:** Volume [Mixer]

---

## ContinuousMixer

Use the object ContinuousMixer to transmute the ingredients of the process into an intermediate or a finished product by mixing them.

### Description

The ingredients can flow into the ContinuousMixer simultaneously from several preceding fluid objects.

- The ContinuousMixer only processes fluids if the product and the ingredients information is defined in the MaterialsTable.
- The ContinuousMixer only starts the mixing process once it receives all the materials from the preceding objects in the correct ratio defined in the MaterialsTable. If the ratio is incorrect, the mixing process will stop immediately.
- The outflow from the ContinuousMixer starts simultaneously when the inflow starts. The outflow is typically equal to the cumulative inflow, but it can be different when you define the recipe in the MaterialsTable accordingly.
- To show a tooltip with information about the ContinuousMixer, hover with the mouse over it.
- To change the length of the graphic and the anchor points of the ContinuousMixer, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

### Add the Object to the Simulation Model

To add the object ContinuousMixer to your simulation model, click **Manage Class Library > Basic Objects > Fluids > ContinuousMixer** on the Home ribbon tab.

**See also:** Continuously Mix Juice and Water, Dialog Box of the ContinuousMixer

---

## Dialog Box of the ContinuousMixer

Double-click the icon of the ContinuousMixer to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under Dialog Items of the Objects.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

---

## Tab Attributes

The tab Attributes provides the settings, which the object offers. The settings are listed in the table of contents. The shared properties are described under the Tab Attributes.

### Product [text box] - ContinuousMixer

Type the name of the intermediate or of the finished Product into the text box. This is the product, which the ContinuousMixer is to produce by mixing the ingredients.

**Remarks**

- Specify the name of this product in the MaterialsTable.
- If the product consists of more than ten ingredients, you can Add Additional Ingredients to the MaterialsTable.

**See also:** Product [SimTalk] - ContinuousMixer

### Materials Table [ContinuousMixer]

The MaterialsTable object contains the data of the different materials which the ContinuousMixer can mix.

**Remarks**

- Click the ellipsis button and select the MaterialsTable in the dialog Select Object.
- Or select the MaterialsTable in a Frame, drag it to the text box and drop it there.
- If you type `-1` for a recipe into the column **Product Amount** of the MaterialsTable of the ContinuousMixer, Plant Simulation assumes the sum of all ingredients as the Product Amount. You only have to explicitly specify the Product Amount if mixing the ingredients increases or decreases the volume, i.e., if the Product Amount is not the sum of the ingredients.

**See also:** MaterialsTable, Select Object [for controls], MaterialsTable [SimTalk] - ContinuousMixer

### Shift Calendar [ContinuousMixer]

Select the ShiftCalendar. It contains the data of the shifts in your installation and controls during which shifts the ContinuousMixer works in the plant.

**Remarks**

- Click the ellipsis button and select the ShiftCalendar in the dialog Select Object.
- Instead of clicking the ellipsis button, you can also select the ShiftCalendar in a Frame, drag it to the text box, and drop it there. This automatically enters the object into the list of Objects on the tab Resources of the ShiftCalendar.

**See also:** ShiftCalendar [object], Associated Shift Calendar, Select Object [for controls], ShiftCalendarObject [SimTalk] - material flow objects

### Current Inflow Rate [ContinuousMixer]

Shows the Current Inflow Rate, i.e., the amount of liters of the material which flows into the ContinuousMixer in a second.

**See also:** CurrentInFlowrate [SimTalk]

### Current Outflow Rate [ContinuousMixer]

Shows the Current Outflow Rate, i.e., the amount of liters of the material that flows out of the ContinuousMixer in a second and that flows through objects of type Pipe to the next object in the flow of materials.

**See also:** CurrentOutFlowrate [SimTalk], Pipe

---

## Tab Failures

Define failures as described under the Tab Failures.

---

## Tab Times

Define the Set-up Time as described under the Tab Times. Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also type in a constant time (Const). You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr`.

**See also:** Select the Set-Up Time

---

## Tab Statistics [ContinuousMixer]

In addition to the values described under the Tab Statistics, the tab Statistics of the ContinuousMixer shows this object-specific value.

| Item (English) | Description | Read-only attribute | Item (German) |
| --- | --- | --- | --- |
| Total Throughput | Shows the amount of product that flowed through the ContinuousMixer. | StatDeleted [SimTalk] - Drain | Gesamtdurchsatz |

---

## Tab Importer

On the Tab Importer you can define services for processing the parts, for setting the station up for a certain type of part, and for repairing the station.

To view Importer Statistics in the Statistics Report, do one of the following:

- Select **View > Show Statistics Report** in the dialog of the object.
- Click the object with the right mouse button in the Frame and select **Show Statistics Report** or press **F6**.
- Click **Show Statistics Report** on the Home ribbon tab.

**See also:** Processing Importer, Set-up Importer, Failure Importer

---

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

---

## Navigate Menu

The commands are described under the Navigate Menu.

---

## View Menu

The View Menu provides commands to access its functions. The View Menu also provides commands pertaining to the Transport Importer:

- Exporters
- Unavailable Services
- Services
- Associated Workplaces

**See also:** View Menu [general description], Transport Importer

---

## Tools Menu

The commands are described under the Tools Menu.

---

## Help Menu

The commands are described under the Help Menu.

---

## Methods of the ContinuousMixer

The ContinuousMixer provides:

- The Methods of the Fluid Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.
