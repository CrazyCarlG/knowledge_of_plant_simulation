# LockoutZone Methods — Summary

This README summarizes the content of the files in this `methods` folder for the **LockoutZone** resource object in Plant Simulation.

## Source Files

- `methods.md` — the main documentation for the LockoutZone methods and read-only attributes.
- `methods.txtx` — a plain-text rendering of the same documentation (contains identical content, including a general description of the Help Menu and syntax conventions).

> Note: There are no subfolders within this directory.

## Overview

The **LockoutZone** provides:

- One specific method: `addObject [SimTalk]` — LockoutZone.
- The inherited *Methods of All Objects*.
- The *Read-Only Attributes of All Objects* plus the LockoutZone-specific read-only attributes.

To view all methods, read-only attributes, and attributes, open the **Show Attributes and Methods** window:

- In the **Class Library**, select **Show Attributes and Methods** from the object's context menu.
- For an **instance**, press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame.

## Understanding the Syntax Line

A syntax line has the form:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` — the path of the object the method applies to.
- Parameters are listed in parentheses with their data type, e.g. `(Parameter:string)`. A constant value, a variable of the required type, or a method returning that type may be used.
- Optional parameters appear in brackets, e.g. `[,Parameter:boolean]`.
- Default values follow the parameter with `:=`, e.g. `:= false`.
- The return value's data type follows the arrow `→`, e.g. `→ boolean`.

> **Note:** Always enter the parentheses for expressions within parentheses `(…)`; omitting them can cause unexpected results and open the Debugger.

## Method

### `addObject` [SimTalk] — LockoutZone

Adds a single object to the LockoutZone designated by `<Path>`.

- **Type:** Method
- **Syntax:**
  ```
  <Path>.addObject(NameOfObject:path) → boolean
  ```
- **Parameter:** `NameOfObject` (data type `path`) — the name of the object to add.
- **Return Value:** data type `boolean`.

**Example:**

```
MyLockoutZone.addObject(MyParallelStation)
```

**See also:** Objects [SimTalk] — LockoutZone, Tab Objects.

## Read-Only Attributes of the LockoutZone

- Includes the LockoutZone-specific read-only attributes and the *Read-Only Attributes of All Objects*.
- Values can be **queried** but **not set**; Plant Simulation computes each value at the point in time it is queried.
