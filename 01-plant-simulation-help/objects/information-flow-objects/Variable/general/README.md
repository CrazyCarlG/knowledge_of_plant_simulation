# Variable 对象 — General（总览）

本目录包含 **Variable 对象**（信息流对象）的通用说明。文档描述的是 Variable 对象本身，即 Plant Simulation 中用于在仿真运行期间长期存储数据的全局变量。

> 源文件：`general.md`（内容详见该文件）；原始导出文本：`general.txtx`。

## 概述

**Variable** 是一个全局变量，在仿真运行期间可被 Plant Simulation 中的其他对象和方法访问。变量可表示存储一个数量的未知项；变量可以改变其内容，因此也称为占位符或未知数。与 Variable 相对的是常量（constant），其值已知且不改变。

Variable 的典型用途：

- 在仿真运行期间长期存储数据
- 递增或递减值
- 赋值

数据类型为 `list`、`queue`、`stack` 或 `table` 的 Variable 在插入时，其名称左侧会显示一个类型图形。

- 双击 Variable 的**名称**打开其对话框（也可右键选择 **Open**）。
- 双击 Variable 的**类型图形**打开对应列表对象的窗口。

此外，Plant Simulation 还提供**局部变量**：必须先在其所在源码中声明才能使用，且仅在声明它的 Method 中有效，方法调用结束时删除。

- 可在 HtmlReport 中显示 Variable 的内容（参见 *Display a Variable*）。
- 将鼠标悬停在 Variable 上可显示工具提示。
- 要修改图形长度和锚点，点击 Edit 功能区选项卡上的 **Show Manipulators** 或按 `M`。

## 添加到仿真模型

在 Home 功能区选项卡点击 **Manage Class Library > Basic Objects > InformationFlow > Variable**，将 Variable 加入模型。

## 对话框（Dialog Box）

双击 Variable 图标打开其对话框：

- **Edit Simulation Properties** — 修改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties** — 通过 **Edit 3D Properties** 按钮编辑 3D 属性，或选中对象后按空格键。

## Name [文本框]

显示 Variable 的当前名称，既可是内置名称，也可是你指定的名称。

备注：可输入字母、数字和下划线（`_`）的组合，例如 `MyVariable`、`MyVariable1`、`My_Variable_1`。对象名称不能以数字开头（例如不允许 `1Variable`）。

## Tab Value

### Data Type [Variable]

从下拉列表中选择 Variable 的数据类型，可使用任意受支持的数据类型。

- 数据类型 `object`：在 **Value** 文本框中输入对象的路径和名称（相对路径的起点是插入该 Variable 的 Frame），或点击按钮在 **Select Object** 对话框中选择对象，也可将对象拖放到 Variable 上——Plant Simulation 会插入对该对象的引用。
- 用 `time` 类型配合随机数分布：选择数据类型 `randtime` 并输入分布函数的参数（`time` 只接受常量值），然后在访问前初始化 randtime 值，例如用方法 `rollDice`。

注意：对于列表数据类型（`table`、`list`、`stack`、`queue`），可使用方法 `unshare`。

对于 Data Type `[用户自定义属性] > real、length、weight、time、speed、acceleration`，可输入小数位（Decimal Places）和整数位（Integer Places）的数量。

### Value [Variable]

选择或输入 Variable 显示的值。所选数据类型决定了操作方式：从下拉列表选择，或直接输入值。

注意：对于 `length`、`weight`、`speed` 类型，**File > Model Settings/Preferences > Units > Mass/Speed/Length** 中选定的单位决定了 Plant Simulation 如何解释该值（例如值 `100` 且 length 设为 `km` 时解释为 100 km）。

- 点击 **Open** 打开与 `table`、`list`、`stack`、`queue` 数据类型对应对象的对话框。
- 若 Variable 指向一个被其他位置/对象引用的列表，对话框会显示 **Unshare** 按钮。

**取消共享（Unshare）一个 Variable：** 点击 **Unshare** 让 Plant Simulation 为该 Variable 分配其自己的列表副本，而不是共享内容（对应方法 `unshare`）。

- 点击按钮在 **Select Object** 对话框中选择 `object` 数据类型的对象，或在 **Value** 中输入对象的路径和名称。
- 按 `F2` 可打开你在文本框中输入名称的对象的对话框。

数据类型 `object` 表示对象的绝对路径或相对路径：

- **绝对路径**始终以句点开头，从 Class Library 开始（例如 `.building`），唯一标识对象。若派生或插入使用 Variable 对象的 Frame，Plant Simulation 不会改变绝对路径——它仍然引用源对象。
- **相对路径**以 `Location` 或 `~` 开头，每次访问 Variable 对象时都考虑 Variable 对象的当前位置。

### Inherit Value [Variable]

要继承 Variable 的值，点击 **Value** 旁的继承复选框使其变为绿色；再次点击则取消继承。

### Initial Value [Variable]

勾选此复选框可将 Variable 在仿真运行期间记录的值复位为初始值。Plant Simulation 在复位阶段设置该值，并在下一次仿真运行的 init 阶段将其复位。

勾选后会出现一个文本框——输入下一次仿真运行的初始值。

注意：数据类型 `table`、`list`、`stack`、`queue` 和 `randtime` 不提供此功能。

## Tab Display

选择 Plant Simulation 在 Frame 窗口中如何显示全局 Variable。

### Font Size [下拉列表]

选择 Variable 在 Frame 中显示的字体大小：**Small**、**Medium**、**Large**、**Extra large**。

### Font Color [Variable]

选择字体颜色。可选预定义颜色，或点击 **More Colors** 后点击 **Select** 在颜色矩阵中选择颜色。

### Background Color [下拉列表]

选择 Variable 背景的颜色，选项与字体颜色相同（预定义 / **More Colors**）。

### Alignment [Variable]

选择 Variable 显示内容与其插入点的对齐方式：

- **Left** — 将 Variable 与类型图形的左边框对齐。
- **Name** — 将显示的 Name 或 Value 的左边框放在插入点上。
- **Value** — 将显示的 Name 的右边框或 Value 的左边框放在插入点上。
- **Right** — 将显示的 Name 或 Value 的右边框放在插入点上。

### Integer Places [文本框]

输入 Variable 显示的整数位数（最多 15 位）。默认 `-1` 表示不设最小值；正值在 3D 显示中用空格填充小数点前的空间。

注意：仅适用于 Data Type `[用户自定义属性] > real、length、weight、time、speed、acceleration`。

### Decimal Places [文本框]

输入 Variable 显示的小数位数（最多 15 位）。默认 `-1` 显示所有现有位数。

注意：仅适用于 `Data Type > real、length、money、weight、time、speed、acceleration`。对于 `time`，`-1` 表示默认时间显示格式（四位小数）；正值表示最多显示该位数。

### Transparent [复选框]

勾选使 Variable 背景透明（显示 Frame 背景色）。清除则文字周围空间显示为白色。

### Show Data Type [Variable]

勾选在 Variable 的名称和值之外还显示数据类型。清除则隐藏。

### Show Units [Variable]

勾选显示 Variable 物理量的单位（单位在 **File > Model Settings/Preferences > Units** 中选择）。对于 `randtime`，**Show Units** 还决定 Plant Simulation 是否显示分布参数。清除 **Show Units** 后，可输入小数位数。

## Tab Statistics

该选项卡显示前五频率和前五持续时间。只有数据类型为 `string` 或 `integer` 的 Variable 会记录统计值。

### Active [复选框] — statistics

勾选后可在仿真运行期间收集统计数据，并显示 **Top 5 Frequencies** 和 **Top 5 Durations**。只有 `string` 或 `integer` 类型的 Variable 记录统计值，且仅当值存在的时间跨度大于零时才记录。

示例——一个 `integer` 类型、Initial Value 为 `0` 的 Variable：

```simtalk
Variable = 1
wait 1
Variable = 2
wait 1
Variable = 1
Variable = 3
wait 1
```

`1`、`2`、`3` 的频率各为 `1`（第二次赋值为 `1` 的时间跨度为 0）。初始值 `0` 也不记录（时间跨度为 0）。因此 `1`、`2`、`3` 的持续时间各为 `33.33%`。

### Statistics Table [Variable]

点击打开统计表，显示以下值：

| 项目 | 描述 |
| --- | --- |
| Value | 显示 Variable 值的名称。 |
| Frequency | 该值出现的次数（仅在实际变化时计数）。 |
| Duration | 该值在统计周期内的完整持续时间。 |
| Frequency [%] | 各频率占 Frequency 列所有值总和的比例。 |
| Duration [%] | 各持续时间占 Duration 列所有值总和的比例。 |
| Mean Duration | 各持续时间的平均持续时间。 |
| Standard Deviation | 持续时间的标准差。 |

### Charts [Variable]

点击打开饼图，显示值的频率和持续时间。

### Frequency Histogram [Variable]

点击打开直方图，显示值出现的频率（次数）。

## Tab Comment [Variable]

输入描述 Variable 功能的注释。先点击复选框关闭继承，然后才能输入数据。将鼠标拖过对象时，注释会作为工具提示显示（按你输入时的格式，即按 Enter 手动指定的换行）。

## 菜单

- **Navigate Menu** — 命令见 Navigate Menu 描述。
- **View Menu** — `Refresh`、`Show Attributes and Methods`（SimTalk：`updateDialog`）。
- **Tools Menu** — `Edit Controls`、`Edit Observers`。
- **Help Menu** — 命令见 Help Menu 描述。

## 给 Variable 赋值

赋新值时，该值必须与当前数据类型兼容。兼容意味着 Plant Simulation 能将其自动转换为正确的值。值改变可能因为：

- Plant Simulation 无法显示小数点后的数字而将其截断（例如 real 值 `3.9` → integer 值 `3`）。
- 数值差异巨大时发生有效数字丢失（浮点运算只保存一定位数的数字；这种误差无法避免，且仅在大小差异至少为 `10⁷` 时发生）。

若把 Variable 赋给 Method，仅输入 Method 名称时 Plant Simulation 会调用并执行该 Method。使用引用运算符 `&` 可获取 `object` 数据类型 Variable 所需的引用。

语法：

```simtalk
Path := any
```

示例：

```simtalk
Variable := Value
Variable := &MyMethod
```

## 调用 Variable 的内容

若 Variable 的内容引用另一个 `object` 数据类型的 Variable，用括号括起该 Variable 名称即可访问其内容。若引用的是 Method，用括号括起该 Method 名称会调用该 Method 本身。

语法：

```simtalk
(Path)
```

示例：

```simtalk
value := (Variable) + 1   -- 访问该变量
(control_gate)            -- 调用该方法
(method)(3.4,"drill")     -- 带参数调用该方法
```

## 读取 Variable 的内容

要访问 `<Path>` 指定的 Variable 内容，直接使用其名称。

语法：

```simtalk
<Path>
```

示例：

```simtalk
MyTable[1,1] := MyVariable
```

## Variable 的方法

Variable 对象提供目录表中列出的方法，以及所有对象的通用方法（*Methods of All Objects*）。

注意：只能通过引用运算符 `&` 访问作用于 Variable 对象本身的方法；没有运算符时，方法会作用于 Variable 的内容。

示例：

```simtalk
.MyPlant.&MyVariable.openDialog
```

要查看对象的所有方法、只读属性和属性，打开窗口 **Show Attributes and Methods**。

## 参见

- Display a Value During the Simulation with a Variable
- Video on YouTube: <https://youtu.be/MXDcx2yplxc?si=PZPyKkBoAAWm4ns_&t=865>
