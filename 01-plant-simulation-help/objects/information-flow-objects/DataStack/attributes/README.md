# Attributes (DataStack)

本目录介绍了 `DataStack`（以及 `DataQueue`）对象的属性（attributes）的查看、读取与设置方法，并列出了这些对象提供的属性组。

## 目录内容

- `attributes.md` — 属性的说明页面（Markdown 格式）。
- `attributes.txtx` — 同一内容的纯文本导出版本。

## 内容总结

### 查看方法、只读属性与属性

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods**（显示属性和方法）窗口。以下两种方式可打开该窗口：

- 在 **Class Library**（类库）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **Class**（类）的方法、只读属性和属性。
- 按 **F8** 键，或在插入了实例的 **Frame** 的 **Home** 功能区选项卡中点击 **Show Attributes and Methods**，可查看所选 **Instance**（实例）的方法、只读属性和属性。

### 查询只读属性

要查询某个只读属性的值，例如可以输入：

```simtalk
print MyDataStack.Full
```

### DataQueue 与 DataStack 提供的属性

`DataStack` 和 `DataQueue` 提供：

- **列表和表格的属性（Attributes of Lists and Tables）**。
- **所有对象的属性（Attributes of All Objects）**。

### 读取与设置属性值

可以通过对话框中的复选框、文本框和下拉列表来读取和设置属性值，也可以通过给相应属性赋值的方式实现。

设置属性值示例：

```simtalk
MyDataStack.MaxDim := -1
MyDataQueue.Alignment := "left"
```

读取属性值示例：

```simtalk
print myDataStack.MaxDim
posit := Station.Cont.XPos
```

### DataQueue 与 DataStack 的区别

`DataQueue` 和 `DataStack` 都是**单列列表**，二者共享所有方法和属性，仅内置属性不同。

- **DataQueue（FIFO，先进先出）**：按插入顺序保存条目，最先移除等待时间最长的条目。
- **DataStack（LIFO，后进先出）**：新条目插入到顶部，最先移除最后添加的单元格内容。

### 将对象添加到仿真模型

在 **Home** 功能区选项卡中点击：

> Manage Class Library > Basic Objects > InformationFlow > DataQueue

要更改 DataQueue 图形的长度和锚点，请在 **Edit** 功能区选项卡中点击 **Show Manipulators** 或按键盘 **M** 键。

## 参见

- Properties of the DataQueue

---

*Plant Simulation Help 11-4243 — Unpublished work. © 2026 Siemens*
