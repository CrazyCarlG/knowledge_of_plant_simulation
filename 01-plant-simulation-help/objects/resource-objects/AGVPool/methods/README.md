# AGVPool 方法总结（Methods of the AGVPool）

本目录汇总了 `AGVPool` 对象（自动导引车池）所提供的方法。内容来源于 `methods.md`。

## 概述

`AGVPool` 提供：

- 下方列出的方法。
- 所有对象共用的方法（Methods of All Objects）。

如需查看对象的全部方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例所在 Frame 的 Home 选项卡上的 **Show Attributes and Methods**，查看所选实例的方法、只读属性和属性。

## 语法行（Syntax line）说明

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：该方法所应用对象的路径。
- 方法签名（由标识符和参数的数据类型组成）写在括号内。例如 `(Parameter:string)` 表示一个 string 类型的参数。除了常量值，也可以使用所需类型的变量，或返回所需类型的方法。
  > **注意：** 括号内的表达式务必输入括号 `(…)`。否则可能导致意外结果并打开调试器（Debugger）。
- 可选参数写在方括号内。例如 `[,Parameter:boolean]` 表示可以输入也可以不输入该 boolean 参数。
- 若参数有默认值，签名会在参数后显示默认值，例如 `:= false`。
- 若方法有返回值，签名会在箭头 `->` 后显示其数据类型，例如 `→ boolean`。

## 方法列表

### getAssignedAGV [SimTalk]

返回由 `<Path>` 指定的 `AGVPool` 中、由编号指定的 AGV。

- **类型：** Method
- **语法：**
  ```
  <Path>.getAssignedAGV(No:integer) -> object
  ```
- **参数：** `No`（integer 类型）——被分配 AGV 的编号。
- **返回值：** object 类型。
- **示例：**
  ```
  print MyAGVPool.getAssignedAGV(2)
  -- 可能返回，例如 .UserObjects.MyAGV:2
  ```
- **参见：** Assigned AGVs [AGVPool]

### getAssignedAGVsTable [SimTalk]

返回包含 `<Path>` 指定的 `AGVPool` 中已分配 AGV 的表格。

- **类型：** Method
- **语法：**
  ```
  <Path>.getAssignedAGVsTable([AssignedAGVs:table]) -> any
  ```
- **参数：** 可选参数 `AssignedAGVs`（table 类型）——指定写入 AGV 的表格名称。
  - 若未指定该可选参数，Plant Simulation 会返回一个包含已分配自动导引车（AGV）的数组。
- **返回值：** any 类型。
- **示例：**
  ```
  MyAGVPool.getAssignedAGVsTable(myAssignedAGVsTable) // 将 AGV 写入指定表格
  MyAGVPool.getAssignedAGVsTable // 将 AGV 写入数组
  ```
- **参见：** Assigned AGVs [AGVPool]

### getIdleAGV [SimTalk]

返回 `<Path>` 指定的 `AGVPool` 中属性 `IsIdle` 为 `true` 的一个 AGV。

- **备注：** `getIdleAGV` 还会将被返回 AGV 的 `IsIdle` 属性设为 `false`。若要让该 AGV 再次可用（通常在 AGV 到达路线终点时），需要自行将 `IsIdle` 重新设为 `true`。
- **类型：** Method
- **语法：**
  ```
  <Path>.getIdleAGV → object
  ```
- **返回值：** object 类型。若无空闲 AGV 可用，则返回 `VOID`。
- **示例：**
  ```
  waituntil AGVPool.NumIdleAGVs > 0
  var AGV := AGVPool.getIdleAGV
  ```
- **参见：**
  - IsIdle [SimTalk] - Transporter
  - NumIdleAGVs [SimTalk]
  - Fine-position an AGV
  - Read-Only Attributes of the AGVPool
