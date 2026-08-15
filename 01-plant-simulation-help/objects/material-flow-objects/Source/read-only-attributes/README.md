# Read-Only Attributes of the Source（Source 对象的只读属性）

本目录包含 Source（源）对象只读属性的相关文档，来源为 Siemens Plant Simulation Help。

## 目录内容

- `read-only-attributes.md` — Source 对象只读属性的 Markdown 说明文档
- `read-only-attributes.txtx` — 相同内容的文本导出版本
- `Plant-Simulation-Help2606_4546-4547.pdf` — 原始帮助文档 PDF

> 本目录下无子文件夹。

## 内容概述

### 总览（Overview）

Source 对象提供以下只读属性：

- 所有对象的只读属性（Read-Only Attributes of All Objects）
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）

**只读属性的特点：**

- 可以查询（query）只读属性的值，但不能设置（set）它们。
- Plant Simulation 会在查询的那一刻计算对应值。
- 多数只读属性对应对象某个选项卡上不可编辑的对话框项，例如 **Statistics（统计）** 选项卡。

**查看对象的所有方法、只读属性和属性的方式：**

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类（Class）的方法、只读属性与属性。
- 按 **F8** 键，或点击已插入实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例（Instance）的方法、只读属性与属性。

**查询只读属性的示例：**

```simtalk
print MySource.UUID
```

### 只读属性列表

#### CurrentBatchNumber [SimTalk]

返回最近创建的部件（part）的批次号。

- 若属性 `GenerateAsBatch` 已激活（`true`）：返回最近创建部件的批次号。
- 若 `GenerateAsBatch` 未激活（`false`）：返回已创建部件的数量。

**类型（Type）：** 只读属性（Read-only attribute）

**语法（Syntax）：**

```simtalk
<Path>.CurrentBatchNumber -> integer
```

**返回值（Return Value）：** 数据类型为 `integer`。

**示例（Example）：**

```simtalk
print MySource.CurrentBatchNumber
```

**另见（See also）：**

- Generate as Batch（复选框）
- GenerateAsBatch [SimTalk]
- Attributes of the Source
- _Attributes of the Source

### Attributes of the Source

Source 对象提供：

- 目录（table of contents）中列出的属性
- 所有对象的属性（Attributes of All Objects）
- 物料流对象的属性（Attributes of the Material Flow Objects）
