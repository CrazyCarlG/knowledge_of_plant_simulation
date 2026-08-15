# Read-Only Attributes of the SankeyDiagram

本目录汇总了 SankeyDiagram 对象的**只读属性（Read-Only Attributes）**相关内容。

## 目录内容

- `read-only-attributes.md` — 只读属性与 `update` 方法的 Markdown 说明文档。
- `read-only-attributes.txtx` — 同一主题的文本提取版本（Plant Simulation Help 导出内容）。

## 内容摘要

### 概述

SankeyDiagram 提供**所有对象的只读属性**。可以查询这些只读属性的值，但不能设置它们，因为 Plant Simulation 会在查询的**时间点**计算该值。

在大多数情况下，一个只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

### 查看属性与方法

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，以显示所选类的方法、只读属性和属性（一般说明）。
- 按 **F8** 键，或在插入实例的 Frame 的 Home 功能区选项卡上点击 **Show Attributes and Methods**，以显示所选实例的方法、只读属性和属性（一般说明）。

### 查询只读属性的示例

例如，可以输入以下语句查询只读属性的值：

```simtalk
print MySankeyDiagram.UUID
```

### `update` [SimTalk] 方法

刷新由 `<Path>` 指定的 SankeyDiagram 显示，使其反映当前值。

| 属性 | 值       |
|------|----------|
| Type | Method   |

**语法**

```simtalk
<Path>.update
```

**示例**

```simtalk
MySankeyDiagram.update
```

**参见**

- Update [in Frame]

### SankeyDiagram 的属性

SankeyDiagram 提供：

- 左侧目录中列出的属性。
- 所有对象的属性（Attributes of All Objects）。

可以通过对话框窗口中的复选框、文本框和下拉列表，或通过给相应属性赋值，来获取和设置属性的值。

---

*Plant Simulation Help — Unpublished work. © 2026 Siemens*
