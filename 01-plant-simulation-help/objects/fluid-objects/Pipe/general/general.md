# Pipe

Use the object **Pipe** to transport free-flowing materials between the other fluid objects in the plant.

## Description

Insert Pipes to transport free-flowing materials between the objects `FluidSource`, `Tank`, `Mixer`, `Portioner`, `DePortioner`, and `FluidDrain`.

While material flows through the Pipe, it shows the color of that material as its color. This is the color selected for the material in the `MaterialsTable`. Establish connections between Pipes and fluid objects with the **Connector**. To make materials flow between the fluid objects, you must use Pipes.

You can insert the Pipe into a Frame:

- As a curved object (the default setting).
- By inserting any sequence of curved segments and straight segments to realistically model curved conveyor systems.

Select different configurations for the Pipe on the tab **Appearance**. Hover over the Pipe to show a tooltip with information.

## Show Manipulators

To change the length of the graphic and the anchor points of the object, click **Show Manipulators** on the Edit ribbon tab or press **M**.

The manipulator at the start and at the end of the length-oriented object is cut off. When you attach an object of the same type to the other object, the two combined halves result in a complete manipulator again. The height of the manipulators of the Pipe goes by the width of the Pipe.

## Add the Object to the Simulation Model

To add the object Pipe to your simulation model, click **Manage Class Library > Basic Objects > Fluids > Pipe** on the Home ribbon tab.

Compare the sample models: click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**, then select the respective Category, Topic, and Example in the dialog Examples Collection, and click **Open Model**.

## Dialog Box of the Pipe

Double-click the icon of the Pipe to open its dialog box.

- **Edit Simulation Properties**: change the simulation properties in the dialog box (shared properties under Dialog Items of the Objects).
- **Edit Animation Properties**: click **Edit 3D Properties** in the lower left corner of the simulation properties dialog box, or select the object and press the spacebar.

## Tab Attributes

The tab Attributes provides the settings the object offers.

### Outflow Rate [Pipe]

Type the Outflow Rate with which the material flows out of the Pipe to the next object. The default value `-1` denotes that the Pipe uses the same outflow rate as its predecessor.

The Outflow Rate is the amount of liters of the material that flows off in a second. This applies to a Pipe located directly after a `FluidSource`, `DePortioner`, `Tank`, or `Mixer`.

If you enter another value than the default, Plant Simulation uses the entered Outflow Rate even if it is higher than the Outflow Rate of the predecessor. This enables the effect that not all succeeding Pipes connected to a FluidSource, Tank, DePortioner, or Mixer must have the same Outflow Rate.

If the predecessor of the Pipe is another Pipe, Plant Simulation ignores the value (the text box is unavailable). This does not apply if the Pipe has a single successor and the predecessor Pipe has a single successor as well — if several Pipes are arranged one behind the other, Plant Simulation uses the lowest specified value for all Pipes.

SimTalk: `OutflowRate [SimTalk] - Pipe`

### Pipe Opened [check box]

Select this check box to open the entrance of the Pipe so materials can flow through it. Clear it to close the Pipe. With an opened Pipe you can model a valve or a gate valve. If you clear Pipe Opened, it shows the state **Pipe Closed** in cyan.

SimTalk: `PipeOpened [SimTalk]`

### Exit Strategy

Select the Exit Strategy according to which the Pipe distributes the flow rate to the succeeding fluid objects:

- **Evenly distributed** — distribute the flow rate evenly among succeeding objects.
- **Percentage [Pipe]** — distribute the flow rate proportionally.

Note: To show the items belonging to the new strategy, click **Apply** after selecting another strategy.

**Percentage [Pipe]** remarks:

- Click **Open List** and type the percentages for the individual succeeding objects. In the example, successor 1 receives 20%, successor 2 receives 30%, etc.
- Type `0` into the cell of a successor to prevent it from receiving material.
- If a successor cannot receive material (e.g. a succeeding Tank is full), the Pipe distributes that successor's portion according to the percentages to the remaining successors.
- The sum of the percentages does not have to add up to 100%. The actual sum of the percentages of all successors that can receive material corresponds to 100%. The percentages `[40, 60]`, `[0.4, 0.6]`, and `[2, 3]` are equivalent.

SimTalk:

- `ExitStrategy [SimTalk] - Pipe`
- `ExitStrategyPercentageValues [SimTalk] - Pipe`

### Current Material [Pipe]

Shows the name of the material that currently flows through the Pipe.

Note: The name is not case-sensitive, just like the names of attributes and methods. In SimTalk you can compare strings case-insensitively with the `~=` operator. The Pipe shows the current material with the color assigned to the material.

SimTalk: `CurrentMaterial [SimTalk] - Pipe`

### Current Flow Rate [text box]

Shows the Current Flow Rate of the materials flowing through the Pipe (liters per second).

SimTalk: `CurrentFlowrate [SimTalk]`

## Tab Times

Define Times as described under the Tab Times. Select a distribution from the drop-down list and type the required values. You can also select a constant time (Const). You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr [SimTalk]`.

See also: Set-up Time [general description], `SetupTime [SimTalk] - fluid objects`.

## Tab Statistics

The Pipe provides the statistics values described under the Tab Statistics.

## Tab User-defined Attributes

Define your own attributes as described under the Tab User-defined.

## Navigate Menu / View Menu / Tools Menu / Help Menu

Commands are described under their respective menus.

SimTalk (View Menu): `updateDialog [SimTalk]`

## Methods of the Pipe

The Pipe provides the Methods of All Objects. To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (F8, or the context menu of the Class Library).

An example of the Syntax line of the individual methods:

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## SetupTime [SimTalk] - fluid objects

Sets the duration of the Set-up Time of the fluid object designated by `<Path>`.

A fluid object has to set up whenever the name of the next material differs from the name of its preceding material. The set-up time is the time it takes to set the object up for processing a different type of material. An identical name designates that materials are of the same type.

**Type**: Attribute

**Syntax**:

```simtalk
<Path>.SetupTime:time
```

**Assignment Value**: you can assign a value of data type time.

**Example**:

```simtalk
MyMixer.SetupTime := 120 // 2 minutes
```

**See also**: Set-up Time [general description], Times and Distributions, Pipe.
