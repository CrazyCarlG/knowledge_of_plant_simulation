# Read-Only Attributes of the PythonModule

## How to Show Attributes and Methods

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class**.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected **Instance**.

To query the value of a read-only attribute, you might, for example, type:

```
print MyPythonModule.UUID
```

---

## ModuleName [SimTalk]

Queries the name of the PythonModule designated by `<Path>`, which is returned in Python with the instruction `__name__`.

### Type
Read-only attribute

### Syntax
```
<Path>.ModuleName -> string
```

### Return Value
The return value has the data type `string`.

### Example
```
print PythonModule.ModuleName -- might return
pmbc4890ad_881f_45b2_b7a2_388d30656003
```

---

## Attributes of the PythonModule

The PythonModule provides:

- The attribute **PythonCode** [SimTalk].
- The **Attributes of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object **Station**.
