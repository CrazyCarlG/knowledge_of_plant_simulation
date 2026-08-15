# Read-Only Attributes of the Variable

> This document summarizes the read-only attributes available on the **Variable** object.

## Overview

Read-only attributes correspond to dialog items on one of the object's tabs (for example, the **Statistics** tab). They can be queried but not modified directly.

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window.

Two ways to open it:

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show the selected **Class**.
- Press **F8** (or click **Show Attributes and Methods** on the **Home** ribbon tab of the Frame) to show the selected **Instance**.

To query the value of a read-only attribute, for example:

```simtalk
print &MyVariable.AsString
```

## Read-Only Attributes

### `asString`

Returns the value of the Variable as a string.

#### Remarks

Having the value as a string is especially useful for Variables of data type `object`. If the Variable contains a relative path, `asString` returns the relative path.

#### Type

Read-only attribute

#### Syntax

```simtalk
<&>Variable.asString → string
```

#### Return Value

The return value has the data type `string`.

#### Example

```simtalk
ObjVariable := "~.ProdMgr.prodplan"
var a1 := ObjVariable             // assigns .Models.Model.ProdMgr.prodplan
var a2 := &ObjVariable.asString   // assigns "~.ProdMgr.prodplan"
```

#### See Also

- Data Type [Variable]
- Attributes of the Variable

## Accessing Attributes of the Variable

The object **Variable** provides:

- The attributes listed in the table of contents.
- The **Attributes of All Objects**.

> **Note**
>
> You can only access attributes of the object `Variable` that refer to the object itself via the reference operator `&`. Without the operator, the attribute is applied to the contents of the Variable.

```simtalk
&Variable.Name := "MyVariable"
```
