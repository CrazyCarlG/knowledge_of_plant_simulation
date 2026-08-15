# Processing, Set-up, Failures, Buffers, Inventory

This document summarizes Plant Simulation help for modeling the flow of materials: setting up stations, defining processing times, modeling failures, buffering parts, and placing parts into/removing them from stock.

---

## 1. Setting a Station Up

You can define how the objects **Station**, **ParallelStation**, **AssemblyStation**, **DismantleStation**, and **Drain** set up to process another type of MU.

You can:
- Select **Set-up Options** on the tab *Set-Up*.
- Select the **Set-Up Time** on the tab *Times*.

### Selecting Set-up Options

Next to *Set-up For*, Plant Simulation shows which type of MU the object is presently set up for (or is going to be set up for). If not set up yet, it shows a hyphen `-`. To distinguish MU types, Plant Simulation uses the MU name or a user-defined attribute.

First select how the station sets up:
- **Set the Station Up Automatically**
- **Only Set the Station Up When it is Empty**
- **Set the Station Up after it Processed a Certain Number of Parts**

Then **Select the Set-Up Criteria**.

#### Set the Station Up Automatically
Select **Automatic** so the object triggers the set-up process as soon as an MU of the corresponding type intends to move onto it. To define the set-up process in a Method, clear the check box.

#### Only Set the Station Up When it is Empty
Select **Only When Empty** to start set-up for the next type only when the object is empty. MUs of the target type can only enter after the set-up finishes. Their set-up time begins when all specified set-up processes are finished; MUs already on the object are processed with the settings of the type for which it was set up before.

#### Set the Station Up after it Processed a Certain Number of Parts
Select **Set-up After** and enter the number of parts after which the object sets up. The object also sets up (and restarts counting from 1) when the part type changes before the entered number is reached.

> **Note:** The **ParallelStation** does not provide the setting *Set-up After n Parts*.

The object always sets up for the part type that enters next, so set-up does not start immediately after the n-th part is processed. Choose:
- **Before Next Part** — set up immediately after the n-th part was processed.
- **After Last Part** — set up after the (n+1)-th part wants to move onto the station.

> **Note:** The number of parts is the number entering the station; they do not necessarily have to be processed. Statistics also counts parts removed before processing (e.g., during set-up or while waiting for a service).

#### Select the Set-Up Criteria
Decide when the object has to be set up:
- When the **MU Name** changes.
- When the value of a **user-defined attribute** of the MU changes. Select *User-defined Attribute* and enter the attribute name (must be of data type `string`). The object sets up when an MU with a different attribute value moves on. Example: an attribute `Color` where the station is set up for "red"; when an MU with value "blue" moves on, it sets up for blue.

### Select the Set-Up Time

The **Set-up Time** is the time to set the station up for a different MU type. MUs of the same name are the same type and require no set-up. On the tab *Times* you can select a distribution, or enter a constant time. You can also select the **Matrix(Type)** distribution when the time depends on both the **source type** and the **target type** (define times in a table; row index = source type, column index = target type).

With the **Formula** distribution you can enter a numeric expression or the name of a Method, using the anonymous identifier `@` to access the MU.

> **Note:** You can also determine the set-up time in a user-defined attribute of data type `method` created for the MU.

---

## 2. Defining Processing Times

The **Processing Time** is the time the MU remains on the material flow object to be processed — the interval between set-up and moving it to its successor. On the tab *Times* you can:
- Select a distribution and enter required values.
- Enter a constant time (`Const`).
- Select `List(Type)` to process the MU depending on its type.
- Select `List(Place)` to process depending on the station/place on a ParallelStation.

With **Formula**, type a numeric expression or a Method name, using `@` to access the MU. The Method may also be a user-defined attribute of data type `method` of the MU.

### Specify Times in Object Dialogs
Times use the format `days:hours:minutes:seconds` (e.g., `12:34` = 12 minutes 34 seconds). Type `1:::` for one day (converted to `1:00:00:00`). Numbers without a colon are interpreted as seconds (e.g., `111` = 1 minute 51 seconds). Change time settings under *File > Model Settings/Preferences > Units > Time Scale*.

### Specify Data of a Probability Distribution
Select the distribution from the drop-down list; Plant Simulation shows the required parameters when you click into the text box. Lower and upper bounds are optional.

### Define Processing Times Depending on the Type of MU
Use the `List(Type)` distribution, enter a DataTable name, put MU names in column 1 and times (seconds) in column 2. Plant Simulation reads the processing time from the table during the run.

### Define Processing Times in a Formula
Define the processing time via:
- A Method name (method must return `time`).
- A basic arithmetic operation typed directly into the text box.
- A formula typed directly, accessing the MU with `@`.

Example Method (`cyclesMethod`), returning time based on MU color:

```
-> time
if @.Name = "red"
   result := 60
elseif .Name = "blue"
   result := 180
else
   result := 120
end
```

Arithmetic operator example: `@.MyAttribute+1` adds 1 minute to MUs with the user-defined attribute `MyAttribute`.

Accessing the MU directly: type `@.timeRed`, after creating a user-defined attribute `timeRed` for the MU.

### Define Processing Times of a ParallelStation
For a ParallelStation with several processing places that have different but constant times, use the `List(Place)` distribution and enter a DataTable name. Entry `[1,2]` matches the processing place at position `[1,2]`.

---

## 3. Modeling Failures

To model machines that fail, define one or several **failure profiles**. Failures affect the technical availability of individual stations. You can:
- Manually fail an object by selecting **Failed** (and clear it manually).
- Define failures with the failure generator on the tab *Failures*.

The station state changes from *operational* to *failed* (shown as a red ring on a pole by default). When failed, the object becomes **inactive** for the failure duration — it receives no parts; a part already on it has processing interrupted and resumed when the failure clears. Plant Simulation adds the failure duration to the processing/dwelling time. A blocked MU is unblocked when the failure ends.

### Configure Failures
Procedure:
1. Select the **Active** check box on the tab *Failures*.
2. Click **New** and enter the parameters of the failure profile.
3. Enter a **Name**.
4. Select if the profile is **Failed** during the run.
5. Select a distribution for the **Start** (time of first failure). The *Lognormal*, *Erlang*, and *Negative exponential* distributions are especially suited for failures.
6. Select a distribution for the **Stop** (time of the last failure).
   - If no Start/Stop time is entered, the first failure occurs after the **Interval** is over.
7. Select **Availability** and enter **Availability** (percent) and **MTTR**, or clear it to specify **Interval** and **Duration** directly. Availability and MTTR are just another representation of Interval/Duration; applying them computes Interval/Duration (and selects Negexp for Interval, Erlang for Duration). Availability of 100% gives MTTR of 0.
8. If clearing *Availability*, select distributions for the **Interval** (time between end of last failure and beginning of next) and the **Duration** of the failure.
9. Select the time base to which failures relate:
   - **Simulation Time** — consumes failure interval time regardless of object state.
   - **Operating Time** — consumes time only if the object is operational (interrupted by pauses/failures).
   - **Processing Time** — consumes time while the object is processing (or moving for conveying objects). For a ParallelStation, the simulated MTBF is reduced as the number of parallel processing operations increases.
10. Click **OK** to add the profile (double-click or **Edit** to edit).
11. Repeat for additional profiles.

> **Note:** When changing failure settings, first clear **Active**, click Apply, change settings, apply, then re-select **Active** so the next failure event is computed with a complete set of valid parameters.

### Change Failure Settings During the Simulation Run
To reduce the Availability/MTTR of `MyStation` during the run, enter into a Method (here `setFailure`):

```
// Reduces the availability and the MTTR during the simulation run.
// This method is called by the init method via a method call after 12 hours.
print EventController.simTime," Simulated availability in the morning: ",round(100 * (1 - MyStation.StatFailPortion),2)," %"
MyStation.initStat
// reduce the availability
MyStation.Availability := 80
MyStation.MTTR := str_to_time("10:00")
MyStation.FailureActive := false
MyStation.FailureActive := true // activate failures
```

> **Note:** With a single failure profile, use the simplified notation above. With several profiles, address attributes via the profile, e.g., `MyStation.Failures.MyFailureProfile1.Availability := 80`.

In the init method, schedule the reduction after 12 hours:

```
&setFailure.executeIn(str_to_time("12:0:0"))
```

In the reset method, reset the availability:

```
MyStation.Availability := 100
```

In the endSim method, show the simulated availability in the Console:

```
print EventController.simTime," Simulated availability in the afternoon: ", round(100 * (1 - MyStation.statFailPortion),2)," %"
```

Type `1:00:00:00` to simulate a day, run the simulation, and watch the Console.

---

## 4. Buffering Parts within the Production Line

The **Buffer**, placed between two components or stations, serves two purposes:
- Temporarily holds parts when a following component fails.
- Moves parts on when preceding components stop, preventing the process from halting.

Dimensioning a Buffer with enough capacity to cover all failures completely decouples both components. It also compensates for fluctuating transport/operating times that cause queues. Insert it from the folder *MaterialFlow* in the Class Library or the toolbar *MaterialFlow* in the Toolbox.

### Use a Buffer between Processing Stations
In a simple line (source → processing station → test station → drain), the processing station is occasionally blocked because the test station is too slow. Insert a **Buffer** between them; it temporarily holds parts before moving them on. Example changes: capacity from 4 to **200**, processing time of **15 minutes**.

The tab *Statistics* shows relative occupancy, the percentage of time relatively empty/full, max/min contents, and entries/exits. You can use a **Chart** to show the number of parts over time.

### Check the Fill Level of the Buffers in the Plant
- In 3D, select **Fill level** from the *Show Contents As* drop-down list.
- On the tab *Statistics*: **Relatively empty** = portion of the collection period the object was empty relative to available time; **Relatively full** = portion all temporary storage places were occupied relative to available time.

#### Configure the Processing Stations
Insert and configure processing stations. Example: five **ParallelStation** objects, X-Dimension and Y-Dimension of 2 (4 processing places each), a normally distributed processing time, and failures with an availability of 92 percent.

#### Configure the Buffers
Insert and configure the Buffers (example: four Buffers). Run the simulation and check each Buffer's *Statistics* tab, specifically *relatively empty* and *relatively full*.

#### Configure the Chart for Showing the Full and Empty Portions
- Insert a **Chart**.
- Tab *Display*: Category > Chart.
- Tab *Data*: Data Source > **Input Channels**; deactivate inheritance of the input channels table and click Input Channels.
- Enter labels **Empty**, **Partially full**, **Full** into the row index cells.
- Create a drag-and-drop control: *Tools > Edit Controls*, click next to drag-and-drop, press **F4** (creates a user-defined attribute of data type `method`). Paste:

```
param draggedObjects: object[]
var obj: object
var numBuffers: integer
var MyTab : table := @.InputChannels // inheritance of the table 'InputChannels' is already deactivated
MyTab.delete({1,0}..{*,*})
for var i := 1 to draggedObjects.dim 
   obj := draggedObjects[i]
   switch obj.internalClassType
   case "Buffer", "PlaceBuffer", "Sorter" 
      numBuffers := self.~.InputChannels.xDim +1
      
      MyTab[numBuffers,0] := obj.Name
      MyTab[numBuffers,1] := obj.Name + ".statRelativeEmptyPortion"
      MyTab[numBuffers,2] := "1 - " + obj.Name + ".statRelativeEmptyPortion - " + obj.Name + ".statRelativeFullPortion"
      MyTab[numBuffers,3] := obj.Name + ".statRelativeFullPortion"
       
   end
next
   
print "Number of detected buffers: ", numBuffers
@.InputChannels := MyTab // makes the chart apply the new settings
@.Active := true
```

- Drag a marquee over all objects, drag them onto the Chart, and drop them. The Chart automatically knows which objects it can display.

#### Show the Fill Level of the Buffers
Select **Fill Level** from *Show Contents As* on the tab *Fill Level* of *Edit 3D Properties* (also set Position, Rotation, Dimension). The fill level bar shows only a quantitative portion, not exact numbers.

| Item | Description | Looks like this |
|---|---|---|
| **MUs** | Shows the MUs stacked in the Buffer (previous-version setting). | |
| **Fill level** | Shows relative fill level on the picture. Gray = background; Red = >90%; Orange = <10%; Green = in between. | |
| **Both** | Shows MUs stacked on top of the fill level indicator. | |

---

## 5. Placing Parts into Stock and Removing Them

To model a warehouse, use the object **Store**. Parts remain in the Store until removed with a Method. The Store accepts parts as long as storage places are available. An incoming part triggers a sensor that calls an **Entrance Control** (a Method) determining the storage place. Without an Entrance Control, the Store deposits into the first free storage place in the coordinate net.

Sample model objects:
- **Source** `Receiving` — creates parts.
- **ParallelStation** `MixOrders` — mixes the original production sequence.
- **Store** `MyStore` — places parts in stock and removes them.
- **Station** `RetrieveFromStore` — retrieves required parts.
- **Drain** `Shipping` — removes parts from the plant.

Material flow is controlled by `placeInStock` (Entrance Control) and `removeFromStock` (Exit Control of `RetrieveFromStore`); both call `AttemptToRemoveNextPart`, which manages the inventory table. Connect `Receiving → MixOrders → MyStore` and `RetrieveFromStore → Shipping` with Connectors (do **not** connect `MyStore` and `RetrieveFromStore`, since retrieving is method-controlled).

### Configure the Stations
- Source: `Interval = 1:00`, `Stop = 1:00:00:00`.
- `MixOrders` (ParallelStation): X-Dimension 200, Y-Dimension 20; random processing time with **Uniform** distribution, parameters `0, 30:00`.
- Store: Dimensions 4 and 8; set Entrance Control to `PlaceInStock`.
- `RetrieveFromStore`: set Exit Control to `RemoveFromStock`, select **Rear** (rear-triggered).

### Program the Method that Places Parts into Stock
Method `placeInStock` (Entrance Control):

```
// entrance control of the object ’MyStore’
// find next free row in the ’InventoryTable’ of ’MyStore’
var NextRow : integer
var NextRow := Inventory.ydim + 1
// enter the ID of the new part and the path
// to the part in the ’InventoryTable’
InventoryTable[0,NextRow] := @.id
InventoryTable[1,NextRow] := @
AttemptToRemoveNextPart // name of our Method 
// increase the capacity of ’MyStore’ if needed
if MyStore.full 
   MyStore.xDim := MyStore.xDim + 4
end
```

### Program the Method that Removes Parts from Stock
Exit Control of `RetrieveFromStore` (`RemoveFromStock`):

```
// rear-triggered exit control of the station 'RetrieveFromStore'
// catches the event after a part has been successfully 
// removed from the Store and left the station 'RetrieveFromStore'
AttemptToRemoveNextPart // name of our Method
```

### Program the Method that Manages the Inventory Table
Method `attemptToRemoveNextPart` (inventory table with two columns: `Sequence` and `MU`):

```
// control called by the methods ’placeInStock’ and ’removeFromStock’
var sequenceNo : integer
var part       : object
// check if the next part according to the original sequence
// is already located in ’MyStore’
if InventoryTable.getRowNo(#NextNumber)>0 
   part := InventoryTable[1,#NextNumber]
   sequenceNo := part.id
end
```

### Display a Value During the Simulation with a Variable
The Variable `NextNumber` shows the identifier of the last part that exited the Store in the original sequence. Extended `attemptToRemoveNextPart`:

```
// control called by the methods ’placeInStock’ and ’removeFromStock’
var sequenceNo : integer
var part       : object
// check if the next part according to the original sequence
// is already located in ’MyStore’
if InventoryTable.getRowNo(#NextNumber)>0 
   part := InventoryTable[1,#NextNumber]
   sequenceNo := part.id
// code for displaying the value with the Variable
   if sequenceNo = NextNumber AND part.move(AttemptToRemoveNextPart)
      NextNumber := NextNumber + 1
      InventoryTable.cutRow(#part.id)
      print "Retrieved part number: ", part.id
   end
end
```

In the reset Method, delete the table contents and reset the Variable:

```
InventoryTable.delete({0,1}..{*,*})
NextNumber := 1
```

### Visualize the Occupancy of the Store Over Time
Use a **Chart** (Plotter):
- Data Source > **Input Channels**; clear the inheritance check box, click Input Channels, enter the Store name (`MyStore`) into row 1, and enter `MyStore.numMU` into cell 1 of column 1.
- Tab *Display*: Category > **Plotter**, Chart Type > **Line**.
- Right-click the Plotter, select **Show**, start the simulation, and watch the values develop over time.
