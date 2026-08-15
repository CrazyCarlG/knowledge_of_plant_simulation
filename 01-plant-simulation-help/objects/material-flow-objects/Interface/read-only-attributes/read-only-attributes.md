# Read-Only Attributes of the Interface

## Method syntax conventions

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. For example, `(Parameter:string)` designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. For example, `[,Parameter:boolean]` means that you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, for example `:= false`.
- If the method has a return value, the signature shows its data type after the arrow `->`, for example `→ boolean`.

## Overview

The Interface provides:

- The read-only attributes listed in the table of contents.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the F8 key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print .Models.Model.MyFrame.Interface.IsEntry
```

## IsEntry [SimTalk]

Returns if the Interface designated by `<Path>` is of type Entrance (`true`) or not (`false`).

### Remarks

The Interface has to be connected with a Connector.

### Type

Read-only attribute

### Syntax

```simtalk
<Path>.IsEntry → boolean
```

### Return Value

The return value has the data type boolean.

### Example

```simtalk
print .Models.Model.Frame.Interface.IsEntry
```

### See also

- Type [Interface]
- IsExit [SimTalk]

## IsExit [SimTalk]

Returns if the Interface designated by `<Path>` is of type Exit (`true`) or not (`false`).

### Remarks

The Interface has to be connected with a Connector.

### Type

Read-only attribute

### Syntax

```simtalk
<Path>.IsExit → boolean
```

### Return Value

The return value has the data type boolean.

### Example

```simtalk
print .Models.Model.Frame.interface.IsExit
```

### See also

- IsEntry [SimTalk]
- Type [Interface]
- Attributes of the Interface

## See also

- _Read-Only Attributes of the Interface
- _Attributes of the Interface
