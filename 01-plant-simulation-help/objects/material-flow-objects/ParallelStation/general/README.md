# ParallelStation 概述

本目录包含 **ParallelStation**（并行工位）对象的帮助文档总结。原始内容来自 `general.md`（以及同内容的 `general.txtx`），本 README 汇总其核心要点。

## 对象用途

**ParallelStation** 用于建模同时并行处理多个零件（MU）的机器。其内置属性与 **Station** 相同，区别在于 ParallelStation 拥有**多个处理位置（processing places）**，而 Station 只有一个处理位置。

## 核心特性

- 如果某个 MU 与其前一个加工零件的名称不同，则始终会产生设置时间（set-up time）。
- Plant Simulation 总是将 MU 作为一个整体移动（非连续移动）：一旦 MU 的前端到达 ParallelStation，整个 MU 即视为已位于其上。
- 在 **MU Animation** 选项卡中可设置零件在 Animation Area 上的分布方式。
- 悬停鼠标可显示关于 ParallelStation 的工具提示。
- 通过 Edit 功能区选项卡的 **Show Manipulators** 或按 `M` 键，可更改图形长度和锚点。

> **注意**：TransferStation 基于 ParallelStation 构建（其属性被修改和增强），因此对 TransferStation 按 `F1` 会打开 ParallelStation 的帮助。

## 查看属性与方法

- 在类库（Class Library）上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 在插入实例的 Frame 中按 `F8` 或点击 Home 功能区选项卡的 **Show Attributes and Methods**，可查看所选实例的对应内容。

可通过对话框中的复选框、文本框、下拉列表，或直接给属性赋值来设置/获取属性值。示例：

```simtalk
-- 设置属性值
MyStation.Pause := true

-- 获取属性值
print MyStation.Pause
posit := MyStation.Cont.XPos
```

## 添加到仿真模型

点击 Home 功能区选项卡：**Manage Class Library > Basic Objects > MaterialFlow > ParallelStation**。

示例模型：Window 功能区选项卡 > **Start Page > Getting Started > Example Models > Small Examples**，在 *Examples Collection* 对话框中选择类别、主题和示例后点击 **Open Model**。

## 对话框与选项卡

双击 ParallelStation 图标可打开其对话框；可编辑仿真属性与 3D 动画属性（通过 **Edit 3D Properties** 按钮或按空格键）。

主要选项卡要点如下：

### Tab Attributes（属性）
- **X-Dimension**：沿 X 轴的处理位置数量。
- **Y-Dimension**：沿 Y 轴的处理位置数量。
- 容量由二维坐标网格表示，等于 `Y-Dimension × X-Dimension`，最大允许值为一千万（10,000,000）。
- **Start Processing When Full（满时开始加工）**：默认选中，仅当每个位置都有零件时才启动加工。

> 减小维度时，务必确保没有 MU 位于将被删除的位置上；否则维度会受到限制（Plant Simulation 不会自动删除或移动新维度之外的 MU）。例如 MU 位于 (3,4) 时，新 x 坐标不得小于 3，新 y 坐标不得小于 4。

**SimTalk**：`XDim`、`YDim`、`Capacity`、`pe, [X,Y]`、`setDim`

### Start Processing When Full（满时开始加工）
- 选中后，新零件只能在当前批次加工完成且全部离开后才可进入。
- 若有另一类型零件想进入，即使未满也会先加工已有零件；只有加工完并清空后，其他类型零件才能进入。
- 若无需设置，不同类型零件也可进入；满载后可能以不同加工时间开始加工（适用于类型相关、位置相关的加工时间以及公式形式的加工时间）。
- 可用方法 `startProcessing` 在未满时强制开始加工。
- 可与 **Recovery Time Starts > When processing is done** 搭配；若设为 *When part exits*，恢复时间从最后一个零件离开时开始。
- 取消勾选后，零件进入后立即加工，新零件可随时进入。

> 只有选中 **Start Processing When Full** 时，才能停用 **Automatic Processing**。
> 对于基于加工时间的故障，当并行加工的零件数增加时，模拟 MTBF 会降低、可用性变小；但选中 **Start Processing When Full** 时此现象不适用。

**SimTalk**：`StartProcessingWhenFull`、`startProcessing`

### Tab Failures（故障）
按 *Tab Failures* 定义故障。基于加工时间的故障同样存在"并行加工越多 MTBF 越低"的注意点，且选中 **Start Processing When Full** 时不适用。

### Tab Times（时间）
- 从下拉列表选择分布并输入所需值；参数显示在选项卡上边框。也可选择常量时间 `Const`。
- 可用方法 `setTypeAndAttr` 设置分布类型与完整参数集。

### Tab Set-Up（设置）
按 *Tab Set-Up* 定义设置属性。

> ParallelStation **不提供** **After n parts** 设置。

### Tab Controls（控制）
提供用于修改对象内置行为的控制。可：
- 通过省略号按钮选择现有 Method 路径（或从 Frame 拖入 Method）。
- 在文本框中按 `F2` 打开 Method 编写控制源码。
- 输入名称后选择上下文菜单 **Create Control** 创建对象自身方法（如 `self.A1Ctrl`）；对空文本框选择 **Create Control** 会插入 `self.OnEntrance` 等。

后续编辑源码：按 `F2`、`Shift` + 双击文本框、上下文菜单 **Open Object**，或在 **User-defined** 选项卡中双击方法名。

> 删除控制时应删除用户定义属性；仅从文本框删除名称不会删除用户定义属性。

### Tab Exit（出口）
选择将 MU 移动到哪个后继。除 **MU Attribute** 外，所有阻塞型出口策略在 MU 无法移动时不会确定后继，而是将额外 MU 加入 Exit Blocking List；第一个被阻塞的 MU 移动后，列表中的所有 MU 会获得 Out 事件继续移动。

### Tab Statistics（统计）
按 *Tab Statistics* 描述。查看固定资源的 Resource Statistics：选择 **View > Show Statistics Report**、在 Frame 中右键选择 **Show Statistics Report**，或按 `F6`。

### Tab Importer（导入器）
定义加工零件、为特定类型零件设置工位、维修工位的服务。查看 Importer Statistics 的方式同上（对话框 View 菜单、右键、`F6` 或 Home 功能区的 **Show Statistics Report**）。

### Tab Energy（能源）
在 Tab Energy 上选择对象的能源设置。

### Tab Costs（成本）
选择成本设置。加工过程中产生的成本 = 投资成本 + 运营成本之和。

- 投资成本仅在折旧期（Depreciation Period）内产生。
- ParallelStation 将成本平均分配到各处理位置。
- 成本作为应计成本分配到零件。
- 当某个处理位置为空时，成本作为一般成本留在 ParallelStation 上。

### Tab User-defined（用户定义）
按 *Tab User-defined* 定义自定义属性。

相关 SimTalk 方法：`getAttrName`、`getAttrNo`、`getAttrType`、`getAttrValue`、`NumAttr`、`setAttrType`、`setAttrValue`、`createAttr`、`deleteAttr`。

## 菜单

- **Navigate Menu / View Menu / Tools Menu / Help Menu**：分别参见对应菜单描述。
- **View Menu** SimTalk：`updateDialog`。
- **Tabs Menu**：用于显示/隐藏所选物流对象的选项卡（隐藏不用的选项卡可加快对话框打开速度）；点击 OK 并重新打开后生效；显示的选项卡左侧有勾选标记；**Inherit** 命令用于开关选项卡显示/隐藏的继承。

## 方法

ParallelStation 提供：
- 左侧目录中列出的方法；
- 物流对象（Material Flow Objects）的方法；
- 所有对象（All Objects）的方法。

可通过 **Show Attributes and Methods** 窗口查看全部方法、只读属性和属性。

## 另见

- Station [object]
- Define Processing Times of a ParallelStation
- Configure the Processing Stations
- Configure the Stations ProcessingA and ProcessingB
- Configure the Stations Which Handle the Pallet
- YouTube 视频：https://youtu.be/PQhEriOzVzU?si=XuPINjSUuC0pHfur&t=646
