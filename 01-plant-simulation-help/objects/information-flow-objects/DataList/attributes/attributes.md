# attributes

## Summary

This page describes how to access and work with attributes of the `DataList` class and its instances, and covers the `DataStack` object.

### Showing attributes and methods

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which an instance was inserted, to show the methods, read-only attributes, and attributes of the selected Instance.

### Setting and getting attribute values

You can set and get an attribute's value either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute:

```simtalk
myDataList.InfoflowReadOnly := true
```

- To get the value of an attribute:

```simtalk
print myDataList.InfoflowReadOnly
posit := Station.Cont.XPos
```

## DataStack

The `DataStack` object is used to access data according to the **LIFO** method (Last In First Out).

### Description

The objects `DataQueue` and `DataStack` are lists with one column. They share all methods and attributes, but differ in their built-in properties:

- `DataStack`: Plant Simulation accesses the content using the **LIFO** method (Last In First Out).
- `DataQueue`: Plant Simulation accesses the content using the **FIFO** method (First In First Out).

### Tips

- Hover with the mouse over a `DataStack` to show a tooltip with information about it.
- To change the length of the graphic and the anchor points of the `DataStack`, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

### Adding the object to the simulation model

To add the `DataStack` object to your simulation model, click:

**Manage Class Library > Basic Objects > InformationFlow > DataStack** on the Home ribbon tab.

## See also

- Properties of the DataQueue
