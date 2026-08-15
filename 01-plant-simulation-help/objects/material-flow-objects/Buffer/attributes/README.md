# Buffer 属性（Attributes）汇总

本目录包含 Buffer（缓冲区）对象的属性文档。原始文档为 `attributes.md`（另有一份 `attributes.txtx` 为同内容的纯文本提取版本，非 Markdown）。以下为内容总结。

## 概述

Buffer 对象提供以下属性来源：

- 本目录表中所列的属性（`BufferType`、`Capacity`）。
- 所有对象的通用属性（Attributes of All Objects）。
- 物料流对象的通用属性（Attributes of the Material Flow Objects）。

## 查看属性与方法

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的属性与方法。
- 在插入了实例的 Frame 中，按 **F8** 键或点击 Home 功能区的 **Show Attributes and Methods**，可查看所选实例的属性与方法。

查询只读属性示例：

```simtalk
print MyBuffer.NumChildren
```

## 读取与设置属性值

可通过对话框中的复选框、文本框、下拉列表，或直接为属性赋值来设置/获取属性值。

设置属性值：

```simtalk
Buffer.BufferType := "Queue"
```

获取属性值：

```simtalk
print Buffer.BufferType
posit := MyStation.Cont.XPos
```

## 属性列表

### BufferType

- **类型**：Attribute
- **语法**：`<Path>.BufferType:string`
- **说明**：设置 Buffer 的类型。
  - `"Queue"`：先进先出（FIFO），MU 按进入顺序离开。
  - `"Stack"`：后进先出（LIFO），最后进入的 MU 最先离开。
- **示例**：`Buffer.BufferType := "Queue"`

### Capacity

- **类型**：Attribute
- **语法**：`<Path>.Capacity:integer`
- **可监视（Watchable）**：是
- **说明**：设置 Buffer 的容量，即可容纳 MU 的最大数量。
  - 容量不以矩阵实现，因此无法访问某个具体位置。
  - 仅当新容量大于等于当前 Buffer 内实际 MU 数量时，才能减小容量。
  - 值 `-1` 表示无限容量。
- **示例**：`Buffer.Capacity := 12`

## 相关对象

### Sorter

使用 Sorter 对象可依据不同排序标准对零件进行排序。

- MU 按设定的优先级离开 Sorter，优先级最高的零件最先移出（与进入时间无关）。
- 优先级由排序标准（Sort Criterion）与排序顺序（Sort Order）共同定义；排序标准的数据类型必须为 `real` 或可转换为 `real`。

排序标准可以是：

- 占用时间（Occupation time）
- MU 属性（MU-Property）
- 方法（Method）

排序顺序：

- **降序（Descending）**：按排序标准值最高者优先移出。
- **升序（Ascending）**：按排序标准值最低者优先移出。

Sorter 在以下情况下重新排序：

- 有新的 MU 进入时。
- 因访问而导致其内容变化时。

其他说明：

- 若仅在 MU 进入时排序，Plant Simulation 假设排序标准在 MU 停留期间不变，此时新 MU 会被插入现有顺序中。
- 若排序标准随时间变化（如 Transporter 的电量），则在内容每次变化时（尤其是 MU 移出前）重新排序。
- 若 MU 没有排序标准或其数据类型无法转换为 `real`，则该 MU 在对象上的顺序未定义；多个 MU 排序标准值相同时，彼此顺序亦未定义。

Sorter 提供替代图形：在 3D 窗口中点击 **Exchange Graphics** 选择替代图形。
