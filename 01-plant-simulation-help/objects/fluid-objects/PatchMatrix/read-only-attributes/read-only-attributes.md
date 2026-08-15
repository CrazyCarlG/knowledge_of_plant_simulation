# Read-Only Attributes of the PatchMatrix

The PatchMatrix provides:

- The _Read-Only Attributes of the Fluid Objects.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object **Station**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the F8 key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

To query the value of a read-only attribute, you might, for example, type:

```java
print MyPatchMatrix.UUID
```

## Attributes of the PatchMatrix

The PatchMatrix provides:

- Read-Only Attributes of the PatchMatrix

---

Plant Simulation Help · Unpublished work. © 2026 Siemens
