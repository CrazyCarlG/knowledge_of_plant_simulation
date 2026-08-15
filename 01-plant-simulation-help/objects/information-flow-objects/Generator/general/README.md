# Generator — General

本目录总结 **Generator（生成器）** 对象的一般性说明，内容来源于 `general.md`（`general.txtx` 为其同内容的文本版本）。

## 概述

Generator 对象用于指定时间，既可以指定为**固定间隔**，也可以指定为**概率分布**。此外，还可以将概率分布限制在整个范围的某个区间内。

- 将鼠标悬停在 Generator 上，可显示其信息提示框。
- 在 Edit 功能区选项卡上点击 **Show Manipulators** 或按键盘 **M** 键，可更改图形长度和锚点。

## 将对象添加到仿真模型

在 Home 功能区选项卡上点击：

> Manage Class Library > Basic Objects > InformationFlow > Generator

## Generator 的对话框

双击 Generator 图标即可打开其对话框。

- **编辑仿真属性**：在对话框中可更改对象的仿真属性，共享属性见 **Dialog Items of the Objects**。
- **编辑动画属性**：通过对话框 **Edit 3D Properties** 编辑 3D 属性，方式为点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮，或选中模型中的对象后按空格键。

## Tab Times（时间选项卡）

按 **Tab Times** 中的说明定义时间。从下拉列表中选择分布，并在文本框中输入该分布所需的值；Plant Simulation 会沿选项卡上边框显示参数。也可选择常量时间（**Const**）。

可使用方法 `setTypeAndAttr [SimTalk]` 设置分布类型及完整参数集。

**字段说明：**

| 字段 | 说明 |
| --- | --- |
| **Active**（复选框） | 选中以激活 Generator，清除以停用。SimTalk: `Active [SimTalk] - Generator` |
| **Start**（文本框） | Generator 首次激活 Interval Control 的时间。输入 `0` 且 Interval 大于 `0` 时，仿真开始后立即触发控制。 |
| **Stop**（文本框） | Generator 最后一次激活 Interval Control 的时间。Interval 与 Duration 始终成对出现，因此 Duration Control 可能在此时间之后仍被激活；若不对激活设置时间限制，输入 `0`。 |
| **Interval**（文本框） | 两次 Interval Control 激活之间的时间间隔。输入 `0` 表示不触发任何控制并停止 Generator。 |
| **Duration**（文本框） | 激活 Interval Control 到 Duration Control 之间的时间跨度。 |

以上时间字段均可选择概率分布并输入其参数，也可通过 `setTypeAndAttr` 设置分布类型与参数集，例如：

```java
Generator.Start.setTypeAndAttr("Normal", 30, 10)
Generator.Stop.setTypeAndAttr("Normal", 1:00, 10)
Generator.Interval.setTypeAndAttr("dEmp", Table)
Generator.Duration.setTypeAndAttr("cEmp", Table)
```

## Tab Controls（控制选项卡）

提供用于修改对象内置行为的控件，包括 **Interval Control** 和 **Duration Control**。

**选择已有 Method 的路径**：点击省略号按钮，在 **Select Object [for controls]** 对话框中定位 Method 并点击 OK，或从 Frame 中拖放 Method 到文本框。按 **F2** 打开 Method 并输入源代码。

**创建对象自身的 Method 控制**：输入有意义的名称并选择 **Create Control [context menu]**（插入如 `self.A1Ctrl`），或在空文本框上选择 **Create Control**（插入如 `self.OnEntrance`）。之后编辑源代码的方式：按 **F2**、按住 **Shift** 双击文本框、在上下文菜单中选择 **Open Object**，或在 **User-defined** 选项卡中双击 Method 名称。删除控制时需删除用户自定义属性（仅删除文本框中的名称不会删除属性）。

- **Interval Control**：按指定的 Interval 间隔调用。SimTalk: `IntervalCtrl [SimTalk]`。
- **Duration Control**：在 Interval 触发后、经过指定 Duration 时间跨度后调用。Duration Control 在 Interval Control 之后被调用，且可能在 Stop Time 之后最后一次被激活。SimTalk: `DurationCtrl [SimTalk]`。

## Tab User-defined（用户自定义选项卡）

按 **Tab User-defined** 中的说明定义自己的属性。

## 菜单

- **Navigate Menu**：命令见 **Navigate Menu**。
- **View Menu**：提供 Refresh 与 Show Attributes and Methods 等命令。SimTalk: `updateDialog [SimTalk]`。
- **Tools Menu**：提供 Edit Controls、Edit Observers 命令。
- **Help Menu**：命令见 **Help Menu**。

## Generator 的方法

Generator 提供 **Methods of All Objects**。要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 可查看所选 Class 的内容。
- 在插入实例的 Frame 中按 **F8** 键或点击 Home 功能区选项卡上的 **Show Attributes and Methods** 可查看所选 Instance 的内容。

方法语法行示例：

```java
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## 相关参考

Interval Control、Duration Control、Probability Distributions、Empirical Distributions、User-defined Distributions。
