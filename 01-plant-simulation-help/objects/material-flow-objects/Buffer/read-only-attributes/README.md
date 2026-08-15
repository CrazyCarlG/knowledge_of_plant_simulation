# Read-Only Attributes of the Buffer

本目录包含 Buffer 对象的只读属性（Read-Only Attributes）相关文档。目录内现有以下文件：

- `read-only-attributes.md`
- `read-only-attributes.txtx`（同一文档的纯文本提取版本）

> 说明：本目录下没有子文件夹，因此没有子文件夹内的 README.md 内容需要汇总。

## 内容摘要

### 1. 方法语法（Syntax of Methods）

以方法语法行示例说明：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所应用对象的路径。
- 方法签名由参数标识符和数据类型组成，写在括号内，例如 `(Parameter:string)` 表示一个 `string` 类型的参数。除常量值外，也可使用所需类型的变量或返回所需类型的方法。
- **注意**：括号内的表达式务必输入括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。
- 可选参数写在方括号内，例如 `[,Parameter:boolean]` 表示可以但不必输入该布尔参数。
- 若参数有默认值，签名会在参数后显示默认值，如 `:= false`。
- 若方法有返回值，签名会在箭头后显示其数据类型，如 `→ boolean`。

### 2. 概述（Overview）

Buffer 提供：

- 所有对象的只读属性（_Read-Only Attributes of All Objects）
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）

只读属性的值可以查询，但不能设置，因为 Plant Simulation 会在查询的时间点计算该值。多数情况下，只读属性对应对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。

查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 按下 F8 键，或点击插入了实例的 Frame 的 Home 选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。

查询只读属性值的示例：

```
print MyBuffer.NumChildren
```

### 3. Buffer 的属性（Attributes of the Buffer）

Buffer 提供：

- 左侧目录中列出的属性
- 所有对象的属性（Attributes of All Objects）
- 物料流对象的属性（Attributes of the Material Flow Objects）

同样可通过 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性和属性。

---

*来源：Plant Simulation Help（Siemens，未发表作品，© 2026 Siemens）*
