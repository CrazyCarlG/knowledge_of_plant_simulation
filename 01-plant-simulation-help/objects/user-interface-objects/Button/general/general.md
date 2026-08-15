# Button [object]

Use the object **Button** for showing a button in the Frame. When you click the button, it executes the action which you programmed in a control.

## Description

The Button executes the action you programmed in the Control when the user clicks it. If you type in a label for the button, Plant Simulation shows that label on the button in the Frame.

By default, Plant Simulation does not show the name of the button as a tooltip in the Frame when you roll the mouse over it. To show your own tooltip, create a user-defined attribute and name it `Tooltip`.

Plant Simulation can show the button in the Frame in a number of ways:

- With the label you type in.
- With an icon you draw in the icon editor. Then, you can show text you type in as the label on that button, for example.
- With a picture you pasted into a new icon in the icon editor. You could name the icons `play` and `play_down` for example.

To open its dialog box, click the button with the right mouse button and select **Open** on the context menu. You can also click a Button in a sub-Frame and trigger the respective action. To select the button in the Frame window, you can also drag a marquee over its icon.

> **Note:** Plant Simulation only accepts the click on the Button if it occupies at least 10 pixels in each direction in the model window. If you zoom out very far, the picture of the Button might become too small, preventing Plant Simulation from recognizing it reliably.

To change the length of the graphic and the anchor points of the Button, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Add the Object to the Simulation Model

To add the object Button to your simulation model, click **Manage Class Library > Basic Objects > UserInterface > Button** on the Home ribbon tab.

## Dialog Box of the Button

Click the Button you inserted into a Frame with the right mouse button and select **Open** on the context menu to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Tab Attributes

The tab **Attributes** provides the settings that the object offers. The shared properties are described under the *Tab Attributes*.

### Width [text box] - Button

Type in the Width in meters with which the object is displayed in the Frame. If you type in long text, you have to adjust the width so that the text fits into the object boundaries without being cut off.

**SimTalk:** `ObjectWidth [SimTalk] - Button`

### Height [text box] - Button

Type in the Height in meters with which the object is displayed in the Frame. To change the height, you can also hold down `Ctrl+Shift` and drag the top or the bottom of the icon.

**SimTalk:** `ObjectHeight [SimTalk] - Button`

### Control [Button]

Modifies the built-in behavior of the object. The object calls the Control when you click the Button.

**Remarks:** The anonymous identifiers `?` and `@` are set to the object when the method is called. Specify a control without parameter to call the control one time when you release the Button.

#### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog *Select Object [for controls]* and click OK. This inserts the name of the Method into the text box of the Control.

Press `F2` in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing *Select Object*, you can also select the Method in a Frame, drag it to the text box and drop it there.

#### Create a Control That Is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens. To edit the source code later on:

- Press `F2`.
- Or hold down `Shift` and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

#### Parameter

You can also specify a control which expects a boolean value as a parameter. This control is called with the value `true` when you click the Button and with the value `false` when you release it.

Plant Simulation executes the Control when you change the size of the Button or when you move it with Drag-and-Drop. If the control does not expect a parameter it will be called, as before, when you release the Button.

**Example** — a control might, for example, look like this:

```simtalk
self.~.~.DataTable.openDialog
self.~.~.&MyMethod.openDialog // opens the dialog of the
// method MyMethod, instead of executing its source code
end
```

**SimTalk:** `Control [SimTalk] - Button`

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

By default Plant Simulation does not show the name of the button as a tooltip in the Frame window. To show your own tooltip, you can create a user-defined attribute and name it `Tooltip`.

## Menus

- **Navigate Menu** — The commands are described under the *Navigate Menu*.
- **View Menu** — The commands are described under the *View Menu*. **SimTalk:** `updateDialog [SimTalk]`
- **Tools Menu** — Provides commands to access its functions: *Edit Controls*, *Edit Observers*.
- **Help Menu** — The commands are described under the *Help Menu*.

## Methods of the Button

The Button provides the *Methods of All Objects*.

To view all of the methods, read-only attributes, and attributes of the object, open the window *Show Attributes and Methods*:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the `F8` key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

An example of the Syntax line of the individual methods might look like this:

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## Value [SimTalk] - Checkbox

Activates (`true`) or deactivates (`false`) the Checkbox designated by `<Path>`. The Checkbox executes a Control when its value changes.

**Syntax:**

```simtalk
<Path>.Value:boolean
```

**Watchable:** The attribute is watchable.

**Assignment Value:** You can assign a value of data type boolean.

**Example:**

```simtalk
MyCheckbox.Value := false
```

**See also:** Value [drop-down list] - Checkbox, Control [Checkbox], Button
