# Read-Only Attributes of the Store — Summary

This README summarizes the content of `read-only-attributes.md` in this directory. It covers the read-only attributes of the **Store** material flow object in Plant Simulation.

## Overview

Read-only attributes of Material Flow Objects can be **queried** but not **set**. Plant Simulation computes their value at the point in time they are queried. In most cases, a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the members of the selected **Class**.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing the instance, to show the members of the selected **Instance**.

## Read-Only Attributes

### Capacity
- **Type:** Read-only attribute (watchable)
- **Syntax:** `<Path>.Capacity → integer`
- **Description:** Returns the capacity of the Store designated by `<Path>`.
- **Remarks:** Capacity is the product of `XDim × YDim × ZDim`.
- **Return value:** `integer`

```simtalk
if MyStore.Capacity <= lotsize
   @.move(MyStore)
end
```

### XDim / YDim / ZDim
- Read-only attributes that give the store's dimensions in each axis.
- Cross-referenced with the X-Dimension, Y-Dimension, and Z-Dimension properties, and with **Capacity**.

### Stock.MyPartName
- **Type:** Read-only attribute
- **Syntax:** `<Path>.Stock.MyPartName → integer`
- **Description:** Returns the current stock of the parts designated by `MyPartName` in the Store designated by `<Path>`.
- **Remarks:** `MyPartName` is the name of the respective part, set in the **Configuration Table** of the Store.
- **Return value:** `integer`

```simtalk
print MyStore.Stock.PartRed
// might, for example, return 1
```

## Attributes of the Store

The Store provides:
- The attributes listed in the table of contents.
- The **Attributes of All Objects**.
- The **Attributes of the Material Flow Objects**.

## Example Query

```simtalk
print Store.Capacity
```
