# DropDownList [object]

Use the object **DropDownList** for showing a drop-down list in the Frame. When you select one of the items, it executes the action which you programmed in the control.

## Description

The DropDownList provides the user with several options, one of which he can select. You can define the items, which the DropDownList shows, either in its dialog or with the attribute `Items`.

Whenever the user of your DropDownList selects another item, the drop-down list executes the action which you programmed in the `Control`.

The DropDownList looks like this by default (with or without a caption).

> **Note:** Plant Simulation only accepts the click on the DropDownList if it occupies at least 10 pixels in each direction in the model window. If you zoom out very far, the picture of the DropDownList might become too small, preventing Plant Simulation from recognizing it reliably.

- To open its dialog box, click the drop-down list with the right mouse button and select **Open** on the context menu.
- To select the drop-down list in the Frame window, you can also drag a marquee over its icon.
- You can also click a DropDownList and select an item in it in a sub-Frame and trigger the respective action.
- To show a tooltip with information about the DropDownList, hover with the mouse over it.
- To change the length of the graphic and the anchor points of the DropDownList, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Add the Object to the Simulation Model

To add the object DropDownList to your simulation model, click **Manage Class Library > Basic Objects > UserInterface > DropDownList** on the Home ribbon tab.

## Dialog Box of the DropDownList

Click the DropDownList, which you inserted into a Frame, with the right mouse button and select **Open** on the context menu to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Tab Attributes

The tab **Attributes** provides the settings which the object offers. The shared properties are described under the *Tab Attributes*.

### Width [text box] - DropDownList

Type in the width in meters with which the DropDownList is shown in the Frame.

**Remarks**

If you type in long names for the Items, you have to adjust the width so that the names of the items in the drop-down list are not cut off.

To change the width, you can also hold down **Ctrl+Shift** and drag the left or right side of the icon. Plant Simulation shows the width in meters.

**SimTalk:** `ObjectWidth [SimTalk] - DropDownList`

### Height [text box] - DropDownList

Type in the height in meters with which the DropDownList is shown in the Frame.

**Remarks**

If you type in a height of more than 30 pixels, Plant Simulation uses a larger font to display the label of the drop-down list.

To change the height, you can also hold down **Ctrl+Shift** and drag the top or the bottom of the icon.

**SimTalk:** `ObjectHeight [SimTalk] - DropDownList`

### Value [text box] - DropDownList

Type in which item in the DropDownList will be selected when you open it. The value is identified by its index number.

**Remarks**

This is one of the items which you typed into the list of Items.

> **Note:** If you localize the items to another language, you will usually use the `Value` instead of the attribute `Item`. The value is a number which is language-independent, while the `Item` is a string which differs from language to language.

**SimTalk:** `Value [SimTalk] - DropDownList`

### Items [button] - DropDownList

To open the list, into which you type the Items which the DropDownList displays when you click it, click this button.

**Remarks**

- If you want to use the index number to access an item in the list, use the attribute `Value`.
- If you want to use the name to access an item in the list, use the attribute `Item`.

**SimTalk:** `Items [SimTalk] - DropDownList`, `Item [SimTalk] - DropDownList`

### Control [DropDownList]

Modifies the built-in behavior of the object. The object calls the Control when you select an item from the DropDownList in the Frame.

**Remarks**

The anonymous identifiers `?` and `@` in the Control are set to the DropDownList when the method is called.

**Select the Path to an Existing Method**

- Click the ellipsis button. Navigate to the location of the Method in the dialog *Select Object [for controls]* and click **OK**. This inserts the name of the Method into the text box of the Control.
- Press **F2** in the text box to open the Method. Then type in the source code of the Control.
- Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

**Create a Control That is a Method of the Object**

- Type a meaningful name into the text box and select **Create Control** [context menu]. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press **F2**.
- Or hold down **Shift** and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

A control might, for example, look like this:

```simtalk
switch ?.Value
  case 1
    print "Item 1 selected"
  case 2 
    print "Item 2 selected"
end
```

**SimTalk:** `Control [SimTalk] - DropDownList`

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

## Navigate Menu

The commands are described under the *Navigate Menu*.

## View Menu

The commands are described under the *View Menu*.

**SimTalk:** `updateDialog [SimTalk]`

## Tools Menu

The Tools Menu provides commands to access its functions: **Edit Controls**, **Edit Observers**.

## Help Menu

The commands are described under the *Help Menu*.

## Methods of the DropDownList

The DropDownList provides the *Methods of All Objects*.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

An example of the Syntax line of the individual methods might look like this:

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## See also

- Select an Option from a Drop-down List
- Configure the Check Box and the Drop-down List
- Configure the Feeder Line with Sensor and Sensor Control
- Select Object [for controls]
- Tools Menu [general description]
