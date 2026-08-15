# Generator — General

The **Generator** object lets you specify times either as a fixed interval or as a probability distribution. You can also limit the probability distributions to a segment of the entire range.

To show a tooltip with information about the Generator, hover with the mouse over it.

To change the length of the graphic and the anchor points of the Generator, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Add the Object to the Simulation Model

To add the object Generator to your simulation model, click:

> Manage Class Library > Basic Objects > InformationFlow > Generator

on the Home ribbon tab.

## Dialog Box of the Generator

Double-click the icon of the Generator to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under **Dialog Items of the Objects**.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

---

## Tab Times

Define Times as described under the **Tab Times**.

Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (**Const**).

You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr [SimTalk]`.

**See also:** Interval Control, Duration Control, Probability Distributions, Empirical Distributions, User-defined Distributions.

---

### Active [check box]

To activate the Generator, select this check box. To deactivate it, clear it.

**SimTalk:** `Active [SimTalk] - Generator`

---

### Start [text box]

Type the time at which the Generator activates the Interval Control for the first time into the text box.

**Remarks**

- If you type in `0` as the Start Time and a value greater than `0` for the Interval, Plant Simulation triggers the control immediately after you started the simulation.
- You can also select any of the probability distributions. Then, you have to type in the parameters, which the selected distribution requires.
- You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr`.

```java
Generator.Start.setTypeAndAttr("Normal", 30, 10)
```

**SimTalk:** `Start [SimTalk] - Generator`, `IntervalCtrl [SimTalk]`, `putAttributeNamesIntoTable [SimTalk] - objects`

**See also:** Interval Control, Start [text box] - Generator.

---

### Stop [text box]

Type the time at which the Generator activates the Interval Control for the last time into the text box.

**Remarks**

- As Interval and Duration always appear in pairs, the Duration Control may be activated even after the time you type in here. If you do not want any time limit to apply for activating the Interval Control, type in `0`.
- You can also select any of the probability distributions. Then, you have to type in the parameters, which the selected distribution requires.
- You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr`.

```java
Generator.Stop.setTypeAndAttr("Normal", 1:00, 10)
```

**SimTalk:** `Stop [SimTalk] - Generator`, `IntervalCtrl [SimTalk]`, `putAttributeNamesIntoTable [SimTalk] - objects`

**See also:** Interval Control, Stop [text box] - Generator.

---

### Interval [text box]

Type in the Interval, i.e., the time between two activations of the Interval Control.

**Remarks**

- Type in `0` to not trigger any controls and stop the Generator.
- You can also select any of the probability distributions. Then, you have to type in the parameters, which the selected distribution requires.
- You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr`.

```java
Generator.Interval.setTypeAndAttr("dEmp", Table)
```

**SimTalk:** `Interval [SimTalk] - Generator`, `IntervalCtrl [SimTalk]`, `putAttributeNamesIntoTable [SimTalk] - objects`

**See also:** Interval Control, Interval [text box] - Generator.

---

### Duration [text box]

Type in the Duration, i.e., the time span between activating the Interval Control and the Duration Control.

**Remarks**

- You can also select any of the probability distributions. Then, you have to type in the parameters, which the selected distribution requires.
- You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr`.

```java
Generator.Duration.setTypeAndAttr("cEmp", Table)
```

**SimTalk:** `Duration [SimTalk] - Generator`, `IntervalCtrl [SimTalk]`, `DurationCtrl [SimTalk]`, `putAttributeNamesIntoTable [SimTalk] - objects`

**See also:** Interval Control, Duration Control.

---

## Tab Controls

Provides controls to modify the built-in behavior of the object.

### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog **Select Object [for controls]** and click OK. This inserts the name of the Method into the text box of the Control.

Press **F2** in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

### Create a Control That is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press **F2**.
- Or hold down **Shift** and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.
- To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

**See also:** Interval Control, Duration Control.

---

### Interval Control

Modifies the built-in behavior of the object. The object calls the Interval Control according to the intervals, which you specified as the Interval.

**Select the Path to an Existing Method**

Click the ellipsis button. Navigate to the location of the Method in the dialog **Select Object [for controls]** and click OK. This inserts the name of the Method into the text box of the Control.

Press **F2** in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

**Create a Control That is a Method of the Object**

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press **F2**.
- Or hold down **Shift** and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.
- To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

**SimTalk:** `IntervalCtrl [SimTalk]`

**See also:** Select Object [for controls], Interval [text box] - Generator.

---

### Duration Control

Modifies the built-in behavior of the object. The object calls the Duration Control after the specified time span of the Duration, depending on the Interval, has elapsed.

**Select the Path to an Existing Method**

Click the ellipsis button. Navigate to the location of the Method in the dialog **Select Object [for controls]** and click OK. This inserts the name of the Method into the text box of the Control.

Press **F2** in the text box to open the Method. Then type in the source code of the Control.

Plant Simulation calls the Duration Control after the Interval Control. The Duration Control may be activated for the last time even after the time you entered as the Stop Time.

Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

**Create a Control That is a Method of the Object**

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press **F2**.
- Or hold down **Shift** and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.
- To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

**SimTalk:** `DurationCtrl [SimTalk]`

**See also:** Select Object [for controls], Stop [text box] - Generator, Duration [text box] - Generator, Interval [text box] - Generator.

---

## Tab User-defined

Define your own attributes as described under the **Tab User-defined**.

---

## Navigate Menu

The commands are described under the **Navigate Menu**.

---

## View Menu

The View Menu provides commands to access its functions:

- Refresh [on View menu]
- Show Attributes and Methods [on View menu]

**SimTalk:** `updateDialog [SimTalk]`

**See also:** View Menu [general description].

---

## Tools Menu

The Tools Menu provides these menu commands:

- Edit Controls
- Edit Observers

---

## Help Menu

The commands are described under the **Help Menu**.

---

## Methods of the Generator

The Generator provides the **Methods of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

An example of the Syntax line of the individual methods might look like this:

```java
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```
