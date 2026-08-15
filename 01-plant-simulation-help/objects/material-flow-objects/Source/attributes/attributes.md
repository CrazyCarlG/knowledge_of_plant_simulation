# Attributes of the Source

The Source provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
MySource.GenerateAsBatch := true
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print MySource.GenerateAsBatch
posit := MyStation.Cont.XPos
```

---

## CurrentBatchNumber

Returns the batch number of the part that was created last if the attribute `GenerateAsBatch` is activated (true). Returns the number of created parts if `GenerateAsBatch` is not activated (false).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.CurrentBatchNumber -> integer`
- **Return Value:** The return value has the data type `integer`.

**Example**

```simtalk
print MySource.CurrentBatchNumber
```

**See also:** Generate as Batch (check box), GenerateAsBatch (SimTalk)

---

## Blocking

Sets if the Source designated by `<Path>` saves the time at which it was supposed to produce the next MU (true) or not (false).

**Remarks**

- When you set `Blocking` to `true`, the Source produces the following MUs at the next possible point in time, i.e., when the Source moved the MU that was blocked by the successor, on (true).
- When you set `Blocking` to `false`, the Source creates another MU only at the Time of Creation which you entered.

- **Type:** Attribute
- **Syntax:** `<Path>.Blocking:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example**

```simtalk
MySource.Blocking := true
```

**See also:** Operating Mode (check box), Time of Creation (Source)

---

## CreationTableActive

Sets if the Source designated by `<Path>` writes all events, for which it produced MUs during a simulation run, into a table (true) or not (false).

**Remarks**

The Source records the creation events in addition to the resource statistics it collects in any case.

- **Type:** Attribute
- **Syntax:** `<Path>.CreationTableActive:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example**

```simtalk
MySource.CreationTableActive := true
```

**See also:** Creation Table (Source), creationTable (SimTalk) - Source

---

## GenerateAsBatch

Makes the Source designated by `<Path>` produce MUs in a single batch all at once (true) or individually one by one (false).

**Remarks**

If you activate Generate as Batch, the Source produces the entire set of parts all at once at the given start time and attempts to move all of the parts on to the next object in a single lot.

> **Note:** This setting applies for the MU Selection > Sequence Cyclical, Sequence, Random, and Percentage.

> **Note:** If you set MU Selection to Number Adjustable and if you activate the check box Generate as Batch, the Amount does not designate the number of parts, but the number of batches that the Source produces.

- **Type:** Attribute
- **Syntax:** `<Path>.GenerateAsBatch:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example**

```simtalk
MySource.GenerateAsBatch := true
```

**See also:** Generate as Batch (check box), CurrentBatchNumber (SimTalk)

---

## Interval

Sets the interval between the times at which the Source designated by `<Path>` produces MUs.

**Remarks**

The behavior of the attribute `Interval` depends on the setting `TimeOfGeneration`:

- **For Time of Creation > Interval Adjustable:**
  - The attribute `Interval` sets the time that elapses between the creation events of the Source designated by `<Path>`. Specify a distribution and enter the values, which that distribution requires. You can also specify `Const` and enter a constant time.
  - The attribute `Start` sets the simulation time at which the Source starts producing MUs.
  - The attribute `Stop` sets the simulation time at which the Source stops producing MUs. A Stop time of 0 (zero) indicates that the Source will keep producing MUs infinitely.
- **For Time of Creation > Number Adjustable:**
  - You can specify one of the Probability Distributions and specify the values that the selected distribution requires. The distribution determines the point in time at which the Source creates the MUs.
  - The Source produces the number of MUs at the different times which the random number generator generated at the beginning of the simulation. The determined times are contained within the bounds if you enter a lower bound and an upper bound.
  - Specify a Constant time to make the Source create the number of MUs all at one point in time.

- **Type:** Attribute
- **Syntax:**

```simtalk
<Path>.Start:time
<Path>.Stop:time
<Path>.Interval:time
```

- **Assignment Value:** You can assign a value of data type `time`.

**Example**

```simtalk
MySource.TimeOfCreation := "Interval adjustable"
MySource.Start := 3600
MySource.Stop := str_to_time("1:00:00:00.00")
MySource.Interval.setTypeAndAttr("Normal",1,500,100,200,900)
```

**See also:** TimeOfGeneration (SimTalk), Start (Source), Interval (Source), Stop, Interval Adjustable (time of creation), Probability Distributions

---

## MUSelection

Sets how the Source designated by `<Path>` selects the MUs to be produced.

**Remarks**

Depending on the setting that you enter, the attribute `Path` either sets the path to the delivery list, the sequence table, the frequency table, or the MU class.

To use a copy of the DataTable instead of a reference to the DataTable, assign the name `.unshare` to the subtable.

- **Type:** Attribute
- **Syntax:** `<Path>.MUSelection:string`
- **Assignment Value:** You can assign a value of data type `string`. You can specify `"Constant"`, `"Sequence Cyclical"`, `"Sequence"`, `"Random"`, `"Percentage"`, or `"Order Controlled"`.

**Example**

```simtalk
MySource.MUSelection := "Sequence"
```

**See also:** Store as Supermarket (check box), Configuration (button), MU selection (drop-down list), Path (SimTalk) - Source

---

## Number

Sets the number of MUs which the Source designated by `<Path>` produces.

**Remarks**

This setting only applies for the Time of Creation > Number Adjustable and Interval Adjustable.

- If you do not enter a Stop time for the setting Interval Adjustable, Plant Simulation produces the amount of parts you entered at the most. The default value of `-1` designates an unlimited number of parts to be produced. Otherwise the Source produces parts until the Stop time is reached and ignores the Amount of parts you entered.
- For the setting Interval Adjustable the Source might possibly create more parts than the Amount you entered, if the check box Generate as Batch is activated. This is because the batches are always produced in their entirety, not in part only.
- For the setting Time of creation > Number Adjustable the value does not designate the amount of MUs but the amount of batches/lots which the Source produces when you activated Generate as Batch.

- **Type:** Attribute
- **Syntax:** `<Path>.Number:integer`
- **Assignment Value:** You can assign a value of data type `integer`.

**Example**

```simtalk
MySource.Number := 5
```

**See also:** MU selection (drop-down list), Number Adjustable (time of creation), Stop (Source), Generate as Batch (check box)

---

## Path

Sets the path to the delivery list, the sequence table, the frequency table, or the MU class of the Source designated by `<Path>`.

**Remarks**

What the path relates to depends on the settings for `TimeOfGeneration` and `MUSelection`.

> **Note:** The Source does not produce parts whose time of creation is in the future when you assign a Delivery Table during the simulation.

- **Type:** Attribute
- **Syntax:** `<Path>.Path:string`
- **Assignment Value:** You can assign a value of data type `string` or `object`.

**Example**

```simtalk
MySource.Path := "MyDeliveryTable"
```

**See also:** Time of Creation (Source)/TimeOfGeneration (SimTalk), MU selection (drop-down list)/MUSelection (SimTalk), Delivery Table (time of creation)

---

## Start

Sets the simulation time at which the Source designated by `<Path>` starts producing MUs.

**Remarks**

`Start` applies when you set the `TimeOfGeneration` to Interval Adjustable.

- The attribute `Interval` sets the time span between two events at which the Source produces MUs.
- The attribute `Stop` sets the simulation time at which the Source stops producing MUs. A Stop time of zero indicates that the Source will keep producing MUs infinitely.

- **Type:** Attribute
- **Syntax:**

```simtalk
<Path>.Start:time
<Path>.Stop:time
<Path>.Interval:time
```

- **Assignment Value:** You can assign a value of data type `time`.

**Example**

```simtalk
MySource.TimeOfGeneration := "Interval adjustable"
MySource.Start := 3600
MySource.Stop := str_to_time("1:00:00:00.00")
MySource.Interval.setTypeAndAttr("Normal",500,100,200,900)
```

**See also:** TimeOfGeneration (SimTalk), Stop (SimTalk) - Source, Interval (SimTalk) - Source, Start (Source), Interval (Source), Stop (Source), Interval Adjustable (time of creation)

---

## Stop

Sets the simulation time at which the Source designated by `<Path>` stops producing MUs.

**Remarks**

- A Stop time of zero indicates that the Source will keep producing MUs infinitely.
- The attribute `Start` sets the simulation time at which the Source starts producing MUs, when you set the `TimeOfGeneration` to Interval Adjustable.
- The attribute `Interval` sets the time span between two events at which the Source produces MUs.

- **Type:** Attribute
- **Syntax:**

```simtalk
<Path>.Start:time
<Path>.Stop:time
<Path>.Interval:time
```

- **Assignment Value:** You can assign a value of data type `time`.

**Example**

```simtalk
MySource.TimeOfGeneration := "Interval adjustable"
MySource.Start := 3600
MySource.Stop := str_to_time("1:00:00:00.00")
MySource.Interval.setTypeAndAttr("Normal",500,100,200,900)
```

**See also:** Start (SimTalk) - Source, Interval (SimTalk) - Source, TimeOfGeneration (SimTalk), Start (Source), Interval (Source), Stop (Source)

---

## TimeOfGeneration

Sets how the Source designated by `<Path>` produces new MUs.

**Remarks**

Depending on the setting that you enter, the attribute `Path` either sets the path to the delivery list, the sequence table, the frequency table, or the MU class.

> **Note:** The Source does not produce parts whose time of creation is in the future when you assign a Delivery Table during the simulation.

> **Note:** Plant Simulation processes the Delivery Table row by row. For this reason the time should increase from row to row. If Plant Simulation processes a row in which the time is located in the past, the part will be created immediately, which is not what you would expect.

- **Type:** Attribute
- **Syntax:** `<Path>.TimeOfGeneration:string`
- **Assignment Value:** You can assign a value of data type `string`. You can specify `"Interval Adjustable"`, `"Number Adjustable"`, `"Delivery Table"`, or `"Trigger"`.

**Examples**

```simtalk
MySource.TimeOfGeneration := "number adjustable"
MySource.TimeOfGeneration := "delivery table"
MySource.path := MyDeliveryTable
```

**See also:** Path (SimTalk) - Source, Time of Creation (Source)

---

## Trigger

Sets the internal Trigger list of the Source designated by `<Path>` or returns it.

- **Type:** Attribute
- **Syntax:** `<Path>.Trigger:array`
- **Assignment Value:** You can assign a value of data type `array`.

**Examples**

```simtalk
var assignedTriggers: object[2]
for var j := 1 to 2 
   assignedTriggers[j] := to_str("Trigger",j) 
next
   Source.Trigger := assignedTriggers 
// sets the trigger list
print MySource.Trigger // gets the trigger list 
// [*.Models.Model.Trigger, *.Models.Model.Trigger2]
```

**See also:** Trigger (time of creation), Drain (object)
