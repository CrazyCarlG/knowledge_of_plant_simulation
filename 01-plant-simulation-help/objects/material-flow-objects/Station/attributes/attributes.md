# Attributes of the Station

This document summarizes the attributes of the **Station** object in Plant Simulation, including how to view, query, and set attributes, and a note about the related **ParallelStation** object.

## Viewing Attributes and Methods

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the **Home** ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Querying Read-Only Attributes

To query the value of a read-only attribute, type, for example:

```simtalk
print MyStation.UUID
```

## Attributes Provided by the Station

The Station provides:

- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

## Setting and Getting Attribute Values

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

To set the value of an attribute, type, for example:

```simtalk
MyStation.Pause := true
```

To get the value of an attribute, type, for example:

```simtalk
print MyStation.Pause
posit := MyStation.Cont.XPos
```

## ParallelStation

Use the object **ParallelStation** for modeling machines that process several parts in parallel at the same time.

### Description

- The built-in properties of the ParallelStation are the same as those of the Station.
- The ParallelStation has several processing places, as opposed to the single processing place of the Station.
- A set-up time always applies if a MU has a different name than the part it processed before, i.e., its predecessor.
- Plant Simulation always moves the MU as a whole, not continually; as soon as its front is located on the ParallelStation, the entire MU is located on it.
- On the tab **MU Animation**, you can set how the parts are distributed on the Animation Area of the ParallelStation.
- To show a tooltip with information about the ParallelStation, hover with the mouse over it.
