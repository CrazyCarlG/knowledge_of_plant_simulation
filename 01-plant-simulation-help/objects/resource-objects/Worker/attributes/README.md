# Worker Attributes — Overview

This directory documents the **attributes of the Worker** object in Plant Simulation. The Worker is an **Exporter object with a capacity of 1**, so in addition to its own attributes it inherits the `_Attributes of the Exporter` and the `Attributes of All Objects`.

Use the window **Show Attributes and Methods** to view all methods, read-only attributes, and attributes of a Worker.

Values can be set and read either through the dialog windows (check boxes, text boxes, drop-down lists) or by assignment in SimTalk:

```simtalk
.Resources.MyWorker:2.Efficiency := 90       -- set a value
print .Resources.Worker.MyWorker:2.Efficiency -- get a value
```

## Attribute Summary

| Attribute | Type | Data Type | Description |
|-----------|------|-----------|-------------|
| `StatTraveledDistance` | Read-only | `length` | Distance (m) the Worker walked between WorkerPool and Workplaces/stations. Without a FootPath the Worker is beamed. |
| `AutomaticMediation` | Attribute | `boolean` | `true` lets the Broker assign the Worker automatically; `false` means you assign it yourself. |
| `BrokerPath` | Attribute | `object` | Path to the Broker that brokers the Worker's services. |
| `Efficiency` | Attribute | `integer` | How fast the Worker performs a job (100% = specified time, 200% = half, 50% = double). |
| `HomeLocation` | Attribute | `object` | Workplace the Worker walks to after finishing its current job. |
| `IsIdle` | Attribute (watchable) | `boolean` | `true` = Worker is idle (not working). Works with `NumIdleWorkers` / `getIdleWorker`. |
| `OrderCtrl` | Attribute | `method` | Method called whenever the Worker is assigned to an importer. |
| `Priority` | Attribute | `integer` | Urgency of a work order; higher priority is brokered first. |
| `ReleaseCtrl` | Attribute | `method` | Method executed as soon as an importer releases the Worker. |
| `Scope` | Attribute | `array[]` (string) | Objects to which the Worker can be brokered for a job. |
| `Services` | Attribute | `array[]` (string) | Names of the Services the Worker provides (case-insensitive). |
| `Shift` | Attribute | `string` | Shift during which the Worker works; `""` = all shifts. |
| `Speed` | Attribute | `speed` | Walking speed on a FootPath or freely within the area. |
| `Stopped` | Attribute | `boolean` | Stops (`true`) or continues (`false`) the Worker on its way. |
| `WorkerPool` | Attribute | `object` | The WorkerPool to which the Worker belongs. |
| `XDim` | Attribute (watchable) | `integer` | Number of parts the Worker can carry in X-Dimension. |
| `YDim` | Attribute (watchable) | `integer` | Number of parts the Worker can carry in Y-Dimension. |
| `ZDim` | Attribute (watchable) | `integer` | Number of parts the Worker can carry in Z-Dimension (stacking, 3D only). |

### Carrying Capacity

The carrying capacity of a Worker is the product `XDim × YDim × ZDim`; the maximum allowed value is one million. Decreasing the capacity may delete occupied places, so parts must be moved or deleted first.

### Importer Type Codes

The `OrderCtrl` and `ReleaseCtrl` methods receive two parameters — `Importer` (object) and `Type` (integer):

| Type | Importer |
|------|----------|
| `0` | Failure / remove-failure importer |
| `1` | Set-up importer |
| `2` | Processing importer |
| `3` | Transport importer |

## Exporter (parent object)

The Worker is an **Exporter** — an object for providing and exporting services, representing a group of people whose individual members cannot be distinguished or addressed individually.

- Works together with the **Broker** and the **Importers** of the Station, ParallelStation, AssemblyStation, and DismantleStation.
- A single Broker manages the Exporter and assigns it to Importers; after finishing a service it registers as available again.
- If an Importer requests several services at once, all must be available before assignment.
- An Exporter with capacity > 1 can serve several Importers simultaneously. Use it when transit times for traveled distances are not important.

## Related SimTalk Methods

- `goTo`, `importExporter` (with `AutomaticMediation`)
- `getIdleWorker`, `NumIdleWorkers` (with `IsIdle`)
- `findNewImporter` (with `ReleaseCtrl`)
- `setWorkersToCreateTable` (with `HomeLocation`)
- `XDim`, `YDim`, `ZDim` (mutually related carrying-capacity attributes)

## Source Files

- `attributes.md` — main markdown reference for Worker attributes.
- `attributes.txtx` — raw help-text export (contains the same content).
