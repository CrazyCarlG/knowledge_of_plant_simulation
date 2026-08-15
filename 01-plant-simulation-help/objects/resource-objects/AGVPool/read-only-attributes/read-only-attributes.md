# Read-Only Attributes of the AGVPool

The AGVPool provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyAGVPool.StatAverageTraveledDistance
```

---

## getIdleAGV [SimTalk]

Returns an AGV of the AGVPool designated by `<Path>` for which the attribute `IsIdle` has the value `true`.

### Remarks

`getIdleAGV` also sets the attribute `IsIdle` of the returned AGV to `false`. You yourself are responsible to set `IsIdle` to `true` again if the AGV is to be available again, normally when the AGV has reached the end of the route.

### Type

Method

### Syntax

```simtalk
<Path>.getIdleAGV → object
```

### Return Value

The return value has the data type `object`.

`VOID` if no idle AGV is available.

### Example

```simtalk
waituntil AGVPool.NumIdleAGVs > 0
var AGV := AGVPool.getIdleAGV
```

### See also

- IsIdle [SimTalk] - Transporter
- NumIdleAGVs [SimTalk]
- Fine-position an AGV
- Read-Only Attributes of the AGVPool

---

## NumIdleAGVs [SimTalk]

Returns the number of AGVs of the AGVPool designated by `<Path>` for which the attribute `IsIdle` returned `true`.

### Type

Read-only attribute

### Syntax

```simtalk
<Path>.NumIdleAGVs → integer
```

### Watchable

The read-only attribute is watchable.

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
waituntil AGVPool.NumIdleAGVs > 0
var AGV := AGVPool.getIdleAGV
```

### See also

- IsIdle [SimTalk] - Transporter
- getIdleAGV [SimTalk]
- Fine-position an AGV
- Video on YouTube: https://youtu.be/PYXYutlaGOs?si=G_5eRYYGFXUoUrSv&t=36

---

## StatAverageTraveledDistance [SimTalk] - AGVPool

Returns the average distance in meters which the AGVs of the AGVPool designated by `<Path>` traveled.

### Type

Read-only attribute

### Syntax

```simtalk
<Path>.StatAverageTraveledDistance → length
```

### Return Value

The return value has the data type `length`.

### Example

```simtalk
print AGVPool.StatAverageTraveledDistance
```

---

## See also

- Attributes of the AGVPool
- _Attributes of the AGVPool

The AGVPool provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

---

*Source: Plant Simulation Help (11-3457 to 11-3460), © 2026 Siemens*
