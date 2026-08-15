# Interface — General（概述）

本目录存放 **Interface**（接口）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。

## 对象用途

**Interface** 用于在 Frame 之间建立过渡，即模型从一部分转移到另一部分，同时支持层级化建模。

Interface 可以是**入口（Entrance）**或**出口（Exit）**，是工件（MU）在仿真模型中从一个 Frame 移动到另一个 Frame 的位置。可以将 Interface 放置在 Frame 中的任意位置，并通过名称来寻址这些连接。

## 核心规则

- 当一个子 Frame 中包含**多个物料流对象**时，必须插入 Interface。若子 Frame 中插入了 Interface，物料总是通过这些 Interface 流动。
- 对于插入到 Frame 中的 Interface，Plant Simulation 会显示它是否通过 Connector 连接到其他对象，并自动识别它是入口还是出口。
- 若子 Frame 中**只有一个**物料流对象，则不必插入 Interface，可将子 Frame 直接与其前驱和后继相连。不使用 Interface 的连接只能跨越**单个**下级层级，不能跨越多个嵌套层级。
- 若模型中插入了 Interface，3D 仿真将跨越这些 Interface 运行。

## 操作 Interface

- 选择上下文菜单中的 **Open External Connections List**，或对话框中的 **Tools > External Connections**，打开显示所有外部连接对象的列表。
- 将鼠标悬停在 Frame 中的 Interface 上，可显示包含外部连接对象的工具提示。
- 选择上下文菜单中的 **Show External Connected Objects**，选择与该 Interface 相连的对象。
- 若已确定下一个选中的出口（例如通过调用后继对象的方法 `succ`），Interface 会在 **Exit** 选项卡上显示其编号。

## 添加到仿真模型

在 Home 功能区标签页点击 **Manage Class Library > Basic Objects > MaterialFlow > Interface**。

## Interface 对话框

双击 Interface 图标即可打开其对话框。

- **Edit Simulation Properties**：修改对象的仿真属性（共享属性见 *Dialog Items of the Objects*）。
- **Edit Animation Properties**：点击左下角的 **Edit 3D Properties**，或选中对象后按空格键。
- 要操作图形，点击 Edit 功能区标签页上的 **Show Manipulators**，或按 `M`。

## 选项卡 Attributes（属性）

### Type（类型）[Interface]

插入 Frame 并用 Connector 连接的 Interface 会显示其类型，可为：

- **入口（Entrance）接口**：工件通过它进入 Frame。
- **出口（Exit）接口**：工件通过它离开 Frame。

### Maximum Number of External Connections（最大外部连接数）[Interface]

输入 Interface 可拥有的最大外部连接数。根据类型不同，任意数量的 Interface 可以有多个前驱或后继。默认值 `-1` 表示外部连接数不受限制。

### Side（侧边）[下拉列表]

选择 Plant Simulation 放置 Interface 的侧边。可选：Frame 的 **Top**（上）、**Right**（右）、**Bottom**（下）、**Left**（左），或 **Angle-dependent**（取决于角度，在确定 Connector 起点/终点时考虑对象之间的角度）。

### Position in %（位置百分比）[Interface]

输入 Plant Simulation 在 Frame 图标上显示到达/离开 Connector 的位置。取值在 `0` 到 `100`% 之间。位置 0 为顶部或左侧，位置 100 为底部或右侧。

当激活 **File > Preferences > General > Connect Objects Automatically** 时，Plant Simulation 会使用此值。自动连接对象仅在 FrameA 的出口与 FrameB 的入口相距不超过三个像素时才有效。

## 选项卡 Exit（出口）[Interface]

在 **Exit** 选项卡上选择对象将工件移动到哪个后继。

注意：

- 若 Plant Simulation 确定某个对象的第 n 个后继（例如 `print MyStation.succ(n)`），且该后继是 Interface，则 Plant Simulation 返回的是该 Interface 根据其 Exit 策略所对应的后继，而不是 Interface 本身。
- 若选择了非阻塞出口策略，Plant Simulation 返回根据出口策略确定的下一个可用后继；当没有后继可接收工件时返回 `VOID`。
- 当 Interface 只有一个后继时，即使选择了非阻塞出口策略，且该后继已被占用或处于故障/暂停状态，Plant Simulation 也会返回该后继。

## 选项卡 User-defined（用户自定义）

在此定义自定义属性（见 *Tab User-defined*）。

## 菜单

- **Navigate 菜单**：命令见 Navigate Menu 说明。
- **View 菜单**：
  - `Refresh`
  - `Show Attributes and Methods`
  - `External Connections`：打开一个表格，显示 Frame 中外部连接的路径。**Connector** 列表示 Frame 出口处的 Connector；**Object** 列表示后继对象的名称。（也可通过上下文菜单 **Open External Connections List** 访问。）
  - `Forward Blocking List`
- **Tools 菜单 / Help 菜单**：命令见相应菜单说明。

## Interface 的方法

Interface 提供所有对象的通用方法（Methods of All Objects）。可通过 **Show Attributes and Methods** 查看（在类库上下菜单中选择，或按 F8 / 点击 Home 标签页上的 **Show Attributes and Methods**）。

语法行示例：

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

## SimTalk 参考

| 主题 | SimTalk |
| --- | --- |
| Unplanned（Frame） | `<Path>.Unplanned:boolean` |
| 类型 | `IsEntry [SimTalk]`、`IsExit [SimTalk]` |
| 最大外部连接数 | `MaxConnections [SimTalk] - Interface` |
| 侧边 | `Side [SimTalk]` |
| 位置 | `Position [SimTalk] - Interface` |
| View 菜单 | `updateDialog [SimTalk]` |

### Unplanned 示例

```simtalk
EngineAssembly.Unplanned := false
```

设为 `false` 即设置为计划工作；当当前时间不在 Frame 所分配的 ShiftCalendar 的任何班次内时，该 Frame 为 unplanned。

## 参见

- States of the Frame
- Unplanned [state, material flow objects]
- Model Transitions Between Frames
- Adapt the 3D Model to the 2D Model
- Connect Objects Automatically [model settings]
- Tab Exit [general description]
- Blocking [exit strategy]
- Strategy [material flow objects]
