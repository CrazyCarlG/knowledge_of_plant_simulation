# Methods of the LockoutZone

The LockoutZone provides:

- The method `addObject [SimTalk]` - LockoutZone.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the F8 key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Syntax line example

An example of the syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

## addObject [SimTalk] - LockoutZone

Adds a single object to the LockoutZone designated by `<Path>`.

- **Type:** Method
- **Syntax:**

```
<Path>.addObject(NameOfObject:path) → boolean
```

- **Parameter:** The parameter `NameOfObject` of data type `path` designates the name of the object you want to add.
- **Return Value:** The return value has the data type `boolean`.

**Example:**

```
MyLockoutZone.addObject(MyParallelStation)
```

**See also:** Objects [SimTalk] - LockoutZone, Tab Objects

## Read-Only Attributes of the LockoutZone

The LockoutZone provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it.
