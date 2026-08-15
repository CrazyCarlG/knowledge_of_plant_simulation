# Attributes of DataQueue and DataStack

## Viewing Attributes and Methods

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Provided Attributes

The DataStack and the DataQueue provide:

- The Attributes of Lists and Tables.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

## Setting and Getting Attribute Values

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes, and drop-down lists in the dialog windows or by assigning values to the respective attributes.

### Setting an attribute value

```simtalk
MyDataStack.MaxDim := -1
MyDataQueue.Alignment := "left"
```

### Getting an attribute value

```simtalk
print myDataStack.MaxDim
posit := Station.Cont.XPos
```

### Querying a read-only attribute value

```simtalk
print MyDataStack.Full
```

## TimeSequence

Use the object **TimeSequence** for recording the course that values take over time, such as shift plans, machine maintenance schedules, or buffer occupancies.

### Description

The TimeSequence is a table with two columns.

- In **Watch mode**, Plant Simulation enters the time-value-pairs each time a watchable value changes.
- In **Sample mode**, Plant Simulation enters the time-value-pairs periodically, during certain time intervals, no matter if the value actually changes or not.

You can use the TimeSequence several times and sort the values to see if the values are always the same over time or if they change randomly.

---
*Plant Simulation Help 11-4257 · Unpublished work. © 2026 Siemens*
