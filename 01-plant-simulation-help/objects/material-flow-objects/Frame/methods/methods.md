# Methods of the Frame

The Frame provides:

- The methods listed below.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show them for the selected Instance.

## Reading a Syntax Line

An example of a syntax line:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature lists the identifier and data type of each parameter in parentheses. For example, `(Parameter:string)` designates a parameter of data type string. Instead of a constant value, you can use a variable of the required type or a method that returns the required data type.
- **Note:** Enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.
- Optional parameters are listed within brackets. `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows it after the parameter, e.g. `:= false`.
- If the method has a return value, the signature shows its data type after the arrow `->`, e.g. `→ boolean`.

---

## getHTMLCode [SimTalk] - Frame

Returns the contents of the Frame designated by `<Path>` as HTML code of a pixel-based graphic and assigns it to the passed parameters.

**Type:** Method

**Syntax**

```
<Path>.getHTMLCode([Caption:string, Width:integer, Height:integer,
SizeInPercent:string, CameraPositionX:real, CameraPositionY:real,
CameraPositionZ:real, CameraRotationX:real, CameraRotationZ:real,
CameraRotationX:real, CameraRotationZ:real]) → string
```

**Parameters**

- `Caption` (string, optional): desired caption of the graphic. If specified, Plant Simulation shows the graphic with this caption.
- `Width` (integer, optional): desired width of the graphic. If Width and Height are not specified, Plant Simulation uses the width/height of the 2D or 3D view in which all objects contained in the Frame are visible.
- `Height` (integer, optional): desired height of the graphic.
- `SizeInPercent` (string, optional): desired size of the graphic in percent, e.g. `"75%"`. You can specify the percentage instead of Width and Height.
- `CameraPositionX` (real, optional): x-axis of the camera position.
- `CameraPositionY` (real, optional): y-axis of the camera position.
- `CameraPositionZ` (real, optional): z-axis of the camera position.
  - You only have to specify the CameraPosition parameters if you also specify the CameraRotation parameters.
- `CameraRotationX` (real, optional): rotation of the camera around the x-axis.
- `CameraRotationZ` (real, optional): rotation of the camera around the z-axis.

You can also use the CameraRotation parameters without specifying the CameraPosition.

If you specify the CameraPosition and/or CameraRotation parameters, you also have to specify the Width and Height or the SizeInPercent.

**Return Value**

The return value has the data type string.

**Examples**

```simtalk
print MyFrame.getHTMLCode
MyFrame.getHTMLCode("Caption")
MyFrame.getHTMLCode(100, 100) // size in mm
MyFrame.getHTMLCode("Caption", 100, 100) // caption and size in mm
MyFrame.getHTMLCode("75%")
// size in percent of the graphic showing all objects
MyFrame.getHTMLCode(*)
// as big as necessary to show all objects and shown as big as possible in
the HtmlReport
MyFrame.getHTMLCode(100,*)
// width in mm, height proportional calculated from the size required to
show all objects
MyFrame.getHTMLCode(*, 100)
// height in mm, width proportional calculated from the size required to
show all objects
MyFrame.getHTMLCode(100%, -1.123, 2.345, -3.456, -45.0, 15.0)
// 100% of the size of the graphic showing all objects while specifying
CameraPosition and CameraRotation
```

**See also:** Display a Frame, Display a HtmlReport

---

## node [SimTalk] - Frame

Returns the designated object in the Frame designated by `<Path>`.

**Remarks:** Plant Simulation numbers the objects within models in the order in which you insert them. You can also call the method for the Class Library.

**Type:** Method

**Syntax**

```
<Path>.node(ObjectNumberOrName:integer/string) → object
```

**Parameter**

- `ObjectNumberOrName` (integer): designates the number of the object.
- `ObjectNumberOrName` (string): designates the name of the object. If a string is passed, the method returns the object with that name. If no such object exists, it returns void.

**Return Value**

The return value has the data type object.

**Examples**

```simtalk
print .model.node(3)
// might, for example, return .Models.MyPlant.MyStation
```

```simtalk
// Writes all objects in the Frame and in Sub-frames to the DataTable.
// Assign the data type object to the first column.
param Frame: object := void
if Frame = VOID
   Frame := current
end
for var i := 1 to Frame.numNodes
   DataTable[1, DataTable.yDim + 1] := Frame.Node(i)     // object
   DataTable [2, DataTable.yDim] := Frame.Node(i).Name   // string
   if Frame.Node(i).InternalClassType = "Frame"          // substructure
        self.execute(Frame.Node(i))                      // recursive call
   end
next
```

**See also:** node [SimTalk] - folder, NumNodes [SimTalk] - Frame

---

## pasteClipboard [SimTalk] - Frame

Pastes the contents of the clipboard into the Frame designated by `<Path>`.

**Type:** Method

**Syntax**

```
<Path>.pasteClipboard([TargetTable:table])
```

**Parameter**

- `TargetTable` (table, optional): writes all pasted objects to the specified table after the method executed. The table has one column of data type object.

**Example**

```simtalk
var tbl: table
var   i: integer
pasteClipboard(tbl)
for var i := 1 to tbl.yDim
   print tbl[1,i]  // outputs all pasted objects
next
```

**SimTalk:** copyObjectsToClipboard [SimTalk]

**See also:** Paste Contents of the Clipboard [Home ribbon], Copy [Home ribbon]

---

## statistics [SimTalk] - Frame

Returns the statistics of all material flow objects collecting statistical data of the Frame designated by `<Path>`.

**Remarks:** Also applies for objects on lower levels of the model, i.e., models within models.

**Type:** Method

**Syntax**

```
<Path>.statistics
<Path>.statistics(NameOfTable:table_path)
<Path>.statistics(FileName:string[, CodePage:string:="UTF-8"])
```

**Parameters**

- `NameOfTable` (table_path): write the data to that table.
- `FileName` (string): write the table to that file. Plant Simulation will overwrite existing entries.
- `CodePage` (string, optional): set the encoding you want to use: ANSI, UTF-8, or Unicode.

**Default Value of the Parameter**

If you do not specify the CodePage parameter, the encoding UTF-8 is used as the default value.

**Example**

```simtalk
building12.statistics                             // outputs to the screen
.plant.statistics(stat_tab)                       // outputs to a table
MySubFrame.statistics("C:\temp\statistics1.txt")  // outputs to a file
```

---

# Read-Only Attributes of the Frame

The Frame provides:

- The read-only attributes listed in the table of contents.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of read-only attributes, but you cannot set them — Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all methods, read-only attributes, and attributes, open the window **Show Attributes and Methods** (via the Class Library context menu for a Class, or F8 / the Home ribbon tab for an Instance).

To query the value of a read-only attribute:

```simtalk
print .Models.Model.Capacity
```
