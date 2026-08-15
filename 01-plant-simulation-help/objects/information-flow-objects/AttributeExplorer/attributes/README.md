# Attributes of the AttributeExplorer

This folder documents the **attributes** of the **AttributeExplorer** object. See [attributes.md](attributes.md) for the full reference.

## Overview

The AttributeExplorer provides 13 attributes, in addition to the Attributes of All Objects. They are summarized in the table below.

| Attribute | Type | Description |
| --- | --- | --- |
| `AttributeRepresentation` | string | Shows attributes with their **Name** or **Alias** (`"Name"` / `"Alias"`). |
| `AttributeTable` | table | Sets the attribute table (tab **Attributes**) for object attributes. |
| `Comment` | string | Sets the comment displayed above the list box. |
| `ExplorerTable` | table | Sets the table shown by the AttributeExplorer; row 0 → Attribute Table, column 0 → Object Table, other columns → Explorer table. |
| `IncludeMUs` | boolean | Also search MUs located within the active Frame (`true`) or not (`false`). |
| `IncludeSubframes` | boolean | Also search Frames located within the active Frame (`true`) or not (`false`). |
| `IsShown` | boolean | Shows (`true`) / hides (`false`) the attribute table. **Watchable.** |
| `Mode` | string | Sets the mode (`"Watch"`, `"Edit"`, or `"Read"`). |
| `ObjectRepresentation` | string | Shows objects with their entire **Path**, **Name**, or **Label** (`"Path"` / `"Name"` / `"Label"`). |
| `ObjectTable` | table | Sets the objects table (tab **Objects**). |
| `QueryTable` | table | Sets the query table (tab **Query**). |
| `ShowComment` | boolean | Shows (`true`) / hides (`false`) the comment text box above the list field. |
| `StartNode` | object | Sets the Frame in which the AttributeExplorer starts finding attributes. |

## Accessing Attribute Values

- To query a read-only attribute:
  ```simtalk
  print MyAttributeExplorer.UUID
  ```
- To set an attribute:
  ```simtalk
  MyAttributeExplorer.Comment := "Processing time changes globally"
  ```
- To get an attribute:
  ```simtalk
  print MyAttributeExplorer.AttributeRepresentation
  posit := Station.Cont.XPos
  ```

## Related

- Show Attributes and Methods window (press **F8** or use the context menu of the Class Library).
- [AttributeExplorer object](../AttributeExplorer.md)
