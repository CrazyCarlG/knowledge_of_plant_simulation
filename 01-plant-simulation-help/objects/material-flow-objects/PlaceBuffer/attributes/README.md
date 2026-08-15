# PlaceBuffer — Attributes（属性）总结

本目录存放 **PlaceBuffer（暂存区/缓冲区工位）** 对象的属性（Attributes）相关文档，内容来源于 Siemens Plant Simulation Help（11-2068 / 11-2069）。本 README 是对 `attributes.md`（`attributes.txtx` 为其原始提取文本，两者内容一致）的总结。

## 内容来源

目录内包含以下文件：

- `attributes.md` — 属性页面的 Markdown 版总结（本 README 的依据）。
- `attributes.txtx` — 从 Plant Simulation 帮助 PDF 提取的原始文本。

## 1. 概述

**PlaceBuffer** 提供：

- 左侧目录（table of contents）中列出的属性；
- 所有对象的属性（Attributes of All Objects）；
- 物料流对象的属性（Attributes of the Material Flow Objects）。

要查看对象的全部方法、只读属性和属性，打开 **Show Attributes and Methods（显示属性与方法）** 窗口：

- 在 **类库（Class Library）** 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选**类（Class）** 的方法、只读属性与属性。
- 在插入实例的 **Frame** 中按 **F8** 键，或点击 **Home** 功能区选项卡上的 **Show Attributes and Methods**，可查看所选**实例（Instance）** 的方法、只读属性与属性。

属性的值既可以通过对话框窗口中的复选框、文本框和下拉列表设置/获取，也可以通过为相应属性赋值来设置/获取：

- **设置属性值**，例如：

```simtalk
MyPlaceBuffer.Accumulating := true
```

- **获取属性值**，例如：

```simtalk
print MyPlaceBuffer.Accumulating
posit := MyStation.Cont.XPos
```

## 2. 属性总览

| 属性 | 类型 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| `Accumulating` | 属性 | `boolean` | 设置当前驱 MU 无法离开时，后续 MU 可以继续向前移动（`true`）还是必须等待（`false`）。 |
| `Capacity` | 属性 | `integer` | 设置 PlaceBuffer 的容量，即工位（位置）数量。 |
| `SequentiallyIndexing` | 属性 | `boolean` | 设置仅当后继位置空闲时才启动某个位置上的加工时间。 |

## 3. 属性详解

### 3.1 Accumulating [SimTalk] — PlaceBuffer

设置由 `<Path>` 指定的 PlaceBuffer 中，当前驱 MU 无法离开时，后续 MU 可以继续向前移动（`true`）还是必须等待（`false`）。

- **类型：** Attribute（属性）
- **语法：** `<Path>.Accumulating:boolean`
- **可监视：** 该属性可监视（watchable）。
- **赋值：** 可赋数据类型 `boolean` 的值。

**备注：** 若当前驱部件无法离开且 `Accumulating` 为 `false` 时，不再有新的 MU 能进入 PlaceBuffer。

**示例：**

```simtalk
MyPlaceBuffer.Accumulating := true
```

**参见：** Accumulating [check box] - PlaceBuffer

---

### 3.2 Capacity [SimTalk] — PlaceBuffer

设置由 `<Path>` 指定的 PlaceBuffer 的容量（Capacity），即其工位（位置）数量。

- **类型：** Attribute（属性）
- **语法：** `<Path>.Capacity:integer`
- **可监视：** 该属性可监视（watchable）。
- **赋值：** 可赋数据类型 `integer` 的值。

**备注：**

- 当 `SequentiallyIndexing` 设置为 `false` 时，值 `-1` 表示无限容量。
- 可通过索引访问各个位置。
- 只有当足够多的位置为空时，才能减小容量。
- 当 PlaceBuffer 中有部件时无法更改容量；只有在它**为空**时才能更改。

**示例：**

```simtalk
MyPlaceBuffer.Capacity := 12
```

**参见：** SequentiallyIndexing [SimTalk]、Sequentially Indexing [check box]

---

### 3.3 SequentiallyIndexing [SimTalk]

设置由 `<Path>` 指定的 PlaceBuffer 中，某个位置上的加工时间（Processing Time）**仅当后继位置空闲时**才开始（`true`），否则不等待（`false`）。

- **类型：** Attribute（属性）
- **语法：** `<Path>.SequentiallyIndexing:boolean`
- **赋值：** 可赋数据类型 `boolean` 的值。

**备注：**

- 在 Sequentially Indexing（顺序索引）模式下，加工时间**不是**部件在某个位置上被加工的时间，而是把部件从当前位置移动到后继位置所用的时间。
- 若容量为 4，则部件在离开 PlaceBuffer 之前加工时间要经过**三次**，因为需要发生三次移动过程。
- 总时间可能因等待时间而变长。因此**最后一个位置不消耗时间**：部件一旦到达最后一个位置，只要后继能接受，即可立即离开。

**示例：**

```simtalk
MyPlaceBuffer.SequentiallyIndexing := true
```

**参见：** Sequentially Indexing [check box]

---

## 4. Buffer（对象）

**Buffer** 对象用于临时存放大量部件，然后将其传递给后继。

### 描述

在两个组件之间插入一个 Buffer：

- **临时存放部件** —— 当后续工位中某个组件发生故障时，避免前序机器停止生产。
- **继续传递部件** —— 当前序组件停止工作时，避免生产流程陷于停顿。

将 Buffer 的容量设置得足够大以覆盖所有故障，可使相关组件之间实现完全解耦。Buffer 不仅能够渡过故障时间，还可作为补偿站，吸收波动的运输时间和操作时间（这些波动会导致机器或组件前形成队列）。但即便如此，它也不能始终避免物料流中断或停摆。

由于 Buffer **没有独立的位置**，因此无需将加工时间（即部件停留在其中的时间）拆分为若干小步骤；取而代之，可以选择部件离开 Buffer 的顺序。

**Buffer Type [下拉列表]：**

- **Queue（队列）** —— 部件按进入顺序离开 Buffer（先进先出，FIFO）。
- **Stack（堆栈）** —— 最后进入的部件最先离开 Buffer（后进先出，LIFO）。

> **注意：** 每个 MU 在 Buffer 中至少停留所输入的 **Dwell Time [Buffer]**（驻留时间）这么久。对于 Buffer Type > Stack，只有当在其之后进入 Buffer 的所有部件都已离开（即该 MU 位于堆栈最顶端）时，它才能离开。

将鼠标悬停在 Buffer 上可显示包含其信息的工具提示。

---

## 5. 相关子文件夹说明

> 本目录（attributes）自身无子文件夹。PlaceBuffer 对象的其余文档位于**同级**子文件夹 `general`、`methods`、`read-only-attributes` 中，各 README.md 内容概述如下，便于交叉查阅：

- **`general/README.md`** —— PlaceBuffer 对象通用说明：对象概述（一排前后排列的缓冲位置、顺序推进、循环移动）、如何添加到仿真模型、对话框与各选项卡（Attributes、Times、Failures、Controls、Exit、Statistics、Energy、Costs、User-defined）、菜单、方法以及 SimTalk 示例。
- **`methods/README.md`** —— PlaceBuffer 的方法：方法 `pe` / `[X Y]`、语法行约定、方法 `pe(1) / [1]` 的详细说明（备注、语法、参数、默认值、返回值、示例），以及只读属性与属性的概述。
- **`read-only-attributes/README.md`** —— PlaceBuffer 的只读属性：只读属性只能查询不能赋值、查看属性与方法窗口的使用方式，以及属性（可读写）的设置/读取示例。

## 目录说明

- `attributes.md`：PlaceBuffer 属性说明的 Markdown 版本（本总结的源文件）。
- `attributes.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

---

*来源：Plant Simulation Help。未发表作品。© 2026 Siemens*
