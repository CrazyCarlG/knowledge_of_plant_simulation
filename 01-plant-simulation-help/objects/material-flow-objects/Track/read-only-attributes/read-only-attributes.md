# Read-Only Attributes of the Track

The Track provides the following read-only attributes:

- The read-only attribute `OccupiedLength [SimTalk] - Track`.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

## Viewing Attributes and Methods

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Store.Capacity
```

---

## OccupiedLength [SimTalk] - Track

Returns the part of the entire Length of the Track designated by `<Path>`, which is occupied by all Transporters located on it.

### Remarks

Each Transporter located on the Track occupies part of the entire length available.

### Type

Read-only attribute

### Syntax

```
<Path>.OccupiedLength → length
```

### Return Value

The return value has the data type `length`.

### Example

```simtalk
print MyTrack.OccupiedLength
```

### See also

- Length [text box] - Track
- Attributes of the Track
