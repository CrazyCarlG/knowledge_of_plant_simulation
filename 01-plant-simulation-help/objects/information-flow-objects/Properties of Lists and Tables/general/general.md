# General — Properties of Lists and Tables

Lists and tables control the course of events in the model and create data during the simulation which they save to be evaluated later on.

Plant Simulation provides lists with one column (`DataList`, `DataStack`, `DataQueue`) and lists with several columns (`DataTable`, `TimeSequence`).

The following topics describe the general properties of the lists and tables. Plant Simulation provides five different lists and tables:

- **The DataList** — accesses all cells randomly by their position. You can add new cells at any position. If you remove a cell, all cells with a higher number move up one position.
- **The DataQueue** — accesses the cell you added first. It adds new cells after the last existing cell.
- **The DataStack** — accesses the cell you added last. If you add a cell, all existing cells move one position down. If you remove a cell, the remaining cells each move up one cell.
- **The DataTable** — accesses all cells randomly by their column and row number. New contents will overwrite and replace any existing contents of the cell.
- **The TimeSequence** — accesses all cells randomly by their column and row number. It adds new entries in ascending order according to the time. Entries with a higher position move up by one position if you remove a previous entry. The time-value pairs that the TimeSequence records belong together, meaning that you can only delete a pair of values, not either the time or the value of a pair.

You can access the properties of the list objects on the List Ribbon Tab.

## See also

- Window of Lists and Tables
- Methods of Lists and Tables
- Accessing Data in Lists
- Read-Only Attributes of Lists and Tables
- Accessing a Range of Cells with a Method
- Attributes of Lists and Tables
- Creating Lists within Lists and Tables
- Working with Lists and Tables

## Window of Lists and Tables

Double-click the icon of the list object which you inserted into your simulation model to open its window.

### Remarks

To change the properties of the Class of the object, double-click it in the Class Library or on the tab **Information Flow** in the Toolbox. There you can view or change the saved data or enter new data. You can also adapt the format and the data types to your needs.

You can access the functions of the list objects on the List Ribbon Tab.

To edit the 3D properties of the object in the 3D model, select the object and press the spacebar. Then change the respective settings in the dialog box **Edit 3D Properties**.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press M on the keyboard.

### See also

- Work with Data in a List or Table
- List Ribbon Tab
- Context Menu of the Contents of List Objects
- Context Menu of Embedded Lists
- Window of Lists and Tables
