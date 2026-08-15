# Methods of the Object Cycle

The object **Cycle** provides:

- The method `setFirstAndLastStation` [SimTalk].
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

## Viewing Methods, Read-Only Attributes, and Attributes

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class**.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected **Instance**.

## Understanding the Syntax Line

An example of the Syntax line of the individual methods might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note**
> Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

---

## setFirstAndLastStation [SimTalk]

Sets the **First Station** and the **Last Station** of the balanced line which the Cycle station designated by `<Path>` synchronizes.

### Remarks

All stations between these stations, which are connected with Connectors, form the balanced line.

### Type

Method

### Syntax

```
<Path>.setFirstAndLastStation(FirstStation:path, LastStation:path) → boolean
```

### Parameters

You can specify the following parameters:

- The parameter `FirstStation` of data type `object/path` designates the First Station.
- The parameter `LastStation` of data type `object/path` designates the Last Station.

### Return Value

The return value has the data type `boolean`.

### Example

```simtalk
MyCycleObject.setFirstAndLastStation(MyStation1, MyStation4)
```

### Related Methods

- `GetFirstStation` [SimTalk]
- `GetLastStation` [SimTalk]
- `setFirstAndLastStation` [SimTalk]

---

## Read-Only Attributes of the Cycle

The **Cycle** provides:

- The read-only attributes listed in the table of contents.
- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Cycle.GetFirstStation
```

> Source: Plant Simulation Help
> Unpublished work. © 2026 Siemens
