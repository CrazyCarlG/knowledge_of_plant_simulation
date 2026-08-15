# DataQueue / DataStack 属性（Attributes）

本目录收录 **DataQueue** 与 **DataStack** 对象的属性说明文档。

## 目录内容

- `attributes.md` — DataQueue / DataStack 属性的 Markdown 说明文档
- `attributes.txtx` — 与 `attributes.md` 内容一致的文本版本

## 内容摘要

### 查看属性与方法

- 在 **Class Library（类库）** 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 在插入实例的 Frame 中，按 **F8** 键或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。

### 提供的属性

DataStack 与 DataQueue 提供以下属性：

- **Lists（列表）** 与 **Tables（表格）** 的属性
- **All Objects（所有对象）** 的属性

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口。

### 设置与获取属性值

既可以通过对话框窗口中的复选框、文本框和下拉列表，也可以通过为相应属性赋值来设置和获取属性值。

- **设置属性值**（示例）：

  ```simtalk
  MyDataStack.MaxDim := -1
  MyDataQueue.Alignment := "left"
  ```

- **获取属性值**（示例）：

  ```simtalk
  print myDataStack.MaxDim
  posit := Station.Cont.XPos
  ```

- **查询只读属性值**（示例）：

  ```simtalk
  print MyDataStack.Full
  ```

### TimeSequence 对象

**TimeSequence** 用于记录数值随时间变化的历程，例如排班计划、机器维护计划或缓冲区占用情况。

- **结构**：TimeSequence 是一个两列表格。
- **Watch 模式**：每当可监视的数值发生变化时，Plant Simulation 记录时间-数值对。
- **Sample 模式**：在特定时间间隔内周期性地记录时间-数值对，无论数值是否实际发生变化。

TimeSequence 可多次使用，并对数值进行排序，以判断这些数值随时间是否保持恒定或随机变化。

---

*Plant Simulation Help 11-4257 · Unpublished work. © 2026 Siemens*
