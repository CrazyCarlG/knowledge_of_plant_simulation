# README — DataQueue (General)

本目录汇总了 **DataQueue（数据队列）** 信息流对象的通用说明。内容来源为同目录下的 `general.md`（以及 `general.txtx` 原始文本）。

> 说明：`general` 目录下暂无子文件夹，因此不存在子文件夹内的 `README.md` 可供合并。本 README 仅基于 `general.md` 的内容总结。

## 概述

- **DataQueue（数据队列）**：Plant Simulation 采用 **FIFO（先进先出）** 方式访问其内容。条目按插入顺序保存，等待时间最长的条目最先被移除。
- **DataStack（数据栈）**：Plant Simulation 采用 **LIFO（后进先出）** 方式访问其内容。新条目插入到顶部，最后添加的条目最先被移除。

基本操作提示：

- 将鼠标悬停在 DataQueue 上可显示相关信息的工具提示（tooltip）。
- 在 **Edit** 功能区选项卡点击 **Show Manipulators** 或按键盘 **M** 键，可更改 DataQueue 图形的长度和锚点。

## 将对象添加到仿真模型

在 **Home** 功能区选项卡上依次点击：

> **Manage Class Library > Basic Objects > InformationFlow > DataQueue**

## DataQueue 的属性

DataQueue 是一个只有一列的列表，Plant Simulation 使用 FIFO 方式访问。

**备注：**

- Plant Simulation 按插入顺序保存条目，并最先移除等待时间最长的条目。
- 可在 **List Ribbon Tab** 上访问列表对象的函数。

> **注意：** DataQueue 始终在已打开的对话框后面（后台）打开；也可通过方法 `openDialogBox` 将其作为对话框在前台打开。

- 数据类型 `Queue` 共享 DataQueue 的内置属性。
- 注意区分插入到模型中的对象 **DataQueue** 与数据类型 **queue**。用户可以创建属于其他对象一部分的、数据类型为 `queue` 的用户自定义属性以及局部/全局变量，它们不是独立对象，也没有自己的图标。
- 因此这些变量和属性不识别 DataQueue 的 SimTalk 函数（如 `Location` 或 `existsIcon`）。其余所有方法（尤其是读写访问方法）对 DataQueue 以及变量和属性均适用。

**另请参见：**

- 分步帮助中的 “Work with Data in a List or Table”
- 分步帮助中的 “Access Data in Lists”
- “Creating a List within a DataQueue or DataStack”
- “Properties of the DataQueue”

## DataQueue 的窗口

双击 DataQueue 图标可打开其窗口，在窗口中可以修改其仿真属性。

**备注：**

- 共享属性在 **Dialog Items of the Objects** 中描述。
- 可在 **List Ribbon Tab** 上访问列表对象的函数。
- 要在 3D 模型中编辑对象的 3D 属性，选中对象并按空格键，然后在 **Edit 3D Properties** 对话框中修改相应设置。
- 要操作对象的图形，点击 **Edit** 功能区选项卡上的 **Show Manipulators** 或按键盘 **M** 键。

## List Ribbon Tab（列表功能区选项卡）

List Ribbon Tab 提供与列表和表格相关的命令。并非所有列表对象都提供全部所述命令。

## DataQueue 与 DataStack 的方法

DataStack 与 DataQueue 提供：

- 左侧目录中列出的方法；
- 列表与表格的方法（Methods of Lists and Tables）；
- 所有对象的方法（Methods of All Objects）。

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类（Class）的属性和方法。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选实例（Instance）的属性和方法。

各方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- 表达式 `<Path>` 表示该方法所应用对象的路径。
- 方法的签名（由参数标识符及其数据类型组成）列在括号中。例如 `(Parameter:string)` 表示数据类型为 `string` 的参数。除常量值外，也可以使用所需类型的变量，或返回所需数据类型的方法。

---

*来源：Plant Simulation Help 11-4245–11-4248。未发表作品。© 2026 Siemens。*
