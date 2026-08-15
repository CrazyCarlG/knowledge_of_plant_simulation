# Track（轨道）— 只读属性（Read-Only Attributes）汇总说明

本目录 `read-only-attributes` 汇总了 Track（轨道）物料流对象的只读属性参考文档。Track 是 Plant Simulation 中的一种长度导向（length-oriented）物料流对象，与 Transporter（运输小车）配合使用，用于建模 AGV（自动导引车）系统。

本文件是本目录下 `read-only-attributes.md` 的内容总结。该目录下无子文件夹。

---

## 1. 只读属性总览

Track 提供以下只读属性，并继承 All Objects（所有对象）与 Material Flow Objects（物料流对象）的只读属性：

| 只读属性 | 说明 |
| --- | --- |
| **OccupiedLength** | 返回 Track 的总 Length 中被其上所有 Transporter 占用的部分。 |

只读属性只能查询、不能设置，因为 Plant Simulation 在查询时计算其值。大多数情况下，只读属性对应对象某个选项卡（例如 Statistics）上不可用的对话框项。

可通过窗口 **Show Attributes and Methods** 查看对象的所有方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **Class** 的方法、只读属性和属性。
- 按 **F8** 键，或在插入实例的 Frame 的 Home 功能区选项卡上点击 **Show Attributes and Methods**，可查看所选 **Instance** 的方法、只读属性和属性。

查询只读属性值示例：

```simtalk
print Store.Capacity
```

---

## 2. OccupiedLength [SimTalk] - Track

返回 `<Path>` 指定的 Track 的总 `Length` 中，被其上所有 Transporter 占用的部分。

### 备注

- 每个位于 Track 上的 Transporter 都会占用部分可用总长度。

### 类型

只读属性（Read-only attribute）

### 语法

```
<Path>.OccupiedLength → length
```

### 返回值

- 数据类型为 `length`。

### 示例

```simtalk
print MyTrack.OccupiedLength
```

### 相关参考

- Length [text box] - Track
- Attributes of the Track

---

## 3. 相关参考

- 属性参考：`attributes/attributes.md`（含 `Length`、`Width`、`Capacity`、`FwDestList`、`BwDestList` 等属性）。
- 方法参考：`methods/methods.md`（含 `getRouteLength` 方法）。
- 对象概述：`general/general.md`。

---

*Source: Plant Simulation Help 11-2463 — 11-2465. Unpublished work. © 2026 Siemens.*
