# Source 对象属性（Attributes of the Source）

本目录汇总了 Plant Simulation 中 **Source（源）** 对象的属性说明。Source 是物料流对象（Material Flow Object），用于在生产系统中产生 MU（可移动单元，即零件/工件）。

## 目录内容

- `attributes.md` — Source 对象的属性详细说明（Markdown 格式）
- `attributes.txtx` — 与 `attributes.md` 内容一致的纯文本版本
- `Plant-Simulation-Help2606_4547-4566.pdf` — 对应的 Plant Simulation Help 帮助文档原始页面

> 注：本目录无子文件夹，因此没有需要额外汇总的子目录 README 内容。

## 属性概览

Source 对象提供以下属性（此外还继承 **所有对象的属性** 和 **物料流对象的属性**）：

| 属性 | 类型 | 数据类型 | 说明 |
|------|------|----------|------|
| `CurrentBatchNumber` | 只读属性 | `integer` | 返回最后创建零件的批号 |
| `Blocking` | 属性 | `boolean` | 设置 Source 是否保存本应生产下一个 MU 的时间 |
| `CreationTableActive` | 属性 | `boolean` | 设置 Source 是否将仿真运行中产生 MU 的所有事件写入表格 |
| `GenerateAsBatch` | 属性 | `boolean` | 设置 Source 是否一次性成批生产 MU |
| `Interval` | 属性 | `time` | 设置 Source 生产 MU 的时间间隔 |
| `MUSelection` | 属性 | `string` | 设置 Source 如何选择要生产的 MU |
| `Number` | 属性 | `integer` | 设置 Source 生产的 MU 数量 |
| `Path` | 属性 | `string` / `object` | 设置交货清单、序列表、频率表或 MU 类的路径 |
| `Start` | 属性 | `time` | 设置 Source 开始生产 MU 的仿真时间 |
| `Stop` | 属性 | `time` | 设置 Source 停止生产 MU 的仿真时间 |
| `TimeOfGeneration` | 属性 | `string` | 设置 Source 生产新 MU 的方式 |
| `Trigger` | 属性 | `array` | 设置或返回 Source 内部的 Trigger 列表 |

## 各属性详细说明

### 1. CurrentBatchNumber（只读属性）

返回最后创建零件的批号：

- 若 `GenerateAsBatch` 为 `true`，返回最后创建零件的**批号**；
- 若 `GenerateAsBatch` 为 `false`，返回已创建的**零件数量**。

```simtalk
print MySource.CurrentBatchNumber
```

### 2. Blocking

设置 Source 是否保存其本应生产下一个 MU 的时间：

- `true`：Source 在下一个可能的时刻（即阻塞的 MU 被后继对象移走时）生产后续 MU；
- `false`：Source 仅在设定的创建时间创建下一个 MU。

```simtalk
MySource.Blocking := true
```

### 3. CreationTableActive

设置 Source 是否将仿真运行期间产生 MU 的所有事件写入表格。开启后，Source 会在常规资源统计之外额外记录创建事件。

```simtalk
MySource.CreationTableActive := true
```

### 4. GenerateAsBatch

设置 Source 是否一次性成批生产 MU：

- `true`：在给定开始时间一次性生产整套零件，并尝试以单个批次将所有零件移入下一对象；
- `false`：逐个单独生产零件。

> 该设置适用于 MU 选择（MU Selection）为 **Sequence Cyclical、Sequence、Random、Percentage** 的情况。
> 若 MU 选择为 **Number Adjustable** 且激活 `Generate as Batch`，则 **Amount（数量）** 表示的是**批次数**而非零件数。

```simtalk
MySource.GenerateAsBatch := true
```

### 5. Interval

设置 Source 生产 MU 的时间间隔，其行为取决于 `TimeOfGeneration` 设置：

- **Time of Creation > Interval Adjustable（间隔可调）**：
  - `Interval` 设置两次创建事件之间经过的时间（可指定分布或常量 `Const`）；
  - `Start` 设置开始生产的仿真时间；
  - `Stop` 设置停止生产的仿真时间，`Stop = 0` 表示无限生产。
- **Time of Creation > Number Adjustable（数量可调）**：
  - 可指定概率分布来确定创建时刻，或指定常量时间让 Source 在单个时间点创建所有 MU。

```simtalk
MySource.TimeOfCreation := "Interval adjustable"
MySource.Start := 3600
MySource.Stop := str_to_time("1:00:00:00.00")
MySource.Interval.setTypeAndAttr("Normal", 1, 500, 100, 200, 900)
```

### 6. MUSelection

设置 Source 如何选择要生产的 MU。取值：

`"Constant"`、`"Sequence Cyclical"`、`"Sequence"`、`"Random"`、`"Percentage"`、`"Order Controlled"`

> 根据具体设置，`Path` 属性会指向交货清单、序列表、频率表或 MU 类。要使用 DataTable 的副本而非引用，可将子表命名为 `.unshare`。

```simtalk
MySource.MUSelection := "Sequence"
```

### 7. Number

设置 Source 生产的 MU 数量（仅适用于 **Number Adjustable** 和 **Interval Adjustable**）：

- 若 Interval Adjustable 未设置 Stop 时间，则最多生产所填数量的零件；默认值 `-1` 表示无限生产；
- 若设置了 Stop 时间，则生产持续到 Stop 时间，忽略所填数量；
- 激活 `Generate as Batch` 时，可能生产多于设定数量的零件（批次必须完整生产）；
- Number Adjustable 且激活 `Generate as Batch` 时，该值表示**批次数**。

```simtalk
MySource.Number := 5
```

### 8. Path

设置交货清单、序列表、频率表或 MU 类的路径（取决于 `TimeOfGeneration` 和 `MUSelection` 设置）。

> 在仿真期间分配交货表（Delivery Table）时，Source 不会生产创建时间在未来（尚未到达）的零件。

```simtalk
MySource.Path := "MyDeliveryTable"
```

### 9. Start

设置 Source 开始生产 MU 的仿真时间（当 `TimeOfGeneration` 设为 Interval Adjustable 时生效）。配合 `Interval`（生产间隔）与 `Stop`（停止时间，0 表示无限）使用。

```simtalk
MySource.TimeOfGeneration := "Interval adjustable"
MySource.Start := 3600
MySource.Stop := str_to_time("1:00:00:00.00")
MySource.Interval.setTypeAndAttr("Normal", 500, 100, 200, 900)
```

### 10. Stop

设置 Source 停止生产 MU 的仿真时间：

- `Stop = 0` 表示无限生产；
- 配合 `Start`（开始时间）与 `Interval`（生产间隔）使用。

```simtalk
MySource.TimeOfGeneration := "Interval adjustable"
MySource.Start := 3600
MySource.Stop := str_to_time("1:00:00:00.00")
MySource.Interval.setTypeAndAttr("Normal", 500, 100, 200, 900)
```

### 11. TimeOfGeneration

设置 Source 生产新 MU 的方式。取值：

`"Interval Adjustable"`、`"Number Adjustable"`、`"Delivery Table"`、`"Trigger"`

> 在仿真期间分配交货表时，Source 不会生产创建时间在未来的零件。
> Plant Simulation 按行处理交货表，因此时间应逐行递增；若处理到时间位于过去的行，零件会被立即创建。

```simtalk
MySource.TimeOfGeneration := "number adjustable"
MySource.TimeOfGeneration := "delivery table"
MySource.Path := MyDeliveryTable
```

### 12. Trigger

设置或返回 Source 内部的 Trigger 列表。

```simtalk
var assignedTriggers: object[2]
for var j := 1 to 2
   assignedTriggers[j] := to_str("Trigger", j)
next
Source.Trigger := assignedTriggers     -- 设置 trigger 列表
print MySource.Trigger                 -- 获取 trigger 列表
-- [*.Models.Model.Trigger, *.Models.Model.Trigger2]
```

## 通用说明

- 可通过对象对话框中的复选框、文本框、下拉列表，或直接为属性赋值来**设置/获取**属性值。
- 设置属性值示例：`MySource.GenerateAsBatch := true`
- 获取属性值示例：`print MySource.GenerateAsBatch`、`posit := MyStation.Cont.XPos`
- 查看对象的全部方法、只读属性和属性：在类库上下文菜单选择 **Show Attributes and Methods**，或选中实例后按 **F8** / 点击 Home 功能区选项卡上的 **Show Attributes and Methods**。
