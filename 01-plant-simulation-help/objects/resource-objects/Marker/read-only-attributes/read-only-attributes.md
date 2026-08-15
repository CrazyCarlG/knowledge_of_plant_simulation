# Read-Only Attributes of the Marker

## getRouteLength [SimTalk] - Marker

Returns the route length of the Marker designated by `<Path>` to the specified destination.

**Type:** Method

**Syntax:**

```
<Path>.getRouteLength(ToMarker:path[, byref ObjectsAlongRoute:object[],
RouteWeightingAttribute:string]) → length
```

### Parameters

You can specify the following parameters:

- The parameter `ToMarker` of data type `path` designates the destination object.
- The optional parameter `ObjectsAlongRoute` designates an array of data type `object` into which the Marker enters the objects along the route to the destination.
- The optional parameter `RouteWeightingAttribute` of data type `string` designates the name of the Route Weighting Attribute for automatic routing. If the parameter is not passed, Plant Simulation does not weight the lengths of the routes.

### Return Value

The return value has the data type `length`.

If the destination is not reachable, Plant Simulation returns the value `-1`.

### Example

```
print Marker1.getRouteLength(Marker2)
```

## Overview

The Marker provides the **Read-Only Attributes of All Objects**.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```
print MyMarker.UUID
```

## Attributes of the Marker

The Marker provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.
