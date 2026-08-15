# Read-Only Attributes of the AngularConverter

## Syntax Line Conventions

An example of the Syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note**
> Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

## Overview

The AngularConverter provides:

- The read-only attribute `IsUp [SimTalk] - AngularConverter`.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

To display the methods, read-only attributes, and attributes:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show them for the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```
print Source.Empty
```

## IsUp [SimTalk] - AngularConverter

Returns if a MU is located on the exit leg of the AngularConverter designated by `<Path>` after the Moving Time has elapsed and after the MU has exited while the Moving Time is still running (`true`) or not (`false`).

| Property | Value |
| --- | --- |
| Type | Read-only attribute |
| Syntax | `<Path>.IsUp → boolean` |
| Watchable | The read-only attribute is watchable. |
| Return Value | The return value has the data type boolean. |

### Example

```
print MyAngularConverter.IsUp
```
