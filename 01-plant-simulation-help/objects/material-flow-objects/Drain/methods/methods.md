# Methods of the Drain

## Overview

The Drain provides:

- The methods listed in the table of contents to the left.
- The Methods of the Station.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods** (the figure in the original documentation illustrates this using the example of the object Station).

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Understanding the Syntax Line

An example of the syntax line of an individual method might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. For example, `(Parameter:string)` designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. For example, `[,Parameter:boolean]` means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, for example `:= false`.
- If the method has a return value, the signature shows its data type after the arrow `->`, for example `→ boolean`.

---

## typeStatistics [SimTalk]

Returns the Detailed Statistics Table of the Drain designated by `<Path>` and writes it into a table.

**Remarks**

The column **Read-only Attribute** lists the read-only attributes of the corresponding statistics values for all part types.

**Type:** Method

**Syntax**

```
<Path>.typeStatistics([TypeStatisticsTable:table]) → boolean
```

**Parameter**

The optional parameter `TypeStatisticsTable` of data type `table` designates the name of the table.

**Return Value**

The return value has the data type `boolean`.

- `true` if statistics collection is activated.
- `false` if statistics collection is deactivated. Then the table remains unaltered.
- Is the table containing the statistics data if statistics collection is activated, if you do not specify the optional parameter.
- `void` if statistics collection is deactivated.

**Examples**

```
MyDrain.typeStatistics(MyDrainStatisticsTable)
// Writes the statistics values to the table named MyDrainStatisticsTable.
// The return value is true if statistics collection is activated.
// It is false if it is deactivated. Then the table remains unaltered.
```

```
MyDrain.typeStatistics
// Writes the statistics values to a table.
// The return value is the statistics table if statistics collection is
// activated.
// It is void if statistics collection is cleared.
```

**See also**

- `typeStatisticsCumulated [SimTalk]`
- `TypeStatOn [SimTalk]`
- Detailed Statistics Table [Drain]
- Statistics report, Part Types Which the Drain Removed From the Plant

---

## typeStatisticsCumulated [SimTalk]

Returns the cumulated statistics table containing the MU Types which the object designated by `<Path>` removed from the plant.

**Type:** Method

**Syntax**

```
<Path>.typeStatisticsCumulated([CumulatedTypeStatisticsTable:table]) → boolean
```

**Parameter**

The optional parameter `CumulatedTypeStatisticsTable` of data type `table` designates the name of the table.

The columns are the same as those in the table which the method `typeStatistics` fills. The column **Type** remains empty though.

**Return Value**

The return value has the data type `boolean`.

- `true` if statistics collection is activated.
- `false` if statistics collection is deactivated. Then the table remains unaltered.
- Is the table containing the statistics data if statistics collection is activated, if you do not specify the optional parameter.
- `void` if statistics collection is deactivated.

**Examples**

```
MyDrain.typeStatisticsCumulated(myCumulatedDrainStatistics)
// Writes the statistics values to the table named MyDrainStatisticsTable.
// The return value is true if statistics collection is activated.
// It is false if it is deactivated. Then the table remains unaltered.
```

```
MyDrain.typeStatisticsCumulated
// Writes the statistics values to a table.
// The return value is the statistics table if statistics collection is
// activated.
// It is void if statistics collection is deactivated.
```

**See also**

- `typeStatistics [SimTalk] - Drain`
- `TypeStatOn [SimTalk]`

---

## Read-Only Attributes of the Drain

The Drain provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```
print Drain.StatAvgExitInterval
```
