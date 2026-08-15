# Attributes of the ParallelStation

The ParallelStation provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
ParallelStation.XDim := 3
ParallelStation.YDim := 4
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print ParallelStation.XDim
posit := MyStation.Cont.XPos
```

---

## StartProcessingWhenFull

Sets if the ParallelStation designated by `<Path>` only starts processing parts if a part each is located on all of its processing stations (`true`).

### Remarks

`StartProcessingWhenFull` is the default setting. Here new parts can only enter the ParallelStation when it finished processing the current set of parts and when all parts have left the ParallelStation again.

When a part of another type wants to enter the ParallelStation, it starts processing the parts that are already located on it even when it is not full. Only when the ParallelStation finished processing these parts and when it is empty again, the parts of another type can enter.

Use the method `startProcessing` to start processing parts even if the ParallelStation is not full yet.

Specify `false` to make the ParallelStation process the parts immediately after they entered. New parts can enter at any time.

If the ParallelStation does not have to be set up, parts of different types can also move onto the ParallelStation. Processing then might start with different Processing Times when the ParallelStation is full. This applies to type-dependent and to place-dependent processing times and when you entered a formula as the processing time.

> **Note**
> For processing time based failures of a ParallelStation, the simulated MTBF is reduced when the number of parallel processing operations of parts on the ParallelStation increases. This means that the more parts are processed simultaneously, the sooner the failure occurs, and the smaller the availability becomes. This then prevents the Availability you entered into the dialog from being reached.
> This does not apply when you activated the setting **Start Processing When Full**.

### Type

Attribute

### Syntax

```
<Path>.StartProcessingWhenFull:boolean
```

### Assignment Value

You can assign a value of data type `boolean`.

### Example

```simtalk
ParallelStation.StartProcessingWhenFull := false
```

### See also

- `startProcessing` [SimTalk] - material flow objects
- Start Processing When Full [check box]

---

## XDim

Sets or gets the number of processing places of the ParallelStation designated by `<Path>` in the X-Dimension.

### Remarks

The Capacity is the product of X-Dimension times Y-Dimension. The greatest allowed value is ten million.

> **Note**
> If you decrease the dimension of the object, make sure that no MUs are located on the places that will be deleted by this action!
> If MUs are located on the object, the dimension is limited, as Plant Simulation neither deletes MUs outside of the new dimension automatically nor moves them to another processing place!
> If, for example, a MU is located at the position (3,4), the new x-coordinate may not be less than 3, and the new y-coordinate may not be less than 4.

### Type

Attribute

### Syntax

```
<Path>.XDim:integer
```

### Watchable

The attribute is watchable.

### Assignment Value

You can assign a value of data type `integer`.

### Example

```simtalk
ParallelStation.XDim := 3
ParallelStation.YDim := 4 // 12 stations
```

### See also

- X-Dimension [ParallelStation]
- `XDim` [SimTalk] - ParallelStation

---

## YDim

Sets or gets the number of processing places of the ParallelStation designated by `<Path>` in the Y-Dimension.

### Remarks

The Capacity is the product of X-Dimension times Y-Dimension. The greatest allowed value is ten million.

> **Note**
> If you decrease the dimension of the object, make sure that no MUs are located on the places that will be deleted by this action!
> If MUs are located on the object, the dimension is limited, as Plant Simulation neither deletes MUs outside of the new dimension automatically nor moves them to another processing place!
> If, for example, a MU is located at the position (3,4), the new x-coordinate may not be less than 3, and the new y-coordinate may not be less than 4.

### Type

Attribute

### Syntax

```
<Path>.YDim:integer
```

### Watchable

The attribute is watchable.

### Assignment Value

You can assign a value of data type `integer`.

### Example

```simtalk
ParallelStation.XDim := 3
ParallelStation.YDim := 4 // 12 stations
```

### See also

- Y-Dimension [ParallelStation]
- `YDim` [SimTalk] - ParallelStation

---

## Related: AssemblyStation

Use the object **AssemblyStation** for adding mounting parts to a main part, for example doors to a car body.

### Description

The AssemblyStation moves the mounting parts either to the main MU—according to the value you enter into the Assembly Table—or it deletes them. Mounting parts might also be called assembly parts, add-on parts, attachment part, attached part, etc.

Use the AssemblyStation to model assembly processes. If the assembly process requires services, you can assign the order in which the AssemblyStation requests mounting parts and services. To dismantle parts from the main part, you can use the DismantleStation.

If the AssemblyStation uses an Assembly Table and you specify an Assembly Time and a Sequence Number for each mounting part, the AssemblyStation assembles the mounting parts sequentially. The assembly of each individual mounting part consumes the specified Assembly Time. After all mounting parts are assembled, the Processing Time of the AssemblyStation passes and the main part then leaves the station.

In sequential assembly mode, the AssemblyStation starts assembling the mounting parts with the lowest Sequence Number, then continues with the next higher Sequence Number, and so on. Only the mounting parts that are needed in the current assembly sequence can enter the AssemblyStation. Within a sequence, the mounting parts are assembled in the order in which they entered the AssemblyStation.

> **Note**
> You cannot move a part via information flow, i.e., by using methods, to the AssemblyStation!
> To show a tooltip with information about the AssemblyStation, hover with the mouse over it.
