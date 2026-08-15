# Turnplate（转盘）— 方法（Methods）汇总说明

本目录 `methods` 汇总了 Turnplate（转盘）物料流对象的方法参考文档。Turnplate 是 Plant Simulation 中的一种物料流对象，用于将 MU（可移动单元）旋转到指定方向。

本文件是 `methods/methods.md` 的内容总结。当前目录下没有子文件夹（因此没有可引用的子目录 README.md）。

---

## 1. 概述

Turnplate 提供以下方法：

- 本目录文档中列出的方法（见下表）。
- Curved Objects（曲线对象）的方法。
- Material Flow Objects（物料流对象）的方法。
- All Objects（所有对象）的方法。

要查看对象的所有方法、只读属性和属性，请打开窗口 **Show Attributes and Methods**。

---

## 2. 语法行约定（Syntax line conventions）

方法的语法行示例如下：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所应用对象的路径。
- 签名（由参数标识符和数据类型组成）列在括号中。例如 `(Parameter:string)` 表示数据类型为 `string` 的参数。除常量值外，也可以使用所需类型的变量，或返回所需数据类型的方法。

> **注意：** 请务必为括号内的表达式输入括号 `(…)`。如果不输入，可能会导致意外结果并打开 Debugger。

- 可选参数列在方括号中。例如 `[,Parameter:boolean]` 表示可以输入、也可以不输入该 boolean 参数。
- 如果参数有默认值，签名会在参数后显示默认值，例如上例中的 `:= false`。
- 如果方法有返回值，签名会在箭头 `->` 后显示其数据类型，例如上例中的 `→ boolean`。

---

## 3. 方法列表

| 方法 | 语法 | 说明 |
| --- | --- | --- |
| **getAttributeList** | `<Path>.getAttributeList(Attributes:table)` | 返回由 `<Path>` 指定的转盘的属性列表。 |
| **rotatePart** | `<Path>.rotatePart(Angle:integer)` | 将转盘上的 MU 旋转指定角度。 |
| **setAttributeList** | `<Path>.setAttributeList(Attributes:table)` | 设置转盘的属性列表，用于确定离开转盘的 MU。 |

---

## 4. 方法详解

### getAttributeList [SimTalk] — Turnplate

返回由 `<Path>` 指定的转盘的属性列表。

**备注（Remarks）**

- 对于 **Strategy > MU Attribute** 策略，包含 MU 的属性名称、属性值以及旋转角度（Angle）。
- 对于 **Strategy > MU Name** 策略，包含部件的属性名称以及旋转角度。

**语法**

```simtalk
<Path>.getAttributeList(Attributes:table)
```

**参数**

参数 `Attributes` 的数据类型为 `table`，表示列表名称。

**示例**

```simtalk
MyTurnplate.getAttributeList(MyAttributesList)
```

**参见：** Strategy [drop-down list] — Turnplate；Open List [Turnplate]；Data Held in Tabular Form in Attributes [material flow objects]。

---

### rotatePart [SimTalk]

将转盘上的 MU 旋转指定角度。

**语法**

```simtalk
<Path>.rotatePart(Angle:integer)
```

**参数**

参数 `Angle` 的数据类型为 `integer`，表示旋转角度。该角度必须是 90 的正倍数或负倍数。

**示例**

```simtalk
?.rotatePart(180)
```

**参见：** Strategy Method [Turnplate]。

---

### setAttributeList [SimTalk] — Turnplate

设置由 `<Path>` 指定的转盘的属性列表。该属性列表用于确定离开转盘的 MU。

**备注（Remarks）**

- 对于 **Strategy > MU Attribute** 策略，可以指定 MU 的属性名称、属性值以及旋转角度。
- 对于 **Strategy > MU Name** 策略，可以指定 MU 名称以及旋转角度。

**语法**

```simtalk
<Path>.setAttributeList(Attributes:table)
```

**参数**

参数 `Attributes` 的数据类型为 `table`，表示一个列表的路径或相同数据类型的变量。Plant Simulation 随后会将传入列表的内容复制到转盘的属性列表中。

**示例**

```simtalk
MyTurnplate.setAttributeList(MyAttributes)
```

**参见：** Strategy [drop-down list] — Turnplate；Open List [Turnplate]；Data Held in Tabular Form in Attributes [material flow objects]。

---

## 5. 相关说明（只读属性）

`methods.md` 末尾还提及了 **Read-Only Attributes of the Turnplate**：

- 只读属性只能查询其值，不能设置，因为 Plant Simulation 在查询时计算其值。
- 大多数情况下，只读属性对应对象某个选项卡（例如 **Statistics**）上不可用的对话框项。

> 只读属性的完整列表请参见同级的 `read-only-attributes/read-only-attributes.md`。
