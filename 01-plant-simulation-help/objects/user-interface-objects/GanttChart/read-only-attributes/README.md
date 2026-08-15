# README — GanttChart（只读属性）

本目录汇总了 **GanttChart（甘特图）** 用户界面对象的只读属性（Read-Only Attributes）说明。内容来源为同目录下的 `read-only-attributes.md`（以及 `read-only-attributes.txtx` 原始文本）。

> 说明：`read-only-attributes` 目录下暂无子文件夹，因此不存在子文件夹内的 `README.md` 可供合并。本 README 仅基于 `read-only-attributes.md` 的内容总结。

## 概述

本页对应帮助文档中的 “Read-Only Attributes of the GanttChart” 页面。该页面主要说明 GanttChart 提供的**只读属性**，并附带说明了 GanttChart 的**属性**（Attributes）以及 `update` 方法。

> 备注：本页面开头还包含 `update [SimTalk]` 方法的内容（该方法同样收录在 *Methods of the GanttChart* 页面中，见同级的 `methods` 目录）。

## update [SimTalk] - GanttChart

用当前值刷新由 `<Path>` 指定的、已显示的 GanttChart。

- **类型：** 方法（Method）
- **语法：** `Path.update`

**示例**

```
MyGanttChart.update
```

## 只读属性（Read-Only Attributes）

GanttChart 提供 **所有对象的只读属性（Read-Only Attributes of All Objects）**。

- 可以**查询**只读属性的值，但**不能设置**它们，因为 Plant Simulation 会针对查询时刻计算该值。
- 多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口（下图以对象 **Station** 为例进行说明）：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选**类（Class）** 的方法、只读属性与属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选**实例（Instance）** 的方法、只读属性与属性。

查询某个只读属性的值，例如：

```
print MyGanttChart.UUID
```

## 属性（Attributes）

GanttChart 提供：

- 左侧目录（table of contents）中列出的属性；
- **所有对象的属性（Attributes of All Objects）**。

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口（下图以对象 **Station** 为例进行说明）：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选**类（Class）** 的方法、只读属性与属性。
- 按 **F8** 键，或点击已插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可显示所选**实例（Instance）** 的方法、只读属性与属性。

属性既可以**获取**其值，也可以**设置**其值，方式有两种：

- 通过对话框中的复选框、文本框和下拉列表；
- 通过为相应属性赋值。

设置某个属性的值，例如：

```
MyGanttChart.IsShown := true
```

---

*来源：Plant Simulation Help 11-4847。Unpublished work. © 2026 Siemens。*
