# Methods of the Display

The Display provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

## Syntax line

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

## Methods

### resetMinMax [SimTalk]

Deletes the minimum and maximum values that the Display designated by `<Path>` shows and sets them back to their default values.

**Type:** Method

**Syntax:**

```
<Path>.resetMinMax
```

**Example:**

```
print MyDisplay.resetMinMax
```

**See also:** Reset Values [button]

### update [SimTalk] - Display

Updates the value that the Display designated by `<Path>` shows after a certain time has elapsed.

**Remarks**

`update` is only useful in conjunction with Sample mode. You can use the method `update` to force the Display to display a current value, for example after you changed the input value.

To be compatible with previous versions of Plant Simulation, you can specify the parameter Time of data type time.

**Type:** Method

**Syntax:**

```
<Path>.update
```

**Example:**

```
MyDisplay.update
```

**See also:** Interval [text box] - Display

## Read-Only Attributes of the Display

The Display provides:

- The read-only attributes listed in the table of contents to the left.
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.
