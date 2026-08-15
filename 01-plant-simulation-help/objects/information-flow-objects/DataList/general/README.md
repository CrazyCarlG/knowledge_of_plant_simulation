# DataList — General (README)

This README summarizes the contents of the `general.md` file in this directory.

## Overview

The **DataList** is a single-column list that provides random access to individual cells by their position (row number). It behaves like a file-card box:

- Adding an entry shifts all subsequent entries down.
- Entries can be deleted.
- Entries can be read and re-added to the DataList.

List-object functions are accessed on the **List Ribbon Tab**.

## Key Notes

- The DataList opens in the background behind open dialog boxes; use the method `openDialogBox` to open it in the foreground.
- The DataList shares its built-in properties with the data type `List`.
- The **object** DataList (insertable into a model) differs from the **data type** `list`:
  - User-defined attributes and local/global variables of data type `list` are part of another object, are not standalone objects, and have no icon of their own.
  - Therefore they do not recognize SimTalk functions such as `Location` or `existsIcon`. All other methods (especially read/write access) apply to both.
- Hover over the DataList to show a tooltip with information about it.
- To change the graphic length and anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.

## Adding the Object to a Simulation Model

Click:

> **Manage Class Library > Basic Objects > InformationFlow > DataList** on the Home ribbon tab.

## See Also

- Properties of Lists and Tables
- Work with Data in a List or Table (Step-by-Step Help)
- Access Data in Lists (Step-by-Step Help)
- Accessing a Range of Cells with a Method
- DataList

## Creating Lists within Lists and Tables

- Creating a List within a DataList

## Window of the DataList

Double-click the DataList icon to open its window, where simulation properties can be changed.

### Remarks

- Shared properties are described under **Dialog Items of the Objects**; list-object functions are on the **List Ribbon Tab**.
- To edit 3D properties in the 3D model, select the object and press the **spacebar**, then adjust settings in **Edit 3D Properties**.
- To manipulate the graphic, click **Show Manipulators** on the Edit ribbon tab or press **M**.

### List Ribbon Tab

Provides commands for lists and tables; not all list objects provide all described commands.

## Methods of the DataList

The DataList provides:

- The methods listed in the table of contents.
- The Methods of Lists and Tables.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open the **Show Attributes and Methods** window.
