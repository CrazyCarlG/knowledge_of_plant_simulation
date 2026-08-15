# Type Conversion Basics — README

本目录包含 SimTalk 数据类型转换基础知识的文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `type-conversion-basics.md` | 数据类型转换（Converting Data Types）的正式文档 |
| `type-conversion-basics.txtx` | 同内容的纯文本版本 |

## 内容总结

该文档介绍 Plant Simulation 中不同数据类型之间的转换规则。核心要点如下：

### 自动类型转换

- Plant Simulation 会自动转换数值类型，其他类型转换需显式进行。
- `integer` 与 `real` 之间会自动相互转换。
- 将 `real` 值赋给 `integer` 变量时，小数部分会被截断（类似 Excel 的 TRUNC 函数）。
- 参数传递时，`real` 与 `integer` 之间也会自动转换。
- `dateTime` 与 `date` 之间同样自动转换，转换时时间部分会被删除。

### 物理数据类型的转换

- 计算时，物理数据类型 `length`、`weight`、`speed`、`acceleration`、`time` 的单位被视为实数处理。
- 若计算结果属于另一物理数据类型，结果会被赋予相应的数据类型（如 `length` 除以 `time` 得到 `speed`）。
- 若结果无法对应物理数据类型，则使用 `real`。

### 物理数据类型的赋值限制

- 只能将具有正确单位的值，或无单位的 `real`/`integer` 值赋给物理数据类型（`length`、`weight`、`speed`、`acceleration`、`time`）的局部变量。
- 其他情况下的赋值会抛出错误以提示潜在问题。

### 舍入解决方案

自动转换从 `real` 到 `integer` 时小数会被截断，文档提供了两种处理方法：

1. 使用 `round` 函数：

```simtalk
var realVal := pi
var intVal : integer := round(realVal)
```

2. 加上 `0.5`：

```simtalk
var realVal := pi
var intVal : integer := realVal + 0.5
```

---

*Source: 12-206 Plant Simulation Help — Unpublished work. © 2026 Siemens*
