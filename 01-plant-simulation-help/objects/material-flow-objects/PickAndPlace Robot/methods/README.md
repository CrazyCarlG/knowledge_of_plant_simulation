# PickAndPlace Robot — Methods（方法）

本目录存放 **PickAndPlace Robot**（拾放机器人）对象的方法说明文档。内容来源为 `methods.md`（`methods.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. 概述

**PickAndPlace Robot** 提供：

- 本目录列出（左侧目录中）的方法；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

要查看对象的全部方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，查看所选**类**的方法、只读属性和属性；
- 在插入实例的 Frame 中按 **F8** 键，或点击 Home 功能区标签页的 **Show Attributes and Methods**，查看所选**实例**的方法、只读属性和属性。

## 2. 语法行（Syntax line）约定

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所应用对象的路径。
- 方法签名（各参数的标识符与数据类型）写在圆括号内。`(Parameter:string)` 表示数据类型为 string 的参数；除常量外，也可使用所需类型的变量或返回所需类型的方法。
- 方括号内为**可选参数**，例如 `[,Parameter:boolean]` 表示可输入也可不输入的 boolean 参数。
- 参数有默认值时，签名会在参数后显示，例如 `:= false`。
- 方法有返回值时，签名会在箭头 `→` 后显示其数据类型，例如 `→ boolean`。

> **注意：** 在圆括号内使用表达式时必须输入圆括号 `(…)`；省略可能导致意外结果并打开 Debugger。

## 3. 方法列表

PickAndPlace Robot 自身定义的方法共 7 个，主要围绕 **Angles Table（角度表）**、**Times Table（时间表）** 以及拾取/放置目标的设置与查询。

### 3.1 calculateAngles

计算机器人（`<Path>` 所指定）与其前驱（predecessor）和后继（successor）在 Frame 中连接时所需的角度。

- **类型：** Method
- **语法：** `<Path>.calculateAngles`

**备注：** 拾放机器人会把计算出的角度写入 **Angles Table**。

**示例：**

```
MyPickAndPlace.calculateAngles
```

**参见：** `getAnglesTable`、`setAnglesTable`、Calculate Angles、Angles Table。

---

### 3.2 getAnglesTable

返回拾放机器人（`<Path>` 所指定）的 **Angles Table**，并将其写入一个表中。

- **类型：** Method
- **语法：** `<Path>.getAnglesTable(AnglesTable:table) → table`

**参数：** `AnglesTable`（数据类型 `table`）表示表的名称，其中包含：

- 机器人拾取工件处的前驱的**名称（Name）**，或机器人放置工件处的后继的**名称**。`Name` 列也可包含传送带（Conveyor）上的传感器，例如 `Conveyor.sensorID(1)`。
- `Name` 列中的工位与拾放机器人之间的**角度（Angle）**。

插入 Connector 或将对象拖放到拾放机器人上时，Plant Simulation 会把相应值加入角度表。删除 Connector **不会**从表中移除相应条目，必须手动删除。也可以手动修改数值/名称或新增工位——例如在 Sensor Control 中请求机器人时很有用。

> **注意：** Plant Simulation 会自动把已修改的工位名称应用到 **Times Table**。

**返回值：** 数据类型 `table`。

**示例：**

```
var myAnglesTable: table
MyPickAndPlace.getAnglesTable(myAnglesTable)
```

**参见：** `setAnglesTable`、`calculateAngles`、Angles Table、Times Table。

---

### 3.3 getDestination

返回拾放机器人（`<Path>` 所指定）将要拾取或放置工件的目标对象。

- **类型：** Method
- **语法：** `<Path>.getDestination → any`

**返回值：** 数据类型 `any`。它可以是目标对象、目标对象上的目标位置，或目标对象上的传感器。当机器人空载旋转到目标时，也会返回一个目标对象。

**示例：**

```
// sets and gets the target of the part
PickAndPlace.setDestination(@.target, true)
print PickAndPlace.getDestination

end
MyStation := ?.getDestination
```

**参见：** `setDestination`、`GetLastDestination`。

---

### 3.4 getTimesTable

返回拾放机器人（`<Path>` 所指定）的 **Times Table**，并将其写入一个表中。

- **类型：** Method
- **语法：** `<Path>.getTimesTable(TimesTable:table) → table`

**参数：** `TimesTable`（数据类型 `table`）表示表的名称。时间表包含：

- 机器人要服务的所有对象的**名称（Names）**，以及机器人放置工件后移动到的**默认角度（Default Angle）**。
- **对角线上方的时间**是机器人空载旋转的时间。
- **对角线下方的时间**是机器人满载旋转（工件在机器人上）的时间。
- 对角线从“默认角度”列的最顶端单元格延伸到最后一列的最底端单元格。

示例中，单元格 A 表示从 Station 到 Source 的带工件旋转时间（0.3743 秒），单元格 B 表示从 Drain 到 Source 的空载旋转时间，单元格 C 表示从 Drain1 到默认角度的空载旋转时间。

插入 Connector 或将对象拖放到机器人上时，Plant Simulation 会把相应值写入 Times Table。计算时，Plant Simulation 假定四分之一圈旋转耗时一秒。这些时间可以修改。

删除 Connector 后，Plant Simulation **不会**从 Times Table 中删除该（现已断开的）对象的条目。必须在 Angles Table 中删除该条目（例如右键该行 → Delete Row）。点击机器人对话框中的 **Apply** 时，Plant Simulation 也会从 Times Table 中删除该条目。

**返回值：** 数据类型 `table`。

**示例：**

```
MyPickAndPlace.getTimesTable(myTimesTable)
var myTimesTable: table
MyPickAndPlace.getTimesTable(myTimesTable)
```

**参见：** `setTimesTable`、Times Table、Angles Table、Default Angle、Empty。

---

### 3.5 setAnglesTable

为拾放机器人（`<Path>` 所指定）分配一个 **Angles Table**。

- **类型：** Method
- **语法：** `<Path>.setAnglesTable(AnglesTable:table)`

**参数：** `AnglesTable`（数据类型 `table`）表示表的名称。可以修改以下数值：

- 机器人拾取工件处的前驱的**名称（Name）**，或机器人放置工件处的后继的**名称**。也可以输入 Conveyor 上的传感器（例如 `Conveyor.Sensors.id1`），用于在 Conveyor 上设置多个角度。
- `Name` 列中的工位与拾放机器人之间的**角度（Angle）**。

插入 Connector 或将对象拖放到机器人上时，Plant Simulation 会加入相应值。删除 Connector 不会移除该条目，必须手动删除。也可以手动修改数值/名称或新增工位（例如在 Sensor Control 中请求机器人）。

> **注意：** Plant Simulation 会自动把已修改的工位名称应用到 **Times Table**。

**示例：**

```
MyPickAndPlace.setAnglesTable(myAngleTable)
```

**参见：** `getAnglesTable`、`calculateAngles`、Angles Table、Times Table。

---

### 3.6 setDestination

设置拾放机器人（`<Path>` 所指定）放置工件或拾取新工件的目标对象。

- **类型：** Method
- **语法：**

```
<Path>.setDestination(DestinationObject:any[, WaitAtTarget:boolean])
<Path>.setDestination(DefaultPosition:void)
```

**参数：**

- `DestinationObject`（数据类型 `any`）表示目标对象、目标对象上的目标位置，或目标对象上的传感器。也可以是 MU 或 MU 上的存储位置。
- `WaitAtTarget`（可选，数据类型 `boolean`）设置机器人是否在目标工位等待（`true`）或不等待（`false`）。
- 若机器人为空，可用 `setDestination(void)` 将其送回默认位置。

**备注：** 通常用于 Target Control / `TargetCtrl`。用 `setDestination` 将机器人送往某个工位时，该工位上的 MU 按如下顺序解除阻塞（unblock）：

1. 首先解除已等待、且为其请求了机器人的 MU。
2. 否则调用 Pull Control（若存在）。
3. 若以上均不适用，则解除 Blocking List 中最早调度的 MU。

**示例：**

```
// set the target of the part
if @.target = SP3
   PickAndPlace.setDestination(@.target, false)
else
   PickAndPlace.setDestination(@.target, true)

end

print PickAndPlace.getDestination
// a target control with a sensor might, for example, look like this:
if not ?.Empty
   if @.PreviousLocation = Conveyor
       ?.setDestination(Station, false)
   else
       ?.setDestination(Conveyor.Sensors.id2, false)
   end
end
?.setDestination(MyStore[2,7])
MyPickAndPlace.setDestination(Conveyor.sensorID(1))
```

**参见：** `getDestination`、`TargetCtrl`、Target Control、Empty。

---

### 3.7 setTimesTable

为拾放机器人（`<Path>` 所指定）分配一个 **Times Table**。

- **类型：** Method
- **语法：** `<Path>.setTimesTable(TimesTable:table)`

**参数：** `TimesTable`（数据类型 `table`）表示表的名称。可以设置以下内容：

- 机器人要服务的所有对象的**名称（Names）**，以及机器人放置工件后移动到的**默认角度（Default Angle）**。
- **对角线上方的时间**是机器人空载旋转的时间；**对角线下方的时间**是机器人满载旋转（工件在机器人上）的时间。对角线从“默认角度”列的最顶端单元格延伸到最后一列的最底端单元格。

示例中，单元格 A 表示从 Source 到 Station 的带工件旋转时间（0.5 秒），单元格 B 表示从 Drain 到 Source 的空载旋转时间，单元格 C 表示从 Drain1 到默认角度的空载旋转时间。

插入 Connector 或将对象拖放到机器人上时，Plant Simulation 会把相应值写入 Times Table。计算时假定四分之一圈旋转耗时一秒。这些时间可以修改。

删除 Connector 后，Plant Simulation 不会从 Times Table 中删除该（现已断开的）对象的条目。请在 Angles Table 中删除该条目（右键该行 → Delete Row）；点击机器人对话框中的 **Apply** 也会从 Times Table 中删除该条目。

**示例：**

```
MyPickAndPlace.setTimesTable(myTimesTable)
```

**参见：** `getTimesTable`、Times Table、Angles Table、Default Angle、Empty。

## 4. PickAndPlace Robot 的只读属性

PickAndPlace Robot 提供：

- 左侧目录中列出的只读属性；
- 所有对象的只读属性（Read-Only Attributes of All Objects）；
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）。

只读属性的值**只能查询、不能设置**，因为 Plant Simulation 在你查询的时刻实时计算该值。大多数情况下，只读属性对应于对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

> 只读属性的详细列表见兄弟目录 `read-only-attributes/`。

## 目录说明

- `methods.md`：PickAndPlace Robot 方法说明的 Markdown 版本（本总结的源文件）。
- `methods.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
