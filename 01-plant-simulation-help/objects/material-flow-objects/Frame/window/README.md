# Frame（对象）— Window 总结

本目录包含 `window.md`（以及同名文本提取文件 `window.txtx`），内容为 Plant Simulation 帮助文档中 **Frame（对象）窗口** 的说明。以下是对其内容的总结。

## 1. Frame 窗口概述

**Frame 窗口**提供创建仿真模型所需的最重要功能，包含 **Frame 功能区选项卡（Frame Ribbon Tab）** 与 **系统菜单（System Menu）**。

- **Frame 自身右键菜单**：提供与 Frame 相关的命令；在 3D 模型中按空格键可在 **Edit 3D Properties** 对话框中编辑 Frame 的 3D 属性。
- **Frame 中选中对象的右键菜单**：提供与该对象相关的命令；按空格键可编辑选中对象的 3D 属性。

## 2. 建模时的拖放操作（Drag-and-Drop While Modeling）

在 Frame 中拖放对象可执行多种操作。表中 `Class Library — Class Library — object — Ctrl` 表示：按住 Ctrl 在 Class Library 内从一个位置拖到另一个位置会复制该对象。

| 操作 | 从 | 到 | 类型 | 加速键 |
|---|---|---|---|---|
| 移动对象 | Class Library | Class Library | object | Shift |
| 复制对象 | Class Library | Class Library | object | Ctrl |
| 派生对象 | Class Library | Class Library | object | Ctrl+Shift |
| 实例化对象 | Class Library | Frame | object | — |
| 移动对象（把实例变成类） | Frame | Class Library | object | — |
| 复制对象 | Frame | Class Library | object | Ctrl |
| 加载图形文件（.GIF/.BMP/.PPM/.PPM RAW/.DXF/.DWG）作为 Frame 背景 | Windows Explorer | Frame | file | — |
| 重复插入所选对象 | Class Library | Frame | object | Shift |
| 执行接收单个 object 类型参数的 Method | Frame 中的对象 | Method | object 类型参数 | — |

## 3. Frame 的系统菜单

系统菜单用于操作或关闭 Frame 窗口，其语言由 Windows 系统语言决定。命令包括：

- **Use Left Area / Use Right Area**：使用 MDI 窗口左/右侧可用区域。
- **Restore**：恢复窗口至正常大小。
- **Move**：改变 Frame 窗口位置。
- **Size**：改变 Frame 窗口大小。
- **Minimize**：最小化为任务栏图标。
- **Maximize**：最大化；此时将 Minimize/Maximize/Close 按钮组合加到 Ribbon Bar。
- **Close**：关闭 Frame 窗口。

## 4. Frame 功能区选项卡

Frame 功能区选项卡提供访问 Frame 功能的命令。

| 命令 | 方法或属性 |
|---|---|
| Find Object（查找对象） | — |
| Incremental Find Object（增量查找） | — |
| Show Unconnected Objects（显示未连接对象） | — |
| Select Shift Calendar（选择班次日历） | `ShiftCalendarObject` |
| Configure User-defined Ribbon Tab（配置自定义功能区） | 各种 |
| Inherit User-defined Ribbon Tab（继承自定义功能区） | 各种 |
| Configure User-defined Context Menu（配置自定义右键菜单） | 各种 |
| Inherit User-defined Context Menu | 各种 |
| Replacement Mode（替换模式） | `replace`、`ReplacementMode` |
| Merge / Exchange | 各种 |
| Inherit Replacement Mode | `replace`、`ReplacementMode` |
| Lock Structure（锁定结构） | `LockStructure` |

### 主要命令说明

- **Find Object**：打开“查找对象”对话框；也可在 Frame 窗口点击后直接输入对象名进行查找。
- **Incremental Find Object**：边输入边增量匹配并高亮对象。可用 **Backspace** 删除字符、**Tab** 查找下一个匹配对象、**Esc** 终止（保留当前选择）、**Return** 终止并执行对象的默认操作（如打开仿真属性对话框）。
- **Show Unconnected Objects**：高亮存在未连接出入口的对象；Frame 若某个 Interface 未连接外部也算未连接。
- **Select Shift Calendar**：设置控制 Frame 工作班次的 ShiftCalendar（SimTalk：`ShiftCalendarObject`、`Unplanned`）。

## 5. 用户自定义功能区选项卡（Configure User-defined Ribbon Tab）

在选定 Frame 中创建常用命令的自定义功能区选项卡，显示在 Frame 预定义选项卡之外；存在自定义选项卡时按钮会高亮。

可执行：为命令添加图标、创建功能区组、动态添加命令、添加命令分隔符、创建访问键。

- **Title**：设置选项卡标题（SimTalk：`UserMenuTitle`）。
- **Active**：显示/隐藏选项卡（SimTalk：`ShowUserMenu`）。
- **New / Delete**：添加/删除命令行。
- **Text to Display**：命令显示文本，可用 `?Formula`、`- Separator`、`#`、`#Group Name` 等前缀控制。
- **Method to Execute**：命令调用的 Method；被调用时匿名标识符 `?` 指向执行选择的 Frame。若 Method 有参数，自动传入所选对象（list 或 object 数组类型）。
- **Create a Ribbon Group**：用 `#` 开头的命令启动功能区组；`#` 后文本为组名。
- **Add an Icon**：图标命名可用 `命令名_16`/`命令名_32` 或 `ribbonN`，按「标签+尺寸 → 仅标签 → 独立于标签」顺序解析。
- **Dynamically Add a Ribbon Command**：以 `?Formula` 作为动态命令，返回字符串；返回空串 `""` 则隐藏命令。
- **Add a Command Separator**：用 `- Separator` 插入命令组之间的分隔符。
- **Create an Access Key**：在字母前加 `&` 设置访问键（Alt+字母）；内置访问键优先。
- **Inherit User-defined Ribbon Tab**：控制派生 Frame 是否继承来源 Frame 的自定义功能区选项卡。

### 用户自定义功能区的右键菜单

提供行编辑命令：Insert Row、Delete Row、Cut Row、Copy Row、Paste Row，以及 Ctrl+C/Ctrl+Ins、Ctrl+X/Shift+Del、Ctrl+V/Shift+Ins、F2、Shift+F2、F4、Shift+F4 等快捷键。

### 用户自定义功能区的属性

- **ShowUserMenu**（`<Path>.ShowUserMenu:boolean`）：显示/隐藏选项卡。
- **UserMenu**（`<Path>.UserMenu:table`）：两列表格，String1 为命令、String2 为执行的 Method；标题写在 DataTable 的 Comment 中。
- **UserMenuTitle**（`<Path>.UserMenuTitle:string`）：设置选项卡标题。

## 6. 用户自定义右键菜单（Configure User-defined Context Menu）

在选定 Frame 中创建常用右键菜单命令。对话框为模态。

- 用连字符 `-` 作为命令名可插入菜单分隔符。
- 自定义右键菜单仅对定义它的 Frame 内所选对象有效，Class Library 不显示。
- 在插入到其他 Frame 的 Frame 中创建时，需先停用 **Inherit**。
- **Active**：激活/停用（SimTalk：`ShowUserPopupMenu`）；激活后右键点击插入的 Frame 图标打开。
- **New / Delete**：添加/删除命令。
- **Text to Display**：命令文本，支持 `?Formula` 动态命令。
- **Method to Execute**：命令执行的 Method；可自动传入所选对象列表（list 类型）及可选的命令序号（integer）。

### 用户自定义右键菜单的属性

- **ShowUserPopupMenu**（`<Path>.ShowUserPopupMenu:boolean`）：显示/隐藏右键菜单。
- **UserPopupMenu**（`<Path>.UserPopupMenu:table`）：两列表格，String1 为命令、String2 为执行的 Method。
- **Inherit User-defined Context Menu**：控制派生 Frame 是否继承自定义右键菜单。

## 7. 替换模式（Replacement Mode）

设置合并 Frame 时 Plant Simulation 如何处理对象，控制加载 `.psobj` 文件时与 Class Library 中已有同名类之间的合并/替换行为。

- 由「替换方」Frame 的替换模式决定合并或替换；「被替换方」的替换模式无影响。

### Merge（合并）

保留被替换 Frame 实例中已更改的设置，并导入到替换对象，然后删除 Class Library 中被替换对象。仅适用于完全相同的 Frame，是默认设置。

### Exchange（交换）

将被替换对象的所有实例转换为替换对象的实例，丢弃被替换对象实例中的自定义修改，并删除 Class Library 中被替换对象。**建议交换前先保存上一版本**，因为所有更改将丢失且无法恢复。

### 示例

- **Merge Classes 示例**：从模型加载 FrameX、FrameY 到另一模型时，FrameA 已存在，选择 Merge 会保留 FrameY 中 FrameA 的修改。
- **Exchange Classes 示例**：用更新的 FrameANew 替换 FrameA 的实例时选择 Exchange；此时无法 Merge，因为 FrameA 与 FrameANew 不同。

### Inherit Replacement Mode

控制派生 Frame 是否继承来源 Frame 的替换模式。

## 8. Lock Structure（锁定结构）

锁定 Frame 结构，防止意外插入、删除、修改对象或改变对象位置与名称。

- 新模型默认关闭；实例化 Frame 中默认开启（结构修改应在类中进行，而非实例）。
- SimTalk：`LockStructure`。

## 9. Frame 自身的右键菜单

在 Frame 背景上右键打开（部分命令位于迷你工具栏），命令包括：

- Reset Simulation（重置仿真）
- Start/Stop Simulation（启动/停止仿真）
- Start Fast Forward Simulation（无动画快速仿真）
- Show Structure（显示结构）
- Show Inheritance（显示继承）
- Show Attributes and Methods（显示属性和方法）

## 10. Frame 中选中对象的右键菜单

选中对象右键打开，迷你工具栏始终提供：Open Origin、Open Class、Cut、Copy、Delete。完整右键菜单命令（部分对象可能不支持全部命令）包括：

- **Activate / Deactivate**：激活/停用对象。
- **Calculate Angles**：让 Turntable 和 PickAndPlace 机器人计算连接角度。
- **Controls**：打开在 Tab Controls 上输入的控件。
- **Create Sensor / Delete Sensor**：在长度导向对象上创建/删除传感器。
- **Edit Dialog / Edit Icons / Edit User-defined Attributes**：编辑对话框/图标/用户自定义属性。
- **Event Debugger**：打开 EventDebugger 对话框。
- **Open / Open Class / Open Origin**：打开对象对话框/类/来源类。
- **Open Comment Window / Open Debugger / Open External Connections List / Open Sensor / Open Values Table / Open Without Control**。
- **Rename**：重命名（F2）。
- **Reorder Successors**：重排后继对象顺序（不影响实例）。
- **Reset Simulation / Run / Show / Show Assigned Objects / Show Attributes and Methods / Show Dialog / Show Exported Services / Show External Connected Objects / Show Sessions Log / Show Statistics Report / Show Structure / Start-Stop Simulation / Start Fast Forward Simulation**。
- **Statistics Wizard / Type Info / Update**。

## 11. Frame 的状态

仿真运行期间，Frame 的状态以 State Graphic 中的彩色矩形显示：

| 状态 | 颜色 | 属性 |
|---|---|---|
| Failed（失败） | 红 | `Failed` |
| Stopped（停止） | 粉 | `Stopped` |
| Paused（暂停） | 蓝 | `Pause` |
| Unplanned（计划外） | 浅蓝 | `Unplanned` |
| Working（工作） | 绿 | `StateWorking` |
| Blocked（阻塞） | 黄 | `StateBlocked` |
| Setting-Up（准备） | 棕 | `StateSetup` |
| 入口关闭 | 青 | `StateEntryShut` |
| 等待服务/安装部件 | 橙 | `StateResourceMissing` |

## 目录说明

- `window.md`：Frame 窗口说明的 Markdown 版本（本总结的源文件）。
- `window.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
