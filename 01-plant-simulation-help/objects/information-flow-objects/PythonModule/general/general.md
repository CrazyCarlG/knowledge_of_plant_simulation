# PythonModule

Use the object **PythonModule** to use Python code in a Plant Simulation model with full access to the Plant Simulation object model from within the Python code.

## Requirements

Using Python requires an installation of CPython on your computer. The official Python distribution from <https://www.python.org/> is recommended; a Python version installed via Anaconda also works.

If you use multiple Python environments, specify the path to the Python DLL with the SimTalk function `setPythonDLLPath`:

```simtalk
setPythonDLLPath(dllpath:string)
```

For example:

```simtalk
setPythonDLLPath("C:\Program Files\Python312\python312.dll")
```

> **Note:** Plant Simulation supports Python versions 3.12, 3.13, and 3.14.

## Limitations When Using Python Libraries

- With certain libraries (e.g. Pandas or NumPy), always exit Plant Simulation instead of just closing the model and opening a new one. Closing a model uninitializes the Python interpreter; reopening and reusing these libraries can crash because they do not support reinitialization.
- Libraries like MatPlotLib can open a window that starts a new Windows message pump. Close such a window before interacting with Plant Simulation again, otherwise it might crash.
- To show a tooltip about the PythonModule, hover the mouse over it.

## Adding the PythonModule to Your Model

To add the PythonModule to the Class Library, click **Manage Class Library > Basic Objects > Information Flow > PythonModule** on the Home ribbon tab.

After adding it to the Class Library, insert a PythonModule object into the model Frame, open its dialog, type in the Python code, and execute it.

Once added, the PythonModule shows the global Python variables on the **Tab Content**.

## Context Menu of the PythonModule

Right-click in the Tab Content to show the context menu. Click **Import** before selecting a context menu command.

- **Show White Space** — shows blank spaces between words.
- **Show Global Variables** — opens a dialog showing the global variables used in this PythonModule.

## What You Can Do With the PythonModule

Python is a high-level programming language with a vast amount of libraries. You can, for example, use the PythonModule to extract simulation results, do extensive data processing with Python libraries, and display values in various charts. You don't even need to know Python itself, as ChatGPT is well-trained for it.

To import the module into the Python interpreter, click **Import** in the top right corner of the PythonModule dialog, or press **F5** while the cursor is on the Tab Content.

> **Note:** Plant Simulation automatically applies the source code when you click Import or press F5.

The PythonModule provides the built-in attribute `PythonCode` (data type string) to get and set the Python source code from a SimTalk Method.

To run Python code from SimTalk, use the methods `call` and `callKw`:

```simtalk
<Path>.call([functionName:string, ...]) -> any
<Path>.callKw([functionName:string, ..., KeyValuePairs:any[] ]) -> any
```

To execute a function defined in the PythonModule, specify the function name as the first argument, then the arguments to pass to Python.

Given the following Python code in the PythonModule:

```python
def multiply(a, b):
    return a*b
```

Click **Apply** in the dialog, then execute the function from SimTalk in a Method with `print`:

```simtalk
print MyPythonModule.call("multiply", 3, 4)
```

> **Note:** Make sure that **Prohibit Access to the Computer** in the Model Settings is cleared. Python error messages are shown in English (not localized).

To call Python functions in SimTalk with keyword arguments, use `callKw`. Pass keyword arguments as an array of keyword/value pairs:

```simtalk
print MyPythonModule.callKw("multiply", ["a", 3, "b", 4])
```

With the Python code typed into the PythonModule you can:

- Access the Model Frame from the Python Code
- Access Attributes and Methods from the Python Code
- Access DataTables from the Python Code
- Access Variables from the Python Code
- Call Global SimTalk Functions from the Python Code
- Execute External Python Code

You can also display a PythonModule in the HtmlReport.

> **Note:** Python code is not intended to replace SimTalk. Since SimTalk also accesses compiled built-in functions, it is generally faster than Python code. As many university graduates learn Python, the PythonModule makes programming in Plant Simulation easier.

## Dialog Box of the PythonModule

Double-click the icon of the PythonModule to open its dialog box.

- **Edit Simulation Properties** — change the simulation properties of the object (shared properties described under "Dialog Items of the Objects").
- **Edit Animation Properties** — edit 3D properties via the **Edit 3D Properties** button (lower left of the simulation properties dialog) or by selecting the object and pressing the spacebar. To manipulate the graphic, click **Show Manipulators** on the Edit ribbon tab or press **M**.

### Import [button] - PythonModule

Click this button to import the code into the Python interpreter and execute it.

- Hold **Shift** while clicking Import to reload the module and delete all global variables.
- Hold **Shift + Ctrl** while clicking to copy an import statement for the module to the clipboard.

SimTalk equivalent: `import [SimTalk] - Python`.

## Tab Content

After adding the PythonModule to the model, it shows the global Python variables on the Tab Content. Type the Python code to execute in Plant Simulation on the Tab Content.

With the Python code you can:

- Access the Model Frame from the Python Code
- Access Attributes and Methods from the Python Code
- Access DataTables from the Python Code
- Access Variables from the Python Code
- Call Global SimTalk Functions from the Python Code
- Call a Function Written in Another PythonModule
- Execute External Python Code

Click **Import** to import the Python code typed on the Tab Content into the Python interpreter.

> **Note:** Plant Simulation saves the Python code in a folder model in a separate `.py` file. The Python variable `__file__` contains the path to that `.py` file. If the model is not a folder model, `__file__` is not defined.

### Access the Model Frame from the Python Code

Use the global Python variables `basis`, `root`, `current`, and `self` in the Python code. The PythonModule shows them when inserted into the model.

- **basis** — references the root of your Class Library. As opposed to SimTalk, a Python path cannot start with a period (`.`), so start an absolute path with `basis`:

```python
print(basis.Models.Model.Station)
```

- **root** — designates the root of the Frame hierarchy (the Frame containing the EventController). Start the path with `root` to access an object in the root Frame:

```python
print(root.EventController)
```

> **Note:** As opposed to SimTalk, you do have to specify the path to an object in Python.

- **current** — designates the Frame into which you inserted the PythonModule. Start the path with `current`:

```python
print(current.Station)
```

- **self** — designates the PythonModule itself.

### Access Attributes and Methods from the Python Code

Use the same syntax as in SimTalk.

**Accessing attributes** of a Plant Simulation object:

```python
print(current.Station.ProcTime)
current.Station.ProcTime = 50
```

**Accessing methods** of a Plant Simulation object:

```python
current.MyStation.deleteObject
print(current.Station.succ())
print(current.Station.succ(1))
```

If a method accepts arguments — even if all are optional — you must always use parentheses to call it.

**Executing SimTalk methods from Python** — use the `execute` method of the Method object:

```python
current.MyMethod.execute()
current.MyMethod.execute("Test", 123)
print(current.MyMethod.execute("Test", 123))
```

### Access DataTables from the Python Code

Use Python index access to access cells. To access column 2, row 3:

```python
print(root.DataTable[2,3])
```

The code above returns a list with the values of the rows; if one of the indices is a slice, Plant Simulation always returns a list containing the row values.

```python
print(current.DataTable[1:, 2])
```

This returns the value of cell `[1,1]`:

```python
print(current.DataTable[1:2, 1:2])
```

It returns a list with a list containing the value of cell `[1,1]`, so a list of lists is returned whenever you specify a range for column and row.

To get the entire content of the DataTable:

```python
print(root.DataTable[None]) # gets the entire content of the DataTable
```

- If the DataTable has a unique column index, you get a Python dictionary with the column index as key.
- Otherwise, you get a Python list of lists containing the row values.

You can also use Python slices to get partial data.

> **Note:** The hash symbol `#` in Python code denotes a comment to the end of the line.

### Access Variables from the Python Code

Use the attribute `Value` of the Variable:

```python
print(root.Variable.Value)
root.Variable.Value = 42
```

### Call Global SimTalk Functions from the Python Code

First import the `PlantSimulation` module, then call the predefined functions Plant Simulation provides:

```python
import PlantSimulation as ps
x = ps.existsObject(".Models.Model.EventController")
print(x)
```

### Call a Function Written in Another PythonModule

To call a function written in one PythonModule from a different PythonModule, get the name of the module you want to import.

In this example, to import code from `PythonModule1` into the current PythonModule:

1. Call `print(__name__)` in PythonModule1 — this prints the module name to the Console.
2. Copy the string from the Console and paste it after the `import` keyword into the PythonModule where you want to execute it.
3. Click **Import** — this prints the result of the multiplication to the Plant Simulation Console.

### Execute External Python Code

Use the SimTalk function `executePythonFile` to execute Python code stored in an external file:

```simtalk
print executePythonFile("D:\test.py", "TestArg")
```

You can access objects in the Plant Simulation model the same way as when executing Python code using a PythonModule.

## Tab User-defined

Define your own attributes as described under the Tab User-defined. The dialog provides the **Callback** method as a user-defined attribute.

## Navigate Menu / View Menu / Tools Menu / Help Menu

- Commands described under the respective menu sections.
- View Menu provides **Refresh** and **Show Attributes and Methods** (SimTalk: `updateDialog`).
- Tools Menu and Help Menu commands described under their respective sections.

## Methods of the PythonModule

The PythonModule provides:

- The methods listed in the table of contents.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library (Class).
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame (Instance).

## See also

- New Syntax [command]
- SimTalk 2.0 and SimTalk 1.0 Compared
- A Quick Tour Through SimTalk 2.0
- General Access to SimTalk
- What You Can Do With the PythonModule
- View the Sample Models
- setPythonDLLPath [SimTalk]
- executePythonFile [SimTalk]
- DataTable [object]
- Variable [object]
- Value [SimTalk] - Variable
- Predefined Functions
- import [SimTalk] - Python
- execute [SimTalk] - Method
- Video on YouTube: <https://youtu.be/2QJeW5r1AF4?si=S8Ee2D-4zyOevXZG>
