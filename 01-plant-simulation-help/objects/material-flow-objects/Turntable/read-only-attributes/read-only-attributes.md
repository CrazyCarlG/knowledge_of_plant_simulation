# Read-Only Attributes of the Turntable

The Turntable provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Turntable.StatRotationEmptyPortion
```

## stopMU [SimTalk]

Stops the MU while the Turntable designated by `<Path>` is still rotating.

### Remarks

When the rotation is finished, the MU automatically moves again.

Use `stopMU` to stop the MU before it reaches the end of the table to prevent collisions for example. You will mostly use `stopMU` in a sensor control.

### Type

Method

### Syntax

```
<Path>.stopMU
```

### Example

```simtalk
MyTurntable.stopMU
```

## CurrentAngle [SimTalk]

Returns the current angle of the Turntable designated by `<Path>`.

### Type

Read-only attribute

### Syntax

```
<Path>.CurrentAngle → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print MyTurntable.CurrentAngle // might return 45 for example
```

## CurrentDestinationAngle [SimTalk]

Returns the destination angle to which the Turntable designated by `<Path>` rotates at the moment.

### Type

Read-only attribute

### Syntax

```
<Path>.CurrentDestinationAngle → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print MyTurntable.CurrentDestinationAngle // might return 74.36 for example
```

## StatRotationEmptyPortion [SimTalk] - Turntable

Returns the portion of the statistics collection period during which the Turntable designated by `<Path>` was rotating empty without a MU being located on the table.

### Type

Read-only attribute

### Syntax

```
<Path>.StatRotationEmptyPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print MyTurntable.StatRotationEmptyPortion
```

### See also

- Tab Statistics [Turnplate]
- Statistics report, Rotation Time
- Empty [state, material flow objects]

## StatRotationEmptyTime [SimTalk] - Turntable

Returns the total time during which the Turntable designated by `<Path>` was rotating empty, i.e., without a MU being located on the table.

### Type

Read-only Attribute

### Syntax

```
<Path>.StatRotationEmptyTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print MyTurntable.StatRotationEmptyTime
```

### See also

- Statistics report, Rotation Time
- Empty [state, material flow objects]

## StatRotationLoadedPortion [SimTalk] - Turntable

Returns the portion of the statistics collection period during which the Turntable designated by `<Path>` was rotating with a MU being located on the table.

### Type

Read-only attribute

### Syntax

```
<Path>.StatRotationEmptyPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print MyTurntable.StatRotationEmptyPortion
```

### See also

- Tab Statistics [Turnplate]
- Statistics report, Rotation Time

## StatRotationLoadedTime [SimTalk] - Turntable

Returns the total time during which the Turntable designated by `<Path>` was rotating with a MU being located on the table.

### Type

Read-only attribute

### Syntax

```
<Path>.StatRotationLoadedTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print MyTurntable.StatRotationLoadedTime
```

### See also

- Statistics report, Rotation Time
