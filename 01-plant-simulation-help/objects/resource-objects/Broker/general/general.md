# Broker [object]

## Overview

Use the object **Broker** for brokering offered services and required services. You might model the manager of a plant, the supervisor of a department, or the foreman of a shop with it.

The Broker cooperates with the **Exporter** and the **importers** (see *Tab Importer* and *Sub-tab Failure*) of the Station, ParallelStation, AssemblyStation, DismantleStation, DePortioner, Mixer, Portioner, and Tank.

The Broker is the go-between for services offered and services required:

- Each Broker can manage several **Exporters/Workers**, which tender services.
- It may receive requests from several **importers** that require services.
- A request consists of a list of the required services and the amount of required services. A service name is a string.

When a Broker receives a request from an importer, it immediately attempts to fulfill it using the Exporters/Workers it manages. If it does not succeed, it may pass the request on to other Brokers connected with a **Connector**. The direction of the Connector determines the direction in which Plant Simulation passes the request on.

- If the Exporters/Workers of different Brokers are able to satisfy the request, those Exporters/Workers are assigned.
- If the request cannot be satisfied immediately, the Broker that received it first will save it.

The Broker then attempts to provide the service at a later point in time. It goes from requested service to requested service and attempts to find an Exporter/Worker for each. If an Exporter/Worker offers the service, it reserves the maximum possible number or the necessary number. That Exporter/Worker can then no longer offer this reserved amount of services for other services. For this reason, request **special services first** and **more general ones last**.

> **Note:** If the importer requests several services at the same time, all of these services have to be available at the same time before the Broker assigns them to the station.

> **Note:** The Broker does **not** run any optimization. It may happen that the Broker cannot assign any Exporters/Workers, although the Exporters/Workers may theoretically be assigned.

## Example: Order of Requested Services

The importer `MyImporter` requires one service A and one service B. There are two Exporters/Workers with a capacity of 1 each:

- `Exporter1` exports services A and B.
- `Exporter2` only exports service A.

Both are registered with the same Broker.

- If `MyImporter` requests the services in the order **(A, B)**, the Broker assigns `Exporter1` for service A and realizes that `Exporter2` cannot export the still missing service; thus it cannot fulfill the request.
- If `MyImporter` requests the services in the order **(B, A)**, it is fulfilled immediately: `Exporter1` provides service B and `Exporter2` provides service A.

The sequence in which a Broker passes requests on is defined uniquely by the Connectors: the Broker first passes the request on to all of its direct successors (defined by the number of the Connector), then to the successors of the successors. When an Exporter/Worker registers with its Broker as being available, the Broker attempts to find new importers for the Exporter/Worker — first checking the unsatisfied requests it manages, then having its Broker successors check for unsatisfied requests.

## Related Tasks

- You can show the **Broker Statistics Table** of a Broker in an HtmlReport.
- Hover with the mouse over the Broker to show a tooltip with information.
- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Adding the Object to the Simulation Model

To add the object Broker to the simulation model:

> **Manage Class Library** > **Basic Objects** > **Resources** > **Broker** on the Home ribbon tab.

## How the Broker Mediates Jobs to the Worker

The Broker mediates jobs to the Worker according to the **Priority** of the work order. During mediation, the Broker runs through the following phases, differentiating whether **Choose the Nearest Worker** is selected or not.

### Choose the Nearest Worker is activated

1. **Initial Phase:** Worker is located at the correct station on any Workplace suited for the required service. Station is within the Worker's Scope.
2. **Phase 1:** Worker is located at the correct station, but on a Workplace that does not support the required service. Station is within the Worker's Scope.
3. **Phase 2:** Worker is not located on a Workplace, but the station is within the Worker's Scope.
4. **Phase 3:** Worker is located at another station on a Workplace, and the correct station is within the Worker's Scope.
5. **Phase 4:** Worker is located at the correct station, the Workplace is suitable, and the Worker does not have a defined Scope.
6. **Phase 5:** Worker is located at the correct station, but on a Workplace that does not support the required service. Worker does not have a defined Scope.
7. **Phase 6:** Worker does not have a Scope and is not located on a Workplace.
8. **Phase 7:** Worker does not have a Scope and is located on a Workplace at the wrong station.
9. **Phase 8:** Worker is working at the moment and has to be drawn off from his current job.

### Choose the Nearest Worker is not activated

The same phases 1–8 apply (initial phase through Phase 8), but without the "nearest Worker" distance criterion.

## Dialog Box of the Broker

Double-click the icon of the Broker to open its dialog box.

- **Edit Simulation Properties:** Shared properties are described under *Dialog Items of the Objects*.
- **Edit Animation Properties:** Click **Edit 3D Properties** in the lower-left corner, or select the object and press the spacebar. To manipulate the graphic, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Tab Attributes

The tab **Attributes** provides these settings:

- **Choose the Nearest Worker** [check box]
- **Importer Request Control** [Broker]
- **Exporter Request Control** [Broker]

### Choose the Nearest Worker [check box]

To make the Broker prefer the Worker who has to walk the shortest path to the Workplace, select this check box. Clear it to make the Broker select any Worker who can do the job, no matter where he is located.

When the Broker receives an import request, it selects Workers according to:

- Highest Priority
- Already located at a Workplace of the requesting station
- Matching Scope

If **Choose the Nearest Worker** is selected, the Broker uses an additional criterion: which Worker has to walk a shorter distance to the Workplace. Plant Simulation computes routes to suitable Workplaces for all eligible Workers while mediating, so enabling this can slow down the simulation.

**SimTalk:** `ChooseNearestWorker [SimTalk]`

## Controls of the Broker

Click the ellipsis button and select a Method in the dialog **Select Object**. Type the source code of the respective control.

### Select the Path to an Existing Method

Click the ellipsis button, navigate to the Method in **Select Object [for controls]**, and click OK. Press `F2` in the text box to open the Method. Alternatively, drag a Method from a Frame and drop it into the text box.

### Create a Control That Is a Method of the Object

1. Type a meaningful name into the text box and select **Create Control** on the context menu. Plant Simulation inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
2. Or select **Create Control** on the empty text box. Plant Simulation inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.
3. Type the source code of the control into the Method that opens.

To edit the source code later: press `F2`, hold `Shift` and double-click the text box, select **Open Object** on the context menu, or open the **User-defined** tab and double-click the Method name.

To delete the control, delete the user-defined attribute (deleting only the name from the text box retains the attribute).

### Execution Order

The **Exporter Request Control** and the **Importer Request Control** are called in this order:

- If both are defined, the Exporter Request Controls are executed first. This way you can make the Worker follow the part when the part moves to the next station (changed behavior versus modeling without controls — without controls, the Worker is brokered for the new station in the WorkerPool).
- If several Importer Request Controls are executed at the same time, their sequence matches the sequence of the Importers in the list **Open Importers**.

## Importer Request Control [Broker]

Modifies the built-in behavior. Sets how the Broker requests importers. The object calls the Importer Request Control whenever the Broker receives a request, or when it would handle the request again (e.g., when an Exporter/Worker registers as being available).

In the source code of the Method, you yourself must ensure the request is taken care of, for example with the method `engage`. With this control you can model your own assignment strategies.

The Importer Request Control does **not** interrupt methods currently executed; it is called only after the current call chain has been executed. Importer requests cannot overtake each other.

**Example:**

- The Processing Importer of `Station2` cannot be satisfied because the Worker is already working at `Station1`.
- `Station1` finishes processing; the Worker is released and the Exit Control of `Station1` is called.
- The Importer Request Control of `Station2` is only called after the Exit Control has been executed.
- If the Exit Control of `Station1` moves the part to `Station3`, the Importer Request Control does not interrupt the exit control. After the exit control, the Importer Request Control of `Station2` is called, then the Importer Request Control of `Station3`.

> **Note:** For Broker hierarchies, Plant Simulation does **not** call the controls of sub-Brokers (Brokers connected with Connectors). It only calls the control of the Broker that you typed into the object.

The standard importer request control as a user-defined attribute looks like this:

```
ImpRequestCtrl [SimTalk]
doStandardExport [SimTalk]
```

## Exporter Request Control [Broker]

Modifies the built-in behavior. Sets how the Broker requests Exporters/Workers. The object calls the Exporter Request Control whenever an Exporter/Worker registers as being available with its Broker; it may then be assigned a new importer.

In the source code of the Method, you yourself must ensure the request is taken care of, for example with the method `engage`. With this control you can assign a specific importer to the Exporter/Worker.

If Exporter and Importer request controls are both defined, the Exporter Request Controls are executed first.

The standard exporter request control as a user-defined attribute looks like this:

```
ExpRequestCtrl [SimTalk]
doStandardExport [SimTalk]
```

## Tab Statistics

The tab **Statistics** shows the most important statistical data. To collect statistics data, select the check box **Broker Statistics**.

| Item | Description | Read-only attribute |
|------|-------------|---------------------|
| Open Requests | Actual number of open requests | `OpenRequests` |
| Open Requests (sum) | Total number of open requests | `StatOpenRequests` |
| Satisfied Requests | Number of satisfied requests | `SatisfiedRequests` |
| Satisfied Requests (sum) | Total number of satisfied requests | `StatSatisfiedRequests` |
| Open Capacity | Amount of available capacities | `OpenCapacity` |
| Open Capacity (sum) | Total amount of open capacities | `StatOpenCapacity` |
| Mediated Capacity | Amount of brokered capacities | `MediatedCapacity` |
| Mediated Capacity (sum) | Total amount of brokered capacities | `StatMediatedCapacity` |

> **Note:** For Broker hierarchies (Brokers connected with Connectors), brokered services are only considered for the Broker that you typed into the Importer, even if the service is provided by sub-Brokers.

To view Broker Statistics in the Statistics Report, select **View > Show Statistics Report** in the dialog, or right-click in the Frame and select **Show Statistics Report**, or press `F6`.

### Broker Statistics [activate]

Select this check box to collect statistics data of the Broker; clear it to deactivate.

**SimTalk:** `BrokerStatOn [SimTalk]`

### Service Statistics [Broker]

Click this button to open the service statistics table, which shows the **Dwelling Time** and the **Mediation Time** per service.

> **Note:** If a service is fulfilled by several Workers or Exporters/Workers, the time interval is recorded only once (same for the count). For en-route time, statistics counts the Worker who was en-route the longest.

**Dwelling Time** columns:

| Item | Description | Read-only attribute |
|------|-------------|---------------------|
| Count | How often the service was brokered (how often the Exporter/Worker stayed at the importer/importers) | — |
| Sum | Sum of times during which the service was brokered | `StatStayTime` |
| Mean Value | Mean duration | `StatStayTimeMu` |
| Standard Deviation | Standard deviation from the mean | `StatStayTimeDelta` |
| Min | Minimum time brokered | — |
| Max | Maximum time brokered | — |

**Mediation Time** columns:

| Item | Description | Read-only attribute |
|------|-------------|---------------------|
| Count | How often the importer/importers were waiting for procurement of the service | — |
| Sum | Sum of waiting times | `StatMediationTime` |
| Mean Value | Mean duration of waiting | `StatMediationTimeMu` |
| Standard Deviation | Standard deviation of waiting times | `StatMediationTimeDelta` |
| Min | Minimum waiting time | — |
| Max | Maximum waiting time | — |

**SimTalk:** `serviceStat [SimTalk]`

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

## Navigate Menu

Commands are described under the *Navigate Menu*.

## View Menu

The View Menu provides commands to access its functions:

- **Refresh** [on View menu]
- **Show Statistics Report** [on View menu]
- **Show Attributes and Methods** [on View menu]
- **Open Importers** [Broker]
- **Satisfied Importers** [Broker]
- **Exporters** [Broker]
- **Offered Services** [Broker]

### Open Importers [Broker]

Opens a table showing all objects whose importers registered an unsatisfied request with the Broker.

Column 1 shows the Importers, column 2 their **Type**: `0` = failure-importer, `1` = set-up-importer, `2` = processing-importer, `3` = transport-importer. An Importer interrupted because another station with higher priority requires the resource is sorted first.

**SimTalk:** `getOpenImporters [SimTalk]`, `forgetOpenRequest [SimTalk]`

### Satisfied Importers [Broker]

Opens a table showing all objects whose importers were assigned Exporters/Workers. Column layout and type codes are the same as Open Importers.

**SimTalk:** `getSatisfiedImporters [SimTalk]`

### Exporters [Broker]

Opens a table showing information about all Exporters registered with the Broker:

- **Exporters** — names of the Exporters/Workers
- **State** — state of the Exporter/Worker
- **Capacity** — capacity of the Exporter/Worker
- **Free Cap.** — free capacity of the Exporter/Worker

**SimTalk:** `AdministeredExporters [SimTalk]`

### Offered Services [Broker]

Opens a table showing information about the services offered by the Exporters/Workers managed by the Broker.

For **Exporter** and **Worker** entries, the columns are:

- **Services** — name of the offered service
- **Capacity** — overall capacity offered
- **Free Cap.** — free capacity offered
- **State** — state of the respective Exporter/Worker

Double-click the name of a service to open a subtable showing the path of the Exporter or the individual Worker.

**SimTalk:** `getOfferedServices [SimTalk]`

## Tools Menu

The Tools Menu provides these menu commands:

- Edit Controls
- Edit Observers

## Help Menu

Commands are described under the *Help Menu*.

## Methods of the Broker

The Broker provides:

- The methods listed in the table of contents.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library (for a selected Class).
- Press `F8` or click **Show Attributes and Methods** on the Home ribbon tab of the Frame (for a selected Instance).

## See also

- How the Broker Mediates Jobs to the Worker
- How the Worker Decides Where to Work
- Model Workers and the Jobs They Do
- Model Workers with Importer, Broker, and Exporter
- Worker [object]
- Workplace
- Priority [Worker] / Priority [SimTalk] - Worker
- Tab Scope / Scope [SimTalk] - Worker
- `brokerStat [SimTalk]`
- `BrokerStatOn [SimTalk]`
- `serviceStat [SimTalk]`
- `ChooseNearestWorker [SimTalk]`
- `ImpRequestCtrl [SimTalk]`
- `ExpRequestCtrl [SimTalk]`
- `doStandardExport [SimTalk]`
