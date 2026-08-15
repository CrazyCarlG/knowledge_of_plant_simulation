# General — 流体对象共享属性（Shared Properties of Fluid Objects）

本目录汇总了 Plant Simulation 流体对象（Fluid Objects）的通用（General）共享属性说明。内容来源于本目录下的 `general.md`（其原始文本见 `general.txtx`）。本目录没有子文件夹，因此没有其他子目录 `README.md` 需要汇总。

## 概述

Plant Simulation 的资源对象用于表示 Workers 及与它们执行任务相关的对象。

> 查看示例模型：点击 Window 功能区选项卡，选择 **Start Page > Getting Started > Example Models > Small Examples**，在 *Examples Collection* 对话框中选择对应的 Category、Topic 和 Example，然后点击 **Open Model**。

## 共享属性（Shared Properties）

流体对象共享以下属性：

- 流体对象的对话框项（Dialog Items of the Fluid Objects）
- 流体对象的方法（Methods of the Fluid Objects）
- 流体对象的只读属性（Read-Only Attributes of the Fluid Objects）
- 流体对象的属性（Attributes of the Fluid Objects）

对象特有的属性请参见各对象对应的子章节。

## 流体对象的对话框项（Dialog Items of the Fluid Objects）

流体对象共享若干对话框项和菜单。双击对象图标可打开其对话框。

- 打开对话框后，Plant Simulation 会显示当前值；可在文本框中输入新设置或从下拉列表中选择。点击 **OK** 或 **Apply** 接受更改并更新对话框，也可按 **F5** 在部分选项卡上显示仿真运行的最新结果。
- 要在 3D 模型中编辑对象的 3D 属性，选中对象并按**空格键**，然后在 *Edit 3D Properties* 对话框中修改设置。
- 要操作对象的图形，点击 Edit 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

### 共享的对话框项和菜单

- Inheritance [general description]
- Name [general description]
- Label [general description]
- Failed [check box] - material flow objects
- Paused/Planned/Unplanned [material flow objects]
- Entrance Locked [material flow objects]
- Exit Locked [material flow objects]
- Tab Set-Up [general description]
- Tab Failures [general description]
- Tab Controls [general description]
- Tab Exit [general description]
- Tab Statistics [material flow objects]
- Tab Importer [general description]
- User-defined Attributes [general description]
- OK / Cancel / Apply
- Navigate Menu
- View Menu
- Tools Menu
- Context Menu of Text Boxes in Dialogs
- Help Menu
- Tab Times [general description]
- States of the Material Flow Objects

## Entrance Locked（入口锁定）[fluid objects]

勾选此复选框可关闭流体对象的入口。若锁定流体对象的入口，则材料无法流入该对象。

- **备注：** 默认情况下，Plant Simulation 将入口被锁定的流体对象的 State Graphic [defined] 显示为一根杆上的青色圆环。
- **SimTalk：** `EntranceLocked [SimTalk]` — fluid objects

## Exit Locked（出口锁定）[fluid objects]

勾选此复选框可关闭流体对象的出口。若关闭流体对象的出口，Plant Simulation 会阻止材料流出。

- **SimTalk：** `ExitLocked [SimTalk]` — material flow objects

## Tab Statistics（统计选项卡）[fluid objects]

流体对象在 **Statistics** 选项卡上显示最重要的统计数据。

- **备注：** Waiting、Working、Blocked、Setting-Up、Failed、Stopped、Paused 和 Unplanned 的值应合计为 100%。

| 项目（英文） | 项目（德文） | 说明 |
| --- | --- | --- |
| Working | Arbeitend | 显示统计收集期间流体对象处于 Working（工作）状态的时间占比。 |
| Setting-up | Rüstend | 显示统计收集期间流体对象处于 Setting-up（设置/换装）状态的时间占比。 |
| Waiting | Wartend | 显示统计收集期间流体对象处于 Waiting（等待）状态的时间占比。 |
| Blocked | Blockiert | 显示统计收集期间流体对象处于 Blocked（阻塞）状态的时间占比。 |
| Failed | Gestört | 显示统计收集期间流体对象处于 Failed（故障）状态的时间占比。 |
| Paused | Pausiert | 显示统计收集期间流体对象处于 Paused（暂停）状态的时间占比。 |
| Unplanned | Ungeplant | 显示统计收集期间流体对象处于 Unplanned（未计划，即统计收集期间未被安排工作）状态的时间占比。 |

并非所有流体对象都提供上述全部统计值，部分流体对象还提供额外值，详见各对象的相应章节。

要查看固定资源（Stationary Resources）的资源统计信息（Resource Statistics），在对象对话框中选择 **View > Show Statistics Report**；也可在 Frame 中点击鼠标右键选择 **Show Statistics Report**，或按 **F6**。

## Navigate Menu（导航菜单）

相关命令在 Navigate Menu 中说明。

## View Menu（视图菜单）

View Menu 提供访问其功能的命令：

- Refresh [on View menu]
- Show Attributes and Methods [on View menu]
- Contents [material flow objects]
- Associated Lockout Zones
- Associated Shift Calendar
- Exit Blocking List (Portioner)
- Forward Blocking List (DePortioner)

View Menu 还提供以下与 Transport Importer 相关的命令：

- Exporters [on View menu]
- Services [on View menu]
- Unavailable Services [on View menu]
- Associated Workplaces [on View menu]

## Tools Menu（工具菜单）

相关命令在 Tools Menu 中说明。

## Help Menu（帮助菜单）

相关命令在 Help Menu 中说明。

## 流体对象的方法（Methods of the Fluid Objects）

流体对象提供：

- 所有对象的方法（The Methods of All Objects）。
- 定义故障的方法（The Methods for Defining Failures）。
- Importer 的方法（The Methods of the Importer）。

各对象的子章节列出了流体对象的其他方法。

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods** 窗口。在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类（Class）的方法、只读属性和属性。
