# Miscellaneous Global Functions (A–M)

SimTalk provides the functions listed below covering a wide range of applications. This document summarizes the global functions from `a-to-m`.

## Table of Contents

- [animation](#animation)
- [applicationHome](#applicationhome)
- [applicationVersion](#applicationversion)
- [calcBrakingDistance](#calcbrakingdistance)
- [calcDroppedPerpendicularFootPoint](#calcdroppedperpendicularfootpoint)
- [callEvery](#callevery)
- [checkForLicense](#checkforlicense)
- [checkID](#checkid)
- [clearConsole](#clearconsole)
- [clearLogFile](#clearlogfile)
- [closeAllWindows](#closeallwindows)
- [closeConsole](#closeconsole)
- [closeHTMLWindow](#closehtmlwindow)
- [closeModel](#closemodel)
- [computeSHA1Hash](#computesha1hash)
- [computeSHA3Hash](#computesha3hash)
- [connectAutomatically](#connectautomatically)
- [createCombinations](#createcombinations)
- [createLicenseFile](#createlicensefile)
- [createPermutations](#createpermutations)
- [currentEventCtl](#currenteventctl)
- [deg2rad](#deg2rad)
- [deleteAllDebugExpressions](#deletealldebugexpressions)
- [deleteFile](#deletefile)
- [enableFullScreenMode](#enablefullscreenmode)
- [execute](#execute)
- [executePythonFile](#executepythonfile)
- [executeSilent](#executesilent)
- [existsFile](#existsfile)
- [existsMethod](#existsmethod)
- [existsObject](#existsobject)
- [exitApplication](#exitapplication)
- [getCallStack](#getcallstack)
- [getCommandLineArg](#getcommandlinearg)
- [getEpsilon](#getepsilon)
- [getExecuteSilentError](#getexecutesilenterror)
- [getFileModificationDateTime](#getfilemodificationdatetime)
- [getHighResolutionClock](#gethighresolutionclock)
- [getLibrariesDirectories](#getlibrariesdirectories)
- [getLibraryFiles](#getlibraryfiles)
- [getLibraryVersionFromFile](#getlibraryversionfromfile)
- [getLogFile](#getlogfile)
- [getProfileCallCycles](#getprofilecallcycles)
- [getSeedTable](#getseedtable)
- [getStandardColor](#getstandardcolor)
- [hideBBL](#hidebbl)
- [isComputerAccessPermitted](#iscomputeraccesspermitted)
- [isSet](#isset)
- [keepWindowsAlwaysOnTop](#keepwindowsalwaysontop)
- [language](#language)
- [licenseName](#licensename)
- [loadModel](#loadmodel)
- [makePathRelative](#makepathrelative)
- [makeRGBValue](#makergbvalue)
- [messageBox](#messagebox)
- [modelFile](#modelfile)

---

## animation

Activates or deactivates the animation of MUs and States during a simulation run.

- Calling without a parameter returns the current animation state.
- Calling with the parameter sets the state (true = activated, false = deactivated).

**Type:** Function

**Syntax**

```
animation → boolean
animation([Activate:boolean]) → boolean
```

**Parameter**

- `Activate` (boolean, optional): `true` activates, `false` deactivates the animation of MUs and States.

**Return Value:** `boolean` — `true` if animation is activated.

**Example**

```
animation         // returns if animation is on or off
animation(true)   // activates animation
```

---

## applicationHome

Returns the folder in which Plant Simulation is installed.

**Type:** Function

**Syntax**

```
applicationHome → string
```

**Return Value:** `string`

**Example**

```
print applicationHome // might return C:\Program Files\Siemens\Plant 
Simulation 2606\
```

---

## applicationVersion

Returns the coded version number of Plant Simulation.

**Type:** Function

**Syntax**

```
applicationVersion -> integer
```

**Return Value:** `integer`, composed as `VVMMMPPP`:
- `VV` is the major version number.
- `MMM` is the minor version number.
- `PPP` is the patch level.

**Example**

```
print applicationVersion // might return 23002008, i.e. version 2302.0008
print applicationVersion // might return 24004000, i.e. version 2404.0000
print applicationVersion // might return 26006000, i.e. version 2606.0000
```

---

## calcBrakingDistance

Calculates the required braking distance for a given speed and deceleration.

The braking distance is calculated according to the formula `s = 1/2 · v²/a`. Especially helpful for the Transporter.

**Type:** Function

**Syntax**

```
calcBrakingDistance(Speed:speed, Deceleration:acceleration) -> length
```

**Parameters**

- `Speed` (speed): the speed.
- `Deceleration` (acceleration): the deceleration.

**Return Value:** `length`

**Example**

```
print calcBrakingDistance(100kmh, 10) // returns 138.888888888889m
```

---

## calcDroppedPerpendicularFootPoint

Calculates the foot of the dropped perpendicular of the point P on the line A1–A2 and returns it.

**Type:** Function

**Syntax**

```
calcDroppedPerpendicularFootPoint(A1:length[3], A2:length[3], P:length[3]) 
-> length[3]
```

**Parameters**

- `A1` (length[3]): first point of the line.
- `A2` (length[3]): second point of the line.
- `P` (length[3]): point for which the foot of the dropped perpendicular is calculated.

**Return Value:** array of three `length` values.

**Example**

```
print calcDroppedPerpendicularFootPoint([1,0.1,0.1],[2,0.2,0.4],[5,0.5,1])
// returns [4.91818181818182, 0.491818181818182, 1.27545454545455]
```

---

## callEvery

Calls all Methods with the designated name in the designated Frame and all of its sub-frames.

- Plant Simulation stops executing the calling Method until all called Methods are executed.
- Frames are searched using the **depth-first strategy**; Methods are executed immediately when encountered.
- Plant Simulation always calls the most recent object first.

**Type:** Function

**Syntax**

```
callEvery(Frame:path, Method:string[, Parameters:parameters])
```

**Parameters**

- `Frame` (path): the Frame within which to call all Methods.
- `Method` (string): name of the Method to call.
- `Parameters` (optional): passed as parameters to the called Methods.

**Example**

```
callEvery(.frame2,"outputMessage",999,"here")
```

---

## checkForLicense

Checks if a user-defined license is available or not.

**Type:** Function

**Syntax**

```
checkForLicense(Feature:string, Version:string, PasswordHash:string) → 
integer
```

**Parameters**

- `Feature` (string): name of the license feature.
- `Version` (string): requested version number of the license.
- `PasswordHash` (string): SHA-1 hash of the license password.

**Return Value:** `integer`
- `0`: The license feature is registered and valid.
- `1`: The license feature is not registered.
- `2`: The file has an invalid registry data format.
- `3`: The SHA-1-Hash is wrong.
- `4`: The Host-ID is wrong.
- `5`: The registered version of the feature is too old.
- `6`: The license has expired.
- `7`: The feature does not permit use with the license type of Plant Simulation (Professional / Standard / Runtime / …).

**Example**

```
if checkForLicense("MyFeature", "1", 
"686483805ac47ca14e03514f7481a7973b401762") = 0 
// The license is available, you can proceed ...
else
closeModel
messageBox("The license 'MyFeature' is unavailable. The model was 
closed.\n", 1, 1)
end
```

---

## checkID

Checks if you can use an expression as the name of an object (`true`) or not (`false`).

**Type:** Function

**Syntax**

```
checkID(Expression:string) → boolean
```

**Parameter**

- `Expression` (string): the expression. All keywords and function calls are considered.

**Return Value:** `boolean`

**Example**

```
print checkID("sin") -- returns false
```

---

## clearConsole

Deletes the contents of the Console window.

**Type:** Function

**Syntax**

```
clearConsole
```

**Example**

```
clearConsole
```

---

## clearLogFile

Deletes the contents of the log file into which Plant Simulation wrote all messages output to the Console window. Does **not** delete the log file itself.

**Type:** Function

**Syntax**

```
clearLogFile → boolean
```

**Return Value:** `boolean`

**Example**

```
clearLogFile
```

---

## closeAllWindows

Closes all open object windows, even those that are minimized, including 3D windows. The optional boolean parameter has no effect.

**Type:** Function

**Syntax**

```
closeAllWindows([UnusedParameter:boolean])
```

**Example**

```
closeAllWindows
```

---

## closeConsole

Closes the open Console window. All messages output to the Console will be lost. The optional boolean parameter has no effect.

**Type:** Function

**Syntax**

```
closeConsole([UnusedParameter:boolean]) → boolean
```

**Return Value:** `boolean`

**Example**

```
closeConsole
```

---

## closeHTMLWindow

Closes the browser window previously opened, identified by the title of the window.

**Type:** Function

**Syntax**

```
closeHTMLWindow(CloseHTMLWindow:string) → boolean
```

**Parameter**

- `CloseHTMLWindow` (string): title of the window to close.

**Return Value:** `boolean`

**Example**

```
closeHTMLWindow("Siemens Corporate Site")
closeHTMLWindow("Image of the ParallelStation")
```

---

## closeModel

Closes the open simulation model without saving it.

You can define a Method named `onCloseModel` in any folder in the Class Library (including the Basis folder). It is executed when the model is closed or Plant Simulation exits (e.g. for clean-up tasks, deleting temporary files). The `onCloseModel` method must declare the boolean parameter `onExitApplication` (false = model closed, true = application exits).

**Type:** Function

**Syntax**

```
closeModel → boolean
```

**Return Value:** `boolean` — returns `false` and does not close the model when called in sub-routines, user-defined attributes of type method, or formulas.

**Note:** To save before closing, call `saveModel` before `closeModel`.

**Example**

```
closeModel
```

---

## computeSHA1Hash

Returns the 40-digit SHA1 hash code of the passed text.

**Type:** Function

**Syntax**

```
computeSHA1Hash(Text:string) → string
```

**Parameter**

- `Text` (string): string for which to compute the hash.

**Return Value:** `string`

**Example**

```
print computeSHA1Hash("MyText") 
// returns 0e9e68d9402c96044f0f93194f7010bc2e056752
```

---

## computeSHA3Hash

Returns the SHA3 hash code of the passed text. Uses the SHA3-256 algorithm (NIST: FIPS 202).

**Type:** Function

**Syntax**

```
computeSHA3Hash(Text:string) → string
```

**Parameter**

- `Text` (string): string for which to compute the hash.

**Return Value:** `string`

**Example**

```
print computeSHA3Hash("MyText") 
// returns 27acf01aa72d499265cc50388f80054e644640586fb04c3165cd4f86d20e02a8
```

---

## connectAutomatically

Automatically connects the object designated by `<Path>` with objects in its vicinity whose entrances and exits are close together.

Rules: uses 3D-coordinates and 3D-sizes; always uses the first possible connection; does not add a new connection on a side that already has one; only connects if bounding boxes overlap in the Z-direction; uses the first Connector class in the Class Library (starting at the top).

**Type:** Function

**Syntax**

```
<Path>.connectAutomatically -> boolean
```

**Return Value:** `boolean`

**Example**

```
MyStation.connectAutomatically
```

---

## createCombinations

Creates all combinations of the specified length of the elements array. If a value is contained multiple times, the result also contains multiple combinations. Limited to 1,000,000 generated combinations.

**Type:** Function

**Syntax**

```
createCombinations(Elements:integer[], Length:integer) -> integer[]
```

**Parameters**

- `Elements` (integer[]): array of elements.
- `Length` (integer): length of the combination.

**Return Value:** `integer[]`

**Examples**

```
// Creates all combinations with two elements
print createCombinations([1,2,3], 2) // returns [1, 2][1, 3][2, 3]
// Creates all combinations of two colors
var arrString:string[]
var arrInt:integer[]
arrString.append("red")
arrString.append("green")
arrString.append("blue")
arrInt.append(1)
arrInt.append(2)
arrInt.append(3)
var resArr = createCombinations(arrInt, 2)
var colorCombination:string
for var y := 1 to resArr.ydim
    print arrString[resArr[1, y]], ", ", arrString[resArr[2, y]]
next
```

---

## createLicenseFile

Generates a user-defined license and writes it to a Windows Registry file, which can then be sent to another person to enter the license on a target computer.

**Type:** Function

**Syntax**

```
createLicenseFile(Feature:string, Version:string, HostID:string, 
ExpirationDate:string/date, Password:string, FileName:string[, 
Restriction:string]) → string
```

**Parameters**

- `Feature` (string): name of the license feature (no blank spaces).
- `Version` (string): version number (no blank spaces); registered version must be ≥ requested version.
- `HostID` (string): Host ID of the computer. Empty string `""` or `"any"` means valid on all computers. Can be a MAC address, Composite Host ID (`COMPOSITE=...`), Sold-To-ID (`SOLDTO=...`), or Enterprise Cloud Account ID (`ECA=...`).
- `ExpirationDate` (string/date): expiration date. `""` or `"permanent"` means no expiration.
- `Password` (string): secret password.
- `FileName` (string): file name or path (`.reg` extension recommended).
- `Restriction` (string, optional): `"Application"`, `"Runtime"`, `"Simulation"`, or `"Viewer"`.

**Return Value:** `string` — the SHA-1 hash of the password.

**Example**

```
PasswordHash := createLicenseFile("MyLicenseName", "1.0", 
"COMPOSITE=0ADF1C780F29", "", "abc", "C:\TEMP\license.reg")
PasswordHash := createLicenseFile("MyLicenseFeature", "1.0", 
"ECA=111111111", "", "abc", "C:\TEMP\license.reg")
```

---

## createPermutations

Creates all permutations of the specified length of the elements array. Duplicate values produce duplicate permutations. Limited to 1,000,000 generated permutations.

**Type:** Function

**Syntax**

```
createPermutations(Elements:integer[], Length:integer) -> integer[]
```

**Parameters**

- `Elements` (integer[]): array of elements.
- `Length` (integer): length of the permutation.

**Return Value:** `integer[]`

**Example**

```
// Creates all permutations with two elements
print createPermutations([1,2,3], 2) // returns [1, 2][1, 3][2, 1][2, 3][3, 
1][3, 2]
```

---

## currentEventCtl

Returns the EventController that controls the current simulation run.

**Type:** Function

**Syntax**

```
currentEventCtl → object
```

**Return Value:** `object`

**Example**

```
if currentEventCtl /= VOID
   print "simulation running in frame", currentEventCtl.location
   print "simulation running in frame", root
end
```

---

## deg2rad

Converts the specified angle in degrees into the respective angle in radians.

**Type:** Function

**Syntax**

```
deg2rad(AngleInDegrees:real) -> real
```

**Parameter**

- `AngleInDegrees` (real): angle in degrees.

**Return Value:** `real`

**Example**

```
print deg2rad(45) // returns 0.785398163397448
```

---

## deleteAllDebugExpressions

Deletes all debug expressions in all methods.

**Type:** Function

**Syntax**

```
deleteAllDebugExpressions
```

**Example**

```
deleteAllDebugExpressions
```

---

## deleteFile

Deletes the specified file for good.

**Type:** Function

**Syntax**

```
deleteFile(FileName:string) -> integer
```

**Parameter**

- `FileName` (string): file to delete.

**Return Value:** `integer` — the Windows error code; `0` if no error occurred.

**Example**

```
deleteFile("MyFile")              // deletes the file named MyFile from the 
installation folder
deleteFile("D:\Publisher.gif")    // deletes the graphics file from the D 
drive
```

---

## enableFullScreenMode

Activates (`true`) or deactivates (`false`) full screen mode.

**Type:** Function

**Syntax**

```
enableFullScreenMode(Activate:boolean)
```

**Parameter**

- `Activate` (boolean): activates (`true`) or deactivates (`false`) full screen mode.

**Example**

```
enableFullScreenMode(true)
```

---

## execute

Receives a string and interprets it as though it were the source code of a method. Accepts all statements.

- The anonymous identifier `?` refers to the Method object that called `execute`; `@` is received by the calling method.
- Use `execute` to run Methods referenced via variables (e.g. `obj.execute`).
- If a runtime error occurs: opens the Debugger (when *Ignore Errors in Formulas* is deactivated), otherwise acts like `executeSilent`.

**Type:** Function

**Syntax**

```
execute(SourceCode:string[ ,Parameter:parameter, ...])
```

**Examples**

```
var objPath : string := "Track"
var attrName: string := "Length"
var attrVal : length := 3.5
execute(to_str(objPath, ".", attrName, ":=", attrVal))

execute("-> integer; return 42") // returns 42 

execute("param x, y: integer; print x+y", 1, 2) // outputs 3 
```

---

## executePythonFile

Executes the source code of the specified Python file. Objects in the model are accessed in the same way as when executing Python code via a PythonModule.

**Type:** Function

**Syntax**

```
executePythonFile(File:string) -> boolean
```

**Parameter**

- `File` (string): Python file containing source code.

**Return Value:** `boolean` — `true` if no error occurred, `false` otherwise.

**Example**

```
print executePythonFile("D:\test.py", "TestArg")
```

---

## executeSilent

Receives a string and interprets it as though it were the source code of a method. Accepts all statements.

- `?` refers to the calling Method object; `@` is received by the calling method.
- If no return value, returns `VOID`.
- On syntax error (when a return value is expected), returns `VOID`.
- On runtime error, returns the default value of the corresponding type and does **not** open the Debugger.
- Otherwise returns the return value of the string method.

**Type:** Function

**Syntax**

```
executeSilent(SourceCode:string[ ,Parameter, ...])
```

**Examples**

```
executeSilent("-> integer; 1+") // returns VOID 

executeSilent("->boolean; Station.name := \"if\"; return true")
// returns false because of a runtime error 

executeSilent("->integer; return := 42") // returns 42

executeSilent("param x, y: integer; print x+y", 1, 2) // returns 3
```

---

## existsFile

Returns whether a file or folder exists (`true`) or not (`false`).

**Type:** Function

**Syntax**

```
existsFile(NameOfFileOrFolder:string) → boolean
```

**Parameter**

- `NameOfFileOrFolder` (string): the file or folder.

**Return Value:** `boolean`

**Examples**

```
var fileName: string
fileName := "MyDataTable.tab"
if not existsFile(fileName) 
   table.writeFile(fileName)
else
   print "The file ",fileName," already exists."
end
print existsFile("noname.mod")
```

---

## existsMethod

Returns whether a path points to a Method object or to a user-defined attribute of data type method.

**Type:** Function

**Syntax**

```
existsMethod(NameOfMethod:string) → boolean
```

**Parameter**

- `NameOfMethod` (string): path of the Method.

**Return Value:** `boolean`

**Example**

```
print existsMethod("Station.MethodAttr")
```

---

## existsObject

Returns whether a path to a simulation object is valid. Cannot access the anonymous identifiers `?`, `@`, `self`, and `current` (use `current.extendPath("Station")` instead).

**Type:** Function

**Syntax**

```
existsObject(NameOfObject:string) → boolean
```

**Parameter**

- `NameOfObject` (string): path of the object.

**Return Value:** `boolean`

**Examples**

```
print existsObject(".Mus.Part:123")
if existsObject("ProdFrame")
   ProdFrame.derive(current,100,200)
end
```

---

## exitApplication

Terminates the simulation run and exits Plant Simulation. Does **not** save model data and issues no warning. You can define `onCloseModel` Methods for clean-up tasks (see `closeModel`).

**Type:** Function

**Syntax**

```
exitApplication
```

**Example**

```
if EventController.EndTime > 36000 
   saveModel("Variation_IIV")
   exitApplication
end
```

---

## getCallStack

Returns the active call stack and writes it to a table. Column 1 (string) contains the absolute path of the method; column 2 (integer) contains the row number of the executed SimTalk instruction. When called in a local ErrorHandler, returns the call stack of the faulty method.

**Syntax**

```
getCallStack → list
```

**Return Value:** `list`

**Example**

```
var tab: table
tab := getcallStack
```

---

## getCommandLineArg

Queries if a command-line argument has been passed to Plant Simulation when starting it.

**Type:** Function

**Syntax**

```
getCommandLineArg(CommandLineArgument:string, byref Value:string) → boolean
```

**Parameters**

- `CommandLineArgument`: the command-line argument to check.
- `Value` (byref): always assigned the value of the next specified command-line argument.

**Return Value:** `boolean` — `true` if Plant Simulation was started with the specified argument.

**Example**

```
// Suppose we started Plant Simulation with these command-line arguments:
// PlantSimulation2606.exe /L Runtime /abc 42 /xyz /myfile "C:\Program 
Files\a.txt"
var arg: string
if getCommandLineArg("abc", arg) 
   print arg // outputs 42
end
if getCommandLineArg("myfile", arg) 
   print arg // outputs C:\Program Files\a.txt
end
if getCommandLineArg("xyz", arg) 
   print arg // outputs an empty string
end
```

---

## getEpsilon

Returns the value set for which Plant Simulation considers numerical values to be about equal.

**Type:** Function

**Syntax**

```
getEpsilon → real
```

**Return Value:** `real`

**Example**

```
print getEpsilon // might output 7e-08
```

---

## getExecuteSilentError

Returns the error message after calling `executeSilent`, or after a formula has been computed (e.g. a table formula or a Formula distribution's Processing Time). Returns an empty string if no error occurred.

**Syntax**

```
getExecuteSilentError -> string
```

**Return Value:** `string`

---

## getFileModificationDateTime

Returns the date and time at which the file was last written. The entire file path (including name and extension `.spp`) must be entered.

**Type:** Function

**Syntax**

```
getFileModificationDateTime(FilePath:string) → dateTime
```

**Parameter**

- `FilePath` (string): full path of the file.

**Return Value:** `dateTime`

**Example**

```
print getFileModificationDateTime("D:\MyControls.spp") 
// might, for example, return 2026-05-11 11:24:43.3760
```

---

## getHighResolutionClock

Returns the number of seconds that passed since opening the model. Useful for measuring extremely short time spans.

**Type:** Function

**Syntax**

```
getHighResolutionClock → real
```

**Return Value:** `real`

**Example**

```
var t1, t2: real
t1 := getHighResolutionClock
var x := sin(t1)
t2 := getHighResolutionClock
print "elapsed time: ", (t2-t1)*1000, " milliseconds"
-- might, for example, return elapsed time: 0.028482056222856 milliseconds
```

---

## getLibrariesDirectories

Returns the Libraries Directories set in the Preferences.

**Type:** Function

**Syntax**

```
getLibrariesDirectories → string[]
```

**Return Value:** `string[]`

**Example**

```
print getLibrariesDirectories // might return [D:\MeineBibliotheken\, 
D:\MyLibraries\]
```

---

## getLibraryFiles

Returns the file paths to `.pslib` files and all their versions.

**Type:** Function

**Syntax**

```
getLibraryFiles(FolderPath:string) → string[]
```

**Parameter**

- `FolderPath` (string): path of a library folder (need not exist in the loaded model).

**Return Value:** `string[]` — alternating file path and version; sorted in descending order by version number; empty if no `.pslib` file found.

**Example**

```
var arr: string[] := getLibraryFiles(".Tools.ExperimentManager")
print "Number of library files: ", arr.dim / 2
print "Newest file: ", when arr.dim > 0 then arr[1] else "(not found)"
var i : integer := 1
while i < arr.dim
   print "File: ", arr[i], "  Version: ", arr[i+1]
   i += 2
end
-- might, for example, return
Number of library files: 1
Newest file: C:\Plant-Simulation-26.6\Libraries\Tools\Experiment.lib
File: C:\Plant-Simulation-26.6\Libraries\Tools\Experiment.lib  Version: 
2404.0025
```

---

## getLibraryVersionFromFile

Returns the version of the library designated by `<Path>`.

**Type:** Function

**Syntax**

```
<Path>.getLibraryVersionFromFile(FilePath:string) → string
```

**Parameter**

- `FilePath` (string): path to a library file (`.pslib`).

**Return Value:** `string`

**Example**

```
print getLibraryVersionFromFile("C:\Program Files\Siemens\Plant Simulation 
2606\Libraries\Tools\MyLibrary.pslib")
```

---

## getLogFile

Gets the log file into which Plant Simulation wrote all messages output to the Console.

**Type:** Function

**Syntax**

```
getLogFile → string
```

**Return Value:** `string`

**Example**

```
getLogFile
```

---

## getProfileCallCycles

Returns a JSON object containing the call cycles that Profiler collected, provided it is activated.

**Type:** Function

**Syntax**

```
getProfileCallCycles([MaxNumCycles:integer]) -> json
```

**Parameter**

- `MaxNumCycles` (integer, optional): restricts the amount of call cycles returned. Omit to return all (may be very large and slow).

**Return Value:** `json`

**Example**

```
print getProfileCallCycles(10)
```

---

## getSeedTable

Returns the active Random Number Seed Values table. Column 1 contains seed values (integer); column 2 contains comments (string); row number matches the random number stream. Seed values apply only to distribution functions (e.g. `z_uniform`, `z_normal`).

**Type:** Function

**Syntax**

```
getSeedTable → table
```

**Return Value:** `table`

**Example**

```
localseedtable := getSeedTable
```

---

## getStandardColor

Returns the specified color value from a standard color palette (e.g. for assigning colors to produced MUs).

**Type:** Function

**Syntax**

```
getStandardColor(Index:integer) -> integer
```

**Parameter**

- `Index` (integer): one of 30 color values of a standard color palette.

**Return Value:** `integer`

**Example**

```
-- Entrance control of a Source object
@._3D.MaterialDiffuseColor = getStandardColor(z_uniform(1,30)
-- Assigns a random color to the created part
```

---

## hideBBL

Minimizes Plant Simulation to an icon in the status area of the taskbar.

**Type:** Function

**Syntax**

```
hideBBL(MinimizeWindow:boolean[, HideWindow:boolean]) → boolean
```

**Parameters**

- `MinimizeWindow` (boolean): `true` minimizes into the taskbar status area; `false` restores the window.
- `HideWindow` (boolean, optional, only relevant when `MinimizeWindow` is `true`): `true` hides the window without showing a status area icon; `false` (default) shows an icon.

**Return Value:** `boolean`

**Example**

```
hideBBL(true) // hides the Plant Simulation window
```

---

## isComputerAccessPermitted

Returns whether access to the computer is permitted for the executed Method (`true`) or not (`false`).

Access may be denied when: access is prohibited under *Model Settings > General > Prohibit Access to the Computer*, or the Method belongs to a library with prohibited access.

**Type:** Function

**Syntax**

```
isComputerAccessPermitted → boolean
```

**Return Value:** `boolean`

**Example**

```
print isComputerAccessPermitted
```

---

## isSet

Returns whether the value of a built-in attribute is set (`true`) or not (`false`).

Useful for values of drop-down lists in object dialogs (e.g. `ResourceType`). Independent of the model language.

**Type:** Function

**Syntax**

```
<Path>.isSet(ValueOfTheAttribute:string) → boolean
```

**Parameter**

- `ValueOfTheAttribute` (string): value of the attribute.

**Return Value:** `boolean`

**Example**

```
print MyStation.ResourceType 
// the value is Storage, outputs Storage or Lagerung in the Console
print MyStation.ResourceType.isSet("Storage") 
// checks, independent of the model language, if the value is Storage or 
Lagerung
```

---

## keepWindowsAlwaysOnTop

Sets whether Plant Simulation windows always appear on top of all open windows.

**Type:** Function

**Syntax**

```
keepWindowsAlwaysOnTop(WindowInForeground:boolean)
```

**Parameter**

- `WindowInForeground` (boolean): `true` keeps windows on top, `false` does not.

**Example**

```
keepWindowsAlwaysOnTop(true)
```

---

## language

Returns the model language selected under *File > Model Settings/Preferences > General > Model Language*.

**Type:** Function

**Syntax**

```
language → integer
```

**Return Value:** `integer` — `0` German, `1` English, `2` Japanese, `3` Chinese, `8` Hungarian.

**Example**

```
print language
```

---

## licenseName

Returns the name of the active Plant Simulation license.

**Type:** Function

**Syntax**

```
licenseName → string
```

**Return Value:** `string` — e.g. `EMPLANT_PRO` (Professional), `EMPLANT_STD` (Standard), `EMPLANT_FND` (Foundation/Essentials), `EMPLANT_APP` (Application), `EMPLANT_RUN` (Runtime), `EMPLANT_RES` (Research), `EMPLANT_EDU` (Educational), `EMPLANT_STUDENT` (Student), `EMPLANT_SIM` (Simulation), `EMPLANT_VIEW` (Viewer).

**Example**

```
print licenseName -- might return EMPLANT_PRO
```

---

## loadModel

Loads the specified simulation model.

**Type:** Function

**Syntax**

```
loadModel(ModelName:string[, Password:string]) → boolean
```

**Parameters**

- `ModelName` (string): path of the simulation model.
- `Password` (string, optional): password for opening an encrypted model file.

**Note:** Only works if no model is currently loaded (typically called after `closeModel` or from external interfaces such as COM).

**Return Value:** `boolean`

**Examples**

```
closeModel
loadModel("C:\MySimulationData\myModel.spp", "MyPassword123")
closeModel
loadModel("D:\MyModels\MyFolderModel.psfm\$.spp")
```

---

## makePathRelative

Converts an absolute path to a relative path.

**Type:** Function

**Syntax**

```
makePathRelative(Path:string[, StartObject:object]) → string
makePathRelative(Path:object[, StartObject:object]) → string
```

**Parameters**

- `Path` (string or object): path to convert; relative to the Frame containing the Method.
- `StartObject` (object, optional): object from which to start evaluating the path.

**Return Value:** `string` — empty string `""` if the path is invalid.

**Example**

```
Station.ExitCtrl := makePathRelative(Station.ExitCtrl)
```

---

## makeRGBValue

Generates the RGB color values of the specified color, usable in the `Color` attribute of Connector, Variable, Comment, and Display.

**Type:** Function

**Syntax**

```
<Path>.makeRGBValue(Red:integer, Green:integer, Blue:integer) → integer
```

**Parameters**

- `Red` (integer): red component (0–255).
- `Green` (integer): green component (0–255).
- `Blue` (integer): blue component (0–255).

**Return Value:** `integer`

**Example**

```
.Models.Model.BackgroundColor.Color := makeRGBValue(110,0,200)
.Models.Model.Connector.Color := makeRGBValue(100,0,200)
.Models.Model.Comment.Color := makeRGBValue(110,0,200)
.Models.Model.Display.Color := makeRGBValue(110,0,200)
.Models.Model.&Variable.Color := makeRGBValue(110,0,200)
```

---

## messageBox

Shows a message box provided by the operating system.

**Type:** Function

**Syntax**

```
messageBox(Text:string[, Buttons:integer[, Icons:integer]]) → integer
```

**Parameters**

- `Text` (string): text to show. To set a title bar, use `"|Title|Text"`. Use `strChr(10)` for line breaks.
- `Buttons` (optional): `1` OK; `3` OK/Cancel; `10` Repeat/Retry/Cancel; `48` Yes/No; `50` Yes/No/Cancel; `76` Abort/Retry/Ignore. Default: OK only.
- `Icons` (optional): `0` none; `1` error; `2` question mark; `3` exclamation mark; `4` info. Default: exclamation mark.

**Return Value:** `integer` — `1` OK; `2` Cancel; `4` Ignore/Continue; `8` Retry/Try Again; `16` Yes; `32` No.

**Examples**

```
switch messageBox("My message text, my text ... ",50, 3)
case 16 
   print "Yes"
case 32 
   print "No"
else
   print "Cancel"
end
messageBox("|My Company|This is a message.") // shows My Company in the 
title bar
```

---

## modelFile

Returns the name of the active model file and the folder within which it is located.

**Type:** Function

**Syntax**

```
modelFile → string
```

**Return Value:** `string`

**Example**

```
print modelFile // outputs for example D:\Public\Plant 
Models\MyPlantAnytown.spp
```

---

*Source: Plant Simulation Help (Miscellaneous Global Functions, A–M).*
