# SimTalk Access to Toolbox and Folder Library

Covers SimTalk programming interfaces for the Toolbox (toolbars) and the Folder in
the Class Library. For every object listed here, the methods and attributes are
also complemented by the **Methods of All Objects**.

> To inspect every method, read-only attribute, and attribute of an object:
> - Right-click the **Class Library** and select **Show Attributes and Methods**.
> - Press **F8** (or click **Show Attributes and Methods** on the Home ribbon) on a
>   selected **Instance** in a Frame.

## Syntax Convention

A typical signature line, e.g.

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` — path of the object the method applies to.
- Parentheses enclose the signature: identifier and parameter data type, e.g.
  `(Parameter:string)` accepts a constant, variable, or method-call result of the
  required type.
- **Note:** always include parentheses around nested expressions; omitting them
  may open the Debugger with unexpected results.
- Square brackets mark **optional** parameters, e.g. `[,Parameter:boolean]`.
- `:= default` after a parameter shows its default value.
- `→ type` shows the return value's data type.

---

## Part 1 — SimTalk Access to the Toolbox

The Toolbox (toolbars) exposes the methods, attributes, and read-only attributes
listed below, plus the Methods of All Objects.

### Visible `[toolbar]`

Shows or hides the selected toolbar in the Toolbox.

```simtalk
<Path>.Visible:boolean
```

- **Type:** Attribute
- **Assignment value:** boolean (true = show, false = hide)

```simtalk
-- hides the toolbar Materialflow in the Toolbox
.Materialflow.Toolbar.Visible := false
```

See also: `Visible [SimTalk] - Toolbar`.

---

### addObject `[SimTalk] - Toolbar`

Adds the icon of an object to the toolbar designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.addObject(Icon:object[, Position:integer]) → boolean`
- **Parameters**
  - `Icon:object` — full path of the object whose icon is added.
  - `Position:integer` *(optional)* — icon position on the toolbar. Position `01`
    sits right of the **Select** button.
- **Return value:** boolean

```simtalk
.MaterialFlow.Toolbar.addObject(.Materialflow.MyStation, 08)
-- adds the icon of MyStation to the toolbar Material Flow
-- and positions it to the right of the object Station
```

See also: *Add Objects to the Toolbox or Delete Them from It*.

---

### delObject `[SimTalk]`

Deletes the icon of an object from the toolbar designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.delObject(Icon:object) → integer`
- **Parameter**
  - `Icon:object` — full path of the object whose icon is removed.
- **Return value:** integer
  - The position of the button if the object existed on the toolbar.
  - `0` if it did not exist.

```simtalk
.MaterialFlow.Toolbar.delObject(.Materialflow.MyStation)
-- deletes the icon of MyStation from the toolbar Material Flow
```

See also: *Remove from Toolbar*, *Add Objects to the Toolbox or Delete Them from It*.

---

### redraw `[SimTalk] - Toolbar`

Redraws the toolbar designated by `<Toolbar-Path>` if it is displayed.

Useful when modifying a toolbar icon (e.g. via `setPixel [SimTalk]`) and you
want the change to be visible immediately.

- **Type:** Method
- **Syntax:** `<Toolbar-Path>.redraw`

```simtalk
var newFolder  : object := basis.createFolder
var newStation : object := .MaterialFlow.Station.derive(newFolder)
.MaterialFlow.Toolbar.addObject(newStation)
updateGUI
sleep(1, false)
newStation.createIcon("ToolboxIcon", 36, 36)
newStation.CurrIconNo := 0
for var y := 1 to 36
    for var x := 1 to 36
        newStation.setPixel(x, y, makeRGBValue(x*7, 0, y*7))
    next
next
.MaterialFlow.Toolbar.redraw
```

---

### Visible `[SimTalk] - Toolbar`

Hides (`false`) or shows (`true`) the toolbar designated by `<Path>` in the Toolbox.

- **Type:** Attribute
- **Syntax:** `<Path>.Visible:boolean`
- **Assignment value:** boolean

```simtalk
-- hides the toolbar Materialflow in the Toolbox
.Materialflow.Toolbar.Visible := false
```

See also: `Visible [toolbar]`.

---

## Part 2 — SimTalk Access to the Folder in the Class Library

The Folder in the Class Library exposes the methods, attributes, and read-only
attributes listed below, plus the Methods of All Objects.

To inspect the full set, see **Show Attributes and Methods** (F8 / context menu)
on the Class Library or on an instance in a Frame.

### createFolder `[SimTalk]`

Creates a new folder, either at root level under `Basis` in the Class Library or
in the folder designated by `<Folder-Path>`.

Plant Simulation assigns a default name (`NewFolder`, `NewFolder1`, ...). You can
rename it via the returned object's `Name`.

- **Type:** Method
- **Syntax**
  - `.createFolder → object`
  - `<Folder-Path>.createFolder → object`
- **Return value:** object

```simtalk
-- creates a new folder in the folder MaterialFlow and renames it to MyFolder
var obj : object := .MaterialFlow.createFolder
obj.Name := "MyFolder"

.createFolder                -- creates a folder in the class library
.MaterialFlow.createFolder   -- creates a folder in the folder MaterialFlow
```

See also: *New [Folder, Frame, Toolbar]*.

---

### createToolbar `[SimTalk]`

Creates a new toolbar, either at root level under `Basis` or in the folder
designated by `<Folder-Path>`.

Default name: `Toolbar`, `Toolbar1`, ... (rename via the returned object).

- **Type:** Method
- **Syntax**
  - `.createToolbar → object`
  - `<Folder-Path>.createToolbar → object`
- **Return value:** object

```simtalk
-- creates a new toolbar in the folder MaterialFlow
-- and renames it to MyMaterialfFlowToolbar
var obj : object := .MaterialFlow.createToolbar
obj.Name := "MyMaterialfFlowToolbar"

.createToolbar                -- creates a toolbar in the class library
.MaterialFlow.createToolbar   -- creates a toolbar in the folder MaterialFlow
```

See also: *New [Folder, Frame, Toolbar]*.

---

### getLibraryInfo `[SimTalk]`

Returns whether the folder designated by `<Folder-Path>` is a library (`true`)
or not (`false`). When it is a library, Plant Simulation also assigns the requested
library information to local variables.

- **Type:** Method
- **Syntax**

```
<Folder-Path>.getLibraryInfo(
    [byref Name:string,
     byref Version:string,
     byref Description:string,
     byref FilePathToLibrary:string,
     byRef IsProhibited:boolean,
     byRef AlternativePaths:string]) → boolean
```

- **Parameters** (1 to 7 optional `byref` locals)
  - `Name:string` — library name.
  - `Version:string` — library version.
  - `Description:string` — library description.
  - `FilePathToLibrary:string` — file path of the library file (`.pslib`); useful
    when loading data from a file located in the same directory as the `.pslib`.
  - `IsProhibited:boolean` — `true` if library methods cannot access the computer;
    `false` if they can.
  - `AlternativePaths:string` — alternative paths of the library; multiple paths
    are separated by a line break (`strAscii(10)`).
- **Return value:** boolean

```simtalk
.Tools.MyLibrary.getLibraryInfo(MyLibraryName, MyLibraryVersion)
```

See also: `setLibraryInfo`, `getLibraryVersionFromFile`, *Make Library*,
*Prohibit Access to the Computer [Make Library]*.

---

### HiddenWhenInLockedFolder `[SimTalk]`

Controls whether the folder designated by `<Folder-Path>` is hidden in the Class
Library when located inside a locked folder (`true`), or still shown (`false`).

- **Type:** Attribute
- **Syntax:** `<Folder-Path>.HiddenWhenInLockedFolder:boolean`
- **Assignment value:** boolean

```simtalk
.Models.MyFolder.MyUser.HiddenWhenInLockedFolder := true
```

See also: `lockFolder`.

---

### IsLocked `[SimTalk]`

Returns whether the folder designated by `<Folder-Path>` is a locked library.

- **Type:** Read-only attribute
- **Syntax:** `<Folder-Path>.IsLocked → boolean`
- **Return value:** boolean

```simtalk
print .MyFolder.IsLocked
```

See also: *Lock Library*.

---

### loadObjectAs `[SimTalk]`

Loads an object (saved to a `.psobj` file) into the folder designated by
`<Folder-Path>`. In most cases this is the Class Library itself, designated by
`.` or `basis`.

- **Type:** Method
- **Syntax**

```
<Folder-Path>.loadObjectAs(
    Object:string
    [, NewName:string,
     Automerge:boolean:=false,
     ReplaceExistingClass:boolean:=false,
     Password:string]) → object
```

- **Parameters**
  - `Object:string` — the object to load.
  - `NewName:string` *(optional)* — new name for the object. Pass an empty string
    `""` to keep the existing name while still defining the boolean parameters
    that follow.
  - `Automerge:boolean:=false` — when `true`, classes that already exist in the
    Class Library are merged automatically and no Merge Report is created.
    When `false`, Plant Simulation opens a dialog for manual merging.
  - `ReplaceExistingClass:boolean:=false` — only meaningful when `Automerge=true`.
    When `true`, newly loaded classes replace the existing ones; when `false`,
    existing classes are preserved. (Equivalent to **Save/Load > Update Class
    Library** vs. **Save/Load > Load Object** in the Class Library context menu.)
    > When loading a library, this parameter has no effect — Plant Simulation
    > decides based on the version number whether to update.
  - `Password:string` *(optional)* — password for encrypted object files.
- **Return value:** object

```simtalk
-- loads the object named protocol and automatically merges it
.loadObjectAs("C:\Users\MyName\protocol.psobj", "Protocol", true, false)
Protocol.CurrIcon := "operational"
```

See also: `autoexecLoadObj`.

---

### lockFolder `[SimTalk]`

Locks the folder designated by `<Folder-Path>` with a password. Plant Simulation
prevents objects inside a locked folder from being opened interactively.

To unlock: clear *Lock Library* in **Manage Class Library** and enter the password,
or hold **Shift** while clicking **OK** on the error message — the password is
then prompted and the lock is temporarily suppressed until the model is saved
and reopened. Information-flow changes are still possible. Instances of locked
objects that have been inserted into Frames outside the locked folder are not
affected.

- **Type:** Method
- **Syntax**

```
<Folder-Path>.lockFolder(
    Lock:boolean/void,
    OldPassword:string
    [, NewPassword:string/void, EncryptMethods:boolean])
```

- **Parameters**
  - `Lock:boolean/void` — `true` locks folder and sub-folders, `false` unlocks
    (and removes any inherited lock from a surrounding folder), `void` removes
    the lock and reactivates a possibly existing lock from the surrounding
    folder.
  - `OldPassword:string` — current password (required when re-locking an already
    locked folder; ignored if the folder was never locked).
  - `NewPassword:string/void` *(optional)* — new password. Only required when
    `Lock=true`. Pass `""` to set no password (then the only way to remove the
    lock is to enter the current password).
  - `EncryptMethods:boolean` *(optional)* — `true` encrypts all unencrypted
    methods in the folder; `false` (default) leaves them as-is. Ignored if
    `Lock≠true`.
- **Return value:** void

```simtalk
.Models.MyFolder.MyUser.lockFolder(true, "My Old Password", "MyNewPassword")
.Models.MyFolder.MyUser.lockFolder(true, "My Old Password", "")   -- no new password
```

See also: `HiddenWhenInLockedFolder`, `IsLocked`, *Lock Library*.

---

### node `[SimTalk] - folder`

Returns an object within the folder designated by `<Folder-Path>`. Objects in a
folder are numbered in the order in which you insert them.

- **Type:** Method
- **Syntax:** `<Folder-Path>.node(ObjectNumberOrName:integer) → object`
- **Parameter**
  - `ObjectNumberOrName:integer` — the object's index or its name.
- **Return value:** object

```simtalk
print .Models.MnEnginePlant.node(5)
-- returns the path and name of the object, e.g. .Models.EnginePlant.Track
```

See also: `numNodes [SimTalk] - folder`.

---

### numNodes `[SimTalk] - folder`

Returns the number of objects in the folder designated by `<Folder-Path>`.
Each sub-folder counts as one object; objects contained within sub-folders are
**not** counted.

- **Type:** Method
- **Syntax:** `<Folder-Path>.numNodes → integer`
- **Return value:** integer

```simtalk
print .Models.MyPlant.numNodes
```

See also: `node [SimTalk] - folder`.

---

### pasteClipboard `[SimTalk] - class library`

Pastes the contents of the clipboard into the folder designated by `<Folder-Path>`.

- **Type:** Method
- **Syntax:** `<Folder-Path>.pasteClipboard([TargetTableOfPastedObjects:table])`
- **Parameter**
  - `TargetTableOfPastedObjects:table` *(optional)* — after the method runs,
    Plant Simulation writes all pasted objects into this table. The table must
    have one column of data type `object`.

```simtalk
var tbl : table
pasteClipboard(tbl)
for var i := 1 to tbl.yDim
    print tbl[1, i]   -- returns all pasted objects
next

.Materialflow.pasteClipboard(MyPastedObjects)
```

See also: *Paste [object class]*.

---

### setLibraryInfo `[SimTalk]`

Marks the folder designated by `<Folder-Path>` as a library and sets its name
and version.

- **Type:** Method
- **Syntax**

```
<Folder-Path>.setLibraryInfo(
    Name:string,
    Version:string
    [, Description:string, AccessProhibited:boolean])
```

- **Parameters**
  - `Name:string` — library name.
  - `Version:string` — library version; numbers separated by periods.
  - `Description:string` *(optional)* — library description. If omitted, the
    current description is preserved.
  - `AccessProhibited:boolean` *(optional)* — `true` prohibits the library from
    accessing the computer (preserves the **Prohibit Access to the Computer**
    flag). If omitted, the existing setting is preserved.
  - > The value `false` is not accepted for `AccessProhibited`: for security
    > reasons, a library cannot be granted computer access through information
    > flow this way.
- **Return value:** void

See also: `getLibraryInfo`, *Make Library*.

---

### setRequiredLicense `[SimTalk]`

Tells the library folder designated by `<Folder-Path>` to request a user-defined
license. When loading a model or object that contains such a library, Plant
Simulation checks the Windows Registry for a license with the matching feature
name, version, Host-ID, validity date, and password.

Use cases:

- Restrict passing on of a simulation model → call `basis.setRequiredLicense`,
  then save the model.
- Restrict passing on of a library → call `setRequiredLicense` on the library
  folder, then save the library.

When updating a library that requires a user-defined license, the new version
must request the same feature, request at least the same version number, and be
protected with the same password. To change the password across an update, call
`setRequiredLicense` first with an empty `Feature` and the old `Password` to
deregister, then again with the new feature/password and the old password as
`PreviousPasswordForUpdate`.

- **Type:** Method
- **Syntax**

```
<Folder-Path>.setRequiredLicense(
    Feature:string,
    Version:string,
    Password:string
    [, FreeInLicense:string,
     Comment:string,
     PreviousPasswordForUpdate:string])
```

- **Parameters**
  - `Feature:string` — license feature name. Pass `""` to remove an existing
    license (correct password required).
  - `Version:string` — requested version; the registered version must be `≥`
    this value.
  - `Password:string` — secret password; the registered license password must
    match this value.
  - `FreeInLicense:string` *(optional)* — license tier in which the license
    becomes free. Allowed values:

    | Value | Meaning |
    |-------|---------|
    | `"-"`            | Never free, not even in Viewer. |
    | `""` *(default)* | Only free in Viewer license. |
    | `"Simulation"`   | Free in Simulation and Viewer. |
    | `"Runtime"`      | Free in Runtime, Simulation, Viewer. |
    | `"Application"`  | Free in Application, Runtime, Simulation, Viewer. |
    | `"Educational"`  | Free in Educational, Runtime, Simulation, Viewer. |

  - `Comment:string` *(optional)* — text appended to the message window
    notification when no matching license exists on load.
  - `PreviousPasswordForUpdate:string` *(optional)* — previous password of the
    library; required when migrating to a new password.
- **Return value:** void

```simtalk
.Standard.MyLibrary.setRequiredLicense(
    "MyFeature", "9.5.7", "MySecretPassword123")
```

User-defined licenses can be generated via the SimTalk function `createLicenseFile`.

See also: `checkForLicense`, `createLicenseFile`.

---

### ShowToolbar `[SimTalk]`

Shows (`true`) or hides (`false`) the toolbar of the specified folder in the
Class Library inside the Toolbox.

- **Type:** Attribute
- **Syntax:** `<Folder-Path>.ShowToolbar:boolean`
- **Assignment value:** boolean

```simtalk
.MaterialFlow.ShowToolbar := false
```

See also: *Show Toolbar*.

---

## Part 3 — Console

The **Console** window shows information about actions Plant Simulation executes.

- Configure which information is shown under
  **File > Preferences > User Interface > Console Filter**.
- To **record** messages, display the Console via the **Window** ribbon tab.
  To **stop** recording, hide it.
- **Close** the Console via the X in its title bar; reopen it from the Window
  ribbon tab.
- **Auto Hide** collapses the window when you click elsewhere and expands again
  when you hover its name. Click the Auto Hide pin to deactivate.

Context menu commands:

- **Copy** — copies selected text.
- **Clear** — clears the Console contents.
- **Select All** — selects all text in the Console.
- **Show Print Output** — toggles output from `print` statements in methods.
- **Show Info Output** — toggles text from info boxes (e.g. reset/init phases,
  warnings, etc.).