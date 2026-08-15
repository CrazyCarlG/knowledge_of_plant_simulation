# Exporter 方法（Methods）总结

本目录包含 Exporter（导出器）对象的方法说明文档。当前目录下无子文件夹，主要来源文件为 `methods.md`（`methods.txtx` 为其纯文本版本，内容一致）。

## 概述

Exporter 是 Plant Simulation 中的资源对象（Resource Object），用于向 Broker（中介）导出服务（Services）。本文档介绍 Exporter 的状态显示及其提供的方法（SimTalk 方法）。

## 1. Exporter 的状态（States）

仿真运行期间，Exporter 的状态以对象图片顶部横向排列的立方体表示，颜色含义如下：

| 状态 | 图形颜色 |
| --- | --- |
| Exporter 发生故障（failed） | 红色 |
| Exporter 正在导出服务（exports services） | 绿色 |
| Exporter 已暂停（paused） | 蓝色 |

## 2. 方法总览

Exporter 提供的方法包括：

- 左侧目录中列出的方法
- 所有对象通用方法（Methods of All Objects）

查看方法、只读属性和属性的方式：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 查看选中 Class 的方法与属性。
- 按 **F8** 键或点击 Frame 的 Home 选项卡中的 **Show Attributes and Methods** 查看选中 Instance 的方法与属性。

### 语法行（Syntax）说明

以 `<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean` 为例：

- `<Path>`：方法所应用对象的路径。
- 括号内为方法签名（参数名与数据类型），例如 `(Parameter:string)` 表示字符串类型参数；可用变量或返回相应类型的方法代替常量。
- 方括号 `[...]` 内的参数为可选参数，例如 `[,Parameter:boolean]`。
- 参数默认值在参数后以 `:= 值` 表示，例如 `:= false`。
- 返回值类型在箭头 `→` 后表示，例如 `→ boolean`。

> 注意：表达式内部的括号 `(…)` 必须输入，否则可能导致意外结果并打开调试器（Debugger）。

## 3. 方法详解

### expStat [SimTalk]

返回 Exporter 的统计表并写入指定的表中。

- **类型**：Method
- **语法**：
  - `<Path>.expStat → boolean`
  - `<Path>.expStat(StatisticsTable:table) → boolean`
- **参数**：`StatisticsTable`（table 类型）指定表名。
- **返回值**（boolean）：
  - `true`：调用成功。
  - `false`：该对象未采集统计数据。
- **示例**：
  ```simtalk
  var MyExporterStatisticsTable: table
  MyExporter.expStat(MyExporterStatisticsTable)
  ```

### findNewImporter [SimTalk]

将 Exporter 在其 Broker 处注册为可用。

- **类型**：Method
- **语法**：`<Path>.findNewImporter`
- **说明**：Broker 随后搜索所有未完成的请求并尝试寻找新的 Exporter；该 Exporter 可承接新订单的信息会传递给所有通过 Connector 连接的 Broker。
- **示例**：
  ```simtalk
  MyExporter.findNewImporter
  ```
- **参见**：Importers [Exporter]、Importers [Worker]

### getExportedServices [SimTalk]

返回 Exporter/Worker 当前导出的所有服务。

- **类型**：Method
- **语法**：`<Path>.getExportedServices([Services:table]) -> any`
- **参数**：可选参数 `Services`（table 类型）指定写入服务的表名。该表含一列，记录当前导出的所有服务；子表包含导入该服务的所有 importer 以及 Exporter 为其提供的服务数量（integer）。
- **返回值**：若未指定可选参数，返回一个数组，包含当前导出的服务。
- **示例**：
  ```simtalk
  MyExporter.getExportedServices(MyExportedServicesTable)
  MyExporter.getExportedServices         // returns an array
  print MyExporter.getExportedServices   // might return [Job1]
  ```
- **参见**：Services [SimTalk] - Exporter、Services [Exporter]、Exported Services [Exporter]、Exported Services [Worker]

### getImporters [SimTalk]

返回 Exporter/Worker 当前正在为其履行订单的所有 importer。

- **类型**：Method
- **语法**：`<Path>.getImporters([Importers:table]) -> any`
- **参数**：可选参数 `Importers`（table 类型）指定写入 importer 的表名。该表包含两列：
  - 第 1 列（object 类型）：当前 Exporter 正在为其履行订单的所有 importer。
  - 第 2 列（integer 类型）：表示类型，`0` 为 failure/remove failure-importer，`1` 为 set-up-importer，`2` 为 processing-importer，`3` 为 transport-importer。
- **返回值**：若未指定可选参数，返回一个数组，包含当前导入该 Exporter/Worker 的已分配对象。
- **示例**：
  ```simtalk
  MyExporter.getImporters(MyImportersTable)
  MyExporter.getImporters         // returns an array
  print MyExporter.getImporters   // might return
  [*.Models.MyProcessingAndSetupBroker.Station3]
  ```
- **参见**：Importers [Exporter]、Importers [Worker]

### hasService [SimTalk]

返回 Exporter/Worker 是否支持指定服务。

- **类型**：Method
- **语法**：`<Path>.hasService(ServiceName:string) → boolean`
- **参数**：`ServiceName`（string 类型）指定服务名称。
- **返回值**（boolean）：支持返回 `true`，不支持返回 `false`。
- **示例**：
  ```simtalk
  MyExporter.hasService("drill")
  ```
- **参见**：Services [SimTalk] - Exporter、Services [Exporter]、Exported Services [Exporter]、Exported Services [Worker]

## 4. 只读属性（Read-Only Attributes）

Exporter 提供的只读属性包括：

- 左侧目录中列出的只读属性
- 所有对象通用只读属性（Read-Only Attributes of All Objects）
