# Read-Only Attributes of the DataTable

本目录汇总了 DataTable（数据表）对象的只读属性（Read-Only Attributes）文档。

## 概述

DataTable 提供以下只读属性：

- 本目录所列出的只读属性。
- Lists 与 Tables 的只读属性（_Read-Only Attributes of Lists and Tables）。
- 所有对象的只读属性（_Read-Only Attributes of All Objects）。

只读属性的值可以被查询（query），但不能被设置（set），因为 Plant Simulation 会在你查询它的那一刻实时计算其值。大多数情况下，只读属性对应对象某个选项卡上不可用的对话框项（例如 **Statistics** 选项卡）。

要查看对象的全部方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，以显示所选 Class 的方法、只读属性和属性。
- 在已插入实例的 Frame 的 Home 功能区选项卡上按 **F8** 或点击 **Show Attributes and Methods**，以显示所选 Instance 的方法、只读属性和属性。

查询只读属性的值示例：

```simtalk
print MyDataTable.Full
```

## 只读属性清单

| 属性 | 说明 | 语法 | 返回值 | 可监视 (Watchable) |
|------|------|------|--------|:------------------:|
| `XDim` | 返回 DataTable 中最后一个含有条目的列的编号。**备注：** 不计入用户自定义索引。 | `<Path>.XDim -> integer` | `integer` | 是 |
| `XDimIndex` | 返回 DataTable 列索引中含有条目的最后一个单元格。**备注：** 不计入第 0 列。 | `<Path>.XDimIndex -> integer` | `integer` | 否 |
| `YDim` | 返回 DataTable 中最后一个含有条目的行的编号。**备注：** 不计入用户自定义索引。 | `<Path>.YDim -> integer` | `integer` | 是 |
| `YDimIndex` | 返回 DataTable 行索引中含有条目的最后一个单元格。 | `<Path>.YDimIndex -> integer` | `integer` | 否 |

## 属性详情

### XDim [SimTalk] - DataTable

返回由 `<Path>` 指定的 DataTable 中最后一个含有条目的列的编号。

- **备注：** Plant Simulation 不计入用户自定义索引。
- **类型：** 只读属性
- **语法：** `<Path>.XDim -> integer`
- **可监视：** 是
- **返回值：** 数据类型 `integer`

**示例：**

```simtalk
print MyDataTable.XDim
print timeSequence.XDim
```

### XDimIndex [SimTalk]

返回由 `<Path>` 指定的 DataTable 列索引中含有条目的最后一个单元格。

- **备注：** Plant Simulation 不计入第 0 列。
- **类型：** 只读属性
- **语法：** `<Path>.XDimIndex -> integer`
- **返回值：** 数据类型 `integer`

**示例：**

```simtalk
print MyDataTable.XDimIndex
```

### YDim [SimTalk] - DataTable

返回由 `<Path>` 指定的 DataTable 中最后一个含有条目的行的编号。

- **备注：** Plant Simulation 不计入用户自定义索引。
- **类型：** 只读属性
- **语法：** `<Path>.YDim -> integer`
- **可监视：** 是
- **返回值：** 数据类型 `integer`

**示例：**

```simtalk
print MyDataTable.YDim
print timeSequence.YDim
```

### YDimIndex [SimTalk]

返回由 `<Path>` 指定的 DataTable 行索引中含有条目的最后一个单元格。

- **类型：** 只读属性
- **语法：** `<Path>.YDimIndex -> integer`
- **返回值：** 数据类型 `integer`

**示例：**

```simtalk
print MyDataTable.YDimIndex
```

## 参见（See also）

- `XDim [SimTalk] - DataTable`
- `YDim [SimTalk] - DataTable`
- `XDimIndex [SimTalk]`
- `YDimIndex [SimTalk]`
- `ColumnIndex [SimTalk]`
- `RowIndex [SimTalk]`
- Number of Columns [lists]
- Number of Rows [lists]

## 目录文件说明

| 文件 | 说明 |
|------|------|
| `read-only-attributes.md` | DataTable 只读属性的 Markdown 文档（本 README 的原始来源）。 |
| `read-only-attributes.txtx` | 对应帮助文档的纯文本导出，内容与 `.md` 基本一致，另包含部分 Attributes 章节内容。 |
