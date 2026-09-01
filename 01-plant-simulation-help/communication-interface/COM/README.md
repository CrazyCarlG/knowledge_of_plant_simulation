# COM Interface

This folder contains documentation for the **COM Interface** of Plant Simulation, which allows external applications to control Plant Simulation remotely via Microsoft's Component Object Model (COM).

## Overview

The COM Interface lets you drive Plant Simulation from any COM-aware application — Office applications (Excel, Word, etc.), Windows Scripting Host (WSH), Python via `pywin32`, and many others. A typical use case is starting a simulation run from Excel and writing the results back into an Excel table.

The COM server is registered under the ProgID `Tecnomatix.PlantSimulation.RemoteControl`. If multiple Plant Simulation versions are installed, the version can be selected explicitly, e.g. `Tecnomatix.PlantSimulation.RemoteControl.26.0`. The COM Interface is part of the Plant Simulation Interface Package.

## Interface Type — `IRemoteControl`

The COM interface is declared as:

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

## Initialization (JScript)

The examples in the documentation assume that Plant Simulation has been initialized via Windows Scripting Host as follows:

```js
var PlantSim =
WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl")
```

## Functions of the COM Interface

| Function | Purpose |
|----------|---------|
| `CloseModel` | Closes the active simulation model. Calls any `onCloseModel` methods in the Class Library. |
| `ExecuteSimTalk` | Executes the specified SimTalk source code; supports up to three arguments and returns the method's return value. |
| `GetValue` | Returns the value of the specified attribute of a Plant Simulation object. |
| `IsSimulationRunning` | Returns `true` if the simulation is currently running, otherwise `false`. |
| `LoadModel` | Loads the specified simulation model. Optionally accepts a password for encrypted models. Does not load call chains. |
| `NewModel` | Creates a new simulation model at the given file path. |
| `OpenConsoleLogFile` | Routes the Plant Simulation Console output to a file. Pass an empty string to stop routing. |
| `Quit` | Exits Plant Simulation. |
| `QuitAfterTime` | Exits Plant Simulation after the specified number of milliseconds. |
| `ResetSimulation` | Resets the EventController at the given path. |
| `SaveModel` | Saves the active simulation model under the specified name. |
| `SetLicenseType` | Sets the license type used by Plant Simulation. |
| `SetNoMessageBox` | Shows (`true`) or hides (`false`) message boxes. |
| `SetPathContext` | Sets the start of the relative path used by `getValue` and `setValue`. |
| `SetSuppressStartOf3D` | Suppresses (`true`) or allows (`false`) starting the 3D view. |
| `SetTrustModels` | Permits (`true`) or prohibits (`false`) loaded models from accessing the computer; corresponds to the `/TrustModels` start option. |
| `SetValue` | Assigns a value to an attribute of a Plant Simulation object. |
| `SetVisible` | Makes Plant Simulation visible (`true`) or invisible (`false`). Default when created as a COM server is invisible. |
| `StartSimulation` | Starts the simulation at the given EventController path, optionally without animation. |
| `StopSimulation` | Stops the running simulation. |

## Events

The COM Interface exposes two events:

- **FireSimTalkMessage** — Triggered from SimTalk via `fireSimTalkMessage(string)`. Useful for pushing messages from Plant Simulation to the controlling application.
- **SimulationFinished** — Raised at the end of a simulation run, so the controlling application can read results.

## Notes on the Lifecycle

- A method `onCloseModel` can be defined in any folder of the Class Library. Plant Simulation calls it both when the model is closed and when Plant Simulation exits, passing `false` or `true` respectively in the `onExitApplication` parameter. Multiple `onCloseModel` methods are all called.
- When Plant Simulation is launched as a COM server, the UI is invisible by default — call `SetVisible(true)` to show it.

## Example: JScript

A complete Windows Scripting Host example that loads a model, sets a parameter, runs the simulation, waits until it finishes, and then closes Plant Simulation:

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

## Example: Python Script

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

## Related Documentation

- Source file in this folder: `COM.md` (full reference for the COM Interface).
- Source raw extract: `Plant-Simulation-Help2606_10814-10864.txtx`.
- For TCP/IP based communication, see the sibling folder `Socket/` and its `Socket.md`.
