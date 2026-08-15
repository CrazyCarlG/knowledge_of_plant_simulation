# Portioner — General

## Overview

The **Portioner** is a fluid object that creates a mobile object (MU) out of a free-flowing product. You can then connect the Portioner with one of the material flow objects to further process the created MUs.

The Portioner is the counterpart of the **DePortioner**.

- Hover over the Portioner with the mouse to show a tooltip with information about it.
- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Adding the Object to the Simulation Model

To add the Portioner to your simulation model:

> Manage Class Library > Basic Objects > Fluids > Portioner

on the Home ribbon tab.

Sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**, then select the Category, Topic, and Example in the **Examples Collection** dialog, and click **Open Model**.

## See Also

- Portion and Deportion Materials
- Simulate Free-flowing Materials and Fluids
- Configure the Portioner Pouring the Chocolate Bars
- Configure the Portioner Which Portions the Product

## Dialog Box of the Portioner

Double-click the icon of the Portioner to open its dialog box.

### Edit Simulation Properties
Change the simulation properties of the object in the dialog box. Shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties
To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:
- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Tab Attributes

The tab **Attributes** provides the settings that the object offers. Shared properties are described under *Tab Attributes*.

### MU [Portioner]
Click the ellipsis button and select the type of MU into which the Portioner transmutes the free-flowing material. You can use a predefined MU or create your own MU for this purpose.

- SimTalk: **MUPath** [SimTalk]

### Amount per MU [Portioner]
Type the total amount of the material which the Portioner is to transmute into the MU.

- SimTalk: **AmountPerMU** [SimTalk] - Portioner

### Fluid from Predecessor [text box]
Type the number of the predecessor object which delivers the fluid material to the Portioner.

- SimTalk: **PredecessorNumber** [SimTalk]

### Current Amount [Portioner]
Shows the current amount of material located in the Portioner at the moment.

- SimTalk: **CurrentAmount** [SimTalk] - Portioner

### Current Inflow Rate [Portioner]
Shows the current inflow rate — the amount of liters of material per second flowing into the Portioner.

- SimTalk: **CurrentInFlowrate** [SimTalk]

### Current Material [Portioner]
Shows the name of the current material that flows into the Portioner.

> **Note:** The name is not case-sensitive. All places using such a case-insensitive string point to the same string in main memory; the first occurrence defines its upper-/lower-casing. In SimTalk you can compare strings case-insensitively with the `~=` operator (see *Relational Operators*).

- SimTalk: **CurrentMaterial** [SimTalk] - Portioner

## Tab Times

Define times as described under *Tab Times*. Select a distribution from the drop-down list and type the required values. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (`Const`).

Set the distribution type and a complete set of parameters with the method `setTypeAndAttr` [SimTalk].

See also:
- Recovery Time [general description]
- Set-up Time [general description]
- Select the Set-Up Time
- `RecoveryTime` [SimTalk] - Mixer
- `SetupTime` [SimTalk] - fluid objects

## Tab Failures

Define failures as described under *Tab Failures*.

## Tab Controls

Provides controls to modify the built-in behavior of the object.

### Select the Path to an Existing Method
- Click the ellipsis button, navigate to the Method in **Select Object** [for controls], and click OK. This inserts the Method name into the text box.
- Press `F2` in the text box to open the Method and type the source code of the control.
- Instead of Select Object, you can also drag the Method from a Frame into the text box and drop it there.

### Create a Control That Is a Method of the Object
- Type a meaningful name into the text box and select **Create Control** [context menu]. Plant Simulation inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on an empty text box. Plant Simulation inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later:
- Press `F2`.
- Hold down `Shift` and double-click into the text box.
- Select **Open Object** on the context menu.
- Click the **User-defined** tab and double-click the Method name in the list.

> To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

See also:
- Select Object [for controls]
- Entrance Control [general description]
- Exit Control [general description]
- Shift Calendar [tab Controls]

## Tab Exit

Select to which successor the object moves the part, as described under *Tab Exit*.

See also:
- Blocking [exit strategy]
- Strategy [material flow objects]

## Tab Statistics

The Portioner shows resource statistics as described under *Tab Statistics*.

## Tab Importer

On the **Tab Importer** you can define services for processing the parts, setting the station up for a certain type of part, and repairing the station.

To view Importer Statistics in the Statistics Report:
- Select **View > Show Statistics Report** in the dialog of the object.
- Right-click the object in the Frame and select **Show Statistics Report**, or press `F6`.
- Click **Show Statistics Report** on the Home ribbon tab.

See also:
- Processing Importer
- Set-up Importer
- Failure Importer

## Tab User-defined

Define your own attributes as described under *Tab User-defined*.

## Navigate Menu

The commands are described under *Navigate Menu*.

## View Menu

The View Menu provides commands to access its functions, including commands pertaining to the Transport Importer.

- Exporters [on View menu]
- Unavailable Services [on View menu]
- Services [on View menu]
- Associated Workplaces [on View menu]

See also:
- View Menu [general description]
- Transport Importer

## Tools Menu

The commands are described under *Tools Menu*.

## Help Menu

The commands are described under *Help Menu*.

## Methods of the Portioner

The Portioner provides:
- The Methods of the Fluid Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the selected Class.
- Press `F8` or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show the selected Instance.
