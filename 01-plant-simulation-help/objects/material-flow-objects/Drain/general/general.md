# Drain — General

This document summarizes the general help content for the **Drain** material flow object in Plant Simulation.

## Trigger [SimTalk]

Sets the internal Trigger list of the Source designated by `<Path>` or returns it.

- **Type:** Attribute
- **Syntax:** `<Path>.Trigger:array`
- **Assignment Value:** You can assign a value of data type `array`.

**Example**

```simtalk
var assignedTriggers: object[2]
for var j := 1 to 2
   assignedTriggers[j] := to_str("Trigger", j)
next
   Source.Trigger := assignedTriggers
// sets the trigger list
print MySource.Trigger // gets the trigger list
// [*.Models.Model.Trigger, *.Models.Model.Trigger2]
```

**See also:** Trigger [time of creation]

## Drain [object]

Use the **Drain** object to remove parts from the plant after they have been processed. It usually represents the shipping department of your plant.

- The built-in properties of the Drain are the same as those of the **Station**; like the Station, it has a single processing place.
- The only difference is that the Drain **removes the processed part from the plant** instead of moving it on to a succeeding object in the flow of materials.
- The Drain is basically the counterpart of the **Source**.

You can also show the statistics table of a Drain in an HtmlReport. To show a tooltip with information about the Drain, hover over it with the mouse. To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press `M`.

### Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > MaterialFlow > Drain** on the Home ribbon tab.

Sample models: **Window ribbon tab > Start Page > Getting Started > Example Models > Small Examples**.

## Dialog Box of the Drain

Double-click the icon of the Drain to open its dialog box.

- **Edit Simulation Properties:** change the simulation properties (shared properties are described under *Dialog Items of the Objects*).
- **Edit Animation Properties:** click **Edit 3D Properties** in the lower-left corner, or select the object and press the spacebar. To manipulate the graphic, click **Show Manipulators** on the Edit ribbon tab or press `M`.

### Tab Times

Define times as described under *Tab Times*. Select a distribution from the drop-down list and type the required values into the text box; parameters are shown along the upper border of the tab. You can also select a constant time (**Const**). Set the distribution type and parameters with the method `setTypeAndAttr [SimTalk]`.

**See also:** Define Processing Times, Select the Set-Up Time, Processing Time, Set-up Time, Recovery Time, Cycle Time.

### Tab Set-Up

Define properties for setting the object up as described under *Tab Set-Up*.

### Tab Failures

Define failures as described under *Tab Failures*.

### Tab Controls

Provides controls to modify the built-in behavior of the object.

**Select the Path to an Existing Method:** click the ellipsis button and navigate in *Select Object [for controls]*. Press `F2` in the text box to open the Method, or drag a Method from a Frame into the text box.

**Create a Control That Is a Method of the Object:**

- Type a meaningful name into the text box and select **Create Control** — Plant Simulation inserts `self.Name_you_typed_in_for_the_control` (e.g. `self.A1Ctrl`).
- Select **Create Control** on an empty text box — Plant Simulation inserts `self.OnBuilt_in_name_of_the_control` (e.g. `self.OnEntrance`).

To edit the source code later: press `F2`, hold `Shift` and double-click the text box, select **Open Object** on the context menu, or use the **User-defined** tab. To delete the control, delete the user-defined attribute (deleting only the name from the text box retains the attribute).

**See also:** Select Object [for controls], Entrance Control, Set-up Control, Pull Control, Shift Calendar.

### Tab Statistics [Drain]

Statistics are described under *Tab Statistics*. In addition to the data in the *Statistics Report*, the Drain collects and shows statistical data of the mobile objects.

- You can also collect statistics for MUs with the same name (see *Tab Type Statistics*).
- Each time the Drain removes a part, it computes the proportional average value of each displayed statistical value by dividing the average value by the average lifetime times 100.
- View cumulated statistics via **View > Show Statistics Report**, right-click the Frame > **Show Statistics Report**, or press `F6`.

**See also:** Tab Statistics [material flow objects], Tab Type Statistics, Statistics Report, Product Statistics of the MUs, Resource Statistics, Resource Type.

## Tab Type Statistics

Shows statistics for MUs with the same name that pass through the simulation model.

- The tab provides the **Type Dependent Statistics** check box; activate it to collect type-based statistics.
- Click **Detailed Statistics Table** to open a table itemizing the MUs removed from the plant by type.

The tab shows this statistical data:

| Item | Description | Read-only Attribute |
|------|-------------|---------------------|
| Working | Percentage of time MUs were located on a working object, relative to the statistics collection periods of all MUs. | `StatProdWorkingPortion`, `StatStoreWorkingPortion`, `StatTranspWorkingPortion` |
| Setting-up | Percentage of time objects were setting up for the MUs. | `StatProdSetupPortion`, `StatStoreSetUpPortion`, `StatTranspSetupPortion` |
| Waiting | Percentage of time objects were waiting for the MUs. | `StatProdWaitingPortion`, `StatStoreWaitingPortion`, `StatTranspWaitingPortion` |
| Stopped | Percentage of time MUs were located on a stopped object. | `StatProdStoppedPortion`, `StatStoreStoppedPortion`, `StatTranspStoppedPortion` |
| Failed | Percentage of time MUs were located on a failed object. | `StatProdFailPortion`, `StatStoreFailPortion`, `StatTranspFailPortion` |
| Paused | Percentage of time MUs were located on a paused or unplanned object. | `StatProdPausingPortion`, `StatStorePausingPortion`, `StatTranspPausingPortion` |
| Average lifespan | Average life-span of MUs created and removed during the collection period (only MUs with activated product statistics are counted). | `StatAvgLifeSpan` |
| Average exit interval | Average time interval between exits of removed MUs; counting starts from the first part arrival. | `StatAvgExitInterval` |
| Total throughput | Number of MUs removed starting when Type dependent statistics was activated. | `StatDeleted` |
| Throughput per minute | Number of MUs removed per minute over all observed available times. | `StatThroughputPerMinute` |
| Throughput per hour | Number of MUs removed per hour over all observed available times. | `StatThroughputPerHour` |
| Throughput per day | Number of MUs removed per day (throughput per hour × 24). | `StatThroughputPerHour` |

**Note:** The sum of the percentages for working, setting-up, failed, stopped, and paused adds up to 100 percent. To view part types in the Statistics Report, select the object and press `F6`, click **Show Statistics Report** on the Home ribbon tab, or right-click the object and select **Show Statistics Report**.

**Video:** https://youtu.be/BvHLQCIjGIA?si=sryvv1gjwWw1LOUF&t=57

### Type Dependent Statistics

Activate statistics collection depending on the MU type removed from the plant.

- **SimTalk:** `TypeStatOn [SimTalk]`
- **See also:** `StatThroughputPerDay`, `StatThroughputPerHour`, `StatAvgExitInterval`, `typeStatisticsCumulated`.

### Detailed Statistics Table [Drain]

The Detailed Statistics Table itemizes the MUs removed from the plant by type. It shows these values:

| Item | Description | Read-only Attribute |
|------|-------------|---------------------|
| Type | Name of the MU. | — |
| Time | Last arrival of a part of this type. | — |
| Total throughput | Number of parts of this type. | `StatThroughputPerDay`, `StatThroughputPerHour` |
| %Parts | Percentage of parts of this type. | — |
| LT_Mean | Mean life time (throughput time) of all investigated parts. | — |
| LT_StdDev | Standard deviation of the life times. | — |
| LT_Min | Minimum life time. | — |
| LT_Max | Maximum life time. | — |
| TPh_Mean | Number of MUs removed per hour over observed available times. | — |
| TPh_StdDev | Standard deviation of throughput per hour. | — |
| TPh_Min | Minimum throughput per hour. | — |
| TPh_Max | Maximum throughput per hour. | — |
| TPd_Mean | Number of MUs removed per day (throughput per hour × 24). | — |
| TPd_StdDev | Standard deviation of throughput per day. | — |
| TPd_Min | Minimum throughput per day. | — |
| TPd_Max | Maximum throughput per day. | — |
| CT_Mean | Mean cycle time of two parts arriving back-to-back. | — |
| CT_StdDev | Standard deviation of the cycle time difference. | — |
| CT_Min | Minimum cycle time difference of two parts arriving back-to-back. | — |
| CTS_Max | Maximum cycle time difference of two parts arriving back-to-back. | — |
| IP_Mean | Mean processing time of the investigated parts. | — |
| IP_StdDev | Standard deviation of the processing times. | — |
| IP_Min | Minimum processing time. | — |
| IP_Max | Maximum processing time. | — |
| S_Mean | Mean set-up time. | — |
| S_StdDev | Standard deviation of the set-up times. | — |
| S_Min | Minimum set-up time. | — |
| S_Max | Maximum set-up time. | — |
| W_Mean | Mean waiting time. | — |
| W_StdDev | Standard deviation of the waiting times. | — |
| W_Min | Minimum waiting time. | — |
| W_Max | Maximum waiting time. | — |
| Stp_Mean | Mean time on a stopped resource. | `StatProdStoppedPortion` |
| Stp_StdDev | Standard deviation of times on a stopped resource. | — |
| Stp_Min | Minimum time on a stopped resource. | — |
| Stp_Max | Maximum time on a stopped resource. | — |
| F_Mean | Mean time on a failed resource. | — |
| F_StdDev | Standard deviation of times on a failed resource. | — |
| F_Min | Minimum time on a failed resource. | — |
| F_Max | Maximum time on a failed resource. | — |
| P_Mean | Mean time on a paused resource. | — |
| P_StdDev | Standard deviation of times on a paused resource. | — |
| P_Min | Minimum time on a paused resource. | — |
| P_Max | Maximum time on a paused resource. | — |

**Production-resource rows (`_P_`):**

| Item | Description | Read-only Attribute |
|------|-------------|---------------------|
| IP_P_Mean | Mean processing time on a Production resource. | `StatProdWorkingPortion` |
| IP_P_StdDev | Standard deviation of processing times on Production. | — |
| IP_P_Min | Minimum processing time on Production. | — |
| IP_P_Max | Maximum processing time on Production. | — |
| S_P_Mean | Mean set-up time on Production. | `StatProdSetupPortion` |
| S_P_StdDev | Standard deviation of set-up times on Production. | — |
| S_P_Min | Minimum set-up time on Production. | — |
| S_P_Max | Maximum set-up time on Production. | — |
| W_P_Mean | Mean waiting time on Production. | `StatProdWaitingPortion` |
| W_P_StdDev | Standard deviation of waiting times on Production. | — |
| W_P_Min | Minimum waiting time on Production. | — |
| W_P_Max | Maximum waiting time on Production. | — |
| Stp_P_Mean | Mean time on a stopped Production resource. | `StatProdStoppedPortion` |
| Stp_P_StdDev | Standard deviation of times on stopped Production. | — |
| Stp_P_Min | Minimum time on stopped Production. | — |
| Stp_P_Max | Maximum time on stopped Production. | — |
| F_P_Mean | Mean time on a failed Production resource. | `StatProdFailPortion` |
| F_P_StdDev | Standard deviation of times on failed Production. | — |
| F_P_Min | Minimum time on failed Production. | — |
| F_P_Max | Maximum time on failed Production. | — |
| P_P_Mean | Mean time on a paused Production resource. | `StatProdPausingPortion` |
| P_P_StdDev | Standard deviation of times on paused Production. | — |
| P_P_Min | Minimum time on paused Production. | — |
| P_P_Max | Maximum time on paused Production. | — |

**Transport-resource rows (`_T_`):**

| Item | Description | Read-only Attribute |
|------|-------------|---------------------|
| IP_T_Mean | Mean processing time on a Transport resource. | `StatTranspWorkingPortion` |
| IP_T_StdDev | Standard deviation of processing times on Transport. | — |
| IP_T_Min | Minimum processing time on Transport. | — |
| IP_T_Max | Maximum processing time on Transport. | — |
| S_T_Mean | Mean set-up time on Transport. | `StatTranspSetupPortion` |
| S_T_StdDev | Standard deviation of set-up times on Transport. | — |
| S_T_Min | Minimum set-up time on Transport. | — |
| S_T_Max | Maximum set-up time on Transport. | — |
| W_T_Mean | Mean waiting time on Transport. | `StatTranspWaitingPortion` |
| W_T_StdDev | Standard deviation of waiting times on Transport. | — |
| W_T_Min | Minimum waiting time on Transport. | — |
| W_T_Max | Maximum waiting time on Transport. | — |
| Stp_T_Mean | Mean time on a stopped Transport resource. | `StatTranspStoppedPortion` |
| Stp_T_StdDev | Standard deviation of times on stopped Transport. | — |
| StpF_T_Min | Minimum time on stopped Transport. | — |
| Stp_T_Max | Maximum time on stopped Transport. | — |
| F_T_Mean | Mean time on a failed Transport resource. | `StatTranspFailPortion` |
| F_T_StdDev | Standard deviation of times on failed Transport. | — |
| F_T_Min | Minimum time on failed Transport. | — |
| F_T_Max | Maximum time on failed Transport. | — |
| P_T_Mean | Mean time on a paused Transport resource. | `StatTranspPausingPortion` |
| P_T_StdDev | Standard deviation of times on paused Transport. | — |
| P_T_Min | Minimum time on paused Transport. | — |
| P_T_Max | Maximum time on paused Transport. | — |

**Storage-resource rows (`_S_`):**

| Item | Description | Read-only Attribute |
|------|-------------|---------------------|
| IP_S_Mean | Mean processing time on a Storage resource. | `StatStoreWorkingPortion` |
| IP_S_StdDev | Standard deviation of processing times on Storage. | — |
| IP_S_Min | Minimum processing time on Storage. | — |
| IP_S_Max | Maximum processing time on Storage. | — |
| S_S_Mean | Mean set-up time on Storage. | `StatStoreSetUpPortion` |
| S_S_StdDev | Standard deviation of set-up times on Storage. | — |
| S_S_Min | Minimum set-up time on Storage. | — |
| S_S_Max | Maximum set-up time on Storage. | — |
| W_S_Mean | Mean waiting time on Storage. | `StatStoreWaitingPortion` |
| W_S_StdDev | Standard deviation of waiting times on Storage. | — |
| W_S_Min | Minimum waiting time on Storage. | — |
| W_S_Max | Maximum waiting time on Storage. | — |
| Stp_S_Mean | Mean time on a stopped Storage resource. | `StatStoreStoppedPortion` |
| Stp_S_StdDev | Standard deviation of times on stopped Storage. | — |
| Stp_S_Min | Minimum time on stopped Storage. | — |
| Stp_S_Max | Maximum time on stopped Storage. | — |
| F_S_Mean | Mean time on a failed Storage resource. | `StatStoreFailPortion` |
| F_S_StdDev | Standard deviation of times on failed Storage. | — |
| F_S_Min | Minimum time on failed Storage. | — |
| F_S_Max | Maximum time on failed Storage. | — |
| P_S_Mean | Mean time on a paused Storage resource. | `StatStorePausingPortion` |
| P_S_StdDev | Standard deviation of times on paused Storage. | — |
| P_S_Min | Minimum time on paused Storage. | — |
| P_S_Max | Maximum time on paused Storage. | — |

**SimTalk:** `typeStatistics [SimTalk] - Drain`, `typeStatisticsCumulated [SimTalk]`

**Video:** https://youtu.be/BvHLQCIjGIA?si=RrcV9zshpXbrOs0I&t=508

## Tab Importer [Drain]

Define services for processing parts, setting the station up for a certain type of part, and repairing the station. This also enables the Worker to carry parts to the Drain.

To view Importer Statistics in the Statistics Report, select the object and press `F6`, or click **Show Statistics Report** on the Home ribbon tab.

**See also:** Tab Importer [general description], Processing Importer, Set-up Importer, Failure Importer.

## Tab User-defined

Define your own attributes as described under *Tab User-defined*.

## Navigate Menu

The commands are described under *Navigate Menu*.

## View Menu

The View Menu provides commands to access its functions:

- Refresh Services
- Show Statistics Report
- Unavailable Services
- Show Attributes and Methods
- Associated Workplaces
- Contents
- Exiting MUs
- Forward Blocking List
- Associated Lockout Zones
- Exporters
- Associated Shift Calendar

## Tools Menu

The commands are described under *Tools Menu*.

## Tabs Menu

Use the commands of the Tabs menu to show or hide individual tabs of the selected material flow objects. Hiding unused tabs makes the dialog open faster and lets you switch faster to the tabs you need.

- Apply changed settings by clicking **OK**, closing the dialog, and reopening it.
- The menu shows a check mark to the left of the displayed tabs.
- **Inherit** turns inheritance of the displayed/hidden tabs in the dialog off or on.

## Help Menu

The commands are described under *Help Menu*.

## Methods of the Drain

The Drain provides:

- The methods listed in the table of contents to the left.
- The methods of the Station.
- The methods of the Material Flow Objects.
- The methods of All Objects.

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (select it on the context menu of the Class Library).
