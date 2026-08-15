# Foundations & Motivation

本目录总结了 SimTalk 语言基础与动机（Foundations & Motivation）的核心内容，主要来源为 `foundations-motivation.md` 与 `foundations-motivation.txtx`。

## 1. 引用参数（Reference Parameters）

- 使用关键字 `byref` 声明的引用参数**不能**有默认参数（default argument）。

## 2. SimTalk 概述（General Access to SimTalk）

- SimTalk 扩展了对仿真模型的建模与控制能力。每个对象都有内置属性提供众多有用功能。
- 若模型需要更详细或完全不同的属性，可在 SimTalk 中编写。可将 **Method** 对象与内置对象结合，创建高度复杂的模型。
- 在 **Method** 对象的实例中输入语句，由内置 **Interpreter** 解释执行。按 **F7** 和 **F5** 键执行源码。
- **Copilot** 可协助在 Method 中编写源码。
- 运行仿真时，Interpreter 逐行执行源码并执行所编程的动作。
- SimTalk 对 Method 源码中方法、属性、只读属性的名称**通常不区分大小写**。

### SimTalk 2.0 与 SimTalk 1.0

- SimTalk 2.0 相比 1.0 更快、更简单、更不易出错，新建仿真模型默认使用 2.0 语法。
- 切换方式：点击 Method 的 Tools 功能区选项卡上的 **New Syntax**。
- 若希望所有新 Method 默认使用 2.0，可在 Class Library 的 Method 类中激活 **New Syntax**。
- 可在模型中自由混合 2.0 与 1.0 语法，无需重写现有源码。
- 在已有 1.0 Method 中点击 **New Syntax** 会自动转换为 2.0。
- 转换模型中所有 Method：按住 Shift，右键 Class Library 中的 **Basis** 对象，点击 **Convert all Methods to New Syntax**。

## 3. 为何使用 SimTalk 2.0？（Why Use SimTalk 2.0?）

2.0 提供大量改进，应尽可能使用 2.0；1.0 的支持未来可能终止。主要改进包括：

- **行控制语法（Line-controlled syntax）**：语句末尾无需分号 `;`，每行一条语句；解释器自动判断语句是否未完成并延续到下一行。可在同一行用分号分隔多条语句。
- **简化的主体语法（Simplified body syntax）**：1.0 需要 `is do end` 关键字，2.0 不再需要。2.0 使用 `param` 声明参数、`var` 声明局部变量、`->` 声明返回值。
- **改进的方法与全局变量引用**：1.0 用 `ref` 引用，2.0 用前导 `&` 引用，例如 `var o:object := &Method`。
- **新的 div/mod 运算符**：1.0 用 `//` 表示整数除法、`\\` 表示取模；2.0 用关键字 `div` 和 `mod`。
- **改进的字符串字面量**：2.0 中反斜杠 `\` 只用于转义双引号和换行，不再转义另一个反斜杠。
- **时间字面量（Time literals）**：以数字开头且必须包含一个或多个冒号，可含小数点及小数位。
- **JSON 字面量**：用花括号 `{}` 括起，元素间以逗号分隔，每个元素由字符串字面量、冒号和 JSON 值组成。
- **默认参数（Default arguments）**：在参数声明后键入赋值运算符与默认值，例如 `param x := 0`。
- **简化的控制流语句**：`if-end`（代替 `if-then-end`）、`for-next`（代替 `for-loop-next`）、`switch-case-end`（代替 `inspect-when-then-end`）、`while-end`（代替 `while-loop-end`）。`then`、`loop` 关键字可选；新增 `continue` 跳过本次循环剩余部分。
- **修改的"约等于"运算符**：`~=`（代替 `==`）、`<~=`（代替 `<==`）、`>~=`（代替 `>==`）。
- **新的复合赋值运算符**：`x += y`（即 `x := x + y`）、`x -= y`、`x *= y`。
- **改进的列表与表格语法**：列表区间仅用花括号 `{}`，不再支持 1.0 的反引号 `` `[] `` 语法；用 `[]` 读取一维列表元素（StackFile、QueueFile 同样适用）；用 `remove` 从 DataList 读取并移除元素。
  - 1.0 中用 `[]` 读取 DataList 单元格会**读取并移除**内容（剩余单元格上移），赋值会插入（现有单元格下移）。
  - 2.0 中用 `[]` 读取内容会保留在原位，赋值会覆盖现有单元格，使 DataList 行为等同于单列 DataTable。

## 4. SimTalk 简介（Introducing SimTalk）

SimTalk 由以下部分组成：

- **内置方法、只读属性、属性**：由内置 Plant Simulation 对象提供，由软件工程师定义。
- **控制结构与语言结构**：通过循环与条件分支控制方法执行顺序。

### 语法符号约定

- `<Path>` 表示方法所应用对象的路径。
- 签名（标识符与参数数据类型）列在括号内，如 `(Parameter:string)` 表示字符串参数；可用相应类型的变量或返回该类型的方法代替常量。
- 可选参数列在方括号内，如 `[,Parameter:boolean]`。
- 参数有默认值时，签名在参数后显示默认值。
- 方法有返回值时，签名在箭头 `->` 后显示数据类型。
- 必须为括号内的表达式 `(…)` 输入括号，省略可能导致意外结果并打开 Debugger。

### 查看方法与属性

打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选 **Class** 的方法与属性。
- 按 **F8** 或点击 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，查看所选 **Instance** 的方法与属性。

### Help 中的拼写约定

- 对象名以大写字母开头且斜体（如 *ParallelStation*、*Station*）。
- 方法名以小写字母开头，后续每个词首字母大写（如 *derive*、*updateDialog*）。
- 属性与只读属性名以大写字母开头（如 *CreationTableActive*、*ReferenceTime*）。
- `MU` 与 `part` 可互换使用；`Part` 首字母大写时指类型为 Part 的 MU。
- SimTalk 对方法、属性、只读属性名不区分大小写（如 `CreationTableActive`、`creationtableactive`、`CREATIONTABLEACTIVE` 等价）。
- SimTalk 支持英语与德语；德语 Help 中英文名与德语名以斜杠分隔（如 *EnergieAktiv [SimTalk] / EnergyActive*）。

## 5. 属性、只读属性、方法与函数

### 属性（Attributes）

- 属性用于设置或获取对象属性，涵盖内置属性、用户自定义属性、局部变量及 Variable 类型对象。
- 示例：`EventController.AbsTimeFormat := true`；`print EventController.AbsTimeFormat // returns true`。

### 方法（Methods）

- 方法是调用时执行任务的源码块，通常有参数、有副作用，可返回值。
- 功能：从对象获取信息并返回值；计算值；启动一个或多个控制对象行为的动作。
- 示例：`TableVariable := EventController.getEventList(-1)`；`MyStation.addObserver("occupied", &myMethod)`。

### 只读属性（Read-only Attributes）

- 只读属性返回对象属性值，不期望参数、无副作用、返回一个值。
- 示例：
  ```simtalk
  param sensorID: integer, Front: boolean
  if @.ID = 1
     @.Speed := 0
     print EventController.SimTime, " The first Transporter stopped."
  end
  ```

### 函数（Functions）

- 函数是一段通用、与具体对象无关的源码。
- 示例：
  ```simtalk
  if currentEventCtl /= VOID
     print "simulation running in frame", currentEventCtl.location
     print "simulation running in frame", root
  end
  ```

## 参见（See Also）

- Declare Parameters（声明参数）
- Colors for Syntax Highlighting（语法高亮颜色）
- SimTalk Access to 3D Functions（SimTalk 访问 3D 函数）
- String [SimTalk] - value
- 视频：https://youtu.be/5t-wLNmKpbU
