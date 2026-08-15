# Workplace Methods

本目录包含 Workplace（工位）对象的方法文档，源文件为 `methods.md` 与 `methods.txtx`（两者内容一致，`methods.txtx` 为 Plant Simulation 帮助系统的导出文本）。

## 概述

Workplace 对象提供以下方法：

- 本目录表中所列的方法（`contentsList`、`getRouteCoordinates`、`getRouteLength`）。
- 所有对象通用方法（Methods of All Objects）。
- 物流对象方法（Methods of the Material Flow Objects）。

查看某对象全部方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的右键菜单选择 **Show Attributes and Methods**，显示所选类的方法、只读属性与属性。
- 在插入了实例的 Frame 中，按 **F8** 键或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，显示所选实例的方法、只读属性与属性。

## 语法行（Syntax Line）

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示该方法所作用对象的路径。
- 方法的签名（由参数标识符与数据类型组成）列于圆括号内。例如 `(Parameter:string)` 表示 string 类型的参数。
- 可选参数列于方括号内。例如 `[,Parameter:boolean]` 表示该 boolean 参数可省略。
- 若参数有默认值，签名会在参数后显示默认值（如上例中的 `:= false`）。
- 若方法有返回值，签名会在箭头后显示其数据类型（如上例中的 `→ boolean`）。

> **注意：** 请务必为括号内的表达式输入圆括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。

## 方法列表

### contentsList [SimTalk] — Workplace

返回一个数组，包含指定 `<Path>` 所代表的 Workplace 的 Contents List（内容列表）中的全部内容，即其中所有 Worker（工人）。

**语法**

```
<Path>.contentsList([ContentsList:table]) → any
```

**参数**

- 可选参数 `ContentsList`（数据类型 `table`）指定方法写入数值的表格名称（DataTable 或局部变量）。Plant Simulation 会自动生成该表格的格式，并删除表格中已有的格式与内容。

**返回值**

- 数据类型为 `any`。

**示例**

```js
Workplace2.contentsList(MyContentsList)
print Workplace2.contentsList
```

**参见**

- Contents [material flow objects]
- Contents [Workplace]

### getRouteCoordinates [SimTalk]

返回 Worker 从 `<Path>` 指定的 Workplace 到达另一个 Workplace 或 WorkerPool 所需行走路线的各途经点（waypoints）的 3D 坐标。

**类型**：Method

**语法**

```
<Path>.getRouteCoordinates(ToWorkplace:path[,
FreelyWithinArea:boolean:=false]) → array
```

**参数**

- `ToWorkplace`（数据类型 `path`）指定作为路线目的地的 Workplace。
- `FreelyWithinArea`（数据类型 `boolean`，可选）设置 Worker 是否在区域内自由行走到达该 Workplace：
  - 指定 `false`（或省略该参数）：通过由连接器（Connectors）连接的 Footpath（步行路径）计算两个 Workplace 之间的路线途经点。
  - 指定 `true`：计算区域内的路线途经点（即 Worker 在区域内自由行走所走的路线）。

**参数默认值**：`false`

**返回值**

- 二维数组，包含各途经点的 X 坐标、Y 坐标和 Z 坐标。

**示例**

```js
var coords:any := Workplace1.getRouteCoordinates(Workplace2)
print coords // outputs [[6.59, -6.0, 0.0] [6.60, -7.40, 0.0] [9.40, -7.40, 0.0] [13.690, -6.0, 0.0]]
```

### getRouteLength [SimTalk] — Workplace

返回 Worker 从 `<Path>` 指定的 Workplace 到达另一个 Workplace 或 WorkerPool 所需行走路线的长度。

**类型**：Method

**语法**

```
<Path>.getRouteLength(ToWorkplace:path[, FreelyWithinArea:boolean:=false])
→ length
```

**参数**

- `ToWorkplace`（数据类型 `path`）指定目的地 Workplace。
- `FreelyWithinArea`（数据类型 `boolean`，可选）设置 Worker 是否在区域内自由行走到达该 Workplace：
  - 接受默认值 `false`（或省略该参数）：通过由连接器（Connectors）连接的 Footpath 计算两个 Workplace 之间的路线长度。
  - 指定 `true`：计算区域内的路线长度（即 Worker 在区域内自由行走所走的路线）。

**参数默认值**：`false`

**返回值**

- 数据类型为 `length`。若 Plant Simulation 未找到路线，返回 `-1`。

**示例**

```js
var len:length := Workplace1.getRouteLength(Workplace2)
```

## 只读属性（Read-Only Attributes）

Workplace 提供所有对象通用的只读属性（Read-Only Attributes of All Objects）。
