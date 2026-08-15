# FluidSource — General

本目录包含 Plant Simulation 中 **FluidSource** 对象的通用（general）文档。该对象用于生产（产出）在工厂中被加工的产品的原料，可以是散装物料（bulk goods）或流体（fluids）。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `general.md` | FluidSource 对象的 Markdown 文档（主内容） |
| `general.txtx` | 同一内容的原始导出文本（含页码脚注，内容与 general.md 基本一致） |

> 本目录下没有子文件夹，也没有其他 README.md 文件，因此本总结基于 `general.md` 的内容整理。

## 概述

- **FluidSource** 用于产出产品的原料（散装物料或流体）。
- 使用 **FluidDrain** 从工厂中移除已加工和混合的产品。
- 更改图形长度与锚点：在 Edit 功能区点击 **Show Manipulators**，或按键盘 **M** 键。
- 悬停鼠标可显示对象提示信息（tooltip）。
- 添加对象：Home 功能区 → **Manage Class Library > Basic Objects > Fluids > FluidSource**。

## 对话框（Dialog Box）

双击 FluidSource 图标打开对话框。可在其中编辑仿真属性（simulation properties）与动画/3D 属性（**Edit 3D Properties** 按钮，或选中对象后按空格键）。

### Tab Attributes 中的主要设置

1. **Outflow Rate（流出速率）**
   - 定义物料从 Tank 流出的速率（单位：升/秒）。
   - 物料经 Pipe 流向下一个对象。
   - 注意：当前流出速率取决于连接的 Pipe 数量；若连接两根 Pipe，在 Pipe 允许的情况下，设定速率会流经每一根 Pipe。若只想让设定量流出，应连接单根 Pipe 后再拆分。
   - SimTalk：`OutflowRate`

2. **Material Selection（物料选择，下拉列表）**
   - 决定 FluidSource 如何选择要生产的物料。
   - 可选值：
     - **Constant** — 只生产单一物料，物料名称填写在 Material 文本框中。
     - **Sequence Cyclical** — 按 Sequence Table 中的顺序与数量循环生产，序列处理完后从头重复。
     - **Sequence** — 按 Sequence Table 中的顺序与数量仅生产一次，处理完即停止。
   - SimTalk：`MaterialSelection`

3. **Material（文本框）**
   - 输入要生产的物料名称；具体含义取决于 Material Selection 的设置。
   - SimTalk：`Material`

4. **Sequence Table（序列表）**
   - 定义要生产的物料及各自的数量（升）。
   - 物料名称（如 MatA、MatB…）需在 MaterialsTable 中定义。
   - 若原料超过十种，需在 MaterialsTable 中增加额外原料。

5. **Materials Table（物料表）**
   - 包含 FluidSource 可生产的不同物料的数据。
   - SimTalk：`MaterialsTable`

6. **Shift Calendar（班次日历）**
   - 包含班次数据，控制 FluidSource 在哪些班次工作。
   - 选择后会自动加入 ShiftCalendar 的 Resources 标签页对象列表。
   - SimTalk：`ShiftCalendarObject`

7. **Current Outflow Rate（当前流出速率）**
   - 显示每秒流出并流经 Pipe 的物料量（升）。
   - SimTalk：`CurrentOutFlowrate`

### 其他标签页

- **Tab Failures** — 定义故障。
- **Tab Statistics** — 除通用统计值外，含对象特有值：
  - **Amount of Material**（物料量，德文 Materialmenge）：显示从 FluidSource 流出的物料总量，只读属性 `StatAmount`。
- **Tab User-defined Attributes** — 自定义属性。

### 菜单

- **Navigate Menu**、**View Menu**（含 SimTalk `updateDialog`）、**Tools Menu**、**Help Menu** — 各命令见对应通用说明。

## 方法（Methods）

FluidSource 提供：
- Fluid Objects 的方法（Methods of the Fluid Objects）。
- All Objects 的方法（Methods of All Objects）。

查看全部方法、只读属性与属性：打开 **Show Attributes and Methods** 窗口（类库上下文菜单，或选中实例后按 **F8** / Home 功能区点击 **Show Attributes and Methods**）。

## 相关主题（See also）

- Configure the FluidSources Providing the Materials
- Configure the FluidSources Which Produce the Materials
- Produce Fluids in a Fixed Sequence
- Dialog Box of the FluidSource
- Pipe
- MaterialsTable
- ShiftCalendar
- Select Object
