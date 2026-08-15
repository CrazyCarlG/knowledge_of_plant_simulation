# Accessing a Range of Cells with a Method

本目录介绍如何在 Plant Simulation 的列表（List）和表格（Table）对象中，用方法（Method）访问**连续的单元格范围**，而不仅是单个单元格。

> 来源：`accessing-range-of-cells.md`（结构化帮助文档）及其文本导出 `accessing-range-of-cells.txtx`。

## 概述

许多 SimTalk 方法（如 `min`、`max`）只能作用于一个单元格范围，因此访问范围需要使用特殊语法。Plant Simulation 将范围访问分为两类：

- 单列列表中的单元格范围（Cell Ranges in Lists with One Column）
- 多列表格中的单元格范围（Cell Ranges in Tables with Several Columns）

## 单列列表中的范围（DataStack / DataQueue / DataList）

访问单列列表的单元格范围时，语法为：

```
{第一个单元格编号}..{最后一个单元格编号}
```

- 左花括号 `{` 表示范围的开始，其后跟单元格索引编号，右花括号 `}` 结束。
- 单元格标识符可以是**大于 0 的数字**、**用户自定义索引**，或**星号 `*`（表示所有单元格）**。
- 若不知道最后一个单元格的标识符，用 `{*}` 表示"最后一个单元格"。

| 示例 | 含义 |
| --- | --- |
| `{1}` | 第一个单元格 |
| `{*}` | 所有单元格 |
| `{2}..{4}` | 第 2 到第 4 个单元格 |
| `{3}..{*}` | 从第 3 个单元格到最后一个单元格 |

## 多列表格中的范围（DataTable）

访问表格中的单元格时，用**列标识符和行标识符，以逗号分隔**：

```
{列, 行}
```

列和行的标识符同样可以是大于 0 的数字、用户自定义索引或星号 `*`（表示整个表格）。

| 示例 | 含义 |
| --- | --- |
| `{1,3}` | 第 1 列、第 3 行的单元格 |
| `{1,*}` | 第 1 列的所有行 |
| `{*,3}` | 第 3 行的所有列 |
| `{*,*}` | 整个表格 |
| `{"vehicle","door"}` | 列索引为 `vehicle`、行索引为 `door` 的单元格 |

### 访问范围（from-to 语句）

范围由位于两个列中的两个单元格组成，中间用两个句点 `..` 分隔：

- 第一个标识符指定**左上角**单元格（列号、行号）；
- 第二个指定**右下角**单元格（列号、行号）；
- 若第二个标识符为 `{*,*}`，Plant Simulation 会处理到**最高有效的列索引和行索引**。

| 示例 | 含义 |
| --- | --- |
| `{1,2}..{3,5}` | 从第 1 列第 2 行到第 3 列第 5 行的单元格 |
| `{1,*}..{4,*}` | 第 1 到第 4 列的所有行 |
| `{2,3}..{*,3}` | 第 3 行中从第 2 列开始的所有列 |
| `{2,3}..{*,*}` | 从第 2 列第 3 行到最高有效单元格 |
| `{*,*}..{3,5}` | 到第 3 列、第 5 行之前的所有列与所有行 |
| `{"ColumnB", 0}..{"ColumnB",*}` | `ColumnB` 的列索引及该列所有行 |

如果范围由两个索引规范组成，Plant Simulation 会将其解释为矩形范围的两个对角点（如同用鼠标选择范围）。

## 用户自定义索引（User-defined Index）

当用户自定义索引的数据类型为 `integer` 时，需要在标识符前加上井号 `#`。因为系统索引（Plant Simulation 分配的行号、列号）也是 `integer` 类型，不加 `#` 将无法区分使用的是系统索引还是用户自定义索引。

| 示例 | 含义 |
| --- | --- |
| `[2]` / `{2,5}` | 系统索引 |
| `[#2]` / `{#2,#7}` | 用户自定义索引 |

> 表示范围语句时必须使用花括号 `{ }`。

## Column Index Belongs to Contents 的影响

范围访问的效果取决于 **"Column Index Belongs to Contents"（列索引属于内容）** 是否被激活。

- **激活时**：`DataTableColumnIndexContents.delete({"ColumnB", *})` 会删除 `ColumnB` 的整个内容，**包括列索引**。
- **未激活时**：`DataTableColumnIndexNotContents.delete({"ColumnB", *})` 只删除 `ColumnB` 的内容，**不包括列索引**。

若要删除包括列索引在内的整个内容（未激活时），使用：

```simtalk
DataTableColumnIndexNotContents.delete({"ColumnB", 0}..{"ColumnB", *})
```

## 相关 SimTalk 方法

`calculateList`、`copyRangeTo`、`delete`（列表）、`determineRange`（DataTable）、`find`（列表）、`findAttr`、`findCeil`、`findFloor`、`initialize`、`max`（列表）、`maxAttr`、`meanValue`、`meanValueAttr`、`min`（列表）、`minAttr`、`setAlignmentCells`、`setEditorRightsCells`、`setFormula`、`standardDeviation`、`standardDeviationAttr`、`sum`（列表）、`sumAttr`。

## 另请参见

- Activate Column Index
- Activate Row Index
- Create a User-defined Column and Row Index
- Specify the Identifier of a Cell
- Specifying a Range of Cells
- Address a User-defined Index
