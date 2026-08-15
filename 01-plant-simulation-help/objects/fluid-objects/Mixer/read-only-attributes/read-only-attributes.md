# Read-Only Attributes of the Mixer

The Mixer provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of the Fluid Objects.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Mixer.Full
```

---

## CurrentAmount [SimTalk] - Mixer

Returns the Current Amount of the material in the mixing container of the Mixer designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.CurrentAmount → real`
- **Return Value:** The return value has the data type `real`. The current amount is measured in liters.

**Example**

```simtalk
print MyMixer.CurrentAmount
```

**See also:** Current Amount [Mixer]

---

## CurrentFillLevel [SimTalk] - Mixer

Returns the Current Fill Level of the material in the mixing container of the Mixer designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.CurrentFillLevel → real`
- **Return Value:** The return value has the data type `real`. The current amount is measured in percent.

**Example**

```simtalk
print MyMixer.CurrentFillLevel
```

**See also:** Current Fill Level [Mixer]

---

## Empty [SimTalk] - Mixer

Returns if the Mixer designated by `<Path>` is Empty (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.Empty → boolean`
- **Watchable:** The read-only attribute is watchable.
- **Return Value:** The return value has the data type `boolean`.

**Example**

```simtalk
print MyMixer.Empty
```

**See also:** Full [SimTalk] - Mixer

---

## EntranceOpen [SimTalk] - Mixer

Returns if material can enter the Mixer designated by `<Path>` because of current recovery times (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.EntranceOpen → boolean`
- **Return Value:** The return value has the data type `boolean`.

**Example**

```simtalk
print MyMixer.EntranceOpen
```

**See also:**
- Entrance Locked [material flow objects]
- TimeUntilEntranceOpen [SimTalk] - Mixer

---

## Full [SimTalk] - Mixer

Returns if the Mixer designated by `<Path>` is Full (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.Full → boolean`
- **Watchable:** The read-only attribute is watchable.
- **Return Value:** The return value has the data type `boolean`.

**Example**

```simtalk
print MyMixer.Full
```

**See also:** Empty [SimTalk] - Mixer

---

## Ready [SimTalk] - Mixer

Returns if the Mixer designated by `<Path>` is done mixing the ingredients (`true`) or not (`false`) and Ready for a new mixing process.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.Ready → boolean`
- **Watchable:** The read-only attribute is watchable.
- **Return Value:** The return value has the data type `boolean`.

**Example**

```simtalk
print MyMixer.Ready
```

---

## StatThroughput [SimTalk] - Mixer

Returns the Throughput, i.e., the amount of the product that the Mixer designated by `<Path>` mixed using the ingredients.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatThroughput → real`
- **Return Value:** The return value has the data type `real`. The throughput is measured in liters.

**Example**

```simtalk
print MyMixer.StatThroughput
```

**See also:** Tab Statistics [FluidDrain]

---

## TimeUntilEntranceOpen [SimTalk] - Mixer

Returns the time until the entrance of the Mixer designated by `<Path>` opens again after the recovery time has elapsed.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.TimeUntilEntranceOpen → real`
- **Return Value:** The return value has the data type `real`.

**Example**

```simtalk
print MyMixer.TimeUntilEntranceOpen
```

**See also:** EntranceOpen [SimTalk] - Mixer
