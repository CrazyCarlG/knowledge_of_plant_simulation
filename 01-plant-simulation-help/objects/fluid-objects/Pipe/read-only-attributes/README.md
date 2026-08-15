# Pipe — Read-Only Attributes（只读属性）摘要

本目录汇总了 Plant Simulation 流体对象 **Pipe（管道）** 的只读属性（Read-Only Attributes）说明。内容来源于本目录下的 `read-only-attributes.md`（其原始文本见 `read-only-attributes.txtx`）。本目录没有子文件夹，因此没有其他子目录 `README.md` 需要汇总。

## 概述

Pipe 提供以下只读属性（均以 SimTalk 访问）：

- 本目录左侧目录中所列的只读属性。
- **_Read-Only Attributes of All Objects**（所有对象共有的只读属性）。

只读属性的值**只能查询，不能设置**：Plant Simulation 会在你查询该属性的那一时刻计算其值。在大多数情况下，只读属性对应对象某个选项卡上一个不可用的对话框项，例如 **Statistics（统计）** 选项卡上的项目。

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods（显示属性和方法）** 窗口：

- 在 **Class Library（类库）** 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选 *Class* 的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例所在 *Frame* 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选 *Instance* 的方法、只读属性和属性。

查询只读属性值的示例：

```simtalk
print Pipe1.LengthOfPipe
```

## 关于表达式与参数（语法约定）

- 表达式 `<Path>` 表示方法所应用到的对象的路径。
- 方法的签名由标识符和参数的数据类型组成，并写在括号内。例如 `(Parameter:string)` 表示一个 `string` 数据类型的参数。除了常量值，也可以使用所需类型的变量或返回所需类型的方法。
- 可选参数写在方括号内。例如 `[,Parameter:boolean]` 表示可以但不必须输入该 boolean 参数。
- 若参数有默认值，签名会在参数之后显示默认值，例如 `:= false`。
- 若方法有返回值，签名会在箭头之后显示其数据类型，例如 `→ boolean`。

> **注意：** 对于嵌套在括号内的表达式 `(…)`，务必输入括号。省略括号可能导致意外结果并打开 Debugger（调试器）。

## 只读属性详解

### CurrentFlowrate [SimTalk]

返回由 `<Path>` 指定的 Pipe 中流经材料的**当前流量（current flow rate）**。

- **类型：** 只读属性
- **语法：** `<Path>.CurrentFlowrate → real`
- **可监视（Watchable）：** 该只读属性可监视。
- **返回值：** 数据类型为 `real`，单位为升/秒（liters per second）。

**示例：**

```simtalk
print Pipe1.CurrentFlowrate
```

**参见：** Current Flow Rate [文本框]

### CurrentMaterial [SimTalk] - Pipe

返回当前流经由 `<Path>` 指定的 Pipe 的**当前材料（Current Material）**。

**备注：** 名称不区分大小写，与对象的属性和方法名称一样。为节省内存并提高访问速度，所有使用这种不区分大小写字符串的位置都指向主内存中的同一个字符串。可见且意外的一个结果是：该字符串**第一次出现时的写法**决定了它的大小写形式。在 SimTalk 中可以使用 `~=` 运算符以不区分大小写的方式比较字符串（参见 Relational Operators，关系运算符）。

- **类型：** 只读属性
- **语法：** `<Path>.CurrentMaterial → string`
- **可监视（Watchable）：** 该只读属性可监视。
- **返回值：** 数据类型为 `string`。

**示例：**

```simtalk
print Pipe1.CurrentMaterial
```

**参见：** Current Material [Pipe]、Relational Operators（关系运算符）

### LengthOfPipe [SimTalk]

返回由 `<Path>` 指定的 Pipe 的**长度（Length）**。

- **类型：** 只读属性
- **语法：** `<Path>.LengthOfPipe → real`
- **返回值：** 数据类型为 `real`。即你在 Frame 中通过点击鼠标左键设置第一个点和最后一个点而插入的 Pipe 的长度。

**示例：**

```simtalk
print Pipe1.LengthOfPipe
```

## 属性（Attributes）相关说明

Pipe 还提供：

- 左侧目录中所列的属性（Attributes）。
- **_Attributes of All Objects**（所有对象共有的属性）。

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods** 窗口（操作方式见上文“概述”）。
