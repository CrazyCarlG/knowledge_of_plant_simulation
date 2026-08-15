# Read-Only Attributes of the Conveyor

## Syntax Line Conventions

An example of the Syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

## Overview

The Conveyor provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```
print Conveyor.CurrentAcceleration
```

## Read-Only Attributes

### CurrentAcceleration

Returns the actual acceleration or deceleration of the Conveyor designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```
<Path>.CurrentAcceleration → acceleration
```

- **Watchable:** The read-only attribute is watchable for special values. By observing this value, you might, for example, detect the event when the Conveyor has reached its Final Speed.
- **Return Value:** The return value has the data type `acceleration`.

**Example**

```
MyConveyor.CurrentAcceleration
```

### OccupiedLength

Returns the section of the entire Length of the Conveyor designated by `<Path>`, which is occupied by all MUs located on it.

- **Remarks:** Each MU located on the Conveyor occupies part of the entire available length.
- **Type:** Read-only attribute
- **Syntax:**

```
<Path>.OccupiedLength → length
```

- **Return Value:** The return value has the data type `length`.

**Example**

```
print Conveyor.OccupiedLength
```

**See also**

- Length [text box] - Conveyor

## Related

- Attributes of the Conveyor
- _Attributes of the Conveyor

The Conveyor provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.
