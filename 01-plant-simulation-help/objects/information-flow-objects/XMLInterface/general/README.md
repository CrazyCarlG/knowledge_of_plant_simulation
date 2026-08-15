# XMLInterface — General

本目录包含 XMLInterface（XML 接口）对象的通用说明文档，内容来自 `general.md`。

## 概述

XMLInterface 对象用于在 Plant Simulation 中读写和访问 XML 数据，支持以下操作：

- 顺序读写数据（Read and Write Data Sequentially）
- 随机读取与访问数据（Read and Access Data Randomly）
- 随机访问与遍历数据（Access and Traverse Data Randomly）

通过 XMLInterface 读取并用 Method 处理后的数据，可用来运行 Plant Simulation 仿真。之后可调用 `write` 与 `writeElement` 方法将仿真结果写回 XML 文件，供 Process Designer 或其他程序继续使用。

> **注意：** 使用 XMLInterface 需要熟悉 XPath（XML Path Language）源代码。

## 添加对象到仿真模型

在 Home 功能区选项卡点击 **Manage Class Library > Basic Objects > InformationFlow > XMLInterface** 即可将 XMLInterface 对象添加到仿真模型。

## 对话框

双击 XMLInterface 图标打开其对话框，可编辑仿真属性（Simulation Properties）和动画属性（Animation Properties）。编辑 3D 属性可点击对话框左下角的 **Edit 3D Properties** 按钮，或选中对象后按空格键。按 `M` 键或点击 Edit 功能区的 **Show Manipulators** 可操作对象图形。

## Tab Attributes（属性选项卡）

### Filename [XMLInterface]
- 点击文件夹图标，选择要访问或保存的 XML 文件名。
- **SimTalk:** `FileName`, `openRead`

### Context [文本框]
- 输入要导入数据的上下文（context），即 XMLInterface 开始读取数据的 XML 文档节点位置。
- 例如输入 `Data/Objects`，可限定要读取的数据范围。
- 若不指定 context，XMLInterface 会导入整个文件，可能耗时且占用大量内存。
- **SimTalk:** `Context`, `setContext`

### Import Method [XML Interface]
- 修改对象的内置行为，由 `openRead` 方法对 XML 文件中包含的所有对象调用，用于控制如何提取并顺序处理导入的数据。
- 可通过省略号按钮选择已有的 Method，或将 Frame 中的 Method 拖入文本框；也可用 **Create Control** 创建用户自定义属性类型的 Method。
- 标准导入方法的示例代码见 `general.md`。
- **SimTalk:** `ImportMethod`, `openRead`, `addAttribute`, `endElement`, `openWrite`, `startElement`, `writeElement`

### Delete File [XML Interface]
- 点击此按钮删除 *Filename* 文本框中所指定的 XML 文件。
- **SimTalk:** `remove`

## Tab User-defined（用户自定义选项卡）

可按照 *Tab User-defined* 的说明定义自己的属性。

## 菜单

- **Navigate Menu / View Menu / Help Menu**：命令详见对应菜单说明；View Menu 对应 SimTalk `updateDialog`。
- **Tools Menu**：提供 **Edit Controls** 和 **Edit Observers** 两个命令。

## XML Interface 的方法

XML Interface 提供：

- 目录中列出的方法（Methods listed in the table of contents）。
- 所有对象共有的方法（Methods of All Objects）。

可通过上下文菜单 **Show Attributes and Methods**，或按 `F8` 键，查看选中对象（类或实例）的方法、只读属性与属性。
