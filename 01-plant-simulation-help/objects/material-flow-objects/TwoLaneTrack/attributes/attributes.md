# Attributes of the TwoLaneTrack

The TwoLaneTrack provides:

- The attributes listed below.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

> **Note:** A number of attributes, which the TwoLaneTrack shares with the other material flow objects, apply to a lane instead of to the entire object. The dialog shows `A` and `B` for the respective lane, but not the attributes proper for these lanes.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

```simtalk
-- Set the value of an attribute
MyTwoLaneTrack.B.Length := 44

-- Get the value of an attribute
print MyTwoLaneTrack.B.Length
posit := MyStation.Cont.XPos
```

---

## OccupiedLength [SimTalk] - lane A or B

Returns the part of the entire length of the specified lane of the TwoLaneTrack designated by `<Path>` which is occupied by all Transporters located on it.

- **Type:** Read-only attribute
- **Syntax:**
  ```simtalk
  <Path>.A.OccupiedLength → length
  <Path>.B.OccupiedLength → length
  ```
- **Return Value:** `length`
- **Example:**
  ```simtalk
  print myTwoLaneTrack.A.OccupiedLength
  ```

---

## BwEntranceCtrl [SimTalk] - lane A or B

Designates a Method object of the object designated by `<Path>`. Plant Simulation calls the Method when a Transporter enters the specified lane of the TwoLaneTrack via its exit and/or when the Transporter moves toward its entrance after entering.

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.BwEntranceCtrl:method
  <Path>.B.BwEntranceCtrl:method
  ```
- **Assignment Value:** `method`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.B.BwEntranceCtrl := &MyBackwardEntranceMethod
  ```

---

## BwEntranceCtrlFront [SimTalk] - lane A or B

Sets if the TwoLaneTrack activates the Backward Entrance Control as soon as the **Front** of the Transporter enters the TwoLaneTrack on the designated lane via its exit and/or when it moves toward its entrance after entering (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.BwEntranceCtrlFront:boolean
  <Path>.B.BwEntranceCtrlFront:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.B.BwEntranceCtrl := &Method1
  MyTwoLaneTrack.B.BwEntranceCtrlFront := false
  ```

---

## BwEntranceCtrlRear [SimTalk] - lane A or B

Sets if the TwoLaneTrack activates the Backward Entrance Control as soon as the **Rear** of the Transporter enters the TwoLaneTrack via its exit and/or when it moves toward its entrance after entering (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.BwEntranceCtrlRear:boolean
  <Path>.B.BwEntranceCtrlRear:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.BwEntranceCtrl := &MyMethod
  MyTwoLaneTrack.A.BwEntranceCtrlRear := false
  MyTwoLaneTrack.B.BwEntranceCtrl := &MyBackwardEntranceMethod
  MyTwoLaneTrack.B.BwEntranceCtrlRear := true
  ```

---

## BwExitCtrl [SimTalk] - lane A or B

Designates a Method object of the object designated by `<Path>`. Plant Simulation calls the Method when a Transporter exits the designated lane of the TwoLaneTrack via its entrance and/or when the Transporter moves toward its entrance when exiting.

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.BwExitCtrl:method
  <Path>.B.BwExitCtrl:method
  ```
- **Assignment Value:** `method`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.B.BwExitCtrl := &MyBackwardExitMethod
  ```

---

## BwExitCtrlFront [SimTalk] - lane A or B

Sets if the TwoLaneTrack activates the Backward Exit Control as soon as the **Front** of the Transporter exits the designated lane via its entrance and/or when the Transporter moves toward its entrance when exiting (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.BwExitCtrlFront:boolean
  <Path>.B.BwExitCtrlFront:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.B.BwExitCtrl := &MyBackwardExitMethod
  MyTwoLaneTrack.A.BwExitCtrlFront := false
  ```

---

## BwExitCtrlRear [SimTalk] - lane A or B

Sets if the TwoLaneTrack activates the Backward Exit Control as soon as the **Rear** of the Transporter exits the designated lane via its entrance and/or when the Transporter moves toward its entrance when exiting (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.BwExitCtrlRear:boolean
  <Path>.B.BwExitCtrlRear:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.B.BwExitCtrl := &MyBackwardExitMethod
  MyTwoLaneTrack.B.BwExitCtrlRear := true
  ```

---

## Capacity [SimTalk] - TwoLaneTrack

Sets the maximum number of Transporters that may be located on the TwoLaneTrack designated by `<Path>` as a whole or in part at any one time.

- **Type:** Attribute
- **Watchable:** yes
- **Syntax:**
  ```simtalk
  <Path>.Capacity:integer
  ```
- **Assignment Value:** `integer` (specify `-1` for an infinite Capacity)
- **Example:**
  ```simtalk
  if MyTwoLaneTrack.Capacity = -1
     @.move(AEConveyor)
  end
  ```

---

## DestListA [SimTalk] - TwoLaneTrack

Sets the path to the Destination List for Transporters which drive in the forward direction on Lane A on the TwoLaneTrack designated by `<Path>`.

The forward destination list of Lane A concurrently is the backward destination list of Lane B.

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.DestListA:object
  ```
- **Assignment Value:** `object`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.DestListA := MyDataList1
  ```

---

## DestListB [SimTalk] - TwoLaneTrack

Sets the path to the Destination List for Transporters which drive in the forward direction on Lane B on the TwoLaneTrack designated by `<Path>`.

The forward destination list of Lane B concurrently is the backward destination list of Lane A.

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.DestListB:object
  ```
- **Assignment Value:** `object`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.DestListB := MyDataList2
  ```

---

## EntranceCtrl [SimTalk] - lane A or B

Designates a Method object of the object designated by `<Path>`. Plant Simulation calls the Method as soon as a Transporter enters the TwoLaneTrack designated by `<Path>` on the specified lane.

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.EntranceCtrl:method
  <Path>.B.EntranceCtrl:method
  ```
- **Assignment Value:** `method`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.EntranceCtrl := &MyEntranceMethod
  ```

---

## EntranceCtrlFront [SimTalk] - lane A or B

Sets if the TwoLaneTrack triggers the entrance control on the specified lane as soon as the **front** of the Transporter enters the TwoLaneTrack (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.EntranceCtrlFront:boolean
  <Path>.B.EntranceCtrlFront:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.EntranceCtrl := &MyEntranceMethod
  MyTwoLaneTrack.A.EntranceCtrlFront := true
  ```

---

## EntranceCtrlRear [SimTalk] - lane A or B

Sets if the TwoLaneTrack triggers the entrance control on the specified lane as soon as the **rear** of the Transporter enters the TwoLaneTrack (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.EntranceCtrlRear:boolean
  <Path>.B.EntranceCtrlRear:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.EntranceCtrl := &MyEntranceMethod
  MyTwoLaneTrack.A.EntranceCtrlRear := true
  ```

---

## EntranceLocked [SimTalk] - lane A or B

Locks the entrance of Lane A/B of the TwoLaneTrack designated by `<Path>` (`true`) or not (`false`). It thus prevents Transporters from entering the object.

The TwoLaneTrack will finish transporting the Transporters already located on it. It does not accept any additional Transporters and enters them into the Blocking List of Lane A/B:

- If the Transporter wants to enter at its entrance, it is entered into the **Forward Blocking List** of Lane A/B.
- If the Transporter is moving backward and wants to enter a length-oriented object at its exit, it is entered into the **Exit Blocking List** of Lane A/B.

The TwoLaneTrack starts transporting again when you set the attribute to `false`. The first Transporter in the Forward Blocking List is moved on first.

- **Type:** Attribute
- **Watchable:** yes
- **Syntax:**
  ```simtalk
  <Path>.A.EntranceLocked:boolean
  <Path>.B.EntranceLocked:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.B.EntranceLocked := true
  waituntil MyTwoLaneTrack.B.NumMu 10 prio 1
  MyTwoLaneTrack.B.EntranceLocked := false
  ```

---

## ExitCtrl [SimTalk] - lane A or B

Designates a Method object of the object designated by `<Path>`. Plant Simulation calls the Method as soon as a Transporter exits the TwoLaneTrack designated by `<Path>` on the specified lane.

If you did not specify a Method, the attribute is `VOID`.

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.ExitCtrl:method
  <Path>.B.ExitCtrl:method
  ```
- **Assignment Value:** `method`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.ExitCtrl := &MyExitMethod
  ```

---

## ExitCtrlFront [SimTalk] - lane A or B

Sets if the TwoLaneTrack triggers the Exit Control as soon as the **front** of the Transporter exits on the specified lane (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.ExitCtrlFront:boolean
  <Path>.B.ExitCtrlFront:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.ExitCtrl := &MyExitMethod
  MyTwoLaneTrack.A.ExitCtrlFront := false
  ```

---

## ExitCtrlRear [SimTalk] - lane A or B

Sets if the TwoLaneTrack triggers the Exit Control as soon as the **rear** of the Transporter exits on the specified lane (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.ExitCtrlRear:boolean
  <Path>.B.ExitCtrlRear:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.ExitCtrl := &MyExitMethod
  MyTwoLaneTrack.A.ExitCtrlRear := true
  ```

---

## ExitLocked [SimTalk] - lane A or B

Locks the exit of Lane A/B of the TwoLaneTrack designated by `<Path>` (`true`) or not (`false`). It thus prevents Transporters from leaving the object.

The TwoLaneTrack does not transport the Transporters to the successor in the material flow, but enters them into the Exit Blocking List of Lane A/B. Once the exit is unlocked again, the TwoLaneTrack moves the first Transporter in the Exit Blocking List on to its successor.

> **Note:** The Transporter does not trigger the Exit Control if you set `ExitLocked` to `true`.

- **Type:** Attribute
- **Watchable:** yes
- **Syntax:**
  ```simtalk
  <Path>.A.ExitLocked:boolean
  <Path>.B.ExitLocked:boolean
  ```
- **Assignment Value:** `boolean`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.ExitLocked := true
  ```

---

## Length [SimTalk] - lane A or B

Sets the physical length of the specified lane of the TwoLaneTrack designated by `<Path>`.

A Transporter enters the specified lane of the TwoLaneTrack at position 0 and exits after covering the length you enter here. Speed and Length yield the dwelling time on the TwoLaneTrack.

- **Type:** Attribute
- **Watchable:** yes
- **Syntax:**
  ```simtalk
  <Path>.A.Length:length
  <Path>.B.Length:length
  ```
- **Assignment Value:** `length`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.Length := 44    -- meters
  MyTwoLaneTrack.B.Length := 43.8  -- meters
  ```

---

## PullCtrl [SimTalk] - lane A or B

Designates a Method object of the object designated by `<Path>`. Plant Simulation calls the Method when the TwoLaneTrack is ready to accept a new Transporter on the specified lane or when it is ready, when a new Transporter is Waiting at its entrance.

In the Pull Control you can determine which Transporter, which intends to move onto the TwoLaneTrack, the TwoLaneTrack will accept. For this you have to get the Forward Blocking List of the respective lane with the method `fwBlockList` and unblock a Transporter in the list with the method `unblock`.

> **Note:** If you only need the first entry of the Forward Blocking List, use the read-only-attribute `FwBlockListEntry1` — access is much faster than with the method `fwBlockList`.

> **Note:** The Pull Control does not determine if a Transporter is to be moved on to this successor or to another successor; it selects one of the Transporters which already decided to move to this successor.

> **Note:** For the TwoLaneTrack the Pull Control only applies to Transporters that drive forward (entering at the entrance and exiting at the exit). It does not apply to Transporters driving in reverse entering at the exit, nor to Transporters that have been moved to a certain position.

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.A.PullCtrl:method
  <Path>.B.PullCtrl:method
  ```
- **Assignment Value:** `method`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.A.PullCtrl := &MyPullMethod
  ```

---

## TrackPitch [SimTalk]

Sets the Track Pitch, which is the distance between the center lines of the two lanes of the TwoLaneTrack designated by `<Path>`.

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.TrackPitch:length
  ```
- **Assignment Value:** `length`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.TrackPitch := 5
  ```

---

## Traffic [SimTalk] - TwoLaneTrack

Sets the side of the TwoLaneTrack designated by `<Path>` on which the bidirectional traffic moves.

- **Type:** Attribute
- **Syntax:**
  ```simtalk
  <Path>.Traffic:string
  ```
- **Assignment Value:** `string` — `"Right-hand traffic"` or `"Left-hand traffic"`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.traffic := "left-hand traffic"
  ```

---

## Width [SimTalk] - TwoLaneTrack

Sets the width of the TwoLaneTrack designated by `<Path>`.

> **Note:** In SimTalk 2.0 you can specify the length units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in`. Type the unit directly after the value, without a separating blank space, for example `10m` or `10.2m`.

- **Type:** Attribute
- **Watchable:** yes
- **Syntax:**
  ```simtalk
  <Path>.Width:length
  ```
- **Assignment Value:** `length`
- **Example:**
  ```simtalk
  MyTwoLaneTrack.Width := 4
  ```
