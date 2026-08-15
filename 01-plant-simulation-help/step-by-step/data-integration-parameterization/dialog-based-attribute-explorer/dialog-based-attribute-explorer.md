# Dialog-Based Attribute Explorer

## Overview

This guide covers how to set parameters in a Plant Simulation model using two approaches:

1. **Setting Parameters for Objects in Your Own Dialog** — create custom dialog boxes that look and work like the built-in Plant Simulation dialogs.
2. **Setting Parameters with the AttributeExplorer** — manage attributes of multiple objects in a single list window.

---

## Setting Parameters in the Model

Introduces how to enter parameters into a simulation model and execute simulation runs with those parameters. You can:

- Set Parameters for Objects in Your Own Dialog
- Set Parameters with the AttributeExplorer
- Compare Model Random Processes
- Compare Run Simulation Experiments

---

## Setting Parameters for Objects in Your Own Dialog

Use the **Dialog** object to:

- Provide a simple user interface for complex simulation models, asking the user to select or enter information Plant Simulation needs.
- Prevent the user from manipulating a Frame (e.g., a complex machine). Enter a Method as an **Open Control** for the Frame and insert a user-defined dialog. When the user double-clicks the Frame, Plant Simulation calls the Method, which opens the dialog instead.

> **Note:** A Dialog window that contains menus uses your Windows theme; a Dialog window without menus uses the standard Siemens PLM theme.

You can insert the Dialog from the folder **UserInterface** in the Class Library, or from the toolbar **User Interface** in the Toolbox. Each Dialog object manages a single dialog box — insert as many Dialog objects as you need dialogs.

You will:

- Plan Layout and Structure of Your Dialog
- Design a Simple Dialog
- Design a Tabbed Dialog
- Program Actions which the Dialog Items Execute
- Program Actions for Interacting with the Dialog
- Create a Dialog Dynamically

---

## Plan Layout and Structure of Your Dialog

Before designing, think about layout and structure:

- Orient dialog items in the direction the user reads (left-to-right, top-to-bottom in Western countries).
- Place the primary dialog item as close to the upper corner as possible.
- Place major command buttons stacked along the right border or lined up across the bottom; put the most important button first.
- Decide whether a flat hierarchy (simple dialog) or tabs (tabbed dialog) is appropriate.

The structure determines creation order:

- For tabs: first create the **Tab Control** (container), then the individual tabs, then the dialog items on each tab.
- For groups: first create the group, then insert and position the items within it. The y-coordinate of items in a group relates to the y-coordinate *within that group*, not the overall dialog.

### Dialog item types

| Dialog item | Icon |
|---|---|
| Static Text Box | |
| Text Box | |
| Button | |
| Drop-Down List Box | |
| Group Box | |
| Check Box | |
| Radio Button | |
| List Box | |
| Image | |
| List View | |
| Tab Control | |
| Tab Page | |
| Menu / menu command | |

> **Note:** Plant Simulation shows the dialog with your **Personalization > Font** settings and **Display > Scale & layout** settings. Text scales, but images always retain their pixel size, so text may overlap images. Test dialogs with different display settings.

---

## Design a Simple Dialog

Use a flat structure when the user only needs to select or enter a small number of items.

### To start designing your own dialog

1. Insert the **Dialog** into the Frame (from folder UserInterface or toolbar User Interface).
2. Enter a **Name** and a **Label**. Unlike the name, the label can contain special characters and blank spaces.
   - If you enter a label, Plant Simulation shows it in the title bar.
   - If not, Plant Simulation shows the Name in the title bar.
3. To insert a dialog item, right-click the tab **Elements** and select the dialog item.

You can add: Menu and Menu Commands, Static Text Box, Text Box, Drop-down List, Group Box, Button, Set of Radio Buttons, Check Box, List Box, List View, Image.

### Other operations

- **Show Dialog** — show the dialog you are creating.
- **Modify** an item — right-click it and select Open.
- **Delete** an item — right-click it and select Delete.
- **Change position** — click Show Dialog, then Edit Dialog, select the item, and drag it. (The Dialog applies coordinates immediately; the move cannot be undone.)
- **Show standard buttons** — select the check box; clear it to hide. If you hide them, you must define your own buttons.
- **Open Modal** — select to prevent the user opening other Plant Simulation windows until the dialog is closed.
- **Position tab** — set X-Position and Y-Position in pixels. Default `-1` for both centers the dialog on screen (zero point is top-left).

---

## Add a Menu and Menu Commands

### To add a menu

- Right-click the tab **Elements** and select **New Menu / New Menu Command**.
- Enter the **Name** (a Method can call the item by this name).
- Enter the **Caption** (what the menu displays). The ampersand `&` designates the access key (e.g., `&Show`).
- For the top menu itself, no Callback Argument is needed.

### To add a menu command

- Right-click the menu name and select **New Menu / Menu Command**.
- Enter Name and Caption (e.g., `&Chart`, `&Report`).
- To use a literal ampersand, type it twice (`Drag && Drop`).
- Enter the **Callback Argument** (e.g., `CallbackChart`, `CallbackReport`) to be passed to the callback method.
- To add a submenu, right-click a menu command and select **New Menu / Menu Command** again.

### Callback method

The callback method is a user-defined attribute of data type `method`. On the tab User-defined, double-click `callback` and click Open. To enter commands, click **Inherit Source Code** so it is *not* selected.

The default source code looks like this:

```simtalk
param action: string
switch action
case "Open"
                // TODO: add code for the "Open" action here
                // for example ?.setCaption("TextBox", "Test")
                // for example ?.setCheckBox("CheckBox", true)
case "Apply"
                // TODO: add code for the "Apply" action here
                // for example print ?.getValue("TextBox")
                // for example print ?.GetCheckBox("CheckBox")
case "Close"
                // TODO: add code for the "Close" action here
end
```

To open the object `MyChart`, enter:

```simtalk
case "CallbackChart" 
   MyChart.IsShown := true 
```

To open the object `MyReport`, enter:

```simtalk
case "CallbackReport" 
   MyReport.show 
```

To change the order of menu commands, select one on the tab Elements, hold Shift and press Up/Down arrow.

---

## Add a Static Text Box

Shows text the user can view but not edit.

- Right-click **Elements** → **New Static Text Box**.
- Enter **Name**, **Caption** (what is displayed), **X/Y-coordinate**.
- The position corresponds to the average width of characters of your system font, not pixels.
- Select whether to **Enable** it, then click OK.

> **Note:** If you cannot see a dialog item, check position settings — identical coordinates stack items on top of each other.

---

## Add a Text Box

A field where the user can enter or edit text.

- Right-click **Elements** → **New Edit Text Box**.
- Enter **Name**, **Callback Argument**.
- Select the **Data Type** the user can enter:

| Selection | The user can enter |
|---|---|
| Any Character | any character (special chars, letters, numbers) |
| Alphanumeric Characters | blank space, letters, numbers |
| Letters | lower/upper case letters |
| Decimal Numbers | `0123456789` |
| Signed Decimal Numbers | `-0123456789` or `+0123456789` |
| Hexadecimal Numbers | e.g., `ADbf09` |
| Octal Numbers | `01234567` (not `18`) |
| Binary Numbers | `0` or `1` |
| Floating Point Numbers | e.g., `12.3E-43` |

- Enter **X/Y-coordinate** and **Width** (default `0` uses our values).
- Select **Enable**, and optionally **Password** to mask text with superscripted lowercase x-es.

---

## Add a Drop-down List

The user selects a single item; when closed it shows the current value.

- Right-click **Elements** → **New DropDownList Box**.
- Enter **Name**, **Callback Argument**, **X/Y-coordinate**, **Width**.
- Click **Items** and enter the items:
  - Add: type name, click Insert or press Enter.
  - Delete: select and click Delete.
  - Move up: select and click Move Up.
  - Rename: select, type new name, click Rename.
  - OK / Cancel.
- Select **Enable**, then click OK.

---

## Add a Group Box Around Dialog Items

Graphically groups a set of items by drawing a frame around them.

- Create the group first, then insert and position items within it.
- Right-click **Elements** → **New Group Box**.
- Enter **Name**, **Caption**, **X/Y-coordinate**, **Width** and **Height**.
- Select **Enable**, then click OK.
- To change item order within a group, select an item, hold Shift and press Up/Down arrow.

---

## Add a Set of Radio Buttons

Enables selecting a single setting from a set of mutually exclusive choices.

- Right-click **Elements** → **New Radio Button**.
- Enter **Name**, **Caption**, **Callback Argument**, **X/Y-coordinate**.
- Enter a **group id** (a number) to group radio buttons that belong together. The user can select only one radio button per group at a time.

> **Note:** Create all items of a radio-button group sequentially (Plant Simulation creates items by row/column position). Windows ignores the Group ID and groups radio buttons row by row according to Y-coordinate. To model radio buttons side by side in two columns, place them within group boxes.

- Select **Enable**, then click OK. Repeat for additional radio buttons.

---

## Add a Check Box

Displays a setting or settings that do not exclude each other; the user can select/clear several at once.

- Right-click **Elements** → **New Check Box**.
- Enter **Name**, **Caption**, **Callback Argument**, **X/Y-coordinate**.
- Select **Enable**, then click OK.

---

## Design a Tabbed Dialog

Use a tabbed dialog when the user selects or enters several different types of information.

Start the same way as a simple dialog (insert Dialog, enter Name/Label, add items via the Elements tab).

You can additionally: Add a Tab Control, Add Tabs to a Tab Control, Detach the Camera from an Object.

Same operations apply: Show Dialog, Edit Dialog (drag to reposition), standard buttons, Open Modal, Position tab.

---

## Add a Tab Control

The tab control is the container holding the individual tabs (pages). Do not confuse it with the tabs themselves.

When the user selects another tab, the Dialog calls the **Callback Method**, executing the actions programmed with the first parameter (the Callback Argument).

- Right-click **Elements** → **New Tab Control**.
- Type the **Name**, **Callback Argument**, **X/Y-coordinate**, **Width** and **Height** (default `0` uses our values).
- Click OK.
- To add a tab, right-click the Tab Control on the Elements tab and select **New Tab Page**.
- To change tab order, select a tab, hold Shift and press Up/Down arrow (first tab = leftmost).

---

## Add Tabs to a Tab Control

Add individual tabs to the Tab Control container.

- Right-click **Elements** → **New Tab Page**.
- Enter **Name** and **Caption** (shown as the tab's title).
- Click OK.
- To reorder, select a tab and use Shift + Up/Down arrow.

---

## Add a List Box

Displays a list of choices; the user double-clicks to select. Unlike the drop-down list, it has a fixed size and does not collapse.

- Right-click **Elements** → **New List Box**.
- Type **Name**, **Callback Argument**, **X/Y-coordinate**, **Width** and **Height**.
- If the list has more items than the height can display, a vertical scrollbar is added.
- Click **Items** and enter items (same Insert/Delete/Move Up/Rename/OK/Cancel operations).
- Select **Enable**, then click OK.

---

## Add a List View

Displays a table in the dialog.

> **Note:** When displaying strings, Plant Simulation only shows the first 260 characters.

- Right-click **Elements** → **New List View**.
- Enter **Name**, **Callback Argument**.
- Enter the name of a table or click the button to select a table.
  - Activate the column index in the DataTable and enter column headings.
  - Enter the items into the cells.
- Enter **X/Y-coordinate**, **Width** and **Height**.
- Select **Enable**, then click OK.

---

## Add a Button

When clicked, it calls the Callback Method with the Callback Argument.

- Right-click **Elements** → **New Button**.
- Enter **Name**, **Caption**, **Callback Argument**, **X/Y-coordinate**, **Width** (default `0` = width of the OK button).
- Select **Enable**, then click OK.

---

## Add an Image

A picture/icon defined for the Dialog. You can enter a number or a name (e.g., `Icon1`).

- Right-click **Elements** → **New Image**.
- Enter **Name**, **X/Y-coordinate**, **Width** and **Height**.
- Enter an **Image ID** (icon number) or image name.
- Click OK.

---

## Create a Dialog Dynamically

You can also create a Dialog dynamically in the model depending on modeling needs.

### Steps to create a dynamic dialog

1. Insert a **Method**, a **DataTable**, and a **Dialog** (named `MyDynamicDialog` in the sample).
2. Program what the tabs show in the Method named `createDialog`.
3. Enter items shown on Tab 3 into the DataTable named `MyTable`.
4. Run `createDialog` to build and show the Dialog.
5. Program the action for double-clicking a row in the table on Tab 3.

### Sample `createDialog` code

```simtalk
Dialog.Label := "My Dynamic Dialog"; print Dialog.Label
var testBool:boolean := true
Dialog.clearData
testBool := testBool AND Dialog.createTabControl("TabControl", 0, 0, 45, 
10)
testBool := testBool AND Dialog.createTabPage("Tab 1","TabControl")
   testBool := testBool AND Dialog.createTabPage("Tab 2","TabControl")
   testBool := testBool AND Dialog.createTabPage("Tab 3","TabControl")
-- Menus
testBool := testBool AND Dialog.createMenu("Show")
testBool := testBool AND Dialog.createMenu("Item 1","Show")
testBool := testBool AND Dialog.createMenu("Item 2","Show")
dialog.setCallbackArgument("Item 1","Item 1 Arg")
dialog.setCallbackArgument("Item 2","Item 2 Arg")
-- Groups on different pages
testBool := testBool AND Dialog.createGroupBox("Group 1", 0,1, 40,3,"Tab 
1")
testBool := testBool AND Dialog.createGroupBox("Group 2", 0,4, 40,4,"Tab 
1")
testBool := testBool AND Dialog.createGroupBox("Group 1", 0,0, 40,3,"Tab 
2")
testBool := testBool AND Dialog.createGroupBox("Group 2", 0,4, 18,4,"Tab 
2")
testBool := testBool AND Dialog.createGroupBox("Group 3", 22,4, 18,4,"Tab 
2")
-- static text outside a group
testBool := testBool AND Dialog.createStaticTextBox("Static text", 
0,0,"Tab 1")
testBool := testBool AND Dialog.createStaticTextBox("Static text", 
0,0,"Tab 3")
Dialog.setCaption("Tab 3.Static text","Double-click a row ...")
-- static text inside a group
testBool := testBool AND Dialog.createStaticTextBox("Click the button", 
0,0,"Tab 1.Group 2")
-- Checkboxes
testBool := testBool AND Dialog.createCheckBox(" Check box 1", 15,0,"Tab 
1")
testBool := testBool AND Dialog.createCheckBox(" Check box 2", 
20,0,"Group 2")
--print Dialog.createCheckBox(" Check box 2", 20,0,"Tab 2.Group 2");
   testBool := testBool AND dialog.setCaption(" Check box 2","Checkbox Gr 
2")-- true
   dialog.setCallbackArgument(" Check box 2","CheckboxGr2")
-- checkbox with action
testBool := testBool AND Dialog.createCheckBox("Check box", 1,0,"Tab 
1.Group 1")
testBool := testBool AND Dialog.setCaption("Check box","Active")
dialog.setCallbackArgument("Check box","Check box")
-- Buttons
testBool := testBool AND Dialog.createButton("My_Button", 0, 1, 13, 
"Group 2")
testBool := testBool AND dialog.setCaption("My_Button","Security")-- true
dialog.setCallbackArgument("My_Button","Button Arg")
testBool := testBool AND Dialog.createButton("A_Button", 0, 1, 13, "Tab 
1.Group 1")
testBool := testBool AND Dialog.setCaption("A_Button","Attention")
Dialog.setSensitive("A_Button",false)
-- Radiobuttons and their groupings in a single group
-- note that radionbuttons of a group must be in a row of the dialog
testBool := testBool AND Dialog.createRadioButton("RadioButton 1",  3, 
0,"Tab 2.Group 1")
testBool := testBool AND Dialog.createRadioButton("RadioButton 2", 20, 
0,"Tab 2.Group 1")
testBool := testBool AND Dialog.createRadioButton("RadioButton 3",  3, 
1,"Tab 2.Group 1")
testBool := testBool AND Dialog.createRadioButton("RadioButton 4", 20, 
1,"Tab 2.Group 1")
Dialog.setGroupID("RadioButton 1", 1)-- row 0
Dialog.setGroupID("RadioButton 2", 1)-- row 0
Dialog.setGroupID("RadioButton 3", 2)-- row 1
Dialog.setGroupID("RadioButton 4", 2)-- row 1
-- radio button in different groups
testBool := testBool AND Dialog.createRadioButton("RB 1", 1, 0,"Tab 
2.Group 2")
testBool := testBool AND Dialog.createRadioButton("RB 2", 1, 1,"Tab 
2.Group 2")
testBool := testBool AND Dialog.createRadioButton("RB 3", 1, 0,"Tab 
2.Group 3")
testBool := testBool AND Dialog.createRadioButton("RB 4", 1, 1,"Tab 
2.Group 3")
Dialog.setGroupID("RB 1", 1)
Dialog.setGroupID("RB 2", 1)
Dialog.setGroupID("RB 3", 2)
Dialog.setGroupID("RB 4", 2)
--- Image in the dialog
testBool := testBool AND Dialog.createImage("My_Image", 25, 0, "Tab 
1.Group 1")
dialog.setIcon("My_Image","my icon")
testBool := testBool AND (dialog.getIcon("My_Image")= "my icon")
-- DropDownList
testBool := testBool AND dialog.createDropDownListBox("unit", 14, 
1,10,"Tab 1.Group 1")
var units:list[string]
units.create
units.insert(1,"mm")
units.insert(2,"m")
units.insert(3,"km")
testBool := testBool AND dialog.setList("unit",units)
dialog.setCallbackArgument("unit","DropDownList")
-- List box
testBool := testBool AND dialog.createListBox("ListBox", 17, 1, 18, 2, 
"Tab 1.Group 2")
testBool := testBool AND dialog.setList("ListBox",units)
dialog.setCallbackArgument("ListBox","ListBox Arg")
-- List view
testBool := testBool AND dialog.createListView("List view", 0, 2, 36, 6, 
"Tab 3")
testBool := testBool AND dialog.setTable("List view",MyTable)
dialog.setCallbackArgument("List view","List view Arg")
-- TextBox
testBool := testBool AND dialog.createEditTextBox("Text Box", 0, 2, 
13,"Tab 1.Group 2")
testBool := testBool AND dialog.setCaption("Text Box", "Enter Password")
testBool := testBool AND dialog.setPasswordMasking("Text Box",true)
dialog.open
print testBool
```

### Sample action code (double-clicking a row on Tab 3)

```simtalk
param action : string
var row:integer
print "Action : ",action
switch action
case "Open" 
case "Apply" 
case "Close" 
case "Button Arg" 
    @.setPasswordMasking("Text Box",NOT @.getPasswordMasking("Text Box"))
case "List view Arg" 
    row := @.getIndex("List view")
    promptmessage(to_str("Where is the ", MyTable[1,row],"?"))
case "Check box" 
    @.setSensitive("A_Button", @.getCheckBox("Check box"))
end
```

Double-clicking a row in the table shows a message box: `Where is the ...?`

---

## Program Actions which the Dialog Items Execute

Program the actions the dialog items execute when the user enters/selects a setting. Enter the source code into a **callback method**.

- By default the callback method is a user-defined attribute of data type `method` named `self.callback`.
  - Open it via the **Method** tab (click the Callback Method text box, press F2 or Shift+double-click Callback).
  - Or via the **User-defined Attributes** tab (double-click Callback, then Open).
- You can also use a Method in a Frame or Class Library folder (useful when several dialogs share the same callback method).

Enter the **Callback Argument** for each dialog item and the statements to execute. Parameters are **case-sensitive**.

The callback method executes the callback parameter when the user:

- Closes a drop-down list box.
- Selects and double-clicks an item in a list box.
- Changes a text box's contents and selects another item, or clicks OK/Apply/Cancel.
- Clicks a button.
- Selects/clears a check box.
- Selects a radio button.
- Selects and double-clicks a row in a list view.
- Selects a tab in a tab control.
- Selects a menu or menu command.

Example — to open `MyChart`:

```simtalk
case "CallbackChart" 
   MyChart.IsShown := true 
```

To open `MyReport`:

```simtalk
case "CallbackReport" 
   MyReport.show 
```

---

## Program Actions for Interacting with the Dialog

Program what happens when the user opens the dialog, applies settings, and closes it (as callback parameters in the Callback Method).

- **Open** section — executes when the user opens the dialog. Initializes contents/sets dialog items to values.
- **Apply** section — executes when the user clicks OK or Apply. Evaluates new or changed values.
- **Close** section — executes when the user clicks Cancel or closes with the title-bar Close button.

> **Note:** Clicking **OK** executes the callback method twice (first Apply, then Close). Clicking **Apply** executes only the Apply section.

### Sample source code

```simtalk
param action: string
switch action
case "Open" 
   @.setIndex("VariantType", @.VariantNo)
   @.setCheckbox("SunRoof", true)
   @.setValue("Vanity text", "Enter your text")
case "Apply" 
   @.VariantNo := @.getIndex("VariantType")
case "Close"
// no action is required
case "CallbackChart" 
   MyChart.IsShown := true 
case "CallbackReport" 
   MyReport.show
end 
```

When the dialog opens: Plant Simulation sets the car variant to the user-defined attribute `VariantNo`, selects the sun-roof check box, and prompts for vanity text.

---

## Setting Parameters with the AttributeExplorer

Instead of opening each object's dialog, the **AttributeExplorer** defines which attributes of which objects to get and show in a list window when you click **Show Explorer**.

Benefits:

- Manage attributes of individual stations at a single location.
- Enter different values for capacities, times, etc.; Plant Simulation writes values back to the object dialogs.
- Export the settings table as a tab-delimited text file and import it into another model for identical settings.
- Find objects of a defined type and attributes (e.g., positions) and align them in the Frame.

Insert the AttributeExplorer from the folder **InformationFlow** in the Class Library, or the toolbar **Information Flow** in the Toolbox.

You will:

- Specify the Objects You Want to Parametrize
- Specify the Attributes You Want to View or Change
- Select How to Show the Objects and the Names
- Find Objects and Attributes

---

## Specify the Objects You Want to Parametrize

Before typing data, click the **Inheritance** check box.

- **View/edit attributes of an object:** drag the object from the Frame over the **Objects** tab and drop it. Plant Simulation inserts the absolute path and name into the selected cell.
  - You can drag-and-drop multiple objects at once. Objects are added in selection order.
- **Add just the name:** drag the object over the icon of the AttributeExplorer.
- **View/edit attributes of all objects of one class:** click the **Query** tab and type `InternalClassType` as the Attribute and the internal class type as the Value.

> **Note:** For built-in objects, the read-only attribute `InternalClassType` returns the object type.

Click **Show Explorer** to see what you defined.

---

## Specify the Attributes You Want to View or Change

Before typing data, click the **Inheritance** check box.

- Type attribute names into the **Name** column cells, or click **Show Attributes**.

In the **Show Attributes** dialog:

- Click and select the Object whose attributes to show.
- Select **Built-in Attributes** or **User-defined Attributes**.
- Select a single or several contiguous attributes (Shift+click) and add them to **Explorer Attributes**.
- Click OK to add to the Attributes tab.

Additional settings:

- **Alias** column — enter a descriptive term for an attribute.
- **Read Only** column — click to make an attribute view-only.

### Cell background colors

| Color | Description |
|---|---|
| blue | The attribute is not watchable. |
| white | The attribute is watchable. |
| gray | You entered a wrong name for a built-in attribute. |

---

## Select How to Show the Objects and the Names

Before typing data, click the **Inheritance** check box.

Select what to do with the added attributes:

- **Edit** — allows editing values. Click Show Explorer, click a cell, type a value; changes are written back when you click Apply/OK.
- **Watch** — displays watchable attribute values (view only). Background colors indicate watchability (blue = not watchable, white = watchable, gray = wrong built-in name).
- **Read Only** — only shows values (view only).

Select how to show objects in the leftmost column:

- Entire **Path** (dragging over the Data tab inserts the absolute path).
- **Name** only (dragging over the icon inserts the name).
- **Label** only.

Select how to show attributes:

- With their **Name**.
- With their **Alias** (enter on the Attributes tab).

Optionally enter a **Comment** (Shift+Enter for a line break). Select **Show comment** and click Apply to display it above the list.

---

## Find Objects and Attributes

Use the AttributeExplorer to find objects in the model. Enter criteria into the **Query** tab, then click **Show Explorer** — the Explorer shows only matching objects.

To also change attributes, enter their names on the Attributes tab and select **Edit** on the Data tab.

In the Query table you can:

- Select the number of opening **Parentheses**.
- Enter the name of any attribute (as shown in Show Attributes and Methods).
- Select a **Condition**:

| Condition | Meaning |
|---|---|
| `<` | less than |
| `<=` | less than or equal to |
| `>` | greater than |
| `>=` | greater than or equal to |
| `=` | equal to (exact for real, length, height, speed, time) |
| `~=` | equal to, case-insensitive (strings) / about equal (values) |
| `/=` | not equal to |
| `Expr` | regular expression (e.g., `^Inf` finds words beginning with "Inf") |
| `Exists` | checks if the object has the attribute |

- Enter the **Value** to find.
- Select the number of closing **Parentheses**.
- Select a boolean **Operator** (`and` / `or`) connecting this row with the next.
- Enter a **Comment**.
- Select the **Frame** to start the search.
- Select **Include Subframes** to also include nested Frames.

> **Note:** Select "show objects with their path" on the Data tab for this setting.
