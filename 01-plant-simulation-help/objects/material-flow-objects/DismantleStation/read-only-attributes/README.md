# DismantleStation - Read-Only Attributes

本目录包含 DismantleStation（拆解站）对象的**只读属性（Read-Only Attributes）**文档。

## 概述

DismantleStation 提供：

- 目录中列出的只读属性
- 所有对象的只读属性（_Read-Only Attributes of All Objects）
- 物流对象（Material Flow Objects）的只读属性

只读属性可以被查询，但不能被设置，因为 Plant Simulation 会在查询的时间点计算其值。大多数情况下，只读属性对应于对象某个选项卡上不可用的对话框项（例如 Statistics 选项卡）。

可通过 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性和属性。

## 内容清单

本目录下的文档涵盖以下只读属性/方法：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `statBlockingTimeTable` | Method | 返回 DismantleStation 的 Blocking Times 表内容并写入指定表 |
| `NumLeavingMU` | 只读属性 | 返回 Exiting MUs（离开的 MU）表中的 MU 数量 |
| `StatAverageDwellTime` | 只读属性 | 返回主部件在 DismantleStation 上停留的平均时间 |

## 详细说明

### statBlockingTimeTable [SimTalk]

- **类型：** Method
- **语法：** `<Path>.statBlockingTimeTable(BlockingTimes:table) → boolean`
- **参数：** `BlockingTimes`（table 类型）指定表名
- **返回值：** boolean
- **示例：**
  ```simtalk
  var myBlockingTimesTable: table
  MyDismantleStation.statBlockingTimeTable(myBlockingTimesTable)
  ```
- **参见：** Tab Statistics [DismantleStation]

### NumLeavingMU [SimTalk]

- **类型：** 只读属性
- **语法：** `<Path>.NumLeavingMU → integer`
- **返回值：** integer
- **示例：**
  ```simtalk
  for var i := 1 to MyDismantleStation.NumLeavingMU
     print MyDismantleStation.leavingMU(i)
  next
  ```
- **参见：** Exiting MUs

### StatAverageDwellTime [SimTalk] - DismantleStation

- **类型：** 只读属性
- **语法：** `<Path>.StatAverageDwellTime → time`
- **返回值：** time
- **备注：** Plant Simulation 仅统计 DismantleStation 未暂停且非计划外的时间
- **示例：**
  ```simtalk
  print MyDismantleStation.StatAverageDwellTime
  ```
- **参见：** Tab Statistics [DismantleStation]、Attributes of the DismantleStation、_Attributes of the DismantleStation

## 查询示例

查询只读属性值的通用方式：

```simtalk
print DismantleStation.NumLeavingMU
```
