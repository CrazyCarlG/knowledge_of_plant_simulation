# The Frame Window

The Frame Window provides access to the most important functions you need for creating your simulation model.

## Remarks

The Frame window provides the **Frame Ribbon Tab** and the **System Menu**.

- The **Context Menu of the Frame Itself** provides commands pertaining to the Frame. To edit the 3D properties of the Frame in the 3D model, press the spacebar, then change settings in the dialog **Edit 3D Properties**.
- The **Context Menu of the Selected Object in the Frame** provides commands pertaining to that object. You can edit the simulation properties of the object there. To edit the 3D properties of the selected object, press the spacebar.

### See also
- Work with Objects in the Frame Window
- Add a Background Graphic to the Frame
- Drag-and-Drop While Modeling
- `setXYWH` [SimTalk], `getXYWH` [SimTalk]
- `RootFrame` [SimTalk]
- `setPosition` [SimTalk]

---

# Drag-and-Drop While Modeling

Drag-and-drop in the Frame while modeling performs a number of actions.

The row `Class Library — Class Library — object — Ctrl` in the table means: dragging an object from the Class Library from one location to another location in the Class Library while holding **Ctrl** down copies the object to that location.

| To do this | Drag from | To | Type |
|---|---|---|---|
| Move the object | Class Library | Class Library | object | Shift |
| Copy the object | Class Library | Class Library | object | Ctrl |
| Derive the object | Class Library | Class Library | object | Ctrl+Shift |
| Instantiate the object | Class Library | Frame | object | — |
| Move the object (makes a class out of the instance) | Frame | Class Library | object | — |
| Copy the object | Frame | Class Library | object | Ctrl |
| Load a graphics file (.GIF, .BMP, .PPM, .PPM RAW, .DXF, or .DWG) as the background graphic of the Frame | Windows Explorer | Frame | file | — |
| Insert the selected object repeatedly | Class Library | Frame | object | Shift |
| Execute a Method, which expects a single parameter of data type object with this object as parameter | Object from Frame | Method | single parameter of data type object | — |

---

# System Menu of the Frame

The system menu shows commands with which you can manipulate or close the Frame window.

> **Note:** Plant Simulation displays the system menu in the language of Windows that is installed on your computer.

## Use Left Area
Uses the left part of the usable area of the MDI window in which Plant Simulation shows the object windows.

## Use Right Area
Uses the right part of the usable area of the MDI window in which Plant Simulation shows the object windows.

## Restore
Restores the Plant Simulation window to normal size.

## Move [window position]
Changes the window position of the Frame window in the Plant Simulation window.

## Size [window position]
Changes the size of the Frame window in the Plant Simulation window.

## Minimize
Reduces the size of the Frame window to an icon in the task bar of the Plant Simulation window.

## Maximize
Enlarges the size of the Frame window to fill the entire Plant Simulation window. When the Frame window is maximized, Plant Simulation adds the button combination Minimize, Maximize, Close to the Ribbon Bar.

## Close [Frame window]
Closes the Frame window.

---

# Frame Ribbon Tab

The Frame ribbon tab provides commands to access the functions of the Frame.

| Command | Method or Attribute |
|---|---|
| Find Object [button] | — |
| Incremental Find Object | — |
| Show Unconnected Objects | — |
| Select Shift Calendar | `ShiftCalendarObject` [SimTalk] - Frame |
| Configure User-defined Ribbon Tab | — |
| Inherit User-defined Ribbon Tab | — |
| Configure User-defined Context Menu | — |
| Inherit User-defined Context Menu | — |
| Replacement Mode | — |
| Merge / Exchange | — |
| Inherit Replacement Mode | `replace` [SimTalk], `ReplacementMode` [SimTalk] |
| Lock Structure [Frame ribbon] | `LockStructure` [SimTalk] |

> **Note:** The other tabs on the Ribbon Bar provide additional commands pertaining to the Frame.

## Find Object [button]
Opens the dialog **Find Object**.

To search for any object in the Frame window, you can also click in the Frame window and start typing its name. Plant Simulation then finds and selects the object.

## Incremental Find Object
Clicking the button and starting to type the name of the object you want to find finds and highlights that object in the opened Frame window.

Plant Simulation shows the characters you type in the status bar. You can type all characters which are allowed for object names. As upper- or lower-casing is not distinguished in object names, you can start typing with lower-case letters.

As soon as Plant Simulation finds an object that matches these characters, it selects that object and zooms to it in the 3D scene. To return to the last active scene before the search, press **Backspace**.

Keys to control Incremental Find Object:
- **Backspace** — delete the last character you typed.
- **Tab** — find the next matching object. If no additional object is found, it selects the first object again and plays a signal tone.
- **Esc** — terminate; retains the current selection.
- **Return** — terminate and execute the default operation of Return for the object (e.g., open the simulation properties dialog).

> **Note:** To find the name of an object in an open folder in the Class Library, press **Ctrl+I** and start typing.

## Show Unconnected Objects
Highlights those objects in the open Frame window that have unconnected entrance and exit points (not connected to any other object with a Connector). A Frame counts as unconnected if one of its Interfaces is not connected to the outside.

## Select Shift Calendar
Sets the ShiftCalendar which contains the data of the shifts in your installation and controls during which shifts the Frame works.

- SimTalk: `ShiftCalendarObject`, `Unplanned` [SimTalk]

## Configure User-defined Ribbon Tab
Creates a user-defined ribbon tab in the selected Frame with commands that you frequently use.

Plant Simulation adds the user-defined ribbon tab to the predefined ribbon tabs of the Frame. When a user-defined ribbon tab exists, the button on the Frame ribbon tab is highlighted.

You can:
- Add an Icon to a Ribbon Command
- Create a Ribbon Group
- Dynamically Add a Ribbon Command
- Add a Command Separator
- Create an Access Key

> **Note:** To create a ribbon tab in a Frame which you inserted into another Frame, deactivate the command **Inherit** first.

### Title [user-defined ribbon tab]
Type in the Title of the user-defined ribbon tab. SimTalk: `UserMenuTitle` [SimTalk].

### Active [check box] - user-defined ribbon tab
Select this check box to show and activate the user-defined ribbon tab. Clear it to deactivate and hide it. SimTalk: `ShowUserMenu` [SimTalk].

> **Note:** If the user-defined ribbon tab calls a Method, Plant Simulation assigns the anonymous identifier `?` to the respective Frame.

### New [ribbon command]
To add a new ribbon command, click this button. Plant Simulation then adds a row to the table.

Proceed as follows:
- Type in the Name of the ribbon command that the Frame window is to show.
- Type in the Method that the ribbon command is to execute.

### Text to Display [user-defined ribbon tab]
Type in the name of the command that Plant Simulation shows on the user-defined ribbon tab. Then select or type in the name of the Method to Execute in the cell to the right.

You can select the following in front of a ribbon command or a group label:
- **`?Formula`** — designate a formula that computes the text used as the label of a group or command.
- **`- Separator`** (hyphen) — insert a group separator.
- **`#`** (no text after) — designate the end of the previous group and start a new unnamed group.
- **`#Group Name`** — start a new ribbon group with the name you enter.
- **`#GroupNameFormula`** — start a new ribbon group using a formula.
- Type two or more hyphens `--` or number signs `##` to show them literally.

If one of the ribbon commands or group labels is dynamic (computed by a formula), the user-defined ribbon category is updated each time it comes into view.

SimTalk: `UserMenu` [SimTalk]

### Create a Ribbon Group
Type in or select the number sign `#` in front of the first command to start a ribbon group on the ribbon tab. Ribbon groups group a number of related commands and are separated by long vertical lines.

Any text following the `#` is used as the name of this ribbon group. If you just enter `#` and no text afterward, Plant Simulation considers this as the end of the previous group and starts a new group without a ribbon label.

The command can also be a formula (dynamic). If a formula creates the Text to Display, Plant Simulation checks the text for line breaks. If line breaks exist, it splits the text and uses it as:
- Name of the ribbon command
- Caption of the tooltip of the ribbon command
- Description of the ribbon command in the tooltip

Example:
```
"Statistics Report\nShow the statistics report.\nGenerates the statistics report of the selected object and shows it."
```

### Add an Icon to a Ribbon Command
To add an icon to a ribbon command:
- Create a new object icon. Specify 16 by 16 pixels and/or 32 by 32 pixels as the size. Name the icon to match the label of the ribbon command.

Naming conventions:
- Use `My Command 1_16` or `My Command 1_32` to indicate the size. If you do not specify the size, Plant Simulation finds the icon but will not document its desired usage in its name.
- Use `ribbon`, independent of the label, and append the number of the command, for example `ribbon1`.
- Plant Simulation resolves the icon name in this sequence:
  1. Ribbon command label with appended size
  2. Ribbon command label without appended size
  3. Icon names which are independent of the label

Plant Simulation chooses the size of the displayed icon based on available space:
  1. If space is tight, it uses the 16 by 16 pixel icon.
  2. If more space is available, it uses the 32 x 32 pixel icon.

> **Note:** If you use a formula for the label, Plant Simulation uses the result of this formula to search for the icon. To prevent problems, name ribbon command icons in a standardized way using `ribbon` and the command number. If you do not type a Method to Execute, Plant Simulation dims the icon.

### Dynamically Add a Ribbon Command
Select `?Formula` and then type over `Formula` in the cell with the name of your formula to use it as a ribbon command.

When you type `?Method1`, the method named `Method1` is called. The return value must be of data type **string**. This way you can toggle between captions (e.g., Activate/Deactivate) and translate commands into different languages. If the methods return an empty string `""`, Plant Simulation hides the respective command.

You can use any formula, even a method call with parameters, such as `?Method1(42)` or a table access, such as `?MyDataTable[1,3]`.

### Add a Command Separator
Type in or select `- Separator` followed by the category name as the Text to Display to insert a vertical separator between groups of ribbon commands.

### Create an Access Key
Type the ampersand character `&` in front of a letter of a command to make this letter the access key (mnemonic key). Plant Simulation activates this command when you press **Alt** and that letter.

If you do not type the ampersand, Plant Simulation assigns an automatically numbered access key. Built-in access keys take precedence over any access keys you define.

> **Note:** You can only create access keys for menu items on a menu, not for dialog items in the dialog itself.

### Method to Execute [user-defined ribbon tab]
Type in the name of the Method, which the Text to Display calls and executes.

When Methods are called by the user-defined ribbon tab, the anonymous identifier `?` points to the Frame in which the selection was executed.

**Parameter:** If the method to execute expects a parameter, Plant Simulation automatically passes it. The objects which you selected in the Frame are passed to this parameter, which has to be of data type **list** or an array of data type **object**.

Example:
```
?.MyStation.proctime := str_to_time(prompt)
```

SimTalk: `UserMenu` [SimTalk]

### Delete [ribbon command]
To delete a command from the user-defined ribbon tab, select the row and click this button.

### Inherit User-defined Ribbon Tab
Turns inheritance for a ribbon tab which you create in a Frame that you inserted into another Frame on or off.
- Turn inheritance on to make any Frame derived from the active Frame inherit the ribbon tab of its origin.
- Turn it off to define a ribbon tab that only applies to the active Frame.

---

# Context Menu of the User-defined Ribbon Tab

The context menu of the user-defined ribbon tab and the user-defined context menu provides row-editing commands.

## Insert Row
Inserts an empty row above the selected row. Hold **Shift** and click Insert Row to insert below the selected row.

## Delete Row
Deletes the selected row from the table.

## Cut Row
Cuts the selected row, converts the data to text, and places it on the clipboard. Plant Simulation separates the two columns of the cut row with a tab stop.

## Copy Row
Copies the selected row, converts the data to text, and places it on the clipboard. Columns are separated with a tab stop.

## Paste Row
Pastes the data of the row from the clipboard to the table. Plant Simulation looks for line breaks and tabulators and separates the text accordingly.

To control where Plant Simulation pastes the row:
- Click in the row and select Paste Row to replace the current row (or paste at the end without overwriting).
- Hold **Ctrl** and select Paste Row to paste above the current row (does not overwrite).
- Hold **Ctrl+Shift** and select Paste Row to paste below the current row (does not overwrite).

## Keyboard Shortcuts

| To do this | Press |
|---|---|
| Copy the current row to the clipboard | Ctrl+C or Ctrl+Ins |
| Cut the current row to the clipboard | Ctrl+X or Shift+Del |
| Paste the contents of the clipboard | Ctrl+V or Shift+Ins |
| Insert the new row above the current row | Ins / Ctrl+ + / Ctrl+Num+ |
| Insert the new row below the current row | Ctrl+Shift+ + / Ctrl+Shift+Num+ |
| Delete the selected row | Del |
| Edit the selected row | F2 |
| Open the Method Editor for the Method in the current row | Shift+F2 |
| Open the drop-down list for selecting items | F4 |
| Create a user-defined method/control | Shift+F4 |

---

# Attributes of the User-defined Ribbon Tab

## ShowUserMenu [SimTalk]
Shows (true) or hides (false) the user-defined ribbon tab.

```
Type:      Attribute
Syntax:    <Path_to_Frame>.ShowUserMenu:boolean
Assignment Value: boolean
```

Example:
```
MyFrame.ShowUserMenu := false
```

## UserMenu [SimTalk]
Sets the user-defined menu of the Frame designated by `<Path>`.

The attribute `UserMenu` passes a table of data type **table** with two columns:
- `String1` designates the command.
- `String2` designates the name of the Method, which the command executes.

> **Note:** `UserMenu` only accesses the items of the user-defined ribbon tab, not its title. Type the title of the user-defined ribbon tab into the text box **Comment** of the DataTable.

```
Type:      Attribute
Syntax:    <Path_to_Frame>.UserMenu:table
Assignment Value: table
```

Example:
```
var tab: table[string, string]
tab.create
tab.writeRow(1, tab.YDim+1, "My Command 1", "self.control1")
tab.writeRow(1, tab.YDim+1, "My Command 2", "self.control2")
current.UserMenu := tab
current.UserMenuTitle := "My Ribbon Tab"
current.ShowUserMenu := true
```

## UserMenuTitle [SimTalk]
Sets the title of the user-defined ribbon tab of the Frame designated by `<Path>` and shows it, if you set the attribute `Active` to true.

```
Syntax:    <Path_to_Frame>.UserMenuTitle:string
Assignment Value: string
```

Example:
```
frame2.UserMenuTitle := "My Ribbon Tab"
```

---

# Configure User-defined Context Menu

Creates a user-defined context menu in the selected Frame with menu commands you often use.

The dialog that the function opens is **modal**. The simulation only continues when the user reacted to the requested interaction.

Type in a hyphen (`-`) as the name of the command to insert a menu separator between groups of commands.

> **Notes:**
> - The commands on the user-defined context menu only apply to the selected object(s) within the Frame for which you defined the context menu.
> - The Class Library does not show the user-defined context menu.
> - To create a user-defined context menu in a Frame which you inserted into another Frame, deactivate **Inherit** first.

### Active [check box] - user-defined context menu
Select **Active** to activate the user-defined context menu. The context menu opens when you right-click the icon of the inserted Frame.

> **Note:** The user-defined context menu is only available for the Frame for which you defined it, after you inserted this Frame in another Frame. If Methods are called by the context menu, the anonymous identifier `?` is preallocated with the associated Frame.

SimTalk: `ShowUserPopupMenu` [SimTalk]

### New [Context Menu Command]
To add a new context menu command, click this button. Plant Simulation adds a row to the table.

Proceed as follows:
- Type in the name of the context menu command that the Frame window is to show.
- Type in the method that the context menu command is to execute.

### Text to Display [user-defined context menu]
Type in the text of the command that Plant Simulation shows on the context menu.

You can also type a formula as a command (designated by a leading question mark). When you type `?Method1`, the method `Method1` is called; its return value must be of data type **string**. If the method returns an empty string `""`, Plant Simulation hides the respective command.

You can use any formulas, e.g., `?Method1(42)` or `?MyDataTable[1,3]`.

SimTalk: `UserPopupMenu` [SimTalk]

### Method to Execute [user-defined context menu]
Type in the name of the Method which the Text to Display calls and executes.

**Parameters:**
- If the method expects a parameter, Plant Simulation automatically passes it. The selected objects located within the same Frame as the Frame whose context menu you open are passed to this parameter, which has to be of data type **list**.
- The optional parameter of data type **integer** sets the number of the context menu command. This way you can use a single callback method for several context menu commands.

### Delete [Context Menu Command]
To delete a context menu command, select the row and click this button.

---

# Attributes of the User-defined Context Menu

## ShowUserPopupMenu [SimTalk]
Shows (true) or hides (false) the context menu which you defined in the Frame designated by `<Path>`.

```
Type:      Attribute
Syntax:    <Path_to_Frame>.ShowUserPopupMenu:boolean
Assignment Value: boolean
```

Example:
```
Frame3.ShowUserPopupMenu := true
```

## UserPopupMenu [SimTalk]
Sets the user-defined context menu of the Frame designated by `<Path>`.

The attribute `UserPopupMenu` passes a table of data type **table** with two columns:
- `String1` designates the menu command.
- `String2` designates the name of the Method, which the command executes.

```
Type:      Attribute
Syntax:    <Path_to_Frame>.UserPopupMenu:table
Assignment Value: table
```

Example:
```
var tab: table[string,string]
tab.create
tab.writeRow(1,1,"Open Component","openComponent")
current.UserPopupMenu := tab
```

## Inherit User-defined Context Menu
Turns inheritance of the user-defined context menu on or off.
- Turn it on to make any Frame derived from the active Frame inherit the context menu of its origin.
- Turn it off to define a context menu that only applies to the active Frame.

---

# Replacement Mode

Sets how Plant Simulation handles objects when you merge Frames.

The replacement mode controls how Plant Simulation treats a `.psobj` file which you load into the active model, when the Class Library of this model already contains another version of these user-defined classes. Plant Simulation compares the names of the existing Frame and the Frame to be loaded, and then either **merges** or **exchanges** the Frames.

The replacement mode of the **replacing** Frame determines if the Frames are merged or replaced. The replacement mode of the replaced Frame has no consequences.

SimTalk: `ReplacementMode` [SimTalk], `replace` [SimTalk]

## Merge
Preserves changed settings in instances of the replaced Frame and imports them into the replacing object. Plant Simulation then deletes the replaced object in the Class Library. This is the default setting.

> This option only works for Frames that are identical.

SimTalk: `replace`, `getNodeName`, `loadObjectAs`, `writeObject` [SimTalk]

## Exchange
Transforms all instances of the replaced object into instances of the replacing object. Plant Simulation discards user-defined modifications in instances of the replaced object and deletes the replaced object from the Class Library.

> **Warning:** Before you Exchange Frames, save the previous version of the Frame, as all changes you made will be lost and there is no way to retrieve them.

## Merge Classes, Example
In simulation model1, the object `userobjectA` was modeled as `FrameA`. The model `FrameA` is also used in `FrameX` and `FrameY`, with changed instances.

`FrameX` and `FrameY` are saved with **Save Object As** as object files (`.psobj`). Plant Simulation also saves all inserted objects, especially `FrameA`.

Then `FrameX.psobj` and `FrameY.psobj` are loaded with **Load > Load Object** into model2:
- Loading `FrameX`: `FrameA` is loaded into the Class Library of model2. Plant Simulation replaces some newly loaded objects with objects already present. `FrameX` is imported as-is.
- Loading `FrameY`: `FrameA` already exists in the Class Library, so it is replaced according to the **Replacement Mode** set in `FrameA`:
  - **Merge** — all changes made in `FrameA` in `FrameY` are preserved.
  - **Exchange** — all changes made in `FrameA` in `FrameY` are lost; `FrameA` in `FrameY` is replaced with the `FrameA` already in the Class Library.

In this case **Merge** is the mode that meets the requirements.

## Exchange Classes, Example
In model1, the user-defined object `FrameA` is used several times in `FrameX`. `FrameX` is saved as `.psobj`.

Then `FrameX` is imported into model2, which contains a more up-to-date version `FrameANew`. To replace instances of `FrameA` in `FrameX` with instances of `FrameANew`, select **Exchange** as Replacement Mode in `FrameANew`. This discards all changes in instances of `FrameA` in `FrameX`.

Merge is not possible in this case, as `FrameA` differs from `FrameANew`.

## Inherit Replacement Mode
Turns inheritance of the replacement mode of a Frame which you inserted into another Frame on or off.

---

# Lock Structure [Frame ribbon]

Locks the structure of the Frame. Lock Structure is deactivated by default for new models, allowing you to immediately start modeling.

When you activate Lock Structure, Plant Simulation prevents unintentional changes (inserting, deleting, changing objects, and changing the position of objects). You can then neither change the position of any objects nor their name.

Lock Structure is activated in instantiated Frames by default. This helps prevent unintentional changes to the structure of an instance, since such changes should apply to all instances and should be made in the class.

SimTalk: `LockStructure` [SimTalk]

---

# Context Menu of the Frame Itself

To open it, click into the background of the Frame with the right mouse button. Some commands are on the mini toolbar, others on the context menu itself.

| To do this | Click or select |
|---|---|
| Reset the simulation in the Frame | Reset Simulation [Home ribbon] |
| Start or stop the simulation in the Frame | Start/Stop Simulation [Home ribbon] |
| Start the simulation without animation in the Frame | Start Fast Forward Simulation [Home ribbon] |
| Show the objects which the Frame contains | Show Structure [Home ribbon] |
| Show the objects which inherit from the Frame | Show Inheritance [Home ribbon] |
| Show the attributes and methods of the Frame | Show Attributes and Methods [Home ribbon] |

---

# Context Menu of the Selected Object in the Frame

The context menu of an object which you insert into a Frame provides a number of commands when you right-click it. Some are on the mini toolbar, others on the context menu itself.

The mini toolbar above the context menu always provides these commands:

| To do this | Click |
|---|---|
| Open the origin of the selected object | Open Origin [Home ribbon] |
| Open the class of the selected object | Open Class [Home ribbon] |
| Cut the selected object from the Frame | Cut [Home ribbon] |
| Copy the selected object in the Frame | Copy [Home ribbon] |
| Delete the selected object from the Frame | Delete [Home ribbon] |

> **Note:** Not all objects provide all of the context menu commands listed below.

## Activate [in Frame]
Activates the selected object (selects the check box **Active**). Deactivate with the command **Deactivate**.

## Calculate Angles
Makes the Turntable and PickAndPlace robot compute the angles at which they are connected to their predecessors and successors. The Turntable enters entry/exit angles into the Entry/Exit Angle Tables; the PickAndPlace robot enters angles into the Angles Table.

## Controls [in Frame]
Opens one of the controls entered on the Tab Controls. The menu item only shows if you actually entered one or several controls.

## Create Sensor [in Frame]
Creates a new sensor on a length-oriented object. Click at the rough position with the right mouse button and select this command, then enter the precise position in the dialog.

## Delete Sensor [in Frame]
Deletes a sensor from a length-oriented object (or press **Del** in 3D).

## Deactivate
Deactivates the selected object (clears the check box **Active**).

## Edit Dialog [in Frame]
Edits the Dialog you created.

## Edit Icons [in Frame]
Opens the Icon Editor to edit, delete, or add new icons.

## Edit User-defined Attributes [in Frame]
Opens the dialog User-defined Attributes.

## Event Debugger [in Frame]
Opens the dialog box of the EventDebugger.

## Open [in Frame]
Opens the dialog box of the selected object (or double-click its icon).

## Open Class [in Frame]
Opens the class of the selected object in the Class Library. For an instance, Plant Simulation moves up the inheritance structure until it reaches an object in the Class Library.

## Open Comment Window
Opens a window that only shows the text typed into the Comment, without formatting and editing options.

## Open Debugger
Opens the Method Debugger at the suspended line of code. If the Method is suspended, Plant Simulation opens the Watch Window instead.

## Open External Connections List
Opens the list showing the paths of the external connections in the Frame where you inserted the Interface object. The column **Connector** shows the Connector at the exit of the Frame; **Object** shows the name of the succeeding object.

## Open Origin [in Frame]
Opens the class from which the selected object was derived.

SimTalk: `Origin` [SimTalk]

## Open Sensor
Opens the dialog of the selected sensor of a length-oriented object.

## Open Values Table
Opens the TimeSequence object that contains the current sequence of Values of the Trigger.

## Open Without Control
Opens the dialog of the object without calling the Open Control (does not apply if the Open Control is an encrypted user-defined attribute of data type method). You can also hold **Alt** while double-clicking.

## Rename [in Frame]
Enters a new name for the selected object (or press **F2**).

## Reorder Successors
Reorders the sequence of the successors of the selected object. Use **Up**/**Down** to move, or **Delete** to delete the Connector. The command does not affect instances of the selected object.

## Reset Simulation [in Frame]
Resets the simulation model (or use Reset Simulation [EventController] or the Home ribbon).

## Run [Method in Frame]
Runs the source code of the Method (or press **F5**).

## Show [in Frame]
Shows the display window of the AttributeExplorer, the HtmlReport, or the Chart.

## Show Assigned Objects [in Frame]
Selects the objects assigned to the LockoutZone or ShiftCalendar as resources.

## Show Attributes and Methods [in Frame]
Shows the attributes and methods of the instance (or press **F8**).

## Show Dialog [in Frame]
Shows the Dialog with the dialog items you created.

## Show Exported Services
Opens the list of all services which the Exporter exports at this time.

## Show External Connected Objects
Selects the objects in the Frame which are connected to the Interface object. If the Frame is closed, Plant Simulation also opens it.

## Show Sessions Log
Shows the sessions log of the MQTT interface.

## Show Statistics Report [in Frame]
Shows statistics of the selected object in the Statistics Report (or press **F6**). Select multiple objects (Shift+click or marquee) and press F6 to show several. The report lets you jump to topics, print, save as HTML/text, and refresh.

SimTalk: `showStatisticsReport` [SimTalk]

## Show Structure [in Frame]
Shows the internal structure of the selected object (parts/objects located on the material flow object or loaded onto the Container/Transporter).

## Start/Stop Simulation [in Frame]
Starts the simulation run, or stops it after the active simulation event has been processed.

## Start Fast Forward Simulation [in Frame]
Starts the simulation run without the animation of MUs and States.

## Statistics Wizard [in Frame]
Opens the Statistics Wizard of the Chart.

## Type Info [in Frame]
Opens a table showing all methods and attributes of the active ActiveX control.

## Update [in Frame]
Updates the displayed Sankey flows of the Sankey Diagram with the current values.

SimTalk: `SankeyDiagram` [object], `update` [SimTalk]

---

# States of the Frame

During simulation runs, Plant Simulation shows the state of the Frame as one or more colored rectangles in the State Graphic of the Frame.

| Description | Color | Attribute |
|---|---|---|
| The Frame is Failed | red | `Failed` [SimTalk] - Frame |
| The Frame is Stopped | pink | `Stopped` [SimTalk] - Frame |
| The Frame is Paused | blue | `Pause` [SimTalk] - Frame |
| The Frame is Unplanned | light blue | `Unplanned` [SimTalk] - Frame |
| The Frame is Working | green | `StateWorking` [SimTalk] |
| The Frame is Blocked | yellow | `StateBlocked` [SimTalk] |
| The Frame is Setting-Up | brown | `StateSetup` [SimTalk] |
| The Entrance of the Frame is closed | cyan | `StateEntryShut` [SimTalk] |
| The Frame is Waiting for services and/or mounting parts | orange | `StateResourceMissing` [SimTalk] |

### See also
- States > State Graphic [defined]
- States of the Material Flow Objects
- States of the Transporter
- States of the Energy Features
- States of the Exporter
