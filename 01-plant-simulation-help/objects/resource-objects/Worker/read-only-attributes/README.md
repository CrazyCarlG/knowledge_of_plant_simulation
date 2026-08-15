# Worker 只读属性（Read-Only Attributes）— 总结

本目录包含 Worker（工人）对象的只读属性文档。目录下共两个文件：

- `read-only-attributes.md` — 主要参考文档，逐条列出 Worker 的只读属性。
- `read-only-attributes.txtx` — 同内容的纯文本抽取版本，内容与 `.md` 基本一致，另附带少量相邻章节片段（如 `transportPart` / `cancelTransportPart` 的错误说明、`Attributes of the Worker` 章节开头）。

> 本目录下没有子文件夹，因此不存在需要额外合并的子级 `README.md`。

## 概述

Worker 提供以下只读属性来源：

- 本页左侧目录中列出的只读属性（即下文的专属属性列表）。
- **Exporter 的全部只读属性**——因为 Worker 本质上是一个容量为 1 的 Exporter。
- **所有对象通用的只读属性（Read-Only Attributes of All Objects）**。

只读属性的值只能查询、不能设置：Plant Simulation 会在你查询的时间点即时计算该值。多数情况下，只读属性对应对象某个选项卡（例如 Statistics 选项卡）上不可编辑的对话框项。

### 查看属性与方法

可通过对象窗口 “Show Attributes and Methods” 查看该对象的全部方法、只读属性和属性：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选**类**的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例所在 Frame 的 Home 功能区的 **Show Attributes and Methods**，可查看所选**实例**的方法、只读属性和属性。

查询只读属性示例：

```simtalk
print .Resources.Worker:1.StatTraveledDistance
```

## 只读属性清单

Worker 专属的只读属性共 34 个，按功能可分为：状态类属性、在途（En-route）统计、服务统计（计数 Count / 占比 Portion / 时长 Time）以及行走距离统计。

### 状态与基础属性

| 属性 | 返回类型 | 可监视 | 说明 |
| --- | --- | --- | --- |
| `AvailableForMediation` | boolean | 是 | Worker 是否可被派遣（broker）去执行任务。为 `true` 当且仅当 Worker 未故障、未暂停、未搬运零件且未被派遣。 |
| `CurrentSpeed` | speed | 是 | Worker 在 Footpath 上或区域内自由行走的当前速度。故障、停止，或位于 WorkerPool / Workplace 上时返回 `0`。 |
| `HasOrder` | boolean | 是 | Worker 是否有搬运零件的订单、正在搬运零件，或只是提供（出口）服务。 |
| `ResCurrentState` | string | 是 | Worker 当前状态。可能值：`Services Setting-up`、`Services Processing`、`Services Repairing`、`Services Transporting`、`Services En-route to Job`、`Services Waiting`、`Exporter Paused`、`Exporter Unplanned`、`Exporter failed`。若 Exporter 统计关闭则返回 `VOID`。 |

### 在途统计（En-route Statistics）

- `StatServicesEnRouteIdleCount` → integer：Worker 在途但无订单的次数。
- `StatServicesEnRouteIdlePortion` → real：Worker 在途但未被分配工作订单的时间占整体统计时间的比例。
- `StatServicesEnRouteIdleTime` → time：Worker 在途但无工作的总时长。
- `StatServicesEnRouteToJobCount` → integer：Worker 被派遣前往 Workplace 执行任务的次数。
- `StatServicesEnRouteToJobPortion` → real：前往 Workplace 执行任务在途时间占整体统计时间的比例。
- `StatServicesEnRouteToJobTime` → time：前往 Workplace 执行任务在途的总时长。

> 说明：若清除 `Get Job Orders at Home Only` 且清除 Workplace 的 `Worker Stays Here After Completing the Job`，或用 `goTo` 方法把 Worker 派往 Workplace，都会计入 En-route Idle 相关统计；若勾选 `Get Job Orders at Home Only`，Worker 返回 WorkerPool 取下一订单的行走也会计入 En-route to Job 相关统计。

### 服务统计（Service Statistics）

服务统计分为若干类别，每类包含三个属性：计数（Count，integer）、占比（Portion，real）、时长（Time，time）。

| 类别 | Count | Portion | Time | 含义 |
| --- | --- | --- | --- | --- |
| Failed（故障） | `StatServicesFailedCount` | `StatServicesFailedPortion` | `StatServicesFailedTime` | 服务故障的次数 / 比例 / 总时长。 |
| Repairing（维修） | `StatServicesRepairingCount` | `StatServicesRepairingPortion` | `StatServicesRepairingTime` | 服务从事维修的次数 / 比例 / 总时长。 |
| Setup（装夹） | `StatServicesSetupCount` | `StatServicesSetupPortion` | `StatServicesSetupTime` | 服务为工作站装夹（setting up）的次数 / 比例 / 总时长。 |
| Transporting（搬运） | `StatServicesTransportingCount` | `StatServicesTransportingPortion` | `StatServicesTransportingTime` | 在 Workplace 之间搬运零件的次数 / 比例 / 总时长。 |
| Waiting for Importer（等待进口） | `StatServicesWaitingImpCount` | `StatServicesWaitingImpPortion` | `StatServicesWaitingImpTime` | 服务等待 importer 的次数 / 比例 / 总时长（占比按容量加权）。 |
| Waiting for MU（等待 MU） | `StatServicesWaitingMUCount` | `StatServicesWaitingMUPortion` | `StatServicesWaitingMUTime` | 服务在 importer 处等待 MU 的次数 / 比例 / 总时长。 |
| Waiting（总等待） | — | `StatServicesWaitingPortion` | `StatServicesWaitingTime` | 等待的总占比与总时长。 |
| Working（工作） | `StatServicesWorkingCount` | `StatServicesWorkingPortion` | `StatServicesWorkingTime` | 服务工作过程的次数 / 比例 / 总时长。 |

重要关系（来自源文档）：

- `StatServicesWaitingPortion` = `StatServicesWaitingImpPortion` + `StatServicesWaitingMUPortion`
- `StatServicesWaitingTime` = `StatServicesWaitingImpTime` + `StatServicesWaitingMUTime`

> “整体统计时间”（overall statistics time）定义为统计采集周期扣除 Unplanned Time 和 Paused Time。

> 故障/未计划/暂停期间，若已为装夹或加工派遣了服务，这些服务会保持派遣状态，因此装夹与加工时间在站点故障期间仍继续累计（见 Setup 与 Working 相关属性的 Note）。

### 行走距离统计

- `StatTraveledDistance` → length：Worker 从 WorkerPool 走到各工作站关联 Workplace、以及在工作站之间行走所覆盖的总距离（单位：米）。

## 语法约定

只读属性查询的一般形式：

```simtalk
<Path>.<AttributeName>
```

其中 `<Path>` 为 Worker 类或实例的路径，例如：

```simtalk
print .Resources.MyWorker:1.AvailableForMediation
print .UserObjects.MyWorker:1.CurrentSpeed
print .Resources.John.ResCurrentState   -- 类
print .Resources.John:1.ResCurrentState -- 实例
```

## 源文档中的已知笔误（供核对参考）

以下为源 `.md` / `.txtx` 文档中可注意到的书写不一致，汇总时按属性名与“Return Value”的数据类型为准：

- `StatServicesWaitingImpTime`：源文档 Syntax 误写为 `StatServicesWaitingImpPortion → time`（属性名应为 `StatServicesWaitingImpTime`），Example 也沿用了 `StatServicesWaitingImpPortion`。
- `StatServicesWorkingTime`：源文档 Syntax 写作 `→ real`，但 Return Value 声明为 `time`，此处以 Return Value 的 `time` 为准。
- `HasOrder` 的 Syntax 使用 `<MU-Path>`（应为 `<Path>`），且箭头写作 `->` 而非 `→`。

## 相关章节链接

- Speed [Worker]
- `goTo` [SimTalk]
- `StatServicesWaitingImpPortion` / `StatServicesWaitingMUPortion` [SimTalk] - Worker
- `StatServicesWaitingImpTime` / `StatServicesWaitingMUTime` [SimTalk] - Exporter
- Resource Statistics [material flow objects]
- Tab Statistics [Worker]
- Statistics report — Service Statistics — States — Time Portions of the Exporters
- Statistics report — Worker Statistics — Traveled Distance by Workers
- Get Job Orders At Home Only
- Worker Stays Here After Completing the Job
- Attributes of the Worker
