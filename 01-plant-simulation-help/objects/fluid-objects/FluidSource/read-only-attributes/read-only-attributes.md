# Read-Only Attributes of the FluidSource

## Overview

The FluidSource provides:

- The read-only attribute **StatAmount** `[SimTalk]`.
- The read-only attributes of the Fluid Objects.
- The read-only attributes of all objects.

You can query the values of read-only attributes, but you cannot set them, because Plant Simulation computes the value for the point-in-time at which you query it. In most cases, a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, on the tab **Statistics**).

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class (general description).
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the methods, read-only attributes, and attributes of the selected Instance (general description).

## Syntax conventions

An example of the syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.
- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter (`:= false` in the example above).
- If the method has a return value, the signature shows its data type after the arrow (`→ boolean` in the example above).

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

## StatAmount [SimTalk]

Returns the amount of material, i.e., the number of liters, that the FluidSource designated by `<Path>` produced.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatAmount → real`
- **Return Value:** The return value has the data type `real`.

### Example

```simtalk
print MyFluidSource.StatAmount
```

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print FluidDrain.StatMaxFlowRate
```

## See also

- Tab Statistics
- Attributes of the FluidSource
- Attributes of the Fluid Objects
- Attributes of All Objects
