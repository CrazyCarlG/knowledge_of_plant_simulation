# README — Read-Only Attributes of the Generator

本目录包含 Generator（发生器）对象的只读属性相关文档，来源为 `read-only-attributes.md` 与 `read-only-attributes.txtx`。以下为内容摘要。

## 概述

Generator 提供 **所有对象的只读属性（Read-Only Attributes of All Objects）**。

- 只读属性的值**可以查询，但不能设置**。
- Plant Simulation 在你查询时计算该时刻的值。
- 大多数情况下，只读属性对应对象某个选项卡上不可用的对话框项，例如 **Statistics（统计）** 选项卡。

## 查看属性与方法

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods（显示属性与方法）** 窗口：

- 在 **类库（Class Library）** 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **类（Class）** 的方法、只读属性和属性。
- 按下 **F8** 键，或点击插入实例的 Frame 的 **Home** 功能区的 **Show Attributes and Methods**，可查看所选 **实例（Instance）** 的方法、只读属性和属性。

## 查询只读属性

查询只读属性值的示例：

```
print MyGenerator.UUID
```

## 方法/属性签名表示法

- `<Path>` 表示方法所适用对象的路径。
- 方法的签名（由标识符和参数数据类型组成）列在括号中。例如 `(Parameter:string)` 表示数据类型为 `string` 的参数。除常量值外，也可以使用所需类型的变量或返回所需数据类型的方法。
- **注意**：表达式中的括号必须输入，例如 `(…)`。遗漏括号可能导致意外结果并打开 Debugger。
- 可选参数列在方括号中。例如 `[,Parameter:boolean]` 表示可以（但非必须）输入该 boolean 参数。
- 若参数有默认值，签名会在参数后显示默认值，例如 `:= false`。
- 若方法有返回值，签名会在箭头 `->` 后显示其数据类型，例如 `-> boolean`。

## Generator 的属性

Generator 提供：

- 左侧目录中列出的属性。
- **所有对象的属性（Attributes of All Objects）**。

属性值可以设置，也可以获取，方式包括：对话框窗口中的复选框、文本框和下拉列表，或通过给相应属性赋值。

---

*Plant Simulation Help 11-4396 / 11-4397*
