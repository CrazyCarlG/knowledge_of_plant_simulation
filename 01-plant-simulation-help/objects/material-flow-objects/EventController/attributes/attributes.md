# Attributes of the EventController

The EventController provides:

- The attributes listed in the table of contents.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
EventController.AbsTimeFormat := true
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print EventController.AbsTimeFormat
posit := MyStation.Cont.XPos
```

## AbsTimeFormat

Shows the time of the EventController designated by `<Path>` as the absolute time (`true`) or as the relative time (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.AbsTimeFormat:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example:**

```simtalk
EventController.AbsTimeFormat := false
```

**See also:** Time [EventController]

## BreakpointsActive

Activates (`true`) or deactivates (`false`) breakpoints of the Event Debugger of the EventController designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.BreakpointsActive:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example:**

```simtalk
EventController.BreakpointsActive := true
```

**See also:** Breakpoints Active

## EndTime

Sets the time at which the simulation run controlled by the EventController designated by `<Path>` will end.

> **Remarks:** Plant Simulation does not change the display in the dialog box after assigning a value to the attribute. You have to click **OK** or **Apply** to update the value!

- **Type:** Attribute
- **Syntax:** `<Path>.EndTime:time`
- **Assignment Value:** You can assign a value of data type `time`.

**Example:**

```simtalk
if root.EventController.EndTime - root.EventController.SimTime < 600
   print "Less than 10 minutes until the end of the simulation."
end
```

**See also:** End Time [EventController]

## ExperimentManager

Is set by the ExperimentManager when it controls an experiment of the EventController designated by `<Path>`.

> **Remarks:** If the EventController controls the simulation, the attribute is void.

- **Type:** Attribute
- **Syntax:** `<Path>.ExperimentManager:path`
- **Assignment Value:** You can assign a value of data type `path`.

**Example:**

```simtalk
print EventController.ExperimentManager
```

**See also:** List of Events, ExperimentManager [object]

## IncrementRandomNumbersVariantOnReset

Makes the EventController designated by `<Path>` generate different random numbers after resetting the model (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.IncrementRandomNumbersVariantOnReset:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example:**

```simtalk
EventController.IncrementRandomNumbersVariantOnReset := false
```

**See also:** Increment Variant on Reset, Simulating Random Processes

## InitCtrl

Designates a Method object of the object designated by `<Path>`. The object calls the Init Control once at the beginning of the simulation run during the init phase before the objects are initialized and before init methods are being executed.

> **Remarks:** Plant Simulation runs the init control when you initialize the simulation model controlled by the EventController designated by `<Path>` by clicking **Start/Stop Simulation** or when the method `start` is called.

- **Type:** Attribute
- **Syntax:** `<Path>.InitCtrl:method`
- **Assignment Value:** You can assign a value of data type `method`.

**Examples:**

```simtalk
EventController.InitCtrl := &myInitControl
// The source code of an init control might look like this:
MyWorkersTable[2,1] := 2 // enters the desired amount of the worker John
MyWorkersTable[2,2] := 1 // enters the desired amount of the worker Nellie
WorkerPool.setCreationTable(MyWorkersTable)
```

**SimTalk:** `init` [SimTalk] - predefined name, `start` [SimTalk] - EventController

**See also:** Start/Stop Simulation [EventController], Init Control [EventController], Set How Many Workers Are Created During Initialization

## RandomNumbersVariant

Sets the random numbers variant that the EventController designated by `<Path>` uses.

> **Remarks:** Different variants generate different random numbers.

- **Type:** Attribute
- **Syntax:** `<Path>.RandomNumbersVariant:integer`
- **Assignment Value:** You can assign a value of data type `integer`.

**Example:**

```simtalk
EventController.RandomNumbersVariant := 2
```

**SimTalk:** `RandomSeed` [SimTalk] - material flow objects

**See also:** Random Numbers Variant, Simulating Random Processes

## Realtime

Sets if the method `start` of the EventController designated by `<Path>` will start a real-time simulation (`true`) or a fast forward simulation (`false`).

> **Remarks:** Realtime only applies if you call the method `start` without the second parameter named `Realtime`.

- **Type:** Attribute
- **Syntax:** `<Path>.Realtime:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example:**

```simtalk
EventController.Realtime := false
EventController.start
```

**SimTalk:** `start` [SimTalk] - EventController

**See also:** Real-time x [EventController], Start Full Speed Simulation [Home ribbon]

## RealtimeScale

Sets the time factor of the EventController designated by `<Path>` that elapses between two events in real-time.

> **Remarks:** The value you specify makes sure that the EventController shows the time span with this factor when the simulation proceeds. The duration of an event in real-time is the simulation time divided by the scaling factor you enter. The resulting duration is an integer.

- **Type:** Attribute
- **Syntax:** `<Path>.RealtimeScale:real`
- **Assignment Value:** You can assign a value of data type `real`.

**Example:**

```simtalk
EventController.RealtimeScale := 10
```

**See also:** Real-time x [EventController]

## ResetCtrl

Designates a Method object of the object designated by `<Path>`. Plant Simulation calls the reset control whenever you click **Reset Simulation** in the EventController designated by `<Path>` or when the method `reset` is called.

> **Remarks:** Plant Simulation executes the reset control before calling any reset method you inserted in the Frame and any of its sub-Frames.

- **Type:** Attribute
- **Syntax:** `<Path>.ResetCtrl:method`
- **Assignment Value:** You can assign a value of data type `method`.

**Example:**

```simtalk
EventController.ResetCtrl := &myResetMethod
```

**SimTalk:** `reset` [SimTalk] - EventController

**See also:** Reset Simulation [EventController], Reset Simulation [EventDebugger]

## SkipLongEventIntervals

Makes the EventController designated by `<Path>` skip long phases during which no relevant event takes place during real-time simulation (`true`) or not (`false`).

> **Remarks:** Events of type Animation and UpdateDisplay are considered to be not relevant.

- **Type:** Attribute
- **Syntax:** `<Path>.SkipLongEventIntervals:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example:**

```simtalk
EventController.SkipLongEventIntervals := true
```

**See also:** Skip Long Event Intervals

## StartDate

Sets the date and the time on which the absolute time of the EventController designated by `<Path>` during the simulation is based.

- **Type:** Attribute
- **Syntax:** `<Path>.StartDate:dateTime`
- **Assignment Value:** You can assign a value of data type `dateTime`.

**Example:**

```simtalk
EventController.StartDate := str_to_dateTime("2025/01/02 14:00:00")
```

**See also:** Start Date [EventController]

## StartStat

Sets the point in time at which the EventController designated by `<Path>` resets statistics collection and starts statistics collection anew.

- **Type:** Attribute
- **Syntax:** `<Path>.StartStat:time`
- **Assignment Value:** You can assign a value of data type `time`.

**Example:**

```simtalk
root.EventController.StartStat := str_to_time("40:00.00") // 40 minutes after simulation start
```

**See also:** Statistics [EventController]

## StartStopCtrl

Designates a Method object of the object designated by `<Path>`.

> **Remarks:** Plant Simulation calls the Method whenever you click **Start/Stop Simulation** in the EventController designated by `<Path>` or when the method `start` is called. Plant Simulation also runs the start stop control whenever you click **Single Step Simulation** in the EventController, when the next event is processed, and when the start stop control is executed again. The attribute is also called when the simulation ends.
>
> You can use the expression `?.IsRunning` in the code of the control to tell if the EventController was started (`false`) or stopped (`true`).

- **Type:** Attribute
- **Syntax:** `<Path>.StartStopCtrl:method`
- **Assignment Value:** You can assign a value of data type `method`.

**Example:**

```simtalk
EventController.StartStopCtrl := &myStartStopControl
```

**SimTalk:** `IsRunning` [SimTalk], `start` [SimTalk] - EventController

**See also:** Start/Stop Simulation [EventDebugger], Single Step Simulation [EventDebugger]

## SummaryReport

Makes the EventController designated by `<Path>` show a summary report at the end of the simulation run of those parts which the Drain deleted (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.SummaryReport:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example:**

```simtalk
EventController.SummaryReport := true
```

**See also:** Show Summary Report [EventController]

## TraceActive

Sets if the EventController designated by `<Path>` records events (`true`) or does not record them (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.TraceActive:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example:**

```simtalk
EventController.TraceActive := true
```

**See also:** Trace File [check box]

## TraceFile

Sets the name of the trace file into which the Event Debugger of the EventController designated by `<Path>` writes the event log.

- **Type:** Attribute
- **Syntax:** `<Path>.TraceFile:string`
- **Assignment Value:** You can assign a value of data type `string`.

**Example:**

```simtalk
EventController.TraceFile := "C:\temp\run1"
```

**See also:** Trace File [text box]
