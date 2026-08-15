# DropDownList 只读属性（Read-Only Attributes）

本目录汇总了 DropDownList（下拉列表）对象的**只读属性**相关帮助文档。目录内当前包含以下源文件：

- `read-only-attributes.md` — 主要说明文档
- `read-only-attributes.txtx` — 同内容的纯文本导出版本

## 内容概述

### 只读属性（Read-Only Attributes of the DropDownList）

DropDownList 提供了 **“所有对象的只读属性”（Read-Only Attributes of All Objects）**：

- 可以**查询（query）**只读属性的值，但**不能设置（set）**它们。
- 每个只读属性的值由 Plant Simulation 在查询的**那一时刻**动态计算得出。
- 多数情况下，一个只读属性对应于对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

### 如何查看属性与方法（Show Attributes and Methods）

查看对象的所有方法、只读属性和属性：

- 在**类库（Class Library）**中，选中某个 **Class**，右键上下文菜单选择 **Show Attributes and Methods**。
- 在已插入实例的 **Frame** 中，按 **F8** 键，或点击 **Home** 功能区选项卡上的 **Show Attributes and Methods**，以查看所选 **Instance** 的方法、只读属性和属性。

### 查询只读属性示例

查询某个只读属性的值，例如：

```simtalk
print MyDropDownList.UUID
```

### DropDownList 的属性（Attributes of the DropDownList）

DropDownList 提供：

- 左侧目录中列出的属性。
- **所有对象的属性（Attributes of All Objects）**。

属性可以**读取（get）**也可以**设置（set）**，既可通过对话框中的复选框、文本框和下拉列表设置，也可通过给相应属性赋值来设置。

设置属性值示例：

```simtalk
MyDropdownList.UseIcon := false
```

## 方法签名记法说明（Method Signature Notation）

- `<Path>` 表示方法所作用的对象的路径。
- 方法的签名（由标识符和参数的数据类型组成）写在括号内，例如 `(Parameter:string)` 表示一个 `string` 类型的参数。除常量值外，也可使用所需类型的变量，或返回所需数据类型的方法。
- **注意：** 括号内表达式的括号 `(…)` 必须正确书写，否则可能产生意外结果并打开调试器（Debugger）。
- 可选参数写在方括号内，例如 `[,Parameter:boolean]` 表示可以（但不必须）输入该 boolean 参数。
- 若参数有默认值，签名会在参数后显示默认值，例如 `:= false`。
- 若方法有返回值，签名会在箭头 `->` 后显示其数据类型，例如 `-> boolean`。
