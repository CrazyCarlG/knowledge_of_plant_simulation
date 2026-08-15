# Methods of the Pipe — Summary

This folder documents the **methods** topic for the `Pipe` fluid object in Plant Simulation.

## Contents

- `methods.md` — Markdown rendering of the help topic.
- `methods.txtx` — Raw source text extracted from the Plant Simulation Help.

> No subfolders with their own `README.md` exist in this directory.

## Summary of `methods.md`

The `Pipe` does not define any object-specific methods of its own. Instead, it provides the **Methods of All Objects**, which are inherited from the base object.

### Viewing methods, read-only attributes, and attributes

To inspect all methods, read-only attributes, and attributes of a `Pipe`, open the **Show Attributes and Methods** window (illustrated in the help using the example of the object `Station`). It can be opened in two ways:

- **Class level** — select **Show Attributes and Methods** on the context menu of the **Class Library** to show members of the selected *Class* (general description).
- **Instance level** — press **F8**, or click **Show Attributes and Methods** on the **Home** ribbon tab of the *Frame* into which the instance was inserted, to show members of the selected *Instance* (general description).

### Method syntax conventions

An example syntax line looks like:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

Conventions used in syntax lines:

- `<Path>` — designates the path of the object to which the method applies.
- **Signature** — the identifier and data type of each parameter, listed in parentheses.
  - Example: `(Parameter:string)` designates a parameter of data type `string`.
  - A constant value may be replaced by a variable of the required type, or by a method returning that type.
- **Optional parameters** — listed in brackets.
  - Example: `[,Parameter:boolean]` means the boolean parameter may, but does not have to, be entered.
- **Default value** — shown after the parameter in the signature.
  - Example: `:= false`.
- **Return value** — its data type is shown after the arrow.
  - Example: `→ boolean`.

> **Note:** Always enter the parentheses for expressions nested within parentheses `(…)`. Omitting them may lead to unexpected results and open the Debugger.

### Read-only attributes

The `Pipe` provides:

- The read-only attributes listed in the table of contents.
- The **_Read-Only Attributes of All Objects**.

Read-only attributes can be **queried but not set**: Plant Simulation computes the value at the point in time when it is queried. In most cases, a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

---

*Source: Plant Simulation Help — Methods of the Pipe*
