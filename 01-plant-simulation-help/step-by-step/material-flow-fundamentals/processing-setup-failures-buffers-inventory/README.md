# Processing, Set-up, Failures, Buffers, Inventory

本目录汇总 Plant Simulation 帮助文档中关于「物料流建模」的核心主题：工位设置（Set-up）、加工时间（Processing Time）、故障（Failures）、缓冲区（Buffers）以及库存出入库（Inventory / Store）。

## 目录内容

- `processing-setup-failures-buffers-inventory.md` — 本主题的整理版摘要（英文）
- `processing-setup-failures-buffers-inventory.txtx` — 原始帮助文档文本（英文）

---

## 1. 设置工位（Setting a Station Up）

定义 **Station**、**ParallelStation**、**AssemblyStation**、**DismantleStation**、**Drain** 如何为加工另一类 MU 而进行设置。

- **设置选项**（*Set-Up* 选项卡）：
  - **Automatic**：MU 准备进入时自动触发设置流程。
  - **Only When Empty**：仅当工位为空时才为下一类型设置，目标类型 MU 在设置完成后才能进入。
  - **Set-up After n Parts**：加工一定数量零件后设置；零件类型提前变化时也会重新设置并重新计数。（**ParallelStation 不支持此项**）
- **设置判据**（Set-Up Criteria）：当 **MU 名称** 变化，或 **用户自定义属性**（数据类型 `string`）的值变化时设置。
- **设置时间**（Set-Up Time，*Times* 选项卡）：可选分布、常量，或用 **Matrix(Type)** 表定义「源类型 → 目标类型」的矩阵时间；**Formula** 可用 `@` 访问 MU。

## 2. 定义加工时间（Defining Processing Times）

加工时间是 MU 停留在物料流对象上被加工的时间（即从设置完成到移动到后继对象之间的间隔）。

- 在 *Times* 选项卡选择：分布、常量（`Const`）、`List(Type)`（按 MU 类型）、`List(Place)`（按 ParallelStation 工位）、`Formula`。
- **时间格式**：`days:hours:minutes:seconds`（如 `12:34` = 12 分 34 秒；`1:::` = 1 天；无冒号按秒计）。
- **Formula**：可输入 Method 名（须返回 `time`）、算术表达式或直接以 `@` 访问 MU，例如 `@.MyAttribute+1`、`@.timeRed`。

## 3. 建模故障（Modeling Failures）

定义**故障档案**（failure profiles）来模拟机器故障，影响工位的技术可用性。

- 方式：手动勾选 **Failed**，或用 *Failures* 选项卡的故障生成器。
- 故障期间对象变为 **inactive**：不接收零件，正在加工的零件中断并在故障清除后继续，故障时长计入加工/停留时间。
- **配置步骤**：勾选 `Active` → `New` → 输入 `Name` → 设置 `Start`（首次故障，适合用 Lognormal/Erlang/Negative exponential）与 `Stop` → 选择 **Availability + MTTR**（会自动换算为 Interval + Duration）或直接指定 **Interval / Duration** → 选择时间基准 → `OK`。
- **时间基准**：
  - **Simulation Time**：无论对象状态如何都消耗间隔时间。
  - **Operating Time**：仅在对象可运行时消耗。
  - **Processing Time**：仅在加工时消耗（ParallelStation 的模拟 MTBF 随并行加工数增加而降低）。
- 运行中可通过 Method 修改 Availability/MTTR（如 `setFailure` + `init`/`reset`/`endSim`）。

## 4. 生产线中的缓冲（Buffering Parts）

**Buffer** 放置在两个部件/工位之间，作用：后继部件故障时暂存零件；前序部件停止时继续输送零件，避免流程中断。

- 容量足够大的 Buffer 可完全解耦两侧部件，并补偿波动导致的排队。
- **Statistics** 选项卡显示：相对占用率、相对空/满时间占比、最大/最小容量、进出数量。
- 3D 中通过 **Show Contents As → Fill level** 查看填充水平；颜色含义：灰=背景、红=>90%、橙=<10%、绿=之间（可选 MUs / Fill level / Both 三种显示方式）。
- 可用 **Chart**（配合 drag-and-drop 控件）展示「空 / 部分满 / 满」的占比。

## 5. 入库与出库（Placing Parts into Stock）

用 **Store** 建模仓库；零件停留在 Store 中直到用 Method 取出。

- Store 的入库触发传感器调用 **Entrance Control**（决定存放位置）；无 Entrance Control 时按坐标网首个空闲位存放。
- 示例模型对象：`Receiving`（Source）、`MixOrders`（ParallelStation，打乱顺序）、`MyStore`（Store）、`RetrieveFromStore`（Station）、`Shipping`（Drain）。
- 关键 Method：
  - `placeInStock`（Entrance Control）：登记零件到 `InventoryTable`，Store 满时增大 `xDim`。
  - `removeFromStock`（RetrieveFromStore 的 Rear-triggered Exit Control）：调用 `AttemptToRemoveNextPart`。
  - `attemptToRemoveNextPart`：管理库存表，按原始顺序取出零件，维护 `NextNumber` 变量。
- 用 **Chart (Plotter)** 以 `MyStore.numMU` 展示 Store 随时间变化的占用情况。

---

*本文档由目录内 `.md` 文件内容整理而成。*
