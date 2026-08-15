# Methods of the Worker

The Worker provides:

- The methods listed in the table of contents.
- The methods of the **Exporter**, as the Worker is an Exporter with capacity 1.
- The methods of **All Objects**.

> **Note:** If you do not use a FootPath, Plant Simulation beams/teleports the Worker to the Workplace.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods** (F8 or context menu).

## Syntax conventions

An example of a syntax line looks like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature, consisting of identifier and data type of parameters, is listed in parentheses. `(Parameter:string)` designates a parameter of data type `string`.
- Optional parameters are listed within brackets: `[,Parameter:boolean]`.
- Default values are shown after the parameter: `:= false`.
- Return values are shown after the arrow `→`, e.g. `→ boolean`.

---

## Methods

### cancelTransportPart

Cancels each and every transport of the parts started with the method `transportPart`, which are scheduled to be carried by the Worker designated by `<Path>`.

**Remarks**

- If one or several parts are scheduled to be transported, Plant Simulation deletes this reservation and the Worker either walks to the WorkerPool or to his base.
- If a Station was specified for picking up finished parts, this reservation is also deleted. Once the Worker has picked up a part and transported it, the reservation cannot be canceled.
- A `Destination` saved in the parts is **not** undone; it remains queryable via the attribute `Destination`.
- Only cancels transports started with `transportPart` — it does **not** cancel automatically mediated transports initiated by the Transport Importer and the Broker.

**Syntax**

```
<Path>.cancelTransportPart -> boolean
```

**Return Value**

- `true` if all transport processes could be canceled.
- `false` if they could not be canceled (e.g. no orders exist, or the Worker picked up at least one part).

**Example**

```
.Resources.MyWorker:1.cancelTransportPart
```

---

### create

Creates an instance of the Worker designated by `<Path>` in the WorkerPool.

**Syntax**

```
<Path>.create(WorkerPool:object)
```

**Parameter**

- `WorkerPool:object` — the WorkerPool where the Worker will be created.

**Example**

```
.Resources.MyWorker.create(MyWorkerPool)
```

---

### getRouteLength

Returns the route of the Worker designated by `<Path>` from his present location to this destination object.

**Remarks**

- If the destination is a station, the method returns the length of the route to the Workplace reachable on the shortest route.
- If the Worker is exporting a service, it only takes Workplaces into consideration which support the service, including Workplaces not restricted to certain services.
- If the destination is a Workplace, Plant Simulation always computes the length to this Workplace, regardless of whether it supports the exported service.

**Syntax**

```
<Path>.getRouteLength(Target:path[, byref FoundWorkplace:object]) → length
```

**Parameters**

- `Target:path` — the destination object (Workplace, WorkerPool, or work station with attached Workplaces).
- `FoundWorkplace:object` (optional, by reference) — the Workplace found at the destination object.

**Return Value**

- Data type `length`; `-1` if Plant Simulation did not find a route.

**Examples**

```
print .Resources.Worker:1.getRouteLength(MyWorkplace1)
var FoundWorkplace: object
.Resources.Worker:1.getRouteLength(MyStation, FoundWorkplace)
print FoundWorkplace
```

---

### getServices

Returns all services of the Worker designated by `<Path>` and writes them into a table.

**Syntax**

```
<Path>.getServices(Services:table)
```

**Parameter**

- `Services:table` — an unformatted table (DataTable in a Frame or local table) with three columns:
  - Column 1 (`string`): Name of the Service.
  - Column 2 (`integer`): Priority.
  - Column 3 (`integer`): Efficiency.

**Example**

```
print .Resources.Worker:1.getServices(MyServicesTable)
```

---

### goTo

Sends the Worker designated by `<Path>` to the designated Workplace.

**Remarks**

- If the Worker is interrupted but must teleport to reach the destination, the Worker does not accept the order and returns `false`.
- If the object is a work station rather than a Workplace, the Worker walks to the closest Workplace assigned to it.

**Syntax**

```
<Path>.goTo(Workplace:object[, ReserveExclusively:boolean:=true]) → boolean
```

**Parameters**

- `Workplace:object` — the Workplace to send the Worker to.
- `ReserveExclusively:boolean` (optional, default `true`) — if `true`, the Workplace is reserved exclusively until the Worker leaves it; if occupied, the Worker stops and `goTo` returns `false`. If `false`, the Workplace is not reserved and the Worker waits until it becomes available.

> **Note:** If `AutomaticMediation` is deactivated and `ReserveExclusively` is `true`, Plant Simulation checks available Capacity and shows an error message if all places are occupied or reserved.

**Return Value**

- `false` if the Worker is exporting a service at the moment; the Worker stays where he is.

**Examples**

```
.Resources.MyWorker:1.goTo(MyWorkplace)
.Resources.MyWorker:1.goTo(MyWorkplace,false)
```

---

### goToHome

Sends the Worker designated by `<Path>` back to his WorkerPool or to his Home Location if one is defined.

**Syntax**

```
<Path>.goToHome → boolean
```

**Return Value**

- `false` if the Worker is exporting a service at the moment.

**Example**

```
.Resources.MyWorker:1.goToHome
```

---

### goToPool

Sends the Worker designated by `<Path>` back to the WorkerPool.

**Syntax**

```
<Path>.goToPool → boolean
```

**Return Value**

- `false` if the Worker is exporting a service at the moment.

**Example**

```
.Resources.MyWorker:1.goToPool
```

---

### setServices

Sets the services that the Worker designated by `<Path>` provides.

**Syntax**

```
<Path>.setServices(Services:table)
```

**Parameter**

- `Services:table` — an unformatted table (DataTable in a Frame or local table) with three columns:
  - Column 1 (`string`): Name of the Service.
  - Column 2 (`integer`): Priority.
  - Column 3 (`integer`): Efficiency.

**Examples**

```
.Resources.Worker:1.setServices(MyServicesTable)
.UserObjects.MyWorker.setServices(MyServicesTable)
```

---

### teleportTo

Teleports the Worker designated by `<Path>` to the designated Workplace.

**Syntax**

```
<Path>.teleportTo(Workplace:object) → boolean
```

**Parameter**

- `Workplace:object` — the Workplace to teleport the Worker to.

**Return Value**

- `true` if the Worker was teleported.
- `false` if not (e.g. the Worker is already located on the Workplace).

**Examples**

```
.Resources.MyWorker:1.teleportTo(MyStation)
-- returns true if a workplace at the station is available and the Worker
can be teleported there
.Resources.MyWorker:2.teleportTo(MyWorkplace1)
-- returns true if the Worker can be teleported to this Workplace
```

---

### teleportToHome

Teleports the Worker designated by `<Path>` back to his WorkerPool or to his HomeLocation if one is defined.

**Syntax**

```
<Path>.teleportToHome → boolean
```

**Return Value**

- `true` if the Worker could be teleported to his Home Location or WorkerPool.
- `false` if not (e.g. already located there).

**Example**

```
.Resources.MyWorker:1.teleportToHome
```

---

### teleportToPool

Teleports the Worker designated by `<Path>` back to the WorkerPool.

**Syntax**

```
<Path>.teleportToPool → boolean
```

**Return Value**

- `true` if the Worker was teleported to his WorkerPool.
- `false` if not (e.g. already located there).

**Example**

```
.Resources.MyWorker:1.teleportToPool
```

---

### transportPart

Makes the Worker designated by `<Path>` transport a single part (or several parts) from its current location to the specified destination.

**Remarks**

- Instead of parts, you can specify a material flow object that provides parts to be picked up. The Worker picks up all parts ready to exit until his Capacity is exhausted.
- If no parts are ready to exit when the Worker arrives, Plant Simulation shows an error message.
- If no Destination is specified, the parts must already have a Destination. The specified Destination is saved in the parts and can be queried with the attribute `Destination`.
- The Worker can only transport several parts if he can pick them all up at the same location.

**Syntax**

```
<Path>.transportPart(PartOrStationOrParts:object/object[ ][, Destination:object]) -> void
<Path>.transportPart(Part:object[, Destination:object]) -> void
<Path>.transportPart(Parts:object[ ][, Destination:object]) -> void
<Path>.transportPart(Station:object[, Destination:object]) -> void
```

**Parameters**

- `Part:object` — the part to be transported.
- `Parts:object[ ]` — an array of parts to be transported.
- `Station:object` — the Station (any material flow object providing parts) at which the Worker picks up parts ready to exit.
- `Destination:object` (optional) — the destination object. If omitted, each part must have its own destination.

**Return Value**

The method has no return value. It outputs error messages if it fails, e.g.:

- The specified Worker is a class object, is brokered automatically, cannot transport parts, or already carries a part.
- The number of parts exceeds the Worker's current Capacity.
- The part or Destination does not exist or has the wrong object type.
- No Destination was specified and the parts have none of their own.
- The part's defined Destination differs from the specified Destination.
- Parts must be picked up at different locations.
- The part is already being transported by a Worker.
- No parts are to be picked up at the Station.

**Examples**

```
waituntil .Resources.Worker:1.HasOrder = false
.Resources.Worker:1.transportPart(Station.cont, Station1)
```

---

## Read-Only Attributes of the Worker

The Worker provides:

- The read-only attributes listed in the table of contents.
- All read-only attributes of the **Exporter**, as the Worker is an Exporter with capacity 1.
