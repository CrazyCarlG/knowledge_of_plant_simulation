# Methods of the Interface — 目录说明

本目录说明 **Interface（接口）** 对象的方法（Methods）与只读属性（Read-Only Attributes）。目录内仅包含一个内容文件 `methods.md`（另有一份原始导出文件 `methods.txtx`），无子文件夹及子级 README.md，故本总结以 `methods.md` 为准。

## 核心内容摘要

### 1. Interface 提供的功能
- **Interface** 提供了 **所有对象的通用方法（Methods of All Objects）**。

### 2. 查看方法与属性
可通过 **Show Attributes and Methods** 窗口查看对象的方法、只读属性和属性（以对象 `Station` 为例说明）：

- 在 **Class Library** 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **类（Class）** 的方法、只读属性和属性。
- 在插入实例的 Frame 中，按 **F8** 键，或点击 **Home** 功能区选项卡上的 **Show Attributes and Methods**，可查看所选 **实例（Instance）** 的方法、只读属性和属性。

### 3. 方法语法（Syntax）说明
单个方法的语法行示例：

```plaintext
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

各符号含义：

- `<Path>`：方法所应用对象的路径。
- 括号 `(…)`：方法的签名（signature），包含参数标识符及数据类型。例如 `(Parameter:string)` 表示一个 `string` 类型的参数。参数位置既可传入常量，也可传入所需类型的变量，或返回所需类型的方法。
- 方括号 `[…]`：可选参数。例如 `[,Parameter:boolean]` 表示可以传入、也可以不传入该 `boolean` 参数。
- `:=`：参数默认值。如 `:= false` 表示该参数默认值为 `false`。
- `→`：返回值类型。如 `→ boolean` 表示方法返回 `boolean` 类型。

> **注意**：在嵌套括号表达式中务必输入完整的括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。

### 4. Interface 的只读属性（Read-Only Attributes）
Interface 提供以下只读属性：

- 左侧目录（table of contents）中列出的只读属性。
- **_Read-Only Attributes of All Objects**（所有对象的通用只读属性）。
- **Read-Only Attributes of the Material Flow Objects**（物流对象的只读属性）。

只读属性只能**查询**、不能**设置**：Plant Simulation 会在查询的时间点计算其值。多数情况下，只读属性对应于对象某个选项卡（例如 **Statistics** 选项卡）上不可编辑的对话框项。
