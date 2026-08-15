# Read-Only Attributes of the AssemblyStation — Summary

This directory documents the read-only attributes of the `AssemblyStation` material flow object. In addition to these object-specific attributes, the `AssemblyStation` also inherits the read-only attributes of all objects and of the material flow objects.

Read-only attributes can only be queried, not set — Plant Simulation computes their values at the point in time they are queried. They typically correspond to unavailable dialog items (e.g., on the **Statistics** tab).

## How to query

Open the **Show Attributes and Methods** window (F8 on the Home ribbon tab for an instance, or via the context menu of the Class Library), or query directly, e.g.:

```simtalk
print AssemblyStation.StatWaitingPartsCount
```

## Related method

- **`statWaitingTimeTable(WaitingTimes:table) → boolean`** — Writes waiting-time statistics into the table `WaitingTimes`. Returns `false` for the settings *MU Types* and *Depends on Main MU*.

## Read-only attributes overview

| Attribute | Return type | Description |
| --- | --- | --- |
| `NumMUsToBeDeleted` | `integer` | Number of MUs from the table *MUs To Be Deleted*. |
| `StatWaitingPartsCount` | `integer` | How often the station was waiting for mounting parts. |
| `StatWaitingPartsDelta` | `real` | Deviation from the mean waiting time for MUs (parts). |
| `StatWaitingPartsMu` | `real` | Mean waiting time for MUs (parts). |
| `StatWaitingPartsPortion` | `real` | Portion of the statistics period spent waiting for mounting parts. |
| `StatWaitingPartsTime` | `time` | Total time spent waiting for MUs (parts). |
| `StatWaitingResCount` | `integer` | How often the station was waiting for mounting parts and/or processing-Exporters/processing-services. |
| `StatWaitingResDelta` | `real` | Standard deviation of waiting times for parts and/or services. |
| `StatWaitingResMu` | `real` | Average waiting time for parts and/or services. |
| `StatWaitingResPortion` | `real` | Ratio of waiting time (parts and/or services) to the statistics collection period. |
| `StatWaitingResTime` | `time` | Total time spent waiting for parts and/or services. |

## Grouping

The statistics attributes form two parallel families, each tracking the same five statistics (count, deviation/delta, mean/mu, portion, and total time):

- **Parts waiting** (`StatWaitingParts*`): waiting for mounting parts (MUs).
- **Resources waiting** (`StatWaitingRes*`): waiting for mounting parts and/or processing-Exporters/processing-services.
