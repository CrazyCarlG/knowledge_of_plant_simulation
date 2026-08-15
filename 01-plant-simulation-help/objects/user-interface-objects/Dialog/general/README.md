# Dialog（对话框对象）— General 摘要

本目录下的 `general.md` 是 **Dialog** 对象（用户界面对象）的帮助文档正文，`general.txtx` 为其原始提取源（内容与 `general.md` 基本一致，含页眉页脚与图片说明）。本文件是对 `general.md` 的结构化总结，便于快速查阅。

## 1. 概述

**Dialog** 对象用于为仿真模型设计一个与内置对话框风格相似的自定义对话框。

主要用途：

- 为复杂的仿真模型提供简单的用户界面，让用户输入 Plant Simulation 执行任务所需的信息。
- 阻止用户直接操作包含复杂机器的 Frame：把 Method 对象作为 Open Control 插入 Frame，双击 Frame 时改为调用该方法，由方法打开 Dialog 让用户选择设置。

要点：

- 每个 Dialog 对象只管理一个对话框；需要多个自定义对话框时插入多个 Dialog 对象。
- 在 **Elements** 选项卡右键可插入对话框条目；**Show Dialog** 预览对话框；**Edit Dialog** 编辑条目位置。
- 含菜单的显示窗口使用 Windows 主题，不含菜单的显示窗口及对话框使用 Siemens PLM 主题。

## 2. 添加到模型

在 Home 功能区点击 **Manage Class Library > Basic Objects > UserInterface > Dialog**。

## 3. 对话框（Dialog Box）

双击 Dialog 图标打开对话框：

- **Edit Simulation Properties**：修改仿真属性（共享属性见 “Dialog Items of the Objects”）。
- **Edit Animation Properties**：编辑 3D 属性（对话框左下角 **Edit 3D Properties** 按钮，或选中对象后按空格键）。

## 4. 主要控件

| 控件 | 说明 |
|---|---|
| **Label** | 对话框标题；为空时显示 Dialog 对象名称 |
| **Show Dialog** | 显示对话框并触发回调方法（Open / Apply / Close 参数） |
| **Edit Dialog** | 编辑对话框中已创建的条目位置 |
| **Tab Elements** | 通过右键菜单插入、打开、删除对话框条目 |

**Show Dialog 相关 SimTalk 方法**：`openDialog`、`close`、`closeDialog`、`open`

## 5. 插入对话框条目

插入前应先规划结构（是否需要 Tab 和菜单）。创建顺序：先创建容器（如 Tab Control），再创建 Tab，最后在每个 Tab 上插入条目。

右键菜单可插入的条目：

| | |
|---|---|
| New Button | New List View |
| New Check Box | New Menu / New Menu Command |
| New DropDownList Box | New Radio Button |
| New Edit Text Box | New Static Text Box |
| New Group Box | New Tab Control |
| New Image | New Tab Page |
| New List Box | |

结构规则：

- 同一分组（Group Box、Menu、Tab Control、Tab）内的条目 Name 不能重复。
- 用 **Shift+Up/Down** 调整 Tab / Menu 中条目的顺序；拖拽可在分组内外移动条目。

相关 SimTalk 方法：`getItemsList`、`deleteItem`

## 6. 各对话框条目

| 条目 | 用途 | 主要 SimTalk 方法 |
|---|---|---|
| **New Button** | 插入按钮，点击时执行回调参数对应动作 | `createButton`、`setCaption`、`setSensitive` |
| **New Check Box** | 复选/继承框，多选不互斥 | `createCheckBox`、`getCheckBox`、`getInheritanceBox`、`setCheckBox`、`setInheritanceBox` |
| **New DropDownList Box** | 下拉列表，单选 | `createDropDownListBox`、`setIndex`、`getIndex`、`setList` |
| **New Edit Text Box** | 可编辑文本框，支持多种字符类型与密码掩码 | `createEditTextBox`、`setEditType`、`getValue`、`setPasswordMasking`、`getPasswordMasking` |
| **New Group Box** | 用边框分组一组控件 | `createGroupBox`、`setCaption`、`setSensitive` |
| **New Image** | 插入图标/图像（Image ID） | `createImage`、`setIcon`、`getIcon` |
| **New List Box** | 列表，双击选择，不折叠 | `getIndex`、`setList`、`getValue` |
| **New List View** | 表格视图，只能选行 | `createListView`、`setTableRow`、`getTableRow`、`getTable`、`setTable` |
| **New Menu / Menu Command** | 菜单及菜单命令（可用 `-` 作分隔符，支持子菜单） | `createMenu`、`setCaption`、`setSensitive` |
| **New Radio Button** | 单选按钮，用 Group ID 分组 | `createRadioButton`、`setCheckBox`、`getCheckBox`、`setGroupID` |
| **New Static Text Box** | 只读静态文本 | `createStaticTextBox`、`setCaption`、`setSensitive` |
| **New Tab Control** | 选项卡容器（勿与单个 Tab 混淆） | `createTabControl`、`setTab`、`getIndex`、`setList` |
| **New Tab Page** | 单个选项卡页 | `createTabPage`、`setCaption`、`setTab` |

### Edit Text Box 支持的字符类型

Any Character、Letters and Digits、Letters、Decimal Number、Signed Decimal Number、Hexadecimal Number、Octal Number、Binary Number、Floating Point Number、Time、Date with Time、Date、Positive Real Number。

## 7. 定义对话框条目属性

根据条目类型显示部分或全部属性：**Name、Caption、Callback Argument、X、Y、Group ID、Image ID、Width、Height、Enable、Items**。

| 属性 | 说明 |
|---|---|
| **Name** | 条目名称，同组内不可重复；不能包含句点 `.`；推荐含类型标识（如 `xyz_button`） |
| **Caption** | 显示文本，可含特殊字符与空格；适用于 Static Text Box、Button、Group Box、Check Box、Menu/Menu Command、Tab Page、Radio Button |
| **Access Key** | Caption 中 `&` 前缀字母成为快捷键（Alt+字母）；字面 `&` 写为 `&&` |
| **Callback Argument** | 传给回调方法的参数（区分大小写） |
| **X / Y** | 位置；单位是系统字体平均字符宽/行高，**不是像素**；相同值会重叠 |
| **Group ID** | 仅 Radio Button，数字分组 |
| **Image ID** | 仅 Image，图标编号或名称 |
| **Width / Height** | 尺寸，单位同上；默认 0 使用系统定义值 |
| **Enable** | 启用/禁用（置灰）；适用于 Button、Check Box、Radio Button、Edit Text Box、List Box、List View |
| **Items** | 仅 DropDownList Box 和 ListBox，编辑列表项（Insert / Delete / Move Up / Rename） |

## 8. 其他设置

- **Show Default Buttons**：显示/隐藏 OK、Cancel、Apply 标准按钮（SimTalk：`ShowStandardButtons`）。
- **Open Modal**：模态打开（SimTalk：`OpenModal`）。
- **Tab Position**：X-Position / Y-Position 屏幕定位，单位像素，原点为左上角；默认 `-1` 居中（SimTalk：`getUserDialogXYWH`）。
- **Tab User-defined**：自定义属性；Dialog 将回调方法作为用户定义属性提供。

## 9. 回调方法（Tab Method）

- **Callback Method**：创建/选择回调方法，可设为默认用户定义属性 `self.callback`。编辑方式：F2、Shift+双击、User-defined 选项卡双击。
- **Argument for Open**：Open 段参数，默认 `Open`，初始化对话框内容（SimTalk：`ArgumentForOpen`）。
- **Argument for Apply**：Apply 段参数，默认 `Apply`，点击 OK/Apply 时执行（SimTalk：`ArgumentForApply`）。
- **Argument for Close**：Close 段参数，默认 `Close`，点击 Cancel 或标题栏关闭时执行（SimTalk：`ArgumentForClose`）。

回调执行时机：

| 条目动作 | 触发 |
|---|---|
| DropDownList Box 关闭 | 执行 Callback Argument |
| List Box 选择并双击 | 执行 Callback Argument |
| Text Box 内容改变并切换焦点 | 执行 Callback Argument |
| Button 点击 | 执行 Callback Argument |
| Check Box 选择/清除 | 执行 Callback Argument |
| Radio Button 选择 | 执行 Callback Argument |
| List View 双击行 | 执行 Callback Argument |
| Tab Control 选择 Tab | 执行 Callback Argument |
| Menu/Menu Command 选择 | 执行 Callback Argument |

> **注意**：点击 **OK** 时回调方法执行两次（先 Apply 段，再 Close 段）；点击 **Apply** 只执行 Apply 段。

## 10. 菜单与方法

- **Navigate Menu** / **View Menu**（SimTalk：`updateDialog`）/ **Tools Menu**（Edit Controls、Edit Observers）/ **Help Menu**。
- **Methods of the Dialog**：提供目录中列出的方法以及 **Methods of All Objects**。查看方式：Class Library 上下文菜单 **Show Attributes and Methods**（查看类）或 Frame 中按 F8（查看实例）。

## 11. 附录

- **WindowWidth 示例**：`MyHtmlReport.WindowWidth := 800 // pixels`
- **回调方法示例**：New Check Box / Inheritance box 的 `switch action` 代码（`Open` / `NameEdit` / `Apply` 三个 case，见 `general.md` 附录）。
