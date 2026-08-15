# Generator - Methods

本目录包含 Generator（生成器）对象的方法与只读属性相关文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `methods.md` | Markdown 格式的 Generator 方法与只读属性说明 |
| `methods.txtx` | 同一内容的纯文本提取版本 |

## 内容概要

### Methods of the Generator（Generator 的方法）

Generator 对象提供 **所有对象的方法（Methods of All Objects）**。

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods（显示属性和方法）** 窗口：

- 在 Class Library（类库）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 在插入了实例的 Frame 中按下 **F8** 键，或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。

### 单个方法的语法（Syntax）

方法语法行示例如下：

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所应用对象的路径。
- 方法的 **签名（signature）** 由参数标识符和数据类型组成，列于括号中。例如 `(Parameter:string)` 表示一个 `string` 类型的参数。除常量值外，也可使用所需类型的变量或返回所需数据类型的方法。
- 可选参数列于方括号内，如 `[,Parameter:boolean]` 表示该 boolean 参数可以输入，也可以不输入。
- 若参数有默认值，签名会在参数后显示默认值，如上例中的 `:= false`。
- 若方法有返回值，签名会在箭头 `->`（即 `→`）之后显示其数据类型，如上例中的 `boolean`。

> **注意**
> 括号内表达式务必输入括号 `(…)`，否则可能导致意外结果并打开 Debugger。

### Read-Only Attributes of the Generator（Generator 的只读属性）

Generator 对象提供 **所有对象的只读属性（_Read-Only Attributes of All Objects）**。

- 只读属性的值可以查询，但无法设置，因为 Plant Simulation 会在查询时计算该值。
- 大多数情况下，只读属性对应对象某个选项卡上不可用的对话框项，例如 **Statistics（统计信息）** 选项卡。
- 查看方式与查看方法相同：打开 **Show Attributes and Methods** 窗口，并通过 Class Library 上下文菜单查看所选类的只读属性。

## 参考信息

- 原文出处：Plant Simulation Help，页码 11-4395 至 11-4396，© 2026 Siemens。
