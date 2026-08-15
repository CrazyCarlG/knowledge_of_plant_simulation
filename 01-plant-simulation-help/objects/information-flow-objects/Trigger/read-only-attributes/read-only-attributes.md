# Read-Only Attributes of the Trigger

## Viewing Attributes and Methods

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show the methods, read-only attributes, and attributes of the selected **Class**.
- Press **F8** or click **Show Attributes and Methods** on the **Home** ribbon tab of the **Frame** into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected **Instance**.

## CurrentValue [SimTalk]

Returns the **Current Value** of the Trigger designated by `<Path>`.

### Remarks
The data type of the value matches the data type of the Trigger.

### Type
Read-only attribute

### Syntax
```
<Path>.CurrentValue → any
```

### Return Value
The return value has the data type `any`.

### Example
```
print MyTrigger.CurrentValue
```

### See also
- Tab Representation
- Attributes of the Trigger

## Attributes of the Trigger

The Trigger provides:
- The attributes listed in the table of contents to the left.
- The **Attributes of All Objects**.

You can set the value of an attribute and get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

To set the value of an attribute:
```
MyTrigger.Combination := true
MyTrigger.CombinationTable.delete({0,1}..{*,*})
MyTrigger.CombinationTable.writeRow(1,1,Trig5,0,10,3600)
MyTrigger.CombinationTable.createNestedList(0,1)
MyTrigger.CombinationTable[0,1].setname("K1")
```

To get the value of an attribute:
```
print MyTrigger.Combination
posit := Station.Cont.XPos
```
