# Connector

Use the object **Connector** for establishing material flow connections between objects along which the parts move through the installation.

## Description

- You cannot change the name of the Connector.
- The Connector connects the material flow objects or the fluid objects on which the MUs move.
- It also connects an object with an exit or entrance — modeled with the **Interface** — of a Frame when you modeled hierarchically (i.e., when you nest Frames within Frames).
- The Connector shows the direction of the connection with an arrowhead in the middle of the connecting line.
- To show the predecessors and the successors of an object in a tooltip, drag the mouse over the respective Connector.
- To show the source and the target of the Connector in the Frame as a tooltip, drag the mouse over the Connector.

## Showing Connections / Anchor Point of the Connector

- You can only establish a single connection between two objects.
- To reorder the sequence of the successors of the selected object, right-click the object in the Frame and select **Reorder Successors** on the context menu.
- You can also reorder the connections by clicking **Show Manipulators** on the Edit ribbon tab.
- With the manipulators of the start and end anchor points you can change the predecessor or the successor respectively of the Connector and attach it to another object. Drag the start or end anchor point from the current object to another object of your choice.
- If you did not select anything in the scene, the command also shows the position manipulators of the Connectors in the scene if Connectors are shown in the scene.
- You can edit the anchor points with the position manipulator, including the start and the end anchor point.
- Plant Simulation shows the start and end anchor point of the Connectors cut in half. This clearly separates Connectors without a length of their own and allows to easily select each of the Connectors.

## Add the Object to the Simulation Model

To add the object Connector to your simulation model, click **Manage Class Library > Basic Objects > MaterialFlow > Connector** on the Home ribbon tab.

## Dialog Box of the Connector

Double-click the Connector, which you inserted into a Frame, to open its dialog box.

### Tab Attributes

The tab **Attributes** provides the settings, which the object offers.

#### Width [text box]

Type in the line Width of the Connector.

**Remarks**

The Width can be a real number between `-1` and `100`.

- The value `1` stands for a line weight of 1 pixel in a Frame window with a zoom factor of 100 %.
- The value `0` stands for a Connector width of 1 pixel no matter if the Frame window is zoomed or not.
- The value `-1` makes the Connector invisible.

```
Width -1   Width 0   Width 1   Width 5
```

The Width is a value of data type `real`. For 3D Only models you can reduce the default width, which corresponds to `0` or `1`, with values between `0` and `1`, to a fraction of that.

**SimTalk**

```
Width [SimTalk] - Connector
```

#### Color

To set the color of the Connector, click the field next to Color.

**Remarks**

You can select one of the predefined colors or you can click More Colors and click the Select button to select a color in the color matrix. Then click OK. Plant Simulation shows this color next to More Colors and uses it as the active color.

**SimTalk**

```
Color [SimTalk] - Connector
```

### Tab User-defined

Define your own attributes as described under the Tab User-defined.

## Navigate Menu

The commands are described under the Navigate Menu.

## View Menu

The View Menu provides commands to access its functions.

- Refresh [on View menu]
- Show Attributes and Methods [on View menu]

**SimTalk**

```
updateDialog [SimTalk]
```

## Tools Menu

The Tools Menu provides these menu commands:

- Edit Controls
- Edit Observers

## Help Menu

The commands are described under the Help Menu.

## Methods of the Connector

The Connector provides:

- The methods listed in the table of contents to the left.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

You can:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the F8 key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

## See Also

- Dialog Box of the Connector
- Connect Objects with the Connector
- Navigate Menu
- View Menu
- Tab User-defined
