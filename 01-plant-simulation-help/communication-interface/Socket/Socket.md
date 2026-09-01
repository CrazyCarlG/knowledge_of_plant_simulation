# Socket

## UpdateInterval [SimTalk]

Sets the time in milliseconds after which Plant Simulation updates the values of the elements of the object designated by `<Path>`, i.e., reads them from shared memory and writes them back to it.

- **Type:** Attribute
- **Syntax:** `<Path>.UpdateInterval:integer`
- **Assignment Value:** You can assign a value of data type integer.

**Example:**
```simalk
SIMITInterface.UpdateInterval := 100 // milliseconds
```

**See also:** Update Interval [text box]

---

## Socket

Use the object `Socket` for exchanging data via a TCP/IP interface with Plant Simulation. The Socket Interface communicates with other applications, which have a socket interface.

### Description

Socket communication is the foundation of the most widespread communication software. Sockets are point-to-point connections, established during initialization, allowing the online exchange of data. As the socket connection is directly based upon the TCP/IP protocol, it ensures fast communication without much data overhead.

With socket connections one process works as a server with additional processes registering as clients. Plant Simulation can be a client as well a server.

If you deactivate the safety setting `File > Model Settings > General > Prohibit Access To The Computer`, access to the Socket Interface via SimTalk will be prevented.

To show a tooltip with information about the Socket Interface, hover with the mouse over it.

To change the length of the graphic and the anchor points of the Socket Interface, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

### Add the Object to the Simulation Model

To add the object `Socket` to the Class Library, click **Manage Class Library > Basic Objects > InformationFlow > Socket** on the Home ribbon tab.

Compare the sample models: Click the **Window** ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog **Examples Collection**, and click **Open Model**.

**See also:** Exchange Data via a Network Socket

---

## Dialog Box of the Socket Interface

Double-click the icon of the Socket Interface to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under Dialog Items of the Objects.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

### On [check box]

To activate the object `Socket` as such, select this check box.

**Remarks:**

- If you are using the object `Socket` as a server socket, it then listens on the specified Port.
- If you are using the object `Socket` as a client socket, it attempts to connect to a server.

Instead, you can also right-click the object `Socket` in the Frame and select **Activate** on the context menu. To deactivate it, select **Deactivate** on the context menu.

---

## Tab Attributes

The tab **Attributes** provides the settings, which the object offers. The settings are listed in the table of contents to the left. The shared properties are described under the Tab Attributes.

### Protocol [drop-down list]

Select the protocol for transmitting the data. **TCP** or **UDP**.

**Remarks:** You can select one of these settings:

- **TCP** — This protocol ensures that the data packages arrive at the destination. When you select TCP, you have to select the check boxes **On** and **Server Socket** for the server. For the client you have to select **On** and clear **Server Socket**. This establishes a connection across which the data will be exchanged. The TCP protocol ensures that the data packages arrive at the destination.
- **UDP** — This protocol creates less overhead than the TCP, but does not guarantee that the data actually does arrive at the destination. When you select UDP, you have to select the check boxes **On** and **Server Socket** for the server. For the client you have to select **On** and clear **Server Socket**. You can now exchange data without a connection having to be established. This creates less overhead, but does not guarantee that the data actually does arrive at the destination.

**Note:** The object `Socket` supports the IPv6 protocol.

### Host [Socket]

Type in the IP address of the computer with which you want to establish the connection.

The IP address of the Host connects to the host computer.

- For a client socket the Host sets the IP address of the host computer to which the Socket Interface is to establish the connection. The number **127.0.0.1** designates the local host.
- For a server socket the Host sets the IP address on which the server is waiting for incoming connections. If the text box is empty or contains the value **127.0.0.1** incoming connections on all network interfaces are allowed.

### Port [Socket]

Type in the port number with which the socket connection exchanges data with other applications.

**Remarks:**

- If you cleared **Server Socket**, you have to type in a local port number that is not already used to be able to select the check box **On**.
- Use port numbers between **1025** and **32025**, as port numbers up to and including the number **1024** designate standard services, such as telnet, ftp, etc.

### Max. Connections

Type in the maximum number of connections which can be active at any one time.

**Remarks:** The setting `Max. Connections` applies when you are running the Socket connection as a Server Socket.

**Note:** Plant Simulation can handle a maximum of 2000 socket connections at any one time. When you activate the objects `Chart` and `GanttChart` these also require a Socket connection.

### Callback Method [text box] - Socket

Modifies the built-in behavior of the object. The object calls the Callback Method when the Socket Interface receives data.

**Select the Path to an Existing Method:**

Click the ellipsis button. Navigate to the location of the Method in the dialog **Select Object [for controls]** and click **OK**. This inserts the name of the Method into the text box of the Control. Press **F2** in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

**Create a Control That is a Method of the Object:**

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.
- Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press **F2**.
- Or hold down **Shift** and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab **User-defined** and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

The standard callback method as a user-defined attribute looks like this:

**Parameters:** During the call two parameters are passed to the method.

- The parameter `ChannelNumber` contains the channel number of the connection of data type integer for the TCP protocol or the Internet address of the client of data type string for the UDP protocol.
- The parameter `ReceivedMessage` contains the content of the received message. The parameter can be of data type string, it can be an array of data type integer, or a list of data type integer.

**Example:**

```simalk
param ChannelNumber: integer, ReceivedMessage: string // TCP protocol
print ReceivedMessage

param Host: string, ReceivedMessage: string           // UDP protocol
print ReceivedMessage
```

```simalk
param ChannelNumber: integer, ReceivedMessage: integer[] // TCP protocol
for var i := 1 to ReceivedMessage.Dim 
   print ReceivedMessage[i]
next
```

### Server Socket [check box]

To use the object `Socket` as a server socket, select this check box. To use it as a client socket, clear the check box.

### Client Host [text box]

Type in the IP address of the client host computer from which you want to establish the connection.

**Remarks:** The Client Host setting is important if you configured several IP addresses on your computer and if you want to set from which IP address the outgoing packet is going to be sent.

**Note:** This setting applies when you are not running the socket connection as a Server Socket but as a client socket.

### Client Port [text box]

Type in the port number with which the socket connection exchanges data with client applications.

**Remarks:**

- If you cleared **Server Socket**, you have to type a local port number that is not already used to be able to select the setting **On**.
- Use port numbers between **1025** and **32025**, as port numbers up to and including the number **1024** designate standard services, such as telnet, ftp, etc.

**Note:** This setting applies when you are not running the socket connection as a Server Socket but as a client socket.

### Use RFC 1006 [check box]

To add an RFC 1006 protocol header to all data, which the Socket Interface sends, select this check box. The protocol header contains the length of the data package.

**Remarks:** RFC 1006 ensures that the receiver receives the data packages with the size in which they were sent. RFC 1006 with the title "ISO Transport Service on top of the TCP" is a protocol extension of the TCP protocol. In addition to the TCP data, it transmits further information to provide certain services for the user.

**Note:** This setting has to be enabled on both sides, sender and receiver, and before the connection is established to work properly.

**Behavior of the TCP Protocol:** If data is transmitted by the TCP protocol, the transmission is data-stream-oriented. In doing so neither information about the length nor information about the start and the end of a message is being transmitted. When sending data this is unproblematic, as the sender knows how many data bytes he wants to send. The receiver on the other hand cannot recognize where a message in the data stream ends and where the next message in the data stream begins.

**Behavior of the RFC 1006 Protocol Extension:** In most applications in automation engineering it is essential to work data-stream-oriented. Here complete message blocks are sent via a connection which are recognized by the receiver as such. RFC-1006 sets which information, in form of a header, is to be added to the data to be transmitted to ensure this. RFC-1006 provides a message-oriented transmission for applications based on the data-stream-oriented TCP protocol.

### Use IPSec [check box]

To use the IPSec network protocol suite to encrypt the Socket communication, select this check box.

**Remarks:** Plant Simulation uses the default settings of IPSec. IPSec stands for Internet Protocol Security.

**Note:** You have to configure IPSec at operation system level beforehand to ensure that encryption works correctly. To ensure the cyber security of Plant Simulation, the computer on which Plant Simulation runs, has to be protected, see Notes on Information Security.

---

## Tab Sessions

The Socket Interface shows the active connections on the tab **Sessions**. It lists the name of the host computer on which the process is running and, separated by a colon, the internal identifying number for each connection per session.

**Remarks:** If the object `Socket` works in Server Socket mode, only this connection to the server socket process is possible.

---

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

---

## Navigate Menu

The commands are described under the Navigate Menu.

---

## View Menu

The View Menu provides commands to access its functions: **Refresh**, **Show Attributes and Methods**. SimTalk: `updateDialog`.

---

## Tools Menu

The commands are described under the Tools Menu.

---

## Help Menu

The commands are described under the Help Menu.

---

## Methods of the Socket Interface

The Socket Interface provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

An example of the Syntax line of the individual methods might look like this: `<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`.

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses.
- Optional parameters are listed within brackets.
- If a parameter has a default value, the signature shows the default value after the parameter.
- If the method has a return value, the signature shows its data type after the arrow `->`.

### broadcast [SimTalk]

Sends a message to all connected processes when the Socket Interface designated by `<Path>` is not working in server socket mode.

- **Type:** Method
- **Syntax:** `<Path>.broadcast(Message:string) → boolean`
- **Parameter:** The parameter `Message` of data type string designates the message.
- **Return Value:** The return value has the data type boolean.

**Example:**
```simalk
Socket.broadcast("The simulation is finished.")
```

### closeSession [SimTalk]

Closes the session of the Socket Interface designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.closeSession(Socket:integer) → void`
- **Parameter:** The parameter `Socket` of data type integer designates the channel.
- **Return Value:** The return value has the data type boolean.

**Example:**
```simalk
Socket.closeSession(1)
```

### getReceiveBufferSize [SimTalk]

Returns the size of the receiving buffer of the Socket Interface designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.getReceiveBufferSize(Channel:integer) → integer`
- **Parameter:** The parameter `Channel` of data type integer designates the number of the communication channel.
- **Return Value:** The return value has the data type integer.

**Example:**
```simalk
print Socket.getReceiveBufferSize(3)
```

### getSendBufferSize [SimTalk]

Returns the size of the sending buffer of the Socket Interface designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.getSendBufferSize(Channel:integer) → integer`
- **Parameter:** The parameter `Channel` of data type integer designates the number of the communication channel.
- **Return Value:** The return value has the data type integer.

**Example:**
```simalk
print Socket.getSendBufferSize(2)
```

### setReceiveBufferSize [SimTalk]

Sets the size of the receiving buffer of the Socket Interface designated by `<Path>` in bytes.

- **Type:** Method
- **Syntax:** `<Path>.setReceiveBufferSize(Channel:integer, BufferSize:integer) → boolean`
- **Parameters:**
  - `Channel` (integer): the number of the communication channel. Assign `-1` to define the default buffer size for new connections. This does not affect the buffer size of existing connections. The value is not saved to the model file.
  - `BufferSize` (integer): the size of the buffer.
- **Return Value:** The return value has the data type boolean.

**Examples:**
```simalk
Socket.setReceiveBufferSize(3,2054) -- sets the receive buffer size of channel 3 to 2054 bytes
Socket.setReceiveBufferSize(-1, 80) -- sets the default receive buffer size for new connections to 80
```

### setSendBufferSize [SimTalk]

Sets the size of the sending buffer the Socket Interface designated by `<Path>` in bytes.

- **Type:** Method
- **Syntax:** `<Path>.setSendBufferSize(Channel:integer, BufferSize:integer) → boolean`
- **Parameters:**
  - `Channel` (integer): the number of the communication channel. Assign `-1` to define the default buffer size for new connections. This does not affect the buffer size of existing connections. The value is not saved to the model file.
  - `BufferSize` (integer): the size of the buffer.
- **Return Value:** The return value has the data type boolean.

**Examples:**
```simalk
Socket.setSendBufferSize(1, 1290)
Socket.setSendBufferSize(-1, 80) -- sets the default send buffer size for new connections to 80
```

### write [SimTalk] - Socket

Sends messages of the Socket Interface designated by `<Path>` to other Plant Simulation processes.

- **Type:** Method
- **Syntax:**
  - `<Path>.write([Channel:integer, ]Message:string) → boolean`
  - `<Path>.write([HostAndPort:any, ]Message:string) → boolean`
- **Parameters:**
  - If you are using the TCP protocol, the optional parameter `Channel` (integer) designates the number of the communication channel.
  - If you are using the UDP protocol, the optional parameter `HostAndPort` (any) designates the Host Name and the Port Number of the computer to which the message is going to be sent.
  - `Message` (string): the message that you want to send.

When the object `Socket` is working in server socket mode, the channel number is 0. To send a null byte at the end of the string, you can use the method `writeNullByte`.

- **Return Value:** The return value has the data type boolean.

**Examples:**
```simalk
Socket.write(3,"crankshaft:red:6")       // TCP
Socket.write("127.0.0.1:30000", "Test")  // UDP
```

### writeArray [SimTalk]

Sends data of the Socket Interface designated by `<Path>` to another process.

- **Type:** Method
- **Syntax:** `<Path>.writeArray(Parameter:any[, Parameter:any, Parameter:any]) → boolean`

**Parameters for the TCP Protocol with Server Socket Cleared (Client):**

The parameter `ByteArray` of data type integer designates the data which is contained in an integer array or in a list of data type integer.

- **Syntax:** `<Path>.writeArray(ByteArray:integer[])`
- **Return Value:** The return value has the data type boolean.

**Example:**
```simalk
Client.writeArray([12, 48, 13])
```

**Parameters for the TCP Protocol with Server Socket Checked (Server):**

The parameter `Channel` (integer) sets the client connection and the parameter `ByteArray` designates the data which is contained in an integer array or in a list of data type integer.

- **Syntax:** `<Path>.writeArray(Channel:integer, ByteArray:integer[]) → boolean`
- **Return Value:** The return value has the data type boolean.

**Example:**
```simalk
Server.writeArray(1, [12, 48, 13])
```

**Parameters for the UDP Protocol:**

Specify one parameter to designate the data which is contained in an integer array or in a list of data type integer. Or specify three parameters:

- `Remote-Port` (integer): the remote port number.
- `Remote-Host` (string): the remote host name.
- `ByteArray` (integer[]): the data which is contained in an integer array or in a list of data type integer.

- **Syntax:**
  - `<Path>.writeArray(ByteArray:integer[]) → boolean`
  - `<Path>.writeArray(Remote-Port:integer, Remote-Host:string, ByteArray:integer[]) -> boolean`
- **Return Value:** The return value has the data type boolean.

**Example:**
```simalk
Socket.writeArray([12, 48, 13])
Socket.writeArray(30000, "Hal9001", [12, 48, 13])
```

### writeByte [SimTalk]

Sends bytes of the Socket Interface designated by `<Path>` to other processes.

- **Type:** Method
- **Syntax:**
  - `<Path>.writeByte([Channel:integer, ]ByteCode:integer) → boolean`
  - `<Path>.writeByte([HostAndPort:any, ]ByteCode:integer) → boolean`
- **Parameters:**
  - If you are using the TCP protocol, the optional parameter `Channel` (integer) designates the number of the communication channel.
  - If you are using the UDP protocol, the optional parameter `HostAndPort` (any) designates the Host Name and the Port Number of the computer to which the message is going to be sent.
  - `ByteCode` (integer): the byte code you want to send.

When the object `Socket` is set to server socket, the channel number is 0. To send a null byte at the end of the string, you can use the method `writeNullByte`.

- **Return Value:** The return value has the data type boolean.

**Example:**
```simalk
Socket.writeByte(3,6)                  // TCP
Socket.writeByte("127.0.0.1:30000",6)  // UDP
```

### writeNullByte [SimTalk]

Sends messages of the Socket Interface designated by `<Path>` to other processes. Plant Simulation sends a null byte at the end of the string.

- **Type:** Method
- **Syntax:**
  - `<Path>.writeNullByte([Channel:integer, ]Message:string) → boolean`
  - `<Path>.writeNullByte([HostAndPort:any, ]Message:string) → boolean`
- **Parameters:**
  - If you are using the TCP protocol, the optional parameter `Channel` (integer) designates the number of the communication channel.
  - If you are using the UDP protocol, the optional parameter `HostAndPort` (any) designates the Host Name and the Port Number of the computer to which the message is going to be sent.
  - `Message` (string): the message you want to send.

When the object `Socket` is set to server socket, the channel number is 0. As compared to the method `write`, Plant Simulation in addition sends a null byte at the end of the string.

- **Return Value:** The return value has the data type boolean.

**Example:**
```simalk
Socket.writeNullByte(4,"crankshaft:blue:2")                  // TCP
Socket.writeNullByte("127.0.0.1:30000","crankshaft:blue:2")  // UDP
```

---

## Read-Only Attributes of the Socket Interface

The Socket Interface provides:

- The read-only attribute `NumConnections [SimTalk]`.
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it.

**Example:**
```simalk
print MySocket.UUID
```

### NumConnections [SimTalk]

Returns the number of connections of the Socket Interface designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.NumConnections -> integer`
- **Return Value:** The return value has the data type integer.

**Example:**
```simalk
print MyClientSocket.NumConnections
```

---

## Attributes of the Socket Interface

The Socket Interface provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

**Examples:**
```simalk
Socket.Host := "127.0.0.1"
print Socket.Host
```

### CallBackMethod [SimTalk] - Socket

Sets the Callback Method of the Socket Interface designated by `<Path>`.

**Remarks:** Plant Simulation executes the Callback Method when the Socket Interface receives data.

- **Type:** Attribute
- **Syntax:** `<Path>.CallBackMethod:method`
- **Assignment Value:** You can assign a value of data type method.

**Parameters:** During the call two parameters are passed to the method:

- The parameter `ChannelNumber` contains the channel number of the connection (integer) for the TCP protocol or the Internet address of the client (string) for the UDP protocol.
- The parameter `ReceivedMessage` contains the contents of the received message. The parameter can be of data type string, an array of data type integer, or a list of data type integer.

**Examples:**
```simalk
Socket.CallBackMethod := &SocketMethod

param ChannelNumber: integer, ReceivedMessage: string
print "Message from channel", channelNo
print "Message: ", message
// writes the value to the global variable 'MessageReceived'
if strLen(SocketMessage) = 1 
   MessageReceived := to_str(strAscii(SocketMessage)) // byte received
else
   MessageReceived := to_str(SocketMessage) // string received
end
// writes the message to the Plant Simulation Console
print "--------------------------------------------------------------------"
print self
print "Message: The number ", MessageReceived, " was received at ", sysdate
```

```simalk
param Host: string, msg: integer[] // UDP protocol
for var i := 1 to msg.dim 
   print msg[i]
next
```

### ClientHost [SimTalk]

Sets the IP address of the client host computer of the Socket Interface designated by `<Path>` from which you want to establish the connection.

**Remarks:** This setting is important if you configured several IP addresses on your computer and if you want to set from which IP address the outgoing packet is going to be sent.

**Note:** This setting applies when you are not running the socket connection as a Server Socket but as a Client Socket.

- **Type:** Attribute
- **Syntax:** `<Path>.ClientHost:string`
- **Assignment Value:** You can assign a value of data type string.

**Example:**
```simalk
MySocket.ClientHost := "128.0.0.1"
```

### ClientPort [SimTalk]

Sets the port number with which the Socket Interface designated by `<Path>` exchanges data with client applications.

**Remarks:** If you cleared `Server Socket`, you have to enter a local port number that is not already used to be able to select the setting `On`.

**Note:** This setting applies when you are not running the socket connection as a Server Socket but as a Client Socket.

- **Type:** Attribute
- **Syntax:** `<Path>.ClientPort:integer`
- **Assignment Value:** You can assign a value of data type integer. Specify a value between 1025 and 32025. Port numbers up to and including 1024 designate standard services, such as telnet, ftp, etc.

**Example:**
```simalk
Socket.ClientPort := 30000
```

### Host [SimTalk] - Socket

Sets the IP address of the host computer to which the Socket Interface designated by `<Path>` is to establish the connection for a client socket.

**Remarks:** The number 127.0.0.1 designates the local host. Sets the IP address on which the server is waiting for incoming connections for a server socket. If the attribute is empty or contains the value "127.0.0.1" incoming connections on all network interfaces are allowed.

- **Type:** Attribute
- **Syntax:** `<Path>.Host:string`
- **Assignment Value:** You can assign a value of data type string.

**Example:**
```simalk
Socket.Host := "127.0.0.1"
```

### MaxConnections [SimTalk] - Socket

Sets the maximum number of client connections (sessions), which can connect to the active server socket of the Socket Interface designated by `<Path>`.

**Remarks:** Each and every connection uses a handle of the operating system and the number of these handles is limited.

**Note:** This setting applies when you are not running the Socket connection in Server Socket mode. Plant Simulation can handle a maximum of 2000 socket connections at any one time. When you activate the objects `Chart` and `GanttChart` these also require a Socket connection.

- **Syntax:** `<Path>.MaxConnections:integer`
- **Assignment Value:** You can assign a value of data type integer.

**Example:**
```simalk
Socket.MaxConnections := 7
```

### On [SimTalk]

Activates the Socket Interface designated by `<Path>` as such (true) or deactivates it (false).

**Remarks:** If you are using it as a Server Socket, it then listens on the specified Port. If you are using it as a Client Socket, it attempts to connect to a server.

- **Type:** Attribute
- **Syntax:** `<Path>.On:boolean`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**
```simalk
Socket.on := true
```

### Port [SimTalk] - Socket

Sets the port number with which the socket connection of the Socket Interface designated by `<Path>` exchanges data.

**Remarks:** If you cleared `Server Socket`, you have to enter a local port number that is not already used to be able to select the setting `On`.

- **Type:** Attribute
- **Syntax:** `<Path>.Port:integer`
- **Assignment Value:** You can assign a value of data type integer. Specify port numbers between 1025 and 32025. Port numbers up to and including 1024 designate standard services, such as telnet, ftp, etc.

**Example:**
```simalk
Socket.Port := 31111
```

### ServerSocket [SimTalk]

Sets if the Socket Interface designated by `<Path>` works as a server socket (true) or as a client socket (false).

- **Type:** Attribute
- **Syntax:** `<Path>.ServerSocket:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**
```simalk
MySocket.ServerSocket := false
```

### TCP [SimTalk]

Sets if the Socket Interface designated by `<Path>` transmits data using the TCP protocol (true) or the UDP protocol (false).

**Remarks:** The TCP protocol and the UDP protocol behave differently:

- When you specify TCP, you have to select the check boxes `On` and `Server Socket` for the server. For the client you have to select `On` and clear `Server Socket`. This establishes a connection across which the data will be exchanged. The TCP protocol ensures that the data packages arrive at the destination.
- When you specify UDP, you have to select the check boxes `On` and `Server Socket` for the server. For the client you have to select `On` and clear `Server Socket`. You can now exchange data without a connection having to be established. This creates less overhead, but does not guarantee that the data actually does arrive at the destination.

**Note:** The object `Socket` supports the IPv6 protocol.

- **Type:** Attribute
- **Syntax:** `<Path>.TCP:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**
```simalk
Socket.TCP := true
```

### UseIPSec [SimTalk]

Sets if the Socket Interface designated by `<Path>` uses the IPSec network protocol suite for the Socket communication (true) or not (false).

**Remarks:** Plant Simulation uses the default settings of IPSec. IPSec stands for Internet Protocol Security.

**Note:** You have to configure IPSec at operation system level beforehand to ensure that encryption works correctly.

- **Type:** Attribute
- **Syntax:** `<Path>.UseIPSec:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**
```simalk
Socket.UseIPSec := true
```

### UseRFC1006 [SimTalk]

Sets if the Socket Interface designated by `<Path>` adds an RFC 1006 protocol header to all sent data, which contains the length of the data package (true) or not (false).

**Remarks:** This ensures that the receiver receives the data packages with the size in which they were sent. RFC-1006 with the title "ISO Transport Service on top of the TCP" is a protocol extension of the TCP protocol. In addition to the TCP data, it transmits further information to provide certain services for the user.

**Note:** This setting has to be enabled on both sides, sender and receiver, and before the connection is made to work properly.

- **Type:** Attribute
- **Syntax:** `<Path>.UseRFC1006:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**
```simalk
Socket.UseRFC1006 := true
```
