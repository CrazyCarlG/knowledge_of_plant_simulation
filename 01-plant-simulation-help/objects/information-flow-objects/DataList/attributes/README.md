# DataList — Attributes（属性）

本目录汇总 **DataList 对象**（信息流对象）的属性（Attributes）相关文档，并综合同一级目录下 `general`、`methods`、`read-only-attributes` 三个子目录的 README 内容。目录内容来源于 `attributes.md`（以及同内容的源文件 `attributes.txtx`）。

## 概述

DataList 是 Plant Simulation 中的单列列表（single-column list），可通过行号（位置）对单个单元格进行随机访问。其行为类似于卡片盒（file-card box）：

- 添加条目时，后续条目依次下移。
- 条目可以被删除。
- 条目可以被读取并重新添加。

DataList 提供：

- 列表和表格（Lists and Tables）的属性。
- 所有对象（All Objects）的属性。

## 查看属性与方法

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，显示所选**类（Class）**的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，显示所选**实例（Instance）**的方法、只读属性和属性。

## 设置与获取属性值

属性的值既可以通过对话框中的复选框、文本框和下拉列表设置，也可以通过赋值语句设置或获取。

- 设置属性值，示例：

```simtalk
myDataList.InfoflowReadOnly := true
```

- 获取属性值，示例：

```simtalk
print myDataList.InfoflowReadOnly
posit := Station.Cont.XPos
```

## 相关对象：DataStack

使用 **DataStack** 对象可按 **LIFO**（Last In First Out，后进先出）方式访问数据。

- **DataQueue** 与 **DataStack** 都是只有一列的列表，它们共享所有方法和属性，区别仅在于内置特性：
  - DataStack 使用 **LIFO** 方式访问内容。
  - DataQueue 使用 **FIFO**（First In First Out，先进先出）方式访问内容。
- 将鼠标悬停在 DataStack 上可显示包含其信息的工具提示。
- 要修改 DataStack 图形的长度和锚点，可点击 Edit 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

### 将 DataStack 添加到仿真模型

点击 Home 功能区选项卡上的：

> **Manage Class Library > Basic Objects > InformationFlow > DataStack**

## 通用说明（general）

- DataList 在后台打开时位于打开的对话框后面；可使用 `openDialogBox` 方法将其置于前台。
- DataList 与数据类型 `List` 共享内置属性。
- **对象** DataList（可插入模型）与**数据类型** `list` 不同：
  - 数据类型 `list` 的用户自定义属性和局部/全局变量属于其他对象的一部分，不是独立对象，也没有自己的图标。
  - 因此它们无法识别 `Location`、`existsIcon` 等 SimTalk 函数；除此之外的其他方法（尤其是读写访问）两者通用。
- 列表对象的功能位于 **List Ribbon Tab**（列表功能区选项卡）上。
- 将 DataList 添加到仿真模型：点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > InformationFlow > DataList**。
- 双击 DataList 图标可打开其窗口修改仿真属性；在 3D 模型中选中对象并按空格键可编辑 3D 属性。

## 方法（methods）

DataList 提供以下方法分组：

- 本对象自身的方法（见下方方法列表）。
- 列表和表格的共享方法（*The Methods of Lists and Tables*）。
- 所有对象的共享方法（*The Methods of All Objects*）。

### 方法列表

| 方法 | 说明 |
|---|---|
| `[row]` | 返回 `<Path>` 指定 DataList 中指定行的值；也可为该行单元格赋新值。 |
| `append` | 将指定条目追加到 DataList 末尾。 |
| `appendList` | 将指定列表所有单元格的内容追加到 DataList 末尾，现有单元格内容保持不变。 |
| `createNestedList` | 在 DataList 中创建包含列表和表格的嵌套列表。 |
| `determineRange` | 解析 DataList 的实际列表范围，并把边界赋给指定的局部变量。 |
| `remove` | 移除指定单元格的内容并返回该值，其后单元格上移一位。 |

> 注：在 SimTalk 2.0 中，用 `[row]` 读取 DataList 单元格时保留内容，赋值时直接覆盖；在 SimTalk 1.0 中，读取会移除该单元格内容（其余单元格上移），赋值会插入新单元格（现有单元格下移）。

## 只读属性（read-only attributes）

DataList 提供：

- 列表与表格（Lists and Tables）的只读属性。
- 所有对象（All Objects）的只读属性。

只读属性只能**查询**，不能**设置**。其值由 Plant Simulation 在查询的时刻实时计算得出。在大多数情况下，只读属性对应于对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。

查询只读属性示例：

```simtalk
print MyDataList.Full
```

## 参见

- Properties of the DataQueue
- Properties of Lists and Tables
- Work with Data in a List or Table (Step-by-Step Help)
- Access Data in Lists (Step-by-Step Help)
- Accessing a Range of Cells with a Method
- The Methods of Lists and Tables
- The Methods of All Objects
