# Method [object] — General

This topic describes the **Method** object itself; the SimTalk programming language is covered in the *SimTalk Reference*.

## Description

You build your own routines using a combination of **built-in methods**, **keywords**, **assignments**, and **control structures** in the Method. You can also check whether one of the built-in **Templates** meets your needs, or write your own templates for yourself and colleagues.

Key points:

- You can modify the behavior of an object by writing **user-defined methods**.
- The built-in properties, the large number of built-in methods, and the **inheritance strategies** help build valid models quickly.
- The **Copilot** can assist you in writing source code in a Method.
- Method functions are available on the **Edit Ribbon Tab** and **Tools Ribbon Tab**.
- Method Editor preferences: **File > Preferences > Editor**.
- Settings applied when calling Methods during simulation runs: **File > Model Settings/Preferences > Simulation > Methods**.
- The Method and user-defined attributes of data type `Method` have their own **random number stream** set via the attribute `RandomSeed`. Plant Simulation automatically assigns a stream when inserting an object (as with material flow objects).
- You can show a Method's return value in an **HtmlReport**.
- Hover over the Method to show a tooltip (user-defined attribute, source code comment, or "Suspended Method").
- Use the **Profiler** to record run-times and call frequency of Methods to detect performance bottlenecks.
- To change the graphic length/anchor points: click **Show Manipulators** on the Edit ribbon tab or press **M**.

### Adding the Object to the Model

Click **Manage Class Library > Basic Objects > InformationFlow > Method** on the Home ribbon tab.

## Programming a Method

The Method is the container for program routines. Double-click its icon in the Frame to open it and type source code.

The structure of a Method is divided into several parts; you can delete or omit unneeded parts. A Method used as an **Exit Control** could look like this:

```simtalk
// My Tooltip. My text, my text, my text, ...
param Sender:object
if Sender /= void
   @.move(Sender)
   return
end
var MUName:string := @.Name
if MUName = "A"
   @.move(1) // parts named 'A' will be moved to the first successor
else
   @.move(2) // parts named 'B' will be moved to the second successor
end
```

Plant Simulation highlights the different parts of the SimTalk syntax in different colors.

### Parts of a Method

1. **Parameters** — the structure begins with the `param` keyword. Omit if not needed.
2. **Return Value** — type the data type of the return value if the Method returns a result.
3. **Local Variables** — declare a local variable by name and data type. Omit if not needed.
4. **Source Code** — the code the Method executes: built-in methods, assignments, control structures, method calls, branches, and loops.

Comments are typed with two forward slashes `//` or two hyphens `--`.

Notes:

- SimTalk normally does **not** distinguish upper-/lower-casing for method, attribute, and read-only attribute names.
- Click **Edit > Reformat** to check branching/looping syntax.

## Working in the Method Window

Double-click the Method's icon to open its window, then type, run, and debug source code. The window provides access to the **Method Editor** and **Method Debugger**.

- Click **Debug** on the Tools ribbon tab or press **F11** to switch to the Method Debugger.
- Click any **Step** button on the debugger toolbar to return to the Method Editor.
- Double-click to select a word; triple-click to select an entire line.
- **Ctrl+A** (or click four times) to select all; **Ctrl+C** copy; **Ctrl+V** paste.
- Copied source code is placed on the clipboard as **RTF text** (plus plain text), so it pastes with SimTalk color highlighting into suitable programs (e.g., MS Word).
- Class breakpoints are copied along with the source code. Class breakpoints from a Method's class are applied when inserting an instance.
- **Export to File** lets you select the text format; choose **HTML Files** or **RichText Files** to preserve color highlighting.
- Drag-and-drop to move selected text; **Ctrl+Z** undo; **Ctrl+Y** redo.
- Insert a line break with a backslash `\` for long source lines (still interpreted as a single entity):

```simtalk
priority:= "Urgent"
very_long_text := "Frank Jones\
                   Halford Lane 9\
                   Cedar Rapids, IA 52409"
Text := "It is \"very\" urgent." // outputs It is "very" urgent.
```

### Comments

- One-line comment: two forward slashes `//` (ends at end of line).
- Multi-line comment: `/* ... */`.
- Comments display in green; they do not affect simulation speed.
- You cannot place a comment inside a string value (within quotation marks).

```simtalk
// comment to the end of the line
price := price * 1.16 // value added tax
/* start of the comment block
   covering several lines
end of the comment block */
```

### Breakpoints (in the Method window)

- **Class breakpoints**: middle mouse button / mouse wheel click in the row markers area.
- **Instance breakpoints**: hold **Shift** + middle mouse button / mouse wheel.
- Activate the breakpoint in a line: hold **Ctrl** + middle click, or press **Ctrl+F9**.
- Open **Breakpoint Settings**: **Ctrl+B**.
- Hover over a breakpoint for a tooltip (always shows if inactive; shows Start Time and Condition if configured).

Breakpoint symbols:

| Symbol | Description |
| --- | --- |
| (filled) | Active class breakpoint |
| (unfilled) | Non-active class breakpoint |
| (filled) | Active instance breakpoint |
| (unfilled) | Non-active instance breakpoint |

### Other shortcuts

- Horizontal scroll: hold **Shift** + roll mouse wheel.
- Run Method: **F5** (or click Run Method); Debug Method: **F11**.
- Font size: hold **Ctrl** + roll mouse wheel (applies to all open Method windows). Alternatives: **Ctrl + +** (increase), **Ctrl + 0** (reset to 10 pt), **Ctrl + -** (decrease).
- Select line numbers, keyword highlighting, and indentation on the **Edit/Tools Ribbon Tabs**.
- Global SimTalk display settings: **File > Preferences > Editor**.
- An asterisk `*` in the title bar indicates unapplied changes; click **Apply changes** on the Edit ribbon tab.

## Calling a Method

A Method can be called:

- **Directly** by clicking **Run** on the Tools ribbon tab (apply changes first). Pressing **F5** then **F7** does the same. If parameters are expected, Plant Simulation opens the Debugger to enter them (mainly used during development).
- **From a control** within another object (e.g., an Entrance Control in a Track triggers a Method when an MU enters).
- **From another Method** (requires the Method's name; if in a different namespace, include the path).
- **From the EventController** via `&method.executeIn(time)` — starts the Method after the given seconds have elapsed.
- **By calling a reference**: if a variable of data type `object` holds a Method reference, use `&Variable.execute`.

Example:

```simtalk
Method1                  // same namespace
root.Frame2.Method1      // path and name
&Method1.executeIn(8.5)  // pass to EventController, execute Method1 after 8.5 seconds
Variable.execute         // call the referenced Method; Variable has data type object
```

## Colors for Syntax Highlighting

| Color | Description |
| --- | --- |
| Black | Normal source code |
| Medium green | Comment |
| Medium blue | SimTalk function |
| Purple | SimTalk keyword |
| Brown | String value |
| Medium red | Outdated function (no longer supported) |
| Gray blue | Deprecated function (outdated; supported for backward compatibility) |
| Red | Template argument to replace in the Method template |

## Working with Breakpoints

Use the Tools ribbon tab buttons or context menu commands:

- **Class breakpoint**: middle mouse button/wheel click in row markers area. Delete all: **Delete All Class Breakpoints**.
- **Instance breakpoint**: hold **Shift** + middle click. Delete all: **Delete All Instance Breakpoints**.
- Activate breakpoint in a line: hold **Ctrl** + middle click, or **Ctrl+F9**.
- Open **Breakpoint Settings**: **Ctrl+B**.
- Hover over a breakpoint for a tooltip (shows if inactive; shows Start Time and Condition if configured).

## States of the Method

During simulation, colored rectangles along the upper border of the Method's picture indicate its state:

| Description | Rectangle color |
| --- | --- |
| Source code contains syntax errors | Red |
| Source code is being executed | Green |
| Suspended by `stopuntil` or `waituntil` | Purple |
| Suspended by `wait` | Blue |
| Source code is encrypted | Dark gray |
| Source code is inherited | Dark green |

## The Method Editor

Double-click the Method icon to open its window. To change the properties of the **Class** [general description], double-click it in the Class Library or on the **Information Flow** tab in the Toolbox. It provides access to the Method Editor and Method Debugger.

To edit 3D properties, select the object and press the **spacebar**, then change settings in the **Edit 3D Properties** dialog.

### Edit Ribbon Tab [Method]

The Edit ribbon tab provides commands for editing the Method's source code.

## See also

- Programming a Method
- Working in the Method Window
- Calling a Method
- Colors for Syntax Highlighting
- Working with Breakpoints
- States of the Method
- The Method Editor
- Method Debugger
- Edit Ribbon Tab [Method]
- Tools Ribbon Tab
- Context Menu of the Method
- Drag-and-Drop in the Method Editor
