# Methods of the Mixer

The Mixer provides:

- The methods listed in the table of contents to the left.
- The Methods of the Fluid Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show them for the selected Instance.

## Syntax Line Format

An example of the syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method — identifier and parameter data types — is listed in parentheses. `(Parameter:string)` designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required type.
- Optional parameters are listed within brackets, e.g. `[,Parameter:boolean]` means the boolean parameter is optional.
- If a parameter has a default value, the signature shows the default value after the parameter, e.g. `:= false`.
- If the method has a return value, its data type appears after the arrow `->`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

---

## addContent [SimTalk]

Adds the specified material to the existing content of the Mixer designated by `<Path>`.

**Type:** Method

**Syntax:**

```
<Path>.addContent(Amount:real[, Material:string, MaterialsTable:path])
```

**Parameters:**

- `Amount` (real) — designates the amount of material.
- `Material` (string, optional) — designates the material.
  - Do **not** specify `Material` to increase the existing amount of the contained (single) educt or the contained product after the mixing operation respectively by the specified amount.
  - Specify `Material` to add the specified amount of the new educt to the content in the Mixer during the filling process. After the mixing process the specified amount is added and the specified material replaces the currently existing product.
- `MaterialsTable` (path, optional) — designates the path to the MaterialsTable.

**Example:**

```simtalk
Tank1.addContent(3, "MyProduct", .Fluids.MaterialsTable)
```

---

## setCurrentContent [SimTalk] - Mixer

Sets the current content of the material in the Mixer designated by `<Path>`.

**Remarks:** The new content replaces the previous content. The content can either be the educt or the product itself.

> **Note:** Typically, you set the initial state of the object with the method `setCurrentContent`.

**Type:** Method

**Syntax:**

```
<Path>.setCurrentContent(Amount:real[, Material:string, MaterialsTable:path])
```

**Parameters:**

- `Amount` (real) — designates the amount of material.
- `Material` (string, optional) — designates the material as such.
- `MaterialsTable` (path, optional) — designates the path to the MaterialsTable.

> **Note:** If the Mixer already contains a material, you can just enter the new `Amount` as a single parameter. Otherwise, you also have to specify the `Material` and the `MaterialsTable`.

**Examples:**

```simtalk
MyMixer.setCurrentContent(3, "MyProduct", .Fluids.MaterialsTable)
Mixer1.setCurrentContent(8) -- Mixer1 already contains a material
```

---

# Read-Only Attributes of the Mixer

The Mixer provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of the Fluid Objects.
- The _Read-Only Attributes of All Objects.

You can query the values of read-only attributes, but you cannot set them — Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (e.g. the **Statistics** tab).

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show them for the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Mixer.Full
```
