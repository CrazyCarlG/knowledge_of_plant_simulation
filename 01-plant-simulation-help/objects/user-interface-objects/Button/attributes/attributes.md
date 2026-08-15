# Attributes of the Button

The Button provides:

- The attributes listed in the table of contents.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

## Examples

To query the value of a read-only attribute:

```simtalk
print MyButton.UUID
```

To set the value of an attribute:

```simtalk
MyButton.UseIcon := false
```

To get the value of an attribute:

```simtalk
print MyButton.UseIcon
posit := Station.Cont.XPos
```

## Control [SimTalk] — Button

Sets the Control, which the Button designated by `<Path>` executes when you click it.

### Remarks

The anonymous identifiers `?` and `@` are set to the Button when the method is called.

You can also enter a control which expects a boolean value as parameter. This control is called with the value `true` when you click the Button and with the value `false` when you release it.

The control is also called when you change the size of the Button or when you move it with Drag-and-Drop. If the control does not expect a parameter it will be called, as before, when you release the button.

### Type

Attribute

### Syntax

```
<Path>.Control:string
```

### Assignment Value

You can assign a value of data type `string`.

### Examples

```simtalk
MyButton.Control := "myControl"
self.~.~.&MyMethod.openDialog
```

## ObjectHeight [SimTalk] — Button

Sets the Height of the Button designated by `<Path>` with which it is shown in the Frame.

### Remarks

For an object height of more than 30 pixels the button shows the text of the label with a larger front size.

### Type

Attribute

### Syntax

```
<Path>.ObjectHeight:integer
```

### Assignment Value

You can assign a value of data type `integer`.

### Example

```simtalk
MyButton.ObjectHeight := 1 // meter
```

Related: Height [text box] — Button

## ObjectWidth [SimTalk] — Button

Sets the Width of the Button designated by `<Path>` with which it is shown in the Frame.

### Remarks

If you enter a long label, you have to adjust the width so that the label fits on the button without the text being cut off.

### Type

Attribute

### Syntax

```
<Path>.ObjectWidth:integer
```

### Assignment Value

You can assign a value of data type `integer`.

### Example

```simtalk
MyButton.ObjectWidth := 4 // meters
```

Related: Width [text box] — Button

## DropDownList [object]

Use the object DropDownList for showing a drop-down list in the Frame. When you select one of the items, it executes the action which you programmed in the control.
