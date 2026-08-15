# Read-Only Attributes of the EventController

The EventController provides:
- The read-only attributes listed in the table of contents.
- The read-only attributes of all objects.

You can query the values of read-only attributes, but you cannot set them — Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the object's tabs (for example, the tab **Statistics**).

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the members of the selected class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the members of the selected instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print EventController.AbsSimTime
```

---

## AbsSimTime [SimTalk]

Returns the current simulation time of the EventController designated by `<Path>` as an absolute time statement.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.AbsSimTime → dateTime`
- **Return Value:** `dateTime`

**Example**

```simtalk
print EventController.AbsSimTime // might return 22026-01-01 06:00:00.0000
```

**See also:** Time [EventController]

---

## GetNextEventTime [SimTalk]

Returns the time at which the next event in the event list of the EventController designated by `<Path>` is scheduled to be executed.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.GetNextEventTime → time`
- **Return Value:** `time`

**Example**

```simtalk
print EventController.GetNextEventTime // might return 10.0000
```

**See also:** List of Events

---

## IsFinished [SimTalk]

Returns whether the EventController designated by `<Path>` has stopped the simulation and has executed all `endSim` methods (`true`) or not (`false`).

**Remarks:** In contrast to the read-only attribute `IsRunning`, `IsFinished` only becomes `true` after all `endSim` methods have been executed.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.IsFinished → boolean`
- **Watchable:** Yes
- **Return Value:** `boolean`

**Example**

```simtalk
print root.EventController.IsFinished
```

**See also:** `endSim` [SimTalk], `IsRunning` [SimTalk]

---

## IsInitialized [SimTalk]

Returns whether the EventController designated by `<Path>` has been initialized (`true`) or not (`false`).

**Remarks:** Plant Simulation initializes the EventController if all the `init` methods, which expect an integer argument, are called with a value of `1` for init phase 1 and all objects are initialized. This is, for example, the case if a failure profile is active and all objects have calculated their first failure event, if the attribute `HasInitValue` of any Variable is set to `true` and the Initial Value has been reset, etc.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.IsInitialized → boolean`
- **Watchable:** Yes
- **Return Value:** `boolean`

**Example**

```simtalk
print root.EventController.IsInitialized
```

**See also:** `HasInitValue` [SimTalk] - Variable, `InitValue` [SimTalk] - Variable, Initial Value [Variable]

---

## IsResetting [SimTalk]

Returns whether the EventController designated by `<Path>` is being reset at the moment (`true`) or not (`false`).

**Remarks:** Plant Simulation sets `IsResetting` to `true` when you reset the simulation model with the EventController designated by `<Path>`. Plant Simulation sets it to `false` again as soon as all `reset` methods have been processed.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.IsResetting → boolean`
- **Watchable:** Yes
- **Return Value:** `boolean`

**Example**

```simtalk
print EventController.IsResetting
```

**See also:** `reset` [SimTalk] - EventController

---

## IsRunning [SimTalk]

Returns whether the EventController designated by `<Path>` is running at the moment (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<Path>.IsRunning → boolean`
- **Watchable:** Yes
- **Return Value:** `boolean`

**Example**

```simtalk
print root.EventController.IsRunning
```

**See also:** `IsFinished` [SimTalk]

---

## SimTime [SimTalk]

Returns the current simulation time of the EventController designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.SimTime → time`
- **Watchable:** Yes
- **Return Value:** `time`

**Note:** You can, for example, watch the `SimTime` value with an object of type Display or Chart. You should never use `SimTime` in a method that affects the simulation with a `waituntil` instruction or a `stopuntil` instruction. The time does not advance continuously, but jumps from event to event. If you activate the animation, Plant Simulation generates additional events so that the `waituntil` or `stopuntil` instruction might be woken up at an earlier point in time than intended.

**Examples**

```simtalk
param sensorID: integer, Front: boolean
if @.ID = 1 
   @.Speed := 0
   print EventController.SimTime, " The first Transporter stopped."
end
```

```simtalk
print "Machine was deactivated at:",
root.EventController.SimTime."
```

**See also:** Time [EventController], `waituntil` [SimTalk], `stopuntil` [SimTalk]
