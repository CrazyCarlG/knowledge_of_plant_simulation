# Attributes of the ShiftCalendar

The ShiftCalendar provides:

- The attributes listed in the table of contents to the left.
- The [Attributes of All Objects](https://example.invalid).

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute:
  ```simtalk
  MyShiftCalendar.ShiftPlan := shiftTimesTable
  ```
- To get the value of an attribute:
  ```simtalk
  print MyShiftCalendar.ShiftPlan
  posit := Station.Cont.XPos
  ```

---

## Unplanned [SimTalk] - ShiftCalendar

Returns, if the ShiftCalendar designated by `<Path>` is unplanned (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.Unplanned → boolean`
- **Watchable:** The read-only attribute is watchable.
- **Return Value:** The return value has the data type `boolean`.

**Example**

```simtalk
print MyShiftCalendar.Unplanned
```

**See also:** Unplanned [state, material flow objects]

---

## Active [SimTalk] - ShiftCalendar

Activates the ShiftCalendar designated by `<Path>` (`true`), i.e., if your plant works in shifts, or deactivates it (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Active:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example**

```simtalk
MyShiftCalendar.Active := true
```

**See also:** Active [check box] - ShiftCalendar

---

## Calendar [SimTalk]

Sets the calendar of the ShiftCalendar designated by `<Path>`.

**Remarks**

Plant Simulation copies the contents of the DataTable, which you specify, to the internal calendar table on the tab **Calendar**. For clarity reasons we recommend to use column and row headers.

- Select the data type `date` for the first column (Date From) of the table and enter the date the shift starts.
- Select the data type `date` for the second column (Date To) and enter the date the shift ends.
- Select the data type `string` for the third column (Reduce Time To) and enter the hours during which the shift in your plant is active.
- Select the data type `string` for the fourth column (Comment) and enter why the shift does not apply.

Assigning the table overwrites the contents of any existing calendar.

- **Type:** Attribute
- **Syntax:** `<Path>.Calendar:any`
- **Assignment Value:** You can assign a value of data type `any`.

**Example**

```simtalk
MyShiftCalendar.Calendar := shiftCalendarTable
```

**See also:** Tab Calendar

---

## Resources [SimTalk] - ShiftCalendar

Sets the resource objects that the ShiftCalendar designated by `<Path>` controls.

**Remarks**

Plant Simulation copies the contents of the DataTable, which you specify, to the internal Resources (Objects table on the tab **Resources**).

Select the data type `object` for the first column of the data table and enter all objects to be controlled by the shift calendar.

Assigning the table overwrites the contents of any existing resource table. For clarity reasons we recommend to use column and row headers. You can also use the rest of the table for any other purpose.

- **Type:** Attribute
- **Syntax:** `<Path>.Resources:any`
- **Assignment Value:** You can assign a value of data type `any`.

**Example**

```simtalk
shifts.Resources := ResourcesTable
```

**See also:** Tab Resources [ShiftCalendar]

---

## ShiftPlan [SimTalk]

Sets the shift calendar of the ShiftCalendar designated by `<Path>`.

**Remarks**

Plant Simulation copies the contents of the DataTable, which you specify, to the internal shift times table on the tab **Shift Times**. For clarity reasons we recommend to use column and row headers.

- Select the data type `string` for the first column (Shift) of the data table and enter the name of the shift.
- Select the data type `time` for the second column (From) and enter the time the shift starts.
- Select the data type `time` for the third column (To) and enter the time the shift ends.
- Select the data type `boolean` for the fourth to the tenth column (Mo through Sun). Enter `true`, when the shift applies to this day. Enter `false`, when the shift does not apply to this day.
- Select the data type `string` for the eleventh column (Pauses) and enter the times of the pauses.

> **Note:** You cannot specify overlapping shifts.

Assigning the table overwrites the contents of any existing shift times.

When you get the shift plan, column 12 of the returned table contains a subtable with the start and end times of the pauses. Column 13 contains an error code. If a value is non-zero, the values in the shift plan are not consistent.

> **Note:** The attribute ShiftPlan returns a temporary table. The ShiftCalendar cannot detect that the temporary table was modified.
> The correct way is to assign the returned table to a variable, modify the temporary table and assign it back to the attribute ShiftPlan.

- **Type:** Attribute
- **Syntax:** `<Path>.ShiftPlan:table`
- **Assignment Value:** You can assign a value of data type `table`.

**Example**

```simtalk
MyShiftCalendar.ShiftPlan := shiftTimesTable
// This code modifies the shift table
var t:table := ShiftCalendar.ShiftPlan
t["From", 1] := 3:00:00
ShiftCalendar.ShiftPlan := t
```

**See also:** Tab Shift Times
