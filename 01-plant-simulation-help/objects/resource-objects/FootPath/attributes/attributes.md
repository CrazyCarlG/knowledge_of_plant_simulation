# Attributes of the FootPath

The **FootPath** provides:

- The attributes listed below.
- The *Attributes of All Objects*.

## Viewing Attributes and Methods

To show the methods, read-only attributes, and attributes of an object or instance:

- Press the **F8** key, or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance (shows the selected *Instance*).
- Select **Show Attributes and Methods** on the context menu of the Class Library (shows the selected *Class*).

To query the value of a read-only attribute:

```simtalk
print MyFootPath.UUID
```

You can set and get attribute values either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

To set the value of an attribute:

```simtalk
MyFootPath.length := 5
```

To get the value of an attribute:

```simtalk
print MyFootPath.length
posit := Station.Cont.XPos
```

---

## Length [SimTalk] — FootPath

Sets the physical **Length** of the Footpath designated by `<Path>`.

**Remarks:** A Worker enters the FootPath at position 0 and exits it after covering the length you specify.

- **Type:** Attribute
- **Syntax:** `<Path>.Length:length`
- **Assignment Value:** You can assign a value of data type `length`.

> **Note:** In SimTalk 2.0 you can specify the length units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in`. Type the unit directly after the value, without a separating blank space (e.g. `10m` or `10.2m`). You can specify the unit for floating point values and for integer values.

**Example:**

```simtalk
MyFootPath.Length := 44m
```

**See also:** Length [text box] — FootPath

---

## Width [SimTalk] — FootPath

Sets the **Width** of the Footpath designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Width:length`
- **Assignment Value:** You can assign a value of data type `length`.

> **Note:** In SimTalk 2.0 you can specify the length units `m`, `mm`, `km`, `cm`, `yd`, `ft`, and `in`. Type the unit directly after the value, without a separating blank space (e.g. `10m` or `10.2m`). You can specify the unit for floating point values and for integer values.

**Example:**

```simtalk
MyFootPath.Width := 2 // meters
```

**See also:** Width [text box] — FootPath

---

## WorkerPool

Use the object **WorkerPool** for modeling the lounge or the staff room of your plant.
