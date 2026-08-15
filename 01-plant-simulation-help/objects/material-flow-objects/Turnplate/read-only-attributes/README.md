# Turnplate（转盘）— 只读属性（Read-Only Attributes）汇总说明

本目录 `read-only-attributes` 汇总了 Turnplate（转盘）物料流对象的只读属性参考文档。Turnplate 是 Plant Simulation 中的一种物料流对象，用于将 MU（可移动单元）旋转到指定方向。

本文件是 `read-only-attributes/read-only-attributes.md` 的内容总结，并参考了同级子目录 `general/README.md` 与 `methods/README.md` 的汇总内容。当前目录下没有子文件夹，因此没有可引用的子目录 README.md。

---

## 1. 概述

Turnplate 提供的只读属性包括：

- 本目录文档中列出的只读属性（见下表）。
- All Objects（所有对象）的只读属性。
- Material Flow Objects（物料流对象）的只读属性。

只读属性只能查询其值，不能设置，因为 Plant Simulation 在查询时计算其值。大多数情况下，只读属性对应对象某个选项卡（例如 **Statistics**）上不可用的对话框项。

要查看对象的所有方法、只读属性和属性，请打开窗口 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，以显示所选 Class 的方法、只读属性和属性。
- 在插入实例的 Frame 的 Home 功能区选项卡上按 **F8** 键或点击 **Show Attributes and Methods**，以显示所选 Instance 的方法、只读属性和属性。

查询只读属性值的示例：

```simtalk
print Turnplate.StatRotationLoadedPortion
```

---

## 2. 只读属性列表

| 只读属性 | 语法 | 返回值 | 说明 |
| --- | --- | --- | --- |
| **StatRotationLoadedPortion** | `<Path>.StatRotationLoadedPortion → real` | `real` | 返回统计收集期内转盘载有 MU 且处于旋转状态的时间占比。 |
| **StatRotationLoadedTime** | `<Path>.StatRotationLoadedTime → time` | `time` | 返回转盘载有 MU 且处于旋转状态的总时间。 |

查询示例：

```simtalk
print MyTurnplate.StatRotationLoadedPortion
print MyTurnplate.StatRotationLoadedTime
```

---

## 3. 只读属性详解

### StatRotationLoadedPortion [SimTalk] — Turnplate

返回由 `<Path>` 指定的转盘在统计收集期内，载有 MU 且处于旋转状态的时间占比。

**语法**

```simtalk
<Path>.StatRotationLoadedPortion → real
```

**返回值**

返回值的数据类型为 `real`。

**示例**

```simtalk
print MyTurnplate.StatRotationLoadedPortion
```

**参见：** Tab Statistics [Turnplate]；Statistics report, Rotation Time。

---

### StatRotationLoadedTime [SimTalk] — Turnplate

返回由 `<Path>` 指定的转盘在载有 MU 时处于旋转状态的总时间。

**语法**

```simtalk
<Path>.StatRotationLoadedTime → time
```

**返回值**

返回值的数据类型为 `time`。

**示例**

```simtalk
print MyTurnplate.StatRotationLoadedTime
```

**参见：** Statistics report, Rotation Time。

---

## 4. 参数 / Attributes（table）

参数 `Attributes` 的数据类型为 `table`，表示一个列表的路径或相同数据类型的变量。Plant Simulation 随后会将传入列表的内容复制到转盘的属性列表中（用于确定离开转盘的 MU 的旋转规则）。

**示例**

```simtalk
MyTurnplate.setAttributeList(MyAttributes)
```

**SimTalk**

```simtalk
getAttributeList [SimTalk] - Turnplate
```

**参见：** Strategy [drop-down list] - Turnplate；Open List [Turnplate]；Data Held in Tabular Form in Attributes [material flow objects]。

---

## 5. 同级目录 README 摘要

### 5.1 general（对象概述）

`general/README.md` 汇总了 Turnplate 的完整参考文档，要点如下：

- **用途**：将 MU 旋转到统一方向，典型应用是包裹运输行业中统一包裹方向以便扫描仪读取地址条形码。
- **关键特性**：
  - 容量为 1，同一时刻转盘上只能有一个 MU。
  - MU 移动到转盘上，当 MU 的 booking point（定位点）到达转盘旋转中心时开始旋转。
  - 转盘上的输送方向是单向的；MU 长度不能超过转盘自身的 Length。
  - 旋转角度应为 90 度的倍数，可输入大于 360 度的值（能被 90 整除）以多次旋转，用于模拟打包机。
  - 默认顺时针旋转 90 度；输入 0 旋转时间则 MU 立即旋转。
- **属性**：Length、Width、Speed、RotationTimePer90Degrees、Strategy、Angle、AttributeType、StrategyCtrl、AutomaticStop，以及只读属性 StatRotationLoadedTime。
- **方法**：getAttributeList、setAttributeList、rotatePart。
- **对话框选项卡**：Attributes、Times、Failures、Controls、Statistics、Energy、Costs、User-defined。
- **Strategy（旋转策略）**：`Angle`、`MU Attribute`、`MU Name`、`Method` 四种。

### 5.2 methods（方法）

`methods/README.md` 汇总了 Turnplate 的方法参考文档，要点如下：

- **语法行约定**：`<Path>` 表示方法所应用对象的路径；参数签名列在括号中；可选参数列在方括号 `[...]` 中；带默认值的参数用 `:= default` 表示；有返回值的方法在箭头 `->` 后显示数据类型。
- **方法列表**：

| 方法 | 语法 | 说明 |
| --- | --- | --- |
| **getAttributeList** | `<Path>.getAttributeList(Attributes:table)` | 返回转盘的属性列表。 |
| **setAttributeList** | `<Path>.setAttributeList(Attributes:table)` | 设置转盘的属性列表，用于确定离开转盘的 MU。 |
| **rotatePart** | `<Path>.rotatePart(Angle:integer)` | 将转盘上的 MU 旋转指定角度（90 的正或负倍数）。 |

- `methods.md` 末尾提及只读属性：只读属性只能查询、不能设置；完整列表见本目录。

---

## 6. 相关参考

- 只读属性对应的统计信息：**Tab Statistics [Turnplate]**，其中额外收集 `Rotation Loaded`（对应只读属性 `StatRotationLoadedPortion`）。
- 查看统计报告：在对象对话框中选择 **View > Show Statistics Report**，或在 Frame 中右键选择 **Show Statistics Report**，或按 **F6**。
- 相关主题：Align and Shrink-Wrap Parts with the Turnplate；Configure the Turnplate to Rotate the Part According to an Attribute。
