# Turnplate（转盘）— 汇总说明

本目录 `general` 汇总了 Turnplate（转盘）物料流对象的完整参考文档。Turnplate 是 Plant Simulation 中的一种物料流对象，用于将 MU（可移动单元）旋转到指定方向。

本文件是 `general/general.md` 以及子目录 `attributes/attributes.md`、`methods/methods.md`、`read-only-attributes/read-only-attributes.md` 的内容总结。

---

## 1. 对象概述（general）

Turnplate（转盘）用于旋转 MU。典型应用场景：在包裹运输行业中，所有包裹需要旋转到统一方向，以便扫描仪自动读取包含地址信息的条形码。

### 关键特性

- **容量为 1**：转盘上同一时刻只能有一个 MU。
- MU 移动到转盘上，当 MU 的 booking point（定位点）到达转盘旋转中心时，转盘开始旋转。
- 旋转完成后，MU 离开转盘。
- 转盘上的输送方向是**单向**的（MU 不能先向前再向后）。
- MU 的长度不能超过转盘自身的 Length。
- 旋转中心默认位于转盘中心。
- 旋转需要一定时间。可输入每 90 度旋转步的时间。若输入 0，则 MU 立即旋转，不消耗任何时间。
- 旋转角度应为 90 度的倍数。若输入其他角度，Plant Simulation 会四舍五入到下一个可被 90 整除的角度。可输入大于 360 度的值（只要能被 90 整除），这样转盘可让 MU 多次旋转，用于模拟打包机（如收缩包装机）。默认顺时针旋转 90 度。
- 转盘旋转 MU 且 MU 离开后，转盘返回起始位置。
- 可在 Length-oriented Objects 的 Appearance 选项卡上选择不同的转盘配置。

### 添加对象到仿真模型

点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > MaterialFlow > Turnplate**。

---

## 2. 属性（Attributes）

Turnplate 提供的属性包括下表列出的属性，以及所有对象的属性和物料流对象的属性。可通过窗口 **Show Attributes and Methods** 查看。

属性可以设置（set）和获取（get）其值。例如：

```simtalk
MyTurnplate.angle := 180          -- 设置
print MyTurnplate.angle           -- 获取
```

### 属性列表

| 属性 | 数据类型 | 说明 |
| --- | --- | --- |
| **Length** | `length` | 设置转盘长度。转盘只能旋转能完整容纳的 MU（短于或等于该值）。可监视（watchable）。 |
| **Width** | `length` | 设置转盘宽度。可监视。 |
| **Speed** | `speed` | 设置 MU 位于转盘上时转盘的输送速度。可输入 `-1` 表示无限速度。可监视。 |
| **RotationTimePer90Degrees** | `time` | 设置转盘每旋转 90 度所需的时间。输入 0 表示立即旋转。 |
| **Strategy** | `string` | 设置转盘旋转 MU 的策略：`"Angle"`、`"MU Attribute"`、`"MU Name"`、`"Method"`。 |
| **Angle** | `integer` | 设置转盘旋转 MU 的角度（度）。应为 90 的倍数；负值表示逆时针。 |
| **AttributeType** | `string` | 设置决定旋转角度的属性数据类型（适用于 Strategy > MU Attribute）。 |
| **StrategyCtrl** | `method` | 指定确定旋转角度的方法对象（适用于 Strategy > Method）。 |
| **AutomaticStop** | `boolean` | 当不输送 MU 时自动将当前速度设为 0。 |
| **StatRotationLoadedTime** | `time`（只读） | 返回转盘在载有 MU 时处于旋转状态的总时间。 |

> 注：`StatRotationLoadedTime` 同时出现在只读属性文档中；它在 attributes.md 中作为统计时间属性列出。

---

## 3. 方法（Methods）

Turnplate 提供的方法包括下表中的方法，以及 Curved Objects、Material Flow Objects 和 All Objects 的方法。

### 方法列表

| 方法 | 语法 | 说明 |
| --- | --- | --- |
| **getAttributeList** | `<Path>.getAttributeList(Attributes:table)` | 返回转盘的属性列表（MU Attribute 或 MU Name 策略下对应的属性名、值、旋转角度）。 |
| **setAttributeList** | `<Path>.setAttributeList(Attributes:table)` | 设置转盘的属性列表（确定离开转盘的 MU 的旋转规则）。 |
| **rotatePart** | `<Path>.rotatePart(Angle:integer)` | 按指定角度旋转转盘上的 MU。角度必须是 90 的正或负倍数。 |

### 语法行约定

- `<Path>` 表示方法所应用对象的路径。
- 签名（参数标识符和数据类型）在括号中列出。
- 可选参数用方括号 `[...]` 表示。
- 带默认值的参数在参数后用 `:= default` 表示。
- 有返回值的方法在箭头 `->` 后显示数据类型。

---

## 4. 只读属性（Read-Only Attributes）

只读属性只能查询，不能设置，因为 Plant Simulation 在查询时计算其值。大多数情况下只读属性对应对象某个选项卡（如 Statistics）上不可用的对话框项。

### 只读属性列表

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

## 5. 对话框选项卡（general.md 摘要）

Turnplate 的对话框包含以下选项卡：

- **Attributes**：设置 Length、Width、Speed、Rotation Time per 90°、Strategy、Angle、Attribute Type、Open List、Strategy Method、Automatic Stop 等。
- **Times**：定义时间分布（可用 `setTypeAndAttr` 方法设置）。
- **Failures**：定义故障。
- **Controls**：提供控件修改对象内置行为（如 Entrance / Exit / Pull 控制）。
- **Statistics**：统计信息，额外收集 `Rotation Loaded`（对应只读属性 `StatRotationLoadedPortion`）。
- **Energy**：能源设置。
- **Costs**：成本设置。转盘输送 MU 时产生成本（总投资成本 + 总运营成本）。
- **User-defined**：定义用户自定义属性。

### 菜单

- **Navigate 菜单**、**View 菜单**、**Tools 菜单**、**Tabs 菜单**、**Help 菜单**等。

---

## 6. Strategy（旋转策略）详解

Strategy 属性决定转盘如何旋转部件，有四种策略：

1. **Angle**：按输入的旋转角度旋转 MU。
2. **MU Attribute**：根据 MU 的内置或用户自定义属性旋转。点击 **Open List** 输入属性名、属性值和旋转角度。
3. **MU Name**：根据 MU 名称旋转。点击 **Open List** 输入 MU 名称和旋转角度。
4. **Method**：根据策略方法旋转。方法内必须调用 `rotatePart`，参数为旋转角度。

默认策略方法（作为用户自定义属性）如下：

```simtalk
?.rotatePart(90)
```

---

## 7. 相关参考

- 示例模型：Window 功能区选项卡 > **Start Page > Getting Started > Example Models > Small Examples**。
- 相关主题：Align and Shrink-Wrap Parts with the Turnplate、Configure the Turnplate to Rotate the Part According to an Attribute。
- YouTube 视频：https://youtu.be/hOvdrDnvXXo?si=Cs5gOF4JB5PBlVma&t=532
