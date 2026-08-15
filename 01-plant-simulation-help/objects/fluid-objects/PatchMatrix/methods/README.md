# PatchMatrix Methods

本目录（`methods`）汇总了 Plant Simulation 中 **PatchMatrix**（流体对象）的方法（Methods）、只读属性（Read-Only Attributes）和属性（Attributes）的说明。目录内包含 `methods.md` 与 `methods.txtx` 两个内容一致的文档，无子文件夹及子 README。

## 概述

PatchMatrix 提供：

- 左侧目录中列出的方法。
- 流体对象（Fluid Objects）的方法。
- 所有对象（All Objects）的方法。

查看对象全部方法、只读属性和属性的方式：打开 **Show Attributes and Methods** 窗口。可通过类库右键菜单或实例所在 Frame 的 Home 选项卡（或按 F8）打开。

## 语法阅读说明

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所应用对象的路径。
- 括号内为方法签名（标识符 + 参数数据类型），参数可用常量、相应类型变量或返回相应类型的方法替代。
- 方括号 `[…]` 表示可选参数。
- `:= false` 表示参数默认值。
- 箭头 `→` 后为返回值数据类型。

> **注意**：表达式中嵌套括号时务必正确输入 `(…)`，否则可能产生意外结果并打开调试器。

## 方法列表

### getConnectionsForPred [SimTalk]

返回 `<Path>` 指定的 PatchMatrix 中与指定前驱（predecessor）存在连接的后继（successor）编号。

- **类型**：Method
- **语法**：`<Path>.getConnectionsForPred(Pred:integer) → array`
- **参数**：`Pred`（integer）— 前驱编号。
- **返回值**：array。

```simtalk
var c : integer[ ]
c := Patchmatrix.getConnectionsForPred(1)
```

### getConnectionsForSucc [SimTalk]

返回 `<Path>` 指定的 PatchMatrix 中与指定后继（successor）存在连接的前驱（predecessor）编号。

- **类型**：Method
- **语法**：`<Path>.getConnectionsForSucc(Succ:integer) → array`
- **参数**：`Succ`（integer）— 后继编号。
- **返回值**：array。

```simtalk
var c : integer[ ]
c := Patchmatrix.getConnectionsForSucc(1)
```

### resetConnections [SimTalk]

重置 `<Path>` 指定的 PatchMatrix 与其前驱/后继之间的现有连接，即切断连接。

- **类型**：Method
- **语法**：`<Path>.resetConnections`

```simtalk
Patchmatrix.resetConnections
```

### setConnections [SimTalk]

建立或切断 `<Path>` 指定的 PatchMatrix 前驱与后继之间的连接（`connect` 为 true 时连接，false 时切断）。

- **类型**：Method
- **语法**：`<Path>.setConnections(Pred:any, Succ:any, connect:boolean) → array`
- **参数**：
  - `Pred`（any）— 前驱，可为编号、名称或编号数组。
  - `Succ`（any）— 后继，可为编号、名称或编号数组。
  - `connect`（boolean）— 是否连接 Pipe（true 连接，false 断开）。

```simtalk
Patchmatrix.setConnections(1,2,true)
Patchmatrix.setConnections(1,[1,2],true)
Patchmatrix.setConnections("PipeIn1","PipeOut2",false)
```

## 只读属性（Read-Only Attributes）

PatchMatrix 提供流体对象及所有对象的只读属性。只读属性可查询但不可设置——其值由 Plant Simulation 在查询时点计算得出；多数只读属性对应对象某选项卡（如 Statistics）上不可用的对话框项。

查询示例：

```simtalk
print MyPatchMatrix.UUID
```

## 属性（Attributes）

PatchMatrix 提供左侧目录中列出的方法、只读属性及属性。

## 相关链接

- Connections [PatchMatrix]
- 各方法间互见：getConnectionsForPred / getConnectionsForSucc / setConnections / resetConnections
