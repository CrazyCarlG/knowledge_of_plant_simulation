# Read-Only Attributes of the Conveyor — 目录说明

本目录包含 Conveyor（传送带）对象的只读属性（Read-Only Attributes）文档。

## 目录内容

- `read-only-attributes.md` — Conveyor 只读属性的完整说明（详见下文总结）
- `read-only-attributes.txtx` — 同一文档的原始文本版本（Siemens Plant Simulation Help 导出内容）

## 内容总结

### 语法行约定（Syntax Line Conventions）

方法/属性的语法行示例如下：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：属性所作用对象的路径。
- 括号内为签名，含参数标识符与数据类型，例如 `(Parameter:string)`。
- 方括号 `[…]` 表示可选参数。
- `:= 默认值` 表示参数的默认值。
- 箭头 `→` 后为返回值的数据类型。

> 注意：表达式内的括号 `(…)` 必须输入，否则可能导致意外结果并打开调试器（Debugger）。

### 概述（Overview）

Conveyor 提供以下只读属性（此外还包括“所有对象的只读属性”与“物料流对象的只读属性”）：

- 只读属性的值**可以查询，但不能设置**，其值由 Plant Simulation 在查询时刻实时计算。
- 大多数只读属性对应对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。
- 查看全部方法/只读属性/属性：在类库上下文菜单或 Frame 的 Home 选项卡中点击 **Show Attributes and Methods**（或按 **F8**）。

查询示例：

```
print Conveyor.CurrentAcceleration
```

### 只读属性列表

#### CurrentAcceleration

返回 `<Path>` 指定的 Conveyor 的当前加速度或减速度。

- **类型**：只读属性
- **语法**：`<Path>.CurrentAcceleration → acceleration`
- **可监视（Watchable）**：可监视特殊值，例如检测 Conveyor 达到最终速度（Final Speed）的事件。
- **返回值**：数据类型 `acceleration`

**示例**

```
MyConveyor.CurrentAcceleration
```

#### OccupiedLength

返回 `<Path>` 指定的 Conveyor 整个长度（Length）中被其上所有 MU 占用的区段长度。

- **备注**：Conveyor 上的每个 MU 都占用整个可用长度的一部分。
- **类型**：只读属性
- **语法**：`<Path>.OccupiedLength → length`
- **返回值**：数据类型 `length`

**示例**

```
print Conveyor.OccupiedLength
```

**另请参见**：Length [text box] - Conveyor

## 相关文档

- Attributes of the Conveyor
- _Attributes of the Conveyor
