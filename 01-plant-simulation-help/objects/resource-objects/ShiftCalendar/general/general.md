# ShiftCalendar [object]

Use the object **ShiftCalendar** for modeling the shift system and organizing the shift work performed in your plant.

## Overview

You can define as many shifts in your simulation model as you need. A shift pauses one or several machines in your model, by setting the boolean attributes `Pause` and `Unplanned` of the respective material flow objects to `true`.

### Note

- If you deactivate the `Pause` during the unplanned time (either by clearing the check box **Pause** in the object's dialog, or by setting the attribute `Pause` to `false`), the object starts to work.
- Use the method `schedule` to make the ShiftCalendar set the date and time to start or finish the production process. We distinguish between:
  - **Forward scheduling** — beginning from the start date forward into the future.
  - **Backward scheduling** — computes the start date going backward in time from the demand date.

Normally, you start with the demand date, computing the start date through backward scheduling. If this start date is located in the past, you have to recompute the dates beginning with the present time and forward-schedule the end date.

- To show a tooltip with information about the ShiftCalendar, hover over it with the mouse.
- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.

### Add the Object to the Simulation Model

To add the object ShiftCalendar to your simulation model, click **Manage Class Library > Basic Objects > Resources > ShiftCalendar** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then select the respective Category, Topic, and Example in the dialog **Examples Collection**, and click **Open Model**.

### See also

- Model a Shift System
- Shift Calendar [tab Controls]
- Select Shift Calendar

---

## Dialog Box of the ShiftCalendar

Double-click the icon of the ShiftCalendar to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M**.

> **Note:** Before you can type in data, click the **Inheritance** check box so that it looks like this ![](blank).

### See also

- Active [check box] - ShiftCalendar

---

## Active [check box] - ShiftCalendar

To make your facility work in shifts, select this check box. To deactivate shift work, clear the check box.

### Remarks

Instead, you can also right-click the ShiftCalendar object in the Frame and select **Activate** on the context menu. To deactivate shift operation, select **Deactivate** on the context menu.

**SimTalk:** Active [SimTalk] - ShiftCalendar

---

## Tab Shift Times

Type in the name of the Shift, the time it starts, the time it ends, and the duration of Pauses on the tab **Shift Times**.

> **Note:** Before you can type data into the table on the tab, click the **Inheritance** check box so that it is turned off.

To select which shift works on which day, select the respective check box in the cells below **Mo, Tu, We, Th, Fr, Sa, Su**.

To manipulate the contents of the list, use the commands on the Context Menu of Embedded Lists.

**SimTalk:** `schedule` [SimTalk] - ShiftCalendar, `ShiftPlan` [SimTalk]

### See also

- Shift [ShiftCalendar]
- From
- To
- Pauses [ShiftCalendar]
- Specify the Names of the Shifts, the Respective Times and Days

---

## Shift [ShiftCalendar]

Type in the names of the different shifts into these cells.

> **Note:** Before you can type data into the table on the tab, click the **Inheritance** check box so that it is turned off.

You might, for example, type in `Morning`, `Evening`, `Graveyard`, etc.

The ShiftCalendar displays these state graphics:

| State |
|-------|
| Unplanned |
| Planned |

**SimTalk:** `GetCurrShift` [SimTalk], `ShiftPlan` [SimTalk]

---

## From

Type the times at which the respective shifts start in these cells.

> **Note:** Before you can type data into the table on the tab, click the **Inheritance** check box so that it is turned off.

Type in a time between 0:00 o'clock and 24:00 o'clock. You can only type in hours and minutes, not hours, minutes and seconds.

- To create a shift located **within one day**, type in a greater number for the time at which it ends than for the time at which it starts. For example, a Morning shift that starts at 6:00 and ends at 14:00 on the same day.
- To create a shift that **spans two days**, type in a smaller number for the time at which it ends than for the time at which it starts. For example, a Graveyard shift that starts at 22:00 at night on one day, and ends at 6:00 in the morning on the next day.

> **Note:** You cannot enter overlapping shift times.

**SimTalk:** `ShiftPlan` [SimTalk]

---

## To

Type the times at which the respective shifts end into these cells.

> **Note:** Before you can type data into the table on the tab, click the **Inheritance** check box so that it is turned off.

Type in a time between 0:00 o'clock and 24:00 o'clock. You can only specify hours and minutes, not hours, minutes and seconds.

- To create a shift located **within one day**, type in a greater number for the time at which it ends than for the time at which it starts. For example, a Morning shift that starts at 6:00 and ends at 14:00 the same day.
- To create a shift that **spans two days**, type in a smaller number for the time at which it ends than for the time at which it starts. For example, a Graveyard shift that starts at 22:00 at night on one day, and ends at 6:00 in the morning on the next day.

> **Note:** You cannot enter overlapping shift times.

**SimTalk:** `ShiftPlan` [SimTalk]

---

## Mo, Tu, We, Th, Fr, Sa, Su

To select the individual days on which the shift in the row is active, click the respective check box in the cells below the days of the week.

> **Note:** Before you can type data into the table on the tab, click the **Inheritance** check box so that it is turned off.

You might, for example:

- Define a Morning shift that works Monday up to and including Friday.
- Define an Evening shift that works Monday up to and including Sunday.

**SimTalk:** `ShiftPlan` [SimTalk]

---

## Pauses [ShiftCalendar]

Type in the times of the breaks for each shift into these cells.

> **Note:** Before you can type data into the table on the tab, click the **Inheritance** check box so that it is turned off.

Type in the hour and the minute when the break starts, a hyphen and the hour and minute the break ends. When you define several breaks, separate them with a semicolon.

To define a coffee break from 9 o'clock to a quarter past 9 o'clock, and a lunch break from 12 o'clock to a quarter till 1 o'clock, type in `9:00-9:15;12:00-12:45`.

To make the ShiftCalendar check if the values you typed in for the breaks are plausible or not and if you used the correct format to enter the break times, click **Apply**.

**SimTalk:** `ShiftPlan` [SimTalk]

---

## Tab Calendar

Define the days on which your plant does not work at all or only works part of the time, and a **Comment** describing the event on the tab **Calendar**.

> **Note:** Before you can use the date picker, click the check box **Inheritance** so that it looks like this ![](blank).

You can also import a calendar that you saved, or export a calendar you defined and then import it into another simulation model. Click into the list field with the right mouse button and select **Import** or **Export**.

To manipulate the contents of the list, use the commands on the Context Menu of Embedded Lists.

**SimTalk:** `Calendar` [SimTalk], `schedule` [SimTalk] - ShiftCalendar

### See also

- Date From
- Date To
- Reduce Time To
- Comment [reduce time to]
- Specify Times During Which the Plant Works Part of the Time

---

## Date From

Type the date at which your plant starts not working into these cells with the date picker.

### Remarks

Proceed as follows:

1. Click the **Inheritance** check box so that it looks like this ![](blank).
2. Double-click into the text box and click the down arrow ![](blank).
3. Select a date in the calendar. Click the right or left buttons to move to another month.

To designate an entire day as a day-off, only select a start date, and no end date (**Date To**), and no **Reduce Time To**.

**SimTalk:** `Calendar` [SimTalk]

---

## Date To

Type the date at which your plant stops not working into these cells with the date picker.

### Remarks

Proceed as follows:

1. Click the **Inheritance** check box so that it looks like this ![](blank).
2. Double-click into the text box and click the down arrow ![](blank).
3. Select a date in the calendar. Click the right or left buttons to move to another month.

To designate a consecutive number of days-off, enter a start date (**Date From**), and an end date, and no **Reduce Time To**.

**SimTalk:** `Calendar` [SimTalk]

---

## Reduce Time To

Type in the hour and the minute when the reduced working time starts, a hyphen and the hour and minute the reduced time ends.

> **Note:** Click the **Inheritance** check box so that it looks like this ![](blank).

If your plant only works half a day on Christmas Eve, for example the shift from midnight to noon, you would type `0:00 - 12:00` into the cell **Reduce Time To**.

To designate several days on which your plant only works part of the time, type the start date in the cell in the column **Date From**, and the end date in the cell in the column **Date To**. Then, type the period of time in the cell **Reduce Time To**.

> **Note:** The ShiftCalendar combines the reduced time and the definition of the shifts for a day. If, for example, the start time of a day with a reduced working time falls on a break, then this work day starts with a break.

**SimTalk:** `Calendar` [SimTalk]

### See also

- Working [state, material flow objects]

---

## Comment [reduce time to]

Type a description of the event causing the **Reduce Time To** in this cell.

> **Note:** Click the **Inheritance** check box so that it looks like this ![](blank).

### See also

- Reduce Time To

---

## Tab Resources [ShiftCalendar]

Assign resources, meaning objects, to the ShiftCalendar on the tab **Resources**.

### Remarks

A resource is any of the built-in Material Flow Objects, or a Frame in which you modeled a machine, whose Working hours you would like to control with the ShiftCalendar.

To add a resource to the tab **Resources**, drag it from the Frame window over the icon of the ShiftCalendar and drop it there. You can also select and then drag-and-drop multiple objects at the same time.

This automatically enters the ShiftCalendar into the text box **Shift Calendar** on the tab **Controls** of the material flow object.

To manipulate the contents of the list, use the commands on the Context Menu of Embedded Lists.

### See also

- Specify the Stations Which the ShiftCalendar Controls
- Resources [SimTalk] - ShiftCalendar
- Shift Calendar [tab Controls]

---

## Objects [ShiftCalendar]

Assign resources to the ShiftCalendar on the tab **Resources**.

### Remarks

A resource is any of the built-in Material Flow Objects, or a Frame in which you modeled a machine, whose Working hours you would like to control with the ShiftCalendar.

- Type the path to and the name of the resource object in a cell. **Or**
- Drag the resource object to the icon of the ShiftCalendar and drop it there. **Or**
- Type the name of the ShiftCalendar object on the tab **Controls** of the material flow object into the text box **Shift Calendar**.

> **Note:** Plant Simulation pauses all resources you assign to a shift.

**SimTalk:** `Resources` [SimTalk] - ShiftCalendar

---

## Tab User-defined

Define your own attributes as described under the **Tab User-defined**.

---

## File Menu [ShiftCalendar]

The File menu provides the commands listed in the table of contents to the left.

### Import Shift Times

Imports the times during which your plant works in shifts from a tab delimited text file.

### Export Shift Times

Exports the shift times you defined on the **Tab Shift Times** to a file.

You can then import this file into another ShiftCalendar or edit it in a word processing program.

### Import Calendar

Imports the calendar, i.e., the days during which your plant works in shifts, from a tab delimited text file.

### Export Calendar

Exports the shift calendar you defined on the **Tab Calendar** to a file.

You can then import this file into another ShiftCalendar or edit it in a word processing program.

---

## Navigate Menu

The commands are described under the **Navigate Menu**.

---

## View Menu

The View Menu provides commands to access its functions.

- Refresh [on View menu]
- Show Assigned Objects [ShiftCalendar]
- Show Attributes and Methods [on View menu]

**SimTalk:** `updateDialog` [SimTalk]

### Show Assigned Objects [ShiftCalendar]

Selects the objects which are assigned to the ShiftCalendar as resources in the Frame window.

Instead, you can also select **Show Assigned Objects [in Frame]** on the context menu of the ShiftCalendar in the Frame.

---

## Tools Menu

The Tools Menu provides these menu commands:

- Edit Controls
- Edit Observers

---

## Help Menu

The commands are described under the **Help Menu**.

---

## Methods of the ShiftCalendar

The ShiftCalendar provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].
