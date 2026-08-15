# Read-Only Attributes of the SankeyDiagram

## Overview

The SankeyDiagram provides the **Read-Only Attributes of All Objects**. You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it.

In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

## Viewing Attributes and Methods

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class (general description).
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance (general description).

## Example: Querying a Read-Only Attribute

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MySankeyDiagram.UUID
```

## `update` [SimTalk] — SankeyDiagram

Refreshes the displayed SankeyDiagram designated by `<Path>` with the current values.

| Property | Value    |
|----------|----------|
| Type     | Method   |

### Syntax

```simtalk
<Path>.update
```

### Example

```simtalk
MySankeyDiagram.update
```

### See also

- Update [in Frame]

## Attributes of the SankeyDiagram

The SankeyDiagram provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

---

*Plant Simulation Help — Unpublished work. © 2026 Siemens*
