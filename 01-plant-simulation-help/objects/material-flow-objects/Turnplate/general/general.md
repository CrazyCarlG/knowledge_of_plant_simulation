# Turnplate

## Description

A typical example is in the package shipping industry where all packages have to be rotated to a uniform direction so that a scanner can automatically read the bar code holding the address information.

Key characteristics:

- The Turnplate has a capacity of one, i.e., only one MU can be located on it at any one time.
- The MU moves onto the Turnplate and the Turnplate starts rotating when the booking point of the MU has reached the center of rotation of the Turnplate.
- When the rotation is finished, the MU exits the Turnplate.
- The conveying direction on the Turnplate is unidirectional, i.e., the MU cannot be conveyed forward and then backward.
- The length of the MU must not be longer than the Length of the Turnplate itself.
- The center of rotation is by default located in the center of the Turnplate.
- The rotation takes up a certain amount of time. You can type in the rotation time per rotation steps of 90 degrees. If you type in a rotation time of 0, the MU is rotated instantaneous without using up any time at all.
- The rotation angle that you type in should be a multiple of 90 degrees. If you type in an angle other than that, Plant Simulation rounds this angle to the next angle that is divisible by 90. You can also type in a value greater than 360 degrees as long as it is divisible by 90. This way the Turnplate can rotate the MU several times to simulate packing machines, such as shrink wrappers, etc. By default, the Turnplate rotates 90 degrees clockwise.
- After the Turnplate has rotated the MU and it has left it, the Turnplate returns to its starting position.
- You can select different configurations for the Turnplate on the tab Appearance of the Length-oriented Objects.

## Tooltip

To show a tooltip with information about the Turnplate, hover with the mouse over it.

To change the length of the graphic and the anchor points of the Turnplate, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Add the Object to the Simulation Model

To add the object Turnplate to your simulation model, click **Manage Class Library > Basic Objects > MaterialFlow > Turnplate** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog Examples Collection, and click **Open Model**.

## See also

- Align and Shrink-Wrap Parts with the Turnplate
- Configure the Turnplate to Rotate the Part According to an Attribute
- Video on YouTube: https://youtu.be/hOvdrDnvXXo?si=Cs5gOF4JB5PBlVma&t=532

## Dialog Box of the Turnplate

Double-click the icon of the Turnplate to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under Dialog Items of the Objects.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Tab Attributes

The tab Attributes provides the settings, which the object offers.

### Length [text box] - Turnplate

Type the Length of the Turnplate into the text box.

**Remarks:** After you inserted it, Plant Simulation shows its length here. The Turnplate only rotates MUs, which it can accommodate in their entirety, meaning that they are shorter or as long as the value you enter here. You can change the length of the graphic and the anchor points of the Turnplate by clicking **Show Manipulators** on the Edit ribbon tab or by pressing **M** on the keyboard.

```simtalk
Length [Turnplate]
```

### Width [text box] - Turnplate

Type the Width of the Turnplate into the text box.

```simtalk
Width [SimTalk] - Turnplate
```

### Speed [text box] - Turnplate

Type the Speed into the text box with which the Turnplate conveys the MU while it is located on the plate.

**Remarks:** You can also type in -1 for an infinite speed.

```simtalk
Speed [SimTalk] - Turnplate
```

### Rotation Time per 90° [text box] - Turnplate

Type the Time into the text box, which it takes the Turnplate to rotate by 90 degrees.

**Remarks:** To rotate the MU immediately, without using up any time at all, type in a rotation time of 0.

```simtalk
RotationTimePer90Degrees [SimTalk] - Turnplate
```

### Strategy [drop-down list] - Turnplate

Select the Strategy according to which the Turnplate rotates the part.

**Remarks:** You can select one of these settings:

- **Angle** rotates the MU according to the rotation Angle, which you type in.
- **MU Attribute** rotates the MU according to a built-in or a user-defined attribute of the MU. Click **Open List** and type in the name of the Attribute of the MU, the Value of the attribute, and the rotation Angle.
- **MU Name** rotates the MU according to its name. Click **Open List** and type in the Name of the MU and the rotation Angle.
- **Method** rotates the MU according to the strategy method. Within this method you have to call the method `rotatePart` with the rotation angle as parameter. Type the name of the method into the text box Strategy Method.

```simtalk
Strategy [SimTalk] - Turnplate
```

**See also:** Configure the Turnplate to Rotate the Part According to an Attribute; Angle [text box] - Turnplate; Open List [Turnplate]; Strategy Method [Turnplate].

### Angle [text box] - Turnplate

Type the Angle in degrees into the text box to which the Turnplate rotates the MU.

**Remarks:**

- The rotation angle should be a multiple of 90. If you type in an angle other than that, Plant Simulation rounds this angle to the next angle that is divisible by 90. You can also type in a value greater than 360 degrees as long as it is divisible by 90. This way the turnplate can rotate the part several times around its own axis to simulate packing machines.
- By default, the turnplate rotates the part 90 degrees clockwise. To rotate the part counter-clockwise, type in negative angles.

```simtalk
Angle [SimTalk] - Turnplate
```

### Attribute Type [drop-down list] - Turnplate

Select the data type of the attribute that determines the rotation angle by which the Turnplate rotates the part.

**Remarks:** This applies to the Strategy > MU Attribute.

```simtalk
AttributeType [SimTalk] - Turnplate
```

**See also:** Strategy [drop-down list] - Turnplate.

### Open List [Turnplate]

To open the rotation angles list for the MUs, click this button.

**Remarks:** The Strategy determines what you type in:

- For the Strategy > MU Attribute you can type in the name of the Attribute of MU part, the Value of the attribute, and the rotation Angle.
- For the Strategy > MU Name you can type in the Name of the attribute of the MU and the rotation Angle.

```simtalk
setAttributeList [SimTalk] - Turnplate
getAttributeList [SimTalk] - Turnplate
```

**See also:** Strategy [drop-down list] - Turnplate; Configure the Turnplate to Rotate the Part According to an Attribute; Data Held in Tabular Form in Attributes [material flow objects].

### Strategy Method [Turnplate]

Modifies the built-in behavior of the object. The object calls the Strategy Method as soon as the booking point of the part is located on the center of rotation of the Turnplate.

**Remarks:** The Strategy Method rotates the MU around the rotation angle which you specify. Within the Strategy Method you have to call the method `rotatePart` with the rotation angle as parameter.

#### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog Select Object [for controls] and click OK. This inserts the name of the Method into the text box of the Control. Press F2 in the text box to open the Method. Then type in the source code of the Control. Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

#### Create a Control That is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens. To edit the source code later on:

- Press F2.
- Or hold down Shift and double-click into the text box.
- Or select Open Object on the context menu.
- Or click the tab User-defined and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

The default strategy method as a user-defined attribute looks like this:

```simtalk
?.rotatePart(90)
```

```simtalk
StrategyCtrl [SimTalk] - Turnplate
rotatePart [SimTalk]
```

**See also:** Select Object [for controls]; Configure the Turnplate; Strategy [drop-down list] - Turnplate.

### Automatic Stop [check box] - Turnplate

To set the Current Speed of the Turnplate to 0 when it does not transport a MU, select this check box.

**Remarks:**

- Automatically stopping the Turnplate might, for example, be the case if it is empty or if it is blocked because a MU cannot leave it.
- If the Speed of the Turnplate is 0, the Energy State changes to Operational.

```simtalk
AutomaticStop [SimTalk] - Turnplate
```

## Tab Times

Define Times as described under the Tab Times.

Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (Const).

You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr`.

```simtalk
setTypeAndAttr [SimTalk]
```

**See also:** Recovery Time [general description]; Recovery Time Starts; Cycle Time [general description].

## Tab Failures

Define failures as described under the Tab Failures.

## Tab Controls

Provides controls to modify the built-in behavior of the object.

### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog Select Object [for controls] and click OK. This inserts the name of the Method into the text box of the Control. Press F2 in the text box to open the Method. Then type in the source code of the Control. Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

### Create a Control That is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens. To edit the source code later on:

- Press F2.
- Or hold down Shift and double-click into the text box.
- Or select Open Object on the context menu.
- Or click the tab User-defined and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

**See also:** Entrance Control [general description]; Exit Control [general description]; Pull Control [general description]; Shift Calendar [tab Controls].

## Tab Statistics [Turnplate]

Statistics is described under the Tab Statistics.

In addition, the Turnplate collects this statistical value:

| Item English | Description | Read-only attribute | Item German |
| --- | --- | --- | --- |
| Rotation Loaded | Shows the portion of the statistics collection period during which the Turnplate was rotating while transporting a MU. | `StatRotationLoadedPortion [SimTalk] - Turnplate` | Drehung belegt |

To view the Rotation Time in the Statistics Report, select **View > Show Statistics Report** in the dialog of the object. You can also click the right mouse button in the Frame and select **Show Statistics Report** or you can press F6.

```simtalk
StatRotationLoadedPortion [SimTalk] - Turnplate
```

**See also:** Resource Statistics [check box]; Resource Type.

## Tab Energy

Select energy settings for the object on the Tab Energy.

## Tab Costs

Select costs settings for the object on the Tab Costs.

While the Turnplate transports MUs costs accrue which result from the sum of the total investment costs and the total operating costs.

**Note:**

- The total investment costs only accrue during the Depreciation Period.
- If the Turnplate is empty, the costs remain with the Turnplate as general costs.

**See also:** Simulate the Accrued Costs of the Machines; CostAnalyzer > How the CostAnalyzer Assigns Costs to Part Types; CostAnalyzer > Costs Shown in the Costs Report.

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

## Navigate Menu

The commands are described under the Navigate Menu.

## View Menu

The View Menu provides commands to access its functions:

- Refresh [on View menu]
- Show Statistics Report [on View menu]
- Show Attributes and Methods [on View menu]
- Contents [material flow objects]
- Forward Blocking List
- Backward Blocking List
- Exit Blocking List
- Associated Lockout Zones
- Associated Shift Calendar

## Tools Menu

The commands are described under the Tools Menu.

## Tabs Menu

Use the commands of the Tabs menu to show or hide individual tabs of the selected material flow objects. If you hide tabs that you do not need, Plant Simulation opens the dialog faster, and you can change to those tabs faster that you need in your daily work.

**Remarks:**

- To apply the changed settings, click OK, close the dialog, and reopen it.
- The menu shows a check mark to the left of the displayed tabs.
- The command Inherit turns inheritance of the displayed or hidden tabs in the dialog off or on.

## Help Menu

The commands are described under the Help Menu.

## Methods of the Turnplate

The Turnplate provides:

- The methods listed in the table of contents to the left.
- The Methods of Curved Objects.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
