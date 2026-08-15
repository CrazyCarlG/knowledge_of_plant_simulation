# MaterialsTable

Use the object **MaterialsTable** to define the ingredients and the products to be created and to be processed in the plant.

The ingredients and products are going to be used by the **FluidSource**, by the **DePortioner**, and by the **Mixer** in your simulation model.

## What you can type in

- **The Name of the Material**, for example `DefaultProduct`, `MyIngredient`, `MyMaterial`, etc.

  The material names are used for:
  - All ingredients and for the product in a chemical formula of the object **Mixer**.
  - The value `Material` of the **FluidSource** and of the **DePortioner**.
  - The value of the `Current material` of the **Pipe** and the **Tank**.
  - The values which the Tab **Statistics** of the object **FluidDrain** shows.

- **The Density** of the material.
- **The Color** to be used during the animation of the product. Click in the respective cell and select a color in the dialog `Colors`. Plant Simulation then enters the color and the color number into the cell.
- **The Product Amount** which is the amount of the intermediate or of the finished product which the **Mixer** is to produce using the ingredients.

  If you type `-1` for a recipe into the column `Product Amount` of the MaterialsTable of the Mixer, Plant Simulation assumes the sum of all ingredients as the Product Amount. You only have to explicitly specify the Product Amount if mixing the ingredients increases or decreases the volume, i.e., if the Product Amount is not the sum of the ingredients.

- **The Unit** of the material. Double-click in the respective cell and select the unit for the material from the drop-down list.
- **The Name of Ingredient 1 to Ingredient 10**, its respective **Amount**, and its respective **Unit**. By default, ten ingredients are provided. You can add additional columns for additional ingredient sets at any time (compare "Add Additional Ingredients to the MaterialsTable"). You do not have to fill in all columns.

## Inheritance

The MaterialsTable shares most of the properties of the **DataTable**. It provides the Methods of the DataTable and the Attributes of the DataTable.

## Adding to a simulation model

To add the object MaterialsTable to your simulation model, click **Manage Class Library > Basic Objects > Fluids > MaterialsTable** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog `Examples Collection`, and click Open Model.

## Viewing attributes and methods

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class (general description).
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance (general description).

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

### Setting an attribute value

```
PatchMatrix.Name := "MyPatchMatrix"
```

### Getting an attribute value

```
print PatchMatrix.Name
```

```
posit := MyStation.Cont.XPos
```

## Add Additional Ingredients to the MaterialsTable

The MaterialsTable is designed for ten ingredients by default. You can add more ingredients as required.

### Remarks

To add additional ingredients:

- Deactivate **Inherit Format** and **Inherit Contents** on the List ribbon tab.
- Open the dialog `List Format` and change to the tab **Dimension**. Increase the number of columns per additional ingredient by three. In the example, six columns were added, meaning two ingredients. Click OK and close the dialog.
- Then copy the columns for Ingredient 9 and Ingredient 10 and paste them into the added columns. While doing so Plant Simulation applies the data type, the caption of the column header, the column width, and the background color of the cells. This way the columns do not have to be configured manually.

Column data types:

- The column `Ingredient` has the data type **string**.
- The column `Amount` has the data type **real**.
- The column `Unit` has the data type **string**.

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
