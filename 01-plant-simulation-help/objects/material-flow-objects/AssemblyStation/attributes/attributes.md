# Attributes of the AssemblyStation

The AssemblyStation provides:

- The attributes listed below.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the members of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the members of the selected Instance.

You can set the value of an attribute and get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
MyAssembly.AssemblyMode := "attach MUs"
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print MyAssembly.Pause
posit := MyStation.Cont.XPos
```

---

## StatWaitingResTime [SimTalk]

Returns the entire time during which the AssemblyStation designated by `<Path>` was waiting for mounting parts and/or for processing-Exporters/processing-services.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatWaitingResTime → time`
- **Return Value:** The return value has the data type `time`.

**Example**

```simtalk
print MyAssembly.StatWaitingResTime
```

**See also**

- Waiting [state, material flow objects]
- Statistics report, Waiting Times for Services and Parts

---

## AssemblyMode [SimTalk]

Sets how the AssemblyStation designated by `<Path>` moves the MUs on.

- **Type:** Attribute
- **Syntax:** `<Path>.AssemblyMode:string`
- **Assignment Value:** You can assign a value of data type `string`.
  - Specify `"Attach MUs"` to move the MUs to the main part.
  - Specify `"Delete MUs"` to delete the MUs.

**Example**

```simtalk
MyAssembly.AssemblyMode := "Attach MUs"
```

**See also:** Assembly Mode [drop-down list]

---

## AssemblyTable [SimTalk]

Sets the table containing the mounting parts of the AssemblyStation designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.AssemblyTable:table`
- **Assignment Value:** You can assign a value of data type `table`.

**Remarks**

Depending on the setting selected under **Assembly Table** (or `AssemblyTableMode`) you specify:

### None

The AssemblyStation does not use an Assembly Table. Instead, it expects a part from each of its predecessors.

### Predecessors

Specify the required settings in the table.

- Type the number of the Predecessor, which moves the part, into column 1 of the table and the Amount into column 2. To use the default value 1, do not specify an Amount.
- To make the AssemblyStation accept parts from this predecessor until the capacity of the main MU is reached, specify `-1` as the Amount. To use parts of the main part number as mounting parts, add the number of the main MU to the Assembly Table.
- Specify the time, in seconds, that each individual part consumes when it's assembled into the column **Assembly Time** and the number of the sequence in which the part is assembled into the column **Sequence Number**. The Assembly Time must be a positive number or 0. If you do not specify a time, the default Assembly Time is 0.
- The Sequence Number must be a positive integer number. The default Sequence Number is 1.
- To assemble the parts non-sequentially, leave the columns **Assembly Time** and **Sequence Number** empty.

### MU Types

Specify the required settings in the table.

- Specify the MU Name of the part, such as Part, Container, Transporter, Shaft, etc., in column 1 and the Amount in column 2.
- Specify the name of the part into the column **MU Name**, not its path, for example `MyMountingPart` and not `*.UserObjects.MyMountingPart`.
- To use the default value 1, do not specify an Amount. To make the AssemblyStation accept parts with this MU Name until the capacity of the main MU is reached, specify `-1` as the Amount.
- Specify the time, in seconds, that each individual part consumes when it's assembled into the column **Assembly Time** and the number of the sequence in which the part is assembled into the column **Sequence Number**. The Assembly Time must be a positive number or 0. If you do not specify a time, the default Assembly Time is 0.
- The Sequence Number must be a positive integer number. The default Sequence Number is 1.
- To assemble the parts non-sequentially, leave the columns **Assembly Time** and **Sequence Number** empty.

### Depends on Main MU

Specify the required settings in the table.

- Specify the Main MU Name of the main MU, such as Part, Container, Transporter, Shaft, etc. Specify an asterisk `*` to handle all main parts which you did not explicitly enter with names of their own into the Assembly Table. Specify the MU Name and the Amount of the parts.
- To use the default value 1, do not specify an Amount. To make the AssemblyStation accept parts with this MU Name until the capacity of the main MU is reached, specify `-1` as the Amount.
- Specify the time, in seconds, that each individual part consumes when it's assembled into the column **Assembly Time** and the number of the sequence in which the part is assembled into the column **Sequence Number**. The Assembly Time must be a positive number or 0. If you do not specify a time, the default Assembly Time is 0.
- The Sequence Number must be a positive integer number. The default Sequence Number is 1.
- To assemble the parts non-sequentially, leave the columns **Assembly Time** and **Sequence Number** empty.

**Note** — For the settings **MU Types** and **Depends on Main MU** this applies:

If the AssemblyStation has objects of type Store as predecessors, it requests the required mounting parts from the Store. If the required parts are not available in the Store at the moment, the Store records the request and delivers the parts to the AssemblyStation once they are available again.

The parts can also be carried from the Store to the AssemblyStation by a Worker. The Store can only provide mounting parts, but no main parts, and it has to be connected with a Connector, even if the Worker carries the part away.

### Fill up Main MU

The AssemblyStation does not use an Assembly Table. Instead, it accepts parts from any of its predecessors until the capacity of the main MU is reached.

**Note** — The columns **Predecessor** and **MU Name** cannot contain duplicate entries.

**Note** — If the assembly table is inherited, inheritance is not automatically deactivated when you write to cells of the assembly table. For this reason you will change the inherited table during an assignment. To deactivate inheritance, assign the assembly table to itself.

**Example**

```simtalk
AssemblyStation.AssemblyTable := AssemblyStation.AssemblyTable  // deactivates inheritance
```

**Example**

```simtalk
var AssemblyTable: table[string,integer]
AssemblyTable.create
AssemblyTable.writeRow(1,1, "MyPartA",1)
AssemblyTable.writeRow(1,2, "MyPartB",2)
MyAssembly.AssemblyTable := AssyList
```

**See also:** Assembly Table

---

## AssemblyTableMode [SimTalk]

Sets the type of the Assembly Table of the AssemblyStation designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.AssemblyTableMode:string`
- **Assignment Value:** You can assign a value of data type `string`.
  - You can specify `"None"`, `"Predecessors"`, `"MUTypes"`, `"Depends on Main MU"`, or `"Fill up Main MU"`.

**Example**

```simtalk
MyAssembly.AssemblyTableMode := "Fill up Main MU"
```

**See also:** Assembly Table

---

## ExitingMU [SimTalk]

Sets what type of MU exits the AssemblyStation designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.ExitingMU:string`
- **Assignment Value:** You can assign a value of data type `string`.
  - Specify `"Main MU"` to make the main MU exit the AssemblyStation.
  - Specify `"New MU"` to make a newly created MU exit it.

**Example**

```simtalk
MyAssembly.ExitingMU := "Main MU"
```

**See also:** Exiting MU [drop-down list] - AssemblyStation

---

## MainMU [SimTalk] - AssemblyStation

Sets the number of the predecessor from which the AssemblyStation designated by `<Path>` pulls the main MU.

- **Type:** Attribute
- **Syntax:** `<Path>.MainMU:integer`
- **Assignment Value:** You can assign a value of data type `integer`.

**Remarks**

Specify `0` if the main part is not delivered by any of the predecessors of the AssemblyStation, e.g. if a Worker transports the main part to the AssemblyStation or if you use a SimTalk command to move the main part to the AssemblyStation.

As the AssemblyStation is connected to at least two stations, the order in which you connect it with the predecessors is important. If the assembly process does not work as expected, check the numbering of the predecessors.

Plant Simulation shows the predecessors and the successors of an object in a Tooltip when you drag the mouse over the respective Connector.

**Example**

```simtalk
MyAssembly.MainMU := 1
MyAssembly.MainMU := 0 // Worker delivers main part via Workplace
```

**See also:** Main MU from Predecessor

---

## NewMU [SimTalk] - AssemblyStation

Sets the path of the MU that the AssemblyStation designated by `<Path>` creates when it deletes the main MU and creates a new MU instead.

- **Type:** Attribute
- **Syntax:** `<Path>.NewMU:string`
- **Assignment Value:** You can assign a value of data type `string`.

**Example**

```simtalk
MyAssembly.NewMU := ".MUs.basicMU"
```

**See also:** Exiting MU [drop-down list] - AssemblyStation

---

## OrderSequence [SimTalk]

Sets the order in which the AssemblyStation designated by `<Path>` requests MUs and/or services.

- **Type:** Attribute
- **Syntax:** `<Path>.OrderSequence:string`
- **Assignment Value:** You can assign a value of data type `string`.
  - You can specify `"MUs then Services"`, `"Services then MUs"`, or `"MUs and Services"`.

**Example**

```simtalk
MyAssembly.OrderSequence := "Services then MUs"
```

**See also:** Sequence [drop-down list] - AssemblyStation

---

## SequentialDelivery [SimTalk]

Makes the Workers deliver the required mounting parts, which the AssemblyStation designated by `<Path>` requested, sequentially one after the other to the AssemblyStation (`true`).

- **Type:** Attribute
- **Syntax:** `<Path>.SequentialDelivery:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Remarks**

- Specify `false` to make a single Worker deliver as many mounting parts as he can carry to the AssemblyStation.
- Specify `false` to make several Workers deliver the mounting parts to the AssemblyStation in parallel at the same time.

**Note**

- If you set `SequentialDelivery` to `true`, the attribute `ReservedFor` returns the object for which the place is currently reserved.
- If you set it to `false`, `ReservedFor` returns an array of objects for which places are reserved.

**Example**

```simtalk
MyAssemblyStation.SequentialDelivery := true
```

**See also:**

- ReservedFor [SimTalk]
- Set How Workers Deliver Mounting Parts
- Workers Sequentially Deliver MUs to Assemble
