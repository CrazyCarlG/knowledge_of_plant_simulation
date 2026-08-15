# TwoLaneTrack 属性（Attributes）— 文档总结

本目录汇总了 **TwoLaneTrack（双车道轨道）** 对象的 Attributes（属性）文档，源文件为 `attributes.md`（另含 `attributes.txtx` 原始文本与 `Plant-Simulation-Help2606_5459-5487.pdf` 帮助原文）。

## 目录内容

- `attributes.md` — TwoLaneTrack 属性的 Markdown 说明文档（本总结的主要依据）
- `attributes.txtx` — 帮助原文的文本版（与 `attributes.md` 内容一致）
- `Plant-Simulation-Help2606_5459-5487.pdf` — Siemens Plant Simulation 帮助原文 PDF

## 概述

TwoLaneTrack 提供以下属性来源：

- 本页列出的专属属性
- All Objects（所有对象）的属性
- Material Flow Objects（物流对象）的属性

> **注意：** TwoLaneTrack 与其他物流对象共享的部分属性，作用于单个**车道（lane）** 而非整个对象。对话框用 `A` 和 `B` 表示对应车道，但不会单独列出各车道专属的属性。

设置 / 获取属性值的方式：既可用对话框中的复选框、文本框与下拉列表，也可直接为对应属性赋值。

```simtalk
-- 设置属性值
MyTwoLaneTrack.B.Length := 44

-- 获取属性值
print MyTwoLaneTrack.B.Length
posit := MyStation.Cont.XPos
```

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口。

### 语法约定

- `<Path>` — 属性所应用对象的路径
- `A` / `B` — 要访问的 TwoLaneTrack 车道
- 冒号 `:` 后为属性的赋值 / 返回数据类型（如 `method`、`boolean`、`integer`、`length`、`string`、`object`）

## 属性清单

| 属性 | 作用域 | 类型 | 说明 |
| --- | --- | --- | --- |
| `Length` | lane A / B | 属性 | 指定车道的物理长度；小车在位置 0 进入，驶过该长度后离开 |
| `EntranceLocked` | lane A / B | 属性 | 锁定入口，阻止 Transporter 进入；被阻塞的小车进入 Forward / Exit Blocking List |
| `ExitLocked` | lane A / B | 属性 | 锁定出口，阻止 Transporter 离开；小车进入 Exit Blocking List |
| `EntranceCtrl` | lane A / B | 属性 | 入口控制方法（Transporter 进入指定车道时调用） |
| `EntranceCtrlFront` | lane A / B | 属性 | 小车**前端**进入时触发入口控制（`true` / `false`） |
| `EntranceCtrlRear` | lane A / B | 属性 | 小车**后端**进入时触发入口控制（`true` / `false`） |
| `ExitCtrl` | lane A / B | 属性 | 出口控制方法（Transporter 离开指定车道时调用） |
| `ExitCtrlFront` | lane A / B | 属性 | 小车**前端**离开时触发出口控制（`true` / `false`） |
| `ExitCtrlRear` | lane A / B | 属性 | 小车**后端**离开时触发出口控制（`true` / `false`） |
| `BwEntranceCtrl` | lane A / B | 属性 | 反向入口控制方法（Transporter 经出口驶入、或驶入后朝入口方向移动时调用） |
| `BwEntranceCtrlFront` | lane A / B | 属性 | 反向入口控制的**前端**触发（`true` / `false`） |
| `BwEntranceCtrlRear` | lane A / B | 属性 | 反向入口控制的**后端**触发（`true` / `false`） |
| `BwExitCtrl` | lane A / B | 属性 | 反向出口控制方法（Transporter 经入口驶出、或驶出时朝入口方向移动时调用） |
| `BwExitCtrlFront` | lane A / B | 属性 | 反向出口控制的**前端**触发（`true` / `false`） |
| `BwExitCtrlRear` | lane A / B | 属性 | 反向出口控制的**后端**触发（`true` / `false`） |
| `PullCtrl` | lane A / B | 属性 | 拉取控制方法（仅适用于正向行驶的 Transporter；可配合 `fwBlockList` / `unblock` 选择接受的小车） |
| `Capacity` | TwoLaneTrack | 属性 | 两车道上同时可容纳的最大 Transporter 数（`-1` 为无限） |
| `DestListA` | TwoLaneTrack | 属性 | A 车道正向行驶的目标列表（同时是 B 车道的反向目标列表） |
| `DestListB` | TwoLaneTrack | 属性 | B 车道正向行驶的目标列表（同时是 A 车道的反向目标列表） |
| `TrackPitch` | TwoLaneTrack | 属性 | 两车道中心线之间的距离 |
| `Traffic` | TwoLaneTrack | 属性 | 双向交通行驶方向：`"Right-hand traffic"` 或 `"Left-hand traffic"` |
| `Width` | TwoLaneTrack | 属性 | 双车道的宽度 |
| `OccupiedLength` | lane A / B | 只读属性 | 返回指定车道上被所有 Transporter 占用的总长度 |

## 补充说明

- 标记为 **Watchable（可监控）** 的属性：`Capacity`、`EntranceLocked`、`ExitLocked`、`Length`、`Width`。
- 反向控制（`Bw*`）用于小车**后退**行驶的场景：从出口驶入、从入口驶出。
- `PullCtrl` 不决定小车驶向哪个后继，而是从已决定驶向该后继的小车中选择其一；对 TwoLaneTrack 而言仅对正向行驶的小车生效。
- 长度单位：在 SimTalk 2.0 中可为 `m`、`mm`、`km`、`cm`、`yd`、`ft`、`in`，例如 `10m`、`10.2m`。
- `OccupiedLength` 虽收录于 `attributes.md`，但为只读属性；其详细说明见同级目录 `read-only-attributes/`。

## 相关文档

- TwoLaneTrack 的方法（Methods of the TwoLaneTrack）— 见同级目录 `methods/`
- TwoLaneTrack 的只读属性（Read-Only Attributes of the TwoLaneTrack）— 见同级目录 `read-only-attributes/`
- TwoLaneTrack 概述与路由机制 — 见同级目录 `general/`
- 所有对象的属性（Attributes of All Objects）
- 物流对象的属性（Attributes of the Material Flow Objects）
