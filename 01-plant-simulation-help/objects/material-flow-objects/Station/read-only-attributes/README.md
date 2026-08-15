# Station — Read-Only Attributes

本目录包含 Station 对象的只读属性（Read-Only Attributes）相关文档，内容来源于 Siemens Plant Simulation Help（11-1718 / 11-1719）。

## 内容概述

### 1. 语法行约定（Syntax Line Conventions）

方法（Method）的语法行示例如下：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所作用对象的路径。
- 括号内为方法的签名（标识符 + 参数数据类型）。`(Parameter:string)` 表示 string 类型参数；除常量值外，也可使用相应类型的变量或返回该类型的方法。
- 可选参数用方括号 `[…]` 表示，如 `[,Parameter:boolean]` 表示可省略该 boolean 参数。
- 参数默认值在参数后以 `:=` 显示，如 `:= false`。
- 返回值类型在箭头 `→` 之后显示，如 `→ boolean`。

> **注意：** 嵌套表达式 `(…)` 的括号必须输入，否则可能产生意外结果并打开调试器（Debugger）。

### 2. Station 的只读属性（Read-Only Attributes）

Station 提供：
- 所有对象的只读属性（Read-Only Attributes of All Objects）
- 物流对象的只读属性（Read-Only Attributes of the Material Flow Objects）

只读属性的值**只能查询，不能设置**——Plant Simulation 会在查询的时间点实时计算该值。多数只读属性对应对象某选项卡（如 **Statistics**）上不可编辑的对话框项。

查询示例：

```
print MyStation.UUID
```

### 3. Station 的属性（Attributes）

Station 提供：
- 所有对象的属性（Attributes of All Objects）
- 物流对象的属性（Attributes of the Material Flow Objects）

### 查看方法、只读属性与属性

打开 **Show Attributes and Methods** 窗口即可查看对象的所有方法、只读属性和属性：
- 在类库（Class Library）中选中类后，右键菜单选择 **Show Attributes and Methods**，查看所选类的相关内容。
- 在 Frame 中插入实例后，按 **F8** 键或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，查看所选实例的相关内容。

---

*Source: Plant Simulation Help (11-1718 / 11-1719). Unpublished work. © 2026 Siemens.*
