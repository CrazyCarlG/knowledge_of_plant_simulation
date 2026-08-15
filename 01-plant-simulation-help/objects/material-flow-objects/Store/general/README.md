# Store（对象）— General 总结

本目录存放 **Store**（仓库）对象的一般说明文档，内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。此外，本 README 还汇总了 Store 各子文件夹（`attributes`、`methods`、`read-only-attributes`）中的属性、方法与只读属性说明，方便在单一文档中概览整个 Store 对象。

## 1. Store 对象概述

**Store** 用于将零件（MU）存放一段时间，通常代表工厂中的仓库。

- MU 会一直保留在 Store 中，直到被移除（例如通过 Method 移除）。
- 存储位以**坐标网**组织，通过 **X-Dimension**、**Y-Dimension**、**Z-Dimension** 三个文本框设置各轴上的存储位数量；只要存储区内还有可用存储位，Store 就会接收 MU。
- 零件进入 Store 时会触发**传感器**，传感器调用 **Entrance Control**（一个 Method 对象）来决定零件放置到哪个存储位。Entrance Control 可更新库存清单或执行任意自定义动作。若未定义 Entrance Control，Store 会将零件放到坐标网中第一个未占用的存储位。
- Store **既无 Setup Time 也无 Processing Time**。
- 缩小 Store 尺寸时，必须删除或移走位于新坐标范围之外的 MU（例如零件位于 (3,4)，则新 X 坐标不得小于 3、新 Y 坐标不得小于 4）。
- **故障期间** Store 不会把零件放入存储，但仍可从中取出零件。
- 可将 Store 配置为 **Supermarket**（超市），用于拉动式物料流策略：Supermarket 存储并管理不同零件类型，并控制每种零件的填充水平；当某零件达到最小库存时，自动向零件供应商下订单以重新补满。
- 可在 **Appearance** 选项卡选择 Store 的不同外观配置；在 **MU Animation** 选项卡设置零件在动画区域内的分布方式。

**添加到模型：** Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > Store`。

**显示操纵器：** 点击 Edit 功能区标签页的 **Show Manipulators**（或按 `M`）更改图形长度和锚点，从而改变 Store 的尺寸。

## 2. Store 对话框

双击 Store 图标打开其对话框：

- **编辑仿真属性**：共享属性见 *Dialog Items of the Objects*。
- **编辑 3D 属性**：点击仿真属性对话框左下角 **Edit 3D Properties** 按钮，或选中对象后按**空格键**。
- **操纵图形**：点击 Edit 功能区标签页的 **Show Manipulators** 或按 `M`。

## 3. Tab Attributes（属性选项卡）

属性选项卡提供左侧目录中列出的设置。Store 的存储位组织为坐标网，可通过 X/Y/Z-Dimension 设置各轴尺寸，并通过坐标访问各存储位。勾选 Supermarket 复选框可将 Store 用作拉动式物料流策略的超市，Plant Simulation 随后会显示 **Configuration** 按钮并置灰维度设置。

### X-Dimension / Y-Dimension / Z-Dimension [Store]

在文本框中输入 Store 沿 x/y/z 轴可存储的 MU 数量。

- **容量（Capacity）= X-Dimension × Y-Dimension × Z-Dimension**，允许的最大值为 **1000 万（ten million）**。
- Z-Dimension 允许在 Store 中堆叠零件（例如高架仓库向上堆叠）。
- 缩小任一维度时，务必确保没有 MU 位于将被删除的存储位上——要么删除这些 MU，要么将其移到较小存储空间的其他存储位。

**相关 SimTalk：** `XDim`、`YDim`、`ZDim`、`Capacity`、`pe(X,Y)` / `[X,Y]`、`setDim`、`getStackHeight`。

### Fill Whole Layer [复选框]

当 Z-Dimension 大于 1 时可选择逐层填充：

- 勾选后 Plant Simulation 总是先开始新的一层，再在其下层堆放零件。
- 默认**未勾选**：Plant Simulation 会把每个存储位堆到其最大 Z-Dimension，再开始新层。
- 该设置也影响只读属性 `Cont`，它会返回堆叠数量最多的堆中最上层的下一个 MU。

**相关 SimTalk：** `FillWholeLayer`、`Cont`。

### Supermarket [复选框]

勾选后将 Store 用作 Supermarket，以建模拉动式物料流策略。

- 仅在 Store **为空**时才能勾选或取消该复选框。
- Supermarket 存储并管理不同零件类型，控制每种零件的填充水平；当某零件达到最小库存时自动向供应商下订单补货。

#### Configuration Table（配置表）

点击 **Configuration** 打开配置表，可设置每行的：

- **Part Type**：零件类型（输入绝对路径，或将 MU 类拖放至单元格）。
- **Name**：零件类型名称（未指定时使用 Part Type 列的对象名；名称必须唯一）。
- **Minimum Stock**：最小库存。
- **Maximum Stock**：最大库存。
- **Initial Stock**：初始库存（初始化 Store 时创建的零件数量；可小于 Minimum Stock，此时在 Init 时触发订单）。
- **Supplier**：供应商，可为另一个 Store、Source 或 Method。

配置表还显示 **Current Stock**（当前库存，不可编辑）与 **Waiting Stock**（剩余已订购零件数量，不可编辑；Source 与 Store 的 `orderParts` 方法会增加该计数器）。

**其他要点：**

- 重新订购时 Plant Simulation 会把 Store 补到最大库存；若订单进行期间有零件离开，仅在“已订购数量 + 当前数量”无法保证最小库存时才追加新订单。
- 若有多个供应商可供应同一零件，可指定一个 Method 决定从哪个供应商订购。该方法须具备如下签名：

```simtalk
param partName:string, minStock:integer, maxStock:integer,
currentStock:integer, orderedParts:integer
```

- 该 Method 的 caller（`?`）是 Store，active element（`@`）是即将缺货的零件。
- 右键选择 **Append Row** / **Insert Row** 添加产品，**Delete Row** 删除行。

**Supermarket 的动画维度自动设置：** X-Dimension 恒为 1，Y-Dimension 显示不同零件类型数量，Z-Dimension 显示 -1；Store 始终将同类型零件放在同一堆上。

**在图表中显示占用情况：** 将配置为 Supermarket 的 Store 拖到 Chart 上，默认显示配置表中所有零件的占用情况。

**相关 SimTalk：** `Supermarket`、`orderParts`、`getSupermarketConfiguration`、`setSupermarketConfiguration`、`Stock.MyPartName`。

## 4. 其他选项卡

- **Tab Times**：定义时间；从下拉列表选择分布并输入参数，也可选常量 `Const`，可用方法 `setTypeAndAttr` 设置分布类型与完整参数集。
- **Tab Failures**：定义故障。
- **Tab Controls**：修改对象内置行为（Entrance/Exit/Pull 等控制）。点击省略号选择已有 Method；输入名称并选 **Create Control** 创建对象方法（插入 `self.名称`，如 `self.A1Ctrl`；空文本框插入 `self.On内置控制名`，如 `self.OnEntrance`）。用 `F2`、`Shift`+双击、右键 **Open Object** 或 **User-defined** 选项卡编辑源代码。
- **Tab Exit**：选择将 MU 移动到的后继对象。
- **Tab Statistics**：统计信息；查看资源统计用 `View > Show Statistics Report`、右键 Frame 选择 Show Statistics Report 或按 `F6`。
- **Tab Energy**：选择能量设置。
- **Tab Costs**：选择成本设置。Store 存放零件期间产生由投资成本与运营成本之和构成的成本；投资成本仅在折旧期内产生；成本按容量比例分摊给零件作为应计成本；Store 为空时成本作为一般成本保留在 Store。
- **Tab User-defined**：定义自定义属性。

## 5. View 菜单

View 菜单提供：`Refresh`、`Show Statistics Report`、`Show Attributes and Methods`、`Show Orders`、`Contents`、`Forward Blocking List`、`Exit Blocking List`。

### Show Orders [Store]

打开表格显示 Store 待处理的订单：所订购 MU 的 **Part Type**、其 **Amount** 以及 **Target**（订购零件的对象）。

### Exit Blocking List [Store]

打开列表，包含所有等待 Worker 搬运离开的 MU。表格 **Waiting for Importers** 显示 MU 的路径、文件夹、名称与编号。

**相关 SimTalk：** `exitBlockList`。

## 6. Store 的方法

Store 提供：

- 左侧目录中列出的方法；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

| 方法 | 语法 | 返回类型 | 说明 |
| --- | --- | --- | --- |
| `findFreePlace` | `<Path>.findFreePlace([StartingAtEnd:boolean:=false, XStart:integer:=1, YStart:integer:=1])` | `any` | 查找并返回一个空闲存储位。也适用于 ParallelStation、Container 及装载空间类型为 Store 的 Transporter。 |
| `findFreePlaceInRange` | `<Path>.findFreePlaceInRange(SearchRange:listrange[, LeftToRight:boolean:=true, TopToBottom:boolean:=true])` | `any` | 在指定范围内查找空闲存储位并返回其位置。 |
| `findPart` | `<Path>.findPart(PartType:string)` | `object` | 查找并返回指定名称的零件。 |
| `getSupermarketConfiguration` | `<Path>.getSupermarketConfiguration(Target:table)` | — | 将 Store 的配置表写入指定 DataTable。 |
| `orderParts` | `<Path>.orderParts(PartType:string, Amount:integer, Target:object)` | — | 从 Store 订购零件；Target 可为任意物料流对象，若为 Supermarket 则增加“剩余订购数量”计数器。 |
| `pe(X,Y)` / `[X,Y]` | `<Path>.pe([X:integer, Y:integer])` / `<Path>[X:integer, Y:integer]` | `any` | 设置/访问指定坐标的存储位（PE）；不指定参数时返回第一个空闲 PE（无空闲时返回 (1,1)）。 |
| `setSupermarketConfiguration` | `<Path>.setSupermarketConfiguration(Source:table/void)` | — | 设置 Store 的配置表；忽略 Current 与 Waiting 列；传 `void` 激活配置表继承。 |

## 7. 属性（Attributes）

Store 提供以下属性（此外还继承 **所有对象的属性** 与 **物料流对象的属性**）：

| 属性 | 类型 | 数据类型 | 说明 |
|------|------|----------|------|
| `XDim` | 属性 | `integer`（可 watch） | 设置 x 轴存储位数量。 |
| `YDim` | 属性 | `integer`（可 watch） | 设置 y 轴存储位数量。 |
| `ZDim` | 属性 | `integer`（可 watch） | 设置 z 轴存储位数量（允许堆叠零件）。 |
| `FillWholeLayer` | 属性 | `boolean` | 设置 Z-Dimension 大于 1 时是否始终填满整层。 |
| `Supermarket` | 属性 | `boolean` | 设置 Store 是否作为超市工作。 |
| `Stock.MyPartName` | 只读属性 | `integer` | 返回指定零件类型 `MyPartName` 的当前库存。 |

设置/获取属性值示例：`MyStore.XDim := 10`、`MyStore.FillWholeLayer := true`、`MyStore.Supermarket := true`、`print MyStore.Stock.PartRed`。

> 相关对象 **PlaceBuffer**：用于在排成一行的多个缓冲位上加工零件（非 Toolbox 默认提供的内置对象）；MU 必须逐位前进，通过最后一位后才能离开。

## 8. 只读属性（Read-Only Attributes）

Store 提供以下只读属性（此外还继承 **所有对象的只读属性** 与 **物料流对象的只读属性**）：

| 只读属性 | 语法 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| `Capacity` | `<Path>.Capacity` | `integer`（可 watch） | 返回 Store 容量，等于 `XDim × YDim × ZDim`。 |
| `Stock.MyPartName` | `<Path>.Stock.MyPartName` | `integer` | 返回指定零件类型的当前库存。 |

只读属性只能查询、不能设置；Plant Simulation 在查询时刻计算其值，多数只读属性对应对象某选项卡（如 Statistics）上不可编辑的对话框项。查询示例：`print MyStore.Capacity`。

## 9. PE（Store 中的存储位）的方法与只读属性

PE（production element，即 Store 中的存储位）提供以下方法与只读属性：

| 成员 | 类型 | 语法 | 说明 |
| --- | --- | --- | --- |
| `Cont` | 只读属性 | `<Path>.pe(X,Y).Cont` / `<Path>[X,Y].Cont` → `object` | 返回指定存储位最上层（栈顶）的 MU。 |
| `getStackHeight` | 只读属性 | `<Path>.pe(X,Y).getStackHeight` → `length` | 返回指定存储位堆叠的**物理高度**（米，非零件数）。也适用于托盘/Container 上的位置及装载空间类型为 Store 的 Transporter。 |
| `NumMU` | 只读属性 | `<Path>.pe(X,Y).NumMU` → `integer` | 返回指定 PE 上的 MU 数量。 |
| `mu` | 方法 | `<Path>.pe(X,Y).mu(MU:integer)` → `object` | 返回指定存储位堆叠中的所有 MU；索引为 Z 方向位置，`-1` 返回堆底 MU，对象为空时返回 `VOID`。 |
| `exitBlockList` | 方法 | `<Path>.exitBlockList([ExitBlockingList:table])` → `void/object[]` | 返回即将离开 Store 并等待 Worker 搬运的 MU；传入 table 时写入该表（两列：object 与仿真时间）。 |

示例：

```simtalk
MyStore.pe(1,1).Cont.move(Station)
MyStore[1,1].Cont.move(Station)
print MyStore[1,1].NumMU
print MyStore[5,5].mu(1)   -- 栈顶 MU（等同于 .Cont）
print MyStore[1,1].MU(-1)  -- 栈底 MU
var musToExit := Store.exitBlockList
```

## 10. 引用的关键 SimTalk 属性与方法

- `XDim`、`YDim`、`ZDim`、`Capacity`
- `FillWholeLayer`、`Supermarket`、`Stock.MyPartName`
- `findFreePlace`、`findFreePlaceInRange`、`findPart`
- `orderParts`、`getSupermarketConfiguration`、`setSupermarketConfiguration`
- `pe(X,Y)` / `[X,Y]`
- `setDim`、`getStackHeight`
- `Cont`、`mu`、`NumMU`、`exitBlockList`
- `setTypeAndAttr`

## 目录说明

- `general.md`：Store 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- `Plant-Simulation-Help2606_4910-4952.pdf`：对应帮助文档的 PDF 片段。

Store 的子文件夹及其内容（已在本 README 中汇总）：

- `attributes/`：`attributes.md`（Store 属性说明）、`attributes.txtx`、PDF。
- `methods/`：`methods.md`（Store 存储位 PE 的方法与只读属性）、`methods.txtx`、PDF。
- `read-only-attributes/`：`read-only-attributes.md`（Store 只读属性）、`read-only-attributes.txtx`、PDF。

> 注：这些子文件夹目前尚未各自创建独立的 README.md，故其内容以各文件夹内的 `.md` 文件为准，并在此统一汇总。
