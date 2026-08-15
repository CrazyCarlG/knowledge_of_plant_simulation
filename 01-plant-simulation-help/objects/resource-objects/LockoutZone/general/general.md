# LockoutZone

Use the object **LockoutZone** for combining a group of material flow objects. If one of these stations fails, all other stations within the lockout zone stop processing their parts as well.

The LockoutZone controls the failures of all stations. It then returns the total availability of the assigned stations.

## Description

- You can insert more than one LockoutZone into a simulation model. The LockoutZones can overlap, meaning that a station can be assigned to more than one LockoutZone.
- You have to define failure profiles for at least one of the stations assigned to the LockoutZone. As soon as one of the stations fails, the LockoutZone stops all processing operations of all assigned stations, meaning it sets their attribute `Stopped` to `true`. You can select if the LockoutZone stops the processing operations immediately or when the service arrives.
- The stations only start processing parts again after all failures were removed. They then only use up the respective remaining processing time.
- You can also determine what happens if the stations start processing parts again by programming a **Resume Control**.
- In case one of the stations is paused if the LockoutZone intends to stop, this station does not start or restart processing after the pause is over.
- You can assign any of the built-in Material Flow Objects or Fluid Objects to the LockoutZone. For stations you modeled yourself in a Frame, the LockoutZone sets the attribute `Stopped` of that Frame to `true`. You then have to model an adequate reaction to the attribute. In addition, you can also add a Worker or the WorkerPool.
- If the station that triggers the lockout zone is assigned to more than one LockoutZone, all stations of all LockoutZones will be stopped. If the station that triggers the lockout zone is assigned to only one LockoutZone, it only stops the station that you assigned to it.
- To show a tooltip with information about the LockoutZone, hover with the mouse over it.
- To change the length of the graphic and the anchor points of the LockoutZone, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Add the Object to the Simulation Model

To add the object LockoutZone to your simulation model, click **Manage Class Library > Basic Objects > Resources > LockoutZone** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog Examples Collection, and click Open Model.

## Dialog Box of the LockoutZone

Double-click the icon of the LockoutZone to open its dialog box.

- **Edit Simulation Properties**: In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.
- **Edit Animation Properties**: To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:
  - Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
  - Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Active [check box]

To activate the LockoutZone, select this check box. It then creates failures and stops the processing operations of all assigned objects when one of these stations fails. To deactivate it, clear the check box.

**SimTalk**: `Active [SimTalk] - LockoutZone`

## Tab Controls

Provides controls to modify the built-in behavior of the object.

### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog *Select Object [for controls]* and click OK. This inserts the name of the Method into the text box of the Control.

Press `F2` in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing *Select Object*, you can also select the Method in a Frame, drag it to the text box and drop it there.

### Create a Control That is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press `F2`.
- Or hold down Shift and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab User-defined and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

Specifying a control overrules the default behavior of the LockoutZone. This means that you yourself are responsible for stopping all processing operations of the assigned objects by assigning `true` to their attribute `Stopped`.

When you want the objects to continue processing parts, you have to make sure to terminate stopped mode by assigning `false` to the attribute `Stopped`.

## Stop Control

Modifies the built-in behavior of the object. The object calls the Stop Control if one of the stations assigned to the LockoutZone fails and thus stops processing parts.

The anonymous identifier `@` designates the triggering station, the anonymous identifier `?` designates the LockoutZone.

**SimTalk**: `StopCtrl [SimTalk]`

## Resume Control

Modifies the built-in behavior of the object. The object calls the Resume Control when all failures of the assigned stations were removed and the stations can thus resume processing parts.

**SimTalk**: `ResumeCtrl [SimTalk]`

## Stop Mode [drop-down list]

Select the Stop Mode of the LockoutZone. You can select one of these settings:

- **Stop immediately**
  Stops the processing operations of all stations that are part of the LockoutZone as soon as one of the stations assigned to it fails. None of the other stations in the model are stopped!
  Within this period of time additional failures can take place for the assigned stations, several failures of differing stations can thus overlap. The stations only start processing parts again after all failures were removed. They then only use up the remaining processing time.
- **Stop when Service arrives**
  Only stops the stations assigned to the LockoutZone when the repair services, which the failed station requested, are assigned. Depending on your modeling situation this can be at a different point in time.
  If you model Footpaths on which the Worker walks to the station, Plant Simulation considers the Worker as received once he has reached the station. For Exporters/Workers who can be beamed, the service is considered to be received once the Broker has assigned the service. This matches the behavior of the Receive Control.

The LockoutZone does not affect the Recovery Time and the Cycle Time of the stations which it controls. The LockoutZone stops these objects and records statistics values for the state `Stopped`. If you deactivate the LockoutZone while it is in the process of stopping other stations, Plant Simulation immediately releases all objects stopped by the LockoutZone. If you reset your model, all objects change their state from stopped to operational.

**SimTalk**: `StopMode [SimTalk]`

## Tab Objects

Assign resources to the LockoutZone on the tab Objects.

A resource is any of the built-in Material Flow Objects, or a Frame in which you modeled a machine, whose Working hours you would like to control with the LockoutZone. In addition, you can also add a Worker or the WorkerPool.

### Objects [LockoutZone]

Assign resources, i.e., material flow objects or fluid objects, to the LockoutZone.

Proceed as follows:

- Before you can type in data, click the **Inheritance** check box.
- Type the path to and the name of the resource object in a cell. Or
- Drag the resource object to the icon of the LockoutZone and drop it there. You can also select and then drag-and-drop multiple objects at the same time!

You can manipulate the contents of the list window with the commands of the *Context Menu of Embedded Lists*.

**SimTalk**: `addObject [SimTalk] - LockoutZone`, `Objects [SimTalk] - LockoutZone`

## Tab Statistics

The tab Statistics shows the most important statistical data of the LockoutZone.

| Item | Description | Read-only attribute |
|------|-------------|---------------------|
| Stopped Portion | Shows the portion of the statistics collection period during which the stations were stopped by a LockoutZone in percent. | `StatStoppedPortion [SimTalk] - LockoutZone` |
| Stopped Count | Shows how often the LockoutZone stopped the stations. | `StatStoppedCount [SimTalk] - LockoutZone` |
| Stopped durations total time | Shows the total time during which the LockoutZone stopped the processing operations of the assigned stations. | `StatStoppedTime [SimTalk]` |
| Stopped durations mean time | Shows the mean time during which the LockoutZone stopped the processing operations of the assigned stations. | `StatStoppedMu [SimTalk] - LockoutZone` |
| Stopped durations Standard Deviation | Shows the standard deviation of the time during which the LockoutZone stopped the processing operations of the assigned stations. | `StatStoppedDelta [SimTalk] - LockoutZone` |
| Stopped intervals mean time | Shows the mean time of the intervals during which the LockoutZone stopped the processing operations of the assigned stations. | `StatStoppedIntervalMu [SimTalk]` |
| Stopped intervals Standard Deviation | Shows the standard deviation of the intervals during which the LockoutZone stopped the processing operations of the assigned stations. | `StatStoppedIntervalDelta [SimTalk]` |

The Statistics Report shows the Stopped Time of the individual material flow objects.

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

## Navigate Menu

The commands are described under the *Navigate Menu*.

## View Menu

The View Menu provides commands to access its functions:

- Refresh [on View menu]
- Show Assigned Objects [LockoutZone]
- Show Attributes and Methods [on View menu]

**SimTalk**: `updateDialog [SimTalk]`

### Show Assigned Objects [LockoutZone]

Selects the objects which are assigned to the LockoutZone as resources in the Frame window.

Instead, you can also select **Show Assigned Objects [in Frame]** on the context menu of the LockoutZone in the Frame.

## Tools Menu

The Tools Menu provides these menu commands:

- Edit Controls
- Edit Observers

## Help Menu

The commands are described under the *Help Menu*.

## Methods of the LockoutZone

The LockoutZone provides:

- The method `addObject [SimTalk] - LockoutZone`.
- The *Methods of All Objects*.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the `F8` key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.
