# PlaceBuffer

The object **PlaceBuffer** processes parts on a number of buffer places arranged in a row, one behind the other. It is not part of the built-in objects that the Toolbox provides by default.

## Description

The MUs processed by the PlaceBuffer advance from place to place and can only leave after passing the last place. This way each place can be called and accessed individually.

### Notes

- The PlaceBuffer is not shown in new models by default; you must add it yourself.
- **If Sequentially Indexing is cleared**, you can only set the Processing Time for the PlaceBuffer as a whole, not for individual places. The Processing Time is equally distributed across all places (e.g., a Processing Time of one minute with a Capacity of three places gives 20 seconds per place). A part can move directly to an idle place. After the part has passed this and all succeeding places, it can exit. If a part is created on an idle place, it does not have to pass this place but may move on to the next place or object.
- **If Sequentially Indexing is checked**, the Processing Time for moving the part on to the next place is used up. For a capacity of four, the threefold processing time passes at least before the part can leave (three move processes). The time can be extended through waiting times.

The PlaceBuffer moves the part cyclically on to its successors. If the first part cannot leave:
- Select **Accumulating** to make MUs move front to end to each other when the exit is Blocked.
- Clear **Accumulating** to make MUs retain their distance (all succeeding MUs stop when the preceding MU cannot exit).

### Graphics

The default graphic is a table of 2 × 1 × 1 m, on whose surface up to four parts move in the X-Direction. Scaling the PlaceBuffer (typically only in X) scales the pre-defined animation area, so you only need to adjust the Capacity.

Two graphics are offered:
- `Table2x1x1modular.jt` in the folder `jt-graphics` (can be imported into any object).
- `PlacebufferModular.s3d` in the folder `s3d-graphics\BuffersAndSorters` (allows adapting table size by changing individually transformable graphics parts without changing element thickness).

You can also set the **Animation Area**. Note:
1. If the Animation Area is active, the PlaceBuffer uses it; the index of the MU is the index of the area in the X-Direction. Capacity in Y-Direction is always 1.
2. If an MU animation path named `Default` with more than one anchor point exists, the MU index is converted into a relative position; MUs are equally distributed on the line.
3. Otherwise the PlaceBuffer uses the first path for the first MU, the second for the second, etc. If no suitable path exists but a `Default` path with a single point exists, that path is used.

For a large-capacity buffer that has to be fast, use the object **Buffer** instead.

To show a tooltip, hover over the PlaceBuffer. To change the graphic length and anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.

### Adding the Object to the Model

Click **Manage Class Library > Basic Objects > MaterialFlow > PlaceBuffer** on the Home ribbon tab.

## Dialog Box

Double-click the PlaceBuffer icon to open its dialog box.

- **Edit Simulation Properties**: change simulation properties in the dialog box (shared properties described under "Dialog Items of the Objects").
- **Edit Animation Properties**: click **Edit 3D Properties** in the lower left corner of the simulation properties dialog, or select the object and press the **spacebar**. To manipulate the graphic, click **Show Manipulators** or press **M**.

## Tab Attributes

### Capacity [text box]

Type the Capacity, i.e., the number of places of the PlaceBuffer.

Remarks:
- Type `-1` for an unlimited number of places if Sequentially Indexing is active.
- Individual places are accessed by their index.
- Capacity can only be reduced if enough places are empty, and only changed if no parts are located in the PlaceBuffer (i.e., it is empty).

### Sequentially Indexing [check box]

Select to only start the Processing Time on a place when the succeeding place is free.

Remarks:
- In this mode, Processing Time represents the time used for moving the part to the succeeding place (not processing on a place). With capacity four, Processing Time passes three times before the part can leave.
- No time is used on the last place; the part can exit immediately once it reaches the last place, provided the successor accepts it.
- If cleared, the default behavior applies; Processing Time is set only for the whole PlaceBuffer and distributed equally across places.

### Accumulating [check box]

Select to make MUs accumulate on the PlaceBuffer, moving front to end to each other when the exit is Blocked. Clear it to make MUs retain their distance (all succeeding MUs stop when the preceding part cannot exit, and no additional MU can enter).

## Tab Times

Define times as described under the Tab Times. Select a distribution from the drop-down list and type the required values. A constant time (Const) can also be selected.

> Note: You can only type in a constant Processing Time for parts in the PlaceBuffer — no statistical distributions, no part-type dependencies, and no formulas. The distribution type and a complete set of parameters can be set with the method `setTypeAndAttr`.

### Processing Time [PlaceBuffer]

Type in the Processing Time of MUs in the PlaceBuffer.

Remarks:
- Only a constant Processing Time can be specified (no probability distribution, no MU-type dependency, no formula).
- It is more of a Dwelling Time than a Processing Time, as parts are buffered then moved on.
- If Sequentially Indexing is cleared: time is set for the whole buffer and equally distributed (e.g., 1 minute / 3 places = 20 seconds per place).
- If Sequentially Indexing is selected: time is used for moving to the next place; with capacity four the threefold time passes at least before leaving, extendable through waiting times.

### Recovery Time / Cycle Time [PlaceBuffer]

Described under the Tab Times.

## Tab Failures

Define failures as described under the Tab Failures.

## Tab Controls

Provides controls to modify the built-in behavior of the object.

- **Select the Path to an Existing Method**: click the ellipsis button and navigate in the "Select Object" dialog; or drag a Method from a Frame into the text box.
- **Create a Control That is a Method of the Object**: type a meaningful name and select **Create Control** (inserts `self.Name_you_typed`, e.g., `self.A1Ctrl`), or select **Create Control** on an empty text box (inserts `self.OnBuilt_in_name`, e.g., `self.OnEntrance`). Press **F2** to open the Method and type source code.
- **Edit later**: press F2, hold Shift and double-click the text box, select **Open Object** on the context menu, or double-click the Method in the User-defined tab.
- **Delete**: delete the user-defined attribute (deleting only the name from the text box retains the attribute).

See also: Entrance Control, Exit Control, Pull Control, Shift Calendar.

## Tab Exit

Select to which successor the object moves the MU. See Blocking and Strategy.

## Tab Statistics

Described under the Tab Statistics. To view Resource Statistics of Stationary Resources, select **View > Show Statistics Report** in the object dialog, right-click in the Frame and select **Show Statistics Report**, or press **F6**.

## Tab Energy

Select energy settings for the object.

## Tab Costs

Select costs settings. While the PlaceBuffer buffers parts, costs accrue from the sum of investment costs and operating costs.

Note:
- Investment costs only accrue during the Depreciation Period.
- Costs are allocated to the part, proportional to capacity, as accrued costs.
- If the PlaceBuffer is empty, the costs remain with the PlaceBuffer as general costs.

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

## Menus

- **Navigate Menu**: described under the Navigate Menu.
- **View Menu**: provides Refresh, Show Statistics Report, Show Attributes and Methods, Contents, plus Forward/Exit Blocking List, Associated Lockout Zones, Associated Shift Calendar.
- **Tools Menu**: described under the Tools Menu.
- **Tabs Menu**: show/hide individual tabs of the selected material flow objects (hiding unneeded tabs opens the dialog faster). Apply changes by clicking OK, closing, and reopening. The menu shows a check mark next to displayed tabs; **Inherit** turns inheritance of displayed/hidden tabs off or on.
- **Help Menu**: described under the Help Menu.

## Methods of the PlaceBuffer

The PlaceBuffer provides:
- The method `pe, [X Y]`.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (context menu of the Class Library for a Class, or **F8** / Home ribbon tab for an instance).

## SimTalk / Code Examples

```simtalk
print place.MU(i)
next
// Returns the topmost MU of the stack:
Store[1,1].Cont
// Returns the second MU from the top on the place 1,2:
Store[1,2].MU(2)
```

Related SimTalk items:

- `XDim [SimTalk] - Store`
- `YDim [SimTalk] - Store`
- `getStackHeight [SimTalk] - Store`
- `mu [SimTalk] - PE, Store`
- `Capacity [SimTalk] - PlaceBuffer`
- `SequentiallyIndexing [SimTalk]`
- `Accumulating [SimTalk] - PlaceBuffer`
- `setTypeAndAttr [SimTalk]`
- `ProcTime [SimTalk] - material flow objects`
- `RecoveryTime [SimTalk] - material flow objects`
- `CycleTime [SimTalk]`

## See also

- Z-Dimension [Store]
- Stack Parts in the Store
- Unload Stacked Parts
- Processing Time [PlaceBuffer]
- Capacity [text box] - PlaceBuffer
- Sequentially Indexing [check box]
- Recovery Time [general description]
- Recovery Time Starts
- Cycle Time [general description]
- Resource Statistics [check box]
- Resource Type
- Simulate the Accrued Costs of the Machines
- CostAnalyzer > How the CostAnalyzer Assigns Costs to Part Types
- CostAnalyzer > Costs Shown in the Costs Report
