# General — DataQueue

## Overview

- **DataQueue** — Plant Simulation accesses the content of the DataQueue using the **FIFO** method (First In First Out). Entries are saved in the order they are inserted, and the item that has been waiting in the queue the longest is removed first.
- **DataStack** — Plant Simulation accesses the content of the DataStack using the **LIFO** method (Last In First Out). New entries are inserted at the top, and the contents of the cell added last are removed first.

To show a tooltip with information about the DataQueue, hover the mouse over it.

To change the length of the graphic and the anchor points of the DataQueue, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Add the Object to the Simulation Model

To add the object DataQueue to your simulation model, click:

> **Manage Class Library > Basic Objects > InformationFlow > DataQueue** on the Home ribbon tab.

## Properties of the DataQueue

The DataQueue is a list with one column that Plant Simulation accesses using the FIFO method (First In First Out).

### Remarks

- Plant Simulation saves entries in the order you insert them and removes the item waiting the longest first.
- You can access the functions of the list objects on the **List Ribbon Tab**.

> **Note:** The DataQueue always opens in the background behind any open dialog boxes. You can also open it in the foreground as a dialog box with the method `openDialogBox`.

- The data type `Queue` shares the built-in properties of the DataQueue.
- Note the difference between the object **DataQueue**, which you insert into your model, and the data type **queue**. You can create user-defined attributes and local/global variables of data type `queue` that are part of another object, and thus are not objects of their own and do not have their own icon.
- For this reason these variables and attributes do not recognize the SimTalk functions of the DataQueue, such as `Location` or `existsIcon`. All other methods, especially for read and write access, apply to both the DataQueue and to variables and attributes.

### See also

- Work with Data in a List or Table in the Step-by-Step Help
- Access Data in Lists in the Step-by-Step Help
- Creating a List within a DataQueue or DataStack
- Properties of the DataQueue

## Window of the DataQueue

Double-click the icon of the DataQueue to open its window. In the window you can change its simulation properties.

### Remarks

- The shared properties are described under **Dialog Items of the Objects**.
- You can access the functions of the list objects on the **List Ribbon Tab**.
- To edit the 3D properties of the object in the 3D model, select the object and press the spacebar, then change the respective settings in the dialog box **Edit 3D Properties**.
- To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## List Ribbon Tab

The List Ribbon Tab provides commands pertaining to the lists and tables. Not all list objects provide all of the described commands.

## Methods of DataQueue and DataStack

The DataStack and the DataQueue provide:

- The methods listed in the table of contents to the left.
- The Methods of Lists and Tables.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the attributes and methods of the selected Instance.

An example of the Syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

---

*Plant Simulation Help 11-4245–11-4248. Unpublished work. © 2026 Siemens.*
