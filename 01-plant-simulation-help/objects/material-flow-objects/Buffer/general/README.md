# Buffer（对象）— General 总结

本目录存放 **Buffer**（缓冲区）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. Buffer 对象概述

在两个生产组件之间插入一个 **Buffer**，用于：

- **临时存放工件（MU）**——当其后序组件发生故障时，避免前序机器停止生产。
- **继续传递工件**——当前序组件停止工作时，避免生产流程陷于停顿。

将 Buffer 的容量设置得足够大以覆盖所有故障，可使相关组件之间实现完全解耦。Buffer 不仅能渡过故障时间，还可作为**补偿站**，吸收波动的运输时间与操作时间（这些波动会导致机器或组件前形成队列）。但即便如此，它也不能始终避免物料流中断。

由于 Buffer **没有独立的位置（place）**，因此无需将加工时间（工件在其中停留的时间）拆分为若干小步骤；取而代之的是，选择工件**离开 Buffer 的顺序**。

## 2. Buffer Type（缓冲区类型）

`Buffer Type [下拉列表]` 设置工件的离开行为：

- **Queue（队列）**——工件按进入顺序离开（先进先出，FIFO）。
- **Stack（堆栈）**——最后进入的工件最先离开（后进先出，LIFO）。

> **注意：** 每个 MU 在 Buffer 中至少停留 **Dwell Time（驻留时间）** 这么久。对于 `Stack`，只有当在其之后进入 Buffer 的所有工件都已离开（即该 MU 位于堆栈最顶端）时，它才能离开。

将鼠标悬停在 Buffer 上可显示包含其信息的工具提示。

## 3. Tips（提示）

- 要更改图形长度和锚点，点击编辑功能区标签页的 **Show Manipulators**，或按 `M`。
- Buffer 非常适合建模**大容量、要求高性能**的缓冲区；如需更高级功能，请改用 **PlaceBuffer**。
- 可在 Buffer 窗口通过 **Exchange Graphics** 选择替代图形。
- Plant Simulation 会以**堆叠**方式显示 Buffer 中的 MU。

## 4. 添加到仿真模型

Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > Buffer`。

## 5. Buffer 对话框

双击 Buffer 图标打开对话框。

- **Edit Simulation Properties**：编辑仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties**（3D）：点击仿真属性对话框左下角的 **Edit 3D Properties**，或选中对象后按**空格键**。

## 6. 选项卡 Attributes（属性）

### Capacity（容量，文本框）

输入 Buffer 可同时容纳的 MU 数量。

- 输入 `-1` 表示**无限容量**。
- 容量**并非**以矩阵方式实现——无法访问单个位置。
- 只有当新值**大于或等于** Buffer 中当前实际 MU 数量时，才能减小容量。

### Buffer Type（缓冲区类型，下拉列表）

设置 MU 的离开行为（见上文 **Buffer Type**）。

## 7. 选项卡 Times（时间）

按 *Tab Times* 的说明定义时间：从下拉列表选择分布类型并输入所需值，Plant Simulation 会在选项卡上边缘显示参数；也可选择恒定时间（**Const**）。可用方法 `setTypeAndAttr` 设置分布类型及完整的参数集。

### Dwell Time（驻留时间 [Buffer]）

输入 MU 在 Buffer 中停留的时间。

- 对于 Buffer，只能指定**恒定**的 Dwell Time。
- 统计中把 Dwell Time 计为**等待时间（waiting time）**，而非加工时间。
- Dwell Time **不会**因故障或暂停而延长。
- 每个 MU 至少停留 Dwell Time；对于 `Stack`，只有当 MU 位于堆栈最顶端时才能离开。

## 8. 选项卡 Failures（故障）

按 *Tab Failures* 的说明定义故障。

## 9. 选项卡 Controls（控制）

提供修改对象内置行为的控制项。

- **选择已有 Method**：点击省略号按钮，在 *Select Object [for controls]* 中导航并点击 OK；或将 Method 从 Frame 拖入文本框。
- **创建作为对象方法的控制**：输入有意义的名字并选择 **Create Control**（插入 `self.<你输入的名字>`，如 `self.A1Ctrl`）；或在空文本框上选择 **Create Control**（插入 `self.On<内置控制名>`，如 `self.OnEntrance`）。在打开的 Method 中编写源代码。
- **之后编辑**：按 `F2`、按住 Shift 双击文本框、在上下文菜单中选择 **Open Object**，或使用 **User-defined** 选项卡。
- **删除**：删除用户自定义属性（仅从文本框删除名字不会删除该属性）。

参见：Entrance Control、Exit Control、Pull Control、Shift Calendar。

## 10. 选项卡 Exit（出口）

选择对象把 MU 移动到哪个后继。参见 *Blocking [exit strategy]* 与 *Strategy [material flow objects]*。

## 11. 选项卡 Statistics（统计）

统计按 *Tab Statistics* 的说明。查看固定资源（Stationary Resources）的**资源统计**：在对象对话框选择 **View > Show Statistics Report**，右键 Frame 选择 **Show Statistics Report**，或按 `F6`。

## 12. 选项卡 Energy（能源）

在 *Tab Energy* 上选择对象的能源设置。

## 13. 选项卡 Costs（成本）

在 *Tab Costs* 上选择成本设置。Buffer 缓冲工件期间，成本由**投资成本**与**运营成本**之和累积：

- 投资成本仅在**折旧期（Depreciation Period）**内累积。
- 成本按容量比例，作为**应计成本（accrued costs）**分配到工件上。
- 若 Buffer 为空，成本作为**一般成本（general costs）**保留在 Buffer 上。

## 14. 选项卡 User-defined（用户自定义）

按 *Tab User-defined* 的说明定义自定义属性。

## 15. 菜单

- **Navigate 菜单**：命令见 *Navigate Menu* 说明。
- **View 菜单**：提供 `Refresh`、`Show Statistics Report`、`Show Attributes and Methods`、`Forward Blocking List`、`Exit Blocking List`、`Associated Lockout Zones`、`Associated Shift Calendar`、`Contents`。
- **Tools 菜单**：命令见 *Tools Menu* 说明。
- **Tabs 菜单**：显示/隐藏所选物料流对象的各个选项卡（隐藏不需要的选项卡可更快打开对话框）。点击 OK、关闭并重新打开后生效；**Inherit** 切换显示/隐藏选项卡的继承。
- **Help 菜单**：命令见 *Help Menu* 说明。

## 16. Buffer 的方法

Buffer 提供：

- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

查看方式：打开 **Show Attributes and Methods** 窗口查看全部方法、只读属性和属性：

- 在类库（Class Library）上下文菜单中选择 **Show Attributes and Methods**（查看所选类），或
- 按 `F8` / 点击包含该实例的 Frame 的 Home 功能区标签页上的 **Show Attributes and Methods**。

## 17. SimTalk 参考

- `Capacity`
- `BufferType`
- `ProcTime`（material flow objects）
- `setTypeAndAttr`
- `putAttributeNamesIntoTable`

## 18. 参见

- Buffer Parts within the Production Line
- Use a Buffer between Processing Stations
- Properties of the DataQueue
- Properties of the DataStack
- Check the Fill Level of the Buffers in the Plant
- Simulate the Accrued Costs of the Machines
- CostAnalyzer > How the CostAnalyzer Assigns Costs to Part Types
- CostAnalyzer > Costs Shown in the Costs Report
- Resource Statistics, Resource Type

## 19. Videos（视频）

- https://youtu.be/PgT4wkT2Xj8?si=Udlvoq8KcAI9GxQw&t=18
- https://youtu.be/PgT4wkT2Xj8?si=d4Sx9mjGHp_Pl0wB&t=98

## 目录说明

- `general.md`：Buffer 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
