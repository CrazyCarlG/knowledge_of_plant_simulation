# Worker Methods — Summary

This README summarizes the Worker methods documented in `methods.md`.

## Overview

The Worker object provides the following methods in addition to:

- The methods of the **Exporter** (the Worker is an Exporter with capacity 1).
- The methods of **All Objects**.

> **Note:** If no FootPath is used, Plant Simulation beams/teleports the Worker to the Workplace.

## Method Index

| Method | Purpose | Returns |
| --- | --- | --- |
| [`cancelTransportPart`](#canceltransportpart) | Cancels all pending `transportPart` orders for the Worker. | `boolean` |
| [`create`](#create) | Creates a Worker instance in a WorkerPool. | — |
| [`getRouteLength`](#getroutelength) | Returns the route length from the Worker to a destination. | `length` |
| [`getServices`](#getservices) | Writes the Worker's services into a table. | — |
| [`goTo`](#goto) | Sends the Worker to a Workplace. | `boolean` |
| [`goToHome`](#gotohome) | Sends the Worker back to the WorkerPool or Home Location. | `boolean` |
| [`goToPool`](#gotopool) | Sends the Worker back to the WorkerPool. | `boolean` |
| [`setServices`](#setservices) | Sets the services the Worker provides. | — |
| [`teleportTo`](#teleportto) | Teleports the Worker to a Workplace. | `boolean` |
| [`teleportToHome`](#teleporttohome) | Teleports the Worker back to the WorkerPool or Home Location. | `boolean` |
| [`teleportToPool`](#teleporttopool) | Teleports the Worker back to the WorkerPool. | `boolean` |
| [`transportPart`](#transportpart) | Makes the Worker transport one or several parts. | — (void) |

## Method Details

### cancelTransportPart

Cancels every transport started with `transportPart` that is scheduled for the Worker.

- Deletes the pickup reservation; the Worker walks back to the WorkerPool or his base.
- Deletes a Station pickup reservation if specified.
- Cannot be undone once the Worker has picked up a part.
- A saved `Destination` in the parts is **not** undone (still queryable via `Destination`).
- Does **not** cancel automatically mediated transports from the Transport Importer / Broker.

```
<Path>.cancelTransportPart -> boolean
```

Returns `true` if all transports could be canceled, `false` otherwise (e.g. no orders, or a part was already picked up).

---

### create

Creates an instance of the Worker in the given WorkerPool.

```
<Path>.create(WorkerPool:object)
```

- `WorkerPool:object` — the WorkerPool where the Worker is created.

---

### getRouteLength

Returns the route length from the Worker's current location to a destination object.

- For a station destination, returns the length to the Workplace reachable on the shortest route.
- If exporting a service, only considers Workplaces that support it (plus unrestricted Workplaces).
- For a Workplace destination, always computes the length to that Workplace regardless of service support.

```
<Path>.getRouteLength(Target:path[, byref FoundWorkplace:object]) → length
```

- `Target:path` — destination object (Workplace, WorkerPool, or station with Workplaces).
- `FoundWorkplace:object` (optional, by reference) — receives the Workplace found at the destination.
- Returns `length`, or `-1` if no route was found.

---

### getServices

Writes all of the Worker's services into a table.

```
<Path>.getServices(Services:table)
```

- `Services:table` — an unformatted table with three columns:
  1. `string` — Service name.
  2. `integer` — Priority.
  3. `integer` — Efficiency.

---

### goTo

Sends the Worker to the designated Workplace.

- If interrupted and teleportation is required, the Worker refuses and returns `false`.
- If a work station is given instead of a Workplace, the Worker walks to the closest Workplace assigned to it.

```
<Path>.goTo(Workplace:object[, ReserveExclusively:boolean:=true]) → boolean
```

- `Workplace:object` — the target Workplace.
- `ReserveExclusively:boolean` (default `true`) — if `true`, the Workplace is reserved exclusively until the Worker leaves; returns `false` if occupied. If `false`, the Worker waits until the Workplace becomes available.

> **Note:** If `AutomaticMediation` is deactivated and `ReserveExclusively` is `true`, Plant Simulation checks available Capacity and errors if all places are occupied/reserved.

Returns `false` if the Worker is currently exporting a service.

---

### goToHome

Sends the Worker back to his WorkerPool or Home Location (if defined).

```
<Path>.goToHome → boolean
```

Returns `false` if the Worker is currently exporting a service.

---

### goToPool

Sends the Worker back to the WorkerPool.

```
<Path>.goToPool → boolean
```

Returns `false` if the Worker is currently exporting a service.

---

### setServices

Sets the services the Worker provides.

```
<Path>.setServices(Services:table)
```

- `Services:table` — an unformatted table with three columns:
  1. `string` — Service name.
  2. `integer` — Priority.
  3. `integer` — Efficiency.

---

### teleportTo

Teleports the Worker to the designated Workplace.

```
<Path>.teleportTo(Workplace:object) → boolean
```

- `Workplace:object` — the target Workplace.
- Returns `true` if teleported, `false` otherwise (e.g. already located there).

---

### teleportToHome

Teleports the Worker back to his WorkerPool or Home Location (if defined).

```
<Path>.teleportToHome → boolean
```

Returns `true` if teleported to the Home Location or WorkerPool, `false` otherwise (e.g. already there).

---

### teleportToPool

Teleports the Worker back to the WorkerPool.

```
<Path>.teleportToPool → boolean
```

Returns `true` if teleported to the WorkerPool, `false` otherwise (e.g. already there).

---

### transportPart

Makes the Worker transport a single part (or several parts) from its current location to the destination.

- Can also specify a material flow object that provides parts; the Worker picks up all ready-to-exit parts until Capacity is exhausted.
- If no parts are ready to exit when the Worker arrives, an error message is shown.
- If no `Destination` is specified, the parts must already have one; a specified `Destination` is saved in the parts (queryable via `Destination`).
- The Worker can only transport several parts if they can all be picked up at the same location.

```
<Path>.transportPart(PartOrStationOrParts:object/object[ ][, Destination:object]) -> void
<Path>.transportPart(Part:object[, Destination:object]) -> void
<Path>.transportPart(Parts:object[ ][, Destination:object]) -> void
<Path>.transportPart(Station:object[, Destination:object]) -> void
```

- `Part:object` — the part to transport.
- `Parts:object[ ]` — an array of parts to transport.
- `Station:object` — the station (any material flow object providing parts) where parts are picked up.
- `Destination:object` (optional) — the destination object.

The method returns no value, but outputs error messages if it fails (e.g. Worker is a class object, brokered automatically, already carries a part, part count exceeds Capacity, invalid part/Destination, differing destinations, parts at different locations, part already being transported, or no parts to pick up).

---

## Read-Only Attributes

The Worker provides its own read-only attributes plus all read-only attributes of the **Exporter** (the Worker is an Exporter with capacity 1).
