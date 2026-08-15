# Methods of the Buffer

本目录记录了 **Buffer（缓存区）对象的方法（Methods）** 相关帮助内容。

## 目录文件

- `methods.md` — Buffer 对象方法的主文档（Markdown 格式）。
- `methods.txtx` — 同内容的原始帮助文本。

## 内容概要

Buffer 对象提供以下方法：

- 物料流对象（Material Flow Objects）的方法。
- 所有对象（All Objects）的方法。

### 查看方法与属性

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口（帮助中以 *Station* 对象为例说明）：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的常规描述。
- 按下 **F8** 键，或点击 Frame 的 Home 功能区选项卡中的 **Show Attributes and Methods**，查看所选实例的常规描述。

### 方法语法

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所作用对象的路径。
- 括号内为方法签名，由参数标识符和数据类型组成，例如 `(Parameter:string)` 表示 string 类型参数。除常量值外，也可使用所需类型的变量或返回所需类型的方法。
- 可选参数列在方括号内，例如 `[,Parameter:boolean]` 表示可以但不必须传入该 boolean 参数。
- 若参数有默认值，签名中会在参数后显示，例如 `:= false`。
- 若方法有返回值，签名中会在箭头 `→` 后显示其数据类型，例如 `→ boolean`。

> **注意**：表达式内的括号 `(…)` 必须输入，否则可能导致意外结果并打开调试器（Debugger）。

### Buffer 的只读属性

Buffer 对象提供：

- 所有对象的只读属性（Read-Only Attributes of All Objects）。
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）。

只读属性的值可以查询，但不能设置，因为 Plant Simulation 会在查询的时间点计算该值。多数情况下，只读属性对应对象某个选项卡上不可用的对话框项，例如 **Statistics（统计）** 选项卡。

## 说明

本目录未包含子文件夹。
