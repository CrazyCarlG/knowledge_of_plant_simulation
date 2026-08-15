# Attributes of the Variable

This document summarizes the SimTalk attributes of the Variable object. Each attribute is accessed via the reference operator `&`; without the operator, the attribute applies to the *contents* of the Variable rather than the object itself.

```simtalk
&Variable.Name := "MyVariable"
```

## Accessing Attributes

- **Class**: Select *Show Attributes and Methods* on the context menu of the Class Library.
- **Instance**: Press **F8**, or click *Show Attributes and Methods* on the Home ribbon tab of the Frame.

> **Note:** You can only access attributes of the object `Variable` (referring to the object itself) via the reference operator `&`. Without the operator, the attribute is applied to the contents of the Variable.

---

## Alignment [SimTalk] - Variable

Sets the alignment of the Variable designated by `&` with its insertion point.

- **Type:** Attribute
- **Syntax:** `<&>Variable.Alignment:string`
- **Value:** string — `"Left"`, `"Name"`, `"Value"`, or `"Right"`

```simtalk
&MyVariable.Alignment := "Right"
```

---

## BackgroundColor [SimTalk] - Variable

Sets the background color of the Variable in the Frame.

- **Type:** Attribute
- **Syntax:** `<&>Variable.BackgroundColor:integer`
- **Value:** integer — set RGB values with `makeRGBValue`.

```simtalk
&MyVariable.BackgroundColor := makeRGBValue(100,100,100)
&MyVariable.BackgroundColor := 6579300 // is the same as the color above
```

---

## Color [SimTalk] - Variable

Sets the font color used to display the Variable in the Frame.

- **Type:** Attribute
- **Syntax:** `<&>Variable.Color:integer`
- **Value:** integer — set RGB values with `makeRGBValue`.

```simtalk
&MyVariable.Color := makeRGBValue(110,0,200)
```

---

## Comment [SimTalk] - Variable

Sets the comment of the Variable designated by `&`.

- **Type:** Attribute
- **Syntax:** `<&>Variable.Comment:string`
- **Value:** string

```simtalk
&MyVariable.Comment := "My comment, my comment"
```

---

## DataType [SimTalk] - Variable

Sets the data type of the Variable designated by `&`.

- **Type:** Attribute
- **Syntax:** `<&>Variable.DataType:string`
- **Value:** string

```simtalk
&MyVariable.DataType := "string"
```

---

## DecimalPlaces [SimTalk] - Variable

Sets the number of decimal places the Variable shows in the Frame.

- **Type:** Attribute
- **Syntax:** `<&>Variable.DecimalPlaces:integer`
- **Value:** integer

**Remarks:**
- The Variable can show up to 15 decimal places. Default `-1` shows all existing places. A positive value shows that number of decimal places.
- Applies only to data types `real`, `length`, `money`, `weight`, `time`, `speed`, and `acceleration`.
- For data type `time`, the value `-1` means the default time display format with four decimal places; a positive value shows at most that many decimal places.

```simtalk
&MyVariable.DecimalPlaces := 12
```

---

## Font [SimTalk] - Variable

Sets the font size used to display the Variable in the Frame.

- **Type:** Attribute
- **Syntax:** `<&>Variable.Font:integer`
- **Value:** integer — `1` = Small, `2` = Medium, `3` = Large, `4` = Extra Large

```simtalk
&MyVariable.Font := 2
```

---

## HasInitValue [SimTalk] - Variable

Sets whether the Variable has an initial value (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<&>Variable.HasInitValue:boolean`
- **Value:** boolean

```simtalk
&MyVariable.DataType := "integer"
&MyVariable.HasInitValue := true
```

---

## InitValue [SimTalk] - Variable

Resets a value recorded during a simulation run to an initial value.

- **Type:** Attribute
- **Syntax:** `<&>Variable.InitValue:any`
- **Value:** any

**Remarks:**
- Plant Simulation sets the value during the reset phase and resets it in the init phase of the next simulation run.
- The data types `table`, `list`, `stack`, `queue`, and `randtime` do not provide this feature.

```simtalk
&MyVariable.DataType := "integer"
&MyVariable.InitValue := 0
```

---

## IntegerPlaces [SimTalk] - Variable

Sets the number of integer places the Variable shows in the Frame.

- **Type:** Attribute
- **Syntax:** `<&>Variable.IntegerPlaces:integer`
- **Value:** integer

**Remarks:**
- Up to 15 integer places. Default `-1` applies no minimum. A positive value fills space before the decimal point with blank spaces.
- Applies only to data types `real`, `length`, `weight`, `time`, `speed`, and `acceleration`.

```simtalk
&MyVariable.IntegerPlaces := 6
-- The value "123"     will show as "   123"
-- The value "123456"  will show as "123456"
-- The value "1234567" will show as "1234567"
```

---

## Name [SimTalk] - Variable

Sets the name of the Variable designated by `&`.

- **Type:** Attribute
- **Syntax:** `<&>Variable.Name:string`
- **Value:** string

**Remarks:**
- Allowed characters: letters, digits, and underscore (`_`), e.g. `MyVariable`, `MyVariable1`, `My_Variable_1`.
- Cannot start with a digit (e.g. `1Variable` is not allowed).

```simtalk
&Variable.Name := "MyVariable"
```

---

## ShowDataType [SimTalk] - Variable

Shows (`true`) or hides (`false`) the data type of the Variable in the Frame.

- **Type:** Attribute
- **Syntax:** `<&>Variable.ShowDataType:boolean`
- **Value:** boolean

```simtalk
&myVariable.ShowDataType := false
```

---

## ShowUnit [SimTalk] - Variable

Shows (`true`) or hides (`false`) the units of the values of the Variable in the Frame.

- **Type:** Attribute
- **Syntax:** `<&>Variable.<UserDefinedAttribute>.ShowUnit:boolean`
- **Value:** boolean

```simtalk
&MyVariable.ShowUnit := true
```

---

## StatisticsActive [SimTalk] - Variable

Collects statistics values of the Variable (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<&>Variable.StatisticsActive:boolean`
- **Value:** boolean

**Remarks:** The Variable only collects statistics for the data types `string` and `integer`.

```simtalk
&MyVariable.StatisticsActive := true
```

---

## Transparent [SimTalk] - Variable

Makes the background of the Variable transparent (`true`) or not (`false`) in the Frame.

- **Type:** Attribute
- **Syntax:** `<&>Variable.Transparent:boolean`
- **Value:** boolean — `true` shows the space around the text in the background image color; `false` shows it in white.

**Remarks:** The `Transparent` setting also applies in 3D.

```simtalk
&MyVariable.Transparent := false
```

---

## Value [SimTalk] - Variable

Sets the value of the Variable designated by `&`.

- **Type:** Attribute
- **Syntax:** `<&>Variable.Value:any`
- **Watchable:** The attribute is watchable.
- **Value:** any

```simtalk
var obj: object 
obj := &MyVariable
waituntil obj.Value = 3 prio 1
regStat 
```
