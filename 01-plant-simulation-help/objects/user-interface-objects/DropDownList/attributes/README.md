# DropDownList 属性（Attributes）— 总结

> 本目录 `attributes/` 包含 DropDownList（下拉列表）对象「属性」相关的文档。主要来源为 `attributes.md`（同内容源文本见 `attributes.txtx`）。本文件是对 `attributes.md` 以及 DropDownList 各子文件夹（`general/`、`methods/`、`read-only-attributes/`）中 `README.md` 内容的综合总结。

## 概述

DropDownList 对象用于在 Frame 中显示一个下拉列表；当用户选择其中某一项时，它会执行 `Control` 中编写的动作。

DropDownList 提供：

- 本目录目录中列出的**属性（Attributes）**。
- **所有对象的属性（Attributes of All Objects）**。

属性既可以**读取（get）**也可以**设置（set）**，方式有两种：

- 通过对话框中的复选框、文本框和下拉列表进行设置；
- 通过给相应属性赋值（SimTalk 语句）进行设置。

### 查看属性与方法（Show Attributes and Methods）

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在**类库（Class Library）**中，右键选中某个 **Class**，在上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 在已插入实例的 **Frame** 中，按 **F8** 键，或点击 **Home** 功能区选项卡上的 **Show Attributes and Methods**，可查看所选**实例（Instance）**的方法、只读属性和属性。

### 读取与设置示例

设置属性值：

```simtalk
MyDropdownList.UseIcon := false
```

读取属性值：

```simtalk
print MyDropdownList.UseIcon
```

查询只读属性值：

```simtalk
print MyDropDownList.UUID
```

---

## DropDownList 的属性列表

| 属性 | 数据类型 | 说明 |
| --- | --- | --- |
| `Control` | `string` | 设置在 Frame 中选择某一项时要执行的控制（Control）方法 |
| `Item` | `string` | 通过**名称**设置当前选中的项 |
| `Items` | `array` | 设置或读取下拉列表显示的选项（数组） |
| `ObjectHeight` | `integer` | 设置 DropDownList 在 Frame 中显示的高度（单位：米） |
| `ObjectWidth` | `integer` | 设置 DropDownList 在 Frame 中显示的宽度（单位：米） |
| `Value` | `integer` | 通过**索引号**设置当前选中的项 |

### Control [SimTalk] - DropDownList

设置 DropDownList（由 `<Path>` 指定）在 Frame 中选中某一项时要执行的控制（Control）方法。

- **语法：** `<Path>.Control:string`
- **赋值类型：** `string`
- **备注：** 方法被调用时，匿名标识符 `?` 和 `@` 会被设置为该 DropDownList。
- **示例：**

```simtalk
MyDropdownList.Control := "myControl"
```

```simtalk
switch ?.Value
case 1
   print "Item 1 selected"
case 2
   print "Item 2 selected"
end
```

### Item [SimTalk] - DropDownList

通过**名称**设置 DropDownList（由 `<Path>` 指定）中将被选中的项。

- **语法：** `<Path>.Item:string`
- **赋值类型：** `string`
- **备注：** 如果对选项做了本地化，通常应使用 `Value` 而不是 `Item`。`Value` 是数字，与语言无关；而 `Item` 是字符串，会因语言而异。
- **示例：**

```simtalk
MyDropdownList.Item := "My item text 1"
```

### Items [SimTalk] - DropDownList

设置或读取 DropDownList（由 `<Path>` 指定）所显示的选项。

- **语法：** `<Path>.Items:array`
- **赋值类型：** `array`
- **备注：**
  - 若要通过索引号访问列表项，请使用属性 `Value`。
  - 若要通过名称访问列表项，请使用属性 `Item`。
- **示例：**

```simtalk
var a : string[] := ["Item 1", "Item 2", "Item 1"]
MyDropdownList.Items := a
```

### ObjectHeight [SimTalk] - DropDownList

设置 DropDownList（由 `<Path>` 指定）在 Frame 中显示的高度。

- **语法：** `<Path>.ObjectHeight:integer`
- **赋值类型：** `integer`
- **示例：**

```simtalk
MyDropDownList.ObjectHeight := 1 // meter
```

### ObjectWidth [SimTalk] - DropDownList

设置 DropDownList（由 `<Path>` 指定）在 Frame 中显示的宽度。

- **语法：** `<Path>.ObjectWidth:integer`
- **赋值类型：** `integer`
- **备注：** 若为 Items 输入了较长的标识符，则必须调整宽度，以免文本被截断。
- **示例：**

```simtalk
MyDropDownList.ObjectWidth := 4 // meters
```

### Value [SimTalk] - DropDownList

设置 DropDownList（由 `<Path>` 指定）中将被选中的项，Plant Simulation 使用该项的**索引号**进行标识。

- **语法：** `<Path>.Value:integer`
- **赋值类型：** `integer`
- **备注：** 若将选项本地化为其他语言，通常应使用 `Value` 而不是 `Item`。`Value` 是数字，与语言无关；而 `Item` 是字符串，会因语言而异。
- **示例：**

```simtalk
MyDropdownList.Value := 3
```

---

## 来自子文件夹 README 的补充内容

### `general/` — DropDownList 对象总体说明

- 可通过 DropDownList 的对话框，或通过属性 `Items` 来定义下拉列表显示的选项。
- 每当用户选择另一项时，下拉列表会执行 `Control` 中编写的动作。
- 右键点击下拉列表并选择 **Open** 可打开其对话框；也可通过拖拽框选框（marquee）套住其图标来选中它。
- 在 **Edit** 功能区选项卡中点击 **Show Manipulators** 或按 `M` 键，可更改图形长度和锚点。
- 添加对象路径：**Home > Manage Class Library > Basic Objects > UserInterface > DropDownList**。
- **Attributes 选项卡**中的相关对话框项：
  - **Width**：输入显示宽度（单位：米），对应 SimTalk 属性 `ObjectWidth`。
  - **Height**：输入显示高度（单位：米），对应 SimTalk 属性 `ObjectHeight`。
  - **Value**：输入打开时将选中的项（用索引号标识），对应 SimTalk 属性 `Value`。
  - **Items**：打开列表以输入显示的选项，对应 SimTalk 属性 `Items` / `Item`。
  - **Control**：修改对象内置行为，对应 SimTalk 属性 `Control`。

### `methods/` — 方法相关说明

- DropDownList 提供**所有对象的方法（Methods of All Objects）**以及**所有对象的只读属性（Read-Only Attributes of All Objects）**。
- 方法语法行示例：`<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`。
- 语法符号含义：`<Path>` 表示对象路径；`(…)` 内为参数签名；`[…]` 内为可选参数；`:=` 后为默认值；`→` 后为返回值类型。

### `read-only-attributes/` — 只读属性说明

- DropDownList 提供**所有对象的只读属性（Read-Only Attributes of All Objects）**。
- 只读属性的值可以**查询（query）**，但**不能设置（set）**；其值由 Plant Simulation 在查询时刻动态计算得出。
- 多数情况下，只读属性对应对象某个选项卡（如 **Statistics** 选项卡）上不可用的对话框项。

---

## 相关属性/方法速查

- SimTalk 属性：`ObjectWidth`、`ObjectHeight`、`Value`、`Items`、`Item`、`Control`
- SimTalk 方法（参考）：`updateDialog`、`openDialog`

## 另请参阅

- Attributes of All Objects
- Methods of All Objects
- Read-Only Attributes of All Objects
