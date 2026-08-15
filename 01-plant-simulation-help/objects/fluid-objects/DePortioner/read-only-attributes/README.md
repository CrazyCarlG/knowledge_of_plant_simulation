# DePortioner — Read-Only Attributes

本目录汇总了 Plant Simulation 中 **DePortioner（分配器）** 对象的只读属性（Read-Only Attributes）文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `read-only-attributes.md` | 主文档，包含语法行说明、概述以及 `CurrentAmount` 只读属性的完整描述 |
| `read-only-attributes.txtx` | 同内容的文本格式来源（Siemens 帮助文档导出的原始文本） |

> 注：本目录无子文件夹，因此没有子目录的 README.md 可汇总。

## 内容摘要

### 1. 关于语法行（About the Syntax Line）

帮助文档中的方法签名示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所应用对象的路径。
- 括号内为方法签名，由参数标识符与数据类型组成，如 `(Parameter:string)`；除常量外也可传入所需类型的变量或返回该类型的方法。
- **注意**：表达式内嵌套括号 `(…)` 时必须成对输入，否则可能产生意外结果并打开调试器（Debugger）。
- 可选参数放在方括号内，如 `[,Parameter:boolean]`。
- 默认值在参数后以 `:= false` 形式给出。
- 返回值类型在箭头 `→` 之后给出，如 `→ boolean`。

### 2. 概述（Overview）

DePortioner 提供三类只读属性：

- 本目录左侧目录表中列出的只读属性；
- _Read-Only Attributes of the Fluid Objects（流体对象的只读属性）；
- _Read-Only Attributes of All Objects（所有对象的只读属性）。

只读属性只能查询、不能设置，因为 Plant Simulation 会在查询的时间点实时计算其值。多数只读属性对应对象某个选项卡（如 **Statistics**）上不可编辑的对话框项。

查看对象全部方法、只读属性与属性的方式：

- 在类库（Class Library）上下文菜单中选择 **Show Attributes and Methods** 查看所选类；
- 在插入实例的 Frame 中按 **F8** 或点击 Home 功能区中的 **Show Attributes and Methods** 查看所选实例。

查询只读属性示例：

```
print DePortioner.CurrentOutFlowrate
```

### 3. 属性（Attributes）

#### CurrentAmount [SimTalk] — DePortioner

返回 `<Path>` 指定的 DePortioner 中当前流体的量（Current Amount）。

- **类型**：只读属性（Read-only attribute）
- **语法**：`<Path>.CurrentAmount → real`
- **返回值**：数据类型为 `real`，当前量以升（liters）为单位。
- **示例**：

```
print MyDePortioner.CurrentAmount
```

- **参见**：
  - Current Amount [DePortioner]
  - Attributes of the DePortioner
  - _Attributes of the DePortioner
