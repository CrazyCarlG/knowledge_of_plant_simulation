# Drain — General（概述）

本目录存放 **Drain**（排水/移除）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. Drain 对象概述

**Drain** 用于在工件（MU）加工完成后将其从工厂中移除，通常代表工厂的发货部门。

- Drain 的内置属性与 **Station** 相同；与 Station 一样，它只有**一个加工位置**。
- 与 Station 的唯一区别在于：Drain 会将加工完成的工件**从工厂中移除**，而不是将其移动到后续物料流对象。
- Drain 本质上是 **Source** 的对应物（Source 生产工件，Drain 移除工件）。
- 可在 HtmlReport 中显示 Drain 的统计表；将鼠标悬停在 Drain 上可显示工具提示；点击编辑功能区标签页的 **Show Manipulators**（或按 `M`）可更改图形长度和锚点。

**添加到模型：** Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > Drain`。

**示例模型：** Window 功能区标签页 → `Start Page > Getting Started > Example Models > Small Examples`。

## 2. Trigger [SimTalk]

设置或返回由 `<Path>` 指定的 Source 的内部 Trigger 列表。

- **类型：** Attribute
- **语法：** `<Path>.Trigger:array`
- **可赋值：** 数据类型为 `array` 的值。

```simtalk
var assignedTriggers: object[2]
for var j := 1 to 2
   assignedTriggers[j] := to_str("Trigger", j)
next
   Source.Trigger := assignedTriggers
// sets the trigger list
print MySource.Trigger // gets the trigger list
// [*.Models.Model.Trigger, *.Models.Model.Trigger2]
```

**参见：** Trigger [time of creation]

## 3. Drain 对话框

双击 Drain 图标即可打开其对话框，可编辑仿真属性与动画属性。

- **编辑仿真属性：** 共享属性见 *Dialog Items of the Objects*。
- **编辑动画属性：** 点击左下角 **Edit 3D Properties** 按钮，或选中对象按空格键；点击 **Show Manipulators**（或按 `M`）操纵图形。

## 4. 选项卡 Times（时间）

按 *Tab Times* 说明定义时间。从下拉列表选择分布类型并在文本框中输入所需值（参数显示在选项卡上边界）；也可选择恒定时间（**Const**）。分布类型与参数可用方法 `setTypeAndAttr [SimTalk]` 设置。

**参见：** Define Processing Times、Select the Set-Up Time、Processing Time、Set-up Time、Recovery Time、Cycle Time。

## 5. 选项卡 Set-Up（设置）

按 *Tab Set-Up* 说明定义对象设置（set-up）的相关属性。

## 6. 选项卡 Failures（故障）

按 *Tab Failures* 说明定义故障。

## 7. 选项卡 Controls（控制）

提供修改对象内置行为的控制项。

- **选择已有 Method 的路径：** 点击省略号按钮，在 *Select Object [for controls]* 中导航选择；在文本框中按 `F2` 打开 Method，或将 Method 从 Frame 拖入文本框。
- **创建对象方法作为控制：**
  - 在文本框中输入有意义名称并选择 **Create Control** —— Plant Simulation 插入 `self.你输入的控制名`（如 `self.A1Ctrl`）。
  - 在空文本框上选择 **Create Control** —— Plant Simulation 插入 `self.On内置控制名`（如 `self.OnEntrance`）。
- **编辑源代码：** 按 `F2`、按住 `Shift` 双击文本框、在上下文菜单选择 **Open Object**，或使用 **User-defined** 选项卡。删除控制需删除相应用户自定义属性（仅从文本框删除名称不会删除该属性）。

**参见：** Select Object [for controls]、Entrance Control、Set-up Control、Pull Control、Shift Calendar。

## 8. 选项卡 Statistics（统计，Drain）

统计按 *Tab Statistics* 说明描述。除 *Statistics Report* 中的数据外，Drain 还会收集并显示移动对象的统计数据。

- 也可为同名 MU 收集统计（见 *Tab Type Statistics*）。
- 每次 Drain 移除一个工件时，它会通过将平均值除以平均寿命再乘以 100，计算出每个显示统计值的比例平均值。
- 查看累计统计：`View > Show Statistics Report`，右键 Frame 选择 **Show Statistics Report**，或按 `F6`。

**参见：** Tab Statistics [material flow objects]、Tab Type Statistics、Statistics Report、Product Statistics of the MUs、Resource Statistics、Resource Type。

## 9. 选项卡 Type Statistics（类型统计）

显示仿真模型中流经的同名 MU 的统计数据。

- 提供 **Type Dependent Statistics** 复选框，激活后按类型收集统计。
- 点击 **Detailed Statistics Table** 打开按类型列出被移除工件的表格。

该选项卡显示的统计数据：

| 项 | 说明 | 只读属性 |
|------|-------------|---------------------|
| Working | MU 位于工作对象上的时间占比（相对所有 MU 的统计收集周期）。 | `StatProdWorkingPortion`、`StatStoreWorkingPortion`、`StatTranspWorkingPortion` |
| Setting-up | 对象为 MU 设置的时间占比。 | `StatProdSetupPortion`、`StatStoreSetUpPortion`、`StatTranspSetupPortion` |
| Waiting | 对象等待 MU 的时间占比。 | `StatProdWaitingPortion`、`StatStoreWaitingPortion`、`StatTranspWaitingPortion` |
| Stopped | MU 位于停止对象上的时间占比。 | `StatProdStoppedPortion`、`StatStoreStoppedPortion`、`StatTranspStoppedPortion` |
| Failed | MU 位于故障对象上的时间占比。 | `StatProdFailPortion`、`StatStoreFailPortion`、`StatTranspFailPortion` |
| Paused | MU 位于暂停或未计划对象上的时间占比。 | `StatProdPausingPortion`、`StatStorePausingPortion`、`StatTranspPausingPortion` |
| Average lifespan | 收集周期内创建并移除的 MU 的平均寿命（仅统计启用了产品统计的 MU）。 | `StatAvgLifeSpan` |
| Average exit interval | 被移除 MU 之间的平均时间间隔（从第一个工件到达时开始计时）。 | `StatAvgExitInterval` |
| Total throughput | 自 Type dependent statistics 激活以来移除的 MU 数量。 | `StatDeleted` |
| Throughput per minute | 在观察到的所有可用时间内每分钟移除的 MU 数量。 | `StatThroughputPerMinute` |
| Throughput per hour | 在观察到的所有可用时间内每小时移除的 MU 数量。 | `StatThroughputPerHour` |
| Throughput per day | 每天移除的 MU 数量（每小时吞吐量 × 24）。 | `StatThroughputPerHour` |

> **注：** working、setting-up、failed、stopped、paused 的百分比之和为 100%。查看统计报告中的工件类型：选中对象按 `F6`，点击 Home 功能区标签页的 **Show Statistics Report**，或右键对象选择 **Show Statistics Report**。

**视频：** https://youtu.be/BvHLQCIjGIA?si=sryvv1gjwWw1LOUF&t=57

### Type Dependent Statistics（类型相关统计）

根据从工厂移除的 MU 类型激活统计收集。

- **SimTalk：** `TypeStatOn [SimTalk]`
- **参见：** `StatThroughputPerDay`、`StatThroughputPerHour`、`StatAvgExitInterval`、`typeStatisticsCumulated`。

### Detailed Statistics Table（详细统计表，Drain）

按类型列出从工厂移除的 MU，显示以下值：

| 项 | 说明 | 只读属性 |
|------|-------------|---------------------|
| Type | MU 名称。 | — |
| Time | 该类型工件的最后到达时间。 | — |
| Total throughput | 该类型工件的数量。 | `StatThroughputPerDay`、`StatThroughputPerHour` |
| %Parts | 该类型工件的百分比。 | — |
| LT_Mean | 所有调查工件的平均寿命（吞吐时间）。 | — |
| LT_StdDev | 寿命的标准差。 | — |
| LT_Min | 最小寿命。 | — |
| LT_Max | 最大寿命。 | — |
| TPh_Mean | 观察到的可用时间内每小时移除的 MU 数量。 | — |
| TPh_StdDev | 每小时吞吐量的标准差。 | — |
| TPh_Min | 最小每小时吞吐量。 | — |
| TPh_Max | 最大每小时吞吐量。 | — |
| TPd_Mean | 每天移除的 MU 数量（每小时吞吐量 × 24）。 | — |
| TPd_StdDev | 每天吞吐量的标准差。 | — |
| TPd_Min | 最小每天吞吐量。 | — |
| TPd_Max | 最大每天吞吐量。 | — |
| CT_Mean | 两个前后到达工件的平均节拍时间（cycle time）。 | — |
| CT_StdDev | 节拍时间差的标准差。 | — |
| CT_Min | 两个前后到达工件的最小节拍时间差。 | — |
| CTS_Max | 两个前后到达工件的最大节拍时间差。 | — |
| IP_Mean | 调查工件的平均加工时间。 | — |
| IP_StdDev | 加工时间的标准差。 | — |
| IP_Min | 最小加工时间。 | — |
| IP_Max | 最大加工时间。 | — |
| S_Mean | 平均设置时间。 | — |
| S_StdDev | 设置时间的标准差。 | — |
| S_Min | 最小设置时间。 | — |
| S_Max | 最大设置时间。 | — |
| W_Mean | 平均等待时间。 | — |
| W_StdDev | 等待时间的标准差。 | — |
| W_Min | 最小等待时间。 | — |
| W_Max | 最大等待时间。 | — |
| Stp_Mean | 位于停止资源上的平均时间。 | `StatProdStoppedPortion` |
| Stp_StdDev | 位于停止资源上时间的标准差。 | — |
| Stp_Min | 位于停止资源上的最小时间。 | — |
| Stp_Max | 位于停止资源上的最大时间。 | — |
| F_Mean | 位于故障资源上的平均时间。 | — |
| F_StdDev | 位于故障资源上时间的标准差。 | — |
| F_Min | 位于故障资源上的最小时间。 | — |
| F_Max | 位于故障资源上的最大时间。 | — |
| P_Mean | 位于暂停资源上的平均时间。 | — |
| P_StdDev | 位于暂停资源上时间的标准差。 | — |
| P_Min | 位于暂停资源上的最小时间。 | — |
| P_Max | 位于暂停资源上的最大时间。 | — |

**生产资源行（`_P_`）：**

| 项 | 说明 | 只读属性 |
|------|-------------|---------------------|
| IP_P_Mean | 生产资源上的平均加工时间。 | `StatProdWorkingPortion` |
| IP_P_StdDev | 生产资源上加工时间的标准差。 | — |
| IP_P_Min | 生产资源上的最小加工时间。 | — |
| IP_P_Max | 生产资源上的最大加工时间。 | — |
| S_P_Mean | 生产资源上的平均设置时间。 | `StatProdSetupPortion` |
| S_P_StdDev | 生产资源上设置时间的标准差。 | — |
| S_P_Min | 生产资源上的最小设置时间。 | — |
| S_P_Max | 生产资源上的最大设置时间。 | — |
| W_P_Mean | 生产资源上的平均等待时间。 | `StatProdWaitingPortion` |
| W_P_StdDev | 生产资源上等待时间的标准差。 | — |
| W_P_Min | 生产资源上的最小等待时间。 | — |
| W_P_Max | 生产资源上的最大等待时间。 | — |
| Stp_P_Mean | 位于停止的生产资源上的平均时间。 | `StatProdStoppedPortion` |
| Stp_P_StdDev | 位于停止的生产资源上时间的标准差。 | — |
| Stp_P_Min | 位于停止的生产资源上的最小时间。 | — |
| Stp_P_Max | 位于停止的生产资源上的最大时间。 | — |
| F_P_Mean | 位于故障的生产资源上的平均时间。 | `StatProdFailPortion` |
| F_P_StdDev | 位于故障的生产资源上时间的标准差。 | — |
| F_P_Min | 位于故障的生产资源上的最小时间。 | — |
| F_P_Max | 位于故障的生产资源上的最大时间。 | — |
| P_P_Mean | 位于暂停的生产资源上的平均时间。 | `StatProdPausingPortion` |
| P_P_StdDev | 位于暂停的生产资源上时间的标准差。 | — |
| P_P_Min | 位于暂停的生产资源上的最小时间。 | — |
| P_P_Max | 位于暂停的生产资源上的最大时间。 | — |

**运输资源行（`_T_`）：**

| 项 | 说明 | 只读属性 |
|------|-------------|---------------------|
| IP_T_Mean | 运输资源上的平均加工时间。 | `StatTranspWorkingPortion` |
| IP_T_StdDev | 运输资源上加工时间的标准差。 | — |
| IP_T_Min | 运输资源上的最小加工时间。 | — |
| IP_T_Max | 运输资源上的最大加工时间。 | — |
| S_T_Mean | 运输资源上的平均设置时间。 | `StatTranspSetupPortion` |
| S_T_StdDev | 运输资源上设置时间的标准差。 | — |
| S_T_Min | 运输资源上的最小设置时间。 | — |
| S_T_Max | 运输资源上的最大设置时间。 | — |
| W_T_Mean | 运输资源上的平均等待时间。 | `StatTranspWaitingPortion` |
| W_T_StdDev | 运输资源上等待时间的标准差。 | — |
| W_T_Min | 运输资源上的最小等待时间。 | — |
| W_T_Max | 运输资源上的最大等待时间。 | — |
| Stp_T_Mean | 位于停止的运输资源上的平均时间。 | `StatTranspStoppedPortion` |
| Stp_T_StdDev | 位于停止的运输资源上时间的标准差。 | — |
| StpF_T_Min | 位于停止的运输资源上的最小时间。 | — |
| Stp_T_Max | 位于停止的运输资源上的最大时间。 | — |
| F_T_Mean | 位于故障的运输资源上的平均时间。 | `StatTranspFailPortion` |
| F_T_StdDev | 位于故障的运输资源上时间的标准差。 | — |
| F_T_Min | 位于故障的运输资源上的最小时间。 | — |
| F_T_Max | 位于故障的运输资源上的最大时间。 | — |
| P_T_Mean | 位于暂停的运输资源上的平均时间。 | `StatTranspPausingPortion` |
| P_T_StdDev | 位于暂停的运输资源上时间的标准差。 | — |
| P_T_Min | 位于暂停的运输资源上的最小时间。 | — |
| P_T_Max | 位于暂停的运输资源上的最大时间。 | — |

**存储资源行（`_S_`）：**

| 项 | 说明 | 只读属性 |
|------|-------------|---------------------|
| IP_S_Mean | 存储资源上的平均加工时间。 | `StatStoreWorkingPortion` |
| IP_S_StdDev | 存储资源上加工时间的标准差。 | — |
| IP_S_Min | 存储资源上的最小加工时间。 | — |
| IP_S_Max | 存储资源上的最大加工时间。 | — |
| S_S_Mean | 存储资源上的平均设置时间。 | `StatStoreSetUpPortion` |
| S_S_StdDev | 存储资源上设置时间的标准差。 | — |
| S_S_Min | 存储资源上的最小设置时间。 | — |
| S_S_Max | 存储资源上的最大设置时间。 | — |
| W_S_Mean | 存储资源上的平均等待时间。 | `StatStoreWaitingPortion` |
| W_S_StdDev | 存储资源上等待时间的标准差。 | — |
| W_S_Min | 存储资源上的最小等待时间。 | — |
| W_S_Max | 存储资源上的最大等待时间。 | — |
| Stp_S_Mean | 位于停止的存储资源上的平均时间。 | `StatStoreStoppedPortion` |
| Stp_S_StdDev | 位于停止的存储资源上时间的标准差。 | — |
| Stp_S_Min | 位于停止的存储资源上的最小时间。 | — |
| Stp_S_Max | 位于停止的存储资源上的最大时间。 | — |
| F_S_Mean | 位于故障的存储资源上的平均时间。 | `StatStoreFailPortion` |
| F_S_StdDev | 位于故障的存储资源上时间的标准差。 | — |
| F_S_Min | 位于故障的存储资源上的最小时间。 | — |
| F_S_Max | 位于故障的存储资源上的最大时间。 | — |
| P_S_Mean | 位于暂停的存储资源上的平均时间。 | `StatStorePausingPortion` |
| P_S_StdDev | 位于暂停的存储资源上时间的标准差。 | — |
| P_S_Min | 位于暂停的存储资源上的最小时间。 | — |
| P_S_Max | 位于暂停的存储资源上的最大时间。 | — |

**SimTalk：** `typeStatistics [SimTalk] - Drain`、`typeStatisticsCumulated [SimTalk]`

**视频：** https://youtu.be/BvHLQCIjGIA?si=RrcV9zshpXbrOs0I&t=508

## 10. 选项卡 Importer（导入，Drain）

定义加工工件、为某种工件类型设置工位以及维修工位的服务，同时使 Worker 能够将工件搬运到 Drain。

- 查看 Importer Statistics：选中对象按 `F6`，或点击 Home 功能区标签页的 **Show Statistics Report**。

**参见：** Tab Importer [general description]、Processing Importer、Set-up Importer、Failure Importer。

## 11. 选项卡 User-defined（用户自定义）

按 *Tab User-defined* 说明定义自定义属性。

## 12. 菜单

- **Navigate 菜单：** 命令见 Navigate Menu 说明。
- **View 菜单：** 提供 `Refresh Services`、`Show Statistics Report`、`Unavailable Services`、`Show Attributes and Methods`、`Associated Workplaces`、`Contents`、`Exiting MUs`、`Forward Blocking List`、`Associated Lockout Zones`、`Exporters`、`Associated Shift Calendar`。
- **Tools 菜单：** 命令见 Tools Menu 说明。
- **Tabs 菜单：** 显示/隐藏所选物料流对象的各个选项卡。隐藏不用的选项卡可加快对话框打开速度、更快切换到所需选项卡；点击 **OK** 关闭并重新打开对话框以应用更改；菜单在已显示选项卡左侧显示勾选标记；**Inherit** 可打开/关闭对话框中显示/隐藏选项卡的继承。
- **Help 菜单：** 命令见 Help Menu 说明。

## 13. Drain 的方法

Drain 提供：

- 左侧目录中列出的方法；
- Station 的方法（Methods of the Station）；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

查看方式：打开 **Show Attributes and Methods**（在类库上下文菜单中选择）查看全部方法、只读属性和属性。

## 目录说明

- `general.md`：Drain 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
