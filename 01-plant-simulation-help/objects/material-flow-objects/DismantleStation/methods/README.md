# DismantleStation — Methods

This folder documents the methods of the **DismantleStation** material flow object.

## Source files

- `methods.md` — markdown version of the methods documentation.
- `methods.txtx` — raw help text export of the same documentation.

## Summary

The DismantleStation provides:

- The methods listed below (also shown in the table of contents).
- The methods of the Material Flow Objects.
- The methods of All Objects.

To view all methods, read-only attributes, and attributes, open the **Show Attributes and Methods** window (`F8`, or via the context menu of the Class Library / the Home ribbon tab).

### Syntax line conventions

- `<Path>` — path of the object the method applies to.
- `(Parameter:type)` — required parameter and its data type.
- `[,Parameter:type]` — optional parameter.
- `:= default` — default value of a parameter.
- `→ type` — return value data type.

## Methods

| Method | Syntax | Description | Return |
| --- | --- | --- | --- |
| `leavingMU` | `<Path>.leavingMU(MU:integer) → object` | Returns the specified MU from the **Exiting MUs** table. | `object` |
| `leavingMUs` | `<Path>.leavingMUs([MUsTable:table]) → any` | Returns the contents of the **Exiting MUs** table; without the optional parameter, returns an array of the MUs that wanted to leave. | `any` |
| `statBlockingTimePerSuccessor` | `<Path>.statBlockingTimePerSuccessor(Successor:integer) → time` | Returns the blocking time for the specified successor from the **Blocking Times** table. | `time` |
| `statBlockingTimeTable` | `<Path>.statBlockingTimeTable(BlockingTimes:table) → boolean` | Writes the contents of the **Blocking Times** table into the given table. | `boolean` |

### Examples

```simtalk
for var i := 1 to MyDismantleStation.NumLeavingMU
   print MyDismantleStation.leavingMU(i)
next

MyDismantleStation.leavingMUs(myEvalTable)
MyDismantleStation.leavingMUs

for var i := 1 to MyDismantleStation.NumSucc
    print MyDismantleStation.statBlockingTimePerSuccessor(i)
next

var myBlockingTimesTable: table
MyDismantleStation.statBlockingTimeTable(myBlockingTimesTable)
```

## Related

- **Read-Only Attributes of the DismantleStation** — query-only values; see `../read-only-attributes`.
- **Tab Statistics [DismantleStation]** — dialog tab related to `statBlockingTimePerSuccessor` / `statBlockingTimeTable`.
- **Exiting MUs** — table referenced by `leavingMU` / `leavingMUs`.
