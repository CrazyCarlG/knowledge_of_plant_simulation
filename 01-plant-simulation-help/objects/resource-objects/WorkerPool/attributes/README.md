# WorkerPool 的属性（Attributes）— 目录说明

本目录 (`attributes`) 汇总了 Siemens Tecnomatix Plant Simulation 中 **WorkerPool（工人池 / 员工休息室）** 资源对象的属性（Attributes）帮助文档。目录内包含以下文件：

- `attributes.md` — WorkerPool 对象属性的完整 Markdown 文档（正式帮助内容）。
- `attributes.txtx` — 同一帮助内容的原始文本提取版（对应 Plant Simulation Help pp. 11-3117 至 11-3139，包含页码、页眉页脚等排版痕迹，内容与 `attributes.md` 等价）。

> 本目录下没有子文件夹。本 README 除总结本目录的 `attributes.md` 外，还汇总了同级子目录（`general`、`methods`、`read-only-attributes`）中各 `README.md` 的要点。

---

## 内容概要

WorkerPool 提供：

- 下列属性（Attributes）。
- **Attributes of All Objects（所有对象的通用属性）**。

要查看对象的全部方法、只读属性与属性，请打开 **Show Attributes and Methods** 窗口。属性的值既可**设置**（通过对话框中的复选框、文本框、下拉列表，或直接为属性赋值），也可**获取**：

```simtalk
MyWorkerPool.BrokerPath := mybroker     -- 设置属性值
print MyWorkerPool.BrokerPath            -- 获取属性值
posit := Station.Cont.XPos               -- 获取属性值
```

### 属性分类

WorkerPool 的属性可分为以下几类：

#### 1. 普通属性（Attribute）

直接在 `<Path>.<属性>` 上赋值/取值。

| 属性 | 数据类型 | 说明 |
| --- | --- | --- |
| `BrokerPath` | `object` | 设置 WorkerPool 用来提供服务的 Broker 的路径。 |
| `EntranceCtrl` | `method` | 指定一个 Method；当 Worker 进入 WorkerPool 时被调用。 |
| `ExitCtrl` | `method` | 指定一个 Method；当 Worker 离开 WorkerPool 时被调用。 |
| `GetJobOrdersAtHomeOnly` | `boolean` | 设置 Worker 是否只在 WorkerPool 或其 Home Location 接收新的工作订单（`true`）。 |
| `InitCtrl` | `method` | 指定一个 Method；在仿真运行开始时的 init 阶段、事件计算**之前**被调用。 |
| `PartsBuffer` | `object` | 设置 Worker 在轮班结束走回 WorkerPool 时存入未能交付零件所用的对象。 |
| `WorkersCanWorkRemotely` | `boolean` | 设置当被分配工位无空闲 Workplace 时，Worker 是否在当前位置完成工作（`true`）。 |
| `WorkersTravelMode` | `string` | 设置 Worker 在模型中的移动方式（Travel Mode）。 |

#### 2. Workers to Create 表的子属性（Sub-attribute）

通过方法 `getWorkersToCreateTableRow(Row:integer)` 的**子属性**读写，用于逐行设置 Workers to Create 表。

| 子属性 | 数据类型 | 说明 |
| --- | --- | --- |
| `AdditionalServices` | `string[]` | Worker 除 Services 列表外可额外执行的服务。 |
| `Amount` | `integer` | 要创建的 Worker 数量。 |
| `Efficiency` | `real` | Worker 执行工作的效率（如 100 = 100%，200 = 耗时减半）。 |
| `HomeLocation` | `path` | Worker 完成当前工作后要前往的 Workplace（Home Location）路径。 |
| `Scope` | `string[]` | Worker 可被调配到的物料流对象路径（也包含子 Frame）。 |
| `Shift` | `string` | Worker 工作的班次名称（在关联的 ShiftCalendar 中定义）。 |
| `Speed` | `speed` | Worker 在 FootPath 上行走的速度。 |
| `Worker` | `object` | 用作待创建 Worker 模板的 Worker 类。 |

示例：

```simtalk
MyWorkerPool.getWorkersToCreateTableRow(1).AdditionalServices := ["drill1", "drill2", "drill3"]
MyWorkerPool.getWorkersToCreateTableRow(1).Amount := 2
MyWorkerPool.getWorkersToCreateTableRow(1).Efficiency := 75
MyWorkerPool.getWorkersToCreateTableRow(1).Worker := .UserObjects.MyWorker
```

#### 3. 只读属性（Read-only attribute）

| 属性 | 数据类型 | 说明 |
| --- | --- | --- |
| `StatAverageTraveledDistance` | `length` | 返回 Worker 从 WorkerPool 到各工位 Workplace 及工位之间行走的平均距离（米）。 |

示例：

```simtalk
print MyWorkerPool.StatAverageTraveledDistance
```

#### 4. Worker [object] 引用

`attributes.md` 末尾还包含了 **Worker [object]** 对象的说明：Worker 用于在工位的 Workplace 上执行工作，是 **Worker–WorkerPool–Workplace–FootPath** 概念（对 Broker–Importer–Exporter 概念的细化）中的核心对象。与 Exporter 不同，Worker 在走向 Workplace 时会消耗时间，并且额外提供 *En-route to the Job* 的统计值。

---

## 同级子目录摘要

### `general` — WorkerPool 对象总览

- **定位**：建模工厂休息室，是 Worker–WorkerPool–Workplace–FootPath 概念的核心对象（细化自 Broker–Importer–Exporter 概念）。
- **工作流**：Worker 在 WorkerPool 中创建并等待订单 → Broker 将其派往发出订单的工位 → 轮班结束走回 WorkerPool，并将未交付零件存入 Parts Buffer。
- **Travel Mode（出行方式）**：`Move freely within area`（自由行走并绕开 3D 障碍）、`Walk along footpaths`（沿 FootPath 网络行走）、`Beam to workplace`（无 FootPath 可达时瞬间传送）。
- **关键选项卡**：Tab Attributes（Workers to Create 表、Get Job Orders At Home Only、Workers Can Work Remotely、Travel Mode、Broker、Shift Calendar、Parts Buffer）、Tab Statistics、Tab Controls（Entrance/Exit Control）、Tab User-defined。
- **方法入口**：通过 **Show Attributes and Methods**（F8 或 Class Library 上下文菜单）查看。

### `methods` — WorkerPool 的方法

| 方法 | 说明 |
| --- | --- |
| `getAssignedWorker(No)` | 返回指定编号的已分配 Worker。 |
| `getAssignedWorkersTable([table])` | 返回已分配 Worker 的表（省略参数时返回数组）。 |
| `getIdleWorker` | 返回第一个空闲 Worker（并将其 `IsIdle` 置 `false`）；无空闲时返回 `VOID`。 |
| `getWorkersToCreateTable(table[, byref Inherited])` | 读取 Workers to Create 表并写入指定表。 |
| `getWorkersToCreateTableRow(row).<subattribute>` | 读取/设置 Workers to Create 表某一行的各项设置。 |
| `getWorkingWorkersTable(table)` | 返回正在工作的 Worker 的表。 |
| `setWorkersToCreateTable(table/void)` | 设置 Workers to Create 表名称（传 `void` 激活继承）。 |

> 本目录的 `getWorkersToCreateTableRow` 的子属性即 `attributes` 目录中列出的 `AdditionalServices`、`Amount`、`Efficiency`、`HomeLocation`、`Scope`、`Shift`、`Speed`、`Worker`。

### `read-only-attributes` — WorkerPool 的只读属性

| 只读属性 | 说明 | 返回值类型 |
| --- | --- | --- |
| `NumAssignedWorkers` | 已分配的 Worker 数量。 | `integer` |
| `NumIdleWorkers` | 空闲（未工作）的 Worker 数量。 | `integer` |
| `StatAverageTraveledDistance` | Worker 到各 Workplace 及工位之间的平均行走距离（米）。 | `length` |

---

## SimTalk 参考汇总

### 属性（本目录）

- 普通属性：`BrokerPath`、`EntranceCtrl`、`ExitCtrl`、`GetJobOrdersAtHomeOnly`、`InitCtrl`、`PartsBuffer`、`WorkersCanWorkRemotely`、`WorkersTravelMode`
- Workers to Create 子属性（`getWorkersToCreateTableRow`）：`AdditionalServices`、`Amount`、`Efficiency`、`HomeLocation`、`Scope`、`Shift`、`Speed`、`Worker`
- 只读属性：`StatAverageTraveledDistance`

### 关联方法（`methods` 目录）

- `getAssignedWorker`、`getAssignedWorkersTable`、`getIdleWorker`
- `getWorkersToCreateTable`、`getWorkersToCreateTableRow`、`getWorkingWorkersTable`、`setWorkersToCreateTable`

### 关联只读属性（`read-only-attributes` 目录）

- `NumAssignedWorkers`、`NumIdleWorkers`、`StatAverageTraveledDistance`
- 相关：`IsIdle`（Worker）、`getIdleWorker`

### 其他相关 SimTalk

- `ShiftCalendarObject`、`setServices`（importer）、`teleportTo`、`teleportToHome`、`teleportToPool`、`WorkerStaysHere`（Workplace）

---

## 参见（See also）

- Attributes of the WorkerPool（本目录 `attributes.md`）
- WorkerPool [object]（`general` 目录）
- Methods of the WorkerPool（`methods` 目录）
- Read-Only Attributes of the WorkerPool（`read-only-attributes` 目录）
- Attributes of All Objects（所有对象的通用属性）
- Worker-WorkerPool-Workplace-FootPath 概念
- Broker-Importer-Exporter 概念

---

*Plant Simulation Help 11-3117 至 11-3139 — Unpublished work. © 2026 Siemens*
