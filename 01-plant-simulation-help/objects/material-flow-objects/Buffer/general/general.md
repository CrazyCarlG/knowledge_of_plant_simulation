# Buffer — General

> Source: `general.txtx` (Plant Simulation Help, © 2026 Siemens)

## Description

Insert a **Buffer** between two components of your plant to:

- **Temporarily hold parts** when one of the components following it in the sequence of stations fails, preventing the preceding machines from stopping production.
- **Move parts on** when the preceding components stop working, preventing the production process from grinding to a halt.

Dimensioning a Buffer with a large enough capacity to cover all failures leads to a complete decoupling of the respective components. The Buffer not only tides over failure times but also acts as a compensating station for fluctuating transport and operating times (which lead to queues forming in front of a machine). Even so, it cannot always prevent the material flow from being interrupted.

Because the Buffer has no individual places, it does not divide processing time (the time a part remains in it) into small individual steps. Instead, you select the sequence in which parts exit the Buffer.

## Buffer Type

`Buffer Type [drop-down list]`

- **Queue** — parts exit in the same order they entered (First In First Out).
- **Stack** — the part that entered last leaves first (Last In First Out).

> **Note:** Each MU remains in the Buffer for at least the **Dwell Time**. For `Stack`, an MU can only exit when all parts that entered after it have already exited — i.e., when the MU is at the very top of the stack.

Hover over the Buffer to show a tooltip with information about it.

## Tips

- To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.
- The Buffer is ideal for modeling a buffer with a great **Capacity** requiring high performance. For more advanced functions, use the **PlaceBuffer**.
- Alternative graphics are available via **Exchange Graphics** in the Buffer window.
- Plant Simulation shows the MUs in the Buffer stacked.

## Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > MaterialFlow > Buffer** on the Home ribbon tab.

## Dialog Box of the Buffer

Double-click the Buffer icon to open its dialog box.

- **Edit Simulation Properties** — shared properties are described under *Dialog Items of the Objects*.
- **Edit Animation Properties** (3D) — click **Edit 3D Properties** in the lower-left corner of the simulation properties dialog, or select the object and press the **spacebar**.

## Tab Attributes

### Capacity `[text box]`

The number of MUs the Buffer can hold at any one time.

- Type `-1` for infinite capacity.
- Capacity is **not** implemented in a matrix — you cannot access individual places.
- You can only reduce the Capacity if the new value is greater than or equal to the actual number of MUs currently in the Buffer.

### Buffer Type `[drop-down list]`

The exit behavior of MUs (see **Buffer Type** above).

## Tab Times

Define times as described under *Tab Times*. Select a distribution from the drop-down list and type the required values; Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (**Const**). Set the distribution type and a complete set of parameters with the method `setTypeAndAttr`.

### Dwell Time `[Buffer]`

The time for which MUs remain in the Buffer.

- For the Buffer you can only specify a **constant** Dwell Time.
- Statistics counts the Dwell Time as **waiting time**, not processing time.
- The Dwell Time is **not** prolonged by failures or pauses.
- Each MU remains at least the Dwell Time; for `Stack`, an MU can only exit when it is at the very top of the stack.

## Tab Failures

Define failures as described under *Tab Failures*.

## Tab Controls

Provides controls to modify the built-in behavior of the object.

- **Select an existing Method** — click the ellipsis button, navigate in *Select Object [for controls]*, and click OK; or drag a Method from a Frame into the text box.
- **Create a control that is a Method of the object** — type a meaningful name and select **Create Control** (inserts `self.Name_you_typed`, e.g. `self.A1Ctrl`), or select **Create Control** on an empty text box (inserts `self.OnBuilt_in_name`, e.g. `self.OnEntrance`). Type the source code into the Method that opens.
- **Edit later** — press F2, hold Shift + double-click, select **Open Object** on the context menu, or use the **User-defined** tab.
- **Delete** — delete the user-defined attribute. (Deleting only the name from the text box retains the attribute.)

See also: Entrance Control, Exit Control, Pull Control, Shift Calendar.

## Tab Exit

Select to which of its successors the object moves the MU. See *Blocking [exit strategy]* and *Strategy [material flow objects]*.

## Tab Statistics

Statistics is described under *Tab Statistics*. To view **Resource Statistics** of Stationary Resources in the Statistics Report, select **View > Show Statistics Report** in the object dialog, right-click in the Frame and select **Show Statistics Report**, or press **F6**.

## Tab Energy

Select energy settings for the object on the *Tab Energy*.

## Tab Costs

Select costs settings on the *Tab Costs*. While the Buffer buffers parts, costs accrue from the sum of **investment costs** and **operating costs**.

- Investment costs only accrue during the **Depreciation Period**.
- Costs are allocated to the part, proportional to capacity, as **accrued costs**.
- If the Buffer is empty, costs remain with the Buffer as general costs.

## Tab User-defined

Define your own attributes as described under *Tab User-defined*.

## Menus

- **Navigate Menu** — commands described under *Navigate Menu*.
- **View Menu** — provides access to: Refresh, Show Statistics Report, Show Attributes and Methods, Forward Blocking List, Exit Blocking List, Associated Lockout Zones, Associated Shift Calendar, Contents.
- **Tools Menu** — commands described under *Tools Menu*.
- **Tabs Menu** — show/hide individual tabs of selected material flow objects. Hiding unused tabs makes the dialog open faster. Click OK, close, and reopen to apply changes. **Inherit** turns inheritance of displayed/hidden tabs on or off.
- **Help Menu** — commands described under *Help Menu*.

## Methods of the Buffer

The Buffer provides:

- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the Class Library context menu (selected Class), or
- Press **F8** / click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing the instance.

## See also

- Buffer Parts within the Production Line
- Use a Buffer between Processing Stations
- Properties of the DataQueue
- Properties of the DataStack
- Check the Fill Level of the Buffers in the Plant
- Simulate the Accrued Costs of the Machines
- CostAnalyzer > How the CostAnalyzer Assigns Costs to Part Types
- CostAnalyzer > Costs Shown in the Costs Report
- Resource Statistics, Resource Type

## SimTalk references

- `Capacity`
- `BufferType`
- `ProcTime` (material flow objects)
- `setTypeAndAttr`
- `putAttributeNamesIntoTable`

## Videos

- https://youtu.be/PgT4wkT2Xj8?si=Udlvoq8KcAI9GxQw&t=18
- https://youtu.be/PgT4wkT2Xj8?si=d4Sx9mjGHp_Pl0wB&t=98
