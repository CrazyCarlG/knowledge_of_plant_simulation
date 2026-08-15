# Tank [object]

Use the object **Tank** to temporarily store a single material before or after processing. The material can flow into the Tank from several predecessors and can flow out of the Tank to several successors.

## Description

The Tank can only accommodate a single type of material at any one time. The inflow of new material is blocked until the Tank is empty, so you cannot let another material flow into the Tank before it is empty all the way.

- To show a tooltip with information about the Tank, hover with the mouse over it.
- To change the length of the graphic and the anchor points of the Tank, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

### Add the Object to the Simulation Model

To add the object Tank to your simulation model, click **Manage Class Library > Basic Objects > Fluids > Tank** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then select the respective Category, Topic, and Example in the dialog *Examples Collection*, and click **Open Model**.

### See also

- Simulate Free-flowing Materials and Fluids
- Configure the Tanks Storing the Materials
- Dialog Box of the Tank

## Dialog Box of the Tank

Double-click the icon of the Tank to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Tab Attributes

The tab *Attributes* provides the settings that the object offers. The settings are listed in the table of contents to the left. The shared properties are described under the *Tab Attributes*.

### Outflow Rate [Tank]

Type the *Outflow Rate* into the text box with which the material flows out of the Tank. The material then flows through the objects of type Pipe to the next object in the flow of materials.

**Remarks**

The Outflow Rate is the amount of liters of the material that flows off in a second.

**Note**

The current Outflow Rate depends on the number of attached Pipes. Let's say you attached two Pipes, then the specified Outflow Rate flows through each one of these Pipes in case the Outflow Rate of the connected Pipes permits this.

If you just want to let the specified amount flow out of the object, attach a single Pipe and split that up into several Pipes later on.

Plant Simulation shows error messages if the Outflow Rate of an empty Tank is greater than the Inflow Rate or if the inflow rate of a full Tank is greater than the Outflow Rate. Do not ignore these error messages, but create Sensors and program Methods which handle these situations. The Sensors have to prevent the Tank from becoming full or empty respectively by opening or closing the connected Pipes.

SimTalk: `OutflowRate [SimTalk] - Tank`

### Volume [Tank]

Type the *Volume* of the Tank into the text box, i.e. the space that the ingredient occupies within the tank.

SimTalk: `Volume [SimTalk] - Tank`

### Shift Calendar [Tank]

Select the *ShiftCalendar*. It contains the data of the shifts in your installation and controls during which shifts the Tank works.

**Remarks**

- Click the ellipsis button and select the ShiftCalendar in the dialog *Select Object*.
- Instead of clicking the ellipsis button, you can also select the ShiftCalendar in a Frame, drag it to the text box, and drop it there.

This automatically enters the object into the list of Objects on the tab *Resources* of the ShiftCalendar.

SimTalk: `ShiftCalendarObject [SimTalk] - material flow objects`

See also: ShiftCalendar [object], Associated Shift Calendar, Select Object [for controls]

### Current Material [Tank]

Shows the name of the *Current Material* that is located in the Tank.

**Remarks**

The name is not case-sensitive, just like the names of attributes and methods of the objects are not case-sensitive. To save memory and improve access speed, all places which use such a case-insensitive string point to the same string in main memory. The visible and unexpected result is that the first occurrence of the string defines how the string is written in terms of upper- and lower-casing.

In SimTalk you can compare strings in a case-insensitive manner with the `~=` operator (compare *Relational Operators*).

The Tank can only accommodate a single type of material at any one time. The inflow of new material is blocked until the Tank is empty, so you cannot let another material flow into the Tank before it is empty all the way.

SimTalk: `CurrentMaterial [SimTalk] - Tank`

### Current Fill Level [Tank]

Shows the *Current Fill Level* of the material in the Tank. The Tank shows the current fill level on the outflow side.

SimTalk: `CurrentFillLevel [SimTalk] - Tank`

### Current Amount [Tank]

Shows the *Current Amount* of the material that is located in the Tank.

SimTalk: `CurrentAmount [SimTalk] - Tank`

### Current Inflow Rate [Tank]

Shows the *Current Inflow Rate*, i.e. the amount of liters of the material which flows into the Tank in a second.

SimTalk: `CurrentInFlowrate [SimTalk]`

### Current Outflow Rate [Tank]

Shows the *Current Outflow Rate*, i.e. the amount of liters of the material that flows out of the Tank in a second.

SimTalk: `CurrentOutFlowrate [SimTalk]`

## Sensors [Tank]

To create sensors in the Tank, click **Sensors**. The button opens the dialog *Sensor List*, where you create new sensors or modify or delete existing sensors.

Proceed as follows:

- To create a new sensor, click **New**.
- To edit the settings of the sensor, click **Edit** or double-click the name of the sensor in the sensor list.
- To delete the sensor that you selected in the list of sensors, click **Delete**.

For the Tank you can:

- Select if the *Position* of the sensor in the Tank is relative or absolute.
- Select if the sensor is to be triggered if the amount of material has *Exceeded* the position of the sensor.
- Select if the sensor is to be triggered if the amount of material is below the position, i.e. has *Underrun* it.
- Select or create the *Control* that the sensor triggers.

See also: _Methods of the Sensors of the Tank, _Attributes of the Sensors of the Tank

### Position [Tank]

Select the type of the *Position* of the sensor in the Tank from the drop-down list. Then type the position of the sensor into the text box *Position*.

**Remarks**

You can select one of these settings:

- **Relative**: Type a value between 0 and 1, i.e. between 0 percent and 100 percent. Plant Simulation shows 0..1 as unit.
- **Absolute**: Type a value between 0 and the Volume you specified. Plant Simulation shows `l` (liters) as unit.

SimTalk: `Position [SimTalk] - Tank`, `PositionType [SimTalk]`

### Exceeded [check box]

To trigger the sensor if the amount of material in the Tank has *Exceeded* the amount, i.e. is located above the sensor position, select this check box.

SimTalk: `Exceeded [SimTalk]`

### Underrun [check box]

To trigger the sensor if the amount of material in the Tank has *Underrun* the amount, i.e. is located below the sensor position, select this check box.

SimTalk: `Underrun [SimTalk]`

### Control [Tank]

Modifies the built-in behavior of the object. The object calls the Control according to the settings you selected.

As soon as you enter a Sensor Control, the context menu of the object in the Frame shows the command *Controls*. You can then select the name of the sensor control on the submenu to edit it.

**Select the Path to an Existing Method**

- Click the ellipsis button. Navigate to the location of the Method in the dialog *Select Object [for controls]* and click OK. This inserts the name of the Method into the text box of the Control.
- Press F2 in the text box to open the Method. Then type in the source code of the Control.
- Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

**Create a Control That is a Method of the Object**

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select *Create Control* [context menu]. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select *Create Control* on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press F2.
- Or hold down Shift and double-click into the text box.
- Or select *Open Object* on the context menu.
- Or click the tab *User-defined* and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

The standard sensor control as a user-defined attribute looks like this:

```simtalk
self.OnEntrance
```

**Parameters**

You can specify the following parameters:

- As soon as the sensor calls this Method, it passes the Sensor-ID as an optional parameter. If the Method expects a parameter of data type integer, the sensor passes the Sensor-ID to the Method. If you do not specify an integer parameter, the Method will be called without a parameter.
- The optional parameter *Exceeded* of data type boolean shows the user if the sensor position is Exceeded or Underrun.

SimTalk: `sensorID(sensorID).Control [SimTalk] - sensor, Tank`, `ID [SimTalk] - Tank`

See also: Select Object [for controls]

## Tab Times

Define Times as described under the *Tab Times*.

Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (`Const`).

You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr [SimTalk]`.

See also: Set-up Time [general description], `SetupTime [SimTalk] - fluid objects`, Select the Set-Up Time

## Tab Failures

Define failures as described under the *Tab Failures*.

## Tab Statistics [Tank]

In addition to the values described under the *Tab Statistics*, the tab *Statistics* of the Tank shows these object-specific values.

| Item (English) | Description | Read-only attribute |
| --- | --- | --- |
| Total Throughput | Shows the amount of material that flowed through the Tank. | `StatDeleted [SimTalk] - Drain` |
| Relatively Empty | Shows the portion of the statistics collection period during which the Tank was Empty in relation to the time during which the Tank was available. | `StatRelativeEmptyPortion [SimTalk]` |
| Relatively Full | Shows the portion of the statistics collection period during which the Tank was full in relation to the time during which the Tank was available. | `StatRelativeFullPortion [SimTalk]` |
| Relative Occupation | Shows the sum of all dwelling times of all materials during the statistics collection period during which the Tank was not paused and not failed. | `Name [SimTalk] - MUs` |

## Tab Importer

On the *Tab Importer* you can define services for processing the parts, for setting the station up for a certain type of part, and for repairing the station.

To view Importer Statistics in the Statistics Report, do one of the following:

- Select **View > Show Statistics Report** in the dialog of the object.
- Click the object with the right mouse button in the Frame and select *Show Statistics Report* or press F6.
- Click *Show Statistics Report* on the Home ribbon tab.

See also: Processing Importer, Set-up Importer, Failure Importer

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

## Navigate Menu

The commands are described under the *Navigate Menu*.

## View Menu

The View Menu provides commands to access its functions. The View Menu also provides commands pertaining to the Transport Importer.

- Exporters [on View menu]
- Unavailable Services [on View menu]
- Services [on View menu]
- Associated Workplaces [on View menu]

See also: View Menu [general description], Transport Importer

## Tools Menu

The commands are described under the *Tools Menu*.

## Help Menu

The commands are described under the *Help Menu*.

## Methods of the Tank

The Tank provides:

- The General Methods of the Tank.
- The Methods of the Sensors of the Tank.
- The Methods of the Fluid Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window *Show Attributes and Methods*. The figure illustrates the information using the example of the object Station.

- Select *Show Attributes and Methods* on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the F8 key or click *Show Attributes and Methods* on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

To set the value of an attribute, you might, for example, type:

```simtalk
MyFluidDrain.Pause := true
```

To get the value of an attribute, you might, for example, type:

```simtalk
print MyFluidDrain.Pause
posit := MyStation.Cont.XPos
```
