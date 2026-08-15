# FootPath 属性（Attributes）汇总

本目录包含 FootPath（步行路径）对象属性的说明文档，源文件为 `attributes.md`。本 README 对该文档内容进行归纳总结。

> 本目录下没有子文件夹，因此没有额外的子级 `README.md` 内容。

## 文档概述

`attributes.md` 首先说明了 FootPath 对象提供的属性来源：

- 文档左侧目录中列出的属性。
- **所有对象通用属性（Attributes of All Objects）**。

同时介绍了查看属性与方法的方式：

- 在插入了实例的 Frame 中，按 **F8** 键或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，显示所选 **Instance（实例）** 的方法、只读属性与属性。
- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，显示所选 **Class（类）** 的方法、只读属性与属性。

以及属性的读写示例：

- 查询只读属性：`print MyFootPath.UUID`
- 设置属性：`MyFootPath.length := 5`
- 读取属性：`print MyFootPath.length`、`posit := Station.Cont.XPos`

属性值既可以通过对话框窗口中的复选框、文本框和下拉列表来设置/获取，也可以通过给相应属性赋值来设置/获取。

## 属性清单

`attributes.md` 共记录了以下 2 个 SimTalk 属性，每个属性均包含类型（Type）、语法（Syntax）、赋值类型（Assignment Value）、示例及关联主题（See also）。

| 属性 | 语法 | 说明 |
| --- | --- | --- |
| `Length` | `<Path>.Length:length` | 设置 FootPath 的物理长度。Worker 从位置 0 进入 FootPath，走过所设定的长度后离开。 |
| `Width` | `<Path>.Width:length` | 设置 FootPath 的宽度。 |

> 说明：两个属性的赋值类型均为数据 `length`。在 SimTalk 2.0 中可直接在数值后紧跟长度单位 `m`、`mm`、`km`、`cm`、`yd`、`ft`、`in`（数值与单位之间不加空格，如 `10m` 或 `10.2m`），浮点数与整数均可指定单位。

示例：

```simtalk
MyFootPath.Length := 44m
MyFootPath.Width := 2 // meters
```

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `attributes.md` | FootPath 对象属性的完整说明文档（Markdown） |
| `attributes.txtx` | 同一帮助内容的原始文本提取版（内容与 `attributes.md` 等价） |
| `README.md` | 本汇总文件 |

## 备注

`attributes.md` 末尾出现的 **WorkerPool** 为下一页帮助主题的衔接内容（WorkerPool 用于建模工厂中的休息室/员工室），不属于 FootPath 的属性说明。
