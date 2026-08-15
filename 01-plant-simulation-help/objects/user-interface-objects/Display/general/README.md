# Display 对象 — General（总览）

本目录包含 **Display（显示）对象**（用户界面对象）的通用说明。Display 用于在仿真运行的整个过程中，随时呈现当前的仿真数据与结果（例如某个属性的值）。

> 源文件：本目录下暂未生成 `general.md`，仅含原始导出文本 `general.txtx`（同目录下的 `plant-simulation-help2606_7524-7547.txtx` 为空文件）。本 README 基于 `general.txtx` 的内容总结。

> 说明：`general` 目录下暂无 `.md` 文件，也无子文件夹，因此不存在子文件夹内的 `README.md` 可供合并。

## 概述

- **Display（显示）** 用于在仿真运行期间持续显示一个值（例如某个属性的值）。
- 若 Display **未激活（not active）**，Plant Simulation 会在插入它的 Frame 中显示其图标；若已激活，则显示对应的值。
- **Sample（采样）模式**：按指定周期更新显示；**Watch（监视）模式**：仅在所显示的值发生变化时更新。
- Display 可以以下三种形式显示值：
  - **文本（Text / string）**
  - **条形（Bar）**
  - **饼图（Pie / slice of a pie）**

> **注意：** Bar 和 Pie 仅支持**数值（numerical values）**。它们直观易懂，但在需要精确值时不适用。

### Bar / Pie 的相对范围显示

- Bar 或 Pie 表示会按指定范围（Minimum / Maximum）相对地显示值：
  - **空** bar/pie 表示值**小于等于**范围下界；
  - **满** bar/pie 表示值**大于等于**范围上界。
- 按住 **Shift + Ctrl** 键并用鼠标左键拖动其外框，可调整 bar/pie 图形的整体大小。
- Display 会将实际的最小值与最大值以**虚线（dashed lines）**显示（精度不高）。在 Bar / Pie 模式下，当前值会显示在 **Data** 选项卡的 **Minimum** 与 **Maximum** 文本框中。

### 其他说明

- 也可以将 Display 的数值显示在 HtmlReport 中（参见 *Display an Object of Type Display*）。
- **注意：** 仅当 **MUs and States [Home 功能区]** 被激活时，Display 才会显示值。若关闭 MUs and States，Plant Simulation 会阻止在仿真期间更新若干值（例如 Variable 或 Display 类型的对象）。
- 将鼠标悬停在 Display 上，可显示包含相关信息的工具提示（tooltip）。
- 要更改 Display 图形的长度和锚点，点击 **Edit** 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

## 将对象添加到仿真模型

在 **Home** 功能区选项卡上依次点击：

> **Manage Class Library > Basic Objects > UserInterface > Display**

## 拖放（Drag-and-Drop）操作

| 要显示的内容 | 拖动对象 | 拖放到 |
| --- | --- | --- |
| 某个物流对象的统计数据 | 该物流对象 | Display |
| 某个 Variable 的当前值 | 该 Variable | Display |

## 对话框（Dialog Box）

双击 Display 的图标即可打开其对话框：

- **Edit Simulation Properties** — 修改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties** — 在 **Edit 3D Properties** 对话框中编辑对象的 3D 属性：
  - 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮；或
  - 在模型中选中对象后按空格键。
- 要操作对象的图形，点击 **Edit** 功能区选项卡上的 **Show Manipulators** 或按键盘 **M** 键。

## Active [复选框] — Display

勾选此复选框以激活 Display 的显示。

**备注：**

- 若 Display 未激活，Plant Simulation 会在 Frame 中显示其 **名称（Name）** 而非值。
- 要取消激活，清除该复选框，或在上下文菜单中选择 **Deactivate**；也可右键点击 Frame 中的 Display 对象，在上下文菜单中选择 **Activate** 来激活。
- SimTalk：`Active`（参见 *Active [SimTalk] - Display*）。

## Tab Data

Data 选项卡提供左侧目录中所列的设置。

### Path [文本框] — Display

点击省略号按钮，在 **Select Object** 对话框中选择 Display 要显示的属性或方法。

**备注：**

- 要显示全局变量的值，可直接输入该 Variable 本身的路径；也可以输入表达式，例如 `buffer.NumMU+1`。
- Display 支持的数据类型：`boolean`、`integer`、`real`、`string`、`object`、`time`、`money`、`length`、`weight`、`speed`、`date`、`dateTime`。
- 若输入的路径无效，文本框背景会变为**红色**。
- 按 **F2** 可打开你在文本框中输入名称的对象的对话框。

SimTalk：`Path`（参见 *Path [SimTalk] - Display*）。另见 *Select Object [for controls]*。

### Comment [文本框] — Display

在 Comment 文本框中输入对所显示值的简短描述（例如属性名称，如 `Fill Level Buffer`）。Display 会在 Frame 窗口中值下方的位置显示该文本。

SimTalk：`Comment`（参见 *Comment [SimTalk] - Display*）。

### Mode [下拉列表] — Display

选择 Display 的**工作模式（Operating Mode）**：**Sample** 或 **Watch**。

**备注：**

- **Sample（采样）模式**：以 **Interval** 文本框中输入的频率更新显示。
- **Watch（监视）模式**：每当值发生变化时就更新显示。若输入的路径和值**不可监视（not watchable）**，Plant Simulation 不会更新显示。
- **Show Attributes and Methods** 窗口中的 **Watchable** 列会显示哪些属性和只读属性可以被 Plant Simulation 监视。

SimTalk：`Sampler`（SimTalk）、`SmpPeriod`（参见 *SmpPeriod [SimTalk] - Display*）。另见 *DisplayType [SimTalk]*、*update [SimTalk] - Display*。

### Interval [文本框] — Display

选择 **Sample** 模式后会显示 **Interval** 文本框，在其中输入显示的更新频率，格式为常规时间格式。

SimTalk：`SmpPeriod`（参见 *SmpPeriod [SimTalk] - Display*）。

### Value [Display]

选择 **Bar** 或 **Pie** 模式可显示**当前值（Current Value）**。

SimTalk：`Value`（参见 *Value [SimTalk] - Display*）。

### Minimum [Display]

选择 **Bar** 或 **Pie** 模式可显示已达到值的**最小值（Minimum）**。

SimTalk：`GetMinimum`、`GetMaximum`、`resetMinMax`。

### Maximum [Display]

选择 **Bar** 或 **Pie** 模式可显示已达到值的**最大值（Maximum）**。

SimTalk：`GetMaximum`、`GetMinimum`、`resetMinMax`。

### Reset Values [按钮]

点击此按钮可复位选项卡上显示的最小值和最大值。

SimTalk：`resetMinMax`。

## Tab Display

Display 选项卡提供左侧目录中所列的设置。

### Type [下拉列表] — Display

选择 Display 显示其记录数据的方式：

- **Text（文本）**
  - 将值显示为文本。对于浮点值，可输入小数位数（最多 15 位）。
  - 默认设置 `-1` 表示显示所有现有位数；输入正值则按该位数显示。
  - 文本内容在 Data 选项卡的 **Comment** 文本框中输入。
- **Bar（条形）与 Pie（饼图）**
  - 按你指定的 **Minimum** 与 **Maximum** 范围相对地映射值：以条形高度或饼图填充扇区来可视化范围内的值。
  - **空** bar/pie 对应小于等于下界的值；**满** bar/pie 对应大于等于上界的值。
  - 按住 **Shift + Ctrl** 键并用鼠标左键拖动图形边框，可更改 bar/pie 图形的高度和宽度。
  - Plant Simulation 会将当前值转换到你输入的范围，并显示其平均值。

> 输入显示值范围的 **Maximum Value（最大值）** 和 **Minimum Value（最小值）**。

**备注：**

- Display 会在 Frame 窗口中用**点线（dotted lines）**显示实际的最小值和最大值，其精度可能不足；当前值显示在 **Data** 选项卡的 **Minimum** 与 **Maximum** 文本框中。
- Display 只能将数值显示为 bar 或 pie，直观但精度不一定足够。
- 要将选项卡上的值复位为 0，点击 **Data** 选项卡上的 **Reset Values**。

SimTalk：`DisplayType`、`MinVal`、`MaxVal`。另见 *GetMaximum [SimTalk]*、*GetMinimum [SimTalk]*、*resetMinMax [SimTalk]*。

### Font Size [下拉列表] — Display

选择 **Type > Text** 模式下 Display 所显示文本的字体大小。

SimTalk：`Font`（参见 *Font [SimTalk] - Display*）。

### Decimal Places [文本框] — Display

当 **Type > Text** 显示浮点值时，可输入小数位数。

**备注：** Display 最多可显示 15 位小数。默认 `-1` 显示所有现有位数；输入正值则按该位数在 Frame 中显示。

SimTalk：`DecimalPlaces`（参见 *DecimalPlaces [SimTalk] - Display*）。

### Color [Display]

选择 Display 所显示文本的颜色，以及其显示图形轮廓的颜色。

**备注：** 可选预定义颜色，或点击 **More Colors** 后点击 **Select** 在颜色矩阵中选择颜色，再点击 **OK**。Plant Simulation 会在 **More Colors** 旁显示该颜色并将其用作当前颜色。

SimTalk：`Color`（参见 *Color [SimTalk] - Display*）。

### Transparent [复选框] — Display

勾选此复选框可使插入 Frame 的 Display 背景透明。

**备注：**

- 透明背景时，Display 会用背景图像的颜色或 Frame 的网格点来显示文字周围的空间。
- 清除复选框则文字周围空间显示为白色。

SimTalk：`Transparent`（参见 *Transparent [SimTalk] - Display*）。

## Tab User-defined

按 *Tab User-defined* 中所述定义自己的属性。

## 菜单

### Navigate Menu

其命令见 *Navigate Menu* 描述。

### View Menu

其命令见 *View Menu* 描述。SimTalk：`updateDialog`。

### Tools Menu

Tools 菜单提供访问其功能的命令：**Edit Controls**、**Edit Observers**。另见 *Tools Menu [general description]*。

### Help Menu

其命令见 *Help Menu* 描述。

## Display 的方法

Display 提供：

- 左侧目录中列出的方法；
- 所有对象的通用方法（*Methods of All Objects*）。

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 **Class Library** 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选**类（Class）**的方法、只读属性和属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 **Home** 功能区选项卡上的 **Show Attributes and Methods**，可显示所选**实例（Instance）**的方法、只读属性和属性。

## 参见

- *Show Values During the Simulation with the Display*
- *Dialog Box of the Display*
- *Transparent [check box] - Display*
- *Font Color [Comment]*

---

*来源：Plant Simulation Help 11-4594–11-4617。未发表作品。© 2026 Siemens。*
