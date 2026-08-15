# Read-Only Attributes of the DataList

## Overview

The DataList provides the following read-only attributes:

- The _Read-Only Attributes of Lists and Tables.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation
computes the value for the point-in-time at which you query it. In most cases a read-only attribute
corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab
Statistics.

## Viewing Attributes and Methods

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show
Attributes and Methods**. The figure below illustrates the information using the example of the object
Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods,
  read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into
  which you inserted an instance to show the methods, read-only attributes, and attributes of the
  selected Instance [general description].

## Querying a Read-Only Attribute

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyDataList.Full
```

## Attributes of the DataList

The DataList provides:

- The Attributes of Lists and Tables.
- The Attributes of All Objects.

### Setting and Getting Attribute Values

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes
and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
myDataList.InfoflowReadOnly := true
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print myDataList.InfoflowReadOnly
```

Example of reading a coordinate value from another object:

```simtalk
posit := Station.Cont.XPos
```

## Related: DataStack

Use the object **DataStack** for accessing data according to the LIFO method (Last In First Out).

The objects **DataQueue** and **DataStack** are lists with one column. They share all methods and attributes,
but differ in their built-in properties.
