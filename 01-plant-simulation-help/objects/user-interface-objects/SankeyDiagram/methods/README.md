# SankeyDiagram — Methods

本目录汇总了 **SankeyDiagram**（桑基图）对象的方法（Methods）相关文档。桑基图用于可视化仿真过程中物料/零件在对象之间流动的数量关系。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `methods.md` | 方法文档（Markdown 版） |
| `methods.txtx` | 方法文档原始来源（Plant Simulation Help 导出文本） |

> 说明：本目录下没有子文件夹，因此无子级 `README.md` 需要汇总。

## 文档概述

SankeyDiagram 对象提供了以下内容用于访问：

- 左侧目录中所列的方法
- **所有对象通用方法**（Methods of All Objects）
- **所有对象通用只读属性**（Read-Only Attributes of All Objects）

如需查看该对象全部的方法、只读属性和属性，可打开 **Show Attributes and Methods**（显示属性和方法）窗口：

- 在 Class Library 的右键菜单中选择 **Show Attributes and Methods**，可查看所选类的成员；
- 在插入实例的 Frame 中按 **F8** 键，或点击 Home 功能区的 **Show Attributes and Methods**，可查看所选实例的成员。

## 语法行（Syntax line）阅读规则

方法的语法行示例如下：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所应用对象的路径；
- 括号内为方法签名（参数标识符 + 数据类型），如 `(Parameter:string)` 表示 `string` 类型的参数，也可使用相应类型的变量或返回该类型的方法替代常量；
- 可选参数放在方括号内，如 `[,Parameter:boolean]`；
- 参数默认值在参数后以 `:=` 标注，如 `:= false`；
- 若方法有返回值，其数据类型在箭头 `->` 之后标注，如 `→ boolean`。

> **注意：** 在括号内书写嵌套表达式时，务必输入括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。

## 方法列表

### 1. getPartFlowData [SimTalk]

将 `<Path>` 指定的 SankeyDiagram 在仿真过程中收集到的流动数据写入指定的 DataTable（数据表）。

- **类型：** Method
- **语法：** `<Path>.getPartFlowData(DataTable:table)`
- **参数：**
  - `DataTable`（数据类型 `table`）：指定 Plant Simulation 写入流动数据的目标表。
- **备注（Remarks）：**
  - SankeyDiagram 收集的是零件在**点向对象**（point-oriented objects）之间移动、或沿**长度向对象**（length-oriented objects）移动的**数量**；
  - 该方法**不考虑**零件移动的**方向**与**顺序**，且无法根据返回数据回溯这些信息。
- **示例：**

```
MySankeyDiagram.getPartFlowData(MyDataTable)
```

### 2. update [SimTalk] - SankeyDiagram

使用当前值刷新 `<Path>` 指定的 SankeyDiagram 的显示。

- **类型：** Method
- **语法：** `<Path>.update`
- **示例：**

```
MySankeyDiagram.update
```

- **另见（See also）：** Update（位于 Frame 中）

## 只读属性（Read-Only Attributes）

SankeyDiagram 提供 **所有对象通用只读属性**。只读属性的值可以查询，但**不能设置**——Plant Simulation 会在查询的时点计算其值。在大多数情况下，只读属性对应于对象某个选项卡上不可用的对话框项（例如 **Statistics**（统计）选项卡）。
