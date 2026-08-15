# README — GanttChart（方法）

本目录汇总了 **GanttChart（甘特图）** 用户界面对象的方法（Methods）说明。内容来源为同目录下的 `methods.md`（以及 `methods.txtx` 原始文本）。

> 说明：`methods` 目录下暂无子文件夹，因此不存在子文件夹内的 `README.md` 可供合并。本 README 仅基于 `methods.md` 的内容总结。

## 概述

GanttChart 提供：

- 左侧目录（table of contents）中列出的方法；
- 所有对象的方法（Methods of All Objects）。

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口。

## 语法行约定（Syntax line conventions）

方法的语法行（Syntax line）示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所作用对象的路径。
- 方法签名（由参数标识符与数据类型组成）列在圆括号中。例如 `(Parameter:string)` 表示数据类型为 string 的参数。除常量值外，也可使用所需类型的变量或返回所需类型的方法。
- **注意：** 务必为括号内的表达式输入括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。
- 可选参数列在方括号内。例如 `[,Parameter:boolean]` 表示可以输入、也可以不输入该 boolean 参数。
- 若参数有默认值，签名会在参数之后显示默认值，例如 `:= false`。
- 若方法有返回值，签名会在箭头 `->` 之后显示其数据类型，例如 `→ boolean`。

## 方法列表

| 方法 | 语法 | 说明 |
| --- | --- | --- |
| `exportChart [SimTalk]` | `<Path>.exportChart(FileName:string[, TimeScale:real])` | 将 GanttChart 导出为 HTML 文件 |
| `getData [SimTalk]` | `<Path>.getData(DataTable:table)` | 返回 GanttChart 当前显示的数据并写入表格 |
| `getHTMLCode [SimTalk]` | `<Path>.getHTMLCode([Caption:string, Scale:real]) → string` | 以 SVG 格式返回 GanttChart 的图表 HTML 代码 |
| `getLanes [SimTalk]` | `<Path>.getLanes(TableToWrite:table)` | 返回为 GanttChart 定义的泳道（lanes） |
| `setData [SimTalk]` | `<Path>.setData(DataTable:table)` | 设置 GanttChart 将要显示的数据 |
| `setLanes [SimTalk]` | `<Path>.setLanes(TableToRead:table)` | 设置 GanttChart 要显示的泳道 |
| `update [SimTalk]` | `Path.update` | 用当前值刷新所显示的 GanttChart |

### exportChart [SimTalk]

将 `<Path>` 指定的 GanttChart 导出为 HTML 文件。

**参数**

- `FileName`（数据类型 `table`）——Plant Simulation 将 HTML 文件写入的表格。
- `TimeScale`（可选，数据类型 `real`）——时间尺度，以“像素/秒”表示。例如取值为 `0.5` 时，持续 60 秒的 Gantt 事件显示为 30 像素长的条形。

**示例**

```
MyGanttChart.exportChart("MyExportedGanttChart.html", 0.5)
// 导出到仿真模型所在文件夹
MyGanttChart.exportChart("D:\MyModels\MyExportedGanttChart.html")
// 导出到指定文件夹
```

### getData [SimTalk]

返回 `<Path>` 指定的 GanttChart 所显示的数据，并将其写入表格。

**参数**

- `DataTable`（数据类型 `table`）——Plant Simulation 将 GanttChart 显示的数据写入的表格。

数据表格式在 `setData` 下描述。

**示例**

```
MyGanttChart.getData(MyGanttDataTable)
```

### getHTMLCode [SimTalk] - GanttChart

以 SVG 格式返回 `<Path>` 指定的 GanttChart 的图表 HTML 代码。

**参数**

- `Caption`（可选，数据类型 `string`）——所需的图形标题。
- `Scale`（可选，数据类型 `real`）——图形的缩放比例。

**返回值**

返回值为 `string` 数据类型。

**示例**

```
HtmlReport.content := "<<" + GanttChart.getHtmlCode("Test (half size)", 0.5) + ">>"
HtmlReport.show
```

**另请参见：** Display a HtmlReport

### getLanes [SimTalk]

返回为 `<Path>` 指定的 GanttChart 定义的泳道。

**参数**

- `TableToWrite`（数据类型 `table`）——Plant Simulation 将 GanttChart 的泳道写入的表格。

泳道由设置 `Top` 和 `Height` 定义，二者数据类型均为 `integer`。

**示例**

```
MyGanttChart.getLanes(MyLanesTable)
```

**另请参见：** `setLanes`、Edit Lanes

### setData [SimTalk]

设置 `<Path>` 指定的 GanttChart 将要显示的数据。

> **备注：** 不能同时手动设置数据并自动收集数据。使用方法 `setData` 时，请将 `CollectData` 设为 `false`。

**参数**

`DataTable`（数据类型 `table`）——包含 GanttChart 将要显示数据的表格。

该表格有八列。前三列必须包含数据；后三列中至少有一列要包含数据。表中每一行描述一个以条形可视化的 Gantt 事件：

- **Start Date** —— 事件的开始日期。
- **End Date** —— 事件的结束日期。
- **Resource** —— 依据其后三列的数据，表示“进入指定状态的资源”、或“指定零件”、或二者兼有。可输入 Frame 中资源的路径，或将资源拖放到相应单元格，或输入自由资源文本。
- **Resource State** —— 资源所处的状态，可取：`Working`、`Setting-up`、`Waiting`、`Blocked`、`PoweringUpDown`、`Failed`、`Stopped`、`Paused` 或 `Unplanned`。该值不必对应任何已存在的物料流实例。
- **Part** —— 由资源加工的零件。输入零件类的路径、冒号以及零件实例编号，例如 `.MUs.Part:1`；也可输入自由零件文本。
- **Part Name** —— GanttChart 显示为工具提示（Tooltip）的任意字符串。
- **Lane** —— Gantt 事件所在的泳道。
- **Color** —— Gantt 事件的颜色。若不输入颜色，Plant Simulation 会自动分配颜色：资源视图中按零件分配，零件视图中按资源分配。

**示例**

```
MyGanttChart.setData(MyGanttData)
```

**另请参见：** `getData`、`setLanes`、Show Chart [button] - GanttChart、CollectData [SimTalk] - GanttChart

### setLanes [SimTalk]

设置 `<Path>` 指定的 GanttChart 要显示的泳道。

**参数**

- `TableToRead`（数据类型 `table`）——包含 GanttChart 所显示泳道的表格。

泳道由设置 `Top` 和 `Height` 定义，二者数据类型均为 `integer`。

**示例**

```
MyGanttChart.setLanes(MyLanesTable)
MyGanttChart.ShowResourceStates := true
```

**另请参见：** `getLanes`、Edit Lanes、Show Chart [button] - GanttChart

### update [SimTalk] - GanttChart

用当前值刷新 `<Path>` 指定的已显示 GanttChart。

**示例**

```
MyGanttChart.update
```

## 只读属性（Read-Only Attributes）

GanttChart 提供 *所有对象的只读属性（Read-Only Attributes of All Objects）*。

只读属性可以查询其值，但不能设置，因为 Plant Simulation 会针对查询时刻计算该值。多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口。

---

*来源：Plant Simulation Help 11-4838。Unpublished work. © 2026 Siemens。*
