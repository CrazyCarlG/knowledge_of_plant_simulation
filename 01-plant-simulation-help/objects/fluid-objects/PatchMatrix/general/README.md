# PatchMatrix — 概述

本文件汇总了 `general` 目录下 Markdown 文档（`general.md`）的内容。该目录无子文件夹，因此不包含子目录中的 README.md。

> 对象 **PatchMatrix** 用于将一根入口 Pipe 与一根出口 Pipe 相连，以控制工厂内流体物料的流动。

## 说明（Description）

- Pipe 在对象 `FluidSource`、`Tank`、`Mixer`、`Portioner`、`DePortioner` 与 `FluidDrain` 之间输送自由流动的物料。
- 使用方式：
  1. 插入要建模的对象。
  2. 用 Connector 将 Pipe 连接到 PatchMatrix。
  3. 双击 PatchMatrix，切换到 **Attributes** 选项卡。
  4. 点击 **Connections**，勾选相应复选框以允许物料流经这些 Pipe。
     - 列标题为入口（incoming）Pipe。
     - 行标题为出口（outgoing）Pipe。
- 将鼠标悬停在 PatchMatrix 上可显示工具提示；在 Edit 功能区点击 **Show Manipulators** 或按 `M` 键可调整图形长度与锚点。

### 添加到仿真模型

点击 Home 功能区的 **Manage Class Library > Basic Objects > Fluids > DePortioner**（原文如此，实际应为 PatchMatrix）。

## 对话框（Dialog Box）

双击 PatchMatrix 图标打开其对话框。

- **Edit Simulation Properties**：修改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties**：在 **Edit 3D Properties** 对话框中编辑对象的 3D 属性（通过仿真属性对话框左下角的 **Edit 3D Properties** 按钮，或选中对象后按空格键）。
- 要操纵对象图形，点击 Edit 功能区的 **Show Manipulators** 或按 `M` 键。

## 属性选项卡（Tab Attributes）

**Attributes** 选项卡提供该对象可用的设置，其中包括 **Connections** 设置。

## Connections [PatchMatrix]

点击此按钮可显示与 PatchMatrix 相连的 Pipe。

**说明（Remarks）**

在相应单元格中勾选复选框，即可将相应 Pipe 相互连接。

- 列标题为入口（incoming）Pipe。
- 行标题为出口（outgoing）Pipe。

示例中，名为 `Pipe` 的入口 Pipe 与出口 Pipe `Pipe2`、`Pipe3` 相连，`Pipe1` 与 `Pipe2` 相连。

将鼠标拖过 PatchMatrix 时，工具提示会显示这些连接。

### SimTalk 方法

- `getConnectionsForPred [SimTalk]`
- `getConnectionsForSucc [SimTalk]`
- `resetConnections [SimTalk]`
- `setConnections [SimTalk]`

## 用户自定义选项卡（Tab User-defined）

按 “Tab User-defined” 所述定义自有属性。

## 菜单（Menus）

- **Navigate Menu**：见 Navigate Menu 说明。
- **View Menu**：见 View Menu 说明。SimTalk 方法：`updateDialog [SimTalk]`。
- **Tools Menu**：见 Tools Menu 说明。
- **Help Menu**：见 Help Menu 说明。

## PatchMatrix 的方法（Methods）

PatchMatrix 提供：

- 目录中列出的方法。
- 流体对象（Fluid Objects）的方法。
- 所有对象（All Objects）的方法。

可通过 **Show Attributes and Methods** 窗口查看全部方法、只读属性和属性：

- 在 Class Library 上下文菜单中选择 *Show Attributes and Methods*，查看所选类（Class）的方法、只读属性和属性。
- 按 `F8` 或点击插入实例的 Frame 的 Home 功能区 *Show Attributes and Methods*，查看所选实例（Instance）的方法、只读属性和属性。

## 源文件备注

`general.md` 末尾附带一段与 **DePortioner** 相关的内容（`RecoveryTime [SimTalk] - DePortioner`），与 PatchMatrix 对象本身无关，疑似源文档复制错误，故未纳入本概述。
