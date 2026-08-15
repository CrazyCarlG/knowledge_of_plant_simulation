# Attributes of the PythonModule

The PythonModule provides:

- The attribute **PythonCode [SimTalk]**.
- The **Attributes of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

---

## ModuleName [SimTalk]

Queries the name of the PythonModule designated by `<Path>`, which is returned in Python with the instruction `__name__`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.ModuleName -> string`
- **Return Value:** The return value has the data type `string`.

**Example**

```simtalk
print PythonModule.ModuleName -- might return 
pmbc4890ad_881f_45b2_b7a2_388d30656003
```

---

## PythonCode [SimTalk]

Designates the Python source code of the PythonModule designated by `<Path>`, which is passed to SimTalk and then executed in Plant Simulation.

- **Type:** Attribute
- **Syntax:** `<Path>.PythonCode:string`
- **Assignment Value:** You can assign a value of data type `string`.

**Example**

```simtalk
PythonModule.PythonCode = "print(42)" -- enter Python code into the PythonModule
```

---

## Variable [object]

Use the object **Variable** for storing data over an extended period of time.

### Description

The object `Variable` is a global variable that other objects and methods in Plant Simulation can access during a simulation run. A variable can represent an unknown item which stores a quantity. Variables can change their content. Variables are also known as placeholders or unknowns. The opposite of a Variable is a constant, whose value is known and does not change.

You might, for example, use a Variable to:

- store data over an extended period of time during your simulation run,
- increment or decrement values,
- assign values, etc.

A Variable of data type `list`, `queue`, `stack`, or `table` shows a type graphic to the left of its name when you insert it.

- Double-click the **Name** of the Variable to open its dialog. Instead, you can also right-click the Variable and select **Open** on the context menu.
- Double-click the type graphic of the Variable to open the window of the list object.

---

## Showing Attributes and Methods

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
PythonModule.Name := "MyPythonModule"
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print MyPythonModule.Origin
```
