# Portioner — General (Summary)

This README summarizes the content of [`general.md`](general.md) for the **Portioner** fluid object.

## Overview

The **Portioner** is a fluid object that turns a free-flowing product into a mobile object (MU). The resulting MUs can then be connected to material-flow objects for further processing. It is the counterpart of the **DePortioner**.

## Adding the Object to a Model

- Path: **Manage Class Library > Basic Objects > Fluids > Portioner** (Home ribbon tab).
- Sample models: **Window > Start Page > Getting Started > Example Models > Small Examples**.

## Dialog Box / Tabs

| Tab | Purpose / Key items |
| --- | --- |
| **Attributes** | `MU` (SimTalk `MUPath`), `Amount per MU` (`AmountPerMU`), `Fluid from Predecessor` (`PredecessorNumber`), `Current Amount` (`CurrentAmount`), `Current Inflow Rate` (`CurrentInFlowrate`), `Current Material` (`CurrentMaterial`) |
| **Times** | Processing-time distributions; set via `setTypeAndAttr` (supports `Const`) |
| **Failures** | Failure modeling |
| **Controls** | Entrance/Exit controls; create controls as object Methods (e.g. `self.OnEntrance`) |
| **Exit** | Successor selection / exit strategy |
| **Statistics** | Resource statistics |
| **Importer** | Services (processing, set-up, failure) |
| **User-defined** | Custom attributes |

## Menus

- **Navigate**, **View**, **Tools**, **Help** menus (standard object menus).
- **View** menu additionally exposes Importer-related commands (Exporters, Services, Unavailable Services, Associated Workplaces).

## Methods

The Portioner provides the methods of the **Fluid Objects** and of **All Objects**.

## See Also

- Portion and Deportion Materials
- Simulate Free-flowing Materials and Fluids
- Configure the Portioner (pouring chocolate bars / portioning the product)
