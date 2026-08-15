# Dialog（对话框对象）— Attributes 摘要

本目录下的 `attributes.md` 是 **Dialog** 对象（用户界面对象）的属性（Attributes）参考文档正文，`attributes.txtx` 为其原始提取源（内容与 `attributes.md` 基本一致，含页眉页脚与图片说明）。本文件是对 `attributes.md` 的结构化总结，便于快速查阅。

> 说明：本目录（`attributes/`）内除 `attributes.md` 与 `attributes.txtx` 外无子文件夹，因此无子文件夹 README.md 需要合并。

---

## 1. 概述

**Dialog** 对象提供：

- 本目录 `attributes.md` 中列出的属性（见下方「属性一览」）。
- 所有对象的通用属性（**Attributes of All Objects**）。

要查看对象的全部方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）右键菜单中选择 **Show Attributes and Methods**，显示所选**类**的方法、只读属性与属性。
- 在插入实例的 Frame 中按 `F8`，或点击 Home 功能区上的 **Show Attributes and Methods**，显示所选**实例**的方法、只读属性与属性。

---

## 2. 读取与设置属性

属性的值既可以通过对话框中的复选框、文本框和下拉列表设置，也可以通过为相应属性赋值来设置与获取。

- 查询只读属性的示例：

```simtalk
print MyDialog.UUID
```

- 设置属性的示例：

```simtalk
MyDialog.Locked := true
MyDialog.openDialog // 显示效果
```

- 获取属性的示例：

```simtalk
print MyDialog.ArgumentForApply
posit := Station.Cont.XPos
```

---

## 3. 属性一览

| 属性 | 数据类型 | 语法 | 说明 |
|---|---|---|---|
| `ArgumentForApply` | string | `<Path>.ArgumentForApply:string` | 用户点击 **Apply** 或 **OK** 时传给回调方法的 Apply 参数 |
| `ArgumentForClose` | string | `<Path>.ArgumentForClose:string` | 用户点击 **Cancel** 或标题栏关闭按钮时传给回调方法的 Close 参数 |
| `ArgumentForOpen` | string | `<Path>.ArgumentForOpen:string` | 打开对话框时传给回调方法的 Open 参数 |
| `CallbackMethod` | object | `<Path>.CallbackMethod:object` | 对话框条目所触发的方法的路径 |
| `DialogX` | integer | `<Path>.DialogX:integer` | 对话框在 x 轴上的显示位置（像素） |
| `DialogY` | integer | `<Path>.DialogY:integer` | 对话框在 y 轴上的显示位置（像素） |
| `Locked` | boolean | `<Path>.Locked:boolean` | 双击图标时锁定对话框布局（`true`）或打开对话框以修改布局（`false`） |
| `OpenModal` | boolean | `<Path>.OpenModal:boolean` | 对话框模态打开（`true`）或非模态打开（`false`） |
| `ShowStandardButtons` | boolean | `<Path>.ShowStandardButtons:boolean` | 显示（`true`）或隐藏（`false`）**OK**、**Cancel**、**Apply** 标准按钮 |

---

## 4. 属性详解

### 4.1 ArgumentForApply [SimTalk]

设计用户在 `<Path>` 指定的 Dialog 对话框中点击 **Apply** 或 **OK** 时传给回调方法（Callback Method）的 **Apply 参数**。

- **类型**：Attribute
- **语法**：`<Path>.ArgumentForApply:string`
- **赋值**：可赋值 `string` 类型的数据。

**备注**

- 若用户点击 **OK**，Dialog 会执行回调方法两次：第一次调用 Apply 段，第二次调用 Close 段。
- 若用户点击 **Apply**，Dialog 只执行回调方法的 Apply 段。

**示例**

```simtalk
MyDialog.ArgumentForApply := "Apply"
```

**参见**：Argument for Apply [文本框]、Callback Method [文本框] - Dialog

---

### 4.2 ArgumentForClose [SimTalk]

设计用户在 `<Path>` 指定的 Dialog 对话框中点击 **Cancel** 或标题栏关闭按钮时传给回调方法的 **Close 参数**。

- **类型**：Attribute
- **语法**：`<Path>.ArgumentForClose:string`
- **赋值**：可赋值 `string` 类型的数据。

**备注**

- 若用户点击 **OK**，Dialog 会执行回调方法两次：第一次调用 Apply 段，第二次调用 Close 段。
- 若用户点击 **Apply**，Dialog 只执行回调方法的 Apply 段。

**示例**

```simtalk
MyDialog.ArgumentForClose := "Close"
```

**参见**：Argument for Close [文本框]、Callback Method [文本框] - Dialog

---

### 4.3 ArgumentForOpen [SimTalk]

设计用户打开 `<Path>` 指定的 Dialog 时传给回调方法的 **Open 参数**。

- **类型**：Attribute
- **语法**：`<Path>.ArgumentForOpen:string`
- **赋值**：可赋值 `string` 类型的数据。

**备注**：可用于在对话框打开时预分配对话框中的数据。

**示例**

```simtalk
MyDialog.ArgumentForOpen := "Open"
```

**参见**：Argument for Open [文本框]、Callback Method [文本框] - Dialog

---

### 4.4 CallbackMethod [SimTalk] - Dialog

设置对话框条目所触发的方法的路径。

- **类型**：Attribute
- **语法**：`<Path>.CallbackMethod:object`
- **赋值**：可赋值 `object` 类型的数据。

**参数（回调方法的各段 / 回调参数）**

- **Open 段**：初始化对话框内容，或将对话框条目设置为所需的值。
- **Apply 段**：用户点击 **OK** 或 **Apply** 时执行，可对新的或更改的值求值。
- **Close 段**：用户点击 **Cancel** 或标题栏的 **Close** 关闭对话框时执行。
- 各对话框条目的 **Callback Argument** 在对应交互时执行：

| 条目 | 触发时机 |
|---|---|
| Drop-down List Box | 用户关闭下拉列表时 |
| List Box | 用户选择并双击某个列表项时 |
| Text Box | 内容改变后切换焦点（或点击其他文本框 / OK / Apply / Cancel）时 |
| Button | 用户点击按钮时 |
| Check Box | 用户选中或清除复选框时 |
| Radio Button | 用户选中单选按钮时 |
| List View | 用户选择某行并双击时 |
| Tab Control | 用户选择某个选项卡时 |
| Menu / Menu Command | 用户选择菜单或菜单命令时 |

**示例**

```simtalk
MyDialog.CallbackMethod := .Models.Model.&DialogMethod
```

**参见**：Callback Method [文本框] - Dialog、Callback Argument [文本框] - Dialog

---

### 4.5 DialogX [SimTalk]

设置 `<Path>` 指定的 Dialog 对话框在 x 轴上的显示位置。

- **类型**：Attribute
- **语法**：`<Path>.DialogX:integer`
- **赋值**：可赋值 `integer` 类型的数据。

**备注**

- 单位为像素。
- 零点为屏幕（或对话框）的左上角。
- 将 `DialogX` 或 `DialogY` 任一设为 `-1`，可将 Dialog 在屏幕上居中。

**示例**

```simtalk
MyDialog.DialogX := 350
```

**参见**：X-Position [dialog item]、DialogY [SimTalk]

---

### 4.6 DialogY [SimTalk]

设置 `<Path>` 指定的 Dialog 对话框在 y 轴上的显示位置。

- **类型**：Attribute
- **语法**：`<Path>.DialogY:integer`
- **赋值**：可赋值 `integer` 类型的数据。

**备注**

- 单位为像素。
- 零点为屏幕（或对话框）的左上角。
- 将 `DialogX` 或 `DialogY` 任一设为 `-1`，可将 Dialog 在屏幕上居中。

**示例**

```simtalk
MyDialog.DialogY := 300
```

**参见**：Y-Position [dialog item]、DialogX [SimTalk]

---

### 4.7 Locked [SimTalk]

设置用户双击 `<Path>` 指定的 Dialog 图标时打开的内容。

- **类型**：Attribute
- **语法**：`<Path>.Locked:boolean`
- **赋值**：可赋值 `boolean` 类型的数据。

- 指定 `true`：锁定 Dialog 对象的对话框，禁止用户修改对话框布局；双击时打开 Dialog。
- 指定 `false`：解锁 Dialog；双击图标时打开对话框，以便用户修改对话框布局。

**示例**

```simtalk
MyDialog.Locked := true
MyDialog.openDialog
```

---

### 4.8 OpenModal [SimTalk]

设置 `<Path>` 指定的 Dialog 对话框是否模态打开。

- **类型**：Attribute
- **语法**：`<Path>.OpenModal:boolean`
- **赋值**：可赋值 `boolean` 类型的数据。

**备注**

- **模态（Modal）**：用户必须关闭该用户自定义对话框后，才能打开其他 Plant Simulation 对话框窗口。
- **非模态（Not modal）**：对话框打开时，用户仍可打开其他 Plant Simulation 窗口。

**示例**

```simtalk
.Models.MyPlant.MyDialog.OpenModal := true
```

**参见**：Open Modal [check box]

---

### 4.9 ShowStandardButtons [SimTalk]

设置 `<Path>` 指定的 Dialog 是否显示标准按钮 **OK**、**Cancel** 和 **Apply**。

- **类型**：Attribute
- **语法**：`<Path>.ShowStandardButtons:boolean`
- **赋值**：可赋值 `boolean` 类型的数据。

- `true`：显示标准按钮；`false`：隐藏标准按钮。

**示例**

```simtalk
Dialog.ShowStandardButtons := false
```

**参见**：Show Default Buttons [check box]

---

## 5. 附注

`attributes.md` 末尾的 **Checkbox [object]** 一节为源文件页脚/相关链接的残留内容（对应其他对象的「See also」跳转），并非 Dialog 对象自身的属性，故未纳入上方的属性一览与详解。
