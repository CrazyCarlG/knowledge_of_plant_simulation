# TwoLaneTrack — General

## Description

The TwoLaneTrack, together with the Transporter, can model an AGV (automated guided vehicle) system.

- The distance a Transporter travels on the TwoLaneTrack is defined by the **Length of Lane A** and the **Length of Lane B**, the Transporter's **MU Length**, and its **Speed**. These determine the time the Transporter remains on the track.
- Unlike point-oriented material flow objects, Plant Simulation uses the actual typed-in length during the simulation run.
- A Transporter may not pass another one moving in front of it. Transporters retain their order of moving onto and leaving the TwoLaneTrack.
- Each lane may have its own length, so when the track turns a corner, the outside lane can be longer than the inside lane.
- If several Transporters travel at different speeds, the faster one collides with the slower one. Plant Simulation activates the **Collision Control** of the faster Transporter and automatically reduces its speed to that of the slower Transporter.
- A Transporter can drive **forward** and **backwards** on the TwoLaneTrack (it drives onto the exit and exits at the entrance). Forward/backward driving are properties of the Transporters, not of the track.
- The maximum capacity is defined by the track length and the lengths of the Transporters on it (e.g., a three-yard track accepts three one-yard Transporters at most). The **Capacity** setting can further restrict the number of Transporters.
- The TwoLaneTrack can be inserted as a **curved object** (default) or as any sequence of curved and straight segments.
- The track supports **bidirectional traffic**: select **Right-hand Traffic** or **Left-hand Traffic**.

## Show Manipulators

To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.

- The manipulator at the start and end of a length-oriented object is cut off. Attaching two objects of the same type combines the two halves into a complete manipulator.

## Add the Object to the Simulation Model

Click **Library > Basic Objects > MaterialFlow > TwoLaneTrack** on the Home ribbon tab.

## Routing

To facilitate a branching TwoLaneTrack, use any of these controls to move a Transporter to the succeeding object. Plant Simulation uses (in priority order):

1. The **Exit Control** of the TwoLaneTrack (highest priority).
2. **Automatic Routing** of the Transporter.
3. The **Driving Control** of the Transporter.
4. The built-in properties of the TwoLaneTrack.

Details:

- If no Exit Control is defined and a destination list is typed for the Transporter, Automatic Routing moves the Transporter to the proper successor using the destination list of the successors.
- You can assign a **Destination** to the Transporter. The track has a **Forward destination list** and **Backward destination list** for each lane. If a destination list is assigned, the track searches the Forward and Backward destination lists of all successors for the Destination and moves the Transporter to the first successor where it is found. If not found, the Transporter moves to the next successor in turn. Search terminates after the first instance of the Destination.
- Automatic routing is inactive if no Destination is typed or if an Exit Control is defined.
- If neither Exit Control nor Destination Lists exist for the successors, the track uses the **Driving Control** of the Transporter.
- If no controls are defined at all, the track moves Transporters to each connected successor in turn.

## Dialog Box

Double-click the icon to open the dialog box.

- **Edit Simulation Properties**: change simulation properties in the dialog box (shared properties described under *Dialog Items of the Objects*).
- **Edit Animation Properties**: click **Edit 3D Properties** in the lower-left corner, or select the object and press the spacebar.

## Tab Attributes

### Lane A

Lane A provides settings for **Length**, **Entrance Locked**, and **Exit Locked**.

#### Length [text box] — lane A

Type the length of Lane A. After insertion, Plant Simulation shows the length here. The lane lengths plus the sum of all Transporter lengths determine how many Transporters the track can accommodate.

SimTalk:

```simtalk
A.Length [SimTalk] - lane A or B
A.OccupiedLength [SimTalk] - lane A or B
```

#### Entrance Locked [lane A]

Prevents Transporters from entering Lane A. The track finishes transporting Transporters already on it and does not accept additional ones; those are entered into the Blocking List of Lane A.

- Transporter entering at the entrance → **Forward Blocking List** of Lane A.
- Transporter moving backward and entering at the exit → **Exit Blocking List** of Lane A.

Transporting resumes when the check box is cleared; the first Transporter in the Forward Blocking List moves on first.

SimTalk:

```simtalk
A.EntranceLocked [SimTalk] - lane A or B
```

#### Exit Locked [lane A]

Prevents Transporters from exiting Lane A. Transporters are entered into the **Exit Blocking List** of Lane A instead of being transported to the successor. When unlocked, the first Transporter in the Exit Blocking List moves on.

> **Note:** The Transporter does not trigger the Exit Control if **Exit Locked** is selected.

SimTalk:

```simtalk
A.ExitLocked [SimTalk] - lane A or B
```

### Lane B

Lane B provides settings for **Length**, **Entrance Locked**, and **Exit Locked**.

#### Length [text box] — lane B

Type the length of Lane B. Same behavior as Lane A.

SimTalk:

```simtalk
B.Length [SimTalk] - lane A or B
B.OccupiedLength [SimTalk] - lane A or B
```

#### Entrance Locked [lane B]

Prevents Transporters from entering Lane B. Blocked Transporters are entered into the Blocking List of Lane B.

- Entering at the entrance → **Forward Blocking List** of Lane B.
- Moving backward and entering at the exit → **Exit Blocking List** of Lane B.

SimTalk:

```simtalk
B.EntranceLocked [SimTalk] - lane A or B
```

#### Exit locked [lane B]

Prevents Transporters from exiting Lane B; they are entered into the **Exit Blocking List** of Lane B.

> **Note:** The Transporter does not trigger the Exit Control if **Exit locked** is selected.

SimTalk:

```simtalk
B.ExitLocked [SimTalk] - lane A or B
```

### Width [text box]

Type the width of both lanes of the TwoLaneTrack.

SimTalk:

```simtalk
Width [SimTalk] - TwoLaneTrack
```

### Track Pitch [text box]

Type the Track Pitch between Lane A and Lane B. The Track Pitch is the distance between the center lines of the two lanes.

SimTalk:

```simtalk
TrackPitch [SimTalk]
```

### Right-hand Traffic / Left-hand Traffic

Select the side on which traffic moves: **Right-hand Traffic** or **Left-hand Traffic**.

SimTalk:

```simtalk
Traffic [SimTalk] - TwoLaneTrack
```

### Capacity [text box]

The maximum number of Transporters that may be located on both lanes (wholly or in part) at any one time. The default value `-1` stands for infinite capacity.

SimTalk:

```simtalk
Capacity [SimTalk] - TwoLaneTrack
```

### Destination List A [text box]

Click the ellipsis button and select a List object. Type all destination objects reachable when the Transporter drives forward on Lane A. The forward destination list of Lane A is concurrently the backward destination list of Lane B.

Plant Simulation searches for the destination in the destination lists of all succeeding TwoLaneTracks directly connected with Connectors. If a succeeding track is connected via an Interface, the Interface should have only a single successor (only the first successor of the Interface is searched).

SimTalk:

```simtalk
DestListA [SimTalk] - TwoLaneTrack
```

### Destination List B [text box]

Click the ellipsis button and select a List object. Type all destination objects reachable when the Transporter drives forward on Lane B. The forward destination list of Lane B is concurrently the backward destination list of Lane A.

SimTalk:

```simtalk
DestListB [SimTalk] - TwoLaneTrack
```

## Tab Failures

Define failures as described under the Tab Failures.

## Tab Controls A/B

Provides controls to modify the built-in behavior of the object.

### Select the Path to an Existing Method

Click the ellipsis button, navigate to the Method, and click OK. Press **F2** in the text box to open the Method and type the source code. Alternatively, drag a Method from a Frame into the text box.

### Create a Control That is a Method of the Object

- Type a meaningful name and select **Create Control** (context menu) — inserts `self.Name_you_typed_in_for_the_control`, e.g. `self.A1Ctrl`.
- Select **Create Control** on an empty text box — inserts `self.OnBuilt_in_name_of_the_control`, e.g. `self.OnEntrance`.

Edit the source code later via **F2**, **Shift + double-click**, **Open Object** on the context menu, or the **User-defined** tab.

To delete the control, delete the user-defined attribute (deleting only the name from the text box retains the attribute).

You can create an **Entrance Control**, **Exit Control**, **Backward Entrance Control**, **Backward Exit Control**, and **Pull Control** for Lane A and/or Lane B. Additionally you can select the **Shift Calendar**, and create/insert **Sensors** on each lane separately or on both lanes.

## Tab Statistics

Statistics are described under the Tab Statistics. To view Resource Statistics of Stationary Resources, select **View > Show Statistics Report**, right-click in the Frame and select **Show Statistics Report**, or press **F6**.

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

## Navigate Menu

Commands are described under the Navigate Menu.

## View Menu

Provides commands to access functions for each of the two lanes:

- Refresh
- Show Statistics Report
- Show Attributes and Methods
- Contents (material flow objects)
- Associated Shift Calendar
- Forward Blocking List
- Backward Blocking List
- Exit Blocking List
- Associated Lockout Zones

## Tools Menu

Commands are described under the Tools Menu.

## Tabs Menu

Show or hide individual tabs of the selected material flow objects. Apply changes by clicking OK, closing, and reopening the dialog. The **Inherit** command turns inheritance of displayed/hidden tabs off or on.

## Help Menu

Commands are described under the Help Menu.

## Methods of the TwoLaneTrack

The TwoLaneTrack provides:

- The methods listed in the table of contents.
- The Methods of Curved Objects.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

> **Note:** A number of methods shared with other material flow objects apply to a **lane** instead of the entire object. To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods**.

## See also

- Model a Transport System with Passive Objects
- Work with Length-oriented Objects
- Routing [TwoLaneTrack]
- Dialog Box of the TwoLaneTrack
- asAny [SimTalk]
- IsLaneA [SimTalk]
- IsLaneB [SimTalk]
- Define Controls for Length-Oriented Objects
- Select Object [for controls]
- Entrance Control / Exit Control / Backward Entrance Control / Backward Exit Control / Pull Control
- Shift Calendar [tab Controls]
- Resource Statistics [check box]
- Resource Type
- Forward Blocking List / Exit Blocking List
