# DropDownList Methods — 总结

本目录包含 DropDownList 对象「方法」相关的文档，目前只有一个内容来源（`methods.md`），其对应的原始帮助文本为 `methods.txtx`。目录内没有子文件夹，也没有其他 README.md。

## 核心结论

- DropDownList 提供 **所有对象的方法（Methods of All Objects）**。
- DropDownList 提供 **所有对象的只读属性（Read-Only Attributes of All Objects）**。

## 如何查看方法、只读属性和属性

打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **类（Class）** 的方法、只读属性和属性。
- 在插入实例的 Frame 上，按 **F8** 键，或点击 Home 功能区的 **Show Attributes and Methods**，可查看所选 **实例（Instance）** 的方法、只读属性和属性。

## 语法行（Syntax Line）

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

各符号含义：

- `<Path>`：该方法所应用对象的路径。
- 括号 `(…)` 内为方法签名，由参数标识符和数据类型组成，例如 `(Parameter:string)` 表示一个 `string` 类型参数。除常量值外，也可使用所需类型的变量或返回所需类型的方法。
  - 注意：括号内的表达式必须输入括号 `(…)`，否则可能导致意外结果并打开 Debugger。
- 方括号 `[…]` 内为可选参数，例如 `[,Parameter:boolean]` 表示可输入也可不输入的 boolean 参数。
- 若参数有默认值，签名中会在参数后显示默认值，如 `:= false`。
- 若方法有返回值，签名中会在箭头 `->` 之后显示其数据类型，如 `→ boolean`。

## 只读属性

- 只读属性的值可以被查询，但不能被设置，因为 Plant Simulation 会在查询时刻计算其值。
- 大多数情况下，只读属性对应对象某个选项卡（如 **Statistics** 选项卡）上不可用的对话框项。

## 文件说明

| 文件 | 内容 |
| --- | --- |
| `methods.md` | DropDownList 方法的 Markdown 文档（主要来源） |
| `methods.txtx` | 对应的原始帮助文本，内容与 `methods.md` 一致，仅排版/来源格式不同 |
