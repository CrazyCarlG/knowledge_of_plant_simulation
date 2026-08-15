# DataList — General

## Description

The **DataList** is a list with one column that provides random access to the contents of the individual cells using their position (i.e., their row number). Think of the DataList as a file-card box:

- When you add an entry, Plant Simulation moves all entries after that position down.
- You can delete an entry.
- You can read an entry and add that entry back to the DataList.

You can access the functions of the list objects on the **List Ribbon Tab**.

## Note

- The DataList always opens in the background behind any open dialog boxes. You can also open it in the foreground as a dialog box with the method `openDialogBox`.
- The DataList shares its built-in properties with the data type `List`.
- Note the difference between the **object** DataList (which you can insert into a model) and the **data type** `list`:
  - User-defined attributes and local/global variables of data type `list` are part of another object, are not an object of their own, and do not have their own icon.
  - For this reason, these variables and attributes do **not** recognize the SimTalk functions of the DataList, such as `Location` or `existsIcon`. All other methods (especially read/write access) apply to both the DataList and to variables/attributes.
- To show a tooltip with information about the DataList, hover the mouse over it.
- To change the length of the graphic and the anchor points of the DataList, click **Show Manipulators** on the Edit ribbon tab or press **M**.

## Add the Object to the Simulation Model

To add the object DataList to your simulation model, click:

> **Manage Class Library > Basic Objects > InformationFlow > DataList** on the Home ribbon tab.

## See also

- Properties of Lists and Tables
- Work with Data in a List or Table (Step-by-Step Help)
- Access Data in Lists (Step-by-Step Help)
- Accessing a Range of Cells with a Method
- DataList

---

## Creating Lists within Lists and Tables

- Creating a List within a DataList

---

## Window of the DataList

Double-click the icon of the DataList to open its window. In the window you can change its simulation properties.

### Remarks

- The shared properties are described under **Dialog Items of the Objects**. You can access the functions of the list objects on the **List Ribbon Tab**.
- To edit the 3D properties of the object in the 3D model, select the object and press the **spacebar**, then change the respective settings in the dialog box **Edit 3D Properties**.
- To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press **M**.

### List Ribbon Tab

The List Ribbon Tab provides commands pertaining to lists and tables. Not all list objects provide all of the described commands.

---

## Methods of the DataList

The DataList provides:

- The methods listed in the table of contents to the left.
- The Methods of Lists and Tables.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
