# Display Attributes（Display 对象属性）

本目录汇总了 **Display** 对象的 SimTalk 属性。Display 对象用于在 Frame 中可视化由某个路径（Path）指定的值。

## 概述

Display 对象提供：

- 本目录所列的属性。
- 「所有对象的属性」（Attributes of All Objects）。

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类。
- 按 **F8**，或点击 Frame 的 Home 功能区的 **Show Attributes and Methods**，可显示所选实例。

可以通过对话框窗口设置/获取属性值，也可以通过赋值语句设置/获取：

```simtalk
-- 设置值
Display1.Sampler := false
Display1.Path := "MyConveyor.NumMU"
Display2.Sampler := true
Display2.SmpInterval := 300
Display2.Path := "root.MyConveyor.utilization"

-- 获取值
print Display1.Path
posit := Station.Cont.XPos
```

## 属性列表

### GetStandardDeviation（只读属性）
返回 Display 所记录值的标准差。

- **语法：** `<Path>.GetStandardDeviation → real`
- **返回值：** 数据类型 `real`

```simtalk
print MyDisplay.GetStandardDeviation
```

### Active（属性）
激活（`true`）或停用（`false`）由 `<Path>` 指定的对象。

- **语法：** `<Path>.Active:boolean`
- **赋值：** `boolean`

```simtalk
MyDisplay.active := true
```

### Color（属性）
设置 Display 在 Frame 中显示值所用的颜色。

- **备注：** 使用 `makeRGBValue` 方法设置 RGB 颜色值。
- **语法：** `<Path>.Color:integer`
- **赋值：** `integer`

```simtalk
MyDisplay.Color := makeRGBValue(255,0,0)
```

### Comment（属性）
设置 Display 在 Frame 中图标下方显示的注释。

- **语法：** `<Path>.Comment:string`
- **赋值：** `string`

```simtalk
MyDisplay.Comment := "My comment"
```

### DecimalPlaces（属性）
设置 Display 显示的小数位数。

- **备注：** 最多可显示 15 位小数；默认 `-1` 显示所有位数；输入正数则显示相应位数。
- **注意：** 此设置仅适用于 Type > Text（文本模式）。
- **语法：** `<Path>.DecimalPlaces:integer`
- **赋值：** `integer`

```simtalk
MyDisplay.DecimalPlaces := 10
```

### DisplayType（属性）
设置 Display 以文本（Text）、条形（Bar）或饼图分段（Pie Segment）方式显示输入值。

- **备注：** Bar 与 Pie 表示法将指定范围内的值映射为不同高度的条形或不同完成度的饼图；范围通过 `MinVal` 与 `MaxVal` 设置。
- **语法：** `<Path>.DisplayType:string`
- **赋值：** `string` — 可取 `"Text"`、`"Bar"` 或 `"Pie"`。

```simtalk
MyDisplay.DisplayMode := "Text"
```

### Font（属性）
设置 Display 以 Text 模式显示文本与注释的字体大小。

- **语法：** `<Path>.Font:integer`
- **赋值：** `integer` — `1` 小、`2` 中、`3` 大、`4` 特大。

```simtalk
MyDisplay.Font := 2
```

### MaxVal（属性）
设置 Bar 与 Pie 模式下显示范围的上限。

- **备注：** 大于等于 `MaxVal` 的值显示为满条/满饼。
- **语法：** `<Path>.MaxVal:real`
- **赋值：** `real`

```simtalk
MyDisplay.MinVal := 10.0
MyDisplay.MaxVal := 35.713
```

### MinVal（属性）
设置 Bar 与 Pie 模式下显示范围的下限。

- **备注：** 小于等于 `MinVal` 的值显示为空条/空饼。
- **语法：** `<Path>.MinVal:real`
- **赋值：** `real`

```simtalk
MyDisplay.MinVal := 5.35
```

### Path（属性）
设置 Display 所示值的路径。

- **语法：** `<Path>.Path:string`
- **赋值：** `string`

```simtalk
Display1.Sampler := false
Display1.Path := "MyConveyor.NumMU"
Display2.Sampler := true
Display2.SmpInterval := 300
Display2.Path := "root.MyConveyor.utilization"
```

### Sampler（属性）
激活（`true`）或停用（`false`）Display 的采样模式。

- **语法：** `<Path>.Sampler:boolean`
- **赋值：** `boolean`
  - `true`：**采样模式（Sample mode）** — 周期性更新显示，与输入值是否变化无关。
  - `false`：**监视模式（Watch mode）** — 输入值变化时更新显示。

```simtalk
if MeinDisplay.Sampler = false
   MyDisplay.Sampler := true // 激活采样模式
   MyDisplay.SmpInterval := 360 // 10 分钟
end
```

### SmpPeriod（属性）
设置 Display 更新显示的间隔，其值必须大于零。

- **备注：** `SmpPeriod` 适用于采样模式。
- **语法：** `<Path>.SmpPeriod:time`
- **赋值：** `time`

```simtalk
MyDisplay.SmpPeriod := str_to_time("3:00.0")
MyDisplay.SmpPeriod := 2 * MyDisplay.SmpPeriod
-- 间隔加倍，采样率减半
```

### Transparent（属性）
设置对象背景在 Frame 中是否透明（`true` 透明，`false` 不透明）。

- **语法：** `<Path>.Transparent:boolean`
- **赋值：** `boolean`
  - `true`：文本周围空间显示为 Frame 背景图像的颜色。
  - `false`：文本周围空间显示为白色。

```simtalk
MyDisplay.Transparent := false
```

### Value（属性）
设置或获取 Display 所显示的值。

- **备注：**
  - `Value` 仅用于监视模式（Watch Mode）。
  - 在采样模式（Sample Mode）下，仅当 **MUs and States** 被激活且 Display 所在 Frame 打开时，Plant Simulation 才会更新该值。
  - 在采样模式下获取该值时，Plant Simulation 会先更新该值。
- **语法：** `<Path>.Value:real`
- **赋值：** `real`
- **返回值：** 被观测值的数据类型

```simtalk
MyDisplay.Value := 5
print MyDisplay.Value
```

## 相关对象：Chart

**Chart** 对象用于呈现仿真运行的当前数据与结果。

可通过以下方式定义要绘制的数据：

- 使用包含数据的 Table（例如仿真结果）。
- 定义 Input Channels，记录关注对象的属性值。

插入到 Frame 中的 Chart 提供 **Statistics Wizard**（统计向导）。在 Frame 的上下文菜单中选择 **Statistics Wizard** 命令即可打开。

---

*来源：`attributes.md` 与 `attributes.txtx`（Siemens Plant Simulation Help）*
