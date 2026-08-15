# Conveyor — Attributes (SimTalk)

This document summarizes the SimTalk attributes of the Conveyor object as described in the source help text.

The Conveyor provides:

- The attributes listed below,
- The **Attributes of All Objects**,
- The **Attributes of the Material Flow Objects**.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the members of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show the members of the selected Instance.

You can set or get the value of an attribute via dialog controls or by assigning values in SimTalk:

```simtalk
-- Set
MyConveyor.AccelerationEnabled := false

-- Get
print MyConveyor.AccelerationEnabled
posit := MyStation.Cont.XPos
```

---

## OccupiedLength

Read-only attribute. Returns the section of the entire Length of the Conveyor that is occupied by all MUs located on it.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.OccupiedLength → length`
- **Return Value:** data type `length`

**Example**

```simtalk
print Conveyor.OccupiedLength
```

**See also:** Length, Attributes of the Conveyor

---

## Acceleration

Sets the Acceleration with which the Conveyor increases its speed in m/s².

- **Remarks:** Can only be set after activating Acceleration/AccelerationEnabled.
- **Type:** Attribute
- **Syntax:** `<Path>.Acceleration:acceleration`
- **Watchable:** Yes
- **Assignment Value:** data type `acceleration`. Any real number ≥ 0. The Conveyor accelerates until it reaches its final Speed, regardless of whether an MU is on it.

> **Note (SimTalk 2.0):** You can specify units `mps²`, `cm²`, `fps²`, and `LU/s²`. Type the unit directly after the value without a separating blank space, e.g. `10mps2` or `10.2mps2`.

**Example**

```simtalk
MyConveyor.Acceleration := 3mps2
```

**See also:** AccelerationEnabled, Speed, Acceleration (text box), Acceleration (check box)

---

## AccelerationEnabled

Activates (`true`) or deactivates (`false`) the Acceleration of the Conveyor.

- **Type:** Attribute
- **Syntax:** `<Path>.AccelerationEnabled:boolean`
- **Assignment Value:** data type `boolean`

**Example**

```simtalk
MyConveyor.AccelerationEnabled := false
```

**See also:** Acceleration (check box)

---

## Accumulating

Sets whether succeeding MUs can move up if the first MU cannot exit the Conveyor (`true`), or whether they retain their distance to each other (`false`).

- **Remarks:** If Accumulating is active, the front of the succeeding MU touches the rear of the preceding MU.
- **Type:** Attribute
- **Syntax:** `<Path>.Accumulating:boolean`
- **Watchable:** Yes
- **Assignment Value:** data type `boolean`

**Example**

```simtalk
MyConveyor.Accumulating := true
```

**See also:** Accumulating (check box)

---

## AutomaticStop

Automatically stops the Conveyor; sets the current speed to 0 when it does not transport an MU.

- **Remarks:** May occur when empty or blocked. Speed is set to 0 immediately (without Deceleration), and set back to Target Speed immediately (without Acceleration). If speed is 0, the Energy State changes to operational.
- **Type:** Attribute
- **Syntax:** `<Path>.AutomaticStop:boolean`
- **Assignment Value:** data type `boolean`

**Example**

```simtalk
MyConveyor.AutomaticStop := true
```

**See also:** Automatic Stop (check box), Operational (energy)

---

## Backwards

Sets whether the Conveyor and the MUs on it move in reverse (`true`) or forward (`false`).

- **Remarks:**
  - In reverse, MUs enter at the exit and leave at the entrance.
  - Without Acceleration, direction reverses immediately. With Acceleration, the Conveyor decelerates to 0, reverses, then accelerates to final speed.
  - If a Target Distance is set for the Transporter, `Backwards` cannot be changed.
- **Type:** Attribute
- **Syntax:** `<Path>.Backwards:boolean`
- **Assignment Value:** data type `boolean`

**Example**

```simtalk
MyConveyor.Backwards := false
```

**See also:** AccelerationEnabled, TargetDistance, Backwards (Conveyor), Acceleration (check box)

---

## Capacity

Sets the number of MUs or MU parts that may be located on the Conveyor as a whole or in part at any one time.

- **Remarks:** When reached, no further MUs are accepted, even if full length is not exhausted.
- **Type:** Attribute
- **Syntax:** `<Path>.Capacity:integer`
- **Watchable:** Yes
- **Assignment Value:** data type `integer`. Specify `-1` for infinite capacity.

**Example**

```simtalk
if MyConveyor.Capacity = -1
   @.move(AEstreet)
end
```

**See also:** Capacity (text box), NumMUParts (material flow objects)

---

## CurrentSpeed

Sets the Current Speed of the Conveyor in the forward direction (positive) or reverse (negative).

- **Remarks:** Any real number. Can only be set after activating Acceleration/AccelerationEnabled.
- **Type:** Attribute
- **Syntax:** `<Path>.CurrentSpeed:speed`
- **Watchable:** Yes (for special values; e.g., detect when final speed is reached)
- **Assignment Value:** data type `speed`
- **Return Value:** `inf` if `-1` (infinite speed) is specified.

**Example**

```simtalk
MyConveyor.CurrentSpeed := 2
```

**See also:** Current Speed (text box), Acceleration (check box)

---

## Deceleration

Sets the Deceleration with which the Conveyor decreases its speed.

- **Remarks:** Any real number ≥ 0. Can only be set after activating Acceleration/AccelerationEnabled.
- **Type:** Attribute
- **Syntax:** `<Path>.Deceleration:acceleration`
- **Watchable:** Yes
- **Assignment Value:** data type `acceleration`

**Example**

```simtalk
MyConveyor.Deceleration := 1
```

**See also:** Deceleration (text box), Acceleration (check box)

---

## EnforceMUDistance

Makes the Conveyor keep the specified MU Distance between MUs, even when they accumulate (`true`) or not (`false`).

- **Remarks:** Only applies if the Conveyor is Accumulating and conveys parts forward. Depending on MU Distance Type and the Speed of succeeding Conveyors, the MU distance might increase.
- **Note:** Changing material flow (via information flow or manually) may temporarily decrease the MU Distance:
  - Inserted/created MUs stop until the distance is met again; the following MU keeps distance to the previous MU until the created MU starts moving.
  - If MU Distance is changed while MUs are located, they keep their original distance at first and only move again when the new distance is met.
- **Type:** Attribute
- **Syntax:** `<Path>.EnforceMUDistance:boolean`
- **Assignment Value:** data type `boolean`

**Example**

```simtalk
MyConveyor.EnforceMUDistance := true
```

**See also:** MUDistance, MU Distance Type (text box), Enforce MU Distance (check box), MU Distance (text box), Accumulating (check box)

---

## Length

Sets the Length of the Conveyor.

- **Remarks:** Length and Speed form the processing time on the object.
- **Type:** Attribute
- **Syntax:** `<Path>.Length:length`
- **Watchable:** Yes
- **Assignment Value:** data type `length`

> **Note (SimTalk 2.0):** Units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in` can be specified directly after the value without a blank space, e.g. `10m` or `10.2m`.

**Example**

```simtalk
MyConveyor.Length := 10.0m
```

**See also:** Speed, Length (text box)

---

## MUDistance

Sets the desired distance of the current MU to the succeeding MU that the Conveyor enforces when the next MU enters.

- **Remarks:** Depending on MU Distance Type, the distance determines:
  - **Gap:** distance between the rear of the preceding MU and the front of the succeeding MU.
  - **Pitch:** distance between the front of the preceding MU and the front of the succeeding MU.
  - If no further parts arrive, the Conveyor stops once the distance is reached; it resumes when the next MU arrives.
  - Default `-1` means the Conveyor does not use MU Distance.
- **Notes:** Distance may grow/shrink if preceding or succeeding Conveyors transport faster/slower. Plant Simulation only runs the distance check when an MU enters. The Conveyor only uses MU Distance in the forward direction.
- **Type:** Attribute
- **Syntax:** `<Path>.MUDistance:integer`
- **Assignment Value:** data type `integer`

**Example**

```simtalk
MyConveyor.MUDistance := 1
```

**See also:** MU Distance Type (text box), MU Distance (text box), Model a Fixed Gap or a No Gap Conveyor, Accumulating (check box)

---

## MUDistanceType

Sets the MU Distance Type of the MU Distance of the Conveyor.

- **Remarks:** The Front of the part always moves toward the end of the length-oriented object in the direction of insertion along the material flow; this also applies when moving backward.
- **Type:** Attribute
- **Syntax:** `<Path>.MUDistanceType:string`
- **Assignment Value:** data type `string`. Allowed values: `"Gap"`, `"Pitch"`, `"Minimum Gap"`, `"Minimum Pitch"`, `"Multiple Gap"`, `"Multiple Pitch"`.

The available settings are:

- **Gap** — distance between the rear of the preceding part and the front of the succeeding part.
- **Pitch** — distance between the front of the preceding part and the front of the succeeding part.
- **Minimum Gap** — minimum distance between rear of preceding MU and front of succeeding MU; prevents the Conveyor from stopping/waiting and enables it to run dry.
- **Minimum Pitch** — minimum distance between front of preceding MU and front of succeeding MU; same behavior.
- **Multiple Gap** — gap can be an integer multiple of the defined MU Distance; the Conveyor does not stop to wait for new MUs.
- **Multiple Pitch** — pitch can be an integer multiple of the defined MU Distance; behaves like a chain conveyor.

**Example**

```simtalk
MyConveyor.MUDistanceType := "Pitch"
```

**See also:** MU Distance Type (text box), MU Distance (text box), Model a Fixed Gap or a No Gap Conveyor, Accumulating (check box)

---

## Speed

Sets the Speed with which the Conveyor transports the MUs.

- **Remarks:** Speed and Length form the Processing Time (Length ÷ Speed). Enter `-1` for infinite speed.
- **Note:** Changing Speed re-computes all speed-related events for MUs on the object; a new Out event may be scheduled and Exit Control may be called again regardless of `ExitControlOnce`.
- **Type:** Attribute
- **Syntax:** `<Path>.SpeedCtrl:speed`
- **Watchable:** Yes
- **Assignment Value:** data type `speed`

**Example**

```simtalk
MyConveyor.Speed := 0.5 // meters per second
```

**See also:** Length, ExitCtrlOnce, Speed (text box), Out event

---

## SpeedCtrl

Designates a Method object of the object.

- **Remarks:** The Conveyor / loading space (Line of the Transporter) calls the Method when it reaches final speed after accelerating/decelerating, or when it stops after decelerating. Not called if speed changes without taking time. Attribute is `VOID` if no Method is entered. Can only be set after activating Acceleration/AccelerationEnabled.
- **Type:** Attribute
- **Syntax:** `<Path>.SpeedCtrl:method`
- **Assignment Value:** data type `method`

**Example**

```simtalk
MyConveyor.SpeedCtrl := &mySpeedControl
```

**See also:** AccelerationEnabled, Speed Control (Conveyor), Acceleration (check box)

---

## Time

Sets the Time which the MU spends moving on the Conveyor.

- **Remarks:** Time divided by Length yields the Speed.
- **Type:** Attribute
- **Syntax:** `<Path>.Time:time`
- **Assignment Value:** data type `time`

**Example**

```simtalk
MyConveyor.Time := 60
```

**See also:** Length, Time (text box)

---

## Attribute Quick Reference

| Attribute | Type | Syntax | Watchable |
|-----------|------|--------|-----------|
| OccupiedLength | Read-only | `<Path>.OccupiedLength → length` | — |
| Acceleration | Attribute | `<Path>.Acceleration:acceleration` | Yes |
| AccelerationEnabled | Attribute | `<Path>.AccelerationEnabled:boolean` | — |
| Accumulating | Attribute | `<Path>.Accumulating:boolean` | Yes |
| AutomaticStop | Attribute | `<Path>.AutomaticStop:boolean` | — |
| Backwards | Attribute | `<Path>.Backwards:boolean` | — |
| Capacity | Attribute | `<Path>.Capacity:integer` | Yes |
| CurrentSpeed | Attribute | `<Path>.CurrentSpeed:speed` | Yes (special values) |
| Deceleration | Attribute | `<Path>.Deceleration:acceleration` | Yes |
| EnforceMUDistance | Attribute | `<Path>.EnforceMUDistance:boolean` | — |
| Length | Attribute | `<Path>.Length:length` | Yes |
| MUDistance | Attribute | `<Path>.MUDistance:integer` | — |
| MUDistanceType | Attribute | `<Path>.MUDistanceType:string` | — |
| Speed | Attribute | `<Path>.SpeedCtrl:speed` | Yes |
| SpeedCtrl | Attribute | `<Path>.SpeedCtrl:method` | — |
| Time | Attribute | `<Path>.Time:time` | — |
