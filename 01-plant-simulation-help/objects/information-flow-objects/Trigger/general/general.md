# Trigger — General

## Description

The **Trigger** maps times to the values of a variable. User-defined attributes take on values designated by the Trigger during a simulation run. You can specify the values either in a single `TimeSequence` object or by combining several time sequences of other Triggers. In addition, a Trigger can control how and when a Source creates MUs.

- Hover with the mouse over the Trigger to show a tooltip with information about it.
- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`.

### Add the Object to the Simulation Model

To add the object Trigger to your simulation model, click **Manage Class Library > Basic Objects > InformationFlow > Trigger** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then select the respective Category, Topic, and Example in the dialog *Examples Collection*, and click Open Model.

**See also:** Produce Parts Using a Trigger Object, Dialog Box of the Trigger.

## Dialog Box of the Trigger

Double-click the icon of the Trigger to open its dialog box.

- **Edit Simulation Properties** — change the simulation properties of the object. Shared properties are described under *Dialog Items of the Objects*.
- **Edit Animation Properties** — edit the 3D properties via **Edit 3D Properties** (lower-left corner of the simulation properties dialog box) or by selecting the object and pressing the spacebar.

---

## Tab Period

### Active [check box]

Activate/deactivate the Trigger during the simulation run.

**Remarks:** You can also right-click the Trigger object in the Frame and select **Activate**/**Deactivate** on the context menu.

**SimTalk:** `Active`

### Time Reference

Select the time reference the Trigger uses during the simulation run:

- **Relative** — type a point in time (`time`) into the text box **Start Time**.
- **Absolute** — type a point in time on a certain date (`dateTime`) into the text box **Start Date**.

**SimTalk:** `Absolute`

### Start Time

Type the point in time (data type `time`) at which the Trigger starts working.

**SimTalk:** `ReferenceTime`

### Start Date

Type the date and the point in time at which the Trigger starts working (for **Time Reference > Absolute**).

**SimTalk:** `ReferenceDate`

### Active Interval

Type the time interval during which the Trigger will be active. After this interval has elapsed, the Trigger value assumes the default value (defined under **Values > Values > Value Table** of the TimeSequence belonging to the Trigger).

**SimTalk:** `ActiveInterval`

### Repeat Periodically

Make the Trigger repeat the values periodically instead of processing them one time only.

**Remarks:** Only select this check box after setting a suitable time unit on the **Tab Representation**; otherwise drawing the display may be time-consuming.

**SimTalk:** `Periodic`

### Period Length

Type the duration of a Trigger's cycle during the simulation run. When **Repeat Periodically** is selected, the Trigger repeats the values after a completed cycle.

**SimTalk:** `PeriodLength`

---

## Tab Values

### Trigger Type

Select the Trigger Type — they differ in the way they generate events:

- **Input Trigger** — takes the values from a single TimeSequence. Click **Values** and type values into the Value Table.
- **Combination** — generates a new Trigger by combining existing Triggers. Click **Combination Table** and type the names of the Triggers to combine. The result is saved in the combination list opened by **Values**.

**SimTalk:** `Combination`, `compute`

### Values

Opens the TimeSequence containing the current sequence of values of the Trigger. Type the default value on the tab **Start Values > Default Value**. Alternatively, right-click the Trigger object and select **Open Values Table**.

**SimTalk:** `ValueTable`

### Combination Table

Opens the Combination Table. Type the Trigger objects to combine into the cells:

- **Time Sequence** column — name of a TimeSequence (accessible in the connection Formula with this name). Click an entry to open its value list.
- **Origin** column — path to the source Trigger.
- **Start Time** column — when the Trigger starts working.
- **Count** column — how often the Trigger repeats.
- **End Time** column — when the Trigger stops working, independently of repeated patterns. If no value is specified, no end time applies.

**SimTalk:** `CombinationTable`, `compute`

### Formula

For the Combination Trigger, type a formula that computes the Trigger's value pattern. The formula connects the Trigger objects typed into the Combination Table. Allowed operations depend on the data type:

- `boolean` TimeSequence — operators `AND`, `OR`, `NOT`.
- numerical TimeSequence — operators `+`, `-`, `*`, `/`.

**Example:**

```
TRIGGER AND TRIGGER2 AND TRIGGER3
weeklyPlan AND dailyPlan
employeenum - 2
```

**SimTalk:** `Formula`

---

## Tab Actions

### Attributes

Click **Attributes** below Trigger and type the names of the objects and attributes that the Trigger controls.

**Remarks:** First turn **Inheritance** off, then:

- **Object** column — name of the object the Trigger controls.
- **Attribute** column — name of the attribute as a string. For a `Variable` object you do not need an attribute; the Trigger passes the current value directly.
- When an error occurs in the value assignment, Plant Simulation inserts the error message in the **Error Message** column.

**SimTalk:** `insertTriggeredAttr`, `deleteTriggeredAttr`

### Methods

Click **Methods** below Trigger to open a list. First turn **Inheritance** off. Type the names of the methods the Trigger controls — Plant Simulation calls a different Method whenever a Trigger value changes, passing the previous and current trigger values as parameters.

**SimTalk:** `insertTriggeredMeth`, `deleteTriggeredMeth`

### Objects

Opens a list containing the Source that creates the parts. The list shows the name of and path to the Source object, which Plant Simulation inserted when you selected **Time of creation > Trigger** in the Source dialog, clicked Trigger, typed the Trigger name, and clicked OK/Apply. This table cannot be edited.

---

## Tab Representation

Defines the **Value Pattern** and the **Time Unit** used to show the values over time.

### Value Pattern

Shows the value pattern over time in an x-y diagram (white background). You can also select the Time unit.

### Time Unit

Select a Time Unit to scale the time axis: **Second**, **Minute**, **Hour**, **Day**.

---

## Menus

- **Navigate Menu** — commands described under the Navigate Menu.
- **View Menu** — `Refresh`, `Show Attributes and Methods`. **SimTalk:** `updateDialog`
- **Tools Menu** — `Edit Controls`, `Edit Observers`.
- **Help Menu** — commands described under the Help Menu.

---

## Methods of the Trigger

The Trigger provides the methods listed in the table of contents plus the **Methods of All Objects**. To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods**:

- In the Class Library context menu, select **Show Attributes and Methods** to show the selected Class.
- Press `F8` or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show the selected Instance.
