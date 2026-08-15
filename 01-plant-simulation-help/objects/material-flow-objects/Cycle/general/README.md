# Cycle（对象）— General 总结

本目录存放 **Cycle**（平衡线 / 节拍同步）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. Cycle 对象概述

**Cycle** 用于在一条**平衡线（balanced line）**中，仅当所有工位都已完成其工件的加工、且没有任何工位处于故障（failed）、暂停（paused）或非计划（unplanned）状态时，才把工件移动到下一个工位。此外，平衡线的**后继对象**必须已准备好接收该工件。

- 平衡线的定义：在 **First Station（首工位）** 与 **Last Station（末工位）** 文本框中输入名称。首、末工位之间所有通过 **Connector** 连接的工位共同构成平衡线。
- 每个工位必须有且仅有一个前驱和一个后继。

## 2. 注意事项

- 目前只有 **Station** 和 **AssemblyStation** 类型的对象可以成为平衡线的一部分。若平衡线中包含 AssemblyStation，则只有当**装配过程完成**后，Cycle 才会继续平衡。
- **Front-triggered Exit Control（前触发出口控制）** 只对 Cycle 所定义的平衡线的**末工位**调用，因为其余工位的目标（Destination）已经确定。此时应改用 **Rear-triggered Exit Control（后触发出口控制）**。
- 对于 Cycle 的工位，**不会**调用 **Pull Control（拉动控制）**。
- 可在仿真模型中插入任意多个 Cycle 对象，它们彼此独立工作。使用多个 Cycle 对象时，确保每个工位只分配给一个 Cycle 对象。

## 3. 通过拖放定义平衡线

- 尚未定义平衡线工位时：将 Station 或 AssemblyStation 拖放到 Cycle 图标上，Plant Simulation 会将其设为平衡线的**首工位**。
- 将另一个对象拖放上去，Plant Simulation 会将其设为**末工位**。
- 已定义末工位后若要更改：按住 **Shift**，将希望用作末工位的对象拖放到 Cycle 上。状态栏会提示正在设置的对象。
- 将鼠标悬停在 Cycle 上可查看相关工具提示。

## 4. 图形操作与添加到仿真模型

- 图形操作：点击编辑功能区标签页的 **Show Manipulators**（或按 `M`）可更改 Cycle 图形的长度与锚点。
- 添加到模型：Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > Cycle`。
- 示例模型：Window 功能区标签页 → `Start Page > Getting Started > Example Models > Small Examples`，选择相应 Category、Topic 与 Example，点击 **Open Model**。

## 5. Cycle 对话框

双击 Cycle 图标打开对话框。

### 编辑仿真属性

在对话框中可修改对象的仿真属性，共享属性见 *Dialog Items of the Objects*。

### 编辑动画属性 / 3D 属性

在 *Edit 3D Properties* 对话框中编辑 3D 属性：

- 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮。
- 或选中模型中的对象并按空格键。

图形操作：点击编辑功能区标签页的 **Show Manipulators**，或按 `M`。

## 6. 选项卡 Attributes（属性）

该选项卡提供 Cycle 对象的设置项，共享属性见 *Tab Attributes*。

### Active（激活，复选框）

选中以同步工位间 MU 的传递；清除以停用平衡线。

- **说明：** 同步后，仅当所有工位都完成其工件加工、且没有工位故障/暂停/非计划时，工件才会被移动到平衡线中的下一工位。
- **SimTalk：** `Active`

### First Station（首工位）

输入希望平衡的工位组的首工位名称，或点击省略号按钮在 *Select Object* 对话框中选择物料流对象。

- **说明：** 首、末工位之间所有通过 Connector 连接的工位构成平衡线。
- **SimTalk：** `GetFirstStation`、`setFirstAndLastStation`

### Last Station（末工位）

输入希望平衡的工位组的末工位名称，或点击省略号按钮在 *Select Object* 对话框中选择物料流对象。

- **说明：** 首、末工位之间所有通过 Connector 连接的工位构成平衡线。
- **SimTalk：** `GetLastStation`、`setFirstAndLastStation`

### Empty Cycle Allowed（允许空循环，复选框）

选中后，即使平衡线前驱没有准备就绪可移动的工件，也允许平衡工位上的工件继续前移，从而产生一个**空循环（idle cycle）**。

- **SimTalk：** `EmptyCycleAllowed`

### Part Can Only Enter on Cycle（仅循环时允许工件进入，复选框）

选中后，工件只有在 Cycle 将所有 MU 向前移动一个工位（即循环为空）时才能进入 Cycle。

- **说明：** 清除该复选框可允许工件随时进入 Cycle。
- **SimTalk：** `EntranceOnlyOnCycle`

## 7. 选项卡 Statistics（统计）

统计按 *Tab Statistics* 说明描述。查看 Stationary Resources 的资源统计：`View > Show Statistics Report`，右键 Frame 选择 **Show Statistics Report**，或按 `F6`。

**参见：** *Resource Statistics [check box]*、*Resource Type*。

## 8. 选项卡 User-defined（用户自定义）

按 *Tab User-defined* 说明定义自定义属性。

## 9. 菜单

- **Navigate 菜单：** 命令见 Navigate Menu 说明。
- **View 菜单：** 提供 `Refresh`、`Show Attributes and Methods`（SimTalk：`updateDialog`）。
- **Tools 菜单：** 命令见 Tools Menu 说明。
- **Help 菜单：** 命令见 Help Menu 说明。

## 10. Cycle 的方法

Cycle 对象提供：

- 方法 `setFirstAndLastStation`；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

查看方式：打开 **Show Attributes and Methods** 窗口（在类库上下文菜单中选择，或按 `F8` / 点击 Frame 的 Home 标签页上的 **Show Attributes and Methods**）查看全部方法、只读属性和属性。

## 目录说明

- `general.md`：Cycle 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
