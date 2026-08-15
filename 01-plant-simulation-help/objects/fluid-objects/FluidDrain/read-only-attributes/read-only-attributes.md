# Read-Only Attributes of the FluidDrain

The FluidDrain provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of the Fluid Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```
print FluidDrain.StatMaxFlowRate
```

---

## typeStatistics [SimTalk] - FluidDrain

Returns the Detailed Statistics Table of the FluidDrain designated by `<Path>` and writes it into a table.

**Type:** Method

**Syntax:**

```
<Path>.typeStatistics(TypeStatisticsTable:table)
```

**Parameter**

The parameter `TypeStatisticsTable` of data type `table` designates the name of the table.

**Remarks**

The table shows these values:

| Name | Description |
| --- | --- |
| Material | Shows the name of the material that the FluidDrain drained from the plant. |
| Throughput | Shows the total amount of the material that the FluidDrain drained from the plant. |

**Examples**

```
var MyFluidDrainStatisticsTable: table
MyFluidDrain.typeStatistics(MyFluidDrainStatisticsTable)
```

**See also:** Detailed Statistics Table [FluidDrain]

---

## StatMaxFlowRate [SimTalk]

Returns the maximum flow rate of the FluidDrain designated by `<Path>`.

**Type:** Read-only attribute

**Syntax:**

```
<Path>.StatMaxFlowRate → real
```

**Return Value**

The return value has the data type `real`.

Is the amount of liters of material that flowed into the FluidDrain per second.

**Example**

```
print MyFluidDrain.StatMaxFlowRate
```

**See also:** Tab Statistics [FluidDrain]

---

## StatThroughput [SimTalk] - FluidDrain

Returns the amount of material that the FluidDrain designated by `<Path>` drained from the plant.

**Type:** Read-only attribute

**Syntax:**

```
<Path>.StatThroughput → real
```

**Return Value**

The return value has the data type `real`.

The throughput is measured in liters.

**Example**

```
print MyFluidDrain.StatThroughput
```

**See also:** Tab Statistics [FluidDrain]

---

## StatThroughputPerDay [SimTalk] - FluidDrain

Returns the amount of material that the FluidDrain designated by `<Path>` drained from the plant during a day while the FluidDrain was available.

**Type:** Read-only attribute

**Syntax:**

```
<Path>.StatThroughputPerDay → real
```

**Return Value**

The return value has the data type `real`.

This is the value of the throughput per hour multiplied with 24.

The throughput is measured in liters.

**Example**

```
print MyFluidDrain.StatThroughputPerDay
```

**See also:** Tab Statistics [FluidDrain]

---

## StatThroughputPerHour [SimTalk] - FluidDrain

Returns the amount of material that the FluidDrain designated by `<Path>` drained from the plant in an hour while the FluidDrain was available.

**Type:** Read-only attribute

**Syntax:**

```
<Path>.StatThroughputPerHour → real
```

**Return Value**

The return value has the data type `real`.

The throughput is measured in liters.

**Example**

```
print MyFluidDrain.StatThroughputPerHour
```

**See also:** Tab Statistics [FluidDrain]
