# ParallelStation — Attributes（属性）总览

本目录汇总 **ParallelStation**（并行工位）对象的属性（Attributes）文档，并整合同级各子目录（`general`、`methods`、`read-only-attributes`）README 的核心内容。当前目录下包含：

- `attributes.md` — Markdown 格式的属性说明文档（英文原版内容）
- `attributes.txtx` — 纯文本格式的同内容说明文档

> 注：本目录下没有子文件夹。

---

## 一、属性（Attributes）

ParallelStation 提供：

- 左侧目录中列出的属性；
- 所有对象的属性（Attributes of All Objects）；
- 物流对象的属性（Attributes of the Material Flow Objects）。

属性的值可以**设置**（set）也可以**获取**（get），既可通过对话框中的复选框、文本框和下拉列表，也可通过为相应属性赋值。

- **设置**属性值：

```simtalk
ParallelStation.XDim := 3
ParallelStation.YDim := 4
```

- **获取**属性值：

```simtalk
print ParallelStation.XDim
posit := MyStation.Cont.XPos
```

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，显示所选**类**的方法、只读属性和属性。
- 按下 **F8** 键，或点击插入实例的 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，显示所选**实例**的方法、只读属性和属性。

本目录 `attributes.md` 中详细介绍的属性如下。

### 1. StartProcessingWhenFull（满时开始加工）

设置由 `<Path>` 指定的 ParallelStation 是否**仅当所有加工工位上都各有一个零件时才启动加工**（`true`）。

**要点：**

- `true` 为默认设置。此时新零件只能在当前批次加工完成且全部离开后才可进入。
- 若另一类型零件想进入，即使未满也会先加工已有零件；只有加工完并清空后，其他类型零件才能进入。
- 可用方法 `startProcessing` 在未满时强制开始加工。
- 指定 `false` 时，零件进入后立即加工，新零件可随时进入。
- 若无需设置，不同类型零件也可进入；满载后可能以不同加工时间开始加工（适用于类型相关、位置相关的加工时间以及公式形式的加工时间）。

> **注意**：对于基于加工时间的故障，并行加工的零件数越多，模拟的 MTBF 越小、可用性越低；但选中 **Start Processing When Full** 时此现象不适用。

- **类型（Type）：** Attribute
- **语法（Syntax）：** `<Path>.StartProcessingWhenFull:boolean`
- **赋值类型：** `boolean`
- **示例：**

```simtalk
ParallelStation.StartProcessingWhenFull := false
```

- **另请参见：** `startProcessing`、Start Processing When Full [check box]

### 2. XDim

设置或获取由 `<Path>` 指定的 ParallelStation 在 X 维方向上的加工工位数量。

- **容量（Capacity）** 等于 `XDim × YDim` 的乘积，最大允许值为一千万（10,000,000）。
- **类型（Type）：** Attribute
- **语法（Syntax）：** `<Path>.XDim:integer`
- **可监视（Watchable）：** 是
- **赋值类型：** `integer`
- **示例：**

```simtalk
ParallelStation.XDim := 3
ParallelStation.YDim := 4 // 12 个工位
```

> **注意**：减小维度时，务必确保没有 MU 位于将被删除的工位上。若对象上有 MU，维度会受到限制，因为 Plant Simulation 不会自动删除或移动新维度之外的 MU。例如 MU 位于 (3,4) 时，新 x 坐标不得小于 3，新 y 坐标不得小于 4。

- **另请参见：** X-Dimension [ParallelStation]、`XDim` [SimTalk] - ParallelStation

### 3. YDim

设置或获取由 `<Path>` 指定的 ParallelStation 在 Y 维方向上的加工工位数量。

- **容量（Capacity）** 等于 `XDim × YDim` 的乘积，最大允许值为一千万（10,000,000）。
- **类型（Type）：** Attribute
- **语法（Syntax）：** `<Path>.YDim:integer`
- **可监视（Watchable）：** 是
- **赋值类型：** `integer`
- **示例：**

```simtalk
ParallelStation.XDim := 3
ParallelStation.YDim := 4 // 12 个工位
```

> **注意**：减小维度时，务必确保没有 MU 位于将被删除的工位上。若对象上有 MU，维度会受到限制，因为 Plant Simulation 不会自动删除或移动新维度之外的 MU。

- **另请参见：** Y-Dimension [ParallelStation]、`YDim` [SimTalk] - ParallelStation

---

## 二、对象概述（来自 `general`）

**ParallelStation** 用于建模同时并行处理多个零件（MU）的机器。其内置属性与 **Station** 相同，区别在于 ParallelStation 拥有**多个处理位置（processing places）**，而 Station 只有一个处理位置。

**核心特性：**

- 如果某个 MU 与其前一个加工零件的名称不同，则始终会产生设置时间（set-up time）。
- Plant Simulation 总是将 MU 作为一个整体移动（非连续移动）：一旦 MU 的前端到达 ParallelStation，整个 MU 即视为已位于其上。
- 在 **MU Animation** 选项卡中可设置零件在 Animation Area 上的分布方式。
- 悬停鼠标可显示关于 ParallelStation 的工具提示。
- 通过 Edit 功能区选项卡的 **Show Manipulators** 或按 `M` 键，可更改图形长度和锚点。

> **注意**：TransferStation 基于 ParallelStation 构建（其属性被修改和增强），因此对 TransferStation 按 `F1` 会打开 ParallelStation 的帮助。

**添加到仿真模型：** Home 功能区选项卡 > **Manage Class Library > Basic Objects > MaterialFlow > ParallelStation**。

**对话框主要选项卡：**

- **Tab Attributes（属性）**：X-Dimension、Y-Dimension 构成容量（`Y-Dimension × X-Dimension`，最大 10,000,000）；**Start Processing When Full** 默认选中。SimTalk：`XDim`、`YDim`、`Capacity`、`pe, [X,Y]`、`setDim`。
- **Tab Failures（故障）**：定义故障；基于加工时间的故障存在"并行加工越多 MTBF 越低"的注意点（选中 **Start Processing When Full** 时不适用）。
- **Tab Times（时间）**：从下拉列表选择分布并输入值；可用 `setTypeAndAttr` 设置分布类型与参数集。
- **Tab Set-Up（设置）**：定义设置属性。ParallelStation **不提供** **After n parts** 设置。
- **Tab Controls（控制）**：选择 Method 或通过 `F2` / **Create Control** 创建控制。
- **Tab Exit（出口）**：选择后继；除 **MU Attribute** 外的阻塞型出口策略使用 Exit Blocking List。
- **Tab Statistics / Tab Importer**：按 `F6` 或 **Show Statistics Report** 查看统计。
- **Tab Energy / Tab Costs**：能源与成本设置；成本平均分配到各处理位置。
- **Tab User-defined**：自定义属性（相关 SimTalk：`getAttrName`、`createAttr`、`deleteAttr` 等）。

---

## 三、方法（来自 `methods`）

ParallelStation 提供：左侧目录中列出的方法、物流对象的方法、所有对象的方法。`methods.md` 中详细介绍的方法如下。

### `findPart [SimTalk]`

在由 `<Path>` 指定的 ParallelStation 上查找指定名称的零件并返回它。

- **语法：** `<Path>.findPart(PartType:string) → object`
- **参数：** `PartType`（`string`）
- **返回值：** `object`

```simtalk
var o: object := MyParallelStation.findPart("Container")
```

### `pe, [X,Y] [SimTalk]`

设置由 `<Path>` 指定的 ParallelStation 生产单元（PE）上指定的加工工位。

- **语法：**

```
<Path>.pe([X:integer,Y:integer]) → any
<Path>[X:integer,Y:integer] → any
```

- **参数：** `X`、`Y`（可选，`integer`）。若不指定参数，返回第一个空闲的 PE；若无空闲 PE，返回工位 (1,1) 上的 PE。
- **返回值：** `any`

```simtalk
@.move(ParallelStation[2,3])
print ParallelStation[2,3].Cont.name
```

---

## 四、只读属性（来自 `read-only-attributes`）

ParallelStation 提供以下只读属性：

- **Capacity [SimTalk] - ParallelStation**
- 所有对象的只读属性（Read-Only Attributes of All Objects）
- 物流对象的只读属性（Read-Only Attributes of the Material Flow Objects）

只读属性的值可以**查询**，但不能**设置**。大多数情况下，只读属性对应对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。

### Capacity [SimTalk] - ParallelStation

返回由 `<Path>` 指定的 ParallelStation 的容量。

| 项目 | 说明 |
| --- | --- |
| **Remarks** | 容量等于 `XDim × YDim` 的乘积。 |
| **Type** | 只读属性（Read-only attribute） |
| **Syntax** | `<Path>.Capacity → integer` |
| **Watchable** | 可监视（watchable） |
| **Return Value** | `integer` |

```simtalk
if ParallelStation.Capacity >= lotsize 
   @.move(ParallelStation)
end
```

---

## 五、相关对象：AssemblyStation（来自 `attributes.md` 末尾）

使用 **AssemblyStation** 对象将装配件（mounting parts）添加到主零件上（例如将车门装配到车身上）。其将装配件移动到主 MU 上（按 Assembly Table 中的值）或删除它们；如需服务，可指定请求顺序。反过程（拆解）使用 **DismantleStation**。

> **注意**：不能通过信息流（即使用方法）将零件移动到 AssemblyStation 上。

---

> 来源：Plant Simulation Help，Unpublished work. © 2026 Siemens
