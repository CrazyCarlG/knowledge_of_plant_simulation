# General（概述）

> 本目录说明 Plant Simulation 的「显示对象与用户界面对象」（Display and User Interface Objects）。
> 内容来源：`general.md`（原始数据见 `general.txtx`）。

## 概述

Plant Simulation 提供两类对象：

- **显示对象（Display Objects）**：用于展示仿真运行的结果。
- **用户界面对象（User Interface Objects）**：用于接收仿真模型使用者的输入。

## 可用对象一览

| 对象 | 用途 |
| --- | --- |
| **Button** | 在 Frame 中显示按钮；点击按钮时执行你在 control 中编写的动作。 |
| **Chart** | 呈现当前数据及仿真运行结果。 |
| **Checkbox** | 在开/关两种状态之间切换，用于切换运行模式等。 |
| **Comment** | 显示你添加到仿真模型中的说明性注释。 |
| **CostAnalyzer** | 分析各台机器以及 Worker 所产生的成本。 |
| **Dialog** | 为对象设计对话框，效果类似内置对话框。 |
| **Display** | 呈现当前数据及仿真运行结果。 |
| **GanttChart** | 以时间轴上的条形图展示活动的时间顺序。 |
| **DropDownList** | 在 Frame 中显示下拉列表；选中某项时执行你在 control 中编写的动作。 |
| **HtmlReport** | 以报告形式呈现当前数据及仿真运行结果，可与同事和客户共享。 |
| **SankeyDiagram** | 可视化零部件的 Sankey 流，以及在区域内自由行走或沿 FootPath 行走的 Worker 的 Sankey 流。 |

## Comment 对象说明

`Comment`（注释）对象用于在仿真模型中添加说明性注释。

- **作用**：帮助你和同事更好地理解模型的设计意图及其工作方式。
- **使用方式**：可以像访问其他对象一样访问它，但 Comment 通常不参与仿真本身。
- **显示方法**：在 Frame 的 View 功能区选项卡中选择 **Options > Show Comments**，或点击相应工具栏图标，即可显示插入到该 Frame 中的所有 Comment 对象。Plant Simulation 会在 Frame 窗口中显示你在 **Display > Text** 下输入的文字。

## 相关参考

- SimTalk
- `openRead` [SimTalk]
- Import Method [XML Interface]
