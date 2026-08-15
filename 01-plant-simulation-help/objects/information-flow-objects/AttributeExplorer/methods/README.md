# AttributeExplorer 的方法（Methods）— 概述

本目录汇总了 Plant Simulation 中 **AttributeExplorer（属性浏览器）** 对象的**方法**帮助文档。目录内包含两个文件，内容一致：

- `methods.md` — 结构化的 Markdown 版本帮助文档。
- `methods.txtx` — Siemens Plant Simulation Help 的原始提取文本（含页码、版权信息等）。

> 本目录下没有子文件夹（无子级 README.md）。

## 核心要点

AttributeExplorer 提供 **Methods of All Objects（所有对象的方法）** 以及 **_Read-Only Attributes of All Objects（所有对象的只读属性）**。也就是说，本页并不单独列出 AttributeExplorer 特有的方法，而是说明它继承/提供了一套通用的方法与只读属性集合。

## 查看方法与属性

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在 **Class Library（类库）** 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选 **Class** 的方法、只读属性与属性；
- 在插入实例的 Frame 的 **Home** 功能区选项卡上，按 **F8** 键或点击 **Show Attributes and Methods**，可显示所选 **Instance** 的方法、只读属性与属性。

## 方法语法（Syntax）

单个方法的语法行示例：

```text
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

各部分的含义：

- `<Path>` — 表示该方法所作用对象的路径；
- 括号 `(…)` — 列出方法的签名，由参数标识符与数据类型组成，例如 `(Parameter:string)` 表示一个 `string` 类型的参数。除常量值外，也可使用所需类型的变量或返回该类型的方法；
- 方括号 `[…]` — 表示可选参数，例如 `[,Parameter:boolean]` 表示可以（但不必）输入该布尔参数；
- `:= false` — 表示参数具有默认值，签名在参数后显示其默认值；
- `->` / `→` — 表示方法具有返回值，箭头后为其数据类型，例如 `→ boolean`。

> **注意**
> 务必为嵌套在括号内的表达式 `(…)` 输入括号。遗漏括号可能导致意外结果并打开 Debugger。

## 只读属性（Read-Only Attributes）

AttributeExplorer 提供 **_Read-Only Attributes of All Objects（所有对象的只读属性）**：

- 只读属性**只能查询、不能设置**，因为 Plant Simulation 会在你查询的时间点实时计算其值；
- 在大多数情况下，只读属性对应对象某个选项卡（如 **Statistics** 选项卡）上不可用的对话框项；
- 查看方式与上述方法相同：打开 **Show Attributes and Methods** 窗口，或通过 Class Library 上下文菜单选择 **Show Attributes and Methods**。

## 参考

- 相关主题：Methods of All Objects、Read-Only Attributes of All Objects、Show Attributes and Methods。
