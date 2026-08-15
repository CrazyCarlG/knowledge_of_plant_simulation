# Chart 对象 — 方法（Methods）

本目录汇总 **Chart** 对象的全部方法（`methods.md` / `methods.txtx`）。

## 概述

**Chart** 用于在 Frame 中可视化当前数据与仿真运行结果。Chart 提供下述方法，以及 **所有对象的通用方法（Methods of All Objects）**。

可通过 **Show Attributes and Methods** 查看全部方法、只读属性与属性：

- 类库上下文菜单 → **Show Attributes and Methods**：显示所选类的成员。
- Frame 中按 **F8** 或 Home 功能区 → **Show Attributes and Methods**：显示所选实例的成员。

## 语法符号说明

- `<Path>`：方法所应用对象的路径。
- 括号内为参数签名（参数名 + 数据类型），例如 `(Parameter:string)`。除常量外，也可使用相应类型的变量或返回该类型的方法。
- `[,Parameter:boolean]`：方括号内为可选参数。
- `:= false`：参数默认值。
- 箭头 `→` 后为返回值的数据类型。

> **注意**：表达式内务必输入括号 `(…)`，否则可能产生意外结果并打开调试器。

## 方法总览

| 方法 | 说明 | 语法 |
|---|---|---|
| `addObject` | 将指定对象添加到 Chart，等同于将其拖到 Chart 上 | `<Path>.addObject(Object:object) → boolean` |
| `copyBitmapToClipboard` | 将 Chart 显示窗口内容以位图复制到剪贴板 | `<Path>.copyBitmapToClipboard([Width:integer, Height:integer])` |
| `copyBitmapToFile` | 将 Chart 图形以 `.png` 文件复制到文件 | `<Path>.copyBitmapToFile(FileName:string, Width:integer, Height:integer)` |
| `copyBitmapToIcon` | 将 Chart 图形复制为指定对象的图标 | `<Path>.copyBitmapToIcon(Destination:object, IconNumberOrName:integer/string[, Width:integer, Height:integer])` |
| `getAnnotations` | 返回 Chart 的 **Annotations**（注解）表内容 | `<Path>.getAnnotations(AnnotationsToGet:table)` |
| `getColor` | 返回 Chart 中某项颜色的 RGB 值 | `<Path>.getColor(ColorNo:integer[, byref Opacity:integer]) → integer` |
| `getHTMLCode` | 以 SVG 格式返回 Chart 图形的 HTML 代码 | `<Path>.getHTMLCode([Caption:string, Width:integer, Height:integer, inMM:boolean]) → string` |
| `getLineStyle` | 返回 Chart 的线型设置（线型、线宽、标记） | `<Path>.getLineStyle(ColorNumber:integer, byRef Style:string, byRef Weight:string, byRef Marker:string)` |
| `printChart` | 将 Chart 窗口内容打印到默认打印机 | `<Path>.printChart([Width:real, Height:real, Orientation:integer])` |
| `putValuesIntoTable` | 将 Chart 采集的值写入指定表格 | `<Path>.putValuesIntoTable(DestinationTable:table)` |
| `resetValues` | 重置 Histogram / Plotter 采集的值 | `<Path>.resetValues` |
| `setAnnotations` | 设置 Chart 的 **Annotations** 表 | `<Path>.setAnnotations(AnnotationsToSet:table)` |
| `setColor` | 设置 Chart 中某项的颜色 | `<Path>.setColor(ColorNo:integer, RGB:integer[, Opacity:integer])` |
| `setLineStyle` | 设置 Chart 的线型设置 | `<Path>.setLineStyle(ColorNumber:integer, LineStyle:string[, LineWeight:string, Marker:string])` |
| `setWindowPosition` | 设置 Chart 窗口的位置、宽度与高度 | `<Path>.setWindowPosition(X:integer, Y:integer, Width:integer, Height:integer)` |
| `showPrintDialog` | 打开 Chart 的打印对话框 | `<Path>.showPrintDialog([Width:real, Height:real])` |
| `update` | 以当前值刷新 Chart 显示 | `<Path>.update → boolean` |

## 方法要点

### 图形输出类

- **`copyBitmapToClipboard`**：可选指定宽高（像素）；省略则使用当前尺寸。
- **`copyBitmapToFile`**：将图形写入 `.png` 文件（`FileName` 不含扩展名时自动补 `.png`）。
- **`copyBitmapToIcon`**：作用于所寻址实例的图标（非对象类的图标）；若指定图标名/编号不存在，则新建图标；省略宽高时使用 Chart 当前宽高。
- **`getHTMLCode`**：返回 SVG 格式的 HTML；可指定标题、宽高，`inMM` 控制单位为毫米（`true`）或像素（`false`）。
- **`printChart`**：可指定打印宽高（毫米）与方向（`0` 默认、`1` 横向、`2` 纵向）。
- **`showPrintDialog`**：打开打印对话框，可选预置打印宽高（毫米）。

### 数据采集类

- **`putValuesIntoTable`**：将采集值写入表格，尤其适用于 Category 为 **Histogram** 或 **Plotter** 的场景。
- **`resetValues`**：删除已有数据并重新采集，可用于记录周直方图或抑制 ramp-up 阶段的数据。
- **`update`**：刷新显示；若 Chart 为 Sample 模式的 Plotter，会额外采样一次新数据点。返回 `true`（Chart 打开）或 `false`（Chart 关闭）。

### 注解（Annotations）类

- **`getAnnotations` / `setAnnotations`**：读写 Chart 的注解表。注解表包含以下列：

| 列 | 说明 |
|---|---|
| **Type** | 注解类型：`0` 垂直线、`1` 水平线、`2` X 轴标签、`3` Y 轴标签、`4` 文本 |
| **Value** | 线条/标签显示位置（水平线/Y 轴标签为 Y 值；垂直线/X 轴标签为 X 值；柱状图中 `3.5` 表示第 3、4 根柱之间） |
| **From** | 线条起点（可为对角线；水平线/文本为 X 值，垂直线为 Y 值） |
| **To** | 线条终点（From 与 To 均为空时贯穿整个窗口） |
| **Color** | 颜色编号（在 Color 选项卡定义） |
| **Style** | 线型（类型 0/1）或标记样式（类型 4） |
| **Text** | 描述文本；可选两位前缀码（`|` + 字母）控制文本位置 |

文本位置前缀码：`|l` 图内左缘、`|L` 图外左缘、`|r` 图内右缘、`|R` 图外右缘、`|c` 图内居中。

### 颜色与线型类

**颜色编号（`ColorNo` / `ColorNumber`）：**

| 项目 | 编号 |
|---|---|
| Grid（网格） | -3 |
| Background（背景） | -2 |
| Desk（底板/网格外区域） | -1 |
| Text（文本） | 0 |
| 预定义输入通道颜色 | 1–14 |

- **`getColor`**：返回 RGB 值，可选 `byref Opacity` 读取透明度。
- **`setColor`**：设置 RGB 颜色与可选透明度（`0` 完全透明，`255` 完全不透明；半透明可提升 Area 图表可读性）。
- **`getLineStyle`**：通过 `byRef` 返回线型（Style）、线宽（Weight）、标记（Marker）。
- **`setLineStyle`**：设置线型、线宽、标记；线型可用缩写（如 `". ."` 代表点线、`"_ _"` 或 `"- -"` 代表虚线）。

**线型 / 标记样式对照（Style 值）：**

| 值 | 线型 | 标记样式 |
|---|---|---|
| 0 | 细实线 | 仅文本（无标记） |
| 1 | 虚线 | 加号 |
| 2 | 点线 | 叉号 |
| 3 | 点划线 | 圆 |
| 4 | 双点划线 | 实心圆 |
| 5 | 中等细实线 | 方形 |
| 6 | 粗实线 | 实心方形 |
| 7 | 网格刻度 | 菱形 |
| 8 | 网格线 | 实心菱形 |
| 9–13 | 无 / 中等粗实线 / 特粗实线 | 三角、圆、方、菱形等标记 |
| 14–36 | 无 | 各类小/大三角、圆、方、菱形标记 |
| 92–99 | 无 | 北/东北/东/东南/南/西南/西/西北箭头 |

### 窗口类

- **`setWindowPosition`**：设置 Chart 窗口左上角坐标（`X`、`Y`）及宽高。
- **`addObject`**：与拖放操作等效（例如 `MyChart.addObject(MyExporter)`）。

## 只读属性（Read-Only Attributes）

Chart 同时提供 **所有对象的只读属性（Read-Only Attributes of All Objects）**。只读属性只能查询、不能设置，其值在查询时由 Plant Simulation 计算；多数只读属性对应对象选项卡上不可编辑的对话框项。

## 相关文档

- 一般说明（General）：[`../general/README.md`](../general/README.md)
- 属性（Attributes）：[`../attributes/attributes.md`](../attributes/attributes.md)
- 只读属性（Read-Only Attributes）：[`../read-only-attributes/read-only-attributes.md`](../read-only-attributes/read-only-attributes.md)
