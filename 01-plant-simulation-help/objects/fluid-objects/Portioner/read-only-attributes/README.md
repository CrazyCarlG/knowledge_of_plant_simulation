# Read-Only Attributes of the Portioner

This directory documents the read-only attributes of the **Portioner** fluid object in Plant Simulation.

## Contents

| File | Description |
| --- | --- |
| `read-only-attributes.md` | Markdown documentation of the Portioner's read-only attributes. |
| `read-only-attributes.txtx` | Plain-text export of the same content. |

## Summary

The Portioner provides:

- The read-only attributes listed in the table of contents.
- The **_Read-Only Attributes of the Fluid Objects**.
- The **_Read-Only Attributes of All Objects**.

Read-only attributes can be queried but not set; Plant Simulation computes their value at the point-in-time of the query. In most cases a read-only attribute corresponds to an unavailable dialog item (e.g., on the Statistics tab).

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing the instance to show the selected Instance.

To query the value of a read-only attribute, for example:

```simtalk
print Portioner.CurrentAmount
```

### Syntax line

An example syntax line of an individual method:

```text
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object the method applies to.
- The signature lists the identifier and data type of each parameter in parentheses (e.g., `(Parameter:string)`). A constant value, a variable of the required type, or a method returning the required type may be used.
- Optional parameters are listed in brackets (e.g., `[,Parameter:boolean]`).
- Default values are shown after the parameter (e.g., `:= false`).
- The return value data type is shown after the arrow (e.g., `→ boolean`).

> **Note**
> Always enter parentheses for expressions within parentheses `(…)`; omitting them may lead to unexpected results and open the Debugger.

## Read-Only Attributes

### CurrentAmount [SimTalk]

Returns the **Current Amount** of the fluid in the container of the Portioner designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.CurrentAmount → real`
- **Return value:** `real`; the current amount is measured in liters.
- **Example:**

  ```simtalk
  print MyPortioner.CurrentAmount
  ```

- **See also:** Current Amount [Portioner]

### CurrentMaterial [SimTalk]

Returns the **Current Material** that flows into the Portioner designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.CurrentMaterial → string`
- **Return value:** `string`
- **Example:**

  ```simtalk
  print MyPortioner.CurrentMaterial
  ```

- **Remarks:** The name is not case-sensitive, just like the names of attributes and methods of the objects. To save memory and improve access speed, all places using such a case-insensitive string point to the same string in main memory; the first occurrence of the string defines how it is written in terms of upper- and lower-casing. In SimTalk you can compare strings case-insensitively with the `~=` operator (see *Relational Operators*).
- **See also:** Current Material [Portioner], Relational Operators, Attributes of the Portioner

---

*Source: Plant Simulation Help 11-2902 / 11-2904 / 11-2905. Unpublished work. © 2026 Siemens.*
