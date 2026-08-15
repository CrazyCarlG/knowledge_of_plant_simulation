# Frame [object]

Use the object **Frame** as the container for creating your simulation models. It might, for example, represent a complex machine, a part of a plant, or the entire plant. The Frame is the principal object facilitating hierarchic modeling.

## Description

The Frame serves for grouping objects and for building hierarchically structured models by inserting any of the built-in objects and any objects you design. The Frame represents the entire plant, while you can model subsections of the plant in Frames of their own, which you insert into the Frame representing the entire plant.

To show a tooltip with information about the Frame or a sub-Frame, hover with the mouse over it.

Model transitions from Frame to Frame with the object **Interface**. Connect objects within the Frame and Frames with the object **Connector**. When you connect Frames with Connectors, Plant Simulation opens the dialog **Select Interface** in which you have to select an Interface, which you inserted into the Frame. A Frame is unconnected if one of its Interfaces is not connected to the outside.

The dialog **Select Interface**:

- Highlights the Interface that has the least number of connections (e.g., the Interface named `Exit` has 1 out of an unlimited number of possible connections).
- Lists in brackets how many connections out of the number you defined the Interface has (e.g., `Max3` has 1 out of the 3 possible connections).
- Marks the Interface that has reached its maximum number of external connections with an asterisk `*` (e.g., `Only1` has reached 1 out of 1 possible connections).

> **Note:** Most of the Tools (such as the TransferStation and the ExperimentManager) and some of the objects in the Object Libraries are modeled as application objects in a Frame. For this reason F1 opens the help for the Frame. To open help for the tool, select **Help > Help on Object** in its dialog.

When you insert a new Frame into your simulation model, it contains temporary (internal) deco graphics labeled **Under Construction** to represent it outward as long as you do not insert any other object into the Frame. This is because the default (external) graphics are set to be invisible.

## Add the Object to the Simulation Model

To add the object Frame to your simulation model, click **Manage Class Library > Basic Objects > MaterialFlow > Frame** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog Examples Collection, and click Open Model.

---

# TraceFile [SimTalk]

Sets the name of the trace file into which the Event Debugger of the EventController designated by `<Path>` writes the event log.

- **Type:** Attribute
- **Syntax:** `<Path>.TraceFile:string`
- **Assignment Value:** You can assign a value of data type string.

**Example:**

```simtalk
EventController.TraceFile := "C:\temp\run1"
```

**See also:** Trace File [text box]

---

# The Frame Window

The Frame Window provides access to the most important functions you need for creating your simulation model.

## Remarks

The Frame window provides the **Frame Ribbon Tab**, and the **System Menu**.

- The Context Menu of the Frame Itself provides commands pertaining to the Frame. To edit the 3D properties of the Frame in the 3D model, press the spacebar. Change the settings in the dialog **Edit 3D Properties**.
- The Context Menu of the Selected Object in the Frame provides commands pertaining to that object. You can edit the simulation properties of the object there. To edit the 3D properties of the selected object in the 3D model, press the spacebar.

**See also:** Work with Objects in the Frame Window, Add a Background Graphic to the Frame, `setXYWH` [SimTalk], `getXYWH` [SimTalk], `RootFrame` [SimTalk], `setPosition` [SimTalk]

## Drag-and-Drop While Modeling

You can use drag-and-drop while modeling in the Frame. The row "Class Library — Class Library — object — Ctrl" means: Dragging an object from the Class Library from one location to another location in the Class Library while holding Ctrl down copies the object to that location.

| To do this | Drag from | To | Accelerator |
|---|---|---|---|
| Move the object | Class Library | Class Library | object Shift |
| Copy the object | Class Library | Class Library | object Ctrl |
| Derive the object | Class Library | Class Library | object Ctrl+Shift |
| Instantiate the object | Class Library | Frame | object — |
| Move the object (makes a class out of the instance) | Frame | Class Library | object — |
| Copy the object | Frame | Class Library | object Ctrl |
| Load a graphics file (.GIF, .BMP, .PPM, .PPM RAW, .DXF, or .DWG) as the background graphic of the Frame | Windows Explorer | Frame | file — |
| Insert the selected object repeatedly | Class Library | Frame | object Shift |
| Execute a Method, which expects a single parameter of data type object with this object as parameter | Object from Frame | Method | single parameter of data type object — |

---

# System Menu of the Frame

The system menu shows commands with which you can manipulate or close the Frame window.

> **Note:** Plant Simulation displays the system menu in the language of Windows that is installed on your computer.

## Use Left Area

Uses the left part of the usable area of the MDI window in which Plant Simulation shows the object windows.

**See also:** Object Windows

## Use Right Area

Uses the right part of the usable area of the MDI window in which Plant Simulation shows the object windows.

**See also:** Object Windows

## Restore

Restores the Plant Simulation window to normal size.

## Move [window position]

Changes the window position of the Frame window in the Plant Simulation window.

## Size [window position]

Changes the size of the Frame window in the Plant Simulation window.

## Minimize

Reduces the size of the Frame window to an icon in the task bar of the Plant Simulation window.

## Maximize

Enlarges the size of the Frame window to fill the entire Plant Simulation window. When the Frame window is maximized, Plant Simulation adds the button combination Minimize, Maximize, Close (otherwise located in the title bar of the window) to the Ribbon Bar.

## Close [Frame window]

Closes the Frame window.

---

# Frame Ribbon Tab

The Frame ribbon tab provides commands to access the functions of the Frame.

| Command | Looks like this | Method or Attribute |
|---|---|---|
| Find Object [button] | | — |
| Incremental Find Object | | — |
| Show Unconnected Objects | | — |
| Select Shift Calendar | | `ShiftCalendarObject` [SimTalk] - Frame |
| Configure User-defined Ribbon Tab | | |
| Inherit User-defined Ribbon Tab | | |
| Configure User-defined Context Menu | | Various |
| Inherit User-defined Context Menu | | Various |
| Replacement Mode | | |
| Merge / Exchange | | |
| Inherit Replacement Mode | | `replace` [SimTalk], `ReplacementMode` [SimTalk] |
| Lock Structure [Frame ribbon] | | `LockStructure` [SimTalk] |

> **Note:** The other tabs on the Ribbon Bar provide additional commands pertaining to the Frame.

## Find Object [button]

Opens the dialog **Find Object**. To search for any object in the Frame window, you can also click in the Frame window and start typing its name. Plant Simulation then finds and selects the object.

**See also:** Find Object [context menu], Finding Objects and Text in Your Simulation Model

## Incremental Find Object

Clicking the button and starting to type the name of the object you want to find finds and highlights that object in the opened Frame window.

Microsoft describes Incremental Find Object as "a type of search that looks for a string in an automatic and progressive way. As the user types a string, possible matches are found, thus enabling the user to stop typing the complete string as soon as the right match is found."

- Plant Simulation shows the characters you type in the status bar. You can type all characters which are allowed for object names. As upper- or lower-casing is not distinguished in object names, you can start typing with lower-case letters.
- As soon as Plant Simulation finds an object that matches these characters, it selects that object and zooms to it in the 3D scene. To return to the last active scene before the search, press **Backspace**.
- If Incremental Find Object did not find and select the object you wanted, it returns to the scene as it was before you started searching.

Keys to control Incremental Find Object:

- Press **Backspace** to delete the last character you typed.
- Press **Tab** to find the next matching object. If no additional object is found, Plant Simulation selects the first object again and plays a signal tone. When cycling through matching objects, Plant Simulation shows the names of the objects in the status bar instead of the search pattern.
- Press **Esc** to terminate Incremental Find Object. Plant Simulation retains the current selection of the object it found.
- Press **Return** to terminate Incremental Find Object and execute the default operation of Return for the object (for example, open the simulation properties dialog).

> **Note:** To find the name of an object in an open folder in the Class Library, press Ctrl+I and start typing.

## Show Unconnected Objects

Highlights those objects in the open Frame window that have unconnected entrance and exit points, i.e., which are not connected to any other object with a Connector. A Frame counts as unconnected if one of its Interfaces is not connected to the outside.

## Select Shift Calendar

Sets the ShiftCalendar which contains the data of the shifts in your installation and controls during which shifts the Frame works.

The command opens the dialog **Select ShiftCalendar**. Select the ShiftCalendar in the dialog **Select Object** or enter the name of the ShiftCalendar.

> **Note:** The ShiftCalendar can change the states `paused` and `unplanned` of the Frame.

**SimTalk:** `ShiftCalendarObject`, `Unplanned` [SimTalk]

**See also:** Unplanned Control

## Configure User-defined Ribbon Tab

Creates a user-defined ribbon tab in the selected Frame with commands, which you frequently use.

Plant Simulation adds the user-defined ribbon tab to the predefined ribbon tabs of the Frame for which you defined it. It shows it on the tab **User**. When a user-defined ribbon tab exists, the button on the Frame ribbon tab is highlighted.

You can:

- Add an Icon to a Ribbon Command
- Create a Ribbon Group
- Dynamically Add a Ribbon Command
- Add a Command Separator
- Create an Access Key

> **Note:** To create a ribbon tab in a Frame, which you inserted into another Frame, deactivate the command Inherit first. Otherwise, this Frame inherits its user-defined ribbon tab from its origin.

### Title [user-defined ribbon tab]

Type in the Title of the user-defined ribbon tab which Plant Simulation uses to show the ribbon tab to the right of the predefined ribbon tabs of the Frame.

**SimTalk:** `UserMenuTitle` [SimTalk]

### Active [check box] - user-defined ribbon tab

To show and activate the user-defined ribbon tab to the right of the predefined ribbon tabs, select this check box. To deactivate and hide it, clear it.

> **Note:** If the user-defined ribbon tab calls a Method, Plant Simulation assigns the anonymous identifier `?` (question mark) to the respective Frame.

**SimTalk:** `ShowUserMenu` [SimTalk]

### New [ribbon command]

To add a New ribbon command to the ribbon tab you are configuring, click this button. Plant Simulation then adds a row to the table in the dialog.

Proceed as follows:

- Type in the Name of the ribbon command that the Frame window is to show. You can also click in the cell and select an item from the drop-down list and enter text.
- Type in the Method that the ribbon command is to execute in the Frame window.

### Text to Display [user-defined ribbon tab]

Type in the name of the command that Plant Simulation shows on the user-defined ribbon tab into the cells below **Text to Display**. Then select or type in the name of the Method to Execute when you click the command into the cell to the right.

You can select the following in front of a ribbon command or a group label:

- Select **?Formula** to designate a formula that computes the text to be used as the label of a group or as the ribbon command.
- Select **- Separator** (hyphen) to insert a group separator. If the group separator has an attached command, the group shows its button in the right bottom corner.
- Select the **#** sign and no text after it to designate the end of the previous group and to start a new unnamed group.
- Select **#Group Name** to start a new ribbon group with the name you enter.
- Type in the name of or select a method that the ribbon command executes to add the ribbon launch button to the group. The button typically opens a dialog box or another element that is related to the group.
- Type in two or more hyphens `--` or two or more number signs `##` to show them as they are.
- Select **#GroupNameFormula** to start a new ribbon group using a formula.

If one of the ribbon commands or group labels is dynamic as the result of computing a formula, the user-defined ribbon category gets updated each time it comes into the view. Thus, the user-defined ribbon tab will only be updated if another tab was active before and the current tab was then activated. Plant Simulation exchanges icons if dynamic ribbon commands or group labels change.

**SimTalk:** `UserMenu` [SimTalk]

### Create a Ribbon Group

Type in or select the number sign `#` in front of the first command to start a ribbon group on the ribbon tab. Ribbon groups group a number of related commands and are separated by long vertical lines between them.

- Any text following the `#` is used as the name of this ribbon group. If you type in `#Dialogs` as Text to Display, the ribbon tab will show Dialogs preceded by a vertical line serving as a group separator.
- If you just enter `#` and no text afterward, Plant Simulation considers this as the end of the previous group and starts a new group without a ribbon label.

The command can also consist of a formula, i.e., it can be dynamic. If a formula creates the Text to Display, Plant Simulation checks the text for line breaks. If line breaks exist, Plant Simulation splits the text and uses it as the:

- Name of the ribbon command
- Caption of the tooltip of the ribbon command
- Description of the ribbon command in the tooltip, provided you entered a description

**Example:**

```simtalk
"Statistics Report\nShow the statistics report.\nGenerates the statistics report of the selected object and shows it."
```

Type in the Methods, which the commands call and execute, into the cells below **Method to execute**.

### Add an Icon to a Ribbon Command

To add an icon to a ribbon command, proceed as follows:

- Create a new object icon. Specify 16 by 16 pixels and/or 32 by 32 pixels as the size. Name the icon to match the label of the ribbon command, for example `My Command 1`.
- Use these naming conventions for the icons:
  - Use `My Command 1_16` or `My Command 1_32` to indicate the size of the icon. If you do not specify the size, Plant Simulation will find the icon, but will not document its desired usage in its name.
  - Use `ribbon`, which is independent of the ribbon command label, and append the number of the command in the ribbon, for example `ribbon1`.
  - Plant Simulation resolves the icon name in this sequence:
    1. Ribbon command label with appended size
    2. Ribbon command label without appended size
    3. Icon names which are independent of the label
- Plant Simulation will choose the size of the displayed icon based on available space:
  1. If space is tight on the ribbon, it uses the 16 by 16 pixel icon.
  2. If the ribbon has more space available, it uses the 32 x 32 pixel icon.

> **Note:** If you use a formula for the label, Plant Simulation uses the result of this formula to search for the icon. To prevent problems with formula results as icon names, you can name ribbon command icons in a standardized way using the default name `ribbon` appended with the number of the command (e.g., `ribbon1`).

If you do not type a Method to Execute into the text box next to Text to Display, Plant Simulation dims the icon.

### Dynamically Add a Ribbon Command

Select `?Formula` and then type over Formula in the cell with the name of your formula to use this formula as a ribbon command.

When you type in `?Method1` for example, the method named `Method1` will be called. The return value of this method has to be of data type string. This way you can toggle between different captions (for example between Activate and Deactivate) and you can translate the commands into different languages. If the methods return an empty string `""`, Plant Simulation hides the respective command.

You can use any formula, even a method call with parameters, such as `?Method1(42)` or a table access, such as `?MyDataTable[1,3]`.

### Add a Command Separator

Type in or select `- Separator` followed by the category name as the Text to Display to insert a vertical separator between groups of ribbon commands.

### Create an Access Key

Type the ampersand character `&` in front of a letter of a command on the ribbon tab to make this letter the access key (mnemonic key) on the user-defined ribbon tab.

Plant Simulation activates this command when you press the Alt key and that letter.

- If you do not type in the ampersand, Plant Simulation assigns an automatically numbered access key.
- The built-in access keys take precedence over any access keys you define! This means that your access key does not work if it is already defined on one of the pre-defined ribbon tabs.

> **Note:** You can only create access keys for menu items on a menu, not for dialog items in the dialog itself.

### Method to Execute [user-defined ribbon tab]

Type in the name of the Method, which the Text to Display calls and executes, into the respective cell.

When Methods are called by the user-defined ribbon tab, the anonymous identifier `?` (question mark) points to the Frame in which the selection was executed. Use this to selectively access objects in the respective Frame.

**Parameter:** If the method to execute expects a parameter, Plant Simulation automatically passes it. The objects, which you selected in the Frame, are passed to this parameter, which has to be of data type list or an array of data type object.

**Example:**

```simtalk
?.MyStation.proctime := str_to_time(prompt)
```

**SimTalk:** `UserMenu` [SimTalk]

### Delete [ribbon command]

To delete a command from the user-defined ribbon tab, select the respective row in the dialog and click this button.

### Inherit User-defined Ribbon Tab

Turns inheritance for a ribbon tab which you create in a Frame, which you inserted into another Frame, on or off.

- Turn inheritance on to make any Frame which you derive from the active Frame inherit the ribbon tab of its origin.
- Turn it off to define a ribbon tab that only applies to the active Frame, but will not be inherited.

### Context Menu of the User-defined Ribbon Tab

The context menu of the user-defined ribbon tab and the user-defined context menu provides the commands listed below.

- **Insert Row [user-defined ribbon tab]** — Inserts an empty row above the selected row in the table. Hold down Shift and click Insert Row to insert an empty row below the selected row.
- **Delete Row [user-defined ribbon tab]** — Deletes the selected row from the table.
- **Cut Row [user-defined ribbon tab]** — Cuts the selected row from the table, converts the cut data to text, and places it on the clipboard. Plant Simulation separates the two columns of the cut row with a tab stop.
- **Copy Row [user-defined ribbon tab]** — Copies the selected row, converts the copied data to text, and places it on the clipboard. The two columns are separated with a tab stop.
- **Paste Row [user-defined ribbon tab]** — Pastes the data of the row from the clipboard to the table. Plant Simulation looks for line breaks and tabulators, separates the text accordingly, and pastes the text into the table.
  - Click in the row where you want to paste and select Paste Row to replace the current row.
  - Hold down Ctrl and select Paste Row to paste above the current row (does not overwrite).
  - Hold down Ctrl and Shift and select Paste Row to paste below the current row (does not overwrite).

### Keyboard Shortcuts for User-defined Ribbon Tab/Context Menu

| To do this | Press |
|---|---|
| Copy the current row to the clipboard | Ctrl+C or Ctrl+Ins |
| Cut the current row to the clipboard | Ctrl+X or Shift+Del |
| Paste the contents of the clipboard (tab-separated columns, line-break separated rows) | Ctrl+V or Shift+Ins |
| Insert the new row above the current row | Ins / Ctrl+ + or Ctrl+Num+ |
| Insert the new row below the current row | Ctrl+Shift+ + or Ctrl+Shift+Num+ |
| Delete the selected row | Del |
| Edit the selected row | F2 |
| Open the Method Editor for the Method in the current row | Shift+F2 |
| Open the drop-down list for selecting items in the column Text to display | F4 |
| Open the context menu for selecting commands in the column Method to execute | F4 |
| Create a user-defined method/control | Shift+F4 |

---

# Attributes of the User-defined Ribbon Tab

## ShowUserMenu [SimTalk]

Shows (`true`) or hides (`false`) the user-defined ribbon tab.

- **Type:** Attribute
- **Syntax:** `<Path_to_Frame>.ShowUserMenu:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**

```simtalk
MyFrame.ShowUserMenu := false
```

**See also:** Active [check box] - user-defined ribbon tab

## UserMenu [SimTalk]

Sets the user-defined menu of the Frame designated by `<Path>`.

The attribute `UserMenu` passes a table of data type table with two columns. `String1` designates the command. `String2` designates the name of the Method, which the command executes.

> **Note:** The attribute `UserMenu` only accesses the items of the user-defined ribbon tab, not its title. Type the title of the user-defined ribbon tab into the text box Comment of the DataTable.

- **Type:** Attribute
- **Syntax:** `<Path_to_Frame>.UserMenu:table`
- **Assignment Value:** You can assign a value of data type table.

**Example:**

```simtalk
var tab: table[string, string]
tab.create
tab.writeRow(1, tab.YDim+1, "My Command 1", "self.control1")
tab.writeRow(1, tab.YDim+1, "My Command 2", "self.control2")
current.UserMenu := tab
current.UserMenuTitle := "My Ribbon Tab"
current.ShowUserMenu := true
```

## UserMenuTitle [SimTalk]

Sets the title of the user-defined ribbon tab of the Frame designated by `<Path>` and shows it, if you set the attribute Active to true.

- **Syntax:** `<Path_to_Frame>.UserMenuTitle:string`
- **Assignment Value:** You can assign a value of data type string.

**Example:**

```simtalk
frame2.UserMenuTitle := "My Ribbon Tab"
```

---

# Configure User-defined Context Menu

Creates a user-defined context menu in the selected Frame with menu commands you often use.

The dialog, which the function opens, is modal. The simulation only continues when the user reacted to the requested interaction by clicking the respective button in the dialog.

- Type in a hyphen (`-`) as the name of the command to insert a menu separator between groups of commands.

> **Note:** The commands on the user-defined context menu only apply to the selected object(s) within the Frame for which you defined the context menu. The Class Library does not show the user-defined context menu.

To create a user-defined context menu in a Frame, which you inserted into another Frame, deactivate the command Inherit first. Otherwise, this Frame inherits its user-defined context menu from its origin.

## Active [check box] - user-defined context menu

To activate the user-defined context menu, select Active. Clear the check box to deactivate it. The context menu opens when you click the right mouse button on the icon of the inserted Frame.

> **Note:** The user-defined context menu is only available for the Frame for which you defined it, after you inserted this Frame in another Frame. If Methods are called by the context menu, the anonymous identifier `?` (question mark) is preallocated with the associated Frame.

**SimTalk:** `ShowUserPopupMenu` [SimTalk]

## New [Context Menu Command]

To add a new context menu command to a Frame in your simulation model, click this button. Plant Simulation then adds a row to the table in the dialog.

Proceed as follows:

- Type in the name of the context menu command that the Frame window is to show.
- Type in the method that the context menu command is to execute in the Frame window.

## Text to Display [user-defined context menu]

Type in the text of the command that Plant Simulation shows on the context menu into the text boxes below **Text to Display**.

You can also type in a formula as a command. A formula is designated by a leading question mark. When you type in `?Method1`, the method named `Method1` will be called. The return value of this method has to be of data type string. This way you can switch between different texts (e.g., Activate and Deactivate) and translate commands into different languages. If the methods return an empty string `""`, Plant Simulation hides the respective command.

> **Note:** You can use any formulas, even a method call with parameters, such as `?Method1(42)` or a table access, such as `?MyDataTable[1,3]`.

**SimTalk:** `UserPopupMenu` [SimTalk]

## Method to Execute [user-defined context menu]

Type in the name of the Method, which the Text to Display calls and executes, in the respective text box below **Method to Execute**.

**Parameters:**

- If the method to execute expects a parameter, Plant Simulation automatically passes it. The selected objects, which are located within the same Frame as the Frame whose context menu you open, are passed to this parameter, which has to be of data type list.
- The optional parameter of data type integer sets the number of the context menu command on the context menu. This way you can use a single callback method for several context menu commands.

## Delete [Context Menu Command]

To delete a context menu command from the user-defined context menu, select the respective row in the dialog and click this button.

---

# Attributes of the User-defined Context Menu

## ShowUserPopupMenu [SimTalk]

Shows (`true`) or hides (`false`) the context menu which you defined in the Frame designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path_to_Frame>.ShowUserPopupMenu:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**

```simtalk
Frame3.ShowUserPopupMenu := true
```

## UserPopupMenu [SimTalk]

Sets the user-defined context menu of the Frame designated by `<Path>`.

The attribute `UserPopupMenu` passes a table of data type table with two columns. `String1` designates the menu command. `String2` designates the name of the Method, which the command executes.

- **Type:** Attribute
- **Syntax:** `<Path_to_Frame>.UserPopupMenu:table`
- **Assignment Value:** You can assign a value of data type table.

**Example:**

```simtalk
var tab: table[string,string]
tab.create
tab.writeRow(1,1,"Open Component","openComponent")
current.UserPopupMenu := tab
```

## Inherit User-defined Context Menu

Turns inheritance of the user-defined context menu, which you create in a Frame and which you inserted into another Frame, on or off.

- Turn it on to make any Frame which you derive from the active Frame inherit the user-defined context menu of its origin.
- Turn it off to define a user-defined context menu that only applies to the active Frame, but will not be inherited.

---

# Replacement Mode

Sets how Plant Simulation handles objects when you merge Frames.

The replacement mode controls how Plant Simulation treats a `.psobj` file which you load into the active model, when the Class Library of this model already contains another version of these user-defined classes. While doing so, Plant Simulation compares the names of the existing Frame and of the Frame to be loaded, and then either merges or exchanges the Frames, depending on the setting you selected.

The replacement mode of the **replacing** Frame determines if the Frames are merged or replaced. The replacement mode of the **replaced** Frame does not have any consequences.

**SimTalk:** `ReplacementMode` [SimTalk], `replace` [SimTalk]

## Merge

Preserves changed settings in instances of the replaced Frame and imports them into the replacing object. Plant Simulation then deletes the replaced object in the Class Library. This is the default setting for merging Frames.

> **Note:** This option only works for Frames that are identical.

**SimTalk:** `replace` [SimTalk], `getNodeName` [SimTalk], `loadObjectAs` [SimTalk], `writeObject` [SimTalk]

## Exchange

Transforms all instances of the replaced object into instances of the replacing object. Plant Simulation discards user-defined modifications in instances of the replaced object and deletes the replaced object from the Class Library.

> **Note:** Before you Exchange Frames in Replacement Mode, we recommend saving the previous version of the Frame, as all changes you made will be lost and there is no way to retrieve them!

## Merge Classes, Example

In simulation model1 we modeled the object `userobjectA` as `FrameA`. We also use the model `FrameA` in the models `FrameX` and `FrameY`. In addition we changed the instances of `FrameA` in `FrameX` and `FrameY`.

We then save `FrameX` and `FrameY` with the context menu command **Save Object As** as object files (`.psobj`) to be able to reuse them in other simulation models. Plant Simulation also saves all objects you inserted into frames, especially `FrameA`.

Then, we load `FrameX` (`FrameX.psobj`) and `FrameY` (`FrameY.psobj`) with the context menu command **Load > Load Object** into simulation model2.

- When loading `FrameX` and all objects contained within (including `FrameA`), they are loaded into the Class Library of simulation model2. Plant Simulation replaces some of the newly loaded objects with objects already present. As `FrameX` did not exist in the Class Library, it is imported as is.
- When loading `FrameY`, Plant Simulation loads all objects contained within. As `FrameA` already exists in the Class Library, Plant Simulation replaces it with the setting you selected under Replacement Mode in `FrameA`:
  - **Merge** — All changes we made in `FrameA` in `FrameY` will be preserved.
  - **Exchange** — All changes we made in `FrameA` in `FrameY` will be lost. `FrameA` in `FrameY` will be replaced with `FrameA` that already exists in the Class Library.

In this case Merge is the mode that meets our requirements.

## Exchange Classes, Example

In simulation model1 we modeled the user-defined object `FrameA`. We use `FrameA` several times in `FrameX`.

We then save `FrameX` with the context menu command **Save Object As** as object file (`.psobj`) to be able to reuse it in other simulation models. All objects inserted into frames, especially `FrameA`, are saved as well.

Then, we import `FrameX` into simulation model2 that contains a more up-to-date version of `FrameA`, `FrameANew`, which we would like to continue using. To replace instances of `FrameA` in `FrameX` with instances of `FrameANew`, we select Exchange as Replacement Mode in `FrameANew`. This discards all changes in instances of `FrameA` in `FrameX`; we are going to continue working with `FrameANew` as intended.

> **Note:** Merge is not possible in this case, as `FrameA` differs from `FrameANew`.

## Inherit Replacement Mode

Turns inheritance of the replacement mode of a Frame which you inserted into another Frame on or off.

- Turn it on to make any Frame which you derive from the active Frame inherit the replacement mode of its origin.
- Turn it off to define a replacement mode that only applies to the active Frame, but will not be inherited.

---

# Lock Structure [Frame ribbon]

Locks the structure of the Frame. Lock Structure is deactivated by default for new models, allowing you to immediately start modeling.

When you activate Lock Structure, Plant Simulation prevents unintentional changes, i.e., inserting, deleting, and changing of objects as well as changing the position of objects. You can then neither change the position of any of the objects nor their name.

Lock Structure is activated in instantiated Frames by default. This helps to prevent unintentional changes to the structure of an instance, although this change should apply to all instances and should thus be made in the class.

**SimTalk:** `LockStructure` [SimTalk]

---

# Context Menu of the Frame Itself

The context menu of the Frame itself provides these commands. To open it, click into the background of the Frame with the right mouse button.

Some of the commands are located on the mini toolbar, while others are commands on the context menu itself. You can also close the context menu and leave the mini toolbar open by clicking the border of the mini toolbar with the left mouse button.

| To do this | click or select |
|---|---|
| Reset the simulation in the Frame | Reset Simulation [Home ribbon] |
| Start or stop the simulation in the Frame | Start/Stop Simulation [Home ribbon] |
| Start the simulation without animation in the Frame | Start Fast Forward Simulation [Home ribbon] |
| Show the objects which Frame contains | Show Structure [Home ribbon] |
| Show the objects which inherit from the Frame | Show Inheritance [Home ribbon] |
| Show the attributes and methods of the Frame | Show Attributes and Methods [Home ribbon] |

---

# Context Menu of the Selected Object in the Frame

The context menu of an object, which you insert into a Frame, provides a number of commands when you click it with the right mouse button.

The mini toolbar above the context menu proper always provides these commands:

| To do this | click |
|---|---|
| Open the origin of the selected object | Open Origin [Home ribbon] |
| Open the class of the selected object | Open Class [Home ribbon] |
| Cut the selected object from the Frame | Cut [Home ribbon] |
| Copy the selected object in the Frame | Copy [Home ribbon] |
| Delete the selected object from the Frame | Delete [Home ribbon] |

Some objects provide additional commands on the mini toolbar to the left or the right of the default buttons.

> **Note:** Not all objects provide all of the context menu commands listed above.

The commands on the context menu proper include:

- **Activate [in Frame]** — Activates the selected object (selects the check box Active). You can deactivate the selected object with the command Deactivate.
- **Calculate Angles** — Makes the Turntable and the PickAndPlace robot compute the angles at which you connected them with their predecessors and successors. The Turntable enters the entry/exit angles into the Entry/Exit Angle Tables; the PickAndPlace robot enters the angles into the Angles Table. **SimTalk:** `calculateAngles` [SimTalk].
- **Controls [in Frame]** — Opens one of the controls, which you entered on the Tab Controls, by clicking Edit Controls on the Home ribbon tab. Only shows if you actually entered one or several controls.
- **Create Sensor [in Frame]** — Creates a new sensor on a length-oriented object. Click at the rough position with the right mouse button and select this command. Enter the precise position and remaining data into the dialog.
- **Delete Sensor [in Frame]** — Deletes a sensor from a length-oriented object. In 3D, press Del.
- **Deactivate** — Deactivates the selected object (clears the check box Active).
- **Edit Dialog [in Frame]** — Edits the Dialog you created.
- **Edit Icons [in Frame]** — Opens the Icon Editor to edit, delete, or add icons.
- **Edit User-defined Attributes [in Frame]** — Opens the dialog User-defined Attributes to edit, delete, or add user-defined attributes.
- **Event Debugger [in Frame]** — Opens the dialog box of the EventDebugger.
- **Open [in Frame]** — Opens the dialog box of the selected object. You can also double-click the icon.
- **Open Class [in Frame]** — Opens the class of the selected object in the Class Library. For an instance, Plant Simulation moves up in the inheritance structure until it reaches an object in the Class Library.
- **Open Comment Window** — Opens a window that only shows the text you typed into the Comment, without formatting and editing options.
- **Open Debugger** — Opens the Method Debugger at the suspended line of code. If the Method is suspended, Plant Simulation opens the Watch Window instead.
- **Open External Connections List** — Opens the list showing the paths of the external connections in the Frame in which you inserted the Interface object.
- **Open Origin [in Frame]** — Opens the class from which the selected object was derived. **SimTalk:** `Origin` [SimTalk].
- **Open Sensor** — Opens the dialog of the selected sensor of the length-oriented object.
- **Open Values Table** — Opens the TimeSequence object that contains the current sequence of Values of the Trigger.
- **Open Without Control** — Opens the dialog of the object without calling the Open Control. You can also hold down Alt while double-clicking the icon.
- **Rename [in Frame]** — Enters a new name for the selected object. You can also select Home > Rename or press F2.
- **Reorder Successors** — Reorders the sequence of the successors of the selected object without deleting and reconnecting the Connectors. Click Up/Down to move the object in the sequence; click Delete to delete a Connector. The sequence of the successors affects how parts are transported. This does not affect instances of the selected object.
- **Reset Simulation [in Frame]** — Resets the simulation model.
- **Run [Method in Frame]** — Runs the source code of the Method. You can also select Run on the Run menu or press F5.
- **Show [in Frame]** — Shows the display window of the AttributeExplorer, HtmlReport, or Chart.
- **Show Assigned Objects [in Frame]** — Selects the objects assigned to the LockoutZone or ShiftCalendar as resources.
- **Show Attributes and Methods [in Frame]** — Shows the attributes and methods of the instance. You can also press F8.
- **Show Dialog [in Frame]** — Shows the Dialog with the dialog items you created.
- **Show Exported Services** — Opens the list that shows all services which the Exporter exports.
- **Show External Connected Objects** — Selects the objects in the Frame which are connected to the Interface object. If the Frame is closed, Plant Simulation also opens the Frame.
- **Show Sessions Log** — Shows the sessions log of the MQTT interface.
- **Show Statistics Report [in Frame]** — Shows statistics of the selected object in the Statistics Report, or press F6. To show statistics of several objects, select them (Shift+click or drag a marquee) and press F6. The report lets you jump to topics, print, save as HTML (*.htm/*.html) or text (*.txt), and refresh.
- **Show Structure [in Frame]** — Shows the internal structure of the selected object, on which parts can be located.
- **Start/Stop Simulation [in Frame]** — Starts or stops the simulation run.
- **Start Fast Forward Simulation [in Frame]** — Starts the simulation run without the animation of MUs and States.
- **Statistics Wizard [in Frame]** — Opens the Statistics Wizard of the Chart.
- **Type Info [in Frame]** — Opens a table that shows all methods and attributes of the active ActiveX control.
- **Update [in Frame]** — Updates the displayed Sankey flows of the Sankey Diagram with the current values.

---

# States of the Frame

During the simulation runs Plant Simulation shows the state of the Frame as one or more colored rectangles in the State Graphic of the Frame.

| State | Color of the State Graphic | Attribute |
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

**See also:** States > State Graphic, States of the Material Flow Objects, States of the Transporter, States of the Energy Features, States of the Exporter

---

# Methods of the Frame

The Frame provides:

- The methods listed in the table of contents (to the left of the original help).
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the F8 key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

An example of the Syntax line of the individual methods might look like this:

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```
