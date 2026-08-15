# Point Clouds (SimTalk Reference)

Summary of SimTalk attributes and functions for state graphics, point clouds, and video recording settings.

## Accessing State Graphics

SimTalk provides the following attributes for the state graphics of material flow and fluid objects.

See also: *Edit 3D Properties [dialog] > States*

### `_3D.StatesForColoring [SimTalk]`

Sets which states are considered for state coloring of the object designated by `<Path>`.

- **Remarks:** Assigning the attribute deactivates graphic inheritance.
- **Type:** Attribute
- **Syntax:** `<Path>._3D.StatesForColoring:string[]`
- **Assignment Value:** You can assign an array of data type string.

**State of the object → Color**

| State of the object | Color |
|---|---|
| Unplanned | light blue |
| Paused | blue |
| Failed | red |
| Stopped | pink |
| Powering up/down | purple |
| Off | dark gray |
| Standby | light gray |
| Working | green |
| Blocked | yellow |
| Setting-Up | brown |
| Entrance closed | cyan |
| Waiting | orange |
| In execution (Method) | dark green |
| Suspended (Method) | purple |
| Encrypted (Method) | gray |
| Syntax error (Method) | light red |
| Program inherited (Method) | turquoise |

- **Note:** You can only assign the states that apply to the respective object.
- **Example:**

```simtalk
MyParallelStation._3D.StatesForColoring := ["Failed", "Stopped",
"Unplanned", "Paused", "Working", "Blocked", "Setting-up"]
```

See also: *States > Orientation [state graphic]*

### `_3D.StatesOrientation [SimTalk]`

Sets the orientation and the color of the state graphics of the object designated by `<Path>`.

- **Remarks:** When you set the attribute, Plant Simulation deletes existing state graphics or re-creates them with the orientation you set. Plant Simulation also resets the transformation (position and scaling) of the state graphic. Assigning the attribute deactivates graphic inheritance.
- **Type:** Attribute
- **Syntax:** `<Path>._3D.StatesOrientation:string`
- **Assignment Value:** You can assign a value of data type string. You can specify `"(Off)"`, `"Horizontal"`, `"Vertical"`, or `"Color"`.
- **Example:**

```simtalk
MyStation._3D.StatesOrientation := "Horizontal"
```

See also: *States > Orientation [state graphic]*

### `_3D.StatesPosition [SimTalk]`

Sets the reference point of the state graphic of the object designated by `<Path>`.

- **Remarks:** Assigning the position moves all state graphics according to these values. Assigning the attribute deactivates graphic inheritance.
- **Type:** Attribute
- **Syntax:** `<Path>._3D.StatesPosition:length[]`
- **Assignment Value:** You can assign an array of data type length.
- **Example:**

```simtalk
MyStation._3D.StatesPosition := [-1, 1, 1]
```

See also: *States > Position [state graphic]*, *`_3D.Position [SimTalk]`*, *Position [SimTalk] - graphic*

### `_3D.StatesScale [SimTalk]`

Sets the scaling of the state graphic of the object designated by `<Path>`.

- **Remarks:** Scaling changes the size and the position of all state graphics. Assigning the attribute deactivates graphic inheritance.
- **Type:** Attribute
- **Syntax:** `<Path>._3D.StatesScale:real/real[3]`
- **Assignment Value:** You can assign:
  - A value of data type real to use uniform scaling.
  - An array of data type real with three values to use different scaling factors for the three axes.
- **Return Value:** The return value is always an array with three values.
- **Example:**

```simtalk
MyStation._3D.StatesScale := 1          // uniform scaling
MyStation._3D.StatesScale := [1, 4, 9]  // different scaling factors for
the x-axis, y-axis and z-axis
var a := MyStation._3D.StatesScale      // 'a' designates an array
```

See also: *States > Scale [state graphic]*, *`_3D.Scale [SimTalk]`*, *Scale [SimTalk] - graphic*, *X/Y/Z [SimTalk] - array*

### `_3D.StatesScaleWithObject [SimTalk]`

Scales the state graphic as well when you scale the object designated by `<Path>` (`true`) or does not scale the state graphic (`false`).

- **Remarks:** To not scale the state graphic when you scale the object itself, specify `false`. Plant Simulation still scales the position of the state graphic though. Assigning the attribute deactivates graphic inheritance.
- **Type:** Attribute
- **Syntax:** `<Path>._3D.StatesScaleWithObject:boolean`
- **Assignment Value:** You can assign a value of data type boolean.
- **Example:**

```simtalk
MyStation._3D.StatesScaleWithObject := true
```

See also: *States > Scale With Object [check box]*

## Accessing Point Clouds

SimTalk provides the following attributes for point clouds of the Frame.

See also: *Edit 3D Properties [dialog] > Point Cloud*

### `_3D.PointCloudPath [SimTalk]`

Sets the file path to the point cloud you want to use in the Frame designated by `<Path>`.

- **Remarks:** A relative path refers to the folder in which your simulation model is located.
- **Type:** Attribute
- **Syntax:** `<Path>._3D.PointCloudPath:string`
- **Assignment Value:** You can assign a value of data type string.
- **Example:**

```simtalk
.Models.MyFrame._3D.PointCloudPath := "C:\Program Files\Siemens\Plant
Simulation 2606\3D\Siemens_Stand_Layers rotate 180degree.pod"
```

See also: *Edit 3D Properties [dialog] > Point Cloud > File Path*

### `_3D.PointCloudPosition [SimTalk]`

Sets the position of the point cloud in the Frame designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>._3D.PointCloudPosition:array`
- **Assignment Value:** You can assign a value of data type array. The values designate the X-position, the Y-position, and the Z-position of the point cloud in the simulation model.
- **Example:**

```simtalk
.Models.MyFrame._3D.PointCloudPosition := [2, 3, 0]
var a := .Models.MyFrame._3D.PointCloudPosition
```

See also: *Edit 3D Properties [dialog] > Point Cloud > Position [point cloud]*

### `_3D.PointCloudRotation [SimTalk]`

Sets the rotation, i.e., the rotation angle and the rotation axis, of the point cloud in the Frame designated by `<Path>`.

- **Remarks:** Plant Simulation interprets the rotation angle as a rotation around the negative z-axis.
- **Type:** Attribute
- **Syntax:** `<Path>._3D.PointCloudRotation:any`
- **Assignment Value:** You can specify:
  - A number which defines the rotation around the negative z-axis at the position at which you inserted the object.
  - An array with four values. The first value designates the angle, the remaining three values designate the components of the rotation axis.
- **Return Value:** When querying the attribute, 3D returns an array with four items.
- **Example:**

```simtalk
.Models.MyFrame._3D.PointCloudRotation := 30             // rotation by 30 degrees
.Models.MyFrame._3D.PointCloudRotation := [45, 0, 1, 0]  // rotates by 45 degrees
                                                         // around the y axis
```

See also: *Edit 3D Properties [dialog] > Point Cloud > Rotation [point cloud]*

## Accessing Video Recording Settings

SimTalk provides the following functions for accessing and recording a video.

### `F3DfinishVideo [SimTalk]`

Finishes the currently running video recording.

- **Remarks:** If you started the video recording with the dialog *Start Simulation Recording* or the function `F3DrecordSimulationVideo [SimTalk]`, finishing the video recording will stop the simulation.
- **Type:** Function
- **Syntax:** `F3DfinishVideo`
- **Example:**

```simtalk
F3DfinishVideo
```

See also: *Video Ribbon Tab > Finish Recording*, *stop [SimTalk] - EventController*

### `F3DisRecordingAVideo [SimTalk]`

Returns if a video is recorded at the moment or not.

- **Type:** Function
- **Syntax:** `F3DisRecordingAVideo -> boolean`
- **Example:**

```simtalk
-- If a video is currently being recorded we set the camera to different
-- positions
if F3DisRecordingAVideo
  -- First we want to show the model from a position we generated
  -- with the ribbon command 3D > View > Marks > Generate SimTalk Code...
  F3DconfigureView([1.043, -26.821, 13.465], 58.500, -17.565, .Models.Model)
  wait 15
  -- Now we play the camera path Ani1
  wait _3D.CameraAnimations.Ani1.play
  wait 5
  -- We set the camera to another position and direction
  F3DconfigureView([1.043, -26.821, 13.465], 58.500, -17.565, .Models.Model)
  wait 10
  -- Now we pause the video to skip parts of the simulation
  F3DpauseVideo(true)
  wait 15
  -- Now we continue recording
  F3DpauseVideo(false)
  wait 10
  waituntil Source.Cont != void
  var MU = Source.Cont
  -- We now attach the camera to a part on the source
  F3DAttachCamera(MU)
  waituntil MU.Location = Conveyor2
  -- Detach the camera
  F3DAttachCamera(void)
  -- We set the camera to another position and direction
  F3DconfigureView([1.043, -26.821, 13.465], 58.500, -17.565, .Models.Model)
  wait 10
  -- Finish the video recording
  F3DfinishVideo
end
```

### `F3DpauseVideo [SimTalk]`

Pauses the currently running video recording or continues playing it.

- **Type:** Function
- **Syntax:** `F3DpauseVideo([StartPause:boolean:=true])`
- **Parameter:** The optional parameter `StartPause` of data type boolean sets if the recording will be paused (`true` or parameter not specified) or continued (`false`).
- **Default Value of the Parameter:** The default value is `true`.
- **Example:**

```simtalk
F3DpauseVideo
```

See also: *Video Ribbon Tab > Pause/Resume Recording*

### `F3DrecordSimulationVideo [SimTalk]`

Starts the simulation or resumes it and records a video of it.

- **Remarks:** 3D records the video with the current settings of the dialog *Record Simulation Video*. Deactivate the safety setting *File > Model Settings > General > Prohibit Access to the Computer* to permit the function to copy data from another folder and write it to the model folder or its sub-folders. The function cannot copy files from the model folder or its sub-folders.
- **Type:** Function
- **Syntax:**

```simtalk
F3DrecordSimulationVideo(FilePath:string, ObjectOfInterest:object/3D
object, RealTimeScale:real[, FrameRate:integer:=25,
Description:string/void:="", RecordApplication:boolean:=false,
StartTime:time/void:=void, EndTime:time/void:=void, CameraPath:string:="",
LoopInfinitely:boolean:=false, StartPathWithRecording:boolean:=false,
EndRecordingWithPath:boolean:=false])
```

**Parameters:**

- **`FilePath`** (`string`) — designates the path to the video file that is going to be recorded.
- **`ObjectOfInterest`** (`object` or 3D object) — designates the object from whose view the simulation is recorded. The object either has to be the root Frame of a simulation or be inserted into the root Frame. An object which does not have an EventController, for example a class, is not allowed.
- **`RealTimeScale`** (`real`) — designates the real timescale with which the video will be played later on.
- **`FrameRate`** (`integer`, optional) — designates the frame rate for recording the video file. Default: 25 frames per second.
- **`Description`** (`string`/`void`, optional) — designates the description shown on the first frame of the video. Specify `void` to show no description; specify an empty string `""` to use the default description (the file name of the model). Default: `""`.
- **`RecordApplication`** (`boolean`, optional) — sets if the entire application window will be recorded (`true`) or only the window of the `ObjectOfInterest` (`false`). If `false` and no such window is open, Plant Simulation opens a suitable window. Default: `false`.
- **`StartTime`** (`time`/`void`, optional) — sets when recording starts. Specify `void` or nothing to start recording when the simulation is started or continued. If you specify a time, recording starts at this point in time; if the point in time is located in the past relative to the current simulation time, the simulation is reset beforehand. Default: `void`.
- **`EndTime`** (`time`/`void`, optional) — sets when recording terminates. Specify `void` or nothing to never terminate recording by itself. If you specify a time, recording and simulation run up to this point in time of the simulation and then terminate. An End Time typed into the EventController will be deactivated for the duration of the recording. Default: `void`.
- **`CameraPath`** (`string`, optional) — designates the camera path that will be played during the simulation and recording. If empty string `""` or nothing, no camera path is played automatically. *Note: only applies to the Frame.* Default: `""`.
- **`LoopInfinitely`** (`boolean`, optional) — sets if the camera path is looped infinitely. `true` replays the path from the start after reaching its end; `false` or nothing makes the view remain at its location. *Note: only applies to the Frame.* Default: `false`.
- **`StartPathWithRecording`** (`boolean`, optional) — sets if the camera path is played when recording starts (`true`) or when the simulation starts/continues (`false` or nothing). *Note: only applies to the Frame.* Default: `false`.
- **`EndRecordingWithPath`** (`boolean`, optional) — sets if simulation and video recording are also terminated when reaching the end of the camera path (`true`) or continued after the end (`false` or nothing). *Note: only applies to the Frame.* Default: `false`.

- **Example:**

```simtalk
F3DrecordSimulationVideo("C:\Users\ha\Desktop\PlantSimulationVideo.avi", 6,
25, "")
```

See also: *Prohibit Access to the Computer [model settings]*, *Start Simulation Recording*, *Video Ribbon Tab > Start Simulation Recording*

### `F3DrecordVideo [SimTalk]`

Records a video of Plant Simulation or of the active window.

- **Remarks:** 3D records the video with the current settings of the dialog *Record Video*. If you deactivate the safety setting *File > Model Settings > General > Prohibit Access to the Computer*, the function can copy data from another folder and write it to the model folder or its sub-folders. The function cannot copy files from the model folder or its sub-folders.
- **Type:** Function
- **Syntax:**

```simtalk
F3DrecordVideo(FilePath:string[, FrameRate:integer:=25,
Description:string:="", RecordApplication:boolean:=false])
```

**Parameters:**

- **`FilePath`** (`string`) — designates the path to the video file that is going to be recorded. By default, the file is saved to `C:\Users\YourLoginName\Desktop\`.
- **`FrameRate`** (`integer`, optional) — designates the frame rate for recording the video file. Default: 25 frames per second.
- **`Description`** (`string`, optional) — designates the description shown on the first frame of the video. Specify `void` to show no description; specify an empty string `""` to use the default description (the file name of the model). Default: `""`.
- **`RecordApplication`** (`boolean`, optional) — sets if the entire application window will be recorded (`true`) or only the 3D window of the `ObjectOfInterest` (`false`). Default: `false`.

- **Example:**

```simtalk
F3DrecordVideo("C:\Users\ha\Desktop\PlantSimulationVideo.avi",
25, .Models.MyChocolatePlant)
```

See also: *Prohibit Access to the Computer [model settings]*, *Video Ribbon Tab > Start Simple Recording*
