# Track（轨道）— 方法（Methods）汇总说明

本目录 `methods` 汇总了 Track（轨道）物料流对象的方法参考文档。Track 是 Plant Simulation 中的一种长度导向（length-oriented）物料流对象，与 Transporter（运输小车）配合使用，用于建模 AGV（自动导引车）系统。

本文件是本目录下 `methods.md` 的内容总结。该目录下无子文件夹。

---

## 1. 方法总览

Track 提供以下方法，并继承 Curved Objects（弯曲对象）、Material Flow Objects（物料流对象）以及 All Objects（所有对象）的方法：

| 方法 | 说明 |
| --- | --- |
| **getRouteLength** | 返回从 Track 到目标的最短路径及其长度。 |

此外，可通过窗口 **Show Attributes and Methods** 查看对象的所有方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **Class** 的方法、只读属性和属性。
- 按 **F8** 键，或在插入实例的 Frame 的 Home 功能区选项卡上点击 **Show Attributes and Methods**，可查看所选 **Instance** 的方法、只读属性和属性。

---

## 2. 语法行约定

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所应用对象的路径。
- 方法签名（参数标识符与数据类型）在括号中列出，例如 `(Parameter:string)` 表示一个 `string` 类型参数。除常量值外，也可使用所需类型的变量或返回所需类型的方法。
- **注意**：务必为括号内的表达式输入括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。
- 可选参数用方括号 `[...]` 表示，例如 `[,Parameter:boolean]` 表示可输入也可不输入的布尔参数。
- 带默认值的参数在参数后以 `:= default` 表示，例如 `:= false`。
- 有返回值的方法在箭头 `->` 后显示其数据类型，例如 `→ boolean`。

---

## 3. getRouteLength [SimTalk] - Track

返回从 `<Path>` 指定的 Track 到目标的最短路径，并返回该路径的长度。

### 备注

- 目标既可以是能通过 Connector 直接到达的物料流对象，也可以是键入到传感器（sensor）中的目的地。

> **注意**：由于该路径是为 Transporters 设计的，Plant Simulation 在计算路径时只考虑 Track 和 TwoLaneTrack 类型的对象。

### 类型

方法（Method）

### 语法

```
<Path>.getRouteLength(Target:path[, Backwards:boolean, Position:length,
ObjectsAlongRoute:table, RouteWeightingAttribute:string]) → length
```

### 参数

| 参数 | 数据类型 | 是否可选 | 说明 |
| --- | --- | --- | --- |
| **Target** | `object` | 否 | 指定目标。 |
| **Backwards** | `boolean` | 可选 | 指定搜索路径的方向。`true` 表示后退，`false` 表示前进（默认）。 |
| **Position** | `length` | 可选 | 指定开始搜索的 Track 位置。若未指定，前向搜索从 Track 末端开始，后向搜索从 Track 起点开始。当目标是位于 Track 自身上的传感器时尤其重要。 |
| **ObjectsAlongRoute** | `table` | 可选 | 将沿路径的对象写入指定表格。 |
| **RouteWeightingAttribute** | `string` | 可选 | 设置自动路由中用于路径加权的属性名称。若未传入该参数，Plant Simulation 不对路径长度进行加权。 |

### 返回值

- 数据类型为 `length`。
- 若未找到路径，返回 `-1`。

### 示例

```simtalk
print Track5.getRouteLength(Track26)
```

### 相关参考

- Destination [SimTalk] - sensors
- RouteWeightingAttr [SimTalk] - Transporter

---

## 4. 只读属性（Read-Only Attributes）

Track 提供以下只读属性，并继承 All Objects（所有对象）与 Material Flow Objects（物料流对象）的只读属性：

| 只读属性 | 说明 |
| --- | --- |
| **OccupiedLength** | 返回 Track 的总 Length 中被其上所有 Transporter 占用的部分。 |

只读属性只能查询、不能设置，因为 Plant Simulation 在查询时计算其值。大多数情况下，只读属性对应对象某个选项卡（例如 Statistics）上不可用的对话框项。

---

*Source: Plant Simulation Help 11-2460 — 11-2463. Unpublished work. © 2026 Siemens.*
