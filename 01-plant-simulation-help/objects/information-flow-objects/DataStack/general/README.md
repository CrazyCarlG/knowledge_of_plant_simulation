# DataStack — General（总结）

本目录包含 DataStack（栈）对象的概述性帮助内容，源文件为 `general.md`（其原始提取文本位于 `general.txtx`，内容一致）。以下为该内容的总结。

## 概述

- Plant Simulation 使用 **LIFO**（后进先出）方式访问 **DataStack** 的内容。
- Plant Simulation 使用 **FIFO**（先进先出）方式访问 **DataQueue** 的内容。

将鼠标悬停在 DataStack 上可显示提示信息；在“编辑”功能区选项卡中点击 **Show Manipulators** 或按键盘 **M** 键，可更改 DataStack 图形的长度与锚点。

## 将对象添加到仿真模型

在“主页”功能区选项卡中点击：

> Manage Class Library > Basic Objects > InformationFlow > DataStack

## DataStack 的属性

DataStack 和 DataQueue 都是**单列列表**，二者共享所有方法和属性，仅内置属性不同。

- **DataStack（LIFO）**：新条目插入到顶部，最先移除最后添加的单元格内容。
- **DataQueue（FIFO）**：按插入顺序保存条目，最先移除等待时间最长的条目。

列表对象的功能可通过 **List Ribbon Tab**（列表功能区选项卡）访问。

### 注意事项

- DataStack 窗口始终在已打开的对话框后面（背景）打开；也可通过 `openDialogBox` 方法将其作为对话框在前台打开。
- 数据类型 **Stack** 与 DataStack 共享内置属性。
- 注意区分对象 **DataStack**（插入模型中的对象）与数据类型 **stack**：可创建 `stack` 类型的用户自定义属性和局部/全局变量，它们属于另一对象的一部分，不是独立对象，也没有自己的图标。因此这些变量和属性不识别 DataStack 的 SimTalk 函数（如 `Location` 或 `existsIcon`）；其余方法（尤其是读写访问方法）对 DataStack 以及这些变量和属性均适用。

## DataStack 的窗口

双击 DataStack 图标可打开其窗口，在其中修改仿真属性。共享属性见“对象的对话框项目”；列表对象的功能位于 **List Ribbon Tab**。

- 在 3D 模型中编辑对象的 3D 属性：选中对象并按 **空格键**，然后在 **Edit 3D Properties** 对话框中修改设置。
- 操作对象图形：点击“编辑”功能区选项卡的 **Show Manipulators** 或按 **M** 键。

## List Ribbon Tab（列表功能区选项卡）

提供与列表和表格相关的命令；并非所有列表对象都提供全部命令。

## DataStack 的方法

DataStack 和 DataQueue 提供以下方法：

- `createNestedList` [SimTalk] — DataQueue
- `pop` [SimTalk] — DataStack
- `push` [SimTalk] — Stack
- `pushList` [SimTalk]
- `top` [SimTalk]

此外还包括 **Methods of Lists and Tables** 与 **Methods of All Objects**。

查看对象所有方法、只读属性和属性：打开 **Show Attributes and Methods** 窗口。

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类（Class）的属性和方法。
- 按 **F8** 键，或在插入实例的 Frame 的“主页”功能区选项卡中点击 **Show Attributes and Methods**，可查看所选实例（Instance）的属性和方法。

## 参见

- Properties of the DataQueue
- DataStack
- Work with Data in a List or Table（Plant Simulation Step-by-Step Help）
- Access Data in Lists（Plant Simulation Step-by-Step Help）
- Creating a List within a DataQueue or DataStack
