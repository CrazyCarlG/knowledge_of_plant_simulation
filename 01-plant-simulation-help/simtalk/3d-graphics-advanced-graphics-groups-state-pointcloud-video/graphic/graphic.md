# Graphic Groups — SimTalk Reference

SimTalk provides methods, attributes, and read-only attributes for accessing **graphic groups**. You can view and access them by clicking **Auto Complete** on the Edit ribbon tab of the Method Editor.

## Methods

### `ungroupGraphic [SimTalk]`

Ungroups the designated group of graphics of the graphic designated by `<Path>`.

**Remarks**

- Assigning the method deactivates graphic inheritance.
- You cannot assign the method if the graphic is an automatically generated graphic group, or if the graphic is located in an automatically generated graphic group.

**Syntax**

```
<Path>.ungroupGraphic
```

**Type:** Method

**Examples**

```simtalk
MyFrame._3D.getGraphic("default", [1,2,3]).ungroupGraphic
MyFrame._3D.getGraphic("deco", [1,2,3]).ungroupGraphic
```

**See also:** Ungroup Group of Graphics, `groupGraphics [SimTalk]`, `_3D.getGraphic [SimTalk]`, Accessing Methods of Graphic Groups

---

### `_3D.addGraphicGroup [SimTalk]`

Adds the specified graphic group to the object designated by `<Path>`.

**Remarks:** Assigning the method deactivates graphic inheritance.

**Syntax**

```
<Path>._3D.addGraphicGroup(GraphicGroupName:string, Visible:boolean[,
Internal:boolean:=false, Locked:boolean:=false])
```

**Parameters**

- `GraphicGroupName` (string) — designates the name of the graphic group.
- `Visible` (boolean) — sets if the graphic group will be visible (`true`) or not visible (`false`).
- `Internal` (boolean, optional, default `false`) — sets if the graphic group will be internal (`true`) or external (`false`).
- `Locked` (boolean, optional, default `false`) — sets if the graphic group will be locked (`true`) or not (`false`).

**Type:** Method

**Example**

```simtalk
MyStation._3D.addGraphicGroup("MyGraphicGroup", true, true, false)
// new source code, is the same as the source code below
var graphicgroup := _3D.addGraphicGroup("MyGraphic", true, false)
// previous source code
_3D.addGraphicGroup("MyGraphic", true, false)
var graphicgroup := _3D.getGraphic("MyGraphic")
```

**See also:** `_3D.deleteGraphicGroup [SimTalk]`, Edit 3D Properties [dialog] > Graphics [tab] > Add [graphic group]

---

### `_3D.deleteGraphicGroup [SimTalk]`

Deletes the specified graphic group from the object designated by `<Path>`.

**Remarks:** Assigning the method deactivates graphic inheritance.

**Syntax**

```
<Path>._3D.deleteGraphicGroup(GraphicGroupName:string) → string
```

**Parameter:** `GraphicGroupName` (string) — designates the name of the graphic group.

**Return Value:** data type `string`.

**Type:** Method

**Example**

```simtalk
MyStation._3D.deleteGraphicGroup("MyGraphicGroup")
```

**See also:** `_3D.addGraphicGroup [SimTalk]`, Edit 3D Properties [dialog] > Graphics [tab] > Delete [button] - graphic group

---

### `_3D.deleteGraphicGroupContent [SimTalk]`

Deletes the graphics from the specified graphic group from the object designated by `<Path>`.

**Remarks:** Assigning the method deactivates graphic inheritance.

**Syntax**

```
<Path>._3D.deleteGraphicGroupContent([GraphicGroupName:string])
```

**Parameter**

- `GraphicGroupName` (string, optional) — designates the name of the graphic group.
- Do not specify the name to delete the content of the default graphic group.
- If you try to delete the content of an automatically generated default graphic group, this attempt will fail without an error message.
- Specify a name to open the Method Debugger.

**Type:** Method

**Example**

```simtalk
MyFrame._3D.deleteGraphicGroupContent("deco")
```

**See also:** Auto Complete, `_3D.deleteGraphicGroupContent [SimTalk]`, Edit 3D Properties [dialog] > Graphics [tab] > Graphic Groups [described]

---

## Attributes

### `_3D.ExternalGraphicGroups [SimTalk]`

Sets the list of all external graphic groups of the Frame designated by `<Path>`.

**Remarks:** Visible external graphic groups are shown in 3D windows that opened a Frame which contains the designated Frame that owns these graphic groups.

**Note:** Assigning the attribute deactivates graphic inheritance of the Frame designated by `<Path>`.

**Syntax**

```
<Path>._3D.ExternalGraphicGroups:string[]
```

**Assignment Value:** You can assign an array of data type `string`.

**Type:** Attribute

**Example**

```simtalk
.Models.Model._3D.ExternalGraphicGroups := ["default", "alternative"]
var a : string[] := .Models.Model._3D.ExternalGraphicGroups
```

**See also:** Internal [graphic group], Internal [SimTalk] - graphic group, External [graphic group], External [SimTalk] - graphic group, Visible [graphic group], Visible [SimTalk] - graphic group, `_3D.InternalGraphicGroups [SimTalk]`, `_3D.VisibleGraphicGroups [SimTalk]`

---

### `_3D.GraphicGroupNames [SimTalk]`

Returns a list of all graphic groups that exist for the object designated by `<Path>`.

**Syntax**

```
<Path>._3D.GraphicGroupNames → string[]
```

**Return Value:** An array of data type `string`.

**Type:** Read-only attribute

**Example**

```simtalk
print .Models.MyEnginePlant.Station._3D.GraphicGroupNames
// might, for example, return [default, mygraphicgroup1, MyGraphicGroup2]
```

**See also:** Edit 3D Properties [dialog] > Graphics [tab] > Graphic Groups [described]

---

### `_3D.InternalGraphicGroups [SimTalk]`

Sets the list of all internal graphic groups of the Frame designated by `<Path>`.

**Remarks:** Visible internal graphic groups are shown in 3D windows that opened the designated Frame that owns these graphic groups.

**Note:** Assigning the attribute deactivates graphic inheritance of the Frame designated by `<Path>`.

**Syntax**

```
<Path>._3D.InternalGraphicGroups:string[]
```

**Assignment Value:** You can assign an array of data type `string`.

**Type:** Attribute

**Example**

```simtalk
.Models.Model._3D.InternalGraphicGroups := ["deco1", deco2"]
var a : string[] := .Models.Model._3D.InternalGraphicGroups
```

**See also:** Internal [graphic group], Internal [SimTalk] - graphic group, External [graphic group], External [SimTalk] - graphic group, Visible [graphic group], Visible [SimTalk] - graphic group, `_3D.ExternalGraphicGroups [SimTalk]`, `_3D.VisibleGraphicGroups [SimTalk]`

---

### `_3D.LockedGraphicGroups [SimTalk]`

Sets the list of all locked graphic groups of the object designated by `<Path>`.

**Remarks:** Locking graphic groups prevents you from selecting this graphic group in the 3D windows which are opened for this object. This makes, for example, sense for the graphic of a factory building which might otherwise be selected inadvertently.

**Note:** Assigning the attribute deactivates graphic inheritance.

**Syntax**

```
<Path>._3D.LockedGraphicGroups:string[]
```

**Assignment Value:** You can assign an array of data type `string`.

**Type:** Attribute

**Example**

```simtalk
.Models.Model.Station1._3D.LockedGraphicGroups := ["Group1, Group2"]
var a: string[] := .Models.Model.Station1._3D.LockedGraphicGroups
```

**See also:** Locked [graphic group], `_3D.InternalGraphicGroups [SimTalk]`, Locked [SimTalk] - graphic group, `_3D.VisibleGraphicGroups [SimTalk]`

---

### `_3D.VisibleGraphicGroups [SimTalk]`

Sets the graphic groups of the object designated by `<Path>` that will be visible.

**Remarks:** Not visible graphic groups are not shown in any 3D window. This makes, for example, sense for objects that you want to visualize in different development stages. The setting Visible allows you to select one or more of multiple graphic groups for the current representation of the object.

**Note:** Assigning the attribute deactivates inheritance of the setting Visible of all graphic groups of the designated Frame.

**Syntax**

```
<Path>._3D.VisibleGraphicGroups:string[]
```

**Assignment Value:** You can assign an array of data type `string`.

**Type:** Attribute

**Example**

```simtalk
MyStation._3D.VisibleGraphicGroups := ["default", "deco"]
```

**See also:** Internal [graphic group], Internal [SimTalk] - graphic group, External [graphic group], External [SimTalk] - graphic group, Visible [graphic group], Visible [SimTalk] - graphic group

---

## Graphic Group Properties

### `External [SimTalk] - graphic group`

Sets if the graphic group designated by `<Path>` is to represent its owning Frame toward the outside (`true`) or not (`false`).

**Remarks**

- Plant Simulation shows an external graphic group in 3D windows that opened an object which contains the Frame which owns the graphic group, but only if the graphic group is set to Visible at the same time.
- Plant Simulation also shows a visible external graphic group, even if it is not internal at the same time, in 3D windows that opened the Frame which owns the graphic group and shows external graphic groups marked as Visible.

**Note:** Assigning the attribute deactivates graphic inheritance of the owning Frame.

**Syntax**

```
<Path>.External:boolean
```

**Assignment Value:** You can assign a value of data type `boolean`.

**Type:** Attribute

**Example**

```simtalk
print _3D.getGraphic("MyGraphicGroup").External
_3D.getGraphic("MyGraphicGroup").External := true
```

**See also:** Visible [SimTalk] - graphic group, Graphic Groups [described], `_3D.getGraphic [SimTalk]`, Show External Graphic Groups

---

### `Generated [SimTalk] - graphic group`

Returns if the graphics of the graphic group designated by `<Path>` are generated automatically or not.

**Remarks:** If the graphic group is generated, you can neither add graphics to it nor delete graphics from it. You can edit its visibility settings though.

**Syntax**

```
<Path>.Generated:boolean
```

**Return Value:** data type `boolean`.

**Type:** Read-only attribute

**Example**

```simtalk
print Station._3D.getGraphic("MyGraphicGroup").Generated
```

**See also:** Graphic Groups [described], `_3D.getGraphic [SimTalk]`

---

### `Internal [SimTalk] - graphic group`

Sets if the graphic group designated by `<Path>` is to decorate its owning Frame inward (`true`) or not (`false`).

**Remarks:** Plant Simulation shows an internal graphic group in 3D windows that opened the Frame, which owns the graphic group, but only if the graphic group is set to Visible at the same time.

**Note:** Assigning the attribute deactivates graphic inheritance of the owning Frame.

**Syntax**

```
<Path>.Internal:boolean
```

**Assignment Value:** You can assign a value of data type `boolean`.

**Type:** Attribute

**Example**

```simtalk
print _3D.getGraphic("MyGraphicGroup").Internal
_3D.getGraphic("MyGraphicGroup").Internal := true
```

**See also:** Visible [SimTalk] - graphic group, Graphic Groups [described], `_3D.getGraphic [SimTalk]`, Show External Graphic Groups

---

### `Locked [SimTalk] - graphic group`

Sets if the graphic group designated by `<Path>` is locked (`true`) or not (`false`).

**Remarks:** Locking a graphic group prevents you from selecting this graphic group in the 3D windows which are opened for this object. This makes, for example, sense for the graphic of a factory building which might otherwise be selected inadvertently.

**Syntax**

```
<Path>.Locked:boolean
```

**Assignment Value:** You can assign a value of data type `boolean`.

**Type:** Attribute

**Example**

```simtalk
print Station._3D.getGraphic("MyGraphicGroup").Locked
Station._3D.getGraphic("MyGraphicGroup").Locked := false
```

**See also:** Graphic Groups [described], `_3D.getGraphic [SimTalk]`

---

### `Visible [SimTalk] - graphic group`

Sets if the graphic group designated by `<Path>` is visible (`true`) or not (`false`).

**Remarks:** Plant Simulation does not show a not visible graphic group in any 3D window. This makes, for example, sense for objects that you want to visualize in different development stages. The setting Visible allows to select one or more of multiple graphic groups for the current representation of the object.

**Note:** Assigning the attribute Visible deactivates inheritance of the visible setting of all graphic groups of the owning object.

**Syntax**

```
<Path>.Visible:boolean
```

**Assignment Value:** You can assign a value of data type `boolean`.

**Type:** Attribute

**Example**

```simtalk
print Station._3D.getGraphic("MyGraphicGroup").Visible
Station._3D.getGraphic("MyGraphicGroup").Visible := false
```

**See also:** Graphic Groups [described], Visible [graphic group], Visible [context menu], `_3D.getGraphic [SimTalk]`
