# TwoLaneTrack 方法（Methods）— 文档总结

本目录汇总了 **TwoLaneTrack（双车道轨道）** 对象的 Methods（方法）文档，源文件为 `methods.md`（另含 `methods.txtx` 原始文本与 `Plant-Simulation-Help2606_5431-5452.pdf` 帮助原文）。

## 目录内容

- `methods.md` — TwoLaneTrack 方法的 Markdown 说明文档（本总结的主要依据）
- `methods.txtx` — 帮助原文的文本版（与 `methods.md` 内容一致）
- `Plant-Simulation-Help2606_5431-5452.pdf` — Siemens Plant Simulation 帮助原文 PDF

## 概述

TwoLaneTrack 提供以下方法/属性来源：

- 本页列出的专属方法
- Curved Objects 的方法
- Material Flow Objects（物流对象）的方法
- All Objects（所有对象）的方法

> **注意：** TwoLaneTrack 与其他物流对象共享的部分方法，作用于单个**车道（lane）** 而非整个对象。

文档还说明了查看全部方法、只读属性和属性的方式：打开 **Show Attributes and Methods** 对话框（类库上下文菜单，或按 F8 / Home 选项卡按钮）。对于 TwoLaneTrack，该对话框会用 `A` 和 `B` 表示对应车道。

### 语法约定

- `<Path>` — 方法所应用对象的路径
- `A` / `B` — 要访问的 TwoLaneTrack 车道
- 圆括号内为签名（标识符 + 参数数据类型）；可选参数用 `[...]` 表示；有默认值时在参数后给出默认值；有返回值时在箭头 `->` 后给出数据类型
- 括号内表达式的括号不可省略，否则可能产生意外结果并打开调试器

## 方法清单

以下方法均适用于 **车道 A 或 B**（`<Path>.A.<方法>` 或 `<Path>.B.<方法>`）。

| 方法 | 返回值 | 说明 |
|------|--------|------|
| `bwBlockList` | `any` | 返回指定车道**后向（backward）阻塞列表**（可选参数：`BackwardBlockingList` 表，两列：对象 + 尝试进入时间） |
| `contentsList` | `any` | 返回指定车道上**全部内容（Contents）**，即该车道 Contents List 中的所有 Transporters（可选表，三列：对象、起点位置、终点位置） |
| `exitBlockList` | `object[]` | 返回指定车道的**出口阻塞列表（Exit Blocking List）**（可选参数：`ExitBlockingList` 表，两列） |
| `fwBlockList` | `any` | 返回指定车道**前向（forward）阻塞列表**（可选参数：`ForwardBlockingList` 表，两列） |
| `getRouteLength` | `length` | 返回从该车道到目标的最短路线长度（参数：`Target`；可选 `Backwards`、`Position`、`ObjectsAlongRoute`、`RouteWeightingAttribute`；无路线返回 `-1`；仅考虑 Track/TwoLaneTrack） |
| `pred` | `object` | 返回指定车道的**直接前驱**（可选 `PredecessorNumber`，默认 1） |
| `predConnector` | `object` | 返回直接连接到该车道的**入向连接器**（可选 `PredecessorNumber`；无连接返回 `VOID`） |
| `predLane` | `any` | 返回指定车道的**直接前驱车道**（可选 `Predecessor`） |
| `predLaneNo` | `integer` | 返回指定车道的**前驱车道编号**（可选 `Predecessor`；仅对象已连接时有效） |
| `succ` | `object` | 返回指定车道的**直接后继**（可选 `SuccessorNumber`，默认 1；遇到 Interface/Frame 时会追踪其后续对象） |
| `succConnector` | `object` | 返回直接连接到该车道的**出向连接器**（可选 `SuccessorNumber`；无连接返回 `VOID`） |
| `succLane` | `any` | 返回指定车道的**直接后继车道**（可选 `Successor`） |
| `succLaneNo` | `integer` | 返回指定车道的**后继车道编号**（可选 `LaneNumber`） |

## 只读属性（Read-Only Attributes）

`methods.md` 末尾说明 TwoLaneTrack 还提供：

- 目录表中列出的只读属性
- All Objects 的只读属性
- Material Flow Objects 的只读属性

（只读属性的详细内容见同级目录 `read-only-attributes/`。）
