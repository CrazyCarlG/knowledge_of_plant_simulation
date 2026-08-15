# Read-Only Attributes of the Marker

This directory documents the read-only attributes and the related SimTalk method available on the **Marker** object in Plant Simulation.

## Summary

The Marker provides the **Read-Only Attributes of All Objects**, plus the SimTalk method `getRouteLength`. You can query the values of read-only attributes, but you cannot set them — Plant Simulation computes each value at the point in time it is queried. In most cases a read-only attribute corresponds to a dialog item that is not editable on one of the object's tabs (for example, the Statistics tab).

## Method: `getRouteLength` [SimTalk]

Returns the route length from the Marker designated by `<Path>` to a specified destination.

- **Type:** Method
- **Syntax:**
  ```
  <Path>.getRouteLength(ToMarker:path[, byref ObjectsAlongRoute:object[],
  RouteWeightingAttribute:string]) → length
  ```

### Parameters

- `ToMarker` (`path`) — designates the destination object.
- `ObjectsAlongRoute` (optional, `object[]`) — an array into which the Marker enters the objects located along the route to the destination.
- `RouteWeightingAttribute` (optional, `string`) — the name of the Route Weighting Attribute used for automatic routing. If omitted, Plant Simulation does not weight the route lengths.

### Return Value

- Data type: `length`.
- If the destination is not reachable, Plant Simulation returns `-1`.

### Example

```
print Marker1.getRouteLength(Marker2)
```

## Attributes

The Marker provides:

- The read-only attributes listed in the documentation's table of contents.
- The **Attributes of All Objects**.

## Querying a Read-Only Attribute

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- In the Class Library: select **Show Attributes and Methods** on the context menu of the selected Class.
- In a Frame: press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which the instance was inserted.

To query the value of a read-only attribute, for example:

```
print MyMarker.UUID
```
