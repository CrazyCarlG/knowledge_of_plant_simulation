# 02-offcial-psfm-model

Siemens Tecnomatix Plant Simulation 的**官方示例模型**（Factory 51、Small Parts Production）及其逆向分析文档。模型以 PSFM 文本格式保存，配套的 `model-knwo-how/` 目录是对各模型结构、逻辑与代码的逐层解读。

**English:** The **official example models** (Factory 51, Small Parts Production) of Siemens Tecnomatix Plant Simulation, plus reverse-engineering notes. Each model is stored in PSFM text format; the accompanying `model-knwo-how/` directory explains its structure, logic, and code layer by layer.

> 模型版权归 Siemens 所有，本目录仅用于学习与知识管理。
> **English:** The models are © Siemens; this directory is for learning and knowledge management only.

## 目录结构 / Directory Structure

```
02-offcial-psfm-model/
├── Factory51/
│   ├── Factory51.psfm/          # 官方示例模型（PSFM 文本格式，约 1592 个对象）
│   │   ├── $ModelInfo.yaml      # 模型版本与设置（Plant Simulation 26.6.2.3599）
│   │   ├── Models/              # 根 Frame 与 P1/P2/Warehouse 各实例对象
│   │   ├── UserObjects/         # 自定义类库（Production、Milling、AGV、Box 等）
│   │   ├── ApplicationObjects/  # 外部应用库（CranesAndMore、HBW3D）
│   │   └── MaterialFlow/ Resources/ InformationFlow/ MUs/ UserInterface/
│   │                            # 标准基础类（Built-in 对象的父类模板）
│   └── model-knwo-how/          # 逆向分析文档（Markdown）
│       ├── Factory51-建模思路.md         # 模型定位、建模范式与控制逻辑梳理
│       ├── Factory51-模型结构.md         # Frame 层级、对象清单与物料流拓扑
│       ├── Factory51-类结构与继承关系.md  # 类继承树与实例化映射
│       └── Factory51-代码样例.md         # SimTalk 代码清单与逐段注释
│
└── Small-Parts-Production/
    ├── Small Parts Production.psfm/  # 官方示例模型（PSFM 文本格式，约 1683 个对象）
    │   ├── $ModelInfo.yaml           # 模型版本与设置（Plant Simulation 26.6.2.3599）
    │   ├── Models/                   # Assembly1/Assembly2 两条装配线实例
    │   ├── UserObjects/              # 自定义类库（Classes: AS/MS/Robot/CrossTransfer/Worker；Modules: Assembly_initialState/PreProduction）
    │   ├── Tools/                    # 工具箱（BottleneckAnalyzer/EnergyAnalyzer/WorkerChart/TransferStation/ExperimentManager）
    │   └── MaterialFlow/ Resources/ InformationFlow/ MUs/ UserInterface/
    │                                 # 标准基础类（Built-in 对象的父类模板）
    └── model-knwo-how/               # 逆向分析文档（Markdown）
        └── Small-Parts-Production-类结构与继承关系.md  # 类继承树与实例化映射
```

## 模型概述 / Model Overview

### Factory 51

**Factory 51** 是一个**离散事件制造 + 仓储物流的一体化演示模型**：原材料由卡车送达 → 高架立体仓库（HBW）暂存 → 配送至两条平行生产线（P1/P2）完成机加工、抛光、喷漆、烘干、后处理、质检 → 成品入库（WMS + RackLane）→ 出货。

核心要点：

- **产品**：两类零件（Aubergine 紫 / Strawberry 粉），各 60 件，共 120 件。
- **生产线**：`Production` 一个类定义两条线 P1、P2（同构复用），内部再派生 Polishing/PostProcess/Painting/Drying 等工序单元。
- **仓储**：复用 `CranesAndMore`（堆垛机/存储区）与 `HBW3D`（高架立体仓库 WMS/巷道）外部库。
- **物流**：叉车/AGV 沿标记点路径搬运；入库为推式、出库为拉式（`StoreExit.Init` 按需拉料）。
- **控制**：`EntranceCtrl`/`ExitCtrl` 挂载自定义 Method；`Production/Line.OnExit` 按下游抛光站空满动态分流。
- **可视化**：实时仿真（`Realtime=true`）、3D 加工动画、`CostAnalyzer` 成本分析与 `SankeyDiagram` 桑基图。

### Small Parts Production

**Small Parts Production** 是一个**小零件装配 + 预生产供料的双产线演示模型**：预生产单元（PreProduction）完成部件预加工与供给 → 两条装配线（Assembly1/Assembly2）并行完成装配 → 下线出货，并内置能耗、瓶颈与工人利用率分析。

核心要点：

- **产品**：多种小零件/装配件，含 `Entity`、`Cap`、`EXA1A/1B/2A/2B`（示例变体）等 MU。
- **生产线**：`Assembly_initialState` 一个 Frame 类定义两条装配线 Assembly1、Assembly2（同构复用），内部挂载 AS1..AS5 装配站、MS1..MS5 加工站、F0..F11 传送带、横移机构（CrossTransfer）与上下料（Source/Unload/Buffer/Drain）。
- **预生产**：`PreProduction` Frame 类作为子模型嵌入装配线，通过 `Entry`/`Exit` Interface 与父 Frame 对接，负责部件预加工（AS6..AS9、MS、Robot）。
- **自定义类库**：`UserObjects/Classes` 暴露 AS(Station)、MS(Station)、Robot(PickAndPlace)、CrossTransfer(Track) 四个可拖拽类；`Worker`/`Worker_Round`/`Adjuster` 三类工人经 Broker 提供 `assemble/correct/test/repair` 服务。
- **核心逻辑**：`CrossTransfer` 类通过 `$CustomAttributes` 定义 `Init/unloadPart/loadPart` 方法，`Init` 内动态创建 `Transporter` 作为横移小车（CSC），`ExitCtrl`/`BwExitCtrl` 以 `self.*` 回调委托。
- **分析工具**：内置 `BottleneckAnalyzer`（瓶颈）、`EnergyAnalyzer`（能耗）、`WorkerChart`/`WorkerUtilization`（工人利用率）、`PalletOptimization`/`BufferOptimization`（托盘/缓冲优化）与 `ExperimentManager`。

## 分析文档索引 / Analysis Docs

### Factory51

| 文档 | 内容 |
|---|---|
| `Factory51-建模思路.md` | 模型定位、推拉结合范式、对象选型理由、关键参数来源、控制逻辑（进货→入库→生产线→出货）与可复用模式 |
| `Factory51-模型结构.md` | Frame 层级树、1592 个对象的类型分布清单、物料流拓扑、控制与数据流关系 |
| `Factory51-类结构与继承关系.md` | 三层层级类继承树（内置 → 类 → 派生 → 实例）、类/实例映射、继承/引用/委托/属性绑定关系 |
| `Factory51-代码样例.md` | SimTalk 源码清单（Source/TruckArrivals/UnloadTruck/WMS/StoreExit/Production/Milling 等）与逐段注释解读 |

### Small Parts Production

| 文档 | 内容 |
|---|---|
| `Small-Parts-Production-类结构与继承关系.md` | 类继承树（2 个 Frame 类 + 8 个对象类 + 10 个 MU 类）、类/实例映射、继承/引用/委托/属性绑定关系（含 EXA1A→EXA1B/2A/2B 派生链、CrossTransfer 自定义方法） |

## 如何打开模型 / How to Open

模型为 PSFM 文本格式（`ModelFormat: 1`），可在 Siemens Tecnomatix Plant Simulation 中打开：

1. 启动 Plant Simulation（本模型基于 `26.6.2.3599`）。
2. `File → Open` 选择对应模型的 `.psfm` 目录（`Factory51/Factory51.psfm` 或 `Small-Parts-Production/Small Parts Production.psfm`）。
3. 运行仿真即可观察实时 3D 演示与 KPI 统计。

> 注：PSFM 中 `.jt` 文件为 Siemens JT 二进制格式（3D 图形），非明文 SimTalk；明文源码位于同目录对象 `.yaml` 的 `$CustomAttributes` 或 `Program` 字段。
