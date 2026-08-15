# Read-Only Attributes of the ShiftCalendar

The ShiftCalendar provides:

- The read-only attributes listed below.
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyShiftCalendar.Unplanned
```

## GetCurrShift [SimTalk]

Returns the name of the shift of the ShiftCalendar designated by `<Path>` that is currently active.

**Remarks:** This is the name you typed into the column Shift on the tab Shift Times.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.GetCurrShift → string
```

**Watchable:** The read-only attribute is watchable.

**Return Value:** The return value has the data type string.

**Example:**

```simtalk
shift := root.MyShiftCalendar.GetCurrShift
```

**See also:** Tab Shift Times, Shift [ShiftCalendar], GetCurrShift [SimTalk]

## Pause [SimTalk] - ShiftCalendar

Returns if the ShiftCalendar designated by `<Path>` is paused (`true`) or not (`false`).

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.Pause → boolean
```

**Watchable:** The read-only attribute is watchable.

**Return Value:** The return value has the data type boolean.

**Example:**

```simtalk
print MyShiftCalendar.Pause
```

**See also:** Paused [state, material flow objects], Pause [SimTalk] - ShiftCalendar

## Unplanned [SimTalk] - ShiftCalendar

Returns if the ShiftCalendar designated by `<Path>` is unplanned (`true`) or not (`false`).

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.Unplanned → boolean
```

**Watchable:** The read-only attribute is watchable.

**Return Value:** The return value has the data type boolean.

**Example:**

```simtalk
print MyShiftCalendar.Unplanned
```

**See also:** Unplanned [state, material flow objects], Attributes of the ShiftCalendar
