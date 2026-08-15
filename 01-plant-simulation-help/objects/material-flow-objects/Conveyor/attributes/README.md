# Conveyor — Attributes（属性）— 目录说明

本目录包含 Conveyor（传送带/输送机）对象的 **属性（Attributes）** SimTalk 参考文档。本文档是对 `attributes.md` 的摘要，并汇总了同层级相关文档（`general`、`methods`、`read-only-attributes`）的目录说明内容。

## 目录内容

- `attributes.md` — Conveyor 属性的完整说明（SimTalk 语法、类型、返回值与示例）
- `attributes.txtx` — 同一文档的原始文本版本（Siemens Plant Simulation Help 导出内容）

## 对象概述

Conveyor 是**长度导向（length-oriented）**的物料流对象，与点导向对象（如 Source、Station）不同，它在仿真中实际使用输入的 **Length（长度）** 参与计算。其核心行为：

- 以恒定速度沿整个长度输送 MU。
- MU 不能超越其前方移动中的 MU。
- 未设置 Exit Control 时，将 MU 均等分配到所有连接的后继对象。
- **Accumulating（累积）** 决定：当前方 MU 无法离开时，后续 MU 是前移并首尾相接，还是保持相互间距。

## 查看属性与方法

Conveyor 提供以下属性（此外还包括「所有对象的属性」与「物料流对象的属性」）：

- 在类库（Class Library）上下文菜单选择 **Show Attributes and Methods**，可查看所选 **类（Class）** 的成员。
- 按 **F8** 或点击 Frame 的 Home 功能区中的 **Show Attributes and Methods**，可查看所选 **实例（Instance）** 的成员。

可通过对话框控件或 SimTalk 赋值来设置/获取属性值：

```simtalk
-- 设置
MyConveyor.AccelerationEnabled := false

-- 获取
print MyConveyor.AccelerationEnabled
posit := MyStation.Cont.XPos
```

## 语法行约定（Syntax Line Conventions）

方法/属性的语法行示例如下：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：属性所作用对象的路径。
- 括号内为签名，含参数标识符与数据类型，例如 `(Parameter:string)`。
- 方括号 `[…]` 表示可选参数。
- `:= 默认值` 表示参数的默认值。
- 箭头 `→` 后为返回值的数据类型。

> 注意：表达式内的括号 `(…)` 必须输入，否则可能导致意外结果并打开调试器（Debugger）。

## 属性列表

### OccupiedLength（只读）

返回 Conveyor 整个长度（Length）中被其上所有 MU 占用的区段长度。

- **类型**：只读属性
- **语法**：`<Path>.OccupiedLength → length`
- **返回值**：数据类型 `length`

### Acceleration

设置 Conveyor 增加速度所用的加速度（m/s²）。

- **备注**：仅在启用 Acceleration/AccelerationEnabled 后可设置；Conveyor 会一直加速到达到最终 Speed，无论其上是否有 MU。
- **语法**：`<Path>.Acceleration:acceleration`
- **可监视**：是
- **赋值**：数据类型 `acceleration`，任意 ≥ 0 的实数。SimTalk 2.0 支持直接写单位（`mps²`、`cm²`、`fps²`、`LU/s²`），如 `10mps2`。

### AccelerationEnabled

启用（`true`）或禁用（`false`）Conveyor 的加速。

- **语法**：`<Path>.AccelerationEnabled:boolean`
- **赋值**：数据类型 `boolean`

### Accumulating

设置当前方 MU 无法离开时，后续 MU 是否前移（`true`），还是保持相互间距（`false`）。

- **备注**：累积激活时，后续 MU 的前端触及前一 MU 的末端。
- **语法**：`<Path>.Accumulating:boolean`
- **可监视**：是

### AutomaticStop

不输送 MU 时自动停止 Conveyor，将当前速度置 0。

- **备注**：可能发生在空载或被阻塞时；速度立即置 0（不经减速），并立即恢复到目标速度（不经加速）。速度为 0 时能量状态变为 operational。
- **语法**：`<Path>.AutomaticStop:boolean`

### Backwards

设置 Conveyor 及其上的 MU 是否反向运行（`true`）或正向运行（`false`）。

- **备注**：反向时 MU 从出口进入、从入口离开。无加速时方向立即反转；有加速时先减速到 0、反转、再加速到最终速度。若为 Transporter 设置了 Target Distance，则无法更改 `Backwards`。
- **语法**：`<Path>.Backwards:boolean`

### Capacity

设置同一时刻可全部或部分位于 Conveyor 上的 MU 或 MU 部件数量上限。

- **备注**：达到上限后不再接收 MU，即使全长未耗尽。
- **语法**：`<Path>.Capacity:integer`
- **可监视**：是
- **赋值**：数据类型 `integer`，`-1` 表示无限容量。

### CurrentSpeed

设置 Conveyor 的当前速度（正向为正，反向为负）。

- **备注**：仅在启用 Acceleration/AccelerationEnabled 后可设置；返回值为 `inf` 表示指定了 `-1`（无限速度）。
- **语法**：`<Path>.CurrentSpeed:speed`
- **可监视**：是（特殊值，如检测达到最终速度）

### Deceleration

设置 Conveyor 降低速度所用的减速度。

- **备注**：任意 ≥ 0 的实数；仅在启用 Acceleration/AccelerationEnabled 后可设置。
- **语法**：`<Path>.Deceleration:acceleration`
- **可监视**：是

### EnforceMUDistance

使 Conveyor 即使在累积时也保持指定的 MU 间距（`true`），或反之（`false`）。

- **备注**：仅在 Conveyor 为累积（Accumulating）且正向输送时生效；间距可能因 MU Distance Type 及后继 Conveyor 的速度而增大。
- **语法**：`<Path>.EnforceMUDistance:boolean`

### Length

设置 Conveyor 的长度。

- **备注**：Length 与 Speed 共同决定对象上的处理时间。
- **语法**：`<Path>.Length:length`
- **可监视**：是
- **赋值**：数据类型 `length`。SimTalk 2.0 支持直接写单位（`m`、`mm`、`km`、`cm`、`yd`、`ft`、`in`），如 `10m`。

### MUDistance

设置 Conveyor 在下一 MU 进入时所强制执行的、当前 MU 与后续 MU 之间的期望距离。

- **备注**：根据 MU Distance Type，距离决定 Gap（前一 MU 末端到后一 MU 前端）或 Pitch（前一 MU 前端到后一 MU 前端）。无后续 MU 到达时 Conveyor 停止，新 MU 到达后重新启动。默认 `-1` 表示不使用 MU 间距。
- **语法**：`<Path>.MUDistance:integer`
- **赋值**：数据类型 `integer`

### MUDistanceType

设置 Conveyor 的 MU 间距类型。

- **语法**：`<Path>.MUDistanceType:string`
- **赋值**：数据类型 `string`，允许值：`"Gap"`、`"Pitch"`、`"Minimum Gap"`、`"Minimum Pitch"`、`"Multiple Gap"`、`"Multiple Pitch"`。
  - **Gap** — 前一 MU 末端到后一 MU 前端的距离。
  - **Pitch** — 前一 MU 前端到后一 MU 前端的距离。
  - **Minimum Gap** / **Minimum Pitch** — 最小距离，使 Conveyor 不必停止等待。
  - **Multiple Gap** / **Multiple Pitch** — 距离可为定义值的整数倍，Conveyor 不停止等待新 MU（后者类似链式输送机）。

### Speed

设置 Conveyor 输送 MU 的速度。

- **备注**：Speed 与 Length 共同决定处理时间（Length ÷ Speed）；输入 `-1` 表示无限速度。更改 Speed 会重算 MU 的所有速度相关事件。
- **语法**：`<Path>.SpeedCtrl:speed`
- **可监视**：是

### SpeedCtrl

指定对象的一个 Method 对象。

- **备注**：Conveyor（或 Transporter 的装载区）在加速/减速后达到最终速度、或减速后停止时调用该方法；速度瞬时改变时不调用。未输入 Method 时属性为 `VOID`。仅在启用 Acceleration/AccelerationEnabled 后可设置。
- **语法**：`<Path>.SpeedCtrl:method`

### Time

设置 MU 在 Conveyor 上移动所花费的时间。

- **备注**：Time 除以 Length 得到 Speed。
- **语法**：`<Path>.Time:time`

## 属性快速对照表

| 属性 | 类型 | 语法 | 可监视 |
|------|------|------|--------|
| OccupiedLength | 只读 | `<Path>.OccupiedLength → length` | — |
| Acceleration | 属性 | `<Path>.Acceleration:acceleration` | 是 |
| AccelerationEnabled | 属性 | `<Path>.AccelerationEnabled:boolean` | — |
| Accumulating | 属性 | `<Path>.Accumulating:boolean` | 是 |
| AutomaticStop | 属性 | `<Path>.AutomaticStop:boolean` | — |
| Backwards | 属性 | `<Path>.Backwards:boolean` | — |
| Capacity | 属性 | `<Path>.Capacity:integer` | 是 |
| CurrentSpeed | 属性 | `<Path>.CurrentSpeed:speed` | 是（特殊值） |
| Deceleration | 属性 | `<Path>.Deceleration:acceleration` | 是 |
| EnforceMUDistance | 属性 | `<Path>.EnforceMUDistance:boolean` | — |
| Length | 属性 | `<Path>.Length:length` | 是 |
| MUDistance | 属性 | `<Path>.MUDistance:integer` | — |
| MUDistanceType | 属性 | `<Path>.MUDistanceType:string` | — |
| Speed | 属性 | `<Path>.SpeedCtrl:speed` | 是 |
| SpeedCtrl | 属性 | `<Path>.SpeedCtrl:method` | — |
| Time | 属性 | `<Path>.Time:time` | — |

## 相关文档（同层级 SimTalk 参考）

- [General（概述）](../general/README.md) — Conveyor 概念、工作原理、对话框及各选项卡设置；含 Attributes 选项卡中每个属性对应的 SimTalk 名称。
- [Methods（方法）](../methods/README.md) — 方法概述及语法行约定。
- [Read-Only Attributes（只读属性）](../read-only-attributes/README.md) — `CurrentAcceleration`、`OccupiedLength` 等只读属性。

Conveyor 提供三组方法/属性：

- 曲线对象（Curved Objects）的方法/属性；
- 物料流对象（Material Flow Objects）的方法/属性/只读属性；
- 所有对象（All Objects）的方法/属性/只读属性。
