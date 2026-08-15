# XML Interface — Attributes

## General Description

To show the methods, read-only attributes, and attributes of a selected **Class** or **Instance**:

- Select **Show Attributes and Methods** on the context menu of the Class Library (for a Class).
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance (for an Instance).

You can set the value of an attribute and get its value, either with the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```
MyFileInterface.FileName := "C:\users\johnE\myData.txt"
```

- To get the value of an attribute, you might, for example, type:

```
print MyXMLInterface.Context
posit := Station.Cont.XPos
```

---

## Attributes

### Context [SimTalk]

Sets the context of the data of the XMLInterface designated by `<Path>` that you want to read.

- **Type:** Attribute
- **Syntax:** `<Path>.Context:string`
- **Assignment Value:** You can assign a value of data type string.

**Example:**

```
MyXMLInterface.Context := "Data/Objects"
```

**See also:** Context [text box], Context [SimTalk]

---

### FileName [SimTalk] — XML Interface

Sets the name of the XML file of the XMLInterface designated by `<Path>` that you want to read.

- **Type:** Attribute
- **Syntax:** `<Path>.FileName:string`
- **Assignment Value:** You can assign a value of data type string.

**Example:**

```
MyXMLInterface.FileName := "C:\users\johnE\myfile.xml"
```

**See also:** Filename [XMLInterface], FileName [SimTalk] — XML Interface

---

### ImportMethod [SimTalk]

Sets the name of the Method in which you programmed how to extract and to sequentially process the imported data for the XMLInterface designated by `<Path>`.

**Remarks:** The import method is called by the method `openRead` for all objects which are contained in the XML file.

- **Type:** Attribute
- **Syntax:** `<Path>.ImportMethod:object`
- **Assignment Value:** You can assign a value of data type object.

**Examples:**

```
MyXMLInterface.ImportMethod := &MyImportMethod
```

```
param Level: integer, LocalName: string, Value: string, AttrTbl: table
var row,size: integer
var nameStr,valueStr: string
var attrName,attrValue: string
// print ""
// print "Level: "+num_to_str(i)
// print "Local Name: "+localName
// print "Value: "+value
nameStr := localName
valueStr := value
size := attrTbl.Ydim
for row := 1 to attrTbl.Ydim
   // print "Attribute Name: "+attrTbl[1,row]
   // print "Attribute Value: "+attrTbl[2,row]
   attrName := attrTbl[1,row]
   attrValue := attrTbl[2,row]
next
numberCalls := numberCalls+1
```

**See also:** Import Method [XML Interface], openRead [SimTalk]

---

## Related Topics

- SimTalk
- openRead [SimTalk]
- User Interface Objects
- Display and User Interface Objects

Plant Simulation provides display objects to show the results of the simulation runs and user interface objects prompting input from the user of the simulation model.

---

*Source: Plant Simulation Help — © 2026 Siemens. Unpublished work.*
