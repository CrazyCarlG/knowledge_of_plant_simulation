# AssemblyStation — Methods（方法）

本目录存放 **AssemblyStation**（装配站）对象的方法说明文档。内容来源为 `methods.md`（`methods.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. 概述

**AssemblyStation** 提供：

- 本目录列出（左侧目录中）的方法；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

要查看对象的全部方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，查看所选**类**的方法、只读属性和属性；
- 在插入实例的 Frame 中按 **F8** 键，或点击 Home 功能区标签页的 **Show Attributes and Methods**，查看所选**实例**的方法、只读属性和属性。

## 2. 语法行（Syntax line）约定

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所应用对象的路径。
- 方法签名（各参数的标识符与数据类型）写在圆括号内。`(Parameter:string)` 表示数据类型为 string 的参数；除常量外，也可使用所需类型的变量或返回所需类型的方法。
- 方括号内为**可选参数**，例如 `[,Parameter:boolean]` 表示可输入也可不输入的 boolean 参数。
- 参数有默认值时，签名会在参数后显示，例如 `:= false`。
- 方法有返回值时，签名会在箭头 `->` 后显示其数据类型，例如 `→ boolean`。

> **注意：** 在圆括号内使用表达式时必须输入圆括号 `(…)`；省略可能导致意外结果并打开 Debugger。

## 3. 方法列表

AssemblyStation 自身定义的方法共 4 个，均与“待删除 MU（MUs To Be Deleted）”表或“等待时间统计”相关。

### 3.1 musToBeDeleted

返回 `<Path>` 所指定 AssemblyStation 的 **MUs to Be Deleted** 表的内容。

- **类型：** Method
- **语法：** `<Path>.musToBeDeleted([Table:table]) → any`

**参数：** 可选参数 `Table`（数据类型 `table`）表示表的名称。

**返回值：** 数据类型为 `any`。若指定可选参数，返回值数据类型为 `boolean`；不指定可选参数则返回一个数组，包含待删除的 MU。

**示例：**

```
MyAssembly.musToBeDeleted
MyAssembly.musToBeDeleted(myEvalTable)
```

**参见：** `MUs To Be Deleted`、`muToBeDeleted`、`NumMUsToBeDeleted`

---

### 3.2 muToBeDeleted

返回 `<Path>` 所指定 AssemblyStation 的 **MUs to Be Deleted** 表中的指定 MU。

- **类型：** Method
- **语法：** `<Path>.muToBeDeleted(NumberOfTheMU:integer) → object`

**参数：** 参数 `NumberOfTheMU`（数据类型 `integer`）表示 MU 在表中的编号。

**返回值：** 数据类型为 `object`。

**示例：**

```
for var i := 1 to MyAssembly.NumMUsToBeDeleted
   print MyAssembly.muToBeDeleted(i)
next
```

**参见：** `MUs To Be Deleted`、`musToBeDeleted`、`NumMUsToBeDeleted`

---

### 3.3 statWaitingTimePerPredecessor

返回 `<Path>` 所指定 AssemblyStation 的某个前驱（predecessor）的安装部件等待时间总和。

- **类型：** Method
- **语法：** `<Path>.statWaitingTimePerPredecessor(Predecessor:integer) → time`

**参数：** 参数 `Predecessor`（数据类型 `integer`）表示前驱的编号。

> **注意：** 主要部件（main part）到达 AssemblyStation 所沿的前驱编号，其返回值恒为 0。

**返回值：** 数据类型为 `time`。

**示例：**

```
var i : integer
for var i := 1 to MyAssembly.NumPred
    print MyAssembly.statWaitingTimePerPredecessor(i)
next
```

**参见：** `Waiting [state, material flow objects]`、`Tab Statistics [AssemblyStation] > Waiting Times`

---

### 3.4 statWaitingTimeTable

返回一个表，其中包含 `<Path>` 所指定 AssemblyStation 的**所有**前驱的安装部件等待时间总和。

**备注：**

- Plant Simulation 只显示安装部件（mounting parts）的等待时间；主要部件（main part）的等待时间恒为 0。
- 仅当装配表（Assembly Table）设为 **None** 或 **Predecessors** 时才显示等待时间。
- 在示例中，主要部件沿 `SourceMainParts` 的 Connector 到达，由于只显示安装部件的等待时间，第一行显示 0。

- **类型：** Method
- **语法：** `<Path>.statWaitingTimeTable(WaitingTimes:table) → boolean`

**参数：** 参数 `WaitingTimes`（数据类型 `table`）表示表的名称。

**返回值：** 数据类型为 `boolean`。当装配表设为 `MU Types` 或 `Depends on Main MU` 时返回 `false`。

**示例：**

```
var myWaitingTimesTable: table
MyAssembly.statWaitingTimeTable(myWaitingTimesTable)
print MyAssembly.statWaitingTimeTable(myWaitingTimesTable)
```

**参见：** `Waiting [state, material flow objects]`、`Tab Statistics [AssemblyStation] > Waiting Times`

## 4. AssemblyStation 的只读属性

AssemblyStation 提供：

- 左侧目录中列出的只读属性；
- 所有对象的只读属性（Read-Only Attributes of All Objects）；
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）。

只读属性的值**只能查询、不能设置**，因为 Plant Simulation 在你查询的时刻实时计算该值。大多数情况下，只读属性对应于对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

## 目录说明

- `methods.md`：AssemblyStation 方法说明的 Markdown 版本（本总结的源文件）。
- `methods.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
