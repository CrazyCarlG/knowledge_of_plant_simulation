# Methods of the Marker

The Marker provides the **Methods of All Objects**.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the **Home** ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Syntax conventions

An example of the syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The method signature (identifier and data type of parameters) is listed in parentheses. `(Parameter:string)` designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter (`:= false` in the example above).
- If the method has a return value, the signature shows its data type after the arrow (`→ boolean` in the example above).

---

## getRouteLength [SimTalk] — Marker

Returns the route length of the Marker designated by `<Path>` to the specified destination.

### Type

Method

### Syntax

```
<Path>.getRouteLength(ToMarker:path[, byref ObjectsAlongRoute:object[],
RouteWeightingAttribute:string]) → length
```

### Parameters

- **`ToMarker`** (`path`) — designates the destination object.
- **`ObjectsAlongRoute`** (optional, `object[]`) — an array of data type `object` into which the Marker enters the objects along the route to the destination.
- **`RouteWeightingAttribute`** (optional, `string`) — the name of the Route Weighting Attribute for automatic routing. If the parameter is not passed, Plant Simulation does not weight the lengths of the routes.

### Return Value

The return value has the data type `length`.

If the destination is not reachable, Plant Simulation returns the value `-1`.

### Example

```simtalk
print Marker1.getRouteLength(Marker2)
```

---

# Read-Only Attributes of the Marker

The Marker provides the **Read-Only Attributes of All Objects**.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, the **Statistics** tab).
