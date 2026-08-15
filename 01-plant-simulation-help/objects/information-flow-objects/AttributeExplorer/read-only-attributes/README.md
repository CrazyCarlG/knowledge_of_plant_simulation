# Read-Only Attributes of the AttributeExplorer

本目录包含 AttributeExplorer 只读属性（Read-Only Attributes）的说明文档。

## 目录内容

- `read-only-attributes.md` — AttributeExplorer 只读属性的完整说明。

## 内容摘要

AttributeExplorer 提供**所有对象的只读属性**（Read-Only Attributes of All Objects）。

- 只读属性只能查询（query），不能设置（set）。Plant Simulation 会在查询时刻计算并返回对应值。
- 多数情况下，只读属性对应对象某个选项卡（如 **Statistics** 选项卡）上不可编辑的对话框项。

### 查看只读属性

可通过 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选 Class 的方法、只读属性和属性。
- 在插入实例的 Frame 中，按 **F8** 键或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，查看所选 Instance 的方法、只读属性和属性。

### 查询只读属性示例

```simtalk
print MyAttributeExplorer.UUID
```

### 方法签名约定

- `<Path>` 表示方法所应用对象的路径。
- 方法签名由标识符和参数数据类型组成，用括号列出。例如 `(Parameter:string)` 表示字符串类型参数；也可使用所需类型的变量或返回所需类型的方法代替常量。
- 括号内表达式的括号 `(…)` 必须输入，否则可能产生意外结果并打开调试器（Debugger）。
- 可选参数列在方括号中，例如 `[,Parameter:boolean]` 表示可输入也可不输入布尔参数。
- 参数有默认值时，签名会在参数后显示默认值，例如 `:= false`。
- 方法有返回值时，签名在箭头 `->` 后显示返回类型，例如 `→ boolean`。

### 属性（Attributes）

AttributeExplorer 提供：

- 左侧目录中列出的属性。
- **所有对象的属性**（Attributes of All Objects）。

属性既可以设置值也可以获取值，可通过对话框中的复选框、文本框和下拉列表，或通过为相应属性赋值来实现。

设置属性值示例：

```simtalk
MyAttributeExplorer.Comment := "Processing time changes globally"
```

---

*Plant Simulation Help 11-4441 / 11-4442 · Unpublished work. © 2026 Siemens*
