# TimeSequence Attributes

本目录汇总 TimeSequence 对象的属性（Attributes）参考文档。

## 目录内容

- `attributes.md` — TimeSequence 属性的完整参考文档。

> 说明：本目录下无子文件夹，因此不存在子目录的 README.md 内容需要合并。

## 概述

TimeSequence 对象用于在仿真运行期间按时间记录数据。要查看对象的全部方法、只读属性和属性，可通过类库上下文菜单或按下 **F8** 键打开 **Show Attributes and Methods** 窗口。

TimeSequence 提供：

- 左侧目录中列出的属性（见下表）。
- Lists 与 Tables 的属性。
- 所有对象的通用属性。

属性的值可以通过对话框中的复选框、文本框、下拉列表，或在 SimTalk 中直接赋值来设置与读取。示例：

```simtalk
MyTimeSequence.ReferenceTime := str_to_time("1:00:00:00.00")  -- 设置属性
print MyTimeSequence.Active                                     -- 读取属性
```

## 属性速查表

| 属性 | 语法 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| `Absolute` | `<Path>.Absolute` | boolean | 将时间参考设为绝对（`true`）或相对（`false`） |
| `Active` | `<Path>.Active` | boolean | 激活（`true`）或停用（`false`）对象，即是否记录数据 |
| `DefaultValue` | `<Path>.DefaultValue` | any | 设置默认值；数据类型与 Contents 选项卡 Value 列一致 |
| `Path` | `<Path>.Path` | string | 设置要记录的值所在的路径（相对或绝对路径） |
| `ReferenceDate` | `<Path>.ReferenceDate` | dateTime | 设置绝对时间参考下时间序列输入的偏移量 |
| `ReferenceTime` | `<Path>.ReferenceTime` | time | 设置开始时间 |
| `Sample` | `<Path>.Sample` | boolean | 周期性记录数据（`true`）或仅在值变化时记录（`false`） |
| `ShowColumnIndex` | `<Path>.ShowColumnIndex` | boolean | 显示（`true`）或隐藏（`false`）列索引 |
| `ShowRowIndex` | `<Path>.ShowRowIndex` | boolean | 显示（`true`）或隐藏（`false`）行索引 |
| `SmpPeriod` | `<Path>.SmpPeriod` | time | 设置采样模式下采样的时间间隔（仅当 `Sample` 为 `true` 时生效） |

## 各属性说明

### Absolute
将 TimeSequence 的时间参考设置为绝对（`true`）或相对（`false`）。

```simtalk
MyTimeSequence.Absolute := true
```

### Active
激活对象（`true`），使其记录数据；或停用对象（`false`）。

```simtalk
MyTimeSequence.Active := true
```

### DefaultValue
设置 TimeSequence 的默认值。数据类型与 TimeSequence 的 **Contents** 选项卡中 **Value** 列的数据类型一致。

```simtalk
MyTimeSequence.DefaultValue := "Body"
```

### Path
设置 TimeSequence 要记录的值的路径，可为相对或绝对路径。

```simtalk
MyTimeSequence.Path := "Station.NumMU"
MyTimeSequence.Path := "&MyVariable"
```

### ReferenceDate
设置 **Time Reference > Absolute** 设置下时间序列输入的偏移量。Plant Simulation 会将其加到时间序列表中的每个时间值上，从而无需重新录入数据即可在时间上平移数值。

```simtalk
ts1.ReferenceDate := sysdate
```

### ReferenceTime
设置 TimeSequence 的开始时间。

```simtalk
ts1.ReferenceTime := str_to_time("1:00:00:00.00")
```

### Sample
使 TimeSequence 周期性记录数据（`true`），或监视数据（仅当值发生变化时记录，`false`）。

```simtalk
ts.Sample := true
```

### ShowColumnIndex
显示（`true`）或隐藏（`false`）TimeSequence 的列索引。

```simtalk
timeSequence2.ShowColumnIndex := false
```

### ShowRowIndex
显示（`true`）或隐藏（`false`）TimeSequence 的行索引。

```simtalk
timeSequence2.ShowRowIndex := true
```

### SmpPeriod
设置 TimeSequence 在采样模式（`Sample` 为 `true`）下采样的频率。

```simtalk
ts.smpPeriod := 60
```

## 相关对象：Trigger

文档还包含 **Trigger** 对象的说明。Trigger 用于在仿真运行期间按照定义的规律改变属性和全局变量的值，也可激活方法执行程序化动作。

- Trigger 将时间映射到变量值；用户定义属性在仿真运行期间取得 Trigger 指定的值。
- 可在单个 TimeSequence 对象中指定值，或组合多个其他 Trigger 的时间序列。
- Trigger 还能控制 Source 创建 MU 的方式与时机。

将 Trigger 添加到模型：**Manage Class Library > Basic Objects > InformationFlow > Trigger**。
