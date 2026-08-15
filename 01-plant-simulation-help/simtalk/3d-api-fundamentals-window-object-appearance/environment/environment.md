# SimTalk Access to 3D Functions

Plant Simulation provides general SimTalk functions plus a number of specific functions for accessing the 3D objects.

## Notes

- SimTalk normally does not distinguish between upper- and lower-casing for the names of methods, attributes, and read-only attributes typed into the source code of a Method.
- You can view and access the attributes and methods of the 3D objects by clicking **Auto Complete** on the Edit ribbon tab of the Method Editor.
- To access the attributes and methods of the 3D objects, type `_3D.` followed by a period in your instructions.
- Most of the 3D attributes and 3D methods listed in the table of contents use array data types for setting and getting values.

## See also

- 3D Properties — Visualizing the Simulation
- Copy Object Settings to a Method
- General Access to SimTalk

---

# General Access

## Table of contents

- Accessing the 3D Window
- Accessing View Options
- Accessing the Bounding Box
- Accessing Length-oriented Objects
- Accessing the Appearance of Objects and MUs
- Accessing the Appearance of the Store
- Accessing the Background Color of Frame and Folder
- Accessing Object Captions
- Accessing the Fill Level of the Buffer
- Accessing Objects in 3D
- Accessing Point Clouds
- Accessing Transformation Settings

## Accessing Animations

- Accessing MU Animations
- Accessing Self Animations
- Accessing Camera Animations
- Accessing Robot Arm Animations
- Accessing Joints
- Accessing Poses
- Accessing the Worker

## Accessing Graphics

- Accessing Methods of Graphic Shapes
- Accessing Attributes of Graphic Shapes
- Accessing Attributes and Read-Only Attributes of Graphic Groups
- Accessing Methods of Graphic Groups
- Accessing Graphics
- Detailed Access To Graphics
- Accessing State Graphics

## Accessing PLMXML Kinematics Files

- Accessing PLMXML Kinematics Files

---

# Copy Object Settings to a Method

You can copy the following settings of simulation objects, animatable objects, and graphics and paste them into a Method:

- **Copy path of selected object**: Press `Ctrl+C` in the Frame, change to the Method, press `Ctrl+V` to paste the path (e.g., `EventController`, `Source`, `Frame`).
- **Copy path of selected shape**: Press `Ctrl+C` in the Frame, change to the Method, press `Ctrl+V` (e.g., `Cuboid`).
- **Copy current material settings of selected shape**: Press `Spacebar` in the Frame, change to the **Material** tab, activate the Material, click the copy button, change to the Method, and press `Ctrl+V` (e.g., `Cuboid`).
- **Copy path of selected animatable object**: Press `Ctrl+C` in the Frame, change to the Method, press `Ctrl+V` (e.g., `Sphere`).

You can then type a period and press `Ctrl+Spacebar` to extend the path (compare the command Auto Complete).

In the illustrations of the Method, the number in brackets — e.g., the highlighted `("deco", [1])` — designates the graphic node with the respective number. The dialog **Show Graphic Structure** also shows this number.

## See also

- `_3D.getGraphic [SimTalk]`
- Auto Complete
- Show Graphic Structure [context menu]

---

# Accessing PLMXML Kinematics Files

SimTalk provides the functions listed here for accessing PLMXML kinematics files.

## applyPLMXMLKinematicStructure [SimTalk]

Applies a kinematics structure from the specified PLMXML file to the graphic designated by `<Path>`.

**Remarks:** During this process animatable objects are created within the simulation object or animatable object, furnished with kinematics settings from the PLMXML file, and containing parts of the graphic designated by `<Path>`.

- **Type:** Method

**Syntax**

```
<Path>.applyPLMXMLKinematicStructure(FilePath:string[,
PreferFirstEntryPoint:boolean:=true, PreferredEntryPointName:string:=""])
-> boolean
```

**Parameters**

- `FilePath` (string) — path to the PLMXML file containing the desired information.
- `PreferFirstEntryPoint` (boolean, optional) — specifies if the first (`true`) or the last (`false`) potential kinematics structure is to be used. Default: `true`.
- `PreferredEntryPointName` (string, optional) — sets the name of the root of the kinematics structure to be used if several potential kinematics structures exist. If empty `""`, the method ignores the parameter. If you specify both optional parameters, the preferred name is stronger than the preferred first/last entry point. Default: `""`.

**Return Value:** boolean — `true` if a kinematics structure was found and applied; `false` if no kinematics structure was found.

**Examples**

```
var newGraphic: any :=
MyStation._3D.getGraphic("default").importGraphics("D:\Graphic.jt")
var kinematicsApplicable:boolean :=
newGraphic.applyPLMXMLKinematicStructure("D:\kin.plmxml")
if not kinematicsApplicable then
   -- error handler
end
```

```
var roots: string[] := getPotentialPLMXMLKinematicRoots("D:\kin.plmxml")
if roots.Dim = 0 then
   -- error handler
else
   var newGraphic: any :=
MyStation._3D.getGraphic("default").importGraphics("D:\Graphic.jt")
   if roots.Dim > 1 then
   var kinematicsApplicable: boolean  :=
newGraphic.applyPLMXMLKinematicStructure("D:\kin.plmxml", true, roots[2])
   if not kinematicsApplicable then
       -- error handler
   end
       else
       var kinematicsApplicable: boolean  :=
newGraphic.applyPLMXMLKinematicStructure("D:\kin.plmxml")
       if not kinematicsApplicable then
-- error handler
       end
   end
end
```

**See also:** `getPotentialPLMXMLKinematicRoots [SimTalk]`

## getPotentialPLMXMLKinematicRoots [SimTalk]

Reads kinematics information from the designated PLMXML file and lists all roots of all potential kinematics structures from the file.

- **Type:** Method

**Syntax**

```
getPotentialPLMXMLKinematicRoots(FilePath:string) -> string[]
```

**Parameter**

- `FilePath` (string) — path to the PLMXML file containing the desired information.

**Return Value:** array of data type `string`.

- If the array is empty, Plant Simulation did not find a kinematics root (e.g., a PLMXML file without kinematics information or with incomplete kinematics).
- If the array contains a single name, the file contains a unique kinematics root.
- If the array contains several names, several ways exist for interpreting the structure which are indistinguishable without context.

**Note:** The same name can occur several times.

**Example**

```
var roots : string[] := getPotentialPLMXMLKinematicRoots("D:\kin.plmxml")
print roots.dim, roots[1]
```

**See also:** `applyPLMXMLKinematicStructure [SimTalk]`

---

# Accessing the 3D Window

SimTalk provides the following methods and functions for accessing the 3D window.

## _3D.closeWindows [SimTalk]

Closes all windows which are opened for the object designated by `<Path>`.

- **Type:** Method

**Syntax**

```
<Path>._3D.closeWindows
```

**Example**

```
MyStation._3D.closeWindows
```

**See also:** `closeDialog [SimTalk]` — all objects

## F3DactivateCameraMark [SimTalk]

Activates the specified camera mark in the currently active 3D window.

**Remarks:** The camera mark changes the viewpoint and object of interest in the active 3D window.

- **Type:** Function

**Syntax**

```
F3DActivateCameraMark(CameraMark:string)
```

**Parameter:** `CameraMark` (string) — name of the camera mark.

**Example**

```
F3DactivateCameraMark("MyCameraMark")
```

**See also:** Camera Marks

## F3DattachCamera [SimTalk]

Attaches the camera of the active 3D window to the specified object or detaches a previously attached camera in the active 3D window.

**Remarks:** `F3DattachCamera` will not do anything if there is no 3D window open or if the active 3D window is shown in Planning View.

- **Type:** Function

**Syntax**

```
F3DattachCamera(ObjectToAttach:any)
```

**Parameter:** `ObjectToAttach` (any) — the object to which you want to attach the camera:
- Specify `void` to detach an attached camera in the active 3D window.
- Specify an object or a 3D object (for example an animatable object) to attach the camera to that object.

**Example**

```
F3DattachCamera(.MUs.Part:1)
```

**See also:** Attach Camera, `F3DconfigurePlanningView [SimTalk]`

## F3DconfigurePlanningView [SimTalk]

Sets the view to a Planning View designated by the specified parameters.

- **Type:** Function

**Syntax**

```
F3DconfigurePlanningView(ViewPosition:real[2], Zoom:real[,
ObjectOfInterest:object/3Dobject])
```

**Parameters**

- `ViewPosition` (real[2]) — array with two values designating the position of the view's projection in the XY Plane.
- `Zoom` (real) — zoom factor of the view.
- `ObjectOfInterest` (object, optional) — opens the object in the active 3D window. Can be an object, a 3D object (e.g., an animatable object), or a simulation object. If not specified, the open 3D window remains unchanged.

**Example**

```
F3DconfigurePlanningView([-14, -15], 16, .Models.MyWarehouse)
```

**See also:** `_3D.getObject [SimTalk]`, Camera Marks, Use Planning View, `F3DconfigureView [SimTalk]`, Generate SimTalk Code and Copy to Clipboard [camera mark]

## F3DconfigureView [SimTalk]

Sets the view to a Modeling View designated by the specified parameters.

- **Type:** Function

**Syntax**

```
F3DconfigureView(CameraPosition:real[3], CameraRotationX:real,
CameraRotationZ:real[, ObjectOfInterest:object])
```

**Parameters**

- `CameraPosition` (real[3]) — array with three values designating the position of the camera in three-dimensional space.
- `CameraRotationX` (real) — rotation of the camera on the x-axis.
- `CameraRotationZ` (real) — rotation of the camera on the z-axis.
- `ObjectOfInterest` (object, optional) — opens the object in the active 3D window. Can be an object, a 3D object (e.g., an animatable object), or a simulation object. If not specified, the open 3D window remains unchanged.

**Example**

```
F3DconfigureView([-8.129, -3.707, 7.832], 45.000,
-15.000, .Models.MyWarehouse)
```

**See also:** `_3D.getObject [SimTalk]`, Camera Marks, `F3DconfigurePlanningView [SimTalk]`, Generate SimTalk Code and Copy to Clipboard [camera mark]

---

# Accessing View Options

SimTalk provides the following attributes for setting view options of the Frame in 3D.

**See also:** View Ribbon Tab

## _3D.PlanningView [SimTalk]

Activates (`true`) or deactivates (`false`) the Planning View in the Frame designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.PlanningView:boolean
```

**Assignment Value:** boolean.

**Example**

```
MyFrame._3D.PlanningView := true
```

**See also:** View Ribbon Tab > Use Planning View

## _3D.ShowBasePlate [SimTalk]

Shows (`true`) or hides the base plate (`false`) below the grid in the Frame designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowBasePlate:boolean
```

**Example**

```
MyFrame._3D.ShowBasePlate := false
```

**See also:** View Ribbon Tab > Show Base Plate

## _3D.ShowConnections [SimTalk]

Shows Connectors/Interfaces/Markers in the active Frame window designated by `<Path>` (`true`) or hides them (`false`).

**Remarks:** `_3D.ShowConnections` shows or hides material flow directions of the length-oriented objects for which you set `_3D.ShowMaterialFlowDirection` to `true`.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowConnections:boolean
```

**Example**

```
MyFrame._3D.ShowConnections := false
```

**See also:** View Ribbon Tab > Show Connections, Show Material Flow Direction [check box], `_3D.ShowMaterialFlowDirection [SimTalk]`, View Ribbon Tab > Show Material Flow Directions [button], `_3D.ShowMaterialFlowDirections [SimTalk]`

## _3D.ShowExternalGraphics [SimTalk]

Shows (`true`) or hides (`false`) external graphic groups of the Frame designated by `<Path>` inward, i.e. in 3D windows that opened the designated Frame.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowExternalGraphics:boolean
```

**Example**

```
MyFrame._3D.ShowExternalGraphics := false
```

**See also:** View Ribbon Tab > Show External Graphic Groups, External [graphic group]

## _3D.ShowGrid [SimTalk]

Shows (`true`) or hides (`false`) the grid in the Frame designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowGrid:boolean
```

**Example**

```
MyFrame._3D.ShowGrid := false
```

**See also:** View Ribbon Tab > Show Grid

## _3D.ShowLabels [SimTalk]

Shows (`true`) or hides (`false`) the labels of the objects in the Frame designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowLabels:boolean
```

**Example**

```
MyFrame._3D.ShowLabels := false
```

**See also:** View Ribbon Tab > Show Object Names

## _3D.ShowMaterialFlowDirections [SimTalk]

Shows (`true`) or hides (`false`) the material flow direction arrows of the length-oriented objects in the Frame designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowMaterialFlowDirections:boolean
```

**Example**

```
MyFrame._3D.ShowMaterialFlowDirections := true
```

**See also:** View Ribbon Tab > Show Material Flow Directions [button], View Ribbon Tab > Show Connections, Show Material Flow Direction [check box]

## _3D.ShowNames [SimTalk]

Shows (`true`) or hides (`false`) the names of the objects in the Frame designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowNames:boolean
```

**Example**

```
MyFrame._3D.ShowNames := false
```

**See also:** View Ribbon Tab > Show Object Names

## _3D.ShowPointClouds [SimTalk]

Shows (`true`) or hides (`false`) point clouds in the Frame designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowPointClouds:boolean
```

**Example**

```
MyFrame._3D.ShowPointClouds := false
```

**See also:** View Ribbon Tab > Show Point Clouds

## _3D.ShowShadows [SimTalk]

Shows (`true`) or hides (`false`) shadows in the Frame designated by `<Path>`.

**Remarks:** Plant Simulation only shows the shadows of the objects in a Frame. Captions, manipulators, path visualizations, and some display objects (e.g., Variable, Comment, etc.) do not throw a shadow most of the time.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowShadows:boolean
```

**Example**

```
MyFrame._3D.ShowShadows := false
```

**See also:** View Ribbon Tab > Show Shadows

## _3D.ShowSky [SimTalk]

Shows (`true`) or hides (`false`) the sky in the Frame designated by `<Path>`.

- **Type:** Attribute

**Syntax**

```
<Path>._3D.ShowSky:boolean
```

**Example**

```
MyFrame._3D.ShowSky := true
```

**See also:** View Ribbon Tab > Show Sky
