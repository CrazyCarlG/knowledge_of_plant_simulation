# ContinuousMixer — General（概述）

本目录包含 Plant Simulation 中 **ContinuousMixer**（连续搅拌器 / 连续混合器）对象的通用（general）文档。该对象用于将生产过程中的各种原料（ingredients）混合，转化成中间产品或最终成品。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `general.md` | ContinuousMixer 对象的 Markdown 文档（主内容） |
| `general.txtx` | 同一内容的原始导出文本（含页码脚注，内容与 general.md 基本一致） |

> 本目录下没有子文件夹，也没有其他 README.md 文件，因此本总结基于 `general.md` 的内容整理。

## 概述

- **ContinuousMixer** 用于通过混合原料，将生产过程中的原料转化为中间产品或最终成品。
- 原料可同时从多个前置流体对象流入 ContinuousMixer。
- 仅当产品与原料信息已在 **MaterialsTable** 中定义时，ContinuousMixer 才会处理流体。
- 仅当按 MaterialsTable 中定义的正确配比收到所有原料后，ContinuousMixer 才会开始混合；若配比不正确，混合过程会立即停止。
- 流出与流入同时开始；流出量通常等于累计流入量，但若在 MaterialsTable 中相应定义配方，流出量也可以不同。
- 将鼠标悬停在 ContinuousMixer 上可显示工具提示；在 Edit 功能区点击 **Show Manipulators** 或按 `M` 键可调整图形长度与锚点。
- 添加对象：Home 功能区 → **Manage Class Library > Basic Objects > Fluids > ContinuousMixer**。

## 对话框（Dialog Box）

双击 ContinuousMixer 图标打开其对话框。

- **Edit Simulation Properties**：修改对象的仿真属性（公共属性见 “Dialog Items of the Objects”）。
- **Edit Animation Properties**：在 **Edit 3D Properties** 对话框中编辑对象的 3D 属性——通过仿真属性对话框左下角的 **Edit 3D Properties** 按钮，或选中对象后按空格键。
- 调整图形：在 Edit 功能区点击 **Show Manipulators** 或按 `M` 键。

## 属性选项卡（Tab Attributes）

- **Product [文本框]**：输入 ContinuousMixer 通过混合原料所要生产的中间产品或最终成品的名称。该产品名称需在 MaterialsTable 中指定；若产品由超过十种原料组成，可在 MaterialsTable 中增加额外原料（Add Additional Ingredients）。
- **Materials Table**：包含 ContinuousMixer 可混合的各种物料数据。可通过省略号按钮在 “Select Object” 对话框中选择，或从 Frame 中拖入文本框。若在 ContinuousMixer 的 MaterialsTable 的 **Product Amount** 列中输入 `-1`，Plant Simulation 会以所有原料之和作为 Product Amount；仅当混合会增大或减小体积（即 Product Amount 不等于原料之和）时，才需显式指定 Product Amount。
- **Shift Calendar**：选择 **ShiftCalendar**（班次日历），其中包含班次数据，用于控制 ContinuousMixer 在哪些班次工作。可通过省略号按钮选择，或从 Frame 拖入文本框（后者会自动将对象加入 ShiftCalendar 的 Resources 选项卡对象列表）。
- **Current Inflow Rate**：显示当前流入速率，即每秒流入 ContinuousMixer 的物料升数。
- **Current Outflow Rate**：显示当前流出速率，即每秒流出 ContinuousMixer 并经 Pipe 流向下一对象的物料升数。

## 故障选项卡（Tab Failures）

按 “Tab Failures” 所述定义故障。

## 时间选项卡（Tab Times）

按 “Tab Times” 所述定义准备时间（Set-up Time）。从下拉列表选择分布并输入所需数值；Plant Simulation 会在选项卡上边缘显示参数。也可输入常量时间（`Const`）。可用方法 `setTypeAndAttr` 设置分布类型及完整参数集。

## 统计选项卡（Tab Statistics）

除 “Tab Statistics” 所述通用值外，ContinuousMixer 还显示以下对象特有值：

| 项目（英文） | 说明 | 只读属性 | 项目（德文） |
| --- | --- | --- | --- |
| Total Throughput | 流经 ContinuousMixer 的产品数量 | `StatDeleted` [SimTalk] - Drain | Gesamtdurchsatz |

## Importer 选项卡（Tab Importer）

用于定义处理零件、为特定类型零件设置工位以及维修工位的服务。可通过以下任一方式在 Statistics Report 中查看 Importer 统计：

- 在对象对话框中选择 **View > Show Statistics Report**。
- 在 Frame 中右键点击对象并选择 **Show Statistics Report**，或按 `F6`。
- 点击 Home 功能区的 **Show Statistics Report**。

## 用户自定义选项卡（Tab User-defined）

按 “Tab User-defined” 所述定义自有属性。

## 菜单（Menus）

- **Navigate Menu**：见 Navigate Menu 说明。
- **View Menu**：提供访问其功能的命令，包括与 Transport Importer 相关的命令（Exporters、Unavailable Services、Services、Associated Workplaces）。
- **Tools Menu**：见 Tools Menu 说明。
- **Help Menu**：见 Help Menu 说明。

## ContinuousMixer 的方法（Methods）

ContinuousMixer 提供：

- 流体对象的方法（Methods of the Fluid Objects）。
- 所有对象的方法（Methods of All Objects）。

查看全部方法、只读属性与属性：打开 **Show Attributes and Methods** 窗口——在 Class Library 上下文菜单中选择 **Show Attributes and Methods** 查看所选类；或按 `F8` / 点击 Frame 的 Home 功能区 **Show Attributes and Methods** 查看所选实例。

## SimTalk 参考

### Volume [SimTalk] - Mixer

设置 `<Path>` 指定的 Mixer 混合容器中可供原料或产品使用的容量（Volume）。

- **类型**：属性（Attribute）
- **语法**：`<Path>.Volume:real`
- **赋值**：可赋 `real` 类型的值。

```simtalk
MyMixer.Volume := 10
```

- **参见**：Volume [Mixer]

## 相关主题（See also）

- Continuously Mix Juice and Water
- Dialog Box of the ContinuousMixer
- MaterialsTable
- Select Object [for controls]
- ShiftCalendar [object]
- Associated Shift Calendar
- Pipe
- Select the Set-Up Time
- Processing Importer / Set-up Importer / Failure Importer
- View Menu [general description]
- Transport Importer
