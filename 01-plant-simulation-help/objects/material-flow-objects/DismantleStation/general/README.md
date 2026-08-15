# DismantleStation — general（概述）

本目录汇总了 **DismantleStation**（拆卸站）对象的通用帮助文档，用于在 Plant Simulation 中建模"拆卸"过程，即从主部件（main part）上移除装配件（mounting parts）。

> 本目录当前包含以下源文件：
> - `general.md`：DismantleStation 帮助页面的 Markdown 汇总。
> - `general.txtx`：同一内容的原始文本提取版本（更冗长）。
> 无子文件夹。

---

## 1. 对象概述

- **用途**：DismantleStation 从主部件上移除装配件。
- 若要建模**装配**（assembly）过程，请使用 **AssemblyStation**。
- 默认情况下，`Dismantle Table`（拆卸表）或设置项 `Main MU to Successor with Number`（主 MU 送往的后继编号）决定 DismantleStation 将部件移动到哪个后继（successor）。
- 若希望 Worker 将所有部件搬运到某个指定目标，可在 **Importer > Transport** 选项卡上把该对象设为 **MU Target**；此时 Plant Simulation 会覆盖上述设置。
- 鼠标悬停在对象上会显示工具提示；点击 Edit 功能区中的 **Show Manipulators** 或按 **M** 键可修改图形长度与锚点。

## 2. 将对象添加到仿真模型

- 在 Home 功能区点击 **Manage Class Library > Basic Objects > MaterialFlow > DismantleStation**。
- 示例模型：**Window** 功能区 → **Start Page > Getting Started > Example Models > Small Examples**，再在 **Examples Collection** 对话框中选择 Category、Topic 与 Example，点击 **Open Model**。

## 3. 对话框与属性编辑

- 双击对象图标打开对话框。
- **Edit Simulation Properties**：修改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties**：编辑 3D 属性，可点击对话框左下角 **Edit 3D Properties** 按钮，或选中对象后按空格键；用 **Show Manipulators** 或 **M** 键操纵图形。

---

## 4. 各选项卡说明

### 4.1 Tab Attributes

设置 DismantleStation 如何从主部件移除部件或创建新部件。

**Sequence [下拉列表]** — 选择如何将拆卸后的 MU 分配给后继：

- **MUs to all Successors**（将所有 MU 发送到所有后继）：
  - 配合 `Dismantle Mode > Create MUs`：为每个后继创建一个新 MU 并移入；主 MU 移向 `Main MU to Successor with Number` 指定的后继。
  - 配合 `Dismantle Mode > Detach MUs`：将 MU 依次移向除主 MU 后继之外的各个后继。例如有 4 个后继、主 MU 移向 2 号后继时，新 MU 移向 1、3、4 号后继，主 MU 移向 2 号。
- **MUs exiting independent of other MUs**：主 MU 及随后每个 MU 尽快按定义移向各自后继。
- **Main MU after other MUs**：先移走装配件，再移走主 MU。
- 若只想卸载拆卸表中指定的装配件，选择 `MUs exiting independent of other MUs` 或 `Main MU after other MUs` 且 `Dismantle Mode > Detach MUs`，并在 `MU` 列填入有效 MU 类、`Number` 列填入正数。

**Dismantle Table [按钮]** — 打开三列表格：

| 列 | 说明 |
|----|------|
| `MU` | MU 类路径，如 `.MUs.Part`、`.MUs.Container`、`.MUs.Transporter`；留空表示任意 MU 类 |
| `Number` | 拆卸数量；填 `-1` 表示全部；不填默认 `1` |
| `Successor` | 后继编号；`Detach MUs` 下不填默认 1 号后继，`Create MUs` 下不填则移到主 MU 所去的后继 |

> 注意：若填写了 **MU Target**，Worker 会把所有 MU 搬运到该目标；否则由 Dismantle Table 或 `Main MU to Successor with Number` 决定。

- 按 MU 类自动移动所有 MU：在 `MU` 填类、`Number` 填 `-1`、`Successor` 填目标后继，重复处理更多类。
- 移动所有 MU 到某后继：`MU` 留空、`Number` 填 `-1`、`Successor` 填目标后继。

**Dismantle Mode [下拉列表]**：

- **Detach MUs**：从主 MU 上拆卸装配件并移向拆卸表指定的后继。
- **Create MUs**：创建（新）装配件。

**Main MU to Successor with Number [文本框]**：输入主 MU 移向的后继编号。不能使用 `0`（会被改为默认值 `1`；若给属性 `Main MU` 赋值 0 会报错）。

**Exiting MU [下拉列表]** — 主 MU 或新 MU 移向后继的方式：

- **Main MU**：将主 MU 移向后继。
- **New MU**：删除主 MU、创建一个新 MU 并移向后继；此时显示 `MU` 文本框，可输入类路径或通过按钮选择。

### 4.2 Tab Times

- 定义处理时间，选择分布并填写参数（分布参数显示在选项卡上边框），也可选常量 **Const**。
- 可用 `setTypeAndAttr` 方法设置分布类型与完整参数。

### 4.3 Tab Set-Up

- 定义对象的调整（set-up）属性，见 *Tab Set-Up*。

### 4.4 Tab Failures

- 定义故障，见 *Tab Failures*。

### 4.5 Tab Controls

- 提供修改对象内置行为的控制项。
- Plant Simulation 对每个离开的部件调用 **Exit Control**；仅调用 `@.move` 时，部件会移向无 Exit Control 时应去的后继。
- **选择已有方法**：点击省略号按钮，在 *Select Object [for controls]* 中导航选择 Method，或从 Frame 中拖放 Method 到文本框。
- **创建对象方法形式的控制**：输入名称后选 **Create Control**（插入 `self.名称`，如 `self.A1Ctrl`）；在空文本框选 **Create Control** 会插入 `self.On内置控制名`（如 `self.OnEntrance`）。后续可用 **F2**、Shift+双击、**Open Object** 或 User-defined 选项卡编辑；删除控制需删除对应的用户自定义属性。

### 4.6 Tab Statistics

- 统计信息见 *Tab Statistics*；此外 DismantleStation 显示 **Blocking Times** 按钮。
- 查看固定资源的 Resource Statistics：对象对话框 **View > Show Statistics Report**，或在 Frame 中右键选 **Show Statistics Report**，或按 **F6**。
- **Blocking Times [表格]**：显示各后继 MU 阻塞时间之和，相关 SimTalk：`statBlockingTimePerSuccessor`、`statBlockingTimeTable`。

### 4.7 Tab Importer

- 定义处理、为特定部件类型调整、维修等服务。
- 注意：若把该对象设为 **Importer > Transport** 的 MU Target，Plant Simulation 会覆盖 Dismantle Table / `Main MU to Successor with Number` 设置。
- 查看 Importer Statistics：选中对象按 **F6**、Home 功能区 **Show Statistics Report**，或右键上下文菜单。

### 4.8 Tab Energy

- 为对象选择能耗设置，见 *Tab Energy*。

### 4.9 Tab Costs

- 选择成本设置。AssemblyStation 添加装配件时产生投资成本与运行成本之和。
- 总投资成本仅在折旧期内产生；成本作为应计成本分配到主部件，装配件此前累计的成本会转移到主部件；若站为空，成本作为一般成本保留在站上。

### 4.10 Tab User-defined

- 定义用户自定义属性，见 *Tab User-defined*。

---

## 5. 菜单

### Navigate Menu
- 命令见 *Navigate Menu*。

### View Menu
提供以下命令：Refresh、Show Statistics Report、Show Attributes and Methods、Contents、Forward Blocking List、Exit Blocking List、Exporters、Services、Unavailable Services、Associated Workplaces、Exiting MUs、Associated Lockout Zones、Associated Shift Calendar。

- **Contents [DismantleStation]**：列出该站已拆卸的所有 MU（相关 SimTalk：`Cont`、`contentsList`、`deleteMovables`、`mu`、`NumMU`、`NumMUParts`）。
- **Exiting MUs**：显示当前位于站上、并在主部件移向第 2 列后继时被删除的 MU（相关 SimTalk：`leavingMU`、`leavingMUs`、`NumLeavingMU`）。

### Tools Menu
- 命令见 *Tools Menu*。

### Tabs Menu
- 显示/隐藏所选物流对象的各个选项卡；隐藏不用的选项卡可加快对话框打开与切换速度。
- 修改后点击 **OK** 关闭并重新打开生效；显示的选项卡前有勾选标记；**Inherit** 命令可开关选项卡显示/隐藏的继承。

### Help Menu
- 命令见 *Help Menu*。

---

## 6. 方法（Methods）

DismantleStation 提供：

- 左侧目录列出的方法；
- *Methods of the Material Flow Objects*；
- *Methods of All Objects*。

查看全部方法、只读属性与属性：打开 **Show Attributes and Methods** 窗口；在 Class Library 上下文菜单选 **Show Attributes and Methods** 查看类，或在 Frame 中按 **F8** / Home 功能区点击 **Show Attributes and Methods** 查看实例。

---

## 7. 相关参考（See Also）

- AssemblyStation
- Remove Parts with the Dismantle Station
- 视频教程（YouTube）：https://youtu.be/yEAqrVDBsns?si=rLxurb7Z5n4OVpJX&t=407
