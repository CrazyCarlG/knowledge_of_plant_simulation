# FileLink Methods — README

This directory documents the methods, read-only attributes, and attributes of the **FileLink** object in Plant Simulation. The information is sourced from the Plant Simulation Help and is covered by the following files:

- `methods.md` — structured Markdown version of the FileLink methods reference.
- `methods.txtx` — plain-text export of the same help topic.

## Summary

### Methods

The FileLink provides:

- **`openFile` [SimTalk]** — the only FileLink-specific method.
- The **Methods of All Objects** (inherited methods common to every object).

To view all methods, read-only attributes, and attributes, open the **Show Attributes and Methods** window:

- In the **Class Library**, select **Show Attributes and Methods** from the context menu to show them for the selected Class.
- For an inserted **Instance**, press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame.

### Syntax line

Methods are documented with a syntax line, for example:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` — the path of the object the method applies to.
- Parentheses `( … )` — the method signature: parameter identifier and data type (e.g. `(Parameter:string)`). A variable of the required type or a method returning that type may be used instead of a constant.
- **Note:** Always enter the parentheses; omitting them can lead to unexpected results and open the Debugger.
- Brackets `[ … ]` — optional parameters.
- `:= value` — default value of a parameter.
- `→ type` — the return value data type (after the arrow).

### `openFile` [SimTalk]

Opens the file linked to the FileLink (designated by `<Path>`) in its originating application or the file type assigned on the computer, so it can be edited.

- **Remarks:** If the safety setting **File > Model Settings > General > Prohibit Access to the Computer** is deactivated, the FileLink cannot open embedded files with a double-click; the same applies to `openFile`.
- **Type:** Method
- **Syntax:** `<Path>.openFile`
- **Example:** `frame1.MyFileLink.openFile`
- **See also:** Prohibit Access to the Computer (model settings).

### Read-Only Attributes

The FileLink provides the **Read-Only Attributes of All Objects**. Their values can be queried but not set, because Plant Simulation computes them at query time. Most read-only attributes correspond to a non-editable dialog item (e.g. on the Statistics tab).

Example query:

```
print MyFileLink.UUID
```

### Attributes

The FileLink provides:

- The attributes listed in the help's table of contents.
- The **Attributes of All Objects** (inherited attributes common to every object).

As with methods, use the **Show Attributes and Methods** window to view the complete list for a selected Class or Instance.
