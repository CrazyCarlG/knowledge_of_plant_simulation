# Methods of the Connector

The Connector provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. You can:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the methods, read-only attributes, and attributes of the selected Instance.

## Understanding the Syntax Line

An example of the Syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier and data type of parameters) is listed in parentheses. `(Parameter:string)` designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.
- Optional parameters are listed within brackets. `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows it after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

---

## connect [SimTalk]

Connects the specified objects within a Frame with the Connector designated by `<Connector-Path>`.

### Remarks

The method `connect` also connects any end of a TwoLaneTrack with any end of another TwoLaneTrack. To do so, pass two lanes to the method `connect`. The exit of the first lane you specify is then connected with the entrance of the second lane. The method still connects the TwoLaneTracks and not the individual lanes.

### Type

Method

### Syntax

```
<Connector-Path>.connect(StartOfConnection:any, EndOfConnectionY:any) → object
<Connector-Path>.connect(StartOfConnection:any, EndOfConnectionY:any[, SideOfConverterStart:integer, SideOfConverterEnd:integer]) → object
```

### Parameters

- **StartOfConnection** (`any`) — designates the starting point of the Connector designated by `<Connector-Path>`.
- **EndOfConnection** (`any`) — designates the end point of the connection.

You can also set an Interface object as first or as second parameter. The return value is the Connector that was just created. If Plant Simulation cannot create the Connector, it opens the Method Debugger.

- **SideOfConverterStart** (`integer`, optional) — sets at which side of the Converter the Connector is to dock: `0` = right, `1` = bottom, `2` = left, `3` = top.
- **SideOfConverterEnd** (`integer`, optional) — only required when you insert a Connector between two Converters. `SideOfConverterStart` then designates the side of the source Converter, and `SideOfConverterEnd` designates the side of the target Converter at which the Connector ends.

### Return Value

The return value has the data type `object`. It is the Connector that has been created.

### Examples

```
.Materialflow.Connector.connect(Station, Store)
.Materialflow.Connector.connect(Station, Interface3)
.Materialflow.Connector.connect(T1, T2)
// connects the exit of T1 with the entrance of T2
.Materialflow.Connector.connect(T1.A, T2.A)
// connects the exit of T1 with the entrance of T2
.Materialflow.Connector.connect(T1.A, T2.B)
// connects the exit of T1 with the exit of T2
.Materialflow.Connector.connect(T1.B, T2.A)
// connects the entrance of T1 with the entrance of T2
.MaterialFlow.Connector.connect("TwoLaneTrack1.B", "TwoLaneTrack2.A")
// connects lanes of two-laned tracks
```

---

# Read-Only Attributes of the Connector

The Connector provides:

- The read-only attributes listed in the table of contents to the left.
- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.
