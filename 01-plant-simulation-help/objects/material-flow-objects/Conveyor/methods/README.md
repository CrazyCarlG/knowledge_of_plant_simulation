# Conveyor Methods

This directory documents the **methods** and **read-only attributes** of the **Conveyor** object in Plant Simulation.

## Contents

- [`methods.md`](methods.md) — the primary reference for the Conveyor's methods, syntax conventions, and read-only attributes.

## Summary

The Conveyor object provides three groups of methods:

- The Methods of Curved Objects
- The Methods of the Material Flow Objects
- The Methods of All Objects

### Viewing Methods and Attributes

To see all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to display the methods, read-only attributes, and attributes of the selected **Class** (general description).
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame holding the instance to display the methods, read-only attributes, and attributes of the selected **Instance** (general description).

### Method Syntax

A typical syntax line looks like this:

```text
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature (identifier and parameter data types) appears in parentheses. `(Parameter:string)`, for example, denotes a string parameter. A constant, a variable of the required type, or a method returning the required type may be supplied.
- **Note:** Always enter the parentheses for nested expressions `(…)`; omitting them may yield unexpected results and open the Debugger.
- Optional parameters appear within brackets, e.g. `[,Parameter:boolean]`.
- A parameter's default value follows it after `:=`, e.g. `:= false`.
- A method's return type appears after the arrow `→`, e.g. `→ boolean`.

### Read-Only Attributes

The Conveyor provides:

- The read-only attributes listed in the source documentation's table of contents.
- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

Read-only attribute values can be queried but not set — Plant Simulation computes the value at the moment of the query. Most read-only attributes correspond to an unavailable dialog item on an object tab, such as the **Statistics** tab.
