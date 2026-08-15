# Attributes of the Drain

The Drain provides:

- The attribute `TypeStatOn` [SimTalk].
- The Attributes of the Station.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

---

## StatTranspWorkingPortion [SimTalk] - Drain

Returns the time portion of the sum of all life times of the MUs during which these stayed on a working material flow object of resource type *Transport*, and which the Drain designated by `<Path>` removed from the plant.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatTranspWorkingPortion -> real
```

**Return Value**

The return value has the data type `real`.

**Example**

```simtalk
print MyDrain.StatTranspWorkingPortion
```

**See also**

- Resource Type of the material flow objects
- Detailed Statistics Table [FluidDrain] of the Drain
- Statistics report, Cumulated Statistics of the Parts which the Drain Removed From the Plant

---

## TypeStatOn [SimTalk]

Activates collecting statistics values of the Drain designated by `<Path>` depending on the type of MU (`true`) or deactivates it (`false`).

**Type**

Attribute

**Syntax**

```
<Path>.TypeStatOn:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

**Example**

```simtalk
MyDrain.TypeStatOn := false
```

**See also**

- Type Dependent Statistics
- typeStatistics [SimTalk] - Drain
- typeStatisticsCumulated [SimTalk]

---

## Getting and Setting Attribute Values

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
MyDrain.Pause := true
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print MyDrain.Pause
posit := MyStation.Cont.XPos
```

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].
