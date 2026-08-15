# ParallelStation

Use the object **ParallelStation** for modeling machines that process several parts in parallel at the same time.

## Description

The built-in properties of the ParallelStation are the same as those of the Station. The ParallelStation has several processing places, as opposed to the single processing place of the Station.

- A set-up time always applies if a MU has a different name than the part it processed before (its predecessor).
- Plant Simulation always moves the MU as a whole, not continually — as soon as its front is located on the ParallelStation, the entire MU is located on it.
- On the tab **MU Animation** you can set how the parts are distributed on the Animation Area of the ParallelStation.
- To show a tooltip with information about the ParallelStation, hover with the mouse over it.

To change the length of the graphic and the anchor points of the ParallelStation, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Showing Attributes and Methods

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the `F8` key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show them for the selected Instance.

You can set and get attribute values either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

Code examples:

```simtalk
-- To set the value of an attribute
MyStation.Pause := true

-- To get the value of an attribute
print MyStation.Pause
posit := MyStation.Cont.XPos
```

## Adding the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > MaterialFlow > ParallelStation** on the Home ribbon tab.

Compare the sample models: click the Window ribbon tab, then **Start Page > Getting Started > Example Models > Small Examples**, select the respective Category, Topic, and Example in the dialog *Examples Collection*, and click **Open Model**.

> **Note:** The TransferStation is based on a ParallelStation whose properties were modified and enhanced. For this reason, opening help of the TransferStation with `F1` opens help for the ParallelStation.

## Dialog Box of the ParallelStation

Double-click the icon of the ParallelStation to open its dialog box.

### Edit Simulation Properties
In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties
To edit the 3D properties in the dialog box **Edit 3D Properties**:
- Click the **Edit 3D Properties** button in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Tab Attributes

Define the number of processing places of the ParallelStation in a net of coordinates. The ParallelStation accesses the individual places using their x-coordinate and y-coordinate.

- Type the number of processing places on the x-axis into the text box **X-Dimension**.
- Type the number of processing places on the y-axis into the text box **Y-Dimension**.
- Activate **Start Processing When Full** if you want the ParallelStation to only start processing parts when each of the places contains a part.

### X-Dimension
Type the number of processing places of the ParallelStation along its X-axis.

- The capacity is represented by a two-dimensional net of coordinates. It is the product of Y-Dimension times X-Dimension. The greatest allowed value is ten million.

> **Note:** If you decrease the dimension of the object, make sure that no MUs are located on the places that will be deleted. If MUs are located on the object, the dimension is limited, as Plant Simulation neither deletes MUs outside of the new dimension automatically nor moves them to another processing place. If, for example, a MU is located at position (3,4), the new x-coordinate may not be less than 3, and the new y-coordinate may not be less than 4.

**SimTalk:** `XDim`, `YDim`, `Capacity`, `pe, [X,Y]`, `setDim`

### Y-Dimension
Type the number of processing places of the ParallelStation along its Y-axis.

- The capacity is represented by a two-dimensional net of coordinates. It is the product of Y-Dimension times X-Dimension. The greatest allowed value is ten million.
- The same note about decreasing dimensions and existing MUs applies.

**SimTalk:** `YDim`, `XDim`, `Capacity`, `pe, [X,Y]`, `setDim`

### Start Processing When Full (check box)
To make the ParallelStation only start processing parts when a part each is located on all of its processing places, select this check box. **This is the default setting.**

- When active, new parts can only enter the ParallelStation when it finished processing the current set of parts and when all parts have left again.
- If a part of another type wants to enter, it starts processing the parts that are already located on it even when it is not full. Only when the ParallelStation finished processing these parts and is empty again can parts of another type enter.
- If the ParallelStation does not have to be set up, parts of different types can also move onto it. Processing might then start with different Processing Times when the ParallelStation is full (applies to type-dependent and place-dependent processing times, and to a formula entered as the processing time).
- Use the method `startProcessing` to start processing parts even if the ParallelStation is not full yet.
- You can also select the setting **Recovery Time Starts > When processing is done** for the start of the Recovery Time. For the setting *When part exits*, the Recovery Time starts when the last part exits the station.

If you clear **Start Processing When Full**, the ParallelStation processes the parts immediately after they enter. New parts can enter at any time.

> **Note:** For the ParallelStation you can only deactivate **Automatic Processing** if **Start Processing When Full** is selected.

> **Note:** For processing-time-based failures of a ParallelStation, the simulated MTBF is reduced when the number of parallel processing operations of parts increases. The more parts are processed simultaneously, the sooner the failure occurs and the smaller the availability becomes. This prevents the Availability entered into the dialog from being reached. This does **not** apply when **Start Processing When Full** is activated.

**SimTalk:** `StartProcessingWhenFull`, `startProcessing`

## Tab Failures
Define failures as described under *Tab Failures*. The same processing-time-based failure note (reduced MTBF with more parallel operations) applies, and does not apply when **Start Processing When Full** is activated.

## Tab Times
Define times as described under *Tab Times*.

- Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab.
- You can also select a constant time (`Const`).
- Set the type of distribution and a complete set of parameters with the method `setTypeAndAttr`.

## Tab Set-Up
Define properties for setting the object up as described under *Tab Set-Up*.

> **Note:** The ParallelStation does not provide the setting **After n parts**.

## Tab Controls
Provides controls to modify the built-in behavior of the object.

**Select the Path to an Existing Method:**
- Click the ellipsis button, navigate to the location of the Method in the dialog *Select Object*, and click OK.
- Press `F2` in the text box to open the Method and type in the source code of the Control.
- Instead of *Select Object*, you can also drag the Method from a Frame and drop it into the text box.

**Create a Control That Is a Method of the Object:**
- Type a meaningful name into the text box and select **Create Control** on the context menu. Plant Simulation inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.
- Type the source code of this control into the Method that opens.

To edit the source code later:
- Press `F2`.
- Or hold down `Shift` and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.

> To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

## Tab Exit
Select to which of its successors the object moves the MU.

All blocking Exit Strategies of the ParallelStation, except for **MU Attribute**, do not determine a successor as soon as a MU cannot move. Plant Simulation enters all additional MUs into the Exit Blocking List. As soon as the first blocked MU is moved, Plant Simulation enters an Out event for all MUs contained in the Exit Blocking List, allowing them to move on.

## Tab Statistics
Statistics is described under *Tab Statistics*.

To view Resource Statistics of Stationary Resources in the Statistics Report, select **View > Show Statistics Report** in the dialog of the object, right-click in the Frame and select **Show Statistics Report**, or press `F6`.

## Tab Importer
On the Tab Importer you can define services for processing the parts, for setting the station up for a certain type of part, and for repairing the station.

To view Importer Statistics in the Statistics Report:
- Select **View > Show Statistics Report** in the dialog of the object.
- Right-click the object in the Frame and select **Show Statistics Report**, or press `F6`.
- Click **Show Statistics Report** on the Home ribbon tab.

## Tab Energy
Select energy settings for the object on the Tab Energy.

## Tab Costs
Select costs settings for the object on the Tab Costs.

While the ParallelStation processes parts, costs accrue which result from the sum of the investment costs and the operating costs.

> **Notes:**
> - The investment costs only accrue during the Depreciation Period.
> - The ParallelStation distributes the costs evenly across its processing places.
> - The costs are allocated to the part as accrued costs.
> - When a processing place of the ParallelStation is empty, the costs remain with the ParallelStation as general costs.

## Tab User-defined
Define your own attributes as described under *Tab User-defined*.

Related SimTalk methods: `getAttrName`, `getAttrNo`, `getAttrType`, `getAttrValue`, `NumAttr`, `setAttrType`, `setAttrValue`, `createAttr`, `deleteAttr`.

## Navigate Menu
The commands are described under the *Navigate Menu*.

## View Menu
The commands are described under the *View Menu*.

**SimTalk:** `updateDialog`

## Tools Menu
The commands are described under the *Tools Menu*.

## Tabs Menu
Use the commands of the Tabs menu to show or hide individual tabs of the selected material flow objects. Hiding unused tabs makes the dialog open faster.

- To apply the changed settings, click OK, close the dialog, and reopen it.
- The menu shows a check mark to the left of the displayed tabs.
- The command **Inherit** turns inheritance of the displayed or hidden tabs in the dialog off or on.

## Help Menu
The commands are described under the *Help Menu*.

## Methods of the ParallelStation

The ParallelStation provides:
- The methods listed in the table of contents to the left.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods** (select **Show Attributes and Methods** on the context menu of the Class Library, or press `F8` / click **Show Attributes and Methods** on the Home ribbon tab of the Frame).

## See Also
- Station [object]
- Define Processing Times of a ParallelStation
- Configure the Processing Stations
- Configure the Stations ProcessingA and ProcessingB
- Configure the Stations Which Handle the Pallet
- Video on YouTube: https://youtu.be/PQhEriOzVzU?si=XuPINjSUuC0pHfur&t=646
