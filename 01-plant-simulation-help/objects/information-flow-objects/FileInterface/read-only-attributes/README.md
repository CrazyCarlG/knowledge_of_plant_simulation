# Read-Only Attributes of the FileInterface

This directory documents the **read-only attributes** of the Plant Simulation **FileInterface** object. The source content is provided in two equivalent forms:

- `read-only-attributes.md` — Markdown version.
- `read-only-attributes.txtx` — raw text export of the Plant Simulation Help page.

> There are no subfolders in this directory, so no additional `README.md` files exist to merge.

## Summary

The FileInterface provides two kinds of read-only attributes:

1. The object-specific read-only attributes listed below.
2. The read-only attributes common to all objects.

Read-only attributes can be **queried but not set**: Plant Simulation computes their value at the moment the query is made. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

To inspect all methods, read-only attributes, and attributes of an object, open **Show Attributes and Methods**:

- On the Class Library context menu (for a selected Class).
- By pressing **F8** or clicking **Show Attributes and Methods** on the Home ribbon tab of the Frame containing an instance (for a selected Instance).

A value can be queried with SimTalk, for example:

```simtalk
print MyFileInterface.IsOpen
```

## Read-Only Attributes

| Attribute | Description | Syntax | Return Type |
|-----------|-------------|--------|-------------|
| `EoF` | Returns `true` when the file designated by `<Path>` is still closed (no data available for processing). After opening with `open`, returns `false` as long as lines can still be read with `readLn`. | `<Path>.EoF → boolean` | `boolean` |
| `IsOpen` | Returns whether the file designated by `<Path>` is open (`true`) or not (`false`). | `<Path>.IsOpen → boolean` | `boolean` |

### EoF [SimTalk]

`EoF` (end of file) reports whether the file is closed/no data is available.

Example:

```simtalk
MyFileInterface.open
while not MyFileInterface.EoF 
   print MyFileInterface.readLn
end
MyFileInterface.close
```

Related: `open [SimTalk] - FileInterface`, `readLn [SimTalk]`, `EoF [SimTalk]`.

### IsOpen [SimTalk] - FileInterface

`IsOpen` reports whether the file designated for writing is open.

Example:

```simtalk
print MyFileInterface.IsOpen
```

## See Also

The directory also documents the **Attributes of the FileInterface**, which includes the attributes listed in the table of contents plus the attributes common to all objects.
