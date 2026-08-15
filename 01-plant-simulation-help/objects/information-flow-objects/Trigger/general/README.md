# Trigger — General（概述）

> 本 README 汇总了 `general.md` 的内容（同目录下的 `general.txtx` 为其原始来源，内容一致）。该目录下没有子文件夹。

## 1. 简介

**Trigger（触发器）** 将时间映射到变量的值。在仿真运行期间，用户定义的属性会取得 Trigger 所指定的值。你可以：

- 在单个 `TimeSequence`（时间序列）对象中指定这些值；
- 或组合多个其他 Trigger 的时间序列。

此外，Trigger 还可以控制 Source（源）**何时、以何种方式**生成 MU（移动单元）。

操作提示：

- 鼠标悬停在 Trigger 上可显示信息提示框（tooltip）。
- 点击 Edit 功能区的 **Show Manipulators**（或按 `M` 键）可更改图形长度和锚点。

### 添加对象到仿真模型

在 Home 功能区点击 **Manage Class Library > Basic Objects > InformationFlow > Trigger**。

参考示例模型：点击 Window 功能区，进入 **Start Page > Getting Started > Example Models > Small Examples**，在 *Examples Collection* 对话框中选择相应的 Category、Topic 和 Example，然后点击 Open Model。

**参见：** Produce Parts Using a Trigger Object、Dialog Box of the Trigger。

## 2. Trigger 对话框

双击 Trigger 图标可打开其对话框。

- **Edit Simulation Properties** —— 修改对象的仿真属性。共享属性见 *Dialog Items of the Objects*。
- **Edit Animation Properties** —— 通过 **Edit 3D Properties**（仿真属性对话框左下角）或选中对象后按空格键来编辑 3D 属性。

---

## 3. Tab Period（周期选项卡）

| 设置项 | 说明 | SimTalk |
| --- | --- | --- |
| **Active**（复选框） | 在仿真运行期间激活/停用 Trigger。也可在 Frame 中右键对象选择 Activate/Deactivate。 | `Active` |
| **Time Reference** | 选择 Trigger 使用的时间参考：**Relative**（相对，在 Start Time 中输入时间点 `time`）；**Absolute**（绝对，在 Start Date 中输入日期时间点 `dateTime`）。 | `Absolute` |
| **Start Time** | 输入 Trigger 开始工作的时间点（数据类型 `time`）。 | `ReferenceTime` |
| **Start Date** | 输入 Trigger 开始工作的日期和时间点（用于 Time Reference > Absolute）。 | `ReferenceDate` |
| **Active Interval** | 输入 Trigger 处于活动状态的时间间隔。间隔结束后，Trigger 值恢复为默认值（在所属 TimeSequence 的 **Values > Values > Value Table** 中定义）。 | `ActiveInterval` |
| **Repeat Periodically** | 使 Trigger 周期性重复数值，而非仅处理一次。建议先在 Tab Representation 上设置合适的时间单位，否则绘制显示可能耗时。 | `Periodic` |
| **Period Length** | 输入 Trigger 一个周期的持续时间。选中 Repeat Periodically 后，完成一个周期即重复数值。 | `PeriodLength` |

---

## 4. Tab Values（数值选项卡）

| 设置项 | 说明 | SimTalk |
| --- | --- | --- |
| **Trigger Type** | 选择 Trigger 类型（生成事件的方式不同）：**Input Trigger**（从单个 TimeSequence 取值，点击 Values 在 Value Table 输入数值）；**Combination**（通过组合现有 Trigger 生成新 Trigger，点击 Combination Table 输入要组合的 Trigger 名称，结果保存到 Values 打开的组合列表中）。 | `Combination`, `compute` |
| **Values** | 打开包含 Trigger 当前数值序列的 TimeSequence。在 **Start Values > Default Value** 选项卡输入默认值。也可右键 Trigger 对象选择 **Open Values Table**。 | `ValueTable` |
| **Combination Table** | 打开组合表，在单元格中输入要组合的 Trigger 对象：**Time Sequence** 列（TimeSequence 名称，可在连接 Formula 中用该名称访问，点击条目打开其数值列表）、**Origin** 列（源 Trigger 的路径）、**Start Time** 列（Trigger 开始工作的时间）、**Count** 列（Trigger 重复次数）、**End Time** 列（Trigger 停止工作的时间，独立于重复模式；不指定则无结束时间）。 | `CombinationTable`, `compute` |
| **Formula** | 为 Combination Trigger 输入计算其数值模式的公式，连接 Combination Table 中输入的 Trigger 对象。允许的运算取决于数据类型：`boolean` TimeSequence 使用 `AND`、`OR`、`NOT`；数值 TimeSequence 使用 `+`、`-`、`*`、`/`。示例：`TRIGGER AND TRIGGER2 AND TRIGGER3`、`weeklyPlan AND dailyPlan`、`employeenum - 2`。 | `Formula` |

---

## 5. Tab Actions（动作选项卡）

| 设置项 | 说明 | SimTalk |
| --- | --- | --- |
| **Attributes** | 点击 Trigger 下方的 **Attributes**，输入 Trigger 所控制的对象和属性名称。需先关闭 **Inheritance**：**Object** 列（Trigger 控制的对象名）、**Attribute** 列（属性名，字符串形式；对于 `Variable` 对象无需属性，Trigger 直接传递当前值）。数值赋值出错时，Plant Simulation 会在 **Error Message** 列插入错误信息。 | `insertTriggeredAttr`, `deleteTriggeredAttr` |
| **Methods** | 点击 Trigger 下方的 **Methods** 打开列表（需先关闭 Inheritance），输入 Trigger 控制的方法名称。每当 Trigger 值变化时，Plant Simulation 调用相应 Method，并将上一个和当前 Trigger 值作为参数传入。 | `insertTriggeredMeth`, `deleteTriggeredMeth` |
| **Objects** | 打开包含生成零件的 Source 的列表，显示 Source 对象的名称和路径（当你在 Source 对话框选择 **Time of creation > Trigger** 并输入 Trigger 名称、点击 OK/Apply 后由 Plant Simulation 插入）。此表不可编辑。 | — |

---

## 6. Tab Representation（表示选项卡）

定义用于显示数值随时间变化的 **Value Pattern** 和 **Time Unit**。

- **Value Pattern** —— 在 x-y 图（白色背景）中显示数值随时间的变化模式，也可选择时间单位。
- **Time Unit** —— 选择缩放时间轴的时间单位：**Second**、**Minute**、**Hour**、**Day**。

---

## 7. 菜单

- **Navigate Menu** —— 命令见 Navigate Menu。
- **View Menu** —— `Refresh`、`Show Attributes and Methods`。SimTalk：`updateDialog`
- **Tools Menu** —— `Edit Controls`、`Edit Observers`。
- **Help Menu** —— 命令见 Help Menu。

---

## 8. Trigger 的方法

Trigger 提供：

- 目录中列出的方法；
- 以及所有对象的通用方法（**Methods of All Objects**）。

查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 上下文菜单中选择 **Show Attributes and Methods**，可显示所选 Class。
- 按 `F8` 或点击 Frame 的 Home 功能区上的 **Show Attributes and Methods**，可显示所选 Instance。
