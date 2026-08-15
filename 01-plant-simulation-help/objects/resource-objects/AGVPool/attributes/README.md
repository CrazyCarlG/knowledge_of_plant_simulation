# AGVPool 属性总结（Attributes of the AGVPool）

本目录汇总了 `AGVPool` 对象（自动导引车池）所提供的属性文档。内容来源于 `attributes.md`（结构化 Markdown 版本）与 `attributes.txtx`（帮助系统的原始提取文本）。二者描述同一对象，此处合并总结。

## 概述

`AGVPool` 提供：

- 下方列出的属性。
- 所有对象共用的属性（Attributes of All Objects）。

如需查看对象的全部方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，查看所选实例的方法、只读属性和属性。

可以通过对话框窗口中的复选框、文本框和下拉列表，或通过给相应属性赋值，来设置/获取属性的值：

- 设置属性值，例如：

```simtalk
MyAGVPool.BrokerPath := mybroker
```

- 获取属性值，例如：

```simtalk
MyAGVPool.AGV := ".UserObjects.MyAGV"
```

## 属性列表

| 名称 | 类型 | 语法 | 赋值/返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `StatAverageTraveledDistance` | 只读属性 | `<Path>.StatAverageTraveledDistance → length` | `length` | 返回 AGVPool 中 AGV 行驶的平均距离（米） |
| `AGV` | 属性 | `<Path>.AGV:path` | `path` | 设置 AGVPool 所创建的 AGV |
| `Amount` | 属性 | `<Path>.Amount:integer` | `integer` | 设置 AGVPool 所创建的 AGV 数量 |

## 成员详解

### StatAverageTraveledDistance [SimTalk]

返回由 `<Path>` 指定的 AGVPool 中 AGV 行驶的平均距离（单位：米）。

- **类型：** 只读属性
- **语法：**

```simtalk
<Path>.StatAverageTraveledDistance → length
```

- **返回值：** `length` 类型。

**示例：**

```simtalk
print AGVPool.StatAverageTraveledDistance
```

### AGV [SimTalk]

设置由 `<Path>` 指定的 AGVPool 所创建的 AGV。

- **类型：** 属性
- **语法：**

```simtalk
<Path>.AGV:path
```

- **赋值：** 可赋 `path` 类型的值。

**备注：**

> 默认情况下，Class Library 中 *MUs* 文件夹里的 **Transporter** 即 AGV。因此 Transporter 的方法、属性和只读属性同样适用于 AGV。

Plant Simulation 在仿真运行的初始化阶段创建指定数量（Amount）的 AGV。

**示例：**

```simtalk
MyAGVPool.AGV := ".UserObjects.MyAGV"
```

```simtalk
var AGV : object := AGVPool.Cont
AGV.setRoute([M1,M2,M3,M4])
waituntil AGV.DestinationWasReached
AGV.setRoute([M1,M2,M3,M4])
```

**参见：**

- AGV [text box]
- AGV [SimTalk]
- setRoute [SimTalk] - Transporter
- setRouteSegments [SimTalk]

### Amount [SimTalk]

设置由 `<Path>` 指定的 AGVPool 所创建的 AGV 数量。

- **类型：** 属性
- **语法：**

```simtalk
<Path>.Amount:integer
```

- **赋值：** 可赋 `integer` 类型的值。

**备注：**

Plant Simulation 在仿真运行的初始化阶段创建指定数量（Amount）的 AGV。

**示例：**

```simtalk
MyAGVPool.Amount := 2
```

**参见：**

- Amount [text box] - AGVPool
- AGV [SimTalk]
- Marker

### Marker

使用 **Marker** 对象在仿真模型中设置路径点，让 AGV 从 AGVPool 驶向其目的地。

## 相关目录

- `general/`：AGVPool 的通用帮助文档（概述、对话框、Attributes / Statistics / User-defined 选项卡、各菜单及代码示例）。
- `methods/`：AGVPool 的方法总结（`getAssignedAGV`、`getAssignedAGVsTable`、`getIdleAGV`）。
- `read-only-attributes/`：AGVPool 的只读属性总结（`getIdleAGV`、`NumIdleAGVs`、`StatAverageTraveledDistance`）。

## 参见

- Attributes of All Objects
- Read-Only Attributes of the AGVPool
- Methods of the AGVPool
- *Source: Plant Simulation Help, © 2026 Siemens*
