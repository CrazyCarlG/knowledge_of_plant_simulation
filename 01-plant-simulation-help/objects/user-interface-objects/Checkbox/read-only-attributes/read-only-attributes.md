# Read-Only Attributes of the Checkbox

## Conventions

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of a method consists of the identifier and the data type of the parameter, listed in parentheses. For example, `(Parameter:string)` designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. For example, `[,Parameter:boolean]` means that you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, e.g. `:= false`.
- If the method has a return value, the signature shows its data type after the arrow `->`, e.g. `-> boolean`.

## Overview

The Checkbox provides the _Read-Only Attributes of All Objects_.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyCheckbox.UUID
```

## Attributes of the Checkbox

The Checkbox provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

To set the value of an attribute, you might, for example, type:

```simtalk
MyCheckbox.Value := false
```
