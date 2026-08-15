# Sorter / general — 内容总结

> **说明：** 本目录虽然位于 `Sorter/general` 路径下，但其中的文档（`general.md` 与 `general.txtx`）实际记录的是 **Store（仓库/存储）** 对象，另在文件开头附带一小段 `PickAndPlace` 示例。本 README 忠实按照源文件内容进行总结。

本目录包含以下文件：

- `general.md` — Store 对象的完整帮助文档（Markdown 格式）
- `general.txtx` — 与 `general.md` 内容对应的纯文本源文件
- `Plant-Simulation-Help2606_4910-4952.pdf` — 对应的 PDF 参考文件

目录下没有子文件夹，因此不存在子文件夹中的 README.md 需要合并。

---

## 1. 概述

- **Store（仓库）对象**：用于将零件（MU）存储一段时间，通常代表工厂中的仓库。
- 零件会一直留在 Store 中，直到被移除（例如通过 Method 移除）。
- 存储位置以坐标网格（net of coordinates）组织，由 **X-Dimension**、**Y-Dimension**、**Z-Dimension** 三个文本框设置。
- Store 在存储区域内有空位时就会接收 MU。
- 零件进入 Store 时触发传感器，传感器调用 **Entrance Control**（一个 Method 对象）来决定零件放到哪个存储位置；该控制可更新库存清单或执行其他自定义操作。
- 若未定义 Entrance Control，Store 会把零件放到坐标网格中第一个空位。
- Store 既没有 Setup Time 也没有 Processing Time。
- 若缩小 Store 尺寸，需先删除或移走位于新坐标范围之外的 MU。
- 故障（failure）期间 Store 不放入零件，但仍可取出零件。

### Supermarket 配置

Store 也可以配置为 **Supermarket（超市）**，用于拉式（pulling）物料流策略：

- 存储并管理不同的零件类型，并为每种零件类型控制库存水位。
- 当某零件类型达到最小库存时，自动向供应商发送订单，以补满库存。
- 不同配置可在 **Appearance** 选项卡选择；在 **MU Animation** 选项卡可设置零件在动画区域中的分布方式。

---

## 2. 文件开头示例（PickAndPlace 片段）

```simtalk
MyPickAndPlace.WaitForFreeTarget := true
```

相关 SimTalk 引用：`ReservedFor [SimTalk]`、`ReservedPlace [SimTalk]`（MU 的）、`contentsAndReservedList [SimTalk]`、`TargetSelection [SimTalk]`。

另见：Wait for Free Target [PickAndPlace]、Target Selection [drop-down list]。

---

## 3. 基本操作

- **Show Manipulators（显示操纵器）**：在 Edit 功能区点击 Show Manipulators 或按键盘 `M`，可改变对象图形的长度与锚点，进而调整 Store 尺寸。
- **添加到仿真模型**：Home 功能区 → `Manage Class Library > Basic Objects > MaterialFlow > Store`。
- **示例模型**：Window 功能区 → `Start Page > Getting Started > Example Models > Small Examples`，选择 Category、Topic 与 Example 后点击 Open Model。
- 悬停鼠标可显示 Store 的提示信息（tooltip）。

---

## 4. 对话框（Dialog Box）

- 双击 Store 图标打开对话框。
- **Edit Simulation Properties**：修改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit 3D Properties**：
  - 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮；
  - 或在模型中选中对象后按空格键。
  - 操作图形仍用 Show Manipulators（Edit 功能区）或按 `M`。

---

## 5. 选项卡详解

### Tab Attributes

存储位置以坐标网格组织，可通过坐标访问各个存储位置。

- **X-Dimension**：Store 沿 x 轴可存储的 MU 数量。
  - 容量 = X × Y × Z 维度，最大允许值为一千万（10,000,000）。
  - 缩小维度时须确保没有 MU 位于将被删除的存储位上。
  - SimTalk：`XDim`、`Capacity`、`pe(X,Y) / [X,Y]`、`setDim`。
- **Y-Dimension**：沿 y 轴可存储的 MU 数量。规则同上。
  - SimTalk：`YDim`、`Capacity`、`pe(X,Y) / [X,Y]`、`setDim`。
- **Z-Dimension**：沿 z 轴可存储的 MU 数量，用于在 Store 中堆叠零件（如高位仓库向上堆叠）。
  - SimTalk：`ZDim`、`getStackHeight`。
- **Fill Whole Layer（整层填充）**：当 Z-Dimension 大于 1 时，可按层堆放零件。
  - 启用后 Plant Simulation 总是先开新层，再在下一层堆放。
  - 默认关闭：默认在每处堆到最大 Z 后，再开新层。
  - 同时影响只读属性 `Cont`（返回堆叠数量最多的堆中的下一个 MU）。
  - SimTalk：`FillWholeLayer`、`Cont`。
- **Supermarket（复选框）**：把 Store 用作 Supermarket 以建模拉式物料流。
  - 仅在 Store 为空时可勾选/取消勾选。
  - 勾选后显示 **Configuration** 按钮，并置灰维度设置。
  - SimTalk：`Supermarket`、`orderParts`。
- **Configuration（按钮）**：打开配置表，设置 Part Type、Name、Minimum Stock、Maximum Stock、Initial Stock、Supplier；表中还会显示 Current Stock 与 Waiting Stock。
  - 动画尺寸自动设置：X-Dimension 恒为 1，Y-Dimension 为零件类型数，Z-Dimension 为 -1；同类型零件始终堆叠在同一堆。
  - 插入模型后先显示默认尺寸，点击 OK 后按配置表设置并传播到子对象。
  - 可将配置为 Supermarket 的 Store 拖到 Chart 上，默认显示配置表中所有零件的占用情况。
  - 供应商可以是另一个 Store、Source 或 Method；若多个供应商可提供该零件，可用 Method 指定。
  - Method 签名：`param partName:string, minStock:integer, maxStock:integer, currentStock:integer, orderedParts:integer`；调用方为 Store，`@` 为缺货零件。
  - 追加/插入/删除行：右键选择 Append Row / Insert Row / Delete Row。
  - SimTalk：`orderParts`、`getSupermarketConfiguration`、`setSupermarketConfiguration`、`Stock.MyPartName`。

### Tab Times

按 Tab Times 的一般说明定义时间。可从下拉列表选择分布并输入所需值；也可选常量时间（Const）；可用方法 `setTypeAndAttr` 设置分布类型与完整参数集。

### Tab Failures

按 Tab Failures 的一般说明定义故障。

### Tab Controls

提供修改对象内置行为的控制。可：

- 选择已有 Method（点击省略号按钮导航，或从 Frame 拖放 Method 到文本框）；
- 创建作为对象 Method 的控制（输入名称并选择 Create Control，或空文本框上选择 Create Control 自动生成 `self.On...`）；
- 编辑源码：按 F2、Shift+双击、右键 Open Object、或在 User-defined 选项卡双击 Method 名。
- 删除控制：删除对应的 user-defined 属性（仅删除文本框名称不会删除属性）。

### Tab Exit

选择对象把 MU 移动到哪个后继对象（见 Blocking [exit strategy]、Strategy [material flow objects]）。

### Tab Statistics

按 Tab Statistics 说明；在对话框中选择 `View > Show Statistics Report`（或 Frame 中右键 Show Statistics Report，或按 F6）可查看固定资源（Stationary Resources）的资源统计。

### Tab Energy

选择对象的能源设置。

### Tab Costs

选择成本设置。Store 放入零件时产生投资成本与运营成本之和：

- 投资成本仅在折旧期（Depreciation Period）内产生；
- 成本按容量比例作为应计成本分配到零件；
- 若 Store 为空，成本作为一般成本留在 Store。

### Tab User-defined

按 Tab User-defined 说明定义自定义属性。

---

## 6. 菜单

- **Navigate Menu**：命令见 Navigate Menu。
- **View Menu**：提供 Refresh、Show Statistics Report、Show Attributes and Methods 等命令；另引用 Show Orders、Contents、Forward Blocking List。
  - **Show Orders [Store]**：打开表格显示 Store 待处理订单，含 Part Type、Amount、Target（下订单的对象）。
  - **Exit Blocking List [Store]**：列出等待 Worker 运走的所有 MU。表格 **Waiting for Importers** 显示 MU 的路径、文件夹、名称与编号。
    - SimTalk：`exitBlockList`（material flow objects、lane A or B）。
- **Tools Menu**：命令见 Tools Menu。
- **Tabs Menu**：显示/隐藏所选物料流对象的各个选项卡；隐藏不需要的选项卡可加快对话框打开与切换速度。命令 **Inherit** 控制选项卡继承的开关。
- **Help Menu**：命令见 Help Menu。

---

## 7. Store 的方法（Methods）

Store 提供：左侧目录中列出的方法、Material Flow Objects 的方法、以及 All Objects 的方法。可用 **Show Attributes and Methods** 窗口查看全部方法、只读属性与属性（类库右键或按 F8）。

方法签名示例格式：`<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`

- `<Path>` 表示方法作用对象的路径；
- 括号内为签名（参数名:类型）；`[,参数:类型]` 表示可选参数；
- 默认值写在参数后（如 `:= false`）；
- 箭头 `→` 后为返回类型。

具体方法：

| 方法 | 作用 | 语法 |
| --- | --- | --- |
| `findFreePlace` | 查找并返回 Store 中的空闲存储位（也适用于 ParallelStation、Container 及载货空间为 Store 的 Transporter） | `<Path>.findFreePlace([StartingAtEnd:boolean:=false, XStart:integer:=1, YStart:integer:=1]) → any` |
| `findFreePlaceInRange` | 在指定范围内查找空闲存储位并返回其位置 | `<Path>.findFreePlaceInRange(SearchRange:listrange[, LeftToRight:boolean:=true, TopToBottom:boolean:=true]) → any` |
| `findPart` | 按名称查找并返回 Store 中的零件 | `<Path>.findPart(PartType:string) → object` |
| `getSupermarketConfiguration` | 返回 Store 的配置表 | `<Path>.getSupermarketConfiguration(Target:table)` |
| `orderParts` | 从 Store 订购零件 | `<Path>.orderParts(PartType:string, Amount:integer, Target:object)` |
| `pe(X,Y) / [X,Y]` | 设置指定存储位（生产元素 PE） | `<Path>.pe([X:integer, Y:integer]) → any` 或 `<Path>[X:integer, Y:integer] → any` |
| `setSupermarketConfiguration` | 设置 Store 的配置表（`void` 可激活配置表继承） | `<Path>.setSupermarketConfiguration(Source:table/void)` |

关键参数说明：

- `findFreePlace`：`StartingAtEnd`（是否从末尾向前搜索，默认 false）、`XStart`/`YStart`（搜索起始坐标，默认 1）。
- `findFreePlaceInRange`：`SearchRange`（listrange，搜索范围）、`LeftToRight`/`TopToBottom`（默认 true）。
- `orderParts`：`PartType`（零件类型名）、`Amount`（订购数量）、`Target`（订购对象，可为任意物料流对象；若为 Supermarket 则增加 Waiting 计数）。
- `pe(X,Y)`：`X`/`Y` 为存储位维度；不指定参数时返回第一个空闲 PE，若无空闲 PE 则返回位置 (1,1)。可用 `[X,Y].Cont` 访问该位置的 MU（只读属性 `Cont`）。

---

## 8. PE（存储位）的方法与只读属性

PE（production element，即 Store 中的存储位）提供目录中列出的方法与只读属性（文档中未展开具体列表，见目录左侧）。
