# Read-Only Attributes of the FileInterface

The FileInterface provides:

- The read-only attributes listed below.
- The read-only attributes of all objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyFileInterface.IsOpen
```

---

## EoF [SimTalk]

`EoF` returns if the file of the FileInterface designated by `<Path>` is still closed, as no data is provided for processing (`true`).

After you opened the file with the method `open`, `EoF` (end of file) returns `false` as long as lines of text may still be read in with the method `readLn`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.EoF → boolean`
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
MyFileInterface.open
while not MyFileInterface.EoF 
   print MyFileInterface.readLn
end
MyFileInterface.close
```

Related: `open [SimTalk] - FileInterface`, `readLn [SimTalk]`, `EoF [SimTalk]`.

---

## IsOpen [SimTalk] - FileInterface

Returns if the file of the FileInterface designated by `<Path>` into which data is to be written is open (`true`) or not open (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.IsOpen → boolean`
- **Return Value:** The return value has the data type `boolean`.

### Example

```simtalk
printMyFileInterface.IsOpen
```

---

## Attributes of the FileInterface

The FileInterface provides:

- The attributes listed in the table of contents.
- The attributes of all objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
