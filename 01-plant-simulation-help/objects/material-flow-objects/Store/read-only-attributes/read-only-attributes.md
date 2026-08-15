# Read-Only Attributes of the Store

## Overview

Read-only attributes of the Material Flow Objects can be **queried** but not **set** — Plant Simulation computes their value at the point-in-time you query them. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the members of the selected **Class**.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which an instance was inserted, to show the members of the selected **Instance**.

To query the value of a read-only attribute, for example:

```simtalk
print Store.Capacity
```

---

## Capacity [SimTalk] - Store

Returns the capacity of the Store designated by `<Path>`.

**Remarks:** The Capacity is the product of `XDim` times `YDim` times `ZDim`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.Capacity → integer`
- **Watchable:** The read-only attribute is watchable.
- **Return Value:** The return value has the data type `integer`.

**Example:**

```simtalk
if MyStore.Capacity <= lotsize 
   @.move(MyStore)
end
```

---

## XDim / YDim / ZDim [SimTalk] - Store

- **See also:**
  - X-Dimension [Store]
  - Y-Dimension [Store]
  - Z-Dimension [Store]
  - Capacity [SimTalk] - Store

---

## Stock.MyPartName [SimTalk]

Returns the current stock of the parts designated by `MyPartName` in the Store designated by `<Path>`.

**Remarks:** `MyPartName` is the name of the respective part, which you set in the **Configuration Table** of the Store.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.Stock.MyPartName → integer`
- **Return Value:** The return value has the data type `integer`.

**Example:**

```simtalk
print MyStore.Stock.PartRed
// might, for example, return 1
```

**See also:**
- Configuration [button]
- Attributes of the Store

---

## Attributes of the Store

The Store provides:

- The attributes listed in the table of contents.
- The **Attributes of All Objects**.
- The **Attributes of the Material Flow Objects**.

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window.
