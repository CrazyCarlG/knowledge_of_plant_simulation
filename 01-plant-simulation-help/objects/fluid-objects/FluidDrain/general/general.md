# FluidDrain

Use the **FluidDrain** to define the ingredients and the products to be processed in the plant.

The FluidDrain removes the free-flowing materials, which the FluidSource introduced into the plant, from the plant after they have been mixed and processed. It differentiates the materials by their names.

To change the length of the graphic and the anchor points of the FluidDrain, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

To show a tooltip with information about the FluidDrain, hover with the mouse over it.

## Add the Object to the Simulation Model

To add the object FluidDrain to your simulation model, click **Manage Class Library > Basic Objects > Fluids > FluidDrain** on the Home ribbon tab.

Compare the sample models: Click the Window ribbon tab, click **Start Page > Getting Started > Example Models > Small Examples**. Then, select the respective Category, the Topic, and the Example in the dialog *Examples Collection*, and click **Open Model**.

## See also

- FluidSource
- Simulate Free-flowing Materials and Fluids

---

# Dialog Box of the FluidDrain

Double-click the icon of the FluidDrain to open its dialog box.

## Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under *Dialog Items of the Objects*.

## Edit Animation Properties

To edit the 3D properties of the object in the dialog box *Edit 3D Properties*:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

---

# Tab Attributes

The tab Attributes provides the settings, which the object offers. The settings are listed in the table of contents to the left. The shared properties are described under the *Tab Attributes*.

## Shift Calendar [FluidDrain]

Select the ShiftCalendar. It contains the data of the shifts in your installation and controls during which shifts the FluidDrain works in the plant.

### Remarks

- Click the ellipsis button and select the ShiftCalendar in the dialog *Select Object*.
- Instead of clicking the ellipsis button, you can also select the ShiftCalendar in a Frame, drag it to the text box, and drop it there. This automatically enters the object into the list of Objects on the tab Resources of the ShiftCalendar.

### SimTalk

```simtalk
ShiftCalendarObject
```

### See also

- ShiftCalendar [object]
- Associated Shift Calendar
- Select Object [for controls]

## Current Inflow Rate [FluidDrain]

Shows the Current Inflow Rate, i.e., the amount of liters of the material which flows into the FluidDrain in a second and which it in turn drains from the plant.

### SimTalk

```simtalk
CurrentInFlowrate
```

---

# Tab Failures

Define failures as described under the *Tab Failures*.

---

# Tab Statistics

Tab Statistics [FluidDrain]

In addition to the resource statistics values that are described under the *Tab Statistics*, the tab Statistics of the FluidDrain shows these values.

| Item (English) | Description | Item (German) |
| --- | --- | --- |
| Total Throughput | Shows the amount of material that the FluidDrain drained from the plant. | Gesamtdurchsatz |
| Throughput per Hour | Shows the amount of material that the FluidDrain drained from the plant in an hour while the FluidDrain was available. | Durchsatz pro Stunde |
| Throughput per Day | Shows the amount of material that the FluidDrain drained from the plant in a day while the FluidDrain was available. This is the value of the throughput per hour multiplied with 24. | Durchsatz pro Tag |
| Maximum Flow Rate | Shows the maximum flow rate, i.e., the amount of liters of the material in a second that flowed through the FluidDrain. | Maximale Flußrate |

## Detailed Statistics Table [FluidDrain]

The Detailed Statistics Table itemizes the materials, which the FluidDrain drained from the plant.

### Remarks

To open the Detailed Statistics Table, click this button.

It shows these values:

| Name | Description |
| --- | --- |
| Material | Shows the name of the material that the FluidDrain drained from the plant. |
| Throughput | Shows the total amount of the material that the FluidDrain drained from the plant. |

### SimTalk

```simtalk
typeStatistics
```

---

# Tab User-defined

Define your own attributes as described under the *Tab User-defined*.

---

# Navigate Menu

The commands are described under the *Navigate Menu*.

---

# View Menu

The commands are described under the *View Menu*.

### SimTalk

```simtalk
updateDialog
```

---

# Tools Menu

The commands are described under the *Navigate Menu*.

---

# Help Menu

The commands are described under the *Help Menu*.

---

# Methods of the FluidDrain

The FluidDrain provides:

- The method `typeStatistics` [SimTalk] - FluidDrain.
- The Methods of the Fluid Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window *Show Attributes and Methods*. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the `F8` key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].
