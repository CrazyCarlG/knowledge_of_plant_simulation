# Interface Attributes

The Interface provides:

- The attributes listed below.
- The [Attributes of All Objects].

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show them for the selected Instance.

You can set and get an attribute's value either through check boxes, text boxes, and drop-down lists in dialog windows, or by assigning values directly:

```simtalk
Interface1.Position := 53
print Interface1.Position
posit := MyStation.Cont.XPos
```

## IsExit [SimTalk]

Returns whether the Interface designated by `<Path>` is of type Exit (`true`) or not (`false`).

**Remarks:** The Interface has to be connected with a Connector.

**Type:** Read-only attribute

**Syntax**

```simtalk
<Path>.IsExit → boolean
```

**Return Value:** The return value has the data type `boolean`.

**Example**

```simtalk
print .Models.Model.Frame.interface.IsExit
```

## MaxConnections [SimTalk] - Interface

Sets the Maximum Number of External Connections of the Interface designated by `<Path>`.

**Type:** Attribute

**Syntax**

```simtalk
<Path>.MaxConnections:integer
```

**Assignment Value:** You can assign a value of data type `integer`. Specify `-1` for an infinite number of connections.

**Example**

```simtalk
Interface1.MaxConnections := 2
```

## Position [SimTalk] - Interface

Sets the Position in % of the Interface designated by `<Path>` at which an incoming or outgoing Connector is shown at the icon of the Frame.

**Remarks:** Plant Simulation uses this value when you activate **File > Preferences > General > Connect Objects Automatically**. Connecting objects automatically only works when the exit of FrameA and the entrance of FrameB are not more than three pixels apart.

**Type:** Attribute

**Syntax**

```simtalk
<Path>.Position:integer
```

**Assignment Value:** You can assign a value of data type `integer` between 0 and 100 percent. Position 0 is the top or left-hand side of the Frame icon; position 100 is the bottom or right-hand side.

**Example**

```simtalk
interface.Position := 53
```

## Side [SimTalk]

Sets the Side of the Frame on which the Interface designated by `<Path>` is located.

**Type:** Attribute

**Syntax**

```simtalk
<Path>.Side:string
```

**Assignment Value:** You can assign a value of data type `string`. Possible values are `"Top"`, `"Right"`, `"Bottom"`, `"Left"`, or `"Angle-dependent"`. `"Angle-dependent"` takes the angle between the objects into account when determining the starting point or the end point of the Connector.

**Example**

```simtalk
interface.Side := "right"
```
