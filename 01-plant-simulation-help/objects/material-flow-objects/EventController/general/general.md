# EventController

Use the object **EventController** for coordinating, synchronizing, and controlling the events taking place during a simulation run.

> **Note:** You cannot change the name of the EventController.

## Description

You can start, stop, and reset the simulation with the EventController. Plant Simulation is a **discrete event-oriented simulation system** that shows the state changes of the model components at certain points in time, not continually over time.

When a part enters a processing station (for example a Station), Plant Simulation computes the time it takes to cover it and enters that time and that event into the **List of scheduled events** of the EventController. Imagine a timeline where you insert markers at certain points in time.

The EventController moves along the timeline like the play-back head of a video player, and interprets messages relating to the events the objects execute. After a certain simulation time (for example the Processing Time) has elapsed, the EventController arrives at the marker which was set when the part entered the station. This marker denotes that the processing time has elapsed and that an **Out** event is pending. The EventController notifies the Station to process the Out event and moves the part on to the succeeding object in the flow of materials. Plant Simulation repeats this process cyclically for all MUs in the simulation model.

> **Note:** If you manually delete the EventController, Plant Simulation resets the model beforehand.

## Starting and Stopping the Simulation

You can start the simulation:
- By clicking **Start/Stop Simulation** in the dialog of the EventController.
- By clicking **Start/Stop Simulation** on the Home Ribbon Tab of the Frame. If you start the simulation without having inserted an EventController, Plant Simulation asks if you would like to insert one.
- By clicking **Start/Stop Simulation** on the mini toolbar.

You can stop the simulation:
- By clicking **Single Step Simulation** in the dialog of the EventController.
- By clicking **Start/Stop Simulation** on the Home ribbon tab a second time.
- By clicking **Start/Stop Simulation** on the mini toolbar.

The simulation stops after the current event has been completely processed.

At the end of the simulation run Plant Simulation executes all methods named `endSim`. The end of the simulation run is reached when the event list is empty or when the **End time** (entered on the tab Settings) has been reached.

You can also run the simulation step-by-step with the **EventDebugger**.

### Add the Object to the Simulation Model

To add the object EventController to your simulation model, click **Manage Class Library > Basic Objects > MaterialFlow > EventController** on the Home ribbon tab.

## Dialog Box of the EventController

Double-click the icon of the EventController to open its dialog box.

- **Edit Simulation Properties** — change its simulation properties. The shared properties are described under *Dialog Items of the Objects*.
- **Edit Animation Properties** — change the dimensions of the graphic of the EventController by clicking **Show Manipulators** on the Edit ribbon tab or pressing **M**.

### Time [EventController]

Shows the current simulation time of the simulation run. Click **Time** to change the display between:
- **Relative time** — Plant Simulation resets the relative time to zero when it starts the simulation run (default).
- **Current time plus simulation time** — Plant Simulation adds the simulation time to the time and date at which it started the simulation run.

Example: if today is the second of January 2023, six o'clock in the morning, and the simulation is to run for two days:
- **Relative time**: `2:00:00:0000` (two days).
- **Current time plus simulation time**: `Mi, 2023/01/04 06:00:00.0000` (Wednesday, January 04, 2023, 6 o'clock in the morning).

**SimTalk:** `AbsSimTime`, `SimTime`

## Tab Controls

The tab **Controls** provides settings for controlling the simulation run.

### Reset Simulation [EventController]

Resets the simulation model. Plant Simulation calls all Methods named `reset` in the simulation model. Once all reset methods have been executed, Plant Simulation:
- Deletes all unprocessed events
- Resets the simulation time to 0
- Resets statistics
- Clears all failures of all objects in the simulation model
- Sets all objects to the state `planned`
- Reactivates inheritance of the settings **Entrance Locked** and **Exit Locked** for new models (if *Tools > Inherit 'Entrance/Exit Locked On Reset* is active)

The Request Control, Receive Control, and Release Control of the Importer are not called when you reset. When you reset while the simulation is running, Plant Simulation finishes processing the current event and then resets the model. Resetting also deletes MUs on the Clipboard.

> **Note:** If the simulation model still contains MUs after resetting (Plant Simulation does not start counting MUs with 1), check if the model contains additional Frames with inserted EventControllers and reset those as well.

Plant Simulation deletes suspensions of methods located in the same Frame (or a sub-Frame) as the EventController. The global method `deleteSuspendedMethods` deletes all suspensions of all methods.

**SimTalk:** `reset` (EventController), `reset` (predefined name), `deleteSuspendedMethods`, `initStat` (material flow objects), `IsInitialized`, `ResetCtrl`

### Start/Stop Simulation [EventController]

Starts the simulation run; click again to stop after the active simulation event has been processed. Plant Simulation calls `init` methods when you click Start/Stop Simulation if they have not been called yet.

**SimTalk:** `start` (EventController), `stop` (EventController), `StartStopCtrl`, `init` (predefined name), `InitCtrl` (EventController), `IsInitialized`

### Start Full Speed Simulation [EventController]

Starts the simulation run with the animation of MUs and States and with full speed. Updates a number of values (e.g. objects of type Variable or Display). Ignores the Real Time scaling factor.

**SimTalk:** `Realtime`, `RealtimeScale`, `start` (EventController)

### Start Fast Forward Simulation [EventController]

Starts the simulation run without the animation of MUs and States and with maximum speed. Prevents updating a number of values (e.g. Variable or Display). Ignores the Real Time scaling factor.

### Single Step Simulation [EventController]

Processes the next simulation event, then stops. Holding **Shift** while clicking opens the Method Debugger for all methods and formulas executed while the event is processed. If `init` methods have not been called yet, they are started instead of processing an event.

**SimTalk:** `StartStopCtrl`

## List of Scheduled Events

Click **List** to open the Event Debugger that shows the event list.

The Event List contains the events the objects scheduled and which the EventController must process. It is sorted ascending by time. Columns:
- **Breakpoint** — shows an `S` for a breakpoint inserted by double-clicking a cell in the row.
- **Type** — the type of the event.
- **Time** — the point in time at which the event is going to be executed (the time interval from the Start Time, *not* the time of day).
- **Receiver** — the object that receives the simulation event.
- **Sender** — the object that sends the simulation event.
- **Insertion Time** — the point in time the event was entered into the event list (hidden by default).
- **Parameters** — additional information for certain event types (e.g. sensor ID for `SensorStart`, failure profile name for `DisruptionBegin`, parameters for `MethCall`).

**SimTalk:** `getEventList`

### Event Types

Plant Simulation provides these types of simulation events:

| Event (English) | Event (German) | Action taking place / state of the object |
|---|---|---|
| `*` | `*` | Designates any type of event. |
| `Animation` | `Animation` | A MU is located on a Track, Conveyor, or on a Buffer. |
| `Battery` | `Batterie` | The battery of a Transporter is full, empty or on reserve. |
| `BlockageEnd` | `BlockierEnde` | The state of a MU changes to unblocked. |
| `Bump` | `Anstoss` | The Transporter collides with another MU (handle in the Collision control). |
| `CheckMUDistance` | `BEAbstandPrüfen` | The MU distance at the start of the Conveyor is reached. |
| `CheckMUPosition` | `BEPositionPrüfen` | Checks if the MU has to be stopped after the exit control on length-oriented objects. |
| `CreateMU` | `ErzeugeBE` | The Source attempts to create MUs. |
| `DeliverParts` | `TeileAbliefern` | The Worker picked up parts and carries them to the destination object. |
| `DisruptionBegin` | `StörBeginn` | The failure of the object starts. |
| `DisruptionEnd` | `StörEnde` | The failure of the object ends. |
| `Distance` | `Abstand` | The Distance Control of the Transporter is called. |
| `EndOfTime` | `ZeitBeendet` | PickAndPlace-robot / Worker done loading/unloading; Mixer finished mixing; Converter/AngularConverter done changing direction; all 3D pose runs arrived. |
| `EndOfTurn` | `EndeDrehen` | PickAndPlace-robot, Turnplate, Turntable or Transporter reaches the end position of rotation. |
| `EntranceEnd` | `EintrittEnde` | The MU completely entered a length-oriented object; Mixer educt amount reached; Portioner MU filled; Worker reached target station. |
| `FinalSpeed` | `EndGeschw` | Transporter or Conveyor reach final speed after accelerating/decelerating. |
| `GenDuration` | `GenDauer` | The Duration Control of the Generator is activated. |
| `GenInterval` | `GenAbstand` | The Interval Control of the Generator is activated. |
| `Init` | `Init` | Initializes the model using the method `init` before the next scheduled event. |
| `InitStat` | `InitStat` | Resets statistics and starts collecting anew. |
| `MethCall` | `MethAufr` | Calls a method scheduled with `executeIn` of the object Method. |
| `MethWakeup` | `MethAufwecken` | Continues the call chain after a `wait` statement time has elapsed. |
| `Out` | `Aus` | A MU exits the object. |
| `OutEnd` | `AusEnde` | A MU completely exits a length-oriented object (Conveyor, Turntable, Track, TwoLaneTrack). |
| `Pause` | `Pause` | Start of a pause (created with `startPauseIn`); ShiftCalendar pause start. |
| `PauseEnd` | `PauseEnde` | End of a pause (created with `startPause`); ShiftCalendar pause end. |
| `PositionReached` | `PositionErreicht` | MU reached center of rotation of Turnplate/Turntable; Converter/AngularConverter reached direction-change point; Transporter reached target. |
| `PoweringUpDown` | `HochRunterfahren` | The material flow object powers up/down to reflect an energy status change. |
| `Reference` | `Referenz` | The booking point of the MU exits the object. |
| `RouteObjectReached` | `RoutenObjektErreicht` | The Transporter driving freely within the area reached a Track. |
| `SensorBookPos` | `SensorBuchPos` | The booking point of the MU activates a sensor. |
| `SensorEnd` | `SensorEnde` | The rear of the MU activates a sensor. |
| `SensorStart` | `SensorBeginn` | The front of the MU activates a sensor. |
| `SetupEnd` | `RuestenEnde` | The set-up time of a MU has expired. |
| `Shift` | `Schicht` | Schedules the start or end of the next shift. |
| `ShiftCalendarStart` | `SchichtkalenderStart` | Sets the state of objects controlled by the ShiftCalendar. |
| `StartActions` | `StarteAktionen` | Determines if the Entrance Control is activated before entrance actions; FluidSource starts producing fluid. |
| `StartTransporter` | `FahrzeugStarten` | The Transporter starts driving again after the Start delay. |
| `TankEmpty` | `TankLeer` | The Tank is empty; Portioner MU emptied; Mixer container empty. |
| `TankFull` | `TankVoll` | The Tank is full; Mixer container full. |
| `TimeSequence` | `Zeitleiste` | The TimeSequence records data. |
| `TriggerAction` | `TriggerAktion` | The values of the Trigger change. |
| `TriggerStart` | `TriggerStart` | The active time of the Trigger starts. |
| `TurnAnimation` | `DrehAnimation` | Animates rotation of PickAndPlace-robot/Turnplate/Turntable. |
| `UpdateDisplay` | `UpdateDisplay` | Updates the values of the object Display. |
| `ZeroSpeed` | `NullGeschw` | Transporter/Conveyor reach speed 0 after decelerating and change direction. |

## Context Menu of the List of Scheduled Events

Provides commands pertaining to the list of scheduled events:

- **Show Receiver** — select the image of the receiving object in the Frame window.
- **Open Receiver** — open the dialog box of the receiving object.
- **Show Sender** — select the image of the sending object in the Frame window.
- **Open Sender** — open the dialog box of the sending object.
- **Stop at Event** — add a breakpoint for the selected event.
- **Create Breakpoint from Event** — create a breakpoint from the selected event (type in or select missing settings in the dialog Breakpoint).
- **Run to Time** — enter the time of the selected event (rounded down to a tenth of a millisecond) into the Run to Time text box of the EventDebugger.
- **Time** — shows the point in time at which the selected event is going to be executed.

## Slower/Faster Slider

Drag right (or right arrow key) to increase simulation speed; drag left (or left arrow key) to decrease speed. Same effect as the Simulation Speed Slider on the Home ribbon tab.

## Real-time x [EventController]

Select the real-time scaling factor. The scaling factor sets the time that elapses between two events in real-time (duration = simulation time / scaling factor, integer value).

- **Start/Stop Simulation** — uses real-time simulation with a scaling factor of 3 by default.
- **Start Full Speed Simulation** — ignores the scaling factor (full speed, with animation).
- **Start Fast Forward Simulation** — ignores the scaling factor (maximum speed, no animation).

**SimTalk:** `Realtime`, `RealtimeScale`, `start` (EventController)

## Tab Settings

Provides various settings for the simulation run.

### Start Date [EventController]

Type in the Date and Time on which the absolute time during the simulation is based.

**SimTalk:** `StartDate` (EventController)

### End Time [EventController]

Type in the End Time (relative time) at which the simulation will finish. Example: to run for two days, type `2:00:00:00` or just `2:::` and click Apply to translate to the full format.

**SimTalk:** `EndTime` (EventController)

### Statistics [EventController]

Type in the point in time at which the EventController starts collecting statistics data. Plant Simulation resets statistics and starts collecting new statistical data from this time on (useful for discarding warm-up phase data).

**SimTalk:** `StartStat`

### Skip Long Event Intervals

Skips long phases during which no relevant event takes place during real-time simulation. Events of type `Animation` and `UpdateDisplay` are considered not relevant. Fast forwards if no relevant event would take place for at least 10 seconds (real-time), while the animation remains active.

**SimTalk:** `SkipLongEventIntervals`

### Show Summary Report [EventController]

Shows a summary report of the parts which the Drain deleted from the plant. At the end of the simulation run, the report checks all Drain objects and shows:

| Item (English) | Description | Read-Only Attribute |
|---|---|---|
| Object | Names of all Drain objects that removed parts | — |
| Name | Names of the part types removed | — |
| Mean Life Time | Mean life time (throughput time) of parts | `StatAvgLifeSpan` (Drain) |
| Total Throughput | Total throughput of parts | `StatDeleted` (Drain) |
| Throughput per Hour | Parts removed per hour | `StatThroughputPerHour` (FluidDrain) |
| Production | Time portion on production resources | — |
| Transport | Time portion on transport resources | — |
| Storage | Time portion on storage resources | — |
| Value Added | Time portion processed on production resources | `StatProdWorkingPortion` (Drain) |
| Portion | Accumulated production/transport/storage values as bars | — |

The summary report is deactivated by default.

**SimTalk:** `SummaryReport`

## Dialog Box of the Event Debugger

The Event Debugger lets you accurately control the execution of simulation events. You can enter a condition when the Event Debugger is to Start/Stop the Simulation and follow event execution step-by-step.

To open the list of scheduled events, click **List** on the tab Controls, or hold Shift and double-click the EventController icon.

### Breakpoints Active

Select this check box to activate breakpoints. Plant Simulation stops executing the event at an inserted breakpoint.

**SimTalk:** `BreakpointsActive`

### Breakpoints

Opens the dialog **Breakpoints**. You can create a new breakpoint, edit an existing one, or delete the selected breakpoint.

### The Dialog Box Breakpoint

- **Receiver** — select (or type the absolute path to) the object that receives the breakpoint. If empty, applies to events with any receiver. **F2** opens the dialog of the typed object.
- **Sender** — select (or type the absolute path to) the object that sends the breakpoint. If empty, applies to events with any sender. **F2** opens the dialog of the typed object.
- **Start Time** — the Start Time at which the breakpoint will be activated.
- **Stop Time** — the Stop Time at which the breakpoint will be deactivated. Start/Stop Time define the active interval; if omitted, no limits apply.
- **Type** — the type of event for which the breakpoint is active (`*` = any type).
- **Condition** — any expression returning a boolean value. If true, the Event Debugger stops the simulation. The anonymous identifier `@` accesses the Receiver; `?` accesses the Sender.
- **Trace File** — select an existing file into which the Event Debugger writes the scheduled events.

**Code example (Condition):**

```simtalk
@.Name = "Wheel" AND @.getNo = 4
```

or

```simtalk
@.length < 100
```

> **Note:** The Method Debugger cannot track the method of the condition!

### Run to Time [text box]

Type in the point in time up to which the simulation runs once you start it. Once reached, the EventController stops without executing `endSim` methods.

### Trace File

- **Trace File [check box]** — make the Event Debugger write all recorded events to the file. **SimTalk:** `TraceActive`
- **Trace File [text box]** — the name of the file to which the Event Debugger writes events (created if it does not exist). **SimTalk:** `TraceFile`

### EventDebugger Simulation Controls

- **Reset Simulation** — same as the Reset Simulation button in the EventController.
- **Start/Stop Simulation** — same as in the EventController.
- **Start Full Speed Simulation** — full speed with animation, ignores Real Time scaling factor.
- **Start Fast Forward Simulation** — maximum speed, no animation, prevents updating Variable/Display values.
- **Single Step Simulation** — process next event then stop. Hold Shift to open the Method Debugger.
- **Debug Next Simulation Step** — open the Method Debugger for all methods/formulas executed while the event is processed.
- **Step Halts Additionally Before Event** — stop twice if the next event is in the future (first step jumps time to the event, second executes it).
- **Close** — close the Event Debugger window.

## Menus

- **Navigate Menu** — described under the Navigate Menu.
- **View Menu** — provides `Refresh`, `Show Summary Report`, `Show Attributes and Methods`. **SimTalk:** `updateDialog`
- **Tools Menu** — provides `Edit Controls > Init Control`, `Random Numbers Variant`, `Increment Variant on Reset`, `Antithetic Random Numbers`, `User-defined Attributes`, `Edit Observers`, `Show Summary Report`.
- **Help Menu** — described under the Help Menu.

### Init Control [EventController]

Modifies the built-in behavior of the object. Called once at the beginning of the simulation run during the init phase, before the objects are initialized and before `init` methods are executed. Useful for initializing attributes that affect event generation (e.g. availability).

- **Path to an Existing Method** — click the ellipsis button and navigate in *Select Object*; or drag-and-drop a Method from a Frame.
- **Create a Control That Is a Method of the Object** — type a name and select *Create Control* (inserts `self.Name_you_typed`, e.g. `self.A1Ctrl`), or select *Create Control* on an empty text box (inserts `self.OnBuilt_in_name`, e.g. `self.OnEntrance`).

**SimTalk:** `InitCtrl` (EventController)

### Random Numbers Variant

Shows and sets the random numbers variant. Different variants generate different random numbers.

**SimTalk:** `RandomNumbersVariant`, `RandomSeed` (material flow objects)

### Increment Variant on Reset

Sets if different random numbers will be generated after resetting the model.

**SimTalk:** `IncrementRandomNumbersVariantOnReset`

### Antithetic Random Numbers

Sets if Plant Simulation uses common or antithetic random numbers. For a uniformly distributed random number `U` between 0 and 1, antithetic random numbers use `1-U`.

**SimTalk:** `setAntitheticRandomNumbers`

## Methods of the EventController

The EventController provides:
- The methods listed in the table of contents.
- The **Methods of All Objects**.

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods** (F8 on the Frame, or the context menu of the Class Library).
