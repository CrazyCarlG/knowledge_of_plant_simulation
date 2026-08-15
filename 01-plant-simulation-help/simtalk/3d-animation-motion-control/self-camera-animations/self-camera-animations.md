# Self & Camera Animations (SimTalk)

Reference for SimTalk attributes and methods controlling **Self Animations** and **Camera Animations** in 3D.

## Overview

Plant Simulation provides functions for Self Animations and Camera Animations.

- **Self Animations**: available on all objects except Folder, Connector, Interface, and MUs.
- **Camera Animations**: available only on the Frame.

You can buffer the entirety (or all animations of a type) in a value of data type `any`:

```simtalk
var a : any := .Materialflow.PickAndPlace._3D.SelfAnimations
var a : any := .Models.Model._3D.CameraAnimations
```

---

## Self Animations

### Setting Attributes

#### `_3D.AniRotationAxis`
Sets the rotation axis for `_3D.SelfAnimations.scheduleRotation`.

- **Type**: Attribute
- **Syntax**: `<Path>._3D.AniRotationAxis:real[3]`
- Assignment: array of three `real` values (X, Y, Z rotation axis components).

```simtalk
MyStation._3D.AniRotationAxis := [0,1,0]
// rotates the object around its y-axis
```

#### `_3D.AniRotationCenter`
Sets the rotation center for `_3D.SelfAnimations.scheduleRotation`.

- **Type**: Attribute
- **Syntax**: `<Path>._3D.AniRotationCenter:length[3]`
- Assignment: array of three `length` values (X, Y, Z position of the rotation center).

```simtalk
MyStation._3D.AniRotationCenter := [1,0,0]
// rotates the object with an offset of 1,0,0
```

#### `_3D.AniTranslationDirection`
Sets the translation direction for the poses animation.

- **Type**: Attribute
- **Syntax**: `<Path>._3D.AniTranslationDirection:length[3]`
- Assignment: array of three `length` values (X, Y, Z translation direction).
- Compare `_3D.getObject` for accessing animatable objects.

```simtalk
MyStation._3D.getObject(1).AniTranslationDirection := [1,0,0]
```

---

### Animation Path Methods (per saved animation)

These methods use `<AnimationPathName>` as the name of a saved animation path.

#### `.delete`
Deletes the specified Self Animation.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.<AnimationPathName>.delete → boolean
  <Path>._3D.SelfAnimations.getAnimation(<...>).delete → boolean
  ```
- Returns `boolean`: `true` if deleted, `false` otherwise.
- **Note**: generated animations cannot be deleted.

```simtalk
.MaterialFlow.Station._3D.SelfAnimations.Default.delete
// deletes the self animation named 'Default' of the class of the Station
```

#### `.getTable`
Writes the animation data of all saved animations into the specified table. Plant Simulation automatically formats the table.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.<AnimationPathName>.getTable(Target:table)
  <Path>._3D.SelfAnimations.getAnimation(<...>).getTable(Target:table)
  ```

```simtalk
// sea stands for self animation
var sea:= Buffer._3D.SelfAnimations
var created : boolean := sea.createAnimationLine("Animation2")
if created // The animation line was created.
   var t: table // Copy the 'Default' line values to the table.
   sea.Default.getTable(t)
   sea.Animation2.setTable(t)
end
```

#### `.IsCurve` / `.IsLine` / `.IsSpline`
Return whether the animation is of type Polycurve / Lines / Spline.

- **Type**: Read-only attribute
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.<AnimationPathName>.IsCurve → boolean
  <Path>._3D.SelfAnimations.getAnimation(<...>).IsCurve → boolean
  ```

```simtalk
var b : boolean := .MaterialFlow.Station._3D.SelfAnimations.Default.IsCurve
var b : boolean := .MaterialFlow.Station._3D.SelfAnimations.Default.IsLine
var b : boolean := .MaterialFlow.Station._3D.SelfAnimations.Default.IsSpline
```

#### `.play`
Schedules the saved Self Animation and then plays it. An implicit `SelfAnimations.reset` runs before executing.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.<AnimationPathName>.play([Backwards:boolean:=false]) → time
  <Path>._3D.SelfAnimations.getAnimation(<...>).play([Backwards:boolean:=false]) → time
  ```
- Parameter `Backwards` (default `false`): play backward (`true`) or forward (`false`).
- Returns `time`: the time the animation takes.

```simtalk
self.~._3D.SelfAnimations.VerticalAni.play
self.~._3D.SelfAnimations.MyAnimationPath.play
```

#### `.schedule`
Schedules the saved animation (does not play yet — call `_3D.SelfAnimations.playAnimation` to run it).

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.<AnimationPathName>.schedule([Backwards:boolean:=false])
  <Path>._3D.SelfAnimations.getAnimation(<...>).schedule([Backwards:boolean:=false])
  ```

```simtalk
self.~._3D.SelfAnimations.VerticalAni.schedule
self.~._3D.SelfAnimations.playAnimation
```

#### `.setTable`
Overwrites the specified Self Animation with the data of the passed table. The table must be formatted correctly, otherwise changes are cancelled.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.<AnimationPathName>.setTable(Source:table)
  <Path>._3D.SelfAnimations.getAnimation(<...>).setTable(Source:table)
  ```

```simtalk
var sea := Buffer._3D.MUAnimations
var created : boolean := sea.createAnimationLine("Animation2")
if created // The animation line was created.
   var t: table // Copy the 'Default' line values to the table.
   sea.Default.getTable(t)
   sea.Animation2.setTable(t)
end
```

---

### Self Animations Methods & Attributes

#### `_3D.SelfAnimations.AnimationTimeBlock`
Time the next animation block will most likely require (relates to simulation time).

- **Type**: Read-only attribute
- **Syntax**: `<Path>._3D.SelfAnimations.AnimationTimeBlock → time`

```simtalk
var t : time := self.~._3D.SelfAnimations.AnimationTimeBlock
```

#### `_3D.SelfAnimations.AnimationTimeTotal`
Time the animation of all blocks will most likely require.

- **Type**: Read-only attribute
- **Syntax**: `<Path>._3D.SelfAnimations.AnimationTimeTotal → time`

```simtalk
var t : time := self.~._3D.SelfAnimations.AnimationTimeTotal
```

#### `_3D.SelfAnimations.createAnimationCurve`
Creates a new saved animation path of type Polycurve.

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.createAnimationCurve(Name:string) → boolean`
- Returns `true` if created successfully (name not yet assigned).

```simtalk
var a: boolean := self.~._3D.SelfAnimations.createAnimationCurve("Curved Movement")
if not a
   print "The animation curve could not be created."
end
```

#### `_3D.SelfAnimations.createAnimationLine`
Creates a new saved animation path of type Lines.

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.createAnimationLine(Name:string) → boolean`

```simtalk
var sea := Buffer._3D.SelfAnimations
```

#### `_3D.SelfAnimations.createAnimationSpline`
Creates a new saved animation path of type Spline.

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.createAnimationSpline(Name:string) → boolean`

```simtalk
var a: boolean := self.~._3D.SelfAnimations.createAnimationSpline("spline movement")
if not a
   print "The animation spline could not be created."
end
```

#### `_3D.SelfAnimations.deleteAllAnimationBlocks`
Deletes all scheduled animation blocks (does not change saved animations).

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.deleteAllAnimationBlocks`

```simtalk
self.~._3D.SelfAnimations.deleteAllAnimationBlocks
```

#### `_3D.SelfAnimations.deleteNextAnimationBlock`
Deletes the entire next scheduled animation block.

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.deleteNextAnimationBlock`

```simtalk
self.~._3D.SelfAnimations.deleteNextAnimationBlock
```

#### `_3D.SelfAnimations.getAnimation`
Returns a Self Animation.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.getAnimation(AnimationPathName:string)
  <Path>._3D.SelfAnimations.getAnimation(Index:integer)
  ```
- `AnimationPathName` (string): a saved animation whose name is an illegal SimTalk identifier (e.g. `"#0#0"`).
- `Index` (integer): the n-th animation.
- Returns `void` if a string is given and no such animation exists (instead of opening the Debugger).

```simtalk
var t: table
self.~._3D.SelfAnimations.getAnimation("#0#0").getTable(t)
var t: table
self.~._3D.SelfAnimations.getAnimation(7).getTable(t)
```

If a saved animation name is a legal SimTalk identifier, access it via the path extension.

#### `_3D.SelfAnimations.getTable`
Writes animation data of all saved animations into the specified table (automatically formatted).

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.getTable(Target:table)`

```simtalk
var t : table
self.~._3D.SelfAnimations.getTable(t)
debug
self.~._3D.SelfAnimations.setTable(t)
```

#### `_3D.SelfAnimations.pause`
Pauses currently playing Self Animations.

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.pause`

```simtalk
self.~._3D.SelfAnimations.pause
```

#### `_3D.SelfAnimations.play`
Plays all scheduled Self Animations.

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.play`

```simtalk
var animations : any := self.~._3D.getObject("Arm").SelfAnimations
animations.reset
animations.RotateDown.schedule
animations.startNextAnimationBlock
animations.FinishDown.schedule
animations.scheduleRotation(0, 360, 90)
@.OutIn(animations.AnimationTimeTotal)
animations.play
self.~._3D.SelfAnimations.scheduleRotation(0, 90, 15)
self.~._3D.SelfAnimations.play
```

#### `_3D.SelfAnimations.playRotation`
Schedules a rotation animation and then plays the scheduled animations. Rotates around the Rotation Axis and Rotation Center defined on the Self Animation tab.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.playRotation(StartRotationAngle:real, TargetRotationAngle:real, AngleVelocity:real) → time
  ```
  Abbreviated form:
  ```simtalk
  <Path>._3D.playRotation(StartRotationAngle:real, TargetRotationAngle:real, AngleVelocity:real) → time
  ```
- Parameters (all `real`): start rotation angle (degrees), target rotation angle (degrees), angle velocity (degrees/second).
- Returns `time` — the duration; can be passed directly to a `wait` instruction.
- **Note**: implicit `_3D.SelfAnimations.reset` before executing.

```simtalk
self.~._3D.SelfAnimations.playRotation(0, 90, 15)
self.~._3D.playRotation(0, 90, 15) // abbreviated form
wait self.~._3D.playRotation(0, 90, 15)
// wait until the rotation is finished
```

#### `_3D.SelfAnimations.playTranslation`
Schedules an anonymous translation animation and then plays the scheduled animations.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.playTranslation(StartTranslation:length[3], TargetTranslation:length[3], Speed:speed) → time
  ```
  Abbreviated form:
  ```simtalk
  <Path>._3D.playTranslation(StartTranslation:real[3], TargetTranslation:real[3], Speed:speed) → time
  ```
- Parameters: `StartTranslation` / `TargetTranslation` (three-value `length` arrays), `Speed` (`speed`, meters/second).
- Returns `time` — can be passed directly to a `wait` instruction.
- **Note**: implicit `SelfAnimations.reset` before executing.

```simtalk
// Moves the existing animation object of the Station with an offset in
// the x direction from 0 to 10 meters. The speed is 2m/s.
var myAnimationObj := Station._3D.getObject(1)
myAnimationObj.SelfAnimations.playTranslation([0,0,0], [10,0,0], 2.0)
// Instead you can also use the abbreviated notation:
var myAnimationObj := Station._3D.getObject(1)
myAnimationObj.playTranslation([0,0,0], [10,0,0], 2.0)
wait Station._3D.playTranslation([0,0,0], [0,0,3.8], 1.2)
wait Station._3D.SelfAnimations.playTranslation([0,0,0], [0,0,3.8], 1.2)
```

#### `_3D.SelfAnimations.resetAnimation`
Resets all scheduled Self Animations — stops the currently playing animation and cancels all scheduled animations.

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.resetAnimation`

```simtalk
var animations : any := self.~._3D.getObject("Arm").SelfAnimations
animations.resetAnimation
animations.DownAdvance.schedule
animations.startNextAnimationBlock
animations.DownFinal.schedule
animations.scheduleRotation(0, 360, 90)
@.outIn(animations.AnimationTimeTotal)
animations.play
self.~._3D.SelfAnimations.resetAnimation
```

#### `_3D.SelfAnimations.scheduleRotation`
Schedules a rotation animation (does not play — call `_3D.SelfAnimations.play`).

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.scheduleRotation(StartRotationAngle:real, TargetRotationAngle:real, AngleVelocity:real)
  ```
- Rotates around the Rotation Axis and Rotation Center defined on the Self Animation tab.

```simtalk
var animations : any := self.~._3D.getObject("Arm").SelfAnimations
animations.reset
animations.DownAdvance.schedule
animations.startNextAnimationBlock
animations.DownFinal.schedule
animations.scheduleRotation(0, 360, 90)
@.outIn(animations.AnimationTimeTotal)
animations.play
self.~._3D.SelfAnimations.scheduleRotation(0, 90, 15)
self.~._3D.SelfAnimations.play
```

#### `_3D.SelfAnimations.scheduleTranslation`
Schedules an anonymous translation animation (does not play — call `_3D.SelfAnimations.play`).

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.SelfAnimations.scheduleTranslation(StartTranslation:length[3], TargetTranslation:length[3], Speed:speed)
  ```

```simtalk
// Drives the existing animation object of the Station with an offset in
// the x direction from 0 to 10 meters. The speed is 2m/s.
var myAnimationObj := Station._3D.getObject(1)
myAnimationObj.SelfAnimations.reset
myAnimationObj.SelfAnimations.scheduleTranslation([0,0,0], [10,0,0], 2.0)
myAnimationObj.SelfAnimations.play
```

#### `_3D.SelfAnimations.setTable`
Overwrites the saved animations of the Self Animation with the data of the passed table. The table must be formatted correctly.

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.setTable(Source:table)`

```simtalk
var t: table
self.~._3D.SelfAnimations.getTable(t)
debug
self.~._3D.SelfAnimations.setTable(t)
```

#### `_3D.SelfAnimations.startNextAnimationBlock`
Terminates the currently playing animation block and starts the next one. The animation of the last block remains active until reset.

- **Type**: Method
- **Syntax**: `<Path>._3D.SelfAnimations.startNextAnimationBlock`

```simtalk
self.~._3D.SelfAnimations.VerticalAni.schedule
self.~._3D.SelfAnimations.scheduleRotation(0, 90, 30)
self.~._3D.SelfAnimations.startNextAnimationBlock
self.~._3D.SelfAnimations.HorizontalAni.schedule
self.~._3D.SelfAnimations.scheduleRotation(90, 45, 15)
self.~._3D.SelfAnimations.startNextAnimationBlock
self.~._3D.SelfAnimations.scheduleRotation(45, 0, 10)
self.~._3D.SelfAnimations.play
```

---

## Camera Animations

Only the **Frame** provides Camera Animations.

### Animation Path Methods (per saved camera animation)

#### `.delete`
Deletes the specified Camera Animation.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.CameraAnimations.<AnimationPathName>.delete → boolean
  <Path>._3D.CameraAnimations.getAnimation(<...>).delete → boolean
  ```

```simtalk
_3D.CameraAnimations.Default.delete
```

#### `.getTable`
Writes animation data of all saved animations of the specified Camera Animation into the table (automatically formatted).

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.CameraAnimations.<AnimationPathName>.getTable(Target:table)
  <Path>._3D.CameraAnimations.getAnimation(<...>).getTable(Target:table)
  ```

```simtalk
// cama stands for camera animation
var cama:= _3D.CameraAnimations
var created : boolean := cama.createAnimationLine("Animation2")
if created // The animation line was created.
   var t: table // Copy the 'Default' line values to the table.
   cama.Default.getTable(t)
   cama.Animation2.setTable(t)
end
```

#### `.IsCurve` / `.IsLine` / `.IsSpline`
Return whether the animation is of type Polycurve / Lines / Spline.

- **Type**: Read-only attribute
- **Syntax**:
  ```simtalk
  <Path>._3D.CameraAnimations.<AnimationPathName>.IsCurve → boolean
  <Path>._3D.CameraAnimations.getAnimation(<...>).IsCurve → boolean
  ```

```simtalk
var b : boolean := _3D.MUAnimations.Default.IsCurve
var b : boolean := _3D.MUAnimations.Default.IsLine
var b : boolean := _3D.CameraAnimations.Default.IsSpline
```

#### `.play`
Schedules the saved Camera Animation and then plays it. Implicit `CameraAnimations.reset` before executing.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.CameraAnimations.<AnimationPathName>.play([Backwards:boolean:=false, Factor:real:=1]) → time
  <Path>._3D.CameraAnimations.getAnimation(<...>).play([Backwards:boolean:=false]) → time
  ```
- `Backwards` (default `false`): play backward/forward.
- `Factor` (default `1`): positive factor multiplied onto animation speed (0.5 = slower, 2 = twice as fast).
- Returns `time`.

```simtalk
self.~._3D.CameraAnimations.VerticalAni.play
self.~._3D.CameraAnimations.MyAnimationPath.play
```

#### `.schedule`
Schedules a saved camera animation (does not play — call `_3D.CameraAnimations.play`).

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.CameraAnimations.<AnimationPathName>.schedule([Backwards:boolean:=false, Factor:real:=1]])
  <Path>._3D.CameraAnimations.getAnimation(<...>).schedule([Backwards:boolean:=false])
  ```

```simtalk
self.~._3D.CameraAnimations.VerticalAni.schedule
self.~._3D.CameraAnimations.playAnimation
```

#### `.setTable`
Overwrites the saved camera animation data with the passed table (must be formatted correctly).

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.CameraAnimations.<AnimationPathName>.setTable(Source:table)
  <Path>._3D.CameraAnimations.getAnimation(<...>).setTable(Source:table)
  ```

```simtalk
var cama := _3D.CameraAnimations
var created : boolean := cama.createAnimationLine("Animation2")
if created // The animation line was created.
   var t: table // Copy the 'Default' line values to the table.
   cama.Default.getTable(t)
   cama.Animation2.setTable(t)
end
```

---

### Camera Animations Methods & Attributes

#### `_3D.CameraAnimations.AnimationTimeBlock`
Time the next block's Camera Animation will most likely require (relates to simulation time). For Camera Animations a block generally consists of a single animation (no overlap).

- **Type**: Read-only attribute
- **Syntax**: `<Path>._3D.CameraAnimations.AnimationTimeBlock → time`

```simtalk
var t : time := self.~._3D.CameraAnimations.AnimationTimeBlock
```

#### `_3D.CameraAnimations.AnimationTimeTotal`
Time the animation of all blocks will most likely require.

- **Type**: Read-only attribute
- **Syntax**: `<Path>._3D.CameraAnimations.AnimationTimeTotal → time`

```simtalk
var t : time := self.~._3D.CameraAnimations.AnimationTimeTotal
```

#### `_3D.CameraAnimations.Count`
Number of saved animation paths for the Camera Animation.

- **Type**: Read-only attribute
- **Syntax**: `<Path>._3D.CameraAnimations.Count → integer`

```simtalk
var cama := MyFrame._3D.CameraAnimations
```

#### `_3D.CameraAnimations.createAnimationCurve`
Creates a new saved animation path of type Polycurve.

- **Type**: Method
- **Syntax**: `<Path>._3D.CameraAnimations.createAnimationCurve(Name:string) → boolean`

```simtalk
var a: boolean := self.~._3D.CameraAnimations.createAnimationCurve("curved movement")
if not a
   print "The animation curve could not be created."
end
```

#### `_3D.CameraAnimations.createAnimationLine`
Creates a new saved animation path of type Lines.

- **Type**: Method
- **Syntax**: `<Path>._3D.CameraAnimations.createAnimationLine(Name:string) → boolean`

```simtalk
var a: boolean := self.~._3D.CameraAnimations.createAnimationLine("straight movement")
if not a
   print "The animation line could not be created."
end
```

#### `_3D.CameraAnimations.createAnimationSpline`
Creates a new saved animation path of type Spline.

- **Type**: Method
- **Syntax**: `<Path>._3D.CameraAnimations.createAnimationSpline(Name:string) → boolean`

```simtalk
var a: boolean := self.~._3D.CameraAnimations.createAnimationSpline("spline movement")
if not a
   print "The animation spline could not be created."
end
```

#### `_3D.CameraAnimations.getAnimation`
Returns the specified Camera Animation.

- **Type**: Method
- **Syntax**:
  ```simtalk
  <Path>._3D.CameraAnimations.getAnimation(AnimationPathName:string)
  <Path>._3D.CameraAnimations.getAnimation(Index:integer)
  ```
- Returns `void` if a string is passed and the animation does not exist (instead of opening the Debugger).

```simtalk
var t: table
self.~._3D.CameraAnimations.getAnimation("#0#0").getTable(t)
var t: table
self.~._3D.CameraAnimations.getAnimation(7).getTable(t)
```

If a saved animation name is a legal SimTalk identifier, access it via the path extension.

#### `_3D.CameraAnimations.getTable`
Writes animation data of all saved animations into the table (automatically formatted).

- **Type**: Method
- **Syntax**: `<Path>._3D.CameraAnimations.getTable(Target:table)`

```simtalk
var t : table
self.~._3D.CameraAnimations.getTable(t)
debug
self.~._3D.CameraAnimations.setTable(t)
```

#### `_3D.CameraAnimations.pause`
Pauses currently playing camera animations.

- **Type**: Method
- **Syntax**: `<Path>._3D.CameraAnimations.pause`

```simtalk
self.~._3D.CameraAnimations.pause
```

#### `_3D.CameraAnimations.play`
Plays all scheduled camera animations.

- **Type**: Method
- **Syntax**: `<Path>._3D.CameraAnimations.play`

```simtalk
var animations : any := self.~._3D.getObject("Arm").CameraAnimations
animations.reset
animations.rotateDown.schedule
animations.startNextAnimationBlock
animations.downFinished.schedule
animations.scheduleRotation(0, 360, 90)
@.austrittIn(animations.AnimationTimeTotal)
animations.play
self.~._3D.CameraAnimations.scheduleRotation(0, 90, 15)
self.~._3D.CameraAnimations.play
```

#### `_3D.CameraAnimations.resetAnimation`
Resets all scheduled Camera Animations — stops all playing and cancels all scheduled animations.

- **Type**: Method
- **Syntax**: `<Path>._3D.CameraAnimations.resetAnimation`

```simtalk
var animations : any := self.~.Models.MyFrame._3D.CameraAnimations
animations.resetAnimation
animations.Roundtrip.schedule
animations.play
self.~._3D.CameraAnimations.resetAnimation
```

#### `_3D.CameraAnimations.setTable`
Overwrites the saved camera animations with the data of the passed table.

- **Type**: Method
- **Syntax**: `<Path>._3D.CameraAnimations.setTable(Source:table)`

```simtalk
var t: table
self.~._3D.CameraAnimations.getTable(t)
debug
self.~._3D.CameraAnimations.setTable(t)
```
