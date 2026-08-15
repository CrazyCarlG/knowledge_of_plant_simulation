# Methods of the Buffer

## Overview

The Buffer provides:

- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The help uses the object *Station* as an illustrative example.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class (general description).
- Press the **F8** key, or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the methods, read-only attributes, and attributes of the selected Instance (general description).

## Syntax of Methods

An example of the syntax line of an individual method might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. For example, `(Parameter:string)` designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. For example, `[,Parameter:boolean]` means that you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, e.g. `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `→`, e.g. `→ boolean` in the example above.

## Read-Only Attributes of the Buffer

The Buffer provides:

- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.
