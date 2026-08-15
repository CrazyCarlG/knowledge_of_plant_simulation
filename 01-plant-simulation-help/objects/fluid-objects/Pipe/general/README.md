# Pipe — General（概述）摘要

本目录汇总了 Plant Simulation 流体对象 **Pipe（管道）** 的通用（General）说明。内容来源于本目录下的 `general.md`（其原始文本见 `general.txtx`）。本目录没有子文件夹，因此没有其他子目录 `README.md` 需要汇总。

## 概述

使用 **Pipe** 对象在工厂中的其他流体对象之间输送自由流动的材料。

> 查看示例模型：点击 Window 功能区选项卡，选择 **Start Page > Getting Started > Example Models > Small Examples**，在 *Examples Collection* 对话框中选择对应的 Category、Topic 和 Example，然后点击 **Open Model**。

## 描述

插入 Pipe 以在 `FluidSource`、`Tank`、`Mixer`、`Portioner`、`DePortioner` 和 `FluidDrain` 等对象之间输送自由流动的材料。

- 材料流经 Pipe 时，Pipe 会以该材料的颜色作为其自身颜色，即你在 `MaterialsTable` 中为该材料选择的颜色。
- 必须使用 **Connector（连接器）** 建立 Pipe 与流体对象之间的连接。
- 要让材料在流体对象之间流动，必须使用 Pipe。

可以将 Pipe 插入 Frame：

- 作为曲线对象（默认设置）。
- 通过插入任意曲线段和直线段的组合，逼真地模拟流体流经的弯曲输送系统。

可以在 **Appearance** 选项卡上为 Pipe 选择不同的配置。将鼠标悬停在 Pipe 上可显示包含相关信息的工具提示。

## Show Manipulators（显示操纵点）

要更改对象的图形长度和锚点，点击 Edit 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

长度方向对象起点和终点的操纵点被截断。当你将同一类型的对象连接到另一个对象上时，两个半截的操纵点会重新组合成一个完整的操纵点。Pipe 操纵点的高度取决于 Pipe 的宽度。

## 将对象添加到仿真模型

要将 Pipe 对象添加到仿真模型中，点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > Fluids > Pipe**。

比较示例模型：点击 Window 功能区选项卡，选择 **Start Page > Getting Started > Example Models > Small Examples**，然后在 *Examples Collection* 对话框中选择相应的 Category、Topic 和 Example，并点击 **Open Model**。

## Pipe 的对话框

双击 Pipe 的图标可打开其对话框。

- **Edit Simulation Properties（编辑仿真属性）**：在对话框中更改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties（编辑动画属性）**：点击仿真属性对话框左下角的 **Edit 3D Properties**，或选中对象并按空格键。

要操作对象的图形，点击 Edit 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

## Tab Attributes（属性选项卡）

Tab Attributes 提供该对象所提供的设置。

### Outflow Rate（流出速率）[Pipe]

在文本框中输入材料从 Pipe 流向下一个对象时的 Outflow Rate。默认值 `-1` 表示 Pipe 使用与其前驱相同的流出速率。

- Outflow Rate 是材料每秒流出的升数。这适用于直接位于 `FluidSource`、`DePortioner`、`Tank` 或 `Mixer` 之后的 Pipe。
- 若输入默认值以外的值，Plant Simulation 会使用所输入的 Outflow Rate，即使它高于前驱的 Outflow Rate。这样可以实现连接到 `FluidSource`、`Tank`、`DePortioner` 或 `Mixer` 的所有后续 Pipe 不必具有相同 Outflow Rate 的效果。
- 若 Pipe 的前驱是另一个 Pipe，Plant Simulation 会忽略该值（文本框不可用）。但这不适用于 Pipe 只有一个后继、且前驱 Pipe 也只有一个后继的情况——当多个 Pipe 首尾相接排列时，Plant Simulation 对所有 Pipe 使用所指定的最低值。

**SimTalk：** `OutflowRate [SimTalk] - Pipe`

### Pipe Opened（管道开启）[复选框]

勾选此复选框以打开 Pipe 的入口，使材料能够流过；清除此复选框则关闭 Pipe。

- 通过开启/关闭 Pipe 可以模拟阀门或闸阀。
- 清除 **Pipe Opened** 后，会以青色显示 **Pipe Closed** 状态。

**SimTalk：** `PipeOpened [SimTalk]`

### Exit Strategy（退出策略）

选择 Pipe 将流量分配给后继流体对象的退出策略：

- **Evenly distributed（均匀分配）**：将流量均匀分配给各后继对象。
- **Percentage [Pipe]（按百分比分配）**：按比例分配流量。

**备注：** 选择其他策略后，点击 **Apply** 以显示属于新策略的项目。

**Percentage [Pipe] 备注：**

- 点击 **Open List**，为各个后继对象输入百分比。例如，后继 1 获得 20%，后继 2 获得 30%，以此类推。
- 在某个后继的单元格中输入 `0`，可阻止其接收材料。
- 若某个后继无法接收材料（例如后续的 Tank 已满），Pipe 会根据百分比将该后继的份额分配给其余后继。
- 百分比之和不必等于 100%。所有能够接收材料的后继的百分比实际总和对应 100%。例如 `[40, 60]`、`[0.4, 0.6]` 和 `[2, 3]` 是等价的。

**SimTalk：**

- `ExitStrategy [SimTalk] - Pipe`
- `ExitStrategyPercentageValues [SimTalk] - Pipe`

### Current Material（当前材料）[Pipe]

显示当前流经 Pipe 的材料名称。

**备注：** 名称不区分大小写，与属性和方法的名称一样。在 SimTalk 中可以使用 `~=` 运算符以不区分大小写的方式比较字符串。Pipe 以分配给该材料的颜色显示当前材料。

**SimTalk：** `CurrentMaterial [SimTalk] - Pipe`

### Current Flow Rate（当前流量）[文本框]

显示流经 Pipe 的材料的当前流量（升/秒）。

**SimTalk：** `CurrentFlowrate [SimTalk]`

## Tab Times（时间选项卡）

按 Tab Times 中的说明定义时间。从下拉列表中选择一个分布并输入所需值；也可以选择常量时间（Const）。可使用方法 `setTypeAndAttr [SimTalk]` 设置分布类型和完整的参数集。

**参见：** Set-up Time [general description]、`SetupTime [SimTalk] - fluid objects`。

## Tab Statistics（统计选项卡）

Pipe 提供 Tab Statistics 中所述的统计值。

## Tab User-defined Attributes（用户自定义属性选项卡）

按 Tab User-defined 中的说明定义自己的属性。

## Navigate Menu / View Menu / Tools Menu / Help Menu（导航/视图/工具/帮助菜单）

相关命令在各自菜单中说明。

**SimTalk（View Menu）：** `updateDialog [SimTalk]`

## Pipe 的方法（Methods of the Pipe）

Pipe 提供所有对象的方法（Methods of All Objects）。要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods**（F8，或 Class Library 的上下文菜单）。

单个方法语法行示例：

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## SetupTime [SimTalk] - fluid objects

设置由 `<Path>` 指定的流体对象的 Set-up Time（换装时间）。

**备注：** 当下一种材料的名称与前一种材料的名称不同时，流体对象必须进行换装。Set-up Time 是将对象设置为可处理不同类型材料所需的时间。名称相同表示材料属于同一类型。

- **类型：** Attribute
- **语法：**

```simtalk
<Path>.SetupTime:time
```

- **赋值类型：** 可赋值 `time` 数据类型。
- **示例：**

```simtalk
MyMixer.SetupTime := 120 -- 2 minutes
```

- **参见：** Set-up Time [general description]、Times and Distributions、Pipe。
