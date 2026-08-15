# Read-Only Attributes of the Worker

The Worker provides:

- The read-only attributes listed in the table of contents to the left.
- All read-only attributes of the Exporter, as the Worker is an Exporter with the capacity of 1.
- The read-only attributes of all objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print .Resources.Worker:1.StatTraveledDistance
```

---

## AvailableForMediation [SimTalk] - Worker

Returns if the Worker designated by `<Path>` can be brokered to do a job (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Watchable:** The read-only attribute is watchable.

### Syntax

```simtalk
<Path>.AvailableForMediation → boolean
```

### Return Value

The return value has the data type `boolean`.

`true` if the Worker is not failed, not paused, does not carry parts, and if he is not brokered.

### Example

```simtalk
print .Resources.MyWorker:2.AvailableForMediation
```

---

## CurrentSpeed [SimTalk] - Worker

Returns the current speed with which the Worker designated by `<Path>` walks on the Footpath or freely within the area.

- **Type:** Read-only attribute
- **Watchable:** The read-only attribute is watchable. By watching it, you might, for example, detect the event when the speed of a Worker changes.

### Syntax

```simtalk
<Path>.CurrentSpeed → speed
```

### Return Value

The return value has the data type `speed`.

It is the speed which you set. `0` if the Worker is failed or stopped or if he is located in the WorkerPool or on a Workplace.

### Example

```simtalk
print .UserObjects.MyWorker:1.CurrentSpeed
```

**See also:** Speed [Worker]

---

## HasOrder [SimTalk] - Worker

Returns if the Worker designated by `<Path>` has the order to transport parts, currently transports parts, or just exports services.

- **Type:** Read-only attribute
- **Watchable:** The attribute is watchable.

### Syntax

```simtalk
<MU-Path>.HasOrder -> boolean
```

### Return Value

The return value has the data type `boolean`.

### Example

```simtalk
waituntil not Worker.HasOrder   -- wait until the Worker is idle, has no
                                 -- order, or carries no parts
 mu.move                         -- transfer the MU, which should place an
                                 -- order for the Worker to transport it
```

---

## ResCurrentState [SimTalk] - Worker

Returns the current state of the Worker designated by `<Path>`.

**Remarks:** During a simulation run the Worker can take on one of these states as described on the Tab Statistics: `Services Setting-up`, `Services Processing`, `Services Repairing`, `Services Transporting`, `Services En-route to Job`, `Services Waiting`, `Exporter Paused`, `Exporter Unplanned`, or `Exporter failed`.

**Note:** If two states occur at the same time, for example Paused and Failed, the read-only attribute returns the state that also has precedence for statistics collection. Paused for example for Paused and Failed.

- **Type:** Read-only attribute
- **Watchable:** The read-only attribute is watchable. Use it in `waituntil`-instructions or to make the object TimeSequence record it in watch mode.

### Syntax

```simtalk
<Path>.ResCurrentState → string
```

### Return Value

The return value has the data type `string`.

`VOID` if Exporter statistics is turned off.

### Example

```simtalk
print .Resources.John.ResCurrentState   -- class
print .Resources.John:1.ResCurrentState -- instance
```

**See also:** Resource Statistics [material flow objects], Tab Statistics [Worker]

---

## StatServicesEnRouteIdleCount [SimTalk]

Returns how often the Worker designated by `<Path>` was on his way without having an order.

**Remarks:** The overall statistics time is the statistics collection time without the Unplanned Time and the Paused Time.

This means that he was on his way, while he could be brokered. This occurs, for example, if you clear `Get Job Orders at Home Only` and also clear `Worker Stays Here After Completing the Job` at the Workplace. If you send the Worker to a Workplace with the method `goTo`, then this will also be added to the value `StatServicesEnRouteIdleCount`.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesEnRouteIdleCount → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesEnRouteIdleCount
```

**See also:** `goTo` [SimTalk], Get Job Orders At Home Only, Worker Stays Here After Completing the Job

---

## StatServicesEnRouteIdlePortion [SimTalk]

Returns the portion of the overall statistics time during which the Worker designated by `<Path>` was en-route without being assigned a job order.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

This means that he was on his way, while he could be brokered. This occurs, for example, if you clear `Get Job Orders at Home Only` and also clear `Worker Stays Here After Completing the Job` at the Workplace. If you send the Worker to a Workplace with the method `goTo`, then the time he was on this way will also be added to the value `StatServicesEnRouteIdlePortion`.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesEnRouteIdlePortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesEnRouteIdlePortion
```

**See also:** `goTo` [SimTalk], Tab Statistics [Worker], Statistics report — Service Statistics — States — Time Portions of the Exporters, Get Job Orders At Home Only, Worker Stays Here After Completing the Job

---

## StatServicesEnRouteIdleTime [SimTalk]

Returns the total time during which the Worker designated by `<Path>` was en-route without having a job.

**Remarks:** This means that he was on his way, while he could be brokered. This occurs, for example, if you clear `Get Job Orders at Home Only` and also clear `Worker Stays Here After Completing the Job` at the Workplace. If you send the Worker to a Workplace with the method `goTo`, then the time he was on this way will also be added to the value `StatServicesEnRouteIdlePortion`.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesEnRouteIdleTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesEnRouteIdleTime
```

**See also:** `goTo` [SimTalk], Get Job Orders At Home Only, Worker Stays Here After Completing the Job

---

## StatServicesEnRouteToJobCount [SimTalk]

Returns how often the Worker designated by `<Path>` was en-route to a Workplace, to which he was brokered to do a job at the associated station.

**Remarks:** If you select `Get Job Orders at Home Only`, Plant Simulation also counts how often the Worker walked back to the WorkerPool to get the next order.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesEnRouteToJobCount → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesEnRouteToJobCount
```

**See also:** Get Job Orders At Home Only

---

## StatServicesEnRouteToJobPortion [SimTalk]

Returns the portion of the overall statistics time during which the Worker designated by `<Path>` was en-route to a Workplace, to which he was brokered to do a job at the associated station.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

If you select `Get Job Orders at Home Only`, Plant Simulation also counts the time during which the Worker walked back to the WorkerPool to get the next order.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesEnRouteToJobPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesEnRouteToJobPortion
```

**See also:** Tab Statistics [Worker], Statistics report — Service Statistics — States — Time Portions of the Exporters, Get Job Orders At Home Only

---

## StatServicesEnRouteToJobTime [SimTalk]

Returns the total time during which the Worker designated by `<Path>` was en-route to a Workplace for which he was brokered to do a job at the associated station.

**Remarks:** If you select `Get Job Orders at Home Only`, Plant Simulation also counts the time during which the Worker walked back to the WorkerPool to get the next order.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesEnRouteToJobTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesEnRouteToJobTime
```

**See also:** Get Job Orders At Home Only

---

## StatServicesFailedCount [SimTalk] - Worker

Returns how often the services of the Worker designated by `<Path>` were failed.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesFailedCount → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesFailedCount
```

---

## StatServicesFailedPortion [SimTalk] - Worker

Returns the portion of the failed time of the services of the overall statistics time of the Worker designated by `<Path>`.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesFailedPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesFailedPortion
```

**See also:** Tab Statistics [Worker], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesFailedTime [SimTalk] - Worker

Returns the total time during which services of the Worker designated by `<Path>` were failed.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesFailedTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesFailedTime
```

---

## StatServicesRepairingCount [SimTalk] - Worker

Returns how often the services of the Worker designated by `<Path>` worked on repairs.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesRepairingCount → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesRepairingCount
```

---

## StatServicesRepairingPortion [SimTalk] - Worker

Returns the portion of the repairing time of the services of the overall statistics time of the Worker designated by `<Path>`.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesRepairingPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesRepairingPortion
```

**See also:** Tab Statistics [Worker], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesRepairingTime [SimTalk] - Worker

Returns the total time which the services of the Worker designated by `<Path>` spent for repairs.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesRepairingTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesRepairingTime
```

---

## StatServicesSetupCount [SimTalk] - Worker

Returns how often the services of the Worker designated by `<Path>` were setting the station up.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesSetupCount → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesSetupCount
```

---

## StatServicesSetupPortion [SimTalk] - Worker

Returns the portion of the set-up time of the services of the overall statistics time of the Worker designated by `<Path>`.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

**Note:** If a station changes to the state failed and/or unplanned or paused and if then services for setting-up or processing are brokered, the services remain brokered. The set-up time and the processing time for the services thus continues while the station is failed.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesSetupPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesSetupPortion
```

**See also:** Tab Statistics [Worker], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesSetupTime [SimTalk] - Worker

Returns the total time the services of the Worker designated by `<Path>` were setting the station up.

**Remarks:** If a station fails and/or is unplanned or paused and services for setting-up or processing are brokered for this station, the services remain assigned. For this reason the set-up time and the processing time for the services continues while the station is failed.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesSetupTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesSetupTime
```

---

## StatServicesTransportingCount [SimTalk]

Returns how often the Worker designated by `<Path>` was carrying parts from Workplace to Workplace.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesTransportingCount → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesTransportingCount
```

---

## StatServicesTransportingPortion [SimTalk]

Returns the portion of the overall statistics time during which the Worker designated by `<Path>` was carrying parts from Workplace to Workplace.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesTransportingPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesTransportingPortion
```

**See also:** Tab Statistics [Worker], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesTransportingTime [SimTalk]

Returns the total time during which the Worker designated by `<Path>` was carrying parts from Workplace to Workplace.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesTransportingTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesTransportingTime
```

---

## StatServicesWaitingImpCount [SimTalk] - Worker

Returns how often the services of the Worker designated by `<Path>` waited for an importer.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWaitingImpCount → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Resources.MyWorker:2.StatServicesWaitingImpCount
```

---

## StatServicesWaitingImpPortion [SimTalk] - Worker

Returns the portion of the overall statistics time which the services of the Worker designated by `<Path>` spent waiting for an importer, weighted with the capacity.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWaitingImpPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:2.StatServicesWaitingImpPortion
```

**See also:** Tab Statistics [Worker], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesWaitingImpTime [SimTalk] - Worker

Returns the total waiting time of the services of the Worker designated by `<Path>` for an importer.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWaitingImpPortion → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:2.StatServicesWaitingImpPortion
```

---

## StatServicesWaitingMUCount [SimTalk] - Worker

Returns how often the services of the Worker designated by `<Path>` spent waiting for a MU at the importer.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWaitingMUCount → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Resources.MyWorker:2.StatServicesWaitingMUCount
```

---

## StatServicesWaitingMUPortion [SimTalk] - Worker

Returns the portion of the overall statistics time during which the services of the Worker designated by `<Path>` were waiting for a MU at the importer.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWaitingMUPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:2.StatServicesWaitingMUPortion
```

**See also:** Tab Statistics [Worker], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesWaitingMUTime [SimTalk] - Worker

Returns the total time the services of the Worker designated by `<Path>` were waiting at the importer for a MU.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWaitingMUTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:2.StatServicesWaitingMUTime
```

---

## StatServicesWaitingPortion [SimTalk] - Worker

Returns the portion of the waiting time of the services of the overall statistics time of the Worker designated by `<Path>`.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

**Note:** The value of `StatServicesWaitingPortion` is the sum of `StatServicesWaitingImpPortion` plus `StatServicesWaitingMUPortion`.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWaitingPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:2.StatServicesWaitingPortion
```

**See also:** `StatServicesWaitingImpPortion` [SimTalk] - Worker, `StatServicesWaitingMUPortion` [SimTalk] - Worker

---

## StatServicesWaitingTime [SimTalk] - Worker

Returns the time which the services of the Worker designated by `<Path>` were waiting in relation to the statistics collection period.

**Remarks:** The value of `StatServicesWaitingTime` is the sum of `StatServicesWaitingImpTime` and `StatServicesWaitingMUTime`.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWaitingTime → time
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:2.StatServicesWaitingTime
```

**See also:** `StatServicesWaitingImpTime` [SimTalk] - Exporter, `StatServicesWaitingMUTime` [SimTalk] - Exporter

---

## StatServicesWorkingCount [SimTalk] - Worker

Returns the number of working processes which the services of the Worker designated by `<Path>` provided.

**Remarks:** If a station changes to the state failed and/or unplanned or paused and if then services for setting-up or processing are brokered, the services remain brokered. The set-up time and the processing time for the services thus continues while the station is failed.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWorkingCount → integer
```

### Return Value

The return value has the data type `integer`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesWorkingCount
```

---

## StatServicesWorkingPortion [SimTalk] - Worker

Returns the working portion of the services of the overall statistics time of the Worker designated by `<Path>`.

**Remarks:** The overall statistics time is the statistics collection period without the Unplanned Time and the Paused Time.

**Note:** If a station changes to the state failed and/or unplanned or paused and if then services for setting-up or processing are brokered, the services remain brokered. The set-up time and the processing time for the services thus continues while the station is failed.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWorkingPortion → real
```

### Return Value

The return value has the data type `real`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesWorkingPortion
```

**See also:** Tab Statistics [Worker], Statistics report — Service Statistics — States — Time Portions of the Exporters

---

## StatServicesWorkingTime [SimTalk] - Worker

Returns the time taken up by working processes of the services of the Worker designated by `<Path>`.

**Remarks:** If a station changes to the state failed and/or unplanned or paused and if then services for setting-up or processing are brokered, the services remain brokered. The set-up time and the processing time for the services thus continues while the station is failed.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatServicesWorkingTime → real
```

### Return Value

The return value has the data type `time`.

### Example

```simtalk
print .Resources.MyWorker:1.StatServicesWorkingTime
```

---

## StatTraveledDistance [SimTalk] - Worker

Returns the distance which the instance of the Worker designated by `<Path>` covered while walking from the WorkerPool to the Workplaces attached to the stations and between the stations in meters.

- **Type:** Read-only attribute

### Syntax

```simtalk
<Path>.StatTraveledDistance → length
```

### Return Value

The return value has the data type `length`.

### Example

```simtalk
print .Resources.MyWorker:2.StatTraveledDistance
```

**See also:** Tab Statistics [Worker], Statistics report — Worker Statistics — Traveled Distance by Workers
