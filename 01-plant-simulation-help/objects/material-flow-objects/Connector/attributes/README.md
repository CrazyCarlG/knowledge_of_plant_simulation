# Connector — Attributes（连接器属性）

本目录汇总了 **Connector（连接器）** 对象的属性（attributes）文档。Connector 属于 Material Flow Objects（物流对象）。

## 目录内容

- `attributes.md` — Connector 属性的格式化说明文档。
- `attributes.txtx` — 同一内容的纯文本源导出（两者内容一致）。

## 概述

Connector 提供：

- 左侧目录中列出的属性；
- 所有对象通用的属性（Attributes of All Objects）。

可通过 **Show Attributes and Methods** 窗口查看该对象的所有方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例的 Frame 中 Home 选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。

属性值既可以通过对话框窗口中的复选框、文本框和下拉列表来设置/获取，也可以通过给相应属性赋值来设置/获取：

- **设置属性值**，例如：

```simtalk
MyStation.succConnector(3).Color := makeRGBValue(0,10,100)
```

- **获取属性值**，例如：

```simtalk
print MyStation.succConnector(3).Width
posit := MyStation.Cont.XPos
```

`<Connector-Path>` 表示属性所作用的 Connector 的有效路径：既可以是 Class Library 中指向该 Connector 的绝对路径（`.Materialflow.Connector`），也可以是通过 `predConnector` 或 `succConnector` 方法的访问。

## 只读属性（Read-Only Attribute）

### SuccLane

返回一个 `TwoLaneTrack` 的车道（lane），该车道的起点与 `<Connector-Path>` 指定的 Connector 相连。

- **备注**：后继车道（successor lane）是 Connector 在前进方向上所指向的车道。若后继对象不是 `TwoLaneTrack`，`SuccLane` 返回该后继对象。
- **类型**：只读属性（Read-only attribute）
- **语法**：`<Connector-Path>.SuccLane → any`
- **返回值**：数据类型 `any`
- **示例**：`print Connector2.SuccLane`

## 属性（Attributes）

### Color

设置 `<Connector-Path>` 指定 Connector 的颜色。

- **备注**：
  - 使用 `makeRGBValue` 方法设置颜色的 RGB 值。若给 `Color` 属性赋予无效值，Plant Simulation 会保留当前颜色。
  - 3D 中的 Connector 同样使用此处定义的颜色。Connector 在 Plant Simulation 中的默认 RGB 颜色 `7, 0, 0` 在 3D 中被解释为白色；其他颜色均按 Plant Simulation 中的定义应用。
- **类型**：属性（Attribute）
- **语法**：`<Connector-Path>.Color:integer`
- **赋值**：可赋予 `integer` 数据类型的值。
- **示例**：

```simtalk
MyStation.succConnector(3).Color := makeRGBValue(100,100,100)
MyStation.succConnector(3).Color := 6579300 // 与上面的颜色相同
```

- **参见**：`makeRGBValue [SimTalk]`、`Color [Connector]`

### Width

设置 `<Connector-Path>` 指定 Connector 的线宽。

- **备注**：
  - `Width` 是 `real` 数据类型的值。
  - 可用 `0` 到 `1` 之间的值，将默认线宽（对应 `0` 或 `1`）缩小为其分数倍。
- **类型**：属性（Attribute）
- **语法**：`<Connector-Path>.Width:real`
- **赋值**：可赋予 `real` 数据类型的值，即 `1` 到 `100` 像素之间的数值：

| Width | 含义 |
| --- | --- |
| `-1` | 使 Connector 不可见 |
| `0` | 无论 Frame 窗口是否缩放，线宽恒为 1 像素 |
| `1` | 缩放因子为 100% 时，线宽为 1 像素 |
| `5` | 缩放因子为 100% 时，线宽为 5 像素 |

- **示例**：

```simtalk
MyStation.succConnector(3).Width := 2
.Materialflow.Connector.Width := 0.5
```

- **参见**：`Width [text box] - Connector`

## 相关对象：EventController

**EventController** 对象用于协调、同步和控制仿真运行期间发生的事件。

- **注意**：无法更改 EventController 的名称。
- 可用 EventController 启动、停止和重置仿真。Plant Simulation 是一个离散事件驱动的仿真系统，它在某些时间点上（而非随时间连续地）显示模型组件的状态变化。例如，当一个工件进入某个处理站（如 Station）时，Plant Simulation 会计算处理所需的时间，并将该时间和事件录入 EventController 的已排程事件列表（List of scheduled events）中。
- EventController 像视频播放器的播放头一样沿时间轴移动，并解释与对象执行的事件相关的消息。经过一定的仿真时间（例如 Processing Time）后，EventController 到达工件进入 Station 时设置的标记处；该标记表示处理时间已结束、一个 `Out` 事件待处理。EventController 随即通知 Station 处理该 `Out` 事件，并将工件移动到物料流中的后继对象。Plant Simulation 会对仿真模型中所有 MU 循环重复这一过程。
