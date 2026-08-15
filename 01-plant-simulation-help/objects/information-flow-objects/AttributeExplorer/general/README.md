# AttributeExplorer (General) — 概述

本目录汇总了 Plant Simulation 中 **AttributeExplorer（属性浏览器）** 对象的通用帮助文档。目录内包含两个文件，内容一致：

- `general.md` — 结构化的 Markdown 版本帮助文档。
- `general.txtx` — Siemens Plant Simulation Help 的原始提取文本（含页码、版权信息等）。

> 本目录下没有子文件夹（无子级 README.md）。

## 什么是 AttributeExplorer

无需逐一打开每个物流对象（material flow object）的对话框并在文本框中输入属性值，AttributeExplorer 允许你**定义要获取哪些对象的哪些属性**，并在列表窗口中统一显示。

核心用法：

1. 点击 **Show Explorer**，在列表窗口中输入容量、时间等各类值；
2. Plant Simulation 将这些值写回对象，并在模型中使用；
3. 可将该设置表 **Export（导出）** 为制表符分隔的文本文件，再 **Import（导入）** 到另一个模型的 AttributeExplorer 中，从而在多个模型间复用相同设置；
4. 属性表也可显示在 HtmlReport 中；悬停鼠标可显示提示（tooltip）；
5. 点击 Edit 功能区选项卡上的 **Show Manipulators** 或按 **M** 键，可调整图形长度与锚点。

## 添加到仿真模型

在 Home 功能区选项卡中依次点击：

```
Manage Class Library > Basic Objects > InformationFlow > AttributeExplorer
```

## 对话框（Dialog Box）

双击图标打开对话框：

- **Edit Simulation Properties** — 修改仿真属性（共享属性见 "Dialog Items of the Objects"）。
- **Edit Animation Properties** — 编辑 3D 属性：
  - 点击仿真属性对话框左下角的 **Edit 3D Properties**，或
  - 在模型中选中对象并按空格键（spacebar）。
- 点击 Edit 功能区选项卡上的 **Show Manipulators** 或按 **M** 键可操控图形。

## 各标签页与功能

### Show Explorer

点击以显示列表窗口，展示在 **Tab Objects** 与 **Tab Attributes** 上定义的对象和属性。

- 点击标题栏的 **X** 关闭列表窗口；
- 结果表按 **Path / Name / Label** 排序，先显示指定对象的数据，再显示查询定义的数据；
- 也可在 Frame 中右键 AttributeExplorer 并选择 **Show**；
- 用 **Context Menu of Embedded Lists** 的命令操控列表内容。

相关 SimTalk：`IsShown`、`AttributeTable`、`ExplorerTable`。

### Tab Data

选择属性模式（设置前需勾选 **Inheritance** 复选框）：

- **Watch** — 显示属性值（可监视性由单元格背景色指示）：
  - 蓝色：属性不可监视（not watchable）；
  - 灰色：属性可监视（watchable）；
  - 红色：属性路径无效。
- **Edit** — 允许编辑属性值，点击 **Apply/OK** 后写回对象对话框；
- **Read Only** — 只读模式，仅可查看，点击 **Apply** 更新显示值。

还可设置：

- **Show Objects With** — 按 Entire Path / Name only / Label only 显示对象；
- **Show Attributes With** — 按 Alias（附加说明）/ Name only 显示属性；
- **Comment / Show Comment** — 输入并显示对对象和值的说明。

相关 SimTalk：`Mode`、`AttributeRepresentation`、`ObjectRepresentation`、`ShowComment`、`Comment`。

### Tab Objects

查看或编辑对象的属性（输入数据前需勾选 **Inheritance**）：

- 从 Frame 窗口将对象**拖放**到 Tab Objects，即可插入对象的绝对路径与名称；
- 可同时拖放多个对象（按在 Frame 中选择的顺序添加）；
- 仅拖到 AttributeExplorer 的**图标**上，则只输入对象名称；
- 按 **F2** 可打开名称所在文本框对应对象的对话框。

相关 SimTalk：`ObjectTable`。

### Tab Attributes

点击 **Show Attributes**，在 **Name** 列输入要编辑/查看的属性名（输入前需勾选 **Inheritance**）。

在 **Attribute Viewer** 对话框中：

- 点击并选择要显示其属性的 Object（在 **Select Object** 对话框中选择）；
- 选择查看内置属性（built-in）还是用户自定义属性（user-defined）；
- 可选择一个或多个连续属性（**Shift+click**）添加；
- 子属性写法示例：`imp.priority`；
- 点击 **OK** 将属性加入 Tab Attributes 列表。

若预设 **Name** 不够直观，可在 **Alias** 列输入描述性术语。

注意：

- 导入文件时，文件必须包含属性的 **Name**（仅含 Alias 无法正确导入）；
- 点击 **Read Only** 单元格可将某属性设为只读。

单元格背景色含义：

- 蓝色：属性不可监视；
- 白色：属性可监视；
- 灰色：内置属性名输入错误。

相关 SimTalk：`ObjectTable`、`AttributeTable`。

### Tab Query

定义查询，按输入到列表单元格中的条件查找对象（输入前需勾选 **Inheritance**）。设置内容包括：开括号数量、属性（Attribute）、条件（Condition）、值（Value）、闭括号数量、运算符（Operator）、注释（Comment），以及要查询的 Frame。

- **Include Subframes** — 同时查询所选 Frame 内的 Frame；
- **Include MUs** — 在查询中包含零件（MU）。

代码化示例：

```text
Name Expr Station.* and ((XPos > 100 and YPos = 200) or ExitStrategy = Cyclic)
```

**Condition（条件）** 可选值：

- `<` 小于
- `<=` 小于等于
- `>` 大于
- `>=` 大于等于
- `=` 等于（对 real、length、weight、speed、time 类型精确比较）
- `~=` 等于（忽略大小写，或约等于）
- `/=` 不等于
- `Expr` 正则表达式（比较 `regex_search`，如 `^Inf` 匹配以 "Inf" 开头的词）
- `Exists` 检查对象是否具有指定属性

**Operator（运算符）**：`and` / `or`，连接当前行与下一行的布尔值。

相关 SimTalk：`QueryTable`、`StartNode`、`IncludeSubframes`、`IncludeMUs`。

### Tab User-defined

按 "Tab User-defined" 中的说明定义自己的属性。

## 菜单（Menus）

- **Navigate Menu** — 命令见 Navigate Menu。
- **View Menu** — Refresh、Show Attributes and Methods（SimTalk：`updateDialog`）。
- **Tools Menu** — Edit Controls、Edit Observers、Export、Import：
  - **Export** — 将 Tab Objects 与 Tab Attributes 内容导出为制表符分隔文本文件；
  - **Import** — 导入包含 Tab Objects 与 Tab Attributes 数据的文本文件。
- **Help Menu** — 命令见 Help Menu。

## AttributeExplorer 的方法

AttributeExplorer 提供 **Methods of All Objects**。可通过 **Show Attributes and Methods** 查看所有方法、只读属性与属性：

- 在 Class Library 上下文菜单中选择 **Show Attributes and Methods**，查看所选 Class；
- 按 **F8** 或点击 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，查看所选 Instance。

语法示例：

```text
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## 参考

- 示例模型：Window 功能区选项卡 > Start Page > Getting Started > Example Models > Small Examples。
- 相关主题：Set Parameters with the AttributeExplorer、Dialog Box of the AttributeExplorer、Watchable Values、Context Menu of Embedded Lists、Select Object。
