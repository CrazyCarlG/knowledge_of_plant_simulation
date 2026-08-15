# Read-Only Attributes of the Generator

## Overview

The Generator provides the **Read-Only Attributes of All Objects**.

You can query the values of read-only attributes, but you cannot set them — Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

## Viewing Attributes and Methods

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class**.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the methods, read-only attributes, and attributes of the selected **Instance**.

## Querying a Read-Only Attribute

To query the value of a read-only attribute, you might, for example, type:

```
print MyGenerator.UUID
```

## Method/Attribute Signature Notation

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter — `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, for example `-> boolean`.

## Attributes of the Generator

The Generator provides:

- The attributes listed in the table of contents to the left.
- The **Attributes of All Objects**.

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

---

*Plant Simulation Help 11-4396 / 11-4397*
