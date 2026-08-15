# AssemblyStation — Attributes（属性）

本目录存放 **AssemblyStation**（装配站）对象的属性说明文档。内容来源为 `attributes.md`（`attributes.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. 概述

**AssemblyStation** 提供：

- 本目录列出的属性；
- 所有对象的属性（Attributes of All Objects）；
- 物料流对象的属性（Attributes of the Material Flow Objects）。

要查看对象的全部方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，查看所选**类**的成员；
- 在插入实例的 Frame 中按 **F8** 键，或点击 Home 功能区标签页的 **Show Attributes and Methods**，查看所选**实例**的成员。

属性的值既可以通过对话框窗口中的复选框、文本框和下拉列表设置/获取，也可以通过为相应属性赋值来设置/获取：

- **设置属性值**，例如：

```simtalk
MyAssembly.AssemblyMode := "attach MUs"
```

- **获取属性值**，例如：

```simtalk
print MyAssembly.Pause
posit := MyStation.Cont.XPos
```

## 2. 属性总览

| 属性 | 类型 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| `StatWaitingResTime` | 只读属性 | `time` | 返回 AssemblyStation 等待安装部件和/或 processing-Exporters/processing-services 的总时间。 |
| `AssemblyMode` | 属性 | `string` | 设置 AssemblyStation 如何将 MU 移出（装配到主要部件或删除）。 |
| `AssemblyTable` | 属性 | `table` | 设置包含安装部件的装配表。 |
| `AssemblyTableMode` | 属性 | `string` | 设置装配表的类型。 |
| `ExitingMU` | 属性 | `string` | 设置离开 AssemblyStation 的 MU 类型。 |
| `MainMU` | 属性 | `integer` | 设置从中拉取主要 MU 的前驱编号。 |
| `NewMU` | 属性 | `string` | 设置 AssemblyStation 删除主要 MU 并创建新 MU 时所创建 MU 的路径。 |
| `OrderSequence` | 属性 | `string` | 设置 AssemblyStation 请求 MU 和/或服务的顺序。 |
| `SequentialDelivery` | 属性 | `boolean` | 设置 Worker 是否逐个顺序递送安装部件。 |

## 3. 属性详解

### 3.1 StatWaitingResTime（只读属性）

返回 `<Path>` 所指定 AssemblyStation 等待安装部件和/或 processing-Exporters/processing-services 的**总时间**。

- **类型：** Read-only attribute（只读属性）
- **语法：** `<Path>.StatWaitingResTime → time`
- **返回值：** 数据类型为 `time`。

**示例：**

```simtalk
print MyAssembly.StatWaitingResTime
```

**参见：** `Waiting [state, material flow objects]`、`Statistics report, Waiting Times for Services and Parts`

---

### 3.2 AssemblyMode

设置 `<Path>` 所指定 AssemblyStation 如何将 MU 移出。

- **类型：** Attribute（属性）
- **语法：** `<Path>.AssemblyMode:string`
- **赋值：** 可赋数据类型 `string` 的值。
  - `"Attach MUs"`：将 MU 移动到主要部件上。
  - `"Delete MUs"`：删除 MU。

**示例：**

```simtalk
MyAssembly.AssemblyMode := "Attach MUs"
```

**参见：** `Assembly Mode [drop-down list]`

---

### 3.3 AssemblyTable

设置 `<Path>` 所指定 AssemblyStation 的包含安装部件的装配表。

- **类型：** Attribute（属性）
- **语法：** `<Path>.AssemblyTable:table`
- **赋值：** 可赋数据类型 `table` 的值。

**备注：** 根据 **Assembly Table**（或 `AssemblyTableMode`）所选设置的不同，需指定不同内容：

**None** — AssemblyStation 不使用装配表，而是期望每个前驱对象各提供一个部件。

**Predecessors（前驱）** — 在表中指定所需设置：

- 在第 1 列输入移动该部件的前驱编号，第 2 列输入 Amount（数量）；缺省值为 1，可不指定。
- Amount 输入 `-1`：使 AssemblyStation 接受该前驱的部件，直到主要 MU 容量被占满。若使用主要部件编号的部件作为安装部件，将主要 MU 编号加入装配表。
- 在 **Assembly Time** 列输入每个部件装配所消耗的时间（秒，须为正数或 0，缺省为 0）；在 **Sequence Number** 列输入装配顺序编号（须为正整数，缺省为 1）。
- 若**非顺序装配**，将 **Assembly Time** 与 **Sequence Number** 两列留空。

**MU Types** — 在表中指定所需设置：

- 在第 1 列输入部件的 MU 名称（如 Part、Container、Transporter、Shaft 等），第 2 列输入 Amount。
- 在 **MU Name** 列输入的是部件**名称**而非路径，例如 `MyMountingPart`，而非 `*.UserObjects.MyMountingPart`。
- Amount 缺省为 1；输入 `-1` 使 AssemblyStation 接受该 MU 名称的部件直到主要 MU 容量被占满。
- **Assembly Time** 与 **Sequence Number** 列同 Predecessors 设置。

**Depends on Main MU（取决于主要 MU）** — 在表中指定所需设置：

- 在第 1 列输入主要 MU 名称（如 Part、Container、Transporter、Shaft 等）。输入星号 `*` 处理所有未单独列出名称的主要部件；输入部件的 MU 名称与 Amount。
- Amount 缺省为 1；输入 `-1` 使 AssemblyStation 接受该 MU 名称的部件直到主要 MU 容量被占满。
- **Assembly Time** 与 **Sequence Number** 列同 Predecessors 设置。

> **注（MU Types 与 Depends on Main MU 适用）：** 若前驱为 Store 类型对象，AssemblyStation 会从 Store 请求所需安装部件；若部件暂缺，Store 会记录请求并在可用后送达。部件也可由 Worker 从 Store 搬运到 AssemblyStation。Store 只能提供安装部件（不能提供主要部件），且必须用 Connector 连接（即使由 Worker 搬运）。

**Fill up Main MU（填满主要 MU）** — AssemblyStation 不使用装配表，而是接受任意前驱的部件，直到主要 MU 容量被占满。

> **注：** **Predecessor** 与 **MU Name** 列不能包含重复条目。

> **注：** 若装配表被继承，写入装配表单元格时继承不会自动取消，因此赋值会修改被继承的表。要取消继承，可将装配表赋值给自身：

```simtalk
AssemblyStation.AssemblyTable := AssemblyStation.AssemblyTable  // 取消继承
```

**示例：**

```simtalk
var AssemblyTable: table[string,integer]
AssemblyTable.create
AssemblyTable.writeRow(1,1, "MyPartA",1)
AssemblyTable.writeRow(1,2, "MyPartB",2)
MyAssembly.AssemblyTable := AssyList
```

**参见：** `Assembly Table`

---

### 3.4 AssemblyTableMode

设置 `<Path>` 所指定 AssemblyStation 的装配表类型。

- **类型：** Attribute（属性）
- **语法：** `<Path>.AssemblyTableMode:string`
- **赋值：** 可赋数据类型 `string` 的值。
  - 可选 `"None"`、`"Predecessors"`、`"MUTypes"`、`"Depends on Main MU"` 或 `"Fill up Main MU"`。

**示例：**

```simtalk
MyAssembly.AssemblyTableMode := "Fill up Main MU"
```

**参见：** `Assembly Table`

---

### 3.5 ExitingMU

设置离开 `<Path>` 所指定 AssemblyStation 的 MU 类型。

- **类型：** Attribute（属性）
- **语法：** `<Path>.ExitingMU:string`
- **赋值：** 可赋数据类型 `string` 的值。
  - `"Main MU"`：使主要 MU 离开 AssemblyStation。
  - `"New MU"`：使新创建的 MU 离开。

**示例：**

```simtalk
MyAssembly.ExitingMU := "Main MU"
```

**参见：** `Exiting MU [drop-down list] - AssemblyStation`

---

### 3.6 MainMU

设置 `<Path>` 所指定 AssemblyStation 从中拉取主要 MU 的前驱编号。

- **类型：** Attribute（属性）
- **语法：** `<Path>.MainMU:integer`
- **赋值：** 可赋数据类型 `integer` 的值。

**备注：**

- 若主要部件不是由任何前驱递送（例如由 Worker 运输到 AssemblyStation，或用 SimTalk 命令移动主要部件到 AssemblyStation），指定 `0`。
- AssemblyStation 至少连接两个工位，因此**连接前驱的顺序很重要**。若装配流程异常，请检查前驱编号。
- 将鼠标悬停在相应 Connector 上时，Plant Simulation 会在工具提示中显示对象的前驱与后继。

**示例：**

```simtalk
MyAssembly.MainMU := 1
MyAssembly.MainMU := 0  // Worker 通过 Workplace 递送主要部件
```

**参见：** `Main MU from Predecessor`

---

### 3.7 NewMU

设置 `<Path>` 所指定 AssemblyStation 在删除主要 MU 并创建新 MU 时所创建 MU 的路径。

- **类型：** Attribute（属性）
- **语法：** `<Path>.NewMU:string`
- **赋值：** 可赋数据类型 `string` 的值。

**示例：**

```simtalk
MyAssembly.NewMU := ".MUs.basicMU"
```

**参见：** `Exiting MU [drop-down list] - AssemblyStation`

---

### 3.8 OrderSequence

设置 `<Path>` 所指定 AssemblyStation 请求 MU 和/或服务的顺序。

- **类型：** Attribute（属性）
- **语法：** `<Path>.OrderSequence:string`
- **赋值：** 可赋数据类型 `string` 的值。
  - 可选 `"MUs then Services"`、`"Services then MUs"` 或 `"MUs and Services"`。

**示例：**

```simtalk
MyAssembly.OrderSequence := "Services then MUs"
```

**参见：** `Sequence [drop-down list] - AssemblyStation`

---

### 3.9 SequentialDelivery

使 Worker 将 `<Path>` 所指定 AssemblyStation 请求的安装部件**逐个顺序**递送到 AssemblyStation（`true`）。

- **类型：** Attribute（属性）
- **语法：** `<Path>.SequentialDelivery:boolean`
- **赋值：** 可赋数据类型 `boolean` 的值。

**备注：**

- 指定 `false`：单个 Worker 一次递送尽可能多的安装部件。
- 指定 `false`：多个 Worker 并行同时递送安装部件。

> **注：** 若设置 `SequentialDelivery` 为 `true`，属性 `ReservedFor` 返回当前预留位置对应的对象；若设为 `false`，`ReservedFor` 返回预留位置对应对象的数组。

**示例：**

```simtalk
MyAssemblyStation.SequentialDelivery := true
```

**参见：** `ReservedFor [SimTalk]`、`Set How Workers Deliver Mounting Parts`、`Workers Sequentially Deliver MUs to Assemble`

## 目录说明

- `attributes.md`：AssemblyStation 属性说明的 Markdown 版本（本总结的源文件）。
- `attributes.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
