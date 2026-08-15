# Read-Only Attributes of the Cycle

The Cycle provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the F8 key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Cycle.GetFirstStation
```

## GetFirstStation [SimTalk]

Returns the first station of the balanced line which the Cycle designated by `<Path>` synchronizes.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.GetFirstStation -> object
```

- **Return Value:** The return value has the data type `object`.
- **Example:**

```simtalk
print MyCycleObject.GetFirstStation
```

- **See also:** First Station

## GetLastStation [SimTalk]

Returns the last station of the balanced line which the Cycle designated by `<Path>` synchronizes.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.GetLastStation -> object
```

- **Return Value:** The return value has the data type `object`.
- **Example:**

```simtalk
print MyCycleObject.GetLastStation
```

- **See also:** Last Station
