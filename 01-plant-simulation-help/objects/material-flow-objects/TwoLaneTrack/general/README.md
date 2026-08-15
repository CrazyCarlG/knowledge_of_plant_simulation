# TwoLaneTrack（双车道轨道）— 文档总结

本 README 汇总 `TwoLaneTrack` 对象的知识库内容，来源包括：

- `general/general.md` — 对象概述、对话框、路由机制
- `attributes/attributes.md` — 属性参考
- `methods/methods.md` — 方法参考
- `read-only-attributes/read-only-attributes.md` — 只读属性参考

---

## 1. 概述（General）

`TwoLaneTrack` 与 `Transporter`（运输小车）一起，可用于构建 **AGV（自动导引车）系统**。

核心特性：

- 小车在轨道上行驶的距离由 **Lane A / Lane B 的长度**、小车的 **MU Length** 及其 **Speed** 决定，从而确定小车在轨道上的停留时间。
- 与面向点（point-oriented）的物流对象不同，仿真运行时实际使用键入的长度。
- 小车**不能超越**前方小车，保持其驶入与驶出轨道的顺序。
- 每条车道可拥有各自长度，因此转弯时外侧车道可以比内侧车道更长。
- 若多辆小车速度不同，较快者会与较慢者"碰撞"，Plant Simulation 会激活较快小车的 **Collision Control** 并自动将其速度降至与较慢者一致。
- 小车可在轨道上**前进与后退**（从出口驶入、从入口驶出）。前进/后退是小车的属性，而非轨道的属性。
- 最大容量由轨道长度及车上所有小车的长度决定（例如 3 码轨道最多容纳 3 辆 1 码小车）。**Capacity** 设置可进一步限制小车数量。
- 轨道可作为**弯曲对象**插入（默认），或由任意弯曲/直线段组合而成。
- 支持**双向交通**：可选 **Right-hand Traffic（右行）** 或 **Left-hand Traffic（左行）**。

### 插入对象

点击 Home 功能区：**Library > Basic Objects > MaterialFlow > TwoLaneTrack**。

### 图形操作（Show Manipulators）

在 Edit 功能区点击 **Show Manipulators** 或按 **M**，可修改图形长度与锚点。

---

## 2. 路由（Routing）

在分叉轨道上，按以下**优先级顺序**决定小车的去向：

1. **Exit Control**（出口控制，最高优先级）
2. **Automatic Routing**（自动路由）
3. **Driving Control**（行驶控制）
4. 轨道内建属性

要点：

- 若未定义 Exit Control 且为小车键入了目标列表（destination list），则 Automatic Routing 利用后继对象的目标列表将小车导向正确的后继。
- 可为小车指定 **Destination**。轨道每条车道分别有 **Forward destination list** 与 **Backward destination list**。
- 若既无 Exit Control 也无目标列表，则使用小车的 **Driving Control**。
- 若完全未定义任何控制，轨道将小车依次轮流送入每个相连的后继。

---

## 3. 对话框（Dialog Box）

双击图标打开对话框：

- **Edit Simulation Properties**：修改仿真属性。
- **Edit Animation Properties**：点击左下角 **Edit 3D Properties**，或选中对象后按空格键。

主要选项卡：

- **Tab Attributes**：Lane A / Lane B 的长度（Length）、入口锁定（Entrance Locked）、出口锁定（Exit Locked），以及 Width、Track Pitch、Traffic、Capacity、Destination List A/B。
- **Tab Failures**：定义故障。
- **Tab Controls A/B**：可创建 Entrance Control、Exit Control、Backward Entrance Control、Backward Exit Control、Pull Control，以及 Shift Calendar 和 Sensors。
- **Tab Statistics / User-defined**：统计与自定义属性。
- **Navigate / View / Tools / Tabs / Help 菜单**：各类辅助命令。

---

## 4. 属性（Attributes）

属性参考见 `attributes.md`，主要包括：

| 属性 | 作用域 | 说明 |
| --- | --- | --- |
| `Length` | lane A / B | 指定车道的物理长度 |
| `EntranceLocked` | lane A / B | 锁定入口，阻止小车进入；阻塞的小车进入 Forward Blocking List |
| `ExitLocked` | lane A / B | 锁定出口，阻止小车离开；小车进入 Exit Blocking List |
| `EntranceCtrl` | lane A / B | 入口控制方法 |
| `EntranceCtrlFront` / `EntranceCtrlRear` | lane A / B | 小车前端/后端进入时触发入口控制 |
| `ExitCtrl` | lane A / B | 出口控制方法 |
| `ExitCtrlFront` / `ExitCtrlRear` | lane A / B | 小车前端/后端离开时触发出口控制 |
| `BwEntranceCtrl` | lane A / B | 反向入口控制方法（经出口驶入） |
| `BwEntranceCtrlFront` / `BwEntranceCtrlRear` | lane A / B | 反向入口控制的前/后端触发 |
| `BwExitCtrl` | lane A / B | 反向出口控制方法（经入口驶出） |
| `BwExitCtrlFront` / `BwExitCtrlRear` | lane A / B | 反向出口控制的前/后端触发 |
| `PullCtrl` | lane A / B | 拉取控制方法（仅适用于正向行驶的小车） |
| `Capacity` | TwoLaneTrack | 两车道上同时可容纳的最大小车数（`-1` 为无限） |
| `DestListA` / `DestListB` | TwoLaneTrack | 正向目标列表（A 的正向列表同时是 B 的反向列表，反之亦然） |
| `TrackPitch` | TwoLaneTrack | 两车道中心线之间的距离 |
| `Traffic` | TwoLaneTrack | `"Right-hand traffic"` 或 `"Left-hand traffic"` |
| `Width` | TwoLaneTrack | 双车道的宽度 |

通用要点：

- 设置/获取属性值可用对话框控件或直接赋值，例如 `MyTwoLaneTrack.B.Length := 44`、`print MyTwoLaneTrack.B.Length`。
- 该对象还继承所有对象的属性、物流对象的属性。多个共享属性作用于**单条车道**而非整个对象，对话框以 `A`/`B` 区分。

---

## 5. 方法（Methods）

方法参考见 `methods.md`，主要包括：

| 方法 | 作用域 | 说明 |
| --- | --- | --- |
| `bwBlockList` | lane A / B | 返回指定车道的反向阻塞列表 |
| `contentsList` | lane A / B | 返回指定车道上所有小车的内容列表（对象、起止位置） |
| `exitBlockList` | lane A / B | 返回指定车道的出口阻塞列表 |
| `fwBlockList` | lane A / B | 返回指定车道的正向阻塞列表 |
| `getRouteLength` | lane A / B | 返回从指定车道到目标的最短路径长度（`-1` 表示未找到路径） |
| `pred` | lane A / B | 返回指定车道的直接前驱对象 |
| `predConnector` | lane A / B | 返回连接到指定车道的入站 Connector |
| `predLane` | lane A / B | 返回指定车道的前驱车道 |
| `predLaneNo` | lane A / B | 返回前驱车道的编号 |
| `succ` | lane A / B | 返回指定车道的直接后继对象 |
| `succConnector` | lane A / B | 返回连接到指定车道的出站 Connector |
| `succLane` | lane A / B | 返回指定车道的后继车道 |
| `succLaneNo` | lane A / B | 返回后继车道的编号 |

通用要点：

- 语法示例：`<Path>.A.exitBlockList([ExitBlockingList:table]) -> object[]`。
- `<Path>` 为对象路径；`A`/`B` 指定要访问的车道。
- 该对象还继承弯曲对象、物流对象、所有对象的方法。多个共享方法作用于**单条车道**而非整个对象。

---

## 6. 只读属性（Read-Only Attributes）

只读属性参考见 `read-only-attributes.md`，主要包括：

| 只读属性 | 作用域 | 说明 |
| --- | --- | --- |
| `IsLaneA` | lane A | 小车是否行驶在 A 车道（boolean） |
| `IsLaneB` | lane B | 小车是否行驶在 B 车道（boolean） |
| `NumPred` | lane A / B | 指定车道的前驱数量（integer） |
| `NumSucc` | lane A / B | 指定车道的后继数量（integer） |
| `OccupiedLength` | lane A / B | 指定车道上被所有小车占用的长度（length） |
| `succLaneNo` | lane A / B | 指定车道的后继车道编号（integer） |

通用要点：

- 只读属性只能查询、不能赋值，值由 Plant Simulation 在查询时点即时计算。
- 查询示例：`print TwoLaneTrack.A.NumPred`。

---

## 7. 查看全部成员

要查看对象的所有方法、只读属性与属性，打开 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 查看所选类。
- 按 **F8** 或点击 Frame 的 Home 功能区 **Show Attributes and Methods** 查看实例。

对于 TwoLaneTrack，对话框以 `A`/`B` 显示对应车道，但不会单独列出各车道专属的成员。

---

## 参见（See also）

- Model a Transport System with Passive Objects
- Work with Length-oriented Objects
- Routing [TwoLaneTrack]
- Define Controls for Length-Oriented Objects
- Forward Blocking List / Backward Blocking List / Exit Blocking List
- Shift Calendar [tab Controls]
- Resource Statistics / Resource Type
