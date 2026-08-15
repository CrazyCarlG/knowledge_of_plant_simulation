# MaterialsTable — Summary

This README summarizes the `MaterialsTable` fluid object, based on `general.md`.

## Overview

The **MaterialsTable** object defines the ingredients and the products to be created and processed in the plant. The defined ingredients and products are consumed by:

- **FluidSource**
- **DePortioner**
- **Mixer**

## Editable fields

- **Name of the Material** — e.g. `DefaultProduct`, `MyIngredient`, `MyMaterial`. The name is used for:
  - Ingredients and the product in the chemical formula of the **Mixer**.
  - The `Material` value of **FluidSource** and **DePortioner**.
  - The `Current material` value of **Pipe** and **Tank**.
  - The values shown on the **Statistics** tab of **FluidDrain**.
- **Density** of the material.
- **Color** — used during product animation; selected via the `Colors` dialog (Plant Simulation stores the color and its number).
- **Product Amount** — the amount of the intermediate/finished product the **Mixer** produces. Enter `-1` to let Plant Simulation use the sum of all ingredients as the Product Amount; specify it explicitly only when mixing changes the volume.
- **Unit** — selected from a drop-down list.
- **Ingredient 1 to Ingredient 10** — each with its **Amount** and **Unit**. Ten ingredients are provided by default; additional ingredient sets can be added (see below). Not all columns must be filled.

## Inheritance

The MaterialsTable shares most properties of the **DataTable**, providing the DataTable's methods and attributes.

## Adding to a simulation model

Click **Manage Class Library > Basic Objects > Fluids > MaterialsTable** on the Home ribbon tab. Sample models are available under **Start Page > Getting Started > Example Models > Small Examples**.

## Viewing attributes and methods

- **Class Library**: select **Show Attributes and Methods** on its context menu.
- **Instance**: press **F8**, or click **Show Attributes and Methods** on the Home ribbon tab of the Frame.

Values can be set/get via dialog controls or by assigning/reading attributes in SimTalk.

### Setting an attribute value

```simtalk
PatchMatrix.Name := "MyPatchMatrix"
```

### Getting an attribute value

```simtalk
print PatchMatrix.Name
posit := MyStation.Cont.XPos
```

## Adding additional ingredients

The table is designed for ten ingredients by default. To add more:

1. Deactivate **Inherit Format** and **Inherit Contents** on the List ribbon tab.
2. Open the `List Format` dialog → **Dimension** tab, and increase the column count by three per additional ingredient.
3. Copy the **Ingredient 9** and **Ingredient 10** columns and paste them into the new columns (Plant Simulation applies the data type, header caption, width, and background color).

Column data types:

- `Ingredient` — **string**
- `Amount` — **real**
- `Unit` — **string**

## See also

- Add Additional Ingredients to the MaterialsTable
- Simulate Free-flowing Materials and Fluids
- Configure the Recipe in the MaterialsTable
- Configure the Recipe of the Product in the MaterialsTable
- CurrentMaterialColor [SimTalk]
- CurrentMaterialDensity [SimTalk]
- DataTable [object]
- Work with Data in a List or Table
- Work with Data in the DataTable
- Methods of the DataTable
- _Attributes of the DataTable
- Resource Objects
