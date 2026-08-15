# Turnplate（转盘）— 属性（Attributes）汇总说明

本目录 `attributes` 汇总了 Turnplate（转盘）物料流对象的属性参考文档。Turnplate 是 Plant Simulation 中的一种物料流对象，用于将 MU（可移动单元）旋转到指定方向。

本文件是 `attributes/attributes.md` 的内容总结，并参考了同级子目录 `general/README.md`、`methods/README.md` 与 `read-only-attributes/README.md` 的汇总内容。当前目录下没有子文件夹，因此没有可引用的子目录 README.md。

---

## 1. 概述

Turnplate 提供的属性包括：

- 本目录文档中列出的属性（见下表）。
- All Objects（所有对象）的属性。
- Material Flow Objects（物料流对象）的属性。

要查看对象的所有方法、只读属性和属性，请打开窗口 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，以显示所选 Class 的方法、只读属性和属性。
- 在插入实例的 Frame 的 Home 功能区选项卡上按 **F8** 键或点击 **Show Attributes and Methods**，以显示所选 Instance 的方法、只读属性和属性。

属性可以设置（set）和获取（get）其值，既可以通过对话框中的复选框、文本框和下拉列表，也可以通过给相应属性赋值来实现。

设置属性值的示例：

```simtalk
MyTurnplate.angle := 180
```

获取属性值的示例：

```simtalk
print MyTurnplate.angle
posit := MyStation.Cont.XPos
```

---

## 2. 属性列表

| 属性 | 数据类型 | 语法 | 说明 |
| --- | --- | --- | --- |
| **Length** | `length` | `<Path>.Length:length` | 设置转盘长度。转盘只能旋转能完整容纳的 MU（短于或等于该值）。可监视（watchable）。 |
| **Width** | `length` | `<Path>.Width:length` | 设置转盘宽度。可监视。 |
| **Speed** | `speed` | `<Path>.Speed:speed` | 设置 MU 位于转盘上时转盘的输送速度。可输入 `-1` 表示无限速度。可监视。 |
| **RotationTimePer90Degrees** | `time` | `<Path>.RotationTimePer90Degrees:time` | 设置转盘每旋转 90 度所需的时间。输入 0 表示立即旋转，不消耗时间。 |
| **Strategy** | `string` | `<Path>.Strategy:string` | 设置转盘旋转 MU 的策略：`"Angle"`、`"MU Attribute"`、`"MU Name"`、`"Method"`。 |
| **Angle** | `integer` | `<Path>.Angle:integer` | 设置转盘旋转 MU 的角度（度）。应为 90 的倍数；负值表示逆时针。 |
| **AttributeType** | `string` | `<Path>.AttributeType:string` | 设置决定旋转角度的属性数据类型（适用于 Strategy > MU Attribute）。 |
| **StrategyCtrl** | `method` | `<Path>.StrategyCtrl:method` | 指定确定旋转角度的方法对象（适用于 Strategy > Method）。 |
| **AutomaticStop** | `boolean` | `<Path>.AutomaticStop:boolean` | 当不输送 MU 时自动将当前速度设为 0。 |
| **StatRotationLoadedTime** | `time`（只读） | `<Path>.StatRotationLoadedTime → time` | 返回转盘在载有 MU 时处于旋转状态的总时间。 |

> 注：`StatRotationLoadedTime` 同时出现在只读属性文档中；它在 `attributes.md` 中作为统计时间属性列出。

---

## 3. 属性详解

### Length [SimTalk] — Turnplate

设置由 `<Path>` 指定的转盘的长度。

**备注（Remarks）**

转盘只能旋转能完整容纳的 MU，即 MU 短于或等于此处输入的值。

**语法**

```simtalk
<Path>.Length:length
```

**可监视（Watchable）**：该属性可监视。

**赋值（Assignment Value）**

可赋数据类型为 `length` 的值。

**注意（Note）**

在 SimTalk 2.0 中可指定长度单位 `m`、`mm`、`km`、`cm`、`yd`、`ft`、`in`。单位直接写在数值之后，不加空格，例如 `10m` 或 `10.2m`。浮点值和整数值均可指定单位。

**示例**

```simtalk
MyTurnplate.Length := 2.0m
```

**参见：** Length [text box] - Turnplate。

---

### Width [SimTalk] — Turnplate

设置由 `<Path>` 指定的转盘的宽度。

**语法**

```simtalk
<Path>.Width:length
```

**可监视（Watchable）**：该属性可监视。

**赋值（Assignment Value）**

可赋数据类型为 `length` 的值。

**注意（Note）**

在 SimTalk 2.0 中可指定长度单位 `m`、`mm`、`km`、`cm`、`yd`、`ft`、`in`。单位直接写在数值之后，不加空格。

**示例**

```simtalk
MyTurnplate.Width := 2 // meters
```

**参见：** Width [text box] - Turnplate, Track。

---

### Speed [SimTalk] — Turnplate

设置由 `<Path>` 指定的转盘在 MU 位于转盘上时输送 MU 的速度。

**备注（Remarks）**

输入 `-1` 表示无限速度。

**语法**

```simtalk
<Path>.Speed:speed
```

**可监视（Watchable）**：该属性可监视。

**赋值（Assignment Value）**

可赋数据类型为 `speed` 的值。

**注意（Note）**

在 SimTalk 2.0 中可指定速度单位 `mps`、`fps`、`kmh`、`mph`。单位直接写在数值之后，不加空格，例如 `100kmh` 或 `100.5kmh`。

```simtalk
var len := 1.0ft
var s : speed := 10.5m / 1:30
var x : length := 3m
```

在 SimTalk 2.0 中可输入单位 `s` 表示秒。有时输入单位是必要的，以确保计算表达式具有正确的数据类型：

```simtalk
var x : length := 10m
var s : speed := x / 2s   // 注意：x/2 的单位会出错，为 m 而不是 m/s
```

**示例**

```simtalk
MyTurnplate.Speed := 1.5
```

**参见：** Speed [text box] - Turnplate。

---

### RotationTimePer90Degrees [SimTalk] — Turnplate

设置由 `<Path>` 指定的转盘每旋转 90 度一步所需的时间。

**备注（Remarks）**

输入旋转时间为 0 表示立即旋转 MU，不消耗任何时间。

**语法**

```simtalk
<Path>.RotationTimePer90Degrees:time
```

**赋值（Assignment Value）**

可赋数据类型为 `time` 的值。

**示例**

```simtalk
MyTurnplate.RotationTimePer90Degrees := 0.75
```

**参见：** Rotation Time per 90° [text box] - Turnplate。

---

### Strategy [SimTalk] — Turnplate

设置由 `<Path>` 指定的转盘旋转 MU 所依据的策略。

**语法**

```simtalk
<Path>.Strategy:string
```

**赋值（Assignment Value）**

可赋数据类型为 `string` 的值。可指定：

- `"Angle"`：按指定的旋转角度（Angle）旋转 MU。
- `"MU Attribute"`：按部件的内置或用户自定义属性旋转 MU。
- `"MU Name"`：按 MU 名称旋转 MU。
- `"Method"`：按策略方法旋转 MU。该方法内必须调用 `rotatePart`，并以旋转角度作为参数。

**示例**

```simtalk
MyTurnplate.Strategy := "MU Attribute"
```

**SimTalk：** Angle [SimTalk] - Turnplate, rotatePart [SimTalk]。

**参见：** Strategy [drop-down list] - Turnplate, Angle [text box] - Turnplate。

---

### Angle [SimTalk] — Turnplate

设置由 `<Path>` 指定的转盘旋转 MU 的旋转角度（度）。

**备注（Remarks）**

- 旋转角度应为 90 度的倍数。若指定其他角度，Plant Simulation 会四舍五入到下一个可被 90 整除的角度。
- 可指定大于 360 度的值（只要能被 90 整除），这样转盘可让 MU 多次旋转，用于模拟打包机。
- 默认转盘顺时针旋转 90 度。要逆时针旋转，请指定负角度。

**语法**

```simtalk
<Path>.Angle:integer
```

**赋值（Assignment Value）**

可赋数据类型为 `integer` 的值。

**示例**

```simtalk
MyTurnplate.Angle := 90
```

**参见：** Angle [text box] - Turnplate。

---

### AttributeType [SimTalk] — Turnplate

设置由 `<Path>` 指定的转盘的属性类型（Attribute Type）。

**备注（Remarks）**

`AttributeType` 适用于 Strategy > MU Attribute。

**语法**

```simtalk
<Path>.AttributeType:string
```

**赋值（Assignment Value）**

可赋数据类型为 `string` 的值。

**示例**

```simtalk
MyTurnplate.AttributeType := "String"
```

**参见：** Attribute Type [drop-down list] - Turnplate, Strategy [drop-down list] - Turnplate。

---

### StrategyCtrl [SimTalk] — Turnplate

指定由 `<Path>` 指定的对象的一个 Method 对象。在其中输入确定转盘旋转 MU 的旋转角度的源代码。

**备注（Remarks）**

当 MU 的 booking point（定位点）到达转盘旋转中心时，转盘会为策略方法调用该 Method。该方法内必须调用 `rotatePart`，并以旋转角度作为参数。

默认策略方法如下：

```simtalk
?.rotatePart(90)
```

**语法**

```simtalk
<Path>.StrategyCtrl:method
```

**赋值（Assignment Value）**

可赋数据类型为 `method` 的值。

**示例**

```simtalk
var rotAngle: integer
if @.typeOf(~.MyPart)           // 旋转部件
   rotAngle := 90
else
   if @.typeOf(~.MyPallet)      // 旋转托盘
        rotAngle := -(4 * 360)  // 负号 (-) 表示逆时针
    end
end
?.rotatePart(rotAngle)
```

```simtalk
MyTurnplate.StrategyCtrl := &myRotationStrategy
```

**SimTalk：** rotatePart [SimTalk]。

**参见：** Strategy Method [Turnplate]。

---

### AutomaticStop [SimTalk] — Turnplate

自动停止由 `<Path>` 指定的转盘。即当转盘不输送 MU 时，将当前速度设为 0。

**备注（Remarks）**

例如当转盘为空，或因 MU 无法离开而被阻塞时，就可能出现这种情况。当转盘速度为 0 时，其能量状态变为 operational（运行）。

**语法**

```simtalk
<Path>.AutomaticStop:boolean
```

**赋值（Assignment Value）**

可赋数据类型为 `boolean` 的值。

**示例**

```simtalk
MyTurnplate.AutomaticStop := true
```

**参见：** Automatic Stop [check box] - Turnplate, Operational [energy]。

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

## 4. 同级目录 README 摘要

### 4.1 general（对象概述）

`general/README.md` 汇总了 Turnplate 的完整参考文档，要点如下：

- **用途**：将 MU 旋转到统一方向，典型应用是包裹运输行业中统一包裹方向以便扫描仪读取地址条形码。
- **关键特性**：
  - 容量为 1，同一时刻转盘上只能有一个 MU。
  - MU 移动到转盘上，当 MU 的 booking point（定位点）到达转盘旋转中心时开始旋转。
  - 转盘上的输送方向是单向的；MU 长度不能超过转盘自身的 Length。
  - 旋转角度应为 90 度的倍数，可输入大于 360 度的值（能被 90 整除）以多次旋转，用于模拟打包机。
  - 默认顺时针旋转 90 度；输入 0 旋转时间则 MU 立即旋转。
- **对话框选项卡**：Attributes、Times、Failures、Controls、Statistics、Energy、Costs、User-defined。
- **Strategy（旋转策略）**：`Angle`、`MU Attribute`、`MU Name`、`Method` 四种。

### 4.2 methods（方法）

`methods/README.md` 汇总了 Turnplate 的方法参考文档，要点如下：

- **语法行约定**：`<Path>` 表示方法所应用对象的路径；参数签名列在括号中；可选参数列在方括号 `[...]` 中；带默认值的参数用 `:= default` 表示；有返回值的方法在箭头 `->` 后显示数据类型。
- **方法列表**：

| 方法 | 语法 | 说明 |
| --- | --- | --- |
| **getAttributeList** | `<Path>.getAttributeList(Attributes:table)` | 返回转盘的属性列表。 |
| **setAttributeList** | `<Path>.setAttributeList(Attributes:table)` | 设置转盘的属性列表，用于确定离开转盘的 MU。 |
| **rotatePart** | `<Path>.rotatePart(Angle:integer)` | 将转盘上的 MU 旋转指定角度（90 的正或负倍数）。 |

### 4.3 read-only-attributes（只读属性）

`read-only-attributes/README.md` 汇总了 Turnplate 的只读属性参考文档，要点如下：

- 只读属性只能查询、不能设置，因为 Plant Simulation 在查询时计算其值。
- 大多数情况下，只读属性对应对象某个选项卡（例如 **Statistics**）上不可用的对话框项。

| 只读属性 | 语法 | 返回值 | 说明 |
| --- | --- | --- | --- |
| **StatRotationLoadedPortion** | `<Path>.StatRotationLoadedPortion → real` | `real` | 返回统计收集期内转盘载有 MU 且处于旋转状态的时间占比。 |
| **StatRotationLoadedTime** | `<Path>.StatRotationLoadedTime → time` | `time` | 返回转盘载有 MU 且处于旋转状态的总时间。 |

---

## 5. 相关参考

- 属性对应的对话框项：**Length [text box]**、**Width [text box]**、**Speed [text box]**、**Rotation Time per 90° [text box]**、**Strategy [drop-down list]**、**Angle [text box]**、**Attribute Type [drop-down list]**、**Open List [Turnplate]**、**Strategy Method [Turnplate]**、**Automatic Stop [check box]**。
- 相关主题：Align and Shrink-Wrap Parts with the Turnplate；Configure the Turnplate to Rotate the Part According to an Attribute。
- 方法参考：`rotatePart [SimTalk]`、`getAttributeList [SimTalk]`、`setAttributeList [SimTalk]`。
