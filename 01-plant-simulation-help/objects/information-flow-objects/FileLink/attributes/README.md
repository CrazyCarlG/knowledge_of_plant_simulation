# FileLink — Attributes（摘要）

本目录包含 Plant Simulation 帮助文档中关于 **FileLink** 对象（信息流对象）的“属性（Attributes）”页面内容。

## 文件说明

- `attributes.md` — FileLink 属性参考的结构化 Markdown 版本。
- `attributes.txtx` — 从帮助文档提取的同一主题纯文本版本。

两者内容一致。

## 概述

FileLink 的属性既可以通过对话框中的复选框、文本框和下拉列表设置/获取，也可以通过为相应属性赋值来设置/获取。FileLink 提供：

- 帮助文档目录（table of contents）中所列出的属性。
- **所有对象的属性（Attributes of All Objects）**（继承自所有对象共有的属性）。

## 查看属性与方法

- 在 **Class Library** 中，从所选 **Class** 的上下文菜单中选择 **Show Attributes and Methods**，即可显示该类的方法、只读属性和属性。
- 对于插入到 Frame 中的 **Instance**，按 **F8** 键或点击 Frame 的 **Home** 功能区选项卡上的 **Show Attributes and Methods**，即可显示该实例的方法、只读属性和属性。

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods** 窗口。

## 设置与获取属性值

- 设置属性值，例如：

```simtalk
frame1.FileLink2.Embed := false
```

- 获取属性值，例如：

```simtalk
print frame1.FileLink2.Embed
posit := Station.Cont.XPos
```

## FileLink 特有的属性

### `Embed` [SimTalk]

使 `<Path>` 所指定的 FileLink 将文件嵌入到 Plant Simulation Frame 中（`true`）或不嵌入（`false`）。

- 该属性**不继承**，默认值为 `false`。
- 赋值为 `true` 时，该版本的文件会成为仿真模型的一部分，移动原文件不影响模型；但嵌入后对文件的更改不会反映到模型中。
- 嵌入可能会显著增大 `.spp` 模型文件的体积。
- 赋值为 `false` 时，Plant Simulation 会创建指向计算机文件系统中文件的链接；若移动或删除该文件，链接将失效，Plant Simulation 无法找到并打开它。

**类型：** Attribute

**语法：**

```simtalk
<Path>.Embed:boolean
```

**赋值类型：** 可赋 `boolean` 数据类型的值。

**示例：**

```simtalk
Model1.FileLink2.Embed := false
print Model1.FileLink2.Embed
```

**另见：** Embed File [check box]、Embed [SimTalk]

### `FileName` [SimTalk] - FileLink

设置或返回 `<Path>` 所指定的 FileLink 的链接/嵌入文件名。

- 赋值时也必须指定文件扩展名。

**类型：** Attribute

**语法：**

```simtalk
<Path>.FileName:string
```

**赋值类型：** 可赋 `string` 数据类型的值。

**示例：**

```simtalk
frame1.FileLink1.FileName := "myName.xls" // MS Excel file
print frame1.FileLink1.FileName
```

**另见：** Filename [FileLink]

## 相关对象引用：FileInterface

属性页面中还包含了 **FileInterface** 对象的说明。FileInterface 用于访问你在其他程序中创建并以 ASCII 格式存储的数据：

- 可在仿真运行期间将文本文件中的数据导入 Plant Simulation，或将协议文件、统计表等直接写入文本文件，无需借助表格或列表。
- Plant Simulation 一次最多可同时打开 10 个文件；一个 FileInterface 一次只管理一个文件。
- FileInterface 只能处理字母、数字和特殊字符，不能处理二进制数据（如程序、图形等）。
- 若停用安全设置 **File > Model Settings > General > Prohibit Access to the Computer**，FileInterface 只能更改模型文件夹中的文件，写函数始终返回 `false`，且只能删除模型文件夹及其子文件夹中的文件。
- 添加对象：点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > InformationFlow > FileInterface**。

## 备注

- 本目录下无子文件夹。
