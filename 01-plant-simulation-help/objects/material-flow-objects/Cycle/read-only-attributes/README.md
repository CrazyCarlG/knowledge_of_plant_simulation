# Read-Only Attributes of the Cycle（Cycle 对象的只读属性）

本目录汇总了物料流对象 **Cycle（循环/同步）** 的只读属性文档。

## 概述

Cycle 对象提供以下只读属性相关文档：

- 本目录左侧目录中列出的只读属性（`GetFirstStation`、`GetLastStation`）。
- _所有对象通用的只读属性（_Read-Only Attributes of All Objects）。
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）。

只读属性的值**只能查询，不能设置**：Plant Simulation 会在你查询的时间点实时计算其值。在大多数情况下，某个只读属性对应对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。

## 如何查看只读属性

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类的方法、只读属性和属性。
- 按 **F8** 键，或点击插入了实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选实例的方法、只读属性和属性。

查询只读属性值的示例：

```simtalk
print Cycle.GetFirstStation
```

## 只读属性列表

### GetFirstStation [SimTalk]

返回 Cycle（由 `<Path>` 指定）所同步的平衡生产线（balanced line）的第一个工位（station）。

- **类型：** 只读属性（Read-only attribute）
- **语法：**

```simtalk
<Path>.GetFirstStation -> object
```

- **返回值：** 数据类型为 `object`。
- **示例：**

```simtalk
print MyCycleObject.GetFirstStation
```

- **参见：** First Station

### GetLastStation [SimTalk]

返回 Cycle（由 `<Path>` 指定）所同步的平衡生产线的最后一个工位（station）。

- **类型：** 只读属性（Read-only attribute）
- **语法：**

```simtalk
<Path>.GetLastStation -> object
```

- **返回值：** 数据类型为 `object`。
- **示例：**

```simtalk
print MyCycleObject.GetLastStation
```

- **参见：** Last Station

## 本目录文件说明

| 文件 | 说明 |
| --- | --- |
| `read-only-attributes.md` | Cycle 只读属性的 Markdown 文档（GetFirstStation、GetLastStation）。 |
| `read-only-attributes.txtx` | 从 Plant Simulation Help 导出的原文文本，内容与 md 版一致，并附带页码（11-2641 至 11-2643）及相邻章节（如 Attributes of the Object Cycle）的片段。 |

## 来源

Plant Simulation Help 11-2641 — 11-2643，© 2026 Siemens，未发表作品（Unpublished work）。
