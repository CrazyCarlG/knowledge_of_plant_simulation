# Read-Only Attributes of Lists and Tables

本目录收录了 Plant Simulation 中列表与表格对象（DataStack、DataQueue、DataList、DataTable、TimeSequence）的**只读属性**参考文档。

## 概述

列表与表格提供一组只读属性，用于返回其当前状态。这些属性**只能查询、不能赋值**——Plant Simulation 会在查询时刻计算并返回对应的值。大多数只读属性对应对象某个选项卡上不可编辑的对话框项（例如 *Statistics* 选项卡）。

查看对象全部方法、只读属性与属性的方式：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **Class** 的方法与属性。
- 在 Frame 中选中实例后按 **F8** 键（或点击 Home 功能区中的 **Show Attributes and Methods**），可查看所选 **Instance** 的方法与属性。

查询只读属性示例：

```simtalk
print MyDataTable.Full
```

## 只读属性一览

| 属性 | 适用对象 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `Void` | 列表/表格的单元格 | `boolean` | 指定单元格是否为空（`true` 为空，`false` 非空） |
| `Dim` | 列表/表格 | `integer` | 条目数量（Dimension）；DataTable 为列数 × 行数的乘积 |
| `Empty` | 列表/表格 | `boolean` | 是否包含空白单元格（`true` 含空白单元格） |
| `Full` | 列表/表格 | `boolean` | 是否已满（`true` 为满） |
| `Occupied` | 列表/表格 | `boolean` | 是否至少有一个单元格含条目（`true` 为有） |

> `Dim` 与 `Full` 为**可监视（watchable）**属性。

### 1. `Void` — 单元格是否为空

判断列表/表格中指定单元格是否为空。

```simtalk
<Path-of-the-list[row]>.void -> boolean
<Path-of-the-table[column,row]>.void -> boolean
```

示例：

```simtalk
if not DataTable[1,1].void
   DataTable[1,1] += 1
end
```

### 2. `Dim` — 条目数量（Dimension）

返回列表/表格的维度（条目数）。对 DataTable 而言，维度 = x 维度（列） × y 维度（单元格）。

```simtalk
<Path>.Dim → integer
```

示例：

```simtalk
print MyDataStack.Dim
number := MyDataQueue.Dim
print MyDataList.Dim
number := table.Dim
```

### 3. `Empty` — 是否含空白单元格

返回列表/表格是否包含空白单元格。

```simtalk
<Path>.Empty → boolean
```

示例：

```simtalk
print MyDataQueue.Empty
print MyDataList.Empty
print MyDataTable.Empty
```

### 4. `Full` — 是否已满

返回列表/表格是否已满。通常情况下列表/表格的条目/单元格数量不受限制（永不为满）；可在对话框中或用 `MaxDim`、`MaxXDim`、`MaxYDim` 属性限制单元格数量。

```simtalk
<Path>.Full → boolean
```

示例：

```simtalk
print MyDataStack.Full
print MyDataList.Full
print MyDataTable.Full
```

**相关属性：** `MaxDim`、`MaxXDim`、`MaxYDim`

### 5. `Occupied` — 是否有条目

返回列表/表格中是否至少有一个单元格包含条目。

```simtalk
<Path>.Occupied → boolean
```

示例：

```simtalk
print MyDataStack.Occupied
print MyDataList.Occupied
print MyDataTable.Occupied
```

## 相关主题：列表与表格的属性

列表与表格的所有形态（**DataStack**、**DataQueue**、**DataList**、**DataTable**、**TimeSequence**）共享一组预定义属性，用于控制其行为或表示其状态。属性与只读属性的区别在于：属性**可读可写**（通过对话框的复选框、文本框、下拉列表，或直接赋值），而只读属性仅可查询。

设置属性示例：

```simtalk
MyDataTable.MaxXDim := -1
```

读取属性示例：

```simtalk
print MyDataTable.MaxXDim
posit := Station.Cont.XPos
```

### 参见

- Attributes for the Format of Lists and Tables
- Attributes for the Text Format of Lists and Tables
- Attributes for Printing Lists and Tables
- Attributes for Showing Settings of Lists and Tables
- Miscellaneous Attributes of Lists and Tables
