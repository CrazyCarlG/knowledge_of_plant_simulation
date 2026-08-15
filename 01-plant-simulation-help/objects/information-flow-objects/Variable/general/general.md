# Variable [object]

Use the object **Variable** for storing data over an extended period of time.

## Description

The object Variable is a global variable that other objects and methods in Plant Simulation can access during a simulation run. A variable can represent an unknown item which stores a quantity. Variables can change their content, and are also known as placeholders or unknowns. The opposite of a Variable is a constant, whose value is known and does not change.

You might use a Variable to:
- Store data over an extended period of time during a simulation run
- Increment or decrement values
- Assign values

A Variable of data type `list`, `queue`, `stack`, or `table` shows a type graphic to the left of its name when you insert it.

- Double-click the Name of the Variable to open its dialog (or right-click and select **Open** on the context menu).
- Double-click the type graphic of the Variable to open the window of the list object.

In addition, Plant Simulation provides local variables. You have to declare a local variable within the source code before you can use it. A local variable is only known in the Method in which you declare it and will be deleted at the end of the method call.

You can show the contents of a Variable in an HtmlReport (compare **Display a Variable**). To show a tooltip with information about the Variable, hover with the mouse over it. To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Add the Object to the Simulation Model

To add the object Variable to your simulation model, click **Manage Class Library > Basic Objects > InformationFlow > Variable** on the Home ribbon tab.

## Dialog Box of the Variable

Double-click the icon of the Variable to open its dialog box.

- **Edit Simulation Properties** — change the simulation properties of the object (shared properties described under *Dialog Items of the Objects*).
- **Edit Animation Properties** — edit 3D properties via the button **Edit 3D Properties** or by selecting the object and pressing the spacebar.

## Name [text box]

Shows the current name of the Variable, either the built-in name or the name you specify.

Remarks: You can type a combination of letters, digits, and underscore (`_`) characters, e.g. `MyVariable`, `MyVariable1`, `My_Variable_1`. The name of an object cannot start with a digit (e.g. `1Variable` is not allowed).

## Tab Value

### Data Type [Variable]

Select the data type of the Variable from the drop-down list. You can use any of the supported Data Types.

- For a Variable of data type `object`, type the path to and the name of the object into the text box **Value** (the starting point of the relative path is the Frame into which the Variable is inserted), or click the button and select the object in the **Select Object** dialog. You can also drag the object onto the Variable and drop it there — Plant Simulation then inserts a reference to the object.
- To use the data type `time` with a random number distribution, select the data type `randtime` and type in the parameters of the distribution function (the data type `time` only accepts constant values). Then initialize the randtime value before accessing it, e.g. with the method `rollDice`.

Note: For the list data types (`table`, `list`, `stack`, `queue`) you can use the method `unshare`.

For the Data Type `[user-defined attribute] > real, length, weight, time, speed, acceleration` you can type in the number of Decimal Places and Integer Places.

### Value [Variable]

Select or type in the value which the Variable shows. The Data type you select determines what you can do: select from a drop-down list, or type the value in.

Note: For the data types `length`, `weight`, and `speed`, the units selected under **File > Model Settings/Preferences > Units > Mass/Speed/Length** determine how Plant Simulation interprets the value (e.g. a value of `100` with length set to `km` is interpreted as 100 km).

- Click **Open** to open the dialog box of the objects corresponding to the data types `table`, `list`, `stack`, or `queue`.
- If the Variable points to a list referenced from additional places/objects, the dialog shows the button **Unshare**.

**Unshare a Variable:** Click **Unshare** to make Plant Simulation assign its own copy of the list to the Variable instead of the shared contents (corresponds to the method `unshare`).

- Click the button and select the object of data type `object` in the **Select Object** dialog, or type the path to and the name of the object into **Value**.
- `F2` opens the dialog of the object whose name you typed into the text box.

The data type `object` designates an absolute or a relative path to an object:
- The **absolute path** always starts with a period, starting in the Class Library (e.g. `.building`), and identifies the object uniquely. Plant Simulation does not change the absolute path if you derive or insert a Frame using a Variable object — the absolute path still references the source object.
- The **relative path**, which starts with `Location` or `~`, considers the current location of the Variable object each time the object Variable is accessed.

### Inherit Value [Variable]

To inherit the value of the Variable, click the inheritance check box next to **Value** so that it is green. Click it again to not inherit the value.

### Initial Value [Variable]

To reset a value which the Variable recorded during a simulation run to an initial value, select this check box. Plant Simulation sets the value during the reset phase and resets it in the init phase of the next simulation run.

After selecting the check box, a text box appears — type the initial value for the next simulation run.

Note: The Data Types `table`, `list`, `stack`, `queue`, and `randtime` do not provide this feature.

## Tab Display

Select how Plant Simulation shows the global Variable in the Frame window.

### Font Size [drop-down list]

Select the Font Size for displaying the Variable in the Frame. Settings: **Small**, **Medium**, **Large**, **Extra large**.

### Font Color [Variable]

Select the Font Color. You can select a predefined color or click **More Colors** and then **Select** to choose a color in the color matrix.

### Background Color [drop-down list]

Select the color of the background of the Variable. Same predefined / **More Colors** options.

### Alignment [Variable]

Select the Alignment of the display of the Variable with its insertion point:

- **Left** — aligns the Variable with the left border of the type graphic.
- **Name** — places the left border of the displayed Name or Value on the insertion point.
- **Value** — places the right border of the displayed Name or the left border of the displayed Value on the insertion point.
- **Right** — places the right border of the displayed Name or Value on the insertion point.

### Integer Places [text box]

Type the number of Integer Places which the Variable shows. It can show up to 15 integer places. Default `-1` means no minimum. A positive value fills up the space before the decimal point with blank spaces in 3D.

Note: Only applies to the Data Type `[user-defined attribute] > real, length, weight, time, speed, acceleration`.

### Decimal Places [text box]

Type the number of Decimal Places which the Variable shows (up to 15). Default `-1` shows all existing places.

Note: Only applies to `Data Type > real, length, money, weight, time, speed, acceleration`. For `time`, `-1` means the default time display format with four decimal places; a positive value shows at most that many decimal places.

### Transparent [check box]

Select to make the background of the Variable transparent (shows the Frame background color). Clear to show the space around the text in white.

### Show Data Type [Variable]

Select to show the data type in addition to the name and value of the Variable. Clear to hide.

### Show Units [Variable]

Select to show the unit of the physical size of the Variable (unit selected under **File > Model Settings/Preferences > Units**). For `randtime`, **Show Units** also sets whether Plant Simulation shows the distribution parameters. If you clear **Show Units**, you can type in the number of Decimal Places.

## Tab Statistics

The tab shows the top five frequencies and the top five durations. Only Variables of Data type `string` or `integer` record statistics values.

### Active [check box] — statistics

Select to collect statistics data during a simulation run and show the **Top 5 Frequencies** and **Top 5 Durations**. Only Variables of type `string` or `integer` record statistics values, and only if they exist for a time span greater than zero.

Example — a Variable of type `integer` with Initial Value `0`:

```simtalk
Variable = 1
wait 1
Variable = 2
wait 1
Variable = 1
Variable = 3
wait 1
```

The Frequency of `1`, `2`, and `3` is `1` each (the second assignment of `1` was only present for a time span of 0). The Initial Value of `0` is not recorded (present for a time span of 0). The Durations of `1`, `2`, and `3` are therefore `33.33%` each.

### Statistics Table [Variable]

Click to open the statistics table. It shows these values:

| Item | Description |
| --- | --- |
| Value | Shows the name of the value of the Variable. |
| Frequency | Number of occurrences of the value (only counts when the value actually changes). |
| Duration | Complete duration the Value had during the collection period. |
| Frequency [%] | Portion of the individual frequencies to the sum of all values in Frequency. |
| Duration [%] | Portion of the individual durations to the sum of all values in Duration. |
| Mean Duration | Mean duration of the individual durations. |
| Standard Deviation | Standard deviation of the duration. |

### Charts [Variable]

Click to open a pie chart showing the frequency and duration of the value.

### Frequency Histogram [Variable]

Click to open a histogram showing the frequency (number of occurrences) of the value.

## Tab Comment [Variable]

Type any comment describing the function of the Variable. First click the check box to turn Inheritance off, then enter data. The comment shows as a tooltip when you drag the mouse over the object (with the line breaks you manually specify by pressing Enter).

## Menus

- **Navigate Menu** — commands described under the Navigate Menu.
- **View Menu** — `Refresh`, `Show Attributes and Methods` (SimTalk: `updateDialog`).
- **Tools Menu** — `Edit Controls`, `Edit Observers`.
- **Help Menu** — commands described under the Help Menu.

## Assigning a Value to a Variable

When assigning a new value, it has to be compatible with the active data type. A value is compatible if Plant Simulation can automatically transform it into a correct value. A change of value may occur because:

- Plant Simulation cannot display digits after the decimal point and cuts them off (e.g. real value `3.9` → integer value `3`).
- Loss of significance occurs for great value differences (floating point only saves a certain number of digits; this error cannot be avoided and only occurs if the difference in size is at least `10⁷`).

If you assign a Variable to a Method, Plant Simulation calls and executes the Method if you only type in its name. Use the reference operator `&` to get the required reference to a Variable of data type `object`.

Syntax:

```simtalk
Path := any
```

Example:

```simtalk
Variable := Value
Variable := &MyMethod
```

## Calling the Contents of a Variable

If the contents of the Variable references another Variable of data type `object`, access the contents by typing the name of this Variable in parentheses. If it references a Method, typing the Method in parentheses calls the Method itself.

Syntax:

```simtalk
(Path)
```

Example:

```simtalk
value := (Variable) + 1   -- accesses the variable
(control_gate)            -- calls the method
(method)(3.4,"drill")     -- calls the method with parameters
```

## Reading the Contents of a Variable

To access the contents of the Variable designated by `<Path>`, use its name.

Syntax:

```simtalk
<Path>
```

Example:

```simtalk
MyTable[1,1] := MyVariable
```

## Methods of the Variable

The object Variable provides the methods listed in the table of contents, plus the Methods of All Objects.

Note: You can only access the methods of the object Variable that refer to the object itself via the reference operator `&`. Without the operator the method is applied to the contents of the Variable.

Example:

```simtalk
.MyPlant.&MyVariable.openDialog
```

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
