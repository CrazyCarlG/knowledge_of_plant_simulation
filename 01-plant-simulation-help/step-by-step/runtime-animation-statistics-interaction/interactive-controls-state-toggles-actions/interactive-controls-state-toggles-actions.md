# Interactive Controls, State Toggles, Actions

## Show Longer or Shorter Time Intervals

The displayed resource states refer to the resource which is currently occupied by the displayed part.

- **Show longer time intervals:** Hold down `Ctrl` and press the `-` key, or roll the mouse wheel backward. This zooms the view in.
- **Show shorter time intervals:** Hold down `Ctrl` and press the `+` key, or roll the mouse wheel forward. This zooms the view out.
- **Change intervals in greater steps:** Hold down `Shift` in addition to `Ctrl`.
- **Return to default zoom factor:** Hold down `Ctrl` and press the `0` key.

## Toggling States and Executing Actions

At times, you may want to toggle between the states on and off, or between different operating modes, etc. in your simulation model. Or you may want to execute an action by clicking a button in the model — for example, open a certain table or method with one click instead of navigating to the object in the Frame and double-clicking it.

You can:

- Switch States with the Checkbox
- Execute the Action
- Select an Option from a Drop-down List

## Toggling States with the Checkbox

You can insert the **Checkbox** into your simulation model from the folder **UserInterface** in the Class Library or from the toolbar **User Interface** in the Toolbox.

To open the dialog of the object Checkbox, double-click the name Checkbox to the right of the icon in the Frame.

The Checkbox looks like this by default (appearance shown in both the Frame and in 3D).

You can use the check box to:

- Toggle the State by Clicking the Checkbox
- Switch Modes Using a Control

### Toggle the State by Clicking the Checkbox

To switch between the on and the off state of the Checkbox, click its icon in the Frame. To show an expression of your choice next to the check box, enter it into the text box **Label** (the example uses "Motor on/off").

When you click the check box in the Frame, it changes its icon from green (meaning on) to red (meaning off).

### Switch Modes Using a Control

If you want the check box to switch modes when a certain action takes place in your simulation model, you have to program this in a **Control**.

Double-click the name of the check box and select the control in which you programmed when the Checkbox switches modes.

In the example, the Checkbox named `MyCheckbox` changes the Value of the Variable named `MyState` from true to false and vice versa in the model.

The source code looks like this:

```simtalk
MyState := MyCheckbox.Value
```

Clicking the Checkbox then switches the state.

## Executing Actions by Clicking a Button

You can insert the **Button** into your simulation model from the folder **UserInterface** in the Class Library or from the toolbar **User Interface** in the Toolbox.

### Define the Appearance of the Button

Plant Simulation shows the button in the Frame in a number of ways:

- **Built-in graphic and label:** For example, with the built-in graphic and the label you type in. You might have to adjust the Width and the Height so that the label fits the button without being cut off. You can do this by holding down `Ctrl+Shift` and dragging a corner of the icon, by entering exact values into the text boxes, or by combining both methods.
- **User-defined icon:** Drawn in the icon editor. Then, you can show the text you enter as the label in this user-defined icon of the button. To be able to tell that you clicked the button, draw two pictures — one for the unclicked state and one for the clicked state. In the example, the name of the unclicked icon is `icon3`, so the name of the clicked icon consequently has to be `icon3_down`. The button does not stay pressed, but returns to its unclicked, raised state when you release the mouse button.
- **Pasted picture:** With a picture you paste into a new icon in the icon editor.

To open the dialog of the button, click it with the right mouse button and select **Open** on the context menu. You can also select the button by dragging a marquee around it.

By default, Plant Simulation does not show a tooltip for the button in the Frame when you roll the mouse over it. To display your own tooltip, create a user-defined attribute and name it `Tooltip`.

After you have defined the appearance of the Button, you have to program the action which the Control executes when the Button is clicked. To execute this action, click the button in the Frame.

### Program the Control for the Action to be Executed

After you defined the appearance of the Button, you have to program the control that clicking the Button executes.

The example uses the Start/Stop Simulation button in the Factory51 sample model. The control was created by clicking the ellipsis button in the text box **Control** and selecting **Create Control** on the context menu.

This source code checks if the EventController is running at the moment. If so, it stops the simulation, and then starts it.

```simtalk
if root.EventController.IsRunning
   root.EventController.stop
else
   root.EventController.start
end
```

## Selecting an Option from a Drop-down List

You can insert the **Drop-Down List** into your simulation model from the folder **UserInterface** in the Class Library or from the toolbar **User Interface** in the Toolbox.

In the sample model, the objects Button, Check Box, and Drop-down List are combined with user-defined controls:

- The **check box** activates or deactivates moving the parts on to a dedicated tray in the plant.
- The **drop-down list** sets the dedicated destination tray of the parts if you turn the check box on.
- A **button** opens the table according to which the Source produces the parts.
- A **button** opens the sensor control of the feeder line that sends the parts on to their destination trays according to the settings of the check box and of the drop-down list.

To create the sample model:

- Configure the Source that Produces the Parts
- Configure the Feeder Line with Sensor and Sensor Control
- Configure the Turnplate to Rotate the Part According to an Attribute
- Configure the Check Box and the Drop-down List
- Configure the Buttons to Open Parts Table and Callback Method

### Configure the Source that Produces the Parts

The Source with the label **Parts In** produces the parts in a cyclical sequence according to the settings entered into the **PartsTable**.

Enter the attribute which sets the tray to which the part is going to be moved into the subtable that double-clicking into the respective cell in the column **Attributes** of the production table opens. The example uses the attribute `Destination` and the respective `Tray`.

If the check box is off, the Source produces the part **Board** in a cyclical sequence and moves the boards across the materials handling equipment to the destination trays. For moving the part, the Callback Method (entered as the Sensor Control into the feeder line) uses the attribute `Destination` of the part.

### Configure the Feeder Line with Sensor and Sensor Control

The feeder line is part of the materials handling equipment that transports the parts to their destination trays. The example line is 11 meters long, with a sensor created at 10 meters and the method `PartDestination` (with the label `Callback`) entered as the Sensor Control.

If the check box is on, the drop-down list is accessed within the callback method `PartDestination` with the attribute `Items`. It then moves the board on to the tray according to the value selected in the drop-down list.

The source code looks like this:

```simtalk
// Apply the destination selected in the drop-down list
// named/labeled 'SelectDestination/Dedicated Destination'.
if DestinationActive.Value // destination is active
// set new destination of the part
   @.Destination := SelectDestination.Items[SelectDestination.Value]
end
```

### Configure the Turnplate to Rotate the Part According to an Attribute

Following the feeder line in the plant, a **Turnplate** is added to rotate the produced boards.

To do so, select **Strategy > MU Attribute** and **Attribute Type > Object**, and enter the required values into the Attribute List. The example enters the Attribute named `Destination`, the names of the destination trays `Tray1` to `Tray4`, and the Angle by which the board will be rotated (`90` stands for 90 degrees clockwise, `-90` stands for 90 degrees counterclockwise).

### Configure the Check Box and the Drop-down List

In the example, the check box and the drop-down list work together:

- The **check box** activates or deactivates moving the boards on to a dedicated tray.
- The **drop-down list** sets the dedicated destination of the boards once you click the check box to set it to on.

To configure the drop-down list:

- Enter the **Width** and the **Height** with which the drop-down list will be shown in the Frame (example: Width of 6 meters, Height of 1 meter).
- Click the button **Items** and enter the items which the drop-down list shows in the Frame.
- Enter the number of the item in the list which the drop-down list will show in the Frame by default into the text box **Value** (example: `1` to make the drop-down list show `Tray1` when it is closed).
- You can set the caption of the drop-down list, show it in the Frame, and set its position. On the **View** ribbon tab, you can select whether to show the name, the label, or both in the Frame.

To open the dialog of the drop-down list, click it with the right mouse button and select **Open** on the context menu.

> **Note:** Plant Simulation only accepts the click on the Checkbox if it occupies at least 10 pixels in each direction in the model window. If you zoom out very far, the Checkbox might become too small, preventing Plant Simulation from recognizing it reliably.

If the check box is on, the drop-down list is accessed within the Callback Method of the sensor with the attribute `Items`. It then moves the board on to the tray according to the value that you selected.

The source code looks like this:

```simtalk
// Apply the destination selected in the drop-down list
// named/labeled 'SelectDestination/Dedicated Destination'
var l: list
l.create
SelectDestination.getItems(l)
if DestinationActive.Value then  // destination is active
// set new destination of the part
   @.Destination := l[SelectDestination.Value]
end
```

### Configure the Buttons to Open Parts Table and Callback Method

To open the parts table and the callback method with one click instead of navigating to them in the Frame and double-clicking their icon, two buttons are configured:

**Button 1** — opens the table according to which the Source named `PartsIn` produces the parts:

- Enter the **Width** and the **Height** with which the button will be shown in the Frame (example: Width of 6 meters, Height of 1 meter).
- Enter the control which will be called when you click the button. A control that is part of the object was used: right-click into the text box **Control** and select **Create Control**.

The following source code opens the parts table named `PartsTable` in the Frame:

```simtalk
self.~.~.PartsTable.openDialog
```

**Button 2** — opens the sensor control of the feeder line that sends the parts on to their destinations according to the settings of the check box and of the drop-down list:

- Enter the **Width** and the **Height** with which the button will be shown in the Frame (example: Width of 6 meters, Height of 1 meter).
- Enter the control which will be called when you click the button. A control that is part of the object was used: right-click into the text box **Control** and select **Create Control**.
