# Methods of the Dialog

The Dialog provides:

- The methods listed in the table of contents (below).
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Syntax line conventions

An example of the Syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method (identifier and data type of the parameter) is listed in parentheses. `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. `[,Parameter:boolean]` means that you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter (`:= false` in the example above).
- If the method has a return value, the signature shows its data type after the arrow (`→ boolean` in the example above).

---

## clearData

Deletes the dialog items of the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.clearData`

```simtalk
MyDialog.clearData
```

---

## close

Closes the dialog box of the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.close(OK:boolean)`
- **Parameter:** `OK` (boolean) designates the action which the dialog takes (OK or Cancel). Specify `true` to apply the changes the user made, or `false` to cancel all changes.

```simtalk
MyDialog.close(true)
```

**See also:** Show Dialog [Dialog], open

---

## closeDialog

Closes the dialog box of the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.closeDialog([ApplyChanges:boolean:=true]) → boolean`
- **Parameter:** `ApplyChanges` (boolean, optional) determines if Plant Simulation ignores all changes the user made in the dialog, or accepts and applies them. `true` makes the Dialog evaluate all settings and apply them as new values; `false` discards the changes.
- **Default Value:** `true`
- **Return Value:** boolean

```simtalk
MyDialog.closeDialog(true)
```

**See also:** Show Dialog [Dialog], openDialog

---

## createButton

Creates a Button in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createButton(Name:string, X:integer, Y:integer, Width:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the button. *(Set the Caption with `setCaption`.)*
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Width` (integer) — Width of the button.
  - `Parent` (string, optional) — parent (e.g. a Group Box or Tab Page).
- **Return Value:** boolean

```simtalk
MyTabbedDialog.createButton("Order", 7, 7, 18, "MyTab4")
```

**See also:** New Button

---

## createCheckBox

Creates a Check Box in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createCheckBox(Name:string, X:integer, Y:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the check box. *(Set the Caption with `setCaption`.)*
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Parent` (string, optional) — parent (e.g. a Group Box or Tab Page).
- **Return Value:** boolean

```simtalk
MySimpleDialog.createCheckBox("SunRoof", 9, 6)
```

**See also:** New Check Box, getValue

---

## createDropDownListBox

Creates a Drop-Down List Box in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createDropDownListBox(Name:string, X:integer, Y:integer, Width:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the drop-down list box.
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Width` (integer) — Width of the drop-down list box.
  - `Parent` (string, optional) — parent (e.g. a Group Box or Tab Page).
- **Return Value:** boolean

```simtalk
MyDialog.createDropDownListBox("unit", 12, 1, 10, "Page.Group")
units.create
units.insert(1,"mm")
units.insert(2,"m")
units.insert(3,"km")
MyDialog.setList("unit",units)
```

**See also:** New DropDownList Box, getValue

---

## createEditTextBox

Creates an Edit Text Box in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createEditTextBox(Name:string, X:integer, Y:integer, Width:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the edit text box.
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Width` (integer) — Width of the edit text box.
  - `Parent` (string, optional) — parent (e.g. a Group Box or Tab Page).
- **Return Value:** boolean

```simtalk
MySimpleDialog.createEditTextBox("Vanity text", 15, 7, 18)
```

**See also:** New Edit Text Box, getValue

---

## createGroupBox

Creates a Group Box in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createGroupBox(Name:string, X:integer, Y:integer, Width:integer, Height:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the group box. *(Set the Caption with `setCaption`.)*
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Width` (integer) — Width of the group box.
  - `Height` (integer) — Height of the group box.
  - `Parent` (string, optional) — parent (e.g. a Tab Page).
- **Return Value:** boolean

```simtalk
MySimpleDialog.createGroupBox("Drive", 4, 26, 4)
```

**See also:** New Group Box

---

## createImage

Creates an Image in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createImage(Name:string, X:integer, Y:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the image.
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Parent` (string, optional) — parent (e.g. a Group Box or Tab Page).
- **Return Value:** boolean

```simtalk
MyTabbedDialog.createImage("ImageItem", 40, 1, "MyTab4")
MyTabbedDialog.setIcon("ImageItem", "CompanyLogo")
```

**See also:** New Image, setIcon

---

## createListBox

Creates a List Box in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createListBox(Name:string, X:integer, Y:integer, Width:integer, Height:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the list box.
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Width` (integer) — Width of the list box.
  - `Height` (integer) — Height of the list box.
  - `Parent` (string, optional) — parent (e.g. a Group Box or Tab Page).
- **Return Value:** boolean

```simtalk
MyTabbedDialog.createListBox("ModelList", 18, 0, 16, 2, "MyTab1")
```

**See also:** New List Box, getValue

---

## createListView

Creates a List View in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createListView(Name:string, X:integer, Y:integer, Width:integer, Height:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the list view.
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Width` (integer) — Width of the list view.
  - `Height` (integer) — Height of the list view.
  - `Parent` (string, optional) — parent (e.g. a Group Box or Tab Page).
- **Return Value:** boolean

```simtalk
MyTabbedDialog.createListView("Configuration", 0, 1, 36, 5, "MyTab4")
```

**See also:** New List View

---

## createMenu

Creates a Menu / Menu Command in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createMenu(Name:string[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the menu. *(Set the Caption with `setCaption`.)*
  - `Parent` (string, optional) — parent of the menu items or sub-menus. For the top-level menu you do not need a parent.
- **Return Value:** boolean

```simtalk
MySimpleDialog.createMenu("Show")
```

**See also:** New Menu / New Menu Command

---

## createRadioButton

Creates a Radio Button in the Dialog designated by `<Path>`.

> **Remarks:** You have to create all items of a group of radio buttons sequentially, because Plant Simulation creates the items according to their row and column position. You cannot arrange two sets of radio buttons side by side (e.g. Red/Blue on the left and Round/Square on the right) as two groups. Windows ignores the Group ID you enter and groups the radio buttons row by row according to the Y-coordinate — it treats Red and Round as one group, and Blue and Square as the other. To model such a layout, place the radio buttons within group boxes instead of loosely onto the dialog.

- **Type:** Method
- **Syntax:** `<Path>.createRadioButton(Name:string, X:integer, Y:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the radio button. *(Set the Caption with `setCaption`.)*
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Parent` (string, optional) — parent (e.g. a Group Box or Tab Page).
- **Return Value:** boolean

```simtalk
MySimpleDialog.createRadioButton("Frontwheel", 3, 0)
```

**See also:** New Radio Button, Add a Set of Radio Buttons, setGroupID, getValue

---

## createStaticTextBox

Creates a Static Text Box in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createStaticTextBox(Name:string, X:integer, Y:integer[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the static text box. *(Set the Caption with `setCaption`.)*
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Parent` (string, optional) — parent (e.g. a Group Box or Tab Page).
- **Return Value:** boolean

```simtalk
MySimpleDialog.createStaticTextBox("Vanity", 5, 7)
```

**See also:** New Static Text Box

---

## createTabControl

Creates a Tab Control in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createTabControl(Name:string, X:integer, Y:integer, Width:integer, Height:integer) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the tab control.
  - `X` (integer) — position on the X-axis.
  - `Y` (integer) — position on the Y-axis.
  - `Width` (integer) — Width of the tab control.
  - `Height` (integer) — Height of the tab control.
- **Return Value:** boolean

```simtalk
MyTabbedDialog.createTabControl("TabControl", 0, 0, 64, 10)
```

**See also:** New Tab Control, getValue

---

## createTabPage

Creates a Tab Page in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.createTabPage(Name:string[, Parent:string]) → boolean`
- **Parameters:**
  - `Name` (string) — Name of the tab page. *(Set the Caption with `setCaption`.)*
  - `Parent` (string, optional) — parent of the tab page, i.e. the Tab Control.
- **Return Value:** boolean

```simtalk
MyTabbedDialog.createTabPage("MyTab1")
```

**See also:** New Tab Page

---

## deleteItem

Deletes the specified dialog item from the Dialog specified by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.deleteItem(DialogItem:string) → boolean`
- **Parameter:** `DialogItem` (string) — the dialog item to delete.
- **Return Value:** boolean — `true` if the dialog item was deleted successfully; `false` if not deleted (e.g. because the dialog item is inherited).

```simtalk
MyTabbedDialog.deleteItem("SunRoof")
```

---

## getCheckBox

Returns whether the Check Box or the Radio Button in the Dialog designated by `<Path>` is selected (`true`) or cleared (`false`).

- **Type:** Method
- **Syntax:** `<Path>.getCheckBox(DialogItem:string) → boolean`
- **Parameter:** `DialogItem` (string) — the Check Box or the Radio Button.
- **Return Value:** boolean

```simtalk
print MyDialog.getCheckBox("My_CheckBox")
```

**See also:** setCheckBox

---

## getIcon

Returns the Image ID or the image name of the image in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.getIcon(DialogItem:string) → string`
- **Parameter:** `DialogItem` (string) — the dialog item.
- **Return Value:** string

```simtalk
print MyDialog.getIcon("My_Image")
```

**See also:** New Image, Image ID, setIcon

---

## getIndex

Returns the number of the designated dialog item in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.getIndex(DialogItem:string) → integer`
- **Parameter:** `DialogItem` (string) — the List Box, the Drop-Down List Box, or the Tab Page. The leftmost tab has the number 1.
  - If you assign another list and it is possible, the Dialog selects the item at the same position in the list box.
  - If it is not possible to select the same position, the Dialog automatically selects the first item in the new list.
- **Return Value:** integer — `0` if the drop-down list box does not contain any items; `1` if it does contain items and no item is selected (the Dialog automatically selects the first item).

```simtalk
print MyDialog.getIndex("doors")
print MyDialog.getIndex("units")
```

**See also:** setIndex, Position of the item in the Items [Dialog] list

---

## getInheritanceBox

Returns the current mode (selected or cleared) of the Inheritance Box of the specified check box in the Dialog designated by `<Path>`.

- **Remarks:** If `true`, the Dialog shows the check box as a check box for inheritance. If `false`, the Dialog shows it as a normal check box.
- **Type:** Method
- **Syntax:** `<Path>.getInheritanceBox(DialogItemName:string) → boolean`
- **Parameter:** `DialogItemName` (string) — name of the check box defined as an Inheritance Box.
- **Return Value:** boolean

```simtalk
print MySimpleDialog.getInheritanceBox("InheritanceBoxSunRoof")
```

**See also:** New Check Box, setInheritanceBox

---

## getItemsList

Returns the full path within the dialog, the name and the type of each dialog item in the Dialog designated by `<Path>`, and writes it into a table.

- **Type:** Method
- **Syntax:** `<Path>.getItemsList(Table:table)`
- **Parameter:** `Table` (table) — the name of the table.

```simtalk
MyDialog.getItemsList(MyElementsTable)
```

**See also:** Name [dialog item in Dialog]

---

## getPasswordMasking

Returns the state of the check box **Password** for a dialog item of type Edit Text Box in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.getPasswordMasking(DialogItem:string) → boolean`
- **Parameter:** `DialogItem` (string) — the check box Password.
- **Return Value:** boolean — `true` if selected, `false` if cleared.

```simtalk
print MyDialog.getPasswordMasking("MyEditTextBox")
```

**See also:** New Edit Text Box, setPasswordMasking

---

## getTable

Returns the name of the table that defines the items which a List View in the Dialog designated by `<Path>` shows.

- **Type:** Method
- **Syntax:** `<Path>.getTable(ListView:string) → string`
- **Parameter:** `ListView` (string) — the list view.
- **Return Value:** string

```simtalk
var table_path : string
table_path := MyDialog.getTable("myListView")
```

**See also:** New List View, setTable

---

## getTableRow

Returns the number of the row in the Items Table that defines the items which a List View in the Dialog designated by `<Path>` shows and which the user selected.

- **Type:** Method
- **Syntax:** `<Path>.getTableRow(Table:string) → integer`
- **Parameter:** `ListView` (string) — the list view.
- **Return Value:** integer

```simtalk
print MyDialog.getTableRow("ListView")
```

**See also:** New List View, Items [Dialog], setTableRow

---

## getUserDialogXYWH

Returns the position of the Dialog designated by `<Path>` and assigns the coordinates to the local variables you specify.

- **Type:** Method
- **Syntax:** `<Path>.getUserDialogXYWH(byRef X:integer, byRef Y:integer, byRef Width:integer, byRef Height:integer)`
- **Parameters:**
  - `X` (integer, byRef) — x-coordinate of the dialog.
  - `Y` (integer, byRef) — y-coordinate of the dialog.
  - `Width` (integer, byRef) — width.
  - `Height` (integer, byRef) — height.

```simtalk
var x,y,w,h: integer
MyDialog.getUserDialogXYWH(x,y,w,h)
print x," ",y," ",w," ",h
```

**See also:** setXYWH, getXYWH

---

## getValue

Returns the changed value of the dialog item in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.getValue(DialogItem:string) → string`
- **Parameter:** `DialogItem` (string) — a dialog item of type Drop-Down List Box, Check Box, Radio Button, List Box, Edit Text Box, or Tab Control. When applied to a Tab Control, it returns the name of the active tab.
- **Return Value:** string

```simtalk
var value: string
var number : integer
value := MyDialog.getValue("unit")
number := str_to_num(value)
```

**See also:** createCheckBox, createDropDownListBox, createEditTextBox, createRadioButton, createTabControl, setCaption

---

## open

Opens the dialog box of the Dialog designated by `<Path>` at the specified position on screen.

- **Type:** Method
- **Syntax:** `<Path>.open(X:integer, Y:integer)`
- **Parameters:**
  - `X` (integer) — X-position at which Plant Simulation opens the dialog box.
  - `Y` (integer) — Y-position at which Plant Simulation opens the dialog box.

```simtalk
MyDialog.open(100,100)
```

**See also:** Show Dialog [Dialog], close, X-Position [dialog item], Y-Position [dialog item]

---

## openDialog

Opens the dialog box of the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:**
  ```
  <Path>.openDialog → boolean
  <Path>.openDialog(CallOpenControl:boolean:=false) → boolean
  ```
- **Parameter:** `CallOpenControl` (boolean) — sets whether Plant Simulation opens the dialog box the same way as double-clicking the icon does and also executes any existing Open Control (`true`), or only opens the dialog (`false`).
- **Default Value:** `false`
- **Return Value:** boolean — `true` if Plant Simulation succeeded in opening the dialog.

```simtalk
myDialog.openDialog
.Models.Model.myDialog.openDialog(false)
```

**See also:** Show Dialog [Dialog], Open Control, closeDialog

---

## setActiveTabPage

Activates the designated tab of the designated tab control of the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.setActiveTabPage(TabControl:string, TabPageName:string)`
- **Parameters:**
  - `TabControl` (string) — the tab control that contains the tab to be activated.
  - `TabPageName` (string) — the tab that will be activated.

```simtalk
MyDialog.setActiveTabPage("MyTabControl", "Page1")
```

**See also:** New Tab Control, New Tab Page

---

## setCallbackArgument

Sets the Callback Argument which the Callback Method of the Dialog designated by `<Path>` executed.

- **Remarks:** The Console shows this parameter if you show it in the Callback method.
- **Type:** Method
- **Syntax:** `<Path>.setCallbackArgument(DialogItem:string, Argument:string) → integer`
- **Parameters:**
  - `DialogItem` (string) — the dialog item to which the callback argument applies.
  - `Argument` (string) — the value of the callback argument.
- **Return Value:** integer

```simtalk
MyDialog.setCallbackArgument("TabControl.Page1.Save","Bill")
```

**See also:** Callback Argument [text box] - Dialog, Callback Method [text box] - Dialog

---

## setCaption

Sets the Caption (i.e. the description) of a dialog item of the Dialog designated by `<Path>`.

- **Remarks:** Plant Simulation shows changes immediately. `setCaption` applies to these dialog items:
  - Static Text Box — changes its caption.
  - Edit Text Box — changes the contents of the text box.
  - Tab Page — changes the label of the tab.
  - Button — changes the label of the button.
  - Group Box — changes its caption.
  - Menu/Menu Command — changes its caption.
  - Check Box — changes its caption.
  - Radio Button — changes its caption.
- **Type:** Method
- **Syntax:** `<Path>.setCaption(DialogItem:string, Caption:string) → boolean`
- **Parameters:**
  - `DialogItem` (string) — the dialog item to which the caption applies.
  - `Caption` (string) — the text to assign as the caption.
- **Return Value:** boolean

```simtalk
MyDialog.setCaption("object",current.name)
if Station.failed
   MyDialog.setCaption("state","failed")
else
   MyDialog.setCaption("state","ready")
end
```

**See also:** Caption [text box] - Dialog, getValue

---

## setCheckBox

Sets whether the Check Box or the Radio Button of the Dialog designated by `<Path>` will be selected (`true`) or cleared (`false`).

- **Type:** Method
- **Syntax:** `<Path>.setCheckBox(DialogItem:string, Active:boolean) → boolean`
- **Parameters:**
  - `DialogItem` (string) — the dialog item.
  - `Active` (boolean) — sets if it will be activated (`true`) or not (`false`).
- **Return Value:** boolean

```simtalk
MyDialog.setCheckBox("My_CheckBox",true)
```

**See also:** New Check Box, New Radio Button, getCheckBox

---

## setEditType

Sets the data type of the Edit Text Box of the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.setEditType(DialogItem:string, Type:string)`
- **Parameters:**
  - `DialogItem` (string) — the name or the name and path of the edit text box.
  - `Type` (string) — which kind of characters the user can type into the edit text box.

| Setting | The user can type in |
| --- | --- |
| Any Character | any character (special characters, lower/upper case letters, numbers) |
| Letters and Digits | lower/upper case letters (incl. umlauts and letters of any language), underscores, blank spaces, and digits 0–9 |
| Letters | lower/upper case letters (incl. umlauts and letters of any language) and blank spaces |
| Decimal Number | 0123456789 |
| Signed Decimal Number | decimal numbers with a negative or positive sign: -+0123456789 |
| Hexadecimal Number | ADbf09, for example |
| Octal Number | 01234567 (not 18, for example) |
| Binary Number | 0 or 1 |
| Floating Point Number | 12.3E-45, for example |
| Time | time values |
| Date with Time | a date containing time values |
| Date | a date |
| Positive Real Number | a positive real number |

```simtalk
MyDialog.setEditType("MyEditTextBox", "Letters and Digits")
```

**See also:** New Edit Text Box

---

## setGroupID

Sets the Group ID of dialog items of a Radio Button of the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.setGroupID(DialogItem:string, Group:integer)`
- **Parameters:**
  - `DialogItem` (string) — the dialog item.
  - `Group` (integer) — the group ID.

```simtalk
MySimpleDialog.setGroupID("Frontwheel", 1)
MySimpleDialog.setGroupID("Rearwheel", 1)
MySimpleDialog.setGroupID("MagRim", 2)
MySimpleDialog.setGroupID("SteelRim", 2)
```

**See also:** Group ID, New Radio Button

---

## setIcon

Sets the Image ID of a dialog item of the Dialog designated by `<Path>` to the specified value.

- **Type:** Method
- **Syntax:** `<Path>.setIcon(DialogItem:string, ImageID:string) → boolean`
- **Parameters:**
  - `DialogItem` (string) — the dialog item.
  - `ImageID` (string) — an Image ID or an Image Name that is an icon of the Dialog to which the image belongs.
- **Return Value:** boolean

```simtalk
MyDialog.setIcon("My_Image","Logo")
MyDialog.setIcon("My_Image","3")
```

**See also:** Image ID, getIcon, createImage

---

## setIndex

Sets the number of the item which the List Box, the Drop-down List Box, or the Tab Page of the Dialog designated by `<Path>` shows.

- **Type:** Method
- **Syntax:** `<Path>.setIndex(DialogItem:string, ItemNumber:integer) → boolean`
- **Parameters:**
  - `DialogItem` (string) — the List Box, the Drop-down List Box, or the Tab Page (can also designate a Tab Control).
  - `ItemNumber` (integer) — the item that will be shown. If you do not enter an item, the Dialog selects the first entry in the list. For a Tab Control, it designates a tab to activate (leftmost tab = 1).
- **Return Value:** boolean

```simtalk
MyDialog.setIndex("units",6)
MyDialog.setIndex("myTabControl",3)
MyDialog.setIndex("listView",3)
```

**See also:** New List Box, New DropDownList Box, New Tab Page, getIndex, Position of the item in the Items [Dialog] list

---

## setInheritanceBox

Selects (`true`) the Inheritance Box of the specified check box in the Dialog designated by `<Path>`, or clears it (`false`).

- **Type:** Method
- **Syntax:** `<Path>.setInheritanceBox(DialogItemName:string, Value:boolean)`
- **Parameters:**
  - `DialogItemName` (string) — the check box for which you want to activate the Inheritance Box feature.
  - `Value` (boolean) — selects (`true`) or clears (`false`) the check box. `true` shows the check box as an inheritance check box; `false` shows it as a normal check box.

```simtalk
MySimpleDialog.setInheritanceBox("InheritanceBoxSunRoof", true)
```

**See also:** New Check Box, getInheritanceBox

---

## setList

Sets the items of a list which the designated dialog items of the Dialog designated by `<Path>` shows.

- **Type:** Method
- **Syntax:** `<Path>.setList(DialogItem:string, List:any) → boolean`
- **Parameters:**
  - `DialogItem` (string) — a List Box, a Drop-down List Box, or a Tab Control.
  - `List` (any) — the one-columned list into which you enter the Items shown by the dialog items or the tabs of the Tab Control.
- **Return Value:** boolean — `true` if the item in the list was addressed and if it changed its display.

```simtalk
MyDialog.setList("sedan",ListSedan)
var units: list[string]
units.create
units.insert(1,"pound")
units.insert(2,"stone")
MyDialog.setList("unit",units)
```

**See also:** New List Box, New DropDownList Box, New Tab Control, Items [Dialog]

---

## setPasswordMasking

Sets whether the check box **Password** of a dialog item of type Edit Text Box in the Dialog designated by `<Path>` will be selected or cleared.

- **Type:** Method
- **Syntax:** `<Path>.setPasswordMasking(DialogItem:string, Selected:boolean) → boolean`
- **Parameters:**
  - `DialogItem` (string) — the check box Password.
  - `Selected` (boolean) — sets if the check box Password will be selected (`true`) or cleared (`false`). When selected, the Dialog shows entered text with superscripted lower-case x's; when cleared, it shows the password as clear text.
- **Return Value:** boolean

```simtalk
MyDialog.setPasswordMasking("Password",true)
```

**See also:** New Edit Text Box, getPasswordMasking

---

## setSensitive

Sets whether the Dialog designated by `<Path>` shows and activates a dialog item, or shows it and dims it.

- **Remarks:** `setSensitive` applies to all dialog items, except the Tab Control, the Tab Page and the Image.
- **Type:** Method
- **Syntax:** `<Path>.setSensitive(DialogItem:string, Activated:boolean) → boolean`
- **Parameters:**
  - `DialogItem` (string) — the dialog item.
  - `Activated` (boolean) — sets if the dialog item will be shown and activated (`true`) or shown and unavailable (`false`).
- **Return Value:** boolean — `true` if the state of the dialog item is activated and has changed; `false` if deactivated and not changed.

```simtalk
if MyDialog.setSensitive("MyButton",false)
   print "The button 'MyButton' was deactivated."
else
   print "The button 'MyButton' has already been deactivated."
end
```

---

## setTab

Moves a dialog item onto a Tab in the Dialog designated by `<Path>`.

- **Remarks:** Do not use `setTab` for dynamically creating tabs in your dialog. You cannot move a dialog item within a group with this method.
- **Type:** Method
- **Syntax:** `<Path>.setTab(DialogItem:string, NewTabPage:string) → boolean`
- **Parameters:**
  - `DialogItem` (string) — the dialog item.
  - `NewTabPage` (string) — the Tab to which the dialog item is moved.
- **Return Value:** boolean

```simtalk
MyDialog.setTab("button","Properties.Settings")
```

---

## setTable

Sets the table that defines the Items which a dialog item of type List View shows in the Dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.setTable(DialogItem:string, AttributeTable:string/object) → boolean`
- **Parameters:**
  - `DialogItem` (string) — the dialog item of type List View.
  - `AttributeTable` (string/object) — the attribute table, either as an object or a user-defined variable of data type `string`.
- **Return Value:** boolean

```simtalk
MyDialog.setTable("list_view",".Models.Model.Station.ListViewTable")
MyDialog.setTable("list_view",.Models.Model.ListViewTable)
```

**See also:** New List View, Items [Dialog], getTable

---

## setTableRow

Sets the number of the row of the Items table which will be selected in a List View of the dialog designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.setTableRow(Table:string, Row:integer) → boolean`
- **Parameters:**
  - `Table` (string) — the items table.
  - `Row` (integer) — the row which will be selected.
- **Return Value:** boolean

```simtalk
MyDialog.setTableRow("MyListViewTable",4)
```

**See also:** New List View, Items [Dialog], getTableRow

---

## updateUserDialog

Updates the contents of the Dialog designated by `<Path>`.

- **Remarks:** The Dialog then shows features that you changed in tables defining the items, or shows new or changed pictures and icons of the items.
- **Type:** Method
- **Syntax:** `<Path>.updateUserDialog`

```simtalk
MyDialog.updateUserDialog
```

---

## Read-Only Attributes of the Dialog

The Dialog provides the **Read-Only Attributes of All Objects**.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example on the tab Statistics).

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
