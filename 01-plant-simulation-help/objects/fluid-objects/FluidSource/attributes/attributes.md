# Attributes of the FluidSource

## Overview

The FluidSource provides:

- The attributes listed in the table of contents to the left.
- The _Attributes of the Fluid Objects.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute:

```simtalk
MyFluidSource.OutflowRate := 1
```

- To get the value of an attribute:

```simtalk
print MyFluidSource.OutflowRate
posit := MyStation.Cont.XPos
```

---

## StatAmount [SimTalk]

Returns the amount of material, i.e., the number of liters, that the FluidSource designated by `<Path>` produced.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatAmount → real`
- **Return Value:** The return value has the data type `real`.

**Example**

```simtalk
print MyFluidSource.StatAmount
```

**See also:** Tab Statistics, Attributes of the FluidSource

---

## Material [SimTalk] - FluidSource

Sets the name of the material which the FluidSource designated by `<Path>` is to produce.

> **Note:** What you enter as the `Material` depends on the setting you selected as the `MaterialSelection`. The name of the material has to be defined in the `MaterialsTable`.

- **Type:** Attribute
- **Syntax:** `<Path>.Material:string`
- **Assignment Value:**
  - For the setting **Constant** you can assign a value of data type `string`.
  - For the settings **Sequence Cyclical** and **Sequence** you can assign a value of data type `any`. This can either be a `DataTable` of data type `object` or the path to a `DataTable`.

You can specify:

- **"Constant":** The FluidSource produces a single type of material only. Specify the name of material with the attribute `Material`.
- **"Sequence cyclical":** The FluidSource produces the materials in the sequence and with the amount in the sequence in which you enter them into the Sequence Table. Once the FluidSource has processed the entire sequence, it starts processing the information in the table again starting at the beginning of the sequence. Specify the name of the Sequence Table with the attribute `Material`.
- **"Sequence":** The FluidSource produces the materials in the sequence and with the amount in the sequence in which you enter them into the Sequence Table. As opposed to Sequence Cyclical, the setting Sequence processes the sequence only once, not repeatedly. Specify the name of the Sequence Table with the attribute `Material`.
- **"Sequence table":** Define the materials, which the FluidSource is to produce, in the Sequence Table.

In the Sequence Table you can specify:

- The name of the Material, for example `StandardMaterial`, `Milk`, `Sugar`, `Cocoa`, etc.
- The Amount in liters of the Material that the FluidSource is to produce.

**Examples**

```simtalk
MyFluidSource.Material := "MyMaterial"
MyFluidSource.MaterialSelection := "Sequence"
MyFluidSource.Material := .UserObjects.MySequenceTable
```

**See also:** Material [text box] - FluidSource, Materials Table [FluidSource], MaterialSelection [SimTalk]

---

## MaterialSelection [SimTalk]

Sets how the FluidSource designated by `<Path>` selects the material it produces.

> **Note:** Depending on what you select here, the setting `Material` either defines the Material itself or the path to the Sequence Table.

- **Type:** Attribute
- **Syntax:** `<Path>.MaterialSelection:string`
- **Assignment Value:**
  - For the setting **Constant** you can assign a value of data type `string`.
  - For the settings **Sequence Cyclical** and **Sequence** you can assign a value of data type `any`. This can either be a `DataTable` of data type `object` or the path to a `DataTable`.

You can specify:

- **"Constant":** The FluidSource produces a single type of material only. Specify the name of material with the attribute `Material`.
- **"ConstSequence cyclical":** The FluidSource produces the materials in the sequence and with the amount in the order in which you enter them into the Sequence Table. Once the FluidSource has processed the entire sequence, it starts processing the information in the table again starting at the beginning of the sequence. Specify the name of the Sequence Table with the attribute `Material`.
- **"Sequence":** The FluidSource produces the materials in the sequence and with the amount in the order in which you enter them into the Sequence Table. As opposed to Sequence Cyclical, the setting Sequence processes the sequence only once, not repeatedly. If the sequence is processed once, the FluidSource does not produce any additional materials. Specify the name of the Sequence Table with the attribute `Material`.

**Example**

```simtalk
MyFluidSource.MaterialSelection := "Sequence"
MyFluidSource.Material := .UserObjects.MySequenceTable
```

**See also:** Material Selection [drop-down list], Material [text box] - FluidSource

---

## MaterialsTable [SimTalk] - FluidSource

Sets the `MaterialsTable` which contains the data of the different materials which the FluidSource designated by `<Path>` can produce.

- **Type:** Attribute
- **Syntax:** `<Path>.MaterialsTable:path`
- **Assignment Value:** You can assign a value of data type `path`.

**Example**

```simtalk
MyFluidSource.MaterialsTable := MyMaterialsTable
```

**See also:** Materials Table [FluidSource]

---

## OutflowRate [SimTalk] - FluidSource

Sets the outflow rate with which the material flows out of the FluidSource designated by `<Path>`.

The material then flows off through objects of type `Pipe` to the next object in the flow of materials. The Outflow Rate is the amount of liters of the material that flows off in a second.

> **Note:** The current Outflow Rate depends on the number of attached Pipes. Let's say you attached two Pipes, then the specified Outflow Rate flows through each one of these Pipes in case the Outflow Rate of the connected Pipes permits this. If you just want to let the specified amount flow out of the object, attach a single Pipe and split that up into several Pipes later on.

- **Type:** Attribute
- **Syntax:** `<Path>.OutflowRate:real`
- **Assignment Value:** You can assign a value of data type `real`.

**Example**

```simtalk
MyFluidSource.OutflowRate := 1
```

**See also:** Outflow Rate [FluidSource], Pipe

---

## FluidDrain

Use the FluidDrain to define the ingredients and the products to be processed in the plant.

The FluidDrain removes the free-flowing materials, which the FluidSource introduced into the plant, from the plant after they have been mixed and processed. It differentiates the materials by their names.

To change the length of the graphic and the anchor points of the FluidDrain, click **Show Manipulators** on the Edit ribbon tab or press **M** on the keyboard.

To show a tooltip with information about the FluidDrain, hover with the mouse over it.

### Add the Object to the Simulation Model

To add the object `FluidDrain` to your simulation model, click **Manage Class Library > Basic Objects > Fluids > FluidDrain** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog **Examples Collection**, and click **Open Model**.
