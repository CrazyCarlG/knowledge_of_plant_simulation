# Converter 方法（Methods）总结

本目录汇总了 Plant Simulation 中 **Converter（转换器）** 对象的方法与只读属性。详细内容见 [methods.md](methods.md)。

## 概述

Converter 提供以下几类方法：

- 本目录列出的方法（见下方列表）
- Curved Objects 的方法（_Methods of Curved Objects）
- Material Flow Objects 的方法（Methods of the Material Flow Objects）
- 所有对象的通用方法（Methods of All Objects）

> 查看全部方法、只读属性与属性：在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，或在插入实例的 Frame 的 Home 选项卡上点击 **Show Attributes and Methods**（或按 **F8**）。

## 方法列表

| 方法 | 用途 | 语法 |
| --- | --- | --- |
| `getAttributeList` | 返回 **Strategy > MU Attribute** 的目标列表（包含 MU 属性名、值以及 MU 从哪一侧离开） | `<Path>.getAttributeList(AttributeList:table)` |
| `getEntranceSide` | 返回最后一个部件移动到 Converter 上的那一侧（无部件时为 `-1`） | `<Path>.getEntranceSide -> integer` |
| `getObjectOfSide` | 返回指定侧上的对象（该侧未占用时为 `VOID`） | `<Path>.getObjectOfSide(side:integer) -> object` |
| `getSideOfConnector` | 返回指定 Connector 连接到 Converter 的那一侧 | `<Path>.getSideOfConnector(Connector:object) → integer` |
| `getSuccessorAtExit` | 返回在指定出口侧连接的后继对象 | `<Path>.getSuccessorAtExit(Side:integer) → object` |
| `setAttributeList` | 设置 **Strategy > MU Attribute** 的目标列表 | `<Path>.setAttributeList(AttributeList:table)` |

## 只读属性（Read-Only Attributes）

Converter 还提供只读属性（包含在 **Read-Only Attributes of the Converter** 一节中）。这些属性的值只能查询、不能设置，由 Plant Simulation 在查询时点实时计算；多数只读属性对应对象某选项卡上不可用的对话框项（例如 **Statistics** 选项卡）。

## 语法说明

- `<Path>`：方法所应用对象的路径。
- 方法签名中括号内为参数标识符及数据类型，如 `(Parameter:string)`。
- 可选参数放在方括号内，如 `[,Parameter:boolean]`。
- 参数默认值在参数后以 `:=` 标注，如 `:= false`。
- 有返回值时，在箭头 `->`（或 `→`）后标注返回数据类型，如 `→ boolean`。
- 表达式中嵌套括号时必须输入括号 `(…)`，否则可能导致意外结果并打开调试器。
