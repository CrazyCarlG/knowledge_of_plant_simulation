# Read-Only Attributes of the Chart

The Chart provides the _Read-Only Attributes of All Objects. You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value at the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs, for example on the tab Statistics.

## update [SimTalk] - Chart

Refreshes the displayed Chart designated by `<Path>` with the current values.

### Remarks

If the Chart is a Plotter in Sample mode, the method `update` has an additional effect: a new data point is set, i.e., the Chart samples one more time — even when the Chart is closed and the method returns `false` for this reason.

### Type

Method

### Syntax

```
<Path>.update -> boolean
```

### Return Value

The return value has the data type `boolean`:

- `true` if the Chart is open.
- `false` if it is closed.

### Example

```
MyChart.update
```

### See also

- Mode [drop-down list] - Chart
- Read-Only Attributes of the Chart

## Querying a read-only attribute

To query the value of a read-only attribute, you might, for example, type:

```
print MyChart.UUID
```

## Attributes of the Chart

The Chart provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

## Viewing methods, read-only attributes, and attributes

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].
