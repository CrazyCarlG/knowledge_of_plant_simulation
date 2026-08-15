# Attributes of the Frame

The Frame provides:
- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

You can:
- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
Frame.StateBlocked := true
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print .Models.Model.BackgroundColor
posit := MyStation.Cont.XPos
```

---

## NumNodes [SimTalk] - Frame

Returns the number of objects in the Frame designated by `<Path>`.

**Remarks**

Each additional Frame you insert into the selected Frame counts as a single object. Plant Simulation does not count the objects contained within the Frames. Connectors also count as objects.

**Type**

Read-only attribute

**Syntax**

```
<Path>.NumNodes → integer
```

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print .Models.MyPlant.NumNodes
```

**See also**

- node [SimTalk] - Frame
- Attributes of the Frame

---

## Failed [SimTalk] - Frame

Fails the Frame designated by `<Path>` (true) or does not fail it (false).

**Type**

Attribute

**Syntax**

```
<Path>.Failed:boolean
```

**Watchable**

The attribute is watchable and Plant Simulation calls a control.

**Assignment Value**

You can assign a value of data type `boolean`.

**Note**

During the reset phase of the simulation Plant Simulation resets all failures.

**Example**

```simtalk
subFrame.failed := true
```

**See also**

- States of the Frame
- Failed [check box] - material flow objects

---

## LockStructure [SimTalk]

Locks the structure of the Frame designated by `<Path>` (true) or unlocks it (false).

**Remarks**

`LockStructure` is deactivated by default, meaning that the Frame is unlocked so that you can create your model in it.

When you activate **Lock Structure**, Plant Simulation prevents unintentional changes, i.e., inserting, deleting, and changing of objects. You can then neither change the position of objects nor their name.

Lock Structure is activated in instantiated Frames by default. This helps to prevent unintentional changes to the structure of an instance, although this change should apply to all instances and should thus be made in the class.

**Type**

Attribute

**Syntax**

```
<Path>.LockStructure:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

**Example**

```simtalk
.frame2.LockStructure := true
print .frame2.LockStructure
```

**See also**

- Lock Structure [Frame ribbon]

---

## Pause [SimTalk] - Frame

Pauses the Frame designated by `<Path>` (true) or does not pause it (false).

**Remarks**

Plant Simulation resets the pause when you reset the EventController.

**Type**

Attribute

**Syntax**

```
<Path>.Pause:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

**Example**

```simtalk
EngineAssembly.Pause := true
```

**See also**

- Pause Material Flow Objects and Frames
- Paused Frames
- States of the Frame

---

## ReplacementMode [SimTalk]

Sets the replacement mode for the Frame designated by `<Path>`.

**Remarks**

The replacement mode of the replacing Frame determines if the Frames are merged or replaced. The replacement mode of the replaced Frame does not have any consequences.

**Type**

Attribute

**Syntax**

```
<Path>.ReplacementMode:string
```

**Assignment Value**

You can assign a value of data type `string`.

You can specify `"exchange"` or `"merge"`.

**Example**

```simtalk
Frame1.ReplacementMode := "merge"
```

**SimTalk**

- loadObjectAs [SimTalk]
- replace [SimTalk]
- writeObject [SimTalk]

**See also**

- Replacement Mode
- Load Object

---

## ShiftCalendarObject [SimTalk] - Frame

Sets the ShiftCalendar, which controls the shifts worked in the Frame designated by `<Path>`.

**Syntax**

```
<Path>.ShiftCalendarObject:path
```

**Assignment Value**

You can assign a value of data type `object`/`path`.

**Example**

```simtalk
EngineAssembly.ShiftCalendarObject := MyShiftCalendar
```

**See also**

- Select Shift Calendar

---

## StateBlocked [SimTalk]

Sets the state of the Frame designated by `<Path>` to blocked (true) or not blocked (false).

**Type**

Attribute

**Syntax**

```
<Path>.StateBlocked:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

**Example**

```simtalk
Frame.StateBlocked := true
```

**See also**

- States of the Frame
- Blocked [state, material flow objects]

---

## StateEntryShut [SimTalk]

Sets the state of the Frame designated by `<Path>` to entrance closed (true) or not closed (false).

**Remarks**

The Frame only shows this state if the Recovery Time is active.

**Type**

Attribute

**Syntax**

```
<Path>.StateEntryShut:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

**Example**

```simtalk
Frame.StateEntryShut := true
```

**See also**

- States of the Frame
- Recovery Time [general description]

---

## StateResourceMissing [SimTalk]

Sets the state of the Frame designated by `<Path>` to resource missing/waiting for an Exporter (true) or not missing (false).

**Remarks**

The state resource missing/waiting applies when the Frame is waiting for resources, i.e., for services or MUs.

**Type**

Attribute

**Syntax**

```
<Path>.StateResourceMissing:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

**Example**

```simtalk
Frame.StateResourceMissing := true
```

**See also**

- States of the Frame
- Waiting [state, material flow objects]

---

## StateSetup [SimTalk]

Sets the state of the Frame designated by `<Path>` to setting-up (true) or not setting-up (false).

**Type**

Attribute

**Syntax**

```
<Path>.StateSetup:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

**Example**

```simtalk
Frame.StateSetup := true
```

**See also**

- States of the Frame
- Setting-Up [state, material flow objects]

---

## StateWorking [SimTalk]

Sets the state of the Frame designated by `<Path>` to working (true) or not working (false).

**Syntax**

```
<Path>.StateWorking:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

**Example**

```simtalk
Frame.StateWorking := true
```

**See also**

- States of the Frame
- Working [state, material flow objects]

---

## Stopped [SimTalk] - Frame

Stops the Frame designated by `<Path>` (true) or does not stop it (false).

**Type**

Attribute

**Syntax**

```
<Path>.Stopped:boolean
```

**Watchable**

The attribute is watchable. You can use an observer to find out if the state changed.

**Assignment Value**

You can assign a value to the data type `boolean`.

**Example**

```simtalk
Frame.Stopped := true
```

**See also**

- States of the Frame
- Stopped [state, material flow objects]

---

## Unplanned [SimTalk] - Frame

Sets the Frame designated by `<Path>` to unplanned when the current time is outside of any shift of the ShiftCalendar to which the Frame is assigned (true).

**Type**

Attribute

**Syntax**

```
<Path>.Unplanned:boolean
```

**Assignment Value**

You can assign a value of data type `boolean`.

Specify `false` to set it to planned to work.

**Example**

```simtalk
EngineAssembly.Unplanned := false
```

**See also**

- States of the Frame
- Unplanned [state, material flow objects]

---

## Interface

Use the object Interface for modeling transitions between Frames, i.e., from one part of the model to another. It also facilitates hierarchic modeling.
