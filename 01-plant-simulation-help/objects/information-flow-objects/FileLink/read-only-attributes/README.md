# FileLink — Read-Only Attributes（摘要）

本目录包含 Plant Simulation 帮助文档中关于 **FileLink** 对象（信息流对象）的“只读属性（Read-Only Attributes）”页面内容。

## 文件说明

- `read-only-attributes.md` — FileLink 只读属性参考的结构化 Markdown 版本。
- `read-only-attributes.txtx` — 从帮助文档提取的同一主题纯文本版本。

两者内容一致。

## 概述

只读属性的值只能查询，不能设置，因为 Plant Simulation 会在查询时计算这些值。大多数只读属性对应对话框中不可编辑的条目（例如 Statistics 选项卡上的条目）。

## 查看只读属性

- 在 **Class Library** 中，从所选 **Class** 的上下文菜单中选择 **Show Attributes and Methods**，即可显示该类的方法、只读属性和属性。
- 对于插入到 Frame 中的 **Instance**，按 **F8** 键或点击 Frame 的 **Home** 功能区选项卡上的 **Show Attributes and Methods**，即可显示该实例的方法、只读属性和属性。

## 查询只读属性

查询某个只读属性的值时，例如可以输入：

```
print MyFileLink.UUID
```

## FileLink 的属性

FileLink 提供：

- 帮助文档目录（table of contents）中所列出的属性。
- **所有对象的属性（Attributes of All Objects）**。

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods** 窗口（帮助文档以 **Station** 对象为例进行了图示说明）。

## 备注

- 本目录下无子文件夹。
