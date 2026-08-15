# DataTable 对象 — Attributes（属性）

本目录汇总了 **DataTable 对象**（信息流对象）的属性（Attributes）文档。属性是可以读写（可设置/可查询）的 SimTalk 成员，用于配置 DataTable 的格式、索引、游标、数据类型与容量等。

> 源文件：`attributes.md`（内容详见该文件）；原始导出文本：`attributes.txtx`。

## 概述

DataTable 的属性用于设置和读取 DataTable 的各类特性。你可以通过对话框中的复选框、文本框和下拉列表来设置/读取属性值，也可以通过给相应属性赋值来设置/读取。

- **设置**属性值，例如：

```simtalk
MyDataTable.ColumnIndex := false
MyDataTable.calculateList({1,3}..{2,4})
```

- **读取**属性值，例如：

```simtalk
print MyDataTable.MaxXDim
posit := Station.Cont.XPos
```

查看对象的全部属性、方法和只读属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类的方法、只读属性和属性。
- 按 `F8` 键，或点击包含该实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选实例的方法、只读属性和属性。

## 属性清单

DataTable 共有以下属性（均以 `<Path>` 表示对象路径）：

| 属性 | 数据类型 | 语法 | 说明 |
|------|----------|------|------|
| `Alignment` | string | `<Path>.Alignment:string` | 设置 DataTable 所有单元格的对齐方式，可指定 `"left"`、`"right"` 或 `"center"`。 |
| `Changed` | boolean | `<Path>.Changed:boolean` | 当 DataTable 内容发生变化时被置为 `true`；可随时重置为 `false` 以检测后续变化（可监视 Watchable）。 |
| `ColumnIndex` | boolean | `<Path>.ColumnIndex:boolean` | 激活（`true`）或停用（`false`）用户自定义列索引。 |
| `ColumnIndexContents` | boolean | `<Path>.ColumnIndexContents:boolean` | 决定列索引是否属于 DataTable 的内容（`true`）或格式（`false`），从而影响 *Inherit Contents* / *Inherit Format* 时的继承行为。 |
| `CommonFormatColumnIndex` | boolean | `<Path>.CommonFormatColumnIndex:boolean` | 激活（`true`）或停用（`false`）列索引的 Common Format（通用格式）。 |
| `CursorX` | integer | `<Path>.CursorX:integer` | 设置内部游标所在的列；第 1 列为 1，若要包含用户自定义索引则设为 0。 |
| `CursorY` | integer | `<Path>.CursorY:integer` | 设置内部游标所在的行；第 1 行为 1，若要包含用户自定义索引则设为 0。 |
| `DataType` | string | `<Path>.DataType:string` | 设置 DataTable 的默认数据类型（字符串形式，如 `"real"`）。 |
| `DataTypeColumnIndex` | string | `<Path>.DataTypeColumnIndex:string` | 设置用户自定义列索引的数据类型。 |
| `FastAccessColumnIndex` | boolean | `<Path>.FastAccessColumnIndex:boolean` | 启用（`true`）/停用（`false`）用户自定义列索引的快速访问。 |
| `FastAccessRowIndex` | boolean | `<Path>.FastAccessRowIndex:boolean` | 启用（`true`）/停用（`false`）用户自定义行索引的快速访问。 |
| `FormatString` | string | `<Path>.FormatString:string` | 设置 DataTable 的格式字符串。 |
| `FormatStringColumnIndex` | string | `<Path>.FormatStringColumnIndex:string` | 根据数据类型设置列索引的格式字符串。 |
| `FormatStringRowIndex` | string | `<Path>.FormatStringRowIndex:string` | 根据数据类型设置行索引的格式字符串。 |
| `MaxXDim` | integer | `<Path>.MaxXDim:integer` | 设置 DataTable 的最大列数；`-1` 表示无限大小。 |
| `MaxYDim` | integer | `<Path>.MaxYDim:integer` | 设置 DataTable 的最大行数；`-1` 表示无限大小。 |
| `Name` | string | `<Path>.Name:string` | 设置 DataTable 的名称；也可通过信息流访问子列表的名称。 |
| `RowIndex` | boolean | `<Path>.RowIndex:boolean` | 激活（`true`）或停用（`false`）用户自定义行索引。 |
| `ShowColumnIndex` | boolean | `<Path>.ShowColumnIndex:boolean` | 显示（`true`）或隐藏（`false`）DataTable 的列索引。 |
| `ShowRowIndex` | boolean | `<Path>.ShowRowIndex:boolean` | 显示（`true`）或隐藏（`false`）DataTable 的行索引。 |
| `UniqueKeyColumnIndex` | boolean | `<Path>.UniqueKeyColumnIndex:boolean` | 对用户自定义列索引应用唯一键（`true`）或不应用（`false`）。 |
| `UniqueKeyRowIndex` | boolean | `<Path>.UniqueKeyRowIndex:boolean` | 对用户自定义行索引应用唯一键（`true`）或不应用（`false`）。 |

## 数据类型（DataType）

属性 `DataType` 与 `DataTypeColumnIndex` 支持以下数据类型：

| 数据类型 | 说明 |
|----------|------|
| Acceleration | 适用于 Conveyor、Track、TwoLaneTrack、Transporter 对象，单位 m/s² |
| Boolean | true 或 false |
| Date | 日期（dd.MM.yyyy） |
| DateTime | 日期加时间（dd.MM.yyyy HH:mm:ss） |
| Integer | 整数值 |
| Length | 浮点数，值取决于长度单位 |
| List | 单列列表，与 DataList 共享属性 |
| Money | 浮点数 |
| Object | 指向仿真模型或对象的引用 |
| Queue | 单列列表，与 DataQueue 共享属性 |
| Real | 浮点数，如 3.1415 |
| Speed | 浮点数，值取决于速度单位 |
| Stack | 单列列表，与 DataStack 共享属性 |
| String | 字符、数字和特殊字符 |
| Table | 一列或多列表格，与 DataTable 共享属性 |
| Time | 时间（hh:mm:ss.ss） |
| Weight | 浮点数，值取决于重量单位 |

## 相关对象：DataList

DataTable 的文档还附带介绍了 **DataList** 对象：一个单列列表，可通过位置（即行号）随机访问各单元格内容，可类比为"卡片盒"。添加条目时，后续条目顺次下移；可以删除、读取并重新添加条目。其相关功能可在 **List Ribbon Tab** 上访问。

> 注意区分**可插入模型中的 DataList 对象**与**数据类型 `list`**：后者是其他对象的一部分，本身不是独立对象、没有自己的图标，因此不识别 DataList 的 SimTalk 函数（如 `Location` 或 `existsIcon`），但其余读写方法对两者都适用。

## 参见

- `ColumnIndex` / `RowIndex` / `ShowColumnIndex` / `ShowRowIndex` — 用户自定义索引相关属性
- `CursorX` / `CursorY` / `setCursor` / `find` / `min` / `max` — 游标与查找相关
- `MaxXDim` / `MaxYDim` — 行列容量相关
- Data Type [lists]、Format String [text box]、Common Format [check box]
- DataList 对象（信息流对象）
- Properties of Lists and Tables（列表和表格的共享属性）

## 目录文件说明

| 文件 | 说明 |
|------|------|
| `attributes.md` | DataTable 属性的 Markdown 文档（本 README 的原始来源）。 |
| `attributes.txtx` | 对应帮助文档的纯文本导出，内容与 `.md` 基本一致。 |
