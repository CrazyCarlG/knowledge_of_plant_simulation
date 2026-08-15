# Comment 对象（注释对象）

> 本目录 `general/` 下只有一个 Markdown 文件 `general.md`（以及同名源文本 `general.txtx`），没有子文件夹，也没有其他 README.md。本文件是对 `general.md` 内容的总结。

## 概述

**Comment**（注释）对象用于在仿真模型中显示说明性文字，帮助你和同事理解模型背后的意图以及模型应当如何运作。

- Comment 可以像其他对象一样被访问，但通常不参与仿真本身。
- 通过 Frame 的 **View** 功能区选项卡中的 **Options > Show Comments**（或点击相应图标）可显示插入到该 Frame 中的所有 Comment 对象。
- Plant Simulation 在 Frame 窗口中显示你在 **Display > Text** 中输入的文本。
- 右键点击 Comment 并选择 **Open Comment Window**，可打开一个仅显示注释（不含格式化和编辑选项）的窗口。
- 将鼠标悬停在 Comment 上可显示相关提示信息（tooltip）。
- 在 **Edit** 功能区选项卡中点击 **Show Manipulators** 或按 `M` 键，可更改图形长度和锚点。

### 添加对象到仿真模型

点击 **Home** 功能区选项卡中的 **Manage Class Library > Basic Objects > UserInterface > Comment**。

## Comment 的对话框

双击插入到 Frame 中的 Comment 图标即可打开其对话框；拖动任意边或角可调整对话框大小。

- **Open Comment Window** —— 右键点击 Comment 并选择 **Open Comment Window**。Plant Simulation 会以输入注释时 **Comment** 选项卡的大小及其所应用的格式打开注释窗口。
- 点击标题栏中的 **Close** 关闭注释窗口。

### 编辑动画属性

在 **Edit 3D Properties** 对话框中编辑 3D 属性：

- 点击仿真属性对话框左下角的 **Edit 3D Properties**。
- 在模型中选择该对象并按空格键。

要操作图形，点击 **Edit** 功能区选项卡中的 **Show Manipulators** 或按 `M` 键。

### Name [文本框] - Comment

显示对象的名称（预定义名称或你指定的名称）。双击并输入即可更改。

**备注：** 可使用字母、数字和下划线（`_`），例如 `MyComment`、`MyComment1`、`My_Comment_1`。名称不能以数字开头（例如不允许 `1Comment`）。

## Comment 选项卡

输入详细说明，作为对 **Display** 选项卡中 **Text** 框里所输入短注释的补充。

**注意：** 仅当勾选 **Save the Content in Rich-text Format** 时，格式化属性才会生效。

- 使用 **Formatting Toolbar** 按钮或 **Context Menu for Formatting the Comment** 对选中的文本应用格式。
- 字符格式属性：应用字体、字号和字体颜色；应用加粗、下划线或斜体。
- 段落格式属性：设置对齐方式（左对齐、居中或右对齐）；使用项目符号设置缩进。
- 或将支持富文本格式（`.rtf`）的文字处理软件（如 WordPad 或 MS Word）中已格式化的文本复制并粘贴（含格式）到文本框中。
- 或在文本框中输入文本后，复制回文字处理软件应用格式，再粘贴回来。按 `Ctrl+A` 全选、`Ctrl+C` 复制、`Ctrl+V` 粘贴。

### Formatting Toolbar（格式工具栏）

对所选 RTF 文本应用格式。仅当选中 **Save the Content in Rich-text Format** 时设置才生效。

| 操作 | 属性 |
| --- | --- |
| 撤销最近的操作 | — |
| 打开 **Font** 对话框（字体、字形、字号、效果） | `Font` |
| 打开 **Colors** 对话框（选择颜色） | `Color` |
| 应用加粗 | — |
| 应用斜体 | — |
| 应用下划线 | — |
| 左对齐 | — |
| 居中 | — |
| 右对齐 | — |
| 添加项目符号（按 `Enter` 换行） | — |
| 打开 **Insert Date and Time** | — |

### Inherit Contents（继承内容）

点击文本框旁的继承复选框，可继承或不继承 Comment 的内容。

### Save the Content in Rich-text Format（以富文本格式保存内容）

勾选此复选框可把文本框内容以富文本格式保存，保留所有格式。勾选后，Plant Simulation 会激活 Formatting Toolbar 设置和 Context Menu for Formatting the Comment。

### Context Menu for Formatting the Comment（格式注释的上下文菜单）

提供格式化菜单命令，也可在 Formatting Toolbar 上选择这些选项：

- **Undo** —— 撤销最近的操作。
- **Font** —— 在 **Font** 对话框中选择字体设置（字体、字形、字号、效果），点击 OK 应用。
- **Color** —— 在 **Color** 对话框中选择颜色设置。点击 **Apply** 应用并保持对话框打开，或 **OK** 应用并关闭。
- **Bold** —— 对选中文本应用加粗。
- **Italic** —— 将选中文本设为斜体。
- **Underline** —— 为选中文本加下划线。
- **Align Left** —— 文本左对齐。
- **Center** —— 文本居中。
- **Align Right** —— 文本右对齐。
- **Bullets** —— 在选中文本前添加项目符号（按 `Enter` 在句子前插入换行）。
- **Insert Date or Time** —— 打开 **Insert Date and Time** 对话框；选择格式并点击 OK 即可在光标位置插入。

## Display 选项卡

在 **Display** 选项卡中选择 Comment 在模型中的显示方式。

### Text [文本框] - Comment

输入将 Comment 对象插入 Frame 时 Plant Simulation 显示的文本。

- 请输入简短文本，否则无法在 Frame 中看到或选中 Comment。
- 如果仅在此处输入文本（**Comment** 选项卡中无内容），则下次打开对话框时 Plant Simulation 会显示 **Display** 选项卡。
- 使用继承复选框可继承或不继承该 Text。

### Font Size [下拉列表] - Comment

选择在 Frame 中显示 Comment 的字号。

### Font Color [Comment]

点击下拉箭头选择 Frame 中显示的文本颜色。

- 颜色仅显示在 Frame 中，不显示在打开的对话框中。
- 选择预定义颜色，或点击 **More Colors** 并点击 **Select** 在颜色矩阵中选择颜色，然后点击 OK。

### Background Color [下拉列表] - Comment

点击下拉箭头选择 Comment 的背景色。

- 选择预定义颜色，或点击 **More Colors** 并点击 **Select** 在颜色矩阵中选择颜色，然后点击 OK。

### Transparent [复选框] - Comment

勾选此复选框可使背景透过文字的镂空部分显示出来。

- 使用透明背景时，Comment 以 Font Color 显示在 Frame 背景上。
- 取消勾选则以白色背景显示文本。

## 菜单

- **Navigate Menu** —— 命令在 Navigate Menu 中说明。
- **View Menu** —— 命令在 View Menu 中说明。
- **Tools Menu** —— 提供访问其功能（如 Edit Observers）的命令。
- **Help Menu** —— 命令在 Help Menu 中说明。

## Comment 的方法

Comment 提供：

- 目录中所列的方法。
- **Methods of All Objects**（所有对象的通用方法）。

要查看所有方法、只读属性和属性，打开 **Show Attributes and Methods**：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 可显示所选类（Class）的成员。
- 按 `F8` 或点击 Frame 的 **Home** 功能区选项卡中的 **Show Attributes and Methods** 可显示所选实例（Instance）的成员。

### SimTalk 引用

- `appendToContent`
- `openComment`
- `Name`
- `Font`
- `Color`
- `SaveAsRichedit`
- `Text`
- `BackgroundColor`
- `Transparent`
- `updateDialog`

## 另请参阅

- Add Text and Display Boards
- Dialog Box of the Comment
- Inherit Contents [Comment]
- `appendToContent` [SimTalk]
- `openComment` [SimTalk]
- `Font` [SimTalk] - Comment
- `Color` [SimTalk] - Comment
- `SaveAsRichedit` [SimTalk]
- `Text` [SimTalk] - Comment
- `BackgroundColor` [SimTalk] - Comment
- `Transparent` [SimTalk] - Comment
- `updateDialog` [SimTalk]
