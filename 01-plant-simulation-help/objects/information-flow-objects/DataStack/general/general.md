# DataStack — General

## Overview

- Plant Simulation accesses the content of the **DataStack** using the **LIFO** method (Last In First Out).
- Plant Simulation accesses the content of the **DataQueue** using the **FIFO** method (First In First Out).

To show a tooltip with information about the DataStack, hover with the mouse over it.

To change the length of the graphic and the anchor points of the DataStack, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## Add the Object to the Simulation Model

To add the object DataStack to your simulation model, click:

> Manage Class Library > Basic Objects > InformationFlow > DataStack

on the Home ribbon tab.

## Properties of the DataStack

The objects **DataStack** and **DataQueue** are lists with one column. They share all methods and attributes, but differ in their built-in properties.

### Remarks

Plant Simulation differentiates between DataStack and DataQueue:

- **DataStack (LIFO):** Plant Simulation inserts new entries at the top of the DataStack and removes the contents of the cell you added last first.
- **DataQueue (FIFO):** Plant Simulation saves entries in the order you insert them and removes the item waiting in the queue the longest first.

You can access the functions of the list objects on the **List Ribbon Tab**.

### Note

The DataStack always opens in the background behind any open dialog boxes. You can also open it in the foreground as a dialog box with the method `openDialogBox`.

The data type **Stack** shares the built-in properties of the DataStack.

Note the difference between the object **DataStack**, which you insert into your model, and the data type **stack**. You can create user-defined attributes and local/global variables of data type `stack` that are part of another object and thus are not an object of their own and do not have their own icon.

For this reason these variables and attributes do not recognize the SimTalk functions of the DataStack, such as `Location` or `existsIcon`. All other methods, especially for read and write access, apply to both the DataStack and to variables and attributes.

## Window of the DataStack

Double-click the icon of the DataStack to open its window. In the window you can change its simulation properties.

The shared properties are described under **Dialog Items of the Objects**. You can access the functions of the list objects on the **List Ribbon Tab**.

To edit the 3D properties of the object in the 3D model, select the object and press the **spacebar**. Then change the respective settings in the dialog box **Edit 3D Properties**.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## List Ribbon Tab

The List Ribbon Tab provides commands pertaining to the lists and tables. Not all list objects provide all of the described commands.

## Methods of the DataStack

The DataStack and the DataQueue provide the methods listed in the table of contents for accessing them.

The DataStack and the DataQueue provide:

- The methods:
  - `createNestedList` [SimTalk] — DataQueue
  - `pop` [SimTalk] — DataStack
  - `push` [SimTalk] — Stack
  - `pushList` [SimTalk]
  - `top` [SimTalk]
- The **Methods of Lists and Tables**.
- The **Methods of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the attributes and methods of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the attributes and methods of the selected Instance.

## See also

- Properties of the DataQueue
- DataStack
- Work with Data in a List or Table (Plant Simulation Step-by-Step Help)
- Access Data in Lists (Plant Simulation Step-by-Step Help)
- Creating a List within a DataQueue or DataStack
