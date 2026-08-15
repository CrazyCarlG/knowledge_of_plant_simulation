# Methods of the Workplace

The Workplace provides:

- The methods listed in the table of contents.
- The Methods of All Objects.
- The Methods of the Material Flow Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which an instance was inserted to show the methods, read-only attributes, and attributes of the selected Instance.

## Syntax Line

An example of the syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. `(Parameter:string)`, for example, designates a parameter of data type string.
- Optional parameters are listed within brackets. `[,Parameter:boolean]`, for example, means that the boolean parameter may be omitted.
- If a parameter has a default value, the signature shows the default value after the parameter (`:= false` in the example above).
- If the method has a return value, the signature shows its data type after the arrow (`→ boolean` in the example above).

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

## contentsList [SimTalk] — Workplace

Returns an array containing the entire contents, i.e., all Workers located in the Contents List of the Workplace designated by `<Path>`.

**Syntax**

```
<Path>.contentsList([ContentsList:table]) → any
```

**Parameter**

The optional parameter `ContentsList` of data type `table` designates the name of the table (a DataTable or a local variable) into which the method writes the values. Plant Simulation automatically generates the format of this table, and deletes any existing format and contents of the table.

**Return Value**

The return value has the data type `any`.

**Example**

```js
Workplace2.contentsList(MyContentsList)
print Workplace2.contentsList
```

**See also**

- Contents [material flow objects]
- Contents [Workplace]

## getRouteCoordinates [SimTalk]

Returns the 3D-coordinates of the waypoints of the route which a Worker would have to cover to get from the Workplace designated by `<Path>` to another Workplace or to the WorkerPool.

**Type**

Method

**Syntax**

```
<Path>.getRouteCoordinates(ToWorkplace:path[, 
FreelyWithinArea:boolean:=false]) → array
```

**Parameters**

- `ToWorkplace` (data type `path`) designates the Workplace which is the destination Workplace of the route.
- `FreelyWithinArea` (data type `boolean`, optional) sets if the Worker gets to the Workplace by walking freely within the area or not.
  - Specify `false` (or omit the parameter) to compute the waypoints of the route between the two Workplaces via Footpaths which are connected with Connectors.
  - Specify `true` to compute the waypoints of the route in the area (the route the Worker, walking freely within the area, would take).

**Default Value of the Parameter**

`false`

**Return Value**

The return value is a two-dimensional array. It contains the X-Coordinate, the Y-Coordinate, and the Z-Coordinate of the waypoints.

**Example**

```js
var coords:any := Workplace1.getRouteCoordinates(Workplace2)
print coords // outputs [[6.59, -6.0, 0.0] [6.60, -7.40, 0.0] [9.40, -7.40, 
0.0] [13.690, -6.0, 0.0]]
```

## getRouteLength [SimTalk] — Workplace

Returns the length of the route which a Worker would have to cover to get from the Workplace designated by `<Path>` to another Workplace or to the WorkerPool.

**Type**

Method

**Syntax**

```
<Path>.getRouteLength(ToWorkplace:path[, FreelyWithinArea:boolean:=false]) 
→ length
```

**Parameters**

- `ToWorkplace` (data type `path`) designates the Workplace which is the destination Workplace.
- `FreelyWithinArea` (data type `boolean`, optional) sets if the Worker gets to the Workplace by walking freely within the area or not.
  - Accept the default value `false` (or omit the parameter) to compute the route length between the two Workplaces via Footpaths which are connected with Connectors.
  - Specify `true` to compute the route length in the area (the route the Worker, walking freely within the area, would take).

**Default Value of the Parameter**

`false`

**Return Value**

The return value has the data type `length`. It is `-1` if Plant Simulation did not find a route.

**Example**

```js
var len:length := Workplace1.getRouteLength(Workplace2)
```

## Read-Only Attributes of the Workplace

The Workplace provides the Read-Only Attributes of All Objects.
