# Interactive Controls, State Toggles, Actions（交互控件、状态切换与动作）总结

本目录对应 Plant Simulation 帮助文档中 **切换状态与执行动作（Toggling States and Executing Actions）** 章节，介绍如何通过 **Checkbox（复选框）**、**Button（按钮）** 和 **Drop-down List（下拉列表）** 等交互控件在仿真模型中切换状态、执行动作以及选择选项，从而快速、便捷地访问模型中的各项设置。

源文件：`interactive-controls-state-toggles-actions.md`（同名文本提取版：`interactive-controls-state-toggles-actions.txtx`）。本目录无子文件夹，因此无子文件夹 README.md。

---

## 1. 显示更长或更短的时间区间

所显示的资源状态，指的是当前被所显示零件（part）占用的资源。

| 目标 | 操作 |
|---|---|
| 显示更长的时间区间（放大视图） | 按住 `Ctrl` 并按 `-` 键，或向后滚动鼠标滚轮 |
| 显示更短的时间区间（缩小视图） | 按住 `Ctrl` 并按 `+` 键，或向前滚动鼠标滚轮 |
| 以更大步长改变区间 | 在按住 `Ctrl` 的同时再按住 `Shift` |
| 返回默认缩放倍率 | 按住 `Ctrl` 并按 `0` 键 |

---

## 2. 切换状态与执行动作（总览）

有时需要在仿真模型中切换开/关状态或不同运行模式；也可能希望通过点击模型中的按钮来执行某个动作——例如一键打开某张表或某个方法，而不必在 Frame 中导航到该对象再双击它。

可以完成三类操作：

- 用 Checkbox 切换状态（Switch States with the Checkbox）
- 执行动作（Execute the Action）
- 从下拉列表选择选项（Select an Option from a Drop-down List）

---

## 3. 用 Checkbox 切换状态

**插入方式：** 从 Class Library 的 **UserInterface** 文件夹，或 Toolbox 的 **User Interface** 工具栏，把 **Checkbox** 插入仿真模型。

**打开对话框：** 双击 Frame 中图标右侧的名称 Checkbox。

复选框可实现两种功能：

### 3.1 点击复选框切换状态

- 点击 Frame 中 Checkbox 的图标，即可在 on / off 状态间切换。
- 要在复选框旁显示自定义说明，在文本框 **Label** 中输入（示例使用 `Motor on/off`）。
- 在 Frame 中点击复选框时，其图标从绿色（on）变为红色（off）。

### 3.2 用控件（Control）切换模式

若要让复选框在仿真模型中发生某个动作时切换模式，需在 **Control** 中编程实现：

1. 双击复选框名称，选择已编程「Checkbox 何时切换模式」逻辑的控件。
2. 示例中，名为 `MyCheckbox` 的 Checkbox 将名为 `MyState` 的 Variable 的值在 true 与 false 之间切换：

```simtalk
MyState := MyCheckbox.Value
```

点击 Checkbox 即切换状态。

---

## 4. 点击按钮执行动作

**插入方式：** 从 Class Library 的 **UserInterface** 文件夹，或 Toolbox 的 **User Interface** 工具栏，把 **Button** 插入仿真模型。

### 4.1 定义按钮外观

Plant Simulation 以多种方式在 Frame 中显示按钮：

- **内置图形与标签：** 使用内置图形加上输入的标签。可能需要调整 Width 与 Height，使标签不被截断。可按住 `Ctrl+Shift` 拖动图标一角、在文本框中输入精确值，或先拖动粗略调整再微调数值。
- **用户自定义图标：** 在图标编辑器中绘制。可在自定义图标中显示输入的标签文本。为能辨别按钮被点击，建议绘制两幅图——一幅为未点击状态、一幅为点击状态。示例中未点击图标名为 `icon3`，则点击图标名必须为 `icon3_down`。按钮不会保持按下状态，松开鼠标即返回未点击的凸起状态。
- **粘贴的图片：** 使用在图标编辑器中粘贴到新图标的图片。

**打开按钮对话框：** 右键点击按钮并在上下文菜单选择 **Open**；也可通过拖动框选（marquee）选中按钮。

**工具提示：** 默认情况下，鼠标悬停时 Plant Simulation 不显示按钮工具提示。要显示自定义工具提示，创建用户自定义属性并命名为 `Tooltip`。

### 4.2 为要执行的动作编程 Control

定义按钮外观后，还需编程点击 Button 时执行的 Control。示例使用 Factory51 示例模型中的 Start/Stop Simulation 按钮，该 Control 通过点击文本框 **Control** 中的省略号按钮并在上下文菜单选择 **Create Control** 创建。

以下源代码检查 EventController 当前是否运行：若在运行则停止仿真，否则启动仿真。

```simtalk
if root.EventController.IsRunning
   root.EventController.stop
else
   root.EventController.start
end
```

---

## 5. 从下拉列表选择选项

**插入方式：** 从 Class Library 的 **UserInterface** 文件夹，或 Toolbox 的 **User Interface** 工具栏，把 **Drop-Down List** 插入仿真模型。

示例模型中，Button、Check Box 与 Drop-down List 与用户自定义控件结合使用：

- **复选框** 激活或停用把零件移动到工厂中专用托盘（tray）的功能。
- **下拉列表** 在复选框打开时设置零件的专用目标托盘。
- 一个 **按钮** 打开 Source 据以生产零件的表。
- 一个 **按钮** 打开发送线（feeder line）的传感器控制，该控制根据复选框与下拉列表的设置把零件发送到目标托盘。

### 创建示例模型的步骤

1. 配置生产零件的 Source
2. 配置带 Sensor 和 Sensor Control 的发送线
3. 配置 Turnplate 按属性旋转零件
4. 配置 Check Box 与 Drop-down List
5. 配置打开零件表和回调方法的 Buttons

### 5.1 配置生产零件的 Source

- 标签为 **Parts In** 的 Source 按 **PartsTable** 中的设置以循环序列生产零件。
- 在列 **Attributes** 中双击相应单元格打开的生产表子表中，输入设置零件将移动到的托盘的属性。示例使用属性 `Destination` 及相应 `Tray`。
- 若复选框关闭，Source 以循环序列生产零件 **Board**，并通过物料搬运设备把板移动到目标托盘；移动零件时，回调方法（作为 Sensor Control 输入到发送线）使用零件的属性 `Destination`。

### 5.2 配置带 Sensor 和 Sensor Control 的发送线

- 发送线是物料搬运设备的一部分，用于把零件运输到目标托盘。
- 示例线长 11 米，在 10 米处创建传感器，方法 `PartDestination`（标签 `Callback`）作为 Sensor Control 输入。
- 若复选框打开，则在回调方法 `PartDestination` 中通过属性 `Items` 访问下拉列表，再按下拉列表选中的值把板移动到托盘。

```simtalk
// Apply the destination selected in the drop-down list
// named/labeled 'SelectDestination/Dedicated Destination'.
if DestinationActive.Value // destination is active
// set new destination of the part
   @.Destination := SelectDestination.Items[SelectDestination.Value]
end
```

### 5.3 配置 Turnplate 按属性旋转零件

- 发送线之后加入一个 **Turnplate** 来旋转生产出的板。
- 选择 **Strategy > MU Attribute** 与 **Attribute Type > Object**，并在 Attribute List 中输入所需值。
- 示例输入属性名 `Destination`、目标托盘名 `Tray1` 至 `Tray4`，以及板将旋转的 Angle（`90` 表示顺时针 90 度，`-90` 表示逆时针 90 度）。

### 5.4 配置 Check Box 与 Drop-down List

复选框与下拉列表协同工作：

- **复选框** 激活或停用把板移动到专用托盘。
- **下拉列表** 在复选框设为 on 后设置板的专用目标。

配置下拉列表：

- 输入 **Width** 与 **Height**（示例：宽 6 米、高 1 米）。
- 点击按钮 **Items**，输入下拉列表在 Frame 中显示的条目。
- 在文本框 **Value** 中输入默认显示的条目编号（示例：`1` 使下拉列表在收起时显示 `Tray1`）。
- 可设置标题、在 Frame 中显示并设置位置；在 **View** 选项卡上可选择显示名称、标签或两者。
- 右键点击下拉列表并选择 **Open** 可打开其对话框。

> **注意：** 仅当 Checkbox 在模型窗口中每个方向至少占 10 像素时，Plant Simulation 才接受对其的点击。若缩小太多，Checkbox 可能变得过小，导致无法被可靠识别。

若复选框打开，则在传感器的回调方法中通过属性 `Items` 访问下拉列表，再按所选值把板移动到托盘：

```simtalk
// Apply the destination selected in the drop-down list
// named/labeled 'SelectDestination/Dedicated Destination'
var l: list
l.create
SelectDestination.getItems(l)
if DestinationActive.Value then  // destination is active
// set new destination of the part
   @.Destination := l[SelectDestination.Value]
end
```

### 5.5 配置打开零件表和回调方法的按钮

配置两个按钮，以便一键打开零件表和回调方法，而无需在 Frame 中导航并双击其图标：

**Button 1** — 打开名为 `PartsIn` 的 Source 据以生产零件的表：

- 输入 Width 与 Height（示例：宽 6 米、高 1 米）。
- 输入点击时调用的 Control（使用对象自身的控件：右键点击文本框 **Control** 并选择 **Create Control**）。

```simtalk
self.~.~.PartsTable.openDialog
```

**Button 2** — 打开发送线的传感器控制，该控制根据复选框与下拉列表的设置把零件发送到目标：

- 输入 Width 与 Height（示例：宽 6 米、高 1 米）。
- 输入点击时调用的 Control（使用对象自身的控件：右键点击文本框 **Control** 并选择 **Create Control**）。

---

## 目录说明

- `interactive-controls-state-toggles-actions.md`：本章节（Checkbox、Button、Drop-down List）的 Markdown 源文件。
- `interactive-controls-state-toggles-actions.txtx`：相同内容的文本提取版。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Toggling States and Executing Actions"。Unpublished work. © 2026 Siemens.*
