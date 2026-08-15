# ContinuousMixer — Methods（方法）

本目录包含 Plant Simulation 中 **ContinuousMixer**（连续搅拌器 / 连续混合器）对象的方法（Methods）文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `methods.md` | ContinuousMixer 对象方法的 Markdown 文档（主内容） |
| `methods.txtx` | 同一内容的原始导出文本（含页码脚注，内容与 methods.md 基本一致） |

> 本目录下没有子文件夹，也没有其他 README.md 文件，因此本总结基于 `methods.md` 的内容整理。

## 概述

ContinuousMixer 提供以下方法：

- 流体对象的方法（Methods of the Fluid Objects）。
- 所有对象的方法（Methods of All Objects）。

要查看对象的全部方法、只读属性和属性，请打开 **Show Attributes and Methods** 窗口。

## 查看方法与属性

- 在 Class Library（类库）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **类（Class）** 的方法、只读属性和属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 Home 功能区中的 **Show Attributes and Methods**，可查看所选 **实例（Instance）** 的方法、只读属性和属性。

## 语法行（Syntax line）示例

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

### 语法约定

- 表达式 `<Path>` 表示方法所作用对象的路径。
- 方法的签名由参数标识符及其数据类型组成，并写在圆括号内。例如 `(Parameter:string)` 表示一个数据类型为 `string` 的参数。除常量值外，也可以使用所需类型的变量，或返回所需数据类型的方法。

> **注意：** 请务必为圆括号内的表达式输入圆括号 `(…)`。省略圆括号可能导致意外结果并打开调试器（Debugger）。

- 可选参数写在方括号内。例如 `[,Parameter:boolean]` 表示可以但不必须输入该 boolean 参数。
- 若参数具有默认值，签名会在参数后显示该默认值，如上例中的 `:= false`。
- 若方法具有返回值，签名会在箭头 `->` 之后显示其数据类型，如上例中的 `→ boolean`。

## 只读属性（Read-Only Attributes）

ContinuousMixer 提供：

- 流体对象的只读属性（Read-Only Attributes of the Fluid Objects）。
- 所有对象的只读属性（Read-Only Attributes of All Objects）。

只读属性的值可以查询，但不能设置，因为 Plant Simulation 会在查询的时间点计算该值。多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

要查看对象的全部方法、只读属性和属性，请打开 **Show Attributes and Methods** 窗口。

## 相关主题（See also）

- ContinuousMixer 的 Attributes（属性）
- ContinuousMixer 的 General（概述）
- Show Attributes and Methods
