# Getting Started: UI & Basic Operations

This document summarizes the Plant Simulation Help topics covering the user interface and basic operations for getting started with Plant Simulation.

---

## Getting to Know Plant Simulation

You can familiarize yourself with Plant Simulation in several ways:

- **View the Videos on YouTube** — accessed from the Start Page, these provide a quick introduction to commonly used modeling tasks. Help topics link to the relevant video with a time code (e.g. `=18`). Videos use shortened YouTube URLs, for example:

  ```
  https://youtu.be/PgT4wkT2Xj8?si=Udlvoq8KcAI9GxQw&t=18
  ```

- **View the Sample Models** — demonstrate how to approach various problems and give ideas for solving modeling tasks. Open via `Example Models > Small Examples` under **Getting Started** on the Start Page.
  - Select the **Category**, **Topic**, and **Sample Model**.
  - Click **Open Model** to open the selected model.
  - Click **More Info** to show a short description.
  - Use the **Search** box to find a model by topic (searches descriptions in the models' ReadMe files). Pressing **Enter** instead of clicking **Search** closes the dialog; reopen via **Start Page** on the Window ribbon tab.

- **Consult the Step-by-Step Help** — go to `File > Help > Contents`, or read the PDF documentation downloaded from the website. Searching the Online Help with Copilot is also recommended.

---

## Working with Plant Simulation, Basics

Topics covered:

- Work with Window Types
- Select Settings in Plant Simulation
- Select View Options in the Frame
- Change the Settings of the Objects
- Find Objects and Text in Your Simulation Model

### Work with Window Types

Plant Simulation is a **multiple-document interface (MDI)** application showing its windows in a common parent window. The program window has a magenta border.

- Windows may open in the background rather than the foreground; move foreground windows aside to access them.
- Instead of closing/reopening the **Class Library**, **Favorites**, **Toolbox**, and **Console**, you can **Auto Hide** them via the title bar.
- See **User Interface Components** in the Reference section for more.

#### Docking Windows

Docking windows (Class Library, Favorites, Toolbox, Console) are docked to part of the program window and always open in the foreground. They have a red border.

- **Undock**: right-click the title bar → **Floating**.
- **Redock**: right-click the title bar → **Docking**.
- Alternatively, drag the title bar to a docking arrow; Plant Simulation highlights the target area in blue and docks the window.
- To prevent a floating window from docking while dragging, hold **Ctrl**.
- To make a docked window floating, double-click the move handle or hold **Ctrl** and drag.
- To dock a floating window again, double-click its title bar or drag it to a side.
- To close a floating window, click **Close** in the title bar.
- Show/hide the Class Library, Favorites, Console, and Toolbox from the **Window** ribbon tab.
- Customize the Quick Access Toolbar and Ribbon via the down arrow → **More Commands**.
- Switch between docking and object windows with **Ctrl+Tab**.

#### Object Windows

Object windows can be maximized, minimized, and arranged. They are the windows of `Frame`, `Method`, `Method Debugger`, `DataQueue`, `DataStack`, `DataList`, `DataTable`, and the Icon Editor. They always open in the background and have a blue border.

- Bring an object window to the foreground by clicking its icon in the window tab bar.
- Arrange (cascade, tile horizontally/vertically) from the **Window** ribbon tab.
- Open DataList, DataQueue, DataStack, and DataTable in the foreground using the method `openDialogBox`.
- Close all object windows with the function `closeAllWindows`.
- Add links to object windows (Frame, Method, DataList, DataQueue, DataStack, DataTable, and user-defined attributes of those data types) to the **Favorites** for quick access.
- Switch between docking and object windows with **Ctrl+Tab**.

#### Changing Between Docking and Object Windows

Press **Ctrl+Tab** to open the **Window Navigator**, which shows a preview of docking and object windows. It stays open until **Ctrl** is released.

- **Left/Right arrow keys** switch between the **Active Docking Windows** and **Active Object Windows** columns.
- **Tab** or **Up/Down arrow keys** switch between windows within a column; releasing **Ctrl** activates the selected window.
- If focus is on a docking window, `Ctrl+Tab` cycles docking windows; if on an object window, it cycles object windows.

#### Dialog Boxes

Dialog boxes belong to material flow, mobile, fluid, resource, information flow, and user interface objects. They have a green border.

- Always open in front; cannot be minimized or maximized.
- Can be dragged outside the program window.
- Edit simulation properties on the respective tabs.
- Open **Edit 3D Properties** via the button in the bottom-left corner.
- Close all open document windows at once via **Close All Windows** on the Window ribbon tab.

### Select Settings in Plant Simulation

- **Model-specific settings** (apply to the active model): `File > Model Settings` (saved in the model file).
- **Settings for new models**: `File > Preferences`. General, 3D, and Editor tabs hold model-independent settings; Simulation, User Interface, and Units tabs hold model-specific settings for new models.
- Add frequently used commands to the Quick Access Toolbar.

#### Select General Options

- Choose the **language** Plant Simulation uses for new models (affects folder/object names, drop-down items, attribute return values, Show Attributes and Methods window, and Method Editor Auto Complete).
- Choose the **date/time format**:

  | Date and time format | Looks like this |
  |---|---|
  | `yyyy/mm/dd` | 12 hour |
  | `yyyy-mm-dd` | 24 hour |
  | `dd.mm.yyyy` | 24 hour |

- Choose the **comment** type added when saving the model:
  - **Without comment** — adds no comment to the `.spp` file.
  - **With comment** — opens a comment window each save.
  - **None** — does not save saving history.
  - When the model crashes, Plant Simulation adds a problem description to the model history. View it via `File > Options > Show Model History`.

#### Select Options for Units and for Displaying the Time

- Select unit/time settings for the active model via `File > Model Settings > Units`, or for all new models via `File > Preferences > Units`.
- **Daylight Saving Time**: EU default starts 02:00 GMT last Sunday in March, ends 03:00 last Sunday in October. For the US, starts 02:00 second Sunday of March, ends 02:00 first Sunday of November.
- **Time Scale**: enter a number between 0 and 86400. Only the display can be changed, not the time scale itself (only when no model is open).
- A time statement is four colon-separated numbers in `days:hours:minutes:seconds`; Plant Simulation stores values in seconds and converts on output.

Examples:

- Standard time format (24h/day, 60min/hour, 60sec/min): `Time Scale 1/1.0`, `Transfer If 24:60:60`.
- Display as `years:months:days:hours` (long simulations): `Time Scale 1/3600`, `Transfer If 12:30:24`.
- Divide a minute into 100 subunits instead of 60 seconds: `Time Scale 1/0.6`, `Transfer If 24:60:100`.

### Change the Settings of the Objects

You can change object settings (attribute values) in several ways:

- Change Values in the Dialog of the Objects
- Change Values by Assigning a Value in SimTalk
- Change Values in the Window Show Attributes and Methods
- Change Values with the AttributeExplorer

#### Change Values in the Dialog of the Objects

Set values by entering into a text box, selecting from a drop-down list, or checking/clearing a check box (clicking the label also works). These settings correspond to attributes accessible via SimTalk; the What's This help shows the attribute name below **SimTalk**.

#### Change Values by Assigning a Value in SimTalk

Set a constant Processing Time of three minutes by typing this instruction into a Method:

```
MyStation.ProcTime := 180
```

or equivalently:

```
MyStation.ProcTime := 3:00
```

**Paths in SimTalk Instructions** — the term `MyStation` designates the object; a period `.` separates the object from the attribute name; the assignment operator `:=` (no space between `:` and `=`) assigns the value. When the Method and the object share the same Frame, the full absolute path (e.g. `.Models.MyPlantAnytown.MyStation`) is not required.

To set the Exit Strategy to a linear sequence, select it in the drop-down list and type successor numbers into the list opened by **Open List**, or type into a Method.

Note: string assignments are not case-sensitive when typed; querying shows sentence case (e.g. `"Linear sequence"`, `"linear sequence"`, and `"LINEAR SEQUENCE"` are all accepted, and `print` shows `Linear sequence`). Clear the **Automatic** check box to set a Station up manually.

#### Change Values in the Window Show Attributes and Methods

- Press **F8** on the object to open the window.
- Double-click an attribute and enter/select a new value.
- Double-click a boolean attribute's row to toggle `true`/`false`.

#### Change Values with the AttributeExplorer

The AttributeExplorer manages attributes of multiple stations at a single location. Enter different values for capacities, times, etc.; Plant Simulation writes them back to the dialogs. Export settings as a tab-delimited text file and import into another model for identical settings. Also used to find objects/attributes (e.g. positions) and align them in the Frame.

### Find Objects and Text in Your Simulation Model

Find object names, conditions, attribute expressions, Method source code, or table expressions.

1. Click **Find Object** on the Frame ribbon tab (or right-click in the Class Library → **Find Object**).
2. Select what to find from the left drop-down list.

YouTube video: `https://youtu.be/FNpiAaUK8iM?si=B1tgMoMpdc03wCmj&t=437`

#### Find the Name of an Object

1. Select **Name** from the left drop-down list.
2. Type the name into the right combo box (e.g. `Station`).
3. Without **Match Whole Word Only**, it finds all words containing the term (e.g. `Station`, `Station1`, `Station11`, `MyStation`).
4. Enter the folder/Frame in **Look In** (or click to select one). Default `.` searches the highest level.
5. Select **Include Subframes** to search nested Frames.
6. Click **Find**.
7. Double-click a result to open its dialog.
8. **Match Whole Word Only** finds only exact whole words.
9. With **Match Case** too, it matches exact casing.
10. **Regular Expression** enables wildcards:

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
| Any one character in the set | `[]` |
| Any one character not in the set | `[^]` |
| Or | `\|` |

Regular expression examples:

- All strings containing `a` + any character + `b`: `a.b`
- Names starting with uppercase `S`: `^[S]`
- Names not ending with `e`: `[^e]$`
- Names with uppercase `L` + any character + `proc`: `L.*proc`

11. Click **Find**.

#### Find a Condition of an Object

1. Select **Condition** from the left drop-down list.
2. Enter any SimTalk expression, e.g. `proctime = 100` or `OpenCtrl = void`.
3. Repeat steps 4–7 from "Find the Name of an Object".
4. Click **Find**.

#### Find Text in a Built-in or a User-defined Attribute of an Object

1. Select **Attribute** from the left drop-down list.
2. Enter the text/value contained in an attribute. The attribute name is shown in parentheses after the object.
3. Repeat steps 4–7 from "Find the Name of an Object".
4. Click **Find**.

#### Find Any Source Code in a Method

1. Select **Source Code** from the left drop-down list.
2. Enter the text/value within a Method's source code.
3. Repeat steps 4–10 from "Find the Name of an Object".
4. Select **Ignore Inherited Name or Text** to search only original source code (not derived/duplicated objects).
5. Click **Find**.
6. Double-click a result to open the Method and jump to the first occurrence; double-click again (or **Open**) for the next occurrence; hold **Shift** and double-click to jump to the previous occurrence.
7. To replace found code, right-click one or more Methods in the results and select **Replace With**, then enter the replacement code.

---

*Source: Plant Simulation Help — Unpublished work. © 2026 Siemens*
