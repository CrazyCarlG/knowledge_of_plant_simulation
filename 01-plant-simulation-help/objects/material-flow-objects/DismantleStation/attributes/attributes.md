# DismantleStation — Attributes

Summary of the SimTalk attributes for the `DismantleStation` material flow object.

## General

The `DismantleStation` provides:

- The attributes listed in the table of contents.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

You can set/get attribute values either via dialog check boxes, text boxes and drop-down lists, or by assigning values to the respective attributes:

```simtalk
MyDismantleStation.NewMU := ".MUs.basicMU"   -- set an attribute
print MyDismantleStation.Pause               -- get an attribute
posit := MyStation.Cont.XPos
```

---

## StatAverageDwellTime [SimTalk]

Returns the average time the main parts stayed on the `DismantleStation` designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatAverageDwellTime → time`
- **Return value:** data type `time`

```simtalk
print MyDismantleStation.StatAverageDwellTime
```

**Remarks:** Plant Simulation only counts times during which the `DismantleStation` was not paused and not unplanned.

**See also:** Tab Statistics, Attributes of the DismantleStation

---

## DismantleMode [SimTalk]

Sets how the `DismantleStation` designated by `<Path>` handles the MUs.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.DismantleMode:string`

**Assignment value** (data type `string`):

- `"Create MUs"` — the DismantleStation creates mounting parts.
- `"Detach MUs"` — the DismantleStation detaches the mounting parts from the main MU and moves them to the successor entered in the Dismantle Table.

```simtalk
MyDismantleStation.DismantleMode := "Detach MUs"
```

**Remarks:** To unload only the mounting parts typed into the Dismantle Table, select `Sequence > MUs exiting independent of other MUs` or `Main MU after other MUs` and `Dismantle Mode > Detach MUs`. Always enter a valid MU class into column `MU` and a positive number into column `Number`.

**See also:** Dismantle Table, Sequence, Dismantle Mode

---

## DismantleTable [SimTalk]

Sets the name of the Dismantle Table of the `DismantleStation` designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.DismantleTable:table`
- **Assignment value:** data type `table`

The Dismantle Table contains the names of the MUs that leave the DismantleStation and its successors:

- **Column `MU`** — path to the MU class (e.g. `.MUs.Part`, `.MUs.Container`, `.MUs.Transporter`); leave empty to designate any MU class.
- **Column `Number`** — number of MUs dismantled; default is `1` if not entered.
- **Column `Successor`** — number of the successor; if not entered, the DismantleStation moves mounting parts to successor number `1` for `Detach MUs`, or to the successor the main MU moves to for `Create MUs`.

**Notes:**

- If you enter a **MU Target**, the Worker carries all parts to that target. Otherwise the Dismantle Table or the `Main MU to successor with number` setting determines it.
- To automatically move all parts according to MU class: enter any MU class in `MU`, `-1` in `Number` (all remaining parts of that class), and the successor number. Repeat for other classes.
- To automatically move all parts to one successor: leave `MU` empty, enter `-1` in `Number`, and the successor number.
- **Inheritance:** if the dismantle table is inherited, inheritance is not automatically deactivated when writing to its cells. Deactivate it by assigning the table to itself.

```simtalk
var DismList:table[object,integer,integer]
DismList.create
DismList.writeRow(1,1, .MUs.MyPart,1,1)
DismList.writeRow(1,2, .MUs.MyPart,2,1)
MyDismantleStation.DismantleTable := DismList

-- Deactivates inheritance:
DismantleStation.DismantleTable := DismantleStation.DismantleTable

-- Entrance control example (EntranceCtrlBeforeActions := true):
?.DismantleList := ?.DismantleList    -- deactivates inheritance
?.DismantleList[2, 1] := @.AmountOfParts
```

**See also:** Dismantle Mode, Dismantle Table, Sequence, MU Target, Main MU to Successor with Number

---

## ExitingMUMode [SimTalk]

Sets whether the main MU exits the `DismantleStation` designated by `<Path>`, or a new MU is created which then exits the object.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.ExitingMUMode:string`

**Assignment value** (data type `string`):

- `"Main MU"` — the DismantleStation moves the main MU on to the succeeding object.
- `"New MU"` — the DismantleStation deletes the main MU, creates a new MU, and moves it on to the successor. The DismantleStation then shows the text box `MU`.

```simtalk
MyDismantleStation.ExitingMUMode := "New MU"
```

**See also:** Exiting MU

---

## MainMU [SimTalk]

Sets the number of the successor to which the `DismantleStation` designated by `<Path>` moves the main MU.

- **Type:** Attribute
- **Syntax:** `<Path>.MainMU:integer`
- **Assignment value:** data type `integer`

```simtalk
MyDismantleStation.MainMU := 2
```

**Remarks:** If a MU Target is entered, the Worker carries all parts to that target; otherwise the Dismantle Table or the `Main MU to successor with number` setting determines it.

**See also:** Main MU to Successor with Number, MU Target, Dismantle Table

---

## NewMU [SimTalk]

Sets the path of the MU that the `DismantleStation` designated by `<Path>` creates.

- **Type:** Attribute
- **Syntax:** `<Path>.NewMU:path`
- **Assignment value:** a path

```simtalk
MyDismantleStation.NewMU := .MUs.basicMU
```

**Remarks:** `NewMU` applies when the DismantleStation deletes the main MU and creates a new MU instead.

**See also:** Exiting MU

---

## Sequence [SimTalk]

Sets how the `DismantleStation` designated by `<Path>` distributes the MUs to the successors to which it is connected.

- **Type:** Attribute
- **Syntax:** `<Path>.Sequence:string`

**Assignment value** (data type `string`):

- `"MUs to all successors"`
- `"MUs exiting independent of other MUs"`
- `"Main MU after other MUs"`

```simtalk
MyDismantleStation.Sequence := "Main MU after other MUs"
```

**Remarks:**

- **MUs to all successors** — with `Create MUs`, a new part is created for each successor; the main MU moves to the successor specified in `Main MU to Successor with Number`. With `Detach MUs`, MUs move to each successor in turn except the one receiving the main MU. For example, with four successors and the main MU moving to successor 2, new MUs go to successors 1, 3, and 4.
- **MUs exiting independent of other MUs** — the DismantleStation attempts to move the main MU and then each MU on to the defined successor as soon as possible.
- **Main MU after other MUs** — first moves the mounting parts on to the successor, then the main MU.

To unload only the mounting parts entered in the Dismantle Table, select `MUs exiting independent of other MUs` or `Main MU after other MUs` with `Dismantle mode > Detach MUs`, entering a valid MU class in `MU` and a positive number in `Number`.

**See also:** Sequence, DismantleMode, DismantleTable

---

## PickAndPlace Robot

Use the object **PickAndPlace robot** for picking up a part at one station, rotating it, and placing it onto another station.

The PickAndPlace robot can pick up and deliver one or more parts (set via `Capacity`). It transports parts to successors like this:

1. The part arrives at the exit of the predecessor and notifies the robot it wants to be picked up.
2. The robot determines if it picks the part up:
   - Without a Pull Control, the robot is notified and accepts the part.
   - With a Pull Control, the robot executes it and picks up the part when it is selected.
3. The robot rotates to the respective predecessor and picks the part up.
