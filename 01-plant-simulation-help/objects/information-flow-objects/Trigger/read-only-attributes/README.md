# Read-Only Attributes of the Trigger

This directory documents the **read-only attributes** of the **Trigger** information-flow object in Plant Simulation. A Trigger is used to control the material flow in a model, and this document describes the read-only attributes that you can query but not set.

## Contents

The directory contains the following files, which hold the same information in two formats:

- `read-only-attributes.md` — Markdown version of the reference.
- `read-only-attributes.txtx` — plain-text version of the reference (source text extracted from Plant Simulation Help).

## Summary

### Viewing Attributes and Methods

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- In the **Class Library**, select **Show Attributes and Methods** on the context menu to show the members of the selected **Class**.
- In a **Frame** containing an instance, press **F8** or click **Show Attributes and Methods** on the **Home** ribbon tab to show the members of the selected **Instance**.

### Read-Only Attribute: `CurrentValue`

The only read-only attribute documented for the Trigger is **`CurrentValue`**.

- **Purpose** — Returns the **Current Value** of the Trigger designated by `<Path>`.
- **Data type** — The data type of the value matches the data type of the Trigger.
- **Type** — Read-only attribute.
- **Syntax**

  ```
  <Path>.CurrentValue → any
  ```

- **Return value** — The return value has the data type `any`.
- **Example**

  ```
  print MyTrigger.CurrentValue
  ```

- **See also** — Tab Representation; Attributes of the Trigger.

### Attributes of the Trigger (General)

The Trigger provides:

- The attributes listed in the table of contents.
- The **Attributes of All Objects** (common attributes shared by all objects).

You can **set** and **get** attribute values either through the dialog windows (check boxes, text boxes, drop-down lists) or by assigning values in SimTalk.

**Examples of setting an attribute value:**

```
MyTrigger.Combination := true
MyTrigger.CombinationTable.delete({0,1}..{*,*})
MyTrigger.CombinationTable.writeRow(1,1,Trig5,0,10,3600)
MyTrigger.CombinationTable.createNestedList(0,1)
MyTrigger.CombinationTable[0,1].setname("K1")
```

**Examples of getting an attribute value:**

```
print MyTrigger.Combination
posit := Station.Cont.XPos
```

## Notes

- To query a read-only attribute, use `print` or assignment, for example `print MyTrigger.CurrentValue`.
- The reference source is *Plant Simulation Help* (pages 11-4365 through 11-4367).
