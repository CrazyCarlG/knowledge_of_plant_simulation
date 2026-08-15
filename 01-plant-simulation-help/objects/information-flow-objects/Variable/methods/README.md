# Variable 对象 — Methods（方法）

本目录包含 **Variable 对象**（信息流对象）的方法（Methods）说明。文档描述可通过 SimTalk 调用的、作用于 Variable 对象的方法与运算符。

> 源文件：`methods.md`（内容详见该文件）；原始导出文本：`methods.txtx`。

## 读取 Variable 的内容

要访问 `<Path>` 指定的 Variable 内容，直接使用其名称即可。

语法：

```simtalk
<Path>
```

示例：

```simtalk
MyTable[1,1] := MyVariable
```

## 方法概述

Variable 对象提供目录表（左侧）中列出的方法，以及所有对象的通用方法（*Methods of All Objects*）。

> **注意：** 只能通过引用运算符 `&` 访问作用于 Variable 对象本身的方法；没有该运算符时，方法会作用于 Variable 的内容。

示例：

```simtalk
.MyPlant.&MyVariable.openDialog
```

### 参见

- 给 Variable 赋值（Assigning a Value to a Variable）
- 调用 Variable 的内容（Calling the Contents of a Variable）
- 读取 Variable 的内容（Reading the Contents of a Variable）
- 所有对象的通用方法（The Methods of All Objects）

要查看对象的所有方法、只读属性和属性，打开窗口 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选 Class 的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选 Instance 的方法、只读属性和属性。

单个方法语法行的示例可能如下：

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所作用对象的路径。
- 方法的签名（由参数的标识符和数据类型组成）列在括号内。例如 `(Parameter:string)` 表示一个 string 类型的参数。除了常量值，也可以使用所需类型的变量或返回所需数据类型的方法。
- **注意：** 对括号内的表达式，务必输入括号 `(…)`。不输入可能导致意外结果并打开调试器（Debugger）。
- 可选参数列在方括号内。例如 `[,Parameter:boolean]` 表示可以但不必输入该 boolean 参数。
- 若参数有默认值，签名会在参数之后显示默认值，如上例中的 `:= false`。
- 若方法有返回值，签名会在箭头 `->` 之后显示其数据类型，如上例中的 `→ boolean`。

---

## & [SimTalk] - Variable

`&` 运算符/引用运算符返回 Variable 的引用，而非其内容。

- **备注：** `&` 运算符适用于 SimTalk 2.0。
- **类型：** 方法/运算符（Method/operator）

**语法：**

```simtalk
&Variable → object
<PathToVariable>.&Variable → object
```

**返回值：** 数据类型为 `object`。

**示例：**

```simtalk
print &myVariable.location // 可能返回 .Models.Model.Frame
```

**参见：** & [SimTalk] - reference operator

---

## create [SimTalk] - Variable

为 `<Path>` 指定的 Variable 创建一个不含内容的数据结构。

- **备注：** 数据类型为 `stack`、`queue`、`list` 和 `table` 的 Variable 本身并不包含数据，而是保存对相应数据结构的引用。使用这些类型的 Variable 之前，Plant Simulation 必须先创建该数据结构，之后才能访问实际数据。任何已存在的引用都会被覆盖。
- **类型：** 方法/运算符（Method/operator）

**语法：**

```simtalk
<Path>.create
```

**示例：**

```simtalk
orderList.create -- 创建名为 orderList 的 Variable
orderList.insert(1,"A-No. 4712")
```

---

## getStatisticsTable [SimTalk] - Variable

返回由引用运算符 `<&>` 指定的 Variable 的统计表。

- **备注：** 若 Variable 的数据类型为 `string`，Plant Simulation 始终以小写字母在第一列显示字符串值。
- **类型：** 方法（Method）

**语法：**

```simtalk
<&>Variable.getStatisticsTable([TargetTable:table]) → any
```

**参数：** 可选参数 `TargetTable`（数据类型 `table`）指定方法 `getStatisticsTable` 将统计数据写入的表。

**返回值：** 数据类型为 `any`。

- 若已激活统计收集，返回 `true`。
- 若已停用统计收集，返回 `false`，此时表保持不变。
- 若已激活统计收集且未指定可选参数，返回包含统计数据的表。
- 若已停用统计收集，返回 `void`。

**示例：**

```simtalk
&MyVariable.getStatisticsTable(mystatisticstable)
// 将统计值写入名为 mystatisticstable 的表。
// 若已激活统计收集，返回值为 true。
// 若已停用，返回值为 false，此时表保持不变。

&MyVariable.getStatisticsTable
// 若已激活统计收集，返回值为统计表。
// 若已停用，返回值为 void。
```

**参见：** Statistics Table [Variable]

---

## increment [SimTalk] - Variable

为引用运算符 `<&>` 指定的 Variable 增加一个值。

- **备注：** 该方法仅适用于数值数据类型。它适用于 Variable 对象和用户自定义属性。
- **类型：** 方法（Method）

**语法：**

```simtalk
<&>Variable.increment
<&>Variable.increment(Value:integer)
```

**参数：**

- 不带参数的方法 `increment` 为 Variable 加 `1`。
- 方法 `increment(Value)` 将参数 `Value`（数据类型 `integer`）指定的值加到 Variable 上。

**示例：**

```simtalk
x := &MyVariable.increment(-3) // 等同于
                               // Variable := Variable - 3 x := Variable
```

---

## ref [SimTalk] - Variable

`ref(Path)` 运算符返回由 `<Path>` 指定的 Variable 的引用，而非其内容。

- **备注：** `ref` 运算符适用于 SimTalk 1.0。
- **类型：** 方法/运算符（Method/operator）

**语法：**

```simtalk
ref(Path) → object
```

**返回值：** 数据类型为 `object`。

**示例：**

```simtalk
print ref(MyVariable).location
```

---

## rollDice [SimTalk]

生成一个新的随机数，并保存到 `<Path>` 指定的 Variable 中。

- **备注：** `rollDice` 适用于数据类型为 `randtime` 的 Variable。
- **类型：** 方法（Method）

**语法：**

```simtalk
<Path>.rollDice → time
```

**返回值：** 数据类型为 `time`。

**示例：**

```simtalk
for var i := 1 to 10
   variable.rolldice // 新的随机数
   print variable    // 输出随机数
next
```

---

## Variable 的只读属性

Variable 对象提供：

- 只读属性 `asString` [SimTalk] - Variable。
- 所有对象的通用只读属性（The Read-Only Attributes of All Objects）。

> **注意：** 只能通过引用运算符 `&` 访问作用于 Variable 对象本身的只读属性。

可以查询只读属性的值，但不能设置它们，因为 Plant Simulation 会在查询的时间点计算该值。在大多数情况下，只读属性对应于对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。

要查看对象的所有方法、只读属性和属性，打开窗口 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选 Class 的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选 Instance 的方法、只读属性和属性。

要查询某个只读属性的值，例如可输入：

```simtalk
print &MyVariable.AsString
```
