# Read-Only Attributes of the Display

The Display provides:

- The read-only attributes listed below.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyDisplay.GetMaximum
```

---

## GetAverage [SimTalk]

Returns the average value of the values that the Display designated by `<Path>` recorded.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.GetAverage → real
```

**Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDisplay.GetAverage
```

---

## GetMaximum [SimTalk]

Returns the maximum value of the range of values that the Display designated by `<Path>` shows.

**Remarks**

Only use `GetMaximum` for Watch Mode. In Sample Mode Plant Simulation only updates the value if **MUs and States** is activated and the Frame, in which the Display is inserted, is open.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.GetMaximum → real
```

**Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDisplay.GetMaximum
```

**See also:** `GetMinimum`, `resetMinMax`, Maximum [Display], Mode [drop-down list] - Display, MUs and States [Home ribbon]

---

## GetMinimum [SimTalk]

Returns the minimum value of the range of values that the Display designated by `<Path>` shows.

**Remarks**

Only use `GetMinimum` for Watch Mode. In Sample Mode Plant Simulation only updates the value if **MUs and States** is activated and the Frame, in which the Display is inserted, is open.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.GetMinimum → real
```

**Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDisplay.GetMinimum
```

**See also:** `GetMaximum`, `resetMinMax`, Minimum [Display], Mode [drop-down list] - Display, MUs and States [Home ribbon]

---

## GetStandardDeviation [SimTalk]

Returns the standard deviation of the values that the Display designated by `<Path>` recorded.

**Type:** Read-only attribute

**Syntax:**

```simtalk
<Path>.GetStandardDeviation → real
```

**Return Value:** The return value has the data type `real`.

**Example:**

```simtalk
print MyDisplay.GetStandardDeviation
```

---

## Related: update [SimTalk]

Updates the value that the Display designated by `<Path>` shows after a certain time has elapsed.

**Remarks**

`update` is only useful in conjunction with Sample mode. You can use the method `update` to force the Display to display a current value, for example after you changed the input value. To be compatible with previous versions of Plant Simulation, you can specify the parameter `Time` of data type `time`.

**Syntax:**

```simtalk
<Path>.update
```

**Example:**

```simtalk
MyDisplay.update
```

**See also:** Interval [text box] - Display
