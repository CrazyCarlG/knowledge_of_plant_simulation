# Store — Attributes (Summary)

This README summarizes the SimTalk attributes of the **Store** material flow object, as documented in [`attributes.md`](attributes.md).

## Overview

The Store exposes:
- The attributes listed below.
- The *Attributes of All Objects*.
- The *Attributes of the Material Flow Objects*.

Attribute values can be set or read either through dialog controls (check boxes, text boxes, drop-down lists) or in SimTalk:

```simtalk
MyStore.YDim := 10   // set
print MyStore.YDim   // get
```

## Attribute Summary

| Attribute | Type | Syntax | Description |
|-----------|------|--------|-------------|
| `Stock.MyPartName` | Read-only | `<Path>.Stock.MyPartName → integer` | Current stock of the parts designated by `MyPartName` (set in the Store's Configuration Table). |
| `FillWholeLayer` | Attribute | `<Path>.FillWholeLayer:boolean` | If `true`, always fills an entire layer when Z-Dimension > 1. |
| `Supermarket` | Attribute | `<Path>.Supermarket:boolean` | If `true`, the Store works as a supermarket. |
| `XDim` | Attribute (watchable) | `<Path>.XDim:integer` | Number of storage places on the x-axis. |
| `YDim` | Attribute (watchable) | `<Path>.YDim:integer` | Number of storage places on the y-axis. |
| `ZDim` | Attribute (watchable) | `<Path>.ZDim:integer` | Number of storage places on the z-axis; permits stacking parts. |

### Key Remarks

- **Capacity** equals the product `XDim × YDim × ZDim` (greatest allowed value: ten million).
- **Decreasing dimensions:** ensure no MUs remain on storage places that would be deleted — delete or move them first.
- **`FillWholeLayer`:** Plant Simulation starts a new layer before stacking parts on the layer below.
- **`Stock.MyPartName`:** `MyPartName` must match a part name set in the Store's Configuration Table.

## Examples

```simtalk
// Stock (read-only)
print MyStore.Stock.PartRed
// might, for example, return 1

// Dimensions
MyStore.XDim := 10
MyStore.YDim := 10
MyStore.ZDim := 4

// FillWholeLayer
MyStore.FillWholeLayer := true

// Supermarket
MyStore.Supermarket := true

// Enumerate all MUs on place (1,1)
var place := Store[1,1]
for var i := 1 to place.NumMU
   print place.MU(i)
next

// Topmost MU of the stack
Store[1,1].Cont

// Second MU from the top on place (1,2)
Store[1,2].MU(2)
```

## Related Object: PlaceBuffer

The **PlaceBuffer** processes parts across buffer places arranged in a row. MUs advance place-by-place and can only leave after passing the last place, allowing each place to be accessed individually. It is not part of the default Toolbox objects.
