# The Method Debugger

Debug the source code you wrote in the Method Editor while the Method is being executed.

## Opening the Method Debugger

- Press `F11` in the Method Editor window.
- Select the command **Debug Method** on the Tools Ribbon Tab in the Method Editor window.

> **Note:** If Plant Simulation is running in the foreground and is stuck in an endless loop, hold down `Ctrl+Alt+left Shift` for several seconds to open the Debugger. If Plant Simulation is not running in the foreground, hold down `Ctrl+Alt+right Shift` for several seconds.

> **Note:** Plant Simulation opens the Debugger automatically when it encounters an error while executing source code or when it hits a breakpoint.

## Debugger Window

The Debugger window shows source code with the parameters and local variables of the Method. You can set breakpoints at critical points and check each step of Method execution.

### Breakpoints

- Press `F9` (or right-click while holding `Shift`) to insert a **Class Breakpoint**, designated by a filled red circle to the left of the line.
- Press `Shift+F9` (or right-click while holding `Shift+Ctrl`) to insert an **Instance Breakpoint**, designated by a red star. It only applies to this instance.

### Working with Source Code

- The Debugger shows values of attributes and local variables as a **Tooltip** when you drag the mouse over an instruction.
- Double-click a word to select it. Triple-click in a line to select the entire line. Quadruple-click to select the entire source code.
- Lines with faulty source code are highlighted in **red**, with a message in the status bar.
- To restart executing source code after a breakpoint or error, hold `Ctrl` and double-click that line.
- If the Debugger was opened due to a runtime error and you close it, Plant Simulation terminates all call chains and stops the simulation.
- To terminate only the incorrect call chain and continue the simulation, press `F5`.
- To continue the incorrect Method at a certain line: use **Set Next Statement**, place the cursor and press `Ctrl+F10`, or hold `Ctrl` and double-click the line. Then press `F5`.

## Watch Window

The lower part of the Debugger window shows the **Watch Window** with these tabs:

- **Variables**
- **Anonymous Identifiers**
- **Call Stack**
- **Call Chains**
- **Suspended**
- **Expressions**

You can open a second watch window (click the split button) to show two tabs at the same time, and change its height by dragging the splitter.

### Opening the Watch Window

- Click the Watch Window icon on the Toolbar.
- Press `F12`.
- Select **Debug > Watch Window**.

### Tab Variables

Shows the names of all local variables and their values.

- Double-click a variable to open the dialog **Variable** to change its value.
- The context menu shows the exact value with **17 floating point digits** for local variables of data type `real`, `length`, `weight`, `speed`, and `acceleration`.
- For values with a physical unit, the value is shown in the respective **SI unit** (Plant Simulation always keeps values internally in SI units; conversion is for display only).

### Tab Anonymous Identifiers

Shows the anonymous identifiers `@`, `?`, `current`, `self`, `root`, and `rootfolder`.

- For user-defined attributes of data type Method, `self.~` is shown in addition.
- For formulas and tables, `xSelf` and `ySelf` are shown.
- The cells next to `@` and `?` allow you to test the Method without running a simulation. If you type a path for `@` or `?`, Plant Simulation replaces the anonymous identifier with that path internally.
- Changed values are shown in red in the cells under Value.

#### @ (at sign)

The cell `@` shows the identifier of the **active MU** (the MU that triggers the call of the current Method in a control). You cannot change its contents.

- Press `F2` to open the dialog box of the MU.

#### ? (question mark)

The cell `?` shows the **name of the object that calls the Method** (another Method name, or the object in which a MU triggered a control call). You cannot change its contents.

- Press `F2` to open the dialog box of the calling object.

### Tab Call Stack

Shows the sequence in which Methods are called (the call chain). The first activated Method is at the bottom; the top line shows the Method currently executing.

- Double-click a cell to open the respective Method with its current settings in the Debugger. Double-click the topmost cell to return to the currently executing Method.
- Column **Method** shows the Method name; column **Parameters** shows the parameters.
- The Parameters column always shows the **current** value (if changed, the new value is shown, not the originally passed value).

SimTalk: `getCallStack`

### Tab Call Chains

Shows Methods ready to be executed immediately (not to be confused with the active Method being executed). Active Methods were called and are waiting to be executed while other Methods are still being executed.

### Tab Suspended

Shows Methods suspended by a `waituntil`-statement or a `stopuntil`-statement (also `wait`-instruction or `sleep`-instruction).

- The caller is displayed in parentheses, preceded by the absolute path. Double-click an entry to change to that Method.
- The third column shows the statement which suspended the Method.
- If a comment after a `waituntil`/`stopuntil`/`wait`/`sleep` statement starts with three hyphens `---` or three forward slashes `///`, only the comment is shown (not the entire statement).

SimTalk: `deleteSuspendedMethods`

The method `deleteSuspendedMethods` deletes all suspensions of all methods. Plant Simulation shows a tooltip in the Frame window with the caller and the suspended instruction (e.g., `waituntil SP.empty prio @.ID wait 5:00 ? = PP`).

### Tab Expressions

Type in any expression for the Debugger to evaluate.

- Double-click a row, type an expression (e.g., `self.xPos+1`), and click OK.
- Select **Show Expression for all Methods** to show the expression in the dialog of all Methods.
- To open a variable or expression whose value has data type `object`, click the cell and press `F2`.
- If the tab shows a local variable or attribute, you can edit its value in the Value column.

> **Note:** The tab Expressions is not available if the Method is executed as a formula.

## Toolbar of the Method Debugger

| Action | Command / SimTalk |
|---|---|
| Open the location (Frame) of the Method | Open Location, `Location` |
| Open the origin from which the active Method was derived | Open Origin, `Origin` |
| Return to the currently executed Method | — |
| Open the Watch Window | Watch Window |
| Execute one line at a time (called methods not loaded) | Step Over |
| Execute one line at a time (called methods also loaded) | Step Into |
| Step out of current Method to next statement in caller | Step Out |
| Continue executing the active Method | Continue |
| Stop the simulation (stop all active Methods) | Terminate Simulation |
| Insert/remove a class breakpoint | Class Breakpoint |
| Insert/remove an instance breakpoint | Instance Breakpoint |
| Delete all breakpoints in the Method | Remove All Breakpoints, `clearAllBreakpoints` |
| Temporarily activate/deactivate MU and State Animation | MU and State Animation |

## Menu Bar

Provides the **File Menu**, **Edit Menu**, **Navigate Menu**, **Debug Menu**, **View Menu**, **Tools Menu**, and **Help Menu**.

### File Menu

- Export to File, Print, Apply Changes (described under Edit Ribbon Tab [Method]).

### Edit Menu

Commands described under the Edit Ribbon Tab.

### Navigate Menu

- Open Location, Open Origin, Open Class, Go to Class, Open Frame.

#### Open Frame

Opens the Frame into which you inserted the Method (or brings it to the foreground).

### Debug Menu

#### Stop On (submenu)

- **Stop on Controls** — stops the simulation when the EventController encounters a control Method (Entrance/Exit Control) started from an object, before executing the calling Method.
- **Stop on Formulas** — stops the simulation and opens the Debugger whenever a formula is evaluated.
- **Stop on Error Handler** — stops the simulation and opens the Debugger whenever an error handling method is executed.
- **Stop on Wakeup** — stops the simulation and opens the Debugger when a suspended method resumes (suspended with `waituntil`, `stopuntil`, `wait`, or `sleep(true, false)`).

#### On Step Into (submenu)

- **Step into Controls** — steps into other call chains (controls or woken up suspended Methods).
- **Step into Formulas** — steps into other formulas (e.g., `print table[1,1]` computing a formula in that cell).
- **Step into Encrypted Methods** — sets whether Step Into (`F11`) stops in encrypted Methods. Deactivated by default. When active, the Debugger shows "The source code is encrypted".

#### Ignore (submenu)

- **Ignore Breakpoints** — ignores user-defined breakpoints. SimTalk: `ignoreBreakpoints`
- **Ignore Error Handlers** — does not execute error handling methods on runtime error; instead opens the Debugger at the error position.
- **Ignore Errors** — stops the simulation after an error in the current Method; highlights the error line in red. Error message shows description, Method, line number, and active call chain. SimTalk: `setErrorStop`
- **Ignore Errors in Formulas** — prevents opening the Debugger when a runtime error occurs in a formula.

#### Step Commands

- **Step Over** — executes one line at a time; called Methods not loaded.
- **Step Into** — executes one line; called Methods loaded. Does not jump into encrypted Methods (behaves like Step Over). Note: Step Into and Step Over do not differ if the next line contains no method call.
- **Step Out** — finishes the current Method and stops at the next statement of the calling Method.
- **Continue** — continues executing the active Method.
- **Run to Cursor** — continues until the statement at the cursor.

> The Debugger shows the **elapsed time** when executing instructions with Step Over, Step Into, Step Out, or Run to Cursor if execution takes **10 milliseconds or longer**.

- **Set Next Statement** — sets the next statement to execute (same as `Ctrl` + double-click). Useful to escape endless loops: hold `Shift+Ctrl+Alt`, set cursor outside the loop, press `Ctrl+F10`, then `F5`.
- **Return From Current Call Chain** — terminates the entire call chain that invoked the current Method; the simulation continues afterward.
- **Terminate Simulation** — terminates all call chains and stops the simulation.
- **Restart Simulation** — resets and restarts the simulation (same as Reset then Start in the EventController).

#### Breakpoint Commands

- **Class Breakpoint** — inserts/removes a breakpoint in the class (see Toggle Class Breakpoint).
- **Instance Breakpoint** — adds/deletes an instance breakpoint (see Toggle Instance Breakpoint).
- **Breakpoint Active** — activates or deactivates the selected breakpoint.
- **Breakpoint Settings** — opens the dialog to set a Start Time and Condition:
  - **Active** — check to activate, clear to deactivate.
  - **Start Time** — the breakpoint activates when the EventController reaches/exceeds this time.
  - **Condition** — evaluated each time the breakpoint is reached; stops only if fulfilled.
- **Next Breakpoint** — goes to the next breakpoint.
- **Previous Breakpoint** — goes to the previous breakpoint.
- **Delete Class Breakpoints** — deletes all class breakpoints.
- **Delete Instance Breakpoints** — deletes all instance breakpoints.
- **Delete All Breakpoints** — deletes all class and instance breakpoints. SimTalk: `clearAllBreakpoints`
- **Delete Breakpoints in All Methods** — deletes all breakpoints in all Methods.

#### Other

- **Watch Window** — opens the Watch Window.

### View Menu

- Show Line Numbers, Syntax-controlled Indentation.

#### MUs and States

Temporarily activates or deactivates MU Animation and Icon Animation together. Restores original state when the Debugger window is closed.

### Tools Menu

- Edit Controls, Edit Observers, User-defined Attributes, Rename.

#### User-defined Attributes

Opens a dialog to add, edit, or delete user-defined attributes of the Method.

#### Rename

Opens the Rename dialog to change the name and label of the Method.

### Help Menu

- **Help on Debugger** — opens the help topic for the Method Debugger.
- **Help on Word** (or `F1`) — opens help for the word under the cursor.

## Context Menu

Provides: Breakpoint Active, Breakpoint Settings, Toggle Class Breakpoint, Toggle Instance Breakpoint, User-defined Attributes, Run to Cursor, Set Next Statement, Open Object, Show Object, Cut, Copy, Paste, Delete.

- **Open Object** — opens the object above whose instruction the mouse is positioned.
- **Show Object** — opens the Frame in which the object is inserted and selects it. If the object references another object, the referenced object is shown.
- **Cut / Copy / Paste / Delete** — standard clipboard operations on selected text.

## Methods of the Method

Accessing a Method automatically executes its source code. To access built-in methods, read-only attributes, or attributes, use the reference operator `&`.

> **Note:** You can only access the methods of the object Method that refer to the object itself via the `&` operator. Without `&`, the method is applied to the contents of the Method.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
