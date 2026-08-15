# FileInterface — Attributes（属性摘要）

本目录包含 Plant Simulation 帮助文档中关于 **FileInterface** 对象（信息流对象）的“属性（Attributes）”页面内容。

## 文件说明

- `attributes.md` — FileInterface 属性参考的结构化 Markdown 版本。
- `attributes.txtx` — 从帮助文档提取的同一主题纯文本版本。

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

## 属性总览

FileInterface 提供下列属性（此外还有“所有对象的通用属性 Attributes of All Objects”）。

| 属性 | 类型 | 语法 | 赋值/返回类型 | 说明 |
| --- | --- | --- | --- | --- |
| `IsOpen` | 只读属性 | `<Path>.IsOpen → boolean` | `boolean` | 返回由 `<Path>` 指定、用于写入数据的文件是否已打开（`true`）或未打开（`false`）。 |
| `Encoding` | 属性 | `<Path>.Encoding:string` | `string` | 设置 Plant Simulation 保存其写入的文件时使用的编码；读取文件时保存该文件的编码，无法识别时返回 `ANSI`。 |
| `FileName` | 属性 | `<Path>.FileName:string` | `string` | 设置由 `<Path>` 指定的文件名称。 |

## 属性详细说明

### IsOpen [SimTalk] - FileInterface（只读属性）

返回由 `<Path>` 指定、用于写入数据的文件是否已打开。

- **类型：** 只读属性（Read-only attribute）
- **语法：** `<Path>.IsOpen → boolean`
- **返回值：** 数据类型 `boolean`

示例：

```simtalk
print MyFileInterface.IsOpen
```

### Encoding [SimTalk]（属性）

设置 Plant Simulation 保存其写入的文件时使用的编码。当 Plant Simulation 读取文件时，该属性保存文件的编码；若无法识别编码，则返回 `ANSI`。

- **类型：** 属性（Attribute）
- **语法：** `<Path>.Encoding:string`
- **赋值：** 数据类型 `string`

可指定的值：

- **`"ANSI"`** — 8 位字符集，最多可表示 256 个字符（0 到 255）；是 7 位 ASCII 字符集的超集。
- **`"UTF-8"`** — Unicode 字符集的另一种编码，每个字符由 1 到 3 个字节表示。
- **`"UTF-16"`** — Unicode 字符集的另一种编码。
- **`"Unicode"`** — 16 位字符集，几乎涵盖世界上所有书面语言；Plant Simulation 以 UTF-16 编码保存 Unicode，每个字符由 2 个字节表示。

示例：

```simtalk
MyFileInterface.Encoding := "Unicode"
```

### FileName [SimTalk] - FileInterface（属性）

设置由 `<Path>` 指定的文件名称。

- **类型：** 属性（Attribute）
- **语法：** `<Path>.FileName:string`
- **赋值：** 数据类型 `string`

示例：

```simtalk
MyFileInterface.FileName := "C:\users\johnE\myData.txt"
```

## 通用使用说明

可以设置属性的值，也可以获取属性的值，既可通过对话框中的复选框、文本框和下拉列表，也可通过给相应属性赋值来实现。

- **设置属性值**（示例）：

```simtalk
MyFileInterface.FileName := "C:\users\johnE\myData.txt"
```

- **获取属性值**（示例）：

```simtalk
print MyFileInterface.FileName
posit := Station.Cont.XPos
```

## 查看方式

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在 **Class Library** 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的方法、只读属性和属性。
- 按 **F8** 键或点击插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，查看所选实例的方法、只读属性和属性。

## 相关条目

- `Encoding [drop-down list]` — 对话框中的编码下拉列表。
- `Filename [FileInterface]` — 对话框中的文件名输入框。
- `XMLInterface` — 用于读取和提取存储在 XML 文件中的数据的对象。

## 相关目录

- `../general/` — FileInterface 的常规（General）页面说明。
- `../methods/` — FileInterface 的方法（Methods）说明。
- `../read-only-attributes/` — FileInterface 的只读属性说明。
