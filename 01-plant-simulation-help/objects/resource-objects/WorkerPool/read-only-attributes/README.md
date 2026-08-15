# WorkerPool 的只读属性（Read-Only Attributes）— 目录说明

本目录 (`read-only-attributes`) 汇总了 Siemens Tecnomatix Plant Simulation 中 **WorkerPool（工人池 / 员工休息室）** 资源对象的只读属性帮助文档。目录内包含以下文件：

- `read-only-attributes.md` — WorkerPool 对象只读属性的完整 Markdown 文档（正式帮助内容）。
- `read-only-attributes.txtx` — 同一帮助内容的原始文本提取版（对应 Plant Simulation Help pp. 11-3113 至 11-3117，包含页码、页眉页脚等排版痕迹，内容与 `read-only-attributes.md` 等价）。

> 本目录下没有子文件夹，因此没有额外的子级 `README.md` 内容。

---

## 内容概要

本目录介绍 WorkerPool 提供的 **只读属性（Read-Only Attributes）**。WorkerPool 除提供目录左侧列出的只读属性外，还提供 **_Read-Only Attributes of All Objects（所有对象的通用只读属性）**。

- 只读属性的值**只能查询，不能设置**——Plant Simulation 会在查询的时刻即时计算其值。
- 大多数只读属性对应对象某一选项卡（例如 **Statistics（统计）** 选项卡）上不可用的对话框条目。
- 查看对象的全部方法、只读属性与属性：打开 **Show Attributes and Methods** 窗口（Frame 实例按 **F8**，或在 Class Library 上下文菜单中选择）。

查询只读属性值的示例：

```simtalk
print MyWorkerPool.StatAverageTraveledDistance
```

---

## WorkerPool 的只读属性一览

| 只读属性 | 说明 | 语法 | 返回值类型 |
| --- | --- | --- | --- |
| `NumAssignedWorkers` | 返回 WorkerPool 已分配的 Worker 数量。 | `<Path>.NumAssignedWorkers -> integer` | `integer` |
| `NumIdleWorkers` | 返回 WorkerPool 中空闲（未工作）的 Worker 数量。 | `<Path>.NumIdleWorkers -> integer` | `integer` |
| `StatAverageTraveledDistance` | 返回 Worker 从 WorkerPool 到各工位 Workplace 及工位之间行走的平均距离（米）。 | `<Path>.StatAverageTraveledDistance → length` | `length` |

---

## 只读属性详解

### NumAssignedWorkers

返回 `<Path>` 指定的 WorkerPool 已分配的 Worker 数量。

- **类型**：Read-only attribute（只读属性）
- **语法**：`<Path>.NumAssignedWorkers -> integer`
- **返回值**：数据类型为 `integer`。

**示例：**

```simtalk
print MyWorkerPool.NumAssignedWorkers
```

相关 SimTalk：`getAssignedWorkersTable`、`getAssignedWorker`、`NumAssignedWorkers`。

---

### NumIdleWorkers

返回 `<Path>` 指定的 WorkerPool 中空闲（即未工作）的 Worker 数量。

- **类型**：Read-only attribute（只读属性）
- **语法**：`<Path>.NumIdleWorkers -> integer`
- **可监视（Watchable）**：该属性可监视。
- **返回值**：数据类型为 `integer`。

**示例：**

```simtalk
waituntil WorkerPool.NumidleWorkers > 0
var worker:object := WorkerPool.getIdleWorker
```

相关 SimTalk：`IsIdle`（Worker）、`getIdleWorker`、`NumIdleWorkers`。

---

### StatAverageTraveledDistance

返回 `<Path>` 指定的 WorkerPool 中，Worker 从 WorkerPool 到各工位所附 Workplace、以及各工位之间行走的**平均距离（米）**。

- **类型**：Read-only attribute（只读属性）
- **语法**：`<Path>.StatAverageTraveledDistance → length`
- **返回值**：数据类型为 `length`。

**示例：**

```simtalk
print MyWorkerPool.StatAverageTraveledDistance
```

---

## SimTalk 参考汇总

只读属性及关联的 SimTalk 项：

- `NumAssignedWorkers`
- `NumIdleWorkers`
- `StatAverageTraveledDistance`
- 相关：`getAssignedWorkersTable`、`getAssignedWorker`、`getIdleWorker`、`IsIdle`（Worker）

---

## 参见（See also）

- Read-Only Attributes of the WorkerPool
- _Read-Only Attributes of All Objects
- Attributes of the WorkerPool（`attributes` 目录）
- Methods of the WorkerPool（`methods` 目录）
- WorkerPool [object]（`general` 目录）

---

*Plant Simulation Help 11-3113 至 11-3117 — Unpublished work. © 2026 Siemens*
