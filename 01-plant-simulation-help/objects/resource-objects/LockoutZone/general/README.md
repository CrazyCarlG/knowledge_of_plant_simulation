# LockoutZone（锁定区域）— 概览

> 本 README 总结了 `general.md` 中关于 **LockoutZone** 资源对象的内容。

## 用途

**LockoutZone** 用于将一组物料流对象组合在一起。当其中某个工位（station）发生故障时，锁定区域内的所有其他工位也会停止加工其零件。

LockoutZone 负责控制所有工位的故障，并返回所分配工位的总体可用性。

## 主要行为

- 一个仿真模型中可插入多个 LockoutZone，且它们可以重叠——即一个工位可被分配给多个 LockoutZone。
- 必须至少为其中一个被分配的工位定义故障配置文件（failure profile）。一旦某个工位发生故障，LockoutZone 会停止所有被分配工位的加工操作，即将它们的属性 `Stopped` 设为 `true`。可选择「立即停止」或「服务到达时停止」。
- 只有当所有故障都被排除后，工位才会重新开始加工零件，并且只消耗剩余的加工时间。
- 可通过编写 **Resume Control（恢复控制）** 来决定工位重新开始加工时的行为。
- 如果某个工位在 LockoutZone 准备停止时正处于暂停状态，则该工位在暂停结束后不会开始或重新开始加工。
- 可将任何内置的物料流对象（Material Flow Objects）或流体对象（Fluid Objects）分配给 LockoutZone。对于用户在 Frame 中自行建模的工位，LockoutZone 会将该 Frame 的属性 `Stopped` 设为 `true`，用户需自行建模对该属性的反应。此外还可添加 Worker 或 WorkerPool。
- 如果触发锁定区域的工位被分配给多个 LockoutZone，则所有 LockoutZone 的所有工位都会被停止；如果只分配给一个 LockoutZone，则仅停止分配给它的工位。
- 将鼠标悬停在 LockoutZone 上可显示提示信息；按 `M` 键或点击「编辑」选项卡上的 **Show Manipulators** 可更改图形长度和锚点。

## 添加到仿真模型

点击「主页」选项卡上的 **Manage Class Library > Basic Objects > Resources > LockoutZone**。

示例模型：点击 Window 选项卡，进入 **Start Page > Getting Started > Example Models > Small Examples**，在 Examples Collection 对话框中选择相应 Category、Topic 和 Example，然后点击 Open Model。

## 对话框

双击 LockoutZone 图标打开其对话框。

- **编辑仿真属性**：可更改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **编辑动画属性**：通过 **Edit 3D Properties** 按钮（位于仿真属性对话框左下角）或选中对象后按空格键，编辑 3D 属性。

## 对话框各项说明

### Active [复选框]

勾选后激活 LockoutZone：当某个被分配工位发生故障时，停止所有被分配对象的加工操作。取消勾选则停用。

**SimTalk**：`Active [SimTalk] - LockoutZone`

### Tab Controls（控制选项卡）

用于修改对象的内置行为。可通过以下方式为控件指定 Method：

- 点击省略号按钮，在 *Select Object [for controls]* 对话框中选择 Method 位置并点击 OK。
- 在文本框中按 `F2` 打开 Method 编写源代码。
- 或将 Frame 中的 Method 直接拖放到文本框。

也可将控件创建为对象自身的用户定义属性（数据类型 Method）：输入名称后选择 **Create Control**，Plant Simulation 会插入 `self.名称`（如 `self.A1Ctrl`）；或在空文本框选择 **Create Control**，插入 `self.On内置控件名`（如 `self.OnEntrance`）。

指定控件会覆盖 LockoutZone 的默认行为——即用户需自行通过将属性 `Stopped` 设为 `true` 来停止所有被分配对象，并将 `Stopped` 设为 `false` 来恢复加工。

### Stop Control（停止控制）

当某个被分配工位发生故障并停止加工时，对象会调用 Stop Control。匿名标识符 `@` 表示触发工位，`?` 表示 LockoutZone。

**SimTalk**：`StopCtrl [SimTalk]`

### Resume Control（恢复控制）

当所有故障被排除、工位可恢复加工时，对象会调用 Resume Control。

**SimTalk**：`ResumeCtrl [SimTalk]`

### Stop Mode [下拉列表]

- **Stop immediately（立即停止）**：一旦某个被分配工位故障，立即停止 LockoutZone 内所有工位的加工（模型中的其他工位不受影响）。期间可发生多次故障、相互重叠；所有故障排除后才恢复加工，且只消耗剩余加工时间。
- **Stop when Service arrives（服务到达时停止）**：仅在故障工位请求的维修服务被指派后才停止。对于通过 Footpath 步行的 Worker，视为其到达工位后；对于可传送的 Exporter/Worker，视为 Broker 指派服务后（与 Receive Control 行为一致）。

LockoutZone 不影响其控制工位的恢复时间（Recovery Time）和循环时间（Cycle Time）。它停止这些对象并为 `Stopped` 状态记录统计值。若在停止过程中停用 LockoutZone，会立即释放所有被停止对象；重置模型时所有对象从 stopped 变为 operational。

**SimTalk**：`StopMode [SimTalk]`

### Tab Objects（对象选项卡）

在 Objects 选项卡上为 LockoutZone 分配资源。资源可为任何内置物料流对象，或建模了机器的 Frame（其工作时间由 LockoutZone 控制），也可添加 Worker 或 WorkerPool。

**Objects [LockoutZone]**：分配物料流或流体对象。步骤：

1. 先点击 **Inheritance** 复选框。
2. 在单元格中输入资源对象的路径和名称；或
3. 将资源对象拖放到 LockoutZone 图标上（可同时多选拖放）。

**SimTalk**：`addObject [SimTalk] - LockoutZone`、`Objects [SimTalk] - LockoutZone`

### Tab Statistics（统计选项卡）

显示 LockoutZone 最重要的统计数据：

| 项目 | 说明 | 只读属性 |
|------|------|----------|
| Stopped Portion | 统计周期内工位被 LockoutZone 停止的时间占比（%） | `StatStoppedPortion [SimTalk] - LockoutZone` |
| Stopped Count | LockoutZone 停止工位的次数 | `StatStoppedCount [SimTalk] - LockoutZone` |
| Stopped durations total time | 停止加工操作的总时间 | `StatStoppedTime [SimTalk]` |
| Stopped durations mean time | 停止加工操作的平均时间 | `StatStoppedMu [SimTalk] - LockoutZone` |
| Stopped durations Standard Deviation | 停止时间的标准差 | `StatStoppedDelta [SimTalk] - LockoutZone` |
| Stopped intervals mean time | 停止区间的平均时间 | `StatStoppedIntervalMu [SimTalk]` |
| Stopped intervals Standard Deviation | 停止区间的标准差 | `StatStoppedIntervalDelta [SimTalk]` |

统计报告会显示各个物料流对象的 Stopped Time。

### Tab User-defined（用户自定义选项卡）

按 *Tab User-defined* 所述定义自定义属性。

## 菜单

- **Navigate Menu**：命令见 *Navigate Menu*。
- **View Menu**：
  - Refresh [on View menu]
  - Show Assigned Objects [LockoutZone]
  - Show Attributes and Methods [on View menu]
  - **SimTalk**：`updateDialog [SimTalk]`
- **Show Assigned Objects [LockoutZone]**：在 Frame 窗口中选中分配给 LockoutZone 的资源对象（也可通过 Frame 中 LockoutZone 的上下文菜单选择 **Show Assigned Objects [in Frame]**）。
- **Tools Menu**：Edit Controls、Edit Observers。
- **Help Menu**：命令见 *Help Menu*。

## 方法（Methods）

LockoutZone 提供：

- 方法 `addObject [SimTalk] - LockoutZone`。
- 所有对象的通用方法（*Methods of All Objects*）。

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 查看所选类。
- 按 `F8` 键或点击插入实例的 Frame 中「主页」选项卡上的 **Show Attributes and Methods** 查看所选实例。
