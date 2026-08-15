# Attributes of the PythonModule

This folder documents the attributes of the **PythonModule** object in Plant Simulation.

## Contents

- `attributes.md` — Markdown documentation for the attributes.
- `attributes.txtx` — Plain-text export of the same content.

This folder contains no subfolders, so there are no README.md files inside subfolders.

## Summary

### Overview

The PythonModule provides:

- The attribute **PythonCode** [SimTalk].
- The **Attributes of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

### Attribute: `PythonCode` [SimTalk]

Designates the Python source code of the PythonModule designated by `<Path>`, which is passed to SimTalk and then executed in Plant Simulation.

- **Type:** Attribute
- **Syntax:** `<Path>.PythonCode:string`
- **Assignment value:** You can assign a value of data type `string`.

Example:

```simtalk
PythonModule.PythonCode = "print(42)" -- enter Python code into the PythonModule
```

### Read-only attribute: `ModuleName` [SimTalk]

Queries the name of the PythonModule designated by `<Path>`; in Python it is returned by the instruction `__name__`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.ModuleName -> string`
- **Return value:** `string`

Example:

```simtalk
print PythonModule.ModuleName -- might return
pmbc4890ad_881f_45b2_b7a2_388d30656003
```

### Object: `Variable`

Use the object **Variable** for storing data over an extended period of time.

The object `Variable` is a global variable that other objects and methods in Plant Simulation can access during a simulation run. It can represent an unknown item that stores a quantity, and its content can change (the opposite of a constant). Common uses include:

- storing data over an extended period of time during a simulation run,
- incrementing or decrementing values,
- assigning values.

A Variable of data type `list`, `queue`, `stack`, or `table` shows a type graphic to the left of its name when inserted.

- Double-click the **Name** of the Variable to open its dialog (or right-click the Variable and select **Open**).
- Double-click the type graphic of the Variable to open the window of the list object.

### Showing attributes and methods

- In the **Class Library**, select **Show Attributes and Methods** on the context menu to view the methods, read-only attributes, and attributes of a **Class**.
- For an **Instance**, press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame where the instance was inserted.

You can set the value of an attribute and get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

To set the value of an attribute, for example:

```simtalk
PythonModule.Name := "MyPythonModule"
```

To get the value of an attribute, for example:

```simtalk
print MyPythonModule.Origin
```
