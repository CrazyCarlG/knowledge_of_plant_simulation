# PatchMatrix Attributes

## Read-Only Attributes of the PatchMatrix

The PatchMatrix provides:

- The **Read-Only Attributes of the Fluid Objects**.
- The **Read-Only Attributes of All Objects**.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyPatchMatrix.UUID
```

## Attributes of the PatchMatrix

The PatchMatrix provides:

- The **Attributes of the Fluid Objects**.
- The **Attributes of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
PatchMatrix.Name := "MyPatchMatrix"
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print PatchMatrix.Name
posit := MyStation.Cont.XPos
```

## MaterialsTable

Use the object **MaterialsTable** to define the ingredients and the products to be created and to be processed in the plant.
