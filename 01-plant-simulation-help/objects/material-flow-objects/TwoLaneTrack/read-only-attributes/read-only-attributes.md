# Read-Only Attributes of the TwoLaneTrack

The TwoLaneTrack provides:

- The read-only attributes listed below.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, on the tab Statistics).

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods. For the TwoLaneTrack the dialog shows A and B for the respective lane, but not the read-only attributes proper for these lanes.

- Select Show Attributes and Methods on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the F8 key or click Show Attributes and Methods on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print TwoLaneTrack.A.NumPred
```

---

## succLaneNo [SimTalk] - lane A or B

Returns the number of the succeeding lane of the specified lane of the TwoLaneTrack designated by `<Path>`.

- **Type:** Method
- **Syntax:**

```simtalk
<Path>.A.succLaneNo([LaneNumber:integer]) → integer
<Path>.B.succLaneNo([LaneNumber:integer]) → integer
```

- **Parameter:** The optional parameter `LaneNumber` of data type `integer` designates the number of the lane of the n-th successor lane of the TwoLaneTrack. The objects have to be connected for this to work.
- **Return Value:** The return value has the data type `integer`.

**Example**

```simtalk
if MyTwoLaneTrack.A.succLaneNo = 1 
   print "succeeding lane is lane A"
end
```

---

## IsLaneA [SimTalk]

Returns if the Transporter drives on lane A of the TwoLaneTrack designated by `<Path>` (true) or not (false).

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.A.IsLaneA → boolean
```

- **Return Value:** The return value has the data type `boolean`.

**Example**

```simtalk
print TwoLaneTrack.A.IsLaneA    // returns true if the Transporter drives 
on lane A
print TwoLaneTrack.A.IsLaneA    // returns false if the Transporter does 
not drive on lane A
```

**See also:** Lane A

---

## IsLaneB [SimTalk]

Returns if the Transporter drives on lane B of the TwoLaneTrack designated by `<Path>` (true) or not (false).

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.B.IsLaneB → boolean
```

- **Return Value:** The return value has the data type `boolean`.

**Example**

```simtalk
print TwoLaneTrack.B.IsLaneB    // returns true if the Transporter drives 
on lane B
print TwoLaneTrack.B.IsLaneB    // returns false if the Transporter does 
not drive on lane B
```

**See also:** Lane B

---

## NumPred [SimTalk] - lane A or B

Returns the number of predecessors of the specified lane of the TwoLaneTrack designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.A.NumPred → integer
<Path>.B.NumPred → integer
```

- **Return Value:** The return value has the data type `integer`.

**Example**

```simtalk
for var i := 1 to MyTwoLaneTrack.B.NumPred
  print MyTwoLaneTrack.B.pred(i) // prints all predecessors
next
```

---

## NumSucc [SimTalk] - lane A or B

Returns the number of successors of the specified lane of the TwoLaneTrack designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.A.NumSucc → integer
<Path>.B.NumSucc → integer
```

- **Return Value:** The return value has the data type `integer`.

**Example**

```simtalk
if MyTwoLaneTrack.A.NumSucc > 1 
  ... // more than one successor
end
```

---

## OccupiedLength [SimTalk] - lane A or B

Returns the part of the entire length of the specified lane of the TwoLaneTrack designated by `<Path>` which is occupied by all Transporters located on it.

**Remarks:** Each Transporter located on the TwoLaneTrack occupies part of the entire available length on the TwoLaneTrack.

- **Type:** Read-only attribute
- **Syntax:**

```simtalk
<Path>.A.OccupiedLength → length
<Path>.B.OccupiedLength → length
```

- **Return Value:** The return value has the data type `length`.

**Example**

```simtalk
print myTwoLaneTrack.A.OccupiedLength
```

**See also:**
- Length [text box] - lane A
- Length [text box] - lane B
- Attributes of the TwoLaneTrack

---

## Attributes of the TwoLaneTrack

The TwoLaneTrack provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.
- The Attributes of the Material Flow Objects.
