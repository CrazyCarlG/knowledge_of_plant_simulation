# Methods of the Button

The Button provides the **Methods of All Objects**.

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window (the figure in the source illustrates this using the object *Station*).

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class** (general description).
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the methods, read-only attributes, and attributes of the selected **Instance** (general description).

## Syntax line example

An example of the syntax line of an individual method might look like this:

```text
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The **signature** of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter — `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->` — `→ boolean` in the example above.

## Read-Only Attributes of the Button

The Button provides the **_Read-Only Attributes of All Objects**.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, on the tab **Statistics**).

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class** (general description).
