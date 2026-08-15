# TimeSequence（时间序列）

本目录（`general`）包含 TimeSequence 对象的通用说明文档，主要内容来源于 `general.md`（`general.txtx` 为同一内容的原始提取文本，二者内容一致）。本 README 对这些内容进行总结。

## 概述

**TimeSequence** 对象用于记录数值随时间的变化过程，例如班次计划（shift plans）、机器维护计划（machine maintenance schedules）或缓冲区占用率（buffer occupancies）。

TimeSequence 是一个**两列的表格**，支持两种记录模式：

- **Watch（监视）模式**：每当一个可监视的值发生变化时，Plant Simulation 就写入一条时间-数值对。
- **Sample（采样）模式**：在指定时间间隔内周期性写入时间-数值对，无论数值是否真正发生变化。

可以多次使用 TimeSequence 并对其数值排序，以判断这些数值随时间是否保持恒定，还是随机变化。

## 表格结构与数据类型

每条记录由两列组成：第一列为**时间点（Point in Time）**，第二列为与该时间点关联的**数值（Value）**。Plant Simulation 会将内容按升序排序；内容可在仿真运行期间动态变化。删除某行的数据对后，后续行会自动上移，不会留下空行。

> **注意**：虽然 TimeSequence 有两列，但其行为类似单列列表——不允许空单元格或成对的空单元格。

- **Value 列**可选的数据类型：`Boolean`、`Integer`、`Real`、`String`、`Object`、`Time`、`Money`、`Length`、`Weight`、`Speed`、`Date`、`DateTime`。
- **Point in Time 列**的数据类型取决于 *Start Values > Time Reference* 的设置，可为 `Time` 或 `DateTime`。

## 设置与获取属性值

可通过对话框中的复选框、文本框、下拉列表，或直接为相应属性赋值来设置/获取属性值。示例：

```simtalk
MyDataStack.MaxDim := -1          -- 设置属性
print myDataStack.MaxDim          -- 获取属性
```

查看方法、只读属性和属性：
- 类（Class）：在类库上下文菜单中选择 **Show Attributes and Methods**。
- 实例（Instance）：在 Frame 的 Home 功能区的 **Show Attributes and Methods**，或按 **F8**。

## 添加到仿真模型

- 调整图形长度和锚点：点击 Edit 功能区的 **Show Manipulators** 或按 **M**。
- 添加对象：Home 功能区 **Manage Class Library > Basic Objects > InformationFlow > TimeSequence**。

## 对话框

双击 TimeSequence 图标打开对话框。可编辑：
- **仿真属性（Edit Simulation Properties）**：共享属性见 *Dialog Items of the Objects*。
- **动画属性（Edit Animation Properties）**：点击 **Edit 3D Properties** 按钮，或选中对象后按空格键打开 **Edit 3D Properties** 对话框。

## 菜单

| 菜单 | 说明 |
|------|------|
| **File** | 命令见 *List Ribbon Tab*。参见：导入文件、导出到文件、导出对象文件、文本文件格式、打印列表、打印设置、关闭模型 |
| **Edit** | 命令见 *Home Ribbon Tab* 与 *List Ribbon Tab*。参见：剪切、复制、粘贴、删除、全选、插入行、查找、替换 |
| **Format** | 命令见 *List Ribbon Tab*。参见：激活列索引、激活行索引、继承格式、继承内容、继承注释 |
| **Navigate** | 命令见 *Navigate Menu* |
| **View** | 命令见 *List Ribbon Tab*。参见：重新计算公式、显示注释、显示数据类型、高亮空单元格、转到单元格 |
| **Tools** | 提供 **Edit Controls**、**Edit Observers** |
| **Help** | 命令见 *Help Menu* |

## 选项卡（Tabs）

### Contents（内容）
在表格中指定时间点与数值。提供两个按钮：
- **Sort**：按升序排序。
- **Set Value**：用设定的 **Default value** 填充第二列的空单元格（SimTalk：`DefaultValue`）。

### Start Values（起始值）
确定 Plant Simulation 如何解释时间列和数值列，可用于整体偏移时间序列的数据。

- **Time Reference**：选择时间值是 **Relative（相对）** 还是 **Absolute（绝对）**（SimTalk：`Absolute`）。
  - 绝对：在 *Reference Date* 文本框输入某日期的具体时间点（`dateTime`）。
  - 相对：在 *Reference Time* 文本框输入一个时长（`time`）。
- **Reference Time / Reference Date**：Plant Simulation 将该值加到时间列上以偏移数据，从而无需重新录入即可整体平移时间（SimTalk：`ReferenceDate`、`ReferenceTime`）。
- **Default Value**：时间序列的默认值（SimTalk：`DefaultValue`）。对于定义 **Trigger** 对象数值演变的时间序列尤为重要，Trigger 在其活动区间之外采用该默认值。

### Record（记录）
设置仿真运行期间记录数值的模式。

- **Value**：输入要记录的数值的相对或绝对路径（SimTalk：`Path`）。路径无效则不记录；Watch 模式下路径必须引用可监视的值。按 **F8** 可查看对象哪些属性可监视（可监视属性在 *Watchable* 列标有 `*`）。
  - 示例：`I.building2.entrance.NumMU`、`frame.variable`、`ResWorking`
- **Mode**：选择 **Watch** 或 **Sample** 模式（SimTalk：`Sample`）。
- **Interval**：Sample 模式下两次记录之间的时间间隔（SimTalk：`SmpPeriod`）。
- **Active**：勾选以记录数值演变；取消勾选则不记录（SimTalk：`Active`）。也可在 Frame 中右键对象选择 **Activate / Deactivate**。

## 方法

TimeSequence 提供以下方法：
- 列方法（Methods for Columns）
- 行方法（Methods for Rows）
- 访问 TimeSequence 的方法（Methods for Accessing the TimeSequence）
- 列表与表格的共享方法
- 所有对象的共享方法

打开 **Show Attributes and Methods** 窗口可查看全部方法、只读属性与属性。
