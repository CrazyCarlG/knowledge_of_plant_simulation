# Mixer — 概述

本文件汇总了 `general` 目录下 Markdown 文档（`general.md`）的内容。该目录无子文件夹，因此不包含子目录中的 README.md。

> 对象 **Mixer** 用于将生产过程中的各种原料（ingredients）混合，转化成中间产品或最终成品。

## 说明（Description）

- 原料可以同时从多个前置 **FluidSource** 或 **Tank** 流入 Mixer。
- 若在 **MaterialsTable** 中定义了产品的原料，Mixer 只使用已定义的原料；当混合容器中相应原料达到所需数量时即开始混合。
- 若未定义原料，Mixer 会接收所有来自连接 Pipe 的物料，并在混合容器装满后开始混合。
- 加工完成后产品流出；Mixer 再次排空后开始“恢复时间”（recovery time），用于冲洗、清洁并为下一过程做准备。
- 将鼠标悬停在 Mixer 上可显示工具提示；在 Edit 功能区点击 **Show Manipulators** 或按 `M` 键可调整图形长度与锚点。

### 添加到仿真模型

点击 Home 功能区的 **Manage Class Library > Basic Objects > Fluids > Mixer**。

## 对话框（Dialog Box）

双击 Mixer 图标打开其对话框。

- **Edit Simulation Properties**：修改对象的仿真属性。
- **Edit Animation Properties**：在 **Edit 3D Properties** 对话框中编辑对象的 3D 属性（通过仿真属性对话框左下角的按钮，或选中对象后按空格键）。

## 属性选项卡（Tab Attributes）

- **Outflow Rate**：物料流出对象并经 Pipe 流向下一对象的速度，单位为升/秒。当前出流速率与所连接的 Pipe 数量有关（连接两条 Pipe 时，每条 Pipe 都会按该速率流出，前提是连接 Pipe 的出流速率允许）。
- **Volume**：混合容器内可供原料或产品使用的容量（升）。
- **Product**：Mixer 要生产的中间产品或成品名称，需在 MaterialsTable 中指定。
- **Product Amount**：要生产的产品数量（升）。默认值 `-1` 表示成品完全利用 Mixer 的容积；若与 MaterialsTable 中的 Product Amount 不同，Plant Simulation 会按比例调整各原料用量以保持配比。
- **Materials Table**：存储 Mixer 可混合的各种物料数据（可通过省略号按钮选择，或从 Frame 拖入）。
- **Current Fill Level**：显示混合容器当前的填充液位（出流侧的物料液位）。
- **Current Amount**：显示当前位于混合容器中的产品数量。
- **Current Inflow Rate**：每秒流入 Mixer 的物料升数。
- **Current Outflow Rate**：每秒流出 Mixer 并经 Pipe 流向下一对象的物料升数。

## 时间选项卡（Tab Times）

按 “Tab Times” 所述定义时间。从下拉列表选择分布并输入所需数值；也可选择常量时间（`Const`）。可用方法 `setTypeAndAttr`（SimTalk）设置分布类型及完整参数集。

## 故障选项卡（Tab Failures）

按 “Tab Failures” 所述定义故障。

## 控制选项卡（Tab Controls）

提供用于修改对象内置行为的控件。

- **选择现有 Method 的路径**：点击省略号按钮导航并选择 Method，或在 Frame 中拖动 Method 到文本框。
- **创建作为对象方法的控件（Control）**：输入名称后选择 **Create Control**，或对空文本框选择 **Create Control**，Plant Simulation 会插入 `self.<控件名>` 或 `self.On<内置控件名>`。
- **Ingredient Complete Control**：当配方中的某种原料已完全到达 Mixer 时被调用，可通过 SimTalk 定义/启动仿真模型中需要发生的任何动作；即使最后一种原料到达时 Mixer 恰好达到所设 Volume，也会被调用。

## Shift Calendar

选择 **ShiftCalendar**，其中包含班次数据，用于控制 Mixer 在哪些班次工作。选中后会自动将该对象加入 ShiftCalendar 的 Resources 选项卡对象列表。

## 统计选项卡（Tab Statistics）

除 “Tab Statistics” 所述通用值外，Mixer 还显示以下对象特有值：

| 项目（英文） | 说明 | 只读属性 | 项目（德文） |
|---|---|---|---|
| Total Throughput | 流经 Mixer 的产品数量 | `StatDeleted`（Drain） | Gesamtdurchsatz |
| Relatively Empty | 统计周期内 Mixer 处于空状态的时间占比（相对可用时间） | `StatRelativeEmptyPortion` | Relativ leer |

## Importer 选项卡（Tab Importer）

用于定义处理零件、为特定类型零件设置工位以及维修工位的服务。可通过 **View > Show Statistics Report**、右键菜单或 `F6`、或 Home 功能区按钮查看 Importer 统计报告。

## 用户自定义选项卡（Tab User-defined）

按 “Tab User-defined” 所述定义自有属性。

## 菜单（Menus）

- **Navigate Menu**：见 Navigate Menu 说明。
- **View Menu**：提供访问其功能的命令，包括与 Transport Importer 相关的命令（Exporters、Unavailable Services、Services、Associated Workplaces）。
- **Tools Menu**：见 Tools Menu 说明。
- **Help Menu**：见 Help Menu 说明。

## Mixer 的方法（Methods）

Mixer 提供：

- 左侧目录中列出的方法。
- 流体对象（Fluid Objects）的方法。
- 所有对象（All Objects）的方法。

可通过 **Show Attributes and Methods** 窗口查看全部方法、只读属性和属性（在 Class Library 上右键选择，或按 `F8` / 点击 Frame 的 Home 功能区按钮）。

## SimTalk 参考

### Underrun [SimTalk]

设置当 `<Path>` 指定的 Tank 中的物料量低于传感器位置（即位于传感器位置之下）时，是否触发传感器。

- **类型**：属性（Attribute）
- **语法**：`<Path>.Sensors.ID<Number>.Underrun:boolean`
- **赋值**：可赋布尔值。

```simtalk
MyTank.Sensors.id1.Underrun := true
```

另见：Underrun（复选框）、Mixer。
