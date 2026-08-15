# Methods of the EventController

The EventController provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## Reading the Syntax Line

An example of the syntax line of an individual method might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses. The expression `(Parameter:string)`, for example, designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

- Optional parameters are listed within brackets. The expression `[,Parameter:boolean]`, for example, means that you can, but do not have to enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `→ boolean` in the example above.

---

## getEventList [SimTalk]

Returns the list of scheduled events of the EventController designated by `<Path>`.

**Type:** Method

**Syntax:**

```
<Path>.getEventList(MaximumNumberOfEvents:integer) → table
```

**Parameter**

The parameter `MaximumNumberOfEvents` of data type integer designates the maximum number of events, which the EventController writes to the data table.

Specify `getEventList(-1)` to write all events to the data table. The event list provides the columns **Type**, **Time**, **Receiver**, **Sender**, **Insertion Time**, and **Parameters**.

**Return Value**

The return value has the data type table.

**Example**

```
TableVariable := EventController.getEventList(-1)
```

**See also:** List of Events, Event List

---

## reset [SimTalk] - EventController

Makes the EventController designated by `<Path>` run all methods in your simulation model that are named `reset`.

**Remarks**

Once all reset methods have been executed, Plant Simulation:

- Deletes all unprocessed events
- Resets the simulation time to 0
- Resets the statistics
- Clears all failures of all objects in the simulation model
- Sets all objects to the state planned
- Deletes all parts if you activate
- Reactivates inheritance of the settings Entrance Locked and Exit Locked for new models if you leave **Tools > Inherit 'Entrance/Exit Locked On Reset** active.

> **Note:** The Request Control, the Receive Control, and the Release Control of the Importer are not being called when you reset the simulation.

Plant Simulation does not execute the reset the simulation command immediately, but only when all methods being executed at the moment have been completely executed. This includes the method, which has triggered the Reset action. The method `start` behaves like this as well.

**Type:** Method

**Syntax:**

```
<Path>.reset
```

**Example**

```
EventController.reset
EventController.start
EventController.RandomNumbersVariant :=
EventController.RandomNumbersVariant + 1
// When this method has been executed all the way, the Eventcontroller will
be reset.

// When the reset phase has been finished all the way, the simulation will
be started again.
end
```

**See also:** ResetCtrl [SimTalk], reset [SimTalk] - predefined name, start [SimTalk] - EventController, Reset Simulation [EventController], Reset Simulation [EventDebugger], Entrance Locked [material flow objects], Exit Locked [material flow objects], Inherit 'Entrance/Exit Locked' On Reset

---

## start [SimTalk] - EventController

Activates the EventController designated by `<Path>` and starts the simulation run.

**Remarks**

If the method is called during the simulation run for another EventController in another Frame, Plant Simulation stops the current EventController and starts the simulation run in the other Frame.

Plant Simulation does not start the EventController immediately, but only when all methods being executed at the moment have been completely executed. The method `reset` behaves like this as well.

**Type:** Method

**Syntax:**

```
<Path>.start([WithAnimation:boolean:=animation,
RealTime:boolean:=EventController.Realtime])
```

**Parameters**

You can specify the following parameters:

- The parameter `WithAnimation` of data type boolean sets if the simulation will be started with animation (`true`) or without animation (`false`).

  **Default Value of the Parameter:** The default value is `animation`. If you do not specify this parameter, the EventController considers the global setting for the animation, compare MUs and States and the function `animation`.

- The parameter `RealTime` of data type boolean sets if the EventController starts a real-time simulation (`true`) or a full-speed simulation (`false`).

  > **Note:** Real-time simulation considers the real-time factor and can thus run faster than real-time if the real-time factor is greater than 1. It can run slower if the real-time factor is smaller than 1.

  **Default Value of the Parameter:** The default value is `EventController.Realtime`. If you do not specify this parameter, the EventController uses the value of the attribute RealTime.

**Example**

```
.delivery.EventController.start(false,false) // starts the simulation with
maximum speed without animation
```

**See also:** reset [SimTalk] - EventController, Realtime [SimTalk], animation [SimTalk], Start/Stop Simulation [EventController], MUs and States [Home ribbon], Real-time x [EventController]

---

## stop [SimTalk] - EventController

Stops the EventController designated by `<Path>` and thus terminates the simulation run.

**Remarks**

The simulation will not stop until the current method execution (including the entire call stack) finished or was suspended. A `wait`-statement will for example suspend method execution.

**Type:** Method

**Syntax:**

```
<Path>.stop([EndSim:boolean:=false])
```

**Parameter**

The optional parameter `EndSim` of data type boolean sets if the simulation will be stopped and if the `endSim` methods will be executed (`true`) or if the simulation will only be stopped (`false`).

**Default Value of the Parameter**

The default value is `false`.

**Example**

```
root.EventController.stop
```

**See also:** endSim [SimTalk], Start/Stop Simulation [EventController], wait [SimTalk], Suspending Methods

---

# Read-Only Attributes of the EventController

The EventController provides:

- The read-only attributes listed in the table of contents to the left.
- The Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To query the value of a read-only attribute, you might, for example, type:

```
print EventController.AbsSimTime
```
