# Read-Only Attributes of the Exporter

The Exporter provides the read-only attributes listed below, along with the `_Read-Only Attributes of All Objects`.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, on the tab **Statistics**).

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the F8 key, or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print .Resources.myExporter:2.AvailableForMediation
```

---

## hasService [SimTalk]

Returns whether the Exporter/Worker designated by `<Path>` supports the designated service (`true`) or not (`false`).

- **Type:** Method
- **Syntax:**

```simtalk
<Path>.hasService(ServiceName:string) → boolean
```

- **Parameter:** `ServiceName` (string) designates the name of the service.
- **Return Value:** boolean

**Example:**

```simtalk
MyExporter.hasService("drill")
```

**See also:** Services [Exporter], Exported Services [Exporter], Exported Services [Worker]

---

## AvailableForMediation [SimTalk]

Returns whether the Exporter designated by `<Path>` can be brokered (`true`) or not (`false`).

- **Type:** Read-only attribute (watchable)
- **Syntax:**

```simtalk
<Path>.AvailableForMediation → boolean
```

- **Return Value:** boolean — `true` if the Exporter is not failed, not paused, and has available capacity.

**Example:**

```simtalk
print .UserObjects.MyExporter:2.AvailableForMediation
```

---

## FreeCapacity [SimTalk]

Returns the capacity which the Exporter designated by `<Path>` can provide at the moment.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.FreeCapacity → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.FreeCapacity
```

**See also:** Tab Statistics [Exporter]

---

## MediatedCapacity [SimTalk]

Returns the capacity which the Exporter designated by `<Path>` brokers at the moment.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.MediatedCapacity → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.MediatedCapacity
```

**See also:** Tab Statistics [Exporter]

---

## StatExporterFailedCount [SimTalk]

Returns how often the Exporter designated by `<Path>` was failed.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterFailedCount → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatExporterFailedCount
```

---

## StatExporterFailedDelta [SimTalk]

Returns the standard deviation of the failure time of the Exporter designated by `<Path>` from the mean value.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterFailedDelta → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatExporterFailedDelta
```

---

## StatExporterFailedMu [SimTalk]

Returns the mean duration of a failure of the Exporter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterFailedMu → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatExporterFailedDelta
```

---

## StatExporterFailedPortion [SimTalk]

Returns the ratio of the times during which the Exporter designated by `<Path>` was failed to the statistics collection period of the Exporter.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterFailedPortion → real
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatExporterFailedPortion
```

**See also:** Tab Statistics [Exporter], Tab Statistics [Worker], Statistics report — Service Statistics — States — Capacities and States of the Exporters

---

## StatExporterFailedTime [SimTalk]

Returns the total time during which the Exporter designated by `<Path>` was failed.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterFailedTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatExporterFailedTime
```

---

## StatExporterOperationalPortion [SimTalk]

Returns the ratio of the working time of the Exporter designated by `<Path>` to the statistics collection period of the Exporter.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterOperationalPortion → real
```

- **Return Value:** real

> **Note:** As the Exporter computes the values that apply to the state *working*, it only provides the read-only attributes `StatExporterOperationalPortion` and `StatExporterOperationalTime`.

**Example:**

```simtalk
print MyExporter.StatExporterOperationalPortion
```

**See also:** Tab Statistics of the Exporter, Statistics report — Service Statistics — States — Capacities and States of the Exporters

---

## StatExporterOperationalTime [SimTalk]

Returns the total time taken up by working processes of the Exporter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterOperationalTime → time
```

- **Return Value:** time

> **Note:** As the Exporter computes the values that apply to the state *working*, it only provides the read-only attributes `StatExporterOperationalPortion` and `StatExporterOperationalTime`.

**Example:**

```simtalk
print MyExporter.StatExporterOperationalTime
```

---

## StatExporterPausedCount [SimTalk]

Returns how often the Exporter designated by `<Path>` was paused.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterPausedCount → time
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatExporterPausedCount
```

---

## StatExporterPausedDelta [SimTalk]

Returns the standard deviation of the paused time of the Exporter designated by `<Path>` from the mean value.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterPausedDelta → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatExporterPausedDelta
```

---

## StatExporterPausedMu [SimTalk]

Returns the mean duration of a pause of the Exporter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterPausedMu → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatExporterPausedMu
```

---

## StatExporterPausedPortion [SimTalk]

Returns the ratio of the paused time of the Exporter designated by `<Path>` to the statistics collection period of the Exporter.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterPausedPortion → real
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatExporterPausedPortion
```

**See also:** Tab Statistics [Exporter], Tab Statistics [Worker], Statistics report — Service Statistics — States — Capacities and States of the Exporters

---

## StatExporterPausedTime [SimTalk]

Returns the total time during which the Exporter designated by `<Path>` was paused.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterPausedTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatExporterPausedTime
```

---

## StatExporterUnplannedCount [SimTalk]

Returns how often the Exporter designated by `<Path>` was not planned to work.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterUnplannedCount → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatExporterUnplannedCount
```

---

## StatExporterUnplannedDelta [SimTalk]

Returns the standard deviation of the unplanned time of the Exporter designated by `<Path>` from the mean value.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterUnplannedDelta → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatExporterUnplannedDelta
```

---

## StatExporterUnplannedMu [SimTalk]

Returns the mean duration of the unplanned time of the Exporter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterUnplannedMu → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatExporterUnplannedMu
```

---

## StatExporterUnplannedPortion [SimTalk]

Returns the ratio of the unplanned time to the statistics collection period of the Exporter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterUnplannedPortion → real
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatExporterUnplannedPortion
```

**See also:** Tab Statistics [Exporter], Tab Statistics [Worker], Statistics report — Service Statistics — States — Capacities and States of the Exporters

---

## StatExporterUnplannedTime [SimTalk]

Returns the total time during which the Exporter designated by `<Path>` was not planned to work.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatExporterUnplannedTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatExporterUnplannedTime
```

---

## StatMaxFreeCapacity [SimTalk]

Returns the maximum capacity which the Exporter designated by `<Path>` can provide.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatMaxFreeCapacity → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatMaxFreeCapacity
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Capacities and States of the Exporters

---

## StatMaxMediatedCapacity [SimTalk]

Returns the maximum occupied capacity of the Exporter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatMaxMediatedCapacity → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatMaxMediatedCapacity
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Capacities and States of the Exporters

---

## StatMinFreeCapacity [SimTalk]

Returns the minimum capacity which the Exporter designated by `<Path>` can provide.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatMinFreeCapacity → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatMinFreeCapacity
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Capacities and States of the Exporters

---

## StatMinMediatedCapacity [SimTalk]

Returns the minimum occupied capacity of the Exporter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatMinMediatedCapacity → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatMinMediatedCapacity
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Capacities and States of the Exporters

---

## StatServicesFailedCount [SimTalk]

Returns how often the services of the Exporter designated by `<Path>` were failed.

> **Remarks:** The Exporter only collects failure times for the services if you activate `FailServices`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesFailedCount → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatServicesFailedCount
```

---

## StatServicesFailedPortion [SimTalk]

Returns the portion of the failed times of the services of the overall statistics time of the Exporter designated by `<Path>`, weighted with the capacity.

> **Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.
>
> **Note:** The Exporter only collects failure times for the services if you activate `FailServices`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesFailedPortion → real
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatServicesFailedPortion
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesFailedTime [SimTalk]

Returns the total time during which services of the Exporter designated by `<Path>` were failed.

> **Remarks:** The Exporter only collects failure times for the services if you activate `FailServices`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesFailedTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatServicesFailedTime
```

---

## StatServicesRepairingCount [SimTalk]

Returns how often the services of the Exporter designated by `<Path>` worked on repairs.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesRepairingCount → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatServicesRepairingCount
```

---

## StatServicesRepairingPortion [SimTalk]

Returns the portion of the repairing time of the services of the overall statistics time of the Exporter designated by `<Path>`, weighted with the capacity.

> **Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesRepairingPortion → real
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatServicesRepairingPortion
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesRepairingTime [SimTalk]

Returns the total time which the services of the Exporter designated by `<Path>` spent for repairs.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesRepairingTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatServicesRepairingTime
```

---

## StatServicesSetupCount [SimTalk]

Returns how often the services of the Exporter designated by `<Path>` were setting the station up.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesSetupCount → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatServicesSetupCount
```

---

## StatServicesSetupPortion [SimTalk]

Returns the portion of the set-up time of the services of the overall statistics time of the Exporter designated by `<Path>`, weighted with the capacity.

> **Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.
>
> **Note:** If a station changes to the state failed and/or unplanned or paused and if then services for setting-up or processing are brokered, the services remain brokered. The set-up time and the processing time for the services thus continues while the station is failed.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesSetupPortion → real
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatServicesSetupPortion
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesSetupTime [SimTalk]

Returns the total time the services of the Exporter designated by `<Path>` were setting the station up.

> **Note:** If a station changes to the state failed and/or unplanned or paused and if then services for setting-up or processing are brokered, the services remain brokered. The set-up time and the processing time for the services thus continues while the station is failed.
>
> **Note:** If a station changes to the state failed and services for setting-up or processing are brokered for this station, the services remain assigned. For this reason the set-up time and the processing time for the services carry on running while the station is failed. To avoid this, activate `FailServices`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesSetupTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatServicesSetupTime
```

---

## StatServicesWaitingImpCount [SimTalk]

Returns how often the services of the Exporter designated by `<Path>` waited for an importer.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWaitingImpCount → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatServicesWaitingImpCount
```

---

## StatServicesWaitingImpPortion [SimTalk]

Returns the portion of the overall statistics time which the services of the Exporter designated by `<Path>` spent waiting for an importer, weighted with the capacity.

> **Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWaitingImpPortion → real
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatServicesWaitingImpPortion
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesWaitingImpTime [SimTalk]

Returns the total waiting time of the services of the Exporter designated by `<Path>` for an importer.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWaitingImpTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatServicesWaitingImpTime
```

---

## StatServicesWaitingMUCount [SimTalk]

Returns how often the services of the Exporter designated by `<Path>` spent waiting for a MU at the importer.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWaitingMUCount → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatServicesWaitingMUCount
```

---

## StatServicesWaitingMUPortion [SimTalk]

Returns the waiting portion for a MU at the importer of the services of the overall statistics time of the Exporter designated by `<Path>`, weighted with the capacity.

> **Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWaitingMUPortion → real
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatServicesWaitingMUPortion
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesWaitingMUTime [SimTalk]

Returns the total time the services of the Exporter designated by `<Path>` were waiting at the importer for a MU.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWaitingMUTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatServicesWaitingMUTime
```

---

## StatServicesWaitingPortion [SimTalk]

Returns the portion of the waiting time of the services of the overall statistics time of the Exporter designated by `<Path>`, weighted with the capacity.

> **Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.
>
> **Note:** The value of `StatServicesWaitingPortion` is the sum of `StatServicesWaitingImpPortion` and `StatServicesWaitingMUPortion`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWaitingPortion → time
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatServicesWaitingPortion
```

---

## StatServicesWaitingTime [SimTalk]

Returns the time which the services of the Exporter designated by `<Path>` were waiting in relation to the statistics collection period, weighted with the capacity.

> **Remarks:** The value of `StatServicesWaitingTime` is the sum of `StatServicesWaitingImpTime` and `StatServicesWaitingMUTime`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWaitingTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatServicesWaitingTime
```

---

## StatServicesWorkingCount [SimTalk]

Returns the number of working processes which the services of the Exporter designated by `<Path>` provided.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWorkingCount → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatServicesWorkingCount
```

---

## StatServicesWorkingPortion [SimTalk]

Returns the portion of the working time of the services of the overall statistics time of the Exporter designated by `<Path>`, weighted with the capacity.

> **Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.
>
> **Note:** If a station changes to the state failed and/or unplanned or paused and if then services for setting-up or processing are brokered, the services remain brokered. The set-up time and the processing time for the services thus continues while the station is failed.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWorkingPortion → real
```

- **Return Value:** real

**Example:**

```simtalk
print MyExporter.StatServicesWorkingPortion
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesWorkingTime [SimTalk]

Returns the time taken up by working processes of the services of the Exporter designated by `<Path>`.

> **Remarks:** If a station changes to the state failed and/or unplanned or paused and if then services for setting-up or processing are brokered, the services remain brokered. The set-up time and the processing time for the services thus continues while the station is failed. To avoid this, activate `FailServices`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatServicesWorkingTime → time
```

- **Return Value:** time

**Example:**

```simtalk
print MyExporter.StatServicesWorkingTime
```

---

## StatSumFreeCapacity [SimTalk]

Returns the sum of the free capacity of the Exporter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatSumFreeCapacity → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatSumFreeCapacity
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Capacities and States of the Exporters

---

## StatSumMediatedCapacity [SimTalk]

Returns the sum of the brokered capacity of the Exporter designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.StatSumMediatedCapacity → integer
```

- **Return Value:** integer

**Example:**

```simtalk
print MyExporter.StatSumMediatedCapacity
```

**See also:** Tab Statistics [Exporter], Statistics report — Service Statistics — States — Capacities and States of the Exporters
