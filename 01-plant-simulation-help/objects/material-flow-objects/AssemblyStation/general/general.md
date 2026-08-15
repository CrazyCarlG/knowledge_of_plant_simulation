# AssemblyStation

Use the object **AssemblyStation** for adding mounting parts to a main part, for example doors to a car body.

## Description

The AssemblyStation moves the mounting parts either to the main MU — according to the value you enter into the Assembly Table — or it deletes them. Mounting parts might also be called assembly parts, add-on parts, attachment part, attached part, etc.

Use the AssemblyStation to model assembly processes. If the assembly process requires services, you can assign the order in which the AssemblyStation requests mounting parts and services. To dismantle parts from the main part, you can use the **DismantleStation**.

If the AssemblyStation uses an Assembly Table and you specify an Assembly Time and a Sequence Number for each mounting part, the AssemblyStation assembles the mounting parts sequentially. The assembly of each individual mounting part consumes the specified Assembly Time. After all mounting parts are assembled, the Processing Time of the AssemblyStation passes and the main part then leaves the station.

In sequential assembly mode, the AssemblyStation starts assembling the mounting parts with the lowest Sequence Number, then continues with the next higher Sequence Number, and so on. Only the mounting parts that are needed in the current assembly sequence can enter the AssemblyStation. Within a sequence, the mounting parts are assembled in the order in which they entered the AssemblyStation.

> **Note:** You cannot move a part via information flow, i.e., by using methods, to the AssemblyStation!

To show a tooltip with information about the AssemblyStation, hover with the mouse over it.

To change the length of the graphic and the anchor points of the AssemblyStation, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Add the Object to the Simulation Model

To add the object AssemblyStation to your simulation model, click **Manage Class Library > Basic Objects > MaterialFlow > AssemblyStation** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog Examples Collection, and click Open Model.

## Dialog Box of the AssemblyStation

Double-click the icon of the AssemblyStation to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under Dialog Items of the Objects.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box Edit 3D Properties:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Tab Attributes

The tab Attributes provides the settings, which the object offers. Set how the AssemblyStation attaches mounting parts to the main part on the tab Attributes.

### Assembly Table

Select if the AssemblyStation uses an Assembly Table and if so which kind.

> **Note:** You cannot change the Assembly Table if the Main MU is already located on the AssemblyStation. To change the Assembly Table in the Entrance Control of the Station, select the check box **Before Actions** of the Entrance Control.

Select the type of Assembly Table you want to use. Then click Open and type the required information into the assembly table.

- **None** — The AssemblyStation does not use an Assembly Table. Instead, it expects a part from each of its predecessors.
- **Predecessors** — Type the required settings into the table.
  - Type the number of the Predecessor, which moves the part, into column 1 of the table and the Amount into column 2 of the Assembly Table. To use the default value 1, do not type in an Amount.
  - To make the AssemblyStation accept parts from this predecessor until the capacity of the main MU is reached, type in `-1` as the Amount. To use parts of the main part number as mounting parts, add the number of the main MU to the Assembly Table.
  - Type the time, in seconds, that each individual part consumes when it's assembled into the column Assembly Time and the number of the sequence in which the part is assembled into the column Sequence Number. The Assembly Time must be a positive number or 0. If you do not specify a time, the default Assembly Time is 0.
  - The Sequence Number must be a positive integer number. The default Sequence Number is 1.
  - To assemble the parts non-sequentially, leave the columns Assembly Time and Sequence Number empty.
- **MU Types** — Enter the required settings into the table.
  - Type the MU Name of the part, such as Part, Container, Transporter, Shaft, etc., into column 1 and the Amount into column 2 of the Assembly Table.
  - Type the name of the part into the column MU Name, not its path, for example `MyMountingPart` and not `*.UserObjects.MyMountingPart`.
  - To use the default value 1, do not type in an Amount. To make the AssemblyStation accept parts with this MU Name until the capacity of the main MU is reached, type in `-1` as the Amount.
  - Type the time, in seconds, that each individual part consumes when it's assembled into the column Assembly Time and the number of the sequence in which the part is assembled into the column Sequence Number. The Assembly Time must be a positive number or 0. If you do not specify a time, the default Assembly Time is 0.
  - The Sequence Number must be a positive integer number. The default Sequence Number is 1.
  - To assemble the parts non-sequentially, leave the columns Assembly Time and Sequence Number empty.
- **Depends on Main MU** — Enter the required settings into the table.
  - Type in the Main MU Name of the main MU, such as Part, Container, Transporter, Shaft, etc.
  - Type in an asterisk `*` to handle all main parts which you did not explicitly enter with names of their own into the assembly table. Type in the MU Name and the Amount of the parts.
  - To use the default value 1, do not type in an Amount. To make the AssemblyStation accept parts with this MU Name until the capacity of the main MU is reached, type in `-1` as the Amount.
  - Type the time, in seconds, that each individual part consumes when it's assembled into the column Assembly Time and the number of the sequence in which the part is assembled into the column Sequence Number. The Assembly Time must be a positive number or 0. If you do not specify a time, the default Assembly Time is 0.
  - The Sequence Number must be a positive integer number. The default Sequence Number is 1.
  - To assemble the parts non-sequentially, leave the columns Assembly Time and Sequence Number empty.
- **Fill up Main MU** — The AssemblyStation does not use an Assembly Table. Instead, it accepts parts from any of its predecessors until the capacity of the main MU is reached.

> **Note:** For the settings MU Types and Depends on Main MU this applies: If the AssemblyStation has objects of type Store as predecessors, it requests the required mounting parts from the Store. If the required parts are not available in the Store at the moment, the Store records the request and delivers the parts to the AssemblyStation once they are available again. The parts can also be carried from the Store to the AssemblyStation by a Worker. The Store can only provide mounting parts, but no main parts, and it has to be connected with a Connector, even if the Worker carries the part away.

**SimTalk:**
- `AssemblyTable [SimTalk]`
- `AssemblyTableMode [SimTalk]`

### Workers Sequentially Deliver MUs to Assemble

To make the Worker deliver the required mounting parts, which the AssemblyStation requested, sequentially one after the other to the AssemblyStation, select this check box.

Workers Sequentially Deliver MUs to Assemble prevents that several Workers walk to the AssemblyStation and cannot deliver and deposit the parts because the AssemblyStation cannot accept them. To accomplish this Plant Simulation reserves a processing place for the mounting part on the AssemblyStation.

> **Note:** If you select Workers Sequentially Deliver MUs to Assemble, the attribute `ReservedFor` returns the part for which the place is currently reserved. If you clear the check box, `ReservedFor` returns an array of parts for which places are reserved.

To make a single Worker deliver as many mounting parts as he can carry to the AssemblyStation, clear the check box. To make several Workers deliver the mounting parts to the AssemblyStation in parallel at the same time, clear the check box.

**SimTalk:**
- `SequentialDelivery [SimTalk]`
- `ReservedFor [SimTalk]`

### Main MU from Predecessor

Type in the number of the Predecessor object which moves the main MU to the AssemblyStation.

Type in `0` if the main part is not delivered by any of the predecessors of the AssemblyStation, e.g. if a Worker transports the main part to the AssemblyStation or if you use a SimTalk command to move the main part to the AssemblyStation.

The predecessor is the object that is connected to the selected object with a Connector and that precedes it in the sequence of stations in the simulation model.

As the AssemblyStation is connected to at least two stations, the order in which you connect it with the predecessors is important. If the assembly process does not work as expected, check the numbering of the predecessors.

Plant Simulation shows the predecessors and the successors of an object in a Tooltip when you drag the mouse over the respective Connector.

**SimTalk:**
- `MainMU [SimTalk] - AssemblyStation`

### Assembly Mode [drop-down list]

Select the Assembly Mode, i.e., how the AssemblyStation handles MUs.

- **Attach MUs** — The AssemblyStation attaches the mounting part to the main MU.
- **Delete MUs** — The AssemblyStation deletes the mounting part after the assembly operation is finished.

**SimTalk:**
- `AssemblyMode [SimTalk]`

### Exiting MU [drop-down list] - AssemblyStation

Select how the AssemblyStation handles the Exiting MU, i.e., the MU, which is leaving the station.

- **Main MU** — The AssemblyStation moves the main MU to the succeeding object.
- **New MU** — The AssemblyStation moves the assembled/new MU to the succeeding object.

If you select New MU, the AssemblyStation shows the button and the text box MU. Click this to open the dialog Select Object and select the new MU in the dialog. When a Workpiece Carrier enters the AssemblyStation, Plant Simulation replaces the individual workpieces with new MUs.

**SimTalk:**
- `ExitingMU [SimTalk]`
- `NewMU [SimTalk] - AssemblyStation`

### Sequence [drop-down list] - AssemblyStation

Select the Sequence in which the AssemblyStation requests parts and/or services from the drop-down list.

- **MUs then Services** — The AssemblyStation requests the MUs before it requests the required services. Select this, if the services are not required until all mounting parts are available. The services are requested when all mounting parts have been moved to the AssemblyStation or have been deleted (compare Assembly Mode). When all mounting parts are available, set-up and processing operations can start, when the AssemblyStation has received the associated services.
- **Services then MUs** — The AssemblyStation requests the services before it requests the required MUs. Select this, if the services are already required for providing the mounting parts. The services are requested before the main part arrives, when the main part is ready to exit the preceding station. When the mounting parts arrive at the AssemblyStation, the Exporters are already located at the AssemblyStation. Set-up and processing procedures only start when all mounting parts are available. The mounting parts are moved to the main part or are deleted before the processing time starts (compare Assembly Mode). If the services are not available for the AssemblyStation, the mounting parts will not be moved to the main part or will not be deleted. The AssemblyStation then records a special Blocking Time.
- **MUs and Services** — The AssemblyStation requests the MUs and the services at the same time. Select this, if the services are already required for providing the mounting parts, but not for the assembly proper.

For the setting Services then MUs the services are requested before the main part arrives. When the AssemblyStation can receive the services immediately, it behaves identically for the settings Services then MUs and MUs and Services. If the AssemblyStation cannot receive the services, the mounting parts will be moved to the main part anyway and will then be deleted.

> **Note:** The AssemblyStation requests set-up services when the main MU enters or attempts to enter.

**SimTalk:**
- `OrderSequence [SimTalk]`

## Tab Times

Define Times as described under the Tab Times. Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (Const).

You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr [SimTalk]`.

## Tab Set-Up

Define properties for setting the object up as described under the Tab Set-Up.

## Tab Failures

Define failures as described under the Tab Failures.

## Tab Controls

Provides controls to modify the built-in behavior of the object.

### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog Select Object [for controls] and click OK. This inserts the name of the Method into the text box of the Control. Press `F2` in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

### Create a Control That is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control** [context menu]. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press `F2`.
- Or hold down `Shift` and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab User-defined and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

## Tab Exit

Select to which of its successors the object moves the MU on the Tab Exit.

## Tab Statistics

Statistics is described under the Tab Statistics. In addition, the AssemblyStation collects these statistical values:

| Item (English) | Description | Read-only attribute | Item (German) |
| --- | --- | --- | --- |
| Waiting Parts | Shows the portion of the statistics collection period during which the AssemblyStation was Waiting [state, material flow objects] for mounting parts. | `StatWaitingPartsPortion [SimTalk]` | Warten auf Teile |
| Waiting Resources | Shows the portion of the statistics collection period during which the AssemblyStation was waiting for Exporters and/or mounting parts. | `StatWaitingResPortion [SimTalk] - AssemblyStation` | Warten auf Ressourcen |

**Waiting Times** — To open the table Waiting Times, which shows the sum of the waiting times for mounting parts for each predecessor, click the button.

To view Waiting Times for Parts in the Statistics Report, select **View > Show Statistics Report** in the dialog of the object. You can also click the right mouse button in the Frame and select **Show Statistics Report** or you can press `F6`.

**Related SimTalk attributes:**
- `StatWaitingResPortion [SimTalk] - AssemblyStation`
- `StatWaitingResCount [SimTalk] - AssemblyStation`
- `StatWaitingPartsPortion [SimTalk]`
- `StatWaitingResDelta [SimTalk] - AssemblyStation`
- `StatWaitingPartsCount [SimTalk]`
- `StatWaitingResMu [SimTalk] - AssemblyStation`
- `StatWaitingPartsDelta [SimTalk]`
- `StatWaitingResTime [SimTalk] - AssemblyStation`
- `StatWaitingPartsMu [SimTalk]`
- `statWaitingTimePerPredecessor [SimTalk]`
- `StatWaitingPartsTime [SimTalk]`
- `statWaitingTimeTable [SimTalk]`

### Waiting Times

To open the Waiting Times table, which shows the sum of the waiting times for mounting parts for each predecessor, click this button.

> **Note:** Plant Simulation only shows Waiting Times for mounting parts. The Waiting Time for the main part always is 0.

> **Note:** Plant Simulation only shows Waiting Times if you selected None or Predecessors as the Assembly Table. For the settings MU Types and Depends on Main MU the button Waiting Times is unavailable as the AssemblyStation does not collect waiting times for them.

> **Note:** In the example the main part arrives along the connector from the SourceMainParts. As only waiting times for mounting parts are shown, the first row shows 0.

**SimTalk:**
- `statWaitingTimeTable [SimTalk]`

## Tab Importer

On the Tab Importer you can define services for processing the parts, for setting the station up for a certain type of part, and for repairing the station.

To view Importer Statistics in the Statistics Report, click the object in the Frame, and press `F6` (Show Statistics Report), or click Show Statistics Report on the Home ribbon tab. You can also click the object in the Frame with the right mouse button and select Show Statistics Report on the context menu.

To view Importer Statistics in the Statistics Report, do one of the following:

- Select **View > Show Statistics Report** in the dialog of the object.
- Click the object with the right mouse button in the Frame and select **Show Statistics Report** or press `F6`.
- Click **Show Statistics Report** on the Home ribbon tab.

## Tab Energy

Select energy settings for the object on the Tab Energy.

## Tab Costs

Select costs settings for the object on the Tab Costs. While the AssemblyStation adds mounting parts to a main part costs accrue which result from the sum of the investment costs and the operating costs.

> **Note:** The total investment costs only accrue during the Depreciation Period. The costs are allocated to the main part as accrued costs. Costs which accrued for the mounting parts so far, are transferred to the main part. If the AssemblyStation is empty, the costs remain with the AssemblyStation as general costs.

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

## Navigate Menu

The commands are described under the Navigate Menu.

## View Menu

The commands are described under the View Menu. It also provides the menu command **MUs To Be Deleted**.

**SimTalk:**
- `updateDialog [SimTalk]`

### MUs To Be Deleted

Opens a list with the MUs currently located on the AssemblyStation that it deletes when the main part exits.

**SimTalk:**
- `muToBeDeleted [SimTalk]`
- `musToBeDeleted [SimTalk]`
- `NumMUsToBeDeleted [SimTalk]`

## Tools Menu

The commands are described under the Tools Menu.

## Tabs Menu

Use the commands of the Tabs menu to show or hide individual tabs of the selected material flow objects. If you hide tabs that you do not need, Plant Simulation opens the dialog faster, and you can change to those tabs faster that you need in your daily work.

To apply the changed settings, click OK, close the dialog, and reopen it. The menu shows a check mark to the left of the displayed tabs. The command **Inherit** turns inheritance of the displayed or hidden tabs in the dialog off or on.

## Help Menu

The Help Menu provides these menu commands:

- Contents
- Help on Object

## Methods of the AssemblyStation

The AssemblyStation provides:

- The methods listed in the table of contents to the left.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
