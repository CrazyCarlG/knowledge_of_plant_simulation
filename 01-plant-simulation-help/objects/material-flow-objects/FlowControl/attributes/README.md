# FlowControl 属性（Attributes）总结

本目录包含 Plant Simulation 中 **FlowControl**（物料流控制器）对象的属性文档：

- `attributes.md` —— FlowControl 属性的结构化 Markdown 文档
- `attributes.txtx` —— Plant Simulation 帮助系统的原始文本导出

本 README 汇总了本目录的 `attributes.md` 内容，并一并概括 FlowControl 对象其他子目录（general、methods、read-only-attributes）中 README 所覆盖的内容，便于快速查阅整个对象。

---

## 1. 对象概述

FlowControl **不加工 MU**，只负责在其后继对象之间分配 MU，或在多个前驱对象之间合并物料流。

- 将 FlowControl 插入至少两个其他对象之间，以控制这些对象之间的物料流。
- 可以将多个 FlowControl 组合使用；前驱和后继对象的数量不受限制。
- **不能建模循环**：不得将 FlowControl 与其自身相连，即使通过其他 FlowControl 或 Interface 间接相连也不允许。
- 由于 FlowControl **不能接收（存储）任何 MU**，因此它不具备其他物料流对象所提供的属性与方法。

**添加到模型**：Home 选项卡 → **Manage Class Library > Basic Objects > MaterialFlow > FlowControl**。

---

## 2. 查看属性、方法与只读属性

- 在对话框中不可用的属性会显示为灰色（对应对象某个选项卡（如 **Statistics**）上不可用的对话框项）。
- 要查看对象的全部方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：
  - 在**类库（Class Library）** 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选**类（Class）** 的内容。
  - 按 **F8** 键，或在插入实例的 Frame 的 Home 功能区选项卡上点击 **Show Attributes and Methods**，可查看所选**实例（Instance）** 的内容。
- 查询只读属性值的示例：

```simtalk
print MyFlowControl.UUID
```

---

## 3. 属性设置与读取

可通过对话框中的复选框、文本框、下拉列表，或在 SimTalk 中赋值来设置/读取属性值。

```simtalk
flowcontrol.name := "MyFlowControl"      -- 设置属性值
print flowcontrol.DefaultSuccessor        -- 读取属性值
posit := MyStation.Cont.XPos
```

FlowControl 提供：

- 下列属性
- **所有对象的属性（Attributes of All Objects）**

---

## 4. 属性一览

| 属性 | 数据类型 | 适用策略 | 说明 |
| --- | --- | --- | --- |
| `AttributeType` | string | Exit Strategy > MU Attribute | 设置决定 FlowControl 移动 MU 方式的属性数据类型 |
| `DefaultSuccessor` | integer | MU Attribute / MU Name | 表中无匹配时移向的默认后继编号；`0` 不移动 MU，`-1` 显示消息 |
| `EntryBehavior` | string | — | 设置从前驱接收 MU 的策略 |
| `EntryBlocking` | boolean | — | 设置 MU 进入 FlowControl 时是否使用阻塞行为 |
| `EntryDistribution` | time | EntryBehavior = Random | 设置随机数分布 |
| `EntrySelectionMethod` | method | EntryBehavior = Method | 设置入口策略使用的方法对象名称 |
| `EntrySelectionProperty` | string | EntryBehavior = Selection | 设置入口策略的选择准则 |
| `ExitBehavior` | string | — | 设置将 MU 移向后继的策略 |
| `ExitBlocking` | boolean | — | 设置 MU 离开 FlowControl 时是否使用阻塞行为 |
| `ExitDistribution` | randTime | ExitBehavior = Random | 设置随机数分布 |
| `ExitSelectionMethod` | method | ExitBehavior = Method | 设置出口策略使用的方法对象名称 |
| `ExitSelectionProperty` | string | ExitBehavior = Selection | 设置出口策略的选择属性 |

---

## 5. 入口策略（EntryBehavior）

`<Path>.EntryBehavior:string`，可选值：

| 策略 | 说明 |
| --- | --- |
| `Cyclic` | 循环依次从所有前驱接收 MU |
| `Cyclic Sequence` | 按列表中定义的前驱顺序循环接收 |
| `First come, first served` | 按前驱意图退出的先后顺序接收 |
| `Least recently used` | 从最久未提供 MU 的前驱接收 |
| `Method` | 由方法返回值决定前驱（`EntrySelectionMethod`） |
| `Most recently used` | 从上次接收 MU 的前驱接收 |
| `Percentage` | 按百分比分布从前驱接收 |
| `Random` | 按所选分布随机选择前驱（`EntryDistribution`） |
| `Selection` | 根据前驱状态与物料流平衡选择（`EntrySelectionProperty`） |
| `Start at Predecessor 1` | 从 1 号前驱开始找第一个可提供 MU 的前驱 |

- **Blocking**：仅从下一个指定的前驱接收 MU。
- **非 Blocking**：可从任一前驱接收。
- 若某个 MU 可通过不同 Connector 到达 FlowControl，则只能使用 **First come, first served** 入口策略。

**EntrySelectionProperty**（EntryBehavior = Selection）允许值：`"Max. Contents"`、`"Min. Contents"`、`"Max. Proc. Time"`、`"Min. Proc. Time"`、`"Max. Num. Out"`、`"Min. Num. Out"`、`"Max. Rel. Occu."`、`"Min. Rel. Occu."`。

---

## 6. 出口策略（ExitBehavior）

`<Path>.ExitBehavior:string`，可选值：

| 策略 | 说明 |
| --- | --- |
| `Assignment` | 不决定后继，在 MU 移向唯一后继时调用方法修改其属性值 |
| `Cyclic` | 循环依次将 MU 移向所有后继 |
| `Cyclic Sequence` | 按列表中定义的后继顺序循环分配 |
| `Least recently used` | 移向等待 MU 最久的后继 |
| `Method` | 由方法返回值决定后继编号（`ExitSelectionMethod`） |
| `Most recently used` | 移向等待 MU 最短的后继 |
| `MU Attribute` | 根据 MU 属性值查表决定后继（`AttributeType`） |
| `MU Name` | 根据 MU 名称查表决定后继 |
| `Percentage` | 按百分比分布分配 |
| `Random` | 按所选分布随机选择后继（`ExitDistribution`） |
| `Selection` | 按后继的某种属性选择（`ExitSelectionProperty`） |
| `Start at Successor 1` | 从 1 号后继开始找第一个可接收的后继 |
| `To all Successors` | 复制进入的 MU，为每个后继各移动一份副本 |

- **Blocking**：仅在期望的后继可接收时移出 MU，否则阻塞。
- **非 Blocking**：任一后继可接收即可移出 MU。
- `Method` 策略的注意：方法中不能移动/删除 MU，且不能使用 `wait`、`waituntil`、`stopuntil` 指令。

**ExitSelectionProperty**（ExitBehavior = Selection）允许值：`"Max. Contents"`、`"Min. Contents"`、`"Max. Rel. Occu."`、`"Min. Rel. Occu."`、`"Max. Num. In"`、`"Min. Num. In"`、`"Max. Proc. Time"`、`"Min. Proc. Time"`、`"Max. Set-up Time"`、`"Min. Set-up Time"`。

---

## 7. 方法（Methods）

FlowControl 提供下列方法，以及所有对象通用的方法（Methods of All Objects）。

| 方法 | 语法 | 用途 |
| --- | --- | --- |
| `getAttributeList` | `<Path>.getAttributeList(AttributeList:table)` | 获取 **Exit Strategy > MU Attribute** 的属性值并写入列表 |
| `getEntryList` | `<Path>.getEntryList(EntryList:any) → boolean` | 获取 **Entry Strategy > Percentage / Cyclic Sequence** 的入口列表 |
| `getExitList` | `<Path>.getExitList(ExitList:any) → boolean` | 获取 **Exit Strategy > Percentage / Cyclic Sequence** 的出口列表 |
| `setAttributeList` | `<Path>.setAttributeList(AttributeList:table)` | 设置 **Exit Strategy > MU Attribute / MU Name** 的属性列表 |
| `setEntryList` | `<Path>.setEntryList(EntryList:any)` | 设置 **Entry Strategy > Percentage / Cyclic Sequence** 的入口列表 |
| `setExitList` | `<Path>.setExitList(ExitList:any)` | 设置 **Exit Strategy > Percentage / Cyclic Sequence** 的出口列表 |

---

## 8. 只读属性（Read-only Attributes）

FlowControl 提供所有对象通用的只读属性（Read-only Attributes of All Objects）。只读属性的值可以查询但不能设置，因为 Plant Simulation 会在查询的时间点计算其值。

```simtalk
print MyFlowControl.UUID
```

---

## 9. 相关对象：Cycle

**Cycle** 对象用于同步零件在工位之间的传递（平衡线）。

- 仅当平衡线上所有工位都完成加工、且没有工位处于失败/暂停/计划外状态时，才将零件移到下一个工位；平衡线的后继也必须就绪。
- 通过输入 **First Station** 与 **Last Station** 名称定义平衡线，两者之间相连的所有工位构成平衡线，每个工位只能有一个前驱和一个后继。
- 目前只有 `Station` 与 `AssemblyStation` 可作为平衡线的组成部分；`AssemblyStation` 须完成装配后 Cycle 才继续平衡。
- 只有 Cycle 的最后一个工位会调用 **Front-triggered Exit Control**（其他工位的 Destination 已确定），应改用 **Rear-triggered Exit Control**。
- Cycle 中的工位不调用 **Pull Control**。
- 可插入多个 Cycle 对象，它们彼此独立；每个工位只能分配给一个 Cycle 对象。

---

## 10. 其他目录说明

- `general/` —— FlowControl 通用说明（对象简介、对话框、入口/出口策略等）
- `methods/` —— FlowControl 方法文档
- `read-only-attributes/` —— FlowControl 只读属性说明

---

*11-2610 Plant Simulation Help*
*Unpublished work. © 2026 Siemens*
