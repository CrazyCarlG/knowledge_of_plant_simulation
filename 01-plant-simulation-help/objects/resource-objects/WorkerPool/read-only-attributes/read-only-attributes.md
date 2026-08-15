# Read-Only Attributes of the WorkerPool

The `WorkerPool` provides these read-only attributes:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure in the documentation illustrates this using the example of the object `Station`.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class (general description).
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance, to show the methods, read-only attributes, and attributes of the selected Instance (general description).

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyWorkerPool.StatAverageTraveledDistance
```

---

## NumAssignedWorkers

Returns the amount of Workers which the `WorkerPool` designated by `<Path>` assigned.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.NumAssignedWorkers -> integer`
- **Return Value:** The return value has the data type `integer`.

### Example

```simtalk
print MyWorkerPool.NumAssignedWorkers
```

### SimTalk

```simtalk
getAssignedWorkersTable [SimTalk]
getAssignedWorker [SimTalk]
NumAssignedWorkers [SimTalk]
```

---

## NumIdleWorkers

Returns the number of Workers in the `WorkerPool` designated by `<Path>` who are idle, i.e., not working.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.NumIdleWorkers -> integer`
- **Watchable:** The attribute is watchable.
- **Return Value:** The return value has the data type `integer`.

### Example

```simtalk
waituntil WorkerPool.NumidleWorkers > 0
var worker:object := WorkerPool.getIdleWorker
```

### SimTalk

```simtalk
IsIdle [SimTalk] - Worker
getIdleWorker [SimTalk]
NumIdleWorkers [SimTalk]
```

---

## StatAverageTraveledDistance

Returns the average distance in meters which the Worker traveled from the `WorkerPool` designated by `<Path>` to the Workplaces attached to the stations and between the stations.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.StatAverageTraveledDistance → length`
- **Return Value:** The return value has the data type `length`.

### Example

```simtalk
print MyWorkerPool.StatAverageTraveledDistance
```

---

## Attributes of the WorkerPool

The `WorkerPool` provides:

- The attributes listed in the table of contents to the left.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**. The figure in the documentation illustrates this using the example of the object `Station`.

---

## Examples (Workers to Create table)

```simtalk
MyWorkerPool.setWorkersToCreateTable(MyWorkersToCreateTable)
var rt: table                                -- read the Workers to Create table
MyWorkerPool.getWorkersToCreateTableRow(rt)  -- set the new amount
rt [2,1]:= AmountOfWorkers                   -- name of a Variable
                                             -- assign the Workers to Create table
                                             -- to the WorkerPool
MyWorkerPool.setWorkersToCreateTable(rt)
```

## SimTalk

```simtalk
getWorkersToCreateTable [SimTalk]
getWorkersToCreateTableRow [SimTalk] - WorkerPool
```

## See also

- Workers to Create
- Tab Scope
- Home Location
- The Relative Path
- Relational Operators
- Read-Only Attributes of the WorkerPool
- _Read-Only Attributes of All Objects
