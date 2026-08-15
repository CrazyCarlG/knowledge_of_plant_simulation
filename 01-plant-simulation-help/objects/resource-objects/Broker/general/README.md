# Broker 对象（general）— 目录总结

本目录包含 Plant Simulation 中 **Broker（中介器）** 资源对象的帮助文档，共两份内容相同的文件：

- `general.md` — Markdown 格式的完整文档
- `general.txtx` — 原始文本导出（带页码，含德文列名等冗余信息）

以下为两份文档的内容总结。

---

## 1. 概述

**Broker** 用于在"提供的服务"（由 Exporter/Worker 提供）与"所需的服务"（由 importer 请求）之间进行中介。可用它来建模工厂经理、部门主管或车间工头。

Broker 与 **Exporter** 及以下对象的 **importer**（见 *Tab Importer* 和 *Sub-tab Failure*）协作：Station、ParallelStation、AssemblyStation、DismantleStation、DePortioner、Mixer、Portioner、Tank。

核心机制：

- 每个 Broker 可管理多个 Exporter/Worker（提供服务）。
- 可接收多个 importer 的服务请求。
- 请求由"所需服务列表 + 各服务数量"组成，服务名是一个字符串。

请求流转规则：

- Broker 收到请求后立即尝试用其管理的 Exporter/Worker 满足。
- 若无法满足，可通过 **Connector** 把请求传递给其他 Broker；Connector 的方向决定传递方向。
- 若不同 Broker 的 Exporter/Worker 能共同满足请求，则分配这些 Exporter/Worker。
- 若无法立即满足，最先收到请求的 Broker 会保存该请求，稍后再尝试。

服务匹配规则：

- 按"服务逐个查找"的方式为每个服务寻找 Exporter/Worker。
- Exporter/Worker 一旦提供某服务，会预留"最大可能数量"或"所需数量"，这部分容量不再提供给其他服务。
- 因此**应先请求特殊服务，最后请求更通用的服务**。

> 注意 1：若 importer 同时请求多个服务，这些服务必须**同时可用**，Broker 才会分配给工位。
> 注意 2：Broker **不做任何优化**，因此可能出现"理论上可分配却分配失败"的情况。

---

## 2. 示例：请求顺序的影响

importer `MyImporter` 各需 1 个服务 A 和 1 个服务 B；有两个容量各为 1 的 Exporter/Worker：

- `Exporter1` 提供 A、B
- `Exporter2` 仅提供 A

- 若按 **(A, B)** 顺序请求：Broker 将 `Exporter1` 分配给 A，发现 `Exporter2` 无法提供缺失的 B，请求失败。
- 若按 **(B, A)** 顺序请求：`Exporter1` 提供 B、`Exporter2` 提供 A，立即满足。

传递顺序：Broker 先传给所有直接后继（由 Connector 编号决定），再传给后继的后继。当 Exporter/Worker 注册为可用时，Broker 先检查自身管理的未满足请求，再让其 Broker 后继检查未满足请求。

---

## 3. Broker 如何向 Worker 派发任务

Broker 按工单的 **Priority（优先级）** 派发任务。派发过程中按以下阶段依次尝试，并区分是否勾选 **Choose the Nearest Worker**。

勾选 **Choose the Nearest Worker** 时（阶段 0–8）：

1. **初始阶段**：Worker 位于正确工位、且在适合所需服务的 Workplace 上，工位在 Worker 的 Scope 内。
2. **阶段 1**：Worker 位于正确工位，但所在 Workplace 不支持所需服务；工位在 Scope 内。
3. **阶段 2**：Worker 不在 Workplace 上，但工位在 Scope 内。
4. **阶段 3**：Worker 位于另一工位的 Workplace 上，且正确工位在 Scope 内。
5. **阶段 4**：Worker 位于正确工位、Workplace 合适，但 Worker 无定义 Scope。
6. **阶段 5**：Worker 位于正确工位，但 Workplace 不支持所需服务；Worker 无定义 Scope。
7. **阶段 6**：Worker 无 Scope 且不在 Workplace 上。
8. **阶段 7**：Worker 无 Scope 且位于错误工位的 Workplace 上。
9. **阶段 8**：Worker 正在工作中，需要从当前任务被抽调。

未勾选时：阶段 1–8 相同，但不使用"最近 Worker"距离准则。

---

## 4. 对话框与选项卡

双击 Broker 图标打开对话框。

- **Edit Simulation Properties**：共享属性见 *Dialog Items of the Objects*。
- **Edit Animation Properties**：点击左下角 **Edit 3D Properties** 或选中对象后按空格键；操作图形用 **Show Manipulators**（Edit 选项卡）或按 `M`。

### Tab Attributes

提供以下设置：

- **Choose the Nearest Worker** [复选框]
- **Importer Request Control** [Broker]
- **Exporter Request Control** [Broker]

**Choose the Nearest Worker**：勾选后 Broker 优先选择步行距离最短的 Worker；清除后选择任意能胜任的 Worker（不论位置）。接收导入请求时按以下准则选 Worker：最高优先级 → 已位于请求工位的 Workplace → 匹配 Scope。勾选后额外计算各 Worker 到工位的路径，可能拖慢仿真。
SimTalk：`ChooseNearestWorker`

### Controls（控制）

点击省略号按钮并在 **Select Object** 中选择 Method，或直接输入源码：

- 选择已有 Method：省略号按钮 → 导航到 Method → OK；或在文本框中按 `F2`；或从 Frame 拖入 Method。
- 创建对象内 Method 作为控制：输入名称 → 右键 **Create Control**（生成 `self.名称`）；或空文本框上选 **Create Control**（生成 `self.On内置名`）。

编辑源码：`F2` / `Shift+双击` / 右键 **Open Object** / **User-defined** 选项卡双击 Method 名。

执行顺序：若同时定义了 Exporter 与 Importer Request Control，**Exporter Request Control 先执行**。多个 Importer Request Control 同时执行时，顺序与 **Open Importers** 列表中 importer 顺序一致。

**Importer Request Control [Broker]**：在 Broker 收到请求或需再次处理请求（如 Exporter/Worker 注册为可用）时调用。源码中需自行确保请求被处理（如用 `engage` 方法），可自定义分配策略。该控制**不打断**当前正在执行的方法，只在当前调用链执行完后才被调用；importer 请求不能互相插队。
标准实现：`ImpRequestCtrl` + `doStandardExport`

**Exporter Request Control [Broker]**：在 Exporter/Worker 向其 Broker 注册为可用时调用，可能被分配新 importer。源码中需自行确保请求被处理（如 `engage`），可指定具体 importer。
标准实现：`ExpRequestCtrl` + `doStandardExport`

> 注意：对于 Broker 层级（多个 Broker 用 Connector 相连），Plant Simulation **不调用子 Broker 的控制**，只调用键入对象中的那个 Broker 的控制。

---

## 5. Tab Statistics（统计）

要收集统计数据，需勾选 **Broker Statistics**。统计项：

| 项目 | 说明 | 只读属性 |
|------|------|----------|
| Open Requests | 当前开放请求数 | `OpenRequests` |
| Open Requests (sum) | 开放请求总数 | `StatOpenRequests` |
| Satisfied Requests | 已满足请求数 | `SatisfiedRequests` |
| Satisfied Requests (sum) | 已满足请求总数 | `StatSatisfiedRequests` |
| Open Capacity | 可用容量 | `OpenCapacity` |
| Open Capacity (sum) | 开放容量总数 | `StatOpenCapacity` |
| Mediated Capacity | 已中介容量 | `MediatedCapacity` |
| Mediated Capacity (sum) | 已中介容量总数 | `StatMediatedCapacity` |

> 注意：Broker 层级中，中介服务只计入键入 importer 中的那个 Broker，即使服务由子 Broker 提供。

查看方式：`View > Show Statistics Report` / 在 Frame 中右键 **Show Statistics Report** / 按 `F6`。

- **Broker Statistics [activate]**：勾选收集统计，SimTalk：`BrokerStatOn`
- **Service Statistics [Broker]**：打开服务统计表，展示每项服务的 **Dwelling Time** 与 **Mediation Time**，SimTalk：`serviceStat`。若服务由多个 Worker/Exporter 满足，时间间隔只记录一次；途中时间按"途中最久"的 Worker 统计。

**Dwelling Time** 列：Count / Sum（`StatStayTime`）/ Mean Value（`StatStayTimeMu`）/ Standard Deviation（`StatStayTimeDelta`）/ Min / Max。

**Mediation Time** 列：Count / Sum（`StatMediationTime`）/ Mean Value（`StatMediationTimeMu`）/ Standard Deviation（`StatMediationTimeDelta`）/ Min / Max。

---

## 6. View Menu（视图菜单）

- Refresh
- Show Statistics Report
- Show Attributes and Methods
- **Open Importers**：显示所有注册了未满足请求的 importer。列 1 为 importer，列 2 为 Type：`0`=failure、`1`=set-up、`2`=processing、`3`=transport；因高优先级工位被中断的 importer 排在最前。SimTalk：`getOpenImporters`、`forgetOpenRequest`
- **Satisfied Importers**：显示已分配 Exporter/Worker 的 importer，列布局同上。SimTalk：`getSatisfiedImporters`
- **Exporters**：显示所有已注册 Exporter 的信息（名称、State、Capacity、Free Cap.）。SimTalk：`AdministeredExporters`
- **Offered Services**：显示 Exporter/Worker 提供的服务（Services、Capacity、Free Cap.、State）；双击服务名可打开子表查看路径。SimTalk：`getOfferedServices`

---

## 7. 方法与参见

Broker 提供：

- 目录中列出的方法
- 所有对象共有的方法（Methods of All Objects）

查看全部方法/只读属性/属性：`Show Attributes and Methods`（Class Library 右键 / `F8` / Home 选项卡）。

相关 SimTalk：`brokerStat`、`BrokerStatOn`、`serviceStat`、`ChooseNearestWorker`、`ImpRequestCtrl`、`ExpRequestCtrl`、`doStandardExport`。

参见：How the Broker Mediates Jobs to the Worker、How the Worker Decides Where to Work、Model Workers and the Jobs They Do、Model Workers with Importer, Broker, and Exporter、Worker [object]、Workplace、Priority [Worker]、Tab Scope / Scope [SimTalk] - Worker。
