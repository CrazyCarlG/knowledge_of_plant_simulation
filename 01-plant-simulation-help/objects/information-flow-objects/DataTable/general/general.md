# DataTable (General)

## Description

You can access the individual cells in the DataTable via their index, i.e., by their position designated by the number of the row and the number of the column. You can compare a DataTable to a shelf in which you enter values and references to the cells and remove them again.

As opposed to the DataList, the contents of the cells remain in the DataTable, and the DataTable can also have blank cells in a range. You can add and remove rows and columns during a simulation run at will.

You can access the functions of the list objects on the **List Ribbon Tab**.

## Notes

- The DataTable always opens in the background behind any open dialog boxes. You can open it in the foreground as a dialog box with the method `openDialogBox`.
- The DataTable shares its built-in properties with the data type `table`. Note the difference between the object **DataTable** that you can insert into models and the data type `table`:
  - You can create user-defined attributes and local/global variables of data type `table` that are part of another object, and thus are not an object of their own and do not have their own icon.
  - For this reason these variables and attributes do not recognize the SimTalk functions of the DataTable, such as `Location` or `existsIcon`. All other methods, especially for read and write access, apply to both the DataTable and to variables and attributes.
- You can also show the contents of a DataTable in an HtmlReport (compare "Display a DataTable or a DataList").
- To show a tooltip with information about the DataTable, hover with the mouse over it.
- To change the length of the graphic and the anchor points of the DataTable, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.
- The **MaterialsTable** of the fluid objects shares the properties of the DataTable.

## Add the Object to the Simulation Model

To add the object DataTable to your simulation model, click **Manage Class Library > Basic Objects > InformationFlow > DataTable** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog *Examples Collection*, and click Open Model.

## See also

- Work with Data in a List or Table in the Step-by-Step Help
- Work with Data in the DataTable in the Step-by-Step Help
- Access Data in Lists in the Step-by-Step Help
- Accessing a Range of Cells with a Method
- Creating Lists within Lists and Tables
- Creating a List within a DataTable
- Window of the DataTable

Example models that use lists and tables:

- Produce Parts According to a Delivery Table
- Produce the Parts with a Source Using a Sequence Table
- Produce Parts in a Fixed Sequence Over and Over Again
- Visualize the Occupancy of the Store Over Time
- Produce Parts With a Random Frequency Entered into a Data Table
- Model Processing and Set-up Jobs
- Produce Parts With a Percentage Entered into a Data Table
- Write the Content List into a Table for Further Processing
- Define Times in the Class of the Processing Stations
- Select Where the Data Comes From
- Create the Work Plan

## Window of the DataTable

Double-click the icon of the DataTable to open its window. In the window you can change its simulation properties.

### Remarks

- The shared properties are described under *Dialog Items of the Objects*.
- You can access the functions of the list objects on the **List Ribbon Tab**.
- To edit the 3D properties of the object in the 3D model, select the object and press the spacebar. Then change the respective settings in the dialog box *Edit 3D Properties*.
- To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

### List Ribbon Tab

The List Ribbon Tab provides commands pertaining to the lists and tables. Not all list objects provide all of the described commands.

## Methods of the DataTable

The DataTable provides:

- Methods of Columns of the DataTable
- Methods of Rows of the DataTable
- Miscellaneous Methods of the DataTable
- Methods for Accessing the DataTable
- Methods for Instantiating the DataTable
- The shared Methods of Lists and Tables
- The shared Methods of All Objects

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.
