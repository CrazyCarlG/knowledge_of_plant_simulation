# Read-Only Attributes of the Comment

## Overview

The **Comment** provides the *Read-Only Attributes of All Objects*.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyComment.UUID
```

## `openComment` [SimTalk]

Opens a window that only shows the comment you entered into the Comment designated by `<Path>` without any formatting options.

- **Type:** Method
- **Syntax:**

```simtalk
<Path>.openComment → boolean
```

- **Return Value:** The return value has the data type `boolean`.

**Example:**

```simtalk
MyComment.openComment
```

**See also:**
- Tab Comment [Comment]
- Read-Only Attributes of the Comment

## Attributes of the Comment

The Comment provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

## Viewing Attributes and Methods

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

---
*Plant Simulation Help 11-4585 / 11-4586 · Unpublished work. © 2026 Siemens*
