# AttributeExplorer (General)

## Description

Instead of opening the dialog of each material flow object and typing attribute values into text boxes, the **AttributeExplorer** lets you define which attributes of which objects it gets and shows in a list window.

To do so, click **Show Explorer**. Then type in the different values (capacities, times, etc.), which Plant Simulation writes back to the objects and uses in the model. You can **Export** this settings table as a tab-delimited text file and **Import** it into the AttributeExplorer of another simulation model, using identical settings across models.

You can also show the attribute table of an AttributeExplorer in an HtmlReport. Hover the mouse over it to show a tooltip. To change the length of the graphic and the anchor points, click **Show Manipulators** on the Edit ribbon tab or press **M**.

## Add the Object to the Simulation Model

Click **Manage Class Library > Basic Objects > InformationFlow > AttributeExplorer** on the Home ribbon tab.

## Dialog Box

Double-click the icon to open its dialog box.

- **Edit Simulation Properties** — change the simulation properties (shared properties described under "Dialog Items of the Objects").
- **Edit Animation Properties** — edit 3D properties:
  - Click **Edit 3D Properties** in the lower-left corner of the simulation properties dialog box, or
  - Select the object in the model and press the spacebar.

To manipulate the graphic, click **Show Manipulators** on the Edit ribbon tab or press **M**.

## Show Explorer

Click this to show the list window displaying the objects and attributes defined on the **Tab Objects** and **Tab Attributes**.

**Remarks**

- Close the list window by clicking the **X** in the title bar.
- The results table is sorted according to **Path**, **Name**, or **Label**. The AttributeExplorer first shows the data of the specified objects, then data defined by the query.
- Alternatively, right-click the AttributeExplorer in the Frame and select **Show** on the context menu.
- Manipulate the list contents with the commands on the **Context Menu of Embedded Lists**.

**SimTalk**

- `IsShown [SimTalk] - AttributeExplorer`
- `AttributeTable [SimTalk]`
- `ExplorerTable [SimTalk]`

## Tab Data

Select settings for the mode of the attributes.

**Remarks** — before selecting settings, click the **Inheritance** check box.

Available settings:

- **Watch**
- **Edit**
- **Read Only**

Also select to:

- **Show Objects** with their Path, Name, or Label.
- **Show Attributes** with their Name or Alias.

Type in a **Comment** and select **Show a Comment**.

**SimTalk**

- `AttributeRepresentation [SimTalk]`
- `Mode [SimTalk] - AttributeExplorer`
- `ObjectRepresentation [SimTalk]`

### Watch

Display the values of watchable attributes of any stations typed on the tab Attributes.

Cell background colors indicate watchability:

| Color | Description |
|-------|-------------|
| blue  | The attribute is not watchable. |
| gray  | The attribute is watchable. |
| red   | You entered an invalid path to an attribute. |

**SimTalk**: `Mode [SimTalk] - AttributeExplorer`

### Edit

Allow editing the values of the attributes of any station specified on the tab Attributes. Plant Simulation writes the modified values back to the object dialogs when you click **Apply/OK**.

**SimTalk**: `Mode [SimTalk] - AttributeExplorer`

### Read Only

Activate read-only mode for attribute values of objects on the tab Objects and tab Attributes. You can only view (not edit) the values; Plant Simulation updates the displayed values when you click **Apply**.

**SimTalk**: `Mode [SimTalk] - AttributeExplorer`

### Show Objects With

Select how objects typed on the tab Objects are shown:

- Entire Path
- Name only
- Label only

**SimTalk**: `ObjectRepresentation [SimTalk]`

### Show Attributes With

Select how attributes typed on the tab Attributes are shown:

- **Alias** — a description you entered, in addition to the built-in name.
- **Name only**

**SimTalk**: `AttributeRepresentation [SimTalk]`

### Show Comment / Comment

- **Show Comment** — select to show explanations typed into the Comment text box.
- **Comment** — type an explanation for the objects and values defined on the tab Objects and tab Attributes. Select **Show Comment** to display it above the list field.

**SimTalk**

- `ShowComment [SimTalk] - AttributeExplorer`
- `Comment [SimTalk] - AttributeExplorer`

## Tab Objects

View or edit the attributes of an object.

**Remarks** — before typing data, click the **Inheritance** check box.

- Drag an object from the Frame window over the tab Objects and drop it there. Plant Simulation inserts the absolute path and name of the object into the selected cell.
- You can drag-and-drop multiple objects at the same time. Objects are added in the order selected in the Frame.
- To enter only the name, drag the object over the **icon** of the AttributeExplorer and drop it there.

**Note**: **F2** opens the dialog of the object whose name is in the text box.

**SimTalk**: `ObjectTable [SimTalk]`

## Tab Attributes

Click **Show Attributes** to type names of attributes whose values you want to edit/view into the **Name** column.

**Remarks** — before typing data, click the **Inheritance** check box.

In the dialog **Attribute Viewer**:

- Click and select the Object whose attributes to show in the dialog **Select Object**.
- Select from the drop-down list whether to view built-in attributes or user-defined attributes.
- Select one or several contiguous attributes (**Shift+click**) and click to add them to the attributes to be shown.
- To add a sub-attribute, type in the attribute and sub-attribute into the cell, for example:

```text
imp.priority
```

Click **OK** to add these attributes to the list displayed on the tab Attributes.

If the predefined **Name** is not meaningful enough, type a descriptive term into the **Alias** column.

**Notes**

- Importing a file only works correctly if the file contains the **Name** of the attribute (not only the Alias).
- To make an attribute read-only, click into the **Read Only** cell.

Cell background colors:

| Color | Description |
|-------|-------------|
| blue  | The attribute is not watchable. |
| white | The attribute is watchable. |
| gray  | You entered a wrong name for a built-in attribute. |

**SimTalk**

- `ObjectTable [SimTalk]`
- `AttributeTable [SimTalk]`

## Tab Query

Define a query that finds objects according to criteria typed into the list cells.

**Remarks** — before typing data, click the **Inheritance** check box.

Select the number of opening Parentheses, type in an Attribute, select a Condition, a Value, the number of closing Parentheses, an Operator, and a Comment. Select the Frame that the AttributeExplorer queries.

- Select **Include Subframes** to also query Frames within the selected Frame.
- Select **Include MUs** to include the parts (MUs) in the query.

Spelled out in code, the query reads like this:

```text
Name Expr Station.* and ((XPos > 100 and YPos = 200) or ExitStrategy = Cyclic)
```

**SimTalk**: `QueryTable [SimTalk]`

### Parentheses [opening]

Select the number of opening Parentheses of the query.

### Attribute

Type in the name of the Attribute to query. You can type any attribute shown in the window **Show Attributes and Methods**.

### Condition

Click the cell and select a Condition from the drop-down list:

- `<` (less than)
- `<=` (less than or equal to)
- `>` (greater than)
- `>=` (greater than or equal to)
- `=` (equal to) — compares attributes of data type real, length, weight, speed, and time for the exact value
- `~=` (equal to, case-insensitive) — compares strings ignoring case, or compares if attribute values are about equal
- `/=` (not equal to)
- `Expr` — a regular expression, compares `regex_search`. Example: `^Inf` finds any word beginning with "Inf".
- `Exists` — checks if the object has the designated attribute.

Then type the value into the corresponding cell in the column **Value**.

### Value

Type in the Value of the attribute to find.

### Parentheses [closing]

Select the number of closing Parentheses of the query.

### Operator

Click the cell and select a boolean Operator from the drop-down list. It connects the boolean values of the active row with the next row (from evaluating the logical expression in a row of the query table):

- `and`
- `or`

### Comment [query]

Type in any Comment explaining the query.

### Frame [find attribute in]

Click the ellipsis button and select the Frame (in **Select Object**) where you want to start finding attributes. Select **Include Subframes** to also include Frames within the selected Frame.

**SimTalk**: `StartNode [SimTalk]`

### Include Subframes

To also include Frames inserted in the selected Frame into the query, select this check box.

**SimTalk**: `IncludeSubframes [SimTalk]`

### Include MUs

To also include the MUs located within the selected Frame into the query, select this check box.

**SimTalk**: `IncludeMUs [SimTalk]`

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

## Menus

### Navigate Menu

Commands described under the Navigate Menu.

### View Menu

- Refresh [on View menu]
- Show Attributes and Methods [on View menu]

**SimTalk**: `updateDialog [SimTalk]`

### Tools Menu

- Edit Controls
- Edit Observers
- Export
- Import

#### Export

Export the contents of the tab Objects and tab Attributes to a tab-delimited text file, which you can import into another list to use identical settings across models.

#### Import

Import a tab-delimited text file containing the data of the tab Objects and tab Attributes.

### Help Menu

Commands described under the Help Menu.

## Methods of the AttributeExplorer

The AttributeExplorer provides the Methods of All Objects. To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame to show them for the selected Instance.

Example of a Syntax line:

```text
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```
