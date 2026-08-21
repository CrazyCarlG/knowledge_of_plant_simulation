# Small Parts Production 类结构与继承关系

> 模型来源：`02-offcial-psfm-model/Small-Parts-Production/Small Parts Production.psfm`（Folder Model，PSFM 文本格式）
> 分析依据：`UserObjects/**`、`MUs/**`、`MaterialFlow|Resources|InformationFlow|MUs|UserInterface/**` 中各 `.yaml` 的 `InternalClassType`、`Name`、`Origin`、`UUID` 字段，以及 `Models/**` 中实例对象的 `Origin` 字段。

**判定规则（PSFM 格式）：**
- `Origin` 字段指向的 UUID 即该对象的"父类 / 派生来源"（Derived from）。`Origin` 为空表示该对象直接基于内置（Built-in）标准对象。
- 位于 `UserObjects/`、`MUs/`、`Tools/` 及标准库目录（`MaterialFlow/` 等）下的对象是**类定义（isClass）**；位于 `Models/` 及 Frame 类内部（`UserObjects/Modules/*`）的对象是**实例（isInstance）**。
- `InternalClassType` 表示对象最终的内置对象类型。
- 类定义文件含完整的属性集与 `Name` 字段；实例文件仅含 `Origin` + `Coordinate3D` 等少量覆盖字段，对象名即文件名。

---

## 一、类继承树（父类 → 子类）

> 三层层级：**内置对象（Built-in）→ 自定义类 → 派生类/实例**。本模型自定义类规模较小，继承深度最多两层。

### 1.1 Frame 类继承树

```
Frame（内置 Built-in）
├── Assembly_initialState   (UserObjects/Modules/Assembly_initialState，自定义 Frame 类，isClass)
│    ├── Assembly1          (Models/Assembly1，实例 isInstance，Origin=Assembly_initialState)
│    └── Assembly2          (Models/Assembly2，实例 isInstance，Origin=Assembly_initialState)
└── PreProduction           (UserObjects/Modules/PreProduction，自定义 Frame 类，isClass)
     └── Assembly_initialState/PreProduction   (嵌入实例，Origin=PreProduction)
          ├── Assembly1/PreProduction          (随 Assembly1 继承而来的实例)
          └── Assembly2/PreProduction          (随 Assembly2 继承而来的实例)
```

### 1.2 物料流 / 资源 / 信息流类继承树

```
Station（内置）
├── AS                     (UserObjects/Classes/AS，自定义 Station 类，isClass)
│    └── AS1..AS8          (各 Frame 内实例，Origin=AS)
└── MS                     (UserObjects/Classes/MS，自定义 Station 类，isClass)
     ├── MS1/MS2/MS4/MS5   (Assembly_initialState 内实例)
     └── MS                (PreProduction 类内实例)
          └── MS6          (Assembly_initialState/PreProduction 内实例，Origin=PreProduction.MS，重命名)

AssemblyStation（内置）
└── MS3 / AS9              (标准 AssemblyStation 实例，Origin=标准 AssemblyStation)

PickAndPlace（内置）
└── Robot                  (UserObjects/Classes/Robot，自定义 PickAndPlace 类，isClass)
     └── Robot             (PreProduction 类内实例)

Track（内置）
└── CrossTransfer          (UserObjects/Classes/CrossTransfer，自定义 Track 类，isClass)
     └── CrossTransferFromTest / CrossTransferToTest   (Assembly_initialState 内实例)

ParallelStation（内置）
├── TransferStation        (Tools/TransferStation/TransferStation，工具箱类，isClass)
│    └── LoadStation / TransferStation   (Assembly_initialState 内实例)
└── (ParallelProc 为标准 ParallelStation 实例)

Worker（内置）
├── Worker                 (UserObjects/Classes/Worker，自定义 Worker 类，isClass)
├── Worker_Round           (UserObjects/Classes/Worker_Round，自定义 Worker 类，isClass)
└── Adjuster               (UserObjects/Classes/Adjuster，自定义 Worker 类，isClass)

Conveyor（内置）
└── F0..F11 / Line1 / Line2   (标准 Conveyor 实例，Origin=标准 Conveyor)

Source / Buffer / Drain / DismantleStation / Workplace / WorkerPool / Broker / ShiftCalendar /
EventController / Interface / Variable / DataTable / FileLink / Chart / Display / Button /
Checkbox / Comment / AttributeExplorer
└── 各 Frame 内同名实例（均直接引用标准基础类）
```

### 1.3 MU 类（物料单元）继承树

```
Part（内置）
├── Entity                 (MUs/Entity，自定义 Part 类，0.4×0.4×0.1)
├── Cap                    (MUs/Cap，自定义 Part 类，0.4×0.4×0.1)
└── EXA1A                  (MUs/EXA1A，自定义 Part 类，根类，0.4×0.4×0.1)
     ├── EXA1B             (MUs/EXA1B，派生类，Origin=EXA1A，无覆盖)
     ├── EXA2A             (MUs/EXA2A，派生类，Origin=EXA1A，无覆盖)
     └── EXA2B             (MUs/EXA2B，派生类，Origin=EXA1A，无覆盖)

Container（内置）
├── Container              (MUs/Container，自定义 Container 类，1×0.8×0.144，槽位 2×2)
├── Carrier                (MUs/Carrier，自定义 Container 类，1×0.8×0.144，槽位 1×2)
└── Pallet                 (MUs/Pallet，自定义 Container 类，1×0.8×0.144，槽位 2×3)

Transporter（内置）
└── Transporter            (MUs/Transporter，自定义 Transporter 类，1.5×0.8×0.4，Speed=0.3，槽位 3×2，CSC 横移小车)
```

---

## 二、类与实例（对象）的实例化关系

> 区分两类实例：**自定义类实例**（`Origin` 指向 `UserObjects/Classes`、`UserObjects/Modules`、`Tools/` 中的自定义类）与**标准库对象实例**（`Origin` 指向标准库目录中的基础类文件）。

### 2.1 Frame 类 → 实例映射

| 实例对象名 | 所属Frame | 对应类(Class) | 是否继承自父类 | 实例化位置 |
| --- | --- | --- | --- | --- |
| Assembly1 | (根 Frame) | Assembly_initialState | 否（Assembly_initialState 为根类） | Models/Assembly1 |
| Assembly2 | (根 Frame) | Assembly_initialState | 否 | Models/Assembly2 |
| PreProduction | Assembly_initialState | PreProduction | 否（PreProduction 为根类） | UserObjects/Modules/Assembly_initialState/PreProduction |
| PreProduction | Assembly1 | PreProduction | 是（随 Frame 继承） | Models/Assembly1/PreProduction |
| PreProduction | Assembly2 | PreProduction | 是（随 Frame 继承） | Models/Assembly2/PreProduction |

### 2.2 自定义对象类 → 实例映射

| 实例对象名 | 所属Frame | 对应类(Class) | 是否继承自父类 | 实例化位置 |
| --- | --- | --- | --- | --- |
| AS1..AS5 | Assembly_initialState | AS | 否（AS 为根类） | UserObjects/Modules/Assembly_initialState |
| AS6..AS8 | PreProduction | AS | 否 | UserObjects/Modules/PreProduction |
| MS1、MS2、MS4、MS5 | Assembly_initialState | MS | 否（MS 为根类） | UserObjects/Modules/Assembly_initialState |
| MS | PreProduction | MS | 否 | UserObjects/Modules/PreProduction |
| MS6 | Assembly_initialState/PreProduction | MS（经 PreProduction.MS 派生） | 是（Derived from PreProduction.MS，并重命名） | UserObjects/Modules/Assembly_initialState/PreProduction |
| Robot | PreProduction | Robot | 否（Robot 为根类） | UserObjects/Modules/PreProduction |
| CrossTransferFromTest / CrossTransferToTest | Assembly_initialState | CrossTransfer | 否（CrossTransfer 为根类） | UserObjects/Modules/Assembly_initialState |
| LoadStation、TransferStation | Assembly_initialState | TransferStation（工具箱） | 否 | UserObjects/Modules/Assembly_initialState |

### 2.3 标准库对象实例（直接引用标准基础类）

| 实例对象名 | 所属Frame | 对应基础类文件 | 内置类型 |
| --- | --- | --- | --- |
| MS3 | Assembly_initialState | MaterialFlow/AssemblyStation.yaml | AssemblyStation |
| AS9 | PreProduction | MaterialFlow/AssemblyStation.yaml | AssemblyStation |
| F0..F11、Line1、Line2 | Assembly_initialState | MaterialFlow/Conveyor.yaml | Conveyor |
| F0..F3 | PreProduction | MaterialFlow/Conveyor.yaml | Conveyor |
| ParallelProc | Assembly_initialState | MaterialFlow/ParallelStation.yaml | ParallelStation |
| Unload | Assembly_initialState | MaterialFlow/DismantleStation.yaml | DismantleStation |
| Source、Source_Paletts | Assembly_initialState | MaterialFlow/Source.yaml | Source |
| Source_Paletts、Source_Parts | PreProduction | MaterialFlow/Source.yaml | Source |
| Buffer | Assembly_initialState | MaterialFlow/Buffer.yaml | Buffer |
| Drain | Assembly_initialState | MaterialFlow/Drain.yaml | Drain |
| Entry、Exit | Assembly_initialState/PreProduction | MaterialFlow/Interface.yaml | Interface |
| Workplace_1..5 | Assembly_initialState | Resources/Workplace.yaml | Workplace |
| Workplace | PreProduction | Resources/Workplace.yaml | Workplace |
| WorkerPool | Assembly_initialState | Resources/WorkerPool.yaml | WorkerPool |
| Broker | Assembly_initialState | Resources/Broker.yaml | Broker |
| ShiftCalendar | Assembly_initialState | Resources/ShiftCalendar.yaml | ShiftCalendar |
| Ereignisverwalter | Assembly_initialState | MaterialFlow/EventController.yaml | EventController |
| Orders | Assembly_initialState | InformationFlow/DataTable.yaml | DataTable |
| Quantity | Assembly_initialState / PreProduction | InformationFlow/Variable.yaml | Variable |
| LiesMich、ReadMe1 | Assembly_initialState | InformationFlow/FileLink.yaml | FileLink |
| AttributeExplorer(×3) | Assembly_initialState | InformationFlow/AttributeExplorer.yaml | AttributeExplorer |
| Chart、Histogram | Assembly_initialState | UserInterface/Chart.yaml | Chart |
| DisplayEnergy、DisplayThroughput | Assembly_initialState | UserInterface/Display.yaml | Display |
| Button(×3)、EnergySavingMeasures(Checkbox)、Comment/Comm_*(×N) | 各 Frame | UserInterface 标准库 | 对应类型 |

### 2.4 类内对象（Containment：作为类模板内容的子对象）

> `UserObjects/Modules/Assembly_initialState/*.yaml`、`UserObjects/Modules/PreProduction/*.yaml` 中的文件，是相应 Frame 类**内部包含**的子对象定义。当 Assembly1/Assembly2 实例化 Assembly_initialState 类时，这些子对象被复制到实例中（`Models/Assembly*` 下以同名文件出现）。

| 父类 | 类内包含的子对象（Containment） |
| --- | --- |
| Assembly_initialState | AS1..AS5(Station 类 AS)、MS1/MS2/MS4/MS5(MS)、MS3(AssemblyStation)、CrossTransferFromTest/CrossTransferToTest(CrossTransfer)、LoadStation/TransferStation(TransferStation 工具)、ParallelProc(ParallelStation)、F0..F11/Line1/Line2(Conveyor)、Source/Source_Paletts(Source)、Buffer、Drain、Unload(DismantleStation)、Workplace_1..5、WorkerPool、Broker、ShiftCalendar、Ereignisverwalter(EventController)、Orders(DataTable)、Quantity(Variable)、LiesMich/ReadMe1(FileLink)、AttributeExplorer×3、Chart/Histogram、DisplayEnergy/DisplayThroughput、Button×3、EnergySavingMeasures(Checkbox)、Comment/Comm_F* 若干、子 Frame PreProduction |
| PreProduction | AS6..AS8(AS)、AS9(AssemblyStation)、MS(MS)、Robot(Robot)、F0..F3(Conveyor)、Source_Paletts/Source_Parts(Source)、Workplace、Quantity(Variable)、Comment/Comm_F0..3 |

> 说明：嵌入在 `Assembly_initialState` 内的 `PreProduction` 实例，额外挂载了 `Entry`/`Exit` 两个 Interface（用于与父 Frame 的物料流对接），并把继承自类的 `MS` 重命名为 `MS6`（见 3.3）。

### 2.5 工具箱（Toolbox）工具实例

> `Tools/` 目录保存工具类的定义，`Models/Assembly*` 下保存拖入模型中的工具实例。

| 工具类 | 工具类位置 | 实例位置 |
| --- | --- | --- |
| BottleneckAnalyzer (Frame) | Tools/BottleneckAnalyzer/BottleneckAnalyzer | Models/Assembly1、Assembly2 |
| EnergyAnalyzer (Frame) | Tools/EnergyAnalyzer/EnergyAnalyzer | Models/Assembly1、Assembly2 |
| WorkerChart (Frame) | Tools/WorkerChart/WorkerChart | Models/Assembly1（Assembly2 为 WorkerUtilization） |
| TransferStation (ParallelStation) | Tools/TransferStation/TransferStation | Assembly_initialState（LoadStation、TransferStation） |
| ExperimentManager (Frame) | Tools/ExperimentManager/ExperimentManager | （通过根 Frame 的 ExperimentManager Variable 引用，未在 Models 内实例化） |
| PalletOptimization / BufferOptimization | （未置于 Tools/，仅作为实例内嵌） | Models/Assembly1/PalletOptimization；Models/Assembly2/BufferOptimization、PalletOptimization |

---

## 三、类关系（继承 / 引用 / 委托 / 属性绑定）

### 3.1 继承（Inheritance）

- **EXA1A → EXA1B / EXA2A / EXA2B**：这是本模型 MU 中唯一的自定义继承链。三个派生 Part 类均以 `Origin=a26c7fac`（EXA1A 的 UUID）继承 EXA1A 的三维尺寸（0.4×0.4×0.1）与图形，且无任何覆盖，仅作为"类型标签"区分不同产品变体。
- **Assembly_initialState → Assembly1 / Assembly2**：两条装配线实例以 `Origin=65505aaf`（Assembly_initialState 的 UUID）继承整条装配线的结构，实现"一条线定义、两条线实例化"。Assembly1 与 Assembly2 同构（Assembly2 额外增加了 `Buffer1` 与 `BufferUsage` 图表）。
- **PreProduction → Assembly_initialState/PreProduction**：预生产 Frame 实例以 `Origin=e5b24adf`（PreProduction 的 UUID）继承预生产单元结构，并随 Assembly_initialState 的实例化继续复制到 Assembly1/Assembly2 中。
- **MS 类 → PreProduction.MS → (嵌入)MS6**：嵌入的 PreProduction 实例把继承来的 `MS` 对象重命名为 `MS6`（`MS6.Origin=PreProduction.MS 的 UUID`），构成"类 → 类内对象 → 实例内对象"的三级派生链，其最终类型仍为 MS 类（Station）。

### 3.2 引用 / 挂载（Reference / Containment）

- **Assembly_initialState 类**内部挂载（包含）约 60 个子对象（见 2.4 表），构成完整装配线：加工站（AS1..AS5、MS1..MS5）、预生产子 Frame（PreProduction）、传送网（F0..F11、Line1/Line2）、横移机构（CrossTransferFromTest/ToTest、LoadStation/TransferStation）、上下料（Source、Source_Paletts、Unload、Buffer、Drain）、工人资源（Workplace×5、WorkerPool、Broker）、排班（ShiftCalendar）、统计与可视化（Orders、Chart、Histogram、Display、AttributeExplorer 等）。
- **PreProduction 类**内部挂载 19 个子对象：AS6..AS9、MS、Robot、F0..F3、Source_Paletts/Source_Parts、Workplace、Quantity 及注释。
- **CrossTransfer 类**通过 `$CustomAttributes` 挂载 3 个自定义方法（`Init`、`unloadPart`、`loadPart`），并在 `Init` 中动态创建子对象（横移小车，见 3.4）。

### 3.3 属性继承 / 覆盖（Inherit from / Override）

- **Origin 机制即属性继承来源**：实例对象通过 `Origin` 指向类，继承其全部属性（加工时间 `ProcTime`、`$Services`、`$Failures`、`3D` 图形等），再按需覆盖（如坐标 `Coordinate3D`、`RandomSeed`）。
- **`$BlockedOrigins`**：嵌入的 `Assembly_initialState/PreProduction/$.yaml` 中列出 3 个 `$BlockedOrigins`（被阻断继承的子对象 UUID），与"新增 Entry/Exit、MS 重命名为 MS6"一致——即该实例在继承 PreProduction 类的同时，局部打断了若干子对象的继承以做定制。
- **类级覆盖示例**：`AS` 类覆盖加工时间为 `ProcTime=[Uniform,58,1:02]`；`MS` 类覆盖为 `ProcTime=[Normal,1:00,15,40,1:30]`；`CrossTransfer` 类覆盖 `Length=4`、`ExitCtrl`/`BwExitCtrl`（绑定自定义方法）。
- **MU 派生类无覆盖**：EXA1B/EXA2A/EXA2B 三个派生类仅含 `Origin` 字段，未覆盖任何属性，完全继承 EXA1A。

### 3.4 委托 / 回调

- **控制方法回调（Exit/Backwards-Exit Control）**：`CrossTransfer` 类通过 `ExitCtrl="self.unloadPart"`、`BwExitCtrl="self.loadPart"` 把出口/反向出口控制委托给自身 `$CustomAttributes` 中定义的方法，而非外部 Method 对象。
- **跨类委托（方法内创建其它类实例）**：`CrossTransfer.Init` 方法内调用 `.MUs.Transporter.create(CT, 2)`，动态创建 `Transporter` MU 作为"cross-sliding car（CSC 横移小车）"，并设置 `backwards/stopped` 状态。这是本模型最核心的自定义 SimTalk 逻辑。
- **工人服务委托（Broker/WorkerPool 服务契约）**：三个 Worker 类通过 `$Services` 声明可提供的服务，由 Broker 按需调度到各工位：
  - `Worker`：`assemble`、`correct`
  - `Worker_Round`：`test`、`assemble`、`correct`
  - `Adjuster`：`repair`、`test`、`assemble`、`correct`
- **跨 Frame 物料流连接（Interface + Connector）**：`PreProduction` 实例的 `Entry`/`Exit` Interface 通过 `$Successors`/`$Predecessors` 与 `$Location`（指向父 Frame Assembly_initialState）实现子 Frame 与父 Frame 的物料流对接，未使用 Exporter/Importer 做跨 Frame 方法委托（模型内无 Exporter/Importer 实例）。

---

## 四、类库来源与命名约定

### 4.1 使用的标准类库对象（Basic Objects）

| 大类 | 标准库目录 | 用到的内置对象类型 |
| --- | --- | --- |
| MaterialFlow | `MaterialFlow/` | Source, Station, ParallelStation, AssemblyStation, DismantleStation, Buffer, Drain, Conveyor, Track, PickAndPlace, Interface, Connector, EventController |
| Resource | `Resources/` | Worker, WorkerPool, Broker, Workplace, ShiftCalendar |
| InformationFlow | `InformationFlow/` | Method, Variable, DataTable, FileLink, AttributeExplorer |
| Fluid | — | 未使用 |
| UserInterface | `UserInterface/` | Button, Chart, Checkbox, Comment, Display |
| MU | `MUs/` | Part, Container, Transporter |

### 4.2 工具箱（Toolbox）工具类

| 库名称 | 用途 | 关键类 |
| --- | --- | --- |
| `BottleneckAnalyzer` | 瓶颈分析工具 | BottleneckAnalyzer(Frame) 及 analyzeModel/analyzeFrame/drawBar 等 Method |
| `EnergyAnalyzer` | 能耗分析工具 | EnergyAnalyzer(Frame) 及 detectEnergyobjects/observeEnergyState 等 Method |
| `WorkerChart` / `WorkerUtilization` | 工人利用率图表工具 | WorkerChart(Frame) 及 GetWorkersFromPool/Refresh 等 Method |
| `TransferStation` | 转接站（并行工位）工具 | TransferStation(ParallelStation) |
| `ExperimentManager` | 实验管理器 | ExperimentManager(Frame)（由根 Frame 的 ExperimentManager Variable 引用） |
| `PalletOptimization` / `BufferOptimization` | 托盘优化 / 缓冲优化工具 | 作为工具实例内嵌于 Models/Assembly1、Assembly2 |

### 4.3 自定义类命名约定

- **路径前缀**：自定义对象类统一放在 `UserObjects/Classes/`；自定义 Frame 类统一放在 `UserObjects/Modules/`；自定义 MU 类统一放在 `MUs/`。代码中通过 `.MUs.Transporter` 等路径访问（见 CrossTransfer.Init）。
- **类库入口 Toolbar**：`UserObjects/Classes/Library`（`InternalClassType: Toolbar`，`Label: "Classes"`）通过 `$ToolbarObjects` 暴露 4 个可拖拽对象类：`CrossTransfer`(Track)、`MS`(Station)、`AS`(Station)、`Robot`(PickAndPlace)。而 `Worker`、`Worker_Round`、`Adjuster` 三个 Worker 类未暴露在 Toolbar，仅供 WorkerPool/Broker 内部调度使用。
- **对象类命名**：以工序/功能缩写命名——`AS`（Assembly Station 装配站）、`MS`（Manufacturing Station 加工站）、`Robot`（搬运机器人）、`CrossTransfer`（横移/转接机构）。
- **MU 类命名**：以实体语义命名——`Entity`（基体）、`Cap`（帽盖）、`EXA1A/1B/2A/2B`（示例产品变体，A/B 后缀表示派生变体）、`Container`、`Carrier`、`Pallet`（三类托盘容器，以槽位数区分）、`Transporter`（CSC 横移小车）。
- **Frame 类命名**：以模块语义命名——`Assembly_initialState`（装配线初始状态）、`PreProduction`（预生产）。
- **实例命名**：Frame 实例以数字后缀区分（`Assembly1`/`Assembly2`）；类内子对象以"类名+序号"命名（`AS1..AS9`、`MS1..MS6`、`F0..F11`）。
- **德语命名残留**：部分对象沿用德语名——`Ereignisverwalter`（EventController）、`LiesMich`（ReadMe/FileLink）；`F` 前缀的传送带（F0..F11）即德语 `Förderstrecke`（输送段）。
- **标准库路径**：模型根目录的 `MaterialFlow/`、`Resources/`、`InformationFlow/`、`UserInterface/` 保存标准对象的基础类（作为派生来源，带 `$BasicObject: true` 标记）。

---

## 附注：无法从文件判定的关系

- 标准库目录（`MaterialFlow/` 等）中的 `.yaml` 文件是标准对象的"基础类模板"，其与 Siemens 内置对象（Built-in）的绑定由 `InternalClassType` 字段隐含表达；文件未显式给出内置对象的继承细节，故内置层在继承树中以"内置（Built-in）"概括。
- 本模型自定义对象类（AS/MS/Robot/Worker 等）均为直接基于内置类型的"根类"，除 EXA1A → EXA1B/2A/2B 外，`UserObjects/Classes` 与 `MUs` 内不存在更深的类间派生；Worker/Worker_Round/Adjuster 三者彼此独立，并非继承关系。
- 各派生/实例对象是否 override 了父类具体哪些属性，仅在 `Origin` 与少量覆盖字段（坐标、`RandomSeed`、`ProcTime`、`$CustomAttributes`）中可见，未逐一比对全部属性差异。
- Assembly1 与 Assembly2 同构的结论来自目录文件清单一致（Assembly2 额外含 `Buffer1`、`BufferUsage`），具体实例坐标差异未逐项比对。
- `.jt` 文件为对象的 JT 三维几何图形数据（非 SimTalk 源码），SimTalk 逻辑仅存于 `.yaml` 的 `$CustomAttributes` / `Program` 字段中。
