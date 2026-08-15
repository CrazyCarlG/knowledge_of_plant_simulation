# Read-Only Attributes of the Converter

The Converter provides:

- The read-only attributes listed below.
- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, because Plant Simulation computes the value for the point in time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the **Statistics** tab.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Converter.GetCurrentExit
```

## GetCurrentExit

Returns the number of the side at which the MU exits the Converter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.GetCurrentExit → integer`
- **Return value:** integer

The figures in the help illustrate the sides depending on the direction in which you inserted the Converter into your simulation model. The numbers designate the side of the Converter at which the MU exits.

**Example**

```simtalk
No := ?.GetCurrentExit
```

## GetNextEntranceNumber

Returns the number of the side at which the next MU can enter the Converter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.GetNextEntranceNumber → integer`
- **Return value:** integer

The figures in the help illustrate the sides depending on the direction in which you inserted the Converter into your simulation model.

**Example**

```simtalk
No := ?.GetNextEntranceNumber
```

## IsUp

Returns whether the Converter designated by `<Path>` is in the up position (`true`) or in the down position (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.IsUp → boolean`
- **Return value:** boolean

**Example**

```simtalk
PosUpDown := MyConverter.IsUp
```

You can also use the attribute `IsUp` to start the lifting process.

**Example**

```simtalk
MyConverter.IsUp := true
```

## StatMovingEmptyPortion

Returns the portion of the statistics collection period during which the Converter designated by `<Path>` was raising or lowering itself and was not conveying a MU.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatMovingEmptyPortion → real`
- **Return value:** real

**Example**

```simtalk
print Converter.StatMovingEmptyPortion
```

**See also:** Tab Statistics [Converter], Moving Time [statistics report]

## StatMovingEmptyTime

Returns the total time during which the Converter designated by `<Path>` was raising or lowering itself and was not conveying a MU.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatMovingEmptyTime → time`
- **Return value:** time

**Example**

```simtalk
print Converter.StatMovingEmptyTime
```

**See also:** Moving Time [statistics report]

## StatMovingLoadedPortion

Returns the portion of the statistics collection period during which the Converter designated by `<Path>` was raising or lowering itself and was conveying a MU.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatMovingLoadedPortion → real`
- **Return value:** real

**Example**

```simtalk
print Converter.StatMovingLoadedPortion
```

**See also:** Tab Statistics [Converter], Moving Time [statistics report]

## StatMovingLoadedTime

Returns the total time during which the Converter designated by `<Path>` was raising or lowering itself and was conveying a MU.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatMovingLoadedTime → time`
- **Return value:** time

**Example**

```simtalk
print Converter.StatMovingLoadedTime
```

**See also:** Moving Time [statistics report]

## Related

The table of contents also references the following related topics:

- `setAttributeList(AttributeList:table)` — copies the contents of the passed list to the target list of the Converter.

  **Example**

  ```simtalk
  Converter.setAttributeList(MyAttributes)
  ```

- `getAttributeList` — see "getAttributeList [SimTalk] - Converter".
- Open List [button] - Converter
- Data Held in Tabular Form in Attributes [material flow objects]
- Strategy [drop-down list] - Converter
- Attributes of the Converter
