# Read-Only Attributes of the Tank

The Tank provides:

- The **General Read-Only Attributes of the Tank**
- The **Read-Only Attributes of the Sensors of the Tank**
- The **Read-Only Attributes of the Fluid Objects**
- The **Read-Only Attributes of All Objects**

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Tank.Full
```

---

## General Read-Only Attributes of the Tank

### CurrentAmount

Returns the **Current Amount** of the material in the Tank designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.CurrentAmount → real`
- **Return Value:** `real` — measured in liters

```simtalk
print MyTank.CurrentAmount
```

**See also:** Current Amount [Tank]

---

### CurrentFillLevel

Returns the **Current Fill Level** of the material in the Tank designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.CurrentFillLevel → real`
- **Return Value:** `real` — measured in percent

```simtalk
print MyTank.CurrentFillLevel
```

**See also:** Current Fill Level [Tank]

---

### CurrentMaterial

Returns the **Current Material**, which is located in the Tank designated by `<Path>`.

> **Remarks:** The Tank can only accommodate a single type of material at any one time. The inflow of a new material is blocked until the Tank is empty, so you cannot let another material flow into the Tank before it is empty all the way.
>
> **Note:** The name is not case-sensitive, just like the names of attributes and methods of the objects are not case-sensitive. To save memory and improve access speed, all places using such a case-insensitive string point to the same string in main memory. The visible and unexpected result is that the first occurrence of the string defines how the string is written in terms of upper- and lower-casing. In SimTalk you can compare strings in a case-insensitive manner with the `~=` operator.

- **Type:** Read-only attribute (watchable)
- **Syntax:** `<Path>.CurrentMaterial → string`
- **Return Value:** `string`

```simtalk
print MyTank.CurrentMaterial
```

**See also:** Current Material [Tank], Relational Operators

---

### Empty

Returns whether the Tank designated by `<Path>` is **Empty** (`true`) or not (`false`).

- **Type:** Read-only attribute (watchable)
- **Syntax:** `<Path>.Empty → boolean`
- **Return Value:** `boolean`

```simtalk
print MyTank.Empty
```

---

### Full

Returns whether the Tank designated by `<Path>` is **Full** (`true`) or not (`false`).

- **Type:** Read-only attribute (watchable)
- **Syntax:** `<Path>.Full → boolean`
- **Return Value:** `boolean`

```simtalk
print MyTank.Full
```

---

### StatRelativeOccupation

Returns the **Relative Occupancy** of the Tank designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatRelativeOccupation → real`
- **Return Value:** `real`

```simtalk
print MyTank.StatRelativeOccupation
```

**See also:** Tab Statistics [Tank]

---

### StatThroughput

Returns the **Throughput**, i.e., the amount of material that flowed through the Tank designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatThroughput → real`
- **Return Value:** `real` — measured in liters

```simtalk
print MyTank.StatThroughput
```

**See also:** Tab Statistics [Tank]

---

## Read-Only Attributes of the Sensors of the Tank

### ID

Returns the unique identifier of a sensor of the Tank designated by `<Path>`, allowing you to access it.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.Sensor.ID → integer`
- **Return Value:** `integer`

```simtalk
// Deletes all sensors of the Tank that are triggered
// when the amount of material exceeds the sensor position.
for i := MyTank.numSensors downto 1
   if MyTank.sensorNo(i).Exceeded = true
      sensorID := MyTank.sensorNo(i).ID
      MyTank.deleteSensor(sensorID)
   end
next
```

**See also:** Sensors [Tank]

---

### NumSensors

Returns the number of sensors defined for the Tank designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.NumSensors → integer`
- **Return Value:** `integer`

```simtalk
print MyTank.NumSensors
```

**See also:** Sensors [Tank]

---

### Origin

Returns the origin of the sensor of the Tank designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.Sensor.Origin → integer`
- **Return Value:** `integer` — if the sensor does not have an origin, it returns `VOID`.

```simtalk
print MyTank.Sensors.id1.Origin
```

**See also:** Sensors [Tank]

---

## Related Methods

### sensors.ID

Returns the specified sensor of the Tank designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.sensors.ID(<Number>) → any`
- **Return Value:** `any` — the number after the ID designates the unique identifier which Plant Simulation assigns when you create the sensor.

```simtalk
MyTank.sensors.ID3.Front := true

var sensor := MyTank.sensors.ID2
sensor.Front := true
```

**See also:** Sensors [Tank], New [sensor]
