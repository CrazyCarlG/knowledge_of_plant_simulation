# Read-Only Attributes of the Drain

## Overview

The **Drain** provides:

- The read-only attributes listed below.
- The **Read-Only Attributes of All Objects**.
- The **Read-Only Attributes of the Material Flow Objects**.

You can query the values of the read-only attributes, but you cannot set them, since Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Drain.StatAvgExitInterval
```

## Attribute Summary

| Attribute | Return Type | Description |
|-----------|-------------|-------------|
| `StatAvgExitInterval` | time | Average time interval between exits of removed MUs |
| `StatAvgLifeSpan` | time | Average life span of the removed MUs |
| `StatDeleted` | integer | Number of MUs removed from the plant |
| `StatProdFailPortion` | real | Portion of life time on failed Production resources |
| `StatProdPausingPortion` | real | Portion of life time on paused/unplanned Production resources |
| `StatProdSetupPortion` | real | Portion of life time on setting-up Production resources |
| `StatProdStoppedPortion` | real | Time portion on Production resources stopped by LockoutZone |
| `StatProdWaitingPortion` | real | Portion of life time on waiting Production resources |
| `StatProdWorkingPortion` | real | Portion of life time on working Production resources |
| `StatStoreFailPortion` | real | Portion of life time on failed Storage resources |
| `StatStorePausingPortion` | real | Portion of life time on paused/unplanned Storage resources |
| `StatStoreSetUpPortion` | real | Portion of life time on setting-up Storage resources |
| `StatStoreStoppedPortion` | real | Time portion on Store resources stopped by LockoutZone |
| `StatStoreWaitingPortion` | real | Portion of life time on waiting Storage resources |
| `StatStoreWorkingPortion` | real | Portion of life time on working Storage resources |
| `StatThroughputPerDay` | real | MUs removed per day (throughput per hour × 24) |
| `StatThroughputPerHour` | real | MUs removed per hour |
| `StatThroughputPerMinute` | real | MUs removed per minute |
| `StatTranspFailPortion` | real | Portion of life time on failed Transport resources |
| `StatTranspPausingPortion` | real | Portion of life time on paused/unplanned Transport resources |
| `StatTranspSetupPortion` | real | Portion of life time on setting-up Transport resources |
| `StatTranspStoppedPortion` | real | Time portion on Transport resources stopped by LockoutZone |
| `StatTranspWaitingPortion` | real | Portion of life time on waiting Transport resources |
| `StatTranspWorkingPortion` | real | Portion of life time on working Transport resources |

## Attributes in Detail

### StatAvgExitInterval

Returns the average time interval between exits of the MUs which the Drain designated by `<Path>` removed from the plant.

**Remarks:** `StatAvgExitInterval` results from adding up the times of all intervals, and then dividing them by the number of intervals. Statistics only starts counting from the time at which the first MU arrived.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatAvgExitInterval → time`
- **Return Value:** The return value has the data type `time`.

**Example:**

```simtalk
print MyDrain.StatAvgExitInterval
```

---

### StatAvgLifeSpan

Returns the average life span of the MUs which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatAvgLifeSpan → time`
- **Return Value:** The return value has the data type `time`.

**Example:**

```simtalk
print MyDrain.StatAvgLifeSpan
```

---

### StatDeleted

Returns the number of MUs which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatDeleted → integer`
- **Return Value:** The return value has the data type `integer`.

**Example:**

```simtalk
print MyDrain.StatDeleted
```

---

### StatProdFailPortion

Returns the portion of the sum of all life times of the MUs during which these stayed on a failed material flow object of resource type **Production**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatProdFailPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
var ra: real
ra := Drain.StatProdFailPortion + Drain.StatStoreFailPortion + 
Drain.StatTranspFailPortion
if ra > 0.6 
   print "Considerable delays caused by failed machines."
end
```

---

### StatProdPausingPortion

Returns the portion of the sum of all life times of the MUs during which these stayed on a paused or unplanned material flow object of resource type **Production**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatProdPausingPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDrain.StatProdPausingPortion
```

---

### StatProdSetupPortion

Returns the portion of the sum of all life times of the MUs during which these stayed on a material flow object of resource type **Production** that was setting-up for the MU type, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatProdSetUpPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
var ra,wa: real
wa := MyDrain.StatProdWaitingPortion
print "The waiting time portion on resources of resource type Production 
for all parts is ", round(100*(wa),2)," %."
ra := MyDrain.StatProdSetUpPortion
print "The set-up time portion on resources of resource type Production for 
all parts is ", round(100*(ra),2)," %."
```

---

### StatProdStoppedPortion

Returns the time portion during which the MU was located on a material flow object of resource type **Production** that was stopped by a LockoutZone, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatProdStoppedPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print Drain.StatProdStoppedPortion
```

---

### StatProdWaitingPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a waiting material flow object of resource type **Production**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatProdWaitingPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
var ra,wa: real
wa := MyDrain.StatProdWaitingPortion
print "The waiting time portion on resources of resource type Production 
for all parts is ", round(100*(wa),2)," %."
ra := MyDrain.StatProdSetUpPortion
print "The set-up time portion on resources of resource type Production for 
all parts is ", round(100*(ra),2)," %."
```

---

### StatProdWorkingPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a working material flow object of resource type **Production**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatProdWorkingPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
var wao: real
wp := MyDrain.StatProdWorkingPortion
print "The working time portion on resources of resource type Production 
for all parts is ", round(100*(wa),2)," %."
```

---

### StatStoreFailPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a failed material flow object of resource type **Storage**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoreFailPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDrain.StatProdFailPortion
```

---

### StatStorePausingPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a paused or unplanned material flow object of resource type **Storage**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStorePausingPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDrain.StatStorePausingPortion
```

---

### StatStoreSetUpPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a material flow object of resource type **Storage** that was setting-up for the MU type, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoreSetUpPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
var ra,wa: real
wa := MyDrain.StatStoreWaitingPortion
print "The waiting time portion on resources of resource type Storage is ", 
round(100*(wa),2)," %."
ra := MyDrain.StatProdSetUpPortion
print "The set-up time portion on resources of resource type Storage is ", 
round(100*(ra),2)," %."
```

---

### StatStoreStoppedPortion

Returns the time portion during which the MU was located on a material flow object of type **Store** that was stopped by a LockoutZone, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoreStoppedPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print Drain.StatStoreStoppedPortion
```

---

### StatStoreWaitingPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a waiting material flow object of resource type **Storage**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoreWaitingPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
var ra,wa: real
wa := MyDrain.StatStoreWaitingPortion
print "The waiting time portion on resources of resource type Storage for 
all parts is ", round(100*(wa),2)," %."
ra := MyDrain.StatProdSetUpPortion
print "The set-up time portion on resources of resource type Storage for 
all parts is ", round(100*(ra),2)," %."
```

---

### StatStoreWorkingPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a working material flow object of resource type **Storage**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoreWorkingPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDrain.StatStoreWorkingPortion
```

---

### StatThroughputPerDay

Returns the number of MUs that the Drain designated by `<Path>` removed from the plant in a day over all observed times during which the Drain was available.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatThroughputPerDay → real`
- **Return Value:** The return value has the data type `real`. This is the value of the throughput per hour multiplied with 24. The throughput is measured in liters.

**Example:**

```simtalk
print MyDrain.StatThroughputPerDay
```

---

### StatThroughputPerHour

Returns the number of MUs that the Drain designated by `<Path>` removed from the plant in an hour over all observed times during which the Drain was available.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatThroughputPerHour → real`
- **Return Value:** The return value has the data type `real`. The throughput is measured in liters.

**Example:**

```simtalk
print MyDrain.StatThroughputPerHour
```

---

### StatThroughputPerMinute

Returns the number of MUs that the Drain designated by `<Path>` removed from the plant in a minute over all observed times during which the Drain was available.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatThroughputPerMinute → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDrain.StatThroughputPerMinute
```

---

### StatTranspFailPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a failed material flow object of type **Transport** which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatTranspFailPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDrain.StatTranspFailPortion
```

---

### StatTranspPausingPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a paused or unplanned material flow object of type **Transport**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatTranspPausingPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDrain.StatTranspPausingPortion
```

---

### StatTranspSetupPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a material flow object of type **Transport** that was setting-up for the MU type, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatTranspSetUpPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
var ra,wa: real
wa := MyDrain.StatTranspWaitingPortion
print "The waiting time portion on resources of type transport for all 
parts is ", round(100*(wa),2)," %."
ra := MyDrain.StatTranspSetUpPortion
print "The set-up time portion on resources of type transport for all parts 
is ", round(100*(ra),2)," %."
```

---

### StatTranspStoppedPortion

Returns the time portion during which the MU was located on a material flow object of resource type **Transport** that was stopped by a LockoutZone, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatTranspStoppedPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print Drain.StatTranspStoppedPortion
```

---

### StatTranspWaitingPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a waiting material flow object of resource type **Transport**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatTranspWaitingPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
var ra,wa: real
wa := MyDrain.StatTranspWaitingPortion
print "The waiting time portion on resources of resource type Transport for 
all parts is ", round(100*(wa),2)," %."
ra := MyDrain.StatTranspSetUpPortion
print "The set-up time portion on resources of type transport for all parts 
is ", round(100*(ra),2)," %."
```

---

### StatTranspWorkingPortion

Returns the time portion of the sum of all life times of the MUs during which these stayed on a working material flow object of resource type **Transport**, and which the Drain designated by `<Path>` removed from the plant.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatTranspWorkingPortion → real`
- **Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDrain.StatTranspWorkingPortion
```

---

## Attributes of the Drain

The Drain additionally provides:

- The attribute `TypeStatOn` [SimTalk].
- The **Attributes of the Station**.
- The **Attributes of All Objects**.
- The **Attributes of the Material Flow Objects**.
