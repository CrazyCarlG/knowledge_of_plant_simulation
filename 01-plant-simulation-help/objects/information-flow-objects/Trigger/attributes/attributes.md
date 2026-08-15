# Trigger Attributes

This document summarizes the SimTalk attributes of the Trigger object.

## General Notes

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows or by assigning values to the respective attributes.

**To set the value of an attribute:**

```simtalk
MyTrigger.Combination := true
MyTrigger.CombinationTable.delete({0,1}..{*,*})
MyTrigger.CombinationTable.writeRow(1,1,Trig5,0,10,3600)
MyTrigger.CombinationTable.createNestedList(0,1)
MyTrigger.CombinationTable[0,1].setname("K1")
```

**To get the value of an attribute:**

```simtalk
print MyTrigger.Combination
posit := Station.Cont.XPos
```

---

## Absolute [SimTalk] - Trigger

Sets the Time Reference of the Trigger designated by `<Path>` to Absolute (`true`) or Relative (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Absolute:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**

```simtalk
MyTrigger.Absolute := true
```

**See also:** Time Reference [Trigger]

---

## Active [SimTalk] - Trigger

Activates the object designated by `<Path>` (`true`) or deactivates it (`false`).

**Remarks:** Only active Triggers trigger the attributes and methods which you entered. We recommend to not activate Triggers that only hold data.

- **Type:** Attribute
- **Syntax:** `<Path>.Active:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**

```simtalk
MyTrigger.Active := true
```

**See also:** Active [check box] - Trigger

---

## ActiveInterval [SimTalk]

Sets the time span during which the Trigger designated by `<Path>` will be active.

**Remarks:** After this time interval has elapsed, the Trigger value will take the default value. Define the default value under **Values > Values > Value Table**.

- **Type:** Attribute
- **Syntax:** `<Path>.ActiveInterval:time`
- **Assignment Value:** You can assign a value of data type time.

**Example:**

```simtalk
MyTrigger.ActiveInterval := str_to_time("1:00.00")
```

**See also:** Active Interval, Values [Trigger]

---

## Combination [SimTalk]

Sets the Trigger Type of the Trigger designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Combination:boolean`
- **Assignment Value:** You can assign a value of data type boolean. Specify `true` for Combination, `false` for Input.

**Example:**

```simtalk
MyTrigger.Combination := false
```

**See also:** Trigger Type

---

## CombinationTable [SimTalk]

Sets the Combination Table, which the Trigger designated by `<Path>` uses.

- **Type:** Attribute
- **Syntax:** `<Path>.CombinationTable:table`
- **Assignment Value:** You can assign a value of data type table.

**Example:**

```simtalk
MyTrigger.Combination := true
MyTrigger.CombinationTable.delete({0,1}..{*,*})
MyTrigger.CombinationTable.writeRow(1,1,Trig5,0,10,3600)
MyTrigger.CombinationTable.createNestedList(0,1)
MyTrigger.CombinationTable[0,1].setname("K1")
```

**See also:** Combination Table

---

## Formula [SimTalk]

Sets the Formula that the Trigger designated by `<Path>` uses to compute its value pattern.

- **Type:** Attribute
- **Syntax:** `<Path>.Formula:string`
- **Assignment Value:** You can assign a value of data type string.

**Example:**

```simtalk
MyTrigger.Formula := "K1 + K2 / K3"
```

**See also:** Formula [Trigger]

---

## Periodic [SimTalk]

Sets if the Trigger designated by `<Path>` will be executed periodically (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Periodic:boolean`
- **Assignment Value:** You can assign a value of data type boolean.

**Example:**

```simtalk
MyTrigger.Periodic := true
```

**See also:** Repeat Periodically

---

## PeriodLength [SimTalk]

Sets the Period Length of the Trigger designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.PeriodLength:time`
- **Assignment Value:** You can assign a value of data type time.

**Example:**

```simtalk
MyTrigger.PeriodLength := 3600
```

**See also:** Period Length

---

## ReferenceDate [SimTalk] - Trigger

Sets the Start Date of the Trigger designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.ReferenceDate:dateTime`
- **Assignment Value:** You can assign a value of data type dateTime.

**Example:**

```simtalk
MyTrigger.ReferenceDate := sysDate
```

**See also:** Start Date [Trigger]

---

## ReferenceTime [SimTalk] - Trigger

Sets the Start Time of the Trigger designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.ReferenceTime:time`
- **Assignment Value:** You can assign a value of data type time.

**Example:**

```simtalk
MyTrigger.ReferenceTime := str_to_time("1:00:00:00.00")
```

**See also:** Start Time [Trigger]

---

## ValueTable [SimTalk]

Sets the Values Table that the Trigger designated by `<Path>` uses to enter the value pattern over time.

- **Type:** Attribute
- **Syntax:** `<Path>.ValueTable:table`
- **Assignment Value:** You can assign a value of data type table.

**Example:**

```simtalk
MyTrigger.ValueTable.delete
MyTrigger.ValueTable.include(TS703)
```

**See also:** Values [Trigger]

---

## Generator

Use the object **Generator** for activating Method objects for the time you specify to create MUs in regular or in statistically distributed intervals.

### Description

Specify the **Start** and the **Stop** time and the time interval which you specify for the **Interval Control** to create the MUs. After the time span you specify for the **Duration**, has elapsed, Plant Simulation calls the Method object you specified as the **Duration Control** on the tab **Controls**. Interval and Duration always appear in pairs.

You can specify the times as a fixed interval or as a probability distribution. You can also limit the probability distributions to a segment of the entire range.

To show a tooltip with information about the Generator, hover with the mouse over it.

To change the length of the graphic and the anchor points of the Generator, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

### Add the Object to the Simulation Model

To add the object Generator to your simulation model, click **Manage Class Library > Basic Objects > InformationFlow > Generator** on the Home ribbon tab.

### Dialog Box of the Generator

Double-click the icon of the Generator to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under **Dialog Items of the Objects**.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

---

*Source: Plant Simulation Help 11-4367 to 11-4379. Unpublished work. © 2026 Siemens.*
