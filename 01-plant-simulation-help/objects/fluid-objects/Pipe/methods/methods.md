# Methods of the Pipe

## Overview

The Pipe provides the **Methods of All Objects**.

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window (illustrated in the help using the example of the object `Station`).

Two ways to open the window:

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show the members of the selected *Class* (general description).
- Press the **F8** key, or click **Show Attributes and Methods** on the **Home** ribbon tab of the *Frame* into which you inserted an instance, to show the members of the selected *Instance* (general description).

## Method Syntax

An example of the syntax line of an individual method looks like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

Conventions used in syntax lines:

- `<Path>` designates the path of the object to which the method applies.
- The method **signature** — the identifier and data type of each parameter — is listed in parentheses.
  - Example: `(Parameter:string)` designates a parameter of data type `string`.
  - Instead of a constant value, you can also pass a variable of the required type or a method that returns the required type.
- **Optional parameters** are listed in brackets.
  - Example: `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a **default value**, the signature shows it after the parameter.
  - Example: `:= false` in the example above.
- If the method has a **return value**, the signature shows its data type after the arrow.
  - Example: `→ boolean` in the example above.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

## Read-Only Attributes of the Pipe

The Pipe provides:

- The read-only attributes listed in the table of contents.
- The **_Read-Only Attributes of All Objects**.

You can query the values of read-only attributes, but you cannot set them — Plant Simulation computes the value for the point in time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, the **Statistics** tab).

---

*Source: Plant Simulation Help (Methods of the Pipe)*
