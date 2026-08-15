# Attributes of the Portioner

The Portioner provides the attributes listed below, plus:

- The `_Attributes` of the Fluid Objects.
- The Attributes of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set and get an attribute's value either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes:

- To set the value of an attribute:

  ```simtalk
  MyPortioner.AmountPerMU := 10
  ```

- To get the value of an attribute:

  ```simtalk
  print MyPortioner.AmountPerMU
  posit := MyStation.Cont.XPos
  ```

---

## CurrentMaterial [SimTalk]

Returns the Current Material that flows into the Portioner designated by `<Path>`.

### Remarks

The name is not case-sensitive, just like the names of attributes and methods of the objects are not case-sensitive.

To save memory and improve access speed, all places which use such a case-insensitive string point to the same string in main memory. The visible and unexpected result is that the first occurrence of the string defines how the string is written in terms of upper- and lower-casing.

In SimTalk you can compare strings in a case-insensitive manner with the `~=` operator (see Relational Operators).

### Type

Read-only attribute

### Syntax

```simtalk
<Path>.CurrentMaterial → string
```

### Return Value

The return value has the data type `string`.

### Example

```simtalk
print MyPortioner.CurrentMaterial
```

### See also

- Current Material [Portioner]
- Relational Operators

---

## AmountPerMU [SimTalk]

Sets the Amount of the material in liters which the Portioner designated by `<Path>` is to transmute into individual MUs.

### Type

Attribute

### Syntax

```simtalk
<Path>.AmountPerMU:real
```

### Assignment Value

You can assign a value of data type `real`.

### Example

```simtalk
MyPortioner.AmountPerMU := 10
```

### See also

- Amount per MU [Portioner]

---

## MUPath [SimTalk]

Sets the type of MU which the Portioner designated by `<Path>` is to create.

### Remarks

You can either use one of the predefined MUs or you can create your own MU for just this purpose.

### Type

Attribute

### Syntax

```simtalk
<Path>.MUPath:path
```

### Assignment Value

You can assign a value of data type `path`.

### Example

```simtalk
MyPortioner.MUPath := .MUs.Container
```

### See also

- MU [Portioner]

---

## PredecessorNumber [SimTalk]

Sets the number of the predecessor object which delivers the material to the Portioner designated by `<Path>`.

### Type

Attribute

### Syntax

```simtalk
<Path>.PredecessorNumber:integer
```

### Assignment Value

You can assign a value of data type `integer`.

### Example

```simtalk
MyPortioner.PredecessorNumber := 2
```

### See also

- Fluid from Predecessor [text box]
- DePortioner

---

## DePortioner

Use the object **DePortioner** to empty incoming parts of bulk goods or fluids, create a fluid out of it, and feed the resulting fluids into a Pipe.

We provide three ways of defining the fluid that is to be created:

- By a fixed material and a fixed amount for every MU. For this setting you can enter the **Material** and the **Amount per MU**.
