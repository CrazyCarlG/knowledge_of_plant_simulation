# Drain Methods（Drain 对象方法）

本目录汇总了 Plant Simulation 中 **Drain（排水/移除）** 对象提供的方法（methods）与只读属性，内容来源于 `methods.md`，并参考了同级 `general/README.md` 中对 Drain 对象的概述。

## 目录内容

- `methods.md` — Drain 方法及只读属性的说明文档（本总结的源文件）。
- `methods.txtx` — 相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

## Drain 对象概述

**Drain** 用于在工件（MU）加工完成后将其从工厂中移除，通常代表工厂的发货部门。

- Drain 的内置属性与 **Station** 相同；与 Station 一样，它只有一个加工位置。
- 与 Station 的唯一区别在于：Drain 会将加工完成的工件**从工厂中移除**，而不是将其移动到后续物料流对象。
- Drain 本质上是 **Source** 的对应物（Source 生产工件，Drain 移除工件）。
- 添加到模型：Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > Drain`。

## 方法概述

Drain 提供：

- 本目录（`methods.md`）中所列的方法。
- Station 的方法（Methods of the Station）。
- Material Flow Objects（物流对象）的方法。
- All Objects（所有对象）的方法。

要查看对象的全部方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性与属性。
- 按 **F8** 键，或点击插入实例的 Frame 中 Home 功能区标签页的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性与属性。

## 语法行说明（Syntax Line）

方法的语法行格式示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所作用对象的路径。
- `(Parameter:string)`：参数签名，包含参数标识符与数据类型；除常量外，也可使用所需类型的变量或返回所需类型的方法。
- `[,Parameter:boolean]`：方括号内为可选参数。
- `:= false`：参数的默认值。
- `→ boolean`：箭头后为返回值的数据类型。

> **注意**：请务必为嵌套在括号内的表达式输入括号 `(…)`，否则可能导致意外结果并打开 Debugger。

## 方法列表

| 方法 | 语法 | 返回类型 | 说明 |
| --- | --- | --- | --- |
| `typeStatistics` | `<Path>.typeStatistics([TypeStatisticsTable:table]) → boolean` | `boolean` | 返回 Drain 的详细统计表（Detailed Statistics Table）并写入一个表。 |
| `typeStatisticsCumulated` | `<Path>.typeStatisticsCumulated([CumulatedTypeStatisticsTable:table]) → boolean` | `boolean` | 返回包含该对象从工厂移除的 MU 类型的累计统计表。 |

### typeStatistics [SimTalk]

返回由 `<Path>` 指定的 Drain 的详细统计表（Detailed Statistics Table），并将其写入一个表。

- **备注**：表格中的 **Read-only Attribute** 列列出了所有工件类型对应统计值的只读属性。
- **类型**：Method
- **参数**：`TypeStatisticsTable`（类型 `table`，可选）— 指定表格名称。
- **返回值**：数据类型为 `boolean`
  - `true`：统计收集已激活。
  - `false`：统计收集未激活，此时表格保持不变。
  - 若未指定可选参数，则返回包含统计数据的表格（统计收集已激活时）。
  - 统计收集未激活时返回 `void`。
- **示例**

```
MyDrain.typeStatistics(MyDrainStatisticsTable)
// 将统计值写入名为 MyDrainStatisticsTable 的表格。
// 统计收集已激活时返回 true，未激活时返回 false（表格保持不变）。
```

```
MyDrain.typeStatistics
// 将统计值写入一个表格。
// 统计收集已激活时返回统计表格，统计被清除时返回 void。
```

- **参见**：`typeStatisticsCumulated [SimTalk]`、`TypeStatOn [SimTalk]`、Detailed Statistics Table [Drain]、Statistics report, Part Types Which the Drain Removed From the Plant。

### typeStatisticsCumulated [SimTalk]

返回累计统计表，其中包含由 `<Path>` 指定的对象从工厂中移除的 MU 类型。

- **类型**：Method
- **参数**：`CumulatedTypeStatisticsTable`（类型 `table`，可选）— 指定表格名称。表格列与 `typeStatistics` 填充的表格相同，但 **Type** 列保持为空。
- **返回值**：数据类型为 `boolean`
  - `true`：统计收集已激活。
  - `false`：统计收集未激活，此时表格保持不变。
  - 若未指定可选参数，则返回包含统计数据的表格（统计收集已激活时）。
  - 统计收集未激活时返回 `void`。
- **示例**

```
MyDrain.typeStatisticsCumulated(myCumulatedDrainStatistics)
// 将统计值写入名为 MyDrainStatisticsTable 的表格。
// 统计收集已激活时返回 true，未激活时返回 false（表格保持不变）。
```

```
MyDrain.typeStatisticsCumulated
// 将统计值写入一个表格。
// 统计收集已激活时返回统计表格，未激活时返回 void。
```

- **参见**：`typeStatistics [SimTalk] - Drain`、`TypeStatOn [SimTalk]`。

## 只读属性（Read-Only Attributes）

Drain 提供：

- 本目录（`methods.md`）中列出的只读属性。
- All Objects 的只读属性（Read-Only Attributes of All Objects）。
- Material Flow Objects 的只读属性（Read-Only Attributes of the Material Flow Objects）。

只读属性的值由 Plant Simulation 在查询时刻计算，只能读取、不能设置；多数只读属性对应对象某个标签页（如 **Statistics**）上不可用的对话框项。查询示例：

```
print Drain.StatAvgExitInterval
```

> 提示：Drain 的统计只读属性（如 `StatAvgLifeSpan`、`StatAvgExitInterval`、`StatDeleted`、`StatThroughputPerMinute`、`StatThroughputPerHour` 等）与其 Type Statistics 标签页及 Detailed Statistics Table 的统计项相对应，详见 `general/README.md` 中的“选项卡 Type Statistics”与“Detailed Statistics Table”部分。

## 相关文档

- `../general/README.md` — Drain 对象概述、对话框与各选项卡说明。
- `../attributes/` — Drain 的属性文档。
- `../read-only-attributes/` — Drain 的只读属性文档。
