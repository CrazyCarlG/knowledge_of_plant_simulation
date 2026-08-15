# Dialog 只读属性（Read-Only Attributes）

本目录介绍 Plant Simulation **Dialog（对话框）** 对象的只读属性、相关方法及属性。

## 内容概览

### 1. updateUserDialog [SimTalk]（方法）

用于更新由 `<Path>` 指定的 Dialog 的内容。

- **作用**：当你在定义条目的表格中做了修改，或者条目的图片/图标发生变化时，Dialog 会显示这些新的或变更后的内容。
- **类型**：方法（Method）
- **语法**：`<Path>.updateUserDialog`
- **示例**：`MyDialog.updateUserDialog`

### 2. Dialog 的只读属性

Dialog 提供 **所有对象的只读属性（Read-Only Attributes of All Objects）**。

- 只读属性的值**可以查询，但不能设置**——Plant Simulation 在你查询的那一刻自动计算其值。
- 大多数情况下，只读属性对应对象某个选项卡上不可编辑的对话框条目（例如 **Statistics** 选项卡）。

### 3. Dialog 的属性

Dialog 提供：

- 左侧目录（table of contents）中列出的属性。
- **所有对象的属性（Attributes of All Objects）**。

## 查看方法、只读属性与属性

要查看对象的全部方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的右键菜单中选择 **Show Attributes and Methods**，可查看所选**类**的方法、只读属性和属性。
- 按下 **F8** 键，或点击 Frame 的 Home 选项卡中的 **Show Attributes and Methods**，可查看插入实例的**实例**的方法、只读属性和属性。

## 查询示例

查询只读属性的值，例如：

```
print MyDialog.UUID
```

---

*来源：Plant Simulation Help 11-5149 / 11-5150*
