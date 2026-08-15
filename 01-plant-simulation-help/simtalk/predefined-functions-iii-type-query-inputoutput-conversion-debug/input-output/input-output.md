# Input/Output Functions (SimTalk)

> **Note:** The dialogs opened by these functions are modal. The simulation only continues when the user reacts to the requested interaction.

---

## Input Functions

### `prompt` [SimTalk]

Asks the user to enter data into a dialog.

**Type:** Function

**Syntax**

```
prompt(Text:string[, MoreText:string, ...]) → string
```

**Parameters**

- **Text** (`string`) — the text to show. Plant Simulation opens a dialog displaying the text and a text box. It pauses the simulation run until the user enters the data and closes the window by clicking OK. Plant Simulation can display a maximum of four lines with a maximum of 45 characters per line. Each line is treated as its own `string` parameter.
  - To show text in the title bar of the dialog, type it between two vertical bars, e.g. `("|My Company|This is a prompt!", "row 2")`.
- **MoreText** (`string`, optional) — additional text to show.

**Return Value**

`string` — the data the user entered.

> **Note:** You can convert the result with the functions for converting data types.

**Examples**

```
// method for querying the number of pallets in a model
-> integer
var s: string
// gets the number of pallets
s := prompt("Enter number", "of pallets")
return str_to_num(s)
var s: string
s := prompt("|My Company|This is a prompt!", "row 2")
```

**See also:** Functions for Converting Data Types

---

### `promptList1` [SimTalk]

Enables the user to pick a single entry from the list, which is displayed in the message window.

**Remarks:** The user can select a single entry and click OK. The dialog is modal; the simulation only continues when the user reacts by clicking the respective button.

**Type:** Function

**Syntax**

```
promptList1(Entry:list[, Text:string, ...]) → integer
```

**Parameters**

- **Entry** (`list`) — a list of any type with one column.
- **Text** (`string`, optional) — the text above the list box. Any number of optional `string` parameters are allowed, each with a maximum length of 45 characters.
  - To show text in the title bar, type it between two vertical bars, e.g. `(DataList, "|My Company|Text ...", "row 2")`.

**Return Value**

`integer` — the index of the selected entry, or `0` when the user clicks Cancel.

**Examples**

```
promptList1(DataList, "Select an entry from the list below",
"additional text, text, text, text, ...")
// the entries are contained in the object DataList
promptlist1(DataList, "|My Company|Text ...", "row 2")
```

---

### `promptListN` [SimTalk]

Enables the user to pick one or several entries from the designated list, which is displayed in the message window.

**Remarks:** The dialog is modal. The user can select one or several entries by Shift/Ctrl+clicking the objects and click OK.

**Type:** Function

**Syntax**

```
promptListN(List:list[, Text:string, ...]) → list
```

**Parameters**

- **List** (`list`) — the list. The user can select one or more entries by holding down Ctrl and clicking. OK closes the dialog and accepts the choice.
- **Text** (`string`, optional) — the text above the list box. Any number of optional `string` parameters are allowed, each with a maximum length of 45 characters.
  - To show text in the title bar, type it between two vertical bars, e.g. `(DataList, "|My Company|Text...", "row 2")`.

**Return Value**

`list[integer]` — the indexes of the selected entries, saved unsorted. When the user clicks Cancel, Plant Simulation returns `0`.

**Examples**

```
// A part entering the plant may be processed by more than one machine.
var machPark: list[string]  // You are going to enter the machines that can
var indices: list[integer]  // process it
machPark.create
machPark[1] := "M7"; machPark[2] := "M12"
machPark[3] := "M4"; machPark[4] := "M19"
indices := promptListN(machPark,
   "Select one or several of the machines that can", "process the part:")
for var i := 1 to Indices.Dim
   switch indices[i]
   case 1
   // M7 selected
   case 2
      // M12 selected
   case 3
      // M4 selected
   case 4
      // M19 selected
   end // switch
next
promptlistN(MyDataList, "Select one or several entries from the list below",
"by Shift+clicking or Ctrl+clicking the objects.","Additional text, text,
text, text, ...")
// the entries are contained in the object MyDataList
promptlistn(DataList, "|My Company|Text...", "row 2")
```

---

## Output Functions

SimTalk provides the following functions for outputting data.

### `beep` [SimTalk]

Plays a beeping sound on the computer speaker. You can use it to alert the user about messages or critical situations.

**Type:** Function

**Syntax**

```
beep
```

**Example**

```
if store.full
   beep // acoustic alert
   print "The Store is full"
else
   @.move(Store)
end
```

---

### `bell` [SimTalk]

Outputs an acoustic signal on the computer speaker.

**Type:** Function

**Syntax**

```
bell(Frequency:integer, Duration:integer)
```

**Parameters**

- **Frequency** (`integer`) — the frequency of the bell sound.
- **Duration** (`integer`) — its duration.

**Example**

```
bell(440,1000)
```

---

### `getUnit` [SimTalk]

Returns the unit of the passed value of the data type length, weight, time, speed, money, or acceleration.

**Remarks:** This is the unit selected under **File > Model Settings > Units**.

**Type:** Function

**Syntax**

```
getUnit(Value:any) → string
```

**Parameter**

- **Value** (`any`) — the value for which you would like to get the unit.

**Return Value**

`string` — the unit.

**Example**

```
var l: length := 100 // meters
// We now assume that the length unit in the Model Settings is set to
kilometers
print l          // returns 0.1 km
print to_str(l)  // returns 0.1, to_str does not add a unit
print getUnit(l) // returns km
// Since we don't have settings for areas we still get SI units here
print l*l          // returns 10000m²
print getUnit(l*l) // returns m²
```

**See also:** Units [model settings]

---

### `infoBox` [SimTalk]

Presents the user with a message box, which shows the designated text.

**Remarks:** Close the message box by calling `infoBox` a second time and passing an empty string `""`.

> **Note:** Open a modal Infobox to prevent the user from modifying a simulation model during a simulation run. If the Debugger is opened, any open message box will be closed. Otherwise, an open modal message box would prevent you from continuing your work.
>
> **Note:** If you inadvertently opened a modal message box without closing it, hold down the Shift+Ctrl+Alt keys for 5 seconds. This closes the message box and opens a dialog you can close by clicking No.

**Type:** Function

**Syntax**

```
infoBox(Text:string, Modal:boolean)
```

**Parameters**

- **Text** (`string`) — the text the message box shows.
- **Modal** (`boolean`) — sets whether the dialog is modal, i.e., whether you cannot access any other Plant Simulation window (`true`) or not (`false`).

**Example**

```
infoBox("My information",false)  // shows "My information"
infoBox("", false)               // closes the info box
```

---

### `print` [SimTalk] — output function

Outputs any amount of text to the Console.

**Remarks:** You can open the Console by clicking the button on the Window ribbon tab. Strings within arrays are enclosed in quotation marks.

**Type:** Function

**Syntax**

```
print ...
```

**Parameter**

- For values of data type length, weight, speed, and acceleration, the Console shows the unit after the value.
- You can specify any number of parameters without any type constraint. Use this function to show error messages or other hints for the user.

**Examples**

```
print "Machine: ",   station.name,  "  - is blocked"
@.Cont.move(MyDrain)
print @, ":"
print "Previous destination: ", @.Destination  // writes the previous
                                               // destination to the Console
@.Destination := LoadingStation
print "New Destination: ", @.Destination      // writes the new
                                              // destination to the Console
print                                         // inserts an empty line
var a : string["Kent, Clark", ""]
var s : string := to_str(a)  -- assigns ["Kent, Clark", ""]
```
