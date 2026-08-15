# Display Attributes

Summary of the SimTalk attributes of the **Display** object, which visualizes a value designated by a path in a Frame.

## Overview

The Display provides:
- The attributes listed in this document.
- The Attributes of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show the selected Instance.

You can set and get attribute values either with the dialog windows or by assigning values to the respective attributes:

```simtalk
-- Set values
Display1.Sampler := false
Display1.Path := "MyConveyor.NumMU"
Display2.Sampler := true
Display2.SmpInterval := 300
Display2.Path := "root.MyConveyor.utilization"

-- Get values
print Display1.Path
posit := Station.Cont.XPos
```

---

## GetStandardDeviation [SimTalk]

Returns the standard deviation of the values that the Display designated by `<Path>` recorded.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.GetStandardDeviation → real`
- **Return Value:** data type `real`

```simtalk
print MyDisplay.GetStandardDeviation
```

---

## Active [SimTalk]

Activates the object designated by `<Path>` (`true`) or deactivates it (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Active:boolean`
- **Assignment Value:** data type `boolean`

```simtalk
MyDisplay.active := true
```

---

## Color [SimTalk]

Sets the color for displaying the values which the Display designated by `<Path>` visualizes in the Frame.

- **Remarks:** Set the RGB values of the color with the method `makeRGBValue`.
- **Type:** Attribute
- **Syntax:** `<Path>.Color:integer`
- **Assignment Value:** data type `integer`

```simtalk
MyDisplay.Color := makeRGBValue(255,0,0)
```

---

## Comment [SimTalk]

Sets the comment that the Display designated by `<Path>` shows underneath its icon in the Frame.

- **Type:** Attribute
- **Syntax:** `<Path>.Comment:string`
- **Assignment Value:** data type `string`

```simtalk
MyDisplay.Comment := "My comment"
```

---

## DecimalPlaces [SimTalk]

Sets the number of decimal places which the Display designated by `<Path>` shows.

- **Remarks:** The Display can show up to 15 decimal places. The default `-1` shows all existing places; type a positive value to show this number of places.
- **Note:** This setting only applies to the Type > Text.
- **Type:** Attribute
- **Syntax:** `<Path>.DecimalPlaces:integer`
- **Assignment Value:** data type `integer`

```simtalk
MyDisplay.DecimalPlaces := 10
```

---

## DisplayType [SimTalk]

Sets if the Display designated by `<Path>` shows the input value as Text, as a Bar, or as a Pie Segment.

- **Remarks:** Bar and Pie representation map values in a specified range to bars of varying height or pies with a varying degree of completion. Set the range with the attributes `MinVal` and `MaxVal`.
- **Type:** Attribute
- **Syntax:** `<Path>.DisplayType:string`
- **Assignment Value:** data type `string` — you can specify `"Text"`, `"Bar"`, or `"Pie"`.

```simtalk
MyDisplay.DisplayMode := "Text"
```

---

## Font [SimTalk]

Sets the font size of the text and of the comment, which the Display designated by `<Path>` displays in Text mode in the Frame.

- **Type:** Attribute
- **Syntax:** `<Path>.Font:integer`
- **Assignment Value:** data type `integer` — you can specify `1` for Small, `2` for Medium, `3` for Large, `4` for Extra Large.

```simtalk
MyDisplay.Font := 2
```

---

## MaxVal [SimTalk]

Sets the upper bound of the displayed range in Bar and Pie modes of the Display designated by `<Path>`.

- **Remarks:** The Display shows values beyond or equal to `MaxVal` as a full bar/pie.
- **Type:** Attribute
- **Syntax:** `<Path>.MaxVal:real`
- **Assignment Value:** data type `real`

```simtalk
MyDisplay.MinVal := 10.0
MyDisplay.MaxVal := 35.713
```

---

## MinVal [SimTalk]

Sets the lower bound of the displayed range in Bar and Pie modes.

- **Remarks:** The Display designated by `<Path>` shows values below or equal to `MinVal` as an empty bar/pie.
- **Type:** Attribute
- **Syntax:** `<Path>.MinVal:real`
- **Assignment Value:** data type `real`

```simtalk
MyDisplay.MinVal := 5.35
```

---

## Path [SimTalk]

Sets the path to the value which the Display designated by `<Path>` shows.

- **Type:** Attribute
- **Syntax:** `<Path>.Path:string`
- **Assignment Value:** data type `string`

```simtalk
Display1.Sampler := false
Display1.Path := "MyConveyor.NumMU"
Display2.Sampler := true
Display2.SmpInterval := 300
Display2.Path := "root.MyConveyor.utilization"
```

---

## Sampler [SimTalk]

Activates Sample mode of the Display designated by `<Path>` (`true`) or deactivates it (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Sampler:boolean`
- **Assignment Value:** data type `boolean`
  - `true` designates **Sample mode** — updates the display periodically, independent of changes of the input value.
  - `false` designates **Watch mode** — updates its display whenever the input value changes.

```simtalk
if MeinDisplay.Sampler = false
   MyDisplay.Sampler := true // activates sample mode
   MyDisplay.SmpInterval := 360 // 10 minutes
end
```

---

## SmpPeriod [SimTalk]

Sets the intervals after which the Display designated by `<Path>` updates the display. Its value must be greater than zero.

- **Remarks:** `SmpPeriod` applies to Sample mode.
- **Type:** Attribute
- **Syntax:** `<Path>.SmpPeriod:time`
- **Assignment Value:** data type `time`

```simtalk
MyDisplay.SmpPeriod := str_to_time("3:00.0")
MyDisplay.SmpPeriod := 2 * MyDisplay.SmpPeriod
-- double interval, half the sampling rate
```

---

## Transparent [SimTalk]

Makes the background of the object designated by `<Path>` transparent in the Frame (`true`) or not transparent (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Transparent:boolean`
- **Assignment Value:** data type `boolean`
  - Specify `true` to show the space around the text in the color of the background image of the Frame.
  - Specify `false` to show the space around the text in white.

```simtalk
MyDisplay.Transparent := false
```

---

## Value [SimTalk]

Sets or gets the value which the Display designated by `<Path>` shows.

- **Remarks:**
  - Only use the attribute `Value` for **Watch Mode**.
  - In **Sample Mode**, Plant Simulation only updates the value if **MUs and States** is activated and the Frame in which the Display is inserted is open.
  - When you get the value and the Display is in Sample Mode, Plant Simulation updates the value beforehand.
- **Type:** Attribute
- **Syntax:** `<Path>.Value:real`
- **Assignment Value:** data type `real`
- **Return Value:** data type of the observed value

```simtalk
MyDisplay.Value := 5
print MyDisplay.Value
```

---

## Chart

The **Chart** object presents current data and results of the simulation run.

Define data to be plotted:
- By using a Table containing the data, such as simulation results.
- By defining Input Channels that record values of attributes of interest of the objects.

A Chart inserted into a Frame provides the **Statistics Wizard**. Select the command **Statistics Wizard** on the context menu of the Frame to open it.
