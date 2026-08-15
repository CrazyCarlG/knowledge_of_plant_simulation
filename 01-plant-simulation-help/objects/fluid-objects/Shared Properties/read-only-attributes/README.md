# Read-Only Attributes of the Fluid Objects（流体对象只读属性）

本目录整理 Plant Simulation 中**流体对象（Fluid Objects）的只读属性**文档。相关内容详见 [read-only-attributes.md](./read-only-attributes.md)。

## 概述

流体对象提供两类只读属性：

- 目录中列出的只读属性（下表）。
- 所有对象（All Objects）共有的只读属性。

只读属性的值**只能查询（query），不能设置（set）**——Plant Simulation 在你查询的时间点即时计算该值。大多数情况下，一个只读属性对应对象某个选项卡上不可用的对话框项（例如 **Statistics** 选项卡上的统计项）。

### 查看方式

通过 **Show Attributes and Methods** 窗口可查看对象的所有方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的信息。
- 在 Frame 中按 **F8**，或点击 Home 选项卡上的 **Show Attributes and Methods**，查看所选实例的信息。

### 查询示例

```simtalk
print MyMixer.ResWorking
```

## 语法约定

单个方法的 Syntax 行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所应用对象的路径。
- 签名（标识符和参数数据类型）写在括号内，如 `(Parameter:string)` 表示字符串参数。除常量外，也可使用所需类型的变量或返回该类型的方法。
- **注意**：嵌套表达式时务必输入括号 `(…)`，否则可能产生意外结果并打开调试器（Debugger）。
- 可选参数用方括号列出，如 `[,Parameter:boolean]`。
- 参数有默认值时，在参数后显示，如 `:= false`。
- 方法有返回值时，其数据类型显示在箭头 `→` 之后，如 `→ boolean`。

## 只读属性一览

| 属性 | 返回值类型 | 说明 | Watchable |
| --- | --- | --- | --- |
| `CurrentInFlowrate` | `real` | 流体对象当前的**入流速率**（每秒流入对象的物料升数） | 是 |
| `CurrentMaterialColor` | `real` | 流体对象当前的物料颜色 | 是 |
| `CurrentMaterialDensity` | `real` | 流体对象当前的物料密度 | 是 |
| `CurrentOutFlowrate` | `real` | 流体对象当前的**出流速率**（每秒流出对象的升数） | 是 |
| `CurrentWeight` | `real` | **DePortioner / Mixer / Portioner / Tank** 中当前物料的重量（单位见 *File > Model Settings > Unit > Mass*） | 否 |
| `ResBlocked` | `boolean` | 流体对象是否被阻塞（Blocked） | 否 |
| `ResCurrentState` | `string` | 流体对象当前的状态 | 是（可用于 `waituntil` 指令或让 `TimeSequence` 以 watch 模式记录） |
| `ResSetup` | `boolean` | 流体对象是否处于 Setting-up（且未 Failed/Paused/Stopped） | 否 |
| `ResWaiting` | `boolean` | 流体对象是否处于 Waiting | 否 |
| `ResWorking` | `boolean` | 流体对象是否处于 Working | 否 |

### `ResCurrentState` 可能的状态

仿真运行期间，物料流资源可能处于以下状态之一：

**Working、Setting-up、Waiting、Blocked、Failed、Stopped、Paused、Powering Up/down、Unplanned**

> **注意**：若两个状态同时发生（如 Paused 与 Failed），该只读属性返回在统计采集中具有优先级的状态（例如 Paused 与 Failed 同时发生时返回 Paused）。

## 相关：流体对象的属性（Attributes）

所有流体对象都具有可设置、可查询的**属性（attributes）**，属性对应对象选项卡上的对话框项（复选框、下拉命令等）。流体对象提供：

- 目录中列出的属性。
- Importer 的属性。
- 所有对象（All Objects）共有的属性。

属性的值既可以通过对话框中的复选框、文本框、下拉列表设置，也可以通过给相应属性赋值来设置/获取。
