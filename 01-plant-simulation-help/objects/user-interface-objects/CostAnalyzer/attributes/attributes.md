# Attributes of the CostAnalyzer

## Overview

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the F8 key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyCostAnalyzer.UUID
```

## Provided Attributes

The CostAnalyzer provides:

- The attribute `CollectData`.
- The Attributes of All Objects.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
MyCostAnalyzer.CollectData := false
```

- To get the value of an attribute, you might, for example, type:

```simtalk
MyCostAnalyzer.CollectData
posit := Station.Cont.XPos
```

## CollectData [SimTalk] - CostAnalyzer

Sets if the CostAnalyzer designated by `<Path>` collects data (`true`) or does not collect data (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.CollectData:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

### Example

```simtalk
MyCostAnalyzer.CollectData := true
```

### See also

- Collect Data [check box] - CostAnalyzer

## HtmlReport [object]

Use the object `HtmlReport` for presenting current data and results of the simulation run in a report that you can share with co-workers and customers.

### Description

You can save the HtmlReport as an `.htm` file and open this file in an HTML-Browser, such as Microsoft Edge, Firefox, Google Chrome, etc. Plant Simulation is not required to open the HtmlReport in an external Browser, meaning that the HtmlReport can be displayed on any computer on which an HTML-Browser is installed.
