# Mixer

Use the object **Mixer** to transmute the ingredients of the process into an intermediate or a finished product by mixing them.

## Description

The ingredients can flow into the Mixer simultaneously from several preceding FluidSources or Tanks.

- If you defined the ingredients for the product in the **MaterialsTable**, the Mixer only uses the defined ingredients. As soon as the respective amount of these ingredients is present in the mixing container, the Mixer starts mixing them.
- If you did not define ingredients for the product, the Mixer takes all materials from the connected Pipes and starts mixing when the mixing container is full.

Once processing is finished, the product flows out of the Mixer. After the Mixer is empty again, the recovery time starts, which is required to flush and to clean it and to prepare it for the next process.

To show a tooltip with information about the Mixer, hover with the mouse over it. To change the length of the graphic and the anchor points of the Mixer, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

### Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > Fluids > Mixer** on the Home ribbon tab.

## Dialog Box of the Mixer

Double-click the icon of the Mixer to open its dialog box.

**Edit Simulation Properties** — change the simulation properties of the object.

**Edit Animation Properties** — to edit the 3D properties of the object in the dialog box **Edit 3D Properties**:
- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Tab Attributes

The tab **Attributes** provides the settings that the object offers.

### Outflow Rate [Mixer]

Type the **Outflow Rate** into the text box. This is the rate with which the material flows out of the object and flows through the objects of type Pipe to the next object in the flow of materials.

The Outflow Rate is the amount of liters of the material that flows off in a second.

> **Note:** The current Outflow Rate depends on the number of attached Pipes. If you attached two Pipes, then the specified Outflow Rate flows through each one of these Pipes in case the Outflow Rate of the connected Pipes enables this. To let the specified amount flow out of the object through a single outlet, attach a single Pipe and split it up into several Pipes later on.

### Volume [Mixer]

Type the **Volume** of the Mixer into the text box. This is the amount of liters that is available for the ingredients or the product respectively within the mixing container.

### Product [text box] - Mixer

Type the name of the intermediate or of the finished Product into the text box. This is the product which the Mixer is to produce by mixing the ingredients.

Specify the name of this product in the MaterialsTable. If the product consists of more than ten ingredients, add additional ingredients to the MaterialsTable.

### Product Amount [text box]

Type the **Amount** of the intermediate or of the finished Product into the text box. This is the amount which the Mixer is to produce by mixing the ingredients.

- The default value `-1` means that the finished product fully utilizes the volume of the Mixer. The product amount is measured in liters.
- If the Product Amount differs from the Product Amount typed into the MaterialsTable, Plant Simulation adjusts the amounts of the individual ingredients accordingly to ensure that the ratio of the ingredients is retained.
- If you type `-1` for a recipe into the column Product Amount of the MaterialsTable of the Mixer, Plant Simulation assumes the sum of all ingredients as the Product Amount. You only have to explicitly specify the Product Amount if mixing the ingredients increases or decreases the volume.

### Materials Table [Mixer]

The **MaterialsTable** object contains the data of the different materials which the Mixer can mix.

- Click the ellipsis button and select the MaterialsTable in the dialog Select Object.
- Or select the MaterialsTable in a Frame, drag it to the text box and drop it there.

### Current Fill Level [Mixer]

Shows the **Current Fill Level** of the mixing container in which the Mixer transmutes the materials. The Mixer shows the current fill level of the material on the outflow side.

### Current Amount [Mixer]

Shows the **Current Amount** of product that is located in the mixing container of the Mixer at the moment.

### Current Inflow Rate [Mixer]

Shows the **Current Inflow Rate**, i.e., the amount of liters of the material which flows into the Mixer in a second.

### Current Outflow Rate [Mixer]

Shows the **Current Outflow Rate**, i.e., the amount of liters of the material that flows out of the Mixer in a second and that flows through objects of type Pipe to the next object in the flow of materials.

## Tab Times

Define Times as described under the Tab Times. Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (`Const`).

You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr` (SimTalk).

## Tab Failures

Define failures as described under the Tab Failures.

## Tab Controls

Provides controls to modify the built-in behavior of the object.

### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog Select Object and click OK. This inserts the name of the Method into the text box of the Control. Press `F2` in the text box to open the Method and type in the source code of the Control. Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

### Create a Control That is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control** (context menu). Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as:

```simtalk
self.A1Ctrl
```

- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as:

```simtalk
self.OnEntrance
```

Type the source code of this control into the Method that opens.

To edit the source code later on:
- Press `F2`.
- Or hold down `Shift` and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab User-defined and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

### Ingredient Complete Control

Modifies the built-in behavior of the object. The object calls the Ingredient Complete Control when an ingredient of the recipe has completely arrived in the Mixer.

With the Ingredient Complete Control you can define/start any actions that need to take place in your simulation model via SimTalk.

The Ingredient Complete Control will also be called if the last ingredient or the last ingredients arrived at the same time at which the Mixer reached the Volume you specified.

## Shift Calendar [Mixer]

Select the **ShiftCalendar**. It contains the data of the shifts in your installation and controls during which shifts the Mixer works.

Click the ellipsis button and select the ShiftCalendar in the dialog Select Object, or select the ShiftCalendar in a Frame, drag it to the text box, and drop it there. This automatically enters the object into the list of Objects on the tab Resources of the ShiftCalendar.

## Tab Statistics [Mixer]

In addition to the values described under the Tab Statistics, the tab Statistics of the Mixer shows these object-specific values:

| Item (English) | Description | Read-only attribute | Item (German) |
|---|---|---|---|
| Total Throughput | Shows the amount of product that flowed through the Mixer. | `StatDeleted` (Drain) | Gesamtdurchsatz |
| Relatively Empty | Shows the portion of the statistics collection period during which the Mixer was Empty in relation to the time during which it was available. | `StatRelativeEmptyPortion` | Relativ leer |

## Tab Importer

On the Tab Importer you can define services for processing the parts, for setting the station up for a certain type of part, and for repairing the station.

To view Importer Statistics in the Statistics Report:
- Select **View > Show Statistics Report** in the dialog of the object.
- Click the object with the right mouse button in the Frame and select **Show Statistics Report**, or press `F6`.
- Click **Show Statistics Report** on the Home ribbon tab.

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

## Menus

- **Navigate Menu** — described under the Navigate Menu.
- **View Menu** — provides commands to access its functions, including commands pertaining to the Transport Importer (Exporters, Unavailable Services, Services, Associated Workplaces).
- **Tools Menu** — described under the Tools Menu.
- **Help Menu** — described under the Help Menu.

## Methods of the Mixer

The Mixer provides:
- The methods listed in the table of contents to the left.
- The Methods of the Fluid Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press `F8` or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show the methods, read-only attributes, and attributes of the selected Instance.

## SimTalk Reference

### Underrun [SimTalk]

Sets if the sensor is to be triggered if the amount of material in the Tank designated by `<Path>` has underrun, i.e., is located below the sensor position (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Sensors.ID<Number>.Underrun:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

```simtalk
MyTank.Sensors.id1.Underrun := true
```

See also: Underrun (check box), Mixer.
