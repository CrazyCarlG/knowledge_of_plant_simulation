# Attributes of DataQueue and DataStack

## Viewing Attributes and Methods

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyDataStack.Full
```

## Provided Attributes

The DataStack and the DataQueue provide:

- The Attributes of Lists and Tables.
- The Attributes of All Objects.

## Setting and Getting Attribute Values

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows or by assigning values to the respective attributes.

To set the value of an attribute, you might, for example, type:

```simtalk
MyDataStack.MaxDim := -1
MyDataQueue.Alignment := "left"
```

To get the value of an attribute, you might, for example, type:

```simtalk
print myDataStack.MaxDim
posit := Station.Cont.XPos
```

## DataQueue vs. DataStack

The objects DataQueue and DataStack are lists with one column. They share all methods and attributes, but differ in their built-in properties.

- **DataQueue**: Plant Simulation accesses the content of the DataQueue using the FIFO method (First In First Out). Plant Simulation saves entries you add in the order you insert them in and removes the item waiting in the queue the longest first.
- **DataStack**: Plant Simulation accesses the content of the DataStack using the LIFO method (Last In First Out). Plant Simulation inserts new entries at the top of the DataStack and removes the contents of the cell you added last first.

## Adding the Object to the Simulation Model

To add the object DataQueue to your simulation model, click **Manage Class Library > Basic Objects > InformationFlow > DataQueue** on the Home ribbon tab.

To change the length of the graphic and the anchor points of the DataQueue, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

## See also

- Properties of the DataQueue
