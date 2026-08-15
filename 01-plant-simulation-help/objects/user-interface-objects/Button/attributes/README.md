# Attributes of the Button（Button 属性）

本目录汇总了 **Button（按钮）** 用户界面对象的**属性**文档。内容来源为同目录下的 `attributes.md`（以及 `attributes.txtx` 原始文本），并合并了 `Button` 其余子文件夹（`general`、`methods`、`read-only-attributes`）中 `README.md` 的要点。

> 说明：`attributes` 目录下没有子文件夹，因此不存在本目录子文件夹内的 `README.md`。本 README 基于 `attributes.md` 的内容总结，并整合了同级目录的 README 摘要。

## 目录内容

- `attributes.md` — Markdown 版本文档（本目录唯一的主文档）。
- `attributes.txtx` — 纯文本导出版本（内容与 `attributes.md` 基本一致）。

---

## 概述

**Button（按钮）** 用于在 Frame 中显示一个按钮，当用户点击它时，会执行你在 Control 中编写的动作。

Button 提供：

- 左侧目录中列出的属性（本目录文档所描述的属性）。
- 所有对象的属性（*Attributes of All Objects*）。

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods（显示属性和方法）** 窗口：

- 在 Class Library（类库）的上下文菜单中选择 **Show Attributes and Methods**，可显示所选**类（Class）** 的方法、只读属性和属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 **Home** 功能区选项卡上的 **Show Attributes and Methods**，可显示所选**实例（Instance）** 的方法、只读属性和属性。

属性既可以**设置**（set），也可以**读取**（get）：可通过对话框窗口中的复选框、文本框和下拉列表来设置，或通过给相应属性赋值来实现。

### 示例

查询只读属性值：

```simtalk
print MyButton.UUID
```

设置属性值：

```simtalk
MyButton.UseIcon := false
```

读取属性值：

```simtalk
print MyButton.UseIcon
posit := Station.Cont.XPos
```

---

## Button 的属性

### Control [SimTalk] — Button

设置由 `<Path>` 指定的 Button 在**点击时执行的 Control**。

- **类型：** Attribute（属性）
- **语法：** `<Path>.Control:string`
- **赋值类型：** 可赋数据类型为 `string` 的值。
- **备注：**
  - 调用方法时，匿名标识符 `?` 和 `@` 被设置为该 Button。
  - 也可输入一个**接收布尔值参数**的 Control：点击按钮时以 `true` 调用，释放按钮时以 `false` 调用。
  - 当更改按钮大小或拖放（Drag-and-Drop）移动按钮时，也会调用该 Control；若 Control 不接收参数，则仍像之前一样在释放按钮时调用。

**示例：**

```simtalk
MyButton.Control := "myControl"
self.~.~.&MyMethod.openDialog
```

### ObjectHeight [SimTalk] — Button

设置由 `<Path>` 指定的 Button 在 Frame 中显示的**高度**。

- **类型：** Attribute（属性）
- **语法：** `<Path>.ObjectHeight:integer`
- **赋值类型：** 可赋数据类型为 `integer` 的值。
- **备注：** 当对象高度超过 30 像素时，按钮会以更大的字号显示标签文字。

**示例：**

```simtalk
MyButton.ObjectHeight := 1 // meter
```

**相关：** Height [text box] — Button

### ObjectWidth [SimTalk] — Button

设置由 `<Path>` 指定的 Button 在 Frame 中显示的**宽度**。

- **类型：** Attribute（属性）
- **语法：** `<Path>.ObjectWidth:integer`
- **赋值类型：** 可赋数据类型为 `integer` 的值。
- **备注：** 如果输入较长的标签，需要调整宽度，使标签完整显示在按钮上而不会被裁切。

**示例：**

```simtalk
MyButton.ObjectWidth := 4 // meters
```

**相关：** Width [text box] — Button

### DropDownList [object]（交叉引用）

> 该条目为 `attributes.md` 末尾的交叉引用主题，实际描述的是**下拉列表对象**（DropDownList），而非 Button 的属性。

使用 DropDownList 对象可在 Frame 中显示一个下拉列表。当你选中其中一个项目时，它会执行你在 Control 中编写的动作。

---

## 同级目录 README 要点

### general（通用说明）

- Button 在 Frame 中显示按钮，点击时执行 Control 中编写的动作。
- 输入标签后，Plant Simulation 会在按钮上显示该标签。
- 默认不显示按钮名称的提示（tooltip）；要显示自定义提示，可创建名为 `Tooltip` 的用户自定义属性。
- 显示方式：显示标签文字、显示图标编辑器中绘制的图标（可在其上叠加文字）、显示粘贴为图标的图片（如 `play`、`play_down`）。
- 添加到模型：**Home > Manage Class Library > Basic Objects > UserInterface > Button**。
- **Tab Attributes** 中的对应项：
  - **Width [文本框]** ↔ `ObjectWidth [SimTalk]`
  - **Height [文本框]** ↔ `ObjectHeight [SimTalk]`
  - **Control [按钮]** ↔ `Control [SimTalk]`
- 也可指定接收布尔值参数的 Control（点击时 `true`、释放时 `false`）。
- Button 提供 *Methods of All Objects*（所有对象的方法）。

### methods（方法）

- Button 提供 **Methods of All Objects**（所有对象的方法），没有 Button 独有的方法。
- 方法的语法行示例：`<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`
  - `<Path>`：方法所作用对象的路径。
  - `(Parameter:string)`：方法签名，参数以标识符和数据类型列出。
  - 可选参数写在方括号内，例如 `[,Parameter:boolean]`。
  - 默认值显示在参数后，例如 `:= false`。
  - 返回类型显示在箭头 `→` 后，例如 `→ boolean`。
- **注意：** 括号内的表达式必须输入括号 `(…)`，否则可能产生意外结果并打开调试器（Debugger）。

### read-only-attributes（只读属性）

- Button 提供 **_Read-Only Attributes of All Objects**（所有对象的只读属性）。
- 只读属性只能查询（query），不能设置（set）；Plant Simulation 在查询的时间点计算其值。
- 多数情况下，只读属性对应对象某个选项卡上不可用的对话框项（例如 **Statistics** 选项卡）。
- 查询只读属性示例：`print MyButton.UUID`

---

## 方法与属性符号约定

- `<Path>`：方法所作用对象的路径。
- 方法签名由标识符和参数数据类型组成，写在括号内，例如 `(Parameter:string)`。
- 括号内的表达式必须输入括号 `(…)`，否则可能导致意外结果并打开调试器。
- 可选参数写在方括号内，例如 `[,Parameter:boolean]`。
- 参数默认值显示在参数后，例如 `:= false`。
- 返回值类型显示在箭头 `→` 后，例如 `→ boolean`。

---

*来源：Plant Simulation Help 11-5194–11-5198。未发表作品。© 2026 Siemens。*
