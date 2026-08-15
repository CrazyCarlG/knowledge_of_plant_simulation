# AngularConverter — General（概述）

本目录存放 **AngularConverter**（转角转换器）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. AngularConverter 对象概述

**AngularConverter** 是物料流中用于**改变 MU 传送方向**的对象，其传送方向在长度方向与横向之间切换（呈转角/L 形）。AngularConverter 一次只能容纳**一个部件（MU）**。

AngularConverter 在物料流中把 MU 移动到后继对象的流程如下：

- MU 移动到 AngularConverter 的**第一段（first leg）**上。一旦 **Booking Point Length（定位点长度）**到达 AngularConverter 的入口，MU 便以 **Entry Speed（入口速度）**沿 **Entry Length（入口长度）**移动，直到 Booking Point Length 到达传送方向改变的位置。在此处 MU 触发 **Moving Time（移动时间）**并改变传送方向。
- 此时 MU 必须完全位于 AngularConverter 的第一段上。为使第一段能完全容纳进入的 MU，**MU Length** 与 **Booking Point Length** 之差不得大于 **Entry Length**。
- 从此处到出口点的所有计算（例如退出对象所需的时间）随后都使用 **MU Width（MU 宽度）**。
- Part（零件）上的**缺口（notch）**标识其右侧。

### 传送方向（Conveying direction）

| 传送方向 | 含义 |
| --- | --- |
| **Forward（正向）** | MU 以前部朝向物料流运动方向移动；改变传送方向后仍保持该方向，即其前部不再指向物料流方向。 |
| **Lateral right（右横向）** | MU 以右侧朝向运动方向移动；改变传送方向后仍保持该方向，即其前部不再指向物料流方向。 |
| **Backward（反向）** | MU 旋转 180°，逆着运动方向向后移动；改变传送方向后仍保持该方向，即其前部不再指向物料流方向。 |
| **Lateral left（左横向）** | MU 以左侧朝向运动方向移动；改变传送方向后仍保持该方向，即其前部不再指向物料流方向。 |

> **注：** Container（容器）和 Part（零件）在其对话框中显示 **Conveying Direction（传送方向）**。

**Moving Time 用尽且 MU 改变传送方向后**，MU 继续移动到 AngularConverter 的**第二段（second leg）**上：MU 以 **Exit Speed（出口速度）**沿 **Exit Length（出口长度）**移动，直到 **Booking Point Width（定位点宽度）**到达 AngularConverter 的出口。一旦 MU 完全离开 AngularConverter，会再次触发 Moving Time，使 AngularConverter 回到其初始位置。Moving Time 过去后，下一个 MU 才能进入。

为使第二段能完全容纳离开的 MU：

- MU **左转**时，**MU Width** 与 **Booking Point Width** 之差不得超过 **Exit Length**。
- MU **右转**时，**Booking Point Width** 的值不得超过 **Exit Length**。

其他操作：

- 在 **Appearance（外观）**选项卡上可选择 AngularConverter 的不同配置。
- 将鼠标悬停在 AngularConverter 上可显示工具提示。
- 点击 Edit 功能区标签页的 **Show Manipulators**（或按 `M`）可更改图形长度和锚点。
- 添加到模型：Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > AngularConverter`。
- 示例模型：Window 功能区标签页 → `Start Page > Getting Started > Example Models > Small Examples`。

**See also：** Change the Conveying Direction with the AngularConverter；YouTube 视频：https://youtu.be/hOvdrDnvXXo?si=HtapSi48BgDSePJA&t=377

## 2. AngularConverter 对话框

双击 AngularConverter 图标打开其对话框。

- **编辑仿真属性（Edit Simulation Properties）：** 共享属性见 *Dialog Items of the Objects*。
- **编辑动画属性（Edit Animation Properties）：** 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮，或选中模型中的对象并按空格键；点击 **Show Manipulators**（或按 `M`）操纵图形。

## 3. 选项卡 Attributes（属性）

该选项卡提供对象所提供的设置。共享属性见 *Tab Attributes*。

### Entry Length（入口长度）[文本框]

输入 AngularConverter 第一段的长度。

> **备注：** Entry Length 覆盖从入口点到 AngularConverter 切换传送方向的位置之间的距离。

**SimTalk：** `EntryLength`

### Exit Length（出口长度）[文本框]

输入 AngularConverter 第二段的长度。

> **备注：** Exit Length 覆盖从 AngularConverter 切换传送方向的位置到 MU 离开对象的位置之间的距离。

**SimTalk：** `ExitLength`

### Width（宽度）[文本框] - AngularConverter

输入 AngularConverter 的宽度。

**SimTalk：** `Width`

### Entry Speed（入口速度）[文本框]

输入 MU 在 AngularConverter 上从入口点移动到切换传送方向位置所用的速度。

**SimTalk：** `EntrySpeed`

### Exit Speed（出口速度）[文本框]

输入 MU 在 AngularConverter 上从切换传送方向位置移动到离开对象位置所用的速度。

**SimTalk：** `ExitSpeed`

### Automatic Stop（自动停止）[复选框] - AngularConverter

勾选后自动停止 AngularConverter，即当其不运输部件时将其当前速度设为 0。

> **备注：** AngularConverter 为空、或因 MU 无法离开而被阻塞时，就会自动停止。当 AngularConverter 速度为 0 时，Energy State（能源状态）变为 Operational（运行）。

**SimTalk：** `AutomaticStop`

## 4. 选项卡 Times（时间）

按 *Tab Times* 说明定义时间。从下拉列表选择分布类型并输入所需值（参数显示在选项卡上边界）；也可选择恒定时间（**Const**）。分布类型与完整参数集可用方法 `setTypeAndAttr` 设置。

AngularConverter 额外提供 **Moving Time（移动时间）**。

**See also：** Recovery Time、Recovery Time Starts、Cycle Time。

### Moving Time（移动时间）[下拉列表] - AngularConverter

Moving Time 是 AngularConverter 在长度方向传送与横向传送之间（以及反向）切换所需的时间。

> **备注：** Moving Time 在 MU 到达 AngularConverter 切换传送方向的转角时被消耗一次；当 MU 完全离开 AngularConverter、使对象回到初始位置时再次被消耗。只有在此之后另一个 MU 才能移动到 AngularConverter 上，因为该对象一次只能容纳一个 MU。

从下拉列表为 Moving Time 选择分布，并输入该分布所需的值（参数显示在选项卡上边界）；也可选择恒定时间（**Const**）。若使用 **Formula（公式）**分布，可输入数值表达式或 Method 名称，并用匿名标识符 `@` 访问该移动时间所适用的 MU。

**SimTalk：** `MovingTime`、`MovingTime.Type`

## 5. 选项卡 Failures（故障）

按 *Tab Failures* 说明定义故障。

## 6. 选项卡 Controls（控制）

提供修改对象内置行为的控制项。

- **选择已有 Method 的路径：** 点击省略号按钮，在 *Select Object [for controls]* 中导航选择并点击 OK；在文本框中按 `F2` 打开 Method 并输入源代码；或将 Method 从 Frame 拖入文本框。
- **创建对象方法作为控制（数据类型为 Method 的用户自定义属性）：**
  - 在文本框中输入有意义名称并选择 **Create Control** —— 插入 `self.你输入的控制名`（如 `self.A1Ctrl`）。
  - 在空文本框上选择 **Create Control** —— 插入 `self.On内置控制名`（如 `self.OnEntrance`）。
- **编辑源代码：** 按 `F2`、按住 `Shift` 双击文本框、在上下文菜单选择 **Open Object**，或使用 **User-defined** 选项卡双击 Method 名称。
- **删除控制：** 需删除相应用户自定义属性（仅从文本框删除名称不会删除该属性）。

**See also：** Select Object [for controls]、Entrance Control、Exit Control、Pull Control、Shift Calendar。

## 7. 选项卡 Exit（出口）

选择对象将 MU 移动到哪个后继。

**See also：** Blocking [exit strategy]、Strategy [material flow objects]。

## 8. 选项卡 Statistics（统计）

统计按 *Tab Statistics* 说明描述。查看 Stationary Resources 的 Resource Statistics：在对象对话框中选择 `View > Show Statistics Report`，或右键 Frame 选择 **Show Statistics Report**，或按 `F6`。

**See also：** Resource Statistics [check box]、Resource Type。

## 9. 选项卡 Energy（能源）

在 *Tab Energy* 上选择对象的能源设置。

## 10. 选项卡 Costs（成本）

在 *Tab Costs* 上选择成本设置。AngularConverter 运输部件期间，成本由**总投资成本**与**总运营成本**之和累积：

> **注：** 总投资成本仅在**折旧期（Depreciation Period）**内累积。若 AngularConverter 为空，成本作为**一般成本（general costs）**保留在 AngularConverter 上。

**See also：** Simulate the Accrued Costs of the Machines、CostAnalyzer > How the CostAnalyzer Assigns Costs to Part Types、CostAnalyzer > Costs Shown in the Costs Report。

## 11. 选项卡 User-defined（用户自定义）

按 *Tab User-defined* 说明定义自定义属性。

## 12. 菜单

- **Navigate 菜单：** 命令见 *Navigate Menu* 说明。
- **View 菜单：** 提供访问其功能的命令：

  | 命令 | 相关 |
  | --- | --- |
  | Refresh [on View menu] | Backward Blocking List |
  | Show Statistics Report [on View menu] | Exit Blocking List |
  | Show Attributes and Methods [on View menu] | Associated Lockout Zones |
  | Contents [material flow objects] | Associated Shift Calendar |

- **Tools 菜单：** 命令见 *Tools Menu* 说明。
- **Tabs 菜单：** 显示/隐藏所选物料流对象的各个选项卡；隐藏不用的选项卡可加快对话框打开与切换速度。点击 **OK** 关闭并重新打开对话框以应用更改；菜单在已显示的选项卡左侧显示勾选标记；**Inherit** 命令切换显示/隐藏选项卡的继承。
- **Help 菜单：** 命令见 *Help Menu* 说明。

## 13. AngularConverter 的方法

AngularConverter 提供：

- Curved Objects（曲线对象）的方法；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

查看方式：打开 **Show Attributes and Methods** 窗口（在类库上下文菜单中选择 **Show Attributes and Methods** 查看类的方法、只读属性和属性；在插入实例的 Frame 中按 `F8` 或点击 Home 功能区标签页的 **Show Attributes and Methods** 查看实例的方法、只读属性和属性）。

## 目录说明

- `general.md`：AngularConverter 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
