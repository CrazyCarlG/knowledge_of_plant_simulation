# FluidDrain — Read-Only Attributes

本目录汇总 FluidDrain（流体排放/排水对象）的**只读属性**（read-only attributes）。

只读属性可以查询、但不可设置，其值由 Plant Simulation 在查询时刻实时计算。大多数只读属性对应对象选项卡上不可编辑的对话框项（例如 **Statistics** 选项卡）。此外，FluidDrain 还提供 `_Read-Only Attributes of the Fluid Objects`（流体对象的只读属性）。

可通过 **Show Attributes and Methods** 窗口查看全部方法、只读属性与属性：
- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的成员；
- 在插入实例的 Frame 中按 **F8** 或点击 Home 选项卡的 **Show Attributes and Methods**，查看所选实例的成员。

查询只读属性示例：`print FluidDrain.StatMaxFlowRate`

---

## 成员清单

| 名称 | 类型 | 返回值类型 | 说明 |
| --- | --- | --- | --- |
| `typeStatistics` | Method | — | 将 FluidDrain 的 Detailed Statistics Table 写入指定表格 |
| `StatMaxFlowRate` | Read-only attribute | `real` | 流入 FluidDrain 的最大流量（升/秒） |
| `StatThroughput` | Read-only attribute | `real` | FluidDrain 从工厂排出的物料总量（升） |
| `StatThroughputPerDay` | Read-only attribute | `real` | FluidDrain 可用期间一天内的排放量（升），等于每小时吞吐量 × 24 |
| `StatThroughputPerHour` | Read-only attribute | `real` | FluidDrain 可用期间一小时内从工厂排出的物料量（升） |

---

## 详细说明

### `typeStatistics(TypeStatisticsTable:table)` — Method

将 `<Path>` 所指定 FluidDrain 的 **Detailed Statistics Table** 写入名为 `TypeStatisticsTable` 的表格。表格包含：

| 列名 | 描述 |
| --- | --- |
| Material | FluidDrain 从工厂排出的物料名称 |
| Throughput | FluidDrain 从工厂排出的物料总量 |

示例：

```simtalk
var MyFluidDrainStatisticsTable: table
MyFluidDrain.typeStatistics(MyFluidDrainStatisticsTable)
```

### `StatMaxFlowRate` — Read-only attribute

返回 FluidDrain 的最大流量，数据类型 `real`，单位为**升/秒**（每秒流入 FluidDrain 的物料升数）。

```simtalk
print MyFluidDrain.StatMaxFlowRate
```

### `StatThroughput` — Read-only attribute

返回 FluidDrain 从工厂排出的物料总量，数据类型 `real`，单位为**升**。

```simtalk
print MyFluidDrain.StatThroughput
```

### `StatThroughputPerDay` — Read-only attribute

返回 FluidDrain 可用期间一天内的排放量，数据类型 `real`，单位为**升**；其值为每小时吞吐量乘以 24。

```simtalk
print MyFluidDrain.StatThroughputPerDay
```

### `StatThroughputPerHour` — Read-only attribute

返回 FluidDrain 可用期间一小时内从工厂排出的物料量，数据类型 `real`，单位为**升**。

```simtalk
print MyFluidDrain.StatThroughputPerHour
```

---

> 参见：`Tab Statistics [FluidDrain]`、`Detailed Statistics Table [FluidDrain]`、`_Read-Only Attributes of the Fluid Objects`。
