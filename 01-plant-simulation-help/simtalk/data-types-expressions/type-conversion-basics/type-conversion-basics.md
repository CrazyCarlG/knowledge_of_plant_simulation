# Converting Data Types

You cannot always combine variables and constants of different data types. You may have to convert them before an operation can be executed on them.

## Automatically Converting Data Types

Plant Simulation automatically converts numeric values. You have to explicitly start all other type conversions.

- Plant Simulation automatically converts the data type `integer` to `real` and vice versa.
- When you assign a `real` value to an `integer` variable, the digits after the decimal point will be lost.
- When parameters are passed, Plant Simulation automatically converts the data type `real` to `integer` and vice versa.
- The same is true for the data types `dateTime` and `date`. Here, Plant Simulation deletes the time part.

During calculations Plant Simulation treats the units of the physical data types `length`, `weight`, `speed`, `acceleration`, and `time` as real numbers.

- If a calculation results in another physical data type, Plant Simulation assigns the result the corresponding data type.
- The quotient of `length` and `time` is assigned the data type `speed`.
- If the result cannot be assigned a physical data type, Plant Simulation uses `real` instead.

You can only assign a value with the correct unit or a value without a unit (`real` or `integer`) to a local variable of physical data types (`length`, `weight`, `speed`, `acceleration`, `time`). In all other cases the assignment throws an error to point out a potential problem.

> **Note**
> Automatic conversion from `real` to `integer` will truncate decimal places, similar to the TRUNC function in Excel.

Currently, we provide two workarounds for this:

Use the `round` function:

```simtalk
var realVal := pi
var intVal : integer := round(realVal)
```

Add the value `0.5`:

```simtalk
var realVal := pi
var intVal : integer := realVal + 0.5
```

---

*Source: 12-206 Plant Simulation Help — Unpublished work. © 2026 Siemens*
