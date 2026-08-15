# Checkbox (General)

## ShowStandardButtons [SimTalk]

Sets whether the Dialog designated by `<Path>` shows the standard buttons **OK**, **Cancel** and **Apply** (`true`) or not (`false`).

**Type:** Attribute

**Syntax:**
```simtalk
<Path>.ShowStandardButtons:boolean
```

**Assignment Value:** You can assign a value of data type `boolean`.

**Example:**
```simtalk
Dialog.ShowStandardButtons := false
```

**See also:** Show Default Buttons [check box]

---

## Checkbox [object]

Use the **Checkbox** object for toggling between the states **on** and **off**, for toggling operating modes, etc.

### Description

The Checkbox switches between the states on and off, switches operating modes, switches between runtime mode and debug mode, etc.

By default, the Checkbox looks like this:

*(image)*

### Note

- Plant Simulation only accepts the click on the Checkbox if it occupies at least **10 pixels** in each direction in the model window. If you zoom out very far, the picture of the Checkbox might become too small, preventing Plant Simulation from recognizing it reliably.
- To change between the on and the off state of the Checkbox, click the picture.
- To open the dialog of the object Checkbox, double-click the name **Checkbox** to the right of the icon.
- You can create any number of icons for the Checkbox. Plant Simulation automatically switches between the icons of the check box according to their name/state. Assign the icons pairs of names according to their state, for example `TrueIcon1` and `FalseIcon1`.
- You can also click the Checkbox in a sub-Frame and switch the value. Compare the check box **Show Warehouse Content** in the Factory51 model.
- To show a tooltip with information about the Checkbox, hover with the mouse over it.
- To change the length of the graphic and the anchor points of the Checkbox, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

### Add the Object to the Simulation Model

To add the object Checkbox to your simulation model, click **Manage Class Library > Basic Objects > UserInterface > Checkbox** on the Home ribbon tab.

**See also:**
- Switch States with the Checkbox
- Select an Option from a Drop-down List
- Configure the Check Box and the Drop-down List

---

## Dialog Box of the Checkbox

Double-click the name **Checkbox** to the right of the icon in the Frame to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under **Dialog Items of the Objects**.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

---

## Tab Data [Checkbox]

The tab **Data** provides the settings listed in the table of contents.

### Value [drop-down list] - Checkbox

Select if the Checkbox is active (`true`) or not (`false`).

**Remarks:**

The Checkbox looks like this by default:

*(image)*

Plant Simulation automatically switches between the icons of the check box according to their name/state. Always create a set of two icons, one for **on** and one for **off**, and name them accordingly. Assign names in pairs to the icons according to their state, for example `TrueIcon1` and `FalseIcon1`.

### Value [SimTalk] - Checkbox

*(SimTalk reference)*

### Control [Checkbox]

Modifies the built-in behavior of the object. The object calls the **Control** when the **Value** of the Checkbox changes when you click it. Plant Simulation only calls the Control of the object itself, not of instances of the object.

#### Select the Path to an Existing Method

- Click the ellipsis button. Navigate to the location of the Method in the dialog **Select Object [for controls]** and click **OK**. This inserts the name of the Method into the text box of the Control.
- Press `F2` in the text box to open the Method. Then type in the source code of the Control.
- Instead of choosing **Select Object**, you can also select the Method in a Frame, drag it to the text box and drop it there.

#### Create a Control That Is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type `Method`:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

#### To edit the source code later on

- Press `F2`.
- Or hold down `Shift` and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

The standard **OnClicked** control as a user-defined attribute looks like this:

```simtalk
(self)
```

**See also:**
- Select Object [for controls]
- Value [drop-down list] - Checkbox
- Configure the Check Box and the Drop-down List

---

## Tab User-defined

Define your own attributes as described under the **Tab User-defined**.

---

## Navigate Menu

The commands are described under the **Navigate Menu**.

---

## View Menu

The commands are described under the **View Menu**.

### updateDialog [SimTalk]

*(SimTalk reference)*

---

## Tools Menu

The **Tools Menu** provides commands to access its functions:

- Edit Controls
- Edit Observers

**See also:** Tools Menu [general description]

---

## Help Menu

The commands are described under the **Help Menu**.

---

## Methods of the Checkbox

The Checkbox provides the **Methods of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object **Station**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class [general description]**.
- Press the `F8` key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected **Instance [general description]**.

An example of the Syntax line of the individual methods might look like this:

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```
