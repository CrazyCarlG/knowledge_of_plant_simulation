# FluidSource Methods

本目录包含 FluidSource 对象的方法（Methods）与只读属性（Read-Only Attributes）的说明文档。

## 文件概览

| 文件 | 说明 |
| --- | --- |
| `methods.md` | 整理后的 Markdown 版本文档（主要参考文档） |
| `methods.txtx` | 从 Plant Simulation 帮助中提取的原始文本版本，内容与 `methods.md` 一致 |

> 注：当前目录下没有子文件夹，因此没有额外的 `README.md` 内容需要汇总。

## 内容总结

### Methods of the FluidSource

FluidSource 对象提供以下方法：

- **Fluid Objects 的方法**（The Methods of the Fluid Objects）
- **所有对象的方法**（The Methods of All Objects）

要查看该对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的右键菜单中选择 **Show Attributes and Methods**，查看所选类的方法、只读属性和属性（一般描述）。
- 在已插入实例的 Frame 中，按 **F8** 键或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，查看所选实例的方法、只读属性和属性（一般描述）。

### 语法行（Syntax line）

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所应用对象的路径。
- 方法签名由参数标识符和数据类型组成，列在括号内。例如 `(Parameter:string)` 表示一个 `string` 类型的参数。除了常量值，也可以使用所需类型的变量，或返回所需类型的方法。

> **注意**
> 务必为括号内的表达式输入括号 `(…)`。省略括号可能导致意外结果并打开调试器（Debugger）。
>
> 可选参数列在方括号内。例如 `[,Parameter:boolean]` 表示可以但不必须输入该 boolean 参数。
>
> 若参数有默认值，签名会在参数后显示默认值，如上例中的 `:= false`。
>
> 若方法有返回值，签名会在箭头 `->` 之后显示其数据类型，如上例中的 `→ boolean`。

### Read-Only Attributes of the FluidSource

FluidSource 对象提供以下只读属性：

- 只读属性 `StatAmount`（SimTalk）
- **Fluid Objects 的只读属性**（The Read-Only Attributes of the Fluid Objects）
- **所有对象的只读属性**（The Read-Only Attributes of All Objects）

只读属性的值可以被查询，但无法被设置，因为 Plant Simulation 会在查询时计算该时间点的值。在大多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

查看对象所有方法、只读属性和属性的方式与上述相同，即打开 **Show Attributes and Methods** 窗口。

## 参考链接

- 相关文档：Fluid Objects、All Objects 的方法与只读属性（见 Plant Simulation 帮助中的对应章节）。
- 帮助页码：`Plant Simulation Help 11-2725` 至 `11-2726`（`methods.txtx` 中的页码标记）。
