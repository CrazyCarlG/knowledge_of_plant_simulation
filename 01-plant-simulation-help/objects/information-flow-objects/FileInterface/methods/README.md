# FileInterface — Methods（方法摘要）

本目录包含 Plant Simulation 帮助文档中关于 **FileInterface** 对象（信息流对象）的“方法（Methods）”页面内容。

## 文件说明

- `methods.md` — FileInterface 方法参考的结构化 Markdown 版本。
- `methods.txtx` — 从帮助文档提取的同一主题纯文本版本。

两者内容一致。本目录无子文件夹。

## FileInterface 概述

**FileInterface** 用于在仿真运行期间访问文本文件中的数据：

- 可以在文本文件中为仿真运行创建数据，并在仿真运行期间将其导入 Plant Simulation。
- 也可以将协议文件（protocol files）、统计表等直接写入文本文件，无需借助表格（tables）或列表（lists）绕行。
- 之后可以在电子表格程序或文字处理应用中可视化或处理这些数据。

关键限制：

- Plant Simulation 一次最多可同时打开 **10 个文件**。
- FileInterface 处理字母、数字和特殊字符，但**不能处理二进制数据**。
- 一个 FileInterface 一次只管理**一个文件**。
- FileInterface 的写函数始终返回 `false`。

## 方法总览

FileInterface 提供下列方法（此外还有“所有对象的通用方法 Methods of All Objects”）。除 `read` 和 `readLn` 返回 `string` 外，其余方法均返回 `boolean`。

| 方法 | 语法 | 返回类型 | 说明 |
| --- | --- | --- | --- |
| `close` | `<Path>.close` | `boolean` | 保存所有未保存的数据并关闭文件。 |
| `formFeed` | `<Path>.formFeed` | `boolean` | 在文件末尾添加换页符（FormFeed），并将光标置于条目末尾；打印时打印机在此字符后换页。 |
| `goBottom` | `<Path>.goBottom` | `boolean` | 将光标移动到文件最后一行的末尾。 |
| `goToLine` | `<Path>.goToLine(LineNumber:integer)` | `boolean` | 将光标移动到指定行的开头；若文件行数不足则返回 `false`。 |
| `goTop` | `<Path>.goTop` | `boolean` | 将光标移动到文件第一行的开头。 |
| `newLine` | `<Path>.newLine` | `boolean` | 在文件末尾添加回车符，并将光标置于条目末尾；用于格式化协议文件。 |
| `open` | `<Path>.open([ReadOnly:boolean:=false])` | `boolean` | 打开文件；可选参数 `ReadOnly` 设置只读权限（`true`）或读写权限（`false`，默认）。 |
| `read` | `<Path>.read` | `string` | 从当前位置读取整个文件。 |
| `readLn` | `<Path>.readLn` | `string` | 读取光标所在行，并将计数器加一。 |
| `remove` | `<Path>.remove` | `boolean` | 若文件已打开则关闭并永久删除该文件。 |
| `write` | `<Path>.write(Data:any)` | `boolean` | 将指定数据追加到文件末尾，不另起一行。 |
| `writeLn` | `<Path>.writeLn(Data:any, ...)` | `boolean` | 将指定数据连同回车符和换行符写入文件，之后的数据写入新的一行。 |

## 通用行为说明

多个方法（`formFeed`、`goBottom`、`goToLine`、`goTop`、`newLine` 等）在文件未打开时会自动打开文件，并在访问后保持打开状态。

写入类方法（`write`、`writeLn`）若文件未以写模式打开，会自动打开、写入并关闭；若文件无法打开（例如路径无效），会报错。为避免报错，可先显式调用 `open`，它在文件无法打开时返回 `false`。

`open` 的备注：

- 文件保持打开，直到用 `close` 关闭。
- 连续执行多个操作时，先打开文件可提高访问速度；操作完成后应关闭文件，因为 Plant Simulation 异常终止时数据不会保存。
- Plant Simulation 一次只能打开 10 个文件，建议关闭不再需要的文件。

## 语法行说明

方法语法行形如：

```
<Path>.open([ReadOnly:boolean:=false]) → boolean
```

- `<Path>` 表示方法所作用对象的路径。
- 括号内为签名（参数标识符及数据类型），如 `(Parameter:string)` 表示 `string` 类型参数。
- 可选参数放在方括号内，如 `[,Parameter:boolean]`。
- 若参数有默认值，在参数后以 `:= 默认值` 表示，如 `:= false`。
- 若方法有返回值，在箭头 `→` 后标明数据类型，如 `→ boolean`。

> **注意：** 括号内的表达式务必输入括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。

## 只读属性

FileInterface 还提供“只读属性（Read-Only Attributes）”（以及“所有对象的通用只读属性”）。只读属性的值只能查询、不能设置，其值由 Plant Simulation 在查询时计算。例如：

```
print MyFileInterface.IsOpen
```

## 相关目录

- `../general/` — FileInterface 的常规（General）页面说明。
- `../attributes/` — FileInterface 的属性（Attributes）说明。
- `../read-only-attributes/` — FileInterface 的只读属性说明。
