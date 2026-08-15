# Marker

Use the object **Marker** for setting waypoints in your simulation model along which the Automated Guided Vehicle (AGV) drives from the AGVPool to its destination.

## Description

With the setting **Default Curve Radius** / `DefaultCurveRadius` you can set the size of the roundings at the Markers. A Default Curve Radius of `0` makes the AGV rotate on the spot instead of driving a curve.

> **Note:** When you insert Markers into your model, make sure that the Markers are aligned. This prevents Plant Simulation from computing unnecessary roundings between the Markers. Misaligned Markers might occur if you inserted Markers into your model while *Show Grid* was off.

> **Note:** If a standing Transporter cannot drive to the first Marker using the specified Default Curve Radius, the Transporter rotates on the spot, if possible, and then drives in a straight line toward the Marker.

The Marker can be **directional** or **omnidirectional**. You can switch between these two states with the check box **Use Rotation of Marker**.

> **Note:** To show or hide a Marker, click **Show Connections**.

### Add the Object to the Simulation Model

To add the object Marker to your simulation model, click **Manage Class Library > Basic Objects > Resources > Marker** on the Home ribbon tab.

## Directional and Omnidirectional Markers

The Markers in your simulation model can be directional or omnidirectional. You can switch between these two states with the check box **Use Rotation of Marker**.

- The AGV does **not** drive through an inserted omnidirectional Marker but turns in front of the inserted Marker toward the next Marker.
- The AGV can drive through directional Markers in both directions. For selecting the direction, Plant Simulation uses the position of the previous Marker in the sequence of Markers.

Plant Simulation computes the route by means of a Marker with a 90-degree angle as follows:

- If the previous Marker is located above the Marker with the 90-degree angle, the AGV drives through the Marker from top to bottom.
- If the previous Marker is located below the Marker with the 90-degree angle, the AGV drives through the Marker from bottom to top.
- If the previous Marker is located exactly at the height of the Marker with the 90-degree angle, Plant Simulation evaluates the current direction of the AGV:
  - If the front of the AGV points up, the AGV drives through the Marker from top to bottom.
  - If the front of the AGV points down, the AGV drives through the Marker from bottom to top.
  - If the front of the AGV points exactly to the center of the Marker, the AGV drives through the Marker from top to bottom.

For Markers with other angles, Plant Simulation proceeds accordingly.

For a directional Marker with the default angle of `0°`, the AGV drives through the markers and then turns on the marker around the angle you set in the direction of the next marker.

For a directional Marker with an angle other than the default, the AGV drives toward the Marker at the angle you entered, crosses it, and leaves it at the designated angle.

## Dialog Box of the Marker

Double-click the icon of the Marker to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Tab Attributes

The tab **Attributes** provides the settings that the object offers. The shared properties are described under *Tab Attributes*.

### Use Rotation of Marker [check box]

To make the AGV use the rotation of the Marker on its way to its destination, select this check box.

Select the check box to make the AGV drive across the Marker and rotate on the Marker with the defined angle in the direction of the next Marker. You can set the rotation angle in the dialog *Edit 3D Properties* of the Marker on the tab **Transformation** under *Settings for the Rotation*.

Clear the check box to make the AGV not drive across the inserted Markers but rotate in front of the Marker toward the next Marker (omnidirectional).

**SimTalk:** `UseRotationOfMarker [SimTalk]`

### Arrival Control [Marker]

Modifies the built-in behavior of the object. The object calls the Arrival Control as soon as the Transporter driving freely within the area arrives at the Marker. In the Arrival Control you can program actions that you want to take when an AGV arrives at the Marker or is closest to the Marker. You might provide your fleet management software with feedback about the position of the AGV.

For an omnidirectional Marker, Plant Simulation executes the control once the Transporter driving freely within the area arrives at the half-way point of the curvature/fillet at the Marker. If you did not enter a Method, the value of the control is `VOID`.

**Select the Path to an Existing Method:** Click the ellipsis button, navigate to the location of the Method in the dialog *Select Object [for controls]*, and click OK.

**Create a Control That is a Method of the Object:**

- Type a meaningful name into the text box and select **Create Control** on the context menu. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

To edit the source code later: press `F2`, or hold `Shift` and double-click into the text box, or select **Open Object** on the context menu, or click the tab **User-defined** and double-click the name of the Method in the list. To delete this control, delete the user-defined attribute.

**SimTalk:** `ArrivalCtrl [SimTalk]`

## Tab User-defined

Define your own attributes as described under *Tab User-defined*.

## Menus

- **Navigate Menu:** commands described under *Navigate Menu*.
- **View Menu:** `Refresh`, `Show Attributes and Methods`. **SimTalk:** `updateDialog [SimTalk]`.
- **Tools Menu:** `Edit Controls`, `Edit Observers`.
- **Help Menu:** commands described under *Help Menu*.

## Methods of the Marker

The Marker provides the **Methods of All Objects**.

To view all of the methods, read-only attributes, and attributes of the object, open the window *Show Attributes and Methods*:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press `F8` or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show them for the selected Instance.

An example of the Syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## Amount [SimTalk] — AGVPool

Sets the amount of AGVs which the AGVPool designated by `<Path>` creates. Plant Simulation creates the specified Amount of AGVs during the init phase of the simulation run.

**Type:** Attribute

**Syntax:**

```
<Path>.Amount:integer
```

**Assignment Value:** You can assign a value of data type `integer`.

**Example:**

```simtalk
MyAGVPool.Amount := 2
```

## See also

- Amount [text box] - AGVPool
- AGV [SimTalk]
- Directional and Omnidirectional Markers
- Dialog Box of the Marker
- Model an Automated Guided Vehicle System (AGVS)
- Select Object [for controls]
- Model an Automated Guided Vehicle System (AGVS) > Cover a Route Along Omnidirectional Markers
- Model an Automated Guided Vehicle System (AGVS) > Cover a Route Along Directional Markers
