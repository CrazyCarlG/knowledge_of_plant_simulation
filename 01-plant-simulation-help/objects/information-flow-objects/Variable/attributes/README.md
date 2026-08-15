# Attributes of the Variable

本目录包含 Variable 对象的 SimTalk 属性（Attributes）说明文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `attributes.md` | Variable 对象 SimTalk 属性的整理摘要（Markdown 格式） |
| `attributes.txtx` | Plant Simulation Help 原始导出文本，含属性的完整参考及交叉引用 |

## 概述

Variable（变量）对象的属性只能通过引用运算符 `&` 访问，该运算符将属性应用到 Variable **对象本身**；若省略 `&`，属性将应用到 Variable 的**内容**（值）上。

```simtalk
&Variable.Name := "MyVariable"
```

### 访问属性的方式

- **类（Class）**：在 Class Library 中右键选择 *Show Attributes and Methods*。
- **实例（Instance）**：按下 **F8**，或点击 Frame 的 Home 功能区选项卡上的 *Show Attributes and Methods*。

## 属性列表

Variable 对象共定义了以下 16 个 SimTalk 属性：

| 属性 | 数据类型 | 说明 |
| --- | --- | --- |
| `Alignment` | string | 设置 Variable 与其插入点的对齐方式，可选 `"Left"`、`"Name"`、`"Value"`、`"Right"` |
| `BackgroundColor` | integer | 设置 Variable 在 Frame 中的背景颜色，通过 `makeRGBValue` 指定 RGB 值 |
| `Color` | integer | 设置 Variable 在 Frame 中的字体颜色，通过 `makeRGBValue` 指定 RGB 值 |
| `Comment` | string | 设置 Variable 的注释 |
| `DataType` | string | 设置 Variable 的数据类型 |
| `DecimalPlaces` | integer | 设置 Variable 在 Frame 中显示的小数位数（最多 15 位，默认 `-1` 显示全部） |
| `Font` | integer | 设置 Variable 显示的字体大小：`1`=Small、`2`=Medium、`3`=Large、`4`=Extra Large |
| `HasInitValue` | boolean | 设置 Variable 是否具有初始值 |
| `InitValue` | any | 将仿真运行期间记录的值重置为初始值 |
| `IntegerPlaces` | integer | 设置 Variable 在 Frame 中显示的整数位数（最多 15 位，默认 `-1` 无最小位数） |
| `Name` | string | 设置 Variable 的名称（允许字母、数字和下划线，不能以数字开头） |
| `ShowDataType` | boolean | 在 Frame 中显示（`true`）或隐藏（`false`）数据类型 |
| `ShowUnit` | boolean | 在 Frame 中显示（`true`）或隐藏（`false`）值的单位 |
| `StatisticsActive` | boolean | 是否收集 Variable 的统计值（仅对 `string` 和 `integer` 类型有效） |
| `Transparent` | boolean | 设置 Variable 背景是否透明（该设置在 3D 中同样适用） |
| `Value` | any | 设置 Variable 的值（该属性可被监视 watchable） |

## 备注

- **DecimalPlaces / IntegerPlaces**：仅适用于 `real`、`length`、`money`、`weight`、`time`、`speed`、`acceleration` 等数据类型。对 `time` 类型，`-1` 表示默认时间显示格式（四位小数）。
- **InitValue**：`table`、`list`、`stack`、`queue`、`randtime` 类型不提供初始值重置功能。
- **StatisticsActive**：Variable 仅对 `string` 和 `integer` 类型收集统计数据。
- **Value**：是可监视（watchable）属性，可在 `waituntil` 等语句中用于条件判断。
