# Button — Methods

This folder documents the methods of the **Button** user-interface object. It contains:

- `methods.md` — the main Markdown documentation.
- `methods.txtx` — the raw source text (same content as `methods.md`).

There are no subfolders in this directory.

## Summary

The Button provides the **Methods of All Objects** — it has no Button-specific methods of its own.

### Viewing methods, attributes, and read-only attributes

To view the full list of methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- **Class level** — right-click the class in the Class Library and select **Show Attributes and Methods**.
- **Instance level** — select an inserted instance in a Frame, then press **F8** or click **Show Attributes and Methods** on the Home ribbon tab.

### Understanding a method's syntax line

A method's syntax line looks like:

```text
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` — path of the object the method applies to.
- `(Parameter:string)` — the method signature; parameters are listed in parentheses with their identifier and data type.
- Optional parameters are listed in brackets, e.g. `[,Parameter:boolean]`.
- A default value is shown after the parameter, e.g. `:= false`.
- A return type is shown after the arrow `→`, e.g. `→ boolean`.

> **Note:** Always enter the parentheses for expressions within parentheses `(…)`. Omitting them may produce unexpected results and open the Debugger.

## Read-Only Attributes

The Button provides the **_Read-Only Attributes of All Objects**. Their values can be queried but not set — Plant Simulation computes them at the point in time they are queried. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).
