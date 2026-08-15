# Read-Only Attributes of DataQueue and DataStack

## `top` [SimTalk]

Reads the contents of a cell in a list with one column **without removing it**.

### Remarks
The DataStack and the DataQueue designated by `<Path>` set the position of the cell according to their built-in properties.

### Type
Method

### Syntax
```
<Path>.top
```

### Example
```simtalk
print MyDataStack.top
```

## Read-Only Attributes of DataQueue and DataStack

The DataStack and the DataQueue provide:

- The Read-Only Attributes of Lists and Tables.
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyDataStack.Full
```

## Attributes of DataQueue and DataStack

The DataStack and the DataQueue provide:

- The Attributes of Lists and Tables.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
