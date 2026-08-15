# Converter — General（概述）

本目录存放 **Converter**（转换器）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. Converter 对象概述

**Converter** 用于建模物料搬运设备。当 MU（可移动单元）移动到 Converter 上时，它要么沿传送方向**直通**，要么由提升机构**抬升**到横向移动的传送层上，再被**横向向左或向右**传送。

- 若部件从 **side 1 或 3** 进入，*直通（straight）* 意味着部件保持其传送方向，并从对侧离开。
- 当 Converter 的插入方向为从左到右（即从上到下）时，横向移动的插入方向为 **从 side 3 到 side 1**。
- 可用方法 `getObjectOfSide` [SimTalk] 查询部件从哪一侧进入 Converter。

Converter 每一侧只能连接**一个对象**。数字表示 MU 从 Converter 的哪一侧离开。

### 侧边定义（插入方向：从左到右）

| 侧 | 含义 |
| --- | --- |
| **3** | 横向向左 |
| **1** | 横向向右 |
| **0** | 沿插入方向（直通） |

- **Side 3（横向向左）：** MU 以前部朝向运动方向移动。Converter 抬升 MU 后，它以其左侧朝向运动方向移动。由于横向移动的插入方向假设为从上到下，此后 Converter 向后移动，只要 MU 被登记在 Converter 上，其左侧即为后部。
- **Side 1（横向向右）：** MU 以前部朝向运动方向移动。Converter 抬升 MU 后，它以其右侧朝向运动方向移动。
- **Side 0（沿插入方向）：** MU 以前部朝向运动方向移动，并在直通传送过程中保持该朝向。

## 2. 容量与传送行为

- 只要 MU 仅沿一个方向被传送，Converter 可容纳**任意数量的 MU**。
- 若 MU 需要改变传送方向，Converter 只能抬升并传送**单个 MU**。
- MU 可从所有侧到达，并被传送到所有侧。
- 目标侧在 **Strategy Method（策略方法）**中确定；目标对象可同时切换到相应的传送方向。
- **首选方向（preferred direction）** 即插入 Converter 的方向，沿此方向传送 MU 无时间延迟。
- 若 MU 离开首选方向，它必须移上 Converter，被抬升（期间 **Moving Time** 消耗），然后从任一侧离开。
- 将 MU 传送到某一侧后，Converter 必须降回默认位置，才能传送下一个部件。抬升/下降时间由 **Moving Time** 指定。

### 连接前驱/后继

连接 Converter 时，可用鼠标确定 Connector 停靠在 Converter 的哪一侧（左、下、上或右）。也可用 Connector 的 `connect` 方法设置该侧。

### 长度导向对象

Converter 是**长度导向（length-oriented）**对象，可指定 **Relative Converting Point For Length** 和/或 **Relative Converting Point For Width**。

## 3. 注意：转换点处的空间要求

若 MU 在转换点处被转换，Converter 必须提供足够空间：

- **Booking Point Length** 到 MU 后部的距离，至多等于长度转换点到 Converter 左侧的距离。
- Booking Point Length 到 MU 前部的距离，至多等于长度转换点到 Converter 右侧的距离。
- **Booking Point Width** 到 MU 左侧的距离，至多等于宽度转换点到 Converter side 3 的距离。
- Booking Point Width 到 MU 右侧的距离，至多等于宽度转换点到 Converter side 1 的距离。

可在 **Appearance（外观）**选项卡上选择 Converter 的不同配置。

## 4. 显示与交互

- 将鼠标悬停在 Converter 上可显示工具提示。
- 点击 Edit 功能区标签页的 **Show Manipulators**（或按 `M`）可更改图形长度和锚点。
- 添加到模型：Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > Converter`。

## 5. Converter 对话框

双击 Converter 图标打开其对话框。

- **编辑仿真属性（Edit Simulation Properties）：** 共享属性见 *Dialog Items of the Objects*。
- **编辑动画属性（Edit Animation Properties）：** 点击左下角的 **Edit 3D Properties** 按钮，或选中对象并按空格键；点击 **Show Manipulators**（或按 `M`）操纵图形。

## 6. 选项卡 Attributes（属性）

### Length（长度）[文本框]

输入 Converter 的长度。若 MU 沿插入方向直通传送，其长度与 MU 的长度共同决定可容纳多少个 MU。若 Converter 垂直传送 MU，当定位点位于中心转换点时，它必须提供足够空间以完整容纳 MU 的长度与宽度。

**SimTalk：** `Length`

### Width（宽度）[文本框]

输入 Converter 的宽度。标准宽度为 1 米。

**SimTalk：** `Width`

### Speed（速度）[文本框]

输入 Converter 传送 MU 的速度。输入 `-1` 表示无限速度。

**SimTalk：** `Speed`

### Capacity（容量）[文本框]

输入 Converter 一次可容纳的 MU 数量（即容量）。默认值 `-1` 表示无限容量。若 Converter 沿插入方向传送 MU，Capacity 可限制其同时传送的 MU 数量（但它仍一次传送单个 MU）。

**SimTalk：** `Capacity`

### Relative Converting Point For Length（长度的相对转换点）

转换点沿长度方向的相对位置（取 0.0 到 1.0 之间的值）。转换点是 Converter 改变 MU 传送方向的位置，其位置不会显示在图形上。

**SimTalk：** `RelConvertingPointL`

### Relative Converting Point For Width（宽度的相对转换点）

转换点沿宽度方向的相对位置（取 0.0 到 1.0 之间的值）。

**SimTalk：** `RelConvertingPointW`

### Automatic Stop（自动停止）[复选框]

勾选后，当 Converter 不运输部件（例如为空或被阻塞）时，将其当前速度设为 0。若速度为 0，Energy State（能源状态）变为 Operational（运行）。

**SimTalk：** `AutomaticStop`

### Go to Default Position（回到默认位置）[复选框]

勾选后，使 Converter 在 MU 离开后返回默认位置。若有 MU 等待横向进入，则它不返回默认位置。

**SimTalk：** `GoToDefaultPosition`

### Strategy（策略）[下拉列表]

选择 Converter 将 MU 传送到下一个物料流对象所用的策略：

- **Default Exit** — 所有 MU 从在后继上选择的 Default Exit 离开。
- **Straight** — 将 MU 直通传送到下一站。若存在多条同等快速的路由，直通路由被优先（部件无需单独化）。在同等快速的路由中，Plant Simulation 选择部件需被转换最少的路由。
- **MU Attribute** — 根据内置或用户自定义属性传送 MU。点击 **Open List**，输入属性名称、值及离开侧；对每个属性重复。
- **MU Name** — 根据 MU 名称传送。点击 **Open List**，输入 MU 名称及离开侧。
- **Method** — 根据 Strategy Method 中输入的属性 `ExitForMU` 传送 MU。
- **Feed in** — 仅当主线上在 **Free Space**（两个相继 MU 之间的距离）内没有 MU 时，才允许支线上的 MU 进入主线。

> **注：** 除 **Feed In** 外，所有策略均遵循先到先服务原则。只有 **Feed In** 策略下主传送带具有优先权。

- **Method at Converting Point** — 在转换点处（而非 MU 进入之前）用属性 `ExitForMU` 确定目标。仅在 Capacity 为 1 时可用。MU 始终在转换点停下；随后 Plant Simulation 调用该方法（例如 `?.ExitForMU := 1`）。

> **注：** 若 MU 有路由且启用了 Automatic Routing（自动路由），则 Strategy Method 不会被调用。

**SimTalk：** `Strategy`、`Strategy Method`、`ExitForMU`

### Strategy Method（策略方法）[Converter]

修改对象的内置行为。当 MU 想要离开 Converter 时，对象调用 Strategy Method，并用属性 `ExitForMU` 设置离开侧。对于 **Strategy > Method at Converting Point**，它在 MU 到达转换点时执行。

> **注：** 不要用 Entrance Control 或 Exit Control 来确定目标——它们被调用的时间点太晚。

作为用户自定义属性的默认策略方法如下：

```simtalk
param entranceNo: integer
?.ExitForMU := 0 /* number of exit */
```

**SimTalk：** `StrategyCtrl`

### Default Exit（默认出口）[下拉列表]

为 **Default Exit**、**MU Attribute** 和 **MU Name** 策略选择默认出口：

| 值 | 含义 |
| --- | --- |
| `1` | 插入方向上横向向右 |
| `2` | 逆插入方向 |
| `3` | 插入方向上横向向左 |
| `0` | 沿插入方向 |

**SimTalk：** `DefaultExit`

### Open List（打开列表）[按钮]

打开 MU 的出口列表（用于 **MU Attribute** 和 **MU Name** 策略）。

**SimTalk：** `AttributeType`

### Attribute Type（属性类型）[下拉列表]

对于 **Strategy > MU Attribute**，选择决定部件移动到的物料流对象的属性数据类型。

## 7. 选项卡 Times（时间）

按 *Tab Times* 说明定义时间。从下拉列表选择分布并输入所需值；使用 **Const** 表示恒定时间。分布类型与参数可用 `setTypeAndAttr` [SimTalk] 设置。

Converter 额外提供 **Moving Time（移动时间）**。

### Moving Time（移动时间）[下拉列表]

Moving Time 是 Converter 将 MU 抬升到不同传送层、再降下并移回默认位置所需的时间。当 Converter 改变 MU 方向、以及 MU 从某一侧进入（即非首选插入方向）时，该时间始终会消耗。

使用 **Formula（公式）**分布时，可输入数值表达式或 Method 名称，并用匿名标识符 `@` 访问部件。

**SimTalk：** `MovingTime`、`MovingTime.Type`、`putAttributeNamesIntoTable`

## 8. 选项卡 Failures（故障）

按 *Tab Failures* 说明定义故障。

## 9. 选项卡 Controls（控制）

提供修改对象内置行为的控制项。选择已有 Method（通过省略号按钮 / **Select Object**），或将控制创建为数据类型为 Method 的用户自定义属性：

- 输入有意义名称并选择 **Create Control** → 插入 `self.你输入的控制名`（如 `self.A1Ctrl`）。
- 在空文本框上选择 **Create Control** → 插入 `self.On内置控制名`（如 `self.OnEntrance`）。

后续编辑：按 `F2`、按住 `Shift` 双击、在上下文菜单中选择 **Open Object**，或使用 **User-defined** 选项卡。删除时需删除相应用户自定义属性。

## 10. 选项卡 Statistics（统计）

统计按 *Tab Statistics* 说明描述。此外，Converter 还收集：

| 项 | 描述 | 只读属性 |
| --- | --- | --- |
| Moving Empty | 统计收集期内 Converter 未传送 MU 而进行抬升/下降的时间占比 | `StatMovingEmptyPortion` |
| Moving Loaded | 统计收集期内 Converter 传送 MU 时进行抬升/下降的时间占比 | `StatMovingLoadedPortion` |

查看统计报告中的 Moving Time：**View > Show Statistics Report**，或右键 Frame 选择 **Show Statistics Report**，或按 `F6`。

## 11. 选项卡 Energy（能源）

按 *Tab Energy* 说明选择能源设置。

## 12. 选项卡 Costs（成本）

Converter 运输部件期间，成本由**总投资成本**与**总运营成本**之和累积。

> **注：** 总投资成本仅在**折旧期（Depreciation Period）**内累积。成本按部件长度相对于 Converter 有效长度的比例分配给部件（较长的部件被分配更高的成本）。若 Converter 为空，成本作为**一般成本（general costs）**保留在 Converter 上。

## 13. 选项卡 User-defined（用户自定义）

按 *Tab User-defined* 说明定义自定义属性。

## 14. 菜单

- **Navigate 菜单：** 命令见 *Navigate Menu* 说明。
- **View 菜单：** 提供 Refresh、Show Statistics Report、Show Attributes and Methods 及 Contents。
- **Tools 菜单：** 命令见 *Tools Menu* 说明。
- **Tabs 菜单：** 显示/隐藏各个选项卡；点击 OK、关闭并重新打开对话框以应用更改。命令 **Inherit** 切换已显示/隐藏选项卡的继承。
- **Help 菜单：** 命令见 *Help Menu* 说明。

## 15. Converter 的方法

Converter 提供：

- 目录表中列出的方法；
- _Methods of Curved Objects（曲线对象的方法）；
- Methods of the Material Flow Objects（物料流对象的方法）；
- Methods of All Objects（所有对象的通用方法）。

查看方式：打开 **Show Attributes and Methods** 窗口（通过类库的上下文菜单）。

## 16. See also

- Convey Parts Laterally with the Converter（视频：https://youtu.be/hOvdrDnvXXo?si=TgnQivMCDc9eD3nU&t=13）
- Convey Parts According to a Strategy Control
- Convey Parts Laterally According to Their Name
- Data Held in Tabular Form in Attributes [material flow objects]
- Recovery Time / Recovery Time Starts
- Cycle Time
- Resource Statistics [check box] / Resource Type
- Simulate the Accrued Costs of the Machines
- CostAnalyzer topics

## 目录说明

- `general.md`：Converter 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
