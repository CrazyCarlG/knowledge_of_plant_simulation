# Trigger Attributes

This README summarizes the SimTalk attributes of the **Trigger** object, based on the file `attributes.md` in this directory.

## Overview

The Trigger object is part of the information-flow objects in Plant Simulation. Its attributes can be set and read either through the dialog windows (check boxes, text boxes, drop-down lists) or by assigning/reading values in SimTalk.

To display the available attributes:

- Select **Show Attributes and Methods** on the Class Library context menu to show them for a Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of a Frame to show them for an Instance.

## Attribute Summary

| Attribute | Type | Data Type | Purpose |
|-----------|------|-----------|---------|
| `Absolute` | Attribute | `boolean` | Sets the Time Reference of the Trigger to Absolute (`true`) or Relative (`false`). |
| `Active` | Attribute | `boolean` | Activates (`true`) or deactivates (`false`) the Trigger. Only active Triggers fire the configured attributes and methods. |
| `ActiveInterval` | Attribute | `time` | Sets the time span during which the Trigger is active; afterwards it returns to its default value. |
| `Combination` | Attribute | `boolean` | Sets the Trigger Type: `true` for Combination, `false` for Input. |
| `CombinationTable` | Attribute | `table` | Sets the Combination Table used by the Trigger. |
| `Formula` | Attribute | `string` | Sets the Formula the Trigger uses to compute its value pattern. |
| `Periodic` | Attribute | `boolean` | Sets whether the Trigger executes periodically (`true`) or not (`false`). |
| `PeriodLength` | Attribute | `time` | Sets the Period Length of the Trigger. |
| `ReferenceDate` | Attribute | `dateTime` | Sets the Start Date of the Trigger. |
| `ReferenceTime` | Attribute | `time` | Sets the Start Time of the Trigger. |
| `ValueTable` | Attribute | `table` | Sets the Values Table used to define the value pattern over time. |

## General Usage

**To set an attribute value:**

```simtalk
MyTrigger.Combination := true
MyTrigger.CombinationTable.delete({0,1}..{*,*})
MyTrigger.CombinationTable.writeRow(1,1,Trig5,0,10,3600)
MyTrigger.CombinationTable.createNestedList(0,1)
MyTrigger.CombinationTable[0,1].setname("K1")
```

**To get an attribute value:**

```simtalk
print MyTrigger.Combination
posit := Station.Cont.XPos
```

## Related References

Several attributes cross-reference other Trigger-related topics, including:

- Time Reference, Active (check box), Values, Trigger Type, Combination Table, Formula, Repeat Periodically, Period Length, Start Date, and Start Time.

## Note on "Generator"

The source file also contains a section describing the **Generator** object (used to activate Method objects at specified times to create MUs in regular or statistically distributed intervals). This section is unrelated to the Trigger attributes and appears to be included from adjacent help-page content.
