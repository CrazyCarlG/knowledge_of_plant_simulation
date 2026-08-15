# Read-Only Attributes of the Button（Button 只读属性）

本目录总结了 Button（按钮）用户界面对象的只读属性文档。目录内仅有两个内容相同的文件：

- `read-only-attributes.md` — Markdown 版本文档
- `read-only-attributes.txtx` — 纯文本导出版本（内容与 `.md` 一致）

## 内容摘要

### 方法与属性符号约定（Method and Attribute Notation Conventions）

- `<Path>` 表示方法所作用对象的路径。
- 方法签名由标识符和参数数据类型组成，写在括号内，例如 `(Parameter:string)` 表示一个 `string` 类型的参数。除常量值外，也可使用所需类型的变量或返回所需类型的方法。
- 括号内的表达式必须输入括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。
- 可选参数写在方括号内，例如 `[,Parameter:boolean]` 表示可以但不必须输入该布尔参数。
- 若参数有默认值，签名会在参数后显示默认值，例如 `:= false`。
- 若方法有返回值，签名会在箭头 `->` 后显示其数据类型，例如 `-> boolean`。

### 只读属性（Read-Only Attributes）

- Button 提供「所有对象的只读属性」（_Read-Only Attributes of All Objects）。
- 只读属性只能查询（query），不能设置（set），因为 Plant Simulation 会在查询的时间点计算其值。
- 多数情况下，只读属性对应对象某个选项卡上不可用的对话框项，例如 **Statistics（统计）** 选项卡。
- 查看对象的所有方法、只读属性和属性：打开 **Show Attributes and Methods（显示属性和方法）** 窗口。
  - 在类库（Class Library）上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
  - 按 **F8** 键，或点击已插入实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。
- 查询只读属性值的示例：

  ```python
  print MyButton.UUID
  ```

### Button 的属性（Attributes of the Button）

- Button 提供：
  - 左侧目录中列出的属性。
  - 所有对象的属性（Attributes of All Objects）。
- 查看方式与只读属性相同（打开 **Show Attributes and Methods** 窗口，类库上下文菜单或 F8 / Home 功能区）。
- 属性既可以设置也可以读取（get/set），可通过对话框窗口中的复选框、文本框和下拉列表，或通过为相应属性赋值来实现。
- 设置属性值的示例：

  ```python
  MyButton.UseIcon := false
  ```

## 说明

- 两个源文件内容一致，`read-only-attributes.txtx` 为 `read-only-attributes.md` 的纯文本副本。
- 本目录不包含子文件夹。
