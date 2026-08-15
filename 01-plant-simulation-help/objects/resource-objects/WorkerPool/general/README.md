# WorkerPool [object] — 目录说明

本目录 (`general`) 汇总了 Siemens Tecnomatix Plant Simulation 中 **WorkerPool（工人池 / 员工休息室）** 资源对象的帮助文档。目录内包含以下文件：

- `general.md` — WorkerPool 对象的完整 Markdown 文档（正式帮助内容）。
- `general.txtx` — 同一帮助内容的原始文本提取版（对应 Plant Simulation Help pp. 11-3063 至 11-3101，包含页码、页眉页脚等排版痕迹，内容与 `general.md` 等价）。

> 本目录下没有子文件夹，因此没有额外的子级 `README.md` 内容。

---

## 内容概要

**WorkerPool** 对象用于建模工厂的休息室（lounge / staff room）。它是 **Worker–WorkerPool–Workplace–FootPath** 概念中的核心对象，该概念是对 **Broker–Importer–Exporter** 概念的细化。

- Worker 在 WorkerPool 中创建，空闲时留在那里等待订单。
- 一旦 Worker 能提供服务，**Broker** 就把他从 WorkerPool 派往发出订单的工位。
- 轮班结束时，Worker 走回 WorkerPool，并把未能交付的零件存入指定的 **Parts Buffer（零件缓冲）**。

### Worker 到达工位的方式（Travel Mode）

- **在区域内自由行走（Move freely within area）** —— Worker 沿最短路线走到 Workplace，并绕开指定障碍物。
- **沿人行道行走（Walk along footpaths）** —— Worker 在 FootPath 网络上行走，行走时消耗时间。
- **传送到工位（Beam to workplace）** —— 若启用且 Worker 无法经 FootPath 到达 Workplace，则被直接传送（beam）到 Workplace。
- **远程工作（Workers can work remotely）** —— 若启用且没有 Workplace / 没有支持该服务的 Workplace / 所有相关 Workplace 均被占用，Worker 看似被传送到工位执行任务（不在该处动画显示，而是继续在 WorkerPool 中动画显示）。

> 若创建 Worker 时不存在 Broker，Plant Simulation 会把 Worker 的 `AutomaticMediation` 设为 `false`。

### 轮班处理

- 若工厂轮班工作，Worker 会把无法交付的零件存入 Parts Buffer（任意接受零件的物料流对象）。
- 若未分配 Parts Buffer，Plant Simulation 会发出警告并停止仿真。
- 若 Parts Buffer 启用了 **transport importer（运输类 importer）**，下一班开始后由一名空闲 Worker 把零件运到目标对象；否则按 Parts Buffer 的 **Exit Strategy** 继续移动零件。

### 可视化

- WorkerPool 初始不显示任何 Worker；在 **Graphics** 选项卡勾选 **Show Content** 才能看到。
- 在 **MU-Animation** 选项卡可让 Worker 显示在 **Animation Path** 或 **Animation Area** 上（沿 Y 维度分布）。
- 把 WorkerPool 拖到 **Chart** 上可显示其 Worker 的统计信息。
- 添加方式：Home 功能区 > **Manage Class Library > Basic Objects > Resources > WorkerPool**。

---

## 对话框（Dialog Box）

双击 WorkerPool 图标打开对话框。共享属性见 "Dialog Items of the Objects"。编辑 3D 属性：点击 **Edit 3D Properties** 按钮，或选中对象后按空格键。

---

## Tab Attributes（属性选项卡）

### Workers to Create（要创建的 Worker 表）

点击该按钮打开定义要创建并插入模型的 Worker 表。输入数据前先点击 **deactivate Inheritance（取消继承）**。

| 列 | 说明 |
| --- | --- |
| **Worker** | 用作模板的 Worker 类，如 `.Resources.Worker` 或 `.UserObjects.MyWorker`。 |
| **Amount** | 要创建的 Worker 数量。 |
| **Shift** | 关联 Shift Calendar 中定义的班次名称。 |
| **Speed** | 可选行走速度；输入数值即取消继承（此后类中的速度更改不再影响该行）。 |
| **Efficiency** | 效率百分比，如 `80` 表示 80%。 |
| **Home Location** | Worker 完成当前工作后要前往的 Workplace 路径。 |
| **Scope** | Worker 可被调配到的物料流对象路径（包含子 Frame）。 |
| **Additional Services** | Worker 在 Services 列表之外额外提供的服务。 |

注意事项：

- 相对路径始终相对于插入 WorkerPool 的 Frame 解析；仿真期间无法解析 Scope 中的路径会报错并询问是否停止（Home Location 同理）。
- 服务名**不区分大小写**；WorkerPool 按输入顺序尝试导出服务。
- 为节省内存/提高速度，不区分大小写的字符串指向内存中的同一字符串——**首次出现**决定其大小写写法。
- SimTalk 中用 `~=` 运算符进行不区分大小写的字符串比较。
- 对 Workers to Create 表的修改只有在**初始化之前**进行才会影响本次仿真。
- 可在 WorkerPool 的 **Init Control** 中修改该表（但不能在 init 方法中，因为该方法执行得太晚）。

设置 **Scope** 的步骤：点击 Scope 单元格 → 打开一个含一个空单元格的表 → 把目标对象拖入 → 按 Enter 增加更多单元格 → 点击 OK。

表中未列出的单个 Worker 可用 `create` 方法为单次仿真创建（仅 WorkerPool 支持）；这些 Worker 在 reset 时被删除，下次 Init 事件时只重建表中的 Worker。

相关 SimTalk：`AdditionalServices`、`Amount`、`Efficiency`、`getWorkersToCreateTable`、`setWorkersToCreateTable`、`setServices`、`Shift`、`Speed`、`Worker`、`GetJobOrdersAtHomeOnly`。

### Get Job Orders At Home Only（仅在家接收订单）

勾选后，Worker 只在 WorkerPool 的工位或其 **Home Location** 接收新的工作订单。

> 若某 Workplace 启用了 **Worker Stays Here After Completing the Job**，此时停留在该 Workplace 的 Worker 无法被调配——需清除所有 Workplace 上的该设置以保证正确调配。

清除该复选框可让 Worker 在任意位置接收订单（自由行走或在 FootPath 上）。

SimTalk：`GetJobOrdersAtHomeOnly`

### Workers Can Work Remotely（可远程工作）

勾选后，若指定工位没有空闲 Workplace，Worker 就在当前位置完成工作。适合构建不含任何 Workplace 的模型（Worker 全程留在 WorkerPool 中）。

> 即使勾选此选项，只要有空闲 Workplace 仍会使用它。若要阻止某服务使用 Workplace，可用 **Exporter** 或限制 Workplace 只支持特定服务。

SimTalk：`WorkersCanWorkRemotely`

### Travel Mode（出行方式）

选择 Worker 的出行方式：

- **Move freely within area** —— 在模型区域内自由行走并绕开 3D 障碍物。
- **Walk along footpaths** —— 沿插入在工位/Workplace 之间的 FootPath 行走。
- **Beam to workplace** —— 若无 FootPath 可达，则瞬间传送（teleport）到 Workplace（相当于容量为 1 的 Exporter）。

> Travel Mode 仅在 Worker 创建时从 WorkerPool 传递给 Worker，之后不再改变。

SimTalk：`WorkersTravelMode`

#### Move freely within area

- 使用 3D 布局自动计算 Workplace 之间、以及 WorkerPool 与 Workplace 之间的最短路线。
- 自动检测障碍物（墙壁、柱子、机器、输送带、安全围栏等）。默认将物料流对象、可动画对象和 Frame 图形标记为 **Barred Areas**；信息流对象与用户界面对象默认不是。
- 在 **Edit 3D Properties > Graphics > Obstacle for the Worker**（图形为 **Graphic Settings**）中设置障碍物行为。
- 可为 Worker 能进入但不该进入的区域（如起重机旋转区）手动创建 **Barred Area**。
- 可通过门/墙铺设 FootPath 让 Worker 穿过；FootPath 必须略长于墙厚。
- 对 FootPath 而言，决定性的长度是**场景**中的长度（起点、终点、锚点），而非 Attributes 选项卡输入的数值。
- 斜坡：计算坡段有效长度时，Plant Simulation 会**将高差扩大三倍**。例如 1 m × 1 m（x/z）的坡段实际长 1.414 m，但按 1 m × 3 m = 3.162 m 计算有效长度。
- Worker 总是走**有效长度最短**的路线；垂直爬升速度降为约三分之一，38° 斜坡约降为一半。
- 楼层之间只能通过坡道/FootPath 或 **Stairs** 移动（参见示例模型 *Factory 51*）。

#### Walk along footpaths

- 插入 FootPath 建模 WorkerPool 与工位之间、或工位之间的距离。
- 用 **Connector** 连接多条 FootPath 构成网络；Worker 在连通网络内走最短路线。
- 行走时间取决于 Worker 的 **Speed** 与所经过 FootPath 的 **Length 之和**。
- 若 Worker 未走 FootPath（或被传送），则不消耗时间。

#### Beam to workplace

- 若没有 FootPath 可达，则瞬间传送（teleport）Worker 到被调配的 Workplace。
- Worker 相当于容量为 1 的 Exporter；适合不含 FootPath 的模型。

SimTalk：`WorkersTravelMode`、`teleportTo`、`teleportToHome`、`teleportToPool`

### Broker

选择为 Worker 分配服务的 Broker（省略号按钮、输入路径如 `.Models.Model.MyBroker`、或拖放）。按 **F2** 打开所输入对象的对话框。

SimTalk：`BrokerPath`

### Shift Calendar

选择控制 WorkerPool 何时工作的 ShiftCalendar。选择后会自动把 WorkerPool 加入该 ShiftCalendar 的 **Resources** 选项卡。若 Worker 轮班工作，还需选择 **Parts Buffer**。

SimTalk：`ShiftCalendarObject`

### Parts Buffer（零件缓冲）

选择 Worker 在轮班结束时存入无法交付零件用的对象。可以是任意接受零件的物料流对象。若未分配且 Worker 在班次结束时带回零件，Plant Simulation 会警告并停止仿真。

- 启用了 transport importer → 下一班开始后由空闲 Worker 把零件运到目标对象。
- 否则 → 零件按 Parts Buffer 的 Exit Strategy 移动。

> 该设置仅在通过 Shift Calendar 控制轮班时生效。

SimTalk：`PartsBuffer`

---

## Tab Statistics（统计选项卡）

| 项目（英文） | 说明 | 只读属性（SimTalk） |
| --- | --- | --- |
| Paused | 统计收集期间 WorkerPool 处于暂停状态的比例 | `StatPausingCount` |
| Unplanned | 统计收集期间 WorkerPool 未安排工作的比例 | `StatUnplannedPortion` |
| Average Traveled Distance | Worker 从 WorkerPool 到各工位 Workplace 及工位之间行走的平均距离（米） | `StatAverageTraveledDistance` |

其他数值与 **Worker 的 Tab Statistics** 一致。查看固定资源的资源统计：**View > Show Statistics Report**（或右键 Frame → Show Statistics Report，或按 F6）。

---

## Tab Controls（控制选项卡）

点击省略号按钮选择 Method（或拖放、或输入名称后按 F2 编辑）。若要创建为 Method 类型的用户自定义属性：

- 输入名称并选择 **Create Control** → 插入 `self.<name>`，如 `self.A1Ctrl`。
- 或在空文本框上选择 **Create Control** → 插入 `self.On<内置名>`，如 `self.OnEntrance`。

后续编辑源码：按 F2、Shift+双击、上下文菜单 **Open Object**，或从 **User-defined** 选项卡打开。删除控制需删除用户自定义属性（仅从文本框删除名称会保留属性）。

| 控制 | 触发时机 | SimTalk |
| --- | --- | --- |
| **Entrance Control** | Worker 进入 WorkerPool 时调用。 | `EntranceCtrl` |
| **Exit Control** | Worker 离开 WorkerPool 时调用。 | `ExitCtrl` |

---

## Tab User-defined（用户自定义选项卡）

定义自己的属性，见 "Tab User-defined" 通用说明。

---

## 菜单

- **View Menu** 提供以下命令：
  - **Assigned Workers** —— 打开 WorkerPool 为其提供服务的所有 Worker 列表。SimTalk：`getAssignedWorkersTable`、`getAssignedWorker`、`NumAssignedWorkers`。
  - **Working Workers** —— 打开正在工作的 Worker 信息列表，显示：提供服务的 Worker、**Location**（Worker 当前所在对象；自由行走的 Worker 显示为 WorkerPool）、**Target** 目标工位、当前提供的 **Service**。SimTalk：`getWorkingWorkersTable`。
  - **Refresh**、**Show Statistics Report**、**Show Attributes and Methods**。
- **Tools Menu** —— **Edit Controls > Init control**、**Edit Observers**。
- **Navigate Menu / Help Menu** —— 见各自通用说明。

### Init Control

在仿真运行开始时的 **init 阶段**调用，位于事件计算**之前**（普通 init 方法在初始事件计算**之后**执行）。可在其中为下一次仿真更改 **Workers to Create** 表，或初始化影响事件生成的属性（如可用性）。

SimTalk：`InitCtrl`

---

## WorkerPool 的方法（Methods）

WorkerPool 提供目录中列出的方法以及 **Methods of All Objects**。查看全部方法、只读属性与属性：打开 **Show Attributes and Methods**（Frame 实例按 F8，或 Class Library 上下文菜单）。

---

## SimTalk 参考汇总

示例：

```simtalk
MyFootPath.Width := 2 // meters
```

相关 SimTalk 属性 / 方法：

- WorkerPool：`AdditionalServices`、`Amount`、`Efficiency`、`Worker`、`Speed`、`Shift`、`getWorkersToCreateTable`、`setWorkersToCreateTable`、`BrokerPath`、`ShiftCalendarObject`、`PartsBuffer`、`WorkersTravelMode`、`WorkersCanWorkRemotely`、`GetJobOrdersAtHomeOnly`、`EntranceCtrl`、`ExitCtrl`、`InitCtrl`、`getAssignedWorkersTable`、`getAssignedWorker`、`NumAssignedWorkers`、`getWorkingWorkersTable`
- 统计：`StatPausingCount`、`StatUnplannedPortion`、`StatAverageTraveledDistance`
- 传送：`teleportTo`、`teleportToHome`、`teleportToPool`
- 相关：`setServices`（importer）、`WorkerStaysHere`（Workplace）

---

## 参见（See also）

- Model Workers and the Jobs They Do
- Worker-WorkerPool-Workplace-FootPath 概念
- Broker-Importer-Exporter 概念
- Show Worker Statistics in a Chart
- 视频：<https://youtu.be/HiPziA8kxc0?si=qYFCTtAc7V4GzXjQ&t=178>
