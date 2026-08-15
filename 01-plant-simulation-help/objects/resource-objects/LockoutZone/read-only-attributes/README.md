# LockoutZone — Read-Only Attributes

Summary of the read-only attributes (and the related method) of the **LockoutZone** resource object.

## General

The LockoutZone provides read-only attributes and the _Read-Only Attributes of All Objects_. You can query their values but cannot set them — Plant Simulation computes each value at the point in time you query it. Most read-only attributes correspond to an unavailable dialog item on one of the object's tabs (for example, the **Statistics** tab).

To inspect all methods, read-only attributes, and attributes, open the **Show Attributes and Methods** window:

- In the **Class Library**, select **Show Attributes and Methods** from the context menu of the selected Class.
- In a Frame, select the instance and press **F8** (or click **Show Attributes and Methods** on the Home ribbon tab).

Example query:

```simtalk
print MyLockoutZone.StatStoppedCount
```

## Method

| Name | Type | Syntax | Returns |
| --- | --- | --- | --- |
| `addObject` | Method | `<Path>.addObject(NameOfObject:path) → boolean` | Adds the object designated by `NameOfObject` to the LockoutZone. |

## Read-only attributes

All `Stat*` attributes below are reported on the **Statistics** tab and are read from a LockoutZone referenced by `<Path>`.

| Attribute | Return type | Description | Watchable |
| --- | --- | --- | --- |
| `StatStoppedCount` | integer | How often the LockoutZone stopped the assigned stations. | yes |
| `StatStoppedDelta` | time | Standard deviation of the time the LockoutZone stopped the stations' processing operations. | yes |
| `StatStoppedIntervalDelta` | time | Standard deviation of the intervals during which the LockoutZone stopped the stations. | yes |
| `StatStoppedIntervalMu` | time | Mean time of the intervals during which the LockoutZone stopped the stations. | yes |
| `StatStoppedIntervalTime` | time | Total time of the intervals during which the LockoutZone stopped the stations. | no |
| `StatStoppedMu` | time | Mean time the LockoutZone stopped the stations' processing operations. | yes |
| `StatStoppedPortion` | real | Portion of the statistics collection period during which the stations were stopped. | yes |
| `StatStoppedTime` | time | Total time the LockoutZone stopped the stations' processing operations. | yes |

### Syntax

```simtalk
<Path>.StatStoppedCount         → integer
<Path>.StatStoppedDelta         → time
<Path>.StatStoppedIntervalDelta → time
<Path>.StatStoppedIntervalMu    → time
<Path>.StatStoppedIntervalTime  → time
<Path>.StatStoppedMu            → time
<Path>.StatStoppedPortion       → real
<Path>.StatStoppedTime          → time
```

### Examples

```simtalk
print MyLockoutZone.StatStoppedCount
print MyLockoutZone.StatStoppedDelta
print MyLockoutZone.StatStoppedIntervalDelta
print MyLockoutZone.StatStoppedIntervalMu
print MyLockoutZone.StatStoppedIntervalTime
print MyLockoutZone.StatStoppedMu
print MyLockoutZone.StatStoppedPortion
print MyLockoutZone.StatStoppedTime
```
