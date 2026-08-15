# FileInterface Attributes

The `FileInterface` object provides attributes for reading and writing files.

## Overview

The `FileInterface` provides:

- The attributes listed below.
- The [Attributes of All Objects].

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show them for the selected Instance.

You can set the value of an attribute and get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows or by assigning values to the respective attributes.

## Attributes

### IsOpen (read-only attribute)

Returns whether the file of the `FileInterface` designated by `<Path>` into which data is to be written is open (`true`) or not open (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.IsOpen → boolean`
- **Return value:** `boolean`

Example:

```simtalk
print MyFileInterface.IsOpen
```

### Encoding (attribute)

Sets the encoding with which Plant Simulation saves the file of the `FileInterface` designated by `<Path>` which it writes.

When Plant Simulation reads a file, the attribute contains the encoding of the file. If Plant Simulation cannot recognize an encoding, it returns `ANSI`.

- **Type:** Attribute
- **Syntax:** `<Path>.Encoding:string`
- **Assignment value:** a value of data type `string`

You can specify:

- `"ANSI"` — an 8-bit character set that enables you to represent up to 256 characters (0 through 255). The ANSI character set is a superset of the 7-bit ASCII character set.
- `"UTF-8"` — another encoding of the Unicode character set. Each character is represented by one to three bytes.
- `"UTF-16"` — another encoding of the Unicode character set.
- `"Unicode"` — a 16-bit character set that includes almost all of the written languages of the world. Plant Simulation saves Unicode in UTF-16 encoding. Each character is represented by two bytes.

Example:

```simtalk
MyFileInterface.Encoding := "Unicode"
```

### FileName (attribute)

Sets the name of the file of the `FileInterface` designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.FileName:string`
- **Assignment value:** a value of data type `string`

Example:

```simtalk
MyFileInterface.FileName := "C:\users\johnE\myData.txt"
```

## General Usage

To set the value of an attribute, for example:

```simtalk
MyFileInterface.FileName := "C:\users\johnE\myData.txt"
```

To get the value of an attribute, for example:

```simtalk
print MyFileInterface.FileName
posit := Station.Cont.XPos
```

## Related

- `Encoding` [drop-down list]
- `Filename` [FileInterface]
- `XMLInterface` — use the `XMLInterface` object for reading and extracting data stored in XML files.
