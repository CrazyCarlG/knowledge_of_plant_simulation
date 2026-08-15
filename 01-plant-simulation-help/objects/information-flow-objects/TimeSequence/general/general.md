# TimeSequence

## Overview

Use the object **TimeSequence** for recording the course that values take over time, such as shift plans, machine maintenance schedules, or buffer occupancies.

The TimeSequence is a table with two columns:

- **Watch mode**: Plant Simulation enters the time-value pairs each time a watchable value changes.
- **Sample mode**: Plant Simulation enters the time-value pairs periodically, during certain time intervals, regardless of whether the value actually changes.

You can use the TimeSequence several times and sort the values to see whether the values are always the same over time or whether they change randomly.

Each entry in the TimeSequence consists of a point in time in the first column and the value associated with that point in time in the second column. Plant Simulation sorts the contents in ascending order. The contents can change dynamically during the simulation run. When you delete a pair of entries contained in a row, Plant Simulation moves the following rows up, so that no blank rows remain.

> **Note**: Although the TimeSequence has two columns, it behaves like a list with one column; it does not allow blank cells or pairs of blank cells.

For the column **Value**, you can select the data types `Boolean`, `Integer`, `Real`, `String`, `Object`, `Time`, `Money`, `Length`, `Weight`, `Speed`, `Date`, and `DateTime`.

The data type of the column **Point in Time** depends on the setting selected under *Start Values > Time Reference* and may take the data types `Time` or `DateTime`.

To show a tooltip with information about the TimeSequence, hover over it with the mouse.

## Setting and Getting Attribute Values

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

To set the value of an attribute:

```simtalk
MyDataStack.MaxDim := -1
MyDataQueue.Alignment := "left"
```

To get the value of an attribute:

```simtalk
print myDataStack.MaxDim
posit := Station.Cont.XPos
```

To show methods, read-only attributes, and attributes:

- Select **Show Attributes and Methods** on the context menu of the Class Library (for a Class).
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance (for an Instance).

## Adding the Object to the Simulation Model

- To change the length of the graphic and the anchor points of the TimeSequence, click **Show Manipulators** on the Edit ribbon tab or press **M**.
- To add the object **TimeSequence** to your simulation model, click **Manage Class Library > Basic Objects > InformationFlow > TimeSequence** on the Home ribbon tab.

## Dialog Box of the TimeSequence

Double-click the icon of the TimeSequence to open its dialog box.

### Edit Simulation Properties
Change the simulation properties of the object in the dialog box. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties
To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M**.

## Menus

### File Menu
The menu commands are described under the **List Ribbon Tab**.

See also: Import File, Export to File [lists], Export Object File, Text File Format, Print List, Print Setup, Close Model.

### Edit Menu
The menu commands are described under the **Home Ribbon Tab** and the **List Ribbon Tab**.

See also: Cut, Copy, Paste Contents of the Clipboard, Delete, Select All, Insert Row, Find, Replace. The context menu of the contents of list objects also provides the most important commands for editing the time sequence.

### Format Menu
The menu commands are described under the **List Ribbon Tab**.

See also: Activate Column Index, Activate Row Index, Inherit Format, Inherit Contents, Inherit Comment.

### Navigate Menu
The commands are described under the **Navigate Menu**.

### View Menu
The commands are described under the **List Ribbon Tab**.

See also: Recompute Formulas, Show Comment, Show Data Type, Highlight Empty Cells, Go To Cell.

### Tools Menu
The Tools Menu provides these commands: **Edit Controls**, **Edit Observers**.

### Help Menu
The commands are described under the **Help Menu**.

## Tab Contents

The TimeSequence shows a table with two columns in which you specify a point in time (time) and the value (string) that trigger an action on the tab **Contents**.

### Sort
To sort the contents of the cells in the time sequence in ascending order, click this button.

### Set Value
To fill blank cells in column 2 with the **Default value** you set, click this button.

SimTalk: `DefaultValue` (see *Default Value*).

## Tab Start Values

Select the settings that determine how Plant Simulation interprets the time and the value column on the tab **Start Values**. You can, for example, easily offset the data of a time sequence here.

### Time Reference
Select whether the time values are **Relative** or **Absolute** values.

Depending on the setting, the data type of column 1 is `time` or `dateTime`. Plant Simulation automatically converts values you specify.

- **Absolute Time Reference**: type a point in time on a certain date (`dateTime`) into the text box *Reference Date*.
- **Relative Time Reference**: type a duration (`time`) into the text box *Reference Time*.

SimTalk: `Absolute` (TimeSequence).

### Reference Time / Reference Date
For *Time Reference > Relative* you define a **Reference Time**. For *Time Reference > Absolute* you define a **Reference Date**.

Plant Simulation adds this value to the time column of the TimeSequence to offset the data you set there. By changing the Reference Time/Date, you can shift the values in time without re-entering the data.

SimTalk: `ReferenceDate` (Trigger), `ReferenceTime` (TimeSequence).

### Default Value
Type in the **Default Value** of the time sequence.

The default value is especially important for a TimeSequence that defines the evolution of the value of a **Trigger** object, because the Trigger takes the default value outside of its active interval.

In addition, Plant Simulation uses the default value to fill blank cells in column 2 of the TimeSequence when you click **Set Value** on the tab **Contents**.

SimTalk: `DefaultValue`.

## Tab Record

Select the settings for the pattern of a value to be recorded while the simulation run progresses on the tab **Record**.

### Value
Type in a relative or an absolute path to the value that the TimeSequence is to record.

When you specify an invalid path, the TimeSequence does not record any data. When you select **Watch** mode, the path must reference a watchable value.

To check which attributes of an object are watchable, select the object and press **F8**. Watchable attributes are marked with an asterisk (`*`) in the column *Watchable* in the window **Show Attributes and Methods**.

Example:

```simtalk
I.building2.entrance.NumMU
frame.variable
ResWorking
```

SimTalk: `Path` (TimeSequence).

### Mode
Select the mode with which the TimeSequence adds new time-value pairs to the columns of the table: **Watch** or **Sample**.

- **Watch** adds a new value each time a watchable value changes. The column *Watchable* in the window **Show Attributes and Methods** shows whether an attribute is watchable or not.
- **Sample** adds a new value periodically during the **Interval** you specify, regardless of whether the value actually changes.

SimTalk: `Sample`.

### Interval
Type the time into the text box that elapses between the points in time at which the TimeSequence records data.

This setting applies for **Sample** mode.

SimTalk: `SmpPeriod` (TimeSequence).

### Active
To record the progression of the values of the TimeSequence, select this check box. To not record any values, clear the check box.

Instead, you can also right-click the TimeSequence object in the Frame and select **Activate** on the context menu. To deactivate it, select **Deactivate** on the context menu.

SimTalk: `Active` (TimeSequence).

## Methods of the TimeSequence

The TimeSequence provides:

- Methods for Columns
- Methods for Rows
- Methods for Accessing the TimeSequence
- The shared Methods of Lists and Tables
- The shared Methods of All Objects

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
