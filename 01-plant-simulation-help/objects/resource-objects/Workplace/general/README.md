# Workplace — General（工作场所 — 通用说明）

本目录汇总 Plant Simulation 资源对象 **Workplace（工作场所）** 的通用文档，内容来源于 `general.md`（以及原始提取文本 `general.txtx`、源 PDF `Plant-Simulation-Help2606_5902-5945.pdf`）。本目录下暂无子文件夹及其子 README.md。

## 概述

`Workplace` 对象用于建模工作站在工人（Worker）实际执行作业的位置。它是 **资源对象（Resource Objects）** 之一。

Plant Simulation 资源对象包括：

- **Exporter** —— 提供/导出服务；代表一群无法区分、无法单独寻址的人员。
- **FootPath** —— 建模 Worker 从 WorkerPool 走到 Workplace 的路径。
- **LockoutZone** —— 控制一组物料流对象；其中一个故障时，其余全部停止处理零件。
- **Marker** —— 设置 AGV 从 AGVPool 驶向目的地途中的里程碑。
- **ShiftCalendar** —— 建模轮班工作制度。
- **Worker** —— 在工位的 Workplace 上作业（不出现在 Resources 工具栏，需在 Class Library 中访问其类）。
- **WorkerPool** —— 建模工厂的工人休息室。
- **Workplace** —— 建模附加在工位上、Worker 实际作业的位置。

> 不要把资源对象与 **物料流资源（material flow resources）**（即内置的 Material Flow Objects、Fluid Objects 或用于建模机器的 Frame）混淆。

## 描述

Worker–WorkerPool–Workplace–FootPath 概念是对 Broker–Importer–Exporter 概念的细化。

- 可将 Workplace 分配给支持 **Importer** 的物料流对象（处理类或维修类 importer）。
- 对于**运输类 importer**（控制 Worker 如何搬运零件），还可将 Workplace 分配给 Buffer、PlaceBuffer、Source、Sorter 和 Store。

要点：

- 可以（但不必须）给工位分配 Workplace。不使用 FootPath 时，Worker 被直接运送到 Workplace（此时 Worker 相当于容量为 1 的 Exporter）。
- Worker 在 WorkerPool 中创建，空闲时留在那里。
- **Broker** 为各个工位调配 Worker。
- Worker 自由行走时沿最短路线并耗时。
- 若 WorkerPool 与 Workplace 之间用 FootPath 连接，Worker 移动与作业过程都会被动画显示，走 FootPath 耗时。
- 启用 **Beam to workplace** 且 Worker 无法经 FootPath 到达 Workplace 时，Plant Simulation 直接将其传送到 Workplace。
- 启用 **Workers can work remotely**，或未插入 Workplace / 没有支持该服务的 Workplace / 所有支持该服务的 Workplace 均被占用时，Worker 在工位作业，但仍在 WorkerPool 中保持动画。

队列图例（图形箭头含义）：

- Part Carried by Worker with Route
- Part Carried by Worker Destination
- Workplace Assigned to Station
- Workplace Reserved for Worker（实心箭头）
- Workplace Reserved for Worker on his Way（空心箭头）

修改图形长度与锚点：在 Edit 功能区点击 **Show Manipulators**，或按 **M** 键。

### 添加对象到模型

Home 功能区点击 **Manage Class Library > Basic Objects > Resources > Workplace**。

## Worker 如何在 Workplace 前排队

无法踏上 Workplace 的 Worker 会在其前面排队等候（无需额外 FootPath）。

- 等待位置取决于 Worker 在 **Forward Blocking List** 中的位置以及 **Distance in Queue**。
- 新模型中队列显示在名为 `Queue` 的 **MU Animation Path** 上；若队列超出预定义路径，会向队尾延伸。
- 若希望 Worker 走到 MU Animation Path 的末端而非 Workplace，选择 **Walk Along the Animation Path of the Queue**。
- 动画路径末端应与 Workplace 处于同一高度（Z 坐标），否则可能无法计算路线。
- 若 Worker 到达被占用的 Workplace/等待位置，Plant Simulation 直接将其移到正确的等待位置。
- 直接走向 Workplace 时到达等待位置不耗时；队列内前移由 Worker 动画完成。

## Workplace 对话框

双击 Workplace 图标打开对话框。

- **Edit Simulation Properties** —— 共享属性见 "Dialog Items of the Objects"。
- **Edit 3D Properties** —— 点击 **Edit 3D Properties** 按钮，或选中对象后按空格键。操作图形点击 **Show Manipulators** 或按 **M**。

### Tab Attributes（属性页）

| 设置 | 说明 | SimTalk |
| --- | --- | --- |
| **Station [Workplace]** | 分配给 Workplace 的工位，须为支持 importer 的物料流对象（如 Source、Drain、Station、ParallelStation、AssemblyStation、DismantleStation、Conveyor）。点击省略号按钮在 Select Object 中选择；或将 Workplace 拖到对象某侧自动录入。已分配/未分配的图标不同。F2 打开文本框中的对象。 | `Station` |
| **At Entrance** | 将 Workplace 附加到 Conveyor 的入口。位置导向对象默认同时勾选 At Entrance 与 At Exit。可拖放设置（提示 `Conveyor @ Entrance`）。通过 SimTalk 分配新工位不改变当前入口/出口分配。 | `AtEntrance` |
| **At Exit** | 将 Workplace 附加到 Conveyor 的出口（提示 `Conveyor @ Exit`）。 | `AtExit` |
| **Capacity** | Workplace 可同时容纳 Worker 的最大数量。Worker 先走到 Workplace 坐标再跳到动画点；Worker 分布显示在 Animation Area 上。仅当 Workplace 为空时才能修改。Recovery Time 只能为容量 1 的 Workplace 定义。 | `Capacity` |
| **Supported Services** | 打开 Workplace 支持的服务列表。输入前先点击 **Inheritance** 复选框，再输入表达式（如 `drilling`、`milling`、`turning`）并 Apply。名称**不区分大小写**，SimTalk 中用 `~=` 比较。若列表为空，Worker 可在此执行任意服务。 | `SupportedServices` |
| **Worker Stays Here After Completing the Job** | 勾选后 Worker 完成任务后留在 Workplace；清除则返回 WorkerPool 或 Home Location。若 WorkerPool 启用了 **Get Job Orders At Home Only** 则必须清除。未被自动调配的 Worker 始终留在 Workplace。容量用尽时，不工作的 Worker 会被挤开并离开。 | `WorkerStaysHere` |
| **Distance in Queue** | 队列动画路径上 Worker 之间的间距。 | `DistanceInQueue` |
| **Walk to the End of the Animation Path of the Queue** | Worker 先走到动画路径末端，再前往目的地。 | `WalkToQueuePathEnd` |
| **Walk Along the Animation Path of the Queue** | Worker 到达 MU Animation Path 后沿其走到等待位置或 Workplace。仅在同时选中 Walk to the End 时生效。沿路径行走不考虑障碍物。 | `WalkAlongQueuePath` |
| **Pick/Drop at Store** | 设置 Worker 在 Store 附加的 Workplace 上取/放零件的行为（仅当 Station 为 Store 时显示）。选项见下文。 | `PickDropAtStore` |

**Pick/Drop at Store** 三个选项：

- **Walk to Workplace**（默认）—— Worker 走到 Workplace 取/放零件；所有 Workplace 设置可用。仅此设置支持 `getRouteLength` 与 `getRouteCoordinates` 路线计算（其余设置分别返回 `-1` 与空数组）。
- **Walk to Store Column** —— Worker 无限制地走到货架列。不可用：Capacity（视为无限）、Worker Stays Here、Distance in Queue、Walk to the End / Walk Along。位置由 Store 侧面尺寸、列数及 Workplace 中心点到 Store 的距离决定。大型多列 Store 会增加路线计算复杂度并影响性能。
- **Walk Along Store to Store Column** —— Worker 先走到第一/最后一列，再沿 Store 延伸到目标列。路线受限，各列仅可从相邻列到达（首尾列无限制），延伸时忽略障碍物。不可用功能同上，性能影响较小。

### Tab Times（时间页）

定义时间分布（可用 `setTypeAndAttr` 设置分布类型与参数，可选分布或常量 `Const`）：

- **Loading Time [Workplace]** —— Worker 在工位拾取单个零件的时间。拾取期间零件记在 Worker 名下，处理工位锁定至时间结束；Loading 期间 Workplace 入口关闭。Worker 中断时 Loading Time 随故障时间延长（工位保持锁定）；Worker 暂停或换班结束则取消并按已完全流逝处理。处理工位的故障/停止/暂停/非计划不影响装载。Formula 分布中 `@` 访问零件、`?` 指向 Workplace、`?.Cont` 访问 Worker。
- **Unloading Time [Workplace]** —— Worker 将零件放到目标工位的时间，按零件累加。放置期间零件记在 Worker 名下，目标工位锁定至时间结束。Worker 中断时延长（目标保持锁定）；暂停/换班取消。仅在目标工位能接收零件时才开始卸载，否则零件进入 Forward Blocking List。
- **Recovery Time [Workplace]** —— 防止前一 Worker 尚未完全离开时下一 Worker 踏上 Workplace。仅适用于容量 1 的 Workplace，在前一 Worker 离开后开始；若 Workplace 被设为某 Worker 的 Home Location 则不生效。

### Tab Controls（控制页）

通过省略号按钮选择 Method（或 F2 打开、或从 Frame 拖入文本框）。可创建为 Method 类型的用户自定义属性：输入名称并选 **Create Control**（插入 `self.Name`，如 `self.A1Ctrl`），或空框上选 Create Control（插入 `self.OnBuilt_in_name`，如 `self.OnEntrance`）。删除控制需删除用户自定义属性（仅删除名称会保留属性）。

| 控制 | 触发时机 | SimTalk |
| --- | --- | --- |
| **Entrance Control** | Worker 踏上 Workplace 时调用。 | `EntranceCtrl` |
| **Exit Control** | Worker 离开 Workplace 时调用。 | `ExitCtrl` |
| **Load Control** | Worker 踏上 Workplace 时调用；设定零件如何从工位转移到 Worker（Worker 已在 Workplace 上装载零件时也会调用）。附带标准装载控制源码。 | `LoadCtrl` |
| **Unload Control** | Worker 踏上附加到目标工位的 Workplace 时调用；设定如何将携带零件放到工位。附带标准卸载控制源码。 | `UnloadCtrl` |

标准 Load Control（用户自定义属性，`@`: worker、`?`: workplace）：

```simtalk
if @.failed = false and @.pause = false
   var mu:object := ?.station.cont
   while mu /= void and @.full = false
        mu.move(@)
        waituntil mu.~ = @
        mu := ?.station.cont
   end
end
```

标准 Unload Control（用户自定义属性）：

```simtalk
if @.failed = false and @.Pause = false
   var station:object := ?.station
   var mu:object := @.cont
   while mu /= void and station.full = false
        waituntil station.EntranceFree
        mu.move(station)
        waituntil mu.~ = station
        mu := @.cont
   end
end
```

### Tab User-defined（用户自定义页）

定义自定义属性，见 "Tab User-defined" 通用说明。

## 菜单

- **Navigate Menu** —— 见 Navigate Menu 通用说明。
- **View Menu** —— Refresh、Show Statistics Report（Contents 与 Reserved Places）、Show Attributes and Methods（Forward Blocking List）。
  - **Contents [Workplace]** —— 列出 Workplace 上停留的所有 Worker（容量大于 1 时显示名称与编号）。SimTalk：`contentsList`。
- **Tools Menu** —— Edit Controls、Edit Observers。
- **Help Menu** —— 见 Help Menu 通用说明。

## Workplace 的方法

Workplace 提供：

- 目录中列出的方法。
- Methods of All Objects（所有对象的方法）。
- Methods of the Material Flow Objects（物料流对象的方法）。

查看全部方法/属性：打开 **Show Attributes and Methods**（Class Library 上下文菜单、F8 或 Home 功能区）。

## 参见

- Model Workers and the Jobs They Do
- Model a Worker Who Waits in Line
- Worker-WorkerPool-Workplace-FootPath 概念
- Broker-Importer-Exporter 概念
- 视频：
  - https://youtu.be/HiPziA8kxc0
  - https://youtu.be/gU1pqu7sWA8

## 本目录文件清单

- `general.md` —— Workplace 通用说明（Markdown，主文档）。
- `general.txtx` —— 从源 PDF 提取的纯文本（内容与 `general.md` 对应，含页码与页脚信息）。
- `Plant-Simulation-Help2606_5902-5945.pdf` —— 原始帮助文档 PDF（页 5902–5945）。
