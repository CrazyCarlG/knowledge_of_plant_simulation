# Dialog（对话框对象）— Methods 摘要

本目录下的 `methods.md` 是 **Dialog** 对象（用户界面对象）的方法参考文档正文，`methods.txtx` 为其原始提取源（内容与 `methods.md` 基本一致，含页眉页脚与图片说明）。本文件是对 `methods.md` 的结构化总结，便于快速查阅。

> 说明：本目录（`methods/`）内除 `methods.md` 与 `methods.txtx` 外无子文件夹，因此无子文件夹 README.md 需要合并。

## 1. 概述

**Dialog** 对象提供两类方法：

- 本目录表列出的方法（见下文）。
- **Methods of All Objects**（所有对象的通用方法）。

查看全部方法、只读属性与属性：在 Class Library 上下文菜单选择 **Show Attributes and Methods**（查看类），或在插入实例的 Frame 中按 **F8** / 点击 Home 功能区 **Show Attributes and Methods**（查看实例）。

## 2. 语法行约定（Syntax line conventions）

以 `<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean` 为例：

- `<Path>`：方法作用对象的路径。
- `(Parameter:string)`：参数签名（标识符 + 数据类型），可传常量、同类型变量或返回该类型的方法。
  > **注意**：嵌套表达式的括号必须输入 `(…)`，否则可能产生意外结果并打开调试器。
- `[,Parameter:boolean]`：方括号内为**可选参数**。
- `:= false`：参数**默认值**。
- `→ boolean`：箭头后为**返回值数据类型**。

## 3. 方法总览（按功能分类）

Dialog 共有 **45 个方法**，可归为六类：打开/关闭对话框、创建条目、删除条目、读取条目、设置条目、其他。

### 3.1 打开 / 关闭对话框（4 个）

| 方法 | 语法 | 说明 |
|---|---|---|
| **open** | `<Path>.open(X:integer, Y:integer)` | 在屏幕指定 (X, Y) 位置打开对话框 |
| **openDialog** | `<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean` | 打开对话框；`CallOpenControl=true` 时等价于双击图标并执行 Open Control，`false`（默认）仅打开对话框 |
| **close** | `<Path>.close(OK:boolean)` | 关闭对话框；`true` 应用更改，`false` 取消所有更改 |
| **closeDialog** | `<Path>.closeDialog([ApplyChanges:boolean:=true]) → boolean` | 关闭对话框；`true`（默认）评估并应用更改，`false` 丢弃更改 |

### 3.2 创建对话框条目 create*（13 个）

共同约定：`Name`（条目名，用 `setCaption` 设置显示文本）、`X` / `Y`（位置）、`Width` / `Height`（尺寸）、`Parent`（可选父级，如 Group Box 或 Tab Page）。均返回 `boolean`。

| 方法 | 语法 | 说明 |
|---|---|---|
| **createButton** | `(Name, X, Y, Width[, Parent]) → boolean` | 创建按钮（Button） |
| **createCheckBox** | `(Name, X, Y[, Parent]) → boolean` | 创建复选框（Check Box） |
| **createDropDownListBox** | `(Name, X, Y, Width[, Parent]) → boolean` | 创建下拉列表框（Drop-Down List Box） |
| **createEditTextBox** | `(Name, X, Y, Width[, Parent]) → boolean` | 创建可编辑文本框（Edit Text Box） |
| **createGroupBox** | `(Name, X, Y, Width, Height[, Parent]) → boolean` | 创建分组框（Group Box） |
| **createImage** | `(Name, X, Y[, Parent]) → boolean` | 创建图像（Image），用 `setIcon` 设置图标 |
| **createListBox** | `(Name, X, Y, Width, Height[, Parent]) → boolean` | 创建列表框（List Box） |
| **createListView** | `(Name, X, Y, Width, Height[, Parent]) → boolean` | 创建列表视图（List View） |
| **createMenu** | `(Name[, Parent]) → boolean` | 创建菜单/菜单命令（Menu / Menu Command） |
| **createRadioButton** | `(Name, X, Y[, Parent]) → boolean` | 创建单选按钮（Radio Button） |
| **createStaticTextBox** | `(Name, X, Y[, Parent]) → boolean` | 创建静态文本框（Static Text Box） |
| **createTabControl** | `(Name, X, Y, Width, Height) → boolean` | 创建选项卡容器（Tab Control，无 Parent 参数） |
| **createTabPage** | `(Name[, Parent]) → boolean` | 创建选项卡页（Tab Page，Parent 为 Tab Control） |

> **createRadioButton 备注**：同一组单选按钮必须**按顺序**创建（按行列位置生成）。不能把两组单选按钮并排（如左 Red/Blue、右 Round/Square）当成两组——Windows 会忽略 Group ID，按 Y 坐标逐行分组。此类布局应把单选按钮放进 Group Box，而非直接松散放置。

### 3.3 删除对话框条目（1 个）

| 方法 | 语法 | 说明 |
|---|---|---|
| **deleteItem** | `<Path>.deleteItem(DialogItem:string) → boolean` | 删除指定条目；成功返回 `true`，失败（如继承的条目）返回 `false` |

### 3.4 读取条目状态 get*（10 个）

| 方法 | 语法 | 说明 |
|---|---|---|
| **getCheckBox** | `(DialogItem:string) → boolean` | 返回复选框/单选按钮是否选中 |
| **getIcon** | `(DialogItem:string) → string` | 返回图像条目的 Image ID 或图像名 |
| **getIndex** | `(DialogItem:string) → integer` | 返回列表/下拉列表/选项卡页当前选中项编号（最左 tab=1）；空下拉列表返回 0，有内容未选时自动选第一项 |
| **getInheritanceBox** | `(DialogItemName:string) → boolean` | 返回复选框是否处于继承框模式（`true`=继承框，`false`=普通复选框） |
| **getItemsList** | `(Table:table)` | 将对话框中每个条目的完整路径、名称、类型写入指定表 |
| **getPasswordMasking** | `(DialogItem:string) → boolean` | 返回编辑文本框是否启用密码掩码 |
| **getTable** | `(ListView:string) → string` | 返回 List View 所用 Items 表的名称 |
| **getTableRow** | `(Table:string) → integer` | 返回 List View 中用户选中的表行号 |
| **getUserDialogXYWH** | `(byRef X, byRef Y, byRef Width, byRef Height)` | 将对话框位置与尺寸写入局部变量（byRef 输出） |
| **getValue** | `(DialogItem:string) → string` | 返回条目当前值（适用于下拉列表、复选框、单选按钮、列表、编辑文本框、Tab Control——对 Tab Control 返回活动 Tab 名） |

### 3.5 设置条目状态 set*（15 个）

| 方法 | 语法 | 说明 |
|---|---|---|
| **setActiveTabPage** | `(TabControl:string, TabPageName:string)` | 激活指定 Tab Control 中的指定 Tab |
| **setCallbackArgument** | `(DialogItem:string, Argument:string) → integer` | 设置条目的回调参数（Callback Argument） |
| **setCaption** | `(DialogItem:string, Caption:string) → boolean` | 设置条目标题/文本（适用于静态文本框、编辑文本框、Tab Page、按钮、分组框、菜单、复选框、单选按钮） |
| **setCheckBox** | `(DialogItem:string, Active:boolean) → boolean` | 选中/清除复选框或单选按钮 |
| **setEditType** | `(DialogItem:string, Type:string)` | 设置编辑文本框允许输入的字符类型（见 3.6 表） |
| **setGroupID** | `(DialogItem:string, Group:integer)` | 设置单选按钮的分组 ID |
| **setIcon** | `(DialogItem:string, ImageID:string) → boolean` | 设置图像条目的 Image ID 或图像名 |
| **setIndex** | `(DialogItem:string, ItemNumber:integer) → boolean` | 设置列表/下拉列表/选项卡页显示的条目（Tab Control 可指定激活的 tab，左=1） |
| **setInheritanceBox** | `(DialogItemName:string, Value:boolean)` | 将复选框设为继承框（`true`）或普通复选框（`false`） |
| **setList** | `(DialogItem:string, List:any) → boolean` | 设置 List Box / Drop-Down List Box / Tab Control 显示的单项列表 |
| **setPasswordMasking** | `(DialogItem:string, Selected:boolean) → boolean` | 设置编辑文本框是否密码掩码（`true` 显示为小写 x，`false` 明文） |
| **setSensitive** | `(DialogItem:string, Activated:boolean) → boolean` | 启用（`true`）/禁用置灰（`false`）条目；不适用于 Tab Control、Tab Page、Image |
| **setTab** | `(DialogItem:string, NewTabPage:string) → boolean` | 将条目移动到指定 Tab；不能用于动态创建 Tab，也不能在组内移动条目 |
| **setTable** | `(DialogItem:string, AttributeTable:string/object) → boolean` | 设置 List View 所用的 Items 表（可传表对象或字符串路径） |
| **setTableRow** | `(Table:string, Row:integer) → boolean` | 设置 List View 的 Items 表中被选中的行 |

### 3.6 setEditType 支持的字符类型

Any Character、Letters and Digits、Letters、Decimal Number、Signed Decimal Number、Hexadecimal Number、Octal Number、Binary Number、Floating Point Number、Time、Date with Time、Date、Positive Real Number。

### 3.7 其他（2 个）

| 方法 | 语法 | 说明 |
|---|---|---|
| **clearData** | `<Path>.clearData` | 删除 Dialog 的所有对话框条目 |
| **updateUserDialog** | `<Path>.updateUserDialog` | 更新对话框内容，使 Items 表、图片、图标的改动立即生效 |

## 4. 只读属性（Read-Only Attributes）

Dialog 提供 **Read-Only Attributes of All Objects**。只读属性只能查询、不能设置（由 Plant Simulation 按查询时刻计算），多数对应对象某选项卡上不可用的对话框条目。查看方式同上（**Show Attributes and Methods** / F8）。

## 5. 快速索引（按方法名首字母）

| 方法 | 类别 | 方法 | 类别 |
|---|---|---|---|
| clearData | 其他 | open | 打开/关闭 |
| close | 打开/关闭 | openDialog | 打开/关闭 |
| closeDialog | 打开/关闭 | setActiveTabPage | 设置 |
| createButton | 创建 | setCallbackArgument | 设置 |
| createCheckBox | 创建 | setCaption | 设置 |
| createDropDownListBox | 创建 | setCheckBox | 设置 |
| createEditTextBox | 创建 | setEditType | 设置 |
| createGroupBox | 创建 | setGroupID | 设置 |
| createImage | 创建 | setIcon | 设置 |
| createListBox | 创建 | setIndex | 设置 |
| createListView | 创建 | setInheritanceBox | 设置 |
| createMenu | 创建 | setList | 设置 |
| createRadioButton | 创建 | setPasswordMasking | 设置 |
| createStaticTextBox | 创建 | setSensitive | 设置 |
| createTabControl | 创建 | setTab | 设置 |
| createTabPage | 创建 | setTable | 设置 |
| deleteItem | 删除 | setTableRow | 设置 |
| getCheckBox | 读取 | updateUserDialog | 其他 |
| getIcon | 读取 | getInheritanceBox | 读取 |
| getIndex | 读取 | getItemsList | 读取 |
| getPasswordMasking | 读取 | getTable | 读取 |
| getTableRow | 读取 | getUserDialogXYWH | 读取 |
| getValue | 读取 | | |
