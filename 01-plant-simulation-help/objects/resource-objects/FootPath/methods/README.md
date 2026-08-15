# FootPath Methods（方法）

本目录包含 FootPath（步行路径）对象的方法文档，源文件为 `methods.md` 与 `methods.txtx`（两者内容一致，`methods.txtx` 为 Plant Simulation 帮助系统的导出文本）。

> 本目录下没有子文件夹，因此没有额外的子级 `README.md` 内容。

## 概述

FootPath 对象提供：

- **Methods of All Objects（所有对象的通用方法）**。FootPath 自身没有额外定义的专属方法。

查看某对象全部方法、只读属性与属性，可打开 **Show Attributes and Methods（显示属性与方法）** 窗口：

- 在 Class Library 的右键菜单选择 **Show Attributes and Methods**，显示所选 **Class（类）** 的方法、只读属性与属性。
- 在插入了实例的 Frame 中，按 **F8** 键或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，显示所选 **Instance（实例）** 的方法、只读属性与属性。

## 语法行（Syntax Line）

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所作用对象的路径。
- 方法的签名（由参数标识符与数据类型组成）列于圆括号内。例如 `(Parameter:string)` 表示 `string` 类型的参数；除常量值外，也可使用所需类型的变量或返回所需类型的方法。
- 可选参数列于方括号内。例如 `[,Parameter:boolean]` 表示该 boolean 参数可省略。
- 若参数有默认值，签名会在参数后显示默认值（如上例中的 `:= false`）。
- 若方法有返回值，签名会在箭头后显示其数据类型（如上例中的 `→ boolean`）。

> **注意：** 请务必为括号内的表达式输入圆括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。

## 只读属性（Read-Only Attributes）

`methods.md` 末尾亦简要提及 FootPath 的只读属性：

- FootPath 提供 **Read-Only Attributes of All Objects（所有对象的通用只读属性）**。
- 只读属性的值**只能查询，不能设置**，其值由 Plant Simulation 在查询的时间点即时计算。
- 大多数只读属性对应对象某个选项卡（如 **Statistics（统计）** 选项卡）上不可用的对话框条目。

> 只读属性的详细说明参见同级目录 `read-only-attributes/`。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `methods.md` | FootPath 对象方法的完整说明文档（Markdown） |
| `methods.txtx` | 同一帮助内容的原始文本提取版（内容与 `methods.md` 等价） |
| `README.md` | 本汇总文件 |

本目录下无子文件夹。
