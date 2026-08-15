# Read-Only Attributes of the AssemblyStation

The `AssemblyStation` provides:

- The read-only attributes listed below.
- The _Read-Only Attributes of All Objects.
- The Read-Only Attributes of the Material Flow Objects.

You can query the values of the read-only attributes, but you cannot set them — Plant Simulation computes the value at the point-in-time you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, on the **Statistics** tab).

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame containing the instance to show them for the selected Instance.

To query the value of a read-only attribute, for example:

```simtalk
print AssemblyStation.StatWaitingPartsCount
```

---

## statWaitingTimeTable

`<Path>.statWaitingTimeTable(WaitingTimes:table) → boolean`

- **Parameter**: `WaitingTimes` of data type `table` designates the name of the table.
- **Return Value**: `boolean`. Returns `false` for the settings *MU Types* and *Depends on Main MU*.

```simtalk
var myWaitingTimesTable: table
MyAssembly.statWaitingTimeTable(myWaitingTimesTable)
print MyAssembly.statWaitingTimeTable(myWaitingTimesTable)
```

**See also**: Waiting [state, material flow objects], Tab Statistics [AssemblyStation] > Waiting Times

---

## NumMUsToBeDeleted [SimTalk]

Returns the number of MUs from the table *MUs To Be Deleted* of the `AssemblyStation` designated by `<Path>`.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.NumMUsToBeDeleted → integer`
- **Return Value**: `integer`

```simtalk
for var i := 1 to MyAssembly.NumMUsToBeDeleted
   print MyAssembly.MUToBeDeleted(i)
next
```

**See also**: MUs To Be Deleted, muToBeDeleted [SimTalk], musToBeDeleted [SimTalk]

---

## StatWaitingPartsCount [SimTalk]

Returns how often the `AssemblyStation` designated by `<Path>` was waiting for mounting parts.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingPartsCount → integer`
- **Return Value**: `integer`

```simtalk
print MyAssembly.StatWaitingPartsCount
```

**See also**: Waiting [state, material flow objects], Statistics report, Waiting Times for Parts

---

## StatWaitingPartsDelta [SimTalk]

Returns the deviation from the mean value of the time spans during which the `AssemblyStation` designated by `<Path>` was waiting for MUs.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingPartsDelta → real`
- **Return Value**: `real`

```simtalk
print MyAssembly.StatWaitingPartsDelta
```

**See also**: Waiting [state, material flow objects], Statistics report, Waiting Times for Parts

---

## StatWaitingPartsMu [SimTalk]

Returns the mean duration of the time spans during which the `AssemblyStation` designated by `<Path>` was waiting for MUs.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingPartsMu → real`
- **Return Value**: `real`

```simtalk
print MyAssembly.StatWaitingPartsMu
```

**See also**: Waiting [state, material flow objects], Statistics report, Waiting Times for Parts

---

## StatWaitingPartsPortion [SimTalk]

Returns the portion of the statistics collection period during which the `AssemblyStation` designated by `<Path>` was waiting for mounting parts.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingPartsPortion → real`
- **Return Value**: `real`

```simtalk
print MyAssembly.StatWaitingPartsPortion
```

**See also**: Waiting [state, material flow objects], Tab Statistics [AssemblyStation], Statistics report, Waiting Times for Parts

---

## StatWaitingPartsTime [SimTalk]

Returns the entire time during which the `AssemblyStation` designated by `<Path>` was waiting for MUs.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingPartsTime → time`
- **Return Value**: `time`

```simtalk
print MyAssembly.StatWaitingPartsTime
```

**See also**: Waiting [state, material flow objects], Statistics report, Waiting Times for Parts

---

## StatWaitingResCount [SimTalk] - AssemblyStation

Returns how often the `AssemblyStation` designated by `<Path>` was waiting for mounting parts and/or for processing-Exporters/processing-services.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingResCount → integer`
- **Return Value**: `integer`

```simtalk
print MyAssembly.StatWaitingResCount
```

**See also**: Waiting [state, material flow objects], Statistics report, Waiting Times for Services and Parts

---

## StatWaitingResDelta [SimTalk] - AssemblyStation

Returns the standard deviation of the times during which the `AssemblyStation` designated by `<Path>` was waiting for mounting parts and/or for processing-Exporters/processing-services.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingResDelta → real`
- **Return Value**: `real`

```simtalk
print MyAssembly.StatWaitingResDelta
```

**See also**: Waiting [state, material flow objects], Statistics report, Waiting Times for Services and Parts

---

## StatWaitingResMu [SimTalk] - AssemblyStation

Returns the average duration of a period of time during which the `AssemblyStation` designated by `<Path>` was waiting for mounting parts and/or for processing-Exporters/processing-services.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingResMu → real`
- **Return Value**: `real`

```simtalk
print MyAssembly.StatWaitingResMu
```

**See also**: Waiting [state, material flow objects], Statistics report, Waiting Times for Services and Parts

---

## StatWaitingResPortion [SimTalk] - AssemblyStation

Returns the ratio of the time during which the `AssemblyStation` designated by `<Path>` was waiting for mounting parts and/or for processing-Exporters/processing-services to the statistics collection period.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingResPortion → real`
- **Return Value**: `real`

```simtalk
print MyAssembly.StatWaitingResPortion
```

**See also**: Waiting [state, material flow objects], Tab Statistics [AssemblyStation], Statistics report, Importers Waiting for Services and Parts, Statistics report, Waiting Times for Services and Parts

---

## StatWaitingResTime [SimTalk] - AssemblyStation

Returns the entire time during which the `AssemblyStation` designated by `<Path>` was waiting for mounting parts and/or for processing-Exporters/processing-services.

- **Type**: Read-only attribute
- **Syntax**: `<Path>.StatWaitingResTime → time`
- **Return Value**: `time`

```simtalk
print MyAssembly.StatWaitingResTime
```

**See also**: Waiting [state, material flow objects], Statistics report, Waiting Times for Services and Parts
