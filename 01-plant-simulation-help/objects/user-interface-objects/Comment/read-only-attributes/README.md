# Read-Only Attributes of the Comment

本目录汇总了 Plant Simulation 中 **Comment（注释）对象** 的只读属性（Read-Only Attributes）相关文档。

## 目录内容

- `read-only-attributes.md` —— Comment 对象的只读属性文档（主要内容）
- `read-only-attributes.txtx` —— 同内容的原始文本来源

## 内容总结

### 概述

**Comment** 对象提供 *所有对象的只读属性（Read-Only Attributes of All Objects）*。

- 只读属性可以**查询**其值，但不能**设置**，因为 Plant Simulation 会在查询的时间点即时计算该值。
- 大多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。
- 查询只读属性值的示例：

```simtalk
print MyComment.UUID
```

### `openComment` [SimTalk]

打开一个窗口，仅显示通过 `<Path>` 指定的 Comment 中输入的内容，不带任何格式选项。

- **类型（Type）：** 方法（Method）
- **语法（Syntax）：**

```simtalk
<Path>.openComment → boolean
```

- **返回值（Return Value）：** 数据类型为 `boolean`。

**示例：**

```simtalk
MyComment.openComment
```

**参见（See also）：**
- Tab Comment [Comment]
- Read-Only Attributes of the Comment

### Comment 的属性

Comment 对象提供：

- 左侧目录中列出的属性。
- 所有对象的属性（Attributes of All Objects）。

### 查看属性与方法

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类（Class）的方法、只读属性和属性 [一般说明]。
- 按下 **F8** 键，或在插入实例的 Frame 的 Home 功能区选项卡中点击 **Show Attributes and Methods**，可显示所选实例（Instance）的方法、只读属性和属性 [一般说明]。

---

*Plant Simulation Help 11-4585 / 11-4586 · Unpublished work. © 2026 Siemens*
