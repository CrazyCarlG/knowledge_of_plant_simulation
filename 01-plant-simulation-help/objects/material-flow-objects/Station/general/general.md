# Station [object]

Use the object **Station** for processing parts on a single processing place. It is used for modeling most machines.

## Description

The Station receives a single MU from its predecessor, processes it, and moves it on to one of its successors after the set-up time and processing time have elapsed. If the types of MUs are not identical (i.e., they do not have the same name), the Station has to set up to process the new type of MU. While a part is located on the Station, it does not receive additional parts but enters them into its Blocking List. It only accepts the blocked MUs one after the other and processes them after it is available again.

If the Station has several successors, it moves the MUs one after the other onto them. If the successor to which the part is to be moved is blocked (full or failed), the Station does not select another available successor. Instead, it does not move the part and thus is blocked. It only moves the part after the successor becomes available again. A different moving behavior can be set with a Method.

> **Note:** Plant Simulation always moves the MU as a whole, not continually — as soon as its booking point is located on the Station, the entire MU is located on it.

To show a tooltip with information about the Station, hover with the mouse over it. To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > MaterialFlow > Station** on the Home ribbon tab.

Sample models: Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples.

## Dialog Box of the Station

Double-click the Station icon to open its dialog box. The shared simulation properties are described under *Dialog Items of the Objects*.

### Edit 3D Properties
- Click **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Or select the object in the model and press the spacebar.

Video: https://youtu.be/PQhEriOzVzU?si=HpfLhwtUyoiMFPzx&t=22

### Tab Times
Define times (set-up time, processing time, recovery time, cycle time, etc.). Select a distribution from the drop-down list and type the required values. Parameters are shown along the upper border of the tab. A constant time (`Const`) can also be selected. The distribution type and parameter set can be set with `setTypeAndAttr [SimTalk]`.

### Tab Set-Up
Define properties for setting the object up.

### Tab Failures
Define failures.

### Tab Controls
Provides controls to modify the built-in behavior of the object. Select the path to an existing Method (ellipsis button, or drag and drop a Method onto the text box). Press `F2` in the text box to open the Method. Create a control as a user-defined attribute of data type Method via **Create Control** (inserts `self.<Name>` such as `self.A1Ctrl`, or `self.On<built-in-name>` such as `self.OnEntrance`). To delete a control, delete the user-defined attribute (deleting only the name keeps the attribute).

### Tab Exit
Select to which successor the object moves the MU. See *Blocking [exit strategy]* and *Strategy [material flow objects]*.

### Tab Statistics
Described under *Tab Statistics*. To view Resource Statistics of Stationary Resources, select **View > Show Statistics Report**, right-click in the Frame and select **Show Statistics Report**, or press `F6`.

### Tab Importer
Define services for processing parts, setting up the station for a certain part type, and repairing the station. To view Importer Statistics, press `F6` or click **Show Statistics Report**.

### Tab Energy
Select energy settings.

### Tab Costs
Select cost settings. While the Station processes a part, costs accrue from the sum of investment costs and operating costs.
- Investment costs only accrue during the Depreciation Period.
- Costs are allocated to the part as accrued costs.
- If the Station is empty, costs remain with the Station as general costs.

### Tab User-defined
Define own attributes.

## Menus

- **Navigate Menu** — commands described under *Navigate Menu*.
- **View Menu** — provides commands to access functions (Refresh Exporters, Show Statistics Report, Show Attributes and Methods, Contents, Forward Blocking List, Exit Blocking List, Services, Associated Workplaces, Associated Lockout Zones, Associated Shift Calendar).
- **Exporters [Station]** — opens a table showing all Exporters currently exporting services. See `getExporters [SimTalk]`.
- **Services [Station]** — opens a table of all imported services. The failure service name is identical to the subtable name. Columns: Name of the Exporter, Amount of services provided. See `getImportedServices`, `getServices`, `setAlternativeServices`, `setServices`.
- **Unavailable Services [Station]** — shows the Failure, Set-up, Processing, and Transport services that are currently unavailable (name shown white on red). Columns: Name of the Exporter, Amount defined, Amount missing, Name of the Alternative.
- **Associated Workplaces [Station]** — lists all Workplaces assigned to the Station. See `assignedWorkplaces [SimTalk]`.
- **Tools Menu** — commands described under *Tools Menu*.
- **Tabs Menu** — show/hide individual tabs of selected material flow objects. The `Inherit` command toggles inheritance of displayed/hidden tabs.
- **Help Menu** — commands described under *Help Menu*.

## Methods of the Station

The Station provides:
- The Methods of All Objects.
- The Methods of the Material Flow Objects.

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (`F8` on an instance, or the context menu of the Class Library).

## Code Example (TypeStatOn [SimTalk])

Activates collecting statistics values of the Drain designated by `<Path>` depending on the type of MU (`true`) or deactivates it (`false`).

```
Type:     Attribute
Syntax:   <Path>.TypeStatOn:boolean
```

Assignment value: data type `boolean`.

```
MyDrain.TypeStatOn := false
```

**See also:** Type Dependent Statistics, `typeStatistics [SimTalk] - Drain`, `typeStatisticsCumulated [SimTalk]`
