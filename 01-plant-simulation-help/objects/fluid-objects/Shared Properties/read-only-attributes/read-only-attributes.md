# Read-Only Attributes of the Fluid Objects

## Overview

The Fluid Objects provide read-only attributes (listed in the table of contents) plus the read-only attributes of all objects. You can **query** the values of read-only attributes, but you cannot set them — Plant Simulation computes the value at the point-in-time when you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, on the **Statistics** tab).

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show them for the selected Instance.

To query the value of a read-only attribute, type for example:

```simtalk
print MyMixer.ResWorking
```

## Syntax Conventions

An example of a Syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier and parameter data types) is listed in parentheses. `(Parameter:string)` designates a string parameter. Instead of a constant value, you can use a variable of the required type or a method returning that type.
- **Note:** Enter the parentheses for expressions within parentheses `(…)`. Omitting them may lead to unexpected results and open the Debugger.
- Optional parameters are listed in brackets, e.g. `[,Parameter:boolean]`.
- If a parameter has a default value, it is shown after the parameter: `:= false`.
- If the method has a return value, its data type is shown after the arrow `→`, e.g. `→ boolean`.

---

## Read-Only Attributes

### CurrentInFlowrate

Returns the current **Inflow Rate** of the fluid object designated by `<Path>`.

- **Remarks:** The inflow rate is the amount of liters of material per second that flows into the object.
- **Type:** Read-only attribute
- **Watchable:** Yes
- **Return Value:** `real`

```
<Path>.CurrentInFlowrate → real
```

```simtalk
print FluidDrain.CurrentInFlowrate
```

---

### CurrentMaterialColor

Returns the current material color in the fluid object designated by `<Path>`.

- **Type:** Read-only attribute
- **Watchable:** Yes
- **Return Value:** `real`

```
<Path>.CurrentMaterialColor → real
```

```simtalk
print SourceCocoa.CurrentMaterialColor
```

**See also:** `MaterialsTable`

---

### CurrentMaterialDensity

Returns the current material density in the fluid object designated by `<Path>`.

- **Type:** Read-only attribute
- **Watchable:** Yes
- **Return Value:** `real`

```
<Path>.CurrentMaterialDensity → real
```

```simtalk
print SourceCocoa.CurrentMaterialDensity
// might, for example, return 1 for 1 gram per cubic centimeter
```

**See also:** `MaterialsTable`

---

### CurrentOutFlowrate

Returns the current **out-flow rate** of the fluid object designated by `<Path>`.

- **Remarks:** The out-flow rate is the amount of liters per second that flows out of the object.
- **Type:** Read-only attribute
- **Watchable:** Yes
- **Return Value:** `real`

```
<Path>.CurrentOutFlowrate → real
```

```simtalk
print Tank.CurrentOutFlowrate
```

---

### CurrentWeight

Returns the weight of the current material in the **DePortioner**, **Mixer**, **Portioner**, or **Tank** designated by `<Path>`.

- **Remarks:** The weight is shown in the unit selected under *File > Model Settings > Unit > Mass*.
- **Type:** Read-only attribute
- **Return Value:** `real`

```
<Path>.CurrentWeight → real
```

```simtalk
print MyMixer.CurrentWeight
```

**See also:** `Mass [model settings]`

---

### ResBlocked

Returns whether the fluid object designated by `<Path>` is blocked (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Return Value:** `boolean`

```
<Path>.ResBlocked → boolean
```

```simtalk
print MyMixer.ResBlocked
```

**See also:** `Blocked [state, material flow objects]`

---

### ResCurrentState

Returns the current state of the fluid object designated by `<Path>`.

- **Remarks:** During a simulation run a material flow resource can take on one of these states: **Working, Setting-up, Waiting, Blocked, Failed, Stopped, Paused, Powering Up/down,** or **Unplanned**.
- **Note:** If two states occur at the same time (e.g. Paused and Failed), the read-only attribute returns the state that also has precedence for statistics collection (e.g. Paused for Paused and Failed).
- **Type:** Read-only attribute
- **Watchable:** Yes — use it in `waituntil` instructions or to make the object `TimeSequence` record it in watch mode.
- **Return Value:** `string`

```
<Path>.ResCurrentState → string
```

```simtalk
print MyMixer.ResCurrentState
```

**See also:** `Resource Statistics`, `Working`, `Setting-Up`, `Waiting`, `Blocked`, `Failed`, `Stopped`, `Paused`, `Powering up/down`, `Unplanned` [states, material flow objects]

---

### ResSetup

Returns whether the fluid object designated by `<Path>` is Setting-up and not failed, not paused, or not stopped (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Return Value:** `boolean`

```
<Path>.ResSetup → boolean
```

```simtalk
print FluidDrain.ResSetup
```

**See also:** `Setting-Up [state, material flow objects]`

---

### ResWaiting

Returns whether the fluid object designated by `<Path>` is Waiting (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Return Value:** `boolean`

```
<Path>.ResWaiting → boolean
```

```simtalk
print MyMixer.ResWaiting
```

**See also:** `Waiting [state, material flow objects]`

---

### ResWorking

Returns whether the fluid object designated by `<Path>` is Working (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Return Value:** `boolean`

```
<Path>.ResWorking → boolean
```

```simtalk
print MyMixer.ResWorking
```

**See also:** `Working [state, material flow objects]`

---

## Related: Attributes of the Fluid Objects

All fluid objects have **attributes** whose value you can set and query. An attribute corresponds to a dialog item (check box, drop-down command, etc.) on one of the object's tabs. The fluid objects provide:

- The attributes listed in the table of contents.
- The attributes of the Importer.
- The Attributes of All Objects.

All fluid objects have predefined attributes controlling their behavior or representing their state. You can set and get an attribute's value either via the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the corresponding attributes.
