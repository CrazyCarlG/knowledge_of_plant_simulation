# Attributes of the Buffer

## Viewing Attributes and Methods

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute:

```simtalk
print MyBuffer.NumChildren
```

The Buffer provides:

- The attributes listed in the table of contents.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

## Setting and Getting Attribute Values

You can set the value of an attribute and you can get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

To set the value of an attribute:

```simtalk
Buffer.BufferType := "Queue"
```

To get the value of an attribute:

```simtalk
print Buffer.BufferType
posit := MyStation.Cont.XPos
```

---

## BufferType

Sets the Buffer Type of the Buffer designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.BufferType:string`
- **Assignment Value:** You can assign a value of data type `string`:
  - Specify `"Queue"` to make the parts exit the Buffer in the same order in which they entered it (First In First Out).
  - Specify `"Stack"` to make the part which entered last leave the Buffer first (Last In First Out).

Example:

```simtalk
Buffer.BufferType := "Queue"
```

See also: Buffer Type (drop-down list).

---

## Capacity

Sets the Capacity, i.e., the maximum number of MUs that can be located in the Buffer designated by `<Path>`.

**Remarks:** As the Capacity is not implemented in a matrix, you cannot access any individual place. You can only reduce the Capacity when the new capacity you enter is greater than or equal to the actual number of MUs located in the Buffer.

- **Type:** Attribute
- **Syntax:** `<Path>.Capacity:integer`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type `integer`. The value `-1` designates an infinite capacity.

Example:

```simtalk
Buffer.Capacity := 12
```

See also: Capacity (text box) - Buffer, Sorter.

---

## Sorter

Use the object **Sorter** for sorting parts according to different sort criteria.

The MUs exit the Sorter according to the priorities you set. The Sorter moves the part with the highest priority first, regardless of the time at which it entered. You can define the priority of the part with the Sort Criterion and the Sort Order. The data type of the sort criterion must be `real` or convertible to `real`.

The sort criterion can be:

- Occupation time
- MU-Property
- Method

Sort order:

- **Descending** sort order: the Sorter moves the part with the highest value (with respect to the sort criterion) first.
- **Ascending** sort order: the Sorter moves the part with the lowest value first.

The Sorter sorts the MUs again when:

- Another MU enters.
- Its contents change because you access it.

If you want to sort the MUs located on the Sorter only when a MU enters, Plant Simulation assumes that the sort criterion does not change during the time the MUs stay on the Sorter. In this case, Plant Simulation adds new MUs to the existing order of MUs located on it.

If the value of the sort criterion depends on the time (for example, the battery charge of a Transporter), Plant Simulation sorts the MUs every time the contents changes, especially before a MU moves.

If a MU does not have a sort criterion, or its data type cannot be converted to `real`, the MU sequence on the object is undefined. If there are several MUs with the same value for the sort criterion, the order of these MUs with respect to each other is not defined.

Alternative graphics for the Sorter are available: click **Exchange Graphics** in the 3D window of the Sorter and select an alternative graphic.
