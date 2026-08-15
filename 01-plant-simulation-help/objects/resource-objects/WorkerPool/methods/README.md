# WorkerPool 的方法（Methods）— 目录说明

本目录 (`methods`) 汇总了 Siemens Tecnomatix Plant Simulation 中 **WorkerPool（工人池 / 员工休息室）** 资源对象的方法（Methods）帮助文档。目录内包含以下文件：

- `methods.md` — WorkerPool 对象方法的完整 Markdown 文档（正式帮助内容）。
- `methods.txtx` — 同一帮助内容的原始文本提取版（对应 Plant Simulation Help pp. 11-3102 至 11-3113，包含页码、页眉页脚等排版痕迹，内容与 `methods.md` 等价）。

> 本目录下没有子文件夹，因此没有额外的子级 `README.md` 内容。

---

## 内容概要

本目录介绍 WorkerPool 提供的 **方法（Methods）**。WorkerPool 除提供目录左侧列出的方法外，还提供 **Methods of All Objects（所有对象的通用方法）**。查看对象的全部方法、只读属性与属性：打开 **Show Attributes and Methods** 窗口（Frame 实例按 **F8**，或在 Class Library 上下文菜单中选择）。

### 语法行约定（Syntax Line Conventions）

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所作用对象的路径。
- 方法的签名（参数标识符与数据类型）写在圆括号内。除了常量值，也可使用所需类型的变量或返回所需类型的方法。
- 圆括号内的表达式必须输入括号 `(…)`，否则可能产生意外结果并打开 Debugger。
- 可选参数写在方括号内：`[,Parameter:boolean]` 表示可输入也可不输入该布尔参数。
- 参数带默认值时，签名在参数后显示默认值（`:= false`）。
- 方法带返回值时，签名在箭头后显示其数据类型（`→ boolean`）。

---

## WorkerPool 的方法一览

| 方法 | 说明 | 语法 |
| --- | --- | --- |
| `getAssignedWorker` | 返回 WorkerPool 中指定编号的已分配 Worker。 | `<Path>.getAssignedWorker(No:integer) -> object` |
| `getAssignedWorkersTable` | 返回包含 WorkerPool 已分配 Worker 的表；省略可选参数时返回数组。 | `<Path>.getAssignedWorkersTable([AssignedWorkers:table]) -> any` |
| `getIdleWorker` | 返回 WorkerPool 中第一个空闲 Worker（并将其 `IsIdle` 置为 `false`）；无空闲时返回 `VOID`。 | `<Path>.getIdleWorker -> object` |
| `getWorkersToCreateTable` | 返回 WorkerPool 的 Workers to Create 表并写入指定表。 | `<Path>.getWorkersToCreateTable(WorkersToCreateTable:table/void[, byref Inherited:boolean])` |
| `getWorkersToCreateTableRow` | 读取/设置 Workers to Create 表某一行的各项设置。 | `<Path>.getWorkersToCreateTableRow(row:integer).<subattribute>` |
| `getWorkingWorkersTable` | 返回包含 WorkerPool 正在工作的 Worker 的表。 | `<Path>.getWorkingWorkersTable(WorkingWorkers:table)` |
| `setWorkersToCreateTable` | 设置 WorkerPool 的 Workers to Create 表名称（传 `void` 激活继承）。 | `<Path>.setWorkersToCreateTable(WorkersToCreateTable:table/void)` |

---

## 方法详解

### getAssignedWorker [SimTalk]

返回 WorkerPool（由 `<Path>` 指定）中由编号指定的已分配 Worker。

- **类型**：Method
- **语法**：`<Path>.getAssignedWorker(No:integer) -> object`
- **参数**：`No`（integer）—— 已分配 Worker 的编号。
- **返回值**：`object`

**示例：**

```simtalk
print MyWorkerPool.getAssignedWorker(2)
-- might, for example, return .Resources.John:2
```

---

### getAssignedWorkersTable [SimTalk]

返回包含 WorkerPool（由 `<Path>` 指定）已分配 Worker 的表。

- **类型**：Method
- **语法**：`<Path>.getAssignedWorkersTable([AssignedWorkers:table]) -> any`
- **参数**：可选参数 `AssignedWorkers`（table）—— 写入 Worker 的表的名称。若省略该可选参数，Plant Simulation 返回一个包含已分配 Worker 的数组。
- **返回值**：`any`

**示例：**

```simtalk
MyWorkerPool.getAssignedWorkersTable(MyAssignedWorkersTable)
MyWorkerPool.getAssignedWorkersTable
```

---

### getIdleWorker [SimTalk]

返回 WorkerPool（由 `<Path>` 指定）中的第一个空闲 Worker。

- **备注**：`getIdleWorker` 返回第一个 `IsIdle` 为 `true` 的空闲 Worker，并将其 `IsIdle` 置为 `false`。不再需要该 Worker 时，可将其送回 WorkerPool 并把 `IsIdle` 置回 `true`。
- **类型**：Method
- **语法**：`<Path>.getIdleWorker -> object`
- **返回值**：`object` —— WorkerPool 中的第一个空闲 Worker；若没有 Worker 空闲则为 `VOID`。

**示例：**

```simtalk
.Resources.WorkerPool.getIdleWorker
```

---

### getWorkersToCreateTable [SimTalk]

返回 WorkerPool（由 `<Path>` 指定）的 Workers to Create 表，并将其写入一个表。

- **备注**：Plant Simulation 始终相对于插入 WorkerPool 的 Frame 解析相对路径。若仿真期间无法解析 Scope 数组中的路径，将显示错误消息并询问是否停止仿真。Home Location 同理。
- **类型**：Method
- **语法**：`<Path>.getWorkersToCreateTable(WorkersToCreateTable:table/void[, byref Inherited:boolean])`
- **参数**：
  - `WorkersToCreateTable`（table）—— 包含待创建 Worker 的表的名称。表的列须为 table 数据类型。若传入可选参数 `Inherited`，此参数可指定为 `VOID`——此时 `WorkersToCreateTable` 被忽略。
  - `Inherited`（boolean，可选）—— 一个局部变量：若 WorkerPool 的 WorkersToCreateTable 被继承则设为 `true`，否则为 `false`。

**示例：**

```simtalk
var rt: table                             // read the Workers to Create table
MyWorkerPool.getWorkersToCreateTable(rt)  // set the new amount
rt [2,1]:= AmountOfWorkers                // name of a Variable
// assign the Workers to Create table to the WorkerPool
MyWorkerPool.setWorkersToCreateTable(rt)
```

---

### getWorkersToCreateTableRow [SimTalk] - WorkerPool

方法 `getWorkersToCreateTableRow` 的子属性用于读取/设置 WorkerPool（由 `<Path>` 指定）的 Workers to Create 表中各行的各项设置。

- **备注**：Plant Simulation 始终相对于插入 WorkerPool 的 Frame 解析相对路径。若仿真期间无法解析 Scope 数组中的路径，将显示错误消息并询问是否停止仿真。Home Location 同理。
- **类型**：Method
- **语法**：

```
<Path>.getWorkersToCreateTableRow(row:integer).AdditionalServices:string[]
<Path>.getWorkersToCreateTableRow(row:integer).Amount:integer
<Path>.getWorkersToCreateTableRow(row:integer).Efficiency:real
<Path>.getWorkersToCreateTableRow(row:integer).HomeLocation:path
<Path>.getWorkersToCreateTableRow(row:integer).Scope:array
<Path>.getWorkersToCreateTableRow(row:integer).Shift:string
<Path>.getWorkersToCreateTableRow(row:integer).Speed:speed
<Path>.getWorkersToCreateTableRow(row:integer).Worker:object
```

- **参数**：
  - `row`（integer）—— 要设置属性的 Workers to Create 表中的行。
  - `AdditionalServices`（string 数组）—— Worker 可提供的额外服务。
  - `Amount`（integer）—— 要创建的 Worker 数量。
  - `Efficiency`（real）—— Worker 的效率。
  - `HomeLocation`（path）—— Worker 完成当前工作后要前往的 Workplace 路径。
  - `Scope`（array）—— Worker 可被调配到的物料流对象的路径（也包含子 Frame）。
  - `Shift`（string）—— Worker 工作的班次（在关联的 ShiftCalendar 中定义班次）。
  - `Speed`（speed）—— Worker 行走的速度。
  - `Worker`（object）—— WorkerPool 用作待创建 Worker 模板的 Worker 类。

**示例：**

```simtalk
MyWorkerPool.getWorkersToCreateTableRow(1).AdditionalServices := ["drill1", "drill2", "drill3"]
```

---

### getWorkingWorkersTable [SimTalk]

返回包含 WorkerPool（由 `<Path>` 指定）正在工作的 Worker 的表。

- **类型**：Method
- **语法**：`<Path>.getWorkingWorkersTable(WorkingWorkers:table)`
- **参数**：`WorkingWorkers`（table）—— 写入正在工作的 Worker 的表的名称。

**示例：**

```simtalk
MyWorkerPool.getWorkingWorkersTable(MyWorkingWorkers)
```

---

### setWorkersToCreateTable [SimTalk]

设置 WorkerPool（由 `<Path>` 指定）的 Workers to Create 表的名称。

- **备注**：Plant Simulation 始终相对于插入 WorkerPool 的 Frame 解析相对路径。若仿真期间无法解析 Scope 数组中的路径，将显示错误消息并询问是否停止仿真。Home Location 同理。
- **类型**：Method
- **语法**：`<Path>.setWorkersToCreateTable(WorkersToCreateTable:table/void)`
- **参数**：`WorkersToCreateTable`（table）—— Workers to Create 表。在表中输入待创建 Worker 的名称、班次名称、数量、速度、效率、Home Location、Scope 与 Additional Services。

  为参数指定 `void` 可激活 WorkerPool 中 Workers to Create 表的继承，而不是用输入的 Worker 填充该表。

- **注意事项**：
  - 对 Workers to Create 表的更改须在**模型初始化之前**进行，才会应用到仿真运行。
  - 名称不区分大小写（与对象属性、方法名一样）。为节省内存并提高访问速度，所有使用这种不区分大小写字符串的位置都指向主内存中的同一字符串——可见且出人意料的结果是：**首次出现**的字符串决定了它的大小写写法。
  - 在 SimTalk 中可用 `~=` 运算符进行不区分大小写的字符串比较。

**示例：**

```simtalk
MyWorkerPool.setWorkersToCreateTable(MyWorkersToCreateTable)
```

```simtalk
var rt: table                                // read the Workers to Create table
MyWorkerPool.getWorkersToCreateTableRow(rt)  // set the new amount
rt [2,1]:= AmountOfWorkers                   // name of a Variable
                                             // assign the Workers to Create table
                                             // to the WorkerPool
MyWorkerPool.setWorkersToCreateTable(rt)
```

---

## WorkerPool 的只读属性（Read-Only Attributes）

WorkerPool 提供只读属性。可查询只读属性的值，但**不能设置**它们——Plant Simulation 在查询的时刻计算其值。大多数情况下，只读属性对应于对象某一选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

---

## SimTalk 参考汇总

方法 / 相关 SimTalk 项：

- `getAssignedWorker`、`getAssignedWorkersTable`、`getIdleWorker`
- `getWorkersToCreateTable`、`getWorkersToCreateTableRow`（及其子属性 `AdditionalServices`、`Amount`、`Efficiency`、`HomeLocation`、`Scope`、`Shift`、`Speed`、`Worker`）
- `getWorkingWorkersTable`、`setWorkersToCreateTable`
- 相关属性：`IsIdle`、`NumIdleWorkers`（Worker）

---

## 参见（See also）

- Methods of All Objects（所有对象的通用方法）
- Show Attributes and Methods（显示属性与方法）
- Read-Only Attributes of the WorkerPool（WorkerPool 的只读属性）
- WorkerPool [object]（`general` 目录）
