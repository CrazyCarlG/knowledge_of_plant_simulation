# Workplace 属性（Attributes）汇总

本目录包含 Workplace（工位）对象属性的说明文档，来源文件为 `attributes.md`。本 README 对该文档内容进行归纳总结。

## 文档概述

`attributes.md` 首先说明了 Workplace 对象的**只读属性（read-only attributes）**与**属性（attributes）**的区别：

- **只读属性**：只能查询值，不能设置。其值由 Plant Simulation 在查询时刻计算得出，通常对应对象标签页（如 Statistics）上不可编辑的对话框项。
- **属性**：既可以读取也可以设置，通过对话框中的复选框、文本框、下拉列表，或通过给对应属性赋值来实现。

文档还介绍了查看属性与方法的方式：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，显示所选类的属性与方法。
- 选中实例后按 **F8** 或点击 Frame 的 Home 标签页上的 **Show Attributes and Methods**。

以及读写示例：

- 查询只读属性：`print MyWorkplace.UUID`
- 设置属性：`MyWorkplace.Station := MyStation`
- 读取属性：`print MyWorkplace.Station`

此外，Workplace 还提供：
- 文档左侧目录中列出的属性
- 所有对象通用的属性（Attributes of All Objects）
- 物料流对象通用的属性（Attributes of the Material Flow Objects）

## 属性清单

`attributes.md` 共记录了以下 18 个属性，每个属性均包含类型（Type）、语法（Syntax）、赋值类型（Assignment Value）、示例及关联主题（See also）。

### 布尔型属性

| 属性 | 语法 | 说明 |
| --- | --- | --- |
| `AtEntrance` | `<Path>.AtEntrance:boolean` | 是否将 Workplace 附着到所分配物料流对象的入口处 |
| `AtExit` | `<Path>.AtExit:boolean` | 是否将 Workplace 附着到所分配物料流对象的出口处 |
| `WalkAlongQueuePath` | `<Path>.WalkAlongQueuePath:boolean` | 是否让 Worker 沿队列动画路径走到队列动画路径末端 |
| `WalkToQueuePathEnd` | `<Path>.WalkToQueuePathEnd:boolean` | 是否让 Worker 走到队列动画路径末端 |
| `WorkerStaysHere` | `<Path>.WorkerStaysHere:boolean` | Worker 完成任务后是否停留在该 Workplace |

> 说明：通过 SimTalk 给 Workplace 重新指定 Station 不会改变其当前入口/出口的附着状态（`AtEntrance` / `AtExit`）。`WalkAlongQueuePath` 仅在同时设置 `WalkToQueuePathEnd` 为 `true` 时才有效。

### 数值/时间型属性

| 属性 | 语法 | 说明 |
| --- | --- | --- |
| `Capacity` | `<Path>.Capacity:integer` | Workplace 上可同时容纳的 Worker 数量（大于 0 的整数） |
| `DistanceInQueue` | `<Path>.DistanceInQueue:length` | 队列动画路径上 Worker 之间的间距 |
| `LoadingTime` | `<Path>.LoadingTime:time` | Worker 在 Workplace 上取件（Loading）所需的时间 |
| `RecoveryTime` | `<Path>.RecoveryTime:time` | 恢复时间，仅当 Capacity 为 1 时可定义 |
| `UnloadingTime` | `<Path>.UnloadingTime:time` | Worker 将零件放置到目标工位所需的时间 |

> 说明：`Capacity` 仅在 Workplace 为空时才能修改。`RecoveryTime` 在 Worker 离开 Workplace 时开始计时，若该 Workplace 被设为 Worker 的 Home Location 则不生效。

### 方法/路径/字符串/数组属性

| 属性 | 语法 | 说明 |
| --- | --- | --- |
| `EntranceCtrl` | `<Path>.EntranceCtrl:method` | Worker 踏上 Workplace 后 Plant Simulation 调用的 Method |
| `ExitCtrl` | `<Path>.ExitCtrl:method` | Worker 离开 Workplace 后调用的 Method |
| `LoadCtrl` | `<Path>.LoadCtrl:method` | 定义零件如何从工位转移到 Workplace 上的 Worker |
| `UnloadCtrl` | `<Path>.UnloadCtrl:method` | 定义 Worker 如何将零件放置到所附着的工位上 |
| `Station` | `<Path>.Station:path` | 分配给 Workplace 的工位（物料流对象）名称 |
| `SupportedServices` | `<Path>.SupportedServices -> string[]` | Workplace 支持的服务列表（字符串数组） |
| `PickDropAtStore` | `<Path>.PickDropAtStore:string` | Worker 在附着于 Store 的 Workplace 取/放件时的行为 |

> 说明：
> - `EntranceCtrl` / `ExitCtrl` / `LoadCtrl` / `UnloadCtrl` 均为指向 Method 对象的属性。文档中提供了 Load/Unload Control 的标准控制逻辑（用户自定义属性）示例代码。
> - `SupportedServices` 的名称不区分大小写；可以用 `~=` 运算符进行不区分大小写的字符串比较。
> - `PickDropAtStore` 可取三个字符串值：
>   - `"Walk to Workplace"`（默认，之前版本的隐式行为）
>   - `"Walk to Store Column"`
>   - `"Walk Along Store to Store Column"`
>
>   后两种设置下不可用：Capacity（视为无限）、Worker Stays Here、Distance in Queue、Walk to the End / Walk Along the Animation Path of the Queue，且会影响路由计算（`getRouteLength` 对非默认设置返回 `-1`，`getRouteCoordinates` 返回空数组）和性能。

### 对象属性

| 属性 | 语法 | 说明 |
| --- | --- | --- |
| `FootPath` | `FootPath [object]` | 用于建模 Worker 从 WorkerPool 走到 Workplace 的路径 |

> 说明：FootPath 用于 Worker-WorkerPool-Workplace-FootPath 概念，细化 Broker-Importer-Exporter 概念。可配合 Connector 连接多个 FootPath 组成网络，Worker 会在该网络中沿最短路径行走。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `attributes.md` | Workplace 对象属性的完整说明文档 |
| `README.md` | 本汇总文件 |

本目录下无子文件夹。
