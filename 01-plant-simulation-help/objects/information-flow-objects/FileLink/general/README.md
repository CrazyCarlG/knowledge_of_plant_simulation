# FileLink — General（摘要）

本目录包含 Plant Simulation 帮助文档中关于 **FileLink** 对象（信息流对象）的“常规（General）”页面内容。

## 概述

FileLink 用于将外部文件链接或嵌入到 Plant Simulation 仿真模型中。

- 默认情况下，Plant Simulation 会将文件的完整路径填入 FileLink 的 **Label** 和 **Filename** 文本框。
- 添加文件后，Plant Simulation 会弹出对话框，询问是否将该文件**嵌入（Embed）**到模型中：
  - 若选择 **是（Yes）**，保存模型时该文件会被复制进模型文件；下次打开模型时，Plant Simulation 会生成一个临时文件（原始文件的副本）。若在保存模型时仍正在源应用中编辑已嵌入的文件，Plant Simulation 会给出提示。
  - 默认命名规则为 `FileLink`、`FileLink1` 等。
- 在 Frame 窗口中显示文件完整路径：**View > Options > Show Object Labels in the Frame**。
- 双击 Frame 中的图标可打开对应应用并编辑文件（前提是计算机上已安装该源应用）。若链接失效，Plant Simulation 会打开 FileLink 对话框，并在 **File Name** 文本框中显示无效链接的路径和名称。

> 关于“禁止访问计算机”的限制：
> - FileInterface 只有在取消勾选 **File > Model Settings > General > Prohibit Access to the Computer** 后，才能通过双击在关联应用中打开嵌入文件；方法 `openFile` 同样适用此限制。
> - 但嵌入的文本文件（`.txt`）和 `.xps` 文件即使勾选了“禁止访问计算机”，也可通过双击打开。
> - 可在 Microsoft Word 中通过 **Save As** 创建 `.xps` 文件，用法类似 PDF；Windows 自带免费的 xps 查看器。

其他操作：
- 右键图标并选择 **Open** 可打开 FileLink 的对话框。
- 将鼠标悬停在图标上可显示工具提示。
- 点击 Edit 功能区选项卡上的 **Show Manipulators** 或按 **M** 键，可更改图形的长度和锚点。

## 如何添加到仿真模型

在 Home 功能区选项卡上点击 **Manage Class Library > Basic Objects > InformationFlow > FileLink**。

## 对话框

双击 FileLink 图标可打开其对话框，在此可修改仿真属性（共享属性见 **Dialog Items of the Objects**）。

- 编辑 3D 图形属性：点击 Edit 选项卡上的 **Show Manipulators** 或按 **M** 键。
- 右键图标并选择 **Open** 打开对话框；双击图标可在关联应用中打开链接文件。

## Tab 属性

### Attributes 选项卡

- **Filename [FileLink]**：点击文件夹图标导航并选择要添加的文件。
  - 从 Windows 资源管理器将文件拖放到 Frame 后，Plant Simulation 会在此文本框中显示该文件的路径和名称。
  - SimTalk：`FileName [SimTalk] - FileLink`
- **Embed File [check box]**：勾选后，将拖放到 Frame 的文件嵌入到模型中。
  - 嵌入后该版本文件成为模型的一部分，移动原文件不影响模型；但嵌入后对文件的更改不会反映到模型中，且会显著增大 `.spp` 模型文件体积。
  - 取消勾选则创建指向计算机文件系统中文件的链接；若移动或删除该文件，链接将失效，Plant Simulation 无法找到并打开它。
  - 相关 SimTalk：`Embed [SimTalk]`、`Prohibit Access to the Computer [model settings]`、`openFile [SimTalk]`

### User-defined 选项卡

自定义属性，见 **Tab User-defined**。

## 菜单

- **Navigate Menu**：命令见 **Navigate Menu**。
- **View Menu**：
  - `Refresh [on View menu]`
  - `Show Attributes and Methods [on View menu]`
  - SimTalk：`updateDialog [SimTalk]`
- **Tools Menu**：**Edit Controls**、**Edit Observers**。
- **Help Menu**：命令见 **Help Menu**。

## 方法

FileLink 提供：
- 方法 `openFile [SimTalk]`。
- 所有对象的通用方法（Methods of All Objects）。

查看全部方法、只读属性和属性：打开 **Show Attributes and Methods** 窗口。
- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的方法、只读属性和属性。
- 按 **F8** 键或点击 Frame 的 Home 选项卡上的 **Show Attributes and Methods**，查看所选实例的方法、只读属性和属性。

## 备注

- 本目录下 `general.md` 与 `general.txtx` 内容一致，`general.txtx` 为从帮助文档提取的纯文本版本。
- 无子文件夹。
