# Methods and Read-Only Attributes of the PE in the Store

The PE (production element), i.e., the place in the Store, provides the methods and read-only attributes listed below.

---

## Cont [SimTalk] — pe, Store

**Type:** Read-only attribute

Returns the MU located at the top-most position on the designated storage place (production element) of the Store designated by `<Path>`.

**Syntax**

```
<Path>.pe(X:integer, Y:integer).Cont → object
<Path>[X:integer, Y:integer].Cont → object
```

**Parameters**

- `X` (integer): position of the storage place in the X-Dimension.
- `Y` (integer): position of the storage place in the Y-Dimension.

**Return Value**

Data type `object`.

**Example**

```simtalk
MyStore.pe(1,1).Cont.move(Station)
MyStore[1,1].Cont.move(Station)
```

**See also:** X-Dimension [Store], Y-Dimension [Store]

---

## exitBlockList [SimTalk] — Store

**Type:** Method

Returns an array containing the MUs that are going to exit the Store designated by `<Path>` and wait for a Worker to pick them up.

**Remarks**

- Specify the optional parameter `ExitBlockingList` of data type `table` to write the objects contained in the Exit Blocking List into this list.
- For the Store, the Exit Blocking List also contains the position of the place for which the part is entered. If you need this information, specify a table instead of writing the data to an array.
- If you do not specify the optional parameter, the returned array is one-dimensional and only contains the objects in the blocking list.
- To query the start times of the blockages (contained in the blocking table), use the attribute `BlockingStarttime`.

**Syntax**

```
<Path>.exitBlockList([ExitBlockingList:table]) -> void/object[]
```

**Parameter**

`ExitBlockingList` (table, optional): name of the table (a DataTable or a local variable) into which the method writes the values. Plant Simulation automatically generates the format of this table with two columns:
- Column 1 (data type `object`): the MUs that unsuccessfully tried to exit the object.
- Column 2: the simulation time at which the MUs attempted to enter the object.

**Return Value**

An array of data type `object`.

**Example**

```simtalk
var musToExit := Store.exitBlockList   // returns an array of MUs, which are going to exit
var t:table
Store.exitBlockList(t)                 // fills the table with MUs, which are going to exit
```

**See also:** SimTalk, BlockingStarttime [SimTalk], exitBlockList [SimTalk] - material flow objects, exitBlockList [SimTalk] - lane A or B, Exit Blocking List, Check the Contents List of the Stations

---

## getStackHeight [SimTalk] — Store

**Type:** Read-only attribute

Returns the height of the stack in meters on the designated storage place in the Store designated by `<Path>`.

**Remarks**

`getStackHeight` also applies to places on pallets/Containers and to Transporters with a loading space of type Store.

**Note**

- The height of the stack designates its physical height, not the number of parts on the stack.
- If you output the value with the method `print`, the unit is the unit selected under **Preferences / Model Settings > Unit > Length**.

**Syntax**

```
<Path>.pe(X:integer, Y:integer).getStackHeight → length
<Path>[X:integer, Y:integer].getStackHeight → length
```

**Parameters**

- `X` (integer): position of the storage place in the X-Dimension.
- `Y` (integer): position of the storage place in the Y-Dimension.

**Return Value**

Data type `length`.

**Example**

```simtalk
print MyStore.pe(2,1).getStackHeight
print MyStore[2,1].getStackHeight
```

**See also:** SimTalk, ZDim [SimTalk] - Store, Stack Parts in the Store, Length [preferences], X-Dimension [Store], Y-Dimension [Store]

---

## mu [SimTalk] — PE, Store

**Type:** Method

Returns all stacked MUs on the designated storage place (on the production element) in the Store designated by `<Path>`.

**Remarks**

- The method `mu` accesses the MUs on the stack if the Z-Dimension is greater than 1.
- The index does not signify the order of entry.
- You can query the greatest index with the read-only attribute `NumMU`.

**Syntax**

```
<Path>.pe(X:integer, Y:integer).mu(MU:integer) → object
<Path>[X:integer, Y:integer].mu(MU:integer) → object
```

**Parameters**

- `X` (integer): position of the storage place in the X-Dimension.
- `Y` (integer): position of the storage place in the Y-Dimension.
- `mu` (integer): position of the storage place in the Z-Dimension. Specify `-1` to return the MU at the bottom of the stack. It returns VOID if the object is empty.

**Default Value of the Parameter**

The default value for the parameter `Number` is 1.

**Note**

The last MU is always the MU located on the bottom storage place; as a rule this is the MU that was moved onto the object first.

**Return Value**

Data type `object`.

**Examples**

```simtalk
print MyStore.pe(5,5).mu(1) // returns the topmost MU on the stack
                            // corresponds to print MyStore.pe(5,5).cont
print MyStore[5,5].mu(2)    // returns the second MU from the top on the stack
print MyStore[5,5].mu(3)    // returns the MU at the bottom of a stack with 3 parts
print MyStore[1,1].MU(1)   // returns the topmost MU on the stack
print MyStore[1,1].MU(-1)  // returns the MU at the bottom of the stack
```

**See also:** SimTalk, NumMU [SimTalk] - PE, Store, X-Dimension [Store], Y-Dimension [Store], Z-Dimension [Store]

---

## NumMU [SimTalk] — PE, Store

**Type:** Read-only attribute

Returns the number of MUs located on the PE (production element) in the Store designated by `<Path>`.

**Syntax**

```
<Path>.pe(X:integer, Y:integer).NumMU → integer
<Path>[X:integer, Y:integer].NumMU → integer
```

**Parameters**

- `X` (integer): position of the storage place in the X-Dimension.
- `Y` (integer): position of the storage place in the Y-Dimension.

**Return Value**

Data type `integer`.

**Example**

```simtalk
print MyStore.pe(1,1).NumMU
print MyStore[1,1].NumMU
```

**See also:** X-Dimension [Store], Y-Dimension [Store]

---

## Read-Only Attributes of the Store

The Store provides:

- The read-only attributes listed in the table of contents to the left.
- The Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, the Statistics tab).

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print Store.Capacity
```
