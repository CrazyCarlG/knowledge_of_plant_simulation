# Cycle

## Description

Use the **Cycle** object to only move a part on to the next station within a balanced line when all stations have finished processing their parts, and when none of the stations is failed, paused, or unplanned. In addition, the successor of the balanced line has to be ready to receive the part.

To define the balanced line, type the name of the **First Station** and of the **Last Station** into the text boxes. All stations between the first and the last station, which are connected with Connectors, form the balanced line. Each station has to have a predecessor and a successor and can only have a single predecessor and a single successor.

## Notes

- At the moment only objects of type **Station** and **AssemblyStation** can be part of the balanced line. If an AssemblyStation is part of the balanced line, the Cycle only continues balancing if the assembly process has been finished.
- A **Front-triggered Exit Control** is only called for the last station of the cycle defined by the object Cycle, as the Destination for all other stations of the cycle is already set. Use a **Rear-triggered Exit Control** instead.
- A **Pull Control** is not called for the stations of the object Cycle.
- You can insert as many Cycle objects as you need into your simulation model. They all work independent of each other. If you use several Cycle objects, make sure to only assign each station to a single Cycle object.

## Defining the Balanced Line by Drag-and-Drop

- If you did not define any stations for the balanced line yet, drag a Station or an AssemblyStation onto the icon of the object Cycle and drop it there. Plant Simulation enters it as the **first** station of the balanced line.
- If you drag another object onto it and drop it there, Plant Simulation enters it as the **last** station.
- If you already defined the last station and would like to change it, hold down **Shift**, drag the object you would like to use as the last station over the Cycle, and drop it there. The status bar shows which object you are setting.

To show a tooltip with information about the Cycle, hover with the mouse over it.

## Graphic Manipulation

To change the length of the graphic and the anchor points of the Cycle, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Adding the Object to the Simulation Model

To add the object Cycle to your simulation model, click **Manage Class Library > Basic Objects > MaterialFlow > Cycle** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog *Examples Collection*, and click **Open Model**.

## Dialog Box of the Object Cycle

Double-click the icon of the Cycle to open its dialog box.

### Edit Simulation Properties
In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties
To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:
- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the **spacebar**.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Tab Attributes

The tab **Attributes** provides the settings which the object offers. The shared properties are described under the *Tab Attributes*.

### Active [check box]

To synchronize the transfer of MUs from station to station, select this check box. To deactivate line balancing, clear the check box.

**Remarks:** After synchronizing, a part is only moved on to the next station within the balanced line when all stations have finished processing their parts and when none of the stations is failed, paused or unplanned.

**SimTalk:**

```simtalk
Active
```

### First Station

Type in the name of the first station of the group of stations which you want to balance. Or click the ellipsis button and select a material flow object in the dialog *Select Object*.

**Remarks:** All stations between the First Station and the Last Station which are connected with Connectors form the balanced line.

**SimTalk:**

```simtalk
GetFirstStation
setFirstAndLastStation
```

### Last Station

Type in the name of the last station of the group of stations which you want to balance. Or click the ellipsis button and select a material flow object in the dialog *Select Object*.

**Remarks:** All stations between the First Station and the Last Station, which are connected with Connectors, form the balanced line.

**SimTalk:**

```simtalk
GetLastStation
setFirstAndLastStation
```

### Empty Cycle Allowed [check box]

To allow parts on the balanced stations to be moved on, although no part is ready to move on from the predecessor of the balanced line, select this check box. This results in an idle cycle.

**SimTalk:**

```simtalk
EmptyCycleAllowed
```

### Part Can Only Enter on Cycle [check box]

To allow parts to enter the Cycle only if the cycle moves all MUs by one station on and is thus empty, select this check box.

**Remarks:** To allow parts to enter the Cycle at any time, clear the check box.

**SimTalk:**

```simtalk
EntranceOnlyOnCycle
```

## Tab Statistics

Statistics is described under the *Tab Statistics*. To view **Resource Statistics** of Stationary Resources in the Statistics Report, select **View > Show Statistics Report** in the dialog of the object. You can also click the right mouse button in the Frame and select **Show Statistics Report**, or press **F6**.

See also: *Resource Statistics [check box]*, *Resource Type*.

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

## Navigate Menu

The commands are described under the *Navigate Menu*.

## View Menu

The View Menu provides commands to access its functions:
- Refresh [on View menu]
- Show Attributes and Methods [on View menu]

**SimTalk:**

```simtalk
updateDialog
```

## Tools Menu

The commands are described under the *Tools Menu*.

## Help Menu

The commands are described under the *Help Menu*.

## Methods of the Object Cycle

The object Cycle provides:
- The method `setFirstAndLastStation`.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.
