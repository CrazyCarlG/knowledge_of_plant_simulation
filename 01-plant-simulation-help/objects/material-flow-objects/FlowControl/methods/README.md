# FlowControl 方法（Methods）总结

本目录包含 FlowControl 对象的方法文档，来源文件为：

- `methods.md` — 结构化的 Markdown 文档
- `methods.txtx` — Plant Simulation 帮助系统的原始文本导出

> 注：本目录下没有子文件夹，因此无子目录 README 需要汇总。

---

## 概述

FlowControl 提供：

- 目录中列出的方法
- 所有对象通用的方法（Methods of All Objects）

由于 FlowControl **不能接收 MU**，因此它不具备其他物料流对象所提供的方法。

可通过打开 **Show Attributes and Methods** 窗口查看该对象的所有方法、只读属性和属性。

---

## 语法约定（Syntax conventions）

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` — 方法所应用对象的路径
- `(Parameter:string)` — 参数标识符及数据类型；也可使用所需类型的变量或返回所需类型的方法
- `[,Parameter:boolean]` — 方括号内为可选参数
- `:= false` — 参数默认值
- `→ boolean` — 方法的返回值数据类型

> **注意：** 表达式内的括号必须成对输入，否则可能导致意外结果并打开调试器（Debugger）。

---

## 方法一览

| 方法 | 语法 | 参数 | 返回值 | 用途 |
| --- | --- | --- | --- | --- |
| `getAttributeList` | `<Path>.getAttributeList(AttributeList:table)` | `AttributeList` (table) | — | 获取 **Exit Strategy > MU Attribute** 设置中的属性值并写入列表 |
| `getEntryList` | `<Path>.getEntryList(EntryList:any) → boolean` | `EntryList` (any) | boolean | 获取 **Entry Strategy > Percentage / Cyclic Sequence** 的内部入口列表 |
| `getExitList` | `<Path>.getExitList(ExitList:any) → boolean` | `ExitList` (any) | boolean | 获取 **Exit Strategy > Percentage / Cyclic Sequence** 的内部出口列表 |
| `setAttributeList` | `<Path>.setAttributeList(AttributeList:table)` | `AttributeList` (table) | — | 设置 **Exit Strategy > MU Attribute / MU Name** 的属性列表 |
| `setEntryList` | `<Path>.setEntryList(EntryList:any)` | `EntryList` (any) | — | 设置 **Entry Strategy > Percentage / Cyclic Sequence** 的入口列表 |
| `setExitList` | `<Path>.setExitList(ExitList:any)` | `ExitList` (any) | — | 设置 **Exit Strategy > Percentage / Cyclic Sequence** 的出口列表 |

---

## 各方法详细说明

### getAttributeList [SimTalk] — FlowControl

返回传给 `<Path>` 所指定 FlowControl 的属性值（用于 **Exit Strategy > MU Attribute** 设置），并写入列表。

- **参数：** `AttributeList`（table）— 列表名称

```simtalk
MyFlowControl.getAttributeList(tab)
```

---

### getEntryList [SimTalk]

返回 `<Path>` 所指定 FlowControl 的内部入口列表内容（用于 **Entry Strategy > Percentage** 或 **Cyclic Sequence** 设置），并写入列表。

- **参数：** `EntryList`（any）— 列表名称
- **返回值：** boolean

```simtalk
var li: list
MyFlowControl.getEntryList(li)
MyFlowControl1.setEntryList(li)
MyFlowControl.getEntryList(DataList)
```

---

### getExitList [SimTalk]

返回 `<Path>` 所指定 FlowControl 的内部出口列表内容（用于 **Exit Strategy > Percentage** 或 **Cyclic Sequence** 设置），并写入列表。

- **参数：** `ExitList`（any）— 列表名称
- **返回值：** boolean

```simtalk
MyFlowControl.getExitList(DataList)
MyFlowControl.setExitList(DataList.copy)
```

---

### setAttributeList [SimTalk] — FlowControl

设置 `<Path>` 所指定 FlowControl 的属性列表（用于 **Exit Strategy > MU Attribute** 或 **MU Name** 设置）。

- **备注：** 可以在 Attribute List 中为 Attribute Value 输入多个期望后继的编号；在非阻塞情况下，Plant Simulation 会检查哪个期望后继能够接收 MU。
- **参数：** `AttributeList`（table）— 列表或同类型变量的路径，Plant Simulation 会将传入列表内容复制到 FlowControl 的内部属性列表。

```simtalk
MyFlowControl.setAttributeList(tab1)
```

---

### setEntryList [SimTalk]

设置 `<Path>` 所指定 FlowControl 的入口列表（用于 **Entry Strategy > Percentage** 或 **Cyclic Sequence** 设置）。

- **参数：** `EntryList`（any）— 列表或同类型变量的路径，Plant Simulation 会将传入列表内容复制到 FlowControl 的内部入口列表。

```simtalk
MyFlowControl.setEntryList(DataList)
MyFlowControl.setEntryList(DataList.copy)
```

---

### setExitList [SimTalk]

设置 `<Path>` 所指定 FlowControl 的出口列表（用于 **Exit Strategy > Percentage** 或 **Cyclic Sequence** 设置）。

- **参数：** `ExitList`（any）— 列表或同类型变量的路径，Plant Simulation 会将传入列表内容复制到 FlowControl 的内部出口列表。

```simtalk
MyFlowControl.setExitList(DataList)
MyFlowControl.setExitList(DataList.copy)
```

---

## 只读属性（Read-Only Attributes）

FlowControl 提供所有对象通用的只读属性（_Read-Only Attributes of All Objects）。

只读属性的值可以查询但不能设置，因为 Plant Simulation 会在查询的时间点计算其值。大多数只读属性对应对象某个选项卡（如 Statistics 选项卡）上不可用的对话框项。

```simtalk
print MyFlowControl.UUID
```

---

## 属性（Attributes）

FlowControl 提供：

- 目录中列出的属性
- 所有对象通用的属性（Attributes of All Objects）

由于 FlowControl 不能接收 MU，因此它不具备其他物料流对象所提供的属性。

---

## 相关参考（See also）

- MU Attribute [FlowControl, exit]
- MU Name
- Percentage [FlowControl, entry]
- Percentage [FlowControl, exit]
- Cyclic Sequence [FlowControl, entry]
- Data Held in Tabular Form in Attributes [material flow objects]
