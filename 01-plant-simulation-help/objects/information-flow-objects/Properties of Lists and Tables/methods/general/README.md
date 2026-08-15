# General — Methods of Lists and Tables

本目录汇总 Lists 与 Tables 的通用（general）方法说明，内容来源于同目录下的 `general.md`。

## 概述

- Lists 与 Tables 共享一组方法；不同类型的对象——`DataStack`、`DataQueue`、`DataList`、`DataTable`、`TimeSequence`——还各自提供对象特有的方法。
- 查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：
  - 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，显示所选类（Class）的属性和方法。
  - 在插入实例的 Frame 上按 **F8** 键，或点击 Home 功能区选项卡中的 **Show Attributes and Methods**，显示所选实例（Instance）的属性和方法。

## 阅读方法签名（语法行）

方法语法行示例：

```
<Path>.readFile(FileName:string[, NoDebugger:boolean:=false,
CodePage:string:="ANSI"]) → boolean
```

- `<Path>` 表示该方法所应用的对象的路径。
- 方法签名（每个参数的标识符与数据类型）列在圆括号内。例如 `(Parameter:string)` 表示一个 `string` 类型的参数；除了常量值，也可使用所需类型的变量或返回所需类型的方法。
- 可选参数用方括号列出。例如 `[,Parameter:boolean]` 表示可以（但不是必须）输入该 boolean 参数。
- 若参数有默认值，签名会在参数之后显示默认值。
- 若方法有返回值，签名会在箭头 `->` 之后显示其数据类型。

> **注意：** 请务必为括号内的表达式输入圆括号 `(…)`；漏输可能导致意外结果并打开调试器（Debugger）。

## 签名缩写

| 参数 | 数据类型 | 取值范围 |
|---|---|---|
| integer | integer | 大于零的整数 |
| any | 所有数据类型 | 取决于数据类型 |
| listrange | — | 一个范围（range） |
| direction | string | `"up"`、`"down"`、`" "` |
| attributes | string | 属性名 |

## 访问 Lists 和 Tables 的方法

- Lists 与 Tables 提供用于访问它们的方法（见左侧目录）。
- 读写访问权限取决于对象类，并在各子章节中说明。

## 参见（See also）

- Methods for Accessing Lists and Tables
- Methods for the Order of Cells within Lists and Tables
- Methods for the Format of Lists and Tables
- Methods for Querying Statistics Values of Lists and Tables
- Methods for Importing and Exporting Data in Text Format
- Instantiating Local Lists and Tables
- Methods for Indirectly Accessing Lists and Tables
- Methods of the DataTable
- Methods of the DataList
- Methods of DataQueue and DataStack
