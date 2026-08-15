# Read-Only Attributes of the Checkbox — Summary

This folder documents the **Read-Only Attributes of the Checkbox** user-interface object in Plant Simulation. The content is provided in two forms:

- `read-only-attributes.md` — Markdown version
- `read-only-attributes.txtx` — plain-text version (Plant Simulation Help export)

## Conventions

The documentation uses the following notation conventions:

- `<Path>` designates the path of the object to which a method applies.
- A method signature consists of the identifier and the data type of the parameter in parentheses, e.g. `(Parameter:string)`. Instead of a constant value you may use a variable of the required type or a method returning that type.
- Expressions within parentheses `(…)` must include the parentheses; omitting them may lead to unexpected results and open the Debugger.
- Optional parameters are listed in brackets, e.g. `[,Parameter:boolean]`.
- Default parameter values are shown after the parameter, e.g. `:= false`.
- Return types are shown after an arrow, e.g. `-> boolean`.

## Overview

- The Checkbox provides the **Read-Only Attributes of All Objects**.
- Read-only attribute values **can be queried but not set**; Plant Simulation computes each value at the point in time it is queried.
- A read-only attribute usually corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).
- To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:
  - In the **Class Library**: select **Show Attributes and Methods** from the context menu to show the selected Class.
  - In a **Frame**: press **F8** or click **Show Attributes and Methods** on the Home ribbon tab to show the selected Instance.
- Example query of a read-only attribute:

  ```simtalk
  print MyCheckbox.UUID
  ```

## Attributes of the Checkbox

The Checkbox provides:

- The attributes listed in the table of contents.
- The **Attributes of All Objects**.

Attribute values can be set and retrieved either through the dialog windows (check boxes, text boxes, drop-down lists) or by assigning values directly.

Example:

```simtalk
MyCheckbox.Value := false
```

## Source

Siemens Plant Simulation Help — section "Read-Only Attributes of the Checkbox" (pages 11-5176 / 11-5177), © 2026 Siemens.
