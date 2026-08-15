# FlowControl — General（物料流控制对象概述）

本目录包含 FlowControl 对象的通用说明文档：

- `general.md` —— FlowControl 的完整帮助文档（Markdown 版）
- `general.txtx` —— 同一内容的文本版（含页码信息）

以下是该目录内容的汇总。

---

## 1. 对象简介

FlowControl（物料流控制器）**不加工 MU**，只负责在其后续对象之间分配 MU，或在多个前驱对象之间合并物料流。

- 将 FlowControl 插入至少两个其他对象之间，以控制这些对象之间的物料流。
- 可以将多个 FlowControl 组合使用；前驱和后继对象的数量不受限制。
- **不能建模循环**：不得将 FlowControl 与其自身相连，即使通过其他 FlowControl 或 Interface 间接相连也不允许。
- 将鼠标悬停在对象上可显示工具提示；按 `M` 键或点击 Edit 选项卡的 **Show Manipulators** 可调整图形长度和锚点。

**添加到模型**：Home 选项卡 → **Manage Class Library > Basic Objects > MaterialFlow > FlowControl**。

---

## 2. 对话框（Dialog Box）

双击 FlowControl 图标打开对话框，可编辑：

- **仿真属性（Edit Simulation Properties）**：共享属性见 “Dialog Items of the Objects”。
- **动画/3D 属性（Edit 3D Properties）**：点击对话框左下角 **Edit 3D Properties** 按钮，或选中对象后按空格键。

---

## 3. Exit 选项卡（出口策略）

从 **Strategy** 下拉列表选择分配 MU 的策略，部分策略还可选择 **Blocking（阻塞）** 或非阻塞。

- **SimTalk 属性**：`ExitBehavior`、`ExitBlocking`

### 出口策略一览

| 策略 | 说明 |
|---|---|
| **Cyclic** | 循环依次将 MU 移向所有后继；到末尾后从头开始。阻塞时若目标后继不能接收则阻塞 MU。 |
| **Cyclic Sequence** | 按列表中定义的后继顺序循环分配（`setExitList`/`getExitList`）。 |
| **Least Recently Used** | 移向等待 MU 最久的后继。 |
| **Method** | 由方法返回值决定后继编号（`ExitSelectionMethod`）；方法中不能移动/删除 MU，不能用 `wait`/`waituntil`/`stopuntil`。 |
| **Most Recently Used** | 只要当前后继能接收，就一直移向同一后继。 |
| **MU Attribute** | 根据 MU 属性值查表决定后继（`setAttributeList`/`getAttributeList`、`AttributeType`）。 |
| **MU Name** | 根据 MU 名称查表决定后继。 |
| **Percentage** | 按百分比分布分配，优先移向“期望值与实际值差距最大”的后继（`setExitList`/`getExitList`）。 |
| **Random** | 按所选概率分布随机选择后继（`ExitDistribution`）。 |
| **Selection** | 按后继的某种属性选择（`ExitSelectionProperty`）。 |
| **Start at Successor 1** | 从 1 号后继开始找第一个可接收的后继。 |
| **To All Successors** | 复制进入的 MU，为每个后继各移动一份副本；始终阻塞，直到所有后继都就绪。 |
| **Assignment** | 不决定后继（始终移向 1 号后继），而是在 MU 移向唯一后继时调用方法修改其属性值。 |

### Selection 策略的属性（Property）

| Property | FlowControl 将 MU 移向 |
|---|---|
| Max. contents | 当前包含 MU 数量最多的后继 |
| Min. contents | 当前包含 MU 数量最少的后继 |
| Max. proc. time | 该 MU 加工时间最长的后继 |
| Min. proc. time | 该 MU 加工时间最短的后继 |
| Max. Set-up time | 该 MU 换装时间最长的后继 |
| Min. Set-up time | 该 MU 换装时间最短的后继 |
| Max. num. in | 接收 MU 最多的后继（需启用资源统计） |
| Min. num. in | 接收 MU 最少的后继（需启用资源统计） |
| Max. rel. occu. | 相对占用率最高的后继（需启用资源统计） |
| Min. rel. occu. | 相对占用率最低的后继（需启用资源统计） |

### 出口策略通用说明

- **Blocking**：仅在期望的后继可接收时移出 MU，否则阻塞。
- **非 Blocking**：任一后继可接收即可移出 MU。
- **Default Successor**（MU Attribute / MU Name 策略）：当表中无匹配时移向的默认后继；填 `0` 表示不移动该 MU，填负数表示同时显示消息。
- **Next Aimed Successor**：显示出口策略下一个要服务的后继（非阻塞时可能与实际移向的后继不同）。

---

## 4. Entry 选项卡（入口策略）

从 **Strategy** 下拉列表选择从前驱接收 MU 的策略，部分策略可选择阻塞/非阻塞。

- **SimTalk 属性**：`EntryBehavior`、`EntryBlocking`
- **重要限制**：若某个 MU 可通过不同 Connector 到达 FlowControl，则只能使用 **First come, first served** 入口策略。

### 入口策略一览

| 策略 | 说明 |
|---|---|
| **Cyclic** | 循环依次从所有前驱接收 MU（`EntryBehavior`/`EntryBlocking`）。 |
| **Cyclic Sequence** | 按列表中定义的前驱顺序循环接收（`setEntryList`/`getEntryList`）。 |
| **First come, first served** | 按前驱意图退出的先后顺序接收。 |
| **Least Recently Used** | 从最久未提供 MU 的前驱接收。 |
| **Method** | 由方法返回值决定前驱（`EntrySelectionMethod`）；阻塞时方法无参数，非阻塞时方法带一个整数参数。 |
| **Most Recently Used** | 从上次接收 MU 的前驱接收。 |
| **Percentage** | 按百分比分布从前驱接收（`setEntryList`/`getEntryList`）。 |
| **Random** | 按所选分布随机选择前驱（`EntryDistribution`）。 |
| **Selection** | 根据前驱的状态和物料流平衡选择（`EntrySelectionProperty`）。 |
| **Start at Predecessor 1** | 从 1 号前驱开始找第一个可提供 MU 的前驱。 |

### Selection 策略的属性（Property）

| Property | FlowControl 从哪个前驱接收 MU |
|---|---|
| Max. contents | 包含 MU 数量最多的前驱 |
| Min. contents | 包含 MU 数量最少的前驱 |
| Max. proc. time | 加工时间最长的前驱 |
| Min. proc. time | 加工时间最短的前驱 |
| Max. num. out | 退出 MU 最多的前驱（需启用资源统计） |
| Min. num. out | 退出 MU 最少的前驱（需启用资源统计） |
| Max. rel. occu. | 相对占用率最高的前驱（需启用资源统计） |
| Min. rel. occu. | 相对占用率最低的前驱（需启用资源统计） |

### 入口策略通用说明

- **Blocking**：仅从下一个指定的前驱接收 MU；其他前驱上等待的 MU 不被接收。
- **非 Blocking**：可从任一前驱接收；入口策略仅在 FlowControl 的阻塞列表中有多个 MU、且因后继就绪而解除阻塞时生效。
- **Next Aimed Predecessor**：显示入口策略下一个要服务的前驱（非阻塞时可能与实际接收的前驱不同）。

---

## 5. 其他选项卡与菜单

- **Tab User-defined**：定义自定义属性。
- **Navigate Menu / Tools Menu / Help Menu**：见对应通用说明。
- **View Menu**：提供 `Refresh` 与 `Show Attributes and Methods` 命令（SimTalk：`updateDialog`）。

---

## 6. 对象方法

FlowControl 提供：

- 目录左侧列出的方法
- 所有对象共有的方法（Methods of All Objects）

由于 FlowControl 本身不接收（存储）MU，因此不具备其他物料流对象所拥有的部分方法。可通过 **Show Attributes and Methods** 窗口查看该对象的所有方法、只读属性和属性。
