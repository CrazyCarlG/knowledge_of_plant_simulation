# AngularConverter — General

## Description

The AngularConverter can accommodate a single part (MU) at any one time.

The AngularConverter moves the MU on to its successor within the flow of materials like this:

- The MU moves onto the first leg of the AngularConverter. Once the **Booking Point Length** has reached the entrance of the AngularConverter, the MU moves along the **Entry Length** with the **Entry Speed** until the Booking Point Length reaches the point at which the conveying direction changes. There the MU triggers the **Moving Time** and changes the conveying direction. At this point in time the MU has to be entirely located on the first leg of the AngularConverter. To allow the first leg to completely accommodate the entering MU, the difference between the **MU Length** and the **Booking Point Length** may not be greater than the **Entry Length**.
- The **MU Width** is then used for all calculations, such as the time until it can exit the object, from here to the exit point.
- The notch on the Part designates its right side.

### Conveying direction

| Conveying direction | Looks like |
|---|---|
| Forward | The MU moves with its front in the direction of motion of the material flow. After changing the conveying direction, the MU retains this direction, meaning that its front does not point in the direction of the material flow. |
| Lateral right | The MU moves with its right-hand side in the direction of motion. After changing the conveying direction, the MU retains this direction, meaning that its front does not point in the direction of the material flow. |
| Backward | The MU is turned 180° and moves backward against the direction of motion. After changing the conveying direction, the MU retains this direction, meaning that its front does not point in the direction of the material flow. |
| Lateral left | The MU moves with its left-hand side in the direction of motion. After changing the conveying direction, the MU retains this direction, meaning that its front does not point in the direction of the material flow. |

> **Note:** Container and Part show the Conveying Direction in their dialog box.

After the Moving Time has been used up and the MU has changed its conveying direction, it continues on the second leg of the AngularConverter. The MU drives along the **Exit Length** with the **Exit Speed** until the **Booking Point Width** has reached the exit of the AngularConverter. Once the MU has completely exited the AngularConverter, the Moving Time is triggered anew to return the AngularConverter to its original position. After the Moving Time has passed, the next MU can enter.

To allow the second leg to completely accommodate the leaving MU, the difference between the **MU Width** and the **Booking Point Width** may not exceed the **Exit Length** when the MU turns left. If the MU turns right, the value for the **Booking Point Width** may not exceed the **Exit Length**.

You can select different configurations for the AngularConverter on the tab **Appearance**.

To show a tooltip with information about the AngularConverter, hover with the mouse over it.

To change the length of the graphic and the anchor points of the AngularConverter, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

To add the object AngularConverter to your simulation model, click **Manage Class Library > Basic Objects > MaterialFlow > AngularConverter** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog **Examples Collection**, and click **Open Model**.

## See also

- Change the Conveying Direction with the AngularConverter
- Video on YouTube: https://youtu.be/hOvdrDnvXXo?si=HtapSi48BgDSePJA&t=377

---

## Dialog Box of the AngularConverter

Double-click the icon of the AngularConverter to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under **Dialog Items of the Objects**.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

---

## Tab Attributes

The tab **Attributes** provides the settings, which the object offers.

The shared properties are described under the **Tab Attributes**.

### Entry Length [text box]

Type the length of the first leg of the AngularConverter into the text box.

**Remarks:** The Entry Length covers the distance from the entry point to the point at which the AngularConverter switches the conveying direction.

**SimTalk:**

```simtalk
EntryLength
```

### Exit Length [text box]

Type the length of the second leg of the AngularConverter into the text box.

**Remarks:** The Exit Length covers the distance from the point at which the AngularConverter switches the conveying direction to the point at which the MU exits the object.

**SimTalk:**

```simtalk
ExitLength
```

### Width [text box] - AngularConverter

Type the Width of the AngularConverter into the text box.

**SimTalk:**

```simtalk
Width
```

### Entry Speed [text box]

Type the Speed into the text box with which the MUs moves on the AngularConverter from the entry point to the point at which the AngularConverter switches the conveying direction.

**SimTalk:**

```simtalk
EntrySpeed
```

### Exit Speed [text box]

Type in the Speed into the text box with which the MUs moves on the AngularConverter from the point at which the AngularConverter switches the conveying direction to the point at which it exits the object.

**SimTalk:**

```simtalk
ExitSpeed
```

### Automatic Stop [check box] - AngularConverter

To automatically stop the AngularConverter, i.e., to set its current speed to 0 if it does not transport a part, select this check box.

**Remarks:** Automatically stopping the AngularConverter might, for example, be the case if it is empty or if it is blocked because a MU cannot leave it. When the speed of the AngularConverter is 0, the Energy State changes to Operational.

**SimTalk:**

```simtalk
AutomaticStop
```

---

## Tab Times [AngularConverter]

Define Times as described under the **Tab Times**.

Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (**Const**).

The AngularConverter provides the **Moving Time** in addition.

You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr`.

**See also:** Recovery Time, Recovery Time Starts, Cycle Time.

### Moving Time [drop-down list] - AngularConverter

The Moving Time is the time it takes the AngularConverter to switch from lengthwise to crosswise conveyance and vice versa.

**Remarks:** The Moving Time is used up, when the MU arrives at the corner at which the AngularConverter switches conveyance and again, when it has completely left the AngularConverter to return the AngularConverter to its original position. Only then can another MU move onto the AngularConverter, as it can only accommodate a single MU at any one time.

Select a distribution for the Moving Time from the drop-down list, and type the values, which that distribution requires, into the text box.

Plant Simulation shows these values along the upper border of the tab. You can also select a constant time (**Const**).

If you use the **Formula** distribution, you can type in a numeric expression or the name of a Method. You can use the anonymous identifier `@` to access the MU for which the moving time applies.

**SimTalk:**

```simtalk
MovingTime
MovingTime.Type
```

---

## Tab Failures

Define failures as described under the **Tab Failures**.

---

## Tab Controls

Provides controls to modify the built-in behavior of the object.

### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog **Select Object [for controls]** and click OK. This inserts the name of the Method into the text box of the Control.

Press **F2** in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing **Select Object**, you can also select the Method in a Frame, drag it to the text box and drop it there.

### Create a Control That is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control** [context menu]. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press **F2**.
- Or hold down **Shift** and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

**See also:** Select Object [for controls], Entrance Control, Exit Control, Pull Control, Shift Calendar.

---

## Tab Exit

Select to which of its successors the object moves the MU on the Tab Exit.

**See also:** Blocking [exit strategy], Strategy [material flow objects].

---

## Tab Statistics

Statistics is described under the **Tab Statistics**.

To view Resource Statistics of Stationary Resources in the Statistics Report, select **View > Show Statistics Report** in the dialog of the object. You can also click the right mouse button in the Frame and select **Show Statistics Report** or you can press **F6**.

**See also:** Resource Statistics [check box], Resource Type.

---

## Tab Energy

Select energy settings for the object on the **Tab Energy**.

---

## Tab Costs

Select costs settings for the object on the **Tab Costs**.

While the AngularConverter transports parts costs accrue which result from the sum of the total investment costs and the total operating costs.

> **Note:** The total investment costs only accrue during the Depreciation Period. If the AngularConverter is empty, the costs remain with the AngularConverter as general costs.

**See also:** Simulate the Accrued Costs of the Machines, CostAnalyzer > How the CostAnalyzer Assigns Costs to Part Types, CostAnalyzer > Costs Shown in the Costs Report.

---

## Tab User-defined

Define your own attributes as described under the **Tab User-defined**.

---

## Navigate Menu

The commands are described under the **Navigate Menu**.

---

## View Menu

The View Menu provides commands to access its functions.

| Command | Related |
|---|---|
| Refresh [on View menu] | Backward Blocking List |
| Show Statistics Report [on View menu] | Exit Blocking List |
| Show Attributes and Methods [on View menu] | Associated Lockout Zones |
| Contents [material flow objects] | Associated Shift Calendar |

---

## Tools Menu

The commands are described under the **Tools Menu**.

---

## Tabs Menu

Use the commands of the Tabs menu to show or hide individual tabs of the selected material flow objects. If you hide tabs that you do not need, Plant Simulation opens the dialog faster, and you can change to those tabs faster that you need in your daily work.

**Remarks:**

- To apply the changed settings, click OK, close the dialog, and reopen it.
- The menu shows a check mark to the left of the displayed tabs.
- The command **Inherit** turns inheritance of the displayed or hidden tabs in the dialog off or on.

---

## Help Menu

The commands are described under the **Help Menu**.

---

## Methods of the AngularConverter

The AngularConverter provides:

- The Methods of Curved Objects.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.
