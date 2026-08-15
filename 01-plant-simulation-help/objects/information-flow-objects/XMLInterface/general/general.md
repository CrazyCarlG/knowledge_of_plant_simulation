# XMLInterface — General

## Overview

With the XMLInterface you can:

- Read and Write Data Sequentially
- Read and Access Data Randomly
- Access and Traverse Data Randomly

You can then use the data, which the XMLInterface read, and which you manipulated with a Method, to run a simulation in Plant Simulation. You might afterward use the methods `write` and `writeElement` to write the simulation results back to an XML file and continue working with these simulation results in Process Designer or another program.

> **Note:** Working with the XMLInterface requires that you are familiar with XPath (XML Path Language) source code.

To show a tooltip with information about the XMLInterface, hover with the mouse over it.

To change the length of the graphic and the anchor points of the XMLInterface, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Add the Object to the Simulation Model

To add the object XMLInterface to your simulation model, click **Manage Class Library > Basic Objects > InformationFlow > XMLInterface** on the Home ribbon tab.

## Dialog Box of the XMLInterface

Double-click the icon of the XMLInterface to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Tab Attributes

The tab *Attributes* provides the settings which the object offers. The settings are listed in the table of contents to the left. The shared properties are described under the *Tab Attributes*.

### Filename [XMLInterface]

Click the folder icon and select the name of the XML file which you want to access or which you want to save.

**SimTalk:** `FileName`, `openRead`

### Context [text box]

Type in the context of the data you want to import. The context designates the node of the structure of the XML document at which the XMLInterface starts reading data.

**Remarks:**

You might, for example, type in the names of certain data, or of certain objects that you are interested in, for example `Data/Objects`.

This way you can restrict the data to be read, i.e., if you do not need to work with all of the data contained in the XML file, you will specify a context.

If you do not type in a context, the XMLInterface imports the entire file, which may contain a large amount of data, some of which you do not need. This might take some time to import and use up a large amount of your computer's RAM.

**SimTalk:** `Context`, `setContext`

### Import Method [XML Interface]

Modifies the built-in behavior of the object. The Import Method is called by the method `openRead` for all objects, which are contained in the XML file. The Import Method controls how to extract and to sequentially process the imported data.

#### Select the Path to an Existing Method

Click the ellipsis button. Navigate to the location of the Method in the dialog *Select Object [for controls]* and click OK. This inserts the name of the Method into the text box of the Control.

Press `F2` in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

#### Create a Control That is a Method of the Object

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press `F2`.
- Or hold down `Shift` and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab *User-defined* and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

The standard import method as a user-defined attribute looks like this:

```simtalk
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

You might, for example, execute a callback method.

After the Method has processed the data, you can sequentially write it back out with the method `writeElement`.

**SimTalk:** `ImportMethod`, `openRead`, `addAttribute`, `endElement`, `openWrite`, `startElement`, `writeElement`

### Delete File [XML Interface]

To delete the XML file whose name is contained in the text box *Filename*, click this button.

**SimTalk:** `remove`

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

## Navigate Menu

The commands are described under the *Navigate Menu*.

## View Menu

The *View Menu* provides the commands listed in the table of contents to the left.

**SimTalk:** `updateDialog`

## Tools Menu

The *Tools Menu* provides commands to access its functions:

- Edit Controls
- Edit Observers

## Help Menu

The commands are described under the *Help Menu*.

## Methods of the XML Interface

The XML Interface provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window *Show Attributes and Methods*.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected *Class [general description]*.
- Press the `F8` key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected *Instance [general description]*.
