# Checkbox — Methods（方法）总结

本目录记录 **Checkbox（复选框）** 对象的方法（Methods）与只读属性（Read-Only Attributes）说明。内容来源为 `methods.md`（以及同目录的 `methods.txtx` 文本源），无子文件夹。

## 方法概述（Overview）

- **Checkbox** 提供 **所有对象的通用方法（Methods of All Objects）**，即其方法集合继承自通用对象方法。
- 若要查看某个对象全部的方法、只读属性与属性，可打开 **Show Attributes and Methods（显示属性与方法）** 窗口。

### 如何打开“显示属性与方法”窗口

- 在 **Class Library（类库）** 中，右键所选 **Class（类）**，选择 **Show Attributes and Methods**，即可查看该类的相关成员。
- 对于已插入 Frame 的 **Instance（实例）**，按 **F8** 键，或在 Frame 的 **Home（开始）** 功能区选项卡上点击 **Show Attributes and Methods**，即可查看该实例的相关成员。

## 方法语法（Method syntax）

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

### 语法约定（Syntax conventions）

- `<Path>`：表示该方法所作用对象的路径。
- **方法签名**：由参数标识符及其数据类型组成，写在括号内。例如 `(Parameter:string)` 表示一个 `string` 类型的参数。除常量值外，也可使用所需类型的变量或返回所需类型的方法。
- **可选参数**：写在方括号内。例如 `[,Parameter:boolean]` 表示可以传入、也可以不传入该 boolean 参数。
- **默认值**：若参数有默认值，签名会在参数后以 `:=` 标注默认值，如示例中的 `:= false`。
- **返回值**：若方法有返回值，签名会在箭头 `→`（或 `->`）之后标注其数据类型，如示例中的 `→ boolean`。

> **注意：** 对于括号内的表达式 `(…)`，务必输入括号。遗漏括号可能导致意外结果，并打开 **Debugger（调试器）**。

## Checkbox 的只读属性（Read-Only Attributes）

- **Checkbox** 提供 **所有对象的通用只读属性（Read-Only Attributes of All Objects）**。
- 只读属性的值**可以查询，但不能设置**：Plant Simulation 会在你查询的那一刻计算其值。多数情况下，只读属性对应对象某个选项卡（例如 **Statistics（统计）** 选项卡）上不可用的对话框项。

### 查看方式

- 在 **Class Library** 中，右键所选 **Class**，选择 **Show Attributes and Methods**，即可查看该类的只读属性。

## 目录结构

```
methods/
├── README.md      # 本总结文件
├── methods.md     # Checkbox 方法说明（Markdown 版本）
└── methods.txtx   # 同内容的文本源
```
