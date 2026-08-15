# README — Read-Only Attributes of the CostAnalyzer

This folder documents the **read-only attributes of the CostAnalyzer** object in Plant Simulation.

## Summary

The CostAnalyzer provides the **Read-Only Attributes of All Objects**. These attributes can be queried but not set — Plant Simulation computes their value at the point-in-time the attribute is queried. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

## Viewing Methods and Attributes

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- In the **Class Library**, select **Show Attributes and Methods** on the context menu to show the selected Class.
- In a **Frame**, press **F8** or click **Show Attributes and Methods** on the **Home** ribbon tab to show the selected Instance.

Example query of a read-only attribute:

```simtalk
print MyCostAnalyzer.UUID
```

## Attributes of the CostAnalyzer

The CostAnalyzer provides:

- The attribute `CollectData`.
- The **Attributes of All Objects**.

## Methods

- **`putPieceCostsIntoTable`** [SimTalk] — Writes the piece costs computed by the CostAnalyzer designated by `<Path>` into the specified DataTable.

  ```simtalk
  <Path>.putPieceCostsIntoTable(DataTable:table)
  ```

  Parameter `DataTable` (data type `table`) designates the destination DataTable.

  ```simtalk
  CostAnalyzer.putPieceCostsIntoTable(MyPieceCosts)
  ```

- **`getPieceCostsTable`** [SimTalk] — See also: *Costs Shown in the Costs Report*.

## Related Topics

- Costs Shown in the Costs Report
- Read-Only Attributes of the CostAnalyzer
- Attributes of the CostAnalyzer
