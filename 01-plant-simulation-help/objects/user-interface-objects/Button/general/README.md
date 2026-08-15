# README — Button (General)

本目录汇总了 **Button（按钮）** 用户界面对象的通用说明。内容来源为同目录下的 `general.md`（以及 `general.txtx` 原始文本）。

> 说明：`general` 目录下暂无子文件夹，因此不存在子文件夹内的 `README.md` 可供合并。本 README 仅基于 `general.md` 的内容总结。

## 概述

**Button（按钮）** 用于在 Frame 中显示一个按钮。当用户点击该按钮时，它会执行你在 Control 中编写的动作。

- 如果在按钮上输入了标签（label），Plant Simulation 会在 Frame 中的该按钮上显示该标签。
- 默认情况下，Plant Simulation 不会在鼠标悬停时显示按钮名称的提示（tooltip）。要显示自定义提示，可创建一个名为 `Tooltip` 的用户自定义属性。
- Plant Simulation 可以多种方式在 Frame 中显示按钮：
  - 显示你输入的标签；
  - 显示你在图标编辑器中绘制的图标（此时也可在其上显示文字标签）；
  - 显示你在图标编辑器中粘贴为图标的图片（例如可将图标命名为 `play`、`play_down`）。

基本操作提示：

- 右键点击按钮并选择上下文菜单中的 **Open**，可打开其对话框；也可点击子 Frame 中的 Button 来触发相应动作。
- 在 Frame 窗口中选择按钮：可在按钮图标上拖动一个选框（marquee）。
- 在 **Edit** 功能区选项卡点击 **Show Manipulators** 或按键盘 **M** 键，可更改按钮图形的长度和锚点。

> **注意：** Plant Simulation 仅在按钮在模型窗口中每个方向至少占据 10 像素时才接受对按钮的点击。如果缩放得太远，按钮图形可能变得过小，导致 Plant Simulation 无法可靠地识别它。

## 将对象添加到仿真模型

在 **Home** 功能区选项卡上依次点击：

> **Manage Class Library > Basic Objects > UserInterface > Button**

## Button 的对话框

右键点击插入到 Frame 中的按钮，选择上下文菜单中的 **Open** 可打开其对话框。

**编辑仿真属性：** 在对话框中可更改对象的仿真属性，共享属性在 *Dialog Items of the Objects* 中描述。

**编辑动画属性：** 在 *Edit 3D Properties* 对话框中编辑对象的 3D 属性：

- 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮；
- 或在模型中选中对象并按空格键。

要操作对象的图形，点击 **Edit** 功能区选项卡上的 **Show Manipulators** 或按键盘 **M** 键。

## Tab Attributes（属性选项卡）

**Attributes** 选项卡提供对象提供的设置，共享属性在 *Tab Attributes* 中描述。

- **Width [文本框]：** 输入对象在 Frame 中显示的宽度（单位：米）。如果输入较长文本，需调整宽度使文本不被裁切。**SimTalk：** `ObjectWidth [SimTalk] - Button`
- **Height [文本框]：** 输入对象在 Frame 中显示的高度（单位：米）。也可按住 `Ctrl+Shift` 拖动图标顶部或底部来更改高度。**SimTalk：** `ObjectHeight [SimTalk] - Button`
- **Control [按钮]：** 修改对象的内置行为。点击按钮时对象会调用该 Control。**SimTalk：** `Control [SimTalk] - Button`
  - 调用方法时会设置匿名标识符 `?` 和 `@` 指向该对象。
  - 指定不带参数的 Control 会在释放按钮时调用一次。

### 选择现有 Method 的路径

- 点击省略号按钮，在 *Select Object [for controls]* 对话框中导航到 Method 所在位置并点击 OK，将 Method 名称插入 Control 文本框。
- 在文本框中按 `F2` 打开 Method 并输入 Control 源代码。
- 也可在 Frame 中选中 Method，将其拖放到文本框。

### 创建作为对象方法的 Control

要创建数据类型为 Method 的用户自定义属性作为 Control：

- 在文本框中输入有意义的名称并选择 **Create Control [context menu]**，Plant Simulation 会插入 `self.你输入的控制名称`（如 `self.A1Ctrl`）。
- 或在空文本框上选择 **Create Control**，Plant Simulation 会插入 `self.On内置控制名称`（如 `self.OnEntrance`）。

在打开的 Method 中输入源代码；之后可通过以下方式编辑：按 `F2`、按住 `Shift` 双击文本框、在上下文菜单中选择 **Open Object**、或点击 **User-defined** 选项卡并双击列表中的 Method 名称。

删除该 Control 时删除对应的用户自定义属性；若只删除文本框中的名称，用户自定义属性仍会保留。

### 参数（Parameter）

也可指定一个接收布尔值参数的 Control：点击按钮时以 `true` 调用，释放时以 `false` 调用。

当更改按钮大小或用拖放移动按钮时，Plant Simulation 也会执行该 Control；若 Control 不接收参数，则仍像之前一样在释放按钮时调用。

**示例：**

```simtalk
self.~.~.DataTable.openDialog
self.~.~.&MyMethod.openDialog // 打开 MyMethod 的对话框，
// 而不是执行其源代码
end
```

## Tab User-defined（用户自定义选项卡）

如 *Tab User-defined* 中所述定义你自己的属性。

默认情况下 Plant Simulation 不会在 Frame 窗口中显示按钮名称的提示。要显示自定义提示，可创建名为 `Tooltip` 的用户自定义属性。

## 菜单

- **Navigate Menu：** 命令在 *Navigate Menu* 中描述。
- **View Menu：** 命令在 *View Menu* 中描述。**SimTalk：** `updateDialog [SimTalk]`
- **Tools Menu：** 提供访问其函数的命令：*Edit Controls*、*Edit Observers*。
- **Help Menu：** 命令在 *Help Menu* 中描述。

## Button 的方法

Button 提供 *Methods of All Objects*（所有对象的方法）。

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类（Class）的方法、只读属性和属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选实例（Instance）的方法、只读属性和属性。

各方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## 相关交叉引用内容

`general.md` 末尾还包含一个交叉引用的主题 **Value [SimTalk] - Checkbox**（关于复选框对象，而非按钮）：

- **Value [SimTalk] - Checkbox：** 激活（`true`）或停用（`false`）由 `<Path>` 指定的复选框。复选框值改变时会执行 Control。
- 语法：`<Path>.Value:boolean`
- 可监视（watchable）：该属性是可监视的。
- 赋值类型：可赋数据类型为 boolean 的值。
- 示例：`MyCheckbox.Value := false`
- 另请参见：Value [drop-down list] - Checkbox、Control [Checkbox]、Button。

---

*来源：Plant Simulation Help 11-5180–11-5192。未发表作品。© 2026 Siemens。*
