# Exporter Attributes（属性） — 目录说明

本目录包含 Exporter 对象（资源对象之一）的 **SimTalk 属性** 说明文档。

- `attributes.md` — 属性的 Markdown 摘要（本目录的主要文档）。
- `attributes.txtx` — 同内容的原始导出文本（Plant Simulation Help 摘录，含页码与页眉）。

> 注：本目录下没有子文件夹，因此没有其他 README.md 需要汇总。

## 内容摘要

Exporter 对象除提供 *Attributes of All Objects*（所有对象通用属性）外，还提供以下属性。属性值既可通过对话框的复选框、文本框、下拉列表设置/读取，也可通过 SimTalk 赋值。

### 只读属性

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| `StatSumMediatedCapacity` | 只读（integer） | 返回指定 Exporter 的中介容量之和。`print MyExporter.StatSumMediatedCapacity` |

### 可读写属性

| 属性 | 语法 | 说明 |
| --- | --- | --- |
| `AutomaticMediation` | `<Path>.AutomaticMediation:boolean` | 控制 Broker 是否自动分配该 Exporter。`true` = 由 Broker 自动分配；`false` = 自行分配。 |
| `BrokerPath` | `<Path>.BrokerPath:object` | 设置负责为该 Exporter 采购服务的 Broker 路径。 |
| `Capacity` | `<Path>.Capacity:integer` | 设置 Exporter 的容量（≥ 0）。仅在不会低于已提供给 importer 的容量时才能降低容量；增大容量时 Broker 会立即寻找新 importer。 |
| `ExpStatOn` | `<Path>.ExpStatOn:boolean` | 激活（`true`）/关闭（`false`）该 Exporter 的统计。 |
| `FailServices` | `<Path>.FailServices:boolean` | 是否在故障时中断其提供的服务（`true` 中断，`false` 不中断）。 |
| `OrderCtrl` | `<Path>.OrderCtrl:method` | 指定一个 Method；每当 Exporter 被分配给 importer 时调用，决定其如何处理订单。参数：`Importer`（object）、`Type`（integer，0=故障/移除故障、1=准备、2=加工、3=运输）。 |
| `Priority` | `<Path>.Priority:integer` | 设置 Exporter 提供服务的优先级；值越大越紧急，仅对注册到同一 Broker 的 Exporter 有效。 |
| `ReleaseCtrl` | `<Path>.ReleaseCtrl:method` | 指定一个 Method；任何 importer 释放 Exporter 时执行。参数同 `OrderCtrl`。调用时 Exporter 已离开 importer，需自行为其分配新 importer（如 `findNewImporter`）。 |
| `Services` | `<Path>.Services:array[]` | 设置/返回该 Exporter 导出的服务名称数组（字符串）。 |

## 相关对象：Broker

文档同时介绍了 **Broker（对象）**：Broker 是服务提供与服务需求之间的中介，可用于建模工厂经理、部门主管或车间工长。

- 与各 Station、ParallelStation、AssemblyStation、DismantleStation、DePortioner、Mixer、Portioner、Tank 的 Exporter 及 importer 协作。
- 每个 Broker 可管理多个 Exporter/Worker，并接收多个 importer 的请求（请求 = 所需服务列表 + 所需数量，服务名称为字符串）。
- 收到请求后立即尝试满足；若无法满足，可沿 Connector 方向将请求传递给其他 Broker；仍无法立即满足则保存请求，稍后再尝试。
- 请求多个服务时需全部同时可用才会分配给 station；Broker 不做优化，可能出现理论上可分配却实际未分配的情况。

## 通用说明

- 属性名（如 `FailServices`、`Services` 中的服务名）不区分大小写，可用 `~=` 运算符进行大小写不敏感比较（见 Relational Operators）。
- 手动输入 `OrderCtrl`/`ReleaseCtrl` 后点击 Apply/OK 时，Plant Simulation 会自动检查 Method 参数是否正确；空方法会自动重排格式，此检查无法关闭。
