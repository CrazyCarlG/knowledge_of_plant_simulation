# Checkbox（通用）—— 内容总结

本目录包含 Plant Simulation 帮助文档中关于 **Checkbox（复选框）** 对象「通用」部分的内容，主要来源为 `general.md`（其同内容的原始文本提取见 `general.txtx`）。

## 概述

Checkbox 对象用于在 **开（on）/ 关（off）** 两种状态之间切换，例如切换运行模式、切换运行时模式与调试模式等。

- 默认外观：一个可点击的复选框图形。
- 添加方式：在 Home 功能区标签页点击 **Manage Class Library > Basic Objects > UserInterface > Checkbox**。

## 使用注意事项

- Plant Simulation 仅在 Checkbox 在模型窗口中每方向至少占据 **10 像素** 时才会识别点击；缩小过多可能导致无法可靠识别。
- 单击图形可在开/关状态间切换。
- 双击图标右侧的名称 **Checkbox** 可打开其对话框。
- 可为 Checkbox 创建任意数量的图标，Plant Simulation 会根据图标的名称/状态自动切换；图标需成对命名，例如 `TrueIcon1` 与 `FalseIcon1`。
- 也可在子 Frame 中单击 Checkbox 切换值（参见 Factory51 模型中的 "Show Warehouse Content" 复选框）。
- 鼠标悬停可显示提示信息（tooltip）。
- 在 Edit 功能区标签页点击 **Show Manipulators** 或按 `M` 键，可更改图形长度与锚点。

## 相关主题（See also）

- Switch States with the Checkbox（用复选框切换状态）
- Select an Option from a Drop-down List（从下拉列表选择选项）
- Configure the Check Box and the Drop-down List（配置复选框与下拉列表）

## 对话框

双击 Frame 中图标右侧的名称 **Checkbox** 打开对话框：

- **Edit Simulation Properties**：编辑对象的仿真属性，共享属性见 "Dialog Items of the Objects"。
- **Edit Animation Properties**：编辑 3D 属性（点击对话框左下角 **Edit 3D Properties** 按钮，或选中对象后按空格键）；按 `M` 键或点击 **Show Manipulators** 操纵图形。

## 主要选项卡与设置

### Tab Data（数据选项卡）

- **Value [drop-down list]**：设置 Checkbox 是否激活（`true`）或不激活（`false`）。图标需成对命名以表示开/关状态。
- **Value [SimTalk]**：对应的 SimTalk 引用。
- **Control [Checkbox]**：修改对象的内置行为。当点击 Checkbox 使 **Value** 改变时，对象调用该 Control。Plant Simulation 只调用对象自身的 Control，不调用其实例的 Control。
  - **选择已有 Method**：点击省略号按钮，在 "Select Object [for controls]" 对话框中选择 Method，或直接将 Method 拖放到文本框。
  - **创建对象自身的 Control**：输入有意义的名字并选择 **Create Control**（插入 `self.名称`，如 `self.A1Ctrl`）；或在空文本框选择 **Create Control**（插入 `self.On内置名称`，如 `self.OnEntrance`）。
  - **后续编辑**：按 `F2`、或按住 `Shift` 双击文本框、或选择上下文菜单 **Open Object**、或在 **User-defined** 选项卡双击 Method 名称。
  - **删除**：删除对应的用户自定义属性（仅删除文本框中的名称不会删除属性）。
  - 标准 **OnClicked** 控件示例：`(self)`。

### Tab User-defined（用户自定义选项卡）

在此定义自己的属性，详见 "Tab User-defined"。

## 菜单

- **Navigate Menu**：命令见 "Navigate Menu"。
- **View Menu**：命令见 "View Menu"，包含 `updateDialog [SimTalk]`。
- **Tools Menu**：提供 **Edit Controls**、**Edit Observers** 等功能。
- **Help Menu**：命令见 "Help Menu"。

## 方法

Checkbox 提供 **Methods of All Objects**（所有对象的通用方法）。

查看全部方法、只读属性与属性：打开 **Show Attributes and Methods** 窗口（在 Class Library 的上下文菜单中选择，或选中实例后按 `F8` / 点击 Home 功能区的 **Show Attributes and Methods**）。

方法语法示例：

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## SimTalk 属性

### ShowStandardButtons

设置由 `<Path>` 指定的 Dialog 是否显示标准按钮 **OK**、**Cancel** 与 **Apply**（`true`）或不显示（`false`）。

- **类型**：Attribute（属性）
- **语法**：`<Path>.ShowStandardButtons:boolean`
- **赋值**：可赋 `boolean` 类型值。

```simtalk
Dialog.ShowStandardButtons := false
```

**参见**：Show Default Buttons [check box]
