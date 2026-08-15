# Read-Only Attributes of the ContinuousMixer — 目录说明

本目录包含 ContinuousMixer 对象的**只读属性（Read-Only Attributes）**相关文档。

## 内容概述

ContinuousMixer 提供以下只读属性：

- **流体对象的只读属性**（Read-Only Attributes of the Fluid Objects）
- **所有对象的只读属性**（Read-Only Attributes of All Objects）

只读属性的值只能**查询**，不能**设置**。Plant Simulation 会在你查询属性的时间点计算其值。大多数情况下，只读属性对应对象某个选项卡上不可用的对话框项，例如 Statistics（统计）选项卡上的项目。

## 文档中说明的主要内容

### 1. 方法语法约定（Method Syntax Conventions）

方法语法行示例：

```text
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所应用对象的路径。
- 方法签名（由参数标识符和数据类型组成）列在括号内。例如 `(Parameter:string)` 表示一个 `string` 类型的参数。除常量值外，也可以使用所需类型的变量或返回所需类型的方法。
- 可选参数放在方括号内，例如 `[,Parameter:boolean]` 表示该布尔参数可以输入，也可以不输入。
- 若参数有默认值，签名会在参数后显示默认值，例如 `:= false`。
- 若方法有返回值，签名会在箭头 `->`（`→`）后显示其数据类型，例如 `→ boolean`。

> **注意：** 务必输入嵌套括号表达式中的括号 `(…)`。否则可能导致意外结果并打开调试器（Debugger）。

### 2. 查看属性和方法

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods**（显示属性和方法）窗口：

- 在 Class Library（类库）的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类的方法、只读属性和属性。
- 按 **F8** 键，或点击插入了实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选实例的方法、只读属性和属性。

### 3. 查询只读属性

查询只读属性的值，例如：

```text
print ContinuousMixer.Full
```

## 附注：ContinuousMixer 的属性（Attributes）

ContinuousMixer 同时提供：

- 左侧目录中列出的属性
- 流体对象的属性（Attributes of the Fluid Objects）
- 所有对象的属性（Attributes of All Objects）

查看方式同上，打开 **Show Attributes and Methods** 窗口即可。

## 目录文件说明

| 文件 | 说明 |
| --- | --- |
| `read-only-attributes.md` | ContinuousMixer 只读属性的 Markdown 版本文档 |
| `read-only-attributes.txtx` | 同一内容的纯文本版本文档 |
