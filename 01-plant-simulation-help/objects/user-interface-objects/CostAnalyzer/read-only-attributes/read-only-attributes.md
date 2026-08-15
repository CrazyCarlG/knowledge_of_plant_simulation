# Read-Only Attributes of the CostAnalyzer

## Overview

The CostAnalyzer provides the **Read-Only Attributes of All Objects**.

You can query the values of the read-only attributes, but you cannot set them — Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the **Statistics** tab.

## Viewing Methods and Attributes

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the **Home** ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyCostAnalyzer.UUID
```

## Attributes of the CostAnalyzer

The CostAnalyzer provides:

- The attribute `CollectData`.
- The **Attributes of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

## Methods

### `putPieceCostsIntoTable` [SimTalk]

Writes the piece costs, which the CostAnalyzer designated by `<Path>` computed, into the specified DataTable.

- **Type:** Method
- **Syntax:**

```simtalk
<Path>.putPieceCostsIntoTable(DataTable:table)
```

- **Parameter:** The parameter `DataTable` of data type `table` designates the DataTable into which Plant Simulation writes the piece costs.
- **Example:**

```simtalk
CostAnalyzer.putPieceCostsIntoTable(MyPieceCosts)
```

### `getPieceCostsTable` [SimTalk]

**See also:** Costs Shown in the Costs Report.

## Related Topics

- Costs Shown in the Costs Report
- Read-Only Attributes of the CostAnalyzer
- Attributes of the CostAnalyzer
