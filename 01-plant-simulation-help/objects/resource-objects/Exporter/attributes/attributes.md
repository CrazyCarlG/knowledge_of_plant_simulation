# Exporter Attributes (SimTalk)

Summary of the SimTalk attributes of the Exporter object, plus related information on the Broker.

## StatSumMediatedCapacity [SimTalk]

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatSumMediatedCapacity → integer`
- **Return value:** integer

Returns the sum of the brokered capacity of the Exporter designated by `<Path>`.

```simtalk
print MyExporter.StatSumMediatedCapacity
```

**See also:** Tab Statistics [Exporter]; Statistics report, Service Statistics — States — Capacities and States of the Exporters.

## Attributes of the Exporter

The Exporter provides:

- The attributes listed in the table of contents.
- The Attributes of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window *Show Attributes and Methods*:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which an instance was inserted, to show them for the selected Instance.

You can set and get attribute values either via the check boxes, text boxes, and drop-down lists in dialog windows, or by assigning values in SimTalk:

```simtalk
MyExporter.ExpStatOn := true
```

```simtalk
print MyExporter.ExpStatOn
posit := Station.Cont.XPos
```

## AutomaticMediation [SimTalk]

- **Type:** Attribute
- **Syntax:** `<Path>.AutomaticMediation:boolean`
- **Assignment value:** boolean

Prevents the Exporter designated by `<Path>` from being automatically assigned by the Broker.

- `true` — make the Broker assign the Exporter automatically.
- `false` — assign the Exporter yourself.

```simtalk
.Resources.myExporter:2.AutomaticMediation := true
param type: integer // Importer type (0=failure, 1=setup, 2=processing, 3=transport)
var t : table
switch type
case 0 
   ?.failImp.releaseExporters
case 1 
   ?.setupImp.getExporters(t)
   if t.yDim > 0
       t[1,1].AutomaticMediation := true
   end
   ?.setupImp.releaseExporters
case 2 
   ?.imp.getExporters(t)
   if t.yDim > 0 
       t[1,1].AutomaticMediation := true
   end
   ?.imp.releaseExporters
end
```

## BrokerPath [SimTalk]

- **Type:** Attribute
- **Syntax:** `<Path>.BrokerPath:object`
- **Assignment value:** object

Sets the path to the Broker which procures the services that the Exporter designated by `<Path>` provides.

```simtalk
print MyExporter.BrokerPath
MyExporter.BrokerPath := myBroker
```

**See also:** Broker [Exporter].

## Capacity [SimTalk]

- **Type:** Attribute
- **Syntax:** `<Path>.Capacity:integer`
- **Assignment value:** integer

Sets the Capacity of the Exporter designated by `<Path>`.

**Remarks:**
- The Capacity is a value greater than or equal to zero.

**Note:**
- You can only reduce the capacity if the Capacity provided to the importers is not fallen short of.
- If you increase the capacity, the Broker will immediately attempt to find new importers.

```simtalk
MyExporter.Capacity := 2
```

**See also:** Capacity [text box] - Exporter.

## ExpStatOn [SimTalk]

- **Type:** Attribute
- **Syntax:** `<Path>.ExpStatOn:boolean`
- **Assignment value:** boolean

Activates exporter statistics of the Exporter designated by `<Path>` (`true`) or deactivates it (`false`).

```simtalk
MyExporter.ExpStatOn := true
```

**See also:** Exporter Statistics [Exporter].

## FailServices [SimTalk]

- **Type:** Attribute
- **Syntax:** `<Path>.FailServices:boolean`
- **Assignment value:** boolean

Fails the services (`true`) which the Exporter designated by `<Path>` provides, or does not fail them (`false`).

**Remarks:**
- If `FailServices` is `false` and the Exporter provides services for an importer, Plant Simulation does not interrupt the respective process of the importer at the beginning of a failure. The respective Out event thus persists. During a failure new requests to the Exporter remain unsatisfied.
- If Plant Simulation interrupts processing (for example through a failure of the Exporter), it deletes the respective Out event and adds it anew at the end of the failure according to the remaining processing time.
- If `FailServices` is `true` and the Exporter provides services for an importer, Plant Simulation interrupts the respective process for the duration of the failure.

**Note:**
- The name is not case-sensitive, just like the names of attributes and methods of the objects.
- To save memory and improve access speed, all places using such a case-insensitive string point to the same string in main memory. The first occurrence of the string defines how the string is written in terms of upper- and lower-casing.
- In SimTalk you can compare strings in a case-insensitive manner with the `~=` operator (see Relational Operators).

```simtalk
MyExporter.FailServices := true
```

**See also:** Fail Services [text box]; Relational Operators.

## OrderCtrl [SimTalk]

- **Type:** Attribute
- **Syntax:** `<Path>.OrderCtrl:method`
- **Assignment value:** method

Designates a Method object of the object designated by `<Path>`.

**Remarks:**
- Plant Simulation calls the Method whenever the Exporter is assigned to an importer.
- It determines how the Exporter handles the order.

**Parameters:** The Order Control has two parameters that define the importer:
- `Importer` (object) — designates the importer.
- `Type` (integer) — designates its type: `0` = failure/remove failure-importer, `1` = set-up-importer, `2` = processing-importer, `3` = transport-importer.

**Reformatting the Method:** If you manually enter an Order Control and click Apply or OK, Plant Simulation automatically checks whether the Method expects the correct parameters. If not, it shows a message asking whether the Method shall be reformatted. Empty methods are reformatted automatically. You cannot suppress the format check.

```simtalk
MyExporter.OrderCtrl := &myOrderCtrl
```

**See also:** Order Control [Exporter].

## Priority [SimTalk]

- **Type:** Attribute
- **Syntax:** `<Path>.Priority:integer`
- **Assignment value:** integer

Sets the Priority with which the Exporter designated by `<Path>` exports services when fulfilling a request.

**Remarks:**
- The Priority of an Exporter is a criterion for the urgency of a request. It is an integer value; the higher its value, the higher the urgency.
- The Priority only applies to Exporters registered with the same Broker.
- If several qualified Exporters with the same priority exist, Plant Simulation first brokers Exporters already on a suitable Workplace at the station; after that, Exporters already at the station but on the wrong Workplace; then Exporters not staying on a Workplace; finally Exporters staying on a Workplace assigned to another station.
- Exporters with a higher capacity will be brokered earlier for identical services than Exporters with a lower priority.
- Plant Simulation provides an Exporter with Priority 10 before an Exporter with Priority 1.

```simtalk
MyExporter.Priority := 3
```

**See also:** Priority [Exporter].

## ReleaseCtrl [SimTalk]

- **Type:** Attribute
- **Syntax:** `<Path>.ReleaseCtrl:method`
- **Assignment value:** method

Designates a Method object of the object designated by `<Path>`.

**Remarks:**
- Plant Simulation executes the control as soon as any importer releases the Exporter.

**Parameters:** The Release Control has two parameters that characterize the importer:
- `Importer` (object) — designates the importer proper.
- `Type` (integer) — designates its type: `0` = failure/remove failure-importer, `1` = set-up-importer, `2` = processing-importer, `3` = transport-importer.

When the control is called, the Exporter has already left its importer. If you entered a Method, you must take care that the Exporter is assigned new importers (for example with the method `findNewImporter`). In this case the Exporter will not automatically register as available with its Broker.

**Reformatting the Method:** Same automatic format check as `OrderCtrl`; empty methods are reformatted automatically, and the check cannot be suppressed.

```simtalk
MyExporter.ReleaseCtrl := &myReleaseCtrl
```

**See also:** Release Control [Exporter]; findNewImporter [SimTalk].

## Services [SimTalk]

- **Type:** Attribute
- **Syntax:** `<Path>.Services:array[]`
- **Assignment value:** array of string

Sets or returns the names of the Services that the Exporter designated by `<Path>` exports.

**Remarks:**
- The name is not case-sensitive (same case-insensitive string behavior as `FailServices`).
- In SimTalk, strings can be compared case-insensitively with the `~=` operator (see Relational Operators).

```simtalk
var a : string[] := ["Job1", "Job2", "Job3"]
Exporter2.Services := a
print MyExporter.Services
```

**See also:** Services [Exporter]; Exported Services [Exporter]; hasService [SimTalk]; Relational Operators.

## Broker [object]

The Broker is the go-between for services offered and services required. Use it to model the manager of a plant, the supervisor of a department, or the foreman of a shop.

**Remarks:**
- The Broker cooperates with the Exporter and the importers (see Tab Importer and Sub-tab Failure) of the Station, ParallelStation, AssemblyStation, DismantleStation, DePortioner, Mixer, Portioner, and Tank.
- Each Broker can manage several Exporters/Workers, which tender services, and may receive requests from several importers that require services. A request consists of a list of required services and the amount of required services. A service name is a string.
- When a Broker receives a request from an importer, it immediately attempts to fulfill it using the Exporters/Workers it manages. If it cannot, it may pass the request on to other Brokers connected with a Connector. The direction of the Connector determines the direction in which the request is passed on.
- If the Exporters/Workers of different Brokers can satisfy the request, those Exporters/Workers are assigned. If the request cannot be satisfied immediately, the Broker that received it first saves it.
- The Broker then attempts to provide the service later, going from requested service to requested service to find an Exporter/Worker for each. If an Exporter/Worker offers the service, it reserves the maximum possible number or the necessary number, and can no longer offer this reserved amount for other services. For this reason, request special services first and more general ones last.

**Note:**
- If the importer requests several services at the same time, all of these services have to be available at the same time before the Broker assigns them to the station.
- The Broker does not run any optimization; it may happen that the Broker cannot assign any Exporters/Workers even though they could theoretically be assigned.
