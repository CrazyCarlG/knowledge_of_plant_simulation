# Attributes of the FlowControl

This document summarizes the attributes of the **FlowControl** material flow object in Plant Simulation.

## Overview

- Attributes that are unavailable in a dialog appear grayed out (corresponding to an unavailable dialog item on one of the tabs, e.g. **Statistics**).
- To view all methods, read-only attributes, and attributes of an object, open **Show Attributes and Methods**:
  - **Class Library** context menu → *Show Attributes and Methods* (for the selected Class).
  - Press **F8** or click *Show Attributes and Methods* on the **Home** ribbon tab of the Frame (for the selected Instance).
- To query a read-only attribute:

```simtalk
print MyFlowControl.UUID
```

The FlowControl provides:
- The attributes listed below.
- The *Attributes of All Objects*.

Since the FlowControl cannot receive any MUs, it does **not** have the attributes that other material flow objects provide.

### Setting and getting values

You can set/get attribute values via dialog check boxes, text boxes, drop-down lists, or by assigning values in SimTalk.

```simtalk
flowcontrol.name := "MyFlowControl"      -- set a value
print flowcontrol.DefaultSuccessor        -- get a value
posit := MyStation.Cont.XPos
```

---

## AttributeType

Sets the data type of the attribute that determines how the FlowControl moves the MUs on.

- **Applies to:** Exit Strategy > MU Attribute
- **Syntax:** `<Path>.AttributeType:string`
- **Assignment value:** string

```simtalk
MyFlowControl.AttributeType := "integer"
```

---

## DefaultSuccessor

Sets the number of the default successor to which the FlowControl moves the MUs.

- **Remarks:**
  - Applies if none of the MUs has an attribute with the value entered into the DataTable.
  - Specify `0` to not move a MU that does not meet any of the table conditions.
  - Specify `-1` to show a message when a MU does not meet any condition in the DataTable.
- **Syntax:** `<Path>.DefaultSuccessor:integer`
- **Assignment value:** integer

```simtalk
MyFlowControl.DefaultSuccessor := 1
```

---

## EntryBehavior

Sets the strategy according to which the FlowControl receives the MUs from its predecessors.

- **Syntax:** `<Path>.EntryBehavior:string`
- **Assignment value:** string

Available strategies:

| Strategy | Description |
| --- | --- |
| `Cyclic` | Cyclically receive MUs from all predecessors. |
| `Cyclic Sequence` | Cyclically receive MUs according to the sequence of predecessors typed into the list. |
| `First come, first served` | Receive MUs from predecessors in the order they intended to exit. |
| `Least recently used` | Receive MUs from the predecessor that has not provided a MU for the longest time. |
| `Method` | Receive MUs from the predecessor defined by the return value of a Method. |
| `Most recently used` | Receive MUs from the predecessor from which the FlowControl last received a MU. |
| `Percentage` | Receive MUs from predecessors according to a percentage distribution. |
| `Random` | Receive MUs from predecessors in a random fashion. |
| `Selection` | Receive MUs according to the state and material flow balance of the predecessors (specify a Property). |
| `Start at Predecessor 1` | Receive MUs from the first available predecessor. |

```simtalk
MyFlowControl.EntryBehavior := "random"
```

---

## EntryBlocking

Sets whether the FlowControl uses blocking behavior when a MU enters the FlowControl (`true`) or not (`false`).

- **Syntax:** `<Path>.EntryBlocking:boolean`
- **Assignment value:** boolean

```simtalk
MyFlowControl.entryBlocking := true
```

---

## EntryDistribution

Sets the random number distribution of the FlowControl.

- **Remarks:** Applies when `EntryBehavior` is set to `Random`.
- **Syntax:** `<Path>.EntryDistribution:time`
- **Assignment value:** time

```simtalk
MyFlowControl.EntryBehavior := "random"
MyFlowControl.EntryDistribution.Type := "normal"
MyFlowControl.EntryDistribution.Mu := 5
MyFlowControl.EntryDistribution.Sigma := 1
```

---

## EntrySelectionMethod

Sets the name of the Method object used by the FlowControl.

- **Remarks:** Applies when `EntryBehavior` is set to `Method`.
- **Note:** You cannot move or delete MUs in the Method (Plant Simulation calls it like a formula). The **Expressions** tab of the Method Debugger is not shown. You also cannot use `wait`, `waituntil`, or `stopuntil` instructions within the Method.
- **Syntax:** `<Path>.EntrySelectionMethod:method`
- **Assignment value:** method

```simtalk
MyFlowControl.EntryBehavior := "method"
MyFlowControl.EntrySelectionMethod := &myMethod
```

---

## EntrySelectionProperty

Sets the selection criterion used by the FlowControl.

- **Remarks:** Applies when `EntryBehavior` is set to `Selection`.
- **Syntax:** `<Path>.EntrySelectionProperty:string`
- **Assignment value:** string

Allowed values:
`"Max. Contents"`, `"Min. Contents"`, `"Max. Proc. Time"`, `"Min. Proc. Time"`, `"Max. Num. Out"`, `"Min. Num. Out"`, `"Max. Rel. Occu."`, `"Min. Rel. Occu."`

```simtalk
MyFlowControl.EntryBehavior := "selection"
MyFlowControl.EntrySelectionProperty := "Max. Contents"
```

---

## ExitBehavior

Sets the strategy according to which the FlowControl moves the MUs on to its successors.

- **Syntax:** `<Path>.ExitBehavior:string`
- **Assignment value:** string

Available strategies:

| Strategy | Description |
| --- | --- |
| `Assignment` | Does not determine the successor. Changes MU attribute values when the MU moves to the single successor. Plant Simulation calls the Method entered in the Method text box to define the assignments. |
| `Cyclic` | Move MUs cyclically on to all successors. |
| `Cyclic Sequence` | Cyclically move MUs according to the sequence of successors typed into a list. |
| `Least recently used` | Move MUs to the successor that has been waiting the longest. |
| `Method` | Move MUs according to the return value of a Method (cannot move/delete MUs; no `wait`/`waituntil`/`stopuntil`). |
| `Most recently used` | Move MUs to the successor that has been waiting the shortest time. |
| `MU Attribute` | Move MUs according to the values of MU attributes. |
| `MU Name` | Move MUs according to their names. |
| `Percentage` | Move MUs according to a percentage distribution. |
| `Random` | Move MUs to a randomly selected successor. |
| `Selection` | Move MUs to the successor meeting a certain Property (specify a Property). |
| `Start at Successor 1` | Move MUs to the first available successor. |
| `To all Successors` | Copy the MUs that enter, moving a copy to each successor. |

```simtalk
MyFlowControl.ExitBehavior := "random"
```

---

## ExitBlocking

Sets whether the FlowControl uses blocking behavior when a MU exits the FlowControl (`true`) or not (`false`).

- **Remarks:** The non-blocking strategy of the setting Exit Strategy > MU Attribute moves the part on when any of the desired successors can receive it.
- **Syntax:** `<Path>.ExitBlocking:boolean`
- **Assignment value:** boolean

```simtalk
MyFlowControl.ExitBlocking := true
```

---

## ExitDistribution

Sets the random number distribution used by the FlowControl.

- **Remarks:** Applies when `ExitBehavior` is set to `"Random"`.
- **Syntax:** `<Path>.ExitDistribution:randTime`
- **Assignment value:** time

```simtalk
MyFlowControl.ExitBehavior := "random"
MyFlowControl.ExitDistribution.Type := "normal"
MyFlowControl.ExitDistribution.Mu := 5
MyFlowControl.ExitDistribution.Sigma := 1
```

---

## ExitSelectionMethod

Sets the name of the Method object used by the FlowControl.

- **Remarks:** Applies when `ExitBehavior` is set to `Method`.
- **Note:** You cannot move or delete MUs in the Method (Plant Simulation calls it like a formula). The **Expressions** tab of the Method Debugger is not shown. You also cannot use `wait`, `waituntil`, or `stopuntil` instructions within the Method.
- **Syntax:** `<Path>.ExitSelectionMethod:method`
- **Assignment value:** method

```simtalk
MyFlowControl.ExitBehavior := "method"
MyFlowControl.ExitSelectionMethod := &myMethod
```

---

## ExitSelectionProperty

Sets the selection property used by the FlowControl.

- **Remarks:** Applies when `ExitBehavior` is set to `Selection`.
- **Syntax:** `<Path>.ExitSelectionProperty:string`
- **Assignment value:** string

Allowed values:
`"Max. Contents"`, `"Min. Contents"`, `"Max. Rel. Occu."`, `"Min. Rel. Occu."`, `"Max. Num. In"`, `"Min. Num. In"`, `"Max. Proc. Time"`, `"Min. Proc. Time"`, `"Max. Set-up Time"`, `"Min. Set-up Time"`

```simtalk
MyFlowControl.ExitBehavior := "Selection"
MyFlowControl.ExitSelectionProperty := "Max. contents"
```

---

## Related: Cycle

The **Cycle** object synchronizes the transfer of parts from station to station.

- Use Cycle to only move a part on to the next station within a balanced line when all stations have finished processing and none is failed, paused, or unplanned. The successor of the balanced line must also be ready to receive the part.
- Define the balanced line by typing the names of the **First Station** and **Last Station**. All connected stations between them form the balanced line. Each station must have exactly one predecessor and one successor.
- **Note:** Only objects of type `Station` and `AssemblyStation` can be part of the balanced line. For an `AssemblyStation`, the Cycle continues balancing only after the assembly process finishes.
- A **Front-triggered Exit Control** is only called for the last station of the cycle (the Destination for all other stations is already set). Use a **Rear-triggered Exit Control** instead.
- A **Pull Control** is not called for the stations of the Cycle object.
- You can insert as many Cycle objects as needed; they work independently. Assign each station to only a single Cycle object.
- Drag a Station/AssemblyStation onto the Cycle icon to set it as the first station; drag another to set it as the last station. To change the last station, hold down **Shift** while dragging the object over the Cycle.
- Hover over the Cycle to show a tooltip with information.
