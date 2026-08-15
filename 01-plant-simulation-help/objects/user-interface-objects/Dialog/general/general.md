# Dialog [object]

Use the object **Dialog** for designing a dialog box for an object that is similar to the built-in dialog boxes.

## Description

With the object Dialog you can:

- Provide the user with a simple user interface for complex simulation models other users work with. This way you can ask the user to type in information which Plant Simulation needs to carry out a task.
- Prevent the user from manipulating a Frame in which you modeled a complex machine, etc. To do so, insert a Method object as an Open Control into the Frame. Double-clicking the Frame will then not open it any longer, but call the method. The method in turn executes the parameter that you typed in, i.e., it opens the dialog, where the user can then select the settings.

Each Dialog object manages a single dialog box. If you need more than one user-defined dialog box in your simulation model, insert as many Dialog objects as you need.

- To create and insert a dialog item, click the right mouse button on the tab **Elements** and select a dialog item on the context menu.
- To show the dialog you are creating, click **Show Dialog**.
- To edit the position of a dialog item, click **Edit Dialog**, select it and drag the mouse to a new location.

> **Note**
> - The display window of the object Dialog that contains menus does not use the standard Siemens PLM theme, but your Windows theme.
> - The display window of the object Dialog that does not contain menus uses the standard Siemens PLM theme.
> - The dialog box of the object Dialog uses the standard Siemens PLM theme.

To show a tooltip with information about the Dialog, hover with the mouse over it.

To change the length of the graphic and the anchor points of the Dialog, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Add the Object to the Simulation Model

To add the object Dialog to your simulation model, click **Manage Class Library > Basic Objects > UserInterface > Dialog** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then select the respective Category, Topic, and Example in the dialog *Examples Collection*, and click **Open Model**.

## Dialog Box of the Object Dialog

Double-click the icon of the Dialog to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:
- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

---

## Label [text box] - Dialog

Type in a Label for the dialog you create. As opposed to the name, you can type in any expression of your choice as the label, including special characters and blank spaces.

You can:
- Type in a label. Plant Simulation then shows that Label in the title bar of the dialog you created.
- Leave the text box Label empty. Plant Simulation then shows the Name of the Dialog object in the title bar of the dialog.

---

## Show Dialog [Dialog]

To show the dialog with the dialog items you created, click this button.

The Dialog executes the Callback Method with the parameters you typed into the text boxes for **Argument for Open**, **Argument for Apply** or **Argument for Close**. This way you can detect if they do what you programmed them to do.

> **Note**
> - Plant Simulation shows the dialog with the settings you select under *Personalization > Font* as well as with the settings you select under *Start > Settings > System > Display > Scale & layout*. If you change these settings, the dialog scales text, while the images always retain their size in pixels. For this reason it can happen that text overlaps the image. We recommend to test your dialogs with different display settings.
> - Dialog items which you create may be hidden by other dialog items if they have the same X and/or Y coordinates.
> - As opposed to the object Dialog provided by previous versions, which used one Callback Method per action, the current version uses a single callback method for defining all of the actions.

Instead, you can also right-click the Dialog object and select **Show Dialog** on the context menu in the Frame.

**SimTalk methods:** `openDialog`, `close`, `closeDialog`, `open`

---

## Edit Dialog [described]

To edit a dialog item which you created in the Dialog, click this button. The Dialog then selects the dialog item in the display window, and you can move it by dragging it to another position.

To edit its properties, click it with the right mouse button and select **Open** on the context menu.

Instead, you can also right-click the Dialog object and select **Edit Dialog** on the context menu in the Frame.

---

## Tab Elements

The tab **Elements** provides a context menu with the commands for inserting dialog items into the dialog you are creating.

- To insert a dialog item, click into the text box with the right mouse button and select the respective item on the context menu.
- You can also select to show or hide the **Default Buttons** (OK, Cancel and Apply) and to open the dialog you create **Modal** (the user cannot open another dialog until he closes the present dialog).
- Once you have inserted dialog items, the tree shows the structure of your dialog. Changing the order in the structure modifies the layout of the dialog.
- To change the order of the tabs, select a tab on the tab Elements, hold down Shift and press the up/down arrow to move the tab left/right. The dialog shows the first tab in the structure as the leftmost tab.

**Open:** To modify an existing dialog item, right-click it and select **Open**.

**Delete:** To delete a dialog item, right-click it and select **Delete**.

---

## Insert a Dialog Item into Your Dialog

Before you start creating your dialog, decide about its structure — which dialog items you need, whether you can show them all in a flat hierarchy or need tabs and menus.

The structure you decide upon determines how and in which order you create the dialog items. For example, to show dialog items on tabs: first create the **Tab Control** (container), then the individual **Tabs**, and finally insert the dialog items on each tab.

To create a new dialog item, select one of these on the context menu:

| | |
|---|---|
| New Button | New List View |
| New Check Box | New Menu / New Menu Command |
| New DropDownList Box | New Radio Button |
| New Edit Text Box | New Static Text Box |
| New Group Box | New Tab Control |
| New Image | New Tab Page |
| New List Box | |

- To add one tab at a time to a Tab Control, right-click it on the tab Elements, select **Tab Page**, and type in a name and caption.
- To add a dialog item to a tab, right-click the name of the tab in the structure and select the item.
- You can type in the same Name for dialog items as long as they are not in the same group. Groups are: Group Box, Menu, Tab Control, and Tab.
- To rearrange the order of items of type Tab within a Tab Control and Menu, use **Shift+Up arrow** or **Shift+Down arrow**.
- To move items out of a group or into one, drag them to the new location.

**SimTalk methods:** `getItemsList`, `deleteItem`

---

## New Button

Inserts a button into the dialog.

When the user clicks a button, it calls the Callback Method with the parameter you typed into **Callback Argument**. It in turn executes the actions you programmed.

Proceed as follows:
- Type in the **Name** of the button.
- Type in the **Caption** that the button displays.
- Type in its **X** and **Y** position in the Dialog.
- Type in its **Width**. The default value of 0 automatically sets the width to the width of the OK button.
- Select if you want to **Enable** the dialog item or not.
- Click **OK**.

**SimTalk methods:** `createButton`, `setCaption`, `setSensitive`

---

## New Check Box

Inserts a check box into the dialog. You can also select if the check box functions as an Inheritance box.

A check box displays a setting or a set of settings that do not exclude each other. The user can select or clear one or several check boxes at the same time.

Proceed as follows:
- Type in the **Name** of the check box.
- Type in the **Caption** that describes what the check box does.
- Type in the **Callback Argument**, which is passed to the Callback Method and executed when the user selects or clears the check box.
- Type in its **X** and **Y** position.
- Select if you want to **Enable** the dialog item or not.
- Select **Inheritance box** to show it as a check box for inheritance; clear it to show it as a normal check box.

Our callback method looks like this:

```SimTalk
param action: string
switch action
case "NameEdit"
   ?.setCheckBox("NameInherit", false)
   // clear check box when the value changes
case "Open"
   ?.setCaption("NameEdit", ?.NameValue)
   ?.setCheckBox("NameInherit", ?.NameValue.InheritValue)
case "Apply"
   var inherit:boolean := ?.getCheckBox("NameInherit") // 'inherit' is a user-defined variable
   if inherit
       ?.NameValue := ?.Origin.NameValue // 'NameValue' is a user-defined attribute
       ?.NameValue.InheritValue := true
       ?.setCaption("NameEdit", ?.NameValue)
   else
       ?.NameValue := ?.getValue("NameEdit")
       ?.NameValue.InheritValue := false
   end
end
```

**SimTalk methods:** `createCheckBox`, `getCheckBox`, `getInheritanceBox`, `getValue`, `setCaption`, `setCheckBox`, `setInheritanceBox`, `setSensitive`

---

## New DropDownList Box

Inserts a drop-down list box into the dialog.

The user can select a single item from the drop-down list. When closed, it displays the current value; when the user clicks the down arrow, it opens and displays more items.

Proceed as follows:
- Type in the **Name** of the drop-down list.
- Type in the **Callback Argument** (executed when the user closes the drop-down list box).
- Type in its **X** and **Y** position.
- Type in its **Width**. Default 0 sets the width to the values defined by us.
- Click **Items** and type in the items the list box displays.
- Select if you want to **Enable** the dialog item or not.
- Click **OK**.

**SimTalk methods:** `createDropDownListBox`, `setIndex`, `getIndex`, `setSensitive`, `setList`

---

## New Edit Text Box

Inserts an edit text box into the dialog.

The user can type text into the edit text box or edit text it already contains.

Proceed as follows:
- Type in the **Name** of the text box.
- Type in the **Callback Argument** (executed when the user changes the contents and selects another dialog item, clicks another text box, or clicks OK/Apply/Cancel). If the edit text box has a Callback Argument, the Callback Method is assigned the callback argument `_Enter` when the user presses Enter and the dialog does not show the Standard Buttons.
- Select which kind of characters the user can type:

| Setting | The user can type in |
|---|---|
| Any Character | any character, incl. special characters, lower/upper case letters and numbers |
| Letters and Digits | lower/upper case letters, umlauts, letters of any language, underscores, blanks, digits 0–9 |
| Letters | lower/upper case letters, umlauts, letters of any language, blanks |
| Decimal Number | 0123456789 |
| Signed Decimal Number | decimal numbers with sign: -+0123456789 |
| Hexadecimal Number | ADbf09, for example |
| Octal Number | 01234567 (but not 18) |
| Binary Number | 0 or 1 |
| Floating Point Number | 12.3E-45, for example |
| Time | time values |
| Date with Time | a date containing time values |
| Date | a date |
| Positive Real Number | a positive real number |

- Type in its **X** and **Y** position and its **Width**.
- Select if you want to **Enable** the dialog item or not.
- To show a password as superscripted lower case Xes instead of clear text, select the password masking option.
- Click **OK**.

**SimTalk methods:** `createEditTextBox`, `setEditType`, `setCaption`, `getValue`, `setSensitive`, `setPasswordMasking`, `getPasswordMasking`

---

## New Group Box

Inserts a group box. A group box graphically groups a set of dialog items or controls by drawing a frame around it.

Proceed as follows:
- Type in the **Name** of the group box.
- Type in the **Caption** the group box displays.
- Type in its **X** and **Y** position.
- Type in its **Width** and **Height**.
- Select if you want to **Enable** the dialog item or not.
- Click **OK**.

**SimTalk methods:** `createGroupBox`, `setCaption`, `setSensitive`

---

## New Image

Inserts an image into the dialog. An image is an icon you defined for the object Dialog. You can type in a number, or a name, such as `Icon1`.

Proceed as follows:
- Type in the **Name** of the image.
- Type in its **X** and **Y** position.
- Type in its **Width** and **Height**.
- Type in the **Image ID**, i.e., the number of the icon, or an image name. The image is an icon of the Dialog to which the image belongs.

**SimTalk methods:** `createImage`, `setIcon`, `getIcon`

---

## New List Box

Inserts a list box into the dialog. A list box displays a list of choices. The user can double-click one of the items to select it. The list does not collapse.

Proceed as follows:
- Type in the **Name** of the list box.
- Type in the **Callback Argument** (executed when the user selects and double-clicks an item).
- Type in its **X** and **Y** position.
- Type in its **Width** and **Height**. If you do not type in values, defaults are used. When you type in a height, it adds a vertical scrollbar if the list contains more items than the height.
- Click **Items** and type in the items the list box displays.
- Select if you want to **Enable** the dialog item or not.
- Click **OK**.

**SimTalk methods:** `getIndex`, `setList`, `setSensitive`, `getValue`

---

## New List View

Inserts a list view into the dialog. A list view shows a table in the dialog.

> **Note**
> - When displaying strings, Plant Simulation only shows the first 260 characters.
> - The user can only select rows, but no columns or individual cells.

Proceed as follows:
- Type in the **Name** of the list view.
- Type in the **Callback Argument** (executed when the user double-clicks a row).
- Type in the name of a table or click and select a table in the dialog *Select Object*. Type the items into the cells of the columns.
- Type in its **X** and **Y** position.
- Type in its **Width** and **Height**.
- Select if you want to **Enable** the dialog item or not.
- Click **OK**.

**SimTalk methods:** `createListView`, `setTableRow`, `getTableRow`, `setSensitive`, `getTable`, `setTable`

---

## New Menu / New Menu Command

Inserts a menu or a menu command into the dialog. A menu provides a list of textual choices from which the user can choose. The Dialog inserts the menus along the top of the dialog.

Proceed as follows:
- Type in the **Name** of the menu.
- Type in the **Caption** of the menu. Type a hyphen (`-`) as the caption of a menu command to insert a separator between groups of commands.
- Type in the **Callback Argument** (executed when the user selects a menu or command).
- Select if you want to **Enable** the dialog item or not.
- Click **OK**.
- To add one menu command at a time, right-click the menu and select **New Menu/New Menu Command** again; type in Name, Caption, Callback Argument, Enable.
- To add a submenu, right-click a menu command and select **New Menu/New Menu Command** again.

> **Note:** The display window of the Dialog that contains menus uses your Windows theme (not the Siemens PLM theme).

**SimTalk methods:** `createMenu`, `setCaption`, `setSensitive`

---

## New Radio Button

Inserts a radio button into the dialog. A set of radio buttons enables the user to select a single setting from a fixed set of choices that exclude each other.

Proceed as follows:
- Type in the **Name** of the radio button.
- Type in the **Caption** that describes what the radio button does.
- Type in the **Callback Argument** (executed when the user selects the radio button).
- Type in its **X** and **Y** position.
- Type in a **Group ID** (a number) for grouping radio buttons that belong together. The user can only select one radio button of a group.
- Select if you want to **Enable** the dialog item or not.

> **Note:** You have to create all items of a group of radio buttons sequentially, because Plant Simulation creates the items according to their row and column position. Windows groups radio buttons row by row according to the Y-coordinate, ignoring the Group ID for layout. If you want side-by-side groups (e.g., Red/Blue and Round/Square), do not place the radio buttons loosely — group them within group boxes.

**SimTalk methods:** `createRadioButton`, `setCheckBox`, `getCheckBox`, `setCaption`, `setGroupID`, `setSensitive`, `getValue`

---

## New Static Text Box

Inserts a static text box into the dialog. A static text box shows text that the user can view, but not edit.

Proceed as follows:
- Type in the **Name** of the static text box.
- Type in the **Caption** that the static text box shows.
- Type in its **X** and **Y** position.
- Select if you want to **Enable** the dialog item or not.
- Click **OK**.

**SimTalk methods:** `createStaticTextBox`, `setCaption`, `setSensitive`

---

## New Tab Control

Inserts a tab control into the dialog. A tab control resembles a notebook that contains any number of pages. The user can navigate between different tabs and/or sections of information.

> **Note:** Do not confuse the tab control with a single tab. The tab control is the container that holds the individual tabs (pages).

When the user selects another tab, the Dialog calls the Callback Method with the first parameter typed as Callback Argument.

Proceed as follows:
- Type in the **Name** of the tab control.
- Type in the **Callback Argument** (executed when the user selects a tab).
- Type in its **X** and **Y** position.
- Type in its **Width** and **Height**.
- Click **OK**.
- To add one tab at a time, right-click it on the tab Elements and select **New Tab Page**.

> **Note:** To change the order of the tabs, select a tab, hold down Shift and press the up/down arrow to move it left/right.

**SimTalk methods:** `createTabControl`, `setTab`, `getIndex`, `getValue`, `setList` (applies for all tab pages of the tab control)

---

## New Tab Page

To insert a tab at a time to the tab control, right-click it on the tab Elements and select **New Tab Page**. A tab offers settings that belong together.

Proceed as follows:
- Type in the **Name** of the tab into the dialog *Dialog Item Tab Page*.
- Type in the **Caption** of the tab. The tab shows this caption as the title on the tab itself.

**SimTalk methods:** `createTabPage`, `setCaption` (applies when you change the caption of one tab page only), `setTab`

---

## Define Properties of a Dialog Item

Depending on the type of item you define, the Dialog shows one or all of these items:

Name, Caption, Callback Argument, X, Y, Group ID, Image ID, Width, Height, Enable, Items

### Name [dialog item in Dialog]

Type in the Name of the dialog item. The Dialog shows this Name in the text box on the tab Elements.

- You can type in the same Name for dialog items as long as they are not in the same group (Group Box, Menu, Tab Control, Tab).
- We recommend a unique identifier containing the type, e.g. `xyz_button`, `xyz_list`.
- You cannot use a period (`.`) in the name. As SimTalk treats this name as a string, you can type in special characters.
- A Method object can call this dialog item using the Name.

**SimTalk methods:** `setCaption`, `getValue`

### Caption [text box] - Dialog

Type in the text which the Dialog shows as the caption of the dialog item.

A caption is handy if you develop libraries in several languages and want the user to switch languages. You can type in special characters and blanks, which you cannot use in the name.

The Caption applies to: New Static Text Box, New Button, New Group Box, New Check Box, New Menu/New Menu Command, New Tab Page, New Radio Button.

**Create an Access Key:** Type the ampersand `&` in front of a letter to make it the access key (mnemonic key). Plant Simulation activates the item when you press **Alt + that letter**. To use `&` literally (e.g., "Drag & Drop"), type it twice: `Drag && Drop`.

> **Note:** If dialogs do not show access keys, ensure *Settings > Ease of Access > Keyboard > Change how keyboard shortcuts work* is On.

**SimTalk methods:** `setCaption`, `getValue`

### Callback Argument [text box] - Dialog

Type in the parameter that is passed to the Callback Method. Parameters are case-sensitive.

The callback method executes this parameter when the user:
- Closes the DropDownList Box.
- Selects and double-clicks an item in the List Box.
- Changes the contents of the Text Box and selects another dialog item afterward, clicks another text box, or clicks OK/Apply/Cancel (the `_Enter` argument is assigned when Enter is pressed with no Standard Buttons).
- Clicks the Button.
- Selects or clears the Check Box.
- Selects the Radio Button.
- Selects a row in the List View and double-clicks it.
- Selects a tab in the Tab Control.
- Selects a Menu/Menu Command.

**SimTalk methods:** `setCallbackArgument`

### X [text box] - Dialog

Type in the x-axis position where Plant Simulation places the dialog item. The value corresponds to the average width of characters of your system font, **not** pixels.

If you typed identical values for different dialog items, the Dialog places them on top of each other.

**SimTalk methods:** `DialogX`, `DialogY`

### Y [text box] - Dialog

Type in the y-axis position. The value corresponds to lines of characters of the system font, **not** pixels. You can type in a value from 0 to 10 for example.

**SimTalk methods:** `DialogY`, `DialogX`

### Group ID

For a dialog item of Type > Radio Button. Type in a number to group radio buttons that belong together. The user can only select one radio button of a group.

**SimTalk methods:** `setGroupID`

### Image ID

For a dialog item of Type > Image. Type in the number of the icon, or the name of the image. The image is an icon of the Dialog to which it belongs.

**SimTalk methods:** `createImage`, `setIcon`, `getIcon`

### Width [text box] - dialog item

Type the Width of the dialog item in the average width of characters of your system font. The default value of 0 sets the width to the values defined by us.

### Height [text box] - dialog item

Type in the Height of the dialog item in lines of characters of your system font. The default value of 0 sets the height to the values defined by us.

### Enable [check box] - dialog item

Select this check box to enable the respective dialog item; clear it to disable it.

Shown for: New Button, New Check Box, New Radio Button, New Edit Text Box, New List Box, New List View.

- **Select Enable** to activate the item; when the user selects it, it triggers the Callback Method.
- **Clear it** to deactivate the item (gray it out) and make it unavailable.

**SimTalk methods:** `setSensitive`

### Items [Dialog]

Shown for dialog items of Type > DropDown List Box and ListBox. Click **Items** to open a dialog into which you type the items they show:

- **Insert** — add an item (type the name, click Insert or press Enter).
- **Delete** — remove a selected item.
- **Move Up** — move an item up one position.
- **Rename** — change the name of a selected item.

Click **OK** to apply; click **Cancel** to discard.

**SimTalk methods:** `setIndex`, `getIndex`, `setList`, `setCaption`, `getValue`

---

## Show Default Buttons [check box]

To show the standard buttons (OK, Cancel, Apply) in the dialog you are creating, select this check box. To hide them, clear it.

If you do not show the button combination OK, Cancel, and Apply, you have to define your own buttons to provide the user a way to apply or discard settings.

**SimTalk:** `ShowStandardButtons`

---

## Open Modal [check box]

To open the dialog box modal (the user cannot open other Plant Simulation dialog boxes until he closes it), select this check box. Clear it to allow the user to open other dialog boxes in addition.

**SimTalk:** `OpenModal`

---

## Tab Position

### X-Position [dialog item]

Type in the x-axis position (of the screen) at which Plant Simulation shows the Dialog when you open it.

- Default `-1` for both X-Position and Y-Position centers the Dialog on screen.
- Unit is pixels; the zero point is the top left corner of the screen.

**SimTalk:** `getUserDialogXYWH`

### Y-Position [dialog item]

Type in the y-axis position of the screen at which the Dialog is shown. Default `-1` centers the Dialog; unit is pixels; zero point is top left corner.

**SimTalk:** `getUserDialogXYWH`

---

## Tab Method

The parameters are going to be called when Plant Simulation executes the Callback Method.

### Callback Method [text box] - Dialog

Creates a Callback Method for the Dialog. Proceed as follows:

- Click and select a Method in the dialog box *Select Object*, then type in the source code. Or accept the default, namely the user-defined attribute of data type method named `self.callback`.
- Select the Method in a Frame, drag it to the text box and drop it there.
- Select **Create Control** and create the control as a Method of the object.

To edit the source code later: press **F2**, or hold **Shift** and double-click into the text box, or click the tab **User-defined** and double-click the Method name.

**Parameters** — the callback method can have these sections:

- **Open** — initializes the contents of the dialog box or sets the dialog items to values of your choice.
- **Apply** — executed when the user clicks OK or Apply; the source code may evaluate new or changed values.
- **Close** — executed when the user clicks Cancel or closes with Close on the title bar.

The Dialog executes the Callback Argument of each item:
- Drop-down List Box — when the user closes it.
- List Box — when the user selects and double-clicks an item.
- Text Box — when the user changes contents and selects another item, clicks another text box, or clicks OK/Apply/Cancel.
- Button — when the user clicks the button.
- Check Box — when the user selects or clears it.
- Radio Button — when the user selects it.
- List View — when the user selects a row and double-clicks it.
- Tab Control — when the user selects a tab.
- Menu/Menu Command — when the user selects a menu or command.

**SimTalk:** `CallbackMethod`

### Argument for Open [text box]

Type in the name of the callback argument for the Open action. The default is `Open`. The Open section initializes the contents of the dialog box.

**SimTalk:** `ArgumentForOpen`

### Argument for Apply [text box]

Type in the name of the callback argument for the Apply action. The default is `Apply`. The Apply section is executed when the user clicks OK or Apply.

> **Note:** When the user clicks **OK**, the Dialog executes the callback method twice — first the Apply section, then the Close section. When the user clicks **Apply**, only the Apply section is executed.

**SimTalk:** `ArgumentForApply`

### Argument for Close [text box]

Type in the name of the callback argument for the Close action. The default is `Close`. The Close section is executed when the user clicks Cancel or closes with the Close button on the title bar.

> **Note:** When the user clicks **OK**, the callback method is executed twice — Apply first, then Close. When the user clicks **Apply**, only Apply is executed.

**SimTalk:** `ArgumentForClose`

---

## Tab User-defined

Define your own attributes as described under the Tab User-defined. The Dialog provides the Callback method as a user-defined attribute.

## Navigate Menu / View Menu / Tools Menu / Help Menu

- **Navigate Menu** — commands described under the Navigate Menu.
- **View Menu** — commands described under the View Menu. SimTalk: `updateDialog`.
- **Tools Menu** — provides commands: Edit Controls, Edit Observers.
- **Help Menu** — commands described under the Help Menu.

---

## Methods of the Dialog

The Dialog provides:
- The methods listed in the table of contents.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show those of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show those of the selected Instance.

---

## Appendix: Example Code

### WindowWidth (SimTalk)

```SimTalk
MyHtmlReport.WindowWidth :=  800 // pixels
```

### Callback method example (New Check Box / Inheritance box)

```SimTalk
param action: string
switch action
case "NameEdit"
   ?.setCheckBox("NameInherit", false)
   // clear check box when the value changes
case "Open"
   ?.setCaption("NameEdit", ?.NameValue)
   ?.setCheckBox("NameInherit", ?.NameValue.InheritValue)
case "Apply"
   var inherit:boolean := ?.getCheckBox("NameInherit") // 'inherit' is a user-defined variable
   if inherit
       ?.NameValue := ?.Origin.NameValue // 'NameValue' is a user-defined attribute
       ?.NameValue.InheritValue := true
       ?.setCaption("NameEdit", ?.NameValue)
   else
       ?.NameValue := ?.getValue("NameEdit")
       ?.NameValue.InheritValue := false
   end
end
```
