# 查询统计值的方法（Querying Statistics Values）

本目录汇总了列表（List）和表（Table）用于查询统计值的 SimTalk 方法。这些方法适用于 `DataStack`、`DataQueue`、`DataList`、`DataTable` 和 `TimeSequence` 对象。

> 来源文件：`Querying Statistics Values.md`

## 方法总览

| 方法 | 功能 | 语法 | 返回值类型 |
| --- | --- | --- | --- |
| `max` | 返回指定单元格范围内的最大值 | `<Path>.max([Range:listrange, ...])` | `real` |
| `meanValue` | 返回指定单元格范围内所有值的算术平均值 | `<Path>.meanValue([Range:listrange, ...])` | `real` / `integer` |
| `min` | 返回指定单元格范围内的最小值 | `<Path>.min([Range:listrange, ...])` | `real` |
| `standardDeviation` | 返回指定单元格范围内所有值相对均值的标准差 | `<Path>.standardDeviation([Range:listrange, ...])` | `real` / `integer` |
| `sum` | 返回指定单元格范围内所有值的总和 | `<Path>.sum([Range:listrange, ...])` | `real` / `integer` |

## 各方法详解

### max
- 返回 `<Path>` 指定的列表或表格单元格范围内的最大值。
- 找到最大值后，会将光标移动到该值所在的单元格。
- 返回值的类型取决于指定范围的统一数据类型；若数据类型不统一，则转换为 `real` 返回。

### meanValue
- 返回 `<Path>` 指定的列表或表格单元格范围内所有值的算术平均值。
- 返回值为 `real` 或 `integer` 类型。

### min
- 返回 `<Path>` 指定的列表或表格单元格范围内的最小值。
- 找到最小值后，会将光标移动到该值所在的单元格。
- 返回值的类型取决于指定范围的统一数据类型；若数据类型不统一，则转换为 `real` 返回。

### standardDeviation
- 返回 `<Path>` 指定的列表或表格单元格范围内所有值相对均值的标准差。
- 返回值为 `real` 或 `integer` 类型。

### sum
- 返回 `<Path>` 指定的列表或表格单元格范围内所有值的总和。
- `Range` 参数可选，若未指定，则对所有单元格求和。
- 返回值的类型取决于指定范围的统一数据类型；若数据类型不统一，则转换为 `real` 返回。

## 通用说明

- **参数**：`Range` 参数的数据类型为 `listrange`，用于指定单元格范围。各方法均可传入多个范围参数（`...`）。
- **数据类型限制**：所有方法仅适用于 `real` 或 `integer` 类型的数据。对于其他数据类型，Plant Simulation 会忽略它们，或将其值视为 0。
- **布尔值处理**：所有方法都将布尔值 `true` 视为 `1.0`，将 `false` 视为 `0.0`。
- **光标行为**：`max` 与 `min` 在找到目标值后，会将光标设置到对应单元格（参见 `CursorX`、`CursorY`）。

## 示例

```SimTalk
print MyDataStack.max({*})
print MyDataQueue.max({1}..{*})
print MyDataList.max({*})
print MyDataTable.max({3,3}..{3,*}) // 最大条目数

print MyDataStack.meanValue({*})
print MyDataQueue.meanValue({1}..{*})
print MyDataList.meanValue({*})
print MyDataTable.meanValue({3,3}..{3,*})

print MyDataStack.min({*})
print MyDataQueue.min({1}..{*})
print MyDataList.min({3}..{*})
print MyDataTable.min({3,3}..{3,*}) // 最小条目数

print MyDataStack.standardDeviation({*})
print MyDataQueue.standardDeviation({1}..{*})
print MyDataList.standardDeviation({*})
print MyDataTable.standardDeviation({3,3}..{3,*})

print MyDataStack.sum({*})
print MyDataQueue.sum({1}..{*})
print MyDataList.sum({*})
print MyDataTable.sum({3,3}..{3,*})
```

## 相关参考

- `CursorX [SimTalk]`
- `CursorY [SimTalk]`
- 指定单元格范围（多列）> 列索引属于内容（Column Index Belongs to Contents）
- 指定单元格范围（多列）> 列索引不属于内容（Column Index Does Not Belong to Contents）
