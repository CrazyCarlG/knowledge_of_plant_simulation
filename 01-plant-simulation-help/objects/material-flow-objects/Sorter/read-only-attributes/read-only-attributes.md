# Read-Only Attributes of the Material Flow Objects

Read-only attributes can be queried but not set, since Plant Simulation computes their value for the point in time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show the methods, read-only attributes, and attributes of the selected Class.
- Press **F8**, or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show them for the selected Instance.

To query the value of a read-only attribute, for example:

```simtalk
print Store.Capacity
```

## Read-Only Attributes of the Store

### Capacity

Returns the capacity of the Store designated by `<Path>`.

**Remarks:** The Capacity is the product of `XDim × YDim × ZDim`.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.Capacity → integer
```

**Watchable:** The read-only attribute is watchable.

**Return Value:** The return value has the data type `integer`.

**Example:**

```simtalk
if MyStore.Capacity <= lotsize
   @.move(MyStore)
end
```

**See also:** XDim, YDim, ZDim, X-Dimension, Y-Dimension, Z-Dimension

### XDim / YDim / ZDim

Read-only attributes of the Store corresponding to the X-, Y-, and Z-Dimension dialog items.

**See also:** Capacity

### Stock.MyPartName

Returns the current stock of the parts designated by `MyPartName` in the Store designated by `<Path>`.

**Remarks:** `MyPartName` is the name of the respective part, which you set in the Configuration Table of the Store.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.Stock.MyPartName → integer
```

**Return Value:** The return value has the data type `integer`.

**Example:**

```simtalk
print MyStore.Stock.PartRed
// might, for example, return 1
```

**See also:** Configuration (button), Attributes of the Store

## Attributes of the Store

The Store provides:

- The attributes listed in the table of contents.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window.

---
*Source: Plant Simulation Help*
