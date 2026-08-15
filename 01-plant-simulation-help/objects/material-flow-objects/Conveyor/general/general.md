# Conveyor — General

## Description

As opposed to the point-oriented material flow objects, Plant Simulation uses the actual **Length**, which you type into the dialog of the Conveyor, during your simulation run.

The Conveyor transports a MU along its entire length with a constant speed. A MU cannot pass another MU moving along in front of it. If you do not enter an Exit Control, the Conveyor distributes the MUs equally among the successors it is connected to.

If the preceding MU cannot exit the Conveyor, the check box **Accumulating** sets if succeeding MUs may move up, so that they are located front to back to each other, or if they will retain their distance to each other.

### How Plant Simulation moves MUs

- **Moving from point-oriented object to length-oriented object**  
  When moving from a point-oriented object, such as a Source or a Station, to a Conveyor, the front of the MU moves to the start of the Conveyor. If Station and Conveyor are not placed directly side by side, the MU seems to hang in thin air (compare Position of the MU). If the objects are placed directly side by side, you will not notice that, as the MU still seems to be located on the predecessor.

- **Moving from length-oriented object to length-oriented object**  
  When moving from Conveyor to Conveyor, the MU moves continually on, i.e., only its front moves on to the successor, while the remainder follows with the Speed you specified. If the transport speeds differ, Plant Simulation uses the speed of the Conveyor on which the Booking Point Length of the MU is located.

- **Moving from length-oriented object to point-oriented object**  
  When moving onto a point-oriented object, such as a Station, the MU always moves completely and instantaneously, i.e., it is then located on that object as a whole, not only its front section.

You can also enter the **MU Distance** between MUs on the Conveyor. This is the distance between the end of the MU that is located on the Conveyor and the beginning of the next MU that wants to enter. If no further MUs arrive, the Conveyor stops when this distance has been reached. As soon as the next MU arrives, it starts to transport MUs again. The default value `-1` means that the Conveyor does not use a MU Distance.

> **Note:** If the preceding Conveyor transports MUs faster than the Conveyor which uses a gap, the MU Distance can become smaller. This happens because the entering MU will be transported with a greater speed until its booking point is located on the conveyor which uses a gap.

### Inserting the Conveyor into a Frame

- As a **curved object** (the default setting). By inserting any sequence of curved segments and straight segments, you can realistically model curved conveyor systems on which the MUs move.

You can select different configurations for the Conveyor on the tab **Appearance**. To show a tooltip with information about the Conveyor, hover with the mouse over it.

### Show Manipulators

To change the length of the graphic and the anchor points of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard. The manipulator at the start and at the end of the length-oriented object is cut off. When you attach an object of the same type to the other object, the two combined halves result in a complete manipulator again. When you move the mouse over a manipulator, Plant Simulation shows a Tooltip.

### Add the Object to the Simulation Model

To add the object Conveyor to your simulation model, click **Manage Class Library > Basic Objects > MaterialFlow > Conveyor** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog Examples Collection, and click Open Model.

**See also:** Work with Length-oriented Objects; Model a Transport System with Active Objects.

---

## Dialog Box of the Conveyor

Double-click the icon of the Conveyor to open its dialog box.

- **Edit Simulation Properties** — change the simulation properties of the object. Shared properties are described under Dialog Items of the Objects.
- **Edit Animation Properties** — to edit the 3D properties in the dialog box Edit 3D Properties:
  - Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
  - Select the object in the model and press the spacebar.
  - To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

**See also:** Tab Importer [Conveyor] > Transport Importer.

---

## Tab Attributes

The tab Attributes provides the settings which the object offers. The settings are listed in the table of contents to the left. Shared properties are described under the Tab Attributes.

You can change the length of the graphic and the anchor points of the Conveyor by clicking **Show Manipulators** on the Edit ribbon tab or by pressing `M` on the keyboard.

### Length [text box]
Type the **Length** of the Conveyor into the text box.

**Remarks:**
- After you inserted it into your simulation model, Plant Simulation shows its length in the text box.
- The length of the Conveyor and the sum of the lengths of all MUs located on it determine how many MUs the Conveyor can accommodate at any one time. The length of the MUs will only be evaluated when you type in an unlimited Capacity.
- If you change the length, Plant Simulation automatically recomputes the Time.

**SimTalk:** `Length` — **See also:** `OccupiedLength`, Capacity, Time.

### Width [text box]
Type the **Width** of the Conveyor into the text box.

**SimTalk:** `Width` — **See also:** Width [tab Appearance].

### Speed [text box]
Type the **Final Speed** with which the Conveyor transports the MUs located on it into the text box.

**Remarks:**
- You can also type in `-1` for an infinite speed.
- If you change the Speed, Plant Simulation automatically recomputes the Time, and vice versa, provided you deactivated Acceleration. The Processing Time is the Length divided by the speed.
- If you activate Acceleration, the Conveyor attempts to reach the final speed no matter if a MU is located on it or not. A MU entering the Conveyor moves with the actual speed of the Conveyor. If the Conveyor currently accelerates, the MU will accelerate as well.

> **Note:** If you change the Speed, Plant Simulation re-computes all events relating to the Speed for all MUs located on it. If the MU located at the exit of the object is neither blocked nor stopped, it may happen that a new Out event is scheduled. In this case the Exit Control is called again independent of the setting Exit Control Once.

**SimTalk:** `Speed` — **See also:** Speed Control, Time, Acceleration, Length.

### Time [text box]
Type the **Time**, which a MU takes to cover the entire length of the empty Conveyor, into the text box.

**Remarks:**
- You can only type in the Time if you clear the check box Acceleration.
- If you change the Time, Plant Simulation automatically recomputes the Speed.
- If you type in `0` as the Time, the display of the speed is meaningless.

**SimTalk:** `Time` — **See also:** Speed, Acceleration.

### Accumulating [check box]
To make the MUs accumulate on the Conveyor, select this check box. This permits the MUs to move front to end to each other when the exit of the object is blocked.

**Remarks:**
- To make the MUs retain their distance to each other (i.e., make all succeeding MUs stop moving when the preceding MU cannot exit the Conveyor), clear the check box. If the object is blocked, it stops, i.e., it reduces its speed to 0.
- If a MU is stopped on a non-accumulating Conveyor, not only the succeeding MUs, but all MUs on this Conveyor are stopped and the current speed of the Conveyor is set to 0.
- If a MU is to be set in motion again, no additional stopped MUs may be located on the Conveyor. If this is the case, all MUs are set in motion and the Conveyor starts moving again.

**SimTalk:** `Accumulating` — **See also:** Exit Blocked; Model an Accumulating/a Non-Accumulating Transport System.

### Backwards
To make the Conveyor itself and the MUs on it move in reverse, select this check box. To make them move forward, clear the check box.

**Remarks:**
- When moving in reverse the MUs enter the Conveyor at its exit and leave it at its entrance.
- If you cleared Acceleration of the Conveyor, it reverses the direction in which it moves immediately without decelerating and accelerating.
- If you selected Acceleration, the Conveyor slows down until its speed is 0. Then it reverses the direction in which it moves and accelerates until it reaches its final speed.

**SimTalk:** `Backwards` — **See also:** Speed, Acceleration, `AccelerationEnabled`.

### Acceleration [check box]
To make the Conveyor increase its speed, select this check box.

**Remarks:**
- Then, type in the **Acceleration** with which it speeds up and the **Deceleration** with which it slows down. The Conveyor also shows the actual **Current Speed** with which it moves.
- If you change the Speed, Plant Simulation recomputes the Time and vice versa, if you deactivate Acceleration.
- If you activate Acceleration, the Conveyor attempts to reach the final speed no matter if a MU is located on it or not. A MU entering the Conveyor moves with the actual speed of the Conveyor. If the Conveyor currently accelerates, the MU will accelerate as well.
- To deactivate acceleration, clear the check box.

**SimTalk:** `AccelerationEnabled` — **See also:** Acceleration, Deceleration, Speed, Time.

### Current Speed [text box]
Shows the **Current Speed** of the Conveyor at the present time here, provided you selected the check box Acceleration.

**Remarks:** The setting is watchable for special values. By watching this value, you might, for example, detect the event when the Conveyor has reached its Final Speed.

**SimTalk:** `CurrentSpeed` — **See also:** Acceleration, Speed Control.

### Acceleration [text box]
Type the **Acceleration** into the text box with which the Conveyor increases its speed.

**Remarks:**
- You can type in any real number greater than or equal to 0.
- You can only type in a value for the Acceleration after you select the check box Acceleration.

**SimTalk:** `Acceleration` — **See also:** Acceleration [check box].

### Deceleration [text box]
Type the **Deceleration** into the text box with which the Conveyor reduces its speed.

**Remarks:**
- You can type in any real number greater than or equal to 0.
- You can only type in a value for the Deceleration after you select the check box Acceleration.

**SimTalk:** `Deceleration` — **See also:** Acceleration [check box].

### Capacity [text box]
Type the **Capacity** of the Conveyor into the text box.

**Remarks:**
- The Capacity is the maximum number of MUs that can be located on the Conveyor as a whole or in part at any one time.
- The default value `-1` designates an infinite capacity.
- You can also type in another number, so that the Conveyor does not make use of the entire available Length.

**SimTalk:** `Capacity` — **See also:** Length.

### MU Distance Type [text box]
Select the **MU Distance Type** for the space between the MUs. Then, type the actual distance into the text box MU Distance.

**Remarks:**
- Plant Simulation only runs the distance check when a MU moves onto the Conveyor. If you selected Accumulating, for example, the distance can fall below the value once the MUs accumulate.

> **Note:** The Front of the part always moves toward the end of the length-oriented object into the direction with which you inserted it along the direction of motion of the material flow. When you insert a length-oriented object, for example a Conveyor, from left to right, the Front of the part is located on the right-hand side and moves toward the right. When you insert a length-oriented object from right to left, the Front of the part is located on the left-hand side and moves toward the left. This also applies to parts which move backward when you select the check box Backward of the Conveyor or the Transporter. The Front of the part keeps on pointing toward the end of the length-oriented object into the direction with which you inserted it.

You can select one of these settings:

- **Gap** — Sets the distance between the rear of the preceding part and the front of the succeeding part.
- **Pitch** — Sets the distance between the front of the preceding part and the front of the succeeding part.
- **Minimum Gap** — Sets the minimum distance between the rear of the preceding MU and the front of the succeeding MU. This setting prevents the Conveyor from stopping and from waiting for new MUs and enables the Conveyor to run dry.
- **Minimum Pitch** — Sets the minimum distance between the front of the preceding MU and the front of the succeeding MU. This setting prevents the Conveyor from stopping and from waiting for new MUs and enables the Conveyor to run dry.
- **Multiple Gap** — Sets the distance between the rear of the preceding MU and the front of the succeeding MU. The distance can be an integer multiple of the defined MU Distance. Just as for Minimum Gap, the Conveyor does not stop to wait for new MUs after the gap has been passed. The next MU can only enter the Conveyor if an integer multiple of the gap can be preserved.
- **Multiple Pitch** — Sets the distance between the front of the preceding MU and the front of the succeeding MU. The distance can be an integer multiple of the defined MU Distance. Just as for Minimum Pitch, the Conveyor does not stop to wait for new MUs after the pitch has been passed. The next MU can only enter the Conveyor if an integer multiple of the pitch can be preserved. For this setting the Conveyor behaves like a chain conveyor.

**SimTalk:** `MUDistanceType` — **See also:** MU Distance; Model a Fixed Gap or a No Gap Conveyor; Model a Multiple Gap or a Multiple Pitch Conveyor.

### MU Distance [text box]
Select the MU Distance Type and type in the desired distance of the current MU to the preceding MU which the Conveyor enforces, when the next MU enters.

**Remarks:**
- Depending on the setting for the MU Distance Type, the MU Distance determines for:
  - **Gap** the distance between the rear of the preceding MU and the front of the succeeding MU.
  - **Pitch** the distance between the front of the preceding MU and the front of the succeeding MU.
- If no further parts arrive, the Conveyor stops once the distance has been reached. As soon as the next MU arrives, it starts to transport MUs again.
- The default value `-1` means that the Conveyor does not use the MU Distance and that MUs can enter at any time as the predecessor provides them.

> **Note:** If the preceding Conveyor transports parts faster/slower than the Conveyor which uses a MU Distance, the distance itself can become greater/smaller. This is because the entering MU moves with a faster/slower speed until its booking point is located on the Conveyor using a MU Distance. If the succeeding Conveyor transports parts faster/slower than the Conveyor which uses a MU Distance, the distance itself can become greater/smaller. This is because the booking point of the leaving MU is located on the succeeding Conveyor, which transports parts with a faster/slower speed.

> **Note:** Plant Simulation only runs the distance check when a part enters. If you selected Accumulating, for example, the distance can be undercut when the parts accumulate.

> **Note:** The Conveyor only uses the MU Distance if it transports parts in the forward direction.

**SimTalk:** `MUDistance` — **See also:** MU Distance Type.

### Enforce MU Distance [check box]
To force the Conveyor to keep the specified MU Distance between the MUs, even if the MUs accumulate on the Conveyor, select this check box.

**Remarks:**
- To allow the MUs to accumulate on the Conveyor and thus move front to end, clear the check box.
- This setting only applies when the Conveyor is Accumulating and conveys MUs in the forward direction.
- Depending on the setting MU Distance Type and the Speed of succeeding Conveyors, the MU Distance might increase.
- Changing the material flow, either via information flow or manually, might temporarily decrease the MU Distance:
  - If you insert MUs on the Conveyor via information flow or if you increase the length of the inserted MU, and thus violate the specified MU Distance, the respective MUs stop until the MU Distance is met again.
  - If you create MUs on a Conveyor via information flow, the created MUs stop until the MU Distance is met again. The following MU keeps the distance to the previous MU instead of to the created MU, until the created MU starts moving.
  - If you change the MU Distance of the Conveyor via information flow while MUs are located on it, the MUs keep their original distance at first. If the MUs are stopped later on, for example because they accumulate on the Conveyor, they only start moving again when the new distance is met.

**SimTalk:** `EnforceMUDistance` — **See also:** Model a Fixed Gap or a No Gap Conveyor; MU Distance; `MUDistance`.

### Automatic Stop [check box]
To set the **Current Speed** of the Conveyor to 0 when it does not transport a MU, select this check box. This might, for example, be the case if it is empty or if it is blocked if a MU cannot leave it.

**Remarks:**
- If you select Automatic Stop, Plant Simulation immediately sets the Speed to 0 without using the value you typed in for the Deceleration. Along the same lines the Speed is immediately set to the Target Speed without using the value you typed in for the Acceleration.
- When the Speed of the Conveyor is 0, the Energy State changes to Operational.

**SimTalk:** Current Speed; `AutomaticStop`.

---

## Tab Times

Define Times as described under the Tab Times. Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (Const).

You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr`.

**See also:** Recovery Time; Recovery Time Starts; Cycle Time.

---

## Tab Failures

Define failures as described under the Tab Failures.

---

## Tab Controls [Conveyor]

Provides controls to modify the built-in behavior of the object.

### Select the Path to an Existing Method
Click the ellipsis button. Navigate to the location of the Method in the dialog Select Object [for controls] and click OK. This inserts the name of the Method into the text box of the Control. Press `F2` in the text box to open the Method. Then type in the source code of the Control. Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

### Create a Control That is a Method of the Object
Proceed as follows to create a control as a user-defined attribute of data type Method:
- Type a meaningful name into the text box and select **Create Control** [context menu]. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens. To edit the source code later on:
- Press `F2`.
- Or hold down `Shift` and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab User-defined and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

You can create an **Entrance Control**, an **Exit Control**, a **Backward Entrance Control**, a **Backward Exit Control**, a **Speed Control**, and a **Pull Control**.

In addition, you can:
- Select the Shift Calendar [tab Controls].
- Create and insert **Sensors**. The Conveyor shows the sensors, which you defined, on its graphic in the Frame window. To open the dialog Sensors, hold down `Alt` and double-click the sensor.

**SimTalk:** `BwExitCtrl`, `BwExitCtrlFront`, `BwExitCtrlRear`, `BwEntranceCtrl`, `BwEntranceCtrlFront`, `BwEntranceCtrlRear`, `EntranceCtrl`, `EntranceCtrlFront`, `EntranceCtrlRear`, `ExitCtrl`, `ExitCtrlFront`, `ExitCtrlRear`, `PullCtrl`, `ShiftCalendarObject`, `SpeedCtrl`.

**See also:** Define Controls for Length-Oriented Objects; Sensors.

### Speed Control [Conveyor]
Modifies the built-in behavior of the object. The Conveyor/loading space of type Line of the Transporter call the Speed Control as soon as they reach their final speed after accelerating or decelerating or when they stop after decelerating.

**Remarks:**
- Plant Simulation does not call the Speed Control if the speed changes without using up any time at all.
- You can only set the Speed Control after you activate Acceleration/`AccelerationEnabled`.
- The Speed Control also applies to the loading space of type Line of the Transporter. It calls the Speed Control as soon as they reach their final speed after accelerating or decelerating or when they stop after decelerating.

**Select the Path to an Existing Method / Create a Control That is a Method of the Object** — same procedure as described above (ellipsis button / Create Control, `self.Name...`, `self.On...`; edit via `F2`, `Shift`+double-click, Open Object, or User-defined tab; delete by deleting the user-defined attribute).

**SimTalk:** `SpeedCtrl`, `LoadBaySpeedCtrl`, `AccelerationEnabled`.

**See also:** Select Object [for controls]; Transporter > Controls [loading space] > Speed Control; Acceleration.

---

## Tab Exit

Select to which of its successors the object moves the MU on the Tab Exit.

**See also:** Blocking [exit strategy]; Strategy [material flow objects].

---

## Tab Statistics [Conveyor]

In addition to the statistics values described under the Tab Statistics, the accumulating Conveyor shows the value **Exit blocked**.

> **Note:** The Conveyor is in the state Working when its Current speed is not 0. It also is working when the conveyor is moving and does not transport a part.

To view Resource Statistics of Stationary Resources in the Statistics Report, select **View > Show Statistics Report** in the dialog of the object. You can also click the right mouse button in the Frame and select Show Statistics Report, or you can press `F6`.

**See also:** Resource Statistics; Resource Type.

---

## Tab Importer [Conveyor]

On the Tab Importer > Sub-tab Transport you can specify how the Worker picks up conveyed parts and carries them to another station. This also enables the Worker to carry parts to the Conveyor.

To view Importer Statistics in the Statistics Report, click the object in the Frame, and press `F6` (Show Statistics Report), or click Show Statistics Report on the Home ribbon tab. You can also click the object in the Frame with the right mouse button and select Show Statistics Report on the context menu.

**See also:** Transport Importer Broker; Active; Request Control; Receive Control; Release Control; Wait for Free Target; MU Target; Priority; Maximum Dwell Time; Services for Carrying Parts Away; Can Be Interrupted and Drawn Off.

---

## Tab Energy

Select energy settings for the object on the Tab Energy.

---

## Tab Costs

Select costs settings for the object on the Tab Costs.

While the Conveyor transports parts costs accrue which result from the sum of the total investment costs and the total operating costs.

> **Note:** The total investment costs only accrue during the Depreciation Period.

These costs are allocated to the part, proportional to the length of the part, as accrued costs. Thus a longer part is allocated higher costs as it occupies a greater part of the Conveyor. If the Conveyor is empty, the costs remain with the Conveyor as general costs.

**See also:** Operating Costs; Operating Costs per Length; Depreciation Period; Investment Costs; Investment Costs per Length; CostAnalyzer.

---

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

---

## Navigate Menu

The commands are described under the Navigate Menu.

---

## View Menu

The commands are described under the View Menu.

**SimTalk:** `updateDialog`.

---

## Tools Menu

The commands are described under the Tools Menu.

---

## Tabs Menu

Use the commands of the Tabs menu to show or hide individual tabs of the selected material flow objects. If you hide tabs that you do not need, Plant Simulation opens the dialog faster, and you can change to those tabs faster that you need in your daily work.

**Remarks:**
- To apply the changed settings, click OK, close the dialog, and reopen it.
- The menu shows a check mark to the left of the displayed tabs.
- The command **Inherit** turns inheritance of the displayed or hidden tabs in the dialog off or on.

---

## Help Menu

The commands are described under the Help Menu.

---

## Methods of the Conveyor

The Conveyor provides:
- The Methods of Curved Objects.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the `F8` key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.
