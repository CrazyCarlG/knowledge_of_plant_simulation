# Read-Only Attributes of the PatchMatrix

This directory documents the read-only attributes of the **PatchMatrix** fluid object.

## Summary

The `read-only-attributes.md` file covers the following:

- The PatchMatrix provides the **Read-Only Attributes of the Fluid Objects** and the **Read-Only Attributes of All Objects**.
- Read-only attributes can be **queried but not set** — Plant Simulation computes their value at the point in time they are queried.
- A read-only attribute usually corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).
- To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window.

### Viewing attributes

- **Class Library context menu** → **Show Attributes and Methods** shows the members of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing an instance to show the members of the selected Instance.

### Querying a read-only attribute

```java
print MyPatchMatrix.UUID
```

## Files in this directory

- `read-only-attributes.md` — full help-page text on the PatchMatrix read-only attributes.
- `read-only-attributes.txtx` — plain-text export of the same help page.

---

Plant Simulation Help · Unpublished work. © 2026 Siemens
