# Read-Only Attributes of the PythonModule

This folder documents the read-only attributes of the **PythonModule** object in Plant Simulation.

## Contents

- `read-only-attributes.md` — Markdown documentation for the read-only attributes.
- `read-only-attributes.txtx` — Plain-text export of the same content.

## Summary

### Showing attributes and methods

- In the **Class Library**, select **Show Attributes and Methods** on the context menu to view the methods, read-only attributes, and attributes of a **Class**.
- For an **Instance**, press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame where the instance was inserted.

To query a read-only attribute's value, for example:

```
print MyPythonModule.UUID
```

### Read-only attribute: `ModuleName`

Queries the name of the PythonModule designated by `<Path>`; in Python it is returned by the instruction `__name__`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.ModuleName -> string`
- **Return value:** `string`

Example:

```
print PythonModule.ModuleName -- might return
pmbc4890ad_881f_45b2_b7a2_388d30656003
```

### Attributes of the PythonModule

The PythonModule provides:

- The attribute **PythonCode** [SimTalk].
- The **Attributes of All Objects**.

Use the **Show Attributes and Methods** window to view all methods, read-only attributes, and attributes of the object.
