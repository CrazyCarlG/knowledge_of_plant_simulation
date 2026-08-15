# ShiftCalendar 属性（Attributes）总览

本目录记录 Plant Simulation 中 **ShiftCalendar（班次日历）** 对象的所有属性。ShiftCalendar 用于定义工厂的班次/工作时间计划，从而控制相关资源对象的工作与非工作时间。

## 概览

ShiftCalendar 提供以下属性（同时继承自 [Attributes of All Objects] 的通用属性）：

| 属性 | 类型 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| `Unplanned` | 只读属性（Read-only） | `boolean` | 返回该 ShiftCalendar 是否处于未计划状态 |
| `Active` | 属性（Attribute） | `boolean` | 激活或停用该 ShiftCalendar |
| `Calendar` | 属性（Attribute） | `any` | 设置日历（节假日/停班日期） |
| `Resources` | 属性（Attribute） | `any` | 设置受该 ShiftCalendar 控制的资源对象 |
| `ShiftPlan` | 属性（Attribute） | `table` | 设置班次时间计划表 |

> 可通过 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性和属性：在 Class Library 的右键菜单中选择，或在 Frame 中按 **F8** 键 / 点击 Home 选项卡中的对应按钮。

---

## 属性详解

### 1. Unplanned（SimTalk）
返回由 `<Path>` 指定的 ShiftCalendar 是否处于未计划（unplanned）状态。

- **类型：** 只读属性
- **语法：** `<Path>.Unplanned → boolean`
- **可监视（Watchable）：** 是
- **返回值：** `boolean`

```simtalk
print MyShiftCalendar.Unplanned
```

### 2. Active（SimTalk）
激活（`true`）或停用（`false`）由 `<Path>` 指定的 ShiftCalendar。若工厂按班次工作则设为 `true`。

- **类型：** 属性
- **语法：** `<Path>.Active:boolean`
- **赋值：** `boolean`

```simtalk
MyShiftCalendar.Active := true
```

### 3. Calendar（SimTalk）
设置由 `<Path>` 指定的 ShiftCalendar 的日历。

- Plant Simulation 会将指定的 DataTable 内容复制到 **Calendar** 选项卡的内部日历表中。
- 建议表格使用列标题与行标题，列设置如下：
  - 第 1 列（Date From）：数据类型 `date`，班次开始的日期；
  - 第 2 列（Date To）：数据类型 `date`，班次结束的日期；
  - 第 3 列（Reduce Time To）：数据类型 `string`，班次生效的小时数；
  - 第 4 列（Comment）：数据类型 `string`，班次不生效的原因。
- 赋值会覆盖已有的日历内容。

- **类型：** 属性
- **语法：** `<Path>.Calendar:any`
- **赋值：** `any`

```simtalk
MyShiftCalendar.Calendar := shiftCalendarTable
```

### 4. Resources（SimTalk）
设置由 `<Path>` 指定的 ShiftCalendar 所控制的资源对象。

- Plant Simulation 会将指定的 DataTable 内容复制到 **Resources** 选项卡的内部对象表中。
- 表格第 1 列数据类型应为 `object`，填入所有受该班次日历控制的对象。
- 赋值会覆盖已有的资源表内容，建议使用列/行标题，其余列可自由使用。

- **类型：** 属性
- **语法：** `<Path>.Resources:any`
- **赋值：** `any`

```simtalk
shifts.Resources := ResourcesTable
```

### 5. ShiftPlan（SimTalk）
设置由 `<Path>` 指定的 ShiftCalendar 的班次时间计划。

- Plant Simulation 会将指定的 DataTable 内容复制到 **Shift Times** 选项卡的内部班次时间表中。
- 建议表格使用列/行标题，列设置如下：
  - 第 1 列（Shift）：`string`，班次名称；
  - 第 2 列（From）：`time`，班次开始时间；
  - 第 3 列（To）：`time`，班次结束时间；
  - 第 4～10 列（Mo～Sun）：`boolean`，该班次是否适用于对应星期（`true`/`false`）；
  - 第 11 列（Pauses）：`string`，休息时间。
- 注意：不能定义相互重叠的班次。
- 赋值会覆盖已有的班次时间内容。
- 读取 ShiftPlan 时：返回表的第 12 列包含休息起止时间的子表，第 13 列为错误码（非零表示班次计划数据不一致）。

> **注意：** `ShiftPlan` 返回的是临时表，ShiftCalendar 无法检测该临时表是否被修改。正确做法是先将返回表赋给变量，修改后再赋回 `ShiftPlan`。

- **类型：** 属性
- **语法：** `<Path>.ShiftPlan:table`
- **赋值：** `table`

```simtalk
MyShiftCalendar.ShiftPlan := shiftTimesTable
// 修改班次表
var t:table := ShiftCalendar.ShiftPlan
t["From", 1] := 3:00:00
ShiftCalendar.ShiftPlan := t
```

---

## 源文件说明

- `attributes.md`：本目录的属性文档（Markdown 格式）。
- `attributes.txtx`：对应的原始帮助文本提取内容（含页码，如 Plant Simulation Help 11-3519～11-3524）。

> 注：`attributes.txtx` 末尾混入了 `LockoutZone` 对象的相关内容，属于相邻章节，不在此 ShiftCalendar 属性范围内。
