# FileInterface — General（摘要）

本目录包含 Plant Simulation 帮助文档中关于 **FileInterface** 对象（信息流对象）的“常规（General）”页面内容。

## 文件说明

- `general.md` — FileInterface 常规参考的结构化 Markdown 版本。
- `general.txtx` — 从帮助文档提取的同一主题纯文本版本。

两者内容一致。

## 概述

**FileInterface** 用于在仿真运行期间访问文本文件中的数据：

- 可以在文本文件中为仿真运行创建数据，并在仿真运行期间将其导入 Plant Simulation。
- 也可以将协议文件（protocol files）、统计表等直接写入文本文件，无需借助表格（tables）或列表（lists）绕行。
- 之后可以在电子表格程序或文字处理应用中可视化或处理这些数据。

## 备注

- Plant Simulation 一次最多可同时打开 **10 个文件**。
- FileInterface 处理字母、数字和特殊字符，但**不能处理二进制数据**（如程序、图形等）。
- 一个 FileInterface 一次只管理**一个文件**。
- 若停用安全设置 **File > Model Settings > General > Prohibit Access to the Computer**，FileInterface 只能更改模型文件夹中的文件（这些文件会自动以读取方式打开）。
- FileInterface 的写函数始终返回 `false`；此外，FileInterface 只能删除模型文件夹及其子文件夹中的文件。
- 将鼠标悬停在 FileInterface 上可显示包含其信息的工具提示。
- 点击 Edit 功能区选项卡上的 **Show Manipulators** 或按键盘上的 **M** 键，可更改图形的长度和锚点。

## 如何添加到仿真模型

在 Home 功能区选项卡上点击 **Manage Class Library > Basic Objects > InformationFlow > FileInterface**。

比较示例模型：点击 Window 功能区选项卡，点击 **Start Page > Getting Started > Example Models > Small Examples**，然后在 *Examples Collection* 对话框中选择相应的 Category、Topic 和 Example，再点击 **Open Model**。

## 对话框

双击 FileInterface 图标可打开其对话框，在此可修改仿真属性（共享属性见 **Dialog Items of the Objects**）。

- 要编辑 3D 模型中的对象的 3D 属性，选中该对象并按**空格键**，然后在 *Edit 3D Properties* 对话框中更改相应设置。
- 编辑 3D 图形属性的两种方式：
  - 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮。
  - 在 3D 模型中选中该对象并按**空格键**。

## Tab 属性

### Attributes 选项卡

- **Filename [FileInterface]**：点击文件夹图标，在 *Open* 对话框中选择文件。
  - 备注：也可以直接输入要导入数据或导出数据的文本文件名称。
  - SimTalk：`FileName [SimTalk] - FileInterface`
- **Encoding [drop-down list]**：选择 Plant Simulation 保存其写入的文本文件时使用的编码。
  - **ANSI** — 8 位字符集，最多可表示 256 个字符（0 到 255）；是 7 位 ASCII 字符集的超集。
  - **UTF-8** — Unicode 字符集的另一种编码，每个字符由 1 到 3 个字节表示。
  - **UTF-16** — Unicode 字符集的另一种编码。
  - **Unicode** — 16 位字符集，几乎涵盖世界上所有书面语言；Plant Simulation 以 UTF-16 编码保存 Unicode，每个字符由 2 个字节表示。
  - 当 Plant Simulation 读取文件时，属性 `Encoding` 保存该文件的编码；若无法识别编码，则返回 `ANSI`。
  - SimTalk：`Encoding [SimTalk]`
- **Delete File [FileInterface]**：删除 **Filename** 文本框中指定名称的文件。
  - SimTalk：`remove [SimTalk] - FileInterface`

### User-defined 选项卡

自定义属性，见 **Tab User-defined**。

## 菜单

- **Navigate Menu**：命令见 **Navigate Menu**。
- **View Menu**：
  - `Refresh [on View menu]`
  - `Show Attributes and Methods [on View menu]`
  - SimTalk：`updateDialog [SimTalk]`
- **Tools Menu**：**Edit Controls**、**Edit Observers**、**Export**、**Import**。
- **Help Menu**：命令见 **Help Menu**。

## 方法

FileInterface 提供：

- 目录（table of contents）中所列出的方法。
- **所有对象的通用方法（Methods of All Objects）**。

查看全部方法、只读属性和属性：打开 **Show Attributes and Methods** 窗口。

- 在 **Class Library** 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的方法、只读属性和属性。
- 按 **F8** 键或点击插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，查看所选实例的方法、只读属性和属性。

## 备注

- 本目录下 `general.md` 与 `general.txtx` 内容一致，`general.txtx` 为从帮助文档提取的纯文本版本。
- 无子文件夹。
