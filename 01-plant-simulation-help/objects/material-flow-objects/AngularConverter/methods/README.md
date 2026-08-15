# AngularConverter — Methods（方法）

本目录存放 **AngularConverter**（转角转换器）对象的方法说明文档。内容来源为 `methods.md`（`methods.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. 概述

AngularConverter 的方法按 **Help Menu（帮助菜单）** 中的说明进行描述。该对象提供：

- **曲线对象的方法**（_Methods of Curved Objects）。
- **物料流对象的方法**（Methods of the Material Flow Objects）。
- **所有对象的通用方法**（Methods of All Objects）。

> **注：** AngularConverter 本身不定义额外专有方法，其可用的方法继承自上述三类通用/父类方法。

### 查看方法的方式

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods（显示属性和方法）** 窗口（以下以对象 Station 为例进行说明）：

- 在 **Class Library（类库）** 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选**类（Class）**的方法、只读属性和属性。
- 在插入实例的 Frame 中，按 **F8** 键，或点击 Home 功能区标签页上的 **Show Attributes and Methods**，可显示所选**实例（Instance）**的方法、只读属性和属性。

## 2. 语法行示例（Syntax Line Example）

单个方法的语法行示例如下：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

语法行各部分的含义：

- **`<Path>`**：指定该方法所作用对象的路径。
- **参数签名**：方法签名由参数的标识符和数据类型组成，写在圆括号内。例如 `(Parameter:string)` 表示一个数据类型为 `string` 的参数。除了常量值，也可以使用所需类型的变量或返回所需数据类型的方法。
- **可选参数**：可选参数写在方括号内。例如 `[,Parameter:boolean]` 表示该布尔参数可以输入，也可以不输入。
- **默认值**：若参数有默认值，签名会在参数后显示默认值，如上例中的 `:= false`。
- **返回值**：若方法有返回值，签名会在箭头 `->` 后显示其数据类型，如上例中的 `→ boolean`。

> **注意：** 请务必为括号内的表达式输入圆括号 `(…)`。若不输入，可能导致意外结果并打开 **Debugger（调试器）**。

## 3. AngularConverter 的只读属性（Read-Only Attributes）

AngularConverter 提供：

- 只读属性 **`IsUp`**（[SimTalk] - AngularConverter）。
- 所有对象的只读属性（_Read-Only Attributes of All Objects）。
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）。

> **注：** 可以查询只读属性的值，但不能设置它们，因为 Plant Simulation 会在查询的时刻计算其值。大多数情况下，只读属性对应于对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。

查看方式与查看方法相同：打开 **Show Attributes and Methods** 窗口（以下以对象 Station 为例进行说明）。

## 目录说明

- `methods.md`：AngularConverter 方法说明的 Markdown 版本（本总结的源文件）。
- `methods.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
