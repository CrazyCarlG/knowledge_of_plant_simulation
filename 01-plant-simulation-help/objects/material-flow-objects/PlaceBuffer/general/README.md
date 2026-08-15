# PlaceBuffer（对象）— General 总结

本目录存放 **PlaceBuffer**（缓冲区工位）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. PlaceBuffer 对象概述

**PlaceBuffer** 在一排**前后依次排列**的若干缓冲位置（place）上加工工件（MU）。它**不属于**工具箱（Toolbox）默认提供的内置对象，需自行添加。

- MU 在这些位置上**从前往后逐位推进**，只有经过**最后一个位置**之后才能离开。这样每个位置都可以被单独调用和访问。
- PlaceBuffer **循环地**把工件向下一个后继移动。

### 备注

- PlaceBuffer **默认不显示**在新模型中，必须手动添加。
- **若未勾选 Sequentially Indexing（顺序索引）**：
  - 只能为 PlaceBuffer **整体**设置加工时间（Processing Time），不能为单个位置设置。
  - 加工时间被**平均分配**到所有位置（例如：加工时间 1 分钟、容量 3 个位置 → 每个位置 20 秒）。
  - 工件可直接移动到某个空闲位置；工件经过该位置及其后所有位置后即可离开。
  - 若工件是在某个空闲位置上被创建的，则它**不必经过该位置**，可直接移动到下一个位置或对象。
- **若勾选了 Sequentially Indexing**：
  - 加工时间表示把工件移动到**下一个位置**所需的时间。
  - 容量为 4 时，工件至少需要经过**三倍的加工时间**才能离开（三次移动过程）。
  - 该时间可通过等待时间进一步延长。

### 累积（Accumulating）行为

当第一个工件无法离开时：

- 勾选 **Accumulating**：出口被阻塞（Blocked）时，MU 会**前后紧挨着**依次移动。
- 取消勾选 **Accumulating**：MU **保持间距**（当最前面的 MU 无法离开时，其后所有 MU 都停止，且不再有新的 MU 进入）。

### 图形（Graphics）

- 默认图形是一张 `2 × 1 × 1 m` 的桌子，其表面最多有四个工件沿 X 方向移动。缩放 PlaceBuffer（通常仅沿 X 方向）会缩放预定义的动画区域，因此通常只需调整**容量（Capacity）**即可。
- 提供两种图形：
  - `Table2x1x1modular.jt`，位于 `jt-graphics` 文件夹（可导入到任意对象）。
  - `PlacebufferModular.s3d`，位于 `s3d-graphics\BuffersAndSorters` 文件夹（可通过更改可独立变换的图形部件来调整桌子尺寸，而不改变部件厚度）。

**设置 Animation Area（动画区域）时注意：**

1. 若动画区域处于激活状态，PlaceBuffer 使用该区域；MU 的索引即为其在 X 方向上的区域索引，Y 方向容量恒为 1。
2. 若存在名为 `Default` 且含多个锚点的 MU 动画路径，MU 索引会被转换为相对位置，MU 在该线上等距分布。
3. 否则，PlaceBuffer 将第一条路径用于第一个 MU，第二条用于第二个 MU，依此类推；若不存在合适路径，但存在仅含单点的 `Default` 路径，则使用该路径。

- 对于需要**高速运行的大容量缓冲区**，请改用 **Buffer** 对象。
- 将鼠标悬停在 PlaceBuffer 上可显示工具提示；点击编辑功能区标签页的 **Show Manipulators**（或按 `M`）可更改图形长度与锚点。

## 2. 添加到仿真模型

Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > PlaceBuffer`。

## 3. PlaceBuffer 对话框

双击 PlaceBuffer 图标打开对话框。

- **Edit Simulation Properties**：在对话框中更改仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties**：点击仿真属性对话框左下角的 **Edit 3D Properties**，或选中对象后按**空格键**；点击 **Show Manipulators** 或按 `M` 操作图形。

## 4. 选项卡 Attributes（属性）

### Capacity（容量，文本框）

输入 PlaceBuffer 的容量，即位置数量。

- 若勾选了 Sequentially Indexing，输入 `-1` 表示**不限位置数**。
- 各个位置通过其**索引**访问。
- 只有当足够多的位置为空时才能减小容量；且只有在 PlaceBuffer 中**没有工件（即完全为空）**时才能更改容量。

### Sequentially Indexing（顺序索引，复选框）

勾选后，仅当**后继位置空闲**时才在某个位置上启动加工时间。

- 在该模式下，加工时间表示把工件移动到后继位置所需的时间（而非在位置上加工的时间）；容量为 4 时，工件至少需经过三倍加工时间才能离开。
- **最后一个位置不消耗时间**：工件一到达最后一个位置，只要后继接受，即可立即离开。
- 若取消勾选，则采用默认行为：只能为整个 PlaceBuffer 设置加工时间，并平均分配到各位置。

### Accumulating（累积，复选框）

- 勾选：出口阻塞时 MU 在 PlaceBuffer 上前后紧挨着累积移动。
- 取消勾选：MU 保持间距（最前面的工件无法离开时，其后所有 MU 停止，且不再有新的 MU 进入）。

## 5. 选项卡 Times（时间）

按 *Tab Times* 的说明定义时间：从下拉列表选择分布类型并输入所需值，也可选择恒定时间（**Const**）。

> **注意：** 只能为 PlaceBuffer 中的工件输入**恒定的加工时间**——不支持统计分布、不按工件类型区分、也不支持公式。可用方法 `setTypeAndAttr` 设置分布类型及完整的参数集。

### Processing Time（加工时间 [PlaceBuffer]）

输入 MU 在 PlaceBuffer 中的加工时间。

- 只能指定**恒定**加工时间（无概率分布、无 MU 类型依赖、无公式）。
- 它更像是一种**驻留时间（Dwelling Time）**而非加工时间，因为工件在此被缓冲后继续前移。
- 若取消勾选 Sequentially Indexing：时间为整个缓冲区设置并平均分配（例如 1 分钟 / 3 个位置 = 每位置 20 秒）。
- 若勾选 Sequentially Indexing：时间用于移动到下一个位置；容量为 4 时，至少需三倍时间才能离开，并可通过等待时间延长。

### Recovery Time / Cycle Time（恢复时间 / 节拍时间 [PlaceBuffer]）

按 *Tab Times* 的说明。

## 6. 选项卡 Failures（故障）

按 *Tab Failures* 的说明定义故障。

## 7. 选项卡 Controls（控制）

提供修改对象内置行为的控制项。

- **选择已有 Method 的路径**：点击省略号按钮，在 "Select Object" 对话框中导航；或将 Method 从 Frame 拖入文本框。
- **创建作为对象方法的控制**：输入有意义的名字并选择 **Create Control**（插入 `self.<你输入的名字>`，如 `self.A1Ctrl`）；或在空文本框中选 **Create Control**（插入 `self.On<内置控制名>`，如 `self.OnEntrance`）。按 `F2` 打开 Method 并编写源代码。
- **之后编辑**：按 `F2`、按住 Shift 双击文本框、在上下文菜单中选择 **Open Object**，或双击 User-defined 选项卡中的 Method。
- **删除**：删除相应的用户自定义属性（仅从文本框删除名字不会删除该属性）。

参见：Entrance Control、Exit Control、Pull Control、Shift Calendar。

## 8. 选项卡 Exit（出口）

选择对象把 MU 移动到哪个后继。参见 *Blocking* 和 *Strategy*。

## 9. 选项卡 Statistics（统计）

按 *Tab Statistics* 的说明。查看 Stationary Resources 的资源统计：对象对话框 `View > Show Statistics Report`，右键 Frame 选择 **Show Statistics Report**，或按 `F6`。

## 10. 选项卡 Energy（能源）

选择对象的能源设置。

## 11. 选项卡 Costs（成本）

选择成本设置。PlaceBuffer 缓冲工件期间，成本由投资成本与运营成本之和累积：

- 投资成本仅在**折旧期（Depreciation Period）**内累积。
- 成本按容量比例，作为**应计成本（accrued costs）**分配到工件上。
- 若 PlaceBuffer 为空，成本作为**一般成本（general costs）**保留在 PlaceBuffer 上。

## 12. 选项卡 User-defined（用户自定义）

按 *Tab User-defined* 的说明定义自定义属性。

## 13. 菜单

- **Navigate 菜单**：命令见 Navigate Menu 说明。
- **View 菜单**：提供 `Refresh`、`Show Statistics Report`、`Show Attributes and Methods`、`Contents`，以及 Forward/Exit Blocking List、Associated Lockout Zones、Associated Shift Calendar。
- **Tools 菜单**：命令见 Tools Menu 说明。
- **Tabs 菜单**：显示/隐藏所选物料流对象的各个选项卡（隐藏不需要的选项卡可更快打开对话框）。点击 OK、关闭并重新打开后生效。菜单在显示的选项卡旁显示对勾；**Inherit** 切换显示/隐藏选项卡的继承。
- **Help 菜单**：命令见 Help Menu 说明。

## 14. PlaceBuffer 的方法

PlaceBuffer 提供：

- 方法 `pe, [X Y]`；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

查看方式：打开 **Show Attributes and Methods**（类库中类的上下文菜单，或实例上按 `F8` / Home 功能区标签页）查看全部方法、只读属性和属性。

## 15. SimTalk / 代码示例

```simtalk
print place.MU(i)
next
// 返回堆栈最顶部的 MU：
Store[1,1].Cont
// 返回位置 1,2 上自顶部数第二个 MU：
Store[1,2].MU(2)
```

相关 SimTalk 项：

- `XDim [SimTalk] - Store`
- `YDim [SimTalk] - Store`
- `getStackHeight [SimTalk] - Store`
- `mu [SimTalk] - PE, Store`
- `Capacity [SimTalk] - PlaceBuffer`
- `SequentiallyIndexing [SimTalk]`
- `Accumulating [SimTalk] - PlaceBuffer`
- `setTypeAndAttr [SimTalk]`
- `ProcTime [SimTalk] - material flow objects`
- `RecoveryTime [SimTalk] - material flow objects`
- `CycleTime [SimTalk]`

## 16. 参见

- Z-Dimension [Store]
- Stack Parts in the Store
- Unload Stacked Parts
- Processing Time [PlaceBuffer]
- Capacity [text box] - PlaceBuffer
- Sequentially Indexing [check box]
- Recovery Time [general description]
- Recovery Time Starts
- Cycle Time [general description]
- Resource Statistics [check box]
- Resource Type
- Simulate the Accrued Costs of the Machines
- CostAnalyzer > How the CostAnalyzer Assigns Costs to Part Types
- CostAnalyzer > Costs Shown in the Costs Report

## 目录说明

- `general.md`：PlaceBuffer 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
