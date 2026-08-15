# Calendars, Lockout Zones & Shift Logic

This document summarizes the Plant Simulation Help topics covering shift systems, the `ShiftCalendar`, and `LockoutZone` objects.

---

## 1. Model Workers with Importer, Broker, and Exporter (Conclusion)

Open the `EventController` and click **Start/Stop Simulation**. Since the `Exporter` can only work at one station at a time, and `Station1` and `Station3` share `Exporter1`, short standstills occur:

- `Station1` has to wait until `Station3` releases `ExporterJob1`, so it is **Blocked**.
- `Station3` has to wait until `Station1` releases `Exporter1`, so it is **Waiting**.
- All stations receive the `Setup` service from `Exporter3`, which is only needed once per station, so it causes no problem.

You can also open the **Statistics** tab to view the data the object collected.

---

## 2. Modeling a Shift System

You can quickly and easily define shifts with the object `ShiftCalendar`.

The `ShiftCalendar` can control the **working hours**, **paused times**, **planned times**, and **unplanned times** of these material flow objects:

`Frame`, `Station`, `ParallelStation`, `AssemblyStation`, `DismantleStation`, `Buffer`, `PlaceBuffer`, `Store`, `Sorter`, `Conveyor`, `AngularConverter`, `Turntable`, `Turnplate`, `Track`, `TwoLaneTrack`, `Source`, `Drain`, `WorkerPool`, and `Exporter`.

It can also control `Frames` that model components of the overall plant. Here you use **Methods** as unplanned time and paused time controls of the Frame to propagate the shift settings to objects inside the Frame.

For fluid objects, the `ShiftCalendar` can control working hours, paused times, planned times, and unplanned times of:

`FluidSource`, `Mixer`, `Portioner`, and `DePortioner`.

You can use the method `schedule` to make the `ShiftCalendar` set the date and time to start or finish the production process.

### Starting and Ending a Shift

- When a `ShiftCalendar` **starts a shift**, it sets the attribute `Unplanned` of the material flow objects and Frames it controls to `false` (deactivates unplanned times). If needed, you can program an **Unplanned Control** for other actions.
- The statistics of the material flow objects then start to collect the **unplanned time** — the time a resource is not planned to work.
- Example: shifts active from 06:00 to 22:00 → planned time is 06:00–22:00; unplanned time is 22:00–06:00 the following morning.
- When a `ShiftCalendar` **finishes a shift**, it sets `Unplanned` to `true` (activates unplanned times). The objects stop processing the current part and release all services.

### Starting and Ending a Break

- When a `ShiftCalendar` **starts a break**, it sets the attribute `Pause` to `true` for the material flow objects and Frames it controls. For material objects, activating a pause also affects statistics; for Frames, Plant Simulation only changes the attribute state (you can program a **Pause Control**).
- When a `ShiftCalendar` **ends a break**, it sets `Pause` to `false`.

Sample models are available under: **Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples**.

---

## 3. Defining Shifts with the ShiftCalendar

Insert the `ShiftCalendar` from the folder **Resources** in the Class Library, or from the toolbar **Resources** in the Toolbox.

You can:

- Specify the names of the shifts, the respective times and days
- Specify times during which the plant works part of the time
- Specify the stations which the `ShiftCalendar` controls
- Schedule date and time to start or finish the production process

Once settings are entered, select the check box **Active** so Plant Simulation uses the shifts.

### Specify the Names of the Shifts, the Respective Times and Days

Before typing data, click the **Inheritance** check box. Type the data for one shift into the cells of one row:

- **Shift** — names of shifts (e.g., Morning shift, Day shift, Evening shift, Graveyard shift).
- **From** — shift start times (between 0:00 and 24:00; only hours and minutes).
  - A shift within one day: end time greater than start time (e.g., Morning shift 6:00 → 14:00).
  - A shift spanning two days: end time smaller than start time (e.g., Graveyard shift 22:00 → 6:00 next day).
- **To** — shift end times (0:00–24:00, hours and minutes only).
- **Days of the week** — click the cells below the days to select active days (e.g., Morning shift Monday–Saturday; Evening shift Monday–Friday).
- **Pauses** — break times for each shift, e.g. `9:00-9:15;12:00-12:45` (coffee break + lunch break). Separate multiple breaks with a semicolon.

Click **Apply** to make the `ShiftCalendar` check that break values are plausible and correctly formatted.

You can also **import/export** shifts as tab-delimited text files (right-click the list field → **Export** or **Import**).

### Specify Times During Which the Plant Works Part of the Time

Click the **Inheritance** check box first.

- **Date From** — date the plant starts not working. Double-click the cell, click the down arrow, and select a date in the calendar.
- To designate an entire day as a day-off, enter only a start date (no **Date To**, no **Reduce Time To**).
- **Date To** — date the plant stops not working (select from the calendar).
- **Reduce Time To** — for a single day working part-time, type the start and end hours of reduced working time (e.g., `0:00 - 12:00` for a half day on Christmas Eve).
- **Comment** — description of why the plant does not work.

> **Note:** The `ShiftCalendar` combines the reduced time and the shift definitions for a day. If a reduced working day's start time falls on a break, the work day starts with a break.

You can also import/export a calendar as a tab-delimited text file.

### Specify the Stations Which the ShiftCalendar Controls

Enter the name of any built-in material flow object, or the name of a `Frame` used to model a machine, into the cells of the list.

This automatically enters the `ShiftCalendar` into:

- The dialog **Select Shift Calendar** opened by the command **Select Shift Calendar** on the Frame ribbon tab.
- The text box **Shift calendar** on the **Controls** tab of the material flow object.

### Schedule Date and Time to Start or Finish the Production Process

Use the method `schedule` to set the date and time to start or finish the production process. There are two modes:

- **Forward scheduling** — beginning from the start date forward into the future.
- **Backward scheduling** — computes the start date going backward in time from the demand date.

Normally you start with the demand date and compute the start date through backward scheduling. If that start date is in the past, recompute beginning with the present time and forward-schedule the end date.

Example — computing the end date of two jobs considering the shifts defined in the `ShiftCalendar`:

```simtalk
var startTime := str_to_dateTime( "4.1.2013 0:00" )
var durationTime := str_to_time( "10:00:00.0" )
var EndTime := ShiftCalendar.schedule( startTime, durationTime, "forward" )
print "StartDate: ", startTime, "   Duration: ", durationTime, "   EndDate: ", EndTime
startTime := str_to_dateTime( "20.12.2013 0:00" )
durationTime := str_to_time( "19:00:00.0" )
EndTime := ShiftCalendar.schedule( startTime, durationTime, "forward" )
print "StartDate: ", startTime, "   Duration: ", durationTime, "   EndDate: ", EndTime
```

The first job starts on January 4, 2013 at midnight and takes 10 hours. The second starts on December 12, 2013 and takes 19 hours. The method prints the results to the Console.

---

## 4. Pausing Material Flow Objects and Frames

The `ShiftCalendar` interacts with the material flow objects and Frames it controls by changing their `Paused`/`Planned`/`Unplanned` state.

An object is:

- **Paused** — not processing parts due to a pause. It resumes once the pause ends (select **Planned** from the drop-down list or set `Pause` to `false`).

> **Note:** When a station fails and a pause occurs during the failure, the failure time is still consumed even though the station is paused. Statistics counts overlapping states as paused time. Resetting the model removes both failures and pauses.

- **Unplanned** — not scheduled to work during the shifts defined in the `ShiftCalendar`.
- **Planned** — scheduled to work during the shifts. Planned/scheduled time is the processing time minus the break times.

### Paused Material Flow Objects

The `ShiftCalendar` changes the paused state of material flow objects according to the defined shifts. The dialog of these objects reflects the present state in the drop-down list during a simulation run.

When paused, a material flow object does not receive any mobile parts. MUs can exit the object only when a Method makes them do so. Plant Simulation stops set-up and processing until the end of the pause or unplanned time.

The unplanned state is identical to the paused state; the only difference is how Plant Simulation counts internal statistics. When planned/scheduled to work, the object receives and processes MUs and moves them to the succeeding object.

### Paused Frames

Pause a `Frame` with its attributes `Pause` and `Unplanned`. Unlike material flow objects (which can also be paused manually), you can only change the paused/unplanned states of a Frame via its attributes.

You can also program a pause and/or unplanned time control, both of which activate a Method when the attribute value changes.

#### Example of a Pause Control

Assign `true` or `false` to the attribute `Pause`. Use the anonymous identifier `?` to access the object from within a control. Plant Simulation executes the Pause Control whenever the paused state changes; reading the paused state within the Method shows the state after the change.

```simtalk
print "Current pause ", current.pause
MyStation.pause := current.pause
var shift := root.ShiftCalendar.getCurrShift
print "Current shift: ", shift
if not current.unplanned 
   if current.pause 
      current.currIcon := "pause"
   else
       current.currIcon := "working"
   end
end 
```

#### Example of an Unplanned Control

Plant Simulation executes the Unplanned Control whenever the unplanned state of the Frame changes. Assign `true` or `false` to the attribute `Unplanned`. Use `?` to access the object.

```simtalk
print "Frame unplanned: ", current.unplanned
MyStation.unplanned := current.unplanned
if current.unplanned 
   current.currIcon := "unplanned"
else
   if current.pause 
      current.currIcon := "pause"
   else
      current.currIcon := "working"
   end
end
```

---

## 5. Modeling a Lockout Zone

The `LockoutZone` combines a group of material flow objects. If one of these stations fails, all other stations that are part of the lockout zone stop processing their parts.

You have to define failure profiles for at least one of the assigned stations. As soon as one station fails, the `LockoutZone` stops all processing operations of all assigned stations. You can select whether it stops immediately or when the required service arrives.

Stations only start processing again after **all** failures are removed, using up only the remaining processing time. You can assign any built-in Material Flow Object or a station modeled in a Frame.

Insert the `LockoutZone` from the folder **Resources** in the Class Library or the toolbar **Resources** in the Toolbox.

You can:

- Specify the stations which the `LockoutZone` stops
- Create a failure profile for one of the stations
- Stop the associated stations immediately after a failure
- Stop the associated stations when the repair man arrives
- Use a Stop Processing Control
- Use a Resume Processing Control

### Specify the Stations Which the LockoutZone Stops

In the sample model, `Station2`, `Station3`, and `Station4` are part of the lockout zone. If `Station3` fails, the lockout zone stops `Station2` and `Station4`.

The stopped-time percentages of `Station2` and `Station4` must match the Failed-time percentage of `Station3`; total availability of the stations within the lockout zone matches the availability of `Station3`.

To add a station as a resource:

- Drag the object's icon (e.g., `Station2`) over the `LockoutZone` icon and drop it there.
- Repeat for `Station3` and `Station4`.

To visually clarify which objects belong to the lockout zone, insert a `Cuboid` into the Frame and assign a Material:

- Click **Cuboid** on the **Edit** ribbon tab and type a small value for **Dimension Z** (height).
- Insert the Cuboid above `Station2` and press **M** to show the manipulators.
- Click the bottom-right corner of the Cuboid and drag it to cover the `LockoutZone` and stations.
- Adjust caption positions (e.g., select `Station1`, press spacebar, change to **Captions** tab in **Edit 3D Properties**; use a Y position of -1.35 for the affected stations).
- Adjust the caption of the `LockoutZone` and assign a Material/color to the Cuboid.

### Create a Failure Profile for One of the Stations

To make one station fail (e.g., `Station3`):

- Click the **Failures** tab and click **New**.
- Enter an **availability** and a **mean time to repair** (e.g., availability 85%, MTTR 15 minutes).
- Click **OK**.

### Stop the Associated Stations Immediately After a Failure

Select **Stop mode > Stop immediately**. The `LockoutZone` then immediately stops `Station2` and `Station4` as soon as `Station3` fails — only stations that are part of the lockout zone are stopped.

Check the statistics:

- Open the dialogs of `Station2`, `Station3`, and `Station4` and go to the **Statistics** tab.
- The stopped percentages of `Station2` and `Station4` match the failed percentage of `Station3`; overall availability matches the failed station.
- To open the statistics report, select the stations in the Frame and press **F6**.

### Stop the Associated Stations When the Repair Man Arrives

Select **Stop mode > Stop when Service arrives**. The `LockoutZone` stops the assigned stations when the repair service requested by the failed station is assigned.

To create the sample model:

- Insert the stations and drag them over the `LockoutZone` icon (e.g., `Station2`, `Station3`, `Station4`).
- Add a `Workplace` to the stations and connect it to the `WorkerPool` with a footpath.
- Define a failure profile for `Station3`.
- Insert a `Broker`, assign it on the sub-tab **Failure**, and activate the failure importer. No other settings need changing.
- Run the simulation. When `Station3` fails, the Worker walks from the `WorkerPool` to the failed station on the footpath. Once the service technician reaches the `Workplace` attached to the failed station, the `LockoutZone` stops the associated stations.

### Use a Stop Processing Control

To use your own logic when one of the assigned stations fails, program a **Stop Control**. Within the Stop Control, the anonymous identifier `@` designates the triggering station, while `?` designates the `LockoutZone`.

Example (writing info into the table `ReportStopping`):

```simtalk
var row:integer := ReportStopping.ydim + 1
ReportStopping["First Failed Station",row] := @.name
ReportStopping["Start Stopping",row] := eventcontroller.simTime
```

### Use a Resume Processing Control

To use your own logic when all failures of all assigned stations were repaired and the stations can continue, program a **Resume Control**. Within it, `@` designates the triggering station and `?` designates the `LockoutZone`.

Example:

```simtalk
var row: integer := ReportStopping.ydim
ReportStopping["Last Failed Station",row] := @.name
ReportStopping["End Stopping",row] := eventcontroller.simTime
ReportStopping["Duration",row] := ReportStopping["End Stopping",row] - ReportStopping["Start Stopping",row]
```

### Stopped Material Flow Objects and Frames

The `LockoutZone` stops the assigned material flow objects by setting their attribute `Stopped` to `true`. It stops an assigned Frame by setting its attribute `Stopped` to `true` as well.
