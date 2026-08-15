# SimTalk Predefined Functions (N to Z)

This document summarizes the SimTalk predefined functions in the N–Z range from the Plant Simulation help.

---

## numOfLimitedObjects

Counts all built-in objects contained in the entire model.

**Remarks**
- Does not count Lists and Tables, Methods, Variables, Comments, MUs, Connectors, Interfaces, EventControllers, the Toolbar, Folders, and Class objects.
- Useful when working with a Plant Simulation Standard License (limited to 4000 objects).
- The root object `Basis` in the Class Library shows how many objects are used and how many are allowed.

**Type:** Function

**Syntax**
```
numOfLimitedObjects → integer
```

**Return Value:** `integer`

**Example**
```
print numOfLimitedObjects // returns 10 for the model in the screenshot
```

---

## openColorSelectBox

Opens the dialog "Colors" provided by Windows.

**Type:** Function

**Syntax**
```
openColorSelectBox(Color:integer) → integer
```

**Parameter**
- `Color` (integer): the active color value. Typically defined with `makeRGBValue`.

**Return Value:** `integer` — the RGB color value of the color selected by the user.

**Example**
```
colorVar := openColorSelectBox(colorVar)
openColorSelectBox(makeRGBValue(255,150,0)) // current color is orange
```

---

## openConsole

Opens the Console window.

**Type:** Function

**Syntax**
```
openConsole → boolean
```

**Return Value:** `boolean` — `true` if the Console was opened, `false` if it could not be opened.

**Example**
```
openConsole
```

---

## openDateSelectBox

Opens a dialog in which you can select a date.

**Remarks**
- Click OK to set the selected date. Closing the dialog with the Close button returns `1900/01/01`.

**Type:** Function

**Syntax**
```
openDateSelectBox(TitleText:string[, InitialDate:date]) → date
```

**Parameters**
- `TitleText` (string): the caption shown in the dialog's title bar.
- `InitialDate` (date, optional): the date initially selected in the dialog.

**Return Value:** `date` — the date the user picked.

**Examples**
```
openDateSelectBox("Select a date")
print openDateSelectBox("Select a date") // returns 2024/05/18
openDateSelectBox("Select a date", str_to_date("2024-05-18"))
print openDateSelectBox("Select a date") // returns 2024/05/18
```

---

## openHTMLBrowser

Starts the HTML Browser and opens the address designated by the string parameter.

**Remarks**
- To open a connection to the local calling Plant Simulation process, use `L` or a forward slash `/` as the first character.
- URLs beginning with `L/` only work when the web server has been started.
- The safety setting *Prohibit Access to the Computer* affects the function:
  - Permits only `http`, `https`, `file`, UNC paths and normal file-system paths.
  - Does not permit references to executable files (extensions listed in `PATH_EXT`).
  - For file paths, only permits paths pointing to the model folder or its sub-folders.

**Type:** Function

**Syntax**
```
openHTMLBrowser(WWWAddress:string) → string
```

**Parameter**
- `WWWAddress` (string): the address to be opened.

**Return Value:** `string`

**Examples**
```
openHTMLBrowser("https://www.siemens.com/global/en.html")
openHTMLBrowser("https://www.siemens.com/global/de.html")
```

---

## openHTMLWindow

Opens a browser window without the properties of a normal HTML browser window.

**Remarks**
- Subject to the same *Prohibit Access to the Computer* restrictions as `openHTMLBrowser`.
- Microsoft Edge WebView2 can display PDF documents; with the runtime installed, `openHTMLWindow` shows PDF documents directly.

**Type:** Function

**Syntax**
```
openHTMLWindow(Address:string, WindowTitle:string, X:integer, Y:integer,
Width:integer, Height:integer) → boolean
```

**Parameters**
- `Address` (string): the address of the browser window.
- `WindowTitle` (string): the title of the window.
- `X`, `Y` (integer): the x/y-coordinates where the window opens.
- `Width`, `Height` (integer): the width and height of the window.

**Return Value:** `boolean`

**Examples**
```
openHTMLWindow("C:\Temp\mysite.htm", "My Page", 200,400,200,300)
openHTMLWindow("C:\Temp\document.pdf", "My pdf document", 200,400,200,300)
```

---

## openObjectSelectBox

Opens the dialog "Select Object".

**Type:** Function

**Syntax**
```
openObjectSelectBox(Filter:string, FrameOrFolder:object) → string
```

**Parameters**
- `Filter` (string): the filter, i.e., which objects the list box shows.
  - Empty string `""` shows all objects.
  - Specify the `InternalClassType` to show only objects of that type.
  - `":Table"` shows only lists and tables.
  - `":MatCarrier"` shows only material flow objects.
  - `":Importer"` shows only material flow objects that have importers.
  - Several types can be separated by colons. Internal identifiers are case-sensitive.
- `FrameOrFolder` (object): the Frame or folder for which the dialog is initially opened.

**Return Value:** `string`

**Examples**
```
var path := openObjectSelectBox("Station", current)
// only shows the objects of type Station in the 'Select Object' dialog
// which are inserted into the simulation model
var path2 := openObjectSelectBox(":Table", .InformationFlow)
// shows all lists and tables in the 'Select Object' dialog
```

---

## processTime

Returns the CPU time, in seconds, which Plant Simulation used.

**Type:** Function

**Syntax**
```
processTime -> real
```

**Return Value:** `real` — resolution of several milliseconds.

**Example**
```
print processTime
```

---

## profiler

Activates or deactivates the Profiler.

**Remarks**
- While active, it continuously collects the frequency of calls and the runtime of methods.

**Type:** Function

**Syntax**
```
profiler(Activate:boolean)
```

**Parameter**
- `Activate` (boolean): activates (`true`) or deactivates (`false`) the Profiler.

**Example**
```
profiler(true) // activate Profiler
```

---

## putValuesIntoTable

Writes the values of a string attribute (which can only take predefined values) into a table.

**Remarks**
- Examples are values of drop-down lists in object dialogs; accessible in "Show Attributes and Methods".
- Example: the attribute `ResourceType` of material flow objects can take `Production/Produktion`, `Transport/Transport`, or `Storage/Lagerung`, depending on Model Language.
- Returns values according to the Model Language (query with `language`).

**Type:** Function

**Syntax**
```
putValuesIntoTable(TargetTable:table)
```

**Parameter**
- `TargetTable` (table): the target table.

**Example**
```
var lst: list[string]
lst.create
MyStation.ResourceType.putValuesIntoTable(lst)
MyDialog.setList("My drop-down list box",lst)
```

**Note:** Query whether a value is selected without querying the model language with `isSet`.

---

## rad2deg

Converts an angle in radians to the respective angle in degrees.

**Type:** Function

**Syntax**
```
rad2deg(AngleInRadians:real) -> real
```

**Parameter**
- `AngleInRadians` (real): the angle in radians to convert.

**Return Value:** `real`

**Example**
```
print rad2deg(0.785398163397448) // returns 45
```

---

## readStringFromFile

Reads the entire contents of a file and returns it as a string.

**Remarks**
- If the file starts with a BOM (Byte Order Mark), it is evaluated and not returned as part of the string.

**Type:** Function

**Syntax**
```
readStringFromFile(FileName:string) -> string
```

**Parameter**
- `FileName` (string): the file to read.

**Return Value:** `string`

**Example**
```
var s: string := readStringFromFile(ApplicationHome +
"Templates\English\Interaction\Interaction_connect.txt")
print s
```

---

## resetProfile

Deletes all data collected by the Profiler up to the time the model is reset.

**Remarks**
- Call before activating the Profiler to record only valid data for the active simulation run.

**Type:** Function

**Syntax**
```
resetProfile
```

**Example**
```
resetProfile
```

---

## resetRandomNumberStream

Resets a random number stream for distribution functions such as `z_uniform`, `z_normal`.

**Remarks**
- Each material flow object uses its own random number stream (set via `RandomSeed`).
- The stream passed here refers to distribution functions, not object streams.

**Type:** Function

**Syntax**
```
resetRandomNumberStream(Stream:integer)
```

**Parameter**
- `Stream` (integer): the random number stream.

**Example**
```
resetRandomNumberStream(5)
```

---

## saveFolderModel

Saves the simulation model in a folder/file structure, which facilitates storing the model in a version control system such as Git.

**Type:** Function

**Syntax**
```
saveFolderModel(FileName:string[, CompactFormat:boolean:=false,
UseGit:boolean:=false])
```

**Parameters**
- `FileName` (string): path and name of the model.
- `CompactFormat` (boolean, default `false`): if `true`, objects inside Frames with an origin are saved to individual `.yaml` files; if `false`, all objects are saved into the `$.yaml` file of the Frame (fewer files, better performance for large models).
- `UseGit` (boolean, default `false`): if `true`, creates a Git repository when the folder model is first saved (initial version committed automatically, `.gitignore` created). Only available if Git is installed.

**Git Commit Support**
- Registry key `FolderModelCommitCommand` (String Value) sets the command called when saving the model. Create it under `HKEY_CURRENT_USER\Software\Siemens\Tecnomatix Plant Simulation 2606` or `HKEY_LOCAL_MACHINE\...`.
- If the key exists, TortoiseGit is started; if it does not, TortoiseGit is not started.
- Enter an empty string `""` to never open the Commit dialog.
- For another source control system, enter its path as the Value data.

**Example**
```
saveFolderModel("D:\MyModels\MyDeportioner.psfm", true, true)
```

---

## saveModel

Saves the current model with the file name you specify.

**Remarks**
- If no directory is specified, the model is saved to the current directory (set via `setCurrentDirectory`).
- `modelFile` returns the current name/folder of the model file.
- Within a formula or `executeSilent`, no call chains are saved (not the currently called/scheduled/suspended Methods).
- With *Prohibit Access to the Computer* deactivated, `saveModel` can copy data from another folder to the model folder (but not from the model folder or its sub-folders).

**Type:** Function

**Syntax**
```
saveModel(ModelName:string[, StopMethodExecution:boolean[,
UseNewName:boolean[, SaveCallChains:boolean]]]) → boolean
```

**Parameters**
- `ModelName` (string): name of the model file; can be a fully qualified path.
- `StopMethodExecution` (boolean, default `false`): if `true`, method execution stops after loading and the Method Debugger opens; the simulation is stopped in both cases.
- `UseNewName` (boolean, default `true`): if `true`, the model uses the new file name; otherwise it keeps its name.
- `SaveCallChains` (boolean, default `true`): if `false`, Methods being executed and suspended Methods are not saved.

**Return Value:** `boolean`

**Example**
```
print saveModel("C:\Temp\MyModel1.spp", false)
if not EventController.isRunning // was the model just loaded?
   if messageBox("Continue the simulation?",48,2) = 16 // Yes?
       EventController.start
   end
end
```

---

## saveProfile

Saves all data collected by the Profiler to the designated file (existing content is overwritten).

**Remarks**
- Can be printed or loaded into a Method object.
- With *Prohibit Access to the Computer* deactivated, `saveProfile` can copy data from another folder to the model folder or its sub-folders (but not from the model folder or its sub-folders).

**Type:** Function

**Syntax**
```
saveProfile(FileName:string[, IncludeTop50CallCycles:boolean]) → boolean
```

**Parameters**
- `FileName` (string): path to the file.
- `IncludeTop50CallCycles` (boolean): if `true`, the Top 50 Call Cycles are written to the file.

**Return Value:** `boolean`

**Example**
```
saveProfile("C:\Users\Jeff\MyRun1.txt")
```

---

## sendSMTPMail

Sends an e-mail via the denoted mail server to the designated address.

**Remarks**
- With *Prohibit Access to the Computer* deactivated, Plant Simulation does not execute the function and shows an error message.

**Type:** Function

**Syntax**
```
sendSMTPMail(Mail-Server:string, Receiver:string, Subject:string,
MessageText:string)
```

**Parameters**
- `Mail-Server` (string): the mail server.
- `Receiver` (string): the receiver of the mail.
- `Subject` (string): the subject.
- `MessageText` (string): the message text.

**Example**
```
sendSMTPMail("mail.company.com", "John.Smith@abc.org", "Test", "Hello John,
the smoke test was successful.")
```

---

## setAntitheticRandomNumbers

Sets whether Plant Simulation uses antithetic random numbers (`true`) or normal random numbers (`false`).

**Type:** Function

**Syntax**
```
setAntitheticRandomNumbers(AntitheticRandomNumbers:boolean) → boolean
```

**Parameter**
- `AntitheticRandomNumbers` (boolean): whether to use antithetic random numbers.

**Return Value:** `boolean` — the previous setting.

**Example**
```
setAntitheticRandomNumbers(true)
```

---

## setConsoleFilter

Sets whether the Console activates the designated Console filters.

**Type:** Function

**Syntax**
```
setConsoleFilter(Filter:string, Activate:boolean) → boolean
```

**Parameters**
- `Filter` (string): the filter(s):
  - `Info`: information about the model without user input.
  - `Message`: information with user input from dialog windows and message boxes.
  - `Print`: information from print commands in Methods.
  - `Debug`: internal program messages for software engineers.
  - Several filters can be separated by the pipe symbol `|`.
- `Activate` (boolean): activates (`true`) or not (`false`) the filter.

**Return Value:** `boolean`

**Example**
```
setConsoleFilter("Info|Message|Debug", false)
```

---

## setEpsilon

Sets the value for which Plant Simulation considers numerical values to be "about equal".

**Type:** Function

**Syntax**
```
setEpsilon(Value:real) → real
```

**Parameter**
- `Value` (real): the epsilon value.

**Note**
- Use the about-equal comparison (`~=`) to prevent rounding errors with real values.

**Return Value:** `real`

**Example**
```
setEpsilon(0.0001)
var a : real := 1.0003
var b : real := 1.00003
if a ~= 1.0  // this condition is false
   print "a is about equal to 1"
end
if b ~= 1.0  // this condition is true
   print "b is about equal to 1"
end
```

---

## setInfiniteLoopDetectionTimeout

Sets the number of seconds method execution might take before Plant Simulation opens the dialog telling you that you can stop method execution with Shift+Alt+Ctrl.

**Type:** Function

**Syntax**
```
setInfiniteLoopDetectionTimeout(Timeout:integer) → integer
```

**Parameter**
- `Timeout` (integer): the timeout in seconds. `0` or a negative value deactivates infinite loop detection. Minimum allowed value is `3` seconds.

**Return Value:** `integer` — the previous value.

**Example**
```
setInfiniteLoopDetectionTimeout(60)
```

---

## setMUTraceRouteMethod

Designates a Method or an array of Methods called each time an MU is moved to another object.

**Remarks**
- Methods registered with `setMUTraceRouteMethod` are removed from the Registry when the EventController is reset; each model must re-register its Methods when initializing.

**Type:** Function

**Syntax**
```
setMUTraceRouteMethod(&Method:object) → object
setMUTraceRouteMethod([array_of_Methods:any]) → object
setMUTraceRouteMethod → object
```

**Parameters for a Single Method Object**
- `fromObject` (object): the object the MU was on before the move.
- `fromLength` (length): the MU's position on a length-oriented object before the move.
- `fromLane` (integer): the lane on a TwoLaneTrack.
- `time` (time): the point in time at which the MU is to be moved.

**Return Value:** `object`

**Example**
```
param fromObject: object, fromLength: length, fromLane: integer, t: time
var numSankeys: integer
var sankeylist: object
var toLength: length
sankeylist := rootfolder.internal.ActiveSankeyObjects

numSankeys := sankeylist.dim
for var i := 1 to numSankeys
   sankeylist.read(i).printTrace(@,fromObject,fromLength,fromLane,?,t)
next
```

**Parameters for an Array of Methods**
- Passing an array of Method objects enters all Methods as Callback Methods and removes all previous ones.
- Calling without a parameter does not change existing Callback Methods but returns an array of them.

**Return Value:** array of `object` containing all previously existing Callback Methods.

**Examples**
```
// add 'MyMethod' to the Callback Methods
var callbacks: object[] := setMUTraceRouteMethod() // get the already
installed Callback Methods
callbacks.append(&MyMethod)      // add MyMethod
setMUTraceRouteMethod(callbacks) // set the previously installed methods
plus MyMethod as Callback Methods
// remove 'MyMethod' from the Callback Methods
callbacks := setMUTraceRouteMethod() // get the installed Callback Methods
callbacks.deleteValue(&MyMethod)     // remove MyMethod from the array
setMUTraceRouteMethod(callbacks)     // set the previously installed
methods minus MyMethod as Callback Methods
// clear all Callback Methods
var empty: object[]
setMUTraceRouteMethod(empty) // setting an empty array will uninstall all
Callback Methods
```

---

## setPythonDLLPath

Specifies the path to the Python installation to use if you have multiple Python environments.

**Remarks**
- Plant Simulation supports Python versions 3.12, 3.13, and 3.14.
- Use `setPythonDLLPath` to choose which installed Python version to use.

**Type:** Function

**Syntax**
```
setPythonDLLPath(dllpath:string)
```

**Parameter**
- `dllPath` (string): the path to the Python dll.

**Examples**
```
setPythonDLLPath("C:\Program Files\Python312\python312.dll")
-- uses the Python version for all users, located in C:\Program
Files\Python312, which is the default setting
setPythonDLLPath("C:\Users\<YourLoginName>\AppData\Local\Programs\Python\Python312\python312.dll")
-- uses the Python version for the current user located in the folder above
```

---

## setRandomSeedCounter

Influences the automatic allocation of the random number seed value (normally not required).

**Remarks**
- When an object is inserted, Plant Simulation automatically assigns a random number seed value; query the next assigned value with `setRandomSeedCounter(0)`.
- After creation, the counter is increased by 1 so the next object gets a different seed value.
- Calling with `0` only returns the current counter; a non-zero value sets the counter.
- Setting the counter lower than the previous value does not guarantee unique seed values.
- Useful when automatically creating simulation models (e.g., via Teamcenter) to use the same seed values across recreations.

**Type:** Function

**Syntax**
```
setRandomSeedCounter(CounterValue:integer) → integer
```

**Parameter**
- `CounterValue` (integer): the value of the counter.

**Return Value:** `integer` — the current random seed counter.

**Example**
```
setRandomSeedCounter(4)
print setRandomSeedCounter(0)
```

---

## setSeedTable

Sets the random number seed values for creating the random number streams.

**Remarks**
- Seed values only apply to distribution functions (e.g., `z_uniform`, `z_normal`).
- Each material flow object uses its own stream (set via `RandomSeed`).
- New random numbers are applied immediately; all random number streams are reset with the new seed values.

**Type:** Function

**Syntax**
```
setSeedTable(SeedTable:table)
```

**Parameter**
- `SeedTable` (table): a table with one or two columns (or a list).
  - First column: random number seed values (integer).
  - Optional second column: comments (string). The row number matches the random number stream number.

**Examples**
```
var t: table[integer]
t.create
t[1,6] := 1
setSeedTable(t)

var t: table[integer]
t.create
t[1,6] := 1
t[2,6] := "Explain usage"
setSeedTable(t)
```

---

## showStatisticsReport

Shows the Statistics Report of the objects typed into the list.

**Type:** Function

**Syntax**
```
showStatisticsReport(List:list[, FileName:string])
```

**Parameters**
- `List` (list): the list with the names of the objects.
- `FileName` (string, optional): the name of the file into which the statistics values are written.

**Example**
```
showStatisticsReport(myStatisticsObjects)
showStatisticsReport(myStatisticsObjects,"My Statistics Report")
```

---

## strHash

Calculates the hash value from the passed string.

**Remarks**
- Value is between `0` and `2147483647` (inclusive).
- Case-sensitive; convert to lower case with `strToLower` if needed.
- Useful for fast string lookup (integer comparison is faster than string comparison).
- Not bijective (not unambiguously reversible). After finding the hash, compare the strings. To map to a smaller value range, use the modulo value.

**Type:** Function

**Syntax**
```
strHash(string) → integer
```

**Return Value:** `integer`

**Example**
```
var hashTable: any[7]
var emptyStringArray: string[]
for var i := 1 to hashTable.dim
   hashTable[i] := emptyStringArray
next
hashTable[strHash("Source")   mod 7 + 1] := ["Source"]
hashTable[strHash("Drain")    mod 7 + 1] := ["Drain"]
hashTable[strHash("AssemblyStation") mod 7 + 1] := ["AssemblyStation"]
var SourceFound: boolean := hashTable[strHash("Source") mod 7 +
1].find("Source") /= 0
var BufferFound: boolean := hashTable[strHash("Buffer") mod 7 +
1].find("Buffer") /= 0
```

---

## throwRuntimeError

Returns an error message to the calling Method in library methods (e.g., when called with invalid parameter values).

**Remarks**
- Can also be used outside libraries.
- When called, Plant Simulation opens the Method Debugger for the calling Method (or the position containing `throwRuntimeError` if no caller exists). Encrypted methods show a message box instead.
- If part of a library, Plant Simulation returns the call chain up to the first Method not belonging to the library and opens the Method Debugger there.
- If an ErrorHandler exists in the calling Method or its callers, it is called instead of opening the Method Debugger (searching outward, then the global error handler).

**Type:** Function

**Syntax**
```
throwRuntimeError(ErrorMessage:string)
```

**Parameter**
- `ErrorMessage` (string): the error message shown.

**Example**
```
param NewPosition : length
// the method drives the hook of the crane to a new position
if NewPosition < 0 or NewPosition > MyCrane.MyCraneArmLength
   throwRuntimeError("invalid crane position")
end
// set the new position ...
```

---

## updateGUI

Updates the graphical user interface of Plant Simulation.

**Remarks**
- Use within long-running Methods to prevent Plant Simulation from appearing unresponsive. `updateGUI` redraws the contents of the Frames.

**Type:** Function

**Syntax**
```
updateGUI -> integer
updateGUI([forceUpdateNow:boolean:=false]) -> integer
```

**Parameter**
- `forceUpdateNow` (boolean, default `false`): set to `true` for an immediate UI update; otherwise redraw once after some time has passed since the last update.

**Example**
```
for var y := 1 to JTFileTable.yDim
   MyFrame._3D.importGraphics([0,y,0], JTFileTable[1,y], false, true)
   updateGUI
next
```

---

## userInterfaceLanguage

Returns the language of the user interface of Plant Simulation.

**Type:** Function

**Syntax**
```
userInterfaceLanguage → integer
```

**Return Value:** `integer`
- `0` = German, `1` = English, `2` = Japanese, `3` = Chinese, `8` = Hungarian.

**Example**
```
if userInterfaceLanguage = 0      // German
   print "Guten Morgen"
elseif userInterfaceLanguage = 1  // English
   print "Good morning"
elseif userInterfaceLanguage = 2  // Japanese
   print "Ohayo gozaimasu"
elseif userInterfaceLanguage = 3  // Chinese
   print "Zao an"
elseif userInterfaceLanguage = 8  // Hungarian
   print "Jó reggelt"
end
```

---

## writeStringToFile

Writes the content of the specified Text to a file.

**Type:** Function

**Syntax**
```
writeStringToFile(Text:string, FileName:string[, Append:boolean,
Encoding:string:="UTF-8"])
```

**Parameters**
- `Text` (string): the text to write.
- `FileName` (string): the file or directory path and name. If the file exists, it is overwritten.
- `append` (boolean, optional): if `false`, existing content is deleted before writing; if `true`, the content is not deleted and a line break (Carriage Return + Line Feed) is appended.
- `Encoding` (string, default `"UTF-8"`):
  - `"UTF-8"` or omitted: UTF-8 with BOM.
  - `"Unicode"` or `"UTF-16"`: UTF-16 with BOM.
  - Empty string `""`: UTF-8 without BOM.

**Examples**
```
writeStringToFile("hello world", "C:\Users\Public\Public Documents\a.txt")
writeStringToFile(&MyMethod.Program, "C:\Temp\SourceCode.txt")
-- exports the source code of MyMethod to a text file
var data:json
data["Name"] = "John Doe"
data["Profession"] = "Simulation specialist"
```
