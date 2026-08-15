# Connector Methods（连接器方法）

本目录汇总了 **Connector（连接器）** 对象的方法（methods）文档。Connector 属于 Material Flow Objects（物流对象）。

## 目录内容

- `methods.md` — Connector 方法及只读属性的说明文档。

## 概述

Connector 提供：

- 左侧目录中列出的方法。
- 所有对象通用的方法（Methods of All Objects）。

可通过 **Show Attributes and Methods** 窗口查看该对象的所有方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例的 Frame 中 Home 选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。

## 语法行（Syntax Line）说明

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所作用对象的路径。
- 括号内为签名（参数的标识符和数据类型）。`(Parameter:string)` 表示一个 string 类型的参数；除了常量，也可以使用所需类型的变量或返回所需类型的方法。
- 可选参数写在方括号内。`[,Parameter:boolean]` 表示可以但不必输入该 boolean 参数。
- 若参数有默认值，签名会在参数后显示，例如 `:= false`。
- 若方法有返回值，签名会在箭头 `->` 后显示其数据类型。

> **注意**：请务必为嵌套在括号内的表达式输入括号 `(…)`，否则可能导致意外结果并打开 Debugger。

## 方法列表

### connect [SimTalk]

将 Frame 中指定的对象与 `<Connector-Path>` 所指定的 Connector 连接起来。

**备注**：`connect` 方法也可以连接两条 TwoLaneTrack（双车轨道）的任意一端。为此需向 `connect` 传入两条车道（lane）；第一条车道的出口会与第二条车道的入口相连。该方法连接的是 TwoLaneTrack 本身，而非单独的车道。

**类型**：Method

**语法**：

```
<Connector-Path>.connect(StartOfConnection:any, EndOfConnection:any) → object
<Connector-Path>.connect(StartOfConnection:any, EndOfConnection:any[, SideOfConverterStart:integer, SideOfConverterEnd:integer]) → object
```

**参数**：

- `StartOfConnection`（`any`）— 指定 `<Connector-Path>` 所指定 Connector 的起点。
- `EndOfConnection`（`any`）— 指定连接的终点。

第一个或第二个参数也可以是一个 Interface 对象。返回值是刚创建的 Connector。若 Plant Simulation 无法创建该 Connector，会打开 Method Debugger。

- `SideOfConverterStart`（`integer`，可选）— 设置 Connector 停靠在 Converter 的哪一侧：`0` = 右，`1` = 下，`2` = 左，`3` = 上。
- `SideOfConverterEnd`（`integer`，可选）— 仅当在两个 Converter 之间插入 Connector 时需要。此时 `SideOfConverterStart` 指定源 Converter 的一侧，`SideOfConverterEnd` 指定目标 Converter 上 Connector 结束的一侧。

**返回值**：数据类型为 `object`，即所创建的 Connector。

**示例**：

```
.Materialflow.Connector.connect(Station, Store)
.Materialflow.Connector.connect(Station, Interface3)
.Materialflow.Connector.connect(T1, T2)
// connects the exit of T1 with the entrance of T2
.Materialflow.Connector.connect(T1.A, T2.A)
// connects the exit of T1 with the entrance of T2
.Materialflow.Connector.connect(T1.A, T2.B)
// connects the exit of T1 with the exit of T2
.Materialflow.Connector.connect(T1.B, T2.A)
// connects the entrance of T1 with the entrance of T2
.MaterialFlow.Connector.connect("TwoLaneTrack1.B", "TwoLaneTrack2.A")
// connects lanes of two-laned tracks
```

## 只读属性（Read-Only Attributes）

Connector 提供：

- 左侧目录中列出的只读属性。
- 所有对象通用的只读属性（Read-Only Attributes of All Objects）。
- 物流对象通用的只读属性（Read-Only Attributes of the Material Flow Objects）。

可以查询只读属性的值，但无法设置它们，因为 Plant Simulation 会在查询的时间点计算该值。大多数情况下，只读属性对应对象某个选项卡（如 Statistics 选项卡）上不可用的对话框项。
