# Pipe — Attributes

This document summarizes the attributes of the Pipe fluid object as described in the Plant Simulation Help.

## Overview

The Pipe provides:

- The attributes listed below.
- The Attributes of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show members of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing an instance to show members of the selected Instance.

You can set and get attribute values via dialog check boxes, text boxes, and drop-down lists, or by assigning values in SimTalk.

```simtalk
-- Set an attribute value
Pipe.PipeOpened := true

-- Get an attribute value
print Pipe.PipeOpened
posit := MyStation.Cont.XPos
```

---

## LengthOfPipe [SimTalk]

Returns the length of the Pipe designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.LengthOfPipe → real`
- **Return Value:** `real` — the length of the Pipe inserted into the Frame (from its first point to its last point).

```simtalk
print Pipe1.LengthOfPipe
```

---

## ExitStrategy [SimTalk] — Pipe

Sets how the flow rate of the Pipe designated by `<Path>` is distributed to the succeeding fluid objects.

- **Type:** Attribute
- **Syntax:** `<Path>.ExitStrategy:string`
- **Assignment Value:** `string` — either `"Evenly distributed"` or `"Percentage"`.

```simtalk
MyPipe.ExitStrategy := "Evenly distributed"
```

**See also:** Exit Strategy - Pipe

---

## ExitStrategyPercentageValues [SimTalk] — Pipe

Sets the proportional distribution of the flow rate for the **Exit Strategy > Percentage**.

**Remarks:**

- Specify `0` for a successor to prevent it from receiving any material.
- If a successor cannot receive material (e.g., a succeeding Tank is full), the Pipe redistributes that successor's portion to the remaining successors according to the percentages.
- The sum of the percentages does **not** have to add up to 100%. The actual sum of the percentages of all successors that can receive material corresponds to 100%. For example, `[40, 60]`, `[0.4, 0.6]`, and `[2, 3]` are equivalent.

- **Type:** Attribute
- **Syntax:** `<Path>.ExitStrategyPercentageValues:array`
- **Assignment Value:** `array`

```simtalk
MyPipe.ExitStrategy := "Percentage"
MyPipe.ExitStrategyPercentageValues := [20, 50, 30]
```

**See also:** Exit Strategy - Pipe > Percentage [Pipe]

---

## OutflowRate [SimTalk] — Pipe

Sets the outflow rate at which material flows out of the Pipe designated by `<Path>` to the next object in the flow of materials.

**Remarks:**

- Default value `-1` means the Pipe uses the same outflow rate as its predecessor.
- The outflow rate is the amount of liters of material that flows off per second.
- Applies to a Pipe located directly after a `FluidSource`, `DePortioner`, `Tank`, or `Mixer`.
- If you specify a value other than the default, Plant Simulation uses it even if it is higher than the predecessor's outflow rate.
- The outflow rate lets succeeding Pipes connected to a `FluidSource`, `Tank`, `DePortioner`, or `Mixer` have different outflow rates.
- If the Pipe's predecessor is another Pipe, the value is ignored and the text box is unavailable — **unless** the Pipe has a single successor and its predecessor Pipe also has a single successor. When several Pipes are arranged one behind the other, Plant Simulation uses the lowest specified value for all Pipes.

- **Type:** Attribute
- **Syntax:** `<Path>.OutflowRate:real`
- **Assignment Value:** `real`

```simtalk
Pipe.OutflowRate := 1
```

**See also:** Outflow Rate [Pipe]

---

## PipeOpened [SimTalk]

Opens the Pipe designated by `<Path>` so that materials can flow through it (`true`).

**Remarks:**

- Use `PipeOpened` to model a valve or gate valve to open and close the Pipe.
- To close the Pipe, specify `false`. The Pipe then shows the state **Pipe Closed** in cyan (state vertical / state horizontal).

- **Type:** Attribute
- **Syntax:** `<Path>.PipeOpened:boolean`
- **Assignment Value:** `boolean`

```simtalk
Pipe.PipeOpened := true
```

**See also:** Pipe Opened [check box]

---

## Related Object: FluidSource

Use the `FluidSource` object to produce the ingredients of the product (bulk goods or fluids) processed in the plant.

- Use the `FluidDrain` to remove processed and mixed products from the plant.
- To change the graphic length and anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.
- Hover over the FluidSource to show a tooltip with information about it.

**Add the object to the simulation model:** Click **Manage Class Library > Basic Objects > Fluids > FluidSource** on the Home ribbon tab.

Compare sample models via **Window > Start Page > Getting Started > Example Models > Small Examples**, then select a Category, Topic, and Example in the **Examples Collection** dialog and click **Open Model**.
