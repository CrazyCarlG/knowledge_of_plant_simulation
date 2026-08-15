# DataTable 对象 — General（总览）

本目录包含 **DataTable 对象**（信息流对象）的通用说明。文档描述的是 DataTable 对象本身，即 Plant Simulation 中用于以行列结构（表格）存储数据、可通过索引访问单元格的对象。

> 源文件：`general.md`（内容详见该文件）；原始导出文本：`general.txtx`。

## 概述

**DataTable** 是一个表格型数据容器，可以通过索引（即单元格所在的行号和列号确定的位置）访问其中的每一个单元格。可以把 DataTable 类比为一个"架子"：向单元格写入值和引用，也可以再把它们移除。

与 **DataList** 相比，DataTable 有以下特点：

- 单元格内容会**保留**在 DataTable 中（DataList 移除数据后不保留空位）。
- DataTable 在一个范围内**可以存在空白单元格**。
- 在仿真运行期间可以**任意添加和删除行、列**。

列表对象的相关功能可以在 **List Ribbon Tab**（列表功能区选项卡）上访问。

## 注意事项（Notes）

- DataTable 总是在后台打开，位于任何已打开对话框的后面；可以用方法 `openDialogBox` 将其作为对话框在前台打开。
- DataTable 与数据类型 `table` 共享其内置属性。注意区分**可插入模型中的 DataTable 对象**与**数据类型 `table`**：
  - 可以创建数据类型为 `table` 的用户自定义属性以及局部/全局变量，它们属于另一个对象的一部分，因此本身不是独立对象、也没有自己的图标。
  - 因此这些变量和属性**不识别** DataTable 的 SimTalk 函数，例如 `Location` 或 `existsIcon`。其余所有方法（尤其是读写访问相关的方法）对 DataTable 以及 `table` 类型的变量/属性都适用。
- 可以在 **HtmlReport** 中显示 DataTable 的内容（参见 *Display a DataTable or a DataList*）。
- 将鼠标悬停在 DataTable 上可显示关于它的工具提示。
- 要修改 DataTable 的图形长度和锚点，点击 Edit 功能区选项卡上的 **Show Manipulators** 或按键盘上的 `M` 键。
- 流体对象的 **MaterialsTable**（物料表）与 DataTable 共享相同的属性。

## 添加到仿真模型

要将 DataTable 对象添加到仿真模型中，在 Home 功能区选项卡点击 **Manage Class Library > Basic Objects > InformationFlow > DataTable**。

查看示例模型：点击 Window 功能区选项卡，点击 **Start Page > Getting Started > Example Models > Small Examples**；然后在 *Examples Collection* 对话框中分别选择 Category、Topic 和 Example，再点击 **Open Model**。

## DataTable 的窗口（Window of the DataTable）

双击 DataTable 的图标打开其窗口，在该窗口中可以修改其仿真属性。

### 备注（Remarks）

- 共享属性参见 *Dialog Items of the Objects*。
- 列表对象的功能可以在 **List Ribbon Tab** 上访问。
- 要编辑对象在 3D 模型中的 3D 属性，选中对象后按空格键，然后在 *Edit 3D Properties* 对话框中修改相应设置。
- 要操作对象的图形，点击 Edit 功能区选项卡上的 **Show Manipulators** 或按 `M` 键。

### List Ribbon Tab（列表功能区选项卡）

List Ribbon Tab 提供与列表和表格相关的命令。并非所有列表对象都提供全部所述命令。

## DataTable 的方法

DataTable 提供以下方法：

- Methods of Columns of the DataTable（DataTable 列的方法）
- Methods of Rows of the DataTable（DataTable 行的方法）
- Miscellaneous Methods of the DataTable（DataTable 的杂项方法）
- Methods for Accessing the DataTable（访问 DataTable 的方法）
- Methods for Instantiating the DataTable（实例化 DataTable 的方法）
- 列表和表格的共享方法（*The shared Methods of Lists and Tables*）
- 所有对象的共享方法（*The shared Methods of All Objects*）

要查看对象的所有方法、只读属性和属性，打开窗口 **Show Attributes and Methods**（该窗口以 Station 对象为例进行说明）。

## 参见

- Work with Data in a List or Table in the Step-by-Step Help
- Work with Data in the DataTable in the Step-by-Step Help
- Access Data in Lists in the Step-by-Step Help
- Accessing a Range of Cells with a Method
- Creating Lists within Lists and Tables
- Creating a List within a DataTable
- Window of the DataTable

使用列表和表格的示例模型：

- Produce Parts According to a Delivery Table
- Produce the Parts with a Source Using a Sequence Table
- Produce Parts in a Fixed Sequence Over and Over Again
- Visualize the Occupancy of the Store Over Time
- Produce Parts With a Random Frequency Entered into a Data Table
- Model Processing and Set-up Jobs
- Produce Parts With a Percentage Entered into a Data Table
- Write the Content List into a Table for Further Processing
- Define Times in the Class of the Processing Stations
- Select Where the Data Comes From
- Create the Work Plan
