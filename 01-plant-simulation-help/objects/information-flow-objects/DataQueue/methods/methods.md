# Methods of DataQueue and DataStack

## Overview

This page documents the methods of the **DataQueue** and **DataStack** objects. For additional methods, refer to:

- The Methods of Lists and Tables.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of an object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show the attributes and methods of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the attributes and methods of the selected Instance.

## Reading a Method Syntax Line

An example of the Syntax line of an individual method:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method (identifier and data type of the parameter) is listed in parentheses. `(Parameter:string)`, for example, designates a parameter of data type `string`. Instead of a constant value, you can also use a variable of the required type or a method that returns the required type.
- Optional parameters are listed within brackets. `[,Parameter:boolean]`, for example, means you may omit the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter.
- If the method has a return value, the signature shows its data type after the arrow `->`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

### Abbreviations used in signatures

| Argument of data type | Data type | Range of values |
|---|---|---|
| integer | integer | integer greater than zero |
| any | all data types | depending on the data type |
| listrange | — | a range |
| direction | string | "up", "down", " " |
| attributes | string | name of an attribute |

---

## Methods

### createNestedList [SimTalk] - DataQueue

Creates a nested list in the DataStack or DataQueue designated by `<Path>`.

**Remarks:** The DataStack or DataQueue has to be of data type `list`, `stack`, `queue`, or `table`. Plant Simulation moves existing entries down one position. When you specify an index greater than the greatest valid index, Plant Simulation places the entry at the first available position in the list, regardless of the actual index, preventing gaps between entries.

**Type:** Method

**Syntax:**

```
<Path>.createNestedList([Name:string]) → list
```

**Parameter:** The optional parameter `Name` of data type `string` designates the name of the list to be created.

**Return Value:** The return value has the data type `list` — the nested list (DataList, DataQueue, DataStack, or DataTable) that was created.

**Example:**

```
MyDataStack.createNestedList("My Sublist")
```

---

### pop [SimTalk] - DataStack

Removes the first cell from a list with one column designated by `<Path>`.

**Remarks:** DataStack and DataQueue cut the entries according to their built-in properties.

**Type:** Method

**Syntax:**

```
<Path>.pop
```

**Return Value:** The data type of the return value matches the data type of the DataStack or the DataQueue.

**Example:**

```
value := MyDataStack.pop
-- removes the first cell from MyDataStack

value := MyDataQueue.pop
-- removes the last cell from MyDataQueue
```

---

### push [SimTalk] - Stack

Adds the specified cell at the first position of the list with one column designated by `<Path>`.

**Remarks:** DataStack and DataQueue add the entries according to their built-in properties.

**Type:** Method

**Syntax:**

```
<Path>.push(Cell:any)
```

**Parameter:** The parameter `Cell` of data type `any` designates the cell.

**Example:**

```
MyDataStack.push("bottles")
-- adds the cell containing the string bottles
-- as the first cell to MyDataStack

MyDataQueue.push("cans")
-- adds the cell containing the string cans
-- as the last cell to MyDataQueue
```

**See also:** `pop [SimTalk] - DataStack`

---

### pushList [SimTalk]

Places the list designated by the parameter of data type `any` into the DataStack or the DataQueue designated by `<Path>`.

**Type:** Method

**Syntax:**

```
<Path>.pushList(List:any)
```

**Parameter:** The parameter `List` of data type `any` has to reference a list of data type `stack`, `queue`, a `list`, or a single column of data type `table`.

- Use the method `copy` if you only want to place a range of a list into a DataStack or a DataQueue.
- The data types of the data you want to insert have to match the data types of the DataStack or DataQueue into which you insert it.

**Example:**

```
// pastes the contents of the DataList into the DataStack
MyDataStack.pushList(MyDataList.copy)

// pastes the specified range from the DataList, starting in cell 4,
// into the DataQueue
MyDataQueue.pushList(MyDataList.copy({4}..{*}))
```

---

### top [SimTalk]

Reads the contents of a cell in a list with one column without removing it.

**Remarks:** The DataStack and the DataQueue designated by `<Path>` set the position of the cell according to their built-in properties.

**Type:** Method

**Syntax:**

```
<Path>.top
```

**Example:**

```
print MyDataStack.top
```

---

## Read-Only Attributes of DataQueue and DataStack

The DataStack and the DataQueue provide:

- The _Read-Only Attributes of Lists and Tables.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them, as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab **Statistics**.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.
