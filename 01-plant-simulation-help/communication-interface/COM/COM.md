# COM Interface

Use the COM object to control Plant Simulation from other applications by entering `Tecnomatix.PlantSimulation.RemoteControl`. This starts the most recent version. If multiple versions are installed, specify the version with `Tecnomatix.PlantSimulation.RemoteControl.<Major>.<Minor>`, for example `Tecnomatix.PlantSimulationRemote.Control.26.0`.

## Remarks

You might, for example, start a simulation run in Plant Simulation from Microsoft Excel and then write the results into an Excel table. You can use the COM Interface to control Plant Simulation from any application that can address COM objects. This includes all Office applications, the Windows Scripting Host, and many other applications.

The type of the interface is `IRemoteControl`:

```cpp
interface IRemoteControl : IDispatch
{
     HRESULT NewModel();
     HRESULT LoadModel(BSTR);
     HRESULT SaveModel(BSTR);
     HRESULT CloseModel();
     HRESULT StartSimulation(BSTR);
     HRESULT StopSimulation();
     HRESULT ResetSimulation(BSTR);
     HRESULT IsSimulationRunning([out,retval]VARIANT_BOOL*);
     HRESULT SetPathContext(BSTR);
     HRESULT ExecuteSimTalk(BSTR,[optional]VARIANT,[out,retval]VARIANT*);
     HRESULT GetValue(BSTR,[out,retval]VARIANT*);
     HRESULT SetValue(BSTR,VARIANT);
     HRESULT Quit();
};
```

The COM Interface is part of the Plant Simulation Interface Package.

## Initialization (JScript)

The examples below are for the Windows Scripting Host using the syntax of JScript. They assume that Plant Simulation was initialized with:

```js
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
```

## Functions of the COM Interface

### CloseModel

Closes the active simulation model.

- **Type:** Function
- **Syntax:** `PlantSim.CloseModel`

**Remarks:** This corresponds to the command Close Model on the Quick Access Toolbar.

You can also define a Method with the name `onCloseModel` in any folder in the Class Library, including the Basis folder. This method is executed when you close the model or when you exit the application. You can, for example, program clean-up tasks, delete temporary files, etc.

The method `onCloseModel` has to declare the boolean parameter `onExitApplication`. Plant Simulation sets this parameter to `false` when `onCloseModel` is called when you close the model. Plant Simulation sets this parameter to `true` when `onCloseModel` is called when you exit Plant Simulation.

You can also program several `onCloseModel` methods and place them into different folders. Plant Simulation then calls all existing `onCloseModel` method classes in the Class Library when you close the model or exit the application.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.CloseModel("C:\\Models\\MyCOMTest.spp")
```

### ExecuteSimTalk

Executes the source code, which you specify, in a Method.

- **Type:** Function
- **Syntax:** `PlantSim.ExecuteSimTalk(SourceCode:string[, Parameter1, Parameter2, Parameter3]) -> any`

**Parameters:**

- `SourceCode` (string) — designates the source code, which is going to be executed in the Method.
- `Parameter1`, `Parameter2`, `Parameter3` (optional) — allow to pass up to three arguments to the SimTalk method contained in the first argument.

When the source code of the method contains a parameter, you can enter this as the second parameter into the method `ExecuteSimTalk`. The method then returns the return value of the method.

**Return Value:** The return value has the data type `any` — it is the return value of the Method.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.ExecuteSimTalk("->real; return 3.14159")
PlantSim.ExecuteSimTalk("param r:real->real; return r*r", 3.14159)
```

### GetValue

Returns the value of the specified attribute of the designated Plant Simulation object.

- **Type:** Function
- **Syntax:** `PlantSim.GetValue(ObjectName:string) -> any`

**Parameter:** `ObjectName` (string) — designates the name of the Plant Simulation object and the name of the attribute.

**Return Value:** The return value has the data type `any`.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.GetValue(".Models.Model.MyStation.ProcTime")
```

### IsSimulationRunning

Returns if the simulation is running at the moment (`true`) or if it is not running (`false`).

- **Type:** Function
- **Syntax:** `PlantSim.IsSimulationRunning -> boolean`

**Return Value:** The return value has the data type `boolean`.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.IsSimulationRunning
```

### LoadModel

Loads the specified Plant Simulation simulation model.

- **Type:** Function
- **Syntax:** `PlantSim.LoadModel(ModelName:string[, Password:string])`

**Remarks:** `LoadModel` corresponds to the command Open Model on the Quick Access Toolbar. The function does not load call chains.

**Parameters:**

- `ModelName` (string) — designates the name of the model that you want to open.
- `Password` (string, optional) — designates the password used for loading an encrypted model.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.LoadModel("C:\\Modely\MyCOMTest.spp")
```

### NewModel

Creates a new simulation model.

- **Type:** Function
- **Syntax:** `PlantSim.NewModel(FilePath:string)`

**Remarks:** `NewModel` corresponds to the command New Model on the Quick Access Toolbar.

**Parameter:** `FilePath` (string) — designates the name of the new model.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.NewModel("C:\\Models\MyCOMModel.spp")
```

### OpenConsoleLogFile

Routes the output of the Plant Simulation Console to a file.

- **Type:** Function
- **Syntax:** `PlantSim.OpenConsoleLogFile(FilePath:string)`

**Remarks:** To terminate routing to the file, specify an empty string `""`.

**Parameter:** `FilePath` (string) — designates the path to the file into which the Console output is going to be written.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.OpenConsoleLogFile("C:\\temp\\MyConsoleProtocolFile.txt")
```

### Quit

Exits Plant Simulation.

- **Type:** Function
- **Syntax:** `PlantSim.Quit`

**Remarks:** `Quit` corresponds to the command Exit on the Quick Access Toolbar.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.Quit
```

### QuitAfterTime

Exits Plant Simulation after the specified time in milliseconds has passed.

- **Type:** Function
- **Syntax:** `PlantSim.QuitAfterTime(Time:integer)`

**Parameter:** `Time` (integer) — designates the time after which Plant Simulation will be terminated.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.QuitAfterTime(10)
```

### ResetSimulation

Resets the EventController.

- **Type:** Function
- **Syntax:** `PlantSim.ResetSimulation(PathOfEventController:string)`

**Remarks:** `ResetSimulation` corresponds to the Reset Simulation button of the EventController.

**Parameter:** `PathOfEventController` (string) — designates the path of the EventController.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.ResetSimulation(".Models.Model.EventController")
```

### SaveModel

Saves the active simulation model with the name you specify.

- **Type:** Function
- **Syntax:** `PlantSim.SaveModel(ModelName:string)`

**Remarks:** `SaveModel` corresponds to the command Save Model on the Quick Access Toolbar.

**Parameter:** `ModelName` (string) — designates the name of the model.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.SaveModel("Plant Cedar Rapids, Iowa")
```

### SetLicenseType

Sets the license type that is going to be used for Plant Simulation.

- **Type:** Function
- **Syntax:** `PlantSim.SetLicenseType(LicenseType:string)`

**Parameter:** `LicenseType` (string) — designates the license type.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.SetLicenseType("Professional")
```

### SetNoMessageBox

Shows a message box (`true`) or hides it (`false`).

- **Type:** Function
- **Syntax:** `PlantSim.SetNoMessageBox(Value:boolean)`

**Parameter:** `Value` (boolean) — sets if Plant Simulation shows a message box (`true`) or not (`false`).

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.SetNoMessageBox(true)
```

### SetPathContext

Sets where a relative path starts.

- **Type:** Function
- **Syntax:** `PlantSim.SetPathContext(StartOfRelativePath:string)`

**Parameter:** `StartOfRelativePath` (string) — designates the start of the relative path.

Note: The function only applies to the methods `getValue` and `setValue`.

**Example:**

```js
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.SetPathContext(".Models.Study1")
PlantSim.GetValue("MyStation.ProcTime")
// accesses .Models.Study1.MyStation.ProcTime
```

### SetSuppressStartOf3D

Sets if Plant Simulation suppresses starting 3D or not.

- **Type:** Function
- **Syntax:** `PlantSim.SetSuppressStartOf3D(Value:boolean)`

**Parameter:** `Value` (boolean) — sets if Plant Simulation suppresses starting of 3D (`true`) or not (`false`).

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.SetSuppressStartOf3D(true)
```

### SetTrustModels

Sets if the COM Interface permits models to have access to the computer or not.

- **Type:** Function
- **Syntax:** `PlantSim.SetTrustModels(Trust:boolean)`

**Parameter:** `Trust` (boolean) — sets if the COM Interface permits models to have access to the computer (`true`) or not (`false`). Specifying `true` corresponds to the start option `/TrustModels`, meaning that general access to the computer is permitted and that model-specific or library-specific settings are overridden.

**Example:**

```js
// JScipt
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.SetVisible(true)
PlantSim.SetTrustModels(true)
```

### SetValue

Assigns a value to an attribute of a Plant Simulation object.

- **Type:** Function
- **Syntax:** `eMPlant.SetValue(NameOfObject:string, AttributeValue:any)`

**Parameters:**

- `NameOfObject` (string) — designates the name of the object and its attribute.
- `AttributeValue` (any) — designates the value of the attribute.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.SetValue("Station.Proctime",120)

// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.SetValue(".Models.Model.MyDataTable[2,1]", 3)
```

### SetVisible

Makes the application Plant Simulation visible (`true`) or invisible (`false`).

- **Type:** Function
- **Syntax:** `eMPlant.SetVisible(Visible:boolean)`

**Remarks:** If Plant Simulation is created as a COM server it is invisible by default. You can use `SetVisible` to make Plant Simulation visible.

**Parameter:** `Visible` (boolean) — sets if the application Plant Simulation is visible (`true`) or invisible (`false`).

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.SetVisible(true)
```

### StartSimulation

Starts the simulation with the EventController.

- **Type:** Function
- **Syntax:** `eMPlant.StartSimulation(PathOfEventController:string[, SimulationWithoutAnimation:boolean])`

**Remarks:** `StartSimulation` corresponds to the Start/Stop Simulation button.

**Parameters:**

- `PathOfEventController` (string) — designates the path of the EventController.
- `SimulationWithoutAnimation` (boolean, optional) — sets if the simulation is going to be executed without animation (`true`) or with animation (`false`).

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.StartSimulation(".Models.Model.EventController")
```

### StopSimulation

Stops the running simulation.

- **Type:** Function
- **Syntax:** `eMPlant.StopSimulation`

**Remarks:** `StopSimulation` corresponds to the Start/Stop Simulation button in the EventController.

**Example:**

```js
// JScript
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
PlantSim.StopSimulation
```

## Events of the COM Interface

The COM Interface provides the events named `SimulationFinished` and `FireSimTalkMessage`.

Consult the documentation that came with your programming application for instructions on how to connect to these events.

### FireSimTalkMessage

Triggers the event `SimTalkMessage` from within SimTalk.

**Remarks:** The name of the function, which will be triggered, depends on the programming language you use, such as Visual Basic, JavaScript, etc. Check the documentation that came with your programming application for details.

You have to specify a parameter of data type string.

**Example:**

```simtalk
fireSimTalkMessage("The buffer is full.")
```

### SimulationFinished

At the end of a simulation run Plant Simulation triggers the event `SimulationFinished`. You can use it to read the results of a simulation run.

## Example of a JScript

A JScript might look as follows:

```js
var vbOKCancel = 1;
var vbCancel = 2;
var vbInformation = 64;
var Finished=false;
var WSHShell = new ActiveXObject("WScript.Shell");
var simple =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl1",
"RemoteControl_");
simple.SetLicenseType("Runtime");
try
{
// Enter the path to a model file!
simple.LoadModel("C:\\Models\\Test.spp");
}
catch (e)
{
WScript.Echo("Could not load Model!");
WScript.Quit();
}
try
{
simple.SetValue(".Models.Model.Buffer.ProcTime", 700.0); } catch (e) {
r=WSHShell.Popup(e.description, 0, "Continue?", vbOKCancel + vbInformation);
if (r == vbCancel)
{
    simple.CloseModel();
    WScript.Quit();
}
}
simple.StartSimulation(".Models.Model.EventController");
if (simple.IsSimulationRunning())
WScript.Echo("Simulation is running!");
// Wait until simulation is finished
while (!Finished) WScript.Sleep(2000);
simple.CloseModel();
simple.Quit();
WScript.Quit();
function RemoteControl_SimulationFinished()
{
WScript.Echo("Simulation Finished!");
Finished = true;
}
function RemoteControl_SimTalkMessage(str) {
WScript.Echo(str);
}
```

## Example of a Python Script

A Python script might look as follows:

```python
# Install pywin32 with this command:
# pip install pywin32
import win32com.client
import time
PlantSim =
win32com.client.Dispatch("Tecnomatix.PlantSimulation.RemoteControl.25.4")
PlantSim.SetVisible(True)
PlantSim.LoadModel("D:/Test.spp")
PlantSim.StartSimulation(".Models.Model");
time.sleep(10)
PlantSim.StopSimulation()
PlantSim.Quit()
```
