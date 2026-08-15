# Read-Only Attributes of the ParallelStation

The ParallelStation provides:

- The read-only attribute **Capacity [SimTalk] - ParallelStation**.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print ParallelStation.Capacity
```

---

## Capacity [SimTalk] - ParallelStation

Returns the capacity of the ParallelStation designated by `<Path>`.

**Remarks**

The Capacity is the product of XDim times YDim.

**Type**

Read-only attribute

**Syntax**

```simtalk
<Path>.Capacity → integer
```

**Watchable**

The attribute is watchable.

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
if ParallelStation.Capacity >= lotsize 
   @.move(ParallelStation)
end
```

**See also**

- XDim [SimTalk] - ParallelStation
- YDim [SimTalk] - ParallelStation
- Y-Dimension [ParallelStation]
- X-Dimension [ParallelStation]
- Capacity [SimTalk] - ParallelStation

---

## Attributes of the ParallelStation

The ParallelStation provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure below illustrates the information using the example of the object Station.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To **set** the value of an attribute, you might, for example, type:

```simtalk
ParallelStation.XDim := 3
ParallelStation.YDim := 4
```

- To **get** the value of an attribute, you might, for example, type:

```simtalk
print ParallelStation.XDim
posit := MyStation.Cont.XPos
```
