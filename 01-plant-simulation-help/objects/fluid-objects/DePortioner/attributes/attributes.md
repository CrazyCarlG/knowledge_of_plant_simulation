# DePortioner — Attributes

The DePortioner provides:
- The attributes listed in the table of contents to the left.
- The `_Attributes` of the Fluid Objects.
- The Attributes of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods** (select it from the context menu of the Class Library, or press F8 / click it on the Home ribbon tab of the Frame).

You can set an attribute's value and get its value either through the dialog windows (check boxes, text boxes, drop-down lists) or by assigning values to the respective attributes:
- Set a value, for example: `MyDePortioner.AmountPerMU := 10`
- Get a value, for example: `print MyDePortioner.AmountPerMU` or `posit := MyStation.Cont.XPos`

---

## CurrentAmount `[SimTalk]`
Returns the current amount of the fluid in the DePortioner designated by `<Path>` at the moment.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.CurrentAmount → real`
- **Return Value:** data type `real`, measured in liters

```simtalk
print MyDePortioner.CurrentAmount
```

---

## AmountPerMU `[SimTalk]`
Sets the total amount in liters of the material that the DePortioner designated by `<Path>` creates.

- **Remarks:** Applies when you select **Fixed** under *Fluid Depends On* / `FluidDependsOn`.
- **Type:** Attribute
- **Syntax:** `<Path>.AmountPerMU:real`
- **Assignment Value:** `real`

```simtalk
MyDePortioner.AmountPerMU := 20
```

---

## AttrNameAmount `[SimTalk]`
Sets the name of the user-defined **Amount Attribute** of the MU, which defines the amount of the material that the DePortioner designated by `<Path>` creates.

- **Remarks:** Applies if you select **MU Attribute** as the definition method of `FluidDependsOn`.
- **Type:** Attribute
- **Syntax:** `<Path>.AttrNameAmount:string`
- **Assignment Value:** `string`

```simtalk
MyDePortioner.AttrNameAmount := "Amount"
```

---

## AttrNameMaterial `[SimTalk]`
Sets the name of the user-defined **Material Attribute** of the MU, which defines the material that the DePortioner designated by `<Path>` creates.

- **Remarks:** Applies when you select **MU Attribute** under `FluidDependsOn`.
- **Type:** Attribute
- **Syntax:** `<Path>.AttrNameMaterial:string`
- **Assignment Value:** `string`

```simtalk
MyDePortioner.AttrNameMaterial := "Material"
```

---

## FluidDependsOn `[SimTalk]`
Sets how the DePortioner designated by `<Path>` creates the material and the amount of the fluid.

- **Remarks:** The name of each material that is to be used has to be defined in the `MaterialsTable`.
- **Type:** Attribute
- **Syntax:** `<Path>.FluidDependsOn:string`
- **Assignment Value:** `string` — you can specify:
  - `"Fixed"` — set the material and amount per MU under *Material* / `Material` and *Amount per MU* / `AmountPerMU`.
  - `"MU Name"` — set the material and amount per MU under *Mapping table* / `MappingTable`.
  - `"MU Attribute"` — set the material and amount per MU under *Material attribute* / `AttrNameMaterial` and *Amount attribute* / `AttrNameAmount`. These are user-defined attributes of the MU that you have to create.

```simtalk
MyDePortioner.FluidDependsOn := "Fixed"
```

---

## MappingTable `[SimTalk]`
Sets the name of the data table that contains the MU Name of the arriving MU, the Material, and the Amount of the fluid that the DePortioner designated by `<Path>` creates.

- **Remarks:** Applies when you select **MU Name** under `FluidDependsOn`.
- **Type:** Attribute
- **Syntax:** `<Path>.MappingTable:path`
- **Assignment Value:** `path`

```simtalk
MyDePortioner.MappingTable := MyMappingTable
```

---

## Material `[SimTalk]`
Sets the name of the material that the DePortioner designated by `<Path>` creates.

- **Remarks:** Applies if you select **Fixed** under `FluidDependsOn`.
- **Type:** Attribute
- **Syntax:** `<Path>.Material:string`
- **Assignment Value:** `string`

```simtalk
MyDePortioner.Material := "StandardMaterial"
```

---

## MaterialsTable `[SimTalk]`
Sets the MaterialsTable which contains the data of the different materials that the DePortioner designated by `<Path>` can create.

- **Type:** Attribute
- **Syntax:** `<Path>.MaterialsTable:path`
- **Assignment Value:** `path`

```simtalk
MyDePortioner.MaterialsTable := MyMaterialsTable
```

---

## OutflowRate `[SimTalk]`
Sets the outflow rate with which the fluid flows out of the DePortioner designated by `<Path>`.

- **Remarks:** The Outflow Rate is the amount of liters of the material that flows off in a second. The material then flows off through objects of type `Pipe` to the next object in the flow of materials.
- **Note:** The current Outflow Rate depends on the number of attached Pipes. If you attach two Pipes, the specified Outflow Rate flows through each one of them, provided the Outflow Rate of the connected Pipes permits this. To let just the specified amount flow out, attach a single Pipe and split it into several Pipes later on.
- **Type:** Attribute
- **Syntax:** `<Path>.OutflowRate:real`
- **Assignment Value:** `real`

```simtalk
MyDePortioner.OutflowRate := 1
```

---

## RecoveryTime `[SimTalk]`
Sets the duration of the Recovery Time of the DePortioner designated by `<Path>`.

- **Remarks:** The Recovery Time is the time required to flush and clean the DePortioner and prepare it for the next process. This is the time during which no material will be accepted after the MU exited the object.
- **Type:** Attribute
- **Syntax:** `<Path>.RecoveryTime:time`
- **Assignment Value:** `time` — specify `0` to allow materials to enter continually.

```simtalk
MyDePortioner.RecoveryTime := 1:00:00
```
