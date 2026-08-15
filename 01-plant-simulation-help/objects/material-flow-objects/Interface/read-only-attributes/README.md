# Interface — Read-Only Attributes

本目录汇总了 **Interface（接口）** 物料流对象的只读属性（Read-Only Attributes）文档。

## 内容来源

- `read-only-attributes.md` — 整理后的只读属性文档
- `read-only-attributes.txtx` — Plant Simulation Help 原始导出内容（同主题，含页码与版权信息）

## 概述

Interface 对象提供以下只读属性：

- 本页目录中列出的只读属性（`IsEntry`、`IsExit`）
- _Read-Only Attributes of All Objects（所有对象的只读属性）
- Read-Only Attributes of the Material Flow Objects（物料流对象的只读属性）

> 只读属性的值只能查询，不能设置。Plant Simulation 会在你查询的时刻计算该值。大多数情况下，只读属性对应对象某个选项卡（如 Statistics 选项卡）上不可编辑的对话框项。

### 查看方式

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，显示所选类的方法、只读属性和属性。
- 在已插入实例的 Frame 上，按 **F8** 键或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，显示所选实例的方法、只读属性和属性。

查询只读属性值的示例：

```simtalk
print .Models.Model.MyFrame.Interface.IsEntry
```

## 只读属性列表

| 属性 | 返回类型 | 说明 |
| --- | --- | --- |
| `IsEntry` | boolean | 判断 `<Path>` 指定的 Interface 是否为 Entrance（入口）类型 |
| `IsExit` | boolean | 判断 `<Path>` 指定的 Interface 是否为 Exit（出口）类型 |

### IsEntry [SimTalk]

返回 `<Path>` 指定的 Interface 是否为 Entrance 类型（`true`）或不是（`false`）。

- **备注**：Interface 必须已通过 Connector（连接器）连接。
- **类型**：只读属性
- **语法**：`<Path>.IsEntry → boolean`
- **返回值**：boolean 类型
- **示例**：

```simtalk
print .Models.Model.Frame.Interface.IsEntry
```

- **另见**：Type [Interface]、IsExit [SimTalk]

### IsExit [SimTalk]

返回 `<Path>` 指定的 Interface 是否为 Exit 类型（`true`）或不是（`false`）。

- **备注**：Interface 必须已通过 Connector（连接器）连接。
- **类型**：只读属性
- **语法**：`<Path>.IsExit → boolean`
- **返回值**：boolean 类型
- **示例**：

```simtalk
print .Models.Model.Frame.interface.IsExit
```

- **另见**：IsEntry [SimTalk]、Type [Interface]、Attributes of the Interface

## 方法语法约定（通用说明）

- `<Path>` 表示该方法所应用对象的路径。
- 方法签名由标识符和参数的数据类型组成，写在括号内。例如 `(Parameter:string)` 表示一个 string 类型的参数。除常量值外，也可使用所需类型的变量或返回所需类型的方法。
- 可选参数用方括号列出，例如 `[,Parameter:boolean]` 表示可输入也可不输入该 boolean 参数。
- 若参数有默认值，签名会在参数后显示默认值，例如 `:= false`。
- 若方法有返回值，签名会在箭头 `->` 后显示其数据类型，例如 `→ boolean`。

> **注意**：嵌套在括号内的表达式务必输入括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。

## 另见

- _Read-Only Attributes of the Interface
- _Attributes of the Interface
- Attributes of the Interface
