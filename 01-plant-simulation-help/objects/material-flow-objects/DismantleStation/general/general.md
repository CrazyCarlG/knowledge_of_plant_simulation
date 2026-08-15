# DismantleStation

Use the object **DismantleStation** to model dismantle processes, i.e., for removing mounting parts from a main part in your plant.

## Description

The DismantleStation removes mounting parts from a main part. To model assembly operations, use the **AssemblyStation**.

Normally the **Dismantle Table** or the setting **Main MU to Successor with Number** determine the successor number to which the DismantleStation moves the part. If you want the Worker to carry all parts to a certain target, enter this object as the **MU Target** on the tab **Importer > Transport**. In this case Plant Simulation overwrites the above settings.

- Hover with the mouse over the object to show a tooltip with information about the DismantleStation.
- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.

### Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > MaterialFlow > DismantleStation** on the Home ribbon tab.

Compare sample models: click the **Window** ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then select the respective Category, Topic, and Example in the dialog **Examples Collection**, and click **Open Model**.

## Dialog Box of the DismantleStation

Double-click the icon of the DismantleStation to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under **Dialog Items of the Objects**.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the **spacebar**.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M**.

## Tab Attributes

The tab **Attributes** provides the settings that the object offers. Set how the DismantleStation removes parts from the main part or creates new parts on this tab. The shared properties are described under the **Tab Attributes**.

### Sequence [drop-down list]

Select how the DismantleStation distributes the dismantled MUs to its successors.

You can select one of these settings:

- **MUs to all Successors**:
  - Select **Create MUs** from the drop-down list **Dismantle Mode**, to make the DismantleStation create a new MU for each successor and move that MU there. The DismantleStation moves the main MU to the successor whose number you typed into the text box **Main MU to Successor with Number**.
  - Select **Detach MUs** from the drop-down list **Dismantle Mode**, to make the DismantleStation move the MUs to each successor in turn, except for the successor that receives the main MU. The DismantleStation moves the main MU to the successor whose number you typed into the text box **Main MU to Successor with Number**. If the DismantleStation has four successors, and moves the main MU on to successor number 2, it passes the new MU on to successors 1, 3, and 4, and moves the main MU to successor 2.

For these settings you have to fill out the **Dismantle Table**:

- **MUs exiting independent of other MUs**: The DismantleStation attempts to move the main MU, and after that each MU, on to the successor you defined, as soon as possible.
- **Main MU after other MUs**: The DismantleStation first moves the mounting parts on to the successor, and then the main MU.

If you only want to unload those mounting parts from the main part that you type into the Dismantle Table, select **MUs exiting independent of other MUs** or **Main MU after other MUs** and the Dismantle mode **Detach MUs**. Always type a valid MU class into the column **MU** and a positive number into the column **Number**.

### Dismantle Table [button]

To open the Dismantle Table, click this button. The DismantleStation opens a table with three columns:

- Type the path to the class of the MUs into the column **MU**, such as `.MUs.Part`, `.MUs.Container`, or `.MUs.Transporter`. Alternatively, leave the entry empty to designate any MU class.
- Type the number of MUs that are dismantled into the column **Number**. Type `-1` to dismantle all parts. If you do not enter a number, the DismantleStation uses the default value `1`.
- Type the number of the successor into the column **Successor**. If you do not type in a value, the DismantleStation moves the mounting parts to successor number 1 for the setting **Dismantle Mode > Detach MUs**. For **Dismantle Mode > Create MUs**, it moves the MUs to the successor to which the main MU moves.

> **Note:** If you type in a **MU Target**, the Worker carries all MUs to this target. If you do not type in a MU Target, the Dismantle Table or the setting **Main MU to Successor with Number** determine it.

Depending on what you select from the drop-down list **Dismantle Mode** (**Create MUs** or **Detach MUs**), the DismantleStation creates the corresponding MUs or searches the table for the successor to which it moves them. In the latter case the Dismantle Table may contain more information than is required for moving the MUs.

If you only want to unload those mounting parts from the main MU that you type into the Dismantle Table, select **Sequence > MUs exiting independent of other MUs** or **Main MU after other MUs** and **Dismantle Mode > Detach MUs**. Always type a valid MU class into **MU** and a positive number into **Number**.

To automatically move all MUs according to their MU class to a successor:

- Type in any MU class into the column **MU** of the Dismantle Table.
- Type `-1` into the column **Number** to designate all remaining parts of this class.
- Type in the number of the desired successor into the column **Successor**.
- Repeat this for additional MU classes.

To automatically move all MUs to a successor:

- Leave the column **MU** in the Dismantle Table empty to designate any MU class.
- Type `-1` into the column **Number** to designate all remaining parts of this class.
- Type in the number of the desired successor into the column **Successor**.

### Dismantle Mode [drop-down list]

Select the Dismantle Mode, i.e., how the DismantleStation handles the mounting parts.

- **Detach MUs**: The DismantleStation detaches the mounting parts from the main MU and moves them on to the successor you typed into the Dismantle Table. If you only want to unload those mounting parts from the main MU that you type into the Dismantle Table, select **Sequence > MUs exiting independent of other MUs** or **Main MU after other MUs** and **Dismantle Mode > Detach MUs**. Always type a valid MU class into **MU** and a positive number into **Number**.
- **Create MUs**: The DismantleStation creates mounting parts.

### Main MU to Successor with Number [text box]

Type in the number of the successor to which the DismantleStation moves the main MU.

- If you type in a **MU Target**, the Worker carries all MUs to this target.
- If you do not type in a MU Target, the Dismantle Table or the setting **Main MU to Successor with Number** determine it.
- You cannot use `0` to send the main MU on. If you type in `0` and click **Apply** or **OK**, Plant Simulation changes `0` to the default value `1`. If you assign `0` to the attribute **Main MU**, Plant Simulation shows an error message.

### Exiting MU [drop-down list]

Select the Exiting MU, i.e., how the DismantleStation moves the main MU or a new MU on to its successor.

- **Main MU**: The DismantleStation moves the main MU on to the succeeding object.
- **New MU**: The DismantleStation deletes the main MU, creates a new MU, and moves it on to the successor. The DismantleStation then shows the text box **MU**. Type the path to the class of the new MU into the text box, or click the button and select the new MU in the dialog **Select Object**.

## Tab Times

Define Times as described under the **Tab Times**. Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (**Const**). You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr`.

## Tab Set-Up

Define properties for setting the object up as described under the **Tab Set-Up**.

## Tab Failures

Define failures as described under the **Tab Failures**.

## Tab Controls

Provides controls to modify the built-in behavior of the object.

Plant Simulation calls the **Exit Control** for each leaving part. When you only call the method `@.move`, Plant Simulation moves the part at the same successor that would receive it without Exit Control.

### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog **Select Object [for controls]** and click **OK**. This inserts the name of the Method into the text box of the Control.

Press **F2** in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing **Select Object**, you can also select the Method in a Frame, drag it to the text box and drop it there.

### Create a Control That is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control** [context menu]. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens. To edit the source code later on:

- Press **F2**.
- Or hold down **Shift** and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

## Tab Statistics

Statistics is described under the **Tab Statistics**. In addition, the DismantleStation shows the button **Blocking Times**.

To view Resource Statistics of Stationary Resources in the Statistics Report, select **View > Show Statistics Report** in the dialog of the object. You can also click the right mouse button in the Frame and select **Show Statistics Report**, or press **F6**.

### Blocking Times [table]

To open the table **Blocking Times**, which shows the sum of the blocking times of the MUs per successor, click this button.

## Tab Importer

Define services for processing the parts, for setting the station up for a certain type of part, and for repairing the station on the **Tab Importer**.

> **Note:** If you want the Worker to carry all parts to a certain target, enter this object as MU target on the tab **Importer > Transport**. In this case Plant Simulation overwrites the settings **Dismantle Table** or **Main MU to Successor with Number** to determine the successor number to which the DismantleStation moves the part.

To view Importer Statistics in the Statistics Report, click the object in the Frame and press **F6** (**Show Statistics Report**), or click **Show Statistics Report** on the Home ribbon tab. You can also right-click the object in the Frame and select **Show Statistics Report** on the context menu.

## Tab Energy

Select energy settings for the object on the **Tab Energy**.

## Tab Costs

Select costs settings for the object on the **Tab Costs**.

While the AssemblyStation adds mounting parts to a main part, costs accrue which result from the sum of the investment costs and the operating costs.

> **Note:** The total investment costs only accrue during the Depreciation Period. The costs are allocated to the main part as accrued costs. Costs which accrued for the mounting parts so far are transferred to the main part. If the AssemblyStation is empty, the costs remain with the AssemblyStation as general costs.

## Tab User-defined

Define your own attributes as described under the **Tab User-defined**.

## Navigate Menu

The commands are described under the **Navigate Menu**.

## View Menu

The View Menu provides commands to access its functions:

- Refresh [on View menu]
- Show Statistics Report [on View menu]
- Show Attributes and Methods [on View menu]
- Contents [DismantleStation]
- Forward Blocking List
- Exit Blocking List
- Exporters [on View menu]
- Services [on View menu]
- Unavailable Services [on View menu]
- Associated Workplaces [on View menu]
- Exiting MUs
- Associated Lockout Zones
- Associated Shift Calendar

### Contents [DismantleStation]

Opens a list containing all MUs that were dismantled on the DismantleStation.

### Exiting MUs

Opens a table displaying the MUs located at present on the DismantleStation, and which it deletes when it moves the main part onto the Successor contained in column 2 of the table.

## Tools Menu

The commands are described under the **Tools Menu**.

## Tabs Menu

Use the commands of the Tabs menu to show or hide individual tabs of the selected material flow objects. If you hide tabs that you do not need, Plant Simulation opens the dialog faster, and you can change to those tabs faster that you need in your daily work.

- To apply the changed settings, click **OK**, close the dialog, and reopen it.
- The menu shows a check mark to the left of the displayed tabs.
- The command **Inherit** turns inheritance of the displayed or hidden tabs in the dialog off or on.

## Help Menu

The commands are described under the **Help Menu**.

## Methods of the DismantleStation

The DismantleStation provides:

- The methods listed in the table of contents to the left.
- The **Methods of the Material Flow Objects**.
- The **Methods of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## See Also

- AssemblyStation
- Remove Parts with the Dismantle Station
- Video on YouTube: https://youtu.be/yEAqrVDBsns?si=rLxurb7Z5n4OVpJX&t=407
