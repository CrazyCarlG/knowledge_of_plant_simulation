# Generator - Attributes

本目录包含 Generator（生成器）对象的属性相关文档，来源为 `attributes.md` 与 `attributes.txtx`（同一内容的纯文本提取版本）。以下为内容摘要。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `attributes.md` | Markdown 格式的 Generator 属性说明 |
| `attributes.txtx` | 同一内容的纯文本提取版本 |

## 概述

Generator 提供：

- 本文档所列出的属性。
- **所有对象的属性（Attributes of All Objects）**。

属性值可以设置，也可以获取，方式包括：对话框窗口中的复选框、文本框和下拉列表，或通过给相应属性赋值。

### 查看属性

- 在 Class Library（类库）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **类（Class）** 的方法、只读属性和属性。
- 按下 **F8** 键，或点击插入实例的 Frame 的 **Home** 功能区的 **Show Attributes and Methods**，可查看所选 **实例（Instance）** 的方法、只读属性和属性。

### 设置与获取属性

设置属性值示例：

```simtalk
MyGenerator.Duration.Type := "uniform"
MyGenerator.Duration.Start := 600 // from 10 minutes
MyGenerator.Duration.Stop := 1200 // to 20 minutes
```

获取属性值示例：

```simtalk
print MyGenerator.Duration.Type
posit := Station.Cont.XPos
```

## 属性清单

### Active [SimTalk] - Generator

激活（`true`）或停用（`false`）由 `<Path>` 指定的对象。

- **类型**：Attribute
- **语法**：`<Path>.Active:boolean`
- **可监视（Watchable）**：该属性可被监视。
- **赋值**：可赋 `boolean` 类型值。

```simtalk
MyGenerator.Active := true
```

### Duration [SimTalk] - Generator

设置由 `<Path>` 指定的 Generator 调用 Interval Control 与 Duration Control 之间的时间跨度。

- **类型**：Attribute
- **语法**：`<Path>.Duration:time`
- **赋值**：可赋 `time` 类型值。

```simtalk
MyGenerator.Duration.Type := "uniform"
MyGenerator.Duration.Start := 600 // from 10 minutes
MyGenerator.Duration.Stop := 1200 // to 20 minutes
Generator.Duration.setTypeAndAttr("cEmp", Table)
```

### DurationCtrl [SimTalk]

指定 `<Path>` 对象的一个 Method 对象。Plant Simulation 在调用 `<Path>` 指定的 Generator 的 Interval Control 之后调用该 Method。

- **类型**：Attribute
- **语法**：`<Path>.DurationCtrl:method`
- **赋值**：可赋 `method` 类型值。

```simtalk
// does an entry exist?
if MyGenerator.DurationCtrl /= VOID // delete entry
   MyGenerator.DurationCtrl := VOID
end
```

### Interval [SimTalk] - Generator

设置 `<Path>` 指定的 Generator 两次激活 Interval Control 之间的时间间隔。

- **类型**：Attribute
- **语法**：`<Path>.Interval:time`
- **赋值**：可赋 `time` 类型值。

```simtalk
obj.Interval.Type:= "Negexp"
obj.Interval.Beta:=150
obj.Interval.LowerBound:=1*60   // 1s *60
obj.Interval.UpperBound:= 10*60 // 10s *60
Generator.Interval.setTypeAndAttr("dEmp", Table)
```

### IntervalCtrl [SimTalk]

指定 `<Path>` 对象的一个 Method 对象。Plant Simulation 在指定间隔内为 `<Path>` 指定的 Generator 调用该 Method。

- **类型**：Attribute
- **语法**：`<Path>.IntervalCtrl:method`
- **赋值**：可赋 `method` 类型值。

```simtalk
// nothing entered yet?
if MyGenerator.IntervalCtrl = VOID
   // enter reference to method
   MyGenerator.IntervalCtrl := &MyMethod
end
```

### Start [SimTalk] - Generator

设置 Generator 调用 Interval Control 的开始时间。

- **类型**：Attribute
- **语法**：`<Path>.Start:time`
- **赋值**：可赋 `time` 类型值。
- **备注**：赋值必须在 Reset（复位）阶段进行。

```simtalk
MyPlant.MyGenerator.Start.type := "const"
MyPlant.MyGenerator.Start := 120 // 2 minutes
Generator.Start.setTypeAndAttr("Normal", 30, 10)
```

### Stop [SimTalk] - Generator

设置 Generator 调用 Interval Control 的停止时间。

- **类型**：Attribute
- **语法**：`<Path>.Stop:time`
- **赋值**：可赋 `time` 类型值。

```simtalk
// normally distributed end with left bound at 1 hour
// and open right bound
.InformationFlow.MyGenerator.Stop.Type := "normal"   // normal distribution
.InformationFlow.MyGenerator.Stop.Mu := 3600         // 1 hour
.InformationFlow.MyGenerator.Stop.Sigma := 600       // 10 minutes
.InformationFlow.MyGenerator.Stop.LowerBound := 1200 // 20 minutes
.InformationFlow.MyGenerator.Stop.UpperBound := 7200 // 2 hours
Generator.Stop.setTypeAndAttr("Normal", 1:00, 10)
```

### AttributeExplorer [object]

使用 **AttributeExplorer** 对象在单一中心位置管理定义仿真模型中各个工位（station）设置的属性。

- 无需逐一打开模型中每个物流对象的对话框输入属性值，即可定义 AttributeExplorer 获取并显示在列表窗口中的属性。
- 点击 **Show Explorer**，输入各值（容量、时间等），Plant Simulation 会写回对象并在模型中使用。
- 可将设置表 **Export** 为制表符分隔的文本文件，并 **Import** 到另一个仿真模型的 AttributeExplorer 中，从而在多个模型中复用相同设置。
- 还可在 HtmlReport 中显示 AttributeExplorer 的属性表，或比较/显示 AttributeExplorer。
- 悬停鼠标可显示提示框；点击 Edit 功能区的 **Show Manipulators** 或按 **M** 键可更改图形长度与锚点。

**将对象添加到仿真模型**：点击 Home 功能区选项卡上的

> Manage Class Library > Basic Objects > InformationFlow > AttributeExplorer

## 参考信息

- 原文出处：Plant Simulation Help，页码 11-4397 至 11-4406，© 2026 Siemens。
