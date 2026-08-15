# Source（对象）— General 总结

本目录存放 **Source**（源）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. Source 对象概述

**Source** 用于生产在模型中流动的工件（MU），通常代表工厂的收货部门或主要生产机器。

- Source 的**容量为 1**，且**无加工时间**。
- 它可以逐个或按混合顺序生产相同或不同类型的 MU。
- 可设置一个过程来确定**创建工件的时间**，以及一个过程来确定**要生产的 MU 类型**。
- 作为主动物料流对象，Source 会尝试将其生产的 MU 移动到所连接的后继对象。
- 可通过勾选或取消 **Blocking** 来定义 Source 无法将 MU 移动到后继对象时的处理方式。
- 使用 **Drain** 移除工厂中的工件（例如建模发货部门）。
- 将鼠标悬停在 Source 上可显示工具提示；点击编辑功能区标签页的 **Show Manipulators**（或按 `M`）可更改图形长度和锚点。

**添加到模型：** Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > Source`。

## 2. Side [SimTalk]

设置 `<Path>` 指定的 Interface 所在 Frame 的侧面。

- 类型：Attribute
- 语法：`<Path>.Side:string`
- 取值：`"Top"`、`"Right"`、`"Bottom"`、`"Left"` 或 `"Angle-dependent"`（考虑对象间角度以确定 Connector 的起点/终点）。

```simtalk
interface.Side := "right"
```

## 3. Source 对话框

双击 Source 图标打开对话框，可编辑仿真属性与动画属性（编辑 3D 属性：点击左下角 **Edit 3D Properties** 按钮，或选中对象按空格键；按 `M` 或点击 **Show Manipulators** 操纵图形）。

## 4. 选项卡 Attributes（属性）

### Operating Mode（运行模式，复选框）

设置 Source 在无法于所设创建时间创建 MU 时的处理方式：

- **勾选 Blocking**：Source 记住本应生产下一 MU 的时间，并在下一可行时间点（被后继阻塞的 MU 移走后）生产后续 MU；仿真时间到达 Stop 时间时停止创建。
- **取消 Blocking**：Source 仅在你输入的创建时间创建另一 MU。

> 当 Source 暂时不可用（故障、暂停或阻塞）时，若勾选 Blocking，创建时间可能发生偏移，导致创建时间设置无法实现。

### Time of Creation（创建时间，Source）

选择 Source 生产 MU 的时间点与方式，可用设置：

- **Interval Adjustable（间隔可调）**：在 **Start** 时间生产第一个 MU；**Interval** 为两次创建事件之间的时间；在 **Stop** 时间生产最后一个 MU。
  - 无 Stop 时间时最多生产输入的 **Amount** 个工件（默认 `-1` = 不限量）。
  - 有 Stop 时间时生产工件直到 Stop 时间，并忽略 **Amount**。
  - 恒定时长会在该时间点生产所有 MU。
- **Number Adjustable（数量可调）**：生产 **Amount** 中输入的 MU 数量；若激活 **Generate as Batch**，Amount 表示**批次**数而非工件数；创建时间按 **Interval** 分布分配。
- **Delivery Table（交付表）**：按交付表中的 **Delivery Time、Class、Number、Name、Attribute** 生产 MU。仿真期间若指定新交付表，也会生产过去本应生产的工件。
- **Trigger（触发器）**：根据一组 **Trigger** 对象控制的值生产 MU。

根据设置，属性 `Path`（对话框项 MU 或 Table）设置到 MU 类、交付列表、序列表、频率表或百分比表的路径。

### Interval Adjustable（间隔可调，创建时间）

按 **Interval、Start、Stop** 定义的时间点生产 MU：

- **Start**：第一个 MU 的生产时间点。
- **Interval**：两次创建事件之间的时间跨度。
- **Stop**：最后一个 MU 的生产时间点（输入 `0` 则按 Amount 生产）。
- 三者均可选择**概率分布**。
- **Amount**：Source 生产的 MU 数量（仅 *Number Adjustable* 与 *Interval Adjustable*）。

> 无 Stop 时间时最多生产 Amount 个（`-1` = 不限量）；有 Stop 时间时忽略 Amount；激活 Generate as Batch 时可能生产超过 Amount 的工件（批次总是整批生产）。

### Number Adjustable（数量可调，创建时间）

生产 Amount 中输入的 MU 数量：

- 激活 Generate as Batch 时 Amount 表示批次而非工件。
- 从 **Creation Times** 选择概率分布来决定创建时间。
- MU 数量按仿真开始时随机数生成器生成的时间生产；可输入上下界限制时间。
- **Constant** 恒定时间会在同一时间点创建所有 MU。

> *Number Adjustable* 不能选择 MU Selection > Sequence。通过 SimTalk 设置创建时间使用属性 `Interval`。

### Delivery Table（交付表，创建时间）

按交付表设置生产 MU：

- 在 **Table** 中输入交付表路径，或点击后在 *Select Object* 中选择表。
- 交付表有 5 列，数据类型为 `time、object、integer、string、table`（`time` 也可用 `date、dateTime、real` 代替）。每行定义一条生产订单：
  - **Delivery Time**：生产 MU 的时间（须逐行递增；过去的时间会立即创建工件）。
  - **MU**：MU 类（支持拖放）。
  - **Number**：MU 数量（输入 `0` 则在下一周期计入间隔但不生产工件）。
  - **Name**：MU 名称（必填：Delivery Time 与 MU；缺省 Number 为单个 MU；缺省 Name 继承类名）。
  - **Attributes**：设置在生产 MU 上的表/用户自定义属性。

> 属性细节：在属性表第 1 列输入属性名，不存在时 Plant Simulation 会自动创建；包含值的列的数据类型会赋给该属性。若列数据类型为 `table/list/stack/queue`，则创建的是**引用**而非复制子列表（改一个即改另一个）。
> 仿真期间指定交付表时，Source 不会生产创建时间在未来的工件。除 Frame 中的 DataTable 外，也可使用 Source 的 `table` 类型用户自定义属性作为交付表。

### Trigger（触发器，创建时间）

根据一个或多个 **Trigger** 对象控制的值生产 MU：

- 点击 **Trigger** 并输入 Trigger 对象名，每个 Trigger 以字符串发送订单。
- 打开 Trigger → 选项卡 **Values** → Trigger Type **Input** → 点击 **Values**，在选项卡 **Contents** 输入订单：
  - 左单元格：Source 创建 MU 的**时间点（Point in Time）**。
  - 右单元格：订单的**值（Value）**，字符串格式为“MU 数量、MU 类型、分布类型及分布参数”：

```simtalk
(<num>, <mu_Type>, <distributionType[, distribution parameters]>)
```

- 数量、MU 类型、分布类型三者必填。
- 分布类型为 `Const` 时，Source 在 Point in Time 列的时间点生产 MU（可选秒级偏移）。
- 其他分布需输入分布参数；分布值设置到 Point in Time 列时间的**时间偏移**（须为正）。

> 若 Source 作为 ShiftCalendar 中的资源，周末会中断生产顺序：勾选 Blocking 时周末不生产 MU；取消 Blocking 时班次重新开始后立即生产并移动 MU。适用于周期重复的创建时间（如 MU Selection > Sequence Cyclical）。

### Interval / Start / Stop [Source]

- **Interval**：*Interval Adjustable* 下两次创建事件之间的时间跨度（Source 创建无限多 MU），可选择分布或 `Const`。
- **Start**：Source 生产第一个 MU 的时间点，可选择分布或恒定时间 `Const`。
- **Stop**：Source 停止生产 MU 的时间，可选择分布或恒定时间 `Const`。

### MU Selection（MU 选择，下拉列表）

选择 Source 生产何种 MU 及如何生产：

- **Constant**：仅一种 MU 类型（路径在文本框 **MU** 中）。
- **Sequence Cyclical**：按表中的固定序列生产 MU；序列处理完后周期重复。
- **Sequence**：按序列表生产 MU；序列**仅处理一次**。
- **Random**：按频率表以随机频率生产 MU。
- **Percentage**：按百分比表以百分比生产 MU。
- **Order Controlled**：仅在 Store 以 **Supermarket** 模式激活或用方法 `orderParts` 订购时才生产 MU。

> 要使用 DataTable 的**副本**而非引用，将子表命名为 `.unshare`。

#### Constant（MU 选择）

生产一种类型的 MU。在 **MU** 旁输入路径，点击选择 MU 类（Part、Container、Transporter），或从工具箱/类库拖放。

#### Sequence Cyclical（MU 选择）

按序列表（**MU Selection > Sequence Cyclical** 路径）生产工件：

- 可预分配用户自定义属性；`table` 类型属性存为**引用**（省内存/提升性能），强制复制给子表赋 `.unshare`。
- 勾选 **Generate as Batch** 将表中 Number 个 MU 在一个批次中一次性生产。
- 取消勾选则逐个生产 MU。
- 处理完整个序列后从头再次开始（周期循环）。

#### Sequence（MU 选择）

按序列表（**MU Selection > Sequence** 路径）生产 MU：

- 序列**仅处理一次**（不重复）。
- 创建时间为 *Number Adjustable* 时**不可用**。
- 属性引用/`.unshare` 与 Generate as Batch 行为同 Sequence Cyclical。

#### Random（MU 选择）

按频率表（**MU Selection > Random** 路径）生产 MU：

- 频率表有 5 列，数据类型 `object、real、integer、string、table`，每行为一条生产订单：
  - **MU**：MU 类。
  - **Frequency**：生产订单的频率。
  - **Number**：要生产的 MU 数量。
  - **Name**：（可选）MU 名称。
  - **Attributes**：（可选）生产 MU 的属性子表。
- 勾选 Generate as Batch 将 Number 个 MU 一个批次生产。*Number Adjustable* 时 Amount 表示批次而非工件。
- 在选项卡 Statistics 激活 **Creation Table** 可查看何时生产了哪些工件类型。

#### Percentage（MU 选择）

按百分比表（**MU Selection > Percentage** 路径）生产 MU：

- 百分比表列：**MU**（名称/路径）、**Portion**（百分比）、**Number**（数量），及可选的 **Name** 与 **Attributes**。
- 勾选 Generate as Batch 将 Number 个 MU 一个批次生产。*Number Adjustable* 时 Amount 表示批次而非工件。
- **Percentage** 是确定性过程：选择下一工件时 Source 转向 Portion 列需求最大的行，形成周期性重复模式。

#### Order Controlled（MU 选择）

仅在 Store 以 **Supermarket** 模式激活或用方法 `orderParts` 订购时才生产 MU：

- 自动路由将生产的工件交付给订购站（若停用则自动启用）。
- Source 按 **Interval Adjustable** 与创建时间之间的 **Interval** 生产 MU。

### Generate as Batch（成批生产，复选框）

使 Source 将表格中的 **Number** 个 MU 在**单个批次**中生产——在给定开始时间一次性生产，作为一个批次移动到下一对象而非逐个移动。

- 适用于 MU Selection > Sequence、Sequence Cyclical、Random、Percentage。
- 创建时间为 *Number Adjustable* 时，**Amount** 表示批次数而非工件数。

## 5. 其他选项卡

- **Tab Failures（故障）**：按故障选项卡说明定义故障。
- **Tab Controls（控制）**：修改对象内置行为。点击省略号按钮选择已有 Method；输入名称并选择 **Create Control** 创建对象方法（插入 `self.名称`，如 `self.A1Ctrl`；空文本框插入 `self.On内置控制名`，如 `self.OnEntrance`）。用 `F2`、`Shift`+双击、右键菜单 **Open Object** 或 **User-defined** 选项卡编辑源代码。
- **Tab Exit（出口）**：选择对象将 MU 移动到哪个后继。
- **Tab Statistics（统计，Source）**：除标准统计值外，提供 **Creation Table** 与 **Open**。查看资源统计：View > Show Statistics Report，右键 Frame 选择 Show Statistics Report，或按 `F6`。
- **Tab User-defined（用户自定义）**：定义自定义属性。

### Creation Table（创建表）

复选框，将仿真运行期间 Source 生产 MU 的所有事件写入表格，点击 **Open** 查看。Source 在资源统计之外还记录创建事件。

### Open（打开创建表）

打开创建表（若勾选 Creation Table），每行列出一次生产事件：

- **Name**：MU 类名。
- **Path**：MU 类路径、MU 名称及其编号。
- **Time of Generation**：Source 创建该 MU 的时间。

## 6. 菜单

- **Navigate 菜单**：命令见 Navigate Menu 说明。
- **View 菜单**：提供 `Refresh`、`Forward Blocking List`、`Show Statistics Report`、`Exit Blocking List`、`Show Attributes and Methods`、`Associated Lockout Zones`、`Show Orders`、`Associated Shift Calendar`、`Contents`。
- **Tools 菜单**：命令见 Tools Menu 说明。
- **Help 菜单**：命令见 Help Menu 说明。

### Show Orders（显示订单）

打开表格显示 Source 待处理的订单：订购工件的 **Name**、其 **Amount**，以及 **Target**（订购工件的对象）。

## 7. Source 的方法

Source 提供：

- 左侧目录中列出的方法；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

查看方式：打开 **Show Attributes and Methods**（类库上下文菜单，或按 `F8` / 点击 Frame 的 Home 功能区标签页上的 Show Attributes and Methods）查看全部方法、只读属性和属性。

## 8. 引用的关键 SimTalk 属性与方法

- `Side`（`<Path>.Side:string`）
- `Blocking`
- `TimeOfGeneration`
- `Number`
- `Interval`、`Start`、`Stop`
- `Path`
- `MUSelection`
- `GenerateAsBatch`、`CurrentBatchNumber`
- `CreationTableActive`、`creationTable`
- `orderParts`
- `getCurrentOrderTableRow`
- `unshare`

## 目录说明

- `general.md`：Source 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- `Plant-Simulation-Help2606_4497-4541.pdf`：对应帮助文档的 PDF 片段。
- 本目录无子文件夹，故无子文件夹 README.md。
