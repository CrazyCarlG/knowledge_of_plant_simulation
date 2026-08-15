# 实例化本地列表和表格（Instantiating Local Lists and Tables）

本目录总结了 Plant Simulation SimTalk 中如何**实例化本地列表和表格**，包括 `create` 与 `createNestedList` 两个方法，以及相关的 `weight` 数据类型说明。

## 概述

数据类型为 `list`、`queue`、`stack` 或 `table` 的本地变量（以及列表中的列表、表格中的表格）本身**并不存储数据**，而是存储对相应数据结构的**引用（reference）**。

当变量在 Method 中声明后，其初始状态为 **void（空）**，即尚未包含对任何数据结构的引用。因此，在访问数据之前，必须**先创建（实例化）**该变量。

列表和表格提供两个用于实例化的方法：

- `create` —— 创建一个空的数据结构。
- `createNestedList` —— 创建一个嵌套的子列表或子表格。

---

## `create` [SimTalk] - 本地列表

在由 `<Local-variable>` 指定的本地变量中创建一个**不含任何内容的空数据结构**。

### 说明（Remarks）

`create` 适用于数据类型为 `list`、`queue`、`stack` 和 `table` 的本地变量。

### 类型（Type）

方法（Method）

### 语法（Syntax）

```
<Local-variable>.create([NumberOfRows:integer])
```

### 参数（Parameter）

可选参数 `NumberOfRows`（数据类型 `integer`）指定列表或表格的**行数**。

### 示例（Example）

```simtalk
var orderlist: table[string,real]
orderlist.create
orderlist[1,1] := "cans"
orderlist[2,1] := 3000.0
orderlist.forget    // 销毁表格
orderlist.create(4) // 重新创建一个包含 4 行的表格
```

### 参见（See also）

- 本地变量中的数据类型（Data Types in Local Variables）

---

## `createNestedList` [SimTalk] - 本地变量

在由 `<local-list>` 或 `<local-table>` 指定的本地变量中创建一个新的**子列表或子表格**。

### 说明（Remarks）

本地变量必须是 `list`、`queue`、`stack` 或 `table` 类型，且该列表/表格对应列的数据类型也必须为 `list`、`stack`、`queue` 或 `table` 类型。

### 类型（Type）

方法（Method）

### 语法（Syntax）

```
<Local-list>.createNestedList(Column:integer, Row:integer[, Name:string]) → list
<Local-table>.createNestedList(Column:integer, Row:integer[, Name:string]) → list
```

### 参数（Parameters）

- `Column`（integer）—— 指定单元格所在的**列**。
- `Row`（integer）—— 指定单元格所在的**行**。
- `Name`（string，可选）—— 指定要创建的子列表或子表格的**名称**。

### 注意（Note）

该方法同样适用于子列表和子表格。

### 返回值（Return Value）

返回值的类型为 `list`，即所创建的嵌套列表（`DataList`、`DataQueue`、`DataStack` 或 `DataTable`）。

### 示例（Examples）

```simtalk
var t: table[table]
t.create                 // 创建一个表格
t.createNestedList(1,1)  // 创建一个子表格
t[1,1][2,3] := "Hello world" // 将 Hello world 写入嵌套表格
```

上述代码在表格的第 1 个单元格中插入一个子表格，随后将 `Hello world` 写入该子表格中 `2,3` 位置的单元格。

```simtalk
var subtable: table
MyDataTable.createNestedList(2,3) // 创建一个子表格
subtable := MyDataTable[2,3]
subtable.createNestedList(1,1)    // 在子表格中再创建一个子表格
subtable[1,1][4,4] := "Hello world"
```

### 参见（See also）

- `setCommonFormat` [SimTalk]
- 激活与停用通用格式（Activating and Deactivating Common Format）
- `createNestedList` [SimTalk] - DataQueue
- `createNestedList` [SimTalk] - DataList
- `createNestedList` [SimTalk] - DataTable
- `createNestedList` [SimTalk] - 本地变量

---

## 相关：`Weight` [SimTalk] - 数据类型

数据类型为 `weight` 的本地变量的取值范围为 `-8.9*10^307 ≤ weight ≤ 8.9*10^307`，显示形式为 `-8.9e307 ≤ real ≤ 8.9e307`。

### 说明（Remarks）

- 当将 `weight` 值赋给变量或属性时，Plant Simulation 将其解释为**千克（kg）**。
- 输出时，Plant Simulation 会将其转换为 **文件 > 模型设置/首选项 > 单位 > 质量（File > Model Settings/Preferences > Units > Mass）** 中所选的单位。
- 数据类型 `time`、`length`、`weight`、`speed` 和 `acceleration` **互不兼容**！例如，只能将 `length`、`real` 或 `integer` 类型的值赋给 `length` 类型的变量。

### 参见（See also）

- `isWeight` [SimTalk]
