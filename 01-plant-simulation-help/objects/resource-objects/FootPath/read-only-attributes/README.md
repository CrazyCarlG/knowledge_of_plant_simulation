# README — Read-Only Attributes of the FootPath

This directory documents the **read-only attributes** of the **FootPath** object in Plant Simulation.

## Source Files

- `read-only-attributes.md` — the primary markdown reference.
- `read-only-attributes.txtx` — plain-text export of the same reference content.

There are no subfolders containing additional `README.md` files.

## Summary

The Exporter provides the **Read-Only Attributes of All Objects**. Read-only attribute values can be queried, but they cannot be set — Plant Simulation computes the value at the point in time when it is queried. In most cases, a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

### Viewing Attributes and Methods

Open the **Show Attributes and Methods** window to view all methods, read-only attributes, and attributes of the object:

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show them for the selected **Class**.
- Press the **F8** key, or click **Show Attributes and Methods** on the **Home** ribbon tab of the Frame containing an inserted instance, to show them for the selected **Instance**.

### Querying a Read-Only Attribute

Query a value with `print`, for example:

```simtalk
print MyFootPath.UUID
```

### Attributes of the FootPath

The FootPath provides:

- The attributes listed in the table of contents to the left.
- The **Attributes of All Objects**.

Attribute values can be set and read either through the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values directly, for example:

```simtalk
MyFootPath.length := 5
```

### Syntax Conventions

- `<Path>` designates the path of the object to which the method applies.
- The method signature — identifier and parameter data type — is listed in parentheses, e.g. `(Parameter:string)`.
- Optional parameters are listed within brackets, e.g. `[,Parameter:boolean]`.
- Default values are shown after the parameter, e.g. `:= false`.
- Return values are shown after the arrow, e.g. `-> boolean`.
- **Note:** Always enter the parentheses for expressions within parentheses `(…)`; omitting them may lead to unexpected results and open the Debugger.

---
*Plant Simulation Help 11-3059 — Unpublished work. © 2026 Siemens*
