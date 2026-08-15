# Frame 建模、仿真控制与拖放

本目录汇总了 Plant Simulation 帮助文档中关于**层次化建模（Frame）**、**仿真控制（EventController）** 与**拖放操作（Drag-and-Drop）** 的内容。

> 说明：本目录仅包含一个说明文档 `frame-modeling-simulation-control-drag-drop.md`（及其原始文本 `frame-modeling-simulation-control-drag-drop.txtx`），无子文件夹。

---

## 目录

1. [层次化建模](#1-层次化建模)
2. [使用 Frame](#2-使用-frame)
3. [从类库中建模](#3-从类库中建模)
4. [向 Frame 插入对象](#4-向-frame-插入对象)
5. [用连接器连接对象](#5-用连接器连接对象)
6. [为 Frame 添加背景图](#6-为-frame-添加背景图)
7. [自定义功能区选项卡 / 上下文菜单](#7-自定义功能区选项卡--上下文菜单)
8. [在 Frame 窗口中操作对象](#8-在-frame-窗口中操作对象)
9. [对象的工具提示](#9-对象的工具提示)
10. [Frame 之间的模型转换](#10-frame-之间的模型转换)
11. [用 EventController 控制仿真](#11-用-eventcontroller-控制仿真)
12. [仿真设置](#12-仿真设置)
13. [事件调试器](#13-事件调试器)
14. [删除零件](#14-删除零件)
15. [拖放操作](#15-拖放操作)

---

## 1. 层次化建模

层次化建模指把一个 Frame 中建模好的**组件**插入到其他 Frame 中，从而可以脱离整体模型单独建模与测试各个组件。

- 可将任意数量的组件组合到构建整体模型的 Frame 中。
- 例：在 `MyComponent1` 中建模组件，再插入到保存完整模型的 `MyPlantAnytown` 中。
- 点击 **Open Origin** 可打开当前 Frame 所派生的源 Frame。
- 组件（大型机器、整个部门）可尽可能贴近真实对象建模、多次插入、设置图标，并像其他对象一样使用。
- **优点**：模型结构清晰；可由多位同事/多个站点分工开发，之后再集成。

**测试组件**：将组件插入测试 Frame，添加 Source 和 Drain，连接所有对象后启动仿真。

---

## 2. 使用 Frame

- 仿真模型通常创建在类库 `Models` 文件夹中的 Frame 内，也可以插入更多 Frame。
- **重命名 Frame**：类库中右键 → Rename；或选中按 `F2`；或 Frame 窗口 Home 选项卡的 Rename（`F4`）。
- **建模**：插入内置/自定义对象，并用 **Connector**（连接器）连接。
- **运行仿真**：插入 **EventController** 来启动、停止、重置仿真。
- **层次结构**：Frame 中嵌套 Frame，构建贴近真实系统的模型。

**视图选项**：通用设置见 `File > Preferences/Model Settings`；Frame 相关设置在 View 选项卡（显示/隐藏对象名、连接器、注释对象、网格等）。新 Frame 继承 `File > Preferences/Model Settings` 的设置；选择 **Inherit Settings** 可恢复内置设置。

---

## 3. 从类库中建模

从类库文件夹把类对象的实例插入模型（通常是 `Models` 文件夹中的 Frame）。

> 注意：重命名已作为入口/出口控制、或作为 `Source > Attributes > MU Selection > MU` 的对象，可能破坏路径语句导致模型无法正常运行。

- **从类库插入**：找到对象 → 点击选中 → 按住拖到 Frame 目标位置后松开。
- **从工具箱插入**：点击工具栏（如 Material Flow）中的图标 → 在 Frame 目标位置单击；按住 `Shift`/`Ctrl` 可插入多个实例；`Ctrl`+点击对象可跳到其类；`Ctrl+Alt`+点击可编辑类属性。

---

## 4. 向 Frame 插入对象

- **新建模型**：Start Page 的 **Create New Model**，或 `File > New`。
- **插入对象**：点击工具箱图标（光标变十字）再在 Frame 中点击；或从类库拖放。
- **插入多个实例**：点击对象后按住 `Ctrl`/`Shift` 反复点击。
- **示例模型**：从 Material Flow 插入一个 Source、三个 Station、一个 Drain；从 User Interface 插入一个 Chart。
- **移动对象**：按住拖动；方向键逐像素移动；`Shift`+方向键逐网格移动。
- **其他**：框选后点击 Icons 选项卡的 **Align to Grid** 对齐网格；按 `Delete` 或右键 Delete 删除。

---

## 5. 用连接器连接对象

物料流对象有**入口点**（接收零件）和**出口点**（零件离开），**Connector** 通过这些点建立物料流连接。

### 自动连接
- 插入对象时使它们相邻放置（需开启 **Connect Objects Automatically**，Planning View 下效果最佳）。
- 要求一个对象的出口与下一个对象的入口间距不超过 **3 像素**。

### 手动连接
1. 点击工具箱中的 **Connector** 进入连接模式（光标变十字）。
2. 依次点击对象 A、对象 B。
3. 仅当 View 选项卡选中 **Show Connections** 时才显示连接。

### 连接器修饰键
| 操作 | 效果 |
|---|---|
| Connector（无按键） | 连接对齐到点击位置附近的网格点 |
| Connector + Ctrl | 保持连接模式，连续连接多个对象 |
| Connector + Shift | 以直角插入连接 |
| Connector + Alt | 在点击位置设置锚点（类似自由绘制） |

### 其他连接器操作
- 查看未连接对象：View 选项卡的 **Unconnected Objects**。
- 线宽/颜色：在 **Weight** 输入数字、在 **Colors** 对话框设置颜色。
- 交换后继/前驱：拖动连接器端点到另一对象。
- 在两个已连接对象之间插入对象：拖到连接器上松开。
- 删除对象时保留连接器：按住 `Ctrl` 再按 `Del`。
- 重排后继：右键对象 → **Reorder Successors**。

---

## 6. 为 Frame 添加背景图

- 将 `.gif`、`.bmp`、`.ppm`、`.dgn`、`.dxf`、`.dwg` 文件从资源管理器/浏览器拖到 Frame 背景上松开。
- `.dxf`/`.dgn`/`.dwg` 为矢量图，而 Plant Simulation 使用位图，需注意尺寸换算。
- CAD 图纸尺寸 ≤ 32000×32000 像素时使用 **Corrective Scaling = 1**；更大时自动缩放以适应 Frame 窗口。

---

## 7. 自定义功能区选项卡 / 上下文菜单

在 Frame 中创建常用命令的自定义选项卡或右键菜单：

1. 点击 **Configure User-defined Ribbon Tab** 或 **Configure User-defined Context Menu**（嵌套 Frame 需先停用 **Inherit**）。
2. 输入 **Title**（标题）。
3. 选中 **Active** 以显示该选项卡。
4. 输入命令名，用 `&` 前缀字母作为访问键。
5. 命令为公式时以 `?` 开头，如 `?Method1`、`?Method1(42)`、`?DataTable[1,3]`；返回空字符串 `""` 可隐藏命令。
6. 在 **Method to execute** 中输入要执行的方法；自定义选项卡中的匿名标识符 `?` 指向命令所在的 Frame。
7. 点击 **OK** 创建。

**从选项卡打开对话框**：在 **Method to execute** 中填入打开对话框的方法名，该方法体为 `name_of_your_user_defined_dialog.open`。

---

## 8. 在 Frame 窗口中操作对象

- **打开对象/Frame 窗口**：双击。
- **插入对象**：类库/工具箱选中后拖到 Frame 松开。
- **选择/移动/取消选择**：单击选中并拖动；点击其他对象或空白处取消。
- **多选**：按住 `Shift` 点击，或框选；`Ctrl+A` 全选。
- **微调**：方向键移动 1 像素，`Shift`+方向键移动 1 网格。
- **查找对象**：Frame 选项卡的 **Incremental Find Object**。
- **缩放**：滚动鼠标滚轮。
- **锁定防修改**：点击锁定开关。
- **Frame 状态**：使用 `StateBlocked`、`StateEntryShut`、`StateWorking`、`Stopped` 等属性，以彩色圆环显示状态。
- **帮助**：选中对象按 `F1`。

### Frame 状态颜色
| 颜色 | 状态 |
|---|---|
| 红 | Failed（失败） |
| 粉 | Stopped（停止） |
| 蓝 | Paused（暂停） |
| 浅蓝 | Unplanned（非计划） |
| 绿 | Working（工作） |
| 黄 | Blocked（阻塞） |
| 棕 | Setting-Up（设置中） |
| 青 | 恢复中 / 入口关闭 |
| 橙 | 等待资源（Exporter） |

---

## 9. 对象的工具提示

鼠标悬停在对象上会显示工具提示。所有对象显示名称（加粗）和来源；状态和类型会附加更多信息（如 EventController 显示当前仿真时间与结束时间；连接器显示连接；运输工具显示路线长度等）。

---

## 10. Frame 之间的模型转换

层次化建模中，用 **Interface**（接口）把组件 Frame 连接到前/后物料流对象或 Frame，实现 MU 在 Frame 之间的转移。

- Interface 会显示是否已连接，以及是入口还是出口。
- 若子 Frame 只含单个物料流对象，可直接连接子 Frame，无需 Interface。
- 默认 `Graphics > Show Content` 激活（3D 显示内容），清除后仅显示子 Frame。
- 从 `MaterialFlow`（类库）或 Material Flow 工具栏插入 Interface。

**配置 Interface**：
1. 选择 Frame 图标的一侧：Top / Right / Bottom / Left。
2. 输入最大外部连接数（前驱/后继）。
3. 输入 **Position in %**（0–100），用于自动连接（要求间距 ≤ 3 像素）。
4. 已连接时显示其 **Type**（Entrance / Exit）。
5. 可在 **Exit** 选项卡选择出口策略。

---

## 11. 用 EventController 控制仿真

**EventController** 协调并同步仿真运行中的事件，把事件及时间写入**计划事件列表**。

**插入**：从 `MaterialFlow`（类库）、Material Flow 工具栏，或 Home 选项卡按钮。

### 时间显示
- **相对时间**：仿真开始时归零（默认）。
- **当前时间 + 仿真时间**：在起始时间/日期基础上累加仿真时间。

### 仿真控制
- **Initialize / Start-Stop Simulation**：先执行所有名为 `Init` 的方法。
- **Reset Simulation**：调用所有名为 `Reset` 的方法，删除未处理事件、时间归零、重置统计、清除暂停/故障。
- **启动**：点击 **Start/Stop Simulation**，或按住 `Shift` 双击 EventController。
- **无动画全速启动**：**Start Fast Forward Simulation**。
- **停止**：再次点击 **Start/Stop Simulation**。
- **全速带动画**：**Start Full Speed Simulation**。
- **逐步执行**：**Single Step Simulation**（处理下一个事件后停止）。
- **打开事件调试列表**：点击 **List**。

### 计划事件列表列
| 列 | 说明 |
|---|---|
| Breakpoint | `S` 表示断点（双击单元格插入） |
| Type | 事件类型，如 `Out`、`Pause`、`PauseEnd` |
| Time | 计划执行时间 |
| Receiver | 接收事件的对象 |
| Sender | 发送事件的对象 |

### 速度与实时模式
- 拖动滑块或按方向键调整速度。
- 实时模式：输入 **Scaling Factor** 缩放因子，设定两事件间的实际时长（时长 = 仿真时间 ÷ 缩放因子）。

---

## 12. 仿真设置

在 EventController 的 **Settings** 选项卡中设置：

- **时间显示**：相对时间（默认）或当前时间 + 仿真时间。
- **日期和时间**：绝对时间的基准。
- **End time（结束时间）**：仿真运行的相对时长，仿真时间到达该值即停止。
- **Statistics reset time（统计重置时间）**：从该时间起重新开始收集统计数据。

---

## 13. 事件调试器

**Event Debugger** 在 **Single Step Simulation** 下精确控制事件执行，支持设置停止条件。

1. 打开 EventController，在 **Controls** 选项卡点击 **List**（事件按时间升序显示类型、时间、接收者、发送者）。
2. 双击单元格插入/删除单个断点（处理该事件前立即停止）。
3. 选中 **Breakpoints Active**。
4. 点击 **Breakpoints** 打开已定义断点列表，点击 **Insert** 添加断点。
5. **Trace File**：输入文件名并勾选以跟踪所有事件。
6. **Stop at Selected Event**：将选中事件添加为断点。
7. **Single Step Simulation**：处理一个事件后停止；**Start/Stop Simulation** 运行到下一个断点。

**示例**：跟踪指定 MU 的全部 `Out` 事件；为某 Station 所有离开的 MU 设断点；按类 + 时间跨度设断点；按属性条件设断点；用跟踪文件记录零件路线。

> 任意事件类型均可用于断点，不限于 `Out` 事件。

---

## 14. 删除零件

- **删除单个 MU**：选中后按 `Delete`。
- **删除所有 MU**（当前 Frame 及其子 Frame）：点击 Home 选项卡的 **Delete MUs**。
- **重置时删除 MU**：在名为 `reset` 的方法中写入 `deleteMovables`。

> 若模型中仍有零件，请检查其他含 EventController 的 Frame 并一并重置。

---

## 15. 拖放操作

拖放在 Plant Simulation 中有多种用途：

- 从类库向 Frame 插入对象。
- 将对象（Broker、ShiftCalendar、控制方法、表等）拖入对话框文本框 —— 默认插入**相对路径**（相对使用该路径的对象的 Frame）；按住 `Shift + Ctrl` 插入**绝对路径**。
- 在路径前加 `*` 使用**对象引用**代替绝对路径，如 `*.Models.FinePositioningAGV.Broker`。
- 按住 `Ctrl` 拖到类库其他位置可**复制/派生**对象创建新类。

### 为多个对象使用拖放控件

支持对多个对象的拖放（以**数组**参数接收），包括 AttributeExplorer、Method、Chart、HtmlReport、Cycle、ShiftCalendar、LockoutZone 等。

**示例流程**：
1. 插入并连接物料流对象（Source、Station、Conveyor、Drain）。
2. 插入 Frame 并重命名（如 `MyFrame`）。
3. 打开 Frame，点击 Home 选项卡的 **Edit Controls**。
4. 右键 **drag-and-drop**，选择 **Create Control**。
5. 修改源代码，用 `param draggedObjects: object[]` 接收拖入对象数组并遍历处理。
6. 选中生产线拖到 Frame 上松开，Console 显示拖入对象。
7. 添加 `debug` 打开方法调试器，在 Variables 选项卡查看 `draggedObjects` 数组。

---

## 相关主题

- 层次化建模、使用 Frame
- 在类库中显示 Frame 内容
- Frame 之间的模型转换
- 层次化结构模型中的报告显示
- 自动连接长度导向对象
- 3D 撤销/重做
- 站点间传送零件
- 事件调试器
- SimTalk 中的对象路径
- 图标编辑器 / 方法编辑器 / 列表与表 / 图表中的拖放
- DataTable 数据处理
- TransferStation 配置
- 用户自定义属性（概述）
- 创建用户自定义属性作为工具提示
