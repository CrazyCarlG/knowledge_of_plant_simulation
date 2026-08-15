# 模型调试函数（Functions for Debugging the Model）

本目录收录 SimTalk 中用于调试仿真模型的相关函数。这些函数主要用于在仿真运行期间中断、检查、终止或配置错误处理与资源限制行为。

> 来源：Plant Simulation 帮助文档 `model-debugging.md`（对应原始文件 `model-debugging.txtx`）。

## 函数总览

| 函数 | 用途 | 返回类型 |
| --- | --- | --- |
| `make2DimArray` | 由一维数组创建二维数组 | `any[]`（二维数组） |
| `clearAllBreakpoints` | 删除所有类断点和实例断点 | — |
| `debug` | 停止仿真并打开调试器窗口 | — |
| `deleteSuspendedMethods` | 终止所有被挂起的方法 | — |
| `getErrorStop` | 读取"公式出错即停 / 错误处理器出错即停"设置 | `boolean` |
| `ignoreBreakpoints` | 忽略（或不忽略）用户自定义断点 | — |
| `setErrorHandler` | 设置全局错误处理方法 | `object` |
| `setErrorStop` | 激活/关闭"公式出错即停 / 错误处理器出错即停" | `boolean` |
| `setMaxDepthOfCalls` | 设置方法调用深度上限 | `integer` |
| `setMaxEdgeLengthWorkerRouteNetwork` | 设置工人路径网络最大边长 | `length` |
| `setMaxNumberOfCallChains` | 限制最大调用链数量 | `integer` |
| `setMaxNumberOfSamples` | 设置最大抽样次数 | `integer` |
| `setMaxSuspendedMethods` | 设置最大挂起方法数 | `integer` |

## 函数详细说明

### make2DimArray
由指定的一维数组的值创建一个二维数组。

- **语法：** `make2DimArray(xDim:integer, arrayData:any[]) -> any[xDim,*]`
- **参数：**
  - `xDim`（`integer`）：待创建数组的 X 维度；Y 维度由 Plant Simulation 根据一维数组的值自动确定。
  - `arrayData`（`any[]`）：用于填充二维数组的值。
- **返回值：** `any[]`，与原始一维数组具有相同基础数据类型的二维数组。

### clearAllBreakpoints
删除仿真模型中所有 Method 里已设置的全部类断点和实例断点。

- **语法：** `clearAllBreakpoints`

### debug
停止仿真运行并打开调试器窗口。当模型中存在错误时，可中断仿真运行并进行调试。

- **语法：** `debug`

### deleteSuspendedMethods
终止所有被挂起的方法，即被 `waituntil`、`stopuntil` 语句或 `sleep` 指令挂起的方法。

- **语法：** `deleteSuspendedMethods([WaitingToo:boolean:=false, OnlyLocal:boolean:=false])`
- **说明：**
  - 不删除 Method 对象本身，仅终止其挂起状态。
  - EventController 在仿真复位阶段会自动终止所有被挂起的方法。
- **参数：**
  - `WaitingToo`（`boolean`，可选）：是否同时删除被 `wait` 指令挂起的方法（默认 `false`）。
  - `OnlyLocal`（`boolean`，可选）：是否只删除根 Frame 或其子 Frame 内的本地挂起（默认 `false`）。

### getErrorStop
读取 **Stop on Formulas**（公式出错即停）与 **Stop on Error Handlers**（错误处理器出错即停）两项设置，并写入传入变量。

- **语法：** `getErrorStop(byRef StopOnErrors:boolean, byRef StopOnErrorsInFormulas:boolean) → boolean`
- **参数：**
  - `StopOnErrors`：写入"Stop on Error Handlers"是否激活。
  - `StopOnErrorsInFormulas`：写入"Stop on Formulas"是否激活。
- **返回值：** `boolean`

### ignoreBreakpoints
在仿真运行期间忽略（`true`）或不忽略（`false`）用户自定义断点。

- **语法：** `ignoreBreakpoints(Ignore:boolean)`
- **参数：** `Ignore`（`boolean`）

### setErrorHandler
将指定 Method 设为全局错误处理方法。

- **语法：** `setErrorHandler(Method:object) → object`
- **说明：**
  - 设置全局错误处理方法后，SimTalk 方法发生运行时错误时不会打开 Method Debugger，而是终止整个调用链（出错方法及其所有调用方法）并调用全局错误处理方法。
  - 仅当没有为方法设置单独的错误处理时，才会调用全局错误处理方法。
  - 设置为 `void` 时，关闭全局错误处理，运行时错误且无单独错误处理时打开调试器。
  - 错误处理方法会收到三个参数：错误消息字符串（须声明为 by reference）、出错方法路径字符串、出错行号整数。
- **返回值：** `object`，返回上一次注册的错误处理方法。

### setErrorStop
激活（`true`）或关闭（`false`）**Stop on Formulas** 与 **Stop on Error Handlers** 功能。

- **语法：** `setErrorStop(StopAfterError:boolean[, StopAfterErrorInFormula:boolean]) → boolean`
- **参数：**
  - `StopAfterError`：为 `true` 时，当前方法出错后停止仿真并打开调试器、高亮出错行；关闭调试器后终止整个调用链；若事件列表还有事件则继续仿真。为 `false` 时直接终止调用链并继续仿真。
  - `StopAfterErrorInFormula`（`boolean`，可选）：是否在公式出错时停止仿真。
- **返回值：** `boolean`

### setMaxDepthOfCalls
设置 Plant Simulation 可调用的方法数量（调用深度）。

- **语法：** `setMaxDepthOfCalls(NumberOfMethods:integer) → integer`
- **说明：** 每个方法在执行期间占用内存，嵌套调用会增加内存占用，默认值 500 对多数应用已足够。
- **返回值：** `integer`，返回先前的最大值；传入 0 时不设置新值。

### setMaxEdgeLengthWorkerRouteNetwork
设置 **Maximum Edge Length**（最大边长）。计算工人路径网络时，仅使用小于等于该值的线段。

- **语法：** `setMaxEdgeLengthWorkerRouteNetwork(newMaxEdgeLength:length) -> length`
- **说明：** 可输入 3 到 100 米之间的值，作用于所有方向；0 表示不限制边长。适用于在模型区域内自由行走的工人的路径网络计算。
- **返回值：** `length`，返回先前的模型设置值。

### setMaxNumberOfCallChains
限制 Plant Simulation 调用的 **Maximum Number of Call Chains**（最大调用链数量）。

- **语法：** `setMaxNumberOfCallChains(NumberOfCallChains:integer) → integer`
- **说明：** 达到设定数量后停止仿真并显示错误消息，可增加该值后继续仿真。
- **返回值：** `integer`，返回先前的最大值；传入 0 时不设置新值。

### setMaxNumberOfSamples
设置 **Maximum Number of Samples**（最大抽样次数），避免因区间边界选择不当导致掷骰子（随机数抽取）耗时过长。

- **语法：** `setMaxNumberOfSamples(NumberOfSamples:integer) → integer`
- **说明：** 可取 1 到 32000 之间的值；超出范围的值被忽略且保留原值。值越大，越晚发现区间边界过近。
- **返回值：** `integer`，返回先前的最大值；传入 0 时不设置新值。

### setMaxSuspendedMethods
设置任意时刻可挂起方法的最大数量（限制由 `waituntil` 语句挂起的方法数量）。

- **语法：** `setMaxSuspendedMethods(NumberOfSuspendedMethods:integer) → integer`
- **说明：** 达到设定数量后，额外方法不再挂起并显示错误消息，可增加该值继续仿真或停止仿真修复建模错误。
- **返回值：** `integer`，返回先前的最大值；传入 0 时不设置新值。
