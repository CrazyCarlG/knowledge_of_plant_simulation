# Methods of the DePortioner

This directory documents the methods and read-only attributes of the **DePortioner** fluid object in Plant Simulation.

## Contents

| File | Description |
| --- | --- |
| `methods.md` | Markdown documentation of the DePortioner's methods and read-only attributes. |
| `methods.txtx` | Plain-text export of the same content. |

> No subfolders are present in this directory, so there are no nested README files to summarize.

## Summary

The DePortioner provides:

- The **Methods of the Fluid Objects**.
- The **Methods of All Objects**.

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the selected Class (general description).
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing the instance to show the selected Instance (general description).

### Syntax line

An example syntax line of a method:

```text
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object the method applies to.
- The signature lists the identifier and data type of each parameter in parentheses (e.g., `(Parameter:string)`). A constant value, a variable of the required type, or a method returning the required type may be used.
- Optional parameters are listed in brackets (e.g., `[,Parameter:boolean]`).
- Default values are shown after the parameter (e.g., `:= false`).
- Return value data type is shown after the arrow (e.g., `→ boolean`).

> **Note**
> Always enter parentheses for expressions within parentheses `(…)`; omitting them may lead to unexpected results and open the Debugger.

## Read-Only Attributes of the DePortioner

The DePortioner provides:

- The read-only attributes listed in the table of contents.
- The **_Read-Only Attributes of the Fluid Objects**.
- The **_Read-Only Attributes of All Objects**.

Read-only attributes can be queried but not set; Plant Simulation computes their value at the point-in-time of the query. In most cases a read-only attribute corresponds to an unavailable dialog item (e.g., on the Statistics tab).

---

*Source: Plant Simulation Help 11-2935 / 11-2936. Unpublished work. © 2026 Siemens.*
