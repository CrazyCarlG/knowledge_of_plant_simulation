# Attributes of the Checkbox

## General

- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.
- To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyCheckbox.UUID
```

The Checkbox provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

To set the value of an attribute, you might, for example, type:

```simtalk
MyCheckbox.Value := false
```

To get the value of an attribute, you might, for example, type:

```simtalk
print MyCheckbox.Value
posit := Station.Cont.XPos
```

## Control [SimTalk] - Checkbox

Sets the control which the Checkbox designated by `<Path>` executes.

### Remarks

- Plant Simulation calls the Control when the value changes when you click the object.
- Plant Simulation only calls the Control of the object itself, not of instances of the object.

### Type

Attribute

### Syntax

```simtalk
<Path>.Control:method
```

### Assignment Value

You can assign a value of data type `method`.

### Example

```simtalk
MyCheckbox.Control := "myControl"
```

### See also

- Control [Checkbox]

## Value [SimTalk] - Checkbox

Activates (`true`) or deactivates (`false`) the Checkbox designated by `<Path>`. The Checkbox executes a Control when its value changes.

### Syntax

```simtalk
<Path>.Value:boolean
```

### Watchable

The attribute is watchable.

### Assignment Value

You can assign a value of data type `boolean`.

### Example

```simtalk
MyCheckbox.Value := false
```

### See also

- Value [drop-down list] - Checkbox
- Control [Checkbox]

## Button [object]

Use the object Button for showing a button in the Frame. When you click the button, it executes the action which you programmed in a control.

### Description

The Button executes the action, which you programmed in the Control, when the user clicks it. If you type in a label for the button, Plant Simulation shows that label on the button in the Frame.
