# Read-Only Attributes of the FluidSource

Summary of the `read-only-attributes.md` content in this directory.

## Overview

The FluidSource provides the following read-only attributes:

- **StatAmount** `[SimTalk]` — the object's own read-only attribute.
- The read-only attributes of the **Fluid Objects**.
- The read-only attributes of **all objects**.

Read-only attribute values can be queried but **cannot be set**, because Plant Simulation computes the value at the point in time when it is queried. In most cases, a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

## Viewing attributes and methods

Open the window **Show Attributes and Methods** to view all methods, read-only attributes, and attributes of the object:

- Select **Show Attributes and Methods** on the Class Library context menu to show the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing an instance, to show the selected Instance.

## Syntax conventions

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` — the path of the object the method applies to.
- `(Parameter:string)` — parameter identifier and data type; a variable or method of the required type may be used instead of a constant.
- `[,Parameter:boolean]` — optional parameters are in brackets.
- `:= false` — a default value follows the parameter.
- `→ boolean` — the return value data type follows the arrow.

> **Note:** Enter parentheses for expressions within parentheses `(…)`; omitting them may yield unexpected results and open the Debugger.

## StatAmount [SimTalk]

Returns the amount of material (number of liters) produced by the FluidSource designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatAmount → real`
- **Return Value:** `real`

### Example

```simtalk
print MyFluidSource.StatAmount
```

## See also

- Tab Statistics
- Attributes of the FluidSource
- Attributes of the Fluid Objects
- Attributes of All Objects
