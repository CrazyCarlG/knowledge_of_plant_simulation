# General — 列表与表格的属性（Properties of Lists and Tables）

本目录汇总了 Plant Simulation 列表与表格对象（Lists and Tables）的通用（General）属性说明。内容来源于本目录下的 `general.md`（其原始文本见 `general.txtx`）。本目录没有子文件夹，因此没有其他子目录 `README.md` 需要汇总。

## 概述

列表和表格控制模型中的事件进程，并在仿真期间创建数据，这些数据被保存下来供后续评估使用。

Plant Simulation 提供两类列表：

- **单列列表**：`DataList`、`DataStack`、`DataQueue`
- **多列列表**：`DataTable`、`TimeSequence`

> 查看示例模型：点击 Window 功能区选项卡，选择 **Start Page > Getting Started > Example Models > Small Examples**，在 *Examples Collection* 对话框中选择对应的 Category、Topic 和 Example，然后点击 **Open Model**。

## 五种列表与表格

Plant Simulation 共提供五种不同的列表和表格：

| 对象 | 访问方式与行为 |
| --- | --- |
| **DataList** | 通过位置随机访问所有单元格。可在任意位置添加新单元格；删除某个单元格后，编号更高的所有单元格上移一位。 |
| **DataQueue** | 访问最先添加的单元格。在最后一个现有单元格之后添加新单元格。 |
| **DataStack** | 访问最后添加的单元格。添加单元格时，所有现有单元格下移一位；删除单元格时，其余单元格各上移一位。 |
| **DataTable** | 通过列号和行号随机访问所有单元格。新内容会覆盖并替换单元格中的现有内容。 |
| **TimeSequence** | 通过列号和行号随机访问所有单元格。按时间升序添加新条目；删除前一个条目后，位置更高的条目上移一位。TimeSequence 记录的「时间—值」对属于一体，即只能删除成对的值，不能只删除时间或只删除值。 |

可在 **List Ribbon Tab**（列表功能区选项卡）上访问列表对象的属性。

## 参见（对应本主题下的子章节）

`general.md` 中的「See also」指向以下相关主题，这些主题分别对应 `Properties of Lists and Tables` 目录下的各子文件夹：

- **Window of Lists and Tables**（列表与表格的窗口）— 见 `window/`
- **Methods of Lists and Tables**（列表与表格的方法）— 见 `methods/`
- **Accessing Data in Lists**（访问列表中的数据）— 见 `methods/accessing-lists-and-tables/`
- **Read-Only Attributes of Lists and Tables**（列表与表格的只读属性）— 见 `read-only-attributes/`
- **Accessing a Range of Cells with a Method**（用方法访问单元格范围）— 见 `accessing-range-of-cells/`
- **Attributes of Lists and Tables**（列表与表格的属性）— 见 `attributes/`
- **Creating Lists within Lists and Tables**（在列表与表格中创建列表）— 见 `creating-lists-within-lists-and-tables/`
- **Working with Lists and Tables**（使用列表与表格）

## 列表与表格的窗口（Window of Lists and Tables）

双击插入到仿真模型中的列表对象图标，即可打开其窗口。

### 备注（Remarks）

- 要修改对象 **Class** 的属性，可在 Class Library 中双击该对象，或在 Toolbox 的 **Information Flow** 选项卡上双击它。在这里可以查看或更改已保存的数据，或输入新数据；也可按需调整格式和数据类型。
- 可在 **List Ribbon Tab** 上访问列表对象的函数。
- 要在 3D 模型中编辑对象的 3D 属性，选中对象并按**空格键**，然后在 **Edit 3D Properties** 对话框中修改相应设置。
- 要操作对象的图形，点击 Edit 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

### 参见

- Work with Data in a List or Table
- List Ribbon Tab
- Context Menu of the Contents of List Objects
- Context Menu of Embedded Lists
- Window of Lists and Tables
