# Pipe — Attributes

Summary of the attributes of the **Pipe** fluid object (Plant Simulation Help).

The Pipe provides the attributes listed below, in addition to the **Attributes of All Objects**.

## Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `LengthOfPipe` | Read-only | Returns the length (`real`) of the Pipe (from its first point to its last point). |
| `ExitStrategy` | Attribute (`string`) | Sets how the flow rate is distributed to succeeding fluid objects: `"Evenly distributed"` or `"Percentage"`. |
| `ExitStrategyPercentageValues` | Attribute (`array`) | Sets the proportional flow-rate distribution for **Exit Strategy > Percentage**. Percentages need not sum to 100%; successors with `0` receive no material, and an unavailable successor's share is redistributed. |
| `OutflowRate` | Attribute (`real`) | Sets the outflow rate (liters/second) to the next object. Default `-1` means "same as predecessor". Applies after a `FluidSource`, `DePortioner`, `Tank`, or `Mixer`. |
| `PipeOpened` | Attribute (`boolean`) | Opens (`true`) or closes (`false`) the Pipe, modeling a valve/gate valve. A closed Pipe shows **Pipe Closed** in cyan. |

## Usage

Set/get attribute values via dialog controls or in SimTalk:

```simtalk
Pipe.PipeOpened := true        -- set
print Pipe.PipeOpened          -- get
```

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (context menu of the Class Library, or press **F8** on the Home ribbon tab of the Frame).

## Related Object

- **FluidSource** — produces the ingredients (bulk goods or fluids) of the product. Add via **Manage Class Library > Basic Objects > Fluids > FluidSource**.
- **FluidDrain** — removes processed and mixed products from the plant.
