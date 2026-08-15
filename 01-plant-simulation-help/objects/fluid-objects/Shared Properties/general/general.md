# General — Shared Properties of Fluid Objects

The Plant Simulation resource objects represent the Workers and the objects related to them for doing their jobs.

> **Compare the sample models:** Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog *Examples Collection*, and click **Open Model**.

## Shared Properties

The fluid objects share the following properties:

- Dialog Items of the Fluid Objects
- Methods of the Fluid Objects
- Read-Only Attributes of the Fluid Objects
- Attributes of the Fluid Objects

You will find the object-specific properties in the subchapters of the respective objects.

## Dialog Items of the Fluid Objects

The fluid objects share a number of dialog items and menus. To open the dialog box of an object, double-click its icon.

After opening the dialog, Plant Simulation shows the current values. Type new settings into the text boxes or select them from the drop-down lists. Click **OK** or **Apply** to accept changes and to update the dialog. Instead, you can also press **F5** to show the most current results of a simulation run on some of the tabs.

To edit the 3D properties of the object in the 3D model, select the object and press the **spacebar**. Then change the respective settings in the dialog *Edit 3D Properties*.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

### Shared dialog items and menus

- Inheritance [general description]
- Name [general description]
- Label [general description]
- Failed [check box] - material flow objects
- Paused/Planned/Unplanned [material flow objects]
- Entrance Locked [material flow objects]
- Exit Locked [material flow objects]
- Tab Set-Up [general description]
- Tab Failures [general description]
- Tab Controls [general description]
- Tab Exit [general description]
- Tab Statistics [material flow objects]
- Tab Importer [general description]
- User-defined Attributes [general description]
- OK / Cancel / Apply
- Navigate Menu
- View Menu
- Tools Menu
- Context Menu of Text Boxes in Dialogs
- Help Menu
- Tab Times [general description]
- States of the Material Flow Objects

## Entrance Locked [fluid objects]

To close the entrance of the fluid object, select this check box. If you lock the entrance of the fluid object, no material can flow into the object.

**Remarks:** Plant Simulation shows the State Graphic [defined] of a fluid object whose entrance is locked as a cyan-colored ring on a pole by default.

**SimTalk:** `EntranceLocked [SimTalk]` — fluid objects

## Exit Locked [fluid objects]

To close the exit of the fluid object, select this check box. If you close the exit of a fluid object, Plant Simulation prevents material from flowing off.

**SimTalk:** `ExitLocked [SimTalk]` — material flow objects

## Tab Statistics [fluid objects]

The fluid objects show the most important statistical data on the tab **Statistics**.

**Remarks:** The values for Waiting, Working, Blocked, Setting-Up, Failed, Stopped, Paused, and Unplanned should add up to 100 percent.

| Item (English) | Item (German) | Description |
| --- | --- | --- |
| Working | Arbeitend | Shows the portion of the statistics collection period during which the fluid object was Working. |
| Setting-up | Rüstend | Shows the portion of the statistics collection period during which the fluid object was setting up. |
| Waiting | Wartend | Shows the portion of the statistics collection period during which the fluid object was waiting. |
| Blocked | Blockiert | Shows the portion of the statistics collection period during which the fluid object was Blocked. |
| Failed | Gestört | Shows the portion of the statistics collection period during which the fluid object was Failed. |
| Paused | Pausiert | Shows the portion of the statistics collection period during which the fluid object was Paused. |
| Unplanned | Ungeplant | Shows the portion of the statistics collection period during which the fluid object was Unplanned, i.e., is not scheduled to work during the statistics collection period. |

Not all fluid objects provide all statistics values described above, while some fluid objects provide additional values that are described in the chapter of the respective object.

To view Resource Statistics of Stationary Resources in the Statistics Report, select **View > Show Statistics Report** in the dialog of the object. You can also click the right mouse button in the Frame and select **Show Statistics Report** or press **F6**.

## Navigate Menu

The commands are described under the Navigate Menu.

## View Menu

The View Menu provides commands to access its functions.

- Refresh [on View menu]
- Show Attributes and Methods [on View menu]
- Contents [material flow objects]
- Associated Lockout Zones
- Associated Shift Calendar
- Exit Blocking List (Portioner)
- Forward Blocking List (DePortioner)

The View Menu also provides these commands pertaining to the Transport Importer:

- Exporters [on View menu]
- Services [on View menu]
- Unavailable Services [on View menu]
- Associated Workplaces [on View menu]

## Tools Menu

The commands are described under the Tools Menu.

## Help Menu

The commands are described under the Help Menu.

## Methods of the Fluid Objects

The fluid objects provide:

- The Methods of All Objects.
- The Methods for Defining Failures.
- The Methods of the Importer.

The sub-chapters about the objects list additional methods for the fluid objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
