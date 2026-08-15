# Attributes of the Fluid Objects（流体对象的属性）

本目录整理 Plant Simulation 中**流体对象（Fluid Objects）的属性（Attributes）**文档，对应源文件 [attributes.md](./attributes.md)（其原始导出文本见 `attributes.txtx`）。本目录没有子文件夹，因此没有其他子目录 `README.md` 需要汇总。

## 概述

所有流体对象都具有**可设置（set）、可查询（query）**的属性（attributes）。一个属性对应对象某个选项卡上的对话框项、复选框或下拉列表命令等。

流体对象提供：

- 本目录（左侧目录）中列出的属性。
- Importer 的属性（_Attributes of the Importer）。
- 所有对象（All Objects）共有的属性（Attributes of All Objects）。

各流体对象各自的子章节中还会列出该对象额外添加的属性。

属性的值既可以通过对话框中的复选框、文本框和下拉列表设置，也可以通过给相应属性赋值来设置或获取。

### 查看方式

通过 **Show Attributes and Methods** 窗口可查看对象的所有方法（methods）、只读属性（read-only attributes）和属性（attributes）：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选**类（Class）**的方法、只读属性和属性。
- 按 **F8** 键，或点击 Frame 中 **Home** 功能区选项卡上的 **Show Attributes and Methods**，查看所选**实例（Instance）**的方法、只读属性和属性。

### 设置 / 获取示例

- 设置属性值，例如：

```simtalk
MyMixer.EntranceLocked := true
```

- 获取属性值，例如：

```simtalk
print MyMixer.EntranceLocked
posit := MyStation.Cont.XPos
```

## 属性一览

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| `ResWorking` | 只读属性（`boolean`） | 返回 `<Path>` 指定的流体对象是否处于 Working（工作）状态（`true`）或否（`false`） |
| `EntranceLocked` | 属性（`boolean`） | 锁定（`true`）或解锁（`false`）`<Path>` 指定的流体对象的入口 |
| `ExitLocked` | 属性（`boolean`） | 锁定（`true`）或解锁（`false`）`<Path>` 指定的流体对象的出口 |
| `RandomSeed` | 属性（`integer`） | 设置随机数种子值，与 EventController 的 Random Numbers Variant 一起用于生成流体对象的随机数 |
| `SetupTime` | 属性（`time`） | 设置 `<Path>` 指定的流体对象的设置（Set-up）时间长度 |

### 各属性说明

#### `ResWorking [SimTalk]` — fluid objects

返回流体对象是否处于 Working 状态。

- **类型：** 只读属性（Read-only attribute）
- **语法：** `<Path>.ResWorking → boolean`
- **返回值：** 数据类型为 `boolean`

```simtalk
print MyMixer.ResWorking
```

#### `EntranceLocked [SimTalk]` — fluid objects

锁定（`true`）或解锁（`false`）流体对象的入口。

- **备注：** 也可通过 **Entrance Locked** 复选框锁定或解锁入口。
- **类型：** 属性（Attribute）
- **语法：** `<Path>.EntranceLocked:boolean`
- **赋值：** 可赋 `boolean` 类型的值

```simtalk
MyMixer.EntranceLocked := true
```

- **SimTalk：** `EntranceFree [SimTalk]`
- **参见：** Entrance Locked [fluid objects]

#### `ExitLocked [SimTalk]` — fluid objects

锁定（`true`）或解锁（`false`）流体对象的出口。

- **备注：** 也可通过 **Exit Locked** 复选框锁定或解锁出口。
- **类型：** 属性（Attribute）
- **语法：** `<Path>.ExitLocked:boolean`
- **赋值：** 可赋 `boolean` 类型的值

```simtalk
MyMixer.ExitLocked := true
```

- **参见：** Exit Locked [fluid objects]

#### `RandomSeed [SimTalk]` — fluid objects

设置随机数种子值，与 EventController 的 Random Numbers Variant 一起用于生成流体对象的随机数。

- **备注：**
  - 向模型中插入对象时，Plant Simulation 会自动为该对象分配随机数种子值。可用函数 `setRandomSeedCounter(0)` 查询下一个被分配的随机种子值；对象创建后，Plant Simulation 将该计数器加 1，使下一个对象获得不同的随机种子值。
  - 若为两个对象分配相同的随机数种子值，这两个对象将生成相同的随机数序列（例如使用分布的加工时间等）。
- **注意：** 种子值影响流体对象用于 Set-up Time 及其他时间的随机数流，也影响故障概况（failure profiles）以及数据类型为 `RandTime` 的用户自定义属性的随机数流。Plant Simulation 会确保所有这些随机数流以不同方式初始化。因此，修改属性 `RandomSeed` 会导致流体对象的随机数流以及所有故障概况和用户自定义属性的随机数流生成新的随机数序列，且所有这些流将生成不同的序列。
- **类型：** 属性（Attribute）
- **语法：** `<Path>.RandomSeed:integer`
- **赋值：** 可赋 `integer` 类型的值

```simtalk
MyMixer.RandomSeed := 40
```

- **SimTalk：** `IncrementRandomNumbersVariantOnReset [SimTalk]`、`setRandomSeedCounter [SimTalk]`
- **参见：** Simulating Random Processes、Random Seed Value、Increment Variant on Reset of the EventController、Random Numbers Variant of the EventController、Data Types [SimTalk]

#### `SetupTime [SimTalk]` — fluid objects

设置流体对象的设置（Set-up）时间长度。

- **备注：**
  - 当下一个物料的名称与其前一个物料的名称不同时，流体对象必须进行设置（set up）。
  - 设置时间是将对象设置为处理不同类型物料所需的时间。名称相同表示物料类型相同。
- **类型：** 属性（Attribute）
- **语法：** `<Path>.SetupTime:time`
- **赋值：** 可赋 `time` 类型的值

```simtalk
MyMixer.SetupTime := 120 // 2 minutes
```

- **参见：** Set-up Time [general description]、Times and Distributions、Pipe

## 相关：流体对象的只读属性（Read-Only Attributes）

流体对象还提供**只读属性（read-only attributes）**，其值只能查询（query），不能设置（set）。相关内容参见同级的 [read-only-attributes](../read-only-attributes/README.md) 目录。

## 相关：流体对象的方法（Methods）

流体对象提供所有对象的方法（The Methods of All Objects）、定义故障的方法（The Methods for Defining Failures）以及 Importer 的方法（The Methods of the Importer）。相关内容参见同级的 [methods](../methods/README.md) 目录。

## 相关：流体对象的通用共享属性（General）

流体对象共享的对话框项、菜单与通用说明参见同级的 [general](../general/README.md) 目录。
