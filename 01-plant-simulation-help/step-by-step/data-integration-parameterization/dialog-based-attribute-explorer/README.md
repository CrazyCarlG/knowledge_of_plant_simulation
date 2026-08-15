# Dialog-Based Attribute Explorer（基于对话框的属性浏览器）总结

本目录包含 `dialog-based-attribute-explorer.md`（以及同名文本提取文件 `dialog-based-attribute-explorer.txtx`），内容为 Plant Simulation 帮助文档中 **数据集成与参数化** 章节下关于“基于对话框的属性浏览器”的说明：介绍如何通过自定义对话框（Dialog 对象）以及 AttributeExplorer 为模型对象设置参数。以下是对其内容的总结。

## 1. 概述（Overview）

本指南介绍在 Plant Simulation 模型中设置参数的两种方法：

1. **在自己的对话框中为对象设置参数（Setting Parameters for Objects in Your Own Dialog）**：创建外观与行为类似内置对话框的自定义对话框。
2. **使用 AttributeExplorer 设置参数（Setting Parameters with the AttributeExplorer）**：在单一列表窗口中管理多个对象的属性。

## 2. 在模型中设置参数（Setting Parameters in the Model）

介绍如何向仿真模型输入参数并执行带参数的仿真运行，可进行的操作包括：

- 在自己的对话框中为对象设置参数
- 使用 AttributeExplorer 设置参数
- 比较模型随机过程（Compare Model Random Processes）
- 比较运行仿真实验（Compare Run Simulation Experiments）

## 3. 在自己的对话框中为对象设置参数（Setting Parameters for Objects in Your Own Dialog）

使用 **Dialog** 对象可以：

- 为复杂仿真模型提供简单用户界面，让用户选择或输入 Plant Simulation 所需信息。
- 阻止用户直接操纵某个 Frame（例如复杂机器）：为 Frame 输入一个 Method 作为 **Open Control** 并插入自定义对话框。当用户双击该 Frame 时，Plant Simulation 调用该 Method，改为打开对话框。

> **注意：** 含有菜单的 Dialog 窗口使用 Windows 主题；不含菜单的 Dialog 窗口使用标准 Siemens PLM 主题。

可以从 Class Library 的 **UserInterface** 文件夹，或 Toolbox 的 **User Interface** 工具栏插入 Dialog。每个 Dialog 对象管理一个对话框——需要多少个对话框就插入多少个 Dialog 对象。

本节涉及：规划对话框布局与结构、设计简单对话框、设计选项卡式对话框、编写对话框项执行的动作、编写与对话框交互的动作、动态创建对话框。

## 4. 规划对话框的布局与结构（Plan Layout and Structure of Your Dialog）

设计前先考虑布局与结构：

- 按用户阅读方向排布对话框项（西方国家为从左到右、从上到下）。
- 把主要对话框项尽量放在上角附近。
- 主要命令按钮沿右边框堆叠，或沿底部排成一行；最重要的按钮放在最前。
- 决定采用扁平层级（简单对话框）还是选项卡（选项卡式对话框）。

结构决定创建顺序：

- 选项卡：先创建 **Tab Control**（容器），再创建各选项卡，再创建每个选项卡上的对话框项。
- 分组：先创建分组，再在其中插入并定位项。分组内各项的 y 坐标是相对于**该分组内部**的 y 坐标，而非整个对话框。

### 对话框项类型

| 对话框项 | 图标 |
|---|---|
| Static Text Box（静态文本框） | |
| Text Box（文本框） | |
| Button（按钮） | |
| Drop-Down List Box（下拉列表框） | |
| Group Box（分组框） | |
| Check Box（复选框） | |
| Radio Button（单选按钮） | |
| List Box（列表框） | |
| Image（图像） | |
| List View（列表视图） | |
| Tab Control（选项卡控件） | |
| Tab Page（选项卡页） | |
| Menu / menu command（菜单 / 菜单命令） | |

> **注意：** Plant Simulation 按你的 **Personalization > Font** 设置和 **Display > Scale & layout** 设置显示对话框。文本会缩放，但图像始终保持像素尺寸，因此文本可能与图像重叠。应在不同显示设置下测试对话框。

## 5. 设计简单对话框（Design a Simple Dialog）

当用户只需选择或输入少量项时使用扁平结构。

### 开始设计自己的对话框

1. 将 **Dialog** 插入 Frame（来自 UserInterface 文件夹或 User Interface 工具栏）。
2. 输入 **Name** 和 **Label**。与 Name 不同，Label 可含特殊字符和空格。
   - 输入 Label 时，Plant Simulation 在标题栏显示它；未输入时显示 Name。
3. 插入对话框项：右键点击 **Elements** 选项卡并选择相应对话框项。

可添加：菜单与菜单命令、静态文本框、文本框、下拉列表、分组框、按钮、单选按钮组、复选框、列表框、列表视图、图像。

### 其他操作

- **Show Dialog**：显示正在创建的对话框。
- **修改**项：右键点击并选择 Open。
- **删除**项：右键点击并选择 Delete。
- **改变位置**：点击 Show Dialog，再点 Edit Dialog，选中项后拖动（Dialog 立即应用坐标，移动不可撤销）。
- **显示标准按钮**：选中复选框显示，清除则隐藏。若隐藏则必须自定义按钮。
- **Open Modal**：选中后阻止用户打开其他 Plant Simulation 窗口，直到对话框关闭。
- **Position 选项卡**：以像素设置 X-Position 和 Y-Position。两者默认 `-1` 使对话框在屏幕居中（零点为左上角）。

## 6. 添加菜单与菜单命令（Add a Menu and Menu Commands）

### 添加菜单

- 右键点击 **Elements** 选项卡，选择 **New Menu / New Menu Command**。
- 输入 **Name**（Method 可用此名调用该项）。
- 输入 **Caption**（菜单显示的内容）。`&` 符号指定访问键（如 `&Show`）。
- 顶层菜单本身不需要 Callback Argument。

### 添加菜单命令

- 右键点击菜单名，选择 **New Menu / Menu Command**。
- 输入 Name 和 Caption（如 `&Chart`、`&Report`）。
- 要显示字面 `&` 需输入两次（`Drag && Drop`）。
- 输入 **Callback Argument**（如 `CallbackChart`、`CallbackReport`），传给回调方法。
- 添加子菜单：右键点击某菜单命令再次选择 **New Menu / Menu Command**。

### 回调方法

回调方法是数据类型为 `method` 的用户自定义属性。在 User-defined 选项卡双击 `callback` 并点击 Open。输入命令前点击 **Inherit Source Code** 使其**不**被选中。

默认源码如下：

```simtalk
param action: string
switch action
case "Open"
                // TODO: add code for the "Open" action here
                // for example ?.setCaption("TextBox", "Test")
                // for example ?.setCheckBox("CheckBox", true)
case "Apply"
                // TODO: add code for the "Apply" action here
                // for example print ?.getValue("TextBox")
                // for example print ?.GetCheckBox("CheckBox")
case "Close"
                // TODO: add code for the "Close" action here
end
```

打开对象 `MyChart`：

```simtalk
case "CallbackChart" 
   MyChart.IsShown := true 
```

打开对象 `MyReport`：

```simtalk
case "CallbackReport" 
   MyReport.show 
```

改变菜单命令顺序：在 Elements 选项卡选中一个，按住 Shift 并按上/下方向键。

## 7. 添加静态文本框（Add a Static Text Box）

显示用户可查看但不可编辑的文本。

- 右键 **Elements** → **New Static Text Box**。
- 输入 **Name**、**Caption**（显示内容）、**X/Y 坐标**。
- 位置对应系统字体字符的平均宽度，而非像素。
- 选择是否 **Enable**，然后点击 OK。

> **注意：** 若看不到某对话框项，检查位置设置——相同坐标会把各项叠在一起。

## 8. 添加文本框（Add a Text Box）

用户可输入或编辑文本的字段。

- 右键 **Elements** → **New Edit Text Box**。
- 输入 **Name**、**Callback Argument**。
- 选择用户可输入的 **Data Type**：

| 选择 | 用户可输入 |
|---|---|
| Any Character | 任意字符（特殊字符、字母、数字） |
| Alphanumeric Characters | 空格、字母、数字 |
| Letters | 大小写字母 |
| Decimal Numbers | `0123456789` |
| Signed Decimal Numbers | `-0123456789` 或 `+0123456789` |
| Hexadecimal Numbers | 如 `ADbf09` |
| Octal Numbers | `01234567`（不能是 `18`） |
| Binary Numbers | `0` 或 `1` |
| Floating Point Numbers | 如 `12.3E-43` |

- 输入 **X/Y 坐标** 和 **Width**（默认 `0` 使用系统值）。
- 选择 **Enable**，可选 **Password** 用上标小写 x 遮蔽文本。

## 9. 添加下拉列表（Add a Drop-down List）

用户选择单个项；收起时显示当前值。

- 右键 **Elements** → **New DropDownList Box**。
- 输入 **Name**、**Callback Argument**、**X/Y 坐标**、**Width**。
- 点击 **Items** 并输入各项：
  - 添加：输入名称，点击 Insert 或按 Enter。
  - 删除：选中后点击 Delete。
  - 上移：选中后点击 Move Up。
  - 重命名：选中、输入新名称、点击 Rename。
  - OK / Cancel。
- 选择 **Enable**，然后点击 OK。

## 10. 为对话框项添加分组框（Add a Group Box Around Dialog Items）

用外框图形化地把一组项圈在一起。

- 先创建分组，再在其中插入并定位各项。
- 右键 **Elements** → **New Group Box**。
- 输入 **Name**、**Caption**、**X/Y 坐标**、**Width** 和 **Height**。
- 选择 **Enable**，然后点击 OK。
- 改变分组内项的顺序：选中项，按住 Shift 并按上/下方向键。

## 11. 添加一组单选按钮（Add a Set of Radio Buttons）

从一组互斥选项中选中单个设置。

- 右键 **Elements** → **New Radio Button**。
- 输入 **Name**、**Caption**、**Callback Argument**、**X/Y 坐标**。
- 输入一个数字 **group id** 把属于同一组的单选按钮分组。每组同一时刻只能选中一个。

> **注意：** 顺序创建单选按钮组的所有项（Plant Simulation 按行/列位置创建项）。Windows 忽略 Group ID，按 Y 坐标逐行分组。要把单选按钮并排成两列，请将它们放在分组框内。

- 选择 **Enable**，然后点击 OK。对其他单选按钮重复。

## 12. 添加复选框（Add a Check Box）

显示互不排斥的一项或多项设置；用户可同时选中/清除多个。

- 右键 **Elements** → **New Check Box**。
- 输入 **Name**、**Caption**、**Callback Argument**、**X/Y 坐标**。
- 选择 **Enable**，然后点击 OK。

## 13. 设计选项卡式对话框（Design a Tabbed Dialog）

当用户要选择或输入多种不同类型的信息时使用选项卡式对话框。

起始步骤与简单对话框相同（插入 Dialog、输入 Name/Label、通过 Elements 选项卡添加项）。

还可添加：添加 Tab Control、向 Tab Control 添加选项卡、（文档原文提及）从对象分离相机。

同样适用：Show Dialog、Edit Dialog（拖动重定位）、标准按钮、Open Modal、Position 选项卡。

## 14. 添加选项卡控件（Add a Tab Control）

Tab Control 是容纳各选项卡（页）的容器，不要与选项卡本身混淆。

当用户选择另一个选项卡时，Dialog 调用 **Callback Method**，执行以第一个参数（Callback Argument）编程的动作。

- 右键 **Elements** → **New Tab Control**。
- 输入 **Name**、**Callback Argument**、**X/Y 坐标**、**Width** 和 **Height**（默认 `0` 使用系统值）。
- 点击 OK。
- 添加选项卡：在 Elements 选项卡右键 Tab Control，选择 **New Tab Page**。
- 改变选项卡顺序：选中选项卡，按住 Shift 并按上/下方向键（第一个选项卡在最左）。

## 15. 向选项卡控件添加选项卡（Add Tabs to a Tab Control）

向 Tab Control 容器添加各个选项卡。

- 右键 **Elements** → **New Tab Page**。
- 输入 **Name** 和 **Caption**（显示为选项卡标题）。
- 点击 OK。
- 重排：选中选项卡，用 Shift + 上/下方向键。

## 16. 添加列表框（Add a List Box）

显示选项列表；用户双击选择。与下拉列表不同，它有固定大小且不收起。

- 右键 **Elements** → **New List Box**。
- 输入 **Name**、**Callback Argument**、**X/Y 坐标**、**Width** 和 **Height**。
- 若列表项数超过高度可显示范围，会自动加垂直滚动条。
- 点击 **Items** 输入各项（Insert/Delete/Move Up/Rename/OK/Cancel 操作同上）。
- 选择 **Enable**，然后点击 OK。

## 17. 添加列表视图（Add a List View）

在对话框中显示一个表格。

> **注意：** 显示字符串时，Plant Simulation 只显示前 260 个字符。

- 右键 **Elements** → **New List View**。
- 输入 **Name**、**Callback Argument**。
- 输入表格名称或点击按钮选择表格。
  - 在 DataTable 中激活列索引并输入列标题。
  - 在单元格中输入项。
- 输入 **X/Y 坐标**、**Width** 和 **Height**。
- 选择 **Enable**，然后点击 OK。

## 18. 添加按钮（Add a Button）

被点击时以 Callback Argument 调用 Callback Method。

- 右键 **Elements** → **New Button**。
- 输入 **Name**、**Caption**、**Callback Argument**、**X/Y 坐标**、**Width**（默认 `0` = OK 按钮的宽度）。
- 选择 **Enable**，然后点击 OK。

## 19. 添加图像（Add an Image）

为 Dialog 定义图片/图标。可输入数字或名称（如 `Icon1`）。

- 右键 **Elements** → **New Image**。
- 输入 **Name**、**X/Y 坐标**、**Width** 和 **Height**。
- 输入 **Image ID**（图标编号）或图像名称。
- 点击 OK。

## 20. 动态创建对话框（Create a Dialog Dynamically）

也可根据建模需要，在模型中动态创建 Dialog。

### 动态创建对话框的步骤

1. 插入一个 **Method**、一个 **DataTable** 和一个 **Dialog**（示例中命名为 `MyDynamicDialog`）。
2. 在名为 `createDialog` 的 Method 中编写各选项卡显示的内容。
3. 把 Tab 3 上显示的各项输入名为 `MyTable` 的 DataTable。
4. 运行 `createDialog` 构建并显示 Dialog。
5. 编写双击 Tab 3 表格中某行时的动作。

### `createDialog` 示例代码

```simtalk
Dialog.Label := "My Dynamic Dialog"; print Dialog.Label
var testBool:boolean := true
Dialog.clearData
testBool := testBool AND Dialog.createTabControl("TabControl", 0, 0, 45, 10)
testBool := testBool AND Dialog.createTabPage("Tab 1","TabControl")
   testBool := testBool AND Dialog.createTabPage("Tab 2","TabControl")
   testBool := testBool AND Dialog.createTabPage("Tab 3","TabControl")
-- Menus
testBool := testBool AND Dialog.createMenu("Show")
testBool := testBool AND Dialog.createMenu("Item 1","Show")
testBool := testBool AND Dialog.createMenu("Item 2","Show")
dialog.setCallbackArgument("Item 1","Item 1 Arg")
dialog.setCallbackArgument("Item 2","Item 2 Arg")
-- Groups on different pages
testBool := testBool AND Dialog.createGroupBox("Group 1", 0,1, 40,3,"Tab 1")
testBool := testBool AND Dialog.createGroupBox("Group 2", 0,4, 40,4,"Tab 1")
testBool := testBool AND Dialog.createGroupBox("Group 1", 0,0, 40,3,"Tab 2")
testBool := testBool AND Dialog.createGroupBox("Group 2", 0,4, 18,4,"Tab 2")
testBool := testBool AND Dialog.createGroupBox("Group 3", 22,4, 18,4,"Tab 2")
-- static text outside a group
testBool := testBool AND Dialog.createStaticTextBox("Static text", 0,0,"Tab 1")
testBool := testBool AND Dialog.createStaticTextBox("Static text", 0,0,"Tab 3")
Dialog.setCaption("Tab 3.Static text","Double-click a row ...")
-- static text inside a group
testBool := testBool AND Dialog.createStaticTextBox("Click the button", 0,0,"Tab 1.Group 2")
-- Checkboxes
testBool := testBool AND Dialog.createCheckBox(" Check box 1", 15,0,"Tab 1")
testBool := testBool AND Dialog.createCheckBox(" Check box 2", 20,0,"Group 2")
   testBool := testBool AND dialog.setCaption(" Check box 2","Checkbox Gr 2")-- true
   dialog.setCallbackArgument(" Check box 2","CheckboxGr2")
-- checkbox with action
testBool := testBool AND Dialog.createCheckBox("Check box", 1,0,"Tab 1.Group 1")
testBool := testBool AND Dialog.setCaption("Check box","Active")
dialog.setCallbackArgument("Check box","Check box")
-- Buttons
testBool := testBool AND Dialog.createButton("My_Button", 0, 1, 13, "Group 2")
testBool := testBool AND dialog.setCaption("My_Button","Security")-- true
dialog.setCallbackArgument("My_Button","Button Arg")
testBool := testBool AND Dialog.createButton("A_Button", 0, 1, 13, "Tab 1.Group 1")
testBool := testBool AND Dialog.setCaption("A_Button","Attention")
Dialog.setSensitive("A_Button",false)
-- Radiobuttons and their groupings in a single group
testBool := testBool AND Dialog.createRadioButton("RadioButton 1",  3, 0,"Tab 2.Group 1")
testBool := testBool AND Dialog.createRadioButton("RadioButton 2", 20, 0,"Tab 2.Group 1")
testBool := testBool AND Dialog.createRadioButton("RadioButton 3",  3, 1,"Tab 2.Group 1")
testBool := testBool AND Dialog.createRadioButton("RadioButton 4", 20, 1,"Tab 2.Group 1")
Dialog.setGroupID("RadioButton 1", 1)-- row 0
Dialog.setGroupID("RadioButton 2", 1)-- row 0
Dialog.setGroupID("RadioButton 3", 2)-- row 1
Dialog.setGroupID("RadioButton 4", 2)-- row 1
-- radio button in different groups
testBool := testBool AND Dialog.createRadioButton("RB 1", 1, 0,"Tab 2.Group 2")
testBool := testBool AND Dialog.createRadioButton("RB 2", 1, 1,"Tab 2.Group 2")
testBool := testBool AND Dialog.createRadioButton("RB 3", 1, 0,"Tab 2.Group 3")
testBool := testBool AND Dialog.createRadioButton("RB 4", 1, 1,"Tab 2.Group 3")
Dialog.setGroupID("RB 1", 1)
Dialog.setGroupID("RB 2", 1)
Dialog.setGroupID("RB 3", 2)
Dialog.setGroupID("RB 4", 2)
-- Image in the dialog
testBool := testBool AND Dialog.createImage("My_Image", 25, 0, "Tab 1.Group 1")
dialog.setIcon("My_Image","my icon")
testBool := testBool AND (dialog.getIcon("My_Image")= "my icon")
-- DropDownList
testBool := testBool AND dialog.createDropDownListBox("unit", 14, 1,10,"Tab 1.Group 1")
var units:list[string]
units.create
units.insert(1,"mm")
units.insert(2,"m")
units.insert(3,"km")
testBool := testBool AND dialog.setList("unit",units)
dialog.setCallbackArgument("unit","DropDownList")
-- List box
testBool := testBool AND dialog.createListBox("ListBox", 17, 1, 18, 2, "Tab 1.Group 2")
testBool := testBool AND dialog.setList("ListBox",units)
dialog.setCallbackArgument("ListBox","ListBox Arg")
-- List view
testBool := testBool AND dialog.createListView("List view", 0, 2, 36, 6, "Tab 3")
testBool := testBool AND dialog.setTable("List view",MyTable)
dialog.setCallbackArgument("List view","List view Arg")
-- TextBox
testBool := testBool AND dialog.createEditTextBox("Text Box", 0, 2, 13,"Tab 1.Group 2")
testBool := testBool AND dialog.setCaption("Text Box", "Enter Password")
testBool := testBool AND dialog.setPasswordMasking("Text Box",true)
dialog.open
print testBool
```

### 动作示例代码（双击 Tab 3 中的某行）

```simtalk
param action : string
var row:integer
print "Action : ",action
switch action
case "Open" 
case "Apply" 
case "Close" 
case "Button Arg" 
    @.setPasswordMasking("Text Box",NOT @.getPasswordMasking("Text Box"))
case "List view Arg" 
    row := @.getIndex("List view")
    promptmessage(to_str("Where is the ", MyTable[1,row],"?"))
case "Check box" 
    @.setSensitive("A_Button", @.getCheckBox("Check box"))
end
```

双击表格某行会弹出消息框：`Where is the ...?`

## 21. 编写对话框项执行的动作（Program Actions which the Dialog Items Execute）

编写用户输入/选择设置时对话框项执行的动作。把源码输入**回调方法**。

- 默认回调方法是数据类型为 `method` 的用户自定义属性 `self.callback`。
  - 通过 **Method** 选项卡打开（点击 Callback Method 文本框，按 F2 或 Shift+双击 Callback）。
  - 或通过 **User-defined Attributes** 选项卡（双击 Callback，再 Open）。
- 也可使用 Frame 或 Class Library 文件夹中的 Method（当多个对话框共享同一回调方法时很有用）。

为每个对话框项输入 **Callback Argument** 及要执行的语句。参数**区分大小写**。

当用户执行以下操作时，回调方法执行回调参数：

- 关闭下拉列表框。
- 在列表框中选中并双击某项。
- 改变文本框内容并选择另一项，或点击 OK/Apply/Cancel。
- 点击按钮。
- 选中/清除复选框。
- 选中单选按钮。
- 在列表视图中选中并双击某行。
- 在选项卡控件中选择选项卡。
- 选择菜单或菜单命令。

打开 `MyChart` 的示例：

```simtalk
case "CallbackChart" 
   MyChart.IsShown := true 
```

打开 `MyReport`：

```simtalk
case "CallbackReport" 
   MyReport.show 
```

## 22. 编写与对话框交互的动作（Program Actions for Interacting with the Dialog）

编写用户打开对话框、应用设置、关闭对话框时发生的行为（作为回调方法中的回调参数）。

- **Open** 段：用户打开对话框时执行。初始化内容/把对话框项设为某值。
- **Apply** 段：用户点击 OK 或 Apply 时执行。评估新增或已更改的值。
- **Close** 段：用户点击 Cancel 或用标题栏关闭按钮关闭时执行。

> **注意：** 点击 **OK** 会执行回调方法两次（先 Apply，再 Close）。点击 **Apply** 只执行 Apply 段。

### 示例源码

```simtalk
param action: string
switch action
case "Open" 
   @.setIndex("VariantType", @.VariantNo)
   @.setCheckbox("SunRoof", true)
   @.setValue("Vanity text", "Enter your text")
case "Apply" 
   @.VariantNo := @.getIndex("VariantType")
case "Close"
// no action is required
case "CallbackChart" 
   MyChart.IsShown := true 
case "CallbackReport" 
   MyReport.show
end 
```

对话框打开时：Plant Simulation 把车型设为用户自定义属性 `VariantNo`，选中天窗复选框，并提示输入自定义文本。

## 23. 使用 AttributeExplorer 设置参数（Setting Parameters with the AttributeExplorer）

不必打开每个对象的对话框，**AttributeExplorer** 定义要获取并显示的哪些对象的哪些属性，点击 **Show Explorer** 时在列表窗口中显示。

好处：

- 在单一位置管理各工位的属性。
- 为产能、时间等输入不同值；Plant Simulation 会把值写回对象对话框。
- 将设置表导出为制表符分隔的文本文件，导入另一模型获得相同设置。
- 查找特定类型和属性（如位置）的对象并在 Frame 中对齐它们。

从 Class Library 的 **InformationFlow** 文件夹，或 Toolbox 的 **Information Flow** 工具栏插入 AttributeExplorer。

本节涉及：指定要参数化的对象、指定要查看或更改的属性、选择对象与名称的显示方式、查找对象与属性。

## 24. 指定要参数化的对象（Specify the Objects You Want to Parametrize）

输入数据前点击 **Inheritance** 复选框。

- **查看/编辑某对象的属性：** 把对象从 Frame 拖到 **Objects** 选项卡上放下。Plant Simulation 把绝对路径和名称插入选中单元格。
  - 可一次拖放多个对象，按选择顺序添加。
- **仅添加名称：** 把对象拖到 AttributeExplorer 的图标上。
- **查看/编辑某类的所有对象的属性：** 点击 **Query** 选项卡，输入 Attribute 为 `InternalClassType`，Value 为内部类类型。

> **注意：** 对内置对象，只读属性 `InternalClassType` 返回对象类型。

点击 **Show Explorer** 查看所定义的内容。

## 25. 指定要查看或更改的属性（Specify the Attributes You Want to View or Change）

输入数据前点击 **Inheritance** 复选框。

- 在 **Name** 列单元格输入属性名，或点击 **Show Attributes**。

在 **Show Attributes** 对话框中：

- 点击并选择要显示其属性的 Object。
- 选择 **Built-in Attributes** 或 **User-defined Attributes**。
- 选择单个或多个连续属性（Shift+点击）并加入 **Explorer Attributes**。
- 点击 OK 添加到 Attributes 选项卡。

其他设置：

- **Alias** 列：为属性输入描述性术语。
- **Read Only** 列：点击使某属性只读。

### 单元格背景色

| 颜色 | 含义 |
|---|---|
| 蓝色 | 属性不可监视（not watchable） |
| 白色 | 属性可监视（watchable） |
| 灰色 | 为内置属性输入了错误名称 |

## 26. 选择对象与名称的显示方式（Select How to Show the Objects and the Names）

输入数据前点击 **Inheritance** 复选框。

选择对添加的属性做何操作：

- **Edit**：允许编辑值。点击 Show Explorer，点击单元格输入值；点击 Apply/OK 后写回。
- **Watch**：显示可监视属性值（仅查看）。背景色表示可监视性（蓝=不可监视、白=可监视、灰=内置名称错误）。
- **Read Only**：仅显示值（仅查看）。

选择最左列对象的显示方式：

- 完整 **Path**（拖到 Data 选项卡插入绝对路径）。
- 仅 **Name**（拖到图标插入名称）。
- 仅 **Label**。

选择属性的显示方式：

- 用其 **Name**。
- 用其 **Alias**（在 Attributes 选项卡输入）。

可选输入 **Comment**（Shift+Enter 换行）。选中 **Show comment** 并点击 Apply，将其显示在列表上方。

## 27. 查找对象与属性（Find Objects and Attributes）

用 AttributeExplorer 在模型中查找对象。在 **Query** 选项卡输入条件，点击 **Show Explorer** —— Explorer 只显示匹配的对象。

要同时更改属性，在 Attributes 选项卡输入属性名，并在 Data 选项卡选择 **Edit**。

在 Query 表中可以：

- 选择起始 **Parentheses**（括号）数量。
- 输入任意属性名（如 Show Attributes and Methods 中所示）。
- 选择 **Condition**：

| 条件 | 含义 |
|---|---|
| `<` | 小于 |
| `<=` | 小于或等于 |
| `>` | 大于 |
| `>=` | 大于或等于 |
| `=` | 等于（对 real、length、height、speed、time 为精确相等） |
| `~=` | 等于，不区分大小写（字符串）/ 约等于（数值） |
| `/=` | 不等于 |
| `Expr` | 正则表达式（如 `^Inf` 查找以 "Inf" 开头的词） |
| `Exists` | 检查对象是否具有该属性 |

- 输入要查找的 **Value**。
- 选择结束 **Parentheses** 数量。
- 选择布尔 **Operator**（`and` / `or`）连接本行与下一行。
- 输入 **Comment**。
- 选择开始搜索的 **Frame**。
- 选择 **Include Subframes** 以包含嵌套 Frame。

> **注意：** 此设置在 Data 选项卡上选择“显示带路径的对象”。

## 目录说明

- `dialog-based-attribute-explorer.md`：基于对话框的属性浏览器章节的 Markdown 版本（本总结的源文件）。
- `dialog-based-attribute-explorer.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Dialog-Based Attribute Explorer"。Unpublished work. © 2026 Siemens.*
