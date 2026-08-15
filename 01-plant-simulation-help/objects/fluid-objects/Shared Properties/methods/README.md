# Methods of the Fluid Objects（流体对象的方法）

本目录包含流体对象（Fluid Objects）"共享属性（Shared Properties）→ 方法（Methods）"部分的帮助文档，对应源文件 `methods.md`（及其原始导出文本 `methods.txtx`）。本目录下暂无子文件夹。

## 内容概述

流体对象提供以下方法：

- **所有对象的方法**（The Methods of All Objects）
- **定义故障的方法**（The _Methods for Defining Failures）
- **导入器的方法**（The _Methods of the Importer）

此外，各流体对象各自的子章节中还会列出该对象额外的方法。

### 查看方法、只读属性与属性

要查看某个对象的所有方法（methods）、只读属性（read-only attributes）和属性（attributes），打开 **Show Attributes and Methods** 窗口。以对象 Station 为例：

- 在 **Class Library** 的右键菜单中选择 **Show Attributes and Methods**，可查看所选**类（Class）**的方法、只读属性和属性。
- 按 **F8** 键，或点击 **Frame** 中 **Home** 功能区选项卡上的 **Show Attributes and Methods**，可查看所选**实例（Instance）**的方法、只读属性和属性。

### 语法行（Syntax Line）

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所作用对象的路径。
- 括号内列出方法签名，由参数标识符和数据类型组成。例如 `(Parameter:string)` 表示一个 string 类型的参数。除了常量值，也可以使用所需类型的变量或返回所需类型的方法。
- 可选参数放在方括号内。例如 `[,Parameter:boolean]` 表示该 boolean 参数可以输入，也可以不输入。
- 若参数有默认值，签名会在参数后显示默认值，如上例中的 `:= false`。
- 若方法有返回值，签名会在箭头 `->`（即 `→`）后显示返回类型，如上例中的 `→ boolean`。

> **注意**
> 请务必为括号内的表达式输入圆括号 `(…)`。若未输入，可能导致意外结果并打开调试器（Debugger）。

## 流体对象的只读属性（Read-Only Attributes）

流体对象提供：

- 左侧目录中列出的只读属性。
- 所有对象的只读属性（_Read-Only Attributes of All Objects）。

只读属性的值可以被查询（query），但不能被设置（set），因为 Plant Simulation 会在查询的时间点计算其值。大多数情况下，只读属性对应对象某个选项卡上不可编辑的对话框项，例如 **Statistics** 选项卡。

同样可通过 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性与属性。
