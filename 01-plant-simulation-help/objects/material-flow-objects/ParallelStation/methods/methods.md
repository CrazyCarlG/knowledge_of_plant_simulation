# Methods — ParallelStation

## `findPart [SimTalk]`

Finds the part with the specified name on the ParallelStation designated by `<Path>` and returns it.

- **Type:** Method
- **Syntax:** `<Path>.findPart(PartType:string) → object`
- **Parameter:** `PartType` (data type `string`) designates the part type.
- **Return Value:** data type `object`

```simtalk
var o: object := MyParallelStation.findPart("Container")
// assigns for example .MUs.Container:1
```

---

## `pe, [X,Y] [SimTalk]`

Sets the designated processing place on the production element (PE) of the ParallelStation designated by `<Path>`.

### Remarks
- Instead of `pe([X,Y])` you can also use `[X,Y]`.
- To access the MU that is located on that place, append `.Cont`.

- **Type:** Method
- **Syntax:**
  ```
  <Path>.pe([X:integer,Y:integer]) → any
  <Path>[X:integer,Y:integer] → any
  ```

### Parameters
- `X` (optional, data type `integer`) — the X-Dimension of the processing place.
- `Y` (optional, data type `integer`) — the Y-Dimension.

If you do not specify the parameters, Plant Simulation returns the first free PE or the PE on the place `(1,1)` if no free PE is available.

- **Return Value:** data type `any`

```simtalk
@.move(ParallelStation[2,3])
@.move(ParallelStation.pe(2,3))
print ParallelStation[2,3].Cont.name
```

**See also:** X-Dimension [ParallelStation]

---

## Read-Only Attributes of the ParallelStation

The ParallelStation provides:

- The read-only attribute `Capacity [SimTalk] - ParallelStation`.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class**.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected **Instance**.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print ParallelStation.Capacity
```
