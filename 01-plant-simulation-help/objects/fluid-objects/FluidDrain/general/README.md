# FluidDrain — General Documentation Summary

This directory contains the general help documentation for the **FluidDrain** object in Plant Simulation.

## Files in this directory

- `general.md` — Markdown version of the FluidDrain help topic.
- `general.txtx` — Text extraction of the same help topic (includes page numbers and copyright footers).

> No subfolders are present in this directory, so there are no nested README files to summarize.

## Overview

The **FluidDrain** removes the free-flowing materials that the **FluidSource** introduced into the plant, after those materials have been mixed and processed. It differentiates the materials by their names.

Key facts:

- Change the length of the graphic and its anchor points via **Show Manipulators** on the Edit ribbon tab, or by pressing `M`.
- Hover over the object to show a tooltip with information about it.
- Add it to the model via **Manage Class Library > Basic Objects > Fluids > FluidDrain** on the Home ribbon tab.
- Example models: **Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples**.

## Dialog Box

Double-click the FluidDrain icon to open its dialog box.

- **Simulation properties** — shared properties are described under *Dialog Items of the Objects*.
- **3D / animation properties** — open the *Edit 3D Properties* dialog by clicking **Edit 3D Properties** (lower left of the simulation properties dialog) or by selecting the object and pressing the spacebar.

## Tabs

| Tab | Description |
| --- | --- |
| **Attributes** | Object-specific settings (see below). |
| **Failures** | Define failures as described under *Tab Failures*. |
| **Statistics** | Resource statistics plus the FluidDrain-specific values listed below. |
| **User-defined** | Define custom attributes as described under *Tab User-defined*. |

### Tab Attributes

- **Shift Calendar** — select the ShiftCalendar that controls during which shifts the FluidDrain works. SimTalk: `ShiftCalendarObject`.
  - Select it via the ellipsis button (dialog *Select Object*), or drag-and-drop it from a Frame into the text box.
- **Current Inflow Rate** — shows the amount (in liters per second) of material flowing into the FluidDrain and being drained from the plant. SimTalk: `CurrentInFlowrate`.

### Tab Statistics

Additional values shown beyond the standard resource statistics:

| Item (English) | Description | Item (German) |
| --- | --- | --- |
| Total Throughput | Amount of material drained from the plant. | Gesamtdurchsatz |
| Throughput per Hour | Amount drained per hour while available. | Durchsatz pro Stunde |
| Throughput per Day | Amount drained per day while available (throughput per hour × 24). | Durchsatz pro Tag |
| Maximum Flow Rate | Maximum flow rate (liters per second) through the FluidDrain. | Maximale Flußrate |

**Detailed Statistics Table** (`typeStatistics`) itemizes the drained materials:

| Column | Description |
| --- | --- |
| Material | Name of the material drained from the plant. |
| Throughput | Total amount of that material drained from the plant. |

## Menus

- **Navigate Menu** — described under *Navigate Menu*.
- **View Menu** — described under *View Menu*; SimTalk: `updateDialog`.
- **Tools Menu** — described under *Navigate Menu*.
- **Help Menu** — described under *Help Menu*.

## Methods

The FluidDrain provides:

- The method `typeStatistics` [SimTalk] — FluidDrain.
- The Methods of the Fluid Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open the window *Show Attributes and Methods* (via the Class Library context menu, the `F8` key, or **Show Attributes and Methods** on the Home ribbon tab of the Frame).

## See also

- FluidSource
- Simulate Free-flowing Materials and Fluids
