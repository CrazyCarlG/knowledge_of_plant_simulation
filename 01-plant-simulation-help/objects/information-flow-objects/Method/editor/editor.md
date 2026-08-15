# Method Editor

To edit the 3D properties of an object in the 3D model, select the object and press the spacebar, then change the respective settings in the dialog box **Edit 3D Properties**.

## Related Topics

- Edit Ribbon Tab [Method]
- Tools Ribbon Tab
- Context Menu of the Method
- Drag-and-Drop in the Method Editor
- Method Debugger
- Programming a Method
- Working in the Method Window
- Colors for Syntax Highlighting

---

# Edit Ribbon Tab [Method]

The **Edit** ribbon tab provides commands for editing the source code of your Method.

## Commands

| Command | SimTalk |
|---|---|
| Import from File | `load [SimTalk] - source code` |
| Export to File | `[source code]` |
| Print | `[source code]` |
| Find Text | `[in Method]` |
| Find Previous | `[source code]` |
| Find Next | `[source code]` |
| Incremental Search | — |
| Undo | `[source code]` |
| Redo | `[source code]` |
| Auto Complete | — |
| Toggle Comment | — |
| Increase Indent | — |
| Decrease Indent | — |
| Reformat Selection | — |
| Move Up | `[source code]` |
| Move Down | `[source code]` |
| Line Operations | — |
| Select Template | — |
| Insert Control Structure | `if-else`, `if-else-end`, `if-elseif-end`, `switch-case-end`, `switch-case-else-end`, `while-end`, `repeat-until`, `for-next` |
| Inherit Source Code | `getAttribute [SimTalk] - object` |
| Apply Changes | `[source code]` |
| Help on Word | — |

> **Note:** The other tabs on the Ribbon Bar provide additional commands pertaining to the Method.

---

## Import from File

Imports source code from a text file. Opens the dialog **Open**. Select the text file that contains the source code you would like to import into the active Method and click **OK**.

**SimTalk:** `load [SimTalk] - source code`

---

## Export to File [source code]

Exports the source code to a file. Opens the dialog **Save As**. Select the folder, type in the file name, select the file type, and click **OK**.

**Remarks**
- To save color highlighting of keywords and comments, select **HTML Files** or **RichText Files**.
- Plant Simulation adds a comment before the source code proper with the path of the Method, so you can always tell which text file belongs to which source code.

**SimTalk:** `writeStringToFile [SimTalk]`

---

## Print [source code]

Opens the dialog **Print**. Select the settings for printing the source code of the Method and print it by clicking **OK**.

---

## Find Text [in Method]

Opens the dialog **Find**. With its settings you can find expressions in your source code and replace them if necessary.

**Remarks**
- You can select text in your source code and temporarily mark it by pressing `Ctrl+F2`. To delete the selection, mark it again and press `Ctrl+F2`, or click **Clear Bookmarks** on the Tools ribbon tab.
- If you select text with `Shift` + arrow keys or the mouse pointer, Plant Simulation highlights all occurrences of this text fragment in color. Jump to these occurrences like bookmarks by clicking the respective buttons or pressing `F2`.
- Plant Simulation does not differentiate between upper- and lower-casing. Find Text searches for:
  - Whole words, except when the selected text contains blank spaces, tabulators, or line breaks.
  - Entire rows.
  - Line comments starting at the character you typed (`--` or `//`).
  - Text which starts or ends with SimTalk-syntax-specific characters, such as `(`, `[`, `"`, `)`, `]`, `;`, etc.
- Moving the text cursor deletes or changes highlighting.

### Find What
Type the expression you want to find into the text box **Find What**.

### Regular Expressions
To use regular expressions in your search, click the button with the arrow pointing right. This opens the window **Regular Expression**.

| Select | To enter and to find |
|---|---|
| Any single character | `.` |
| Beginning of line | `^` |
| End of line | `$` |
| Beginning of word | `\<` |
| End of word | `\>` |
| Group | `\(\)` |
| Zero or one matches | `?` |
| Zero or more matches | `*` |
| One or more matches | `+` |
| Any one character in the set | `[ ]` |
| Any one character not in the set | `[^]` |
| Or | `\|` |

Plant Simulation only finds a search term with a regular expression if you select the check box **Regular Expression**.

### Replace With
Type the expression that replaces the search term typed into the text box **Find What**.

### Match Whole Word Only
To only find whole words instead of searching for the expression inside longer words, select the check box.

### Match Case
To only find text with the same upper/lower case pattern as the expression in **Find What**, select the check box.

### Regular Expression
To use regular expressions in your search, select the check box.

### Direction [in Search]
Select the direction in which Plant Simulation searches through the source code:
- **Up** — search toward the beginning of the Method.
- **Down** — search toward the end of the Method.

> `Shift+Ctrl+F3` searches for the next occurrence upward; `Ctrl+F3` searches for the next occurrence downward.

### Find Next [source code]
Finds the next instance of the expression in **Find What** and selects it in the source code.

### Replace [source code]
Replaces the expression from **Find What** with the expression in **Replace With**, then searches for the next occurrence and stops there.

### Mark All
Highlights all instances of the expression in **Find What**. Use the Tools ribbon tab commands (Toggle Bookmarks, Clear All Bookmarks, Next Bookmark, Previous Bookmark) to act on them.

### Replace All
Replaces all instances of the expression from **Find What** with the expression in **Replace With**.

### Find Previous [source code]
Finds and highlights the previous occurrence of the search term in **Find What**.

### Find Next [source code]
Finds and highlights the next instance of the expression in **Find What** starting at the cursor position.

---

## Incremental Search

Finds the expression which you start typing. Plant Simulation highlights the character combination while you type.

- If you mistype a word, delete the last character with `Backspace`, then type the correct character.
- Press `F3` to find the next instance.
- Press `Esc` to terminate Incremental Search.

**Incremental Search for Workers:** Incremental Search also finds Workers located on Workplaces, FootPaths, and on their way to the WorkerPool (but not Workers in the WorkerPool). For Workers it also includes the class name and instance counter (e.g., `Worker:1` finds the first instance of the class `Worker`).

---

## Undo [source code]

Undoes the last change made to the source code.

## Redo [source code]

Redoes all changes made with an undo action.

---

## Auto Complete

Automatic data entry: type the first letter(s) of an attribute/read-only attribute/method name, then press `Ctrl+Spacebar` or `Shift+Ctrl+Spacebar`, or click **Auto Complete**.

When the name is no longer unique, Plant Simulation opens a window to select an attribute/read-only attribute/method. Double-click or use up/down keys and press `Enter`. Plant Simulation completes the name and adds the corresponding characters — period, opening parenthesis, assignment operator (`:=`), and closing parenthesis — if necessary.

You can filter attributes/methods according to the same criteria as in the window **Show Attributes and Methods**:

| To do this | Click |
|---|---|
| Show Attributes/Methods for Standard Users | — |
| Show Attributes/Methods for Expert Users | — |
| Show General Attributes/Methods | — |
| Show User Interface/Animation Attributes/Methods | — |
| Show Control Attributes/Methods | — |
| Show Simulation Attributes/Methods | — |
| Show Energy related Attributes/Methods | — |
| Show 3D Attributes and Methods | — |
| Show Statistics Attributes/Methods | — |
| Show Attributes (built-in attributes, local variables, objects of type Variable) | — |
| Show Read-Only Attributes (no parameters, no side effects, return a value) | — |
| Show Methods (built-in methods, user-defined attributes of type method, objects of type Variable) | — |
| Show Global Functions (global functions and constants) | — |
| Show Objects (objects in the Frame, objects of type Variable and Method) | — |
| Show Keywords | — |

If you insert a function or Method with parameters, Plant Simulation shows the status bar with the signature to make typing parameters easier. It hides the status bar when you type the closing parenthesis or press `Esc`.

**See also:** Show Completion Tooltip [preferences]; Video on YouTube: https://youtu.be/MXDcx2yplxc?si=NS9lkfDV2ERnn83N&t=457

---

## Toggle Comment

Changes the current line or selection into a comment or into normal source code and vice versa.

**Video:** https://youtu.be/MXDcx2yplxc?si=pS2IRdpKXzPBWu0u&t=560

---

## Increase Indent / Decrease Indent

Moves the selected range of source code one tab length to the right (Increase) or left (Decrease).

Select the tab size under **File > Preferences > Editor > Text settings > Tab Size**.

---

## Reformat Selection

Automatically indents the selected source code according to the tab settings to show the Method's structure more clearly. Reformatting automatically indents all rows inside an `if-else-end` block, for example.

To reformat the entire source code, click anywhere within it and select **Reformat Selection**.

> **Note:** Not available in SimTalk Version 1.0.

---

## Move Up / Move Down [source code]

Moves the selected line(s) of source code up or down one line.

---

## Line Operations

Provides subcommands for manipulating lines of source code:
- **Duplicate Line** — duplicates the selected line(s).
- **Delete Line** — deletes the selected line(s).
- **Copy Line** — copies the selected line(s).
- **Cut Line** — cuts the selected line(s).

---

## Select Template

Opens a dialog to select one of the provided templates for commonly used tasks.

**Proceed as follows:**
1. Select the **Category** of template in the left list box.
2. Select the **Template** in the middle list box.
3. View the description of the selected category in the right text box.
4. Click **OK** to insert the template into your source code.

Select the **Template Directory** under **Preferences > Editor**. See "Create Your Own Method Templates" to add your own templates.

**SimTalk:** `setErrorHandler [SimTalk]`

---

### Create Your Own Method Templates

Create a method template in a text editor and save it as a text file (`*.txt`).

**Syntax:**
- Create the file in the subfolder `C:\Program Files\Siemens\Plant Simulation XX\Templates\English\Name_of_Your_Category`. The dialog **Select Template** shows this name below **Select the Category**.
- Type two hyphens `--` followed by the key combination to set one.
- Type two hyphens `--` and the name of the template (shown below **Select the Template**).
- Type two hyphens `--` and a description (shown in the rightmost field).
- Type `/*` then the comment the template shows after loading, closed with `*/`.
- Type the variable to use and any comment.
- Type the item the user should replace within left/right double angle quotation marks, e.g. `«attribute»=«value»`.
- Add a Tooltip: start with `/*` followed by the search term in double angle quotes, finish with `§§*/`.
- Type the key combination to insert the code snippet.

To insert the snippet, if the key combination is `Ctrl+T C`: hold `Ctrl`, press `T`, release `Ctrl`, then type `C`.

**Example** — processing time depending on an attribute of the part:

```
-- Determines the processing time of a station in a formula
-- according to an attribute of the MU.
-- @ is the MU that triggers the formula
-- ? is the station calling this method
->time
if @.«attribute»=«value» 
   result:=«time»
   -- add your code here
elseif @.«attribute»=«value»
   result:=«time»
   -- add your code here
else
   -- add your code here
end
```

> **Note:** Compare any of the method templates that are part of your program package.

---

## Insert Control Structure

Provides subcommands for inserting control structure statements into the source code.

```
if-else              while-end
if-else-end          repeat-until
if-elseif-end        for-next
switch-case-end      for-downto-next
switch-case-else-end
```

> The control structures create ready-made SimTalk source code.
> **Note:** Not available in SimTalk Version 1.0.

For each control structure (`if-else`, `if-else-end`, `if-elseif-end`, `switch-case-end`, `switch-case-else-end`, `while-end`, `repeat-until`, `for-next`, `for-downto-next`):
- Inserts the statement at the cursor position.
- Type the condition, then press `Tab` to jump to where the executed statement goes.
- You can highlight several statements first; Plant Simulation then inserts the structure around them.
- Drag the mouse over red-marked sections to show a Tooltip.

---

## Inherit Source Code

Turns inheritance of the source code of a Method object inserted into a Frame off or on.

As long as inheritance is on, you cannot modify the source code; the Method uses the source code of the Method from which it is derived (its origin). Click **Inherit Source Code** to turn it off and edit the source code.

**SimTalk:** `getAttribute [SimTalk] - object`

---

## Apply Changes [source code]

Applies any changes made to the source code and leaves the dialog box open.

## Help on Word

Opens the help topic for the highlighted word you double-clicked or in front of which the input cursor is placed. Provides quick help for instructions, built-in attributes/read-only attributes/methods/functions.

---

# Tools Ribbon Tab

The **Tools** ribbon tab provides commands for working with the source code of your Method.

## Commands

| Command | SimTalk |
|---|---|
| Run | `execute [SimTalk] - Method` |
| Debug Method | `debug [SimTalk]` |
| Toggle Bookmarks | — |
| Clear All Bookmarks | — |
| Previous Bookmark | — |
| Next Bookmark | — |
| Toggle Class Breakpoint | — |
| Toggle Instance Breakpoint | — |
| Delete All Class Breakpoints | — |
| Delete All Instance Breakpoints | — |
| Delete All Breakpoints | — |
| Previous Breakpoint | — |
| Next Breakpoint | — |
| Toggle Outline | — |
| Previous Outline | — |
| Next Outline | — |
| Collapse All Outlines | — |
| Expand All Outlines | — |
| Hide/Unhide Text | — |
| Encrypt Method | `encrypt [SimTalk]` |
| Decrypt Method | `decrypt [SimTalk]` |
| New Syntax | `UsingNewSyntax [SimTalk]` |
| Syntax-controlled Indentation | — |
| Show Line Numbers | — |
| View (Show Outlining, Highlight Current Line, Show Completion Tooltip) | — |

> **Note:** Some settings can also be selected under **File Menu > Preferences > Editor** (apply to all new Methods). Settings on the Tools ribbon tab only apply to the open Method.

---

## Run [button] - Method

Runs the entire Method, executing the entire source code. You can also right-click the Method and select **Run**.

**SimTalk:** `execute [SimTalk] - Method`

## Debug Method [button]

Runs the Method one step at a time in the Debugger.

- Opens the Method Debugger where you can step through using **Step Into** or **Step Over**. Same as running the Method while holding `Ctrl+Alt+Shift`.
- If stuck in an endless loop (foreground): hold `Ctrl+Alt+Shift` left keys for 5 seconds to open the Method Debugger.
- If not in foreground: hold `Ctrl+Alt+Shift` right keys for 5 seconds.

**SimTalk:** `debug [SimTalk]`

---

## Bookmarks

- **Toggle Bookmarks** — adds a bookmark for the current row/selected range (highlighted in the bar to the left).
- **Clear All Bookmarks** — deletes all bookmarks.
- **Previous Bookmark** / **Next Bookmark** — go to the previous/next bookmark.

Temporary bookmarks (e.g., after changing source code beyond the original end) are marked brighter than saved bookmarks and are lost if you do not apply the source code.

---

## Breakpoints

- **Toggle Class Breakpoint** — adds/deletes a breakpoint for all instances sharing the source code of this class. Set with `F9`. Designated by a filled red circle.
- **Toggle Instance Breakpoint** — adds/deletes a breakpoint for this instance only. Set with `Shift+F9`. Designated by a red star.
- If both a class and instance breakpoint are in the same line, the Method shows a white star within a red circle.
- When the Method reaches a breakpoint, the Method Debugger opens and highlights the line in yellow; you can inspect/modify local variables and parameters.
- To activate all breakpoints in a line, hold `Ctrl` and double-click a breakpoint.
- To open the **Breakpoint Settings** dialog, hold `Shift` + `Ctrl` and double-click a breakpoint.
- To activate/deactivate Instance Breakpoints, hold `Shift` and click in the row marker/breakpoint area.
- **Delete All Class Breakpoints** / **Delete All Instance Breakpoints** / **Delete All Breakpoints** — delete the respective breakpoints.
- **Previous Breakpoint** / **Next Breakpoint** — go to the previous/next breakpoint.
- You can set breakpoints for an encrypted method; the Method then stops during execution in the Debugger, and shows the breakpoint left of "Source code is encrypted".

---

## Outlining

- **Toggle Outline** — switches the collapsed/uncollapsed state of the outline at the cursor.
- **Previous Outline** / **Next Outline** — go to the previous/next outline (outlines have a `+` sign in front of a line).
- **Collapse All Outlines** / **Expand All Outlines** — collapse/expand all outlines.
- **Hide/Unhide Text** — creates an outline from the selected source code or deletes an existing outline.

---

## Encrypt Method / Decrypt Method

- **Encrypt Method** — encrypts the source code to prevent unauthorized access. Type the password into **Password** and **Confirm Password**. After clicking OK, the source code cannot be accessed without the password. Once encrypted, the command changes to **Decrypt**. You can encrypt all Methods in the model via **File > Options > Encrypt Methods**.
- **Decrypt Method** — decrypts the encrypted source code using the correct password. You can decrypt the entire model via **File > Options > Decrypt Methods**.

**SimTalk:** `encrypt [SimTalk]`, `decrypt [SimTalk]`

---

## New Syntax [command]

Activates **SimTalk 2.0** syntax (the improved, abbreviated notation).

- To use SimTalk 2.0 for all new Methods, activate New Syntax in the Method class in the Class Library.
- Clicking New Syntax on an existing SimTalk 1.0 Method automatically converts its source code to SimTalk 2.0 notation.
- The New Syntax setting is written to the model file.
- To convert all existing Methods: hold `Shift`, right-click the object **Basis** in the Class Library, and click **Convert all Methods to New Syntax**.

**SimTalk:** `UsingNewSyntax [SimTalk]`

---

## Syntax-controlled Indentation [Tools ribbon]

Activates/deactivates indentation according to the predefined SimTalk syntax. When active, Plant Simulation automatically indents the cursor at a new line according to delimiting keywords (e.g., text between `if` and `end`). The change applies for the entire session to all newly opened Methods.

> **Note:** Not available in SimTalk Version 1.0.

---

## Show Line Numbers [Tools ribbon]

Shows or hides line numbers to the left of the rows of source code. The change applies for the entire session to all newly opened Methods.

---

# View [Method]

The **View** submenu sets what Plant Simulation shows in the Frame window. Settings here override those under **File > Preferences > Editor**. A check mark indicates an active command. Changes apply for the entire session to all newly opened Methods.

- **Show Outlining [Method]** — shows outlining of control/loop structures as expandable/collapsible structures.
  > Not available in SimTalk Version 1.0.
- **Highlight Current Line [source code]** — highlights (or not) the current line.
- **Show Completion Tooltip [command]** — shows a Tooltip when Auto Complete reaches a point where the name is unique, so you can press `Ctrl+Spacebar` without typing many letters.

---

# Context Menu of the Method

The context menu (right mouse button) provides the most important commands for the Method. Some commands are on the mini toolbar; others on the context menu itself. Close the context menu while leaving the mini toolbar open by clicking the border of the mini toolbar with the left mouse button.

| Command | Button |
|---|---|
| Open Location | — |
| Open Origin | — |
| Open Class | — |
| Copy Objects | — |
| Cut Objects | — |
| Paste Objects | — |
| Delete Objects | — |
| Inherit Source Code | — |
| Apply Changes | — |
| Toggle Class Breakpoint | — |
| Toggle Instance Breakpoint | — |
| Open Object | — |
| Show Object | — |
| Run | — |
| Debug | — |
| Insert Control Structure | — |

---

# Drag-and-Drop in the Method Editor

Drag-and-drop in the Method Editor performs a number of actions. Hold down the keys described below.

| To do this | Drag from | To | Type | Accelerator |
|---|---|---|---|---|
| Move the selected text | text window | text window | text | none |
| Copy the selected text | text window | text window | text | Ctrl |
| Insert the selected text | any | text window | text | any |
| Copy the selected text | text window | any | text | Ctrl |
| Cut the selected text | text window | any | text | none |
| Pass the dropped objects as a parameter of data type array to the Method | Frame window | Method | object | none |

## Multiple Drag and Drop with SimTalk

An example of multiple drag-and-drop with SimTalk:

```simtalk
param a: object[]
for var i := 1 to a.Dim 
   print "i=", i, " : ", a[i]
next 
```

If we select the objects `Station`, `Station1`, and `ParallelStation` in the Frame window, drag them onto the icon of the Method and drop them there, the Console shows:

```
i=1 : .Models.Model.Station
i=2 : .Models.Model.ParallelStation
i=3 : .Models.Model.Station1
```

---

# Method Debugger

Debug the source code written in the Method Editor in the Method Debugger while the Method is being executed.

**To open the Method Debugger:**
- Press `F11` in the Method Editor window.
- Select **Debug Method** on the Tools Ribbon Tab.

> If Plant Simulation is stuck in an endless loop (foreground), hold `Ctrl+Alt+left Shift` for several seconds; if not in foreground, hold `Ctrl+Alt+right Shift`.

Plant Simulation opens the Debugger automatically when it encounters an error while executing the source code or when it hits a breakpoint.
