# XML Interface — Attributes

本目录汇总了 **XMLInterface** 对象的属性（Attributes）文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `attributes.md` | XMLInterface 属性的 Markdown 文档（主文档） |
| `attributes.txtx` | 对应的纯文本源文档，内容与 `attributes.md` 基本一致 |

## 内容概要

### 概述

要查看所选 **类（Class）** 或 **实例（Instance）** 的方法、只读属性和属性：

- 对于 **类**：在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**。
- 对于 **实例**：按下 **F8**，或点击插入实例的 Frame 的 Home 选项卡中的 **Show Attributes and Methods**。

属性的值可以通过对话框中的复选框、文本框、下拉列表进行设置和读取，也可以通过赋值语句来完成，例如：

```
MyFileInterface.FileName := "C:\users\johnE\myData.txt"
print MyXMLInterface.Context
posit := Station.Cont.XPos
```

### 属性列表

文档共描述了 XMLInterface 的三个属性：

1. **Context [SimTalk]**
   - 设置 `<Path>` 指定的 XMLInterface 要读取的数据上下文。
   - 语法：`<Path>.Context:string`
   - 可赋值为字符串（string）类型。
   - 示例：`MyXMLInterface.Context := "Data/Objects"`

2. **FileName [SimTalk] — XML Interface**
   - 设置 `<Path>` 指定的 XMLInterface 要读取的 XML 文件名。
   - 语法：`<Path>.FileName:string`
   - 可赋值为字符串（string）类型。
   - 示例：`MyXMLInterface.FileName := "C:\users\johnE\myfile.xml"`

3. **ImportMethod [SimTalk]**
   - 设置用于提取并顺序处理导入数据的方法名。
   - 备注：该方法由 `openRead` 为 XML 文件中包含的所有对象调用。
   - 语法：`<Path>.ImportMethod:object`
   - 可赋值为对象（object）类型。
   - 示例：`MyXMLInterface.ImportMethod := &MyImportMethod`

### 相关主题

- SimTalk
- openRead [SimTalk]
- User Interface Objects
- Display and User Interface Objects

> 来源：Plant Simulation Help — © 2026 Siemens. Unpublished work.
