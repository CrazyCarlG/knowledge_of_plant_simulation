# Worker Modeling & Job Execution（工人建模与作业执行）— 目录摘要

本目录对应 Plant Simulation 帮助文档中的 **Modeling Workers and the Jobs They Do** 主题，介绍如何在仿真模型中建模工人（Worker）及其执行的作业。内容来源为 `worker-modeling-job-execution.md`（同目录的 `worker-modeling-job-execution.txtx` 为同一内容的原始导出文本）。

> **注意：** 物流对象的能量状态（energy states）与同名资源状态（resource states）含义不同——资源状态值对应统计采集周期，能量状态值对应总能耗。

## 核心对象

| 对象 | 作用 |
|------|------|
| **Worker** | 在机器旁的 `Workplace` 上执行作业的工人 |
| **Workplace** | 工人在机器上作业/维修时所站的位置 |
| **WorkerPool** | 工人被创建及等待作业的地方（如休息室/员工室） |
| **Broker** | "工头"，负责把工人分派到机器的作业上 |
| **FootPath** | 工人从 WorkerPool 走到 Workplace 所走的路径 |
| **Exporter / Importer** | 与 Broker 配合，用于建模共享资源（人与工具） |

**使用原则：** 当工人到达机器的时间重要时使用 `Worker`（会沿 FootPath 与 Workplace 动画显示）；当生产零件需要共享资源时使用 `Importer` + `Broker` + `Exporter`。

---

## 各章节摘要

### 1. Model a Worker Who Works at a Machine（工人在机器上作业）
配置 `WorkerPool` 的 **Workers to Create** 表 → 插入并关联 `Broker` → 插入 `Workplace` 并绑定机器（设置 **Station**）与 **Supported Services**（`StandardService`）→ 在机器 **Importer > Processing** 激活并指定 Broker → 用 Connector 连接 WorkerPool 与 FootPath。运行后工人沿 FootPath 走到 Workplace 完成一件零件作业后返回。

### 2. Model a Worker Who Repairs a Machine（工人维修机器）
在前例基础上新增维修工人：插入 FootPath 与维修 Workplace（服务 `repair`），在 WorkerPool 表中新增一行并在 **Additional Services** 填 `repair`；配置机器 **Failures**（如 `Interval 9:`、`Duration 1:`）并在 **Importer > Failure** 激活、将 **Services for Repairing** 改为 `repair`。运行后一个工人加工零件、另一个工人在故障时维修机器。

### 3. Model a Worker Who Carries Parts Between Workplaces（工人在工位间搬运零件）
工人在装载时被 Broker 分派到站点，携带零件离开 Workplace 时分派结束。设置 Workplace 的 **Loading/Unloading Time**；工人按 **Transport** 目标评估并先走向最近目标。班次结束时返回 WorkerPool，未交付零件放入 WorkerPool 的 **Parts Buffer**（无缓冲区会警告并停止）。子示例：

- **Walk on FootPaths（沿 FootPath 行走）**：为取件站与目标站分别挂 Workplace，用 FootPath 连接并连回 WorkerPool，激活取件站的 Transport Importer 并设置 MU Target，设 **Maximum Dwell Time** 避免工人等件过久。
- **Carry Several Parts（3D，一次搬多个零件）**：推荐用预定义 **Animation Area**，或手动画 **Animation Paths**（左右手各一条 `#0#0`/`#1#0`）。将 Worker 的 Y/Z-Dimension 设为 `2`，并设置转运站 Maximum Dwell Time 使工人等第二个零件。
- **Wait for a Free Target（等待空闲目标）**：在 Source 的 **Importer > Transport** 勾选 **Wait for Free Target**，使目标空闲时才请求工人；配合 `ParallelStation`（多个加工位）与 Conveyor，工人等待直到有空闲加工位。可用只读属性 `Conveyor.ReservedFor`、`Part.ReservedPlace` 等观察预留情况。

### 4. Model a Worker Who Walks Freely（工人自由行走）
工人可不受 FootPath 约束自由行走并绕过障碍（机器、护栏、AGV 路径、立柱、楼梯等），部分功能需在 3D 下设置。子示例：

- **Walk Freely Within the Model（模型内自由行走）**：WorkerPool 设置 **Travel Mode > Move freely within the area**；用 **Barred Area** 插入障碍（按 `o` 显示障碍）。
- **Walk One-Way（单向通行）**：Barred Area 用 **Form > One-sided delimitation**，工人可跨虚线侧、不可跨实线侧。
- **Walk Through Doors（穿门）**：自由行走仍需 FootPath 穿越障碍；用工厂布局图作背景（整个图形为单一障碍），在门洞处铺设略长于障碍深度的 FootPath。**有效路径长度**取 3D 场景中的实际长度（非 Attributes 值）；斜坡会将高差×3 计入有效长度，工人选最短"有效"路径；垂直攀爬速度降为 1/3，约 38° 楼梯降为约一半。
- **Walk Through Doors / Climb Stairs（上天桥/爬楼梯）**：用 **Mezzanine + Stairs** 搭建过街天桥让工人安全跨越输送带，需移除连接处栏杆、修正尺寸。

> **障碍间隙：** 障碍与对象/图形之间保留 40 cm 间隙（因默认工人宽 80 cm），可在 Model Settings/Preferences 修改 **Worker Width**。

### 5. Model a Worker Who Waits in Line（工人排队）
自由行走的工人可在被占用的 Workplace 前排队。子示例：

- **Queue Up（排队）**：默认工人直接走到 Workplace，需在 Workplace 的 **MU Animation > Animation Paths** 中调整标记让工人排队。
- **Walk to the End of the Queue（走到队尾）**：在 Workplace 选 **Walk to the End of the Animation Path of the Queue**，工人走到队尾后有空位再上前。
- **Walk Along the Queue（沿队行走）**：额外选 **Walk Along the Animation Path of the Queue**，工人沿队列保持位置前进。两选项都清除时工人直接在空闲时走到 Workplace。当 Workplace 容量用尽时，站着的工人被"挤开"并退出到 WorkerPool/Home Location。

### 6. Model a Worker Who Returns to the Home Location（工人返回 Home Location）
工人完成作业后返回其 **Home Location**，且仅在其 **Scope**（可被分派到的物流对象集合）内被分派。

- 构建加工线（Source → Conveyor → Station1(Workplace) → Conveyor → Station2(Workplace) → Conveyor → Drain）+ Broker + WorkerPool；第一个 Workplace 需清除 **Worker stays here after completing the job**。
- 在 WorkerPool 的 **Workers to Create** 表中拖入 Worker、设置 **Home Location**（Home1 Workplace）与 **Scope**（可被分派的站点，分号分隔）。运行后工人依次去 Station1/Station2 作业后返回 Home1。

### 7. Model a Worker Picking Up / Placing Parts At a Store（工人在 Store 取/放零件）
自由行走的工人在 Source 取件后放入 Store。子示例（均设置 WPStore 的 **Pick/Drop at Store** 选项）：

- **Walk to a Workplace Attached to a Store**：`Pick/Drop at Store > Walk to Workplace`，工人走上 WPStore 逐个填满储位；可用 Store 只读属性 `Full` 的观察者清空 Store（附 SimTalk 源码）。
- **Walk to a Store Column**：`Walk to Store Column`，工人走到目标储位列旁放置零件。
- **Walk Along the Store to a Store Column**：`Walk Along Store to Store Column`，工人走到 Store 左角后沿行依次放置。

### 8. Show Worker Statistics in a Chart（在图表中显示工人统计）
配置两个站点（不同 Processing/Loading/Unloading Time）与多个 Worker（如 Jack、Jill，可设 Amount 与 Home Location），用 **Chart**（Data Source = Worker Pools，按 Creation Table 分组，Occupancy = Operational + failed，Sample Mode）显示工人统计，配合 SankeyDiagram 展示工人流动。

### 9. Set How Many Workers Are Created During Initialization（初始化时设置工人数量）
通过 EventController 的 **Init Control**（运行开始时、对象初始化前执行一次）修改 WorkerPool 的 **Workers to Create**：插入 Method（如 `myInitControl`）→ 加入 EventController 的 Init 控制 → 用 DataTable（Worker/Amount 两列）配合 `WorkerPool.setWorkersToCreateTable(MyWorkersTable)` 设定数量。

### 10. Model Workers with Importer, Broker, and Exporter（用 Importer/Broker/Exporter 建模工人）
用 **Broker–Importer–Exporter** 机制建模共享资源（人/工具），基本四步：站点在 **Importer** 子选项卡指定所需服务与 Broker → Exporter 在 **Attributes** 指定所提供服务与 Broker。子示例：

- **Model Processing Jobs（加工作业）**：多个站点共享同一 Exporter 的服务时（如 Station1/Station3 共享 `ExporterJob1`），因 Exporter 一次只能在一个站点作业而产生短暂停滞。
- **Model Processing and Set-up Jobs（加工 + 换型作业）**：增加 Setup 服务（如 `Exporter3` 提供 Setup），在 **Importer > Set-up** 子选项卡清除 **Common Resources** 并输入 Setup 服务。

---

## 关键要点汇总

- **大小写不敏感：** 服务名、属性名、方法名均不区分大小写；首次出现的字符串决定其大小写形式，SimTalk 中可用 `~=` 进行不区分大小写比较。
- **工人不走动排查：** 若工人不在模型中走动，检查其 Workplace 所属站点的 **Importer** 选项卡的 importer 是否已激活。
- **Parts Buffer：** 班次结束时未交付的零件需放入 WorkerPool 的 Parts Buffer，否则 Plant Simulation 会警告并停止。
- **3D 动画：** 一次搬运多零件优先用预定义 Animation Area；自定义 Animation Paths 较繁琐。
- **自由行走路径计算：** 有效路径长度取 3D 场景实际长度；斜坡高差×3 计入；选最短有效路径。
