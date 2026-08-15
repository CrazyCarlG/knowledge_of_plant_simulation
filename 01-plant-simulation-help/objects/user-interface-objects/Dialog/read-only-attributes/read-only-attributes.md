# Read-Only Attributes of the Dialog

## updateUserDialog [SimTalk]

Updates the contents of the Dialog designated by `<Path>`.

**Remarks**

The Dialog then shows features that you changed in tables defining the items, or shows new or changed pictures and icons of the items.

**Type**

Method

**Syntax**

```
<Path>.updateUserDialog
```

**Example**

```
MyDialog.updateUserDialog
```

## Read-Only Attributes of the Dialog

The Dialog provides the *Read-Only Attributes of All Objects*.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```
print MyDialog.UUID
```

## Attributes of the Dialog

The Dialog provides:

- The attributes listed in the table of contents to the left.
- The **Attributes of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

---

*Plant Simulation Help 11-5149 / 11-5150*
