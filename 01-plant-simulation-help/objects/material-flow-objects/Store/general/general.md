# Store [object]

Use the object **Store** for storing parts for a certain time. It usually represents a warehouse in your plant.

## Description

The MUs remain in the Store until you remove them, for example by using a Method. Type the number of storage places into a net of coordinates, i.e., into the text boxes **X-Dimension**, **Y-Dimension**, and **Z-Dimension**. The Store receives MUs as long as storage places are available within the storage area.

The part triggers a sensor when it enters the Store. The sensor then calls an **Entrance Control** (a Method object) that determines the storage place onto which the Store places the part. The Entrance Control can update the inventory list or execute any other action you define. If you do not define an Entrance Control, the Store places the part onto the first unoccupied storage place in the net of coordinates.

The Store has neither a Set-up Time nor a Processing Time. If you decrease the size of the Store, you will have to delete or move MUs that are located outside of these new coordinates. For example, if a part is located at position (3,4), the new x-coordinate may not be less than 3, and the new y-coordinate less than 4.

During a failure the Store does not place any parts into storage but can still remove them from storage.

You can also configure the Store as a **Supermarket** in pulling material flow strategies. The Supermarket stores and manages the different part types and controls the fill level for each part type in the Store. Once the minimum stock for a part type is reached, the Supermarket automatically sends an order to the parts supplier so that it fills the Store up again.

You can select different configurations for the Store on the tab **Appearance**. On the tab **MU Animation** you can set how the parts are distributed across the Animation Area of the Store.

## Show Manipulators

To change the length of the graphic and the anchor points of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard. You can use the manipulators to change the dimensions of the Store.

## Add the Object to the Simulation Model

To add the object Store to your simulation model, click **Manage Class Library > Basic Objects > MaterialFlow > Store** on the Home ribbon tab.

## Dialog Box of the Store

Double-click the icon of the Store to open its dialog box.

### Edit Simulation Properties

In the dialog box you can change the simulation properties of the object. The shared properties are described under **Dialog Items of the Objects**.

### Edit Animation Properties

To edit the 3D properties of the object in the dialog box **Edit 3D Properties**:

- Click the button **Edit 3D Properties** in the lower left corner of the simulation properties dialog box.
- Select the object in the model and press the spacebar.

To manipulate the graphic of the object, click **Show Manipulators** on the Edit ribbon tab or press `M` on the keyboard.

## Tab Attributes

The tab **Attributes** provides the settings listed in the table of contents to the left.

The storage places of the Store are organized in a net of coordinates whose dimension you can set in the **X-Dimension**, **Y-Dimension**, and **Z-Dimension**. You can access the various storage places using their coordinates.

Select the check box to use the Store as **Supermarket** for pulling material flow strategies. Plant Simulation then shows the **Configuration** button and dims the settings for the dimension.

### X-Dimension [Store]

Type the number of MUs which the Store can store along the x-axis into the text box **X-Dimension**.

**Remarks**

- The Capacity of the Store is X-Dimension times Y-Dimension times Z-Dimension. The greatest allowed value is ten million.
- If you decrease the dimension of the Store, make sure that no MUs are located on the storage places that will be deleted by this action! Either delete these MUs or move them to another storage place on the smaller storage space.

**SimTalk**

- `XDim` [SimTalk] - Store
- `Capacity` [SimTalk] - Store
- `pe(X,Y)` / `[X,Y]` [SimTalk] - Store
- `setDim` [SimTalk]

### Y-Dimension [Store]

Type the number of MUs which the Store can store along the y-axis into the text box **Y-Dimension**.

**Remarks**

- The Capacity of the Store is X-Dimension times Y-Dimension times Z-Dimension. The greatest allowed value is ten million.
- If you decrease the dimension of the Store, make sure that no MUs are located on the storage places that will be deleted by this action! Either delete these MUs or move them to another storage place on the smaller storage space.

**SimTalk**

- `YDim` [SimTalk] - Store
- `Capacity` [SimTalk] - Store
- `pe(X,Y)` / `[X,Y]` [SimTalk] - Store
- `setDim` [SimTalk]

### Z-Dimension [Store]

Type the number of MUs which the Store can store along the z-axis into the text box **Z-Dimension**.

**Remarks**

- The Z-Dimension enables stacking parts in the Store, for example upward in a high bay warehouse. The Capacity of the Store is X-Dimension times Y-Dimension times Z-Dimension.
- If you decrease the dimension of the Store, make sure that no MUs are located on the storage places that will be deleted by this action! Either delete these MUs or move them to another storage place on the smaller storage space.

**SimTalk**

- `ZDim` [SimTalk] - Store
- `getStackHeight` [SimTalk] - Store

### Fill Whole Layer [check box] - Store

If the Z-Dimension of the Store is greater than 1, you can stock parts layer by layer by selecting **Fill Whole Layer**.

**Remarks**

- Plant Simulation always starts a new layer first and only then stacks the parts on the layer below.
- By default, **Fill Whole Layer** is deactivated and Plant Simulation stacks the parts on each place up to its maximum Z-Dimension and then starts a new layer.
- Fill Whole Layer also affects the read-only attribute `Cont`. It returns the next MU from the stack containing the highest number of MUs.

**SimTalk**

- `FillWholeLayer` [SimTalk] - Store
- `Cont` [SimTalk] - material flow objects

### Supermarket [check box]

To use the Store as a Supermarket, select the check box. You can use the Supermarket to model pulling material flow strategies.

**Remarks**

- You can only select and clear the check box Supermarket if the Store is empty.
- The Supermarket stores and manages the different part types and controls the fill level for each part type in the Store. When the minimum stock for a part type is reached, the Supermarket automatically sends an order to the parts supplier so that it fills up the Store again with the respective part type.

**Configuration Table**

Click **Configuration** to open the Configuration Table in which you can set the Part Type, the Minimum Stock, the Maximum Stock, the Initial Stock, and the Supplier. The Configuration Table also shows the Current Stock and the Waiting Stock.

Plant Simulation automatically sets the dimensions of the Store for the animation:

- The X-Dimension is always 1.
- The Y-Dimension shows the amount of the different part types.
- The Z-Dimension shows -1.
- The Store always places parts of the same type on a stack.

After inserting the Store into your model, Plant Simulation shows it with the default dimensions. Clicking OK then shows it with the settings that you typed into the Configuration Table and propagates the values to the child objects.

**Show the Occupancy of the Supermarket in a Chart**

If you drag the Store configured as a Supermarket onto a Chart, it shows the occupancy for all parts that are defined in the Configuration Table by default.

**SimTalk**

- `Supermarket` [SimTalk]
- `orderParts` [SimTalk] - Store

### Configuration [button]

To open the configuration table, click the button. Specify the Part Type, the Name of the part, the Minimum Stock, the Maximum Stock, the Initial Stock, and the Supplier.

**Remarks**

- When you activate the check box Supermarket, Plant Simulation activates the Configuration button.
- Before you can type in data, click the Inheritance check box.

Proceed as follows:

- Type in the absolute path of the Part Type or drag the MU class into the cell and drop it there.
- Type in the Name of the Part Type. If you do not specify anything, Plant Simulation uses the name of the object from the column Part Type. The names that you enter have to be unique.
- Type in the Minimum stock of the part type. This is the smallest amount of parts of the designated part type in the Supermarket.
- Type in the Maximum stock of the part type. This is the greatest amount of parts of the designated part type in the Supermarket.
- Type in the Initial stock of the part type. This is the amount of parts of the designated part type which are created while initializing the Store. The Initial Value can also be smaller than the Minimum Value. In this case the order is triggered on Init.
- Type in the Supplier of the part type. The supplier can be another Store, a Source, or a Method.

When re-ordering parts, Plant Simulation fills the Store to the Maximum stock. If parts leave the Store while an order is open, Plant Simulation only creates an additional order if the amount of the already ordered parts plus the current parts do not secure the Minimum Stock.

Specify a Method to set from which supplier the parts are ordered if several suppliers can provide this part. The Method has to have the following signature:

```simtalk
param partName:string, minStock:integer, maxStock:integer,
currentStock:integer, orderedParts:integer
```

- The parameters contain the data from the configuration of the part which is running out of stock.
- The caller (`?`) of the method is the Store, and the active element (`@`) is the part which is running out of stock.
- The column **Current** shows how many parts of this part type are located in the Store at the moment. You cannot edit this column.
- The column **Waiting** shows the amount of remaining ordered parts. You cannot edit this column. The method `orderParts` of Source and Store increase this counter.

Click the right mouse button and select **Append Row** or **Insert Row** to add additional products and their data. Click **Delete Row** to delete the selected row.

**SimTalk**

- `orderParts` [SimTalk] - Store
- `getSupermarketConfiguration` [SimTalk]
- `setSupermarketConfiguration` [SimTalk]
- `Stock.MyPartName` [SimTalk]

## Tab Times

Define Times as described under the Tab Times.

Select a distribution from the drop-down list and type the values that this distribution requires into the text box. Plant Simulation shows the parameters along the upper border of the tab. You can also select a constant time (Const). You can set the type of the distribution and a complete set of parameters with the method `setTypeAndAttr` [SimTalk].

## Tab Failures

Define failures as described under the Tab Failures.

## Tab Controls

Provides controls to modify the built-in behavior of the object.

**Select the Path to an Existing Method**

Click the ellipsis button. Navigate to the location of the Method in the dialog **Select Object [for controls]** and click OK. This inserts the name of the Method into the text box of the Control. Press `F2` in the text box to open the Method. Then type in the source code of the Control.

Instead of choosing Select Object, you can also select the Method in a Frame, drag it to the text box and drop it there.

**Create a Control That is a Method of the Object**

Proceed as follows to create a control as a user-defined attribute of data type Method:

- Type a meaningful name into the text box and select **Create Control [context menu]**. Plant Simulation then inserts `self.Name_you_typed_in_for_the_control`, such as `self.A1Ctrl`.
- Select **Create Control** on the empty text box. Plant Simulation then inserts `self.OnBuilt_in_name_of_the_control`, such as `self.OnEntrance`.

Type the source code of this control into the Method that opens.

To edit the source code later on:

- Press `F2`.
- Or hold down Shift and double-click into the text box.
- Or select **Open Object** on the context menu.
- Or click the tab User-defined and double-click the name of the Method in the list.

To delete this control, delete the user-defined attribute. If you only delete the name from the text box, the user-defined attribute is retained.

## Tab Exit

Select to which of its successors the object moves the MU on the Tab Exit.

## Tab Statistics

Statistics is described under the Tab Statistics.

To view **Resource Statistics** of Stationary Resources in the Statistics Report, select **View > Show Statistics Report** in the dialog of the object. You can also click the right mouse button in the Frame and select **Show Statistics Report** or you can press `F6`.

## Tab Energy

Select energy settings for the object on the Tab Energy.

## Tab Costs

Select costs settings for the object on the Tab Costs.

While the Store places parts into storage, costs accrue which result from the sum of the investment costs and the operating costs.

- The investment costs only accrue during the Depreciation Period.
- The costs are allocated to the part, proportional to the capacity, as accrued costs.
- If the Store is empty, the costs remain with the Store as general costs.

## Tab User-defined

Define your own attributes as described under the Tab User-defined.

## View Menu

The View Menu provides commands to access its functions:

- Refresh [on View menu]
- Show Statistics Report [on View menu]
- Show Attributes and Methods [on View menu]
- Show Orders [Source]
- Contents [material flow objects]
- Forward Blocking List

### Show Orders [Store]

Opens a table that shows the orders which are pending with the Store.

**Remarks**

The table contains the Part Type of the ordered MU, its Amount, and the Target of the part. The Target is the object that orders the parts.

### Exit Blocking List [Store]

Opens a list, which contains all MUs which are waiting to be carried away by a Worker.

**Remarks**

The table **Waiting for Importers** shows the path of the MU, its folder, its name, and its number, which waits for a Worker to pick it up and carry it away.

**SimTalk**

- `exitBlockList` [SimTalk] - material flow objects
- `exitBlockList` [SimTalk] - lane A or B

## Tabs Menu

Use the commands of the Tabs menu to show or hide individual tabs of the selected material flow objects. If you hide tabs that you do not need, Plant Simulation opens the dialog faster, and you can change to those tabs faster that you need in your daily work.

**Remarks**

- To apply the changed settings, click OK, close the dialog, and reopen it.
- The menu shows a check mark to the left of the displayed tabs.
- The command **Inherit** turns inheritance of the displayed or hidden tabs in the dialog off or on.

## Methods of the Store

The Store provides:

- The methods listed in the table of contents to the left.
- The Methods of the Material Flow Objects.
- The Methods of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. Select **Show Attributes and Methods** on the context menu of the Class Library, or press `F8` (or click **Show Attributes and Methods** on the Home ribbon tab of the Frame).

An example of the Syntax line of the individual methods might look like this:

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- The expression `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of the parameter, is listed in parentheses.
- Optional parameters are listed within brackets.
- If a parameter has a default value, the signature shows the default value after the parameter, `:= false` in the example above.
- If the method has a return value, the signature shows its data type after the arrow `->`, `boolean` in the example above.

### findFreePlace [SimTalk]

Finds a free storage place in the Store designated by `<Path>` and returns it.

**Remarks**

The method applies to the Store, the ParallelStation, the Container, and to the Transporter with a loading space of type Store.

**Type:** Method

**Syntax**

```simtalk
<Path>.findFreePlace([StartingAtEnd:boolean:=false, XStart:integer:=1,
YStart:integer:=1]) → any
```

**Parameters**

- The optional parameter `StartingAtEnd` of data type boolean specifies if the search is to proceed starting at the end backward toward the front (true) or not (false). Default value is `false`.
- The optional parameter `XStart` of data type integer designates the X-coordinate of the storage place from which on the search is to be started. Default value is `1`.
- The optional parameter `YStart` of data type integer designates the Y-coordinate of the storage place from which on the search is to be started. Default value is `1`.

**Return Value:** The return value has the data type `any`.

**Example**

```simtalk
var freePlace := .MUs.Container:1.findFreePlace
if freePlace /= void
   var x,y:integer

   freeplace.getStoragePlace(x, y)

   print "Found free place at (", x, ", ", y, ")"
end
```

### findFreePlaceInRange [SimTalk]

Finds a free storage place within the designated range of the Store designated by `<Path>` and returns the position of the free place.

**Type:** Method

**Syntax**

```simtalk
<Path>.findFreePlaceInRange(SearchRange:listrange[,
LeftToRight:boolean:=true, TopToBottom:boolean:=true]) -> any
```

**Parameters**

- The parameter `SearchRange` of data type `listrange` designates the range of the list to be searched.
- The optional parameter `LeftToRight` of data type boolean sets if the list is searched from left to right (true) or from right to left (false). Default value is `true`.
- The optional parameter `TopToBottom` of data type boolean sets if the list is searched from top to bottom (true) or from bottom to top (false). Default value is `true`.

**Return Value:** The return value has the data type `any`.

**Example**

```simtalk
MyStore.findFreePlaceInRange({2,2}..{*.*}, false)
```

### findPart [SimTalk] - Store

Finds the part with the specified name in the Store designated by `<Path>` and returns it.

**Type:** Method

**Syntax**

```simtalk
<Path>.findPart(PartType:string) → object
```

**Parameter:** The parameter `PartType` of data type string designates the part type.

**Return Value:** The return value has the data type `object`.

**Example**

```simtalk
var o: object := MyStore.findPart("Container")
// returns for example .MUs.Container:1
```

### getSupermarketConfiguration [SimTalk]

Returns the configuration table of the Store designated by `<Path>`.

**Type:** Method

**Syntax**

```simtalk
<Path>.getSupermarketConfiguration(Target:table)
```

**Parameter:** The parameter `Target` of data type `table` designates the DataTable into which the configuration settings will be written.

**Example**

```simtalk
MyStore.getSupermarketConfiguration(MyDataTable)
```

### orderParts [SimTalk] - Store

Orders parts from the Store designated by `<Path>`.

**Type:** Method

**Syntax**

```simtalk
<Path>.orderParts(PartType:string, Amount:integer, Target:object)
```

**Parameters**

- The parameter `PartType` of data type string designates the name of the part type that is going to be ordered.
- The parameter `Amount` of data type integer designates the amount of parts that is going to be ordered.
- The parameter `Target` of data type object designates the object that orders the parts. The target (destination object) can be any material flow object. If the Target is a Supermarket, Plant Simulation increases the counter of the amount of remaining ordered parts (compare the column Waiting in the Configuration table of the Store).

**Examples**

```simtalk
MyStore.orderParts("MyPart", 12, MyStation)
```

```simtalk
param partsName:string, minStock:integer, maxStock:integer,
currentStock:integer, orderedParts:integer
var amount:integer := maxStock-currentStock-orderedParts
if amount > 0 then
   MyStore.orderParts(partsName, amount, ?)
end
```

### pe(X,Y) / [X,Y] [SimTalk] - Store

Sets the designated storage place on the production element (PE) in the Store designated by `<Path>`.

**Remarks**

- Instead of `pe([X,Y])` you can also use `[X,Y]`.
- To access the MU that is located on the designated storage place, append `.Cont`.
- The read-only attribute `Cont` returns the MU at the called position.

**Type:** Method

**Syntax**

```simtalk
<Path>.pe([X:integer, Y:integer]) -> any
<Path>[X:integer, Y:integer] -> any
```

**Parameters**

- The optional parameter `X` of data type integer designates the X-Dimension of the storage place.
- The optional parameter `Y` of data type integer designates the Y-Dimension.

If you do not specify the parameters, Plant Simulation returns the first free PE or the PE on the place (1,1) if no free PE is available.

**Return Value:** The return value has the data type `any`.

**Example**

```simtalk
@.move(MyStore.pe(2,3))
MyStore[2,3].Cont.move(Station)
```

### setSupermarketConfiguration [SimTalk]

Sets the configuration table of the Store designated by `<Path>`.

**Type:** Method

**Syntax**

```simtalk
<Path>.setSupermarketConfiguration(Source:table/void)
```

**Parameter:** The parameter `Source` of data type `table` designates the DataTable which contains the configuration. When setting the configuration, Plant Simulation ignores the columns Current and Waiting. Specify `void` for the parameter Source to activate inheritance of the Configuration table of the Store.

**Examples**

```simtalk
MyStore.setSupermarketConfiguration(MyDataTable)
```

```simtalk
MyStore.setSupermarketConfiguration(void) -- activates inheritance of the
configuration table
```

## Methods and Read-Only Attributes of the Place in the Store [PE]

The PE (production element), i.e., the place in the Store, provides the methods and read-only attributes listed in the table of contents to the left.

## See also

- Wait for Free Target [PickAndPlace]
- Target Selection [drop-down list]
- Place Parts into Stock and Remove Parts from It
- Use the Store as Supermarket
- Stack Parts in the Store
- Unload Stacked Parts
- Entrance Control [general description]
- Exit Control [general description]
- Pull Control [general description]
- Shift Calendar [tab Controls]
- Blocking [exit strategy]
- Strategy [material flow objects]
- MU selection [drop-down list] > Order Controlled [MU selection]
