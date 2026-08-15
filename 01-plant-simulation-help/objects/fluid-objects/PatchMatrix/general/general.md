# PatchMatrix

## Overview

Use the object **PatchMatrix** to connect an entrance pipe with an exit pipe to control the flow of fluid materials within the plant.

Pipes transport free-flowing materials between the objects `FluidSource`, `Tank`, `Mixer`, `Portioner`, `DePortioner`, and `FluidDrain`.

## Usage

1. Insert the objects you would like to model.
2. Connect the Pipes with Connectors to the PatchMatrix.
3. Double-click the PatchMatrix and change to the tab **Attributes**.
4. Click **Connections** and select the respective check boxes to allow materials to flow through these Pipes.
   - The column header contains the incoming pipes.
   - The row header contains the outgoing pipes.

To show a tooltip with information about the PatchMatrix, hover the mouse over it.

To change the length of the graphic and the anchor points of the object, click **Show Manipulators** on the Edit ribbon tab or press `M`.

### Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > Fluids > DePortioner** on the Home ribbon tab.

## Dialog Box of the PatchMatrix

Double-click the icon of the PatchMatrix to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M`.

## Tab Attributes

The tab **Attributes** provides the settings which the object offers, including the setting **Connections**.

## Connections [PatchMatrix]

Click this button to show the Pipes which are connected with the PatchMatrix.

**Remarks**

Select the check boxes in the respective cells to connect the respective Pipes with each other.

- The column header contains the incoming pipes.
- The row header contains the outgoing pipes.

In the example, the entrance pipe named `Pipe` is connected with the exit pipes `Pipe2` and `Pipe3`, and `Pipe1` is connected with `Pipe2`.

If you drag the mouse over the PatchMatrix, the tooltip shows this.

### SimTalk Methods

- `getConnectionsForPred [SimTalk]`
- `getConnectionsForSucc [SimTalk]`
- `resetConnections [SimTalk]`
- `setConnections [SimTalk]`

## Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

## Navigate Menu

The commands are described under the *Navigate Menu*.

## View Menu

The commands are described under the *View Menu*.

SimTalk method: `updateDialog [SimTalk]`

## Tools Menu

The commands are described under the *Tools Menu*.

## Help Menu

The commands are described under the *Help Menu*.

## Methods of the PatchMatrix

The PatchMatrix provides:

- The methods listed in the table of contents.
- The *Methods of the Fluid Objects*.
- The *Methods of All Objects*.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the `F8` key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the methods, read-only attributes, and attributes of the selected Instance.

---

## RecoveryTime [SimTalk] - DePortioner

Sets the duration of the **Recovery Time** of the DePortioner designated by `<Path>`.

**Remarks**

The Recovery Time is the time required to flush and clean the DePortioner and prepare it for the next process. This is the time during which no material will be accepted after the MU exited the object.

**Type**: Attribute

**Syntax**

```
<Path>.RecoveryTime:time
```

**Assignment Value**

You can assign a value of data type `time`. Specify `0` to allow materials to enter continually.

**Example**

```simtalk
MyDePortioner.RecoveryTime := 1:00:00
```

**See also**

- `RecoveryTime [SimTalk] - Mixer`
