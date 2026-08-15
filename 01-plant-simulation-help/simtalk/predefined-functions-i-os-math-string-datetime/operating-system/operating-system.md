# Operating System Functions (SimTalk)

Plant Simulation provides predefined functions you can use in your controls. Functions are not object-specific; they apply in general.

SimTalk provides the functions below for accessing functions of the operating system.

---

## availableMemory

Returns the entire amount of main memory available in megabytes.

- **Type:** Function
- **Syntax:** `availableMemory → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print availableMemory
```

---

## browseForFolder

Opens a dialog that MS Windows provides, in which you can select the folder to be opened or create a new folder.

- **Type:** Function
- **Syntax:** `browseForFolder(Message:string) → string`
- **Parameter:** `Message` (string) — the message you want to show to the user.
- **Return Value:** The return value has the data type `string`.

**Example:**

```simtalk
browseForfolder("Select the folder you would like to open:")
```

---

## copyFile

Copies a file from one location to another location.

- **Type:** Function
- **Syntax:** `copyFile(Source:string, Destination:string) → boolean`
- **Parameters:**
  - `Source` (string) — the file you want to copy.
  - `Destination` (string) — the folder into which you want to copy it.
- **Return Value:** The return value has the data type `boolean`.
  - `true` if copying was successful.
  - `false` if it failed.

**Remarks:** If you deactivate the safety setting *File > Model Settings > General > Prohibit Access to the Computer*, `copyFile` can copy data from another folder and write it to the model folder or its sub-folders. It cannot copy files *from* the model folder or its sub-folders.

**Example:**

```simtalk
copyFile("C:\file.txt", "C:\temp\file.txt")
```

**See also:** Prohibit Access to the Computer [model settings]

---

## copyObjectsToClipboard

Copies one or several objects to the internal Plant Simulation clipboard.

- **Type:** Function
- **Syntax:** `copyObjectsToClipboard(Objects:object/object[])`
- **Parameter:** `Objects` (object or object[]) — a single object or an array of objects.

**Remarks:** Copying an object to the clipboard deletes the previous contents of the clipboard.

**Note:** A Connector can only be copied to the clipboard successfully if its predecessor object and its successor object are copied as well.

**Example:**

```simtalk
var objs: object[]
objs := [Station, Station1, Connector]
copyObjectsToClipboard(objs)
.Models.Frame2.pasteClipboard
```

**See also:** `pasteClipboard` [SimTalk] - Frame

---

## copyTextToClipboard

Copies the specified text to the clipboard.

- **Type:** Function
- **Syntax:** `copyTextToClipboard(TextToBeCopied:string)`
- **Parameter:** `TextToBeCopied` (string) — the text you want to copy.

**Remarks:** Copying text to the clipboard deletes the previous contents of the clipboard.

**Example:**

```simtalk
copyTextToClipboard("My long text, text, text.")
```

**See also:** `getTextFromClipboard` [SimTalk]

---

## getApplicationProcessID

Returns the current process identifier (PID) of the current Plant Simulation session.

- **Type:** Function
- **Syntax:** `getApplicationProcessID → integer`
- **Return Value:** The return value has the data type `integer`.

**Example:**

```simtalk
print getApplicationProcessID -- might return 8252 for the Plant Simulation process
```

**See also:** `system` [SimTalk], `startExtProc` [SimTalk]

---

## getCurrentDirectory

Returns the current Plant Simulation working folder.

- **Type:** Function
- **Syntax:** `getCurrentDirectory → string`
- **Return Value:** The return value has the data type `string`.

**Example:**

```simtalk
print getCurrentDirectory
```

**See also:** `setCurrentDirectory` [SimTalk], Specifying Start Options, `-cwd dir`

---

## getEnv

Returns the specified environment variable of the operating system.

- **Type:** Function
- **Syntax:** `getEnv(EnvironmentVariable:string) → string`
- **Parameter:** `EnvironmentVariable` (string) — the environment variable.
- **Return Value:** The return value has the data type `string`. It is an empty string `""` if the variable does not exist.

**Example:**

```simtalk
print getEnv("PATH")
```

**See also:** `setEnv` [SimTalk]

---

## getFilesOfFolder

Returns a list of all files and folders which match the specified search pattern.

- **Type:** Function
- **Syntax:** `getFilesOfFolder(SearchPattern:string) → list`
- **Parameter:** `SearchPattern` (string) — the directory and the search pattern.
  - The asterisk `*` in the search pattern designates any string.
  - The question mark `?` in the search pattern designates a single character.
- **Return Value:** The return value has the data type `list`.

**Example:**

```simtalk
var allFiles, executables: list
allFiles := getFilesOfFolder("C:\Temp\*")            // returns a list of all files and folders within the 'Temp' folder
executables := getFilesOfFolder("C:\Windows\*.exe")  // returns a list of all executables within the 'Windows' folder
```

---

## getRegistry

Returns a key from the folders `HKEY_CLASSES_ROOT`, `HKEY_CURRENT_USER`, and `HKEY_LOCAL_MACHINE` in the MS Windows Registry Editor.

- **Type:** Function
- **Syntax:** `getRegistry(Key:string, Value:string)`
- **Parameters:**
  - `Key` (string) — the key in a folder.
  - `Value` (string) — the value of the key.
- **Return Values:** The function returns values of these data types:
  - `void` if the value does not exist
  - `integer` for a DWORD value (REG_DWORD)
  - `string` in all other cases (REG_SZ, REG_EXPAND_SZ, REG_MULTZI_SZ, REG_BINARY)

**Example:**

```simtalk
print getRegistry("HKEY_LOCAL_MACHINE\SOFTWARE\Siemens\Tecnomatix Plant Simulation 2606", "")
// returns the folder in which Plant Simulation is installed
```

---

## getTextFromClipboard

Copies text from the MS Windows clipboard and returns it as a string.

- **Type:** Function
- **Syntax:** `getTextFromClipboard → string`
- **Return Value:** The return value has the data type `string`.

**Example:**

```simtalk
print getTextFromClipboard // returns text from the Clipboard
```

**See also:** `copyTextToClipboard`

---

## selectFileForOpen

Opens the dialog *Open* in which the user can select the file he wants to open.

- **Type:** Function
- **Syntax:**
  ```simtalk
  selectFileForOpen([FileFilter:string]) → string
  selectFileForOpen(["Text Files (*.txt)|*.txt||"]) → string
  selectFileForOpen(["Text Files (*.txt, *.doc)|*.txt;*.doc||"]) → string
  selectFileForOpen(["Model Files (*.spp, *.psobj)|*.spp;*.psobj|Text Files (*.txt, *.doc)|*.txt;*.doc||"]) → string
  selectFileForOpen([FileFilter:string, PredefinedName:string]) → string
  ```
- **Parameters:**
  - You can call `selectFileForOpen` with filters as parameters. These filters conform to the conventions set forth by Microsoft: `Comment1 | FileFilter1 | Comment2 | FileFilter2 ||`. Windows shows this Comment (which designates the type of file) in the text box *File type*. It only shows the types of files whose extensions you entered as the `FileFilter`. To show several file types, separate the individual types with a pipe `|` sign. Terminate the string with two pipes `||`.

  | To show in the text box *File type* | File Type |
  |---|---|
  | all text files with extension `.txt` | `selectFileForOpen("Text Files (*.txt)|*.txt||")` |
  | all text files with extension `.txt` and `.doc` | `selectFileForOpen("Text Files (*.txt, *.doc)|*.txt;*.doc||")` |
  | all files with extension `.spp`, `.psobj`, `.txt`, and `.doc` | `selectFileForOpen("Model Files (*.spp, *.psobj)|*.spp;*.psobj|Text Files (*.txt, *.doc)|*.txt;*.doc||")` |

  - The optional parameter `PredefinedName` (string) — the default path, i.e., the folder in which Plant Simulation opens the file selection box.
- **Return Value:** The return value has the data type `string`. If the user clicks Cancel, Plant Simulation returns an empty string `""`.

**Examples:**

```simtalk
var str: string
str := selectFileForOpen
if str /= ""
   statTable.readFile(str)
end
```

```simtalk
selectFileForOpen("", "C:\\Temp\\")
selectFileForOpen("Text Files (*.txt)|*.txt||", "C:\\Temp\\")
```

**See also:** Open Model File

---

## selectFileForSave

Opens the dialog *Save As* and lets you type in the file location.

- **Type:** Function
- **Syntax:**
  ```simtalk
  selectFileForSave([FileFilter:string, PredefinedName:string]) → string
  selectFileForSave("Text Files (*.txt)|*.txt||") → string
  selectFileForSave("Text Files (*.txt, *.doc)|*.txt;*.doc||") → string
  selectFileForSave("Model Files (*.spp, *.psobj)|*.spp;*.psobj|Text Files (*.txt, *.doc)|*.txt;*.doc||") → string
  ```
- **Parameters:**
  - The optional parameter `FileFilter` (string) — the file filter. These filters conform to the conventions set forth by Microsoft: `Comment1 | FileFilter1 | Comment2 | FileFilter2 ||`. Windows shows this Comment in the text box *File type*. When you want to show several file types, separate the individual types with a pipe `|` sign. Terminate the string with two pipes `||`.

  | To show in the text box *File type* | File Type |
  |---|---|
  | all text files with extension `.txt` | `selectFileForSave("Text Files (*.txt)|*.txt||")` |
  | all text files with extension `.txt` and `.doc` | `selectFileForSave("Text Files (*.txt, *.doc)|*.txt;*.doc||")` |
  | all files with extension `.spp`, `.psobj`, `.txt`, and `.doc` | `selectFileForSave("Model Files (*.spp, *.psobj)|*.spp;*.psobj|Text Files (*.txt, *.doc)|*.txt;*.doc||")` |

  - The optional parameter `PredefinedName` (string) — the predefined file name. The dialog shows this name in the text box *File Name*; the user can overwrite it though.
- **Return Value:** The return value has the data type `string`. It is an empty string `""` if the user clicks Cancel.

**Remarks:** The user has to enter a name for the file to be saved into the text box *File Name* or select an existing name from the list shown by the dialog.

**Examples:**

```simtalk
var str: string
str := selectFileForSave
if str /= ""
   saveModel(str)
end
```

```simtalk
selectFileForSave("Model Files (*.spp, *.psobj)|*.spp;*.psobj|Text Files (*.txt, *.doc)|*.txt;*.doc||", "MyModel.spp")
```

**See also:** Save Model File As

---

## setCodePage

Sets the code page for exchanging data in ANSI format via certain interfaces, for example the Oracle interface.

- **Type:** Function
- **Syntax:** `setCodePage([CodePageName:integer])`
- **Parameter:** `CodePageName` (integer) — the number of the code page.
- **Return Value:** The return value has the data type `integer`. It is the previous value of the code page before it was changed.

**Example:**

```simtalk
setCodePage(932)   // Japanese
setCodePage(936)   // Chinese
setCodePage(1250)  // Hungarian
setCodePage(1252)  // English, German
setCodePage(0)     // sets the code page of the operating system
print setCodePage  // returns the current code page
```

**See also:** Specifying Start Options, `/Codepage`

---

## setCurrentDirectory

Sets the current working folder for Plant Simulation.

- **Type:** Function
- **Syntax:** `setCurrentDirectory(WorkingFolder:string) → boolean`
- **Parameter:** `WorkingFolder` (string) — the working folder.
- **Return Value:** The return value has the data type `boolean`.
  - `true` if the working folder was set successfully.
  - `false` if the working folder was not set.

**Remarks:** If you deactivate the safety setting *File > Model Settings > General > Prohibit Access to the Computer*, `setCurrentDirectory` can copy data from another folder and write it to the model folder or its sub-folders. It cannot copy files *from* the model folder or its sub-folders.

**Example:**

```simtalk
print setCurrentDirectory("C:\users\hank")
```

**See also:** Prohibit Access to the Computer [model settings], `getCurrentDirectory` [SimTalk], Specifying Start Options, `-cwd dir`

---

## setEnv

Sets the specified environment variable.

- **Type:** Function
- **Syntax:** `setEnv(EnvironmentVariable:string, Value:string) → boolean`
- **Parameters:**
  - `EnvironmentVariable` (string) — the name of the variable.
  - `Value` (string) — its value.
- **Return Value:** The return value has the data type `boolean`.

**Remarks:** If you deactivate the safety setting *File > Model Settings > General > Prohibit Access to the Computer*, Plant Simulation does not run `setEnv` and shows an error message.

**Examples:**

```simtalk
setEnv("ralf","0")
startExtProc("PlantSimulation2606.exe")
```

In the external process you just started you can then query the value you set:

```simtalk
print getEnv("ralf") // returns the value of the variable
```

**See also:** Prohibit Access to the Computer [model settings], `getEnv` [SimTalk]

---

## SHGetKnownFolderPath

Returns the path of a standard folder in the file system of your computer.

- **Type:** Function
- **Syntax:** `SHGetKnownFolderPath(CLSID:string) → string`
- **Parameter:** `CLSID` (string) — a standard folder in the file system of your computer. For more information, consult KNOWNFOLDERID.
- **Return Value:** The return value has the data type `string`.

**Example:**

```simtalk
print SHGetKnownFolderPath("{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}")
// returns the path to the Desktop, for example C:\Users\MyLoginName\Desktop
```

**See also:** https://docs.microsoft.com/en-us/windows/win32/shell/knownfolderid

---

## sleep

Suspends a Method for the specified time. The time is not the simulation time of the EventController, but the real-time of your computer's clock.

- **Type:** Function
- **Syntax:** `sleep(Time:real[, SuspendProcess:boolean:=true])`
- **Parameters:**
  - `Time` (real) — the amount of time in seconds in real-time for which the Method will be suspended.
  - `SuspendProcess` (boolean, optional) — determines if `sleep` suspends the Plant Simulation process for the time in seconds designated by the `Time` parameter (`true`). This is especially helpful when starting other processes from Plant Simulation and you do not want Plant Simulation to consume CPU time. If you enter `false`, Plant Simulation will not be blocked for the time span, but only stops executing the Method. This way `sleep` works like a `wait`-instruction — the only difference is that the time during which `sleep` waits is real-time, while the time for `wait` is simulation time.
- **Default Value of the Parameter:** `true`

**Example:**

```simtalk
sleep(3.5, false)
```

**See also:** `wait` [SimTalk]

---

## startExtProc

Starts the specified external process.

- **Type:** Function
- **Syntax:** `startExtProc(PathToProgram:string[, Visible:boolean, WaitUntilProcessTerminated:boolean]) → integer`
- **Parameters:**
  - `PathToProgram` (string) — the external process. This usually is a program with a graphical user interface that does not have a Console. Plant Simulation itself will continue to be executed while the external process is open. Enter a double-backslash `\\` as a path separator. The function either returns the process ID (PID) or it returns `0` if the function fails.
  - `Visible` (boolean) — sets if the started program is to be visible (`true`) or not (`false`). If you do not specify the parameter, the program window will be visible.
  - `WaitUntilProcessTerminated` (boolean) — sets if the function is to wait until the started program was terminated (`true`) or not (`false`). If you do not specify the parameter, the function does not wait, i.e., the instructions which follow after `startExtProc` will be executed immediately.
- **Return Value:** The return value has the data type `integer`.

**Remarks:** If you deactivate the safety setting *File > Model Settings > General > Prohibit Access to the Computer*, Plant Simulation does not execute `startExtProc` and shows an error message.

**Note:** If the command window distracts you from a system command, for example `system("dir file.txt")`, you can hide the command window with the function `startExtProc`, for example `startExtProc("cmd.exe /C dir file.txt", false, true)`.

**Example:**

```simtalk
startExtProc("C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe")
```

**See also:** Prohibit Access to the Computer [model settings], `system` [SimTalk], `getApplicationProcessID` [SimTalk]

---

## system

Executes the specified system command during the simulation run. Plant Simulation will be blocked until the system command is completely executed.

- **Type:** Function
- **Syntax:** `system(Command:string) → integer`
- **Parameter:** `Command` (string) — the command.
- **Return Value:** The return value has the data type `integer`. It is identical with the exit state of the command.

**Remarks / Notes:**
- You can only specify DOS commands. Always start programs with a graphical user interface using the function `startExtProc` or programs will block each other.
- If you deactivate the safety setting *File > Model Settings > General > Prohibit Access to the Computer*, Plant Simulation does not execute `system` and shows an error message.

**Example:**

```simtalk
if system("del C:\temp\file.txt") = 0
   print "file deleted"
end
```

**See also:** Prohibit Access to the Computer [model settings], `startExtProc` [SimTalk]
