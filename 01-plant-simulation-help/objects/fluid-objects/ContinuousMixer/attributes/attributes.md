# Attributes of the ContinuousMixer

The ContinuousMixer provides:

- The attributes listed in the table of contents to the left.
- The _Attributes of the Fluid Objects.
- The Attributes of All Objects.

## Viewing Attributes and Methods

To show the methods, read-only attributes, and attributes of the selected Class or Instance:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected **Class** [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected **Instance** [general description].

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

### Querying a read-only attribute

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print ContinuousMixer.Full
```

## Setting and Getting Attribute Values

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

### Setting an attribute

To set the value of an attribute, you might, for example, type:

```simtalk
MyContinuousMixer.OutflowRate := 1
```

### Getting an attribute

To get the value of an attribute, you might, for example, type:

```simtalk
print MyContinuousMixer.OutflowRate
```

```simtalk
posit := MyStation.Cont.XPos
```

## Attribute Reference

### MaterialsTable [SimTalk] - ContinuousMixer

Sets the MaterialsTable which contains the final product and the details of the ingredients of each FluidSource such as ratio/density/color, which the ContinuousMixer designated by `<Path>` can mix.

**Syntax**

```
<Path>.MaterialsTable:path
```

**Assignment Value**

You can assign a value of data type path.

**Example**

```simtalk
MyContinuousMixer.MaterialsTable := MyMaterialsTable
```

**See also**

- Materials Table [Mixer], object

### Product [SimTalk] - ContinuousMixer

Sets the name of the intermediate or of the finished product which the ContinuousMixer designated by `<Path>` is to produce by mixing the ingredients.

**Remarks**

The name of this Product has to be defined in the MaterialsTable.

**Type**

Attribute

**Syntax**

```
<Path>.Product:string
```

**Assignment Value**

You can assign a value of data type string.

**Example**

```simtalk
MyContinuousMixer.Product := "MyProduct"
```

**See also**

- Product [text box] - Mixer
- Materials Table [Mixer]
- Portioner

## Related Object: Portioner

Use the object **Portioner** to create a mobile object out of a free-flowing product. You can then connect the Portioner with one of the material flow objects to further process the created MUs.
