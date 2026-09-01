# Socket

## Overview

The **Socket** object in Plant Simulation exchanges data via a TCP/IP interface with other applications that have a socket interface. Sockets are point-to-point connections based on TCP/IP, enabling fast online data exchange with minimal overhead. Plant Simulation can act as either a server or a client.

> If `File > Model Settings > General > Prohibit Access To The Computer` is deactivated, access to the Socket Interface via SimTalk will be blocked.

### Add to Simulation Model

`Home ribbon > Manage Class Library > Basic Objects > InformationFlow > Socket`

Sample models: `Window ribbon > Start Page > Getting Started > Example Models > Small Examples`

---

## Dialog Box

Double-click the Socket icon to open its dialog. Use **Edit 3D Properties** to edit 3D settings; press **M** (Show Manipulators) to edit the graphic.

### On [check box]
- Activates the Socket object.
- Server socket: listens on the specified `Port`.
- Client socket: attempts to connect to a server.
- Alternative: right-click → **Activate** / **Deactivate** on the context menu.

---

## Tab Attributes

### Protocol [drop-down list]
- **TCP** — guarantees data delivery. Requires `On` + `Server Socket` for the server; `On` + clear `Server Socket` for the client.
- **UDP** — lower overhead but no delivery guarantee. Same `On` / `Server Socket` pattern; connectionless exchange.
- Supports IPv6.

### Host [Socket]
IP address of the remote host:
- **Client:** the host to connect to (`127.0.0.1` = local host).
- **Server:** the IP the server listens on. Empty or `127.0.0.1` allows all network interfaces.

### Port [Socket]
Port number for data exchange. Use **1025–32025** (≤ 1024 reserved for standard services). In client mode, supply an unused local port before enabling `On`.

### Max. Connections
Maximum simultaneous connections (server mode only). Plant Simulation supports up to 2000 socket connections total (Chart and GanttChart also consume one).

### Callback Method [text box] - Socket
User-defined method invoked when data is received.
- Use the ellipsis button or **F2** to open the method.
- Drag a method from a Frame into the text box.
- Create as a control via `self.Name` or `self.OnBuilt_in_name`.
- Parameters passed:
  - `ChannelNumber` — integer (TCP) / string host address (UDP)
  - `ReceivedMessage` — string, integer array, or integer list

### Server Socket [check box]
Select to run as a server socket; clear for client mode.

### Client Host [text box]
Outgoing-source IP for the client socket (relevant when the machine has multiple IPs).

### Client Port [text box]
Local port for the client socket. Range **1025–32025**.

### Use RFC 1006 [check box]
Adds an RFC 1006 header (carries the data package length) so message boundaries are preserved on the data-stream-oriented TCP. Must be set on both ends before the connection.

### Use IPSec [check box]
Encrypts socket traffic with IPSec. Requires prior OS-level IPSec configuration.

---

## Tab Sessions

Lists active connections as `HostName:IdentifyingNumber` per session. In server mode, only the connection to the server socket process is shown.

## Tab User-defined

Define your own attributes (see Tab User-defined reference).

## Menus

Navigate, View (`Refresh`, `Show Attributes and Methods` → SimTalk `updateDialog`), Tools, and Help menus are described in their respective general reference pages.

---

## Methods of the Socket Interface

View all methods via **Show Attributes and Methods** (F8). Signature convention: `<Path>.method(Parameters) → returnType`, with `[]` denoting optional parameters and `:= default` denoting default values.

### broadcast [SimTalk]
Sends a message to all connected processes (non-server-socket mode).
- Syntax: `<Path>.broadcast(Message:string) → boolean`
- Example: `Socket.broadcast("The simulation is finished.")`

### closeSession [SimTalk]
Closes a socket session.
- Syntax: `<Path>.closeSession(Socket:integer) → void`
- Example: `Socket.closeSession(1)`

### getReceiveBufferSize [SimTalk]
Returns the receive buffer size in bytes.
- Syntax: `<Path>.getReceiveBufferSize(Channel:integer) → integer`
- Example: `print Socket.getReceiveBufferSize(3)`

### getSendBufferSize [SimTalk]
Returns the send buffer size in bytes.
- Syntax: `<Path>.getSendBufferSize(Channel:integer) → integer`
- Example: `print Socket.getSendBufferSize(2)`

### setReceiveBufferSize [SimTalk]
Sets the receive buffer size.
- Syntax: `<Path>.setReceiveBufferSize(Channel:integer, BufferSize:integer) → boolean`
- `Channel = -1` sets the default for new connections (not persisted; not affecting existing connections).
- Example: `Socket.setReceiveBufferSize(3, 2054)`

### setSendBufferSize [SimTalk]
Sets the send buffer size.
- Syntax: `<Path>.setSendBufferSize(Channel:integer, BufferSize:integer) → boolean`
- Same `-1` default rule as above.
- Example: `Socket.setSendBufferSize(1, 1290)`

### write [SimTalk] - Socket
Sends string messages.
- TCP — `<Path>.write([Channel:integer,] Message:string) → boolean`
- UDP — `<Path>.write([HostAndPort:any,] Message:string) → boolean`
- In server mode, channel number is `0`. Use `writeNullByte` to append a null terminator.
- Examples:
  ```simtalk
  Socket.write(3, "crankshaft:red:6")         // TCP
  Socket.write("127.0.0.1:30000", "Test")     // UDP
  ```

### writeArray [SimTalk]
Sends an integer array or integer list.
- **TCP client:** `<Path>.writeArray(ByteArray:integer[]) → boolean`
- **TCP server:** `<Path>.writeArray(Channel:integer, ByteArray:integer[]) → boolean`
- **UDP:** `<Path>.writeArray(ByteArray:integer[])` or `<Path>.writeArray(Remote-Port:integer, Remote-Host:string, ByteArray:integer[]) → boolean`
- Examples:
  ```simtalk
  Client.writeArray([12, 48, 13])
  Server.writeArray(1, [12, 48, 13])
  Socket.writeArray([12, 48, 13])
  Socket.writeArray(30000, "Hal9001", [12, 48, 13])
  ```

### writeByte [SimTalk]
Sends a single byte.
- TCP — `<Path>.writeByte([Channel:integer,] ByteCode:integer) → boolean`
- UDP — `<Path>.writeByte([HostAndPort:any,] ByteCode:integer) → boolean`
- Example: `Socket.writeByte(3, 6)` (TCP) / `Socket.writeByte("127.0.0.1:30000", 6)` (UDP)

### writeNullByte [SimTalk]
Same as `write` but appends a null byte to the string.
- Example: `Socket.writeNullByte(4, "crankshaft:blue:2")` (TCP)

---

## Read-Only Attributes

### NumConnections [SimTalk]
Number of active connections of the Socket Interface.
- Syntax: `<Path>.NumConnections → integer`
- Example: `print MyClientSocket.NumConnections`

---

## Attributes

### CallBackMethod [SimTalk] - Socket
Sets the callback method invoked when data is received.
- Syntax: `<Path>.CallBackMethod:method`
- Example: `Socket.CallBackMethod := &SocketMethod`

### ClientHost [SimTalk]
Outgoing packet source IP (client mode).
- Syntax: `<Path>.ClientHost:string`
- Example: `MySocket.ClientHost := "128.0.0.1"`

### ClientPort [SimTalk]
Client local port. Range **1025–32025**.
- Syntax: `<Path>.ClientPort:integer`
- Example: `Socket.ClientPort := 30000`

### Host [SimTalk] - Socket
Remote host IP for client / listening IP for server.
- Syntax: `<Path>.Host:string`
- Example: `Socket.Host := "127.0.0.1"`

### MaxConnections [SimTalk] - Socket
Max simultaneous server-socket sessions.
- Syntax: `<Path>.MaxConnections:integer`
- Example: `Socket.MaxConnections := 7`

### On [SimTalk]
Activates/deactivates the Socket. Watchable.
- Syntax: `<Path>.On:boolean`
- Example: `Socket.on := true`

### Port [SimTalk] - Socket
Port number for data exchange. Range **1025–32025**.
- Syntax: `<Path>.Port:integer`
- Example: `Socket.Port := 31111`

### ServerSocket [SimTalk]
`true` = server mode, `false` = client mode.
- Syntax: `<Path>.ServerSocket:boolean`
- Example: `MySocket.ServerSocket := false`

### TCP [SimTalk]
`true` = TCP protocol, `false` = UDP. IPv6 supported.
- Syntax: `<Path>.TCP:boolean`
- Example: `Socket.TCP := true`

### UseIPSec [SimTalk]
`true` = enable IPSec encryption (requires OS configuration).
- Syntax: `<Path>.UseIPSec:boolean`
- Example: `Socket.UseIPSec := true`

### UseRFC1006 [SimTalk]
`true` = add RFC 1006 length header. Must be set on both ends before connection.
- Syntax: `<Path>.UseRFC1006:boolean`
- Example: `Socket.UseRFC1006 := true`