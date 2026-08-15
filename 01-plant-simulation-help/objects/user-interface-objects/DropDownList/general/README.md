# DropDownList 对象（下拉列表对象）

> 本目录 `general/` 下只有一个 Markdown 文件 `general.md`（以及同名源文本 `general.txtx`），没有子文件夹，也没有其他 README.md。本文件是对 `general.md` 内容的总结。

## 概述

**DropDownList**（下拉列表）对象用于在 Frame 中显示一个下拉列表。当你选择其中某一项时，它会执行你在 `Control` 中编写的动作。

- 你可以通过 DropDownList 的对话框，或通过属性 `Items` 来定义下拉列表显示的选项。
- 每当用户选择另一项时，下拉列表会执行你在 `Control` 中编写的动作。
- 默认情况下，DropDownList 的外观如下（可带或不带标题 caption）。

> **注意：** Plant Simulation 只有在 DropDownList 在模型窗口中每个方向至少占据 10 像素时才会接受对其的点击。如果缩放得过小，DropDownList 的图形可能会变得太小，导致 Plant Simulation 无法可靠识别它。

- 右键点击下拉列表并选择 **Open**，可打开其对话框。
- 也可以在 Frame 窗口中拖拽一个框选框（marquee）套住其图标来选中下拉列表。
- 还可以在子 Frame 中点击一个 DropDownList 并选择其中某项，从而触发相应动作。
- 将鼠标悬停在 DropDownList 上可显示相关提示信息（tooltip）。
- 在 **Edit** 功能区选项卡中点击 **Show Manipulators** 或按 `M` 键，可更改图形长度和锚点。

### 添加对象到仿真模型

要将 DropDownList 对象添加到仿真模型，点击 **Home** 功能区选项卡中的 **Manage Class Library > Basic Objects > UserInterface > DropDownList**。

## DropDownList 的对话框

右键点击插入到 Frame 中的 DropDownList，并在上下文菜单中选择 **Open**，即可打开其对话框。

### 编辑仿真属性

在对话框中可以更改对象的仿真属性。共享属性在 *Dialog Items of the Objects*（对象的对话框项）中说明。

### 编辑动画属性

在 **Edit 3D Properties** 对话框中编辑对象的 3D 属性：

- 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮。
- 或在模型中选择该对象并按空格键。

要操作图形，点击 **Edit** 功能区选项卡中的 **Show Manipulators** 或按 `M` 键。

## Attributes 选项卡

**Attributes** 选项卡提供了该对象提供的设置。共享属性在 *Tab Attributes* 中说明。

### Width [文本框] - DropDownList

输入 DropDownList 在 Frame 中显示时的宽度（单位：米）。

**备注：**

- 如果为 Items 输入的名称较长，则必须调整宽度，以免下拉列表中项的名称被截断。
- 要更改宽度，也可以按住 **Ctrl+Shift** 并拖动图标的左侧或右侧。Plant Simulation 会以米为单位显示宽度。

**SimTalk：** `ObjectWidth [SimTalk] - DropDownList`

### Height [文本框] - DropDownList

输入 DropDownList 在 Frame 中显示时的高度（单位：米）。

**备注：**

- 如果输入的高度超过 30 像素，Plant Simulation 会使用更大的字体来显示下拉列表的标签。
- 要更改高度，也可以按住 **Ctrl+Shift** 并拖动图标的顶部或底部。

**SimTalk：** `ObjectHeight [SimTalk] - DropDownList`

### Value [文本框] - DropDownList

输入打开 DropDownList 时将选中哪一项。该值通过其索引号（index number）来标识。

**备注：**

- 这是你输入到 Items 列表中的项之一。

> **注意：** 如果你将选项本地化为另一种语言，通常应使用 `Value` 而不是属性 `Item`。Value 是数字，与语言无关；而 `Item` 是字符串，会因语言而异。

**SimTalk：** `Value [SimTalk] - DropDownList`

### Items [按钮] - DropDownList

点击此按钮可打开列表，在其中输入点击 DropDownList 时显示的 Items（选项）。

**备注：**

- 如果要使用索引号访问列表中的某一项，请使用属性 `Value`。
- 如果要使用名称访问列表中的某一项，请使用属性 `Item`。

**SimTalk：** `Items [SimTalk] - DropDownList`、`Item [SimTalk] - DropDownList`

### Control [DropDownList]

修改对象的内置行为。当你在 Frame 中从 DropDownList 中选择某一项时，对象会调用该 Control。

**备注：**

调用该方法时，Control 中的匿名标识符 `?` 和 `@` 会被设置为该 DropDownList。

**选择指向现有方法的路径：**

- 点击省略号按钮，在 *Select Object [for controls]* 对话框中导航到 Method 所在位置并点击 **OK**。这会把 Method 的名称插入到 Control 的文本框中。
- 在文本框中按 **F2** 打开该 Method，然后输入 Control 的源代码。
- 除了选择 Select Object，也可以在 Frame 中选中 Method，将其拖到文本框中并放下。

**创建作为对象方法的 Control：**

- 在文本框中输入一个有意义的名称，并选择 **Create Control** [上下文菜单]。Plant Simulation 会插入 `self.你为控制输入的名称`，例如 `self.A1Ctrl`。
- 在空文本框上选择 **Create Control**。Plant Simulation 会插入 `self.On对象内置控制名称`，例如 `self.OnEntrance`。

在打开的 Method 中输入该 Control 的源代码。

稍后编辑源代码：

- 按 **F2**。
- 或按住 **Shift** 并双击文本框。
- 或在上下文菜单中选择 **Open Object**。
- 或点击 **User-defined** 选项卡，并双击列表中 Method 的名称。

要删除此 Control，请删除用户自定义属性。如果仅从文本框中删除名称，用户自定义属性仍会保留。

例如，一个 Control 可能如下所示：

```simtalk
switch ?.Value
  case 1
    print "Item 1 selected"
  case 2 
    print "Item 2 selected"
end
```

**SimTalk：** `Control [SimTalk] - DropDownList`

## User-defined 选项卡

按照 *Tab User-defined* 中的说明定义你自己的属性。

## 菜单

- **Navigate Menu** —— 命令在 *Navigate Menu* 中说明。
- **View Menu** —— 命令在 *View Menu* 中说明。**SimTalk：** `updateDialog [SimTalk]`
- **Tools Menu** —— 提供访问其功能的命令：**Edit Controls**、**Edit Observers**。
- **Help Menu** —— 命令在 *Help Menu* 中说明。

## DropDownList 的方法

DropDownList 提供 *Methods of All Objects*（所有对象的通用方法）。

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类（Class）的方法、只读属性和属性 [一般说明]。
- 按 `F8` 键，或点击插入实例的 Frame 的 **Home** 功能区选项卡中的 **Show Attributes and Methods**，可显示所选实例（Instance）的方法、只读属性和属性 [一般说明]。

单个方法语法行（Syntax line）的示例可能如下所示：

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## SimTalk 引用

- `ObjectWidth`
- `ObjectHeight`
- `Value`
- `Items`
- `Item`
- `Control`
- `updateDialog`

## 另请参阅

- Select an Option from a Drop-down List
- Configure the Check Box and the Drop-down List
- Configure the Feeder Line with Sensor and Sensor Control
- Select Object [for controls]
- Tools Menu [general description]
