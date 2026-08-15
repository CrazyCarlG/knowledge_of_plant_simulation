# Quick Tour 目录说明

本目录包含 SimTalk 2.0 快速导览（A Quick Tour Through SimTalk 2.0）主题的文档，目前包含以下文件：

- `quick-tour.md` — A Quick Tour Through SimTalk 2.0 的 Markdown 版本
- `quick-tour.txtx` — 同一主题的原始文本版本（内容与 `quick-tour.md` 基本一致）

## 内容总结

本主题是对 **SimTalk 2.0** 的快速导览，概述了新特性与改进功能，并提供了足够的信息帮助读者开始编写 SimTalk 代码。导览中介绍的所有内容在 Plant Simulation 帮助的其余部分都有详细说明。

### 快速导览概述

- 导览涵盖三个主题：**简单值（Simple Values）**、**控制流（Control Flow）** 和 **声明默认参数（Declare Default Arguments）**。
- 作为第一个示例，SimTalk 通过 `print` 语句在 Method 中打印 "Hello World!"。
- SimTalk 语句末尾**不需要分号**（不同于 C、C++ 或 JavaScript）。

### 简单值（Simple Values）

使用局部变量和数组定义简单值。

- **局部变量**：使用 `var` 创建局部变量，例如 `var myVariable := 42`。
- **数据类型**：局部变量必须与所赋值的数据类型一致；当初始值信息不足或没有初始值时，在变量名后用冒号显式指定数据类型，例如 `var myVariable: real := 3.1415`。
- **数组**：使用方括号 `[]` 创建数组，并通过方括号内的索引访问元素，例如 `myIntegerArray[1]`；可用 `append` 添加元素。

### 控制流（Control Flow）

使用条件语句和循环定义控制流。

- **条件语句**：使用 `if` 和 `switch`。
- **循环**：使用 `for`、`while` 和 `repeat`。
- **括号可选**：条件或循环变量两边的括号可以输入，也可以省略。
- `switch` 适用于需要检查大量不同值的情况。
- `while` 重复执行代码块直到条件改变；`repeat ... until` 将条件放在末尾，确保循环至少执行一次。

### 声明默认参数（Declare Default Arguments）

在 SimTalk 2.0 中，可为 Method 的形参指定默认参数（又称可选参数）。

- 语法示例：`param x: integer := 123`。
- 若调用 Method 时未传入该参数，则形参使用默认值。
- 也可以只为部分形参指定默认参数；一旦某个形参有默认参数，其后的所有形参也必须有默认参数。

#### 默认参数的允许值

- 默认参数只接受**常量值**：数字、字符串常量、布尔常量 `true`/`false`、`void` 和 `pi`。
- 数据类型为 `object`、`table`、`list`、`stack`、`queue` 和 `any` 的形参只能使用 `void` 作为默认参数。
- 数据类型为 `date` 和 `dateTime` 的形参**不能**有默认参数。
- 数据类型为 `array` 的形参可使用空数组 `[]` 或空 JSON 对象 `{}` 作为默认参数。

### 备注（Note）

- 在按 SimTalk 1.0 记法编写的现有 Method 中点击，会自动将源代码转换为正确的 SimTalk 2.0 记法。
- 单击 Debugger 功能区选项卡上的 **Find Outdated Functions**，可在仿真模型中所有 Method 的源代码中查找过时的方法、属性和函数。

### 参见（See Also）

- Operators and Expressions > Arithmetic Operators
- Declare Local Variables in the Source Code
- Constant Values
- Colors for Syntax Highlighting
