# PSFM 模型解析提示词集

本目录包含一套用于「从 Plant Simulation 模型文件（PSFM）逆向提取仿真模型信息」的 AI 提示词。目标产出三个维度：**模型结构**、**建模思路**、**代码样例**，并额外覆盖**类结构与继承关系**。

## 文件清单

| 文件 | 用途 |
| --- | --- |
| `00-role-setup.md` | 全局角色设定，会话开头贴一次 |
| `01-model-structure.md` | 提取模型结构（Frame 层级 / 对象清单 / 物料流拓扑 / 控制与数据流） |
| `02-class-hierarchy.md` | 提取类结构与继承关系（父类/子类/实例化/类关系） |
| `03-modeling-approach.md` | 提取建模思路（定位 / 范式 / 控制逻辑 / 亮点） |
| `04-code-samples.md` | 提取 SimTalk 代码样例（源码 + 注释解读 + 依赖） |
| `05-master-report.md` | 一体化综合产出，每模型生成一份完整解析报告 |

## 使用顺序

1. 每次会话开头，先贴 `00-role-setup.md` 建立角色与知识库上下文。
2. 按需使用 01–04，各自独立运行。
3. 需要完整文档时，用 `05-master-report.md` 一次产出。

## 前置条件（重要）

- **先区分两种模型存储格式**：
  - **`.psfm` 文件夹模型（Folder Model）**：本质是一个目录，内部已是文本文件（根部的 `$.spp` 主文件、每 Frame 一个 `$.yaml`、PythonModule 的 `.py`、`.UserSettings.yaml` 等）。**无需转换**，直接读取/粘贴这些文本文件即可。
  - **`.spp` 单文件模型**：可能是二进制格式，直接粘贴会变乱码；需先在 Plant Simulation 中用 **File → Save As** 存为文本格式（或另存为 `.psfm` 文件夹模型），否则提示词只能拿到乱码。
- **每次只贴一个模型**的内容，不要多个模型混在一起，避免对象归属混乱。
- 若是 `.psfm` 文件夹模型，建议优先贴根部的 `$.spp` 与各 Frame 的 `$.yaml`（它们包含对象定义与 SimTalk 源码）。
- 提示词中引用的知识库路径（供 AI 判定对象类型）为：

```text
/root/knowledge_of_plant_simulation/01-plant-simulation-help/
```

## 知识库对象分类速查

- `objects/material-flow-objects/`：Source, Station, ParallelStation, AssemblyStation, DismantleStation, Buffer, PlaceBuffer, Store, Sorter, Converter, Drain, Conveyor, Track, TwoLaneTrack, Turntable, AngularConverter, PickAndPlace Robot, Interface, Frame, Connector, EventController, FlowControl, Cycle
- `objects/resource-objects/`：Worker, WorkerPool, Broker, Exporter, FootPath, LockoutZone, Marker, ShiftCalendar, Workplace, AGVPool
- `objects/information-flow-objects/`：Method, Variable, DataTable, DataList, DataQueue, DataStack, TimeSequence, Generator, Trigger, FileInterface, FileLink, XMLInterface, ODBC, SQLite, AttributeExplorer, PythonModule
- `objects/fluid-objects/`：Mixer, FluidDrain, MaterialsTable 等
- `objects/user-interface-objects/`：用户界面对象
- `simtalk/`：SimTalk 语言参考（语法、预定义函数、控制流）
