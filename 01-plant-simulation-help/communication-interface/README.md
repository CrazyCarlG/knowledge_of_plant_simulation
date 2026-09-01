# Communication Interface

This folder documents the **Communication Interfaces** of Plant Simulation, which allow Plant Simulation to exchange data with external applications, other processes, devices, and IoT brokers.

## Overview

Plant Simulation provides three primary mechanisms for external communication:

| Interface | Folder | Purpose |
|-----------|--------|---------|
| **COM Interface** | [`COM/`](./COM/) | Drive Plant Simulation from any COM-aware application (Excel, WSH, Python via `pywin32`, etc.) using Microsoft's Component Object Model. |
| **Socket** | [`Socket/`](./Socket/) | Exchange data via TCP/IP (or UDP) point-to-point with applications, devices, or other Plant Simulation processes. |

> **Note:** If `File > Model Settings > General > Prohibit Access To The Computer` is deactivated, all SimTalk-accessible communication (Socket) is blocked.

---

## 1. COM Interface — `COM/`

Lets external applications **control** Plant Simulation remotely.

- **ProgID:** `Tecnomatix.PlantSimulation.RemoteControl` (latest version) or `Tecnomatix.PlantSimulation.RemoteControl.<Major>.<Minor>` (e.g. `.26.0`, `.25.4`).
- **Package:** Plant Simulation Interface Package.
- **Interface:** `IRemoteControl : IDispatch` — declared in IDL with the methods listed below.
- **Typical use:** Drive a simulation run from Excel / Office / WSH / Python and write the results back into a spreadsheet.

### Core Methods

| Method | Purpose |
|--------|---------|
| `NewModel(FilePath)` | Create a new model at the given file path. |
| `LoadModel(ModelName[, Password])` | Open a model (optionally encrypted). Does not load call chains. |
| `SaveModel(ModelName)` | Save the active model. |
| `CloseModel` | Close the model; triggers `onCloseModel` in Class Library. |
| `StartSimulation(EventControllerPath[, NoAnimation])` | Start the simulation run. |
| `StopSimulation` | Stop a running simulation. |
| `ResetSimulation(EventControllerPath)` | Reset an EventController. |
| `IsSimulationRunning` | Returns whether the simulation is currently running. |
| `ExecuteSimTalk(Source[, P1, P2, P3])` | Execute SimTalk source code with up to 3 parameters; returns the method's value. |
| `GetValue(ObjectPath)` / `SetValue(ObjectPath, Value)` | Read/write any Plant Simulation attribute. |
| `SetPathContext(StartPath)` | Anchor for relative paths used by `GetValue`/`SetValue`. |
| `Quit` / `QuitAfterTime(ms)` | Exit Plant Simulation (immediately or after a delay). |
| `SetVisible(bool)` | Show/hide Plant Simulation. Default is **invisible** when started as a COM server. |
| `SetLicenseType(LicenseType)` | Switch license (e.g. `"Runtime"`, `"Professional"`). |
| `SetNoMessageBox(bool)` | Suppress message boxes. |
| `SetSuppressStartOf3D(bool)` | Skip starting the 3D view. |
| `SetTrustModels(bool)` | Equivalent to the `/TrustModels` start option. |
| `OpenConsoleLogFile(FilePath)` | Route Console output to a file (`""` to stop). |

### Events

- **`SimulationFinished`** — fired at the end of a run so the caller can read results.
- **`FireSimTalkMessage`** — fired from SimTalk via `fireSimTalkMessage(string)` to push messages to the controlling application.

### Lifecycle Note

Define a method `onCloseModel(onExitApplication:boolean)` in any folder of the Class Library. Plant Simulation calls all of them both when the model is closed (`onExitApplication := false`) and when Plant Simulation exits (`onExitApplication := true`).

### Quick Examples

**JScript (Windows Scripting Host):**

```js
var PlantSim = WScript.CreateObject("Tecnomatix.PlantSimulation.RemoteControl");
PlantSim.LoadModel("C:\\Models\\Test.spp");
PlantSim.SetValue(".Models.Model.Buffer.ProcTime", 700.0);
PlantSim.StartSimulation(".Models.Model.EventController");
// ... handle SimulationFinished event ...
PlantSim.CloseModel();
PlantSim.Quit();
```

**Python (`pywin32`):**

```python
import win32com.client, time
PlantSim = win32com.client.Dispatch("Tecnomatix.PlantSimulation.RemoteControl.25.4")
PlantSim.SetVisible(True)
PlantSim.LoadModel("D:/Test.spp")
PlantSim.StartSimulation(".Models.Model")
time.sleep(10)
PlantSim.StopSimulation()
PlantSim.Quit()
```

Full reference: [`COM/COM.md`](./COM/COM.md).

---

## 2. Socket — `Socket/`

The **Socket object** exchanges data with other applications via TCP/IP. Plant Simulation can act as a server or a client.

- **Path in Class Library:** `Home ribbon > Manage Class Library > Basic Objects > InformationFlow > Socket`
- **Protocols:** TCP (reliable, connection-oriented) / UDP (lower overhead, no delivery guarantee). IPv6 supported.
- **Port range:** **1025–32025** (ports ≤ 1024 are reserved for standard services).
- **Max simultaneous connections:** up to **2000** across all sockets (each `Chart` and `GanttChart` also consumes one).

### Key Attributes (Dialog / SimTalk)

- `On` — activate/deactivate the socket.
- `ServerSocket` — `true` = server mode, `false` = client mode.
- `TCP` — `true` = TCP, `false` = UDP.
- `Host` — remote host IP (client) / listening IP (server). Empty or `127.0.0.1` accepts all interfaces (server).
- `Port` — port number (1025–32025).
- `MaxConnections` — max concurrent server connections.
- `ClientHost` / `ClientPort` — outgoing source IP / local port (client mode).
- `CallBackMethod` — method invoked when data is received (parameters: `ChannelNumber`, `ReceivedMessage`).
- `UseRFC1006` — prepends a length header so message boundaries are preserved on the TCP byte stream (set on both ends before connecting).
- `UseIPSec` — encrypt socket traffic via OS-configured IPSec.

### Methods

| Method | Purpose |
|--------|---------|
| `broadcast(Message)` | Send to all connected processes (non-server-socket mode). |
| `closeSession(Socket)` | Close a socket session. |
| `getReceiveBufferSize(Channel)` / `getSendBufferSize(Channel)` | Read buffer sizes. |
| `setReceiveBufferSize(Channel, Size)` / `setSendBufferSize(Channel, Size)` | Set buffer sizes; `Channel = -1` sets default for new connections. |
| `write([Channel,] Message)` / `write([HostAndPort,] Message)` | Send a string (TCP/UDP). |
| `writeNullByte(...)` | Like `write`, but appends a null terminator. |
| `writeArray(...)` | Send integer array/list (TCP client / TCP server / UDP variants). |
| `writeByte([Channel,] ByteCode)` / `writeByte([HostAndPort,] ByteCode)` | Send a single byte. |

### Callback Method

The Callback Method is invoked automatically when data arrives. Typical SimTalk signature:

```simtalk
param ChannelNumber: integer, ReceivedMessage: string  -- TCP
param Host: string,       ReceivedMessage: string      -- UDP
param ChannelNumber: integer, ReceivedMessage: integer[] -- TCP, byte array
```

### Read-Only Attribute

- `NumConnections` — number of active connections.

### Sample models

`Window ribbon > Start Page > Getting Started > Example Models > Small Examples`

Full reference: [`Socket/Socket.md`](./Socket/Socket.md).

---

## Source Files

| File | Description |
|------|-------------|
| `COM/COM.md` | Full COM Interface reference (interface declaration, all methods, events, examples). |
| `COM/README.md` | Curated summary of the COM Interface. |
| `COM/Plant-Simulation-Help2606_10642-10668.txtx` | Raw text extract from Plant Simulation Help 2606. |
| `Socket/Socket.md` | Full Socket reference (dialog, attributes, methods). |
| `Socket/README.md` | Curated summary of the Socket object. |
| `Socket/Plant-Simulation-Help2606_10814-10864.txtx` | Raw text extract from Plant Simulation Help 2606. |

---

*Source: Plant Simulation Help — "Communication Interface". Unpublished work. © 2026 Siemens.*