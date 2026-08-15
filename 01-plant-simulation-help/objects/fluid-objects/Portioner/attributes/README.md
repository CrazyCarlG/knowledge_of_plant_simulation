# Portioner 属性（Attributes）汇总

本目录包含 Portioner 对象的属性文档，源文件为 `attributes.md`（及同内容的文本导出 `attributes.txtx`）。

## 概述

Portioner 提供的属性包括：

- 本页列出的属性（见下表）。
- 流体对象（Fluid Objects）的 `_Attributes`。
- 所有对象（All Objects）的属性。

查看对象的全部方法、只读属性与属性：在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**（显示属性与方法），或在包含实例的 Frame 中按 **F8** / 点击 Home 功能区上的 **Show Attributes and Methods**。

属性的读写可通过对话框中的复选框、文本框、下拉列表完成，也可在 SimTalk 中直接赋值/读取，例如：

```simtalk
MyPortioner.AmountPerMU := 10      -- 设置属性值
print MyPortioner.AmountPerMU      -- 读取属性值
```

## 属性一览

| 属性 | 类型 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| `CurrentMaterial` | 只读属性 | `string` | 返回流入 Portioner 的当前物料（Current Material）。 |
| `AmountPerMU` | 属性 | `real` | 设置 Portioner 将物料转化为单个 MU 的物料量（单位：升）。 |
| `MUPath` | 属性 | `path` | 设置 Portioner 要创建的 MU 类型（可用预定义 MU 或自定义 MU）。 |
| `PredecessorNumber` | 属性 | `integer` | 设置向 Portioner 供料的前驱对象编号。 |

## 各属性语法与示例

### CurrentMaterial [SimTalk]

```simtalk
<Path>.CurrentMaterial → string
```

```simtalk
print MyPortioner.CurrentMaterial
```

- 类型：只读属性（Read-only attribute）
- 返回值类型：`string`
- 说明：物料名称不区分大小写（比较时可用 `~=` 运算符）。
- 参见：Current Material [Portioner]、Relational Operators

### AmountPerMU [SimTalk]

```simtalk
<Path>.AmountPerMU:real
```

```simtalk
MyPortioner.AmountPerMU := 10
```

- 类型：属性（Attribute）
- 可赋值数据类型：`real`
- 参见：Amount per MU [Portioner]

### MUPath [SimTalk]

```simtalk
<Path>.MUPath:path
```

```simtalk
MyPortioner.MUPath := .MUs.Container
```

- 类型：属性（Attribute）
- 可赋值数据类型：`path`
- 说明：可使用预定义 MU，也可为此专门创建自己的 MU。
- 参见：MU [Portioner]

### PredecessorNumber [SimTalk]

```simtalk
<Path>.PredecessorNumber:integer
```

```simtalk
MyPortioner.PredecessorNumber := 2
```

- 类型：属性（Attribute）
- 可赋值数据类型：`integer`
- 参见：Fluid from Predecessor [text box]、DePortioner

## 相关对象

- **DePortioner**：与 Portioner 相反，用于清空进入的散装物料/流体部件，将其转化为流体并送入 Pipe。定义流体的三种方式之一是通过固定物料与每个 MU 的固定量（对应 **Material** 与 **Amount per MU** 设置）。
