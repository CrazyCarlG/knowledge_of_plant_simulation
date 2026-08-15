# Read-Only Attributes of the LockoutZone

The LockoutZone provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```
print MyLockoutZone.StatStoppedCount
```

---

## addObject [SimTalk] - LockoutZone

Adds a single object to the LockoutZone designated by `<Path>`.

- **Type:** Method
- **Syntax:** `<Path>.addObject(NameOfObject:path) → boolean`

**Parameter**

The parameter `NameOfObject` of data type `path` designates the name of the object you want to add.

**Return Value**

The return value has the data type `boolean`.

**Example**

```
MyLockoutZone.addObject(MyParallelStation)
```

**See also:** Tab Objects

---

## StatStoppedCount [SimTalk] - LockoutZone

Returns how often the LockoutZone designated by `<Path>` stopped the assigned stations.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoppedCount → integer`
- **Watchable:** The read-only attribute is watchable.

**Return Value**

The return value has the data type `integer`.

**Example**

```
print MyLockoutZone.StatStoppedCount
```

**See also:** Tab Statistics [LockoutZone]

---

## StatStoppedDelta [SimTalk] - LockoutZone

Returns the standard deviation of the time during which the LockoutZone designated by `<Path>` stopped the processing operations of the assigned stations.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoppedDelta → time`
- **Watchable:** The read-only attribute is watchable.

**Return Value**

The return value has the data type `time`.

**Example**

```
print MyLockoutZone.StatStoppedDelta
```

**See also:** Tab Statistics [LockoutZone]

---

## StatStoppedIntervalDelta [SimTalk]

Returns the standard deviation of the intervals during which the LockoutZone designated by `<Path>` stopped the processing operations of the assigned stations.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoppedIntervalDelta → time`
- **Watchable:** The read-only attribute is watchable.

**Return Value**

The return value has the data type `time`.

**Example**

```
print MyLockoutZone.StatStoppedIntervalDelta
```

**See also:** Tab Statistics [LockoutZone]

---

## StatStoppedIntervalMu [SimTalk]

Returns the mean time of the intervals during which the LockoutZone designated by `<Path>` stopped the processing operations of the assigned stations.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoppedIntervalMu → time`
- **Watchable:** The read-only attribute is watchable.

**Return Value**

The return value has the data type `time`.

**Example**

```
print MyLockoutZone.StatStoppedIntervalMu
```

**See also:** Tab Statistics [LockoutZone]

---

## StatStoppedIntervalTime [SimTalk]

Returns the total time of the intervals during which the LockoutZone designated by `<Path>` stopped the processing operations of the assigned stations.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoppedIntervalTime → time`

**Return Value**

The return value has the data type `time`.

**Example**

```
print MyLockoutZone.StatStoppedIntervalTime
```

**See also:** Tab Statistics [LockoutZone]

---

## StatStoppedMu [SimTalk] - LockoutZone

Returns the mean time during which the LockoutZone designated by `<Path>` stopped the processing operations of the assigned stations.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoppedMu → time`
- **Watchable:** The read-only attribute is watchable.

**Return Value**

The return value has the data type `time`.

**Example**

```
print MyLockoutZone.StatStoppedMu
```

**See also:** Tab Statistics [LockoutZone]

---

## StatStoppedPortion [SimTalk] - LockoutZone

Returns the portion of the statistics collection period during which the stations were stopped by the LockoutZone designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoppedPortion → real`
- **Watchable:** The read-only attribute is watchable.

**Return Value**

The return value has the data type `real`.

**Example**

```
print MyLockoutZone.StatStoppedPortion
```

**See also:** Tab Statistics [LockoutZone]

---

## StatStoppedTime [SimTalk]

Returns the total time during which the LockoutZone designated by `<Path>` stopped the processing operations of the assigned stations.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatStoppedTime → time`
- **Watchable:** The read-only attribute is watchable.

**Return Value**

The return value has the data type `time`.

**Example**

```
print MyLockoutZone.StatStoppedTime
```

**See also:** Tab Statistics [LockoutZone]
